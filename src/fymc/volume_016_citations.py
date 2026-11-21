"""Curated 180-citation Probate Real Estate baseline (15 per chapter across Q1-Q12) mined strictly from verified Probate Real Estate YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'cleanout',
     'client',
     'clients',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'direct',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'budget',
     'building',
     'business',
     'buyer',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'cleanout',
     'concierge',
     'confirmation',
     'contract',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'customer',
     'decision',
     'direct',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'cashflow',
     'certified',
     'chad',
     'cleanout',
     'commission',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'cost',
     'costs',
     'county',
     'court',
     'cpres',
     'direct',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'budget',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'cleanout',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'direct',
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
 5: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'audit',
     'authority',
     'avoid',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'clawback',
     'cleanout',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'direct',
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
 6: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'cleanout',
     'client',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'data',
     'deal',
     'direct',
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
 7: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'checklist',
     'cleanout',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'delivery',
     'direct',
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
 8: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'all',
     'api',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'cleanout',
     'concierge',
     'confirmation',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'crm',
     'data',
     'database',
     'direct',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'1014',
     'act',
     'administration',
     'advance',
     'agency',
     'agreement',
     'all',
     'assisted',
     'attorney',
     'auction',
     'authority',
     'basis',
     'building',
     'business',
     'buyout',
     'california',
     'calling',
     'campaign',
     'capital',
     'cash',
     'certified',
     'chad',
     'cleanout',
     'compliance',
     'concierge',
     'confirmation',
     'contract',
     'coordination',
     'corbett',
     'county',
     'court',
     'cpres',
     'direct',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'1014',
      'act',
      'administration',
      'advance',
      'agency',
      'agent',
      'ai',
      'all',
      'assisted',
      'attorney',
      'auction',
      'authority',
      'automate',
      'automation',
      'basis',
      'building',
      'business',
      'buyout',
      'california',
      'calling',
      'campaign',
      'capital',
      'cash',
      'certified',
      'chad',
      'cleanout',
      'concierge',
      'confirmation',
      'coordination',
      'corbett',
      'county',
      'court',
      'cpres',
      'dashboard',
      'direct',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'1014',
      'act',
      'administration',
      'advance',
      'agency',
      'all',
      'assisted',
      'attorney',
      'auction',
      'authority',
      'basis',
      'building',
      'business',
      'buyout',
      'california',
      'calling',
      'campaign',
      'capital',
      'cash',
      'certified',
      'chad',
      'cleanout',
      'concierge',
      'confirmation',
      'contractor',
      'coordination',
      'corbett',
      'county',
      'court',
      'cpres',
      'direct',
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
 12: {'1014',
      'act',
      'action',
      'administration',
      'advance',
      'agency',
      'all',
      'assisted',
      'attorney',
      'auction',
      'authority',
      'basis',
      'building',
      'business',
      'buyout',
      'california',
      'calling',
      'campaign',
      'capital',
      'cash',
      'certified',
      'chad',
      'cleanout',
      'concierge',
      'confirmation',
      'coordination',
      'corbett',
      'county',
      'court',
      'cpres',
      'day',
      'days',
      'direct',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Matt McGilvray',
      'channel': 'Matt McGilvray',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=fi8ZbbtnVgM&t=179s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s real estate market or what we should list it for. And not every probate sale "
              'requires court confirmation. Many personal representatives have full authority '
              'under the Independent Administration of Estates Act, allowing them to sell '
              'without a confirmation hearing.',
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': "'s real estate market or what we should list it for. And not every probate sale "
             'requires court confirmation. Many personal representatives have full authority '
             'under the Independent Administration of Estates Act, allowing them to sell '
             'without a confirmation hearing.',
      'title': 'How Do You Determine the Right Asking Price for a Probate Property? | '
               'California Probate (Matt McGilvray)',
      'url': 'https://www.youtube.com/watch?v=fi8ZbbtnVgM&t=179s',
      'video_id': 'fi8ZbbtnVgM'},
     {'author': 'Finance Brief',
      'channel': 'Finance Brief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:53](https://www.youtube.com/watch?v=LPs1XDGVnWs&t=1133s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each owned property has its own expenses, mortgage payments, capital '
              "improvement needs, and performance. The owner should not confuse the company's "
              'total revenue with its actual profit or assume that the market value of its '
              'properties represents available cash.',
      'timestamp': 1133,
      'timestamp_label': '[00:18:53]',
      'timestamp_seconds': 1133,
      'tip': 'Each owned property has its own expenses, mortgage payments, capital improvement '
             "needs, and performance. The owner should not confuse the company's total revenue "
             'with its actual profit or assume that the market value of its properties '
             'represents available cash.',
      'title': 'The Economics of Owning a Real Estate Business #usa (Finance Brief)',
      'url': 'https://www.youtube.com/watch?v=LPs1XDGVnWs&t=1133s',
      'video_id': 'LPs1XDGVnWs'},
     {'author': 'BizMove',
      'channel': 'BizMove',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=ouKH71PUV3E&t=203s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Remember that the estate sale business requires adaptability and a commitment '
              'to providing value to your clients and customers. Building a strong reputation '
              'takes time, so be patient and stay dedicated to delivering quality services.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'Remember that the estate sale business requires adaptability and a commitment to '
             'providing value to your clients and customers. Building a strong reputation '
             'takes time, so be patient and stay dedicated to delivering quality services.',
      'title': 'Starting an Estate Sale Business Tips | Free Estate Sale Business Plan '
               'Template Included (BizMove)',
      'url': 'https://www.youtube.com/watch?v=ouKH71PUV3E&t=203s',
      'video_id': 'ouKH71PUV3E'},
     {'author': 'PRINTgenie',
      'channel': 'PRINTgenie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:07](https://www.youtube.com/watch?v=FfQ1DIK5kHE&t=2287s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm not devaluating our product but it is a tire kicker. But the real value is "
              "all they have to to do is scan that QR code. They don't have to fill out "
              "anything. They don't even have to look at it. But the act of scanning it will "
              'then notify you on your phone.',
      'timestamp': 2287,
      'timestamp_label': '[00:38:07]',
      'timestamp_seconds': 2287,
      'tip': "I'm not devaluating our product but it is a tire kicker. But the real value is "
             "all they have to to do is scan that QR code. They don't have to fill out "
             "anything. They don't even have to look at it. But the act of scanning it will "
             'then notify you on your phone.',
      'title': 'Consumer Title Automates Direct Mail Marketing with Title ToolBox + PRINTgenie '
               '| No Minimums (PRINTgenie)',
      'url': 'https://www.youtube.com/watch?v=FfQ1DIK5kHE&t=2287s',
      'video_id': 'FfQ1DIK5kHE'},
     {'author': 'Darcel Lobo',
      'channel': 'Darcel Lobo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=wQcPBrtGgYY&t=22s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's why this niche is exploding. And let's not also forget that estate "
              'planning can be one of the most profitable and lifestylefriendly practice '
              "areas. No court dates, predictable clients, and usually you're charging flat "
              'fees.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "And that's why this niche is exploding. And let's not also forget that estate "
             'planning can be one of the most profitable and lifestylefriendly practice areas. '
             "No court dates, predictable clients, and usually you're charging flat fees.",
      'title': 'How to Start an Estate Planning Law Firm: What Lawyers Need To Know (Darcel '
               'Lobo)',
      'url': 'https://www.youtube.com/watch?v=wQcPBrtGgYY&t=22s',
      'video_id': 'wQcPBrtGgYY'},
     {'author': 'JunkRemovalWeb',
      'channel': 'JunkRemovalWeb',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:05](https://www.youtube.com/watch?v=L8fzGwXd_kk&t=485s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2025 business came from repeat clients  and another 22 % from past client '
              "referrals. That's half their business writing on reputation.",
      'timestamp': 485,
      'timestamp_label': '[00:08:05]',
      'timestamp_seconds': 485,
      'tip': '2025 business came from repeat clients  and another 22 % from past client '
             "referrals. That's half their business writing on reputation.",
      'title': 'Estate Cleanout Business: Win Families, Executors & Realtors (JunkRemovalWeb)',
      'url': 'https://www.youtube.com/watch?v=L8fzGwXd_kk&t=485s',
      'video_id': 'L8fzGwXd_kk'},
     {'author': 'Academy of Probate',
      'channel': 'Academy of Probate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=b7b8x4Jqz6c&t=103s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Putting that property on the market at volume at market value you want to make '
              'sure you are putting your clients interest first and foremost which is the.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'Putting that property on the market at volume at market value you want to make '
             'sure you are putting your clients interest first and foremost which is the.',
      'title': 'Unlocking  How to Wholesale MLS Property Probate Real Estate (Academy of '
               'Probate)',
      'url': 'https://www.youtube.com/watch?v=b7b8x4Jqz6c&t=103s',
      'video_id': 'b7b8x4Jqz6c'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=d3g2CkHYVp4&t=222s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Option one was a cash offer closed in two or three days if as soon as I could '
              "get title option two wasn't as is where is sale on on the market and we would "
              'get a higher number than that option three was we sell all the personal '
              'property use that money for improvements.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': 'Option one was a cash offer closed in two or three days if as soon as I could '
             "get title option two wasn't as is where is sale on on the market and we would "
             'get a higher number than that option three was we sell all the personal property '
             'use that money for improvements.',
      'title': 'Probate Mastery is more than Probate Training and Certification | Chad '
               "Corbett's Probate Course (Probate Mastery)",
      'url': 'https://www.youtube.com/watch?v=d3g2CkHYVp4&t=222s',
      'video_id': 'd3g2CkHYVp4'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:48](https://www.youtube.com/watch?v=cbWbIqZ3KnU&t=1188s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now that said even the one even the properties that are held in trust i teach '
              'two things one is how to market to the family directly by providing value.',
      'timestamp': 1188,
      'timestamp_label': '[00:19:48]',
      'timestamp_seconds': 1188,
      'tip': 'Now that said even the one even the properties that are held in trust i teach '
             'two things one is how to market to the family directly by providing value.',
      'title': 'What Is the Best Way to Get Started with Probate Real Estate Investing? [Chad '
               'Corbett] (Beau Eckstein, Business Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=cbWbIqZ3KnU&t=1188s',
      'video_id': 'cbWbIqZ3KnU'},
     {'author': 'At Home with Jody',
      'channel': 'At Home with Jody',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=eQ9rTXDlJQM&t=470s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's something that a lot of people don't think about or don't understand. "
              "You don't have to choose just one option. You can pull out high-value items for "
              'an online sale or an auction and then do a traditional estate sale for the '
              'rest.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': "Here's something that a lot of people don't think about or don't understand. You "
             "don't have to choose just one option. You can pull out high-value items for an "
             'online sale or an auction and then do a traditional estate sale for the rest.',
      'title': 'Estate Sale Planning Basics: How to Clear Out a Home Without Feeling '
               'Overwhelmed (At Home with Jody)',
      'url': 'https://www.youtube.com/watch?v=eQ9rTXDlJQM&t=470s',
      'video_id': 'eQ9rTXDlJQM'},
     {'author': 'Florida Realtors YouTube',
      'channel': 'Florida Realtors YouTube',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=yyvDp4R_T84&t=238s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You provide a high level of service it's cumbersome and it's time-consuming so "
              'you have to be your clients boots on the ground this is often an emotional and '
              'overwhelming time for seniors you have a tremendous opportunity to share your '
              'expertise and your real tore heart.',
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': "You provide a high level of service it's cumbersome and it's time-consuming so "
             'you have to be your clients boots on the ground this is often an emotional and '
             'overwhelming time for seniors you have a tremendous opportunity to share your '
             'expertise and your real tore heart.',
      'title': 'How Realtors Can Guide Clients Transitioning to Senior Living (Florida '
               'Realtors YouTube)',
      'url': 'https://www.youtube.com/watch?v=yyvDp4R_T84&t=238s',
      'video_id': 'yyvDp4R_T84'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:08](https://www.youtube.com/watch?v=-lMVLigkZQI&t=1988s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t know the shape of the house. They didn't ask for any inspection reports. "
              'They just wanted to know that their client was getting fair market value. '
              'David, what what do they mean by licensed? Like are you a licensed realtor?',
      'timestamp': 1988,
      'timestamp_label': '[00:33:08]',
      'timestamp_seconds': 1988,
      'tip': "'t know the shape of the house. They didn't ask for any inspection reports. They "
             'just wanted to know that their client was getting fair market value. David, what '
             'what do they mean by licensed? Like are you a licensed realtor?',
      'title': 'How to Secure Estate Attorney Partnerships for Probate Deals (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=-lMVLigkZQI&t=1988s',
      'video_id': '-lMVLigkZQI'},
     {'author': 'Brandon Mulrenin',
      'channel': 'Brandon Mulrenin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:06](https://www.youtube.com/watch?v=tHKQUQ1PDts&t=1386s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They do a hell of a job and so mike thank you so much for for uh for the value '
              'you dropped today bro I appreciate it yeah my pleasure anytime.',
      'timestamp': 1386,
      'timestamp_label': '[00:23:06]',
      'timestamp_seconds': 1386,
      'tip': 'They do a hell of a job and so mike thank you so much for for uh for the value '
             'you dropped today bro I appreciate it yeah my pleasure anytime.',
      'title': 'How to Get PROBATE LISTINGS from Probate Attorneys (Brandon Mulrenin)',
      'url': 'https://www.youtube.com/watch?v=tHKQUQ1PDts&t=1386s',
      'video_id': 'tHKQUQ1PDts'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=6EHNu72T83s&t=20s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh we're here for you guys to ask your questions, share your stories. Um, we'll "
              'share some uh strategies that you can be using in your business to to grow kind '
              'of the probate and the estate administration niche or the the the estate niche.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Uh we're here for you guys to ask your questions, share your stories. Um, we'll "
             'share some uh strategies that you can be using in your business to to grow kind '
             'of the probate and the estate administration niche or the the the estate niche.',
      'title': 'Probate Cold Calling Scripts That Work in 2025 (Watch This Before Your Next '
               'Call) (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=6EHNu72T83s&t=20s',
      'video_id': '6EHNu72T83s'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=pgW-G0oZoa4&t=158s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So you guys are probably not buying more than one or two counties. I spend '
              '$2,200 a month on the probate list here in Dallas Fort Worth. So, I get about '
              "30 or 40 out of state clients. Those are the ones that I'm mailing very "
              'aggressively and calling.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'So you guys are probably not buying more than one or two counties. I spend '
             '$2,200 a month on the probate list here in Dallas Fort Worth. So, I get about 30 '
             "or 40 out of state clients. Those are the ones that I'm mailing very "
             'aggressively and calling.',
      'title': "How to Find and Convert Probate Leads for Real Estate Deals (Even If You're "
               'Just Starting Out) (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=pgW-G0oZoa4&t=158s',
      'video_id': 'pgW-G0oZoa4'}],
 2: [{'author': 'California Probate Real Estate Made Simple',
      'channel': 'California Probate Real Estate Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:31](https://www.youtube.com/watch?v=lrpGu0nZK1E&t=511s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bond premiums if a bond is required. Later, attorney fees if you hired counsel '
              'and their fee is set by the court. The earlier you file these, the sooner the '
              "timeline begins and the sooner you'll have legal authority to act.",
      'timestamp': 511,
      'timestamp_label': '[00:08:31]',
      'timestamp_seconds': 511,
      'tip': 'Bond premiums if a bond is required. Later, attorney fees if you hired counsel '
             'and their fee is set by the court. The earlier you file these, the sooner the '
             "timeline begins and the sooner you'll have legal authority to act.",
      'title': 'Start Probate in California: Step-by-Step Guide (2025) (California Probate '
               'Real Estate Made Simple)',
      'url': 'https://www.youtube.com/watch?v=lrpGu0nZK1E&t=511s',
      'video_id': 'lrpGu0nZK1E'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:21](https://www.youtube.com/watch?v=ih5FQvZZVck&t=741s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm sorry, the court the confirmation of sale order to the court sooner you get "
              'it back. And then you want to get an original certified copy to escrow and then '
              "on that that serves your buyer and then you close quickly as possible. I'm Bill "
              'Gross, the LA probate expert.',
      'timestamp': 741,
      'timestamp_label': '[00:12:21]',
      'timestamp_seconds': 741,
      'tip': "I'm sorry, the court the confirmation of sale order to the court sooner you get "
             'it back. And then you want to get an original certified copy to escrow and then '
             "on that that serves your buyer and then you close quickly as possible. I'm Bill "
             'Gross, the LA probate expert.',
      'title': 'LA Probate Overbids: 1 in 6 Court Confirmation Sales Get Overbid (Bill Gross, '
               'the LA Probate Expert)',
      'url': 'https://www.youtube.com/watch?v=ih5FQvZZVck&t=741s',
      'video_id': 'ih5FQvZZVck'},
     {'author': 'Michael Franke',
      'channel': 'Michael Franke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:29](https://www.youtube.com/watch?v=iJVCVwX-rmA&t=1349s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s no will, how heirs are determined, how and when administrators get letters "
              'of administration, how to get an early contract for an amendment, and how to '
              "amend it once authority exists so it's enforceable, all of a sudden you stop "
              'guessing.',
      'timestamp': 1349,
      'timestamp_label': '[00:22:29]',
      'timestamp_seconds': 1349,
      'tip': "'s no will, how heirs are determined, how and when administrators get letters of "
             'administration, how to get an early contract for an amendment, and how to amend '
             "it once authority exists so it's enforceable, all of a sudden you stop guessing.",
      'title': 'Probate for Real Estate Investors (Step-by-Step Beginner Guide) (Michael '
               'Franke)',
      'url': 'https://www.youtube.com/watch?v=iJVCVwX-rmA&t=1349s',
      'video_id': 'iJVCVwX-rmA'},
     {'author': 'Duc Minh Lam',
      'channel': 'Duc Minh Lam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=dQOLpmObWhY&t=404s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "California's landmark disclosure reforms. We are talking upfront written "
              'accounting of all professional fees and performance incentives before anyone '
              'signs a single document. Zero hidden fees, zero opaque kickbacks, just total '
              "clarity to protect the seller's equity.",
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': "California's landmark disclosure reforms. We are talking upfront written "
             'accounting of all professional fees and performance incentives before anyone '
             'signs a single document. Zero hidden fees, zero opaque kickbacks, just total '
             "clarity to protect the seller's equity.",
      'title': 'Orange County Commercial Real Estate Insights for Investors on Probate Costs '
               '(Duc Minh Lam)',
      'url': 'https://www.youtube.com/watch?v=dQOLpmObWhY&t=404s',
      'video_id': 'dQOLpmObWhY'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:23](https://www.youtube.com/watch?v=P5kUaYnRKbo&t=2303s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I could, you know, all the services I could offer them. I could, you know, put '
              'it on the market. I I was or knew investors that could uh pay cash quick. And I '
              'I remember a guy saying to me, "Well, give me both options." " So, I I did a '
              'quick analysis.',
      'timestamp': 2303,
      'timestamp_label': '[00:38:23]',
      'timestamp_seconds': 2303,
      'tip': 'I could, you know, all the services I could offer them. I could, you know, put '
             'it on the market. I I was or knew investors that could uh pay cash quick. And I '
             'I remember a guy saying to me, "Well, give me both options." " So, I I did a '
             'quick analysis.',
      'title': 'Post-Election Prospecting, Probate Calling Tips & New Holiday Mailers! | ATL '
               'Mastermind 602 (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=P5kUaYnRKbo&t=2303s',
      'video_id': 'P5kUaYnRKbo'},
     {'author': 'Flipping Mastery TV',
      'channel': 'Flipping Mastery TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:07](https://www.youtube.com/watch?v=K_L_G6jbyAE&t=487s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Probate expert when offering your service to a probate attorney offer to pay '
              'him or her a referral fee some will be open to this idea and some are unable.',
      'timestamp': 487,
      'timestamp_label': '[00:08:07]',
      'timestamp_seconds': 487,
      'tip': 'Probate expert when offering your service to a probate attorney offer to pay him '
             'or her a referral fee some will be open to this idea and some are unable.',
      'title': 'How To Buy Probate Real Estate Cheap! (Flipping Mastery TV)',
      'url': 'https://www.youtube.com/watch?v=K_L_G6jbyAE&t=487s',
      'video_id': 'K_L_G6jbyAE'},
     {'author': 'Horizon Real Estate & Probate and Trust Help',
      'channel': 'Horizon Real Estate & Probate and Trust Help',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=Lt0e4PdSMmo&t=213s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "On that subject a quick note on costs california probate is not free you'll "
              'have to pay california probate fees during this whole process of settling.',
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "On that subject a quick note on costs california probate is not free you'll have "
             'to pay california probate fees during this whole process of settling.',
      'title': 'What is Probate? Your Full Guide Through the Probate Process in California '
               '(Horizon Real Estate & Probate and Trust Help)',
      'url': 'https://www.youtube.com/watch?v=Lt0e4PdSMmo&t=213s',
      'video_id': 'Lt0e4PdSMmo'},
     {'author': 'Flip With Rick',
      'channel': 'Flip With Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[03:12:22](https://www.youtube.com/watch?v=e3YN7RJaj6U&t=11542s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm done with that, I'll head your way. Just give me a call when you're heading "
              'over. Now, I can find a new probate attorney. And by the way, to open a '
              "probate, it's usually less than $400 in court fees, not attorney fees. The "
              'typical attorney to open a probate.',
      'timestamp': 11542,
      'timestamp_label': '[03:12:22]',
      'timestamp_seconds': 11542,
      'tip': "I'm done with that, I'll head your way. Just give me a call when you're heading "
             'over. Now, I can find a new probate attorney. And by the way, to open a probate, '
             "it's usually less than $400 in court fees, not attorney fees. The typical "
             'attorney to open a probate.',
      'title': 'How to Wholesale Probates (Full Course) 4 Hours (Flip With Rick)',
      'url': 'https://www.youtube.com/watch?v=e3YN7RJaj6U&t=11542s',
      'video_id': 'e3YN7RJaj6U'},
     {'author': 'Ronald D. Payne II - Estates Attorney',
      'channel': 'Ronald D. Payne II - Estates Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=5JWPb5QsWx4&t=36s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You ask the clerk of court to certify who's in charge of everything and then "
              'you gather their assets pay their bills and then hopefully.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "You ask the clerk of court to certify who's in charge of everything and then you "
             'gather their assets pay their bills and then hopefully.',
      'title': 'Overview of Probate in NC // Ronald D. Payne II, Estate Planning and Probate '
               'Attorney (Ronald D. Payne II - Estates Attorney)',
      'url': 'https://www.youtube.com/watch?v=5JWPb5QsWx4&t=36s',
      'video_id': '5JWPb5QsWx4'},
     {'author': 'Sell a House in Probate California | Brendan Mohr',
      'channel': 'Sell a House in Probate California | Brendan Mohr',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=Gz6Ih7tLzdQ&t=114s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or administrator only has limited Authority then he has to go to a court '
              "hearing to have the judge confirm the sale that's the only way the real estate.",
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Or administrator only has limited Authority then he has to go to a court hearing '
             "to have the judge confirm the sale that's the only way the real estate.",
      'title': 'What is a Probate Sale With Court Confirmation | Brendan Mohr (Sell a House in '
               'Probate California | Brendan Mohr)',
      'url': 'https://www.youtube.com/watch?v=Gz6Ih7tLzdQ&t=114s',
      'video_id': 'Gz6Ih7tLzdQ'},
     {'author': 'Rick Ginn',
      'channel': 'Rick Ginn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=OMiXHCnv8tU&t=423s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pr agrees to it and that's the right person and then the buyer is the right "
              "person and they're going to pay for it that's it that's the only so so many.",
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': "Pr agrees to it and that's the right person and then the buyer is the right "
             "person and they're going to pay for it that's it that's the only so so many.",
      'title': 'The Biggest Mistake People Make Wholesaling Probate Properties (Rick Ginn)',
      'url': 'https://www.youtube.com/watch?v=OMiXHCnv8tU&t=423s',
      'video_id': 'OMiXHCnv8tU'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=-ZhpzThVK5o&t=147s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And uh and squander it on the cheap and i see that happening all the time and i '
              "yeah i'm listening right now where they were in escrow for.",
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'And uh and squander it on the cheap and i see that happening all the time and i '
             "yeah i'm listening right now where they were in escrow for.",
      'title': 'Chad Corbett Explains Why Probate Calls are Important (Bill Gross, the LA '
               'Probate Expert)',
      'url': 'https://www.youtube.com/watch?v=-ZhpzThVK5o&t=147s',
      'video_id': '-ZhpzThVK5o'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=svPbBkp8nRQ&t=30s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Level of education and an education a course that teaches the methodology that '
              'made this so fun and easy for me and my business starting all the way back in '
              '2011 and probate mastery was that course.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'Level of education and an education a course that teaches the methodology that '
             'made this so fun and easy for me and my business starting all the way back in '
             '2011 and probate mastery was that course.',
      'title': 'Learn Probate and Build a Probate Business - Probate Training and '
               'Certification with Chad Corbett (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=svPbBkp8nRQ&t=30s',
      'video_id': 'svPbBkp8nRQ'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:58](https://www.youtube.com/watch?v=nNLFW4SvPGo&t=2638s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Mentioned buying the Sun out of his Airship isn't that going to just put the um "
              "the the buyer that's buying the Airship put them in the upside down situation.",
      'timestamp': 2638,
      'timestamp_label': '[00:43:58]',
      'timestamp_seconds': 2638,
      'tip': "Mentioned buying the Sun out of his Airship isn't that going to just put the um "
             "the the buyer that's buying the Airship put them in the upside down situation.",
      'title': 'Innovative Strategies for Sellers and Investors in the Probate Market | '
               'Probate Mastermind #439 (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=nNLFW4SvPGo&t=2638s',
      'video_id': 'nNLFW4SvPGo'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:56:09](https://www.youtube.com/watch?v=LNsr_JuZvn8&t=3369s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um it it is not a way to necessarily circumvent having to pay high one-on-one '
              'coaching fees, but it is a way to get questions answered. So if if you want '
              'that weekly private coaching strategy and accountability, 500 a session.',
      'timestamp': 3369,
      'timestamp_label': '[00:56:09]',
      'timestamp_seconds': 3369,
      'tip': 'Um it it is not a way to necessarily circumvent having to pay high one-on-one '
             'coaching fees, but it is a way to get questions answered. So if if you want that '
             'weekly private coaching strategy and accountability, 500 a session.',
      'title': 'How to Work Probate Leads Before They Need to Sell (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=LNsr_JuZvn8&t=3369s',
      'video_id': 'LNsr_JuZvn8'}],
 3: [{'author': 'California Probate Real Estate Made Simple',
      'channel': 'California Probate Real Estate Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=32VmI6oEsPQ&t=172s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And once the court approves you, you'll receive what's called certified letters "
              'of administration or letters of testamentary. These letters are your official '
              'authority to act on behalf of the estate, including selling the real estate.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': "And once the court approves you, you'll receive what's called certified letters "
             'of administration or letters of testamentary. These letters are your official '
             'authority to act on behalf of the estate, including selling the real estate.',
      'title': 'How to Sell a House in Probate California (Step-by-Step Guide + Insider Tip) '
               '(California Probate Real Estate Made Simple)',
      'url': 'https://www.youtube.com/watch?v=32VmI6oEsPQ&t=172s',
      'video_id': '32VmI6oEsPQ'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=Xt7XgZo03Nw&t=105s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re in real estate and, um, you're kind of looking for a little bit of a leg up "
              "where you don't have to spend all the cost of creating your own business, you "
              'do want to do it with me where we share costs and we share some of the revenue '
              'on the back end.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "'re in real estate and, um, you're kind of looking for a little bit of a leg up "
             "where you don't have to spend all the cost of creating your own business, you do "
             'want to do it with me where we share costs and we share some of the revenue on '
             'the back end.',
      'title': '5 Proven Ways to Grow Your Probate Real Estate Business (and Never Run Out of '
               'Leads) (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=Xt7XgZo03Nw&t=105s',
      'video_id': 'Xt7XgZo03Nw'},
     {'author': 'Residential Assisted Living Academy',
      'channel': 'Residential Assisted Living Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=l7Esttpxsx0&t=42s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Keep your startup costs in mind as they may include purchasing, you know, real '
              'estate or purchasing land and building real estate or renovating a property, '
              'obtaining necessary licenses, hiring staff, FFN, carrying costs, and marketing '
              'your business.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Keep your startup costs in mind as they may include purchasing, you know, real '
             'estate or purchasing land and building real estate or renovating a property, '
             'obtaining necessary licenses, hiring staff, FFN, carrying costs, and marketing '
             'your business.',
      'title': 'How to Start a Residential Assisted Living Business (Residential Assisted '
               'Living Academy)',
      'url': 'https://www.youtube.com/watch?v=l7Esttpxsx0&t=42s',
      'video_id': 'l7Esttpxsx0'},
     {'author': 'Unit Math',
      'channel': 'Unit Math',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:05](https://www.youtube.com/watch?v=i8GDo8WTXWw&t=725s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's $3 million of property. At 25% down plus closing costs, the investor "
              'puts in about $840,000 of cash and borrows $2. The 10 houses produce about '
              '$162,000 of NOI. The loans cost about $193,000 a year. The portfolio runs about '
              '$32,000 in the red.',
      'timestamp': 725,
      'timestamp_label': '[00:12:05]',
      'timestamp_seconds': 725,
      'tip': "That's $3 million of property. At 25% down plus closing costs, the investor puts "
             'in about $840,000 of cash and borrows $2. The 10 houses produce about $162,000 '
             'of NOI. The loans cost about $193,000 a year. The portfolio runs about $32,000 '
             'in the red.',
      'title': 'The Economics of Owning Rental Properties (The Hidden Costs That Eat Your '
               'Profits!) (Unit Math)',
      'url': 'https://www.youtube.com/watch?v=i8GDo8WTXWw&t=725s',
      'video_id': 'i8GDo8WTXWw'},
     {'author': 'Frank Lopez Broker Group',
      'channel': 'Frank Lopez Broker Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=6YQBrw5g_-c&t=307s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm taking it back, cuz you're the one that's supposed to be answering the "
              'questions here. So, let me ask you this, um because this comes up a lot. They '
              'mom lives in LA County, passes away. Kids moved all over all over the country.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': "I'm taking it back, cuz you're the one that's supposed to be answering the "
             'questions here. So, let me ask you this, um because this comes up a lot. They '
             'mom lives in LA County, passes away. Kids moved all over all over the country.',
      'title': 'The Probate Overbid Process Explained: How Probate Court Protects Heirs From a '
               'Low Sale Price. (Frank Lopez Broker Group)',
      'url': 'https://www.youtube.com/watch?v=6YQBrw5g_-c&t=307s',
      'video_id': '6YQBrw5g_-c'},
     {'author': 'Cortes Law Firm',
      'channel': 'Cortes Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=oqbFju_2Muc&t=79s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Capital gains event of a hundred and ninety thousand dollars and I know what '
              "you're gonna say because we get it all the time in our comments well I fixed "
              'it.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Capital gains event of a hundred and ninety thousand dollars and I know what '
             "you're gonna say because we get it all the time in our comments well I fixed it.",
      'title': 'No Step Up Basis for Capital Gains! (Cortes Law Firm)',
      'url': 'https://www.youtube.com/watch?v=oqbFju_2Muc&t=79s',
      'video_id': 'oqbFju_2Muc'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:08](https://www.youtube.com/watch?v=Gyb24k08sGk&t=548s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Better the competition you the chance to make a profit now this is primarily '
              "for buyers agents or for agents that represent investors as buyers and they're "
              "not a lot of these properties there's about 50 a month of all of the "
              'accounting.',
      'timestamp': 548,
      'timestamp_label': '[00:09:08]',
      'timestamp_seconds': 548,
      'tip': 'Better the competition you the chance to make a profit now this is primarily for '
             "buyers agents or for agents that represent investors as buyers and they're not a "
             "lot of these properties there's about 50 a month of all of the accounting.",
      'title': 'How to Leverage MLS Limited Authority for Probate Leads (Bill Gross, the LA '
               'Probate Expert)',
      'url': 'https://www.youtube.com/watch?v=Gyb24k08sGk&t=548s',
      'video_id': 'Gyb24k08sGk'},
     {'author': 'EstateSail | The All-In-One Estate Sale Manager',
      'channel': 'EstateSail | The All-In-One Estate Sale Manager',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=bx6BgPRa2JY&t=475s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is going to shoot up quite quickly here. And we can as it's finishing up, "
              'we can just start to scroll down and edit prices how we want. We still have all '
              "of the same price research tools built in right here. So you'll see it's "
              'already finished.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': "This is going to shoot up quite quickly here. And we can as it's finishing up, "
             'we can just start to scroll down and edit prices how we want. We still have all '
             "of the same price research tools built in right here. So you'll see it's already "
             'finished.',
      'title': 'EstateSail Full Walkthrough: From Inventory to Checkout and Online Sales '
               '(EstateSail | The All-In-One Estate Sale Manager)',
      'url': 'https://www.youtube.com/watch?v=bx6BgPRa2JY&t=475s',
      'video_id': 'bx6BgPRa2JY'},
     {'author': 'Calvora Property Group',
      'channel': 'Calvora Property Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=mT_cRaJJe8A&t=149s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step four, you get a cash offer, a real number in writing. And this is the part '
              'that matters most. Read it over, sleep on it, talk it over with your family. We '
              'will never pressure you, and the offer costs you nothing.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'Step four, you get a cash offer, a real number in writing. And this is the part '
             'that matters most. Read it over, sleep on it, talk it over with your family. We '
             'will never pressure you, and the offer costs you nothing.',
      'title': 'Inherited a House? Sell It As-Is — Complete Walkthrough (Calvora Property '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=mT_cRaJJe8A&t=149s',
      'video_id': 'mT_cRaJJe8A'},
     {'author': 'Flip With Rick',
      'channel': 'Flip With Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:26](https://www.youtube.com/watch?v=ZS8hjtChnG8&t=1526s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Call a catch all and here's what a catchall is is this is where all my other "
              'Direct Mail goes into and then these are always postcards and then this is '
              'going to be your regular we buy.',
      'timestamp': 1526,
      'timestamp_label': '[00:25:26]',
      'timestamp_seconds': 1526,
      'tip': "Call a catch all and here's what a catchall is is this is where all my other "
             'Direct Mail goes into and then these are always postcards and then this is going '
             'to be your regular we buy.',
      'title': 'How to Master Probate Marketing | Wholesaling Real Estate | Part 2 (Flip With '
               'Rick)',
      'url': 'https://www.youtube.com/watch?v=ZS8hjtChnG8&t=1526s',
      'video_id': 'ZS8hjtChnG8'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:54](https://www.youtube.com/watch?v=kvSTArlGoMU&t=1434s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t need and in many cases can't afford. Uh, these sellers are more "
              'appreciative, uh, willing to trust your expertise and less likely to nickel and '
              "dime you over commission or price. Uh, they're often in the middle of a complex "
              'probate or an estate administration process.',
      'timestamp': 1434,
      'timestamp_label': '[00:23:54]',
      'timestamp_seconds': 1434,
      'tip': "'t need and in many cases can't afford. Uh, these sellers are more appreciative, "
             'uh, willing to trust your expertise and less likely to nickel and dime you over '
             "commission or price. Uh, they're often in the middle of a complex probate or an "
             'estate administration process.',
      'title': 'How Probate Real Estate Specialists Find Leads,  Real Life Court Visits & Atty '
               'Referral Strategies (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=kvSTArlGoMU&t=1434s',
      'video_id': 'kvSTArlGoMU'},
     {'author': 'Horizon Real Estate & Probate and Trust Help',
      'channel': 'Horizon Real Estate & Probate and Trust Help',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=lo2f0qbkjaQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're unsure, this is something that you can confirm with your trust or "
              'probate attorney. Number two is really important. It is to secure the property. '
              "You're going to want to sort of know who has the keys.",
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "If you're unsure, this is something that you can confirm with your trust or "
             'probate attorney. Number two is really important. It is to secure the property. '
             "You're going to want to sort of know who has the keys.",
      'title': "Executor's 10 Guides to Selling an Inherited Home (Horizon Real Estate & "
               'Probate and Trust Help)',
      'url': 'https://www.youtube.com/watch?v=lo2f0qbkjaQ&t=79s',
      'video_id': 'lo2f0qbkjaQ'},
     {'author': 'Open Letter Marketing',
      'channel': 'Open Letter Marketing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=MLoqvKtXJ20&t=312s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Up as a real estate professional uh we have weekly trainings inside so they '
              "know exactly who you're reaching out to what the need is and the strategy "
              'behind everything.',
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': 'Up as a real estate professional uh we have weekly trainings inside so they know '
             "exactly who you're reaching out to what the need is and the strategy behind "
             'everything.',
      'title': 'Starting out with direct mail? (Open Letter Marketing)',
      'url': 'https://www.youtube.com/watch?v=MLoqvKtXJ20&t=312s',
      'video_id': 'MLoqvKtXJ20'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:53](https://www.youtube.com/watch?v=KirkNi05zPU&t=413s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Right and I I said it doesn't sound like you're ready to decide right now and "
              'he said yeah but I will be soon I go great do you mind if I call you back in a '
              "couple of weeks and he said you know you're the nicest person that's called.",
      'timestamp': 413,
      'timestamp_label': '[00:06:53]',
      'timestamp_seconds': 413,
      'tip': "Right and I I said it doesn't sound like you're ready to decide right now and he "
             'said yeah but I will be soon I go great do you mind if I call you back in a '
             "couple of weeks and he said you know you're the nicest person that's called.",
      'title': 'Rapport and Prospecting Tips for Probate Real Estate Agents | Probate '
               'Mastermind #435 (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=KirkNi05zPU&t=413s',
      'video_id': 'KirkNi05zPU'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:35](https://www.youtube.com/watch?v=lA-S6Qgcqwo&t=2975s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business that's creating vendor and attorney relationships and when you get to "
              'the point where your attorneys and vendors are bringing you multiple.',
      'timestamp': 2975,
      'timestamp_label': '[00:49:35]',
      'timestamp_seconds': 2975,
      'tip': "Business that's creating vendor and attorney relationships and when you get to "
             'the point where your attorneys and vendors are bringing you multiple.',
      'title': 'Probate Real Estate Strategies: Proven Marketing Tactics to Get More Leads & '
               'Attorney Referrals (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=lA-S6Qgcqwo&t=2975s',
      'video_id': 'lA-S6Qgcqwo'}],
 4: [{'author': 'The Retirement Loan Guy',
      'channel': 'The Retirement Loan Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:41](https://www.youtube.com/watch?v=T3KZz5kBYZ4&t=281s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A home owned by a business entity, like an LLC, generally isn't eligible. This "
              'is the one that catches people who had an attorney do careful estate planning '
              "years ago, so it's worth a quick conversation before you assume anything either "
              'way.',
      'timestamp': 281,
      'timestamp_label': '[00:04:41]',
      'timestamp_seconds': 281,
      'tip': "A home owned by a business entity, like an LLC, generally isn't eligible. This "
             'is the one that catches people who had an attorney do careful estate planning '
             "years ago, so it's worth a quick conversation before you assume anything either "
             'way.',
      'title': 'Will My Home Even Qualify for a Reverse Mortgage? Condo, Trust, Manufactured '
               'Home (The Retirement Loan Guy)',
      'url': 'https://www.youtube.com/watch?v=T3KZz5kBYZ4&t=281s',
      'video_id': 'T3KZz5kBYZ4'},
     {'author': 'Tricia Garcia Real Estate',
      'channel': 'Tricia Garcia Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=qNeCeQehzRg&t=260s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'California, Ventura County, LA County, anywhere. It could be for single family '
              'homes. It could be for condos, multiple units, all of them count. Now, I need '
              'to clear up the biggest source of confusion that I see going around online.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'California, Ventura County, LA County, anywhere. It could be for single family '
             'homes. It could be for condos, multiple units, all of them count. Now, I need to '
             'clear up the biggest source of confusion that I see going around online.',
      'title': '$0 Taxable Gain on an $800,000 Sale? The Step-Up Basis Strategy Explained '
               '(Tricia Garcia Real Estate)',
      'url': 'https://www.youtube.com/watch?v=qNeCeQehzRg&t=260s',
      'video_id': 'qNeCeQehzRg'},
     {'author': 'Carolynn Castillo',
      'channel': 'Carolynn Castillo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:02](https://www.youtube.com/watch?v=RR9l10XmnC4&t=902s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t work or cold calling this or that. Okay, cold calling is the quickest, "
              'fastest way to get money in this business. Okay, is there other ways to get '
              'money? You can market, you can network, right? You can um do mailers, direct '
              'mail, right?',
      'timestamp': 902,
      'timestamp_label': '[00:15:02]',
      'timestamp_seconds': 902,
      'tip': "'t work or cold calling this or that. Okay, cold calling is the quickest, "
             'fastest way to get money in this business. Okay, is there other ways to get '
             'money? You can market, you can network, right? You can um do mailers, direct '
             'mail, right?',
      'title': 'Unlocking the Gold Rush of Probate Real Estate for 2026! 🎉 (Carolynn Castillo)',
      'url': 'https://www.youtube.com/watch?v=RR9l10XmnC4&t=902s',
      'video_id': 'RR9l10XmnC4'},
     {'author': 'Meinzer Legal Briefs',
      'channel': 'Meinzer Legal Briefs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=k-XM0z4Yjzs&t=21s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The California probate is restrictive, cumbersome, and lengthy. The Independent '
              'Administration of Estates Act, or IAEA, is designed to streamline the process, '
              'at least a little.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'The California probate is restrictive, cumbersome, and lengthy. The Independent '
             'Administration of Estates Act, or IAEA, is designed to streamline the process, '
             'at least a little.',
      'title': 'Independent Administration of Estates Act (IAEA) in Probate (Meinzer Legal '
               'Briefs)',
      'url': 'https://www.youtube.com/watch?v=k-XM0z4Yjzs&t=21s',
      'video_id': 'k-XM0z4Yjzs'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:30](https://www.youtube.com/watch?v=uTFKO8zRNsI&t=2430s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um we mentioned from all the leads. Um so I basically just give a login into my '
              "lead list. I give access to the um county's GIS or tax software.",
      'timestamp': 2430,
      'timestamp_label': '[00:40:30]',
      'timestamp_seconds': 2430,
      'tip': 'Um we mentioned from all the leads. Um so I basically just give a login into my '
             "lead list. I give access to the um county's GIS or tax software.",
      'title': 'How I Convert Probate Leads Using a Resource Package & Follow-Up Plan  ( + VA '
               'execution tips) (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=uTFKO8zRNsI&t=2430s',
      'video_id': 'uTFKO8zRNsI'},
     {'author': 'Selling Inherited Property - The Prepared Heir',
      'channel': 'Selling Inherited Property - The Prepared Heir',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:51](https://www.youtube.com/watch?v=rnWBVJVgbTw&t=291s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Belongings and you can really lean on your probate attorney for their guidance '
              'through this having your family members come in and sort through the '
              'belongings.',
      'timestamp': 291,
      'timestamp_label': '[00:04:51]',
      'timestamp_seconds': 291,
      'tip': 'Belongings and you can really lean on your probate attorney for their guidance '
             'through this having your family members come in and sort through the belongings.',
      'title': 'Estate Cleanout Tips: How To Remove Items From A House After Death (Selling '
               'Inherited Property - The Prepared Heir)',
      'url': 'https://www.youtube.com/watch?v=rnWBVJVgbTw&t=291s',
      'video_id': 'rnWBVJVgbTw'},
     {'author': 'My Jennarocity',
      'channel': 'My Jennarocity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=zQLAx7SK5ZI&t=15s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tell you my story in 2015 I just got my real estate license and I was getting '
              'my real estate business up off the ground I was trying.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Tell you my story in 2015 I just got my real estate license and I was getting my '
             'real estate business up off the ground I was trying.',
      'title': 'Learn How To Become an Estate Sale Liquidator (My Jennarocity)',
      'url': 'https://www.youtube.com/watch?v=zQLAx7SK5ZI&t=15s',
      'video_id': 'zQLAx7SK5ZI'},
     {'author': 'Discover Colorado - The Cobb Home Team',
      'channel': 'Discover Colorado - The Cobb Home Team',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=1kkoh35VCho&t=44s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Talk to your loved one about their goals and concerns. Safety, independence, '
              'social connection. Second, understanding their finances. Is there long-term '
              'care insurance, veterans benefits? And does selling a home factor into all '
              "these finances when you're talking to families?",
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'Talk to your loved one about their goals and concerns. Safety, independence, '
             'social connection. Second, understanding their finances. Is there long-term care '
             'insurance, veterans benefits? And does selling a home factor into all these '
             "finances when you're talking to families?",
      'title': 'Where to Start With Senior Placement (Discover Colorado - The Cobb Home Team)',
      'url': 'https://www.youtube.com/watch?v=1kkoh35VCho&t=44s',
      'video_id': '1kkoh35VCho'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:26](https://www.youtube.com/watch?v=et_msiK8rvo&t=746s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And we had a safety net in place for the ones that needed it, and then we move '
              "along and they feel like it just helps reinforce the rapport and trust you're "
              'building. Chad you just fractured my ego? Um, ultimately, um, ultimately.',
      'timestamp': 746,
      'timestamp_label': '[00:12:26]',
      'timestamp_seconds': 746,
      'tip': 'And we had a safety net in place for the ones that needed it, and then we move '
             "along and they feel like it just helps reinforce the rapport and trust you're "
             'building. Chad you just fractured my ego? Um, ultimately, um, ultimately.',
      'title': 'Probate Real Estate Scripts Training: Live Cold Call Role Play #59 (All The '
               'Leads)',
      'url': 'https://www.youtube.com/watch?v=et_msiK8rvo&t=746s',
      'video_id': 'et_msiK8rvo'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:57](https://www.youtube.com/watch?v=kLAKLVbvcQY&t=357s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ownership in the area uh as I mentioned the sale uh possibly they have to go '
              "back to probate court but if not the floor well and technically it's um public "
              "auction also he presented a public auction let's open the public yeah.",
      'timestamp': 357,
      'timestamp_label': '[00:05:57]',
      'timestamp_seconds': 357,
      'tip': 'Ownership in the area uh as I mentioned the sale uh possibly they have to go '
             "back to probate court but if not the floor well and technically it's um public "
             "auction also he presented a public auction let's open the public yeah.",
      'title': 'Probate Overbid Auction: Watch a Real Los Angeles Sale (Bill Gross, the LA '
               'Probate Expert)',
      'url': 'https://www.youtube.com/watch?v=kLAKLVbvcQY&t=357s',
      'video_id': 'kLAKLVbvcQY'},
     {'author': 'Reverse Mortgages by Tim Oddo',
      'channel': 'Reverse Mortgages by Tim Oddo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=R4eJOKRQISs&t=15s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now they're no longer both are living and now you are left with the home well "
              "first of all it's really similar to just a normal mortgage.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Now they're no longer both are living and now you are left with the home well "
             "first of all it's really similar to just a normal mortgage.",
      'title': 'What Happens to a Reverse Mortgage When the Homeowner Dies? (Reverse Mortgages '
               'by Tim Oddo)',
      'url': 'https://www.youtube.com/watch?v=R4eJOKRQISs&t=15s',
      'video_id': 'R4eJOKRQISs'},
     {'author': 'Flip With Rick',
      'channel': 'Flip With Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:08](https://www.youtube.com/watch?v=_VFauJR1UAw&t=1448s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Person's passed away they have to move on and get the everything done so what "
              "does this do for us it's real simple all these scenarios right here allow us to "
              'have additional time to dispo our properties.',
      'timestamp': 1448,
      'timestamp_label': '[00:24:08]',
      'timestamp_seconds': 1448,
      'tip': "Person's passed away they have to move on and get the everything done so what "
             "does this do for us it's real simple all these scenarios right here allow us to "
             'have additional time to dispo our properties.',
      'title': 'Wholesaling Probate Real Estate STEP BY STEP [Part 1] (Flip With Rick)',
      'url': 'https://www.youtube.com/watch?v=_VFauJR1UAw&t=1448s',
      'video_id': '_VFauJR1UAw'},
     {'author': 'More Flip with Rick',
      'channel': 'More Flip with Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=utX5VR1nHk4&t=160s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Saying that to you and now it's kind of a trust that's got built and now it's "
              "like okay they're comfortable with you in this situation well what if they ask "
              'you like well how did you get my information.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "Saying that to you and now it's kind of a trust that's got built and now it's "
             "like okay they're comfortable with you in this situation well what if they ask "
             'you like well how did you get my information.',
      'title': 'The Perfect Cold Calling Script for Probate Leads in Wholesaling Real Estate '
               '(More Flip with Rick)',
      'url': 'https://www.youtube.com/watch?v=utX5VR1nHk4&t=160s',
      'video_id': 'utX5VR1nHk4'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=omZ157LG-W8&t=195s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I set up attorney relationships and make sure that attorneys are referring me. '
              'And um, when those things were all running really well, um, I had the ability '
              'and I had the right to go, "I\'m not going to cold call anymore.".',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'I set up attorney relationships and make sure that attorneys are referring me. '
             'And um, when those things were all running really well, um, I had the ability '
             'and I had the right to go, "I\'m not going to cold call anymore.".',
      'title': 'Probate Cold Calling vs Direct Mail: Which Gets More Listings? (Probate '
               'Mastery)',
      'url': 'https://www.youtube.com/watch?v=omZ157LG-W8&t=195s',
      'video_id': 'omZ157LG-W8'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=u46B4m0SDCw&t=68s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I thought we were the ones because we started our business with prospecting and '
              "we have made over a million dollars in our career. What I'm trying to get to is "
              'that. I would love those people who create syndicates.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'I thought we were the ones because we started our business with prospecting and '
             "we have made over a million dollars in our career. What I'm trying to get to is "
             'that. I would love those people who create syndicates.',
      'title': 'How Rosie Is Scaling Her Net Worth By Expanding Into Investment - Group '
               'Coaching with Chad Corbett (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=u46B4m0SDCw&t=68s',
      'video_id': 'u46B4m0SDCw'}],
 5: [{'author': 'Hans Goldstein: Tax & Exit Planning',
      'channel': 'Hans Goldstein: Tax & Exit Planning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=RKZ0VLSjISY&t=114s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '5 million under IRC section 1014. And a sale at that price produces essentially '
              'no capital gain. The $1,442,169 is not deferred. Holding trades the use of the '
              'cash during life and assumes the risk that the land could be worth less at '
              'death.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': '5 million under IRC section 1014. And a sale at that price produces essentially '
             'no capital gain. The $1,442,169 is not deferred. Holding trades the use of the '
             'cash during life and assumes the risk that the land could be worth less at '
             'death.',
      'title': 'Step Up in Basis Real Estate: Sell Now or Hold Until Death? (2026) (Hans '
               'Goldstein: Tax & Exit Planning)',
      'url': 'https://www.youtube.com/watch?v=RKZ0VLSjISY&t=114s',
      'video_id': 'RKZ0VLSjISY'},
     {'author': 'Sell That Wreck! With Stephanie Burt',
      'channel': 'Sell That Wreck! With Stephanie Burt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=6xUa7KjeSSY&t=181s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The mistake that I see isn't that people skip the attorney, it's that they wait "
              "until there's a problem. And here's the thing, a lot of those problems are much "
              'easier to avoid than they are to fix.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': "The mistake that I see isn't that people skip the attorney, it's that they wait "
             "until there's a problem. And here's the thing, a lot of those problems are much "
             'easier to avoid than they are to fix.',
      'title': '6 Critical First Steps if You Just Inherited a House (Sell That Wreck! With '
               'Stephanie Burt)',
      'url': 'https://www.youtube.com/watch?v=6xUa7KjeSSY&t=181s',
      'video_id': '6xUa7KjeSSY'},
     {'author': 'NOVA Real Estate Solutions',
      'channel': 'NOVA Real Estate Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=JG6VKzYq_uA&t=116s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That relief was invaluable. While the initial cost of an attorney might seem '
              'significant, consider it an investment. Mistakes in probate can lead to much '
              'larger financial penalties, prolonged court battles, or even personal liability '
              'for the executive.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': 'That relief was invaluable. While the initial cost of an attorney might seem '
             'significant, consider it an investment. Mistakes in probate can lead to much '
             'larger financial penalties, prolonged court battles, or even personal liability '
             'for the executive.',
      'title': 'Probate Process is a Trap (Unless You Know This) | Virginia Probate Explained '
               '2025 (NOVA Real Estate Solutions)',
      'url': 'https://www.youtube.com/watch?v=JG6VKzYq_uA&t=116s',
      'video_id': 'JG6VKzYq_uA'},
     {'author': 'The Medicare Family',
      'channel': 'The Medicare Family',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=hvl2NRPSVTE&t=66s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's the court process. If it avoids the court process, it just goes all "
              'the way around it. One, you avoid the publicity, avoid the cost, the time '
              'involved in going through the attorneys and the courts to get to the other '
              'side.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': "So that's the court process. If it avoids the court process, it just goes all "
             'the way around it. One, you avoid the publicity, avoid the cost, the time '
             'involved in going through the attorneys and the courts to get to the other side.',
      'title': 'How To Save Your House From Medicaid Recovery (Lady Bird Deeds Explained) (The '
               'Medicare Family)',
      'url': 'https://www.youtube.com/watch?v=hvl2NRPSVTE&t=66s',
      'video_id': 'hvl2NRPSVTE'},
     {'author': 'Rosen Injury Law',
      'channel': 'Rosen Injury Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:41](https://www.youtube.com/watch?v=7cYFXxbOdbc&t=521s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even if you have a will and you have your estate plan done, if all you have is '
              'a will, it will not avoid probate. Actually, the word probate means the legal '
              'administration of your estate, including that will distributing the assets to '
              'your heirs.',
      'timestamp': 521,
      'timestamp_label': '[00:08:41]',
      'timestamp_seconds': 521,
      'tip': 'Even if you have a will and you have your estate plan done, if all you have is a '
             'will, it will not avoid probate. Actually, the word probate means the legal '
             'administration of your estate, including that will distributing the assets to '
             'your heirs.',
      'title': 'Estate Planning Myths & Law Firm Growth with Alina Nuñez | Eric Rosen Podcast '
               '(Rosen Injury Law)',
      'url': 'https://www.youtube.com/watch?v=7cYFXxbOdbc&t=521s',
      'video_id': '7cYFXxbOdbc'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:28](https://www.youtube.com/watch?v=d-rZkDYaJhQ&t=628s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also, on the side, be building out your attorney relationships, visiting the '
              'courthouse, building out your network, creating content online. Do those things '
              'which are going to create a nice passive organic easy form of business.',
      'timestamp': 628,
      'timestamp_label': '[00:10:28]',
      'timestamp_seconds': 628,
      'tip': 'Also, on the side, be building out your attorney relationships, visiting the '
             'courthouse, building out your network, creating content online. Do those things '
             'which are going to create a nice passive organic easy form of business.',
      'title': 'Become a Probate Real Estate Specialist & Close More Deals (Real Examples '
               'Inside!) (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=d-rZkDYaJhQ&t=628s',
      'video_id': 'd-rZkDYaJhQ'},
     {'author': 'California Probate Real Estate Made Simple',
      'channel': 'California Probate Real Estate Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=-UQpV25bgAM&t=187s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s recorded against the home. And when you work with me, I take care of all of "
              'that for you. And if something pops up, I work with your probate attorney and '
              'our title officer to work it out immediately, long before a buyer is even in '
              'the picture.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': "'s recorded against the home. And when you work with me, I take care of all of "
             'that for you. And if something pops up, I work with your probate attorney and '
             'our title officer to work it out immediately, long before a buyer is even in the '
             'picture.',
      'title': 'Santa Clara Probate: Full Authority Sale Mistake Costs (California Probate '
               'Real Estate Made Simple)',
      'url': 'https://www.youtube.com/watch?v=-UQpV25bgAM&t=187s',
      'video_id': '-UQpV25bgAM'},
     {'author': 'Unbundled Attorney',
      'channel': 'Unbundled Attorney',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:04](https://www.youtube.com/watch?v=e7NC2IktQnY&t=2404s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That risk but he really needed to get his documents executed so I mean there's "
              "just there's there there are business decisions that you have to make.",
      'timestamp': 2404,
      'timestamp_label': '[00:40:04]',
      'timestamp_seconds': 2404,
      'tip': "That risk but he really needed to get his documents executed so I mean there's "
             "just there's there there are business decisions that you have to make.",
      'title': 'Building a Six-Figure a Month, Client-Centered Probate and Estate Planning Law '
               'Practice (Unbundled Attorney)',
      'url': 'https://www.youtube.com/watch?v=e7NC2IktQnY&t=2404s',
      'video_id': 'e7NC2IktQnY'},
     {'author': 'Pace Morby',
      'channel': 'Pace Morby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=7E_4DS5bEAI&t=26s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Authority to sell that so probate solves that problem well doesn't a will solve "
              'that problem uh a will says.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': "Authority to sell that so probate solves that problem well doesn't a will solve "
             'that problem uh a will says.',
      'title': 'What Is Probate In Real Estate? (Pace Morby)',
      'url': 'https://www.youtube.com/watch?v=7E_4DS5bEAI&t=26s',
      'video_id': '7E_4DS5bEAI'},
     {'author': 'Brent Daniels - Wholesaling Inc',
      'channel': 'Brent Daniels - Wholesaling Inc',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=wmbh_a5UnqI&t=202s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Texas where you can avoid probate altogether through an affidavit if you have '
              "like all the airs but that's a whole other thing okay there's crazy.",
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': 'Texas where you can avoid probate altogether through an affidavit if you have '
             "like all the airs but that's a whole other thing okay there's crazy.",
      'title': 'Real Estate Wholesale Properties in Probate - A Conversation w/ Al Nicoletti '
               '(Brent Daniels - Wholesaling Inc)',
      'url': 'https://www.youtube.com/watch?v=wmbh_a5UnqI&t=202s',
      'video_id': 'wmbh_a5UnqI'},
     {'author': 'The Real Estate Lawyer',
      'channel': 'The Real Estate Lawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=ASuTQp-hvNU&t=15s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Does probate affect real estate  i'm tiffany weber real estate attorney.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Does probate affect real estate  i'm tiffany weber real estate attorney.",
      'title': 'What is Probate in Real Estate? (The Real Estate Lawyer)',
      'url': 'https://www.youtube.com/watch?v=ASuTQp-hvNU&t=15s',
      'video_id': 'ASuTQp-hvNU'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=6iVpjQj9wjc&t=15s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Were right ready to go I'm sure you inspired a lot of people out there we "
              'preach that all the time but I think until people see it or they hear it.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Were right ready to go I'm sure you inspired a lot of people out there we preach "
             'that all the time but I think until people see it or they hear it.',
      'title': 'Direct Mail, Followups, + More! Marketing to Probate Real Estate Leads | '
               'Probate Mastermind #282 (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=6iVpjQj9wjc&t=15s',
      'video_id': '6iVpjQj9wjc'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=g3dWuQ30j4Y&t=55s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Court made a mistake they they wrote the wrong year on the court date it was '
              "last year instead of this year and I was like really that's crazy so I end up "
              'calling.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'Court made a mistake they they wrote the wrong year on the court date it was '
             "last year instead of this year and I was like really that's crazy so I end up "
             'calling.',
      'title': 'How Offering Help to Overloaded Probate Attorneys Can Get You More Referrals! '
               '📈 (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=g3dWuQ30j4Y&t=55s',
      'video_id': 'g3dWuQ30j4Y'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=WAsEf6usAg0&t=36s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Colleagues and I said and second how being an expert probably people are scared '
              "to be an expert but the truth is half the referrals that come to me aren't "
              "probate they just know I'm an expert in real estate and solving problems.",
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Colleagues and I said and second how being an expert probably people are scared '
             "to be an expert but the truth is half the referrals that come to me aren't "
             "probate they just know I'm an expert in real estate and solving problems.",
      'title': 'The Reputation of a Probate Real Estate Specialist | with Chad Corbett (Bill '
               'Gross, the LA Probate Expert)',
      'url': 'https://www.youtube.com/watch?v=WAsEf6usAg0&t=36s',
      'video_id': 'WAsEf6usAg0'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=6m0W2cil7rU&t=253s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Me some time and I I'll will walk through to make sure that we can get the most "
              "that we can get for it all of a sudden the attorneys think I'm a hero.",
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': "Me some time and I I'll will walk through to make sure that we can get the most "
             "that we can get for it all of a sudden the attorneys think I'm a hero.",
      'title': 'Divorce\xa0& Probate Leads: How to Build a Strong Attorney Referral Network '
               'for Realtors & Investors (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=6m0W2cil7rU&t=253s',
      'video_id': '6m0W2cil7rU'}],
 6: [{'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=D2NGOVJ2s6U&t=346s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s about people and situation and you'll find a way to bring real estate in "
              "quickly and you'll get paid for that. But, lead with your heart, provide value "
              'first, and call all the leads, and this will be a very successful pillar in '
              'your business.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': "'s about people and situation and you'll find a way to bring real estate in "
             "quickly and you'll get paid for that. But, lead with your heart, provide value "
             'first, and call all the leads, and this will be a very successful pillar in your '
             'business.',
      'title': 'What You Miss By Scrubbing Your Probate Real Estate Leads - Tips From Chad '
               'Corbett (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=D2NGOVJ2s6U&t=346s',
      'video_id': 'D2NGOVJ2s6U'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:44](https://www.youtube.com/watch?v=LaCR15esK0k&t=2684s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Meeting them, like even calling you the attorney first and saying, I'd like to "
              'interview you to see if you would qualify to represent my client and in '
              'building their estate plan.',
      'timestamp': 2684,
      'timestamp_label': '[00:44:44]',
      'timestamp_seconds': 2684,
      'tip': "Meeting them, like even calling you the attorney first and saying, I'd like to "
             'interview you to see if you would qualify to represent my client and in building '
             'their estate plan.',
      'title': 'Marketing to Pre-Probate vs Probate Leads, Vendor Referrals, and Probate '
               'Attorney Script ideas (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=LaCR15esK0k&t=2684s',
      'video_id': 'LaCR15esK0k'},
     {'author': 'The Professionalist: Real Estate Investing Podcast',
      'channel': 'The Professionalist: Real Estate Investing Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:50](https://www.youtube.com/watch?v=C0exaWWfFMk&t=530s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"I want to buy your house cash." Um that approach does work, but it\'s a '
              'numbers game. Um I kind of come at it from a different angle. You know, I do a '
              'good amount of direct mail. We do cold calling to market to the list.',
      'timestamp': 530,
      'timestamp_label': '[00:08:50]',
      'timestamp_seconds': 530,
      'tip': '"I want to buy your house cash." Um that approach does work, but it\'s a numbers '
             'game. Um I kind of come at it from a different angle. You know, I do a good '
             'amount of direct mail. We do cold calling to market to the list.',
      'title': 'How to Find Inheritance & Pre-Probate Real Estate Deals in 2026 (Step-by-Step) '
               '(The Professionalist: Real Estate Investing Podcast)',
      'url': 'https://www.youtube.com/watch?v=C0exaWWfFMk&t=530s',
      'video_id': 'C0exaWWfFMk'},
     {'author': 'Virtual Wholesaling Made Simple',
      'channel': 'Virtual Wholesaling Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=gUS4TsLhgiY&t=56s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re first getting started in wholesaling, your biggest priority should be "
              'building momentum. Not just chasing the biggest assignment fee. Not trying to '
              'find some secret list that nobody else knows about, but momentum.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "'re first getting started in wholesaling, your biggest priority should be "
             'building momentum. Not just chasing the biggest assignment fee. Not trying to '
             'find some secret list that nobody else knows about, but momentum.',
      'title': 'PROBATE IS DEAD (FOR BEGINNERS) (Virtual Wholesaling Made Simple)',
      'url': 'https://www.youtube.com/watch?v=gUS4TsLhgiY&t=56s',
      'video_id': 'gUS4TsLhgiY'},
     {'author': 'Phone Sniper — Real Estate Investor Software',
      'channel': 'Phone Sniper — Real Estate Investor Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=HH0UX5IwhHM&t=115s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, what you can do is you can automatically search and click this button right '
              'here, find errors, and it will automatically run a skip trace of all known '
              'relatives or associates of the person who used to own the property.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'So, what you can do is you can automatically search and click this button right '
             'here, find errors, and it will automatically run a skip trace of all known '
             'relatives or associates of the person who used to own the property.',
      'title': 'Text Every Heir on a Probate Lead at Once (Phone Sniper — Real Estate Investor '
               'Software)',
      'url': 'https://www.youtube.com/watch?v=HH0UX5IwhHM&t=115s',
      'video_id': 'HH0UX5IwhHM'},
     {'author': 'Flip With Rick',
      'channel': 'Flip With Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:19](https://www.youtube.com/watch?v=4-UlN2iP-_c&t=859s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'She\'s like, "No, no, we\'re fine with that. It was open up the title, get it '
              "going. They're going to fund it with cash, so it's no big deal. You see, if you "
              'take all that away, only thing the lawyer can do is pick apart little terms.',
      'timestamp': 859,
      'timestamp_label': '[00:14:19]',
      'timestamp_seconds': 859,
      'tip': 'She\'s like, "No, no, we\'re fine with that. It was open up the title, get it '
             "going. They're going to fund it with cash, so it's no big deal. You see, if you "
             'take all that away, only thing the lawyer can do is pick apart little terms.',
      'title': 'How to Make $50,000 Per Month Wholesaling the Probate List (Flip With Rick)',
      'url': 'https://www.youtube.com/watch?v=4-UlN2iP-_c&t=859s',
      'video_id': '4-UlN2iP-_c'},
     {'author': 'PROFITABLE',
      'channel': 'PROFITABLE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:19](https://www.youtube.com/watch?v=Tsd1Ymoso1Q&t=1099s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It also establishes the legal relationship between the two parties. And here's "
              'something many first-time investors underestimate. A landlord is not simply '
              "renting out a building. They're operating a service business. The property must "
              'be maintained.',
      'timestamp': 1099,
      'timestamp_label': '[00:18:19]',
      'timestamp_seconds': 1099,
      'tip': "It also establishes the legal relationship between the two parties. And here's "
             'something many first-time investors underestimate. A landlord is not simply '
             "renting out a building. They're operating a service business. The property must "
             'be maintained.',
      'title': 'How Real Estate Investors Actually Make Money From Rentals (PROFITABLE)',
      'url': 'https://www.youtube.com/watch?v=Tsd1Ymoso1Q&t=1099s',
      'video_id': 'Tsd1Ymoso1Q'},
     {'author': 'National Referral Network',
      'channel': 'National Referral Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=pryGLjB9I8k&t=80s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Planning their estate plan one is going to the be the personal side that we all '
              "deal with when we're doing estate planning but on the business side.",
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'Planning their estate plan one is going to the be the personal side that we all '
             "deal with when we're doing estate planning but on the business side.",
      'title': 'Effective Estate Planning for Business Owners (National Referral Network)',
      'url': 'https://www.youtube.com/watch?v=pryGLjB9I8k&t=80s',
      'video_id': 'pryGLjB9I8k'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:15](https://www.youtube.com/watch?v=Mash-3wq9zY&t=315s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t go in comparable to the way that Richie did. Um, a lot of people go in and "
              'they say, "Hey, um, I\'m a real estate agent. I want to list inherited '
              'properties and I want to be able to find how to get all the data and figure out '
              'who to call.".',
      'timestamp': 315,
      'timestamp_label': '[00:05:15]',
      'timestamp_seconds': 315,
      'tip': "'t go in comparable to the way that Richie did. Um, a lot of people go in and "
             'they say, "Hey, um, I\'m a real estate agent. I want to list inherited '
             'properties and I want to be able to find how to get all the data and figure out '
             'who to call.".',
      'title': 'Winning Probate Leads: Know the Process, Serve Your Market (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=Mash-3wq9zY&t=315s',
      'video_id': 'Mash-3wq9zY'},
     {'author': 'JM Junk Removers',
      'channel': 'JM Junk Removers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=0dYqJW59Zxg&t=328s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We take all of our trash cans we take 10 trash cans uh and then we're just "
              "we're filling the trash cans with the smaller stuff that didn't go in the first "
              'load right we lay out the tarps into a big circle uh let me take this real '
              'quick.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': "We take all of our trash cans we take 10 trash cans uh and then we're just we're "
             "filling the trash cans with the smaller stuff that didn't go in the first load "
             'right we lay out the tarps into a big circle uh let me take this real quick.',
      'title': 'Estate Clean-out / Things to Consider When Pricing a Job / How to be Faster on '
               'Multiple Load Jobs (JM Junk Removers)',
      'url': 'https://www.youtube.com/watch?v=0dYqJW59Zxg&t=328s',
      'video_id': '0dYqJW59Zxg'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:32](https://www.youtube.com/watch?v=sy23pOWuMEU&t=1652s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yourself getting confident and getting clear on your offer is the best first '
              "step when it comes time to get data depends on the market you're in and some.",
      'timestamp': 1652,
      'timestamp_label': '[00:27:32]',
      'timestamp_seconds': 1652,
      'tip': 'Yourself getting confident and getting clear on your offer is the best first '
             "step when it comes time to get data depends on the market you're in and some.",
      'title': 'Interview with Chad Corbett of Probate Mastery (Bill Gross, the LA Probate '
               'Expert)',
      'url': 'https://www.youtube.com/watch?v=sy23pOWuMEU&t=1652s',
      'video_id': 'sy23pOWuMEU'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=9eNkvtVoeao&t=15s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh 2023 and this is all the leads Mastermind podcast over 422. uh just so you '
              "all know uh Bruce has decided he'd rather go spend time with.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Uh 2023 and this is all the leads Mastermind podcast over 422. uh just so you '
             "all know uh Bruce has decided he'd rather go spend time with.",
      'title': 'Navigating the Competitive Probate Real Estate Market | Probate Mastermind '
               '#422 (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=9eNkvtVoeao&t=15s',
      'video_id': '9eNkvtVoeao'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=dzqHqDnAl_E&t=104s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I need to hit to get there?" And for me, at 24 probate and estate closings in a '
              "year, if it's all going to come, let's pretend it all comes out of a probate "
              "list. So there's no attorney referrals and things like that. It's just all from "
              'a probate list.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'I need to hit to get there?" And for me, at 24 probate and estate closings in a '
             "year, if it's all going to come, let's pretend it all comes out of a probate "
             "list. So there's no attorney referrals and things like that. It's just all from "
             'a probate list.',
      'title': 'How to Build a Successful Probate Real Estate Business & Generate Consistent '
               'Leads (2025) (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=dzqHqDnAl_E&t=104s',
      'video_id': 'dzqHqDnAl_E'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:15:01](https://www.youtube.com/watch?v=IRtAt7-sQHc&t=4501s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um but I I spent a lot of time filtering that list down to find people that '
              "have been in the middle of probate with vacant houses for a long time. If I'm "
              'doing a new list, I need to run a 6-month campaign at minimum. Um and there '
              'there were some other questions.',
      'timestamp': 4501,
      'timestamp_label': '[01:15:01]',
      'timestamp_seconds': 4501,
      'tip': 'Um but I I spent a lot of time filtering that list down to find people that have '
             "been in the middle of probate with vacant houses for a long time. If I'm doing a "
             'new list, I need to run a 6-month campaign at minimum. Um and there there were '
             'some other questions.',
      'title': 'Probate Direct Mail Marketing: Build Better Campaigns (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=IRtAt7-sQHc&t=4501s',
      'video_id': 'IRtAt7-sQHc'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=hxVdTk3sSHo&t=311s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Think that you really need to take anything with you okay I would probably show '
              "up to that first meeting look I'm trying to learn more about your practice um "
              'so that I can see if you might be a good fit for a few of my clients over the '
              'next couple of years a few.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': 'Think that you really need to take anything with you okay I would probably show '
             "up to that first meeting look I'm trying to learn more about your practice um so "
             'that I can see if you might be a good fit for a few of my clients over the next '
             'couple of years a few.',
      'title': 'Working with Probate Attorneys: What to Bring, What to Say, and What NOT to Do '
               '(Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=hxVdTk3sSHo&t=311s',
      'video_id': 'hxVdTk3sSHo'}],
 7: [{'author': 'SwiftProbate',
      'channel': 'SwiftProbate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=lAC-1ovhHAo&t=87s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If that person cannot serve, the court may appoint an alternate named in the '
              'will, or an administrator. The process varies by state and county, but the '
              'steps are similar. Step one: the original will and a certified death '
              'certificate.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'If that person cannot serve, the court may appoint an alternate named in the '
             'will, or an administrator. The process varies by state and county, but the steps '
             'are similar. Step one: the original will and a certified death certificate.',
      'title': 'Letters Testamentary Explained: What They Are and How to Get Them '
               '(SwiftProbate)',
      'url': 'https://www.youtube.com/watch?v=lAC-1ovhHAo&t=87s',
      'video_id': 'lAC-1ovhHAo'},
     {'author': "The Executor's Guide",
      'channel': "The Executor's Guide",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=HPpVk5fp1No&t=404s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So here is this step, in one breath. File in the probate court of the county '
              'where they legally lived: the original will, a certified death certificate, the '
              'petition, and the filing fee your clerk confirms. Notify the heirs and '
              'beneficiaries the way your state requires.',
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': 'So here is this step, in one breath. File in the probate court of the county '
             'where they legally lived: the original will, a certified death certificate, the '
             'petition, and the filing fee your clerk confirms. Notify the heirs and '
             'beneficiaries the way your state requires.',
      'title': 'Probate, Plain and Simple: Filing, Letters Testamentary, and Your First Court '
               "Steps (The Executor's Guide)",
      'url': 'https://www.youtube.com/watch?v=HPpVk5fp1No&t=404s',
      'video_id': 'HPpVk5fp1No'},
     {'author': 'MarcCormier',
      'channel': 'MarcCormier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=t0-A8dVrr1o&t=252s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I put all five steps on a free one-page checklist for Maryland, Virginia, DC. '
              'If your parents are still healthy, this is the part to act on. The worst '
              'do-it-yourself move is deeding the house to your kids for two reasons.',
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': 'I put all five steps on a free one-page checklist for Maryland, Virginia, DC. If '
             'your parents are still healthy, this is the part to act on. The worst '
             'do-it-yourself move is deeding the house to your kids for two reasons.',
      'title': 'Can Medicaid Take Your Parents’ House After They Die? (MarcCormier)',
      'url': 'https://www.youtube.com/watch?v=t0-A8dVrr1o&t=252s',
      'video_id': 't0-A8dVrr1o'},
     {'author': 'Law Office of Amanda L. Rocha',
      'channel': 'Law Office of Amanda L. Rocha',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=vslnvJCGR5c&t=22s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The I IAEA or Independent Administration and Estates Act is something that is '
              'used in California probate when you are going through the probate process. This '
              'allows you to act outside of the hand holding so to speak of the judge during '
              'probate.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'The I IAEA or Independent Administration and Estates Act is something that is '
             'used in California probate when you are going through the probate process. This '
             'allows you to act outside of the hand holding so to speak of the judge during '
             'probate.',
      'title': 'Independent Administration of Estates Act- IAEA (Law Office of Amanda L. '
               'Rocha)',
      'url': 'https://www.youtube.com/watch?v=vslnvJCGR5c&t=22s',
      'video_id': 'vslnvJCGR5c'},
     {'author': 'Alix',
      'channel': 'Alix',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=McUc7Xu_MHo&t=154s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step two: capital gains tax. Once someone inherits a home, there can be a lot '
              "of fear around getting hit with a huge capital gains tax bill. I'm here to let "
              "you know that most likely it’s not something you need to worry about. That's "
              'because the step-up in basis.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'Step two: capital gains tax. Once someone inherits a home, there can be a lot of '
             "fear around getting hit with a huge capital gains tax bill. I'm here to let you "
             "know that most likely it’s not something you need to worry about. That's because "
             'the step-up in basis.',
      'title': 'Selling Inherited Property: 4 Crucial Steps for Executors (Alix)',
      'url': 'https://www.youtube.com/watch?v=McUc7Xu_MHo&t=154s',
      'video_id': 'McUc7Xu_MHo'},
     {'author': 'Carolynn Castillo',
      'channel': 'Carolynn Castillo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:26](https://www.youtube.com/watch?v=ewbkVPWFtKM&t=1166s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, and the other thing that I would tell you um, in this process is um, not '
              'communicating with all the beneficiaries. So, you do want to make sure that '
              'they have the letters of testimony, they have the letters of administration.',
      'timestamp': 1166,
      'timestamp_label': '[00:19:26]',
      'timestamp_seconds': 1166,
      'tip': 'Um, and the other thing that I would tell you um, in this process is um, not '
             'communicating with all the beneficiaries. So, you do want to make sure that they '
             'have the letters of testimony, they have the letters of administration.',
      'title': 'What Is the Probate Process? A Step-by-Step Breakdown for Realtors (Carolynn '
               'Castillo)',
      'url': 'https://www.youtube.com/watch?v=ewbkVPWFtKM&t=1166s',
      'video_id': 'ewbkVPWFtKM'},
     {'author': 'Simplify Senior Transitions with Dale Corpus',
      'channel': 'Simplify Senior Transitions with Dale Corpus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=S5zYm8kcrug&t=40s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "San Mato San Francisco salano or Napa County this video is for you I'm Dale "
              'Corpus a senior transition specialist based in sanone California and I help '
              'families navigate the H selling process when transitioning a loved one into '
              "senior living let's get started.",
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "San Mato San Francisco salano or Napa County this video is for you I'm Dale "
             'Corpus a senior transition specialist based in sanone California and I help '
             'families navigate the H selling process when transitioning a loved one into '
             "senior living let's get started.",
      'title': 'What You Need to Know Before Selling a Senior’s Home (Legal, Financial & '
               'Emotional Considerations) (Simplify Senior Transitions with Dale Corpus)',
      'url': 'https://www.youtube.com/watch?v=S5zYm8kcrug&t=40s',
      'video_id': 'S5zYm8kcrug'},
     {'author': 'Tennessee Probate Realty Group',
      'channel': 'Tennessee Probate Realty Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=_VnXEkxAEO0&t=146s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Entire probate process the will must be submitted to the probate court for '
              'official approval this step also addresses potential will contest or.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Entire probate process the will must be submitted to the probate court for '
             'official approval this step also addresses potential will contest or.',
      'title': 'Understanding the Tennessee Probate Process (Tennessee Probate Realty Group)',
      'url': 'https://www.youtube.com/watch?v=_VnXEkxAEO0&t=146s',
      'video_id': '_VnXEkxAEO0'},
     {'author': 'ProbateBiz: Probate Real Estate Training',
      'channel': 'ProbateBiz: Probate Real Estate Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=cDuy_EpieeM&t=38s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So I have very specific steps on how I prepare myself to meet with my future '
              "client step one is to pull up all the information regarding the decedent's.",
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'So I have very specific steps on how I prepare myself to meet with my future '
             "client step one is to pull up all the information regarding the decedent's.",
      'title': 'Probate Real Estate | Probate Value vs Market Value (ProbateBiz: Probate Real '
               'Estate Training)',
      'url': 'https://www.youtube.com/watch?v=cDuy_EpieeM&t=38s',
      'video_id': 'cDuy_EpieeM'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:48](https://www.youtube.com/watch?v=9tTK_fAGgNE&t=1548s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That you cover these these steps of the checklist you can modify it that to '
              "specifically in your area but that's a that's a great way to to help and can be "
              'an easier part of the conversation to continue you know add value in advance.',
      'timestamp': 1548,
      'timestamp_label': '[00:25:48]',
      'timestamp_seconds': 1548,
      'tip': 'That you cover these these steps of the checklist you can modify it that to '
             "specifically in your area but that's a that's a great way to to help and can be "
             'an easier part of the conversation to continue you know add value in advance.',
      'title': 'Success in Probate Deals, Inheritance, and Property Clean Out | Probate '
               'Mastermind #426 (All The Leads)',
      'url': 'https://www.youtube.com/watch?v=9tTK_fAGgNE&t=1548s',
      'video_id': '9tTK_fAGgNE'},
     {'author': 'Justin Stivers',
      'channel': 'Justin Stivers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:23](https://www.youtube.com/watch?v=Owbx6t3ocjM&t=983s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Attorney and go through the probate process so that's sometimes how they update "
              "it so there's no I can't give you a 100% answer when they always update it.",
      'timestamp': 983,
      'timestamp_label': '[00:16:23]',
      'timestamp_seconds': 983,
      'tip': "Attorney and go through the probate process so that's sometimes how they update "
             "it so there's no I can't give you a 100% answer when they always update it.",
      'title': 'Probate 101 for Realtors (Justin Stivers)',
      'url': 'https://www.youtube.com/watch?v=Owbx6t3ocjM&t=983s',
      'video_id': 'Owbx6t3ocjM'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=PEzIdVcykYI&t=46s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'd much rather have a trust administration than a probate. Honestly the payout "
              "is just as, I mean, it's not as high in the trust administration, but you can "
              'close about five of those in the time that you can go through our terrible '
              'court system.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "I'd much rather have a trust administration than a probate. Honestly the payout "
             "is just as, I mean, it's not as high in the trust administration, but you can "
             'close about five of those in the time that you can go through our terrible court '
             'system.',
      'title': 'Attorney prospecting: Real estate agent/investor tips for probate vs. Estate '
               'planning referrals (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=PEzIdVcykYI&t=46s',
      'video_id': 'PEzIdVcykYI'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:43](https://www.youtube.com/watch?v=7FoxQuVXm2k&t=2983s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, they're going to be state side having a a a highlevel dialogue with someone "
              'to help them through the probate process. And all these are the reasons why '
              'each lead that I get in a county is normally going to cost me about $32 a lead.',
      'timestamp': 2983,
      'timestamp_label': '[00:49:43]',
      'timestamp_seconds': 2983,
      'tip': "So, they're going to be state side having a a a highlevel dialogue with someone "
             'to help them through the probate process. And all these are the reasons why each '
             'lead that I get in a county is normally going to cost me about $32 a lead.',
      'title': 'What Every Probate Real Estate Specialist Needs to Know Before Making Probate '
               'Their Main Focus (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=7FoxQuVXm2k&t=2983s',
      'video_id': '7FoxQuVXm2k'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=7NYfu3V_uSQ&t=264s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um I'm probably going to put some pages in there that are information about the "
              'probate process. So, maybe some information on what they need if they want to '
              'do a cash advance, maybe a page or two on securing real estate, securing '
              'assets.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': "Um I'm probably going to put some pages in there that are information about the "
             'probate process. So, maybe some information on what they need if they want to do '
             'a cash advance, maybe a page or two on securing real estate, securing assets.',
      'title': 'The Probate Letter That Actually Gets Callbacks (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=7NYfu3V_uSQ&t=264s',
      'video_id': '7NYfu3V_uSQ'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:33](https://www.youtube.com/watch?v=QU_nb_NyIhU&t=873s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The probate attorneys, they know exactly how to move a family from start to '
              'finish through the application process and get to uh settlement of probate and '
              'and the final accounting and get it closed. Do they know how to get clients?',
      'timestamp': 873,
      'timestamp_label': '[00:14:33]',
      'timestamp_seconds': 873,
      'tip': 'The probate attorneys, they know exactly how to move a family from start to '
             'finish through the application process and get to uh settlement of probate and '
             'and the final accounting and get it closed. Do they know how to get clients?',
      'title': 'Probate Real Estate Specialist Guide: How Realtors & Investors Build '
               'Predictable Income (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=QU_nb_NyIhU&t=873s',
      'video_id': 'QU_nb_NyIhU'}],
 8: [{'author': 'Sell a House in Probate California | Brendan Mohr',
      'channel': 'Sell a House in Probate California | Brendan Mohr',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=P4n8gqfBg3M&t=21s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Welcome back to the channel featuring the leading probate real estate team in '
              "all of California. I'm Brendan Moore, realtor, Masters Club Life member, and "
              'certified probate trust specialist by the California Association of Realtors.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Welcome back to the channel featuring the leading probate real estate team in '
             "all of California. I'm Brendan Moore, realtor, Masters Club Life member, and "
             'certified probate trust specialist by the California Association of Realtors.',
      'title': 'Can You Avoid Court Confirmation in Probate if an Heir Objects in California? '
               '| Brendan Mohr (Sell a House in Probate California | Brendan Mohr)',
      'url': 'https://www.youtube.com/watch?v=P4n8gqfBg3M&t=21s',
      'video_id': 'P4n8gqfBg3M'},
     {'author': 'RLS Law Corporation',
      'channel': 'RLS Law Corporation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:48](https://www.youtube.com/watch?v=lNaVAVnUZTE&t=528s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a kind of interesting little what occurs is a court confirmation sale, and "
              "it's a little auction in the courthouse.",
      'timestamp': 528,
      'timestamp_label': '[00:08:48]',
      'timestamp_seconds': 528,
      'tip': "'s a kind of interesting little what occurs is a court confirmation sale, and "
             "it's a little auction in the courthouse.",
      'title': 'How Long Does Probate Take in California? (RLS Law Corporation)',
      'url': 'https://www.youtube.com/watch?v=lNaVAVnUZTE&t=528s',
      'video_id': 'lNaVAVnUZTE'},
     {'author': 'Rick Ginn',
      'channel': 'Rick Ginn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:17:05](https://www.youtube.com/watch?v=WU_DwL7k5ZE&t=4625s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "10 real cash buyers is like having 500 cash buyer uh database. They're all "
              'Everyone I got 10,000 cash buyers. You got 9,990 wholesalers and you got about '
              "eight um wannabes in there and then maybe there's two real cash buyers.",
      'timestamp': 4625,
      'timestamp_label': '[01:17:05]',
      'timestamp_seconds': 4625,
      'tip': "10 real cash buyers is like having 500 cash buyer uh database. They're all "
             'Everyone I got 10,000 cash buyers. You got 9,990 wholesalers and you got about '
             "eight um wannabes in there and then maybe there's two real cash buyers.",
      'title': 'Mastering Probate Wholesaling: Your Ultimate Guide to Real Estate Success in '
               '2024 (Rick Ginn)',
      'url': 'https://www.youtube.com/watch?v=WU_DwL7k5ZE&t=4625s',
      'video_id': 'WU_DwL7k5ZE'},
     {'author': 'Real Estate Skills',
      'channel': 'Real Estate Skills',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=M9iyZc2j_uQ&t=143s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is my favorite software that's ever been invented. So the MLS stands for "
              "the Multiple Listing Service and it's a database of all properties on the "
              "market across the United States. Here's a quick example of the listing sheet.",
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': "This is my favorite software that's ever been invented. So the MLS stands for "
             "the Multiple Listing Service and it's a database of all properties on the market "
             "across the United States. Here's a quick example of the listing sheet.",
      'title': 'How To Start Wholesale Real Estate In 2027 (15hrs/wk)! (Real Estate Skills)',
      'url': 'https://www.youtube.com/watch?v=M9iyZc2j_uQ&t=143s',
      'video_id': 'M9iyZc2j_uQ'},
     {'author': 'The Aaron Novello Podcast',
      'channel': 'The Aaron Novello Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=H-CW9uu5s-I&t=260s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Go back home then she would uh look up the information put all of the data into '
              "let's say follow up boss cause that was a platform that we used even though "
              'they just changed a rule recently.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Go back home then she would uh look up the information put all of the data into '
             "let's say follow up boss cause that was a platform that we used even though they "
             'just changed a rule recently.',
      'title': 'How to Get Probate Real Estate Listings (The "Courthouse" Strategy) (The Aaron '
               'Novello Podcast)',
      'url': 'https://www.youtube.com/watch?v=H-CW9uu5s-I&t=260s',
      'video_id': 'H-CW9uu5s-I'},
     {'author': 'Maximilian Dier',
      'channel': 'Maximilian Dier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:22](https://www.youtube.com/watch?v=LeQ9QiM4CLo&t=1342s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Again, I got to be careful about what I show you. You go, you know, go back to '
              "your software, and then I'll quickly skip trace, let's say, the kids address. "
              "That's where actually one of the kids lives. Pretty crazy that you can get all "
              'this data.',
      'timestamp': 1342,
      'timestamp_label': '[00:22:22]',
      'timestamp_seconds': 1342,
      'tip': 'Again, I got to be careful about what I show you. You go, you know, go back to '
             "your software, and then I'll quickly skip trace, let's say, the kids address. "
             "That's where actually one of the kids lives. Pretty crazy that you can get all "
             'this data.',
      'title': 'How to Wholesale Probate Properties (Step by Step) 💀 (Maximilian Dier)',
      'url': 'https://www.youtube.com/watch?v=LeQ9QiM4CLo&t=1342s',
      'video_id': 'LeQ9QiM4CLo'},
     {'author': 'Duc Minh Lam',
      'channel': 'Duc Minh Lam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:52](https://www.youtube.com/watch?v=1UT8pIVtejc&t=352s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "When you're right in the middle of a major life transition, complete peace of "
              "mind is exactly what you need. It's way more than just selling a house. It's "
              "about managing a crisis with absolute authority. Let's talk numbers cuz the "
              'data here is just incredible.',
      'timestamp': 352,
      'timestamp_label': '[00:05:52]',
      'timestamp_seconds': 352,
      'tip': "When you're right in the middle of a major life transition, complete peace of "
             "mind is exactly what you need. It's way more than just selling a house. It's "
             "about managing a crisis with absolute authority. Let's talk numbers cuz the data "
             'here is just incredible.',
      'title': 'California Probate Sales: Managing Property During Estate Transitions (Duc '
               'Minh Lam)',
      'url': 'https://www.youtube.com/watch?v=1UT8pIVtejc&t=352s',
      'video_id': '1UT8pIVtejc'},
     {'author': 'Michelle Bell - Realtor',
      'channel': 'Michelle Bell - Realtor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=F1mwNdsm-HA&t=107s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also, have the estate lawyer confirm how a buyout could work under the will and '
              'who has the to make all of the arrangements. The house might still belong to '
              'the estate or it might have already been transferred to the beneficiaries. That '
              'will affect how it moves forward.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'Also, have the estate lawyer confirm how a buyout could work under the will and '
             'who has the to make all of the arrangements. The house might still belong to the '
             'estate or it might have already been transferred to the beneficiaries. That will '
             'affect how it moves forward.',
      'title': 'How to Buy Out Your Siblings When You Inherit a House (Ontario) (Michelle Bell '
               '- Realtor)',
      'url': 'https://www.youtube.com/watch?v=F1mwNdsm-HA&t=107s',
      'video_id': 'F1mwNdsm-HA'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:51](https://www.youtube.com/watch?v=kOa87jAYRNs&t=591s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So they think we don't need an attorney. And so there's an opportunity to "
              'comarket through. Certified probate experts who are direct marketing through '
              'email, through direct mail, through outbound phone campaigns.',
      'timestamp': 591,
      'timestamp_label': '[00:09:51]',
      'timestamp_seconds': 591,
      'tip': "So they think we don't need an attorney. And so there's an opportunity to "
             'comarket through. Certified probate experts who are direct marketing through '
             'email, through direct mail, through outbound phone campaigns.',
      'title': 'How to prospect attorneys and build impactful referral relationships in the '
               'estate planning space (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=kOa87jAYRNs&t=591s',
      'video_id': 'kOa87jAYRNs'},
     {'author': 'Executorium',
      'channel': 'Executorium',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=aHu-G7VTUnc&t=102s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well as my 84y old grandfather um all worked together to uh start downsizing my '
              "father's estate that being said um there's certainly some things especially.",
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Well as my 84y old grandfather um all worked together to uh start downsizing my '
             "father's estate that being said um there's certainly some things especially.",
      'title': 'Talking Estate Cleanouts: Executor to Estate Cleanout Pro (Executorium)',
      'url': 'https://www.youtube.com/watch?v=aHu-G7VTUnc&t=102s',
      'video_id': 'aHu-G7VTUnc'},
     {'author': 'Bill Gross, the LA Probate Expert',
      'channel': 'Bill Gross, the LA Probate Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:42](https://www.youtube.com/watch?v=4hp5f-_boUM&t=1602s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Done you let us know if any when something needs signed and you can literally i '
              'mean these were the fastest cash conversion deals.',
      'timestamp': 1602,
      'timestamp_label': '[00:26:42]',
      'timestamp_seconds': 1602,
      'tip': 'Done you let us know if any when something needs signed and you can literally i '
             'mean these were the fastest cash conversion deals.',
      'title': 'Interview with Chad Corbett (Bill Gross, the LA Probate Expert)',
      'url': 'https://www.youtube.com/watch?v=4hp5f-_boUM&t=1602s',
      'video_id': '4hp5f-_boUM'},
     {'author': 'Selling Inherited Property - The Prepared Heir',
      'channel': 'Selling Inherited Property - The Prepared Heir',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:36](https://www.youtube.com/watch?v=dtCGp46sZEg&t=396s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Consider liking the video and subscribing to our Channel and I'm not asking you "
              'to do any of this for a vanity Matrix It sincerely helps me know what questions '
              "you have and what's important to you thank you for watching and I'll see you "
              'next week.',
      'timestamp': 396,
      'timestamp_label': '[00:06:36]',
      'timestamp_seconds': 396,
      'tip': "Consider liking the video and subscribing to our Channel and I'm not asking you "
             'to do any of this for a vanity Matrix It sincerely helps me know what questions '
             "you have and what's important to you thank you for watching and I'll see you "
             'next week.',
      'title': 'Sibling Showdown! How To Buyout Your Sibling On Inherited Property | '
               'Sacramento County (Selling Inherited Property - The Prepared Heir)',
      'url': 'https://www.youtube.com/watch?v=dtCGp46sZEg&t=396s',
      'video_id': 'dtCGp46sZEg'},
     {'author': '23ABC News | KERO',
      'channel': '23ABC News | KERO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=uvfLAJ4V3PM&t=103s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Appreciate a teapot or a painting just warms our hearts as for Mom's old stove "
              "it's still here in the family house and Melissa hopes a new family will love it "
              "that way you don't waste your money I'm John mataris foreign.",
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "Appreciate a teapot or a painting just warms our hearts as for Mom's old stove "
             "it's still here in the family house and Melissa hopes a new family will love it "
             "that way you don't waste your money I'm John mataris foreign.",
      'title': "Finding an Estate Sale Company | DON'T WASTE YOUR MONEY (23ABC News | KERO)",
      'url': 'https://www.youtube.com/watch?v=uvfLAJ4V3PM&t=103s',
      'video_id': 'uvfLAJ4V3PM'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:26](https://www.youtube.com/watch?v=NH2VGynt0Wk&t=746s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And guide you through this and the, into a niche where you're not blowing all "
              'of your money on internet leads and figuring out which text is going to work '
              "and which email and which CRM and all of this. It's a focused conversation on "
              'taking a part of society.',
      'timestamp': 746,
      'timestamp_label': '[00:12:26]',
      'timestamp_seconds': 746,
      'tip': "And guide you through this and the, into a niche where you're not blowing all of "
             'your money on internet leads and figuring out which text is going to work and '
             "which email and which CRM and all of this. It's a focused conversation on taking "
             'a part of society.',
      'title': 'Ending The Real Estate Feast Or Famine and Building a Successful Business | '
               'Certified Probate Course (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=NH2VGynt0Wk&t=746s',
      'video_id': 'NH2VGynt0Wk'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=0oMatPnporI&t=101s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'March or sorry april it closed but her and her husband are moving to north '
              'carolina to be with their son and she called me up and said we want you to sell '
              "right so that's amazing the indirect.",
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'March or sorry april it closed but her and her husband are moving to north '
             'carolina to be with their son and she called me up and said we want you to sell '
             "right so that's amazing the indirect.",
      'title': 'How to become a probate real estate agent - 5 probate listings! Probate '
               'Training with Chad Corbett (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=0oMatPnporI&t=101s',
      'video_id': '0oMatPnporI'}],
 9: [{'author': 'The Legacy Desk',
      'channel': 'The Legacy Desk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=qlBYQPngO0o&t=40s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To answer it, we'll follow one house along a timeline, from the day it's bought "
              'to the day an heir sells it, using federal tax law and Internal Revenue Service '
              'publications. This is general education, not legal advice. Talk to a licensed '
              'attorney in your state.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "To answer it, we'll follow one house along a timeline, from the day it's bought "
             'to the day an heir sells it, using federal tax law and Internal Revenue Service '
             'publications. This is general education, not legal advice. Talk to a licensed '
             'attorney in your state.',
      'title': 'Do I Pay Capital Gains on an Inherited House? (The Legacy Desk)',
      'url': 'https://www.youtube.com/watch?v=qlBYQPngO0o&t=40s',
      'video_id': 'qlBYQPngO0o'},
     {'author': 'Gyd Path',
      'channel': 'Gyd Path',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=AMYbwbqYqY8&t=412s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before accepting more work, you add family access rules to the revised '
              'contract. Level four, full-service estate sale company. You sit across the '
              'probate folder while heirs debate commission terms. At the branded box truck, '
              'you direct the crew loading dollies and racks.',
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': 'Before accepting more work, you add family access rules to the revised contract. '
             'Level four, full-service estate sale company. You sit across the probate folder '
             'while heirs debate commission terms. At the branded box truck, you direct the '
             'crew loading dollies and racks.',
      'title': 'What Happens If You Start an Estate Sale Company (Gyd Path)',
      'url': 'https://www.youtube.com/watch?v=AMYbwbqYqY8&t=412s',
      'video_id': 'AMYbwbqYqY8'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:39](https://www.youtube.com/watch?v=evd32pAim5s&t=819s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so that part is open to the public in California by law. So anybody can go '
              'in there. Uh, so I would just check and it might be that you went in on a court '
              'date, El Paso County, Colorado.',
      'timestamp': 819,
      'timestamp_label': '[00:13:39]',
      'timestamp_seconds': 819,
      'tip': 'And so that part is open to the public in California by law. So anybody can go '
             'in there. Uh, so I would just check and it might be that you went in on a court '
             'date, El Paso County, Colorado.',
      'title': 'How to Get a Probate Attorney Referral (Timing + Nurture Tips) (Probate '
               'Mastery)',
      'url': 'https://www.youtube.com/watch?v=evd32pAim5s&t=819s',
      'video_id': 'evd32pAim5s'},
     {'author': 'Local Probate Help',
      'channel': 'Local Probate Help',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=Bggg_tJ_y2g&t=175s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You may want to make sure the property even has the appropriate protection in '
              'place. Of course, any repairs, access changes, or maintenance arrangements '
              'should really be coordinated with someone who has the legal authority to act. '
              'Now, this is very important.',
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'You may want to make sure the property even has the appropriate protection in '
             'place. Of course, any repairs, access changes, or maintenance arrangements '
             'should really be coordinated with someone who has the legal authority to act. '
             'Now, this is very important.',
      'title': 'Can You Clean Out an Inherited House Before Probate in California? (Local '
               'Probate Help)',
      'url': 'https://www.youtube.com/watch?v=Bggg_tJ_y2g&t=175s',
      'video_id': 'Bggg_tJ_y2g'},
     {'author': 'The Accidental Executor',
      'channel': 'The Accidental Executor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=JsLnTFCaOUQ&t=42s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When someone dies without a will and nobody opens probate, the law still '
              'decides who inherits. State intestacy rules give the property to the heirs, '
              'usually the spouse and children as tenants in common. Each one owns a '
              "fractional share. Nobody's name gets put on the deed.",
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'When someone dies without a will and nobody opens probate, the law still decides '
             'who inherits. State intestacy rules give the property to the heirs, usually the '
             'spouse and children as tenants in common. Each one owns a fractional share. '
             "Nobody's name gets put on the deed.",
      'title': "Heirs' Property: The Trap That Costs Families Their Land (The Accidental "
               'Executor)',
      'url': 'https://www.youtube.com/watch?v=JsLnTFCaOUQ&t=42s',
      'video_id': 'JsLnTFCaOUQ'},
     {'author': 'American Estate Planning Series',
      'channel': 'American Estate Planning Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Hi5epLariAQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Involved in a probate so I'm I'm Paul Rabelais I'm gonna state planning "
              'attorney I help our clients get and keep their legal affairs in order and '
              "there's.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Involved in a probate so I'm I'm Paul Rabelais I'm gonna state planning attorney "
             "I help our clients get and keep their legal affairs in order and there's.",
      'title': 'Probate Process From Start To Finish (American Estate Planning Series)',
      'url': 'https://www.youtube.com/watch?v=Hi5epLariAQ&t=15s',
      'video_id': 'Hi5epLariAQ'},
     {'author': 'The Aaron Novello Podcast',
      'channel': 'The Aaron Novello Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=44RbpWBPcbI&t=70s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, one of the ones that I like the most, it's served me very well. I told Jose "
              'that statistic in 2025, 20% of all sales in the state of California were '
              'probate after somebody passed away.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': "So, one of the ones that I like the most, it's served me very well. I told Jose "
             'that statistic in 2025, 20% of all sales in the state of California were probate '
             'after somebody passed away.',
      'title': 'The Probate Lead Strategy That Made This Real Estate Agent $50K (The Aaron '
               'Novello Podcast)',
      'url': 'https://www.youtube.com/watch?v=44RbpWBPcbI&t=70s',
      'video_id': '44RbpWBPcbI'},
     {'author': 'Win-Win Realtors TV',
      'channel': 'Win-Win Realtors TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=L_bEDREJSKQ&t=282s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Been for information purposes only it is not to be misconstrued as legal advice '
              'if you need legal advice contact an attorney if you need an estate planning or '
              'probate attorney feel free to contact me for a referral.',
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': 'Been for information purposes only it is not to be misconstrued as legal advice '
             'if you need legal advice contact an attorney if you need an estate planning or '
             'probate attorney feel free to contact me for a referral.',
      'title': 'WHAT IS A  COURT CONFIRMATION OF THE SALE OF REAL PROPERTY?  #Probate '
               '#executor #administrator (Win-Win Realtors TV)',
      'url': 'https://www.youtube.com/watch?v=L_bEDREJSKQ&t=282s',
      'video_id': 'L_bEDREJSKQ'},
     {'author': 'นพดล เกิดยิ้ม',
      'channel': 'นพดล เกิดยิ้ม',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=X-vkv-PR3pY&t=140s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No state takes your house the day you sign up for Medicaid. But what is real '
              "has a name. The Medicaid Estate Recovery Program, MERP. It's required under "
              'federal law OBRA 1993 and it applies to anyone 55 or older who received '
              'long-term care through Medicaid.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'No state takes your house the day you sign up for Medicaid. But what is real has '
             "a name. The Medicaid Estate Recovery Program, MERP. It's required under federal "
             'law OBRA 1993 and it applies to anyone 55 or older who received long-term care '
             'through Medicaid.',
      'title': "State Just Changed 3 Medicaid Estate Recovery Rules: Here's What Every "
               'Homeowner Must Do (นพดล เกิดยิ้ม)',
      'url': 'https://www.youtube.com/watch?v=X-vkv-PR3pY&t=140s',
      'video_id': 'X-vkv-PR3pY'},
     {'author': 'Wanda Rochelle, Probate Resource',
      'channel': 'Wanda Rochelle, Probate Resource',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=Ghymi1mvrRQ&t=86s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Filed how long would that take every probate case is different so it's "
              "difficult to say let's take a look at a sample letter of administration so you "
              'can see what it looks like I have one for you for the state of Georgia.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': "Filed how long would that take every probate case is different so it's difficult "
             "to say let's take a look at a sample letter of administration so you can see "
             'what it looks like I have one for you for the state of Georgia.',
      'title': 'Probate From Start To Finish | How To Get Probate Letters | Probate Realtor | '
               'Probate Real Estate (Wanda Rochelle, Probate Resource)',
      'url': 'https://www.youtube.com/watch?v=Ghymi1mvrRQ&t=86s',
      'video_id': 'Ghymi1mvrRQ'},
     {'author': 'Lawyer Greg McIntyre',
      'channel': 'Lawyer Greg McIntyre',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=T42HfbxscSQ&t=101s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Property other state planning strategies in a free consultation our telephone '
              'number is 888999 6600 or you can visit our website at mcelder law.com '
              "scheduling please don't wait till it's too late McIntyre Elder love.",
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'Property other state planning strategies in a free consultation our telephone '
             'number is 888999 6600 or you can visit our website at mcelder law.com scheduling '
             "please don't wait till it's too late McIntyre Elder love.",
      'title': 'What is Heir Property? (Lawyer Greg McIntyre)',
      'url': 'https://www.youtube.com/watch?v=T42HfbxscSQ&t=101s',
      'video_id': 'T42HfbxscSQ'},
     {'author': 'Rilus Law',
      'channel': 'Rilus Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=CxNRQb9rqlw&t=64s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Some basics about about probate and we'll go from there so step one you've got "
              'to define the players get some of the key terms decedent or or dead person.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': "Some basics about about probate and we'll go from there so step one you've got "
             'to define the players get some of the key terms decedent or or dead person.',
      'title': 'Probate and Real Estate - Why Attorneys should work with Investors (Rilus Law)',
      'url': 'https://www.youtube.com/watch?v=CxNRQb9rqlw&t=64s',
      'video_id': 'CxNRQb9rqlw'},
     {'author': 'Realestate Doru',
      'channel': 'Realestate Doru',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:24](https://www.youtube.com/watch?v=kVqHwTzx-bo&t=384s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Could be credit cards anything you know - beautiful - somebody has 90 days of '
              'stuff up so if a house is worth 100,000 and credits are saying that you owe.',
      'timestamp': 384,
      'timestamp_label': '[00:06:24]',
      'timestamp_seconds': 384,
      'tip': 'Could be credit cards anything you know - beautiful - somebody has 90 days of '
             'stuff up so if a house is worth 100,000 and credits are saying that you owe.',
      'title': 'Probate Real Estate Investing | Law Clerk on Demand (Realestate Doru)',
      'url': 'https://www.youtube.com/watch?v=kVqHwTzx-bo&t=384s',
      'video_id': 'kVqHwTzx-bo'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=76c0h_es98E&t=32s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so, um, generally they're going to say, I um um uh focus my practice is "
              'built on estates and probate or estates and wills or something like that. And '
              'that um that attorney um generally wants estate planning pre-death and estate '
              'administration post death.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "And so, um, generally they're going to say, I um um uh focus my practice is "
             'built on estates and probate or estates and wills or something like that. And '
             'that um that attorney um generally wants estate planning pre-death and estate '
             'administration post death.',
      'title': 'Get Real Estate LISTINGS From PROBATE Attorneys (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=76c0h_es98E&t=32s',
      'video_id': '76c0h_es98E'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:23](https://www.youtube.com/watch?v=O0ZquS92FrQ&t=443s)',
      'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                   'acquisitions, executor concierge services, and probate-attorney referral '
                   'flywheels (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Support magnumopusproject.com and one of our team members will get back to you '
              'immediately thanks so much guys and welcome to the magnum opus project.',
      'timestamp': 443,
      'timestamp_label': '[00:07:23]',
      'timestamp_seconds': 443,
      'tip': 'Support magnumopusproject.com and one of our team members will get back to you '
             'immediately thanks so much guys and welcome to the magnum opus project.',
      'title': 'The Magnum Opus Project with Chad Corbett (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=O0ZquS92FrQ&t=443s',
      'video_id': 'O0ZquS92FrQ'}],
 10: [{'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:36](https://www.youtube.com/watch?v=URZzrpQSKmU&t=1356s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So I respect and appreciate all you guys for being in program here with Chad '
               'and Pinell and bettering yourself. If you feel like I can help come join me at '
               'agent mastery live, but agent mastery live.',
       'timestamp': 1356,
       'timestamp_label': '[00:22:36]',
       'timestamp_seconds': 1356,
       'tip': 'So I respect and appreciate all you guys for being in program here with Chad '
              'and Pinell and bettering yourself. If you feel like I can help come join me at '
              'agent mastery live, but agent mastery live.',
       'title': 'Speaking to Probate Sellers with Kevin Ward, Chad Corbett | Probate Script '
                'for Cold Calling (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=URZzrpQSKmU&t=1356s',
       'video_id': 'URZzrpQSKmU'},
      {'author': 'Wealth Pilot',
       'channel': 'Wealth Pilot',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:29](https://www.youtube.com/watch?v=osCrPBaE5OY&t=809s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'When a contract collapses after weeks of coordinated work, the brokerage loses '
               'the commission it was counting on, but it does not get back the money already '
               'spent on photography, marketing, transaction coordination and agent time. '
               'Every failed deal is a net cash loss.',
       'timestamp': 809,
       'timestamp_label': '[00:13:29]',
       'timestamp_seconds': 809,
       'tip': 'When a contract collapses after weeks of coordinated work, the brokerage loses '
              'the commission it was counting on, but it does not get back the money already '
              'spent on photography, marketing, transaction coordination and agent time. Every '
              'failed deal is a net cash loss.',
       'title': 'The Economics of Owning a Real Estate Business (Wealth Pilot)',
       'url': 'https://www.youtube.com/watch?v=osCrPBaE5OY&t=809s',
       'video_id': 'osCrPBaE5OY'},
      {'author': 'Your Dose of Real Estate With Tristan Ahumada',
       'channel': 'Your Dose of Real Estate With Tristan Ahumada',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:57](https://www.youtube.com/watch?v=jfeGte-B2tk&t=357s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ll create a nice actual visual beautiful presentation or beautiful AI. Damn, "
               'so much to go to, right? Step number three, build trust through shared '
               'education. All right, this is where I want you to invite the attorney to '
               'coffee or lunch.',
       'timestamp': 357,
       'timestamp_label': '[00:05:57]',
       'timestamp_seconds': 357,
       'tip': "'ll create a nice actual visual beautiful presentation or beautiful AI. Damn, "
              'so much to go to, right? Step number three, build trust through shared '
              'education. All right, this is where I want you to invite the attorney to coffee '
              'or lunch.',
       'title': 'Real Estate Agents: Turn Probate Lawyers into Referral Partners (Your Dose of '
                'Real Estate With Tristan Ahumada)',
       'url': 'https://www.youtube.com/watch?v=jfeGte-B2tk&t=357s',
       'video_id': 'jfeGte-B2tk'},
      {'author': 'Sell a House in Probate California | Brendan Mohr',
       'channel': 'Sell a House in Probate California | Brendan Mohr',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:17](https://www.youtube.com/watch?v=G-_4Dz5R2z8&t=197s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Full Authority no court confirmation required uh 18 to 30 days is very very '
               "common and it's very doable and it's very doable.",
       'timestamp': 197,
       'timestamp_label': '[00:03:17]',
       'timestamp_seconds': 197,
       'tip': 'Full Authority no court confirmation required uh 18 to 30 days is very very '
              "common and it's very doable and it's very doable.",
       'title': 'What is a Probate Sale Without Court Confirmation | Full Authority | Brendan '
                'Mohr (Sell a House in Probate California | Brendan Mohr)',
       'url': 'https://www.youtube.com/watch?v=G-_4Dz5R2z8&t=197s',
       'video_id': 'G-_4Dz5R2z8'},
      {'author': 'BatchTV',
       'channel': 'BatchTV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=xF9PxjJDUX0&t=94s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Business whether you're using batch leads as a real estate agent if you're "
               'wholesaling whatever the case might be you can almost completely wipe these.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': "Business whether you're using batch leads as a real estate agent if you're "
              'wholesaling whatever the case might be you can almost completely wipe these.',
       'title': 'Direct Mail Hacks: A Step-by-Step Guide (BatchTV)',
       'url': 'https://www.youtube.com/watch?v=xF9PxjJDUX0&t=94s',
       'video_id': 'xF9PxjJDUX0'},
      {'author': 'Grow with Juan Polanco',
       'channel': 'Grow with Juan Polanco',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:03](https://www.youtube.com/watch?v=B4TEVmeFhLk&t=363s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI thing now the mentorship programs that we is out there the coaching '
               'information new information now you know anybody can uh you know do this '
               "business I I absolutely I I think it's doable because now it's much easier.",
       'timestamp': 363,
       'timestamp_label': '[00:06:03]',
       'timestamp_seconds': 363,
       'tip': 'AI thing now the mentorship programs that we is out there the coaching '
              'information new information now you know anybody can uh you know do this '
              "business I I absolutely I I think it's doable because now it's much easier.",
       'title': 'How to Become a Real Estate Agent in 2026 | What Beginners Need to Know (Grow '
                'with Juan Polanco)',
       'url': 'https://www.youtube.com/watch?v=B4TEVmeFhLk&t=363s',
       'video_id': 'B4TEVmeFhLk'},
      {'author': 'Win-Win Realtors TV',
       'channel': 'Win-Win Realtors TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:33](https://www.youtube.com/watch?v=nenCgIcDQpw&t=93s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'While waiting on the confirmation of sales date the listing agent continues to '
               "market the property in order to get maximum dollar for the estate they're "
               'going to market that property for overbids on the property on the date of the '
               'confirmation sale.',
       'timestamp': 93,
       'timestamp_label': '[00:01:33]',
       'timestamp_seconds': 93,
       'tip': 'While waiting on the confirmation of sales date the listing agent continues to '
              "market the property in order to get maximum dollar for the estate they're going "
              'to market that property for overbids on the property on the date of the '
              'confirmation sale.',
       'title': 'HOW TO MAKE AN OVERBID ON A PROBATE PROPERTY IN CALIFORNIA? (Win-Win Realtors '
                'TV)',
       'url': 'https://www.youtube.com/watch?v=nenCgIcDQpw&t=93s',
       'video_id': 'nenCgIcDQpw'},
      {'author': 'Probate Place',
       'channel': 'Probate Place',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:46](https://www.youtube.com/watch?v=AEDxCUhuyaQ&t=46s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'With letters testamentary, the judge admits the will and appoints an executor '
               "or administrator, who receives letters, the court papers showing who's in "
               'charge. With a muniment of title, the judge admits the will without opening an '
               'administration.',
       'timestamp': 46,
       'timestamp_label': '[00:00:46]',
       'timestamp_seconds': 46,
       'tip': 'With letters testamentary, the judge admits the will and appoints an executor '
              "or administrator, who receives letters, the court papers showing who's in "
              'charge. With a muniment of title, the judge admits the will without opening an '
              'administration.',
       'title': 'What is probate in Texas? (Probate Place)',
       'url': 'https://www.youtube.com/watch?v=AEDxCUhuyaQ&t=46s',
       'video_id': 'AEDxCUhuyaQ'},
      {'author': 'Rick Ginn',
       'channel': 'Rick Ginn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:49:27](https://www.youtube.com/watch?v=LqNx0dBk2f8&t=2967s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Well crap, I don't have a buyer. Now I can go in like hyper speed mode and try "
               "to find a buyer in the next 30 days. It might take you 60, but the thing's "
               "vacant. You have it under a lock box and all these people coming in, there's "
               'just zero resistance.',
       'timestamp': 2967,
       'timestamp_label': '[00:49:27]',
       'timestamp_seconds': 2967,
       'tip': "Well crap, I don't have a buyer. Now I can go in like hyper speed mode and try "
              "to find a buyer in the next 30 days. It might take you 60, but the thing's "
              "vacant. You have it under a lock box and all these people coming in, there's "
              'just zero resistance.',
       'title': 'Mastering Probate Wholesaling: Your Ultimate Guide to Real Estate Success in '
                '2026 (Rick Ginn)',
       'url': 'https://www.youtube.com/watch?v=LqNx0dBk2f8&t=2967s',
       'video_id': 'LqNx0dBk2f8'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:42](https://www.youtube.com/watch?v=bTg9P9DMD1U&t=1362s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I talk to agents who call me all the time, off offline and say, how do I build '
               'my business? How do I build a real estate business in probate and into their '
               'experience agent? The first thing I always go to is have you done some probate '
               'business?',
       'timestamp': 1362,
       'timestamp_label': '[00:22:42]',
       'timestamp_seconds': 1362,
       'tip': 'I talk to agents who call me all the time, off offline and say, how do I build '
              'my business? How do I build a real estate business in probate and into their '
              'experience agent? The first thing I always go to is have you done some probate '
              'business?',
       'title': 'Real Estate Referral Networking Ideas: Probate real estate coaching (Probate '
                'Mastery)',
       'url': 'https://www.youtube.com/watch?v=bTg9P9DMD1U&t=1362s',
       'video_id': 'bTg9P9DMD1U'},
      {'author': 'American Estate Planning Series',
       'channel': 'American Estate Planning Series',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=CnMSGOG8ey0&t=15s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Letters are and how to get them all right so this has happened to me hundreds '
               'and hundreds of times over the years we get a call after.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Letters are and how to get them all right so this has happened to me hundreds '
              'and hundreds of times over the years we get a call after.',
       'title': 'Probate Letters: How To Get These Magic Papers (American Estate Planning '
                'Series)',
       'url': 'https://www.youtube.com/watch?v=CnMSGOG8ey0&t=15s',
       'video_id': 'CnMSGOG8ey0'},
      {'author': 'Bill Gross, the LA Probate Expert',
       'channel': 'Bill Gross, the LA Probate Expert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:55](https://www.youtube.com/watch?v=3VpuIk5nId0&t=835s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What came out of me option one cash offer 88 000. you saw the physical flinch '
               'it hurt her.',
       'timestamp': 835,
       'timestamp_label': '[00:13:55]',
       'timestamp_seconds': 835,
       'tip': 'What came out of me option one cash offer 88 000. you saw the physical flinch '
              'it hurt her.',
       'title': 'Chad Corbett on Probate Weekly with Bill Gross (Bill Gross, the LA Probate '
                'Expert)',
       'url': 'https://www.youtube.com/watch?v=3VpuIk5nId0&t=835s',
       'video_id': '3VpuIk5nId0'},
      {'author': 'Community Legal Services of Philadelphia',
       'channel': 'Community Legal Services of Philadelphia',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:56](https://www.youtube.com/watch?v=306n65tYnxQ&t=536s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your spouse child parent sibling or grandchild DPW May wave aate recovery you '
               'should contact us with any questions and to learn more about hardship.',
       'timestamp': 536,
       'timestamp_label': '[00:08:56]',
       'timestamp_seconds': 536,
       'tip': 'Your spouse child parent sibling or grandchild DPW May wave aate recovery you '
              'should contact us with any questions and to learn more about hardship.',
       'title': 'Medicaid Estate Recovery: A Primer (Community Legal Services of Philadelphia)',
       'url': 'https://www.youtube.com/watch?v=306n65tYnxQ&t=536s',
       'video_id': '306n65tYnxQ'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=_T085ecA9bI&t=146s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Part of the magnum opus course library thanks so much and I look forward to '
               'bringing this course to you and hopefully really really helping you scale your '
               "business up beyond where it's where it is now thanks so much and have a great "
               'day.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Part of the magnum opus course library thanks so much and I look forward to '
              'bringing this course to you and hopefully really really helping you scale your '
              "business up beyond where it's where it is now thanks so much and have a great "
              'day.',
       'title': 'EARN ATTORNEY REFERRALS NOW: New Course for Real Estate Professionals '
                '(Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=_T085ecA9bI&t=146s',
       'video_id': '_T085ecA9bI'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:49:25](https://www.youtube.com/watch?v=6dyFJnKpQDI&t=2965s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm glad to hear it Frank you want to share any of the successes you had uh "
               'with a group you want to jump on the car real quick.',
       'timestamp': 2965,
       'timestamp_label': '[00:49:25]',
       'timestamp_seconds': 2965,
       'tip': "I'm glad to hear it Frank you want to share any of the successes you had uh "
              'with a group you want to jump on the car real quick.',
       'title': 'Build Your Credibility as a Probate Professional (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=6dyFJnKpQDI&t=2965s',
       'video_id': '6dyFJnKpQDI'}],
 11: [{'author': 'Sell a House in Probate California | Brendan Mohr',
       'channel': 'Sell a House in Probate California | Brendan Mohr',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:18](https://www.youtube.com/watch?v=8b2qxYk3wDs&t=18s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Next welcome back to the channel featuring the leading probate real estate '
               "team in all of California I'm Brendan Moore realtor and certified.",
       'timestamp': 18,
       'timestamp_label': '[00:00:18]',
       'timestamp_seconds': 18,
       'tip': 'Next welcome back to the channel featuring the leading probate real estate team '
              "in all of California I'm Brendan Moore realtor and certified.",
       'title': 'What Is a Probate Real Estate Auction in California? | Brendan Mohr (Sell a '
                'House in Probate California | Brendan Mohr)',
       'url': 'https://www.youtube.com/watch?v=8b2qxYk3wDs&t=18s',
       'video_id': '8b2qxYk3wDs'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:48:45](https://www.youtube.com/watch?v=hBucLBjJpwg&t=2925s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, for for us, we have our letters that go out very consistently, all the '
               "attorney stuff. I'm hiring Bruce's team to do my calls for me. Um, I have a TC "
               'that helps me with my transa transactions. I have viral marketing that helps '
               'me with my videos.',
       'timestamp': 2925,
       'timestamp_label': '[00:48:45]',
       'timestamp_seconds': 2925,
       'tip': 'So, for for us, we have our letters that go out very consistently, all the '
              "attorney stuff. I'm hiring Bruce's team to do my calls for me. Um, I have a TC "
              'that helps me with my transa transactions. I have viral marketing that helps me '
              'with my videos.',
       'title': 'Probate Attorney Referral Tips and Probate Attorney Referral Methods (Probate '
                'Mastery)',
       'url': 'https://www.youtube.com/watch?v=hBucLBjJpwg&t=2925s',
       'video_id': 'hBucLBjJpwg'},
      {'author': 'Ariana Jay',
       'channel': 'Ariana Jay',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=cxcqaoT1cxQ&t=15s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Is Ariana J I help those who want to start grow or scale their licensed '
               'Assisted Living group home or Community have business do so and build well '
               "we're.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Is Ariana J I help those who want to start grow or scale their licensed '
              'Assisted Living group home or Community have business do so and build well '
              "we're.",
       'title': 'How to start a licensed residential assisted living, Step by Step. (Ariana '
                'Jay)',
       'url': 'https://www.youtube.com/watch?v=cxcqaoT1cxQ&t=15s',
       'video_id': 'cxcqaoT1cxQ'},
      {'author': 'The Sanborn Team',
       'channel': 'The Sanborn Team',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:35](https://www.youtube.com/watch?v=-1OrRi_sTzA&t=215s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Get the property you want if you are unfamiliar with Probate Court proceedings '
               'if you have any doubts about how to present your offer or if you just want to '
               'hear it all again call the sandborn team the sandborn team no excuses just '
               'great.',
       'timestamp': 215,
       'timestamp_label': '[00:03:35]',
       'timestamp_seconds': 215,
       'tip': 'Get the property you want if you are unfamiliar with Probate Court proceedings '
              'if you have any doubts about how to present your offer or if you just want to '
              'hear it all again call the sandborn team the sandborn team no excuses just '
              'great.',
       'title': 'Probate: How to Overbid on Real Property (The Sanborn Team)',
       'url': 'https://www.youtube.com/watch?v=-1OrRi_sTzA&t=215s',
       'video_id': '-1OrRi_sTzA'},
      {'author': 'Rick Ginn',
       'channel': 'Rick Ginn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:26](https://www.youtube.com/watch?v=C9alsmfSoC4&t=566s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, a lot of times the realtor's free. Just call out, get their information, "
               'and talk to them and see if they have a cash buyer given the opportunity to '
               "make this transaction easy on you. The next one's a probate attorney. Now, you "
               "don't hire the probate attorney.",
       'timestamp': 566,
       'timestamp_label': '[00:09:26]',
       'timestamp_seconds': 566,
       'tip': "So, a lot of times the realtor's free. Just call out, get their information, "
              'and talk to them and see if they have a cash buyer given the opportunity to '
              "make this transaction easy on you. The next one's a probate attorney. Now, you "
              "don't hire the probate attorney.",
       'title': 'Wholesaling Probate Properties Start to Finish - Part 1 (Rick Ginn)',
       'url': 'https://www.youtube.com/watch?v=C9alsmfSoC4&t=566s',
       'video_id': 'C9alsmfSoC4'},
      {'author': 'Horizon Real Estate & Probate and Trust Help',
       'channel': 'Horizon Real Estate & Probate and Trust Help',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:17](https://www.youtube.com/watch?v=zSsn_jeexks&t=437s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The final piece of removing items from house after death is to hire an estate '
               'Liquidator and a state company a buyout or a donate this last step of the '
               'estate.',
       'timestamp': 437,
       'timestamp_label': '[00:07:17]',
       'timestamp_seconds': 437,
       'tip': 'The final piece of removing items from house after death is to hire an estate '
              'Liquidator and a state company a buyout or a donate this last step of the '
              'estate.',
       'title': 'How to Organize an Estate Cleanout, Removing Items from House After Death '
                '(Horizon Real Estate & Probate and Trust Help)',
       'url': 'https://www.youtube.com/watch?v=zSsn_jeexks&t=437s',
       'video_id': 'zSsn_jeexks'},
      {'author': 'Serg Lupescu',
       'channel': 'Serg Lupescu',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:36](https://www.youtube.com/watch?v=JUTV80jUHSI&t=216s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Have a playlist on my channel talking about all this assisted living '
               'information but you can go on there and you can see what it takes to start an.',
       'timestamp': 216,
       'timestamp_label': '[00:03:36]',
       'timestamp_seconds': 216,
       'tip': 'Have a playlist on my channel talking about all this assisted living '
              'information but you can go on there and you can see what it takes to start an.',
       'title': 'Starting an Assisted Living Home for beginners | Residential Assisted Living '
                '(Serg Lupescu)',
       'url': 'https://www.youtube.com/watch?v=JUTV80jUHSI&t=216s',
       'video_id': 'JUTV80jUHSI'},
      {'author': 'Bill Gross, the LA Probate Expert',
       'channel': 'Bill Gross, the LA Probate Expert',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:21](https://www.youtube.com/watch?v=98dpuziGiYY&t=1041s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Learn where the court layout is where their rooms are where to park all those '
               'kinds of things also i would say teach investors the.',
       'timestamp': 1041,
       'timestamp_label': '[00:17:21]',
       'timestamp_seconds': 1041,
       'tip': 'Learn where the court layout is where their rooms are where to park all those '
              'kinds of things also i would say teach investors the.',
       'title': '11 Ways to Make a Sale in Probate Real Estate | #6 - Court Confirmation '
                'Sales/Auctions (Bill Gross, the LA Probate Expert)',
       'url': 'https://www.youtube.com/watch?v=98dpuziGiYY&t=1041s',
       'video_id': '98dpuziGiYY'},
      {'author': 'Illinois Probate Solutions',
       'channel': 'Illinois Probate Solutions',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:06](https://www.youtube.com/watch?v=dHEXFlygm_8&t=126s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Correct decision while under serious pressure it's also a praise for her for "
               'hiring an ethical estate sale company that upon finding the cash.',
       'timestamp': 126,
       'timestamp_label': '[00:02:06]',
       'timestamp_seconds': 126,
       'tip': "Correct decision while under serious pressure it's also a praise for her for "
              'hiring an ethical estate sale company that upon finding the cash.',
       'title': "5 Don'ts Before Cleaning Out An Estate (Illinois Probate Solutions)",
       'url': 'https://www.youtube.com/watch?v=dHEXFlygm_8&t=126s',
       'video_id': 'dHEXFlygm_8'},
      {'author': 'Cesar Espinoza - Houston Probate Realtor',
       'channel': 'Cesar Espinoza - Houston Probate Realtor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:57](https://www.youtube.com/watch?v=l68yR0_4B4g&t=297s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You can still try a consignment shop before you donate. And here's the part "
               'people miss. Those items may count towards what a buyout company will offer '
               'you later. Donate them early and you may be lowering your number without '
               'realizing it. That said, donations matter.',
       'timestamp': 297,
       'timestamp_label': '[00:04:57]',
       'timestamp_seconds': 297,
       'tip': "You can still try a consignment shop before you donate. And here's the part "
              'people miss. Those items may count towards what a buyout company will offer you '
              'later. Donate them early and you may be lowering your number without realizing '
              'it. That said, donations matter.',
       'title': 'Estate Cleanout in Houston: 7 Things Executors Must Do | Realtor Cesar '
                'Espinoza (Cesar Espinoza - Houston Probate Realtor)',
       'url': 'https://www.youtube.com/watch?v=l68yR0_4B4g&t=297s',
       'video_id': 'l68yR0_4B4g'},
      {'author': 'National Referral Network',
       'channel': 'National Referral Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=22eVzYFh7is&t=15s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Professionals help Elevate all professionals and anyone that cares to watch '
               "the video and this morning we've got Jeff marsace a state planning.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Professionals help Elevate all professionals and anyone that cares to watch the '
              "video and this morning we've got Jeff marsace a state planning.",
       'title': 'Estate Planning Mastery: Keeping Your Wealth in the Family and Out of '
                "In-Laws' Reach (National Referral Network)",
       'url': 'https://www.youtube.com/watch?v=22eVzYFh7is&t=15s',
       'video_id': '22eVzYFh7is'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:34](https://www.youtube.com/watch?v=z0GTjTG76ls&t=214s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And I took the people that were already around me, my estate sale company, my '
               'cash investors, my contractors, and we kind of built a team specifically for '
               'helping people in your situation.',
       'timestamp': 214,
       'timestamp_label': '[00:03:34]',
       'timestamp_seconds': 214,
       'tip': 'And I took the people that were already around me, my estate sale company, my '
              'cash investors, my contractors, and we kind of built a team specifically for '
              'helping people in your situation.',
       'title': 'Real Estate Cold Calling -  Inbound probate leads role play | Real Estate '
                'Coaching with Chad Corbett (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=z0GTjTG76ls&t=214s',
       'video_id': 'z0GTjTG76ls'},
      {'author': 'Dan Collins',
       'channel': 'Dan Collins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:29](https://www.youtube.com/watch?v=WinbHNSQLbg&t=209s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'One six two one five two zero four two or you may email me at D Collins at '
               'Collins - commercial dotnet for more videos and information please feel free '
               "to visit my website Collins fiduciary broker com I'm Dan Collins thank you for "
               'watching.',
       'timestamp': 209,
       'timestamp_label': '[00:03:29]',
       'timestamp_seconds': 209,
       'tip': 'One six two one five two zero four two or you may email me at D Collins at '
              'Collins - commercial dotnet for more videos and information please feel free to '
              "visit my website Collins fiduciary broker com I'm Dan Collins thank you for "
              'watching.',
       'title': 'Overbids in Probate Real Estate Sales (Dan Collins)',
       'url': 'https://www.youtube.com/watch?v=WinbHNSQLbg&t=209s',
       'video_id': 'WinbHNSQLbg'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:52:46](https://www.youtube.com/watch?v=uJxayMyF-i4&t=3166s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And my very last question of Dan set it all off for me too. When you were '
               'mentioning something about the team enough, we putting the property in a land '
               'trust, doing the paint, the carpet, and having the a hundred grand to split.',
       'timestamp': 3166,
       'timestamp_label': '[00:52:46]',
       'timestamp_seconds': 3166,
       'tip': 'And my very last question of Dan set it all off for me too. When you were '
              'mentioning something about the team enough, we putting the property in a land '
              'trust, doing the paint, the carpet, and having the a hundred grand to split.',
       'title': 'Making cash offers fast, solving problems with probate real estate deals, and '
                'wholesaling ethics (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=uJxayMyF-i4&t=3166s',
       'video_id': 'uJxayMyF-i4'},
      {'author': 'Matt McGilvray',
       'channel': 'Matt McGilvray',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=fi8ZbbtnVgM&t=183s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And not every probate sale requires court confirmation. Many personal '
               'representatives have full authority under the Independent Administration of '
               'Estates Act, allowing them to sell without a confirmation hearing.',
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': 'And not every probate sale requires court confirmation. Many personal '
              'representatives have full authority under the Independent Administration of '
              'Estates Act, allowing them to sell without a confirmation hearing.',
       'title': 'How Do You Determine the Right Asking Price for a Probate Property? | '
                'California Probate (Matt McGilvray)',
       'url': 'https://www.youtube.com/watch?v=fi8ZbbtnVgM&t=183s',
       'video_id': 'fi8ZbbtnVgM'}],
 12: [{'author': 'Smile Abroad with Sam & Spencer',
       'channel': 'Smile Abroad with Sam & Spencer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:41](https://www.youtube.com/watch?v=q0NbvHAFXsA&t=941s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I see every day on Reddit or in Facebook groups people talking about their '
               '9-month plan, 12 month plan as they figure out how to get rid of all of their '
               "stuff. If you're really serious about this and you want to move, you can do it "
               'in 60 days.',
       'timestamp': 941,
       'timestamp_label': '[00:15:41]',
       'timestamp_seconds': 941,
       'tip': 'I see every day on Reddit or in Facebook groups people talking about their '
              '9-month plan, 12 month plan as they figure out how to get rid of all of their '
              "stuff. If you're really serious about this and you want to move, you can do it "
              'in 60 days.',
       'title': 'DIY Estate Sale Guide: How We Made $10,839 in 48 Hours (Smile Abroad with Sam '
                '& Spencer)',
       'url': 'https://www.youtube.com/watch?v=q0NbvHAFXsA&t=941s',
       'video_id': 'q0NbvHAFXsA'},
      {'author': 'Property Preservation Insiders',
       'channel': 'Property Preservation Insiders',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:01:06](https://www.youtube.com/watch?v=4pX2VabEor4&t=3666s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And by the way, when I first started in preservation working for working for '
               'Regionals all by my itty bitty self and yes, I was working six days a week. '
               'Um, yeah, 10 grand is a slow month at that stage. And then um tell you again '
               'asked uh you think of a market in Michigan.',
       'timestamp': 3666,
       'timestamp_label': '[01:01:06]',
       'timestamp_seconds': 3666,
       'tip': 'And by the way, when I first started in preservation working for working for '
              'Regionals all by my itty bitty self and yes, I was working six days a week. Um, '
              'yeah, 10 grand is a slow month at that stage. And then um tell you again asked '
              'uh you think of a market in Michigan.',
       'title': 'Property Preservation 101: Foreclosures, Lock Changes & Big Money (Property '
                'Preservation Insiders)',
       'url': 'https://www.youtube.com/watch?v=4pX2VabEor4&t=3666s',
       'video_id': '4pX2VabEor4'},
      {'author': 'Real Estate The Ramsey Way',
       'channel': 'Real Estate The Ramsey Way',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:44](https://www.youtube.com/watch?v=eC2q1zU3G2A&t=464s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We want to start building our forever home. Um and sometimes we're like, "
               '"Yeah, let\'s go ahead and you know, get in bed, you know, take a loan out." '
               'And then there\'s times where we usually like, "Well, what if we just cash '
               'flow everything, call it a day?".',
       'timestamp': 464,
       'timestamp_label': '[00:07:44]',
       'timestamp_seconds': 464,
       'tip': "We want to start building our forever home. Um and sometimes we're like, "
              '"Yeah, let\'s go ahead and you know, get in bed, you know, take a loan out." '
              'And then there\'s times where we usually like, "Well, what if we just cash flow '
              'everything, call it a day?".',
       'title': 'How Do I Prepare to Receive an Inherited Property? (Real Estate The Ramsey '
                'Way)',
       'url': 'https://www.youtube.com/watch?v=eC2q1zU3G2A&t=464s',
       'video_id': 'eC2q1zU3G2A'},
      {'author': 'Aronsohn & So, Probate Real Estate',
       'channel': 'Aronsohn & So, Probate Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=Ivp-A8gsOnI&t=109s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Make its way through the court recording system about a week or so after the '
               'attorney files that order it is scanned into the system with the court seal at '
               'that point the document is submitted to escrow to complete the sale process '
               'which can take another 10 to 21 days.',
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': 'Make its way through the court recording system about a week or so after the '
              'attorney files that order it is scanned into the system with the court seal at '
              'that point the document is submitted to escrow to complete the sale process '
              'which can take another 10 to 21 days.',
       'title': 'Overbidding in Court for Probate Real Estate (Aronsohn & So, Probate Real '
                'Estate)',
       'url': 'https://www.youtube.com/watch?v=Ivp-A8gsOnI&t=109s',
       'video_id': 'Ivp-A8gsOnI'},
      {'author': 'Mario Joyner- Las Vegas RE - Probate & Commercial',
       'channel': 'Mario Joyner- Las Vegas RE - Probate & Commercial',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=Eysvzbieyro&t=15s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Confirmation as last week and I tell you this it was a very exciting day in '
               'the courtroom now I thank you for those of you who watch weekly Mrs Patricia '
               'more.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Confirmation as last week and I tell you this it was a very exciting day in the '
              'courtroom now I thank you for those of you who watch weekly Mrs Patricia more.',
       'title': 'February 10th Las Vegas Probate Ct Results: 11 Properties Confirmed, 2 '
                'Overbid in INTENSE Auction (Mario Joyner- Las Vegas RE - Probate & '
                'Commercial)',
       'url': 'https://www.youtube.com/watch?v=Eysvzbieyro&t=15s',
       'video_id': 'Eysvzbieyro'},
      {'author': 'Laura Cowan, Esq.',
       'channel': 'Laura Cowan, Esq.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:11](https://www.youtube.com/watch?v=qquf8lhULDs&t=191s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Starting to really learn how to network and nurture those relationships the '
               "right way you start to dial these in and you'll start to get a constant influx "
               'of business from all different resources which is what you want thanks '
               'everyone see you next time.',
       'timestamp': 191,
       'timestamp_label': '[00:03:11]',
       'timestamp_seconds': 191,
       'tip': 'Starting to really learn how to network and nurture those relationships the '
              "right way you start to dial these in and you'll start to get a constant influx "
              'of business from all different resources which is what you want thanks everyone '
              'see you next time.',
       'title': 'Top 3 Ways To Get Estate Planning Clients (Laura Cowan, Esq.)',
       'url': 'https://www.youtube.com/watch?v=qquf8lhULDs&t=191s',
       'video_id': 'qquf8lhULDs'},
      {'author': 'Carol Benning',
       'channel': 'Carol Benning',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:08](https://www.youtube.com/watch?v=ZUxMEt0kKoU&t=1208s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Proper planning with an elder law attorney is vital to avoid penalties. Let's "
               'take the case of Alice, 69, who recently met with an attorney to start her '
               '5-year plan.',
       'timestamp': 1208,
       'timestamp_label': '[00:20:08]',
       'timestamp_seconds': 1208,
       'tip': "Proper planning with an elder law attorney is vital to avoid penalties. Let's "
              'take the case of Alice, 69, who recently met with an attorney to start her '
              '5-year plan.',
       'title': 'Medicaid Estate Recovery: 7 Ways to Protect Your Family Home Before 2027 '
                '(Carol Benning)',
       'url': 'https://www.youtube.com/watch?v=ZUxMEt0kKoU&t=1208s',
       'video_id': 'ZUxMEt0kKoU'},
      {'author': 'Sell a House in Probate California | Brendan Mohr',
       'channel': 'Sell a House in Probate California | Brendan Mohr',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:26](https://www.youtube.com/watch?v=GS1quJmfAA4&t=86s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Always consult with an attorney now every day we help people save thousands of '
               'dollars and headaches through our very unique one-of-a-kind probate.',
       'timestamp': 86,
       'timestamp_label': '[00:01:26]',
       'timestamp_seconds': 86,
       'tip': 'Always consult with an attorney now every day we help people save thousands of '
              'dollars and headaches through our very unique one-of-a-kind probate.',
       'title': 'What is The Probate Sale Overbid Process | California Court Confirmation | '
                'Brendan Mohr (Sell a House in Probate California | Brendan Mohr)',
       'url': 'https://www.youtube.com/watch?v=GS1quJmfAA4&t=86s',
       'video_id': 'GS1quJmfAA4'},
      {'author': 'Brett Chotkevys',
       'channel': 'Brett Chotkevys',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:04](https://www.youtube.com/watch?v=fFnH_VM4S48&t=184s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Plan done for me and you know what that's money well well spent because at "
               "that place even if I'm not ready yet I know exactly what I can do and what I "
               "can't do and next time I have all my ducks in a row I'm able to pull the "
               'trigger make an offer on something.',
       'timestamp': 184,
       'timestamp_label': '[00:03:04]',
       'timestamp_seconds': 184,
       'tip': "Plan done for me and you know what that's money well well spent because at that "
              "place even if I'm not ready yet I know exactly what I can do and what I can't "
              "do and next time I have all my ducks in a row I'm able to pull the trigger make "
              'an offer on something.',
       'title': 'How to Find & Prepare Property for Assisted Living | Step-by-Step Guide '
                '(Brett Chotkevys)',
       'url': 'https://www.youtube.com/watch?v=fFnH_VM4S48&t=184s',
       'video_id': 'fFnH_VM4S48'},
      {'author': 'The Family Land Lawyer',
       'channel': 'The Family Land Lawyer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:08](https://www.youtube.com/watch?v=Y515EhC17RU&t=428s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's my little tidbit for you today make sure that you are not in the number "
               'of land owners who are not including their interest in land in their estate '
               "plans y'all take care and have a wonderful day.",
       'timestamp': 428,
       'timestamp_label': '[00:07:08]',
       'timestamp_seconds': 428,
       'tip': "That's my little tidbit for you today make sure that you are not in the number "
              'of land owners who are not including their interest in land in their estate '
              "plans y'all take care and have a wonderful day.",
       'title': "Shocked that more heirs property owners aren't doing this! (The Family Land "
                'Lawyer)',
       'url': 'https://www.youtube.com/watch?v=Y515EhC17RU&t=428s',
       'video_id': 'Y515EhC17RU'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=y1TInRM-Flc&t=54s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's just say I start with 100 leads. That's 50 people that I've had a "
               'conversation with that um I may have spent four $400 for an ISA. Um where I '
               "could kick out a six-month mail campaign, 600 mailers at $1. And I know that's "
               "expensive mail, but there's $900.",
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': "Let's just say I start with 100 leads. That's 50 people that I've had a "
              'conversation with that um I may have spent four $400 for an ISA. Um where I '
              "could kick out a six-month mail campaign, 600 mailers at $1. And I know that's "
              "expensive mail, but there's $900.",
       'title': 'Cold Calling Probate or Mailing Letters — Which Gets Better Results? (Probate '
                'Mastery)',
       'url': 'https://www.youtube.com/watch?v=y1TInRM-Flc&t=54s',
       'video_id': 'y1TInRM-Flc'},
      {'author': 'Legacy Legal Planning, LLC | MA Estate Planning',
       'channel': 'Legacy Legal Planning, LLC | MA Estate Planning',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:18](https://www.youtube.com/watch?v=WJr4n3V_2aY&t=258s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "When people finally get their plan in place, what they usually feel isn't "
               "relief about documents, it's relief that the people they love won't be left "
               'guessing. That is what a legacy really is. Clarity and care carried forward.',
       'timestamp': 258,
       'timestamp_label': '[00:04:18]',
       'timestamp_seconds': 258,
       'tip': "When people finally get their plan in place, what they usually feel isn't "
              "relief about documents, it's relief that the people they love won't be left "
              'guessing. That is what a legacy really is. Clarity and care carried forward.',
       'title': "What Is Estate Planning? A Beginner's Guide for Massachusetts Residents "
                '(Legacy Legal Planning, LLC | MA Estate Planning)',
       'url': 'https://www.youtube.com/watch?v=WJr4n3V_2aY&t=258s',
       'video_id': 'WJr4n3V_2aY'},
      {'author': 'Carolynn Castillo',
       'channel': 'Carolynn Castillo',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:03:30](https://www.youtube.com/watch?v=XN-9ankgVNk&t=3810s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Us so that's when we contact them um Sanji are we are we out of time here I "
               "mean I can maybe finish these last questions you're on meal you're a meal.",
       'timestamp': 3810,
       'timestamp_label': '[01:03:30]',
       'timestamp_seconds': 3810,
       'tip': "Us so that's when we contact them um Sanji are we are we out of time here I "
              "mean I can maybe finish these last questions you're on meal you're a meal.",
       'title': 'Mastering Probate Real Estate: A Comprehensive Training Guide (Carolynn '
                'Castillo)',
       'url': 'https://www.youtube.com/watch?v=XN-9ankgVNk&t=3810s',
       'video_id': 'XN-9ankgVNk'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:40](https://www.youtube.com/watch?v=8bwGbc8cjHo&t=160s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Families and real value to attorneys this could be your best year ever so go '
               'to earn attorney referrals right now get signed up and we will see you in the '
               'course and on the live call july 21st thanks so much and have a great day.',
       'timestamp': 160,
       'timestamp_label': '[00:02:40]',
       'timestamp_seconds': 160,
       'tip': 'Families and real value to attorneys this could be your best year ever so go to '
              'earn attorney referrals right now get signed up and we will see you in the '
              'course and on the live call july 21st thanks so much and have a great day.',
       'title': 'EARN ATTORNEY REFERRALS NOW: New Course for Real Estate Professionals '
                '(Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=8bwGbc8cjHo&t=160s',
       'video_id': '8bwGbc8cjHo'},
      {'author': 'California Probate Real Estate Made Simple',
       'channel': 'California Probate Real Estate Made Simple',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:53](https://www.youtube.com/watch?v=32VmI6oEsPQ&t=293s)',
       'relevance': 'Attributed practitioner commentary on probate real estate brokerage & '
                    'acquisitions, executor concierge services, and probate-attorney referral '
                    'flywheels (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "This is when the heirs finally receive their inheritance. Now, here's a major "
               'point most people overlook. Independent Administration of Estates Act, known '
               'as the IAEA, you can usually sell the house without needing any court '
               'confirmation every step of the way.',
       'timestamp': 293,
       'timestamp_label': '[00:04:53]',
       'timestamp_seconds': 293,
       'tip': "This is when the heirs finally receive their inheritance. Now, here's a major "
              'point most people overlook. Independent Administration of Estates Act, known as '
              'the IAEA, you can usually sell the house without needing any court confirmation '
              'every step of the way.',
       'title': 'How to Sell a House in Probate California (Step-by-Step Guide + Insider Tip) '
                '(California Probate Real Estate Made Simple)',
       'url': 'https://www.youtube.com/watch?v=32VmI6oEsPQ&t=293s',
       'video_id': '32VmI6oEsPQ'}]}
