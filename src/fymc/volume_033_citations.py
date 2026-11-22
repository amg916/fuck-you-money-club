"""Curated 180-citation Insurance Housing & Corporate Rental Arbitrage baseline (15 per chapter across Q1-Q12) mined strictly from verified Insurance Housing & Corporate Rental Arbitrage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 2: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyer',
     'buyout',
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
 3: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 4: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 5: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'audit',
     'automation',
     'avoid',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 6: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 7: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 8: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'api',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 9: {'8000',
     'accommodations',
     'addendum',
     'additional',
     'adjusters',
     'agency',
     'agreement',
     'airbnb',
     'alacrity',
     'ale',
     'apartment',
     'apartments',
     'arbitrage',
     'assistants',
     'automation',
     'avoiding',
     'b2b',
     'background',
     'bad',
     'ban',
     'bans',
     'bedroom',
     'bgrs',
     'bill',
     'booking',
     'break',
     'budget',
     'building',
     'business',
     'buyout',
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
 10: {'8000',
      'accommodations',
      'addendum',
      'additional',
      'adjusters',
      'agency',
      'agent',
      'agreement',
      'ai',
      'airbnb',
      'alacrity',
      'ale',
      'apartment',
      'apartments',
      'arbitrage',
      'assistants',
      'automate',
      'automation',
      'avoiding',
      'b2b',
      'background',
      'bad',
      'ban',
      'bans',
      'bedroom',
      'bgrs',
      'bill',
      'booking',
      'break',
      'budget',
      'building',
      'business',
      'buyout',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'8000',
      'accommodations',
      'addendum',
      'additional',
      'adjusters',
      'agency',
      'agreement',
      'airbnb',
      'alacrity',
      'ale',
      'apartment',
      'apartments',
      'arbitrage',
      'assistants',
      'automation',
      'avoiding',
      'b2b',
      'background',
      'bad',
      'ban',
      'bans',
      'bedroom',
      'bgrs',
      'bill',
      'booking',
      'break',
      'budget',
      'building',
      'business',
      'buyout',
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
 12: {'8000',
      'accommodations',
      'action',
      'addendum',
      'additional',
      'adjusters',
      'agency',
      'agreement',
      'airbnb',
      'alacrity',
      'ale',
      'apartment',
      'apartments',
      'arbitrage',
      'assistants',
      'automation',
      'avoiding',
      'b2b',
      'background',
      'bad',
      'ban',
      'bans',
      'bedroom',
      'bgrs',
      'bill',
      'booking',
      'break',
      'budget',
      'building',
      'business',
      'buyout',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Official Success Formula',
      'channel': 'Official Success Formula',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:25](https://www.youtube.com/watch?v=NSyEBVGX02o&t=805s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you get a good unit that has like a low low lower than market rent, you have '
              'flexibility to like drop your prices. How hard is it to to to make a thousand '
              'bucks a month on Airbnb with a one-bedroom apartment?',
      'timestamp': 805,
      'timestamp_label': '[00:13:25]',
      'timestamp_seconds': 805,
      'tip': 'If you get a good unit that has like a low low lower than market rent, you have '
             'flexibility to like drop your prices. How hard is it to to to make a thousand '
             'bucks a month on Airbnb with a one-bedroom apartment?',
      'title': 'He Makes $600K/Month Without Owning a Single Property | Airbnb Arbitrage '
               'Secrets with Colin Wright (Official Success Formula)',
      'url': 'https://www.youtube.com/watch?v=NSyEBVGX02o&t=805s',
      'video_id': 'NSyEBVGX02o'},
     {'author': 'Milan Sánchez Stiepovic',
      'channel': 'Milan Sánchez Stiepovic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=nPFkgk7QMfA&t=325s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to move on into the like the cons or the bad sides that the dark side "
              "of Airbnb arbitrage. Um in my opinion, the first one it's that the saturation, "
              'especially with social media nowadays, Airbnb arbitrage, by far, is the most '
              'popular and mainstream model.',
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': "'re going to move on into the like the cons or the bad sides that the dark side "
             "of Airbnb arbitrage. Um in my opinion, the first one it's that the saturation, "
             'especially with social media nowadays, Airbnb arbitrage, by far, is the most '
             'popular and mainstream model.',
      'title': 'Whats better? Airbnb Arbitrage vs Airbnb Management (Co-hosting) (Milan '
               'Sánchez Stiepovic)',
      'url': 'https://www.youtube.com/watch?v=nPFkgk7QMfA&t=325s',
      'video_id': 'nPFkgk7QMfA'},
     {'author': 'Sean Rakidzich',
      'channel': 'Sean Rakidzich',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=pjQc-j6P4_0&t=212s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, you can access the midterm rental market as an owner or as a arbitrage '
              "operator. So, let's look at the other half. Let's look at the half that is "
              'transient. If we go all the way to the very end, the Airbnb space, right?',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': 'So, you can access the midterm rental market as an owner or as a arbitrage '
             "operator. So, let's look at the other half. Let's look at the half that is "
             'transient. If we go all the way to the very end, the Airbnb space, right?',
      'title': 'DO NOT Try Mid-Term Rentals Without Watching This Video (Sean Rakidzich)',
      'url': 'https://www.youtube.com/watch?v=pjQc-j6P4_0&t=212s',
      'video_id': 'pjQc-j6P4_0'},
     {'author': 'Richie Matthews',
      'channel': 'Richie Matthews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=fH0oThfTwlg&t=213s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And now that you've found your market, now you've acquired your deal. So now "
              "you're running your properties. It can be the most active business model if you "
              'allow it to be or the most passive.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "And now that you've found your market, now you've acquired your deal. So now "
             "you're running your properties. It can be the most active business model if you "
             'allow it to be or the most passive.',
      'title': 'Apartment Arbitrage: The (True) Time It Takes To Earn (Richie Matthews)',
      'url': 'https://www.youtube.com/watch?v=fH0oThfTwlg&t=213s',
      'video_id': 'fH0oThfTwlg'},
     {'author': 'PBD Living | Furnished Housing',
      'channel': 'PBD Living | Furnished Housing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=DviX_t2s-0E&t=217s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This isn't just good PR, it's good business. Corporate clients now prioritize "
              'vendors with strong ESG commitments, and relocation partners are selecting '
              'housing partners who align with their values. Four, direct booking equals '
              'direct control.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': "This isn't just good PR, it's good business. Corporate clients now prioritize "
             'vendors with strong ESG commitments, and relocation partners are selecting '
             'housing partners who align with their values. Four, direct booking equals direct '
             'control.',
      'title': 'The Corporate Housing Revolution Why Flexibility, and Human Centered Design '
               'Are Winning (PBD Living | Furnished Housing)',
      'url': 'https://www.youtube.com/watch?v=DviX_t2s-0E&t=217s',
      'video_id': 'DviX_t2s-0E'},
     {'author': 'CID Insurance',
      'channel': 'CID Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:57](https://www.youtube.com/watch?v=OEkTTQjwjDw&t=1077s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're ensuring each building properly and to value and then again on the "
              'statement of values we can also include additional property components.',
      'timestamp': 1077,
      'timestamp_label': '[00:17:57]',
      'timestamp_seconds': 1077,
      'tip': "We're ensuring each building properly and to value and then again on the "
             'statement of values we can also include additional property components.',
      'title': "Lessor's Risk Only (LRO) - Landlord Insurance & Commercial Buildings (CID "
               'Insurance)',
      'url': 'https://www.youtube.com/watch?v=OEkTTQjwjDw&t=1077s',
      'video_id': 'OEkTTQjwjDw'},
     {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:14](https://www.youtube.com/watch?v=ZJwE-gL3Y20&t=2174s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um what what does that relationship building look like? Uh and what does your '
              "marketing Yeah, what is your marketing efforts look like when you're trying to "
              'create a relationship with a business to provide you uh, these these clients?',
      'timestamp': 2174,
      'timestamp_label': '[00:36:14]',
      'timestamp_seconds': 2174,
      'tip': 'Um what what does that relationship building look like? Uh and what does your '
             "marketing Yeah, what is your marketing efforts look like when you're trying to "
             'create a relationship with a business to provide you uh, these these clients?',
      'title': 'How to Start a Corporate Housing Company w/ Tim Touchette (Short Term Sage - '
               'Airbnb, Vacation Rental Host)',
      'url': 'https://www.youtube.com/watch?v=ZJwE-gL3Y20&t=2174s',
      'video_id': 'ZJwE-gL3Y20'},
     {'author': 'Dr Chau Ong',
      'channel': 'Dr Chau Ong',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=v4LiJvYw8rc&t=301s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So so that's why it's so important for you to do corporate housing because you "
              'got better clients you got more options you got more market to work.',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': "So so that's why it's so important for you to do corporate housing because you "
             'got better clients you got more options you got more market to work.',
      'title': 'Corporate Housing VS Vacation Rental - Which is Better? All You Need To Know '
               'About Airbnb Arbitrage (Dr Chau Ong)',
      'url': 'https://www.youtube.com/watch?v=v4LiJvYw8rc&t=301s',
      'video_id': 'v4LiJvYw8rc'},
     {'author': 'Jose Luiz Morales',
      'channel': 'Jose Luiz Morales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:26](https://www.youtube.com/watch?v=5tg19JIMU0o&t=2366s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Building value for people like I get DMS all the time it's just like hey I want "
              "to pick your brain I'm not going to talk to someone that's going to pick my "
              'brain.',
      'timestamp': 2366,
      'timestamp_label': '[00:39:26]',
      'timestamp_seconds': 2366,
      'tip': "Building value for people like I get DMS all the time it's just like hey I want "
             "to pick your brain I'm not going to talk to someone that's going to pick my "
             'brain.',
      'title': 'Providing Housing for Insurance Companies | Hosting Insurance Relocation '
               'Claims | Midterm Rentals (Jose Luiz Morales)',
      'url': 'https://www.youtube.com/watch?v=5tg19JIMU0o&t=2366s',
      'video_id': '5tg19JIMU0o'},
     {'author': 'Nate Bunty',
      'channel': 'Nate Bunty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=0Z4NHI1xnKY&t=81s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Upon with a security deposit so that's it lieu of them actually putting the the "
              'additional months rent you know two months rent to get in that sort of thing '
              "you have this Surety service the other thing that I'm seeing is a true "
              'Insurance product.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': "Upon with a security deposit so that's it lieu of them actually putting the the "
             'additional months rent you know two months rent to get in that sort of thing you '
             "have this Surety service the other thing that I'm seeing is a true Insurance "
             'product.',
      'title': 'Security Deposit Alternatives (Nate Bunty)',
      'url': 'https://www.youtube.com/watch?v=0Z4NHI1xnKY&t=81s',
      'video_id': '0Z4NHI1xnKY'},
     {'author': 'Midterm Rental Consulting',
      'channel': 'Midterm Rental Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:28](https://www.youtube.com/watch?v=Y9ZI_NB4b9A&t=448s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Everything I do to market for my current clients because that would not be fair '
              "to the people that pay me But I will give you a tip here Don't But I will give "
              "you a tip here Don't write your listing.",
      'timestamp': 448,
      'timestamp_label': '[00:07:28]',
      'timestamp_seconds': 448,
      'tip': 'Everything I do to market for my current clients because that would not be fair '
             "to the people that pay me But I will give you a tip here Don't But I will give "
             "you a tip here Don't write your listing.",
      'title': 'Why I Never Worry About Finding Tenants (Midterm Rentals 2025) (Midterm Rental '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=Y9ZI_NB4b9A&t=448s',
      'video_id': 'Y9ZI_NB4b9A'},
     {'author': 'TurboTenant',
      'channel': 'TurboTenant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=HBrEcXEe2_I&t=353s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Getting monthly Revenue why would I ever break the lease yeah well there are a '
              'lot of different reasons maybe the property requires extreme repairs and.',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': 'Getting monthly Revenue why would I ever break the lease yeah well there are a '
             'lot of different reasons maybe the property requires extreme repairs and.',
      'title': 'Debunking Lease Breaking Myths: Navigating Early Termination | Be A Better '
               'Landlord (TurboTenant)',
      'url': 'https://www.youtube.com/watch?v=HBrEcXEe2_I&t=353s',
      'video_id': 'HBrEcXEe2_I'},
     {'author': 'Public Adjuster Show with Vince Perri',
      'channel': 'Public Adjuster Show with Vince Perri',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=ZQjrOy75-Ow&t=139s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Location for the homeowner to say amazing service contact black diamond '
              'services today so you can find out more information for yourself.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Location for the homeowner to say amazing service contact black diamond services '
             'today so you can find out more information for yourself.',
      'title': 'The Pros and Cons of Hiring a Public Adjuster - Insurance Claims Training '
               '(Public Adjuster Show with Vince Perri)',
      'url': 'https://www.youtube.com/watch?v=ZQjrOy75-Ow&t=139s',
      'video_id': 'ZQjrOy75-Ow'},
     {'author': 'Rich Somers',
      'channel': 'Rich Somers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:59](https://www.youtube.com/watch?v=g075AOuQIwk&t=2819s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Almost don't have to like record short firm 100% which is pretty cool 100% bro "
              "but there it is he's ring Kanye I'm rich Summers listeners thanks for tuning in "
              "we'll see you in the next one peace.",
      'timestamp': 2819,
      'timestamp_label': '[00:46:59]',
      'timestamp_seconds': 2819,
      'tip': "Almost don't have to like record short firm 100% which is pretty cool 100% bro "
             "but there it is he's ring Kanye I'm rich Summers listeners thanks for tuning in "
             "we'll see you in the next one peace.",
      'title': 'The Mid-term Rental Playbook | Ruben Kanya E185 (Rich Somers)',
      'url': 'https://www.youtube.com/watch?v=g075AOuQIwk&t=2819s',
      'video_id': 'g075AOuQIwk'},
     {'author': 'Passports and Preemies',
      'channel': 'Passports and Preemies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=xzWDO7GD3hk&t=284s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Things it'll also be helpful if you include in your listing like how far you "
              'are from each Hospital maybe how far you are from public transportation what is '
              'the parking situation like you know making sure that we feel prepared to show '
              'up and go to work.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "Things it'll also be helpful if you include in your listing like how far you are "
             'from each Hospital maybe how far you are from public transportation what is the '
             'parking situation like you know making sure that we feel prepared to show up and '
             'go to work.',
      'title': 'How to Successfully Rent Your Property to Travel Nurses (Passports and '
               'Preemies)',
      'url': 'https://www.youtube.com/watch?v=xzWDO7GD3hk&t=284s',
      'video_id': 'xzWDO7GD3hk'}],
 2: [{'author': 'Sean Rakidzich',
      'channel': 'Sean Rakidzich',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=lGwvDjwR4uU&t=264s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Month booking I think goes like 27 days and my collectors like 4400 are just '
              "under 4,400 on Airbnb so I'm more than doubled my money for a month on booking "
              "so people are glad to pay this money so don't worry about that also in this "
              "building there's a company.",
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': 'Month booking I think goes like 27 days and my collectors like 4400 are just '
             "under 4,400 on Airbnb so I'm more than doubled my money for a month on booking "
             "so people are glad to pay this money so don't worry about that also in this "
             "building there's a company.",
      'title': 'How Rental Arbitrage Works | Margin on Rentals Explained | Short Term  Lease '
               'Tips (Sean Rakidzich)',
      'url': 'https://www.youtube.com/watch?v=lGwvDjwR4uU&t=264s',
      'video_id': 'lGwvDjwR4uU'},
     {'author': 'readingDlaw',
      'channel': 'readingDlaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=9mr0xXwbasA&t=343s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Seven, talk to legal aid or a victim advocate before you sign any lease break '
              'agreement or pay a fee. Three myths to leave behind. Myth one, if you flee '
              'abuse, you automatically owe every month left on the lease.',
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': 'Seven, talk to legal aid or a victim advocate before you sign any lease break '
             'agreement or pay a fee. Three myths to leave behind. Myth one, if you flee '
             'abuse, you automatically owe every month left on the lease.',
      'title': 'Domestic violence and breaking your lease early: WA, OR, IL and HUD survivor '
               'rules (US) (readingDlaw)',
      'url': 'https://www.youtube.com/watch?v=9mr0xXwbasA&t=343s',
      'video_id': '9mr0xXwbasA'},
     {'author': 'Jorge Contreras | Airbnb Arbitrage',
      'channel': 'Jorge Contreras | Airbnb Arbitrage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=d8qhoiAWdLs&t=115s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every single month and they never have to worry about getting a late fee or the '
              'payment changing and then of course in the lease agreement we are going to have '
              "the terms right how much I'm paying.",
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'Every single month and they never have to worry about getting a late fee or the '
             'payment changing and then of course in the lease agreement we are going to have '
             "the terms right how much I'm paying.",
      'title': "The Negotiation Script I Use When Subleasing Airbnb's | Jorge Contreras (Jorge "
               'Contreras | Airbnb Arbitrage)',
      'url': 'https://www.youtube.com/watch?v=d8qhoiAWdLs&t=115s',
      'video_id': 'd8qhoiAWdLs'},
     {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
      'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:25](https://www.youtube.com/watch?v=XTn3a_-I1Rg&t=505s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You get to do what you want to do, and we are all here to operate businesses. '
              'Your pricing is going to be different because you do not have to compensate for '
              "that booking fee that's going to be taken out. With Airbnb's new fee structure, "
              'Airbnb is adding 15.',
      'timestamp': 505,
      'timestamp_label': '[00:08:25]',
      'timestamp_seconds': 505,
      'tip': 'You get to do what you want to do, and we are all here to operate businesses. '
             'Your pricing is going to be different because you do not have to compensate for '
             "that booking fee that's going to be taken out. With Airbnb's new fee structure, "
             'Airbnb is adding 15.',
      'title': 'How to Land Travel Nurse Tenants Right Now | Full Breakdown (Landlord Diaries '
               '- The Monthly Rentals Podcast)',
      'url': 'https://www.youtube.com/watch?v=XTn3a_-I1Rg&t=505s',
      'video_id': 'XTn3a_-I1Rg'},
     {'author': 'AmericanModernIns',
      'channel': 'AmericanModernIns',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=fR49bewBEuo&t=30s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just add our endorsement to cover Airbnb-type properties. Not many other '
              'carriers offer this. The third rental opportunity is for more established real '
              'estate investors. You can bundle up to 30 homes onto one policy, with one bill '
              'to pay, and one renewal date.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Just add our endorsement to cover Airbnb-type properties. Not many other '
             'carriers offer this. The third rental opportunity is for more established real '
             'estate investors. You can bundle up to 30 homes onto one policy, with one bill '
             'to pay, and one renewal date.',
      'title': 'Flexible insurance coverage for all types of rental property '
               '(AmericanModernIns)',
      'url': 'https://www.youtube.com/watch?v=fR49bewBEuo&t=30s',
      'video_id': 'fR49bewBEuo'},
     {'author': 'Ontario Renter Rights',
      'channel': 'Ontario Renter Rights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=N08BrJ9_Luw&t=217s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Void clause number 2, pay everything now. Section 15, an acceleration clause is '
              'void. That is a clause saying that if you default, miss a payment, break a '
              'rule, all the remaining rent for the whole term becomes due at once.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'Void clause number 2, pay everything now. Section 15, an acceleration clause is '
             'void. That is a clause saying that if you default, miss a payment, break a rule, '
             'all the remaining rent for the whole term becomes due at once.',
      'title': "Your Lease Expired — You Don't Have to Leave (and Other Void Lease Clauses) "
               '(Ontario Renter Rights)',
      'url': 'https://www.youtube.com/watch?v=N08BrJ9_Luw&t=217s',
      'video_id': 'N08BrJ9_Luw'},
     {'author': 'DoorLoop',
      'channel': 'DoorLoop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=DMY8aqSWFmQ&t=233s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The third tip is to add a buyout option while you're at it. Buyout in this case "
              'refer to the ability of the tenant to pay a portion of the remainder of their '
              'lease early to terminate their lease. Typically, this fee is around two months '
              'rent.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': "The third tip is to add a buyout option while you're at it. Buyout in this case "
             'refer to the ability of the tenant to pay a portion of the remainder of their '
             'lease early to terminate their lease. Typically, this fee is around two months '
             'rent.',
      'title': 'Early Termination of Lease Agreements for Landlords (DoorLoop)',
      'url': 'https://www.youtube.com/watch?v=DMY8aqSWFmQ&t=233s',
      'video_id': 'DMY8aqSWFmQ'},
     {'author': 'Tenant Law Group, PC',
      'channel': 'Tenant Law Group, PC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=mXtFESh8Jwc&t=76s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your lease is an early termination fee this is a set amount you'd pay to end "
              'your tency early typically ranging from 1 to 3 months rent while it might seem.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "Your lease is an early termination fee this is a set amount you'd pay to end "
             'your tency early typically ranging from 1 to 3 months rent while it might seem.',
      'title': 'What Happens If You Break Your Lease Early? (Tenant Law Group, PC)',
      'url': 'https://www.youtube.com/watch?v=mXtFESh8Jwc&t=76s',
      'video_id': 'mXtFESh8Jwc'},
     {'author': 'RPOAM Real Estate Investor Podcast',
      'channel': 'RPOAM Real Estate Investor Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:45](https://www.youtube.com/watch?v=f2vS4cnBnoI&t=1185s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Terms of okay then what are my fees going to be so we originally did it on the '
              'on that 30 we had the franchise fee based off that 30 and it was it was just.',
      'timestamp': 1185,
      'timestamp_label': '[00:19:45]',
      'timestamp_seconds': 1185,
      'tip': 'Terms of okay then what are my fees going to be so we originally did it on the '
             'on that 30 we had the franchise fee based off that 30 and it was it was just.',
      'title': 'Increasing Your Rental Income 3 to 4 Times by Providing Corporate Housing with '
               'Angela Healy (RPOAM Real Estate Investor Podcast)',
      'url': 'https://www.youtube.com/watch?v=f2vS4cnBnoI&t=1185s',
      'video_id': 'f2vS4cnBnoI'},
     {'author': 'Midterm Rental Consulting',
      'channel': 'Midterm Rental Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:39](https://www.youtube.com/watch?v=PLf1d4djjZw&t=399s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it's not just showing up in home searches, but it's becoming a massive part "
              'of the buyer decision tree. And I feel and have felt that it is the same for '
              'rentals.',
      'timestamp': 399,
      'timestamp_label': '[00:06:39]',
      'timestamp_seconds': 399,
      'tip': "So, it's not just showing up in home searches, but it's becoming a massive part "
             'of the buyer decision tree. And I feel and have felt that it is the same for '
             'rentals.',
      'title': 'Watch this Before Renting on Furnished Finder (Midterm Rental Consulting)',
      'url': 'https://www.youtube.com/watch?v=PLf1d4djjZw&t=399s',
      'video_id': 'PLf1d4djjZw'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:23](https://www.youtube.com/watch?v=a7yG_MgRly4&t=263s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're going to pay a premium to have somebody of her stature and her space to "
              'be able to do that. So, as we build this, this is what I want you guys to know. '
              'And with Airbnb coming into the space, like I knew this was going to happen.',
      'timestamp': 263,
      'timestamp_label': '[00:04:23]',
      'timestamp_seconds': 263,
      'tip': "They're going to pay a premium to have somebody of her stature and her space to "
             'be able to do that. So, as we build this, this is what I want you guys to know. '
             'And with Airbnb coming into the space, like I knew this was going to happen.',
      'title': 'The Mid-Term Rental Strategy That Made $1,000,000 (Most Hosts Are Doing the '
               'Opposite) (Jesse Vasquez)',
      'url': 'https://www.youtube.com/watch?v=a7yG_MgRly4&t=263s',
      'video_id': 'a7yG_MgRly4'},
     {'author': 'The Listing Real Estate Management',
      'channel': 'The Listing Real Estate Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=WU7IqO6I6fk&t=189s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Tenants signed a legally binding contract so there's no room for negotiation I "
              'hope this information helps and feel free to contact us here at the listing '
              'Real Estate Management if you have any questions thank you foreign.',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': "Tenants signed a legally binding contract so there's no room for negotiation I "
             'hope this information helps and feel free to contact us here at the listing Real '
             'Estate Management if you have any questions thank you foreign.',
      'title': 'What to do if my Tenant Breaks the Lease Agreement? (The Listing Real Estate '
               'Management)',
      'url': 'https://www.youtube.com/watch?v=WU7IqO6I6fk&t=189s',
      'video_id': 'WU7IqO6I6fk'},
     {'author': 'Renter Lifestyle',
      'channel': 'Renter Lifestyle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=EyV5J0CkYDA&t=333s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are able to find them a replacement closing thoughts breaking a lease is never '
              'an easy decision but if you are in a situation where you must do so I hope that '
              'this video has been helpful in informing you of your options.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': 'Are able to find them a replacement closing thoughts breaking a lease is never '
             'an easy decision but if you are in a situation where you must do so I hope that '
             'this video has been helpful in informing you of your options.',
      'title': 'How to Break Your Lease Without Penalty [10 Effective Strategies] (Renter '
               'Lifestyle)',
      'url': 'https://www.youtube.com/watch?v=EyV5J0CkYDA&t=333s',
      'video_id': 'EyV5J0CkYDA'},
     {'author': 'LaShaun Shanae',
      'channel': 'LaShaun Shanae',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:34](https://www.youtube.com/watch?v=nZd4KYLOZDw&t=934s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Roles though a lot of times we already know the employer and so we're know "
              "they're they're pretty good to go and there's not a time where they don't pay.",
      'timestamp': 934,
      'timestamp_label': '[00:15:34]',
      'timestamp_seconds': 934,
      'tip': "Roles though a lot of times we already know the employer and so we're know "
             "they're they're pretty good to go and there's not a time where they don't pay.",
      'title': 'How to Get Started Investing in Corporate Rentals. (LaShaun Shanae)',
      'url': 'https://www.youtube.com/watch?v=nZd4KYLOZDw&t=934s',
      'video_id': 'nZd4KYLOZDw'},
     {'author': "She's Got Assets",
      'channel': "She's Got Assets",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:53:04](https://www.youtube.com/watch?v=pWVHjrvUQkc&t=3184s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thank you so much for joining uh reach out if you are interested in the course '
              "and we'll chat more thanks so much have a great evening.",
      'timestamp': 3184,
      'timestamp_label': '[00:53:04]',
      'timestamp_seconds': 3184,
      'tip': 'Thank you so much for joining uh reach out if you are interested in the course '
             "and we'll chat more thanks so much have a great evening.",
      'title': "How to Get Your Mid-Term Rental Booked with Insurance Contracts (She's Got "
               'Assets)',
      'url': 'https://www.youtube.com/watch?v=pWVHjrvUQkc&t=3184s',
      'video_id': 'pWVHjrvUQkc'}],
 3: [{'author': 'Aurelio Licata',
      'channel': 'Aurelio Licata',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:52](https://www.youtube.com/watch?v=Q3hSpjquUTE&t=1012s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re not going to incur interest. So you just make the minimum payment on these "
              'business credit cards every single month with the profit of the Airbnb property '
              'and then come 12 months from now or from then you have multiple Airbnbs cash '
              'flow and you pay the card off in full.',
      'timestamp': 1012,
      'timestamp_label': '[00:16:52]',
      'timestamp_seconds': 1012,
      'tip': "'re not going to incur interest. So you just make the minimum payment on these "
             'business credit cards every single month with the profit of the Airbnb property '
             'and then come 12 months from now or from then you have multiple Airbnbs cash '
             'flow and you pay the card off in full.',
      'title': 'I pitched 500 landlords Airbnb and learned this (Aurelio Licata)',
      'url': 'https://www.youtube.com/watch?v=Q3hSpjquUTE&t=1012s',
      'video_id': 'Q3hSpjquUTE'},
     {'author': 'House Math',
      'channel': 'House Math',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:10](https://www.youtube.com/watch?v=8fGpZhTvLQo&t=310s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now his gain is close to 200,000. Plus that 65,000 of depreciation and the home '
              'sale break is gone. Depending on his income, the federal tax bill could easily '
              'reach $40,000 or more. The same sale that was tax-free could now cost him a big '
              'chunk of his profit.',
      'timestamp': 310,
      'timestamp_label': '[00:05:10]',
      'timestamp_seconds': 310,
      'tip': 'Now his gain is close to 200,000. Plus that 65,000 of depreciation and the home '
             'sale break is gone. Depending on his income, the federal tax bill could easily '
             'reach $40,000 or more. The same sale that was tax-free could now cost him a big '
             'chunk of his profit.',
      'title': 'Should You Rent Out Your House or Sell It? (House Math)',
      'url': 'https://www.youtube.com/watch?v=8fGpZhTvLQo&t=310s',
      'video_id': '8fGpZhTvLQo'},
     {'author': 'Humza Zafar',
      'channel': 'Humza Zafar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:08](https://www.youtube.com/watch?v=1D3J3ID1ZZM&t=1028s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You actually have a higher uh revenue per unit. Your economics look a lot '
              'better. You have hire less VAS, hire less employees, you have a less software '
              "cost. So that's actually my goal is that I don't want to be at 300 units.",
      'timestamp': 1028,
      'timestamp_label': '[00:17:08]',
      'timestamp_seconds': 1028,
      'tip': 'You actually have a higher uh revenue per unit. Your economics look a lot '
             'better. You have hire less VAS, hire less employees, you have a less software '
             "cost. So that's actually my goal is that I don't want to be at 300 units.",
      'title': 'Humza Zafar on Scaling to $1M/mo with Airbnb Arbitrage & Why Most Hosts Fail | '
               'BNB Inside (Humza Zafar)',
      'url': 'https://www.youtube.com/watch?v=1D3J3ID1ZZM&t=1028s',
      'video_id': '1D3J3ID1ZZM'},
     {'author': 'Allen Duan | Midterm Rental + Co-Hosting Expert',
      'channel': 'Allen Duan | Midterm Rental + Co-Hosting Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:52](https://www.youtube.com/watch?v=aDxy2Ei3pfQ&t=652s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Sometimes it's not worth it because you get a really bad guest and it's just "
              'not worth the trouble at that point. You end up losing money because of that '
              'booking. So, you have to think about that as well when you do pricing.',
      'timestamp': 652,
      'timestamp_label': '[00:10:52]',
      'timestamp_seconds': 652,
      'tip': "Sometimes it's not worth it because you get a really bad guest and it's just not "
             'worth the trouble at that point. You end up losing money because of that '
             'booking. So, you have to think about that as well when you do pricing.',
      'title': 'Rental Arbitrage or Co-Hosting? My 8-Year Journey Reveals Which Is Best For '
               'You (Allen Duan | Midterm Rental + Co-Hosting Expert)',
      'url': 'https://www.youtube.com/watch?v=aDxy2Ei3pfQ&t=652s',
      'video_id': 'aDxy2Ei3pfQ'},
     {'author': 'Real Life Planning with Cynthia Meyer',
      'channel': 'Real Life Planning with Cynthia Meyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:09](https://www.youtube.com/watch?v=icpm0fFsk6Y&t=489s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, that means before you launch, you should have a solid cash reserve to cover '
              '3 months of expenses in the property, build that into your budget and your '
              'offer price so that you have some cash retained for the possibility of not '
              'being full all the time.',
      'timestamp': 489,
      'timestamp_label': '[00:08:09]',
      'timestamp_seconds': 489,
      'tip': 'So, that means before you launch, you should have a solid cash reserve to cover '
             '3 months of expenses in the property, build that into your budget and your offer '
             'price so that you have some cash retained for the possibility of not being full '
             'all the time.',
      'title': 'What to Know Before Starting a Mid-Term Rental (Real Life Planning with '
               'Cynthia Meyer)',
      'url': 'https://www.youtube.com/watch?v=icpm0fFsk6Y&t=489s',
      'video_id': 'icpm0fFsk6Y'},
     {'author': 'Nurse Lexi',
      'channel': 'Nurse Lexi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=v2OZyLu0O58&t=203s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first month um the cost of the unit was pretty much the same that i was '
              'going to pay for an airbnb.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'The first month um the cost of the unit was pretty much the same that i was '
             'going to pay for an airbnb.',
      'title': 'Corporate Housing for Travel Nurses (Nurse Lexi)',
      'url': 'https://www.youtube.com/watch?v=v2OZyLu0O58&t=203s',
      'video_id': 'v2OZyLu0O58'},
     {'author': 'The Furnished Rental Strategist',
      'channel': 'The Furnished Rental Strategist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:01](https://www.youtube.com/watch?v=iMXOGF4Engc&t=601s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step three, all-inclusive pricing. Tenants expect utilities, internet, and '
              'furnishings included. Build those costs into your rent. Step four, market on '
              'the right platform. Furnish finders is huge for traveling nurses. Airbnb works '
              'great if you set a 30-day minimum.',
      'timestamp': 601,
      'timestamp_label': '[00:10:01]',
      'timestamp_seconds': 601,
      'tip': 'Step three, all-inclusive pricing. Tenants expect utilities, internet, and '
             'furnishings included. Build those costs into your rent. Step four, market on the '
             'right platform. Furnish finders is huge for traveling nurses. Airbnb works great '
             'if you set a 30-day minimum.',
      'title': 'Furnished\xa0Rental\xa0Properties\xa02025- Mid Term Rental\xa0Strategy for '
               'Passive Income (The Furnished Rental Strategist)',
      'url': 'https://www.youtube.com/watch?v=iMXOGF4Engc&t=601s',
      'video_id': 'iMXOGF4Engc'},
     {'author': 'Airbnb Hosting and Short Term Rental Tips',
      'channel': 'Airbnb Hosting and Short Term Rental Tips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=264jEA_cXOw&t=15s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In today's video we're going to break it all down from pricing to Leasing and "
              "literally everything in between we'll tell you what you need to know what most.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "In today's video we're going to break it all down from pricing to Leasing and "
             "literally everything in between we'll tell you what you need to know what most.",
      'title': 'The Beginners Guide to Airbnb Mid-Term Rentals (Airbnb Hosting and Short Term '
               'Rental Tips)',
      'url': 'https://www.youtube.com/watch?v=264jEA_cXOw&t=15s',
      'video_id': '264jEA_cXOw'},
     {'author': 'The Phoenix Insurance',
      'channel': 'The Phoenix Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:48](https://www.youtube.com/watch?v=S15pjuTJ618&t=288s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of coverage what do I mean by better invest it means do we have replacement '
              'cost which would be better than actual cash value okay it means having '
              'coverage.',
      'timestamp': 288,
      'timestamp_label': '[00:04:48]',
      'timestamp_seconds': 288,
      'tip': 'Of coverage what do I mean by better invest it means do we have replacement cost '
             'which would be better than actual cash value okay it means having coverage.',
      'title': 'Rental Property Insurance - Watch this Video If YOU Own Rental Properties! '
               '(The Phoenix Insurance)',
      'url': 'https://www.youtube.com/watch?v=S15pjuTJ618&t=288s',
      'video_id': 'S15pjuTJ618'},
     {'author': 'Kinney Insurance Agency',
      'channel': 'Kinney Insurance Agency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=lID4C-ymanQ&t=55s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The water overflows, goes into the unit below you causing damage. The landlord '
              'potentially could come after you for those damages. In all three scenarios, a '
              'personal liability policy will protect you from paying out-of-pocket costs.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'The water overflows, goes into the unit below you causing damage. The landlord '
             'potentially could come after you for those damages. In all three scenarios, a '
             'personal liability policy will protect you from paying out-of-pocket costs.',
      'title': 'Renters Insurance Mini-Series: Personal Liability (Kinney Insurance Agency)',
      'url': 'https://www.youtube.com/watch?v=lID4C-ymanQ&t=55s',
      'video_id': 'lID4C-ymanQ'},
     {'author': 'Dr Chau Ong',
      'channel': 'Dr Chau Ong',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=Bbit4NDO_Hc&t=197s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of the key thing when you ask asked for that budget is asked for the price '
              "range what is the price range instead of just asking for what's your budget "
              'right.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'Of the key thing when you ask asked for that budget is asked for the price range '
             "what is the price range instead of just asking for what's your budget right.",
      'title': 'How I Made 10K A MONTH With This Mid-Term Rentals| Insurance Housing (Dr Chau '
               'Ong)',
      'url': 'https://www.youtube.com/watch?v=Bbit4NDO_Hc&t=197s',
      'video_id': 'Bbit4NDO_Hc'},
     {'author': 'BiggerPockets',
      'channel': 'BiggerPockets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=8MMoqEHoIn0&t=134s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'However your tenant may not realize that your insurance only covers the '
              "building's structure and the damage cost it won't cover damage to the tenant's.",
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'However your tenant may not realize that your insurance only covers the '
             "building's structure and the damage cost it won't cover damage to the tenant's.",
      'title': 'Landlords: Always (Always, Always) Require Renters Insurance—Here’s Why | '
               'Daily Podcast (BiggerPockets)',
      'url': 'https://www.youtube.com/watch?v=8MMoqEHoIn0&t=134s',
      'video_id': '8MMoqEHoIn0'},
     {'author': 'Jorge Garcia | Roadmap Lodging',
      'channel': 'Jorge Garcia | Roadmap Lodging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=tVKu7I7bzh8&t=190s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You send an availability and rate and insurance approved. No Airbnb algorithm, '
              'no nightly pricing, no constant turnovers. Once you perform well, they remember '
              "you. That's how repeat placements happen.",
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': 'You send an availability and rate and insurance approved. No Airbnb algorithm, '
             'no nightly pricing, no constant turnovers. Once you perform well, they remember '
             "you. That's how repeat placements happen.",
      'title': 'Insurance Relocation Explained (Jorge Garcia | Roadmap Lodging)',
      'url': 'https://www.youtube.com/watch?v=tVKu7I7bzh8&t=190s',
      'video_id': 'tVKu7I7bzh8'},
     {'author': 'SureVestor',
      'channel': 'SureVestor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=pv1TYEchw80&t=98s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Coverage at a comparable price that benefits the tenant and your owner the real '
              'question is why do a resident insurance program at all to benefit your '
              'management company your owner your tenant learn how all parties can benefit '
              'from the surevestor system.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Coverage at a comparable price that benefits the tenant and your owner the real '
             'question is why do a resident insurance program at all to benefit your '
             'management company your owner your tenant learn how all parties can benefit from '
             'the surevestor system.',
      'title': 'Tenant Liability Insurance (SureVestor)',
      'url': 'https://www.youtube.com/watch?v=pv1TYEchw80&t=98s',
      'video_id': 'pv1TYEchw80'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=0EJuemJoH-0&t=20s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are looking to increase their cash flow in fact some of my properties we are '
              '5xing the long-term rental rate so stay tuned hang out with us as Serge and I '
              'are going to talk about the insurance relocation claim in depth.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Are looking to increase their cash flow in fact some of my properties we are '
             '5xing the long-term rental rate so stay tuned hang out with us as Serge and I '
             'are going to talk about the insurance relocation claim in depth.',
      'title': 'How to Make THOUSANDS a Month w/ "Temporary Housing Claim" Mid-Term Rentals '
               '(Jesse Vasquez)',
      'url': 'https://www.youtube.com/watch?v=0EJuemJoH-0&t=20s',
      'video_id': '0EJuemJoH-0'}],
 4: [{'author': 'Jorge Garcia | Roadmap Lodging',
      'channel': 'Jorge Garcia | Roadmap Lodging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:28](https://www.youtube.com/watch?v=iQn0PMSPJ5Q&t=508s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most hosts present themselves as well people. I love hiking, >> which is great '
              'for Airbnb. But an insurance adjuster with a $20,000 housing budget, they want '
              'to deal with a business, an entity. So, Superhost Dave is actually a liability '
              'here >> in a way.',
      'timestamp': 508,
      'timestamp_label': '[00:08:28]',
      'timestamp_seconds': 508,
      'tip': 'Most hosts present themselves as well people. I love hiking, >> which is great '
             'for Airbnb. But an insurance adjuster with a $20,000 housing budget, they want '
             'to deal with a business, an entity. So, Superhost Dave is actually a liability '
             'here >> in a way.',
      'title': 'Land 90 Day Corporate Housing Contracts (Jorge Garcia | Roadmap Lodging)',
      'url': 'https://www.youtube.com/watch?v=iQn0PMSPJ5Q&t=508s',
      'video_id': 'iQn0PMSPJ5Q'},
     {'author': 'Colin Wright',
      'channel': 'Colin Wright',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=iwB0c3u7Gpo&t=174s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'HOA if there is one, and the landlord. Understand any permits or licensing that '
              "apply, and get the landlord's permission in writing. You also need a real "
              'startup budget, deposit, rent, furniture, supplies, insurance, photos, and '
              'enough cash to handle a slower launch.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'HOA if there is one, and the landlord. Understand any permits or licensing that '
             "apply, and get the landlord's permission in writing. You also need a real "
             'startup budget, deposit, rent, furniture, supplies, insurance, photos, and '
             'enough cash to handle a slower launch.',
      'title': 'How I’d Start a $1,000,000/yr Airbnb Arbitrage Business in 2026 (I own 150+ '
               'Airbnbs) (Colin Wright)',
      'url': 'https://www.youtube.com/watch?v=iwB0c3u7Gpo&t=174s',
      'video_id': 'iwB0c3u7Gpo'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:44](https://www.youtube.com/watch?v=70ZSuGbTIJo&t=644s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've been doing for some time now is actually building relationships with your "
              "local insurance adjusters before competition actually intensifies. And you're "
              'absolutely going to want to diversify your client base beyond insurance '
              'housing.',
      'timestamp': 644,
      'timestamp_label': '[00:10:44]',
      'timestamp_seconds': 644,
      'tip': "I've been doing for some time now is actually building relationships with your "
             "local insurance adjusters before competition actually intensifies. And you're "
             'absolutely going to want to diversify your client base beyond insurance housing.',
      'title': 'Airbnb’s Bold Move with CRS Temporary Housing — Huge News for MTR Hosts! '
               '(Jesse Vasquez)',
      'url': 'https://www.youtube.com/watch?v=70ZSuGbTIJo&t=644s',
      'video_id': '70ZSuGbTIJo'},
     {'author': 'The CoLiving Insider',
      'channel': 'The CoLiving Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:57](https://www.youtube.com/watch?v=zj0PhRK1anA&t=477s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Has been  at or above break-even for 90 days. Put each house in its own limited '
              'liability company or LLC, so one bad.',
      'timestamp': 477,
      'timestamp_label': '[00:07:57]',
      'timestamp_seconds': 477,
      'tip': 'Has been  at or above break-even for 90 days. Put each house in its own limited '
             'liability company or LLC, so one bad.',
      'title': 'Rental Arbitrage Gone Wrong: 5 Ways a Master Lease Fails (The CoLiving '
               'Insider)',
      'url': 'https://www.youtube.com/watch?v=zj0PhRK1anA&t=477s',
      'video_id': 'zj0PhRK1anA'},
     {'author': 'Vida Arias',
      'channel': 'Vida Arias',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=mrB_eHKg6Pc&t=195s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One of my previous insurance agents that i've worked with which she was working "
              'with ellis insurance agency i called ale solutions and thd.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': "One of my previous insurance agents that i've worked with which she was working "
             'with ellis insurance agency i called ale solutions and thd.',
      'title': 'providing housing for insurance companies | *watch me call relocation '
               'companies | midterm rentals (Vida Arias)',
      'url': 'https://www.youtube.com/watch?v=mrB_eHKg6Pc&t=195s',
      'video_id': 'mrB_eHKg6Pc'},
     {'author': 'Midterm Rental Consulting',
      'channel': 'Midterm Rental Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=j86lznzD4FU&t=21s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And to gather this information, I reviewed more than 200 pages of my consulting '
              'notes with landlord hosts nationwide who are doing midterm rentals across '
              "Airbnb, Furnishfinder, Zillow, and Booking. If you are new here, I'm Aaron "
              'Spreadlin, and this is my channel.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'And to gather this information, I reviewed more than 200 pages of my consulting '
             'notes with landlord hosts nationwide who are doing midterm rentals across '
             "Airbnb, Furnishfinder, Zillow, and Booking. If you are new here, I'm Aaron "
             'Spreadlin, and this is my channel.',
      'title': 'Furnished Rentals in 2026: Forget Nurses & Insurance Claims (Midterm Rental '
               'Consulting)',
      'url': 'https://www.youtube.com/watch?v=j86lznzD4FU&t=21s',
      'video_id': 'j86lznzD4FU'},
     {'author': 'Olivia Tati',
      'channel': 'Olivia Tati',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:52](https://www.youtube.com/watch?v=bUvn66qXbaE&t=1672s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A jacket inside or something um but I know about that because it was through '
              'Airbnb you know I can have like the lease agreement but.',
      'timestamp': 1672,
      'timestamp_label': '[00:27:52]',
      'timestamp_seconds': 1672,
      'tip': 'A jacket inside or something um but I know about that because it was through '
             'Airbnb you know I can have like the lease agreement but.',
      'title': 'How to Make 3x More By Renting to Insurance Companies (Olivia Tati)',
      'url': 'https://www.youtube.com/watch?v=bUvn66qXbaE&t=1672s',
      'video_id': 'bUvn66qXbaE'},
     {'author': 'Blue Fox Properties',
      'channel': 'Blue Fox Properties',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=7sscnFcWkp4&t=307s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Doors and windows must open easily and safely. Anything that restricts '
              'emergency exit can cause issues during a claim. Number five, compliance with '
              'local building and fire codes. Insurance companies expect rentals to meet '
              'minimum safety standards.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': 'Doors and windows must open easily and safely. Anything that restricts emergency '
             'exit can cause issues during a claim. Number five, compliance with local '
             'building and fire codes. Insurance companies expect rentals to meet minimum '
             'safety standards.',
      'title': 'Homeowner insurance vs. Landlord insurance- Why the wrong policy can leave you '
               'financially exposed (Blue Fox Properties)',
      'url': 'https://www.youtube.com/watch?v=7sscnFcWkp4&t=307s',
      'video_id': '7sscnFcWkp4'},
     {'author': 'BiggerPockets',
      'channel': 'BiggerPockets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=bfsA8QKK2ZU&t=67s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next day affordable landlord Insurance in literally just a few clicks from '
              'single family to short-term rentals to apartment buildings and Beyond.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'Next day affordable landlord Insurance in literally just a few clicks from '
             'single family to short-term rentals to apartment buildings and Beyond.',
      'title': "DON'T Get This Wrong: Landlord Insurance vs. Homeowners Insurance "
               '(BiggerPockets)',
      'url': 'https://www.youtube.com/watch?v=bfsA8QKK2ZU&t=67s',
      'video_id': 'bfsA8QKK2ZU'},
     {'author': 'Bryan Gutowsky | Michigan Insurance',
      'channel': 'Bryan Gutowsky | Michigan Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=UUWJRIHQaqk&t=196s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then next, a little specific to rental property insurance policies. Make '
              'sure that the named insured does accurately reflect how you have the home deed. '
              'It can be common for a lot of these rental properties to be deed to an LLC.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'And then next, a little specific to rental property insurance policies. Make '
             'sure that the named insured does accurately reflect how you have the home deed. '
             'It can be common for a lot of these rental properties to be deed to an LLC.',
      'title': 'Rental Property Insurance vs Homeowners Insurance – What You Need To Know '
               '(Bryan Gutowsky | Michigan Insurance)',
      'url': 'https://www.youtube.com/watch?v=UUWJRIHQaqk&t=196s',
      'video_id': 'UUWJRIHQaqk'},
     {'author': 'Short-Term Stays & Rentals',
      'channel': 'Short-Term Stays & Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=QIziS47827w&t=205s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Insurance is not about expecting disaster. It is about making sure one random '
              'Tuesday does not destroy years of work you put into building this rental '
              'income. Want to learn more about protecting your mid-term rental the smart way?',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Insurance is not about expecting disaster. It is about making sure one random '
             'Tuesday does not destroy years of work you put into building this rental income. '
             'Want to learn more about protecting your mid-term rental the smart way?',
      'title': 'What Insurance Do I Need for a Midterm Rental? (Short-Term Stays & Rentals)',
      'url': 'https://www.youtube.com/watch?v=QIziS47827w&t=205s',
      'video_id': 'QIziS47827w'},
     {'author': 'Envy Property Management',
      'channel': 'Envy Property Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=Iv_qchMsG9E&t=71s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Covers the building structure and the damage caused it won't cover damage to "
              "the tenant's personal property this is where renters insurance will.",
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': "Covers the building structure and the damage caused it won't cover damage to the "
             "tenant's personal property this is where renters insurance will.",
      'title': "The Difference Between Renter's Insurance and Tenant Liability Insurance (Envy "
               'Property Management)',
      'url': 'https://www.youtube.com/watch?v=Iv_qchMsG9E&t=71s',
      'video_id': 'Iv_qchMsG9E'},
     {'author': 'Steadily',
      'channel': 'Steadily',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=8qVhmrP1DZM&t=157s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'More than one property regardless of the price you want to make sure that your '
              'landlord insurance offers the right coverage to safeguard your investment '
              'property to find out more go to steadily.com and get your commitment free quote '
              'in minutes.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'More than one property regardless of the price you want to make sure that your '
             'landlord insurance offers the right coverage to safeguard your investment '
             'property to find out more go to steadily.com and get your commitment free quote '
             'in minutes.',
      'title': 'Differences Between Homeowners Insurance And Landlord Insurance | Steadily '
               '(Steadily)',
      'url': 'https://www.youtube.com/watch?v=8qVhmrP1DZM&t=157s',
      'video_id': '8qVhmrP1DZM'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=O1Wmu9p-zdc&t=15s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Exactly how I did that I basically sent an email to an insurance company and '
              "they rented my house for me so I'm gonna break this down for you guys check "
              'this.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Exactly how I did that I basically sent an email to an insurance company and '
             "they rented my house for me so I'm gonna break this down for you guys check "
             'this.',
      'title': 'How to Make 8k a Month by Hosting Insurance Relocation Claims #midtermrentals '
               '(Jesse Vasquez)',
      'url': 'https://www.youtube.com/watch?v=O1Wmu9p-zdc&t=15s',
      'video_id': 'O1Wmu9p-zdc'},
     {'author': 'Elemental Risk Management',
      'channel': 'Elemental Risk Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=yqr3C1o6bxQ&t=172s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's a lot of different scenarios things that can happen other "
              'considerations always happy to help answer questions consult provide '
              'consultation so feel free to contact us but thanks for watching this video we '
              'appreciate you taking the time.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': "There's a lot of different scenarios things that can happen other considerations "
             'always happy to help answer questions consult provide consultation so feel free '
             'to contact us but thanks for watching this video we appreciate you taking the '
             'time.',
      'title': 'What is Lessors Risk or Commercial Landlord Insurance, and What Does it Cover? '
               '(Elemental Risk Management)',
      'url': 'https://www.youtube.com/watch?v=yqr3C1o6bxQ&t=172s',
      'video_id': 'yqr3C1o6bxQ'}],
 5: [{'author': 'LoCasa',
      'channel': 'LoCasa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:12](https://www.youtube.com/watch?v=VFt0XueZxpE&t=732s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve got these clauses locked into your addendum. It's the difference between a "
              'thriving Airbnb business and a legal nightmare. So, of course, want a copy of '
              'the exact addendum we use to get landlord approval for Airbnb arbitrage?',
      'timestamp': 732,
      'timestamp_label': '[00:12:12]',
      'timestamp_seconds': 732,
      'tip': "'ve got these clauses locked into your addendum. It's the difference between a "
             'thriving Airbnb business and a legal nightmare. So, of course, want a copy of '
             'the exact addendum we use to get landlord approval for Airbnb arbitrage?',
      'title': 'Airbnb Arbitrage Lease Addendum: Must-Have Clauses to Protect Your Business | '
               'LoCasa (LoCasa)',
      'url': 'https://www.youtube.com/watch?v=VFt0XueZxpE&t=732s',
      'video_id': 'VFt0XueZxpE'},
     {'author': 'Quentin West',
      'channel': 'Quentin West',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:55](https://www.youtube.com/watch?v=XSg1bi0bVwI&t=535s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "47 units, I thought I was building something. And there's nothing wrong with "
              "that. Cash flow businesses are how most people get started, and they're how you "
              'get any money to work with in the first place. So, the problem was never that '
              'it was a cash flow business.',
      'timestamp': 535,
      'timestamp_label': '[00:08:55]',
      'timestamp_seconds': 535,
      'tip': "47 units, I thought I was building something. And there's nothing wrong with "
             "that. Cash flow businesses are how most people get started, and they're how you "
             'get any money to work with in the first place. So, the problem was never that it '
             'was a cash flow business.',
      'title': "DON'T Try Airbnb Arbitrage Until You Watch This ($10M+ Made) (Quentin West)",
      'url': 'https://www.youtube.com/watch?v=XSg1bi0bVwI&t=535s',
      'video_id': 'XSg1bi0bVwI'},
     {'author': 'Real Estate Pros Show',
      'channel': 'Real Estate Pros Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:17](https://www.youtube.com/watch?v=-OpbvAckfkQ&t=917s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's no better opportunity to build a consistent business than to literally "
              'partner with pros to help you avoid costly mistakes, avoid the need for capital '
              "to do deals, and help you eliminate your fears as you're starting your "
              'business.',
      'timestamp': 917,
      'timestamp_label': '[00:15:17]',
      'timestamp_seconds': 917,
      'tip': "There's no better opportunity to build a consistent business than to literally "
             'partner with pros to help you avoid costly mistakes, avoid the need for capital '
             "to do deals, and help you eliminate your fears as you're starting your business.",
      'title': 'How Insurance Housing Pays More Than Airbnb (Hybrid Rental Strategy Explained) '
               '(Real Estate Pros Show)',
      'url': 'https://www.youtube.com/watch?v=-OpbvAckfkQ&t=917s',
      'video_id': '-OpbvAckfkQ'},
     {'author': 'Vivian Yip',
      'channel': 'Vivian Yip',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=vN9xRfDWrWk&t=125s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And trust me, this one's actually relevant to your business. Your pricing isn't "
              'the problem. Something else is quietly blocking your bookings and most hosts '
              'have no idea. I see it all the time in our Crew Homes Network. Hosts lower '
              'their rates and nothing changes.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': "And trust me, this one's actually relevant to your business. Your pricing isn't "
             'the problem. Something else is quietly blocking your bookings and most hosts '
             'have no idea. I see it all the time in our Crew Homes Network. Hosts lower their '
             'rates and nothing changes.',
      'title': "Airbnb's New Rules: Are Hosts at Risk? | Myka Artis (Vivian Yip)",
      'url': 'https://www.youtube.com/watch?v=vN9xRfDWrWk&t=125s',
      'video_id': 'vN9xRfDWrWk'},
     {'author': 'Alex Sabio',
      'channel': 'Alex Sabio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=52k99Zbi6fk&t=326s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Risks they're saving the 10 they're saving the maintenance cost and uh they "
              "have full occupancy so the question is why isn't every landlord doing it right "
              "right there's risks involved so a lot of landlords think Airbnb oh my God "
              "they're gonna trash.",
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': "Risks they're saving the 10 they're saving the maintenance cost and uh they have "
             "full occupancy so the question is why isn't every landlord doing it right right "
             "there's risks involved so a lot of landlords think Airbnb oh my God they're "
             'gonna trash.',
      'title': 'Scaling to 76 Airbnb Arbitrage Units with Rafa Loza (Alex Sabio)',
      'url': 'https://www.youtube.com/watch?v=52k99Zbi6fk&t=326s',
      'video_id': '52k99Zbi6fk'},
     {'author': 'Bailey Kramer',
      'channel': 'Bailey Kramer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:50](https://www.youtube.com/watch?v=De_DgYIghMo&t=350s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Might take roughly two days to set up, and again, that's for building the bed, "
              'the nightstand, the dresser, the couch, TV stand, all those things. And then of '
              'course, a three bedroom property is gonna take a little bit longer, closer to '
              'three or four days.',
      'timestamp': 350,
      'timestamp_label': '[00:05:50]',
      'timestamp_seconds': 350,
      'tip': "Might take roughly two days to set up, and again, that's for building the bed, "
             'the nightstand, the dresser, the couch, TV stand, all those things. And then of '
             'course, a three bedroom property is gonna take a little bit longer, closer to '
             'three or four days.',
      'title': 'The One Mid Term Rental Furnishing Mistake Tanking Your Occupancy Rate (Bailey '
               'Kramer)',
      'url': 'https://www.youtube.com/watch?v=De_DgYIghMo&t=350s',
      'video_id': 'De_DgYIghMo'},
     {'author': 'The Bougie Baldie',
      'channel': 'The Bougie Baldie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:01](https://www.youtube.com/watch?v=PaAH8z8rPe8&t=361s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay no pets that's not a problem and then what do they do for parking um so "
              "there's a parking space in front of the building okay.",
      'timestamp': 361,
      'timestamp_label': '[00:06:01]',
      'timestamp_seconds': 361,
      'tip': "Okay no pets that's not a problem and then what do they do for parking um so "
             "there's a parking space in front of the building okay.",
      'title': 'Providing Housing For Insurance Companies (The Bougie Baldie)',
      'url': 'https://www.youtube.com/watch?v=PaAH8z8rPe8&t=361s',
      'video_id': 'PaAH8z8rPe8'},
     {'author': 'Colony Solutions - Business Insurance',
      'channel': 'Colony Solutions - Business Insurance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=ltlYiLn1uB4&t=24s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Insurance why is this well landlords ask for business insurance to protect both '
              'you and themselves from all sort of risk and liabilities just think about it '
              'what.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'Insurance why is this well landlords ask for business insurance to protect both '
             'you and themselves from all sort of risk and liabilities just think about it '
             'what.',
      'title': 'Why Your Commercial Lease Requires Business Insurance (Colony Solutions - '
               'Business Insurance)',
      'url': 'https://www.youtube.com/watch?v=ltlYiLn1uB4&t=24s',
      'video_id': 'ltlYiLn1uB4'},
     {'author': 'ezLandlordForms',
      'channel': 'ezLandlordForms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=8wMQUi8wEbw&t=121s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information they need to choose qualified tenants avoid the headaches and risks '
              'that come from renting to unqualified tenants start screening like a pro '
              'landlord today ready to get started visit easy landlord forms.com to create an '
              'account or send a screening request.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Information they need to choose qualified tenants avoid the headaches and risks '
             'that come from renting to unqualified tenants start screening like a pro '
             'landlord today ready to get started visit easy landlord forms.com to create an '
             'account or send a screening request.',
      'title': 'Best Tenant Screening Service for Landlords (ezLandlordForms)',
      'url': 'https://www.youtube.com/watch?v=8wMQUi8wEbw&t=121s',
      'video_id': '8wMQUi8wEbw'},
     {'author': 'The CoLiving Insider',
      'channel': 'The CoLiving Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=VbsbBFnJvik&t=305s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And a turnover checklist so every room is reset the same way every time. The '
              'most common mistake with this guest is building the whole plan on one hospital '
              'or one job site. The investor sees a big hospital, buys a house nearby and '
              'fills it with travel nurses.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': 'And a turnover checklist so every room is reset the same way every time. The '
             'most common mistake with this guest is building the whole plan on one hospital '
             'or one job site. The investor sees a big hospital, buys a house nearby and fills '
             'it with travel nurses.',
      'title': 'Travel Nurses and Contract Workers: The Co-Living Guest Who Pays More (Guest '
               'Type 2 of 7) (The CoLiving Insider)',
      'url': 'https://www.youtube.com/watch?v=VbsbBFnJvik&t=305s',
      'video_id': 'VbsbBFnJvik'},
     {'author': 'CorporateHousingTV',
      'channel': 'CorporateHousingTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=HkJIx9DYeiA&t=51s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Year they do an incredible job of vetting everybody for you taking care of all '
              "the paperwork the rental agreement it's all done for you the money is.",
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'Year they do an incredible job of vetting everybody for you taking care of all '
             "the paperwork the rental agreement it's all done for you the money is.",
      'title': 'CHBO Review — How I Rented My Furnished Home with Corporate Housing by Owner '
               'as a Property Owner (CorporateHousingTV)',
      'url': 'https://www.youtube.com/watch?v=HkJIx9DYeiA&t=51s',
      'video_id': 'HkJIx9DYeiA'},
     {'author': 'Plus Relocation',
      'channel': 'Plus Relocation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=fv6KqAzMsVI&t=32s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Leasing periods this is something that the employee is typically signing for '
              'rather than the company once the corporate apartment has been secured the.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'Leasing periods this is something that the employee is typically signing for '
             'rather than the company once the corporate apartment has been secured the.',
      'title': 'How do I prepare a relocating employee for their time in temporary housing? '
               '(Plus Relocation)',
      'url': 'https://www.youtube.com/watch?v=fv6KqAzMsVI&t=32s',
      'video_id': 'fv6KqAzMsVI'},
     {'author': 'David Piotrowski',
      'channel': 'David Piotrowski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=dOXVjIvVseI&t=163s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Housing accommodations in which the tenant shares bathroom or kitchen '
              'facilities with the owner who maintained their principal residence at the.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Housing accommodations in which the tenant shares bathroom or kitchen facilities '
             'with the owner who maintained their principal residence at the.',
      'title': 'AB1482 - Exemptions to the Tenant Protection Act of 2019 (David Piotrowski)',
      'url': 'https://www.youtube.com/watch?v=dOXVjIvVseI&t=163s',
      'video_id': 'dOXVjIvVseI'},
     {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
      'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:52](https://www.youtube.com/watch?v=utDX2blYFMk&t=1192s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Way make landlord life a breeze with key check the game changer for Modern '
              'Property Owners physics key.com to unlock the power of stress-free property '
              'management and take your rental business to new.',
      'timestamp': 1192,
      'timestamp_label': '[00:19:52]',
      'timestamp_seconds': 1192,
      'tip': 'Way make landlord life a breeze with key check the game changer for Modern '
             'Property Owners physics key.com to unlock the power of stress-free property '
             'management and take your rental business to new.',
      'title': 'The Travel Nurse Advantage | Over 12% Cash on Cash Return with Furnished '
               'Finder | Ep. 135 (Landlord Diaries - The Monthly Rentals Podcast)',
      'url': 'https://www.youtube.com/watch?v=utDX2blYFMk&t=1192s',
      'video_id': 'utDX2blYFMk'},
     {'author': 'Commercial Real Estate Pro Network',
      'channel': 'Commercial Real Estate Pro Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:23](https://www.youtube.com/watch?v=ZVbVs2WDmLw&t=263s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Will endeavor uh to notify you if the policy cancels so those are the basic on '
              'a certificate of liability uh hopefully that helps if you have any questions '
              'please reach out give me a call uh Darren gross at excuse me Darren atj Daren '
              'gross.com.',
      'timestamp': 263,
      'timestamp_label': '[00:04:23]',
      'timestamp_seconds': 263,
      'tip': 'Will endeavor uh to notify you if the policy cancels so those are the basic on a '
             'certificate of liability uh hopefully that helps if you have any questions '
             'please reach out give me a call uh Darren gross at excuse me Darren atj Daren '
             'gross.com.',
      'title': 'Landlord   Tenant Required Insurance Certificate of Liability Insurance '
               '(Commercial Real Estate Pro Network)',
      'url': 'https://www.youtube.com/watch?v=ZVbVs2WDmLw&t=263s',
      'video_id': 'ZVbVs2WDmLw'}],
 6: [{'author': 'Linda Kim',
      'channel': 'Linda Kim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:51:30](https://www.youtube.com/watch?v=5vV0oy-jJ7g&t=3090s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh I think people like it when there's an onsuite, there's a bathroom in the "
              "bedroom >> and then also >> that's a big deal >> because I I'm building my "
              'first Airbnb or for a short-term rental.',
      'timestamp': 3090,
      'timestamp_label': '[00:51:30]',
      'timestamp_seconds': 3090,
      'tip': "Uh I think people like it when there's an onsuite, there's a bathroom in the "
             "bedroom >> and then also >> that's a big deal >> because I I'm building my first "
             'Airbnb or for a short-term rental.',
      'title': 'The Six-Figure Airbnb Arbitrage System Without Owning Property (Linda Kim)',
      'url': 'https://www.youtube.com/watch?v=5vV0oy-jJ7g&t=3090s',
      'video_id': '5vV0oy-jJ7g'},
     {'author': 'Henrick Mathieu - Moving To Ottawa',
      'channel': 'Henrick Mathieu - Moving To Ottawa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=N4x6hSMmcaM&t=154s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The advantage of using suppliers from the list is that they already agreed not '
              'to charge more than the cap rate. And they submit their bill directly to BGRS, '
              'so no money out of pocket for you and having to deal with receipts.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'The advantage of using suppliers from the list is that they already agreed not '
             'to charge more than the cap rate. And they submit their bill directly to BGRS, '
             'so no money out of pocket for you and having to deal with receipts.',
      'title': 'CAF Relocation : WHAT TO EXPECT ! Posting message, HHT, BGRS and more [20121] '
               '(Henrick Mathieu - Moving To Ottawa)',
      'url': 'https://www.youtube.com/watch?v=N4x6hSMmcaM&t=154s',
      'video_id': 'N4x6hSMmcaM'},
     {'author': 'Short Term Rental Secrets',
      'channel': 'Short Term Rental Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=D63ppvOFpvk&t=15s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business i started identifying what customers i really went to uh customers i '
              'really want to appeal to and then on my first deal i took out i.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Business i started identifying what customers i really went to uh customers i '
             'really want to appeal to and then on my first deal i took out i.',
      'title': 'Scaling a Rental Arbitrage Business With Systems & Teams with Brian Fontenot '
               '(Short Term Rental Secrets)',
      'url': 'https://www.youtube.com/watch?v=D63ppvOFpvk&t=15s',
      'video_id': 'D63ppvOFpvk'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:27](https://www.youtube.com/watch?v=VtuboLMzJj0&t=1227s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where we actually find tenants. I have a lot of people asking me all the time, '
              'Jess, where do I list my properties? Tell you guys right now, you absolutely '
              'want to be listed on Airbnb. You absolutely want to be listed on VBO.',
      'timestamp': 1227,
      'timestamp_label': '[00:20:27]',
      'timestamp_seconds': 1227,
      'tip': 'Where we actually find tenants. I have a lot of people asking me all the time, '
             'Jess, where do I list my properties? Tell you guys right now, you absolutely '
             'want to be listed on Airbnb. You absolutely want to be listed on VBO.',
      'title': 'Mid-Term Rentals 101 (2025): Watch This FIRST — Leases, Deposits & Listings '
               '(Jesse Vasquez)',
      'url': 'https://www.youtube.com/watch?v=VtuboLMzJj0&t=1227s',
      'video_id': 'VtuboLMzJj0'},
     {'author': '60SecondLaw',
      'channel': '60SecondLaw',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:14](https://www.youtube.com/watch?v=X_XeyY10oQE&t=314s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step one is all about paper. Read it, write it, keep it. Step two, negotiate '
              'the buyout. Call the landlord, explain the situation, and propose a deal. A '
              'fixed payment to end the lease, effective on a specific date. Offer to help '
              'find a replacement tenant.',
      'timestamp': 314,
      'timestamp_label': '[00:05:14]',
      'timestamp_seconds': 314,
      'tip': 'Step one is all about paper. Read it, write it, keep it. Step two, negotiate the '
             'buyout. Call the landlord, explain the situation, and propose a deal. A fixed '
             'payment to end the lease, effective on a specific date. Offer to help find a '
             'replacement tenant.',
      'title': 'Want Out of Your Lease Early? The Real Cost of Breaking It (60SecondLaw)',
      'url': 'https://www.youtube.com/watch?v=X_XeyY10oQE&t=314s',
      'video_id': 'X_XeyY10oQE'},
     {'author': 'The Furnished Rental Strategist',
      'channel': 'The Furnished Rental Strategist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:43](https://www.youtube.com/watch?v=P52IQsnqFe0&t=403s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This doesn't have to be permanent. Let me give you a clearer example. Let's say "
              'you own a four-bedroom home in Gilbert. On paper, as an Airbnb, it looked like '
              'a great deal.',
      'timestamp': 403,
      'timestamp_label': '[00:06:43]',
      'timestamp_seconds': 403,
      'tip': "This doesn't have to be permanent. Let me give you a clearer example. Let's say "
             'you own a four-bedroom home in Gilbert. On paper, as an Airbnb, it looked like a '
             'great deal.',
      'title': 'When to Switch from Airbnb to Mid-Term Rentals (Phoenix Investors Need to Hear '
               'This) (The Furnished Rental Strategist)',
      'url': 'https://www.youtube.com/watch?v=P52IQsnqFe0&t=403s',
      'video_id': 'P52IQsnqFe0'},
     {'author': 'Bailey Kramer',
      'channel': 'Bailey Kramer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:18](https://www.youtube.com/watch?v=J-7ks576i8Q&t=438s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But I always update that list too. Whenever I find new companies. So if you '
              "click the link below, you'll have the most updated version of the companies I "
              'use and register my properties on. So Aly solutions, this was the first one on '
              'the list and kind of my favorite.',
      'timestamp': 438,
      'timestamp_label': '[00:07:18]',
      'timestamp_seconds': 438,
      'tip': 'But I always update that list too. Whenever I find new companies. So if you '
             "click the link below, you'll have the most updated version of the companies I "
             'use and register my properties on. So Aly solutions, this was the first one on '
             'the list and kind of my favorite.',
      'title': 'Get Insurance Companies to Book Your Property! (Bailey Kramer)',
      'url': 'https://www.youtube.com/watch?v=J-7ks576i8Q&t=438s',
      'video_id': 'J-7ks576i8Q'},
     {'author': 'Cherif Medawar',
      'channel': 'Cherif Medawar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=enwvqXWa1Wk&t=15s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Willing to lease with a sublease agreement how do we structure the earnest '
              'money and 45 days due diligence to find a tenant to sublease to the last.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Willing to lease with a sublease agreement how do we structure the earnest money '
             'and 45 days due diligence to find a tenant to sublease to the last.',
      'title': 'How Does A Sublease Work? (Cherif Medawar)',
      'url': 'https://www.youtube.com/watch?v=enwvqXWa1Wk&t=15s',
      'video_id': 'enwvqXWa1Wk'},
     {'author': 'Attorney Robert Flessas',
      'channel': 'Attorney Robert Flessas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=aMeH-WgmCCg&t=15s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If this is your first time here you might want to subscribe right now because '
              "if you do you'll know where to find me to get answers to your.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'If this is your first time here you might want to subscribe right now because if '
             "you do you'll know where to find me to get answers to your.",
      'title': 'CAN A LANDLORD NOT RENEW YOUR LEASE AT ANYTIME? (Attorney Robert Flessas)',
      'url': 'https://www.youtube.com/watch?v=aMeH-WgmCCg&t=15s',
      'video_id': 'aMeH-WgmCCg'},
     {'author': 'FIRE ♦ Rich Rice',
      'channel': 'FIRE ♦ Rich Rice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:46](https://www.youtube.com/watch?v=qW_BPyW-9Ug&t=886s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I saw Johnny's face kind of. Hey, I probably a few of few others, but I just "
              "happen to see yours first, so I'm picking on you. So, arbitrage basically, it's "
              "it's it's master leasing a property.",
      'timestamp': 886,
      'timestamp_label': '[00:14:46]',
      'timestamp_seconds': 886,
      'tip': "I saw Johnny's face kind of. Hey, I probably a few of few others, but I just "
             "happen to see yours first, so I'm picking on you. So, arbitrage basically, it's "
             "it's it's master leasing a property.",
      'title': 'Profitable Rentals with Purpose: Housing Displaced Families (FIRE ♦ Rich Rice)',
      'url': 'https://www.youtube.com/watch?v=qW_BPyW-9Ug&t=886s',
      'video_id': 'qW_BPyW-9Ug'},
     {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=scmRAbKvEPk&t=120s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So there's an agreement and stuff that's back and forth and you have to deal "
              'with some of the other tenants and things that might object to even just '
              'having.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': "So there's an agreement and stuff that's back and forth and you have to deal "
             'with some of the other tenants and things that might object to even just having.',
      'title': 'Which is Harder to Start and Scale, Rental Arbitrage or Cohosting? (Short Term '
               'Sage - Airbnb, Vacation Rental Host)',
      'url': 'https://www.youtube.com/watch?v=scmRAbKvEPk&t=120s',
      'video_id': 'scmRAbKvEPk'},
     {'author': 'Midterm Rental Consulting',
      'channel': 'Midterm Rental Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:01](https://www.youtube.com/watch?v=fXUr5E30rH8&t=541s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The landlord so I can cancel the contract if I find out your sub Leasing and '
              "you didn't clear it with me first and in writing no subase of the property.",
      'timestamp': 541,
      'timestamp_label': '[00:09:01]',
      'timestamp_seconds': 541,
      'tip': 'The landlord so I can cancel the contract if I find out your sub Leasing and you '
             "didn't clear it with me first and in writing no subase of the property.",
      'title': 'Lease Language for Midterm Rental Landlords (Midterm Rental Consulting)',
      'url': 'https://www.youtube.com/watch?v=fXUr5E30rH8&t=541s',
      'video_id': 'fXUr5E30rH8'},
     {'author': 'pinefinancial',
      'channel': 'pinefinancial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:48](https://www.youtube.com/watch?v=zFdoBfVEFUU&t=408s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just making it fun to read and like easier to get through than just a '
              "step-by-step book awesome and where's the best place for someone to either find "
              'you or the book yeah so the book.',
      'timestamp': 408,
      'timestamp_label': '[00:06:48]',
      'timestamp_seconds': 408,
      'tip': 'Just making it fun to read and like easier to get through than just a '
             "step-by-step book awesome and where's the best place for someone to either find "
             'you or the book yeah so the book.',
      'title': 'Medium-Term Rentals: How to Manage Mid-Term Rental Properties (pinefinancial)',
      'url': 'https://www.youtube.com/watch?v=zFdoBfVEFUU&t=408s',
      'video_id': 'zFdoBfVEFUU'},
     {'author': 'Jorge Garcia | Roadmap Lodging',
      'channel': 'Jorge Garcia | Roadmap Lodging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=6E0c94bnI-s&t=146s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're a member who made their lives easier. That's why when new employees "
              "relocate, you're the first call they make. You're not writing algorithms. So, "
              'how do you build a relationship that actually lasts? You need to follow up on '
              'every sale.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': "They're a member who made their lives easier. That's why when new employees "
             "relocate, you're the first call they make. You're not writing algorithms. So, "
             'how do you build a relationship that actually lasts? You need to follow up on '
             'every sale.',
      'title': 'I Built My Corporate Housing Business BACKWARDS (And It Works Better) (Jorge '
               'Garcia | Roadmap Lodging)',
      'url': 'https://www.youtube.com/watch?v=6E0c94bnI-s&t=146s',
      'video_id': '6E0c94bnI-s'},
     {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
      'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:20](https://www.youtube.com/watch?v=-wmwnisQl4w&t=440s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Give us the rooms for them you know but um currently in our portfolio we don't "
              'really count the Arbitrage as part of our portfolio right now okay I think.',
      'timestamp': 440,
      'timestamp_label': '[00:07:20]',
      'timestamp_seconds': 440,
      'tip': "Give us the rooms for them you know but um currently in our portfolio we don't "
             'really count the Arbitrage as part of our portfolio right now okay I think.',
      'title': '$100K from 15 Insurance Stays in 30 Days | The Midterm Rental Blueprint w/ KP '
               'Akom | Ep. 125 (Landlord Diaries - The Monthly Rentals Podcast)',
      'url': 'https://www.youtube.com/watch?v=-wmwnisQl4w&t=440s',
      'video_id': '-wmwnisQl4w'}],
 7: [{'author': 'Richie Matthews',
      'channel': 'Richie Matthews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:10](https://www.youtube.com/watch?v=O4cBKKUBS64&t=790s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s work, business, and leisure. So step one is list your property on Airbnb. "
              'Step two is hire a VA and have that person then list your property on Booking. '
              'Expedia, Google Travel, Furnishfinder, ALeSolutions, and SAM.',
      'timestamp': 790,
      'timestamp_label': '[00:13:10]',
      'timestamp_seconds': 790,
      'tip': "'s work, business, and leisure. So step one is list your property on Airbnb. "
             'Step two is hire a VA and have that person then list your property on Booking. '
             'Expedia, Google Travel, Furnishfinder, ALeSolutions, and SAM.',
      'title': 'Billion Dollar Blueprint For Apartment Arbitrage (Richie Matthews)',
      'url': 'https://www.youtube.com/watch?v=O4cBKKUBS64&t=790s',
      'video_id': 'O4cBKKUBS64'},
     {'author': 'Jorge Garcia | Roadmap Lodging',
      'channel': 'Jorge Garcia | Roadmap Lodging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=PJdlrM6k8ks&t=75s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They lose their routine, their comfort, their sense of their sense of '
              "stability. That's when insurance companies step in because every homeowner's "
              'policy includes something called ALE. Additional living expenses.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'They lose their routine, their comfort, their sense of their sense of stability. '
             "That's when insurance companies step in because every homeowner's policy "
             'includes something called ALE. Additional living expenses.',
      'title': 'How Insurance Claims Pay More Than Airbnb Ever Will (Jorge Garcia | Roadmap '
               'Lodging)',
      'url': 'https://www.youtube.com/watch?v=PJdlrM6k8ks&t=75s',
      'video_id': 'PJdlrM6k8ks'},
     {'author': 'Noelle Randall',
      'channel': 'Noelle Randall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=cJJUHWNqI-I&t=20s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to share with you a simple step-by-step process on how to start, "
              'launch or grow a corporate housing business.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "I'm going to share with you a simple step-by-step process on how to start, "
             'launch or grow a corporate housing business.',
      'title': 'How To Do Corporate Housing (Noelle Randall)',
      'url': 'https://www.youtube.com/watch?v=cJJUHWNqI-I&t=20s',
      'video_id': 'cJJUHWNqI-I'},
     {'author': 'How Master',
      'channel': 'How Master',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=NHwhu1sMUfo&t=156s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Communication is mostly handled by email or phone, so don't expect an "
              "integrated messaging system like Airbnb. It's more direct, but also less "
              "secure. That's fine if you're careful, but again, you need to verify everything "
              'before making a commitment.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': "Communication is mostly handled by email or phone, so don't expect an integrated "
             "messaging system like Airbnb. It's more direct, but also less secure. That's "
             "fine if you're careful, but again, you need to verify everything before making a "
             'commitment.',
      'title': 'Furnished Finder Review: My Honest Experience Using It to Rent Temporary '
               'Housing as a Travel Nurse (How Master)',
      'url': 'https://www.youtube.com/watch?v=NHwhu1sMUfo&t=156s',
      'video_id': 'NHwhu1sMUfo'},
     {'author': 'Airbnb Hosting and Short Term Rental Tips',
      'channel': 'Airbnb Hosting and Short Term Rental Tips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:13](https://www.youtube.com/watch?v=wVmj30HlGcQ&t=973s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'OTAAS or wherever they come from, there might be different steps. I say you '
              "even do it when they're from Airbnb, but credit checks, >> background checks, "
              '>> background checks, income checks, >> and this has to be fair across every '
              'single applicant.',
      'timestamp': 973,
      'timestamp_label': '[00:16:13]',
      'timestamp_seconds': 973,
      'tip': 'OTAAS or wherever they come from, there might be different steps. I say you even '
             "do it when they're from Airbnb, but credit checks, >> background checks, >> "
             'background checks, income checks, >> and this has to be fair across every single '
             'applicant.',
      'title': 'Should You Pivot your Airbnb to a Mid-Term Rental? (not what you think!) '
               '(Airbnb Hosting and Short Term Rental Tips)',
      'url': 'https://www.youtube.com/watch?v=wVmj30HlGcQ&t=973s',
      'video_id': 'wVmj30HlGcQ'},
     {'author': 'eForms',
      'channel': 'eForms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=z85yNn7zCws&t=162s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Into your lease agreement in the first place we're e-forms the largest online "
              'database of legal forms and we have just about every document that you can '
              'imagine for leases evictions and more click the link to access more templates '
              'that can guide you through the process.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': "Into your lease agreement in the first place we're e-forms the largest online "
             'database of legal forms and we have just about every document that you can '
             'imagine for leases evictions and more click the link to access more templates '
             'that can guide you through the process.',
      'title': 'How To Break A Lease Early (And Avoid Getting Taken to Court) (eForms)',
      'url': 'https://www.youtube.com/watch?v=z85yNn7zCws&t=162s',
      'video_id': 'z85yNn7zCws'},
     {'author': 'John Racine',
      'channel': 'John Racine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:17](https://www.youtube.com/watch?v=iNwc9csMvTA&t=617s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Maybe, maybe not, but you won't know until you run the numbers. And that's "
              'really my point. Let me give you a quick example from my own experience. '
              'Through CGR Stays, my property management, co-hosting and furnished rental '
              'business, we operate a rental arbitrage property.',
      'timestamp': 617,
      'timestamp_label': '[00:10:17]',
      'timestamp_seconds': 617,
      'tip': "Maybe, maybe not, but you won't know until you run the numbers. And that's "
             'really my point. Let me give you a quick example from my own experience. Through '
             'CGR Stays, my property management, co-hosting and furnished rental business, we '
             'operate a rental arbitrage property.',
      'title': "Rent Can't Go Up? Here's the Midterm Rental Alternative That Pays (John "
               'Racine)',
      'url': 'https://www.youtube.com/watch?v=iNwc9csMvTA&t=617s',
      'video_id': 'iNwc9csMvTA'},
     {'author': 'KSL News Utah',
      'channel': 'KSL News Utah',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=UvKA-_UlbVU&t=90s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "McKay thinks it's a conversation worth having. My question for my colleagues "
              'is, should we continue this policy where the exemption applies to rentals and '
              "we're getting more and more rentals? Now, this bill has only started moving "
              'through the legislative process here.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': "McKay thinks it's a conversation worth having. My question for my colleagues is, "
             "should we continue this policy where the exemption applies to rentals and we're "
             'getting more and more rentals? Now, this bill has only started moving through '
             'the legislative process here.',
      'title': "Landlord, tenant groups unite to oppose limiting Utah's residential property "
               'tax exemption (KSL News Utah)',
      'url': 'https://www.youtube.com/watch?v=UvKA-_UlbVU&t=90s',
      'video_id': 'UvKA-_UlbVU'},
     {'author': 'Better Call Kal',
      'channel': 'Better Call Kal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=2ZipHRbP_7U&t=39s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Chance so let's get started on the video number one review your lease the first "
              'step in trying to get out the lease agreement is to thoroughly review your.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "Chance so let's get started on the video number one review your lease the first "
             'step in trying to get out the lease agreement is to thoroughly review your.',
      'title': 'Lawyer Explains: How To Get Out Of A Lease Early (Better Call Kal)',
      'url': 'https://www.youtube.com/watch?v=2ZipHRbP_7U&t=39s',
      'video_id': '2ZipHRbP_7U'},
     {'author': 'Jorge Contreras | Airbnb Arbitrage',
      'channel': 'Jorge Contreras | Airbnb Arbitrage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=_M0OdXelhoU&t=189s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Properties right wear and tear take up all the parking in the street disrupt '
              'the neighborhood parties are never a good situation and so when you say the '
              "word Airbnb they didn't hear Airbnb they heard.",
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': 'Properties right wear and tear take up all the parking in the street disrupt the '
             'neighborhood parties are never a good situation and so when you say the word '
             "Airbnb they didn't hear Airbnb they heard.",
      'title': 'The BEST way to Pitch a Landlord for Airbnb Arbitrage (step-by-step) (Jorge '
               'Contreras | Airbnb Arbitrage)',
      'url': 'https://www.youtube.com/watch?v=_M0OdXelhoU&t=189s',
      'video_id': '_M0OdXelhoU'},
     {'author': 'Temporary Accommodations',
      'channel': 'Temporary Accommodations',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=lXiREzZ0FPo&t=116s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In the balance there's comfort in knowing there's a temporary housing partner "
              'you can trust to achieve positive outcomes at this first critical step toward '
              "restoration leading to greater policyholder satisfaction and retention that's "
              'why ta.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "In the balance there's comfort in knowing there's a temporary housing partner "
             'you can trust to achieve positive outcomes at this first critical step toward '
             "restoration leading to greater policyholder satisfaction and retention that's "
             'why ta.',
      'title': 'Temporary Accommodations Intro Video (Temporary Accommodations)',
      'url': 'https://www.youtube.com/watch?v=lXiREzZ0FPo&t=116s',
      'video_id': 'lXiREzZ0FPo'},
     {'author': 'Jorge Garcia | Roadmap Lodging',
      'channel': 'Jorge Garcia | Roadmap Lodging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=68tMFzAJyS0&t=25s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'll walk you through it step-by-step. Now, here's the thing, relocation "
              "coordinators, HR managers, insurance adjusters, they're all juggling people, "
              'timelines, and logistics. The last thing they want is another pushy host '
              'selling a unit.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "I'll walk you through it step-by-step. Now, here's the thing, relocation "
             "coordinators, HR managers, insurance adjusters, they're all juggling people, "
             'timelines, and logistics. The last thing they want is another pushy host selling '
             'a unit.',
      'title': 'Corporate Housing Outreach That Works: My Word-for-Word Pitch (Jorge Garcia | '
               'Roadmap Lodging)',
      'url': 'https://www.youtube.com/watch?v=68tMFzAJyS0&t=25s',
      'video_id': '68tMFzAJyS0'},
     {'author': 'Dr Chau Ong',
      'channel': 'Dr Chau Ong',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=JWjjZOTJhUs&t=494s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One how you feel what would we like and my friend never stop never give up '
              'until you achieve your Financial Freedom we are here every step of the way we '
              'see you on the inside of our amazing mentorship.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': 'One how you feel what would we like and my friend never stop never give up until '
             'you achieve your Financial Freedom we are here every step of the way we see you '
             'on the inside of our amazing mentorship.',
      'title': 'Mid-term Rental Corporate Housing Arbitrage (Dr Chau Ong)',
      'url': 'https://www.youtube.com/watch?v=JWjjZOTJhUs&t=494s',
      'video_id': 'JWjjZOTJhUs'},
     {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
      'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:10](https://www.youtube.com/watch?v=fofW0XVB9fA&t=1570s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have my assistant actually go on Furnish finder and I tell her hey look for '
              "three bedroom two and a half bathrooms with a fenced in yard that's pet "
              'friendly in.',
      'timestamp': 1570,
      'timestamp_label': '[00:26:10]',
      'timestamp_seconds': 1570,
      'tip': 'Have my assistant actually go on Furnish finder and I tell her hey look for '
             "three bedroom two and a half bathrooms with a fenced in yard that's pet friendly "
             'in.',
      'title': 'Master Insurance Housing: Partner w/ Other Furnished Finder Hosts Like Will '
               'Dotson | Ep. 111 (Landlord Diaries - The Monthly Rentals Podcast)',
      'url': 'https://www.youtube.com/watch?v=fofW0XVB9fA&t=1570s',
      'video_id': 'fofW0XVB9fA'},
     {'author': 'Caytlyn Cole Tolliver',
      'channel': 'Caytlyn Cole Tolliver',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:57](https://www.youtube.com/watch?v=KIPX-8cQrqc&t=597s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Happen to those so I did scan those in and just put the fake duplicate one in '
              "the house yeah those are my nine lessons that I've learned so far renting out "
              'our home to traveling nurses thank you so much for watching and I will see you '
              'in my next video bye.',
      'timestamp': 597,
      'timestamp_label': '[00:09:57]',
      'timestamp_seconds': 597,
      'tip': 'Happen to those so I did scan those in and just put the fake duplicate one in '
             "the house yeah those are my nine lessons that I've learned so far renting out "
             'our home to traveling nurses thank you so much for watching and I will see you '
             'in my next video bye.',
      'title': "9 Lessons I've learned from renting our home to traveling nurses (Caytlyn Cole "
               'Tolliver)',
      'url': 'https://www.youtube.com/watch?v=KIPX-8cQrqc&t=597s',
      'video_id': 'KIPX-8cQrqc'}],
 8: [{'author': 'Rafa Loza',
      'channel': 'Rafa Loza',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:40](https://www.youtube.com/watch?v=894g1JF-IuM&t=700s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you need that kind of stuff, you know, go talk to Tony Robbins. He's got "
              'some fantastic stuff. But in the uh arbitrage world, I I want you guys to '
              "understand something. You're not building an Airbnb business.",
      'timestamp': 700,
      'timestamp_label': '[00:11:40]',
      'timestamp_seconds': 700,
      'tip': "If you need that kind of stuff, you know, go talk to Tony Robbins. He's got some "
             'fantastic stuff. But in the uh arbitrage world, I I want you guys to understand '
             "something. You're not building an Airbnb business.",
      'title': 'How To Start An Airbnb Business Without Owning Property (Part 1 of 3) (Rafa '
               'Loza)',
      'url': 'https://www.youtube.com/watch?v=894g1JF-IuM&t=700s',
      'video_id': '894g1JF-IuM'},
     {'author': 'Rafael Loza',
      'channel': 'Rafael Loza',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:50](https://www.youtube.com/watch?v=J8lQc66Jf6c&t=350s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Management software the dynamic pricing tool the high-speed internet the photos '
              "and the cleaners okay there's a lot out there but these for me I've realized "
              'have made the best impact in my business.',
      'timestamp': 350,
      'timestamp_label': '[00:05:50]',
      'timestamp_seconds': 350,
      'tip': 'Management software the dynamic pricing tool the high-speed internet the photos '
             "and the cleaners okay there's a lot out there but these for me I've realized "
             'have made the best impact in my business.',
      'title': 'How to Automate your Airbnb Rental Arbitrage! (Rafael Loza)',
      'url': 'https://www.youtube.com/watch?v=J8lQc66Jf6c&t=350s',
      'video_id': 'J8lQc66Jf6c'},
     {'author': 'NickProRealty',
      'channel': 'NickProRealty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=JXpAcw_t-CQ&t=36s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second, they search Airbnb regulations and short-term rental bans because rules '
              'keep tightening in many cities and enforcement is getting real.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Second, they search Airbnb regulations and short-term rental bans because rules '
             'keep tightening in many cities and enforcement is getting real.',
      'title': 'MTR vs. Airbnb: How Savvy Investors Are Pivoting for 2026 (NickProRealty)',
      'url': 'https://www.youtube.com/watch?v=JXpAcw_t-CQ&t=36s',
      'video_id': 'JXpAcw_t-CQ'},
     {'author': 'The Furnished Rental Strategist',
      'channel': 'The Furnished Rental Strategist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:57](https://www.youtube.com/watch?v=xbiJ4HzellI&t=477s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every guest must submit an ID and sign a lease agreement. I collect a '
              'refundable security deposit. We run a soft background check if booked direct. I '
              'use tools like tenant cloud or owner to send agreements and collect payment.',
      'timestamp': 477,
      'timestamp_label': '[00:07:57]',
      'timestamp_seconds': 477,
      'tip': 'Every guest must submit an ID and sign a lease agreement. I collect a refundable '
             'security deposit. We run a soft background check if booked direct. I use tools '
             'like tenant cloud or owner to send agreements and collect payment.',
      'title': 'Want to\xa0know how to Set Up a Mid-Term Rental in Phoenix: Full 2025 Guide '
               '(The Furnished Rental Strategist)',
      'url': 'https://www.youtube.com/watch?v=xbiJ4HzellI&t=477s',
      'video_id': 'xbiJ4HzellI'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:38](https://www.youtube.com/watch?v=NTumQCcmf3s&t=1838s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's really really what uh what we do this. So, you're going to have one bank "
              'account, the lease, the furniture, the software, and still have no business '
              "because nobody's booking the property. So, as I mentioned earlier, we need to "
              'know the basic booking process.',
      'timestamp': 1838,
      'timestamp_label': '[00:30:38]',
      'timestamp_seconds': 1838,
      'tip': "It's really really what uh what we do this. So, you're going to have one bank "
             'account, the lease, the furniture, the software, and still have no business '
             "because nobody's booking the property. So, as I mentioned earlier, we need to "
             'know the basic booking process.',
      'title': 'If I Started a Midterm Rental Today, These Are the 7 Things I’d Get Right '
               '(Jesse Vasquez)',
      'url': 'https://www.youtube.com/watch?v=NTumQCcmf3s&t=1838s',
      'video_id': 'NTumQCcmf3s'},
     {'author': 'Jesse Vasquez',
      'channel': 'Jesse Vasquez',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=pHQyi1xl5jc&t=257s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, P&L is going to be very, very important. This is another big piece of the '
              "puzzle. I don't think people realize when you start a business, which again, if "
              "you're just listing on a platform like Airbnb or Furnish Finder, you don't "
              'actually own a business.',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'So, P&L is going to be very, very important. This is another big piece of the '
             "puzzle. I don't think people realize when you start a business, which again, if "
             "you're just listing on a platform like Airbnb or Furnish Finder, you don't "
             'actually own a business.',
      'title': 'How to Start Your Midterm Rental Business with Just ONE Property (Jesse '
               'Vasquez)',
      'url': 'https://www.youtube.com/watch?v=pHQyi1xl5jc&t=257s',
      'video_id': 'pHQyi1xl5jc'},
     {'author': 'Clint Coons Esq. | Real Estate Asset Protection',
      'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:57](https://www.youtube.com/watch?v=2WVMiZV3TYI&t=2037s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a new regulation that's coming out there, maybe a ban or a limitation on "
              'permits. So these 30 day stays are something that I think everyone needs to be '
              'thinking about as well and putting an extra tool in your toolbox.',
      'timestamp': 2037,
      'timestamp_label': '[00:33:57]',
      'timestamp_seconds': 2037,
      'tip': "'s a new regulation that's coming out there, maybe a ban or a limitation on "
             'permits. So these 30 day stays are something that I think everyone needs to be '
             'thinking about as well and putting an extra tool in your toolbox.',
      'title': 'This Mid-Term Rental Strategy Will CHANGE Real Estate Investing Forever (Clint '
               'Coons Esq. | Real Estate Asset Protection)',
      'url': 'https://www.youtube.com/watch?v=2WVMiZV3TYI&t=2037s',
      'video_id': '2WVMiZV3TYI'},
     {'author': 'TurboTenant',
      'channel': 'TurboTenant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:43](https://www.youtube.com/watch?v=mVLtwRhKCcA&t=523s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, ultimately the platform was kind of built for relocation companies to '
              "be a tool for them to find landlords faster, but that also means that it's a "
              'resource for landlords.',
      'timestamp': 523,
      'timestamp_label': '[00:08:43]',
      'timestamp_seconds': 523,
      'tip': 'And so, ultimately the platform was kind of built for relocation companies to be '
             "a tool for them to find landlords faster, but that also means that it's a "
             'resource for landlords.',
      'title': 'Insurance Companies Will Pay Landlords for Monthly Rentals — Here’s How to Get '
               'In (TurboTenant)',
      'url': 'https://www.youtube.com/watch?v=mVLtwRhKCcA&t=523s',
      'video_id': 'mVLtwRhKCcA'},
     {'author': 'Bailey Kramer',
      'channel': 'Bailey Kramer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=DFn2vbuykUY&t=218s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's really two approaches. The first approach is really a passive approach. "
              'Meaning not doing anything. And what will happen then is whenever. Somebody in '
              'your area needs housing. Supposedly the first place that these ALE agents will '
              'look is in their database.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': "There's really two approaches. The first approach is really a passive approach. "
             'Meaning not doing anything. And what will happen then is whenever. Somebody in '
             'your area needs housing. Supposedly the first place that these ALE agents will '
             'look is in their database.',
      'title': 'How To List On ALE Solutions To Secure Insurance Bookings (Bailey Kramer)',
      'url': 'https://www.youtube.com/watch?v=DFn2vbuykUY&t=218s',
      'video_id': 'DFn2vbuykUY'},
     {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
      'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:04](https://www.youtube.com/watch?v=JtRa4_SzshI&t=1744s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I\'m like, "Wait a minute, you\'re thinking the wrong way." If you have it '
              'posted on FurnishFinder, you have it on Airbnb, you have it on all these '
              "platforms, that's our job, right? We're bringing the travelers to this "
              'platform.',
      'timestamp': 1744,
      'timestamp_label': '[00:29:04]',
      'timestamp_seconds': 1744,
      'tip': 'And I\'m like, "Wait a minute, you\'re thinking the wrong way." If you have it '
             'posted on FurnishFinder, you have it on Airbnb, you have it on all these '
             "platforms, that's our job, right? We're bringing the travelers to this platform.",
      'title': 'Airbnb Burnout? The MTR Strategy Every STR Host Needs | Ep. 146 (Landlord '
               'Diaries - The Monthly Rentals Podcast)',
      'url': 'https://www.youtube.com/watch?v=JtRa4_SzshI&t=1744s',
      'video_id': 'JtRa4_SzshI'},
     {'author': 'The Furnished Rental Strategist',
      'channel': 'The Furnished Rental Strategist',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=QgmxJy8KlCc&t=363s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, how do you actually find these tenants? Furnishers is the number one '
              'platform for travel nurses and professionals. Airbnb and VBO with 30-day '
              'minimums are great for insurance and families.',
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': 'So, how do you actually find these tenants? Furnishers is the number one '
             'platform for travel nurses and professionals. Airbnb and VBO with 30-day '
             'minimums are great for insurance and families.',
      'title': 'Furnished Housing for Travel Nurses (and More!) | Mid-Term Rental Demand 2025 '
               '(The Furnished Rental Strategist)',
      'url': 'https://www.youtube.com/watch?v=QgmxJy8KlCc&t=363s',
      'video_id': 'QgmxJy8KlCc'},
     {'author': 'GirlsLikeYou',
      'channel': 'GirlsLikeYou',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:27](https://www.youtube.com/watch?v=j1XiSUq59Jk&t=807s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where where did I stay so using those search engines like I said I used furnish '
              'finders on furnish finders they had houses for rent and they had rooms for rent '
              'I saw houses but since I had decided not to bring my pet I was okay with just '
              'renting a room.',
      'timestamp': 807,
      'timestamp_label': '[00:13:27]',
      'timestamp_seconds': 807,
      'tip': 'Where where did I stay so using those search engines like I said I used furnish '
             'finders on furnish finders they had houses for rent and they had rooms for rent '
             'I saw houses but since I had decided not to bring my pet I was okay with just '
             'renting a room.',
      'title': 'Travel Nurse Housing | Shared Housing Pros/Cons | GirlsLikeYou (GirlsLikeYou)',
      'url': 'https://www.youtube.com/watch?v=j1XiSUq59Jk&t=807s',
      'video_id': 'j1XiSUq59Jk'},
     {'author': 'BNB Fastlane',
      'channel': 'BNB Fastlane',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:32](https://www.youtube.com/watch?v=SGmMixWY7CA&t=632s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're here we want to get you started and get you to this point so you can do "
              "the same so let's get started I'll see you in the next one.",
      'timestamp': 632,
      'timestamp_label': '[00:10:32]',
      'timestamp_seconds': 632,
      'tip': "You're here we want to get you started and get you to this point so you can do "
             "the same so let's get started I'll see you in the next one.",
      'title': "3 BEST Airbnb Business Models Explained (Pro's and Cons) Co-hosting, "
               'Arbitrage, Management Business (BNB Fastlane)',
      'url': 'https://www.youtube.com/watch?v=SGmMixWY7CA&t=632s',
      'video_id': 'SGmMixWY7CA'},
     {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=Z-l9YSGM49I&t=432s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You'd like to connect with John the community and I then go on over to our "
              'Facebook group the host nation talk to your host in the next episode keep on '
              'hosting.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': "You'd like to connect with John the community and I then go on over to our "
             'Facebook group the host nation talk to your host in the next episode keep on '
             'hosting.',
      'title': "Airbnb Rental Arbitrage Contract DO's and DON'TS (Corporate Lease Addendum) "
               '(Short Term Sage - Airbnb, Vacation Rental Host)',
      'url': 'https://www.youtube.com/watch?v=Z-l9YSGM49I&t=432s',
      'video_id': 'Z-l9YSGM49I'},
     {'author': 'Envy Property Management',
      'channel': 'Envy Property Management',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=JoRxVtdO-LA&t=235s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you have any questions about property management or what we can do to help '
              'you increase your return on your investment please give us a call at 801 '
              "337-4337 or visit our website at nvpm.com that's envypm.com for watching guys "
              "we'll see you next.",
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'If you have any questions about property management or what we can do to help '
             'you increase your return on your investment please give us a call at 801 '
             "337-4337 or visit our website at nvpm.com that's envypm.com for watching guys "
             "we'll see you next.",
      'title': 'The Benefits of Tenant Liability Insurance Landlords MUST Know! (Envy Property '
               'Management)',
      'url': 'https://www.youtube.com/watch?v=JoRxVtdO-LA&t=235s',
      'video_id': 'JoRxVtdO-LA'}],
 9: [{'author': 'Jeremy Werden',
      'channel': 'Jeremy Werden',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=kXJgiO6RYaU&t=112s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, the exact terms can vary, but the key thing here is you don't have an "
              "upfront investment. Now, let's break down how much you can make. Let's just say "
              'you rent a two-bedroom apartment for $2,500 a month.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': "So, the exact terms can vary, but the key thing here is you don't have an "
             "upfront investment. Now, let's break down how much you can make. Let's just say "
             'you rent a two-bedroom apartment for $2,500 a month.',
      'title': '6 Brutal Reasons I Quit Airbnb Arbitrage And Switched to Co Hosting (Jeremy '
               'Werden)',
      'url': 'https://www.youtube.com/watch?v=kXJgiO6RYaU&t=112s',
      'video_id': 'kXJgiO6RYaU'},
     {'author': 'Lodge Compliance',
      'channel': 'Lodge Compliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=zQI1CpxOnQ0&t=133s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, Maine has a statewide lodging tax of 9%, while Maryland applies '
              'both state and local lodging taxes. In major cities like Chicago, combined '
              'short-term rental taxes can exceed 21%. Beyond taxes, compliance also includes '
              'federal legal obligations.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': 'For example, Maine has a statewide lodging tax of 9%, while Maryland applies '
             'both state and local lodging taxes. In major cities like Chicago, combined '
             'short-term rental taxes can exceed 21%. Beyond taxes, compliance also includes '
             'federal legal obligations.',
      'title': 'Airbnb Rules in the USA 2026: STR Laws, Taxes, Permits & Regulations Explained '
               '(Lodge Compliance)',
      'url': 'https://www.youtube.com/watch?v=zQI1CpxOnQ0&t=133s',
      'video_id': 'zQI1CpxOnQ0'},
     {'author': 'The Matus Law Group',
      'channel': 'The Matus Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=UPCGK8bIfnU&t=25s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Monmouth County must understand before listing a single night. At the state '
              'level, New Jersey classifies most short-term stays as transient accommodations, '
              'focusing heavily on sales tax and state occupancy fee compliance, rather than '
              'outright banning rentals.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Monmouth County must understand before listing a single night. At the state '
             'level, New Jersey classifies most short-term stays as transient accommodations, '
             'focusing heavily on sales tax and state occupancy fee compliance, rather than '
             'outright banning rentals.',
      'title': "A Legal Guide for Airbnb Hosts: New Jersey's Short-Term Rental Laws by "
               'Christine Matus (The Matus Law Group)',
      'url': 'https://www.youtube.com/watch?v=UPCGK8bIfnU&t=25s',
      'video_id': 'UPCGK8bIfnU'},
     {'author': 'United Policyholders',
      'channel': 'United Policyholders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=bPQqrGrXfiI&t=21s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Known as additional living expense um in the aftermath of a wildfire and we're "
              'going to be focused on the rules as they are in the state of california I will '
              'be one of the speakers today and the other instructor will be sandy watts and '
              'welcome.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Known as additional living expense um in the aftermath of a wildfire and we're "
             'going to be focused on the rules as they are in the state of california I will '
             'be one of the speakers today and the other instructor will be sandy watts and '
             'welcome.',
      'title': '2020_7_23_Insurance Benefits for Temporary/Additional Living Expenses (United '
               'Policyholders)',
      'url': 'https://www.youtube.com/watch?v=bPQqrGrXfiI&t=21s',
      'video_id': 'bPQqrGrXfiI'},
     {'author': 'TurboTenant',
      'channel': 'TurboTenant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=_6CIsjeFw-w&t=173s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Disclosure section may be the most misunderstood part of a lease agreement if '
              'you use a recycled agreement it may not include any new laws your state.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'Disclosure section may be the most misunderstood part of a lease agreement if '
             'you use a recycled agreement it may not include any new laws your state.',
      'title': 'What Landlords MUST Include in Residential Lease Agreements (TurboTenant)',
      'url': 'https://www.youtube.com/watch?v=_6CIsjeFw-w&t=173s',
      'video_id': '_6CIsjeFw-w'},
     {'author': 'The Real Estate Classroom',
      'channel': 'The Real Estate Classroom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=5XzcoZ5NWj4&t=102s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Or in the case where the lease agreement doesn't have any kind of prohibition, "
              'then the tenant is free to do it. Now remember, the relationship here, here are '
              'the legal terms, in this relationship between the landlord and tenant.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': "Or in the case where the lease agreement doesn't have any kind of prohibition, "
             'then the tenant is free to do it. Now remember, the relationship here, here are '
             'the legal terms, in this relationship between the landlord and tenant.',
      'title': 'Assignment of Lease and Subleasing | Real Estate Exam Prep Videos (The Real '
               'Estate Classroom)',
      'url': 'https://www.youtube.com/watch?v=5XzcoZ5NWj4&t=102s',
      'video_id': '5XzcoZ5NWj4'},
     {'author': 'eForms',
      'channel': 'eForms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=5Q9y-UGaIA8&t=32s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And if you'd rather get legal guidance, you can now chat with a licensed "
              'attorney right on our website. What is a lease and can you end it early? A '
              'lease is a contract between a tenant and a landlord for a fixed amount of time.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "And if you'd rather get legal guidance, you can now chat with a licensed "
             'attorney right on our website. What is a lease and can you end it early? A lease '
             'is a contract between a tenant and a landlord for a fixed amount of time.',
      'title': 'Can You Break a Lease Early? Tenant Rights Explained (eForms)',
      'url': 'https://www.youtube.com/watch?v=5Q9y-UGaIA8&t=32s',
      'video_id': '5Q9y-UGaIA8'},
     {'author': 'Mindful Rental Pros',
      'channel': 'Mindful Rental Pros',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:38](https://www.youtube.com/watch?v=rIPWQCsi2z8&t=458s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What about local issues in terms of legality and code and insurance? You have '
              'to check that anyway for any kind of rental. You need to understand what code '
              "is. You need to understand what's legal, and you need to talk to your insurer "
              'about landlord insurance.',
      'timestamp': 458,
      'timestamp_label': '[00:07:38]',
      'timestamp_seconds': 458,
      'tip': 'What about local issues in terms of legality and code and insurance? You have to '
             'check that anyway for any kind of rental. You need to understand what code is. '
             "You need to understand what's legal, and you need to talk to your insurer about "
             'landlord insurance.',
      'title': 'Mid-Term Rentals: How to Get Steady Bookings Without the Turnover (Mindful '
               'Rental Pros)',
      'url': 'https://www.youtube.com/watch?v=rIPWQCsi2z8&t=458s',
      'video_id': 'rIPWQCsi2z8'},
     {'author': 'The Legal Aid Society',
      'channel': 'The Legal Aid Society',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=sIjDgu8Ns9w&t=189s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Writing by disputing it with the credit agency there are many things to '
              'consider and we at the legal aid society are happy to talk you through your '
              'options please visit our website at legalaidnyc.org to get more information.',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': 'Writing by disputing it with the credit agency there are many things to consider '
             'and we at the legal aid society are happy to talk you through your options '
             'please visit our website at legalaidnyc.org to get more information.',
      'title': '5 Things You Need to Know About Breaking Your Lease (The Legal Aid Society)',
      'url': 'https://www.youtube.com/watch?v=sIjDgu8Ns9w&t=189s',
      'video_id': 'sIjDgu8Ns9w'},
     {'author': 'Be A Claims Adjuster',
      'channel': 'Be A Claims Adjuster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=_Odm8IhYr80&t=216s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Al some variables that should be considered include your covered perils '
              'uninhabitable condition reasonable necessity and policy limits it is essential '
              'as a property adjuster that you familiarize yourself with the terms and '
              'conditions of the insurers policy.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'Al some variables that should be considered include your covered perils '
             'uninhabitable condition reasonable necessity and policy limits it is essential '
             'as a property adjuster that you familiarize yourself with the terms and '
             'conditions of the insurers policy.',
      'title': 'Additional Living Expenses (ALE) (Be A Claims Adjuster)',
      'url': 'https://www.youtube.com/watch?v=_Odm8IhYr80&t=216s',
      'video_id': '_Odm8IhYr80'},
     {'author': 'eLeaseAgreement',
      'channel': 'eLeaseAgreement',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=Pgdbie9cCw0&t=68s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Joe renter and this is the person that's coming in new that's going be renting "
              "from Joe renter so we'll just make his name Joe schma this is the street "
              "address of it me 90 Alton Road we'll just say which is our offices down in "
              'Miami in the State of Florida ZIP code.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "Joe renter and this is the person that's coming in new that's going be renting "
             "from Joe renter so we'll just make his name Joe schma this is the street address "
             "of it me 90 Alton Road we'll just say which is our offices down in Miami in the "
             'State of Florida ZIP code.',
      'title': 'How to Fill in Sublease Agreement (eLeaseAgreement)',
      'url': 'https://www.youtube.com/watch?v=Pgdbie9cCw0&t=68s',
      'video_id': 'Pgdbie9cCw0'},
     {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:01](https://www.youtube.com/watch?v=z5rgPmF_Dm4&t=2641s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Need to develop on the sales and because you are selling yourself you're not "
              'buying the property you are selling your concept to them and then they need to '
              'buy from you the contract that so when I understood that for me it was much '
              'easier.',
      'timestamp': 2641,
      'timestamp_label': '[00:44:01]',
      'timestamp_seconds': 2641,
      'tip': "Need to develop on the sales and because you are selling yourself you're not "
             'buying the property you are selling your concept to them and then they need to '
             'buy from you the contract that so when I understood that for me it was much '
             'easier.',
      'title': 'What its like scaling a Rental Arbitrage business in Mexico City w/ Nathan & '
               'Raquel Carillo (Short Term Sage - Airbnb, Vacation Rental Host)',
      'url': 'https://www.youtube.com/watch?v=z5rgPmF_Dm4&t=2641s',
      'video_id': 'z5rgPmF_Dm4'},
     {'author': 'Midterm Rental Consulting',
      'channel': 'Midterm Rental Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=kaZB8y5juss&t=423s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Home and the reason for doing this is because when you put in the filters both '
              'in furnish finder and in Airbnb it allows you to pick for bed and bath '
              'configuration but then it shows you everything.',
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': 'Home and the reason for doing this is because when you put in the filters both '
             'in furnish finder and in Airbnb it allows you to pick for bed and bath '
             'configuration but then it shows you everything.',
      'title': 'Furnished Finder Tips for a Successful Rental (Midterm Rental Consulting)',
      'url': 'https://www.youtube.com/watch?v=kaZB8y5juss&t=423s',
      'video_id': 'kaZB8y5juss'},
     {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
      'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:55](https://www.youtube.com/watch?v=vbHlGVZKjvg&t=775s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Discussing this use case with my mother-in-law the other day and she was like '
              "well we've never gotten placed in a in a home for when something.",
      'timestamp': 775,
      'timestamp_label': '[00:12:55]',
      'timestamp_seconds': 775,
      'tip': 'Discussing this use case with my mother-in-law the other day and she was like '
             "well we've never gotten placed in a in a home for when something.",
      'title': 'The Insurance Housing Blueprint Generating 4x Market Rate Returns w/ Ruben '
               'Kanya | Ep. 114 (Landlord Diaries - The Monthly Rentals Podcast)',
      'url': 'https://www.youtube.com/watch?v=vbHlGVZKjvg&t=775s',
      'video_id': 'vbHlGVZKjvg'},
     {'author': "She's Got Assets",
      'channel': "She's Got Assets",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:48](https://www.youtube.com/watch?v=5Py6jcyyUyA&t=2148s)',
      'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                   'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                   'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mailbox or no mailbox I feel like this is the 5050 thing some people are '
              'adamant absolutely should not allow people to get mail um it provides waterers '
              "right I've heard different different explanations of this I don't think.",
      'timestamp': 2148,
      'timestamp_label': '[00:35:48]',
      'timestamp_seconds': 2148,
      'tip': 'Mailbox or no mailbox I feel like this is the 5050 thing some people are adamant '
             'absolutely should not allow people to get mail um it provides waterers right '
             "I've heard different different explanations of this I don't think.",
      'title': 'Mastering Midterm Rentals Strategies for Disaster Relief Housing w/ Insurance '
               "for Displaced Families (She's Got Assets)",
      'url': 'https://www.youtube.com/watch?v=5Py6jcyyUyA&t=2148s',
      'video_id': '5Py6jcyyUyA'}],
 10: [{'author': 'Vivian Yip',
       'channel': 'Vivian Yip',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=DNkNK6FNKog&t=340s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, we do a little bit of individual business, but it's just not a big piece "
               'of what we do. So, it is a little bit different, per se. And then, we also do '
               'a lot of kind of arbitrage models in the apartment community or the apartment '
               'industry.',
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': "Now, we do a little bit of individual business, but it's just not a big piece "
              'of what we do. So, it is a little bit different, per se. And then, we also do a '
              'lot of kind of arbitrage models in the apartment community or the apartment '
              'industry.',
       'title': 'How Corporate Housing Maintains 95% Occupancy Without Airbnb (Vivian Yip)',
       'url': 'https://www.youtube.com/watch?v=DNkNK6FNKog&t=340s',
       'video_id': 'DNkNK6FNKog'},
      {'author': 'Real Property Management Palisade',
       'channel': 'Real Property Management Palisade',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=aUKpl6xobwU&t=117s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Policies can have surprises there. And if you're building a portfolio, ask "
               'about an umbrella policy. Cheap additional liability protection on top of '
               "everything else. It's one phone call to your insurance agent. The property at "
               'this address is becoming a rental.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "Policies can have surprises there. And if you're building a portfolio, ask "
              'about an umbrella policy. Cheap additional liability protection on top of '
              "everything else. It's one phone call to your insurance agent. The property at "
              'this address is becoming a rental.',
       'title': "Renting Out Your House Your Homeowners Insurance Probably Doesn't Cover It "
                '(Real Property Management Palisade)',
       'url': 'https://www.youtube.com/watch?v=aUKpl6xobwU&t=117s',
       'video_id': 'aUKpl6xobwU'},
      {'author': 'Puyatola',
       'channel': 'Puyatola',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:07](https://www.youtube.com/watch?v=ssQaIBf4KZY&t=487s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sarah rents her apartment John sold his home, but occupancy or rent-back '
               'agreement. John needs to call his insurance agent so they can cancel or '
               'convert his policy appropriately.',
       'timestamp': 487,
       'timestamp_label': '[00:08:07]',
       'timestamp_seconds': 487,
       'tip': 'Sarah rents her apartment John sold his home, but occupancy or rent-back '
              'agreement. John needs to call his insurance agent so they can cancel or convert '
              'his policy appropriately.',
       'title': 'PL 5 - Four Homes, Four Insurance Policies | Homeowners, Renters, Condo, and '
                'Landlord Comparison (Puyatola)',
       'url': 'https://www.youtube.com/watch?v=ssQaIBf4KZY&t=487s',
       'video_id': 'ssQaIBf4KZY'},
      {'author': 'LoCasa',
       'channel': 'LoCasa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:18](https://www.youtube.com/watch?v=OSi_ARPIpaM&t=498s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, that's just a quick caveat for you. But that's why I rented out the spare "
               'bedroom in my Las Vegas apartment. I wanted to see I cleaned all of it myself. '
               "I'm obviously going to delegate that out. I'm having to talk to all of the "
               'guests.',
       'timestamp': 498,
       'timestamp_label': '[00:08:18]',
       'timestamp_seconds': 498,
       'tip': "So, that's just a quick caveat for you. But that's why I rented out the spare "
              'bedroom in my Las Vegas apartment. I wanted to see I cleaned all of it myself. '
              "I'm obviously going to delegate that out. I'm having to talk to all of the "
              'guests.',
       'title': '5 Ways to Scale Airbnb Arbitrage Without a Business Loan | LoCasa (LoCasa)',
       'url': 'https://www.youtube.com/watch?v=OSi_ARPIpaM&t=498s',
       'video_id': 'OSi_ARPIpaM'},
      {'author': 'Short Term Dojo',
       'channel': 'Short Term Dojo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:53](https://www.youtube.com/watch?v=tfwUVSMpB2c&t=653s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's another benefit here where if big-ticket items go bad you're not on the "
               "hook for them financially business taxes i'm not going to go into.",
       'timestamp': 653,
       'timestamp_label': '[00:10:53]',
       'timestamp_seconds': 653,
       'tip': "That's another benefit here where if big-ticket items go bad you're not on the "
              "hook for them financially business taxes i'm not going to go into.",
       'title': 'Running a Short Term Rental though the Master Lease (Arbitrage) model (Short '
                'Term Dojo)',
       'url': 'https://www.youtube.com/watch?v=tfwUVSMpB2c&t=653s',
       'video_id': 'tfwUVSMpB2c'},
      {'author': 'Multiple Streams Queen (Dani Bryant)',
       'channel': 'Multiple Streams Queen (Dani Bryant)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=YHN32S73aOo&t=25s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Personal lease is literally you going as the person "me" Dani, the Multiple '
               'Streams Queen me going and applying for an apartment in my name corporate '
               'lease is you going and applying for an apartment or a place in your business '
               'name.',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': 'Personal lease is literally you going as the person "me" Dani, the Multiple '
              'Streams Queen me going and applying for an apartment in my name corporate lease '
              'is you going and applying for an apartment or a place in your business name.',
       'title': 'How to Get a Corporate Lease for Airbnb? (Multiple Streams Queen (Dani '
                'Bryant))',
       'url': 'https://www.youtube.com/watch?v=YHN32S73aOo&t=25s',
       'video_id': 'YHN32S73aOo'},
      {'author': 'Insurance Savvy',
       'channel': 'Insurance Savvy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:44](https://www.youtube.com/watch?v=Xnrpk3PKFg4&t=224s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your additional living expense coverage limits with your insurance agent you '
               'want to make sure you have enough coverage to maintain your standard of living '
               "if something happens to your home it's also important to update your policy as "
               'your family or housing needs change.',
       'timestamp': 224,
       'timestamp_label': '[00:03:44]',
       'timestamp_seconds': 224,
       'tip': 'Your additional living expense coverage limits with your insurance agent you '
              'want to make sure you have enough coverage to maintain your standard of living '
              "if something happens to your home it's also important to update your policy as "
              'your family or housing needs change.',
       'title': 'Understanding Additional Living Expense Coverage in Homeowners Insurance '
                '(Insurance Savvy)',
       'url': 'https://www.youtube.com/watch?v=Xnrpk3PKFg4&t=224s',
       'video_id': 'Xnrpk3PKFg4'},
      {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=wt5AlXFsjDQ&t=15s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The show is all about creating systems that help you automate your business '
               "give any more time and money freedom if you're ready to start living the.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'The show is all about creating systems that help you automate your business '
              "give any more time and money freedom if you're ready to start living the.",
       'title': 'Rental Arbitrage community questionnaire (pitching landlords, insurance, '
                'objections) (Short Term Sage - Airbnb, Vacation Rental Host)',
       'url': 'https://www.youtube.com/watch?v=wt5AlXFsjDQ&t=15s',
       'video_id': 'wt5AlXFsjDQ'},
      {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
       'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:56](https://www.youtube.com/watch?v=n77MirHjIVo&t=1076s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s Airbnb's version of a rental agreement. Um but we have a rental agreement "
               'for every property and where it changes with the mid-term rental is it becomes '
               "a lease, you know, it's like an actual lease.",
       'timestamp': 1076,
       'timestamp_label': '[00:17:56]',
       'timestamp_seconds': 1076,
       'tip': "'s Airbnb's version of a rental agreement. Um but we have a rental agreement "
              'for every property and where it changes with the mid-term rental is it becomes '
              "a lease, you know, it's like an actual lease.",
       'title': 'STR w/ MTR: The Rental Strategy Making Landlords More Money With Less Work | '
                'Ep. 160 (Landlord Diaries - The Monthly Rentals Podcast)',
       'url': 'https://www.youtube.com/watch?v=n77MirHjIVo&t=1076s',
       'video_id': 'n77MirHjIVo'},
      {'author': '360 BNB Solutions',
       'channel': '360 BNB Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:39](https://www.youtube.com/watch?v=prqw1liLbCM&t=339s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You have the God bless be safe guys put the word Airbnb if you want comments '
               "I'll personally reach out to help you out let's roll.",
       'timestamp': 339,
       'timestamp_label': '[00:05:39]',
       'timestamp_seconds': 339,
       'tip': 'You have the God bless be safe guys put the word Airbnb if you want comments '
              "I'll personally reach out to help you out let's roll.",
       'title': 'Landlords Will Say "YES" To Airbnb Arbitrage If You Say This 1 Thing... (360 '
                'BNB Solutions)',
       'url': 'https://www.youtube.com/watch?v=prqw1liLbCM&t=339s',
       'video_id': 'prqw1liLbCM'},
      {'author': 'Caytlyn Cole Tolliver',
       'channel': 'Caytlyn Cole Tolliver',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:14](https://www.youtube.com/watch?v=ObdxpkrC-yE&t=194s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Policies by any means but this is what I learned from our agent and the '
               'insurance policy that we hold you need to have uh landlord insurance or what '
               'is also.',
       'timestamp': 194,
       'timestamp_label': '[00:03:14]',
       'timestamp_seconds': 194,
       'tip': 'Policies by any means but this is what I learned from our agent and the '
              'insurance policy that we hold you need to have uh landlord insurance or what is '
              'also.',
       'title': "Renting on Furnished Finder | 6 lessons I learned the hard way, so you don't "
                'have to (Caytlyn Cole Tolliver)',
       'url': 'https://www.youtube.com/watch?v=ObdxpkrC-yE&t=194s',
       'video_id': 'ObdxpkrC-yE'},
      {'author': 'Dopazo Insurance',
       'channel': 'Dopazo Insurance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:29](https://www.youtube.com/watch?v=-vWCekxkuSs&t=209s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Understand the differences so you can make your best insurance buying decision '
               "if you don't have an independent insurance agent or you would like a second "
               'opinion please reach out to us at www.dapazoinsurance.com.',
       'timestamp': 209,
       'timestamp_label': '[00:03:29]',
       'timestamp_seconds': 209,
       'tip': 'Understand the differences so you can make your best insurance buying decision '
              "if you don't have an independent insurance agent or you would like a second "
              'opinion please reach out to us at www.dapazoinsurance.com.',
       'title': 'Does General Liability Cover Damage To Rented Premises? (Dopazo Insurance)',
       'url': 'https://www.youtube.com/watch?v=-vWCekxkuSs&t=209s',
       'video_id': '-vWCekxkuSs'},
      {'author': 'The Fearless Investors',
       'channel': 'The Fearless Investors',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:09:13](https://www.youtube.com/watch?v=L48GgPbkHHU&t=4153s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Have a network issue yeah but but yeah overall just you know just a flight '
               "example I'll go ahead jake it looks looks like he's in a rough spot tj if you "
               'want to keep sharing there and then we can uh check him with jay again.',
       'timestamp': 4153,
       'timestamp_label': '[01:09:13]',
       'timestamp_seconds': 4153,
       'tip': 'Have a network issue yeah but but yeah overall just you know just a flight '
              "example I'll go ahead jake it looks looks like he's in a rough spot tj if you "
              'want to keep sharing there and then we can uh check him with jay again.',
       'title': 'Clubhouse: AirBnB Arbitrage vs. Co-Hosting vs. Owning (The Fearless '
                'Investors)',
       'url': 'https://www.youtube.com/watch?v=L48GgPbkHHU&t=4153s',
       'video_id': 'L48GgPbkHHU'},
      {'author': 'Public Adjuster Show with Vince Perri',
       'channel': 'Public Adjuster Show with Vince Perri',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:44:36](https://www.youtube.com/watch?v=UvQF37P1Rn8&t=2676s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's interesting though because there's there's a struggle there right so we "
               "probably could at some point if they're not signing assignment benefits and "
               "you're negotiating those amounts because that's what happens all the time "
               'right but like I honestly.',
       'timestamp': 2676,
       'timestamp_label': '[00:44:36]',
       'timestamp_seconds': 2676,
       'tip': "It's interesting though because there's there's a struggle there right so we "
              "probably could at some point if they're not signing assignment benefits and "
              "you're negotiating those amounts because that's what happens all the time right "
              'but like I honestly.',
       'title': 'The Benefits of Roofers and Public Adjusters Working Together - David Dube - '
                'Claims Game Podcast 034 (Public Adjuster Show with Vince Perri)',
       'url': 'https://www.youtube.com/watch?v=UvQF37P1Rn8&t=2676s',
       'video_id': 'UvQF37P1Rn8'},
      {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:48](https://www.youtube.com/watch?v=roqaSiCOnsI&t=948s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Show if you'd like to connect with John the community and I then go on over to "
               'our Facebook group the host nation talk to your host in the next episode keep '
               'on hosting.',
       'timestamp': 948,
       'timestamp_label': '[00:15:48]',
       'timestamp_seconds': 948,
       'tip': "Show if you'd like to connect with John the community and I then go on over to "
              'our Facebook group the host nation talk to your host in the next episode keep '
              'on hosting.',
       'title': 'What is Rental Arbitrage vs Cohosting vs BRRRR vs Turnkey (Short Term Sage - '
                'Airbnb, Vacation Rental Host)',
       'url': 'https://www.youtube.com/watch?v=roqaSiCOnsI&t=948s',
       'video_id': 'roqaSiCOnsI'}],
 11: [{'author': 'Richie Matthews',
       'channel': 'Richie Matthews',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:16](https://www.youtube.com/watch?v=VtVf0h80q0w&t=256s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I was still very skeptical about this whole business model. Here are the '
               'principles for how I would recommend that you do all that without hiring a '
               'property manager and without doing the work yourself. So step one is the day '
               'you sign your lease, hire a virtual assistant.',
       'timestamp': 256,
       'timestamp_label': '[00:04:16]',
       'timestamp_seconds': 256,
       'tip': 'I was still very skeptical about this whole business model. Here are the '
              'principles for how I would recommend that you do all that without hiring a '
              'property manager and without doing the work yourself. So step one is the day '
              'you sign your lease, hire a virtual assistant.',
       'title': 'Rental Arbitrage Has Changed — Use This New System (Richie Matthews)',
       'url': 'https://www.youtube.com/watch?v=VtVf0h80q0w&t=256s',
       'video_id': 'VtVf0h80q0w'},
      {'author': 'Vicsmanor',
       'channel': 'Vicsmanor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:31](https://www.youtube.com/watch?v=obnSO0EuoMk&t=1531s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Well, I spent 28 years in executive level management. I I I was I was a and I '
               'was a I was a project manager. I managed cross functional teams. I built my '
               'own teams as a manager and director. So, I you know, building a team was never '
               'really a problem.',
       'timestamp': 1531,
       'timestamp_label': '[00:25:31]',
       'timestamp_seconds': 1531,
       'tip': 'Well, I spent 28 years in executive level management. I I I was I was a and I '
              'was a I was a project manager. I managed cross functional teams. I built my own '
              'teams as a manager and director. So, I you know, building a team was never '
              'really a problem.',
       'title': 'How Brian Biernat Scaled to 15+ Rentals with Rental Arbitrage | Quit His '
                '6-Figure Job (Vicsmanor)',
       'url': 'https://www.youtube.com/watch?v=obnSO0EuoMk&t=1531s',
       'video_id': 'obnSO0EuoMk'},
      {'author': 'Jorge Garcia | Roadmap Lodging',
       'channel': 'Jorge Garcia | Roadmap Lodging',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:12](https://www.youtube.com/watch?v=Ewazlh6zOLM&t=252s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Building demand first gives you freedom. You just need five great '
               'relationships that feed you steady contracts with systems, automation, '
               'templates, standardized setups. You can scale without stress.',
       'timestamp': 252,
       'timestamp_label': '[00:04:12]',
       'timestamp_seconds': 252,
       'tip': 'Building demand first gives you freedom. You just need five great relationships '
              'that feed you steady contracts with systems, automation, templates, '
              'standardized setups. You can scale without stress.',
       'title': 'I Built My Corporate Housing Business Backwards (On Purpose) (Jorge Garcia | '
                'Roadmap Lodging)',
       'url': 'https://www.youtube.com/watch?v=Ewazlh6zOLM&t=252s',
       'video_id': 'Ewazlh6zOLM'},
      {'author': 'Short Term Sage - Airbnb, Vacation Rental Host',
       'channel': 'Short Term Sage - Airbnb, Vacation Rental Host',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:20](https://www.youtube.com/watch?v=Y2Nj2IYzw-Q&t=800s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Could be a profitable business what I'm doing he's very business savvy he told "
               'me that you know it can scale and I said hmm I spoke to a couple brokers I '
               'spoke.',
       'timestamp': 800,
       'timestamp_label': '[00:13:20]',
       'timestamp_seconds': 800,
       'tip': "Could be a profitable business what I'm doing he's very business savvy he told "
              'me that you know it can scale and I said hmm I spoke to a couple brokers I '
              'spoke.',
       'title': 'How to manage and build Rental Arbitrage properties remotely w/ Farhan Abbasi '
                '(Short Term Sage - Airbnb, Vacation Rental Host)',
       'url': 'https://www.youtube.com/watch?v=Y2Nj2IYzw-Q&t=800s',
       'video_id': 'Y2Nj2IYzw-Q'},
      {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
       'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:05](https://www.youtube.com/watch?v=mOvanxNbxWw&t=365s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The logistics the the simple things um I've got a really good team team there "
               'yeah self-managing Arbitrage with Furniture finder is incredibly simple I.',
       'timestamp': 365,
       'timestamp_label': '[00:06:05]',
       'timestamp_seconds': 365,
       'tip': "The logistics the the simple things um I've got a really good team team there "
              'yeah self-managing Arbitrage with Furniture finder is incredibly simple I.',
       'title': 'Gain Back Your Time | Start A Mid-Term Rental Arbitrage Business Today! | Ep. '
                '131 (Landlord Diaries - The Monthly Rentals Podcast)',
       'url': 'https://www.youtube.com/watch?v=mOvanxNbxWw&t=365s',
       'video_id': 'mOvanxNbxWw'},
      {'author': 'AvenueWest Managed Corporate Housing',
       'channel': 'AvenueWest Managed Corporate Housing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=g7utkw_SRk4&t=109s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You're looking for whether you need a studio apartment in the city or a "
               'three-bedroom home in the suburbs corporate housing providers are.',
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': "You're looking for whether you need a studio apartment in the city or a "
              'three-bedroom home in the suburbs corporate housing providers are.',
       'title': 'What is Corporate Housing - The 30 Day Stay (AvenueWest Managed Corporate '
                'Housing)',
       'url': 'https://www.youtube.com/watch?v=g7utkw_SRk4&t=109s',
       'video_id': 'g7utkw_SRk4'},
      {'author': 'Sedgwick',
       'channel': 'Sedgwick',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=QuVIeGSvUpw&t=15s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Team whether they need accommodations during an emergency evacuation '
               'immediately after a storm a fire or water damage or to remediate damages say.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Team whether they need accommodations during an emergency evacuation '
              'immediately after a storm a fire or water damage or to remediate damages say.',
       'title': 'Sedgwick Temporary Housing (Sedgwick)',
       'url': 'https://www.youtube.com/watch?v=QuVIeGSvUpw&t=15s',
       'video_id': 'QuVIeGSvUpw'},
      {'author': 'Short Term Rental Secrets',
       'channel': 'Short Term Rental Secrets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:41](https://www.youtube.com/watch?v=etWVAe5zZDc&t=1661s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You may be rewarded for being a professional. You may be rewarded for having '
               "more reviews in a way that helps you if you're on page three of Vrbo or Airbnb "
               'get noticed earlier, but the booking may still be likely to point at Vrbo or '
               'Airbnb.',
       'timestamp': 1661,
       'timestamp_label': '[00:27:41]',
       'timestamp_seconds': 1661,
       'tip': 'You may be rewarded for being a professional. You may be rewarded for having '
              "more reviews in a way that helps you if you're on page three of Vrbo or Airbnb "
              'get noticed earlier, but the booking may still be likely to point at Vrbo or '
              'Airbnb.',
       'title': 'Midterm Rentals Booming: Demand +30%, Supply +10%. Should You Jump In? '
                'Ex-Vrbo President Answers (Short Term Rental Secrets)',
       'url': 'https://www.youtube.com/watch?v=etWVAe5zZDc&t=1661s',
       'video_id': 'etWVAe5zZDc'},
      {'author': 'Jesse Vasquez',
       'channel': 'Jesse Vasquez',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:54](https://www.youtube.com/watch?v=Ncr7TdF1G34&t=354s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Grabbing data that's in our backyards it's on google for free connecting with "
               "these agencies and we're talking about building a sustainable viable business.",
       'timestamp': 354,
       'timestamp_label': '[00:05:54]',
       'timestamp_seconds': 354,
       'tip': "Grabbing data that's in our backyards it's on google for free connecting with "
              "these agencies and we're talking about building a sustainable viable business.",
       'title': "The BEST Mid Term Rental Strategy You Probably Aren't Using | Insurance "
                'Relocation Claims (Jesse Vasquez)',
       'url': 'https://www.youtube.com/watch?v=Ncr7TdF1G34&t=354s',
       'video_id': 'Ncr7TdF1G34'},
      {'author': 'Beau Eckstein, Business Ownership Coach',
       'channel': 'Beau Eckstein, Business Ownership Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:29](https://www.youtube.com/watch?v=GFTAQzCp4aM&t=929s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Available like airb like Arbitrage you don't need much money you just need the "
               'skill sets to do it right and you just kind of stumbled into it and learned '
               'and then taught yourself and kind of grew it which is it was just a cool '
               'story.',
       'timestamp': 929,
       'timestamp_label': '[00:15:29]',
       'timestamp_seconds': 929,
       'tip': "Available like airb like Arbitrage you don't need much money you just need the "
              'skill sets to do it right and you just kind of stumbled into it and learned and '
              'then taught yourself and kind of grew it which is it was just a cool story.',
       'title': 'Maximizing Profits with Rental Arbitrage on Airbnb and VRBO (Beau Eckstein, '
                'Business Ownership Coach)',
       'url': 'https://www.youtube.com/watch?v=GFTAQzCp4aM&t=929s',
       'video_id': 'GFTAQzCp4aM'},
      {'author': 'Furnished Finder',
       'channel': 'Furnished Finder',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=Xove5nsUtbI&t=99s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Safe and protected contacting the owners of the apartments that I was trying '
               "to and this just worked out perfect for me so I love it for the eaves I'd use "
               'it.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': 'Safe and protected contacting the owners of the apartments that I was trying to '
              "and this just worked out perfect for me so I love it for the eaves I'd use it.",
       'title': 'Conversations with Travel Nurses by Furnished Finder - Patrick Ales '
                '(Furnished Finder)',
       'url': 'https://www.youtube.com/watch?v=Xove5nsUtbI&t=99s',
       'video_id': 'Xove5nsUtbI'},
      {'author': 'Footy 90 Soccer',
       'channel': 'Footy 90 Soccer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:59](https://www.youtube.com/watch?v=uaSsC0pAd-8&t=479s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Can handle everything from tenant screening and communication to rent '
               'collection and Property Maintenance this allows you to step back from the '
               'day-to-day operations and focus on growing your portfolio and enjoying the '
               'fruits of your passive.',
       'timestamp': 479,
       'timestamp_label': '[00:07:59]',
       'timestamp_seconds': 479,
       'tip': 'Can handle everything from tenant screening and communication to rent '
              'collection and Property Maintenance this allows you to step back from the '
              'day-to-day operations and focus on growing your portfolio and enjoying the '
              'fruits of your passive.',
       'title': 'How I Made $100,000 in Passive Income from Corporate Housing (Footy 90 '
                'Soccer)',
       'url': 'https://www.youtube.com/watch?v=uaSsC0pAd-8&t=479s',
       'video_id': 'uaSsC0pAd-8'},
      {'author': 'Midterm Rental Consulting',
       'channel': 'Midterm Rental Consulting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:45](https://www.youtube.com/watch?v=r-8W10XEuGg&t=165s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "All you pay and it's a Marketplace like Facebook because it's just a listing "
               "but there's not a lot of technology behind it whereas Airbnb it takes three "
               "percent and then there's all this technology.",
       'timestamp': 165,
       'timestamp_label': '[00:02:45]',
       'timestamp_seconds': 165,
       'tip': "All you pay and it's a Marketplace like Facebook because it's just a listing "
              "but there's not a lot of technology behind it whereas Airbnb it takes three "
              "percent and then there's all this technology.",
       'title': 'Furnished Finder FAQs - 5 Most Asked Questions (Midterm Rental Consulting)',
       'url': 'https://www.youtube.com/watch?v=r-8W10XEuGg&t=165s',
       'video_id': 'r-8W10XEuGg'},
      {'author': 'Vetted Homes',
       'channel': 'Vetted Homes',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=XVJjiJc_2mM&t=71s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Representative is it makes them feel like they are making my job so easy I'm "
               'not having to sit here and explain why and follow up and send them material '
               "and tell them to go to our website and they're just like rock and roll.",
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': "Representative is it makes them feel like they are making my job so easy I'm "
              'not having to sit here and explain why and follow up and send them material and '
              "tell them to go to our website and they're just like rock and roll.",
       'title': 'Get Your Home Booked FIRST: How to Win Over Insurance Companies for Mid-Term '
                'Rentals! (Vetted Homes)',
       'url': 'https://www.youtube.com/watch?v=XVJjiJc_2mM&t=71s',
       'video_id': 'XVJjiJc_2mM'},
      {'author': 'Rafa Loza',
       'channel': 'Rafa Loza',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:20](https://www.youtube.com/watch?v=894g1JF-IuM&t=1520s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You know, at 15,000 to 20,000 per per property, you can afford to hire a local '
               'property manager, cleaning crew, handyman still profit significantly. But the '
               'problem is that in those heavy vacation rental markets, finding a property to '
               'arbitrage is pretty freaking difficult.',
       'timestamp': 1520,
       'timestamp_label': '[00:25:20]',
       'timestamp_seconds': 1520,
       'tip': 'You know, at 15,000 to 20,000 per per property, you can afford to hire a local '
              'property manager, cleaning crew, handyman still profit significantly. But the '
              'problem is that in those heavy vacation rental markets, finding a property to '
              'arbitrage is pretty freaking difficult.',
       'title': 'How To Start An Airbnb Business Without Owning Property (Part 1 of 3) (Rafa '
                'Loza)',
       'url': 'https://www.youtube.com/watch?v=894g1JF-IuM&t=1520s',
       'video_id': '894g1JF-IuM'}],
 12: [{'author': 'Bailey Kramer',
       'channel': 'Bailey Kramer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:05](https://www.youtube.com/watch?v=Fz00u2_mgqE&t=245s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Is that the simplest way to explain it is let's just say you have a four week "
               "booking here, then you have a seven night gap and then you have another, let's "
               'say a three month booking here. That gap in between the bookings is called an '
               'orphan day gap.',
       'timestamp': 245,
       'timestamp_label': '[00:04:05]',
       'timestamp_seconds': 245,
       'tip': "Is that the simplest way to explain it is let's just say you have a four week "
              "booking here, then you have a seven night gap and then you have another, let's "
              'say a three month booking here. That gap in between the bookings is called an '
              'orphan day gap.',
       'title': 'Mid Term Rental Pricing Strategy: Revealed (Bailey Kramer)',
       'url': 'https://www.youtube.com/watch?v=Fz00u2_mgqE&t=245s',
       'video_id': 'Fz00u2_mgqE'},
      {'author': 'Restart Tax Talk',
       'channel': 'Restart Tax Talk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:05](https://www.youtube.com/watch?v=SpF7mXFixD8&t=245s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And forgetting the personal days, including the week you gave your sister. '
               'From the former IRS revenue agent behind this channel: the calendar decides '
               'this one. Export your booking history; it shows the average stay, the rented '
               'days, and the blocked days.',
       'timestamp': 245,
       'timestamp_label': '[00:04:05]',
       'timestamp_seconds': 245,
       'tip': 'And forgetting the personal days, including the week you gave your sister. From '
              'the former IRS revenue agent behind this channel: the calendar decides this '
              'one. Export your booking history; it shows the average stay, the rented days, '
              'and the blocked days.',
       'title': 'R-3 | Airbnb Taxes 2026: Landlord, Business or Hotel? (14-Day Rule, 7-Day '
                'Rule, Schedule E or C) (Restart Tax Talk)',
       'url': 'https://www.youtube.com/watch?v=SpF7mXFixD8&t=245s',
       'video_id': 'SpF7mXFixD8'},
      {'author': 'Multiple Streams Queen (Dani Bryant)',
       'channel': 'Multiple Streams Queen (Dani Bryant)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=jD3cHooRd3k&t=15s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'People ask how do I start for one how to get started you need to have a '
               'business I do the business model rental Arbitrage we do not do.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'People ask how do I start for one how to get started you need to have a '
              'business I do the business model rental Arbitrage we do not do.',
       'title': 'How to start corporate lease - Airbnb Superhost (Multiple Streams Queen (Dani '
                'Bryant))',
       'url': 'https://www.youtube.com/watch?v=jD3cHooRd3k&t=15s',
       'video_id': 'jD3cHooRd3k'},
      {'author': 'Brittany Janae',
       'channel': 'Brittany Janae',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:50](https://www.youtube.com/watch?v=M846PBAG924&t=170s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Want to take a little break away from Airbnb so the first person that I had '
               'say um that was for a three-month clinical.',
       'timestamp': 170,
       'timestamp_label': '[00:02:50]',
       'timestamp_seconds': 170,
       'tip': 'Want to take a little break away from Airbnb so the first person that I had say '
              'um that was for a three-month clinical.',
       'title': 'Renting for Travel Nurses: The Ultimate Guide for Landlords| My Experience '
                'Using Furnished Finders (Brittany Janae)',
       'url': 'https://www.youtube.com/watch?v=M846PBAG924&t=170s',
       'video_id': 'M846PBAG924'},
      {'author': "Adulting Shouldn't Suck",
       'channel': "Adulting Shouldn't Suck",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:42](https://www.youtube.com/watch?v=07RfH5S46pg&t=462s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Any consequences once the landlord receives the notice the lease will end in '
               '30 days or at the end of the month so if you need to break a lease and you.',
       'timestamp': 462,
       'timestamp_label': '[00:07:42]',
       'timestamp_seconds': 462,
       'tip': 'Any consequences once the landlord receives the notice the lease will end in 30 '
              'days or at the end of the month so if you need to break a lease and you.',
       'title': 'How To Break Your Lease | Get Out Of Your Lease With No Penalty (Adulting '
                "Shouldn't Suck)",
       'url': 'https://www.youtube.com/watch?v=07RfH5S46pg&t=462s',
       'video_id': '07RfH5S46pg'},
      {'author': 'Adam James Speaks',
       'channel': 'Adam James Speaks',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:24](https://www.youtube.com/watch?v=AxwgX6EuFNc&t=1644s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s put a plan together, let's do it. If there's some things that need to have "
               "deferred maintenance, let's say hold off or put a plan in place to do that in "
               'the future, right? Once we start getting some income generated.',
       'timestamp': 1644,
       'timestamp_label': '[00:27:24]',
       'timestamp_seconds': 1644,
       'tip': "'s put a plan together, let's do it. If there's some things that need to have "
              "deferred maintenance, let's say hold off or put a plan in place to do that in "
              'the future, right? Once we start getting some income generated.',
       'title': 'No Property? No Problem: How to Master Rental Arbitrage (Adam James Speaks)',
       'url': 'https://www.youtube.com/watch?v=AxwgX6EuFNc&t=1644s',
       'video_id': 'AxwgX6EuFNc'},
      {'author': 'Business Guide',
       'channel': 'Business Guide',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=gO0LLG_9nSA&t=187s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A one-time thing or premium trial if you need to create more legal forms and '
               "also I mean one dollar for seven days it's nothing and it's way way more "
               "comfortable that's about it guys thanks for watching and see you in the next "
               'one have a great day and goodbye.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': 'A one-time thing or premium trial if you need to create more legal forms and '
              "also I mean one dollar for seven days it's nothing and it's way way more "
              "comfortable that's about it guys thanks for watching and see you in the next "
              'one have a great day and goodbye.',
       'title': 'Tenant Sublease Agreement Template - How To Fill Tenant Sublease Agreement '
                '(Business Guide)',
       'url': 'https://www.youtube.com/watch?v=gO0LLG_9nSA&t=187s',
       'video_id': 'gO0LLG_9nSA'},
      {'author': 'Landlord Diaries - The Monthly Rentals Podcast',
       'channel': 'Landlord Diaries - The Monthly Rentals Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:35](https://www.youtube.com/watch?v=yo5DDACarw0&t=755s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "As you know the 401K is a 30 50 year plan who won that I mean We're Not Gonna "
               'Be Alive then yeah right and then yeah and then most any kind of business out.',
       'timestamp': 755,
       'timestamp_label': '[00:12:35]',
       'timestamp_seconds': 755,
       'tip': "As you know the 401K is a 30 50 year plan who won that I mean We're Not Gonna "
              'Be Alive then yeah right and then yeah and then most any kind of business out.',
       'title': 'FF59 Dr. Chau’s Method: Cashflow $10-20k/Month in 90 Days with the '
                'MTR/Corporate Housing Strategy (Landlord Diaries - The Monthly Rentals '
                'Podcast)',
       'url': 'https://www.youtube.com/watch?v=yo5DDACarw0&t=755s',
       'video_id': 'yo5DDACarw0'},
      {'author': 'Think Insurance',
       'channel': 'Think Insurance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:35](https://www.youtube.com/watch?v=zqIy396b0ac&t=275s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Then you have whatever your limit there is and you can still survive without '
               "having to out pocket money that you didn't plan on month to month and that's.",
       'timestamp': 275,
       'timestamp_label': '[00:04:35]',
       'timestamp_seconds': 275,
       'tip': 'Then you have whatever your limit there is and you can still survive without '
              "having to out pocket money that you didn't plan on month to month and that's.",
       'title': 'Why you need a renters liability policy (Think Insurance)',
       'url': 'https://www.youtube.com/watch?v=zqIy396b0ac&t=275s',
       'video_id': 'zqIy396b0ac'},
      {'author': 'Gng. Jackson',
       'channel': 'Gng. Jackson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:20](https://www.youtube.com/watch?v=hp6VgBcT7YQ&t=140s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Kitchen so they have prepared all of this for us it is actually complete first '
               "pens everything that we will need for for a month okay I'll show you the "
               "master's bedroom.",
       'timestamp': 140,
       'timestamp_label': '[00:02:20]',
       'timestamp_seconds': 140,
       'tip': 'Kitchen so they have prepared all of this for us it is actually complete first '
              "pens everything that we will need for for a month okay I'll show you the "
              "master's bedroom.",
       'title': 'TEMPORARY CORPORATE HOUSING TOUR |  | SHORT TERM RENTAL |SHORT TERM SAGE '
                '(Gng. Jackson)',
       'url': 'https://www.youtube.com/watch?v=hp6VgBcT7YQ&t=140s',
       'video_id': 'hp6VgBcT7YQ'},
      {'author': 'Driven Saver',
       'channel': 'Driven Saver',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:15](https://www.youtube.com/watch?v=uCQYAZ1ws_w&t=375s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This helps just a little bit with a le and once again not probably the thing '
               'that I figured out the most but hopefully it helps a little bit and I hope '
               "that you have a great day and I'll see you soon with another video bye.",
       'timestamp': 375,
       'timestamp_label': '[00:06:15]',
       'timestamp_seconds': 375,
       'tip': 'This helps just a little bit with a le and once again not probably the thing '
              'that I figured out the most but hopefully it helps a little bit and I hope that '
              "you have a great day and I'll see you soon with another video bye.",
       'title': 'ALE (Additional Living Expenses) after a major insurance claim (Driven Saver)',
       'url': 'https://www.youtube.com/watch?v=uCQYAZ1ws_w&t=375s',
       'video_id': 'uCQYAZ1ws_w'},
      {'author': 'Hannigan Insurance Agency',
       'channel': 'Hannigan Insurance Agency',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:55](https://www.youtube.com/watch?v=aGvo7Dq3gTM&t=175s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It happen in 17 years people try and fool the insurance company it always '
               "bites them in the ass right seamus I hear you so don't do that get the proper "
               "coverage on your home this is brian hannigan we'll see you on day 27.",
       'timestamp': 175,
       'timestamp_label': '[00:02:55]',
       'timestamp_seconds': 175,
       'tip': 'It happen in 17 years people try and fool the insurance company it always bites '
              "them in the ass right seamus I hear you so don't do that get the proper "
              "coverage on your home this is brian hannigan we'll see you on day 27.",
       'title': 'Do I Need Landlord Insurance When Renting Out My House? (Hannigan Insurance '
                'Agency)',
       'url': 'https://www.youtube.com/watch?v=aGvo7Dq3gTM&t=175s',
       'video_id': 'aGvo7Dq3gTM'},
      {'author': 'Jacob and Elissa',
       'channel': 'Jacob and Elissa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:27](https://www.youtube.com/watch?v=ZoPbBZvfW94&t=627s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Have to continuously answer questions to troubleshoot things and then also '
               "make sure everyone's happy at the end of the day and people keep coming back "
               'to stay your properties.',
       'timestamp': 627,
       'timestamp_label': '[00:10:27]',
       'timestamp_seconds': 627,
       'tip': 'Have to continuously answer questions to troubleshoot things and then also make '
              "sure everyone's happy at the end of the day and people keep coming back to stay "
              'your properties.',
       'title': 'Understanding Security Deposits and Damage Waivers for Short-Term Rentals '
                '(Jacob and Elissa)',
       'url': 'https://www.youtube.com/watch?v=ZoPbBZvfW94&t=627s',
       'video_id': 'ZoPbBZvfW94'},
      {'author': 'Crowley Insurance Agency, Inc',
       'channel': 'Crowley Insurance Agency, Inc',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:32](https://www.youtube.com/watch?v=TkI2Qak3r34&t=212s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Coverage that's built into your homeowners policy if you've got any questions "
               'regarding this coverage or any parts of your home policy feel free to reach '
               "out we appreciate you watching and we'll see you again soon.",
       'timestamp': 212,
       'timestamp_label': '[00:03:32]',
       'timestamp_seconds': 212,
       'tip': "Coverage that's built into your homeowners policy if you've got any questions "
              'regarding this coverage or any parts of your home policy feel free to reach out '
              "we appreciate you watching and we'll see you again soon.",
       'title': "What is Loss of Use Coverage on your Homeowner's Insurance? (Crowley "
                'Insurance Agency, Inc)',
       'url': 'https://www.youtube.com/watch?v=TkI2Qak3r34&t=212s',
       'video_id': 'TkI2Qak3r34'},
      {'author': 'LoCasa',
       'channel': 'LoCasa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:58](https://www.youtube.com/watch?v=VFt0XueZxpE&t=178s)',
       'relevance': 'Attributed practitioner commentary on carrier-paid Insurance Additional '
                    'Living Expense (`ALE`) displaced-policyholder placements, corporate '
                    'master-leases, and 30-to-270-day relocation housing arbitrage (Chapter '
                    'Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "1 day to a week to 3 weeks or over a month. It's totally up to your "
               'discretion, but you have to understand, many leases ban hotel-like stays. You '
               'need explicit permission for guest stays under 30 days. And of course, like I '
               'just said, why it matters.',
       'timestamp': 178,
       'timestamp_label': '[00:02:58]',
       'timestamp_seconds': 178,
       'tip': "1 day to a week to 3 weeks or over a month. It's totally up to your discretion, "
              'but you have to understand, many leases ban hotel-like stays. You need explicit '
              'permission for guest stays under 30 days. And of course, like I just said, why '
              'it matters.',
       'title': 'Airbnb Arbitrage Lease Addendum: Must-Have Clauses to Protect Your Business | '
                'LoCasa (LoCasa)',
       'url': 'https://www.youtube.com/watch?v=VFt0XueZxpE&t=178s',
       'video_id': 'VFt0XueZxpE'}]}
