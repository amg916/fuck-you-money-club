"""Curated 180-citation Land Flipping baseline (15 per chapter across Q1-Q12) mined strictly from verified Land Flipping YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'client',
     'clients',
     'closing',
     'cold',
     'compliance',
     'comps',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'budget',
     'business',
     'buyer',
     'calling',
     'capital',
     'cash',
     'check',
     'closing',
     'cold',
     'compliance',
     'comps',
     'contract',
     'county',
     'covenants',
     'customer',
     'data',
     'datatree',
     'days',
     'deals',
     'decision',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'cashflow',
     'check',
     'closing',
     'cold',
     'commission',
     'compliance',
     'comps',
     'cost',
     'costs',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'budget',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'closing',
     'cold',
     'compliance',
     'comps',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
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
 5: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'audit',
     'avoid',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'clawback',
     'closing',
     'cold',
     'compliance',
     'comps',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
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
 6: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'client',
     'closing',
     'cold',
     'compliance',
     'comps',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deal',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
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
 7: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'checklist',
     'closing',
     'cold',
     'compliance',
     'comps',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'delivery',
     'diligence',
     'direct',
     'disposition',
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
 8: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'api',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'closing',
     'cold',
     'compliance',
     'comps',
     'county',
     'covenants',
     'crm',
     'data',
     'database',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disposition',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'academy',
     'access',
     'acquisition',
     'acreage',
     'act',
     'agreement',
     'assemblage',
     'battery',
     'blind',
     'bosch',
     'broker',
     'business',
     'calling',
     'capital',
     'cash',
     'check',
     'closing',
     'cold',
     'compliance',
     'comps',
     'contract',
     'county',
     'covenants',
     'data',
     'datatree',
     'days',
     'deals',
     'deed',
     'delinquent',
     'diligence',
     'direct',
     'disclosure',
     'disposition',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'academy',
      'access',
      'acquisition',
      'acreage',
      'act',
      'agent',
      'ai',
      'assemblage',
      'automate',
      'automation',
      'battery',
      'blind',
      'bosch',
      'broker',
      'business',
      'calling',
      'capital',
      'cash',
      'check',
      'closing',
      'cold',
      'compliance',
      'comps',
      'county',
      'covenants',
      'dashboard',
      'data',
      'datatree',
      'days',
      'deals',
      'deed',
      'delinquent',
      'diligence',
      'direct',
      'disposition',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'academy',
      'access',
      'acquisition',
      'acreage',
      'act',
      'assemblage',
      'battery',
      'blind',
      'bosch',
      'broker',
      'business',
      'calling',
      'capital',
      'cash',
      'check',
      'closing',
      'cold',
      'compliance',
      'comps',
      'contractor',
      'county',
      'covenants',
      'data',
      'datatree',
      'days',
      'deals',
      'deed',
      'delinquent',
      'diligence',
      'direct',
      'disposition',
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
 12: {'academy',
      'access',
      'acquisition',
      'acreage',
      'act',
      'action',
      'assemblage',
      'battery',
      'blind',
      'bosch',
      'broker',
      'business',
      'calling',
      'capital',
      'cash',
      'check',
      'closing',
      'cold',
      'compliance',
      'comps',
      'county',
      'covenants',
      'data',
      'datatree',
      'day',
      'days',
      'deals',
      'deed',
      'delinquent',
      'diligence',
      'direct',
      'disposition',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=U4C3AVYK9M4&t=173s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In conclusion, direct mail is by far the best way to acquire undermarket value '
              'land and to build a successful land flipping business. We have tested '
              'extensively all other methods, including texting, cold calling, and emailing.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': 'In conclusion, direct mail is by far the best way to acquire undermarket value '
             'land and to build a successful land flipping business. We have tested '
             'extensively all other methods, including texting, cold calling, and emailing.',
      'title': 'Breaking Down The Numbers Of The Land Flipping Business Model (Apke Brothers)',
      'url': 'https://www.youtube.com/watch?v=U4C3AVYK9M4&t=173s',
      'video_id': 'U4C3AVYK9M4'},
     {'author': 'Michael Bull',
      'channel': 'Michael Bull',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:47](https://www.youtube.com/watch?v=V4qnHYV6EVo&t=767s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If we have a property over 50% of market value, somewhere between 60 and 80% of '
              "market value, we're going to wholesale the property. If we can get the deal for "
              "50% of market value or less, we're going to cash close. The majority of our "
              'deals in our business are cash close.',
      'timestamp': 767,
      'timestamp_label': '[00:12:47]',
      'timestamp_seconds': 767,
      'tip': 'If we have a property over 50% of market value, somewhere between 60 and 80% of '
             "market value, we're going to wholesale the property. If we can get the deal for "
             "50% of market value or less, we're going to cash close. The majority of our "
             'deals in our business are cash close.',
      'title': 'What Is Wholesaling in Real Estate? Assignment vs Double Close vs Novation '
               '(Michael Bull)',
      'url': 'https://www.youtube.com/watch?v=V4qnHYV6EVo&t=767s',
      'video_id': 'V4qnHYV6EVo'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:19](https://www.youtube.com/watch?v=pBstDNy9IuM&t=1099s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll explain exactly how I do it. But a data service basically allows you to "
              'filter very specific types of properties and property owners in any county in '
              'the country or most counties in the country. The one that I use is called '
              'DataTree.',
      'timestamp': 1099,
      'timestamp_label': '[00:18:19]',
      'timestamp_seconds': 1099,
      'tip': "'ll explain exactly how I do it. But a data service basically allows you to "
             'filter very specific types of properties and property owners in any county in '
             'the country or most counties in the country. The one that I use is called '
             'DataTree.',
      'title': 'Before Your Next Land Deal: 7 Things to Know - REWBCON 2022 with Seth Williams '
               '(REtipster)',
      'url': 'https://www.youtube.com/watch?v=pBstDNy9IuM&t=1099s',
      'video_id': 'pBstDNy9IuM'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:45](https://www.youtube.com/watch?v=Q830bJqxC1Q&t=1665s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like the acreage, the zoning of each property, the road access, the flood '
              "zones, whether there's wetlands on it, the market value, things like that. Like "
              'think of all of the perfect information you would ever want to see on the best '
              'list ever.',
      'timestamp': 1665,
      'timestamp_label': '[00:27:45]',
      'timestamp_seconds': 1665,
      'tip': 'Like the acreage, the zoning of each property, the road access, the flood zones, '
             "whether there's wetlands on it, the market value, things like that. Like think "
             'of all of the perfect information you would ever want to see on the best list '
             'ever.',
      'title': 'The Future of Land Investing Is Here | REtipster Podcast (REtipster)',
      'url': 'https://www.youtube.com/watch?v=Q830bJqxC1Q&t=1665s',
      'video_id': 'Q830bJqxC1Q'},
     {'author': 'LandApp by LandGate',
      'channel': 'LandApp by LandGate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:57](https://www.youtube.com/watch?v=Uaymin1wo40&t=717s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Revenue stream on day one up here in year one for anywhere from 40 to 45 '
              'percent to 17 million dollar number all right so there is a market out there '
              'wanting to buy these revenue streams and this in fact is the deal that was made '
              'to this landowner in Brown County Ohio.',
      'timestamp': 717,
      'timestamp_label': '[00:11:57]',
      'timestamp_seconds': 717,
      'tip': 'Revenue stream on day one up here in year one for anywhere from 40 to 45 percent '
             'to 17 million dollar number all right so there is a market out there wanting to '
             'buy these revenue streams and this in fact is the deal that was made to this '
             'landowner in Brown County Ohio.',
      'title': 'Solar & Energy Storage Lease Process (LandApp by LandGate)',
      'url': 'https://www.youtube.com/watch?v=Uaymin1wo40&t=717s',
      'video_id': 'Uaymin1wo40'},
     {'author': 'RocketPrint and Mail',
      'channel': 'RocketPrint and Mail',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=pIgr8VsT8qA&t=71s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each acquisition um it after we sell it generates approximately $10,000. Um our '
              'our last campaign over the quarter we we purchased about six properties uh '
              'totaling somewhere between 100 to 150,000 in revenue.',
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'Each acquisition um it after we sell it generates approximately $10,000. Um our '
             'our last campaign over the quarter we we purchased about six properties uh '
             'totaling somewhere between 100 to 150,000 in revenue.',
      'title': 'Land N Deed, Land Investor Direct Mail Case Study (RocketPrint & Mail) '
               '(RocketPrint and Mail)',
      'url': 'https://www.youtube.com/watch?v=pIgr8VsT8qA&t=71s',
      'video_id': 'pIgr8VsT8qA'},
     {'author': 'Joe Crump',
      'channel': 'Joe Crump',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=mtE3-cvmAN0&t=20s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '" Well, first of all, you don\'t have to buy properties cheap in order to '
              'resell them. You can buy them at full market value.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': '" Well, first of all, you don\'t have to buy properties cheap in order to resell '
             'them. You can buy them at full market value.',
      'title': 'How Do I Comply With The Dodd-Frank Act? (Joe Crump)',
      'url': 'https://www.youtube.com/watch?v=mtE3-cvmAN0&t=20s',
      'video_id': 'mtE3-cvmAN0'},
     {'author': 'Paul Jang',
      'channel': 'Paul Jang',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=e8Ouv9k5iag&t=230s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cash but they go for owner financing but it gives you also more chances to sell '
              'your individual lots and start with getting some recurring revenue right so.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'Cash but they go for owner financing but it gives you also more chances to sell '
             'your individual lots and start with getting some recurring revenue right so.',
      'title': 'Subdividing Rural Land For Sale - What is the Process? (Paul Jang)',
      'url': 'https://www.youtube.com/watch?v=e8Ouv9k5iag&t=230s',
      'video_id': 'e8Ouv9k5iag'},
     {'author': 'dhall3000',
      'channel': 'dhall3000',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=GpQWztIpKSo&t=80s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Easement for access yeah it's one number yeah um or if and or if you're asking "
              'what is the diminution in value of the adjacent property after it grants you an '
              "easement right it's a different question right either one can be used for your "
              'negotiation.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "Easement for access yeah it's one number yeah um or if and or if you're asking "
             'what is the diminution in value of the adjacent property after it grants you an '
             "easement right it's a different question right either one can be used for your "
             'negotiation.',
      'title': 'Landlocked property access easement appraisal (dhall3000)',
      'url': 'https://www.youtube.com/watch?v=GpQWztIpKSo&t=80s',
      'video_id': 'GpQWztIpKSo'},
     {'author': 'Sumner Healey',
      'channel': 'Sumner Healey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=GsUpcKZrJAQ&t=237s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "On the deal or the market and so every week we get deals where it's like I "
              "think this is a good deal but I'm not positive for X Y and Z reason or maybe.",
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': "On the deal or the market and so every week we get deals where it's like I think "
             "this is a good deal but I'm not positive for X Y and Z reason or maybe.",
      'title': 'Double Closing Strategies for Land Investors: Complete Guide | Sumner Healey '
               '(Sumner Healey)',
      'url': 'https://www.youtube.com/watch?v=GsUpcKZrJAQ&t=237s',
      'video_id': 'GsUpcKZrJAQ'},
     {'author': 'Commercial Property Advisors',
      'channel': 'Commercial Property Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=ek2QTeZlqCY&t=203s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Hey, Peter, the mobile home parks, there\'s so few of them. There\'s it\'s '
              'saturated, right? The the niche is overpop populate." Look at this data that we '
              'pulled, right?',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': '"Hey, Peter, the mobile home parks, there\'s so few of them. There\'s it\'s '
             'saturated, right? The the niche is overpop populate." Look at this data that we '
             'pulled, right?',
      'title': 'Mobile Home Park or RV Park? How to Choose the Right Asset (Commercial '
               'Property Advisors)',
      'url': 'https://www.youtube.com/watch?v=ek2QTeZlqCY&t=203s',
      'video_id': 'ek2QTeZlqCY'},
     {'author': 'Living in Virginia With Ben Quann',
      'channel': 'Living in Virginia With Ben Quann',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=uvqvdLjMBL0&t=21s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even for the guys that are thinking, "Oh, I\'m just buying it for recreational '
              "use. I'm not planning on building on it. For the resale value, you always want "
              'to check this. Buildable lot versus a non-buildable lot is a totally different '
              'ballgame when it comes to valuations.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Even for the guys that are thinking, "Oh, I\'m just buying it for recreational '
             "use. I'm not planning on building on it. For the resale value, you always want "
             'to check this. Buildable lot versus a non-buildable lot is a totally different '
             'ballgame when it comes to valuations.',
      'title': 'Perc Test Explained: Why It’s Crucial Before Buying Land to Build a House '
               '(Living in Virginia With Ben Quann)',
      'url': 'https://www.youtube.com/watch?v=uvqvdLjMBL0&t=21s',
      'video_id': 'uvqvdLjMBL0'},
     {'author': 'Jon Jasniak',
      'channel': 'Jon Jasniak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:05](https://www.youtube.com/watch?v=N5LpbcKdDVE&t=485s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Maybe build a shop little to no restrictions on this land and the market is '
              'absolutely huge and we can deliver it to customers like this all across the '
              'country.',
      'timestamp': 485,
      'timestamp_label': '[00:08:05]',
      'timestamp_seconds': 485,
      'tip': 'Maybe build a shop little to no restrictions on this land and the market is '
             'absolutely huge and we can deliver it to customers like this all across the '
             'country.',
      'title': 'How I Made $500k with a Minor Land Subdivision (Jon Jasniak)',
      'url': 'https://www.youtube.com/watch?v=N5LpbcKdDVE&t=485s',
      'video_id': 'N5LpbcKdDVE'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:29](https://www.youtube.com/watch?v=NqZ26rAeL40&t=1229s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You got any value it means the world to ron and I and it really drives this '
              "business forward other than that guys we'll see you next episode and thank you "
              'for joining thanks guys.',
      'timestamp': 1229,
      'timestamp_label': '[00:20:29]',
      'timestamp_seconds': 1229,
      'tip': 'You got any value it means the world to ron and I and it really drives this '
             "business forward other than that guys we'll see you next episode and thank you "
             'for joining thanks guys.',
      'title': 'Direct Mail Marketing for Real Estate vs Everything Else (Apke Brothers)',
      'url': 'https://www.youtube.com/watch?v=NqZ26rAeL40&t=1229s',
      'video_id': 'NqZ26rAeL40'},
     {'author': 'Hayden Crabtree',
      'channel': 'Hayden Crabtree',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=Hh6ptGrGpDQ&t=364s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The people if you need any help with any of this drop me a comment below or '
              "shoot me an email Hayden haydencrabster.com and I'm happy to help out with that "
              'being said I hope you found this video valuable go send some mail.',
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': 'The people if you need any help with any of this drop me a comment below or '
             "shoot me an email Hayden haydencrabster.com and I'm happy to help out with that "
             'being said I hope you found this video valuable go send some mail.',
      'title': '😱 I sent 1,000 LETTERS to OFF-Market Property Owners (This is what Happened) '
               '(Hayden Crabtree)',
      'url': 'https://www.youtube.com/watch?v=Hh6ptGrGpDQ&t=364s',
      'video_id': 'Hh6ptGrGpDQ'}],
 2: [{'author': 'Ajay Sharma',
      'channel': 'Ajay Sharma',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:47](https://www.youtube.com/watch?v=Jb9R7WTh63s&t=707s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm really trying to comb through the fundamentals of what a deal acquisition "
              'system looks like, right? So, you have your your data, you have your lead gen, '
              'you have within lead gen texting and cold calling, in-house and outsourced. And '
              "then of course we've got direct mail.",
      'timestamp': 707,
      'timestamp_label': '[00:11:47]',
      'timestamp_seconds': 707,
      'tip': "I'm really trying to comb through the fundamentals of what a deal acquisition "
             'system looks like, right? So, you have your your data, you have your lead gen, '
             'you have within lead gen texting and cold calling, in-house and outsourced. And '
             "then of course we've got direct mail.",
      'title': 'The 4-Part Deal Acquisition System Every Land Business Needs (Ajay Sharma)',
      'url': 'https://www.youtube.com/watch?v=Jb9R7WTh63s&t=707s',
      'video_id': 'Jb9R7WTh63s'},
     {'author': 'Clause Gate',
      'channel': 'Clause Gate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=cPrVIwbUYrs&t=296s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In that unfortunate situation, a lender title policy would pay off the bank for '
              'the remaining mortgage loan balance to protect their business interest. '
              'However, without an owner title policy, you would lose all the cash you put '
              'into your down payment and equity payments.',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'In that unfortunate situation, a lender title policy would pay off the bank for '
             'the remaining mortgage loan balance to protect their business interest. However, '
             'without an owner title policy, you would lose all the cash you put into your '
             'down payment and equity payments.',
      'title': 'Closing Costs Explained: Lender Policy vs Owner Policy (Clause Gate)',
      'url': 'https://www.youtube.com/watch?v=cPrVIwbUYrs&t=296s',
      'video_id': 'cPrVIwbUYrs'},
     {'author': 'Land Academy',
      'channel': 'Land Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:46](https://www.youtube.com/watch?v=5U1h-yosUoE&t=526s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s under contract and I theoretically open escrow. So the seller title, "
              "correct? So the seller is all excited because chances are well they you didn't "
              "renegotiate the deal. It's more than they thought they would get. And so in 30 "
              "days they're expecting some money.",
      'timestamp': 526,
      'timestamp_label': '[00:08:46]',
      'timestamp_seconds': 526,
      'tip': "'s under contract and I theoretically open escrow. So the seller title, correct? "
             "So the seller is all excited because chances are well they you didn't "
             "renegotiate the deal. It's more than they thought they would get. And so in 30 "
             "days they're expecting some money.",
      'title': 'Why Double Closing Land Deals Fail Most Of The Time (And What Smart Investors '
               'Do Instead) (Land Academy)',
      'url': 'https://www.youtube.com/watch?v=5U1h-yosUoE&t=526s',
      'video_id': '5U1h-yosUoE'},
     {'author': 'Maximilian Dier',
      'channel': 'Maximilian Dier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:02](https://www.youtube.com/watch?v=hIbsCLgyqbg&t=1322s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm just I'm just trying to budget on my side. So, if I have a couple thousand "
              "dollar and all the attorney closing costs, I'll pay all of that. You don't have "
              'to pay for anything. I want the offer that I present you just to be like what '
              'you receive.',
      'timestamp': 1322,
      'timestamp_label': '[00:22:02]',
      'timestamp_seconds': 1322,
      'tip': "I'm just I'm just trying to budget on my side. So, if I have a couple thousand "
             "dollar and all the attorney closing costs, I'll pay all of that. You don't have "
             'to pay for anything. I want the offer that I present you just to be like what '
             'you receive.',
      'title': 'Cold Calling Vacant Land Sellers LIVE (Maximilian Dier)',
      'url': 'https://www.youtube.com/watch?v=hIbsCLgyqbg&t=1322s',
      'video_id': 'hIbsCLgyqbg'},
     {'author': 'Discount Lots',
      'channel': 'Discount Lots',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=_Nxxv3hxz1w&t=80s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some come with specific requirements at better price, others give you '
              "flexibility. And we're up front about which is which, so you could pick what "
              'fits your plan and your budget. No credit check, low down payment, and a '
              'flexible monthly payment keeps it within reach.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'Some come with specific requirements at better price, others give you '
             "flexibility. And we're up front about which is which, so you could pick what "
             'fits your plan and your budget. No credit check, low down payment, and a '
             'flexible monthly payment keeps it within reach.',
      'title': 'Buying Land in Florida? Check wetlands, flood zones & water tables #buyland '
               '#floridaland #wetlands (Discount Lots)',
      'url': 'https://www.youtube.com/watch?v=_Nxxv3hxz1w&t=80s',
      'video_id': '_Nxxv3hxz1w'},
     {'author': 'Seller Finance Consultants, Inc.',
      'channel': 'Seller Finance Consultants, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=SB_vfxPYuF8&t=171s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The same time forbidden by a seller not using an MLL what about handling the do '
              'on sale Clause the buyer pays the the mortgage fee just as in any other '
              'transaction so why not take the free insurance we can help you too so contact '
              'us now.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'The same time forbidden by a seller not using an MLL what about handling the do '
             'on sale Clause the buyer pays the the mortgage fee just as in any other '
             'transaction so why not take the free insurance we can help you too so contact us '
             'now.',
      'title': 'The Only True Dodd Frank Seller Finance Exemption and Why You Need an MLO For '
               'All Seller Financing (Seller Finance Consultants, Inc.)',
      'url': 'https://www.youtube.com/watch?v=SB_vfxPYuF8&t=171s',
      'video_id': 'SB_vfxPYuF8'},
     {'author': 'Heather Blankenship',
      'channel': 'Heather Blankenship',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:58](https://www.youtube.com/watch?v=FY9TF9ZkLwk&t=718s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Typically, deals that are already on the market and the owners have made the '
              "decision to sell can obviously be bought faster, but you're going to pay a "
              "premium because you're usually competing with other buyers for those "
              'properties.',
      'timestamp': 718,
      'timestamp_label': '[00:11:58]',
      'timestamp_seconds': 718,
      'tip': 'Typically, deals that are already on the market and the owners have made the '
             "decision to sell can obviously be bought faster, but you're going to pay a "
             "premium because you're usually competing with other buyers for those properties.",
      'title': 'The 30-Minute Beginner’s Course for RV Park Investing (Heather Blankenship)',
      'url': 'https://www.youtube.com/watch?v=FY9TF9ZkLwk&t=718s',
      'video_id': 'FY9TF9ZkLwk'},
     {'author': 'Jack Bosch',
      'channel': 'Jack Bosch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:16](https://www.youtube.com/watch?v=nVJMPjUWdZw&t=676s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We have a contract that we have used all around our business all around the '
              'United States to get deals under contract for 10 to 45 cents on the dollar, '
              "most of which the percolation tests pass. Some of them it didn't pass and we "
              'still were able to sell these properties.',
      'timestamp': 676,
      'timestamp_label': '[00:11:16]',
      'timestamp_seconds': 676,
      'tip': 'We have a contract that we have used all around our business all around the '
             'United States to get deals under contract for 10 to 45 cents on the dollar, most '
             "of which the percolation tests pass. Some of them it didn't pass and we still "
             'were able to sell these properties.',
      'title': 'What To Do If Your Land Fails A Perc Test (Before You Panic) (Jack Bosch)',
      'url': 'https://www.youtube.com/watch?v=nVJMPjUWdZw&t=676s',
      'video_id': 'nVJMPjUWdZw'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:21](https://www.youtube.com/watch?v=Zu8LEqQ-L0w&t=1101s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So a lot of this is pure profit. And you can even set this up so that the '
              'initial down payment you get from this buyer completely pays off all the money '
              'you have invested into the deal.',
      'timestamp': 1101,
      'timestamp_label': '[00:18:21]',
      'timestamp_seconds': 1101,
      'tip': 'So a lot of this is pure profit. And you can even set this up so that the '
             'initial down payment you get from this buyer completely pays off all the money '
             'you have invested into the deal.',
      'title': 'Land Investing 101 (Beginners Guide): Learn the Land Flipping Business Model '
               'in 20 Minutes (REtipster)',
      'url': 'https://www.youtube.com/watch?v=Zu8LEqQ-L0w&t=1101s',
      'video_id': 'Zu8LEqQ-L0w'},
     {'author': 'David Miller',
      'channel': 'David Miller',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=orMrWlpfWj4&t=114s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Suggestion is that before any person buys a piece of property that they check '
              'and may or make a condition on their contract the purchasing then it have a.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Suggestion is that before any person buys a piece of property that they check '
             'and may or make a condition on their contract the purchasing then it have a.',
      'title': 'Landlocked property, easements, and shark attacks!!! David Holmes Attorney '
               '(David Miller)',
      'url': 'https://www.youtube.com/watch?v=orMrWlpfWj4&t=114s',
      'video_id': 'orMrWlpfWj4'},
     {'author': 'MissStateExtension',
      'channel': 'MissStateExtension',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=UkiDG5GpG_Y&t=15s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "At  Panther Tract, which is my family's place uh in Yazoo County. >> My name is "
              "Jessica Brant.  I live in Greenville, but we're in Yazoo.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "At  Panther Tract, which is my family's place uh in Yazoo County. >> My name is "
             "Jessica Brant.  I live in Greenville, but we're in Yazoo.",
      'title': 'Wetland Reserve Easements: Benefits for Landowners and the Environment '
               '(MissStateExtension)',
      'url': 'https://www.youtube.com/watch?v=UkiDG5GpG_Y&t=15s',
      'video_id': 'UkiDG5GpG_Y'},
     {'author': 'The Real Estate Classroom',
      'channel': 'The Real Estate Classroom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=HsA2g1n57AY&t=230s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And it sounds a lot like what it means. There is a necessary reason for the '
              "easement itself. Let's say that we have a property owner, and this is a highway "
              "and there's no way for this property owner right here to access the real world, "
              'alright?',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'And it sounds a lot like what it means. There is a necessary reason for the '
             "easement itself. Let's say that we have a property owner, and this is a highway "
             "and there's no way for this property owner right here to access the real world, "
             'alright?',
      'title': 'Basics of Easements & Encroachments | Real Estate Exam Prep Videos (The Real '
               'Estate Classroom)',
      'url': 'https://www.youtube.com/watch?v=HsA2g1n57AY&t=230s',
      'video_id': 'HsA2g1n57AY'},
     {'author': 'The Real Estate Lawyer',
      'channel': 'The Real Estate Lawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:06](https://www.youtube.com/watch?v=gP3fDaUu5Iw&t=246s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Purchase because you're adding some new title defect or some new title "
              "obligation that wasn't disclosed or not existing when you went under contract "
              "so there's a little bonus tip for you if you want to actually Grant um or place "
              'deeded restrictions on property.',
      'timestamp': 246,
      'timestamp_label': '[00:04:06]',
      'timestamp_seconds': 246,
      'tip': "Purchase because you're adding some new title defect or some new title "
             "obligation that wasn't disclosed or not existing when you went under contract so "
             "there's a little bonus tip for you if you want to actually Grant um or place "
             'deeded restrictions on property.',
      'title': 'How To Legally Remove Deeded Property Restrictions (HOA, ETC.) (The Real '
               'Estate Lawyer)',
      'url': 'https://www.youtube.com/watch?v=gP3fDaUu5Iw&t=246s',
      'video_id': 'gP3fDaUu5Iw'},
     {'author': 'Real Estate Made Crystal Clear',
      'channel': 'Real Estate Made Crystal Clear',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:21](https://www.youtube.com/watch?v=okIP6dYiTD4&t=801s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Complicated of real estate situations and make them Crystal Clear see what I '
              'did there real estate made Crystal Clear thank you guys so much for watching.',
      'timestamp': 801,
      'timestamp_label': '[00:13:21]',
      'timestamp_seconds': 801,
      'tip': 'Complicated of real estate situations and make them Crystal Clear see what I did '
             'there real estate made Crystal Clear thank you guys so much for watching.',
      'title': 'How to Find HOA Covenants Conditions & Restrictions #HOACovenants (Real Estate '
               'Made Crystal Clear)',
      'url': 'https://www.youtube.com/watch?v=okIP6dYiTD4&t=801s',
      'video_id': 'okIP6dYiTD4'},
     {'author': 'LandSpeed Price Boss',
      'channel': 'LandSpeed Price Boss',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=FOpRZxfMs4I&t=159s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to do the same thing and my cursor just above the box holding down on "
              'my left button scroll down make sure that save properties highlight copy and '
              "paste we're just going to do it a couple more cause I want to get all of it all "
              'the abs.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': "I'm going to do the same thing and my cursor just above the box holding down on "
             'my left button scroll down make sure that save properties highlight copy and '
             "paste we're just going to do it a couple more cause I want to get all of it all "
             'the abs.',
      'title': 'Scraping LandWatch (LandSpeed Price Boss)',
      'url': 'https://www.youtube.com/watch?v=FOpRZxfMs4I&t=159s',
      'video_id': 'FOpRZxfMs4I'}],
 3: [{'author': 'Hidden Money',
      'channel': 'Hidden Money',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=hWcjM0400as&t=162s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the land is worth 15,000 and you offer 6,000 cash with a quick close, many '
              'will say yes. Your offer should be 30 to 50% of market value to leave room for '
              "profit and cover your costs. You've got a verbal agreement, now comes due "
              'diligence.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'If the land is worth 15,000 and you offer 6,000 cash with a quick close, many '
             'will say yes. Your offer should be 30 to 50% of market value to leave room for '
             "profit and cover your costs. You've got a verbal agreement, now comes due "
             'diligence.',
      'title': 'How to Flip Vacant Land for Profit | The Land Flipping Business Explained '
               '(Hidden Money)',
      'url': 'https://www.youtube.com/watch?v=hWcjM0400as&t=162s',
      'video_id': 'hWcjM0400as'},
     {'author': 'Jeff',
      'channel': 'Jeff',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=mM0tCRujCDM&t=191s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Doesn't say the closing cost yeah doesn't say what the closing costs are here "
              "then you'd go closing costs see see you can put equals question mark monthly "
              'equals ninety seven interest zero comp price.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "Doesn't say the closing cost yeah doesn't say what the closing costs are here "
             "then you'd go closing costs see see you can put equals question mark monthly "
             'equals ninety seven interest zero comp price.',
      'title': 'Landwatch and Zillow Comps (Jeff)',
      'url': 'https://www.youtube.com/watch?v=mM0tCRujCDM&t=191s',
      'video_id': 'mM0tCRujCDM'},
     {'author': 'DealMachine Podcast',
      'channel': 'DealMachine Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:49](https://www.youtube.com/watch?v=HE45qWS8txg&t=589s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, on average, we see across our business and in our community, 6,000 8,000 '
              'direct mail pieces on average per deal. Average profit per deal is about 25 '
              "thousand-ish. If you're doing a cold call, it takes about 6 weeks per deal, "
              'right?',
      'timestamp': 589,
      'timestamp_label': '[00:09:49]',
      'timestamp_seconds': 589,
      'tip': 'So, on average, we see across our business and in our community, 6,000 8,000 '
             'direct mail pieces on average per deal. Average profit per deal is about 25 '
             "thousand-ish. If you're doing a cold call, it takes about 6 weeks per deal, "
             'right?',
      'title': "He Makes MILLIONS Flipping Vacant Land (Here's How) (DealMachine Podcast)",
      'url': 'https://www.youtube.com/watch?v=HE45qWS8txg&t=589s',
      'video_id': 'HE45qWS8txg'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:07](https://www.youtube.com/watch?v=iSZpxOj5Cus&t=427s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So just with lower margins you're the more aggressive pricing the lower margins "
              "you'll get and the more deals you'll get right ron.",
      'timestamp': 427,
      'timestamp_label': '[00:07:07]',
      'timestamp_seconds': 427,
      'tip': "So just with lower margins you're the more aggressive pricing the lower margins "
             "you'll get and the more deals you'll get right ron.",
      'title': 'How to Price Direct Mail to Get More Out Of Your Land Deals (Apke Brothers)',
      'url': 'https://www.youtube.com/watch?v=iSZpxOj5Cus&t=427s',
      'video_id': 'iSZpxOj5Cus'},
     {'author': 'Sumner Healey',
      'channel': 'Sumner Healey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=pWQCNBiSpUY&t=15s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Business and this is the exact strategy that we' Ed to land multiple deals that "
              "have net us over six figures in profit it's pretty awesome I think you guys "
              'are.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Business and this is the exact strategy that we' Ed to land multiple deals that "
             "have net us over six figures in profit it's pretty awesome I think you guys are.",
      'title': 'Full Subdivide Land Guide: Fastest Profits in Real Estate ($192k profit case '
               'study) (Sumner Healey)',
      'url': 'https://www.youtube.com/watch?v=pWQCNBiSpUY&t=15s',
      'video_id': 'pWQCNBiSpUY'},
     {'author': 'PRYCD',
      'channel': 'PRYCD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=3kN1hBRUqVU&t=58s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pricing section we have county field state field acreage field or we can take '
              'the square footage field either one and then the city field is optional if.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Pricing section we have county field state field acreage field or we can take '
             'the square footage field either one and then the city field is optional if.',
      'title': 'PRYCD List Upload Example Video (PRYCD)',
      'url': 'https://www.youtube.com/watch?v=3kN1hBRUqVU&t=58s',
      'video_id': '3kN1hBRUqVU'},
     {'author': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
      'channel': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=3x8J7AdyCEw&t=131s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, uh I don't know, maybe an apartment building will still work, but we're not "
              "going to pay a commercial price. Certainly, you can't put a business there. So, "
              "I think we're really in the retail range of five to six per acre.",
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': "So, uh I don't know, maybe an apartment building will still work, but we're not "
             "going to pay a commercial price. Certainly, you can't put a business there. So, "
             "I think we're really in the retail range of five to six per acre.",
      'title': 'Zillow Land Comping: Master Acreage Pricing 🔑 (Cool Wholesaling+ Land '
               'Deals-Real Estate Investing)',
      'url': 'https://www.youtube.com/watch?v=3x8J7AdyCEw&t=131s',
      'video_id': '3x8J7AdyCEw'},
     {'author': 'Barndo And Tiny Homes Vision',
      'channel': 'Barndo And Tiny Homes Vision',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:15](https://www.youtube.com/watch?v=VIdzLB23cAw&t=495s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Three. Septic or so septic costs depend on your perk test results. As we '
              'covered dot a drain field installation after a successful perk test can cost.',
      'timestamp': 495,
      'timestamp_label': '[00:08:15]',
      'timestamp_seconds': 495,
      'tip': 'Three. Septic or so septic costs depend on your perk test results. As we covered '
             'dot a drain field installation after a successful perk test can cost.',
      'title': 'Raw Land Traps 2026: Perc Tests, Road Access & Utility Costs Explained (Barndo '
               'And Tiny Homes Vision)',
      'url': 'https://www.youtube.com/watch?v=VIdzLB23cAw&t=495s',
      'video_id': 'VIdzLB23cAw'},
     {'author': 'Jerome Maldonado',
      'channel': 'Jerome Maldonado',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=ZvmmZBcu3kc&t=168s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On the watch the biggest thing is you got to check your utilities you got to '
              'check your infrastructure cost on what its gonna take to put in the asphalt '
              'the.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'On the watch the biggest thing is you got to check your utilities you got to '
             'check your infrastructure cost on what its gonna take to put in the asphalt the.',
      'title': 'How To Subdivide Land (Jerome Maldonado)',
      'url': 'https://www.youtube.com/watch?v=ZvmmZBcu3kc&t=168s',
      'video_id': 'ZvmmZBcu3kc'},
     {'author': 'Texas Agriculture Law',
      'channel': 'Texas Agriculture Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=D_ZiLS1CYJg&t=182s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A lot of time legal fees court costs and headaches so if you're dealing with "
              'landlock property like I say we do have resources available to help check out '
              'our show notes for those and now you know there can be landlocked property in '
              'Texas.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': "A lot of time legal fees court costs and headaches so if you're dealing with "
             'landlock property like I say we do have resources available to help check out '
             'our show notes for those and now you know there can be landlocked property in '
             'Texas.',
      'title': 'Landlocked Property in Texas - What You Need to Know! (Texas Agriculture Law)',
      'url': 'https://www.youtube.com/watch?v=D_ZiLS1CYJg&t=182s',
      'video_id': 'D_ZiLS1CYJg'},
     {'author': 'Once Upon a Brick · The Land Investor',
      'channel': 'Once Upon a Brick · The Land Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:56](https://www.youtube.com/watch?v=Tmf12E9Dg7A&t=416s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And usually, you know, properties with more road frontage, better access, they '
              "have more they are more valuable and they command a higher price. And there's "
              'many things like that, right? Is there utilities going to this piece of land? '
              'You know, how close is electric?',
      'timestamp': 416,
      'timestamp_label': '[00:06:56]',
      'timestamp_seconds': 416,
      'tip': 'And usually, you know, properties with more road frontage, better access, they '
             "have more they are more valuable and they command a higher price. And there's "
             'many things like that, right? Is there utilities going to this piece of land? '
             'You know, how close is electric?',
      'title': "The $10,000 Land Trap: Don't Overpay #landinvesting #realestate (Once Upon a "
               'Brick · The Land Investor)',
      'url': 'https://www.youtube.com/watch?v=Tmf12E9Dg7A&t=416s',
      'video_id': 'Tmf12E9Dg7A'},
     {'author': 'Texas Land Hub',
      'channel': 'Texas Land Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=bwY6HXq0w4g&t=61s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But if you do all the amenities right, it can generate quite a bit more money '
              'in comparison to a mobile home park. The upside of a mobile home park is people '
              'are going to stay there for longer periods of time. The cash flow is going to '
              'be consistent.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': 'But if you do all the amenities right, it can generate quite a bit more money in '
             'comparison to a mobile home park. The upside of a mobile home park is people are '
             'going to stay there for longer periods of time. The cash flow is going to be '
             'consistent.',
      'title': 'Investing in RV vs. Mobile Home Parks|  Key Differences Explained (Texas Land '
               'Hub)',
      'url': 'https://www.youtube.com/watch?v=bwY6HXq0w4g&t=61s',
      'video_id': 'bwY6HXq0w4g'},
     {'author': 'Acrewell Land Company',
      'channel': 'Acrewell Land Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=AYim3zSksEs&t=230s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Advanced enough to do what soil does naturally in a septic system soil purifies '
              'water it does it free of of any cost it just does it naturally there in.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': 'Advanced enough to do what soil does naturally in a septic system soil purifies '
             'water it does it free of of any cost it just does it naturally there in.',
      'title': 'The "Perc Test": Soil and Septic Basics (Acrewell Land Company)',
      'url': 'https://www.youtube.com/watch?v=AYim3zSksEs&t=230s',
      'video_id': 'AYim3zSksEs'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:38](https://www.youtube.com/watch?v=8qUfThwrzAw&t=1898s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Substituted for one of the other trust stores and so I own a I think a one '
              "sixth share so the cost of underwriting it's a tiny lean business Nick Curry "
              'is.',
      'timestamp': 1898,
      'timestamp_label': '[00:31:38]',
      'timestamp_seconds': 1898,
      'tip': 'Substituted for one of the other trust stores and so I own a I think a one sixth '
             "share so the cost of underwriting it's a tiny lean business Nick Curry is.",
      'title': 'Land Funding Expert Steve Hodgdon Breaks Down What Really Matters | REtipster '
               'Podcast 181 (REtipster)',
      'url': 'https://www.youtube.com/watch?v=8qUfThwrzAw&t=1898s',
      'video_id': '8qUfThwrzAw'},
     {'author': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
      'channel': 'Cool Wholesaling+ Land Deals-Real Estate Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=t8XDRE0ZjFc&t=36s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Else down here until you hit South Carolina but so it's south of fville there's "
              "Red Springs St Paul's Rayford and so then we get an idea of where we are and "
              'then we can go on to Zillow and sort of transfer that idea and just pull up uh '
              'you know Red.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "Else down here until you hit South Carolina but so it's south of fville there's "
             "Red Springs St Paul's Rayford and so then we get an idea of where we are and "
             'then we can go on to Zillow and sort of transfer that idea and just pull up uh '
             'you know Red.',
      'title': 'How to use Zillow for comping vacant land ii- Determine the best price to '
               'offer so you can profit (Cool Wholesaling+ Land Deals-Real Estate Investing)',
      'url': 'https://www.youtube.com/watch?v=t8XDRE0ZjFc&t=36s',
      'video_id': 't8XDRE0ZjFc'}],
 4: [{'author': 'Florida Land Facts',
      'channel': 'Florida Land Facts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:31](https://www.youtube.com/watch?v=zWTn3NY8wqc&t=271s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Handshake permission from a neighbor is not access. It can vanish the day they '
              'sell. Check the deed and the recorded plat for an easement or a platted road '
              'and find out who maintains that road, the county or you and the other lot '
              'owners.',
      'timestamp': 271,
      'timestamp_label': '[00:04:31]',
      'timestamp_seconds': 271,
      'tip': 'Handshake permission from a neighbor is not access. It can vanish the day they '
             'sell. Check the deed and the recorded plat for an easement or a platted road and '
             'find out who maintains that road, the county or you and the other lot owners.',
      'title': 'Before You Buy Cheap Florida Land: 7 Checks That Kill Deals (Perc, Septic, '
               'Flood, Access) (Florida Land Facts)',
      'url': 'https://www.youtube.com/watch?v=zWTn3NY8wqc&t=271s',
      'video_id': 'zWTn3NY8wqc'},
     {'author': "The Owner's Math",
      'channel': "The Owner's Math",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:13](https://www.youtube.com/watch?v=xjNh4eemKCs&t=793s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ground rent on raw acreage outside town is cheap. You avoid the single largest '
              'line in the development budget, which drops your capital requirement by half or '
              'more and can take your cash on cash return from good to spectacular.',
      'timestamp': 793,
      'timestamp_label': '[00:13:13]',
      'timestamp_seconds': 793,
      'tip': 'Ground rent on raw acreage outside town is cheap. You avoid the single largest '
             'line in the development budget, which drops your capital requirement by half or '
             'more and can take your cash on cash return from good to spectacular.',
      'title': "The Economics of Owning an RV Storage Lot (The Owner's Math)",
      'url': 'https://www.youtube.com/watch?v=xjNh4eemKCs&t=793s',
      'video_id': 'xjNh4eemKCs'},
     {'author': 'House Cashers LLC',
      'channel': 'House Cashers LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=Up2OF5KmfcU&t=138s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In Georgia, ask your closing attorney. One, find both title lines on your loan '
              "estimate. Two, read the schedule B exceptions. Three, buy the owner's policy "
              'for estate homes, cash deals, or vacant property.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'In Georgia, ask your closing attorney. One, find both title lines on your loan '
             "estimate. Two, read the schedule B exceptions. Three, buy the owner's policy for "
             'estate homes, cash deals, or vacant property.',
      'title': "Owner's Title Insurance: What It Covers, What It Costs, and What Changed "
               '(House Cashers LLC)',
      'url': 'https://www.youtube.com/watch?v=Up2OF5KmfcU&t=138s',
      'video_id': 'Up2OF5KmfcU'},
     {'author': 'LAVERNE MCGEE TV',
      'channel': 'LAVERNE MCGEE TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=ptM7-3KSnO4&t=103s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'YOU CAN ALSO CHECK WITH YOUR LOCAL COUNTY TO SEE IF THEY HAVE THEIR OWN MAPS. '
              'SEMINOLE COUNTY HAS SEVERAL PROJECTS UPDATING THEIR INFORMATION. YOU CAN GIVE '
              'THEM A CALL TO FIND OUT ABOUT FLOOD ZONES THERE. AND FEMA RECOMMENDS THAT '
              'PROPERTY OWNERS, ALL OF THEM GET INSURANCE.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'YOU CAN ALSO CHECK WITH YOUR LOCAL COUNTY TO SEE IF THEY HAVE THEIR OWN MAPS. '
             'SEMINOLE COUNTY HAS SEVERAL PROJECTS UPDATING THEIR INFORMATION. YOU CAN GIVE '
             'THEM A CALL TO FIND OUT ABOUT FLOOD ZONES THERE. AND FEMA RECOMMENDS THAT '
             'PROPERTY OWNERS, ALL OF THEM GET INSURANCE.',
      'title': 'HOW TO READ A FLOOD MAP BY FEMA TO SEE IF YOU ARE IN A FLOOD ZONE (LAVERNE '
               'MCGEE TV)',
      'url': 'https://www.youtube.com/watch?v=ptM7-3KSnO4&t=103s',
      'video_id': 'ptM7-3KSnO4'},
     {'author': 'Flip With Rick',
      'channel': 'Flip With Rick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:30](https://www.youtube.com/watch?v=4Ueirfxr5Ww&t=810s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just do a double closing it's an insurance policy it's not that easy because if "
              "you don't have the funds for it your cash buyer is not down with it I.",
      'timestamp': 810,
      'timestamp_label': '[00:13:30]',
      'timestamp_seconds': 810,
      'tip': "Just do a double closing it's an insurance policy it's not that easy because if "
             "you don't have the funds for it your cash buyer is not down with it I.",
      'title': 'How to Do a Double Closing Wholesaling Deal with No Money Needed! (Flip With '
               'Rick)',
      'url': 'https://www.youtube.com/watch?v=4Ueirfxr5Ww&t=810s',
      'video_id': '4Ueirfxr5Ww'},
     {'author': 'David Reitz',
      'channel': 'David Reitz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:48](https://www.youtube.com/watch?v=WHUzvXvl_18&t=228s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like if you don't want to tie up a bunch of your cash, my audience is primarily "
              'real estate investors, guys that are already in the business. And so cash is '
              'super critical. You know, those of us who are developers and flippers, like we '
              'need our cash, do it on a credit card.',
      'timestamp': 228,
      'timestamp_label': '[00:03:48]',
      'timestamp_seconds': 228,
      'tip': "Like if you don't want to tie up a bunch of your cash, my audience is primarily "
             'real estate investors, guys that are already in the business. And so cash is '
             'super critical. You know, those of us who are developers and flippers, like we '
             'need our cash, do it on a credit card.',
      'title': 'Guide To Subdividing Land: Fastest Profits In Real Estate (David Reitz)',
      'url': 'https://www.youtube.com/watch?v=WHUzvXvl_18&t=228s',
      'video_id': 'WHUzvXvl_18'},
     {'author': 'Financial Times',
      'channel': 'Financial Times',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=QwCGBQ0n2tM&t=138s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Strategically positioned near the energy-sapping data centres in the metroplex '
              'of Dallas-Fort Worth, it’s only a few years old, but already being superseded '
              'by the next generation of larger battery systems coming online.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'Strategically positioned near the energy-sapping data centres in the metroplex '
             'of Dallas-Fort Worth, it’s only a few years old, but already being superseded by '
             'the next generation of larger battery systems coming online.',
      'title': 'Texas’ battery storage: a boom and bust market? | FT Energy Source (Financial '
               'Times)',
      'url': 'https://www.youtube.com/watch?v=QwCGBQ0n2tM&t=138s',
      'video_id': 'QwCGBQ0n2tM'},
     {'author': 'LandApp by LandGate',
      'channel': 'LandApp by LandGate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=2lVnO8IebI0&t=15s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How to solve it so what is a landlocked property a landlocked property is a '
              "parcel of land that doesn't have direct access to a public road or highway "
              "it's.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'How to solve it so what is a landlocked property a landlocked property is a '
             "parcel of land that doesn't have direct access to a public road or highway it's.",
      'title': 'What does landlocked mean, and how do you solve it? (LandApp by LandGate)',
      'url': 'https://www.youtube.com/watch?v=2lVnO8IebI0&t=15s',
      'video_id': '2lVnO8IebI0'},
     {'author': 'The Well Entrepreneur',
      'channel': 'The Well Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:55](https://www.youtube.com/watch?v=p_LcZVcrC3U&t=415s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Check out my website laurenhardyco.com for a free wholesaling mini course hope '
              "you guys enjoy and I'll see you guys next time.",
      'timestamp': 415,
      'timestamp_label': '[00:06:55]',
      'timestamp_seconds': 415,
      'tip': 'Check out my website laurenhardyco.com for a free wholesaling mini course hope '
             "you guys enjoy and I'll see you guys next time.",
      'title': 'How To Get A Cold Call List - Tax Delinquent List (The Well Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=p_LcZVcrC3U&t=415s',
      'video_id': 'p_LcZVcrC3U'},
     {'author': 'Seller Financing, Real Estate & Note Investing',
      'channel': 'Seller Financing, Real Estate & Note Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=X6Bv1fbSvBk&t=290s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You can check that out uh let's see L trust I assume um that means I have to "
              'separate l have to have a separate land trust for each property.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': "You can check that out uh let's see L trust I assume um that means I have to "
             'separate l have to have a separate land trust for each property.',
      'title': 'Q&A: Owner Financing and Selling the Notes, Land Trusts, Dodd-Frank, SAFE Act '
               '(Seller Financing, Real Estate & Note Investing)',
      'url': 'https://www.youtube.com/watch?v=X6Bv1fbSvBk&t=290s',
      'video_id': 'X6Bv1fbSvBk'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:21](https://www.youtube.com/watch?v=JL60o3hoi_w&t=801s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It really is, but it's very easy to misunderstand the opportunity and what is "
              "and isn't available here. If you want to learn more about what this business "
              "has to offer, go check out the library of land investing content that we've "
              'been building for years over at retipster.',
      'timestamp': 801,
      'timestamp_label': '[00:13:21]',
      'timestamp_seconds': 801,
      'tip': "It really is, but it's very easy to misunderstand the opportunity and what is "
             "and isn't available here. If you want to learn more about what this business has "
             "to offer, go check out the library of land investing content that we've been "
             'building for years over at retipster.',
      'title': 'How Land Investing Really Works (REtipster)',
      'url': 'https://www.youtube.com/watch?v=JL60o3hoi_w&t=801s',
      'video_id': 'JL60o3hoi_w'},
     {'author': 'MassDEP',
      'channel': 'MassDEP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:18](https://www.youtube.com/watch?v=lRc-2cEUn7U&t=2418s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mia McDonald: you open the layer list Mia McDonald: with its stack of diamonds. '
              "Mia McDonald: When you open it, it's going to show you that the nfhl, the "
              'National Flood hazard layer.',
      'timestamp': 2418,
      'timestamp_label': '[00:40:18]',
      'timestamp_seconds': 2418,
      'tip': 'Mia McDonald: you open the layer list Mia McDonald: with its stack of diamonds. '
             "Mia McDonald: When you open it, it's going to show you that the nfhl, the "
             'National Flood hazard layer.',
      'title': 'How to Identify Zones in the Land Subject to Coastal Storm Flowage (LSCSF) '
               'from FEMA Maps (MassDEP)',
      'url': 'https://www.youtube.com/watch?v=lRc-2cEUn7U&t=2418s',
      'video_id': 'lRc-2cEUn7U'},
     {'author': 'The Ramsey Show Highlights',
      'channel': 'The Ramsey Show Highlights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:33](https://www.youtube.com/watch?v=svuRdMOkJF4&t=213s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All fall into that same category so you're going to be fine you'll be fine I'm "
              "glad you're concerned about it but don't go get buying you know gimmick "
              "insurance or something get identity theft insurance from xander and that's "
              "plenty you'll be in good shape.",
      'timestamp': 213,
      'timestamp_label': '[00:03:33]',
      'timestamp_seconds': 213,
      'tip': "All fall into that same category so you're going to be fine you'll be fine I'm "
             "glad you're concerned about it but don't go get buying you know gimmick "
             "insurance or something get identity theft insurance from xander and that's "
             "plenty you'll be in good shape.",
      'title': 'What is Title Insurance and Do I Need It? (The Ramsey Show Highlights)',
      'url': 'https://www.youtube.com/watch?v=svuRdMOkJF4&t=213s',
      'video_id': 'svuRdMOkJF4'},
     {'author': 'Get Rich Education',
      'channel': 'Get Rich Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=HubgOyQ00K4&t=192s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That little notification Bell that's the only way you'll be assured of seeing "
              "the next explained series video I'm Keith winhold I'll see you next time you "
              'can watch this one next.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': "That little notification Bell that's the only way you'll be assured of seeing "
             "the next explained series video I'm Keith winhold I'll see you next time you can "
             'watch this one next.',
      'title': 'Title Insurance Explained In Under 4 Minutes! (Get Rich Education)',
      'url': 'https://www.youtube.com/watch?v=HubgOyQ00K4&t=192s',
      'video_id': 'HubgOyQ00K4'},
     {'author': 'Jerome Maldonado',
      'channel': 'Jerome Maldonado',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=ffCHGUtstfA&t=412s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That looks like this right here and you simply go in and you divide that right '
              'in half okay now the lot might be off-site you know it might be something that '
              'kind of looks oblong.',
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': 'That looks like this right here and you simply go in and you divide that right '
             'in half okay now the lot might be off-site you know it might be something that '
             'kind of looks oblong.',
      'title': 'Subdivide Land Guide: Fastest Profits in Real Estate (Jerome Maldonado)',
      'url': 'https://www.youtube.com/watch?v=ffCHGUtstfA&t=412s',
      'video_id': 'ffCHGUtstfA'}],
 5: [{'author': 'Land Academy',
      'channel': 'Land Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:44](https://www.youtube.com/watch?v=NqKIWNpO1Ic&t=344s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That and that that business model really works. Today's topic, the truth about "
              'cold calling, emailing, and texting for land house deals. So, like I said, '
              'could be titled uh four or five ways to contact potential sellers.',
      'timestamp': 344,
      'timestamp_label': '[00:05:44]',
      'timestamp_seconds': 344,
      'tip': "That and that that business model really works. Today's topic, the truth about "
             'cold calling, emailing, and texting for land house deals. So, like I said, could '
             'be titled uh four or five ways to contact potential sellers.',
      'title': 'Why Cold Calling, Emailing & Texting Fail In Real Estate | Land Deal Marketing '
               'Explained (Land Academy)',
      'url': 'https://www.youtube.com/watch?v=NqKIWNpO1Ic&t=344s',
      'video_id': 'NqKIWNpO1Ic'},
     {'author': 'Olufemi Ajose',
      'channel': 'Olufemi Ajose',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=tF_EbilAGj4&t=77s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re able to really turn on a faucet of cash flow with their land flipping "
              'business from sending direct mail. Now those four pillars are branding great '
              'copy framing and problem identification.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "'re able to really turn on a faucet of cash flow with their land flipping "
             'business from sending direct mail. Now those four pillars are branding great '
             'copy framing and problem identification.',
      'title': '$1M flipping vacant land with direct mail | The exact system (Olufemi Ajose)',
      'url': 'https://www.youtube.com/watch?v=tF_EbilAGj4&t=77s',
      'video_id': 'tF_EbilAGj4'},
     {'author': 'Thomas | Land Flipping',
      'channel': 'Thomas | Land Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[04:57:49](https://www.youtube.com/watch?v=ZfyoS572Kbk&t=17869s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've shown you the the mistakes, the easy traps to fall into. It's a lot to "
              "take in, but don't over complicate it. If you stick to these basics that I've "
              'outlined here, you will succeed in this business.',
      'timestamp': 17869,
      'timestamp_label': '[04:57:49]',
      'timestamp_seconds': 17869,
      'tip': "I've shown you the the mistakes, the easy traps to fall into. It's a lot to take "
             "in, but don't over complicate it. If you stick to these basics that I've "
             'outlined here, you will succeed in this business.',
      'title': 'leaking my $63k/month land flipping blueprint (Full Breakdown) (Thomas | Land '
               'Flipping)',
      'url': 'https://www.youtube.com/watch?v=ZfyoS572Kbk&t=17869s',
      'video_id': 'ZfyoS572Kbk'},
     {'author': 'US Realty Training',
      'channel': 'US Realty Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=B_XnC97BYF8&t=210s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Honey, I think we bought a house that has deed restrictions." Well, then we '
              'have a problem. Now, the question then is, well, how do we find out if a house '
              'has a deed restriction? Now, you as a realtor, you have access to this stuff.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': 'Honey, I think we bought a house that has deed restrictions." Well, then we have '
             'a problem. Now, the question then is, well, how do we find out if a house has a '
             'deed restriction? Now, you as a realtor, you have access to this stuff.',
      'title': 'What are Real Estate Deed Restrictions? (US Realty Training)',
      'url': 'https://www.youtube.com/watch?v=B_XnC97BYF8&t=210s',
      'video_id': 'B_XnC97BYF8'},
     {'author': 'HOA LAND WARS',
      'channel': 'HOA LAND WARS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:56](https://www.youtube.com/watch?v=CnlqGcAGqOo&t=596s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I went back through the closing papers on my kitchen table. That was the first '
              'moment the dispute stopped looking like a simple fight over access.',
      'timestamp': 596,
      'timestamp_label': '[00:09:56]',
      'timestamp_seconds': 596,
      'tip': 'I went back through the closing papers on my kitchen table. That was the first '
             'moment the dispute stopped looking like a simple fight over access.',
      'title': 'HOA Signed a Mineral Lease Under My Home—Then the Royalty Trail Led Elsewhere '
               '(HOA LAND WARS)',
      'url': 'https://www.youtube.com/watch?v=CnlqGcAGqOo&t=596s',
      'video_id': 'CnlqGcAGqOo'},
     {'author': 'ACRE Partner',
      'channel': 'ACRE Partner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:07](https://www.youtube.com/watch?v=x1a5YxEWplQ&t=427s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t see what might go wrong. You can't see your blind spots because nothing's "
              "ever gone wrong yet, right? And you haven't learned the hard way. And I've "
              'learned the hard way. And I want to help you avoid all of these mistakes that I '
              'made.',
      'timestamp': 427,
      'timestamp_label': '[00:07:07]',
      'timestamp_seconds': 427,
      'tip': "'t see what might go wrong. You can't see your blind spots because nothing's "
             "ever gone wrong yet, right? And you haven't learned the hard way. And I've "
             'learned the hard way. And I want to help you avoid all of these mistakes that I '
             'made.',
      'title': 'How Real Estate Media Agencies Scale From $10K to $100K+ Per Month (Proven '
               'Blueprint) (ACRE Partner)',
      'url': 'https://www.youtube.com/watch?v=x1a5YxEWplQ&t=427s',
      'video_id': 'x1a5YxEWplQ'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:30](https://www.youtube.com/watch?v=IS6mrT0hkGw&t=1710s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So what I found in due diligence, especially in areas like Idaho, like they '
              "love it when somebody is calling before there's a problem to understand what's "
              'going on with the property.',
      'timestamp': 1710,
      'timestamp_label': '[00:28:30]',
      'timestamp_seconds': 1710,
      'tip': 'So what I found in due diligence, especially in areas like Idaho, like they love '
             "it when somebody is calling before there's a problem to understand what's going "
             'on with the property.',
      'title': 'The Report That Gives Land Investors an Unfair Advantage w/ Don Healy | '
               'REtipster Podcast 258 (REtipster)',
      'url': 'https://www.youtube.com/watch?v=IS6mrT0hkGw&t=1710s',
      'video_id': 'IS6mrT0hkGw'},
     {'author': 'Cody Bjugan',
      'channel': 'Cody Bjugan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:29](https://www.youtube.com/watch?v=1B8q3q_Xt-s&t=29s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's quicker, but also the paydays are relative. If you're just getting started "
              'in the game, I have no problem with you doing minor partitions. I did several '
              'of them in the very beginning days, right, 20 some odd years ago.',
      'timestamp': 29,
      'timestamp_label': '[00:00:29]',
      'timestamp_seconds': 29,
      'tip': "It's quicker, but also the paydays are relative. If you're just getting started "
             'in the game, I have no problem with you doing minor partitions. I did several of '
             'them in the very beginning days, right, 20 some odd years ago.',
      'title': 'Minor Partition vs. Subdivision in Land Development (Cody Bjugan)',
      'url': 'https://www.youtube.com/watch?v=1B8q3q_Xt-s&t=29s',
      'video_id': '1B8q3q_Xt-s'},
     {'author': 'Debt Free Doctor - Dr. Jeff Anzalone',
      'channel': 'Debt Free Doctor - Dr. Jeff Anzalone',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=tZwHEMuaXiQ&t=238s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Streams of income you have to cheaper expenses you have the higher cash rates '
              'so to to answer the most frequently Asked question Jeff why did you start '
              'investing in RV parks now you know the answer.',
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': 'Streams of income you have to cheaper expenses you have the higher cash rates so '
             'to to answer the most frequently Asked question Jeff why did you start investing '
             'in RV parks now you know the answer.',
      'title': 'Buying an RV Park? WATCH THIS to Avoid Mistakes! (Debt Free Doctor - Dr. Jeff '
               'Anzalone)',
      'url': 'https://www.youtube.com/watch?v=tZwHEMuaXiQ&t=238s',
      'video_id': 'tZwHEMuaXiQ'},
     {'author': 'Sunsynk',
      'channel': 'Sunsynk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=VZWhkHs1sXA&t=115s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And I would say to any installer, please make sure you fully understand what '
              "you're installing. Understanding the EMS, the energy management system, "
              "understand its functions, understand how to program it. And if you don't "
              "understand the basics, then that's a problem.",
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'And I would say to any installer, please make sure you fully understand what '
             "you're installing. Understanding the EMS, the energy management system, "
             "understand its functions, understand how to program it. And if you don't "
             "understand the basics, then that's a problem.",
      'title': 'Understanding Commercial & Industrial Solar PV Systems with Battery Storage '
               '(Sunsynk)',
      'url': 'https://www.youtube.com/watch?v=VZWhkHs1sXA&t=115s',
      'video_id': 'VZWhkHs1sXA'},
     {'author': 'Wells, Septic & More',
      'channel': 'Wells, Septic & More',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=F-UdA3MqSzw&t=105s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Going to go back to the county and you're going to say hey Mr County guy here's "
              "what I'm working with I want to build a four-bedroom house on this.",
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "Going to go back to the county and you're going to say hey Mr County guy here's "
             "what I'm working with I want to build a four-bedroom house on this.",
      'title': 'What Happens When You Fail a Perc Test For A Septic System (Wells, Septic & '
               'More)',
      'url': 'https://www.youtube.com/watch?v=F-UdA3MqSzw&t=105s',
      'video_id': 'F-UdA3MqSzw'},
     {'author': 'Jerome Maldonado',
      'channel': 'Jerome Maldonado',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=fNHhVpzVhdo&t=15s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Apartment complexes while I'm doing any other real estate or business "
              'transaction small simple subdivides have always been advantageous and '
              'extremely.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Apartment complexes while I'm doing any other real estate or business "
             'transaction small simple subdivides have always been advantageous and extremely.',
      'title': 'How to Subdivide Land for Maximum Profit (Jerome Maldonado)',
      'url': 'https://www.youtube.com/watch?v=fNHhVpzVhdo&t=15s',
      'video_id': 'fNHhVpzVhdo'},
     {'author': 'Country Land Sellers',
      'channel': 'Country Land Sellers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=6qNh515jvww&t=520s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Five four one three seven five zero zero one two or just email us at support at '
              'the farm finders comm thanks for timing I have video is helpful.',
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': 'Five four one three seven five zero zero one two or just email us at support at '
             'the farm finders comm thanks for timing I have video is helpful.',
      'title': 'The Secret to researching land easily with County GIS! (Country Land Sellers)',
      'url': 'https://www.youtube.com/watch?v=6qNh515jvww&t=520s',
      'video_id': '6qNh515jvww'},
     {'author': 'DGB Media',
      'channel': 'DGB Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:17](https://www.youtube.com/watch?v=4KWC7a6vLcY&t=2957s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know on the entrepreneur tip of course thank you thank you thank you man '
              'thanks for having us yes sir all right bet my hting hard and my pockets on full '
              "I got it out the streets I ain't never go to school I play the rear view.",
      'timestamp': 2957,
      'timestamp_label': '[00:49:17]',
      'timestamp_seconds': 2957,
      'tip': 'You know on the entrepreneur tip of course thank you thank you thank you man '
             'thanks for having us yes sir all right bet my hting hard and my pockets on full '
             "I got it out the streets I ain't never go to school I play the rear view.",
      'title': 'How to Flip Land and Make $20,000 Texting with The Land Flipping Empire (DGB '
               'Media)',
      'url': 'https://www.youtube.com/watch?v=4KWC7a6vLcY&t=2957s',
      'video_id': '4KWC7a6vLcY'},
     {'author': 'MassDEP',
      'channel': 'MassDEP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=Q3kV6OiudSU&t=145s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Took to go down those three inches and you divide that by three and that is the '
              'percolation rate in minutes per inch how many minutes per inch did it take to '
              'go for the last three inches that is the actual final stage of the percolation '
              'test.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'Took to go down those three inches and you divide that by three and that is the '
             'percolation rate in minutes per inch how many minutes per inch did it take to go '
             'for the last three inches that is the actual final stage of the percolation '
             'test.',
      'title': 'Perc Tests (MassDEP)',
      'url': 'https://www.youtube.com/watch?v=Q3kV6OiudSU&t=145s',
      'video_id': 'Q3kV6OiudSU'}],
 6: [{'author': 'Michael Bull',
      'channel': 'Michael Bull',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:34](https://www.youtube.com/watch?v=PMSn1EaZ42Y&t=634s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Maybe we start with cold calling and get a first deal or two and then '
              'transition over to direct mail because it does cost some money. So, just to '
              'rehash the three, we have direct mail, cold calling, and cold texting. All '
              'three are very profitable.',
      'timestamp': 634,
      'timestamp_label': '[00:10:34]',
      'timestamp_seconds': 634,
      'tip': 'Maybe we start with cold calling and get a first deal or two and then transition '
             'over to direct mail because it does cost some money. So, just to rehash the '
             'three, we have direct mail, cold calling, and cold texting. All three are very '
             'profitable.',
      'title': 'Cold Calling vs Cold Texting vs Direct Mail: Which One Actually Works Best for '
               'Land Flipping? (Michael Bull)',
      'url': 'https://www.youtube.com/watch?v=PMSn1EaZ42Y&t=634s',
      'video_id': 'PMSn1EaZ42Y'},
     {'author': 'Maximilian Dier',
      'channel': 'Maximilian Dier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:20](https://www.youtube.com/watch?v=KmEcpx-t8YM&t=560s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Guys, it it doesn't matter what year it is. These are the best lists and this "
              "will always be the best list whether you're doing massive outreach for cold "
              "calling or text blasting or if you're just trying to do some niche dialing and "
              'try to get your first wholesale deal.',
      'timestamp': 560,
      'timestamp_label': '[00:09:20]',
      'timestamp_seconds': 560,
      'tip': "Guys, it it doesn't matter what year it is. These are the best lists and this "
             "will always be the best list whether you're doing massive outreach for cold "
             "calling or text blasting or if you're just trying to do some niche dialing and "
             'try to get your first wholesale deal.',
      'title': 'How to Pull The BEST Wholesale List For Cold Calling & Texting (Maximilian '
               'Dier)',
      'url': 'https://www.youtube.com/watch?v=KmEcpx-t8YM&t=560s',
      'video_id': 'KmEcpx-t8YM'},
     {'author': 'Joséphine Saffert',
      'channel': 'Joséphine Saffert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:14](https://www.youtube.com/watch?v=_kxaCpUojPw&t=614s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now you know how to navigate the parser viewer and pull the data developers '
              'rely on to uncover great opportunities. But if you want to go deeper, actually '
              'learn how to find, land, fund the deal, and manage development projects, join '
              'me inside Developer Academy.',
      'timestamp': 614,
      'timestamp_label': '[00:10:14]',
      'timestamp_seconds': 614,
      'tip': 'Now you know how to navigate the parser viewer and pull the data developers rely '
             'on to uncover great opportunities. But if you want to go deeper, actually learn '
             'how to find, land, fund the deal, and manage development projects, join me '
             'inside Developer Academy.',
      'title': 'Parcel Viewer Tutorial: How To Find Land Deals Fast (Joséphine Saffert)',
      'url': 'https://www.youtube.com/watch?v=_kxaCpUojPw&t=614s',
      'video_id': '_kxaCpUojPw'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=E9KBudZB1Do&t=78s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s just see what kind of data we can find there. And when you do this search, "
              "this is the kind of thing you're going to initially see. And what you want to "
              'do is, first of all, go up here where it says listing type.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "'s just see what kind of data we can find there. And when you do this search, "
             "this is the kind of thing you're going to initially see. And what you want to do "
             'is, first of all, go up here where it says listing type.',
      'title': 'How to Find the Best Counties for Land Investing with Zillow (REtipster)',
      'url': 'https://www.youtube.com/watch?v=E9KBudZB1Do&t=78s',
      'video_id': 'E9KBudZB1Do'},
     {'author': 'Peter Kelly Property',
      'channel': 'Peter Kelly Property',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=KmCwZ5I6BYU&t=216s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I study is the position of the existing home. How it relates to its boundaries '
              'and what this means for access, layout, and the livability of the home at the '
              'rear. That leads into the next big deal breaker, which is the vehicle access.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'I study is the position of the existing home. How it relates to its boundaries '
             'and what this means for access, layout, and the livability of the home at the '
             'rear. That leads into the next big deal breaker, which is the vehicle access.',
      'title': 'Backyard Subdivision, What Most People Get Wrong (Peter Kelly Property)',
      'url': 'https://www.youtube.com/watch?v=KmCwZ5I6BYU&t=216s',
      'video_id': 'KmCwZ5I6BYU'},
     {'author': 'Danielle Dojcak',
      'channel': 'Danielle Dojcak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=ieOUjD1jQXA&t=38s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '" cuz you want to find out so you can do the digging to find out if there\'s '
              "any uh deed restriction recorded in the land that's going to prevent them from "
              'having that ability to do what they want. So, no HOA does not necessarily mean '
              'no restrictive covenants.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': '" cuz you want to find out so you can do the digging to find out if there\'s any '
             "uh deed restriction recorded in the land that's going to prevent them from "
             'having that ability to do what they want. So, no HOA does not necessarily mean '
             'no restrictive covenants.',
      'title': 'Did you know, NO HOA does not mean NO Rules? #hoa #landrestrictions '
               '#landusepolicy #land (Danielle Dojcak)',
      'url': 'https://www.youtube.com/watch?v=ieOUjD1jQXA&t=38s',
      'video_id': 'ieOUjD1jQXA'},
     {'author': 'Just Call Maggie',
      'channel': 'Just Call Maggie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=sazxc_VdXOw&t=56s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First up, we have deed conditions or restrictions, also known as restrictive '
              'covenants. These are specific limitations written into the property deed by the '
              'seller and outline conditions the new owner must follow.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'First up, we have deed conditions or restrictions, also known as restrictive '
             'covenants. These are specific limitations written into the property deed by the '
             'seller and outline conditions the new owner must follow.',
      'title': 'Real Estate Exam Prep: Understanding Private Property Restrictions (Just Call '
               'Maggie)',
      'url': 'https://www.youtube.com/watch?v=sazxc_VdXOw&t=56s',
      'video_id': 'sazxc_VdXOw'},
     {'author': 'Once Upon a Brick · The Land Investor',
      'channel': 'Once Upon a Brick · The Land Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:40](https://www.youtube.com/watch?v=QB6c4nBfXrs&t=280s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '99 and make your payments $249 until you pay off the 17,000. And often '
              "depending on the type of deal and the seller, there's no there's probably no "
              'credit check. And then we can see right here the taxes are 48 bucks a year.',
      'timestamp': 280,
      'timestamp_label': '[00:04:40]',
      'timestamp_seconds': 280,
      'tip': '99 and make your payments $249 until you pay off the 17,000. And often depending '
             "on the type of deal and the seller, there's no there's probably no credit check. "
             'And then we can see right here the taxes are 48 bucks a year.',
      'title': 'How to Find Land Deals (LandWatch, LandSearch & Hidden Sources) #realestate '
               '(Once Upon a Brick · The Land Investor)',
      'url': 'https://www.youtube.com/watch?v=QB6c4nBfXrs&t=280s',
      'video_id': 'QB6c4nBfXrs'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:33](https://www.youtube.com/watch?v=LDjHRRkWVYE&t=933s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Buying flips and then negotiating on that end but let's talk about for the "
              'people who just want to go after Double closing yeah I mean you find a data.',
      'timestamp': 933,
      'timestamp_label': '[00:15:33]',
      'timestamp_seconds': 933,
      'tip': "Buying flips and then negotiating on that end but let's talk about for the "
             'people who just want to go after Double closing yeah I mean you find a data.',
      'title': 'How to Use Double Closing to Dominate Land Investing with Zero Money Down '
               '(Apke Brothers)',
      'url': 'https://www.youtube.com/watch?v=LDjHRRkWVYE&t=933s',
      'video_id': 'LDjHRRkWVYE'},
     {'author': 'Ryan Dossey',
      'channel': 'Ryan Dossey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=1VVAkFWqVKE&t=431s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would you be interested in selling your house at blank to a client of mine if '
              "so please call me at blank we're going to track all of the leads inside of a "
              'CRM I.',
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': 'Would you be interested in selling your house at blank to a client of mine if so '
             "please call me at blank we're going to track all of the leads inside of a CRM I.",
      'title': 'How I Got 2 Listings from 1 Direct Mail Campaign (Step-by-Step Guide for '
               'Realtors) (Ryan Dossey)',
      'url': 'https://www.youtube.com/watch?v=1VVAkFWqVKE&t=431s',
      'video_id': '1VVAkFWqVKE'},
     {'author': 'Simple Explain',
      'channel': 'Simple Explain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=e7VCFv7koQE&t=124s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Neighboring land is used to provide such access there are various types of '
              'easements some easier to acquire than others but Savvy buyers who understand '
              'the rules can find good investments in landlocked.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'Neighboring land is used to provide such access there are various types of '
             'easements some easier to acquire than others but Savvy buyers who understand the '
             'rules can find good investments in landlocked.',
      'title': 'Landlocked: Definition in Real Estate and Easement Solution (Simple Explain)',
      'url': 'https://www.youtube.com/watch?v=e7VCFv7koQE&t=124s',
      'video_id': 'e7VCFv7koQE'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=WmRK4kG81e4&t=33s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sometimes you can get away without some of these things on the super cheap '
              'deals, but a lot of times it just takes a lot of work to figure out, is this '
              'even a good deal in the first place?',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Sometimes you can get away without some of these things on the super cheap '
             'deals, but a lot of times it just takes a lot of work to figure out, is this '
             'even a good deal in the first place?',
      'title': 'Land Flipping is NOT a Passive Investment Strategy (REtipster)',
      'url': 'https://www.youtube.com/watch?v=WmRK4kG81e4&t=33s',
      'video_id': 'WmRK4kG81e4'},
     {'author': 'Phill Grove',
      'channel': 'Phill Grove',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=B1mBRW8QMrw&t=175s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would like to join us on this webinar well somewhere uh on this video you can '
              'click a button or find a a way you can uh join us register for the video and '
              "and the uh uh webinar and we'll see you there I look forward to it all right.",
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'Would like to join us on this webinar well somewhere uh on this video you can '
             'click a button or find a a way you can uh join us register for the video and and '
             "the uh uh webinar and we'll see you there I look forward to it all right.",
      'title': 'Owner Finance Webinar - The Dodd-Frank Act EXPOSED! (Phill Grove)',
      'url': 'https://www.youtube.com/watch?v=B1mBRW8QMrw&t=175s',
      'video_id': 'B1mBRW8QMrw'},
     {'author': 'Compass Land USA',
      'channel': 'Compass Land USA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=bPbMFP-bGyU&t=259s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That way you're the very first to know when a new property tour video is "
              "published thank you so much for watching I'll talk to you soon.",
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': "That way you're the very first to know when a new property tour video is "
             "published thank you so much for watching I'll talk to you soon.",
      'title': 'How to Change Flood Zone Determination (with FEMA LOMA) (Compass Land USA)',
      'url': 'https://www.youtube.com/watch?v=bPbMFP-bGyU&t=259s',
      'video_id': 'bPbMFP-bGyU'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:48](https://www.youtube.com/watch?v=9cX2NuhnYro&t=888s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's growth in this area or there's a new school being built or a new "
              'employer is coming into town or maybe they list a lot of vacant lots and they '
              'deal with this type of property all the time.',
      'timestamp': 888,
      'timestamp_label': '[00:14:48]',
      'timestamp_seconds': 888,
      'tip': "There's growth in this area or there's a new school being built or a new "
             'employer is coming into town or maybe they list a lot of vacant lots and they '
             'deal with this type of property all the time.',
      'title': 'How to Find Land Values and Market Insights with Zillow (REtipster)',
      'url': 'https://www.youtube.com/watch?v=9cX2NuhnYro&t=888s',
      'video_id': '9cX2NuhnYro'}],
 7: [{'author': 'Content Marketing Course Reviews by Ippei',
      'channel': 'Content Marketing Course Reviews by Ippei',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:09](https://www.youtube.com/watch?v=NoB05d5Eap4&t=249s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2006, just before weathering the 2008 housing market crash, teaches students to '
              'source potential deals primarily through tax delinquent lists obtained either '
              'directly from county records or through specialized online data providers.',
      'timestamp': 249,
      'timestamp_label': '[00:04:09]',
      'timestamp_seconds': 249,
      'tip': '2006, just before weathering the 2008 housing market crash, teaches students to '
             'source potential deals primarily through tax delinquent lists obtained either '
             'directly from county records or through specialized online data providers.',
      'title': 'REtipster Review - Seth Williams Land Investing Course (Cost Are Crazy!) '
               '(Content Marketing Course Reviews by Ippei)',
      'url': 'https://www.youtube.com/watch?v=NoB05d5Eap4&t=249s',
      'video_id': 'NoB05d5Eap4'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:17](https://www.youtube.com/watch?v=bFiThXyiz7c&t=1157s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Getting leads coming in from any place that's not Direct Mail you'll definitely "
              'want to go through some extra steps to verify that that seller actually is who.',
      'timestamp': 1157,
      'timestamp_label': '[00:19:17]',
      'timestamp_seconds': 1157,
      'tip': "Getting leads coming in from any place that's not Direct Mail you'll definitely "
             'want to go through some extra steps to verify that that seller actually is who.',
      'title': 'Land Flipping for Beginners: The Full 7-Step Process (REtipster)',
      'url': 'https://www.youtube.com/watch?v=bFiThXyiz7c&t=1157s',
      'video_id': 'bFiThXyiz7c'},
     {'author': 'Clay Hepler',
      'channel': 'Clay Hepler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=c8ekY72VGy0&t=494s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "People think it's just market selection. It's not just market selection. It's "
              'market selection and data selection, right? So, [snorts] last thing is '
              'marketing selection. Now, there are five core ways that people get deals in '
              'this business.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': "People think it's just market selection. It's not just market selection. It's "
             'market selection and data selection, right? So, [snorts] last thing is marketing '
             'selection. Now, there are five core ways that people get deals in this business.',
      'title': 'The 4-Channel Marketing System That Makes Me $3M in Land Deals (Clay Hepler)',
      'url': 'https://www.youtube.com/watch?v=c8ekY72VGy0&t=494s',
      'video_id': 'c8ekY72VGy0'},
     {'author': 'EltonDP',
      'channel': 'EltonDP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:34](https://www.youtube.com/watch?v=sM7ge9ahsGY&t=214s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We also have the quality control from the manufacturer as well as for '
              'electrical work come out, check if we installed everything correctly, approve '
              'our work, and then we continue using the same process all down the field.',
      'timestamp': 214,
      'timestamp_label': '[00:03:34]',
      'timestamp_seconds': 214,
      'tip': 'We also have the quality control from the manufacturer as well as for electrical '
             'work come out, check if we installed everything correctly, approve our work, and '
             'then we continue using the same process all down the field.',
      'title': 'How a Solar Farm is Constructed From Beginning to End (EltonDP)',
      'url': 'https://www.youtube.com/watch?v=sM7ge9ahsGY&t=214s',
      'video_id': 'sM7ge9ahsGY'},
     {'author': 'Gaurav J - TheElectricalGuy',
      'channel': 'Gaurav J - TheElectricalGuy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:44](https://www.youtube.com/watch?v=GNmL-gBPe3g&t=764s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'EMS energy management system. So all the data will flow through them and they '
              'can make the right decision. So you can say the BMS is the watchdog of complete '
              'battery energy system especially the battery modules.',
      'timestamp': 764,
      'timestamp_label': '[00:12:44]',
      'timestamp_seconds': 764,
      'tip': 'EMS energy management system. So all the data will flow through them and they '
             'can make the right decision. So you can say the BMS is the watchdog of complete '
             'battery energy system especially the battery modules.',
      'title': 'Battery Energy Storage System | BESS | All Components Explained (Gaurav J - '
               'TheElectricalGuy)',
      'url': 'https://www.youtube.com/watch?v=GNmL-gBPe3g&t=764s',
      'video_id': 'GNmL-gBPe3g'},
     {'author': 'Liberty Acres',
      'channel': 'Liberty Acres',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=qSoWEXftiCQ&t=104s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Huntsville says its subdivision process takes about 120 days start to finish if '
              'no obstacles come up. Liberty Acres is a family-owned land company based in '
              'Atlanta. Thinking about selling land you could subdivide?',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Huntsville says its subdivision process takes about 120 days start to finish if '
             'no obstacles come up. Liberty Acres is a family-owned land company based in '
             'Atlanta. Thinking about selling land you could subdivide?',
      'title': 'How to Subdivide Land: Steps, Costs and Approvals (Liberty Acres)',
      'url': 'https://www.youtube.com/watch?v=qSoWEXftiCQ&t=104s',
      'video_id': 'qSoWEXftiCQ'},
     {'author': 'Zach Ginn',
      'channel': 'Zach Ginn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=3VKazhO11yk&t=184s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The property so whenever it's sold it has to get paid when it's an attacks "
              'delinquent which is usually under two years now each county is different guys.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': "The property so whenever it's sold it has to get paid when it's an attacks "
             'delinquent which is usually under two years now each county is different guys.',
      'title': 'Wholesaling Tax Delinquent Properties (Step by Step) (Zach Ginn)',
      'url': 'https://www.youtube.com/watch?v=3VKazhO11yk&t=184s',
      'video_id': '3VKazhO11yk'},
     {'author': 'PRYCD',
      'channel': 'PRYCD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=7jGQIvwqBwc&t=15s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Step by step of the way to make sure you're getting the most out of our system "
              "so we're going to go through pages such as our research page.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Step by step of the way to make sure you're getting the most out of our system "
             "so we're going to go through pages such as our research page.",
      'title': 'PRYCD Land Step-By-Step Process Flow (PRYCD)',
      'url': 'https://www.youtube.com/watch?v=7jGQIvwqBwc&t=15s',
      'video_id': '7jGQIvwqBwc'},
     {'author': 'Delaware Valley Septic, Sewer, & Storm',
      'channel': 'Delaware Valley Septic, Sewer, & Storm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=F5XXV-dhw1Q&t=131s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Standing on top of um is flooding so what we're doing is we're testing right "
              'below it for a whole new system I laid out oversized bed for a very large house '
              "so now we're just waiting on the inspector to come check out the soils to see "
              'if we can get approved.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': "Standing on top of um is flooding so what we're doing is we're testing right "
             'below it for a whole new system I laid out oversized bed for a very large house '
             "so now we're just waiting on the inspector to come check out the soils to see if "
             'we can get approved.',
      'title': 'Perc Test Walkthrough (Delaware Valley Septic, Sewer, & Storm)',
      'url': 'https://www.youtube.com/watch?v=F5XXV-dhw1Q&t=131s',
      'video_id': 'F5XXV-dhw1Q'},
     {'author': 'William Bronchick',
      'channel': 'William Bronchick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:21](https://www.youtube.com/watch?v=ZGvGq-_10yA&t=1941s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Could verify the information and then they're going to print out a bunch of "
              "disclosures and then you're going to have your buy or sign that at closing with "
              'all your other title company and so forth.',
      'timestamp': 1941,
      'timestamp_label': '[00:32:21]',
      'timestamp_seconds': 1941,
      'tip': "Could verify the information and then they're going to print out a bunch of "
             "disclosures and then you're going to have your buy or sign that at closing with "
             'all your other title company and so forth.',
      'title': 'Webinar Weds: Understanding Dodd-Frank and Seller Financing (William '
               'Bronchick)',
      'url': 'https://www.youtube.com/watch?v=ZGvGq-_10yA&t=1941s',
      'video_id': 'ZGvGq-_10yA'},
     {'author': 'Soils Inc. & VA Septic',
      'channel': 'Soils Inc. & VA Septic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=vTDxU1jKGSI&t=15s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Department review and John why do we uh why do we do these Health Department '
              "reviews to confirm that it's in compliance with state and local.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Department review and John why do we uh why do we do these Health Department '
             "reviews to confirm that it's in compliance with state and local.",
      'title': 'Septic System Safety: Soil Testing and Health Dept. Review on Unique Land '
               '(Soils Inc. & VA Septic)',
      'url': 'https://www.youtube.com/watch?v=vTDxU1jKGSI&t=15s',
      'video_id': 'vTDxU1jKGSI'},
     {'author': 'Mason Dixon Acres',
      'channel': 'Mason Dixon Acres',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=8h9gMkksdD8&t=117s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Back porch or something but in short a site with that much rock and that large '
              'of rock is just not suitable for a septic system of any type.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Back porch or something but in short a site with that much rock and that large '
             'of rock is just not suitable for a septic system of any type.',
      'title': 'We Failed Our Septic Test. Now What? (Mason Dixon Acres)',
      'url': 'https://www.youtube.com/watch?v=8h9gMkksdD8&t=117s',
      'video_id': '8h9gMkksdD8'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:33](https://www.youtube.com/watch?v=potSOIxnw0E&t=2853s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bureau of Land Management and they have this vast record system and '
              'interestingly enough you can go this leg Legacy rehost system actually lets you '
              'search for mineral and gas and oil leases throughout the country so you can go '
              'there to the blm.gov.',
      'timestamp': 2853,
      'timestamp_label': '[00:47:33]',
      'timestamp_seconds': 2853,
      'tip': 'Bureau of Land Management and they have this vast record system and '
             'interestingly enough you can go this leg Legacy rehost system actually lets you '
             'search for mineral and gas and oil leases throughout the country so you can go '
             'there to the blm.gov.',
      'title': 'Land Rights: Grazing, Timber and Mineral Rights and Leases for Genealogists - '
               'James Tanner (BYU Library Family History Center)',
      'url': 'https://www.youtube.com/watch?v=potSOIxnw0E&t=2853s',
      'video_id': 'potSOIxnw0E'},
     {'author': 'Tim Howell',
      'channel': 'Tim Howell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=rtRAjfGZ_nY&t=180s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You still have to come out and touch a road so one way you could come out is '
              'possibly come over here down here run right next to this property here come '
              'over I went backwards sorry.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'You still have to come out and touch a road so one way you could come out is '
             'possibly come over here down here run right next to this property here come over '
             'I went backwards sorry.',
      'title': 'Subdivisions and road frontage (Tim Howell)',
      'url': 'https://www.youtube.com/watch?v=rtRAjfGZ_nY&t=180s',
      'video_id': 'rtRAjfGZ_nY'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:45](https://www.youtube.com/watch?v=yp6qPMTkjgE&t=345s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re at on the property, so be sure to check that out if you're doing this. "
              'Another thing to keep in mind is that it is possible in some areas to build '
              "what's called a modified septic system.",
      'timestamp': 345,
      'timestamp_label': '[00:05:45]',
      'timestamp_seconds': 345,
      'tip': "'re at on the property, so be sure to check that out if you're doing this. "
             'Another thing to keep in mind is that it is possible in some areas to build '
             "what's called a modified septic system.",
      'title': 'What the Heck is a "Perc Test" (and How Much Does it Really Matter)? '
               '(REtipster)',
      'url': 'https://www.youtube.com/watch?v=yp6qPMTkjgE&t=345s',
      'video_id': 'yp6qPMTkjgE'}],
 8: [{'author': 'Acrewell Land Company',
      'channel': 'Acrewell Land Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:34](https://www.youtube.com/watch?v=TbH_4hSsYHU&t=694s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Land Portal, I could click the map search menu and I would enter the state '
              'Georgia, the county Camden, and I would set acreage filters however I wanted '
              "to. Let's just say I'd go to type land and I would search minimum acres two, "
              'maximum acres five.',
      'timestamp': 694,
      'timestamp_label': '[00:11:34]',
      'timestamp_seconds': 694,
      'tip': 'Land Portal, I could click the map search menu and I would enter the state '
             'Georgia, the county Camden, and I would set acreage filters however I wanted to. '
             "Let's just say I'd go to type land and I would search minimum acres two, maximum "
             'acres five.',
      'title': 'Zillow Is Lying To You About Land Prices (Acrewell Land Company)',
      'url': 'https://www.youtube.com/watch?v=TbH_4hSsYHU&t=694s',
      'video_id': 'TbH_4hSsYHU'},
     {'author': 'Sumner Advanced',
      'channel': 'Sumner Advanced',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=zyoO3FxrTDQ&t=184s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um if you have someone that that doesn't work for, you know, 90 days probably "
              "wasn't going to work for them either. And that's probably more of a cash "
              'closing candidate. But most of our double close folks that just has had no '
              'appreciable difference.',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': "Um if you have someone that that doesn't work for, you know, 90 days probably "
             "wasn't going to work for them either. And that's probably more of a cash closing "
             'candidate. But most of our double close folks that just has had no appreciable '
             'difference.',
      'title': 'How We Double Close Land Deals Without Killing Our Profit (Sumner Advanced)',
      'url': 'https://www.youtube.com/watch?v=zyoO3FxrTDQ&t=184s',
      'video_id': 'zyoO3FxrTDQ'},
     {'author': 'Real Estate Pros Show',
      'channel': 'Real Estate Pros Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=Z_ZynszdCFo&t=137s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And in 2023, we started developing Land Portal, which is a data software '
              'essentially a data provider for land properties in particular where you can '
              'filter based on land attributes, not just like the square footage of the house '
              'or all these other things.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'And in 2023, we started developing Land Portal, which is a data software '
             'essentially a data provider for land properties in particular where you can '
             'filter based on land attributes, not just like the square footage of the house '
             'or all these other things.',
      'title': 'How Ron Apke Made $700K Profit in His First Year Flipping Vacant Land | Land '
               'Investing Explained (Real Estate Pros Show)',
      'url': 'https://www.youtube.com/watch?v=Z_ZynszdCFo&t=137s',
      'video_id': 'Z_ZynszdCFo'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:58](https://www.youtube.com/watch?v=8LneZstpCGY&t=598s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, we're going to do that for an example property within Lamp Portal. We found "
              'Carroll County, Georgia. Great market for subdividing based on the numbers. '
              "Let's say we sent them direct mail and we have some leads coming back.",
      'timestamp': 598,
      'timestamp_label': '[00:09:58]',
      'timestamp_seconds': 598,
      'tip': "So, we're going to do that for an example property within Lamp Portal. We found "
             'Carroll County, Georgia. Great market for subdividing based on the numbers. '
             "Let's say we sent them direct mail and we have some leads coming back.",
      'title': 'Subdivide Land With These Simple Steps (Apke Brothers)',
      'url': 'https://www.youtube.com/watch?v=8LneZstpCGY&t=598s',
      'video_id': '8LneZstpCGY'},
     {'author': 'Casey Joiner',
      'channel': 'Casey Joiner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:20](https://www.youtube.com/watch?v=z_2D2D6Cusc&t=1400s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I didn't do was check the with the county and get a permit to subdivide the "
              "parcel. There's certain exemptions that uh the county has that we may have "
              'fallen under, but uh you know, a lot of these communities kind of like Graden '
              'to some extent.',
      'timestamp': 1400,
      'timestamp_label': '[00:23:20]',
      'timestamp_seconds': 1400,
      'tip': "I didn't do was check the with the county and get a permit to subdivide the "
             "parcel. There's certain exemptions that uh the county has that we may have "
             'fallen under, but uh you know, a lot of these communities kind of like Graden to '
             'some extent.',
      'title': 'Florida Title Insurance Explained - What Buyers MUST Know Before Closing '
               '(Casey Joiner)',
      'url': 'https://www.youtube.com/watch?v=z_2D2D6Cusc&t=1400s',
      'video_id': 'z_2D2D6Cusc'},
     {'author': 'PushLeads',
      'channel': 'PushLeads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=fXtOfFlKqmc&t=247s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Next, get an elevation certificate from a licensed surveyor. That document, '
              'costing $400 to $800, is the single most powerful tool for controlling your '
              'premium every foot above base flood elevation earns a meaningful discount. '
              'Before any renovation, check your zone first.',
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': 'Next, get an elevation certificate from a licensed surveyor. That document, '
             'costing $400 to $800, is the single most powerful tool for controlling your '
             'premium every foot above base flood elevation earns a meaningful discount. '
             'Before any renovation, check your zone first.',
      'title': 'What is a FEMA flood zone and does it affect your claim? (PushLeads)',
      'url': 'https://www.youtube.com/watch?v=fXtOfFlKqmc&t=247s',
      'video_id': 'fXtOfFlKqmc'},
     {'author': 'SpeedFreakLS1',
      'channel': 'SpeedFreakLS1',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:24](https://www.youtube.com/watch?v=tBKeO4d6hqc&t=624s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, it all had to be tested here. I didn't see that testing, but I imagine "
              "they've got some sort of heat source. They'll stand on top or around the "
              'battery and ensure that that sensor is picking up the correct battery and '
              'sending that data back to the house.',
      'timestamp': 624,
      'timestamp_label': '[00:10:24]',
      'timestamp_seconds': 624,
      'tip': "So, it all had to be tested here. I didn't see that testing, but I imagine "
             "they've got some sort of heat source. They'll stand on top or around the battery "
             'and ensure that that sensor is picking up the correct battery and sending that '
             'data back to the house.',
      'title': 'Battery Energy Storage Systems (BESS) (SpeedFreakLS1)',
      'url': 'https://www.youtube.com/watch?v=tBKeO4d6hqc&t=624s',
      'video_id': 'tBKeO4d6hqc'},
     {'author': 'For Land and Country',
      'channel': 'For Land and Country',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:48](https://www.youtube.com/watch?v=7FfLOUMhyyA&t=768s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Zillow and then I'll also use the land portal to look at this as well. We have "
              "a comping tool in land portal. Actually, let's just do that. That'll make it "
              'really easy. We can create a report here. We can go to a custom comp report.',
      'timestamp': 768,
      'timestamp_label': '[00:12:48]',
      'timestamp_seconds': 768,
      'tip': "Zillow and then I'll also use the land portal to look at this as well. We have a "
             "comping tool in land portal. Actually, let's just do that. That'll make it "
             'really easy. We can create a report here. We can go to a custom comp report.',
      'title': 'This Zillow Property Looks PERFECT for a Family Compound… But Is It? (For Land '
               'and Country)',
      'url': 'https://www.youtube.com/watch?v=7FfLOUMhyyA&t=768s',
      'video_id': '7FfLOUMhyyA'},
     {'author': 'Land Academy',
      'channel': 'Land Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=qBNi7kpsYC4&t=126s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Amazing tool >> and we resolved this among many many other things that are now '
              "being uh there we're expecting academy members and ourselves to manually "
              'execute all this right.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Amazing tool >> and we resolved this among many many other things that are now '
             "being uh there we're expecting academy members and ourselves to manually execute "
             'all this right.',
      'title': 'Why Neutral Letters Don’t Work In Land Flipping | Avoid These Common Mailer '
               'Mistakes (Land Academy)',
      'url': 'https://www.youtube.com/watch?v=qBNi7kpsYC4&t=126s',
      'video_id': 'qBNi7kpsYC4'},
     {'author': 'WE ARE LAND SPECIALISTS',
      'channel': 'WE ARE LAND SPECIALISTS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:05](https://www.youtube.com/watch?v=JRa_lwdSNjo&t=125s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All right so the apn this is nashville all right so what county is this one '
              "second mecklenburg all right mecklenburg county let me see what's up with mr "
              'michael martin.',
      'timestamp': 125,
      'timestamp_label': '[00:02:05]',
      'timestamp_seconds': 125,
      'tip': 'All right so the apn this is nashville all right so what county is this one '
             "second mecklenburg all right mecklenburg county let me see what's up with mr "
             'michael martin.',
      'title': 'HOW TO RUN VACANT LAND COMPS USING ZILLOW | LAND SPECIALIST (WE ARE LAND '
               'SPECIALISTS)',
      'url': 'https://www.youtube.com/watch?v=JRa_lwdSNjo&t=125s',
      'video_id': 'JRa_lwdSNjo'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:59](https://www.youtube.com/watch?v=JRIbKp3FaEs&t=419s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um but like I said priced can be a tool a resource I'm not pushing guys away "
              "from it but I don't want people putting in 40 for X County and just.",
      'timestamp': 419,
      'timestamp_label': '[00:06:59]',
      'timestamp_seconds': 419,
      'tip': "Um but like I said priced can be a tool a resource I'm not pushing guys away "
             "from it but I don't want people putting in 40 for X County and just.",
      'title': 'How to Score Big Land Flipping Deals Using Direct Mail (Apke Brothers)',
      'url': 'https://www.youtube.com/watch?v=JRIbKp3FaEs&t=419s',
      'video_id': 'JRIbKp3FaEs'},
     {'author': 'Great Lands LLC',
      'channel': 'Great Lands LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:21](https://www.youtube.com/watch?v=Mdkx15sX_XM&t=861s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Search the Hat area um in this um in this Zone and see what the you know uh '
              'what have been sold recently and what is being what what has been sold recently '
              'and what is hard really in this area so if I go to estimated.',
      'timestamp': 861,
      'timestamp_label': '[00:14:21]',
      'timestamp_seconds': 861,
      'tip': 'Search the Hat area um in this um in this Zone and see what the you know uh what '
             'have been sold recently and what is being what what has been sold recently and '
             'what is hard really in this area so if I go to estimated.',
      'title': 'Propstream for Land Investors (Great Lands LLC)',
      'url': 'https://www.youtube.com/watch?v=Mdkx15sX_XM&t=861s',
      'video_id': 'Mdkx15sX_XM'},
     {'author': 'Seller Finance Consultants, Inc.',
      'channel': 'Seller Finance Consultants, Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:57:50](https://www.youtube.com/watch?v=gSHz85xxIz4&t=3470s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just it's because they um they want to know all this stuff and I think they "
              "even want the IRS to know who you know who's getting interest income and and "
              "that's a way of tracking.",
      'timestamp': 3470,
      'timestamp_label': '[00:57:50]',
      'timestamp_seconds': 3470,
      'tip': "Just it's because they um they want to know all this stuff and I think they even "
             "want the IRS to know who you know who's getting interest income and and that's a "
             'way of tracking.',
      'title': 'RehabValuator.com and Daniil Kleyman: Seller Financing, Dodd-Frank, and '
               'Profitability in 2014 (Seller Finance Consultants, Inc.)',
      'url': 'https://www.youtube.com/watch?v=gSHz85xxIz4&t=3470s',
      'video_id': 'gSHz85xxIz4'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:15](https://www.youtube.com/watch?v=iC5tSNnegIw&t=1155s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're talking CRM, your website, your phone, texting, calendars, email, all the "
              'automations you could ever need, and even a ton of helpful AI tools. And the '
              "best part is it's all in one place.",
      'timestamp': 1155,
      'timestamp_label': '[00:19:15]',
      'timestamp_seconds': 1155,
      'tip': "We're talking CRM, your website, your phone, texting, calendars, email, all the "
             'automations you could ever need, and even a ton of helpful AI tools. And the '
             "best part is it's all in one place.",
      'title': 'The Best Advice I Never Got About Land Investing (REtipster)',
      'url': 'https://www.youtube.com/watch?v=iC5tSNnegIw&t=1155s',
      'video_id': 'iC5tSNnegIw'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:16](https://www.youtube.com/watch?v=HpkNhY7WclQ&t=1036s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, two conversations over the 4-year period. Now, we talk to them like every '
              'single month. Like we literally have like our CRM that reminds us, "All right, '
              'you got to call this person." Unless obviously sometimes people like "Stop '
              'calling me every month.".',
      'timestamp': 1036,
      'timestamp_label': '[00:17:16]',
      'timestamp_seconds': 1036,
      'tip': 'So, two conversations over the 4-year period. Now, we talk to them like every '
             'single month. Like we literally have like our CRM that reminds us, "All right, '
             'you got to call this person." Unless obviously sometimes people like "Stop '
             'calling me every month.".',
      'title': 'Land Flipping: Why Your Buyers Are the Real Asset w/ Abi Asija | REtipster '
               'Podcast 290 (REtipster)',
      'url': 'https://www.youtube.com/watch?v=HpkNhY7WclQ&t=1036s',
      'video_id': 'HpkNhY7WclQ'}],
 9: [{'author': 'Clay Hepler',
      'channel': 'Clay Hepler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=IRJeZQijnxU&t=264s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What I'm sharing is what's working in our business. You need to get your own "
              "legal counsel. Here's a real thing no one talks about. You can't be a onetrick "
              "pony in this business. If you only do cash flips, you'll be limited by your "
              'capital or your funer capital.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': "What I'm sharing is what's working in our business. You need to get your own "
             "legal counsel. Here's a real thing no one talks about. You can't be a onetrick "
             "pony in this business. If you only do cash flips, you'll be limited by your "
             'capital or your funer capital.',
      'title': 'Double Closing for Land Investors 2026 | Ultimate Guide for Beginners (Even in '
               'Restricted States) (Clay Hepler)',
      'url': 'https://www.youtube.com/watch?v=IRJeZQijnxU&t=264s',
      'video_id': 'IRJeZQijnxU'},
     {'author': 'Land Academy',
      'channel': 'Land Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:31](https://www.youtube.com/watch?v=fTJxXxQQQGs&t=391s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to see let the market work itself out. I'm going to let 5% of these "
              'deals close and I\'m going to cash the check." So now I\'ve got a contract and '
              "not open estro. I just have a contract that I'm staring at that says I'm going "
              'to buy this property for 20 grand.',
      'timestamp': 391,
      'timestamp_label': '[00:06:31]',
      'timestamp_seconds': 391,
      'tip': "I'm going to see let the market work itself out. I'm going to let 5% of these "
             'deals close and I\'m going to cash the check." So now I\'ve got a contract and '
             "not open estro. I just have a contract that I'm staring at that says I'm going "
             'to buy this property for 20 grand.',
      'title': 'Why Double Closing May Be Dead In 2025 | Real Estate Strategies That Still '
               'Work (Land Academy)',
      'url': 'https://www.youtube.com/watch?v=fTJxXxQQQGs&t=391s',
      'video_id': 'fTJxXxQQQGs'},
     {'author': 'William Bronchick',
      'channel': 'William Bronchick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=MNznbFmtOwI&t=255s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dodd-Frank um Dodd-Frank basically deals with the mechanics for owner financing '
              'transactions. So, it deals with how you can do and what you can do and what '
              'terms you can offer and how you take buyers and so forth. It is a federal law '
              "which means it's the same in every state.",
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'Dodd-Frank um Dodd-Frank basically deals with the mechanics for owner financing '
             'transactions. So, it deals with how you can do and what you can do and what '
             'terms you can offer and how you take buyers and so forth. It is a federal law '
             "which means it's the same in every state.",
      'title': 'Seller Financing after Dodd-Frank (William Bronchick)',
      'url': 'https://www.youtube.com/watch?v=MNznbFmtOwI&t=255s',
      'video_id': 'MNznbFmtOwI'},
     {'author': 'Jack Bosch',
      'channel': 'Jack Bosch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:40](https://www.youtube.com/watch?v=JXUkA5K7RSc&t=400s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '445 acre ones have road access on the bottom, the 20 acre says road X is on the '
              'top, you have fulfilled their criteria and now if you look at their legal '
              'description, you can work with a data company, they can help you rewrite those '
              'legal descriptions.',
      'timestamp': 400,
      'timestamp_label': '[00:06:40]',
      'timestamp_seconds': 400,
      'tip': '445 acre ones have road access on the bottom, the 20 acre says road X is on the '
             'top, you have fulfilled their criteria and now if you look at their legal '
             'description, you can work with a data company, they can help you rewrite those '
             'legal descriptions.',
      'title': 'How To Subdivide Land For Profit (Step By Step) (Jack Bosch)',
      'url': 'https://www.youtube.com/watch?v=JXUkA5K7RSc&t=400s',
      'video_id': 'JXUkA5K7RSc'},
     {'author': 'BiggerPockets',
      'channel': 'BiggerPockets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=y_3SP6N-l4c&t=72s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just make sure to check out your local jurisdiction's rules and laws. Every "
              'state and city is different. Subdivision is rather simple. It involves taking '
              'one tract or piece of land and dividing it into two or more tracts of land.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "Just make sure to check out your local jurisdiction's rules and laws. Every "
             'state and city is different. Subdivision is rather simple. It involves taking '
             'one tract or piece of land and dividing it into two or more tracts of land.',
      'title': 'Subdividing Land: What Real Estate Investors Should Know | Daily Podcast 183 '
               '(BiggerPockets)',
      'url': 'https://www.youtube.com/watch?v=y_3SP6N-l4c&t=72s',
      'video_id': 'y_3SP6N-l4c'},
     {'author': 'Groundwork',
      'channel': 'Groundwork',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:53](https://www.youtube.com/watch?v=dSAQlt9llvM&t=413s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make the purchase contingent on a passing soil evaluation with enough time for '
              'wet weather testing if your county requires it. Ask your attorney or agent how '
              'to word it because contingency rules vary by state and I am an engineer, not a '
              'lawyer.',
      'timestamp': 413,
      'timestamp_label': '[00:06:53]',
      'timestamp_seconds': 413,
      'tip': 'Make the purchase contingent on a passing soil evaluation with enough time for '
             'wet weather testing if your county requires it. Ask your attorney or agent how '
             'to word it because contingency rules vary by state and I am an engineer, not a '
             'lawyer.',
      'title': "Don't Buy Land Until It Passes This Test (Perc Test Explained)! (Groundwork)",
      'url': 'https://www.youtube.com/watch?v=dSAQlt9llvM&t=413s',
      'video_id': 'dSAQlt9llvM'},
     {'author': 'Law Case Summaries',
      'channel': 'Law Case Summaries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=wij1Dm2XEX8&t=66s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The court held that a way of necessity is implied by law as an incident to a '
              'grant. Common sense dictates that if a grantee has no legal right of access '
              "except over the grantor's land, a way of necessity must be implied to prevent "
              'the land from being useless.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'The court held that a way of necessity is implied by law as an incident to a '
             'grant. Common sense dictates that if a grantee has no legal right of access '
             "except over the grantor's land, a way of necessity must be implied to prevent "
             'the land from being useless.',
      'title': 'Barry v Hasseldine: Strict Easement of Necessity (Landlocked Land) [1952] Ch '
               '835 (Law Case Summaries)',
      'url': 'https://www.youtube.com/watch?v=wij1Dm2XEX8&t=66s',
      'video_id': 'wij1Dm2XEX8'},
     {'author': 'American Fault Lines',
      'channel': 'American Fault Lines',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:58](https://www.youtube.com/watch?v=BQMMvL0zywU&t=1198s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'There is no legal recourse, no lease agreement, and no refund. That leaves the '
              'most desperate option, which you can see lining the industrial access roads and '
              'frontage streets outside cities like Phoenix, Las Vegas, and Portland.',
      'timestamp': 1198,
      'timestamp_label': '[00:19:58]',
      'timestamp_seconds': 1198,
      'tip': 'There is no legal recourse, no lease agreement, and no refund. That leaves the '
             'most desperate option, which you can see lining the industrial access roads and '
             'frontage streets outside cities like Phoenix, Las Vegas, and Portland.',
      'title': 'America’s RV Parks Are Becoming Too Expensive — Full Time Residents Have '
               'Nowhere Left to Go (American Fault Lines)',
      'url': 'https://www.youtube.com/watch?v=BQMMvL0zywU&t=1198s',
      'video_id': 'BQMMvL0zywU'},
     {'author': 'Liberty Acres',
      'channel': 'Liberty Acres',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=Mio31c7ePlc&t=72s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then have a soil scientist or engineer say which systems could fit. Ask the '
              'utility about public sewer, and get a written estimate for the system and its '
              'upkeep. State rules differ, so check your own.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Then have a soil scientist or engineer say which systems could fit. Ask the '
             'utility about public sewer, and get a written estimate for the system and its '
             'upkeep. State rules differ, so check your own.',
      'title': 'Failed Perc Test? What It Means and Your Septic Options (Liberty Acres)',
      'url': 'https://www.youtube.com/watch?v=Mio31c7ePlc&t=72s',
      'video_id': 'Mio31c7ePlc'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=5p6zCt25Tyw&t=21s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Not have access to his property he got a property a purchase agreement back he '
              'got a property under contract the first thing you need to do is make sure '
              "you're.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Not have access to his property he got a property a purchase agreement back he '
             'got a property under contract the first thing you need to do is make sure '
             "you're.",
      'title': 'Landlocked Properties & What To Do With A Property With No Access (Apke '
               'Brothers)',
      'url': 'https://www.youtube.com/watch?v=5p6zCt25Tyw&t=21s',
      'video_id': '5p6zCt25Tyw'},
     {'author': 'Legal Counsel P.A.',
      'channel': 'Legal Counsel P.A.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=4mnTabZRS60&t=85s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Securing legal access to their property each situation is unique and the the '
              'appropriate solution will depend on specific circumstances and legal '
              'considerations if you have any questions about landlock property call legal '
              'council PA have questions we have answers.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Securing legal access to their property each situation is unique and the the '
             'appropriate solution will depend on specific circumstances and legal '
             'considerations if you have any questions about landlock property call legal '
             'council PA have questions we have answers.',
      'title': 'Is Your Florida Property Landlocked? Here’s What You Can Do (Legal Counsel '
               'P.A.)',
      'url': 'https://www.youtube.com/watch?v=4mnTabZRS60&t=85s',
      'video_id': '4mnTabZRS60'},
     {'author': 'Ryan Dossey',
      'channel': 'Ryan Dossey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:45](https://www.youtube.com/watch?v=hzDGK6PCjPg&t=285s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Violated right so if I want to make this even more like legit looking I would '
              "just throw these in now typically on something like this you're going to need "
              "the person's uh company name city state and zip that's really easy to find you "
              'just go to opencorporates.',
      'timestamp': 285,
      'timestamp_label': '[00:04:45]',
      'timestamp_seconds': 285,
      'tip': 'Violated right so if I want to make this even more like legit looking I would '
             "just throw these in now typically on something like this you're going to need "
             "the person's uh company name city state and zip that's really easy to find you "
             'just go to opencorporates.',
      'title': 'Getting Sued For Texting AND Cold Calling 😨 (Ryan Dossey)',
      'url': 'https://www.youtube.com/watch?v=hzDGK6PCjPg&t=285s',
      'video_id': 'hzDGK6PCjPg'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:18](https://www.youtube.com/watch?v=m1GoTr9J5TM&t=1638s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re gonna advertise certain terms in your listing, saying that seller financing "
              "is available and this is exactly what you can get, then you'd better actually "
              "use that when you get to closing, and don't change it up and do something "
              'different.',
      'timestamp': 1638,
      'timestamp_label': '[00:27:18]',
      'timestamp_seconds': 1638,
      'tip': "'re gonna advertise certain terms in your listing, saying that seller financing "
             "is available and this is exactly what you can get, then you'd better actually "
             "use that when you get to closing, and don't change it up and do something "
             'different.',
      'title': 'What the Dodd-Frank Act Means for Vacant Land & Seller Financing (REtipster)',
      'url': 'https://www.youtube.com/watch?v=m1GoTr9J5TM&t=1638s',
      'video_id': 'm1GoTr9J5TM'},
     {'author': 'Apke Brothers',
      'channel': 'Apke Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=tZnXE47jWp4&t=50s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Which is great so let's just choose a state here so state we're just going to "
              "do colorado and we'll do boulder county colorado okay so we have the area right "
              'now.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': "Which is great so let's just choose a state here so state we're just going to do "
             "colorado and we'll do boulder county colorado okay so we have the area right "
             'now.',
      'title': 'Is Data Tree the Best Data Tool for Land Investing? (Review & Tutorial) (Apke '
               'Brothers)',
      'url': 'https://www.youtube.com/watch?v=tZnXE47jWp4&t=50s',
      'video_id': 'tZnXE47jWp4'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=TzjxQStPaW4&t=248s)',
      'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                   'parcel underwriting, minor subdivisions, and title-insured dispositions '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Texas because it is a Texas state law. And so what does all of that mean? Well, '
              'an exempt subdivide allows you to bypass all approving authorities.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'Texas because it is a Texas state law. And so what does all of that mean? Well, '
             'an exempt subdivide allows you to bypass all approving authorities.',
      'title': 'The Essential Types of Land Subdivisions (Part 1 of 4) | The Real Deal w/ Neil '
               'Clements (REtipster)',
      'url': 'https://www.youtube.com/watch?v=TzjxQStPaW4&t=248s',
      'video_id': 'TzjxQStPaW4'}],
 10: [{'author': 'Apke Brothers',
       'channel': 'Apke Brothers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:09](https://www.youtube.com/watch?v=cFfiZJm0txo&t=309s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But I talked to so many people in the land space to where I see pretty much '
               'all of the strategies that we talk about work. Like even the paid ads, '
               'whatever, PPC, that type of stuff. I I know some people running their business '
               'off of uh cold calling, texting, mail.',
       'timestamp': 309,
       'timestamp_label': '[00:05:09]',
       'timestamp_seconds': 309,
       'tip': 'But I talked to so many people in the land space to where I see pretty much all '
              'of the strategies that we talk about work. Like even the paid ads, whatever, '
              'PPC, that type of stuff. I I know some people running their business off of uh '
              'cold calling, texting, mail.',
       'title': 'How to Get More Land Deals With Direct Mail (Apke Brothers)',
       'url': 'https://www.youtube.com/watch?v=cFfiZJm0txo&t=309s',
       'video_id': 'cFfiZJm0txo'},
      {'author': 'Brent Bowers',
       'channel': 'Brent Bowers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:44](https://www.youtube.com/watch?v=JNufnuENoDM&t=524s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But I want to give you one more pro tip on how to find a realtor a real estate '
               "professional licensed real estate agent that deals in land and that's by going "
               "to landwatch. 's just say we're going to keep using that El Paso County "
               'Colorado example.',
       'timestamp': 524,
       'timestamp_label': '[00:08:44]',
       'timestamp_seconds': 524,
       'tip': 'But I want to give you one more pro tip on how to find a realtor a real estate '
              "professional licensed real estate agent that deals in land and that's by going "
              "to landwatch. 's just say we're going to keep using that El Paso County "
              'Colorado example.',
       'title': 'How To Find Comps For Land (Brent Bowers)',
       'url': 'https://www.youtube.com/watch?v=JNufnuENoDM&t=524s',
       'video_id': 'JNufnuENoDM'},
      {'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:00](https://www.youtube.com/watch?v=oJpqcR4iFy8&t=300s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Tree user you can actually get discounted access to data tree if you sign up '
               "to the re tips your affiliate link I'll have that beneath this video if you "
               "want to check it out hope this was helpful thanks for watching I'll talk to "
               'you next time.',
       'timestamp': 300,
       'timestamp_label': '[00:05:00]',
       'timestamp_seconds': 300,
       'tip': 'Tree user you can actually get discounted access to data tree if you sign up to '
              "the re tips your affiliate link I'll have that beneath this video if you want "
              "to check it out hope this was helpful thanks for watching I'll talk to you next "
              'time.',
       'title': 'How to Build a Hand-Picked List of Properties by “Parcel Tagging” on DataTree '
                '(REtipster)',
       'url': 'https://www.youtube.com/watch?v=oJpqcR4iFy8&t=300s',
       'video_id': 'oJpqcR4iFy8'},
      {'author': 'Land Insights',
       'channel': 'Land Insights',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:45](https://www.youtube.com/watch?v=Tj5JsRK_YdQ&t=1665s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It just made a guess for us here. Uh like I called out and claude. It's all "
               "priced out like it's ready to go. You can send this uh data set to Rocket "
               'Print and then you just got to reference the right columns in your template.',
       'timestamp': 1665,
       'timestamp_label': '[00:27:45]',
       'timestamp_seconds': 1665,
       'tip': "It just made a guess for us here. Uh like I called out and claude. It's all "
              "priced out like it's ready to go. You can send this uh data set to Rocket Print "
              'and then you just got to reference the right columns in your template.',
       'title': 'The Land Flipping Direct Mail Strategy That Actually Works (Land Insights)',
       'url': 'https://www.youtube.com/watch?v=Tj5JsRK_YdQ&t=1665s',
       'video_id': 'Tj5JsRK_YdQ'},
      {'author': 'PlanningWebcastSeries',
       'channel': 'PlanningWebcastSeries',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:50](https://www.youtube.com/watch?v=A84PRdZGcoE&t=1010s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The the Inflation Reduction Act passed in 2000 late 2021 um I instituted new a '
               'production tax credits and um production tax credits and investment tax '
               'credits that are that for which batteries large scale batteries are eligible.',
       'timestamp': 1010,
       'timestamp_label': '[00:16:50]',
       'timestamp_seconds': 1010,
       'tip': 'The the Inflation Reduction Act passed in 2000 late 2021 um I instituted new a '
              'production tax credits and um production tax credits and investment tax credits '
              'that are that for which batteries large scale batteries are eligible.',
       'title': 'Planning and Zoning for Battery Energy Storage Systems (BESS) '
                '(PlanningWebcastSeries)',
       'url': 'https://www.youtube.com/watch?v=A84PRdZGcoE&t=1010s',
       'video_id': 'A84PRdZGcoE'},
      {'author': 'Flip With Rick',
       'channel': 'Flip With Rick',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:34](https://www.youtube.com/watch?v=U4t9j_wTBLk&t=634s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I was interested in selling my home, but he was a licensed real estate agent, '
               'so he was asking because of that." If you\'re not licensed, you\'re not '
               "calling someone because you want to go list their house cuz that's technically "
               'illegal.',
       'timestamp': 634,
       'timestamp_label': '[00:10:34]',
       'timestamp_seconds': 634,
       'tip': 'I was interested in selling my home, but he was a licensed real estate agent, '
              'so he was asking because of that." If you\'re not licensed, you\'re not calling '
              "someone because you want to go list their house cuz that's technically illegal.",
       'title': 'How to Legally Cold Call & Text the DNC LIST! (Flip With Rick)',
       'url': 'https://www.youtube.com/watch?v=U4t9j_wTBLk&t=634s',
       'video_id': 'U4t9j_wTBLk'},
      {'author': 'Flipping Mastery TV',
       'channel': 'Flipping Mastery TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:35](https://www.youtube.com/watch?v=YPqUHvSAZrU&t=1055s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You would consider and it's the standard everybody sees this script after that "
               'you say oh long pause you act disappointed.',
       'timestamp': 1055,
       'timestamp_label': '[00:17:35]',
       'timestamp_seconds': 1055,
       'tip': "You would consider and it's the standard everybody sees this script after that "
              'you say oh long pause you act disappointed.',
       'title': 'How To Make Offers To Land Owners - Masterclass Video 5 w/ Joe McCall '
                '(Flipping Mastery TV)',
       'url': 'https://www.youtube.com/watch?v=YPqUHvSAZrU&t=1055s',
       'video_id': 'YPqUHvSAZrU'},
      {'author': 'Apke Brothers',
       'channel': 'Apke Brothers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:29:44](https://www.youtube.com/watch?v=lWYFLEd7PA0&t=1784s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's how you want to sell. With cold calling, you need like tonality is so "
               'important. And obviously like you need a script at the same time. Some people '
               'try to go cold calling without a script.',
       'timestamp': 1784,
       'timestamp_label': '[00:29:44]',
       'timestamp_seconds': 1784,
       'tip': "That's how you want to sell. With cold calling, you need like tonality is so "
              'important. And obviously like you need a script at the same time. Some people '
              'try to go cold calling without a script.',
       'title': 'Cold Calling Q&A: How to Get Landowners to Say “Yes” (Apke Brothers)',
       'url': 'https://www.youtube.com/watch?v=lWYFLEd7PA0&t=1784s',
       'video_id': 'lWYFLEd7PA0'},
      {'author': 'Amber Shah of St. Augustine Realtor',
       'channel': 'Amber Shah of St. Augustine Realtor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:47](https://www.youtube.com/watch?v=O6tZ8o1scfY&t=227s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So so that was helpful and we shall continue. Look at these beautiful '
               "butterflies. They're way back there now. And then there's one right there. And "
               "that's all I have to say about that. So, if you have any other properties that "
               'you want to go check out in St.',
       'timestamp': 227,
       'timestamp_label': '[00:03:47]',
       'timestamp_seconds': 227,
       'tip': 'So so that was helpful and we shall continue. Look at these beautiful '
              "butterflies. They're way back there now. And then there's one right there. And "
              "that's all I have to say about that. So, if you have any other properties that "
              'you want to go check out in St.',
       'title': '🎥 Landlocked Land in Florida?! What I Learned While Hunting for Access, '
                'Easements & Closest Neighbor (Amber Shah of St. Augustine Realtor)',
       'url': 'https://www.youtube.com/watch?v=O6tZ8o1scfY&t=227s',
       'video_id': 'O6tZ8o1scfY'},
      {'author': 'Land Investing Pros',
       'channel': 'Land Investing Pros',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:37](https://www.youtube.com/watch?v=ipLt_cz8tEY&t=157s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Real um pretty much when you acquire your first lot in the land investing '
               "business that's when you realize this is actually.",
       'timestamp': 157,
       'timestamp_label': '[00:02:37]',
       'timestamp_seconds': 157,
       'tip': 'Real um pretty much when you acquire your first lot in the land investing '
              "business that's when you realize this is actually.",
       'title': 'Which Marketing Strategy is better: Blind Offers or Neutral Letters? (Land '
                'Investing Pros)',
       'url': 'https://www.youtube.com/watch?v=ipLt_cz8tEY&t=157s',
       'video_id': 'ipLt_cz8tEY'},
      {'author': 'Land Flipping 101',
       'channel': 'Land Flipping 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=gwLVELHJjbc&t=190s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So if you have a parcel of land that you wouldn't have access to without "
               'crossing an adjoining piece of land then any road easement would likely be in '
               'a pertinent.',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': "So if you have a parcel of land that you wouldn't have access to without "
              'crossing an adjoining piece of land then any road easement would likely be in a '
              'pertinent.',
       'title': 'Landlocked Properties and Easements (Land Flipping 101)',
       'url': 'https://www.youtube.com/watch?v=gwLVELHJjbc&t=190s',
       'video_id': 'gwLVELHJjbc'},
      {'author': 'Debt Free Doctor - Dr. Jeff Anzalone',
       'channel': 'Debt Free Doctor - Dr. Jeff Anzalone',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:52](https://www.youtube.com/watch?v=5o06VeN0Gak&t=412s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'People that that are looking to either invest on their own or with us cuz we '
               'want people informed as much as possible because man once you once you wire '
               "that money and sign that check it's all on you so hopefully this helps and uh "
               "we'll see you in the next video.",
       'timestamp': 412,
       'timestamp_label': '[00:06:52]',
       'timestamp_seconds': 412,
       'tip': 'People that that are looking to either invest on their own or with us cuz we '
              'want people informed as much as possible because man once you once you wire '
              "that money and sign that check it's all on you so hopefully this helps and uh "
              "we'll see you in the next video.",
       'title': 'RV Park Investing: How to Buy Your First Park with No Experience (Debt Free '
                'Doctor - Dr. Jeff Anzalone)',
       'url': 'https://www.youtube.com/watch?v=5o06VeN0Gak&t=412s',
       'video_id': '5o06VeN0Gak'},
      {'author': 'Matt Wood',
       'channel': 'Matt Wood',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:18](https://www.youtube.com/watch?v=ZU1aoe6pwQI&t=378s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A really bright Sun today I've got three batteries fully charged my remotes "
               'fully charged my memory card is cleaned out my settings are good to go so now '
               "I'm ready to fly.",
       'timestamp': 378,
       'timestamp_label': '[00:06:18]',
       'timestamp_seconds': 378,
       'tip': "A really bright Sun today I've got three batteries fully charged my remotes "
              'fully charged my memory card is cleaned out my settings are good to go so now '
              "I'm ready to fly.",
       'title': 'HOW TO SHOOT Acreage With a Drone - 5 TIPS l Drone VLOGs #4 (Matt Wood)',
       'url': 'https://www.youtube.com/watch?v=ZU1aoe6pwQI&t=378s',
       'video_id': 'ZU1aoe6pwQI'},
      {'author': 'The Jen Holden Group of Compass',
       'channel': 'The Jen Holden Group of Compass',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:06](https://www.youtube.com/watch?v=3ppoErpmGfs&t=486s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Survey done before you do anything else and it's gonna help you with a lot of "
               'the other decisions that you need to meet yep thank you very much Thanks.',
       'timestamp': 486,
       'timestamp_label': '[00:08:06]',
       'timestamp_seconds': 486,
       'tip': "Survey done before you do anything else and it's gonna help you with a lot of "
              'the other decisions that you need to meet yep thank you very much Thanks.',
       'title': 'Perc testing, flood plains, slope, septic - oh my! Bill Bower explains it all '
                'to us! (The Jen Holden Group of Compass)',
       'url': 'https://www.youtube.com/watch?v=3ppoErpmGfs&t=486s',
       'video_id': '3ppoErpmGfs'},
      {'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:34](https://www.youtube.com/watch?v=rYCHQ59jzhY&t=154s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So I'm going to stick with that. And if I was working in a market where there "
               "just weren't that many comps based on the sold price, I could go with the four "
               'sale listings and just subtle with that. I would just want to be aware that '
               'these are not actual sold prices.',
       'timestamp': 154,
       'timestamp_label': '[00:02:34]',
       'timestamp_seconds': 154,
       'tip': "So I'm going to stick with that. And if I was working in a market where there "
              "just weren't that many comps based on the sold price, I could go with the four "
              'sale listings and just subtle with that. I would just want to be aware that '
              'these are not actual sold prices.',
       'title': 'How to Use Redfin and LandWatch to Determine Land Values (REtipster)',
       'url': 'https://www.youtube.com/watch?v=rYCHQ59jzhY&t=154s',
       'video_id': 'rYCHQ59jzhY'}],
 11: [{'author': 'Land Investing Pros',
       'channel': 'Land Investing Pros',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:16](https://www.youtube.com/watch?v=gMTr4Kngzx8&t=496s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I work with and the owners. Uh they're if they're ready to go that allows me "
               "to be faster at closing the deals and that's the whole point. Um this is to be "
               'able to just get the acquisition done, right?',
       'timestamp': 496,
       'timestamp_label': '[00:08:16]',
       'timestamp_seconds': 496,
       'tip': "I work with and the owners. Uh they're if they're ready to go that allows me to "
              "be faster at closing the deals and that's the whole point. Um this is to be "
              'able to just get the acquisition done, right?',
       'title': 'Land Flipping Formula: Neutral Offers VS Blind Offers (Land Investing Pros)',
       'url': 'https://www.youtube.com/watch?v=gMTr4Kngzx8&t=496s',
       'video_id': 'gMTr4Kngzx8'},
      {'author': 'DataTree by First American',
       'channel': 'DataTree by First American',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=EmWzMGDpkTY&t=34s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Data is derived from properties and parcels County Assessors determine the '
               'value of each property based on the valuation and.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': 'Data is derived from properties and parcels County Assessors determine the '
              'value of each property based on the valuation and.',
       'title': 'Public Records Property Data: Data 101 Series | DataTree by First American '
                '(DataTree by First American)',
       'url': 'https://www.youtube.com/watch?v=EmWzMGDpkTY&t=34s',
       'video_id': 'EmWzMGDpkTY'},
      {'author': 'ACRE Partner',
       'channel': 'ACRE Partner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=LlahXSpP0k4&t=91s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Step two is you have to build the right team. You have to build a a team '
               "that's going to allow you to get there. The hard truth is most solarpreneurs, "
               "they don't want to scale up. They don't want to actually spend their money on "
               'building out their business.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': "Step two is you have to build the right team. You have to build a a team that's "
              'going to allow you to get there. The hard truth is most solarpreneurs, they '
              "don't want to scale up. They don't want to actually spend their money on "
              'building out their business.',
       'title': 'How I Scaled My Real Estate Media Business to $7M (Step by Step) (ACRE '
                'Partner)',
       'url': 'https://www.youtube.com/watch?v=LlahXSpP0k4&t=91s',
       'video_id': 'LlahXSpP0k4'},
      {'author': 'Apke Brothers',
       'channel': 'Apke Brothers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:27](https://www.youtube.com/watch?v=Ls2lelB6ImM&t=267s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Interviewing the kado taco he owns 50 Plus locations he's scaling it to 100 um "
               "and it's incredible because that's a hard business to scale so learning from.",
       'timestamp': 267,
       'timestamp_label': '[00:04:27]',
       'timestamp_seconds': 267,
       'tip': "Interviewing the kado taco he owns 50 Plus locations he's scaling it to 100 um "
              "and it's incredible because that's a hard business to scale so learning from.",
       'title': '$100K Blueprint: Flipping Land with Texts in 2025 (Apke Brothers)',
       'url': 'https://www.youtube.com/watch?v=Ls2lelB6ImM&t=267s',
       'video_id': 'Ls2lelB6ImM'},
      {'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=Uaqe67xWZN0&t=20s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, he's talked pretty openly about going into tens of thousands of dollars of "
               'debt to get started and he sends huge volumes of direct mail and text messages '
               "and he's built a team around the business.",
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "So, he's talked pretty openly about going into tens of thousands of dollars of "
              'debt to get started and he sends huge volumes of direct mail and text messages '
              "and he's built a team around the business.",
       'title': 'The Land Strategy That Replaced His W-2 w/ Landon Bleau | REtipster Podcast '
                '291 (REtipster)',
       'url': 'https://www.youtube.com/watch?v=Uaqe67xWZN0&t=20s',
       'video_id': 'Uaqe67xWZN0'},
      {'author': 'Land Profit Generator with Jack & Michelle Bosch',
       'channel': 'Land Profit Generator with Jack & Michelle Bosch',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=tfERI-RnheU&t=15s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Here on looking at on iTunes or any of the other of Android podcast platforms '
               'then welcome my name is Jack Bosch and welcome to the forever cash live '
               'podcast.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Here on looking at on iTunes or any of the other of Android podcast platforms '
              'then welcome my name is Jack Bosch and welcome to the forever cash live '
              'podcast.',
       'title': 'FCP 058: LANDLOCKED REAL ESTATE - HOW TO TURN A PROBLEM PROPERTY INTO PURE '
                'PROFIT (Land Profit Generator with Jack & Michelle Bosch)',
       'url': 'https://www.youtube.com/watch?v=tfERI-RnheU&t=15s',
       'video_id': 'tfERI-RnheU'},
      {'author': 'Sumner Healey',
       'channel': 'Sumner Healey',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=R4icAmTE4WI&t=15s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'With you the truth about blind offers and frankly the information in this '
               'video has the real potential to flip your business from not doing great to.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'With you the truth about blind offers and frankly the information in this video '
              'has the real potential to flip your business from not doing great to.',
       'title': 'Vacant Land Blind Offers: Insider Truths & Tips | Land Investing Tips | '
                'Sumner Healey 2025 (Sumner Healey)',
       'url': 'https://www.youtube.com/watch?v=R4icAmTE4WI&t=15s',
       'video_id': 'R4icAmTE4WI'},
      {'author': 'Land Academy',
       'channel': 'Land Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:12](https://www.youtube.com/watch?v=abgGG4YJgLw&t=132s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Get a check when Safa stand in line mail the check it's not worth the time of "
               'the business owner my two cents dot dot dot.',
       'timestamp': 132,
       'timestamp_label': '[00:02:12]',
       'timestamp_seconds': 132,
       'tip': "Get a check when Safa stand in line mail the check it's not worth the time of "
              'the business owner my two cents dot dot dot.',
       'title': 'Land Investors Review by Seth Williams of ReTipster (CFFL 424) (Land Academy)',
       'url': 'https://www.youtube.com/watch?v=abgGG4YJgLw&t=132s',
       'video_id': 'abgGG4YJgLw'},
      {'author': 'NBC 10 WJAR',
       'channel': 'NBC 10 WJAR',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:39](https://www.youtube.com/watch?v=gnZroureXsw&t=219s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We reached out to Holliston for a comment but never received a reply I'm nbc10 "
               "it team reporter Parker gavigan nbc10 news and Parker I know you'll stay on "
               'this story if you have a tip for Parker and the nbc10 IT team call 41455 9123 '
               'or send an email to itam at WJ com.',
       'timestamp': 219,
       'timestamp_label': '[00:03:39]',
       'timestamp_seconds': 219,
       'tip': "We reached out to Holliston for a comment but never received a reply I'm nbc10 "
              "it team reporter Parker gavigan nbc10 news and Parker I know you'll stay on "
              'this story if you have a tip for Parker and the nbc10 IT team call 41455 9123 '
              'or send an email to itam at WJ com.',
       'title': 'I-Team: Landlocked property owners want access (NBC 10 WJAR)',
       'url': 'https://www.youtube.com/watch?v=gnZroureXsw&t=219s',
       'video_id': 'gnZroureXsw'},
      {'author': 'Tyler Bobo Investor, Alaska Realtor',
       'channel': 'Tyler Bobo Investor, Alaska Realtor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:19](https://www.youtube.com/watch?v=zzxrwQSJnC4&t=139s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Want to live next to a dog team you'd buy in a neighborhood that doesn't allow "
               "that if you don't want to live in an area with a bunch of horses you can buy.",
       'timestamp': 139,
       'timestamp_label': '[00:02:19]',
       'timestamp_seconds': 139,
       'tip': "Want to live next to a dog team you'd buy in a neighborhood that doesn't allow "
              "that if you don't want to live in an area with a bunch of horses you can buy.",
       'title': 'Home Owners Association (HOA) or Covenants Condition and Restrictions (CC&R) '
                '(Tyler Bobo Investor, Alaska Realtor)',
       'url': 'https://www.youtube.com/watch?v=zzxrwQSJnC4&t=139s',
       'video_id': 'zzxrwQSJnC4'},
      {'author': 'VestRight',
       'channel': 'VestRight',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:11](https://www.youtube.com/watch?v=V0GF_nQKkTU&t=671s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Learn more there's all types of content you can set up a call with my team and "
               'we can explore if this is the right fit for you thanks so much for watching '
               "and we'll talk to you soon.",
       'timestamp': 671,
       'timestamp_label': '[00:11:11]',
       'timestamp_seconds': 671,
       'tip': "Learn more there's all types of content you can set up a call with my team and "
              'we can explore if this is the right fit for you thanks so much for watching and '
              "we'll talk to you soon.",
       'title': 'Land Acquisition 101 - 5 Things You Must Know | VestRight (VestRight)',
       'url': 'https://www.youtube.com/watch?v=V0GF_nQKkTU&t=671s',
       'video_id': 'V0GF_nQKkTU'},
      {'author': 'PRYCD',
       'channel': 'PRYCD',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=mhHvzO1O8To&t=15s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Basis of those property owners that own a property within a certain County but '
               "don't actually live in the county itself and so to get this value what we're.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Basis of those property owners that own a property within a certain County but '
              "don't actually live in the county itself and so to get this value what we're.",
       'title': 'PRYCD Out of County Owner to Total Parcel Ratio Map Example (PRYCD)',
       'url': 'https://www.youtube.com/watch?v=mhHvzO1O8To&t=15s',
       'video_id': 'mhHvzO1O8To'},
      {'author': '6 Figure Revenue',
       'channel': '6 Figure Revenue',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:30](https://www.youtube.com/watch?v=HbQpeDGaA_c&t=450s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Photos so probably 75 people use our drones to get their listings out in a '
               "better way just because it's a different perspective if they want to show how "
               'big the backyard is or the house or the property they can do that and it makes '
               'it easier.',
       'timestamp': 450,
       'timestamp_label': '[00:07:30]',
       'timestamp_seconds': 450,
       'tip': 'Photos so probably 75 people use our drones to get their listings out in a '
              "better way just because it's a different perspective if they want to show how "
              'big the backyard is or the house or the property they can do that and it makes '
              'it easier.',
       'title': 'How To Start $3,000/Week Real Estate Drone Photography Business (6 Figure '
                'Revenue)',
       'url': 'https://www.youtube.com/watch?v=HbQpeDGaA_c&t=450s',
       'video_id': 'HbQpeDGaA_c'},
      {'author': 'Elegment Land',
       'channel': 'Elegment Land',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:45](https://www.youtube.com/watch?v=JkPCf6kuMu0&t=465s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Part of the community fostering a sense of belonging and connection with '
               'like-minded individuals who enjoy the same vacations that you do with '
               'ownership you have the ultimate control and freedom to make the most of your '
               'RV lifestyle and create lasting memory.',
       'timestamp': 465,
       'timestamp_label': '[00:07:45]',
       'timestamp_seconds': 465,
       'tip': 'Part of the community fostering a sense of belonging and connection with '
              'like-minded individuals who enjoy the same vacations that you do with ownership '
              'you have the ultimate control and freedom to make the most of your RV lifestyle '
              'and create lasting memory.',
       'title': 'RV Lot Renting vs. Buying:  The Pros and Cons of RV Lot Ownership (Elegment '
                'Land)',
       'url': 'https://www.youtube.com/watch?v=JkPCf6kuMu0&t=465s',
       'video_id': 'JkPCf6kuMu0'},
      {'author': 'Michael Bull',
       'channel': 'Michael Bull',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=PMSn1EaZ42Y&t=36s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "300 transactions and we've grown our business to multi-7 figures doing each of "
               'the three marketing channels. At one point, we had a marketing team for direct '
               'mail, a marketing team for cold calling, and a marketing team for texting.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': "300 transactions and we've grown our business to multi-7 figures doing each of "
              'the three marketing channels. At one point, we had a marketing team for direct '
              'mail, a marketing team for cold calling, and a marketing team for texting.',
       'title': 'Cold Calling vs Cold Texting vs Direct Mail: Which One Actually Works Best '
                'for Land Flipping? (Michael Bull)',
       'url': 'https://www.youtube.com/watch?v=PMSn1EaZ42Y&t=36s',
       'video_id': 'PMSn1EaZ42Y'}],
 12: [{'author': 'Maximilian Dier',
       'channel': 'Maximilian Dier',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:58](https://www.youtube.com/watch?v=uQ2jDRUrtoY&t=118s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, let me jump into it right now and start cold calling. Hopefully, we got '
               "the right contact. Hopefully, they have a piece of land. Hopefully, it's tax "
               'delinquent. And then hopefully they want to sell. So, the divers should be '
               'going, guys.',
       'timestamp': 118,
       'timestamp_label': '[00:01:58]',
       'timestamp_seconds': 118,
       'tip': 'So, let me jump into it right now and start cold calling. Hopefully, we got the '
              "right contact. Hopefully, they have a piece of land. Hopefully, it's tax "
              'delinquent. And then hopefully they want to sell. So, the divers should be '
              'going, guys.',
       'title': '🌳 Cold Calling Vacant Landowners Until I Get a DEAL (Maximilian Dier)',
       'url': 'https://www.youtube.com/watch?v=uQ2jDRUrtoY&t=118s',
       'video_id': 'uQ2jDRUrtoY'},
      {'author': 'REIPrintMail',
       'channel': 'REIPrintMail',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:32](https://www.youtube.com/watch?v=L4oZCP8R6RQ&t=992s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t have to worry about that kind of stuff with direct mail. But I think it's "
               'important I support we use in my own business. We do business-to-business '
               "calling. That brings up another topic, so let's talk about that. We in our "
               'business are business-to-business.',
       'timestamp': 992,
       'timestamp_label': '[00:16:32]',
       'timestamp_seconds': 992,
       'tip': "'t have to worry about that kind of stuff with direct mail. But I think it's "
              'important I support we use in my own business. We do business-to-business '
              "calling. That brings up another topic, so let's talk about that. We in our "
              'business are business-to-business.',
       'title': 'Real Estate Investors Beware! Texting and Cold calling rules from a TCPA '
                'LEGAL expert (REIPrintMail)',
       'url': 'https://www.youtube.com/watch?v=L4oZCP8R6RQ&t=992s',
       'video_id': 'L4oZCP8R6RQ'},
      {'author': 'DannyG Real Estate',
       'channel': 'DannyG Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:01](https://www.youtube.com/watch?v=UqPvFZ6TGGo&t=301s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And so it it just depends on what strategy you want to go towards. But that is '
               'how you pull comps. Say there was nothing within 30 days. I would want to just '
               'zoom out until I found something that I did. So 90 day 30 days is really '
               'tough.',
       'timestamp': 301,
       'timestamp_label': '[00:05:01]',
       'timestamp_seconds': 301,
       'tip': 'And so it it just depends on what strategy you want to go towards. But that is '
              'how you pull comps. Say there was nothing within 30 days. I would want to just '
              'zoom out until I found something that I did. So 90 day 30 days is really tough.',
       'title': 'How I Pull Comps on Zillow as Real Estate Investor (2025) (DannyG Real '
                'Estate)',
       'url': 'https://www.youtube.com/watch?v=UqPvFZ6TGGo&t=301s',
       'video_id': 'UqPvFZ6TGGo'},
      {'author': 'Sumner Advanced',
       'channel': 'Sumner Advanced',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=8pB5HoHJ4Bk&t=117s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So and it went contingent same day. So what do we Did we think it sold at 175 '
               "or not? Went contingent in one day. But this one I'm like, okay, I can vouch I "
               'think I can the data vouchers for 175. But if we find perhaps another example, '
               'now this one took 117 days.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'So and it went contingent same day. So what do we Did we think it sold at 175 '
              "or not? Went contingent in one day. But this one I'm like, okay, I can vouch I "
              'think I can the data vouchers for 175. But if we find perhaps another example, '
              'now this one took 117 days.',
       'title': "How I Price Land When Sold Prices Aren't Public (Sumner Advanced)",
       'url': 'https://www.youtube.com/watch?v=8pB5HoHJ4Bk&t=117s',
       'video_id': '8pB5HoHJ4Bk'},
      {'author': 'Clay Hepler',
       'channel': 'Clay Hepler',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:00](https://www.youtube.com/watch?v=o_c7zC-iYqE&t=360s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And that's where you come in. And even if you don't have these relationships "
               'yet, you can start small. You can use seller financing. You can partner with '
               "someone who has capital and split it 50/50. And you're not locked out because "
               "you don't have cash.",
       'timestamp': 360,
       'timestamp_label': '[00:06:00]',
       'timestamp_seconds': 360,
       'tip': "And that's where you come in. And even if you don't have these relationships "
              'yet, you can start small. You can use seller financing. You can partner with '
              "someone who has capital and split it 50/50. And you're not locked out because "
              "you don't have cash.",
       'title': 'Subdividing Land 101: How We Turned 80 Acres in Minnesota Into $235K in 10 '
                'Minutes (Clay Hepler)',
       'url': 'https://www.youtube.com/watch?v=o_c7zC-iYqE&t=360s',
       'video_id': 'o_c7zC-iYqE'},
      {'author': 'Maximilian Dier',
       'channel': 'Maximilian Dier',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:45](https://www.youtube.com/watch?v=xPy40xTlt64&t=885s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, guys, the list is loaded up. I'm just going to start calling. Uh Facebook "
               'guys are great. Uh what questions do you have on Facebook ads, fitness? Uh you '
               "shouldn't touch Facebook ads without at least a $3,000 a month budget. "
               'Preferably $5,000 a month is a sweet spot.',
       'timestamp': 885,
       'timestamp_label': '[00:14:45]',
       'timestamp_seconds': 885,
       'tip': "So, guys, the list is loaded up. I'm just going to start calling. Uh Facebook "
              'guys are great. Uh what questions do you have on Facebook ads, fitness? Uh you '
              "shouldn't touch Facebook ads without at least a $3,000 a month budget. "
              'Preferably $5,000 a month is a sweet spot.',
       'title': 'Cold Calling Code Violations LIVE (Watch Me Get a Wholesale Deal) (Maximilian '
                'Dier)',
       'url': 'https://www.youtube.com/watch?v=xPy40xTlt64&t=885s',
       'video_id': 'xPy40xTlt64'},
      {'author': 'Next Move with Rob',
       'channel': 'Next Move with Rob',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:58](https://www.youtube.com/watch?v=HrG-12X_ds8&t=718s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'END filter, I highly recommend that. Second, extra batteries and a charging '
               'hub because a big property may still need a second battery even with a '
               'one-flight plan.',
       'timestamp': 718,
       'timestamp_label': '[00:11:58]',
       'timestamp_seconds': 718,
       'tip': 'END filter, I highly recommend that. Second, extra batteries and a charging hub '
              'because a big property may still need a second battery even with a one-flight '
              'plan.',
       'title': 'How I Shoot Acreage Listings With the DJI Mavic 4 Pro - One Flight, Three '
                'Lenses (Next Move with Rob)',
       'url': 'https://www.youtube.com/watch?v=HrG-12X_ds8&t=718s',
       'video_id': 'HrG-12X_ds8'},
      {'author': 'HOA Insanity',
       'channel': 'HOA Insanity',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:14](https://www.youtube.com/watch?v=KuFkYy1kf7s&t=734s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Her face turned red and she started whispering furiously to Bramwell who could '
               'only shrug helplessly. We left the courthouse and I felt victorious. The next '
               'day, I signed the lease agreement with Breenidge Energy. The signing bonus hit '
               'my bank account within a week.',
       'timestamp': 734,
       'timestamp_label': '[00:12:14]',
       'timestamp_seconds': 734,
       'tip': 'Her face turned red and she started whispering furiously to Bramwell who could '
              'only shrug helplessly. We left the courthouse and I felt victorious. The next '
              'day, I signed the lease agreement with Breenidge Energy. The signing bonus hit '
              'my bank account within a week.',
       'title': 'HOA Claimed My Mineral Rights Were Theirs I Showed Up With the Original Deed '
                'and a Geologist! (HOA Insanity)',
       'url': 'https://www.youtube.com/watch?v=KuFkYy1kf7s&t=734s',
       'video_id': 'KuFkYy1kf7s'},
      {'author': 'RocketPrint and Mail',
       'channel': 'RocketPrint and Mail',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:54](https://www.youtube.com/watch?v=xY-aEaO4M98&t=114s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's easy to start to think, you know, is this going to work? But staying "
               'consistent and you know, 2,000 letters every single week again and again and '
               'again and again from different states, different counties and it does work.',
       'timestamp': 114,
       'timestamp_label': '[00:01:54]',
       'timestamp_seconds': 114,
       'tip': "It's easy to start to think, you know, is this going to work? But staying "
              'consistent and you know, 2,000 letters every single week again and again and '
              'again and again from different states, different counties and it does work.',
       'title': 'Enchanted Farms, Real Estate Land Investor Direct Mail Case Study (Rocket '
                'Print & Mail) (RocketPrint and Mail)',
       'url': 'https://www.youtube.com/watch?v=xY-aEaO4M98&t=114s',
       'video_id': 'xY-aEaO4M98'},
      {'author': 'RENVU Solar Equipment Distribution',
       'channel': 'RENVU Solar Equipment Distribution',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:43](https://www.youtube.com/watch?v=CLwCvBlXLA4&t=763s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The batteries anywhere from 25 to 30 years which is really is not realistic so '
               "although our cycle life is just 6 000 it's a more realistic and conservative "
               'approach with how you were going to use the battery at the end of the day.',
       'timestamp': 763,
       'timestamp_label': '[00:12:43]',
       'timestamp_seconds': 763,
       'tip': 'The batteries anywhere from 25 to 30 years which is really is not realistic so '
              "although our cycle life is just 6 000 it's a more realistic and conservative "
              'approach with how you were going to use the battery at the end of the day.',
       'title': 'Energy Storage System Sizing Webinar with Fortress Power | RENVU (RENVU Solar '
                'Equipment Distribution)',
       'url': 'https://www.youtube.com/watch?v=CLwCvBlXLA4&t=763s',
       'video_id': 'CLwCvBlXLA4'},
      {'author': 'Wyman Gentry',
       'channel': 'Wyman Gentry',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:12](https://www.youtube.com/watch?v=ItWPpkhNHto&t=252s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Imagine doing like three to four of these every day, including them in your '
               'photo packages. Just remember, you need your part 107 in order to charge '
               'clients to do this kind of work. And if you want to start making even more '
               'money, then you need to be doing real estate video.',
       'timestamp': 252,
       'timestamp_label': '[00:04:12]',
       'timestamp_seconds': 252,
       'tip': 'Imagine doing like three to four of these every day, including them in your '
              'photo packages. Just remember, you need your part 107 in order to charge '
              'clients to do this kind of work. And if you want to start making even more '
              'money, then you need to be doing real estate video.',
       'title': 'Top Drone Shots For Real Estate Photography (Wyman Gentry)',
       'url': 'https://www.youtube.com/watch?v=ItWPpkhNHto&t=252s',
       'video_id': 'ItWPpkhNHto'},
      {'author': 'Apke Brothers',
       'channel': 'Apke Brothers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:30:34](https://www.youtube.com/watch?v=j3-xqUjgb7k&t=1834s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "We've had a pricing module before in the past for pricing blind offers next "
               "week we're going to get even more detailed into it on zip code pricing "
               "strategies other than that guys thank you so much and we'll see you next time "
               'thanks for joining guys see you next time.',
       'timestamp': 1834,
       'timestamp_label': '[00:30:34]',
       'timestamp_seconds': 1834,
       'tip': "We've had a pricing module before in the past for pricing blind offers next "
              "week we're going to get even more detailed into it on zip code pricing "
              "strategies other than that guys thank you so much and we'll see you next time "
              'thanks for joining guys see you next time.',
       'title': 'How to Do Proper Due Diligence on Any Land Deal (Apke Brothers)',
       'url': 'https://www.youtube.com/watch?v=j3-xqUjgb7k&t=1834s',
       'video_id': 'j3-xqUjgb7k'},
      {'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:47](https://www.youtube.com/watch?v=k24QX2JK1ps&t=707s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I don't want to do a ton of it. If I have to get on the phone with with a "
               "seller or a buyer every so often, I don't mind that. But I don't want to do "
               'that all day in the business.',
       'timestamp': 707,
       'timestamp_label': '[00:11:47]',
       'timestamp_seconds': 707,
       'tip': "I don't want to do a ton of it. If I have to get on the phone with with a "
              "seller or a buyer every so often, I don't mind that. But I don't want to do "
              'that all day in the business.',
       'title': 'The Regulatory Squeeze on Land Investors with Seth Williams (REtipster)',
       'url': 'https://www.youtube.com/watch?v=k24QX2JK1ps&t=707s',
       'video_id': 'k24QX2JK1ps'},
      {'author': 'Land Academy',
       'channel': 'Land Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:03](https://www.youtube.com/watch?v=CbpqiGq5E5Y&t=363s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Before we start recording the show how do you feel about your hair I don't I "
               "don't have any feelings about my hair before we sit down and record these "
               'shows.',
       'timestamp': 363,
       'timestamp_label': '[00:06:03]',
       'timestamp_seconds': 363,
       'tip': "Before we start recording the show how do you feel about your hair I don't I "
              "don't have any feelings about my hair before we sit down and record these "
              'shows.',
       'title': 'DataTree vs TitlePro vs RealQuest Pro (LA 1422) (Land Academy)',
       'url': 'https://www.youtube.com/watch?v=CbpqiGq5E5Y&t=363s',
       'video_id': 'CbpqiGq5E5Y'},
      {'author': 'Ajay Sharma',
       'channel': 'Ajay Sharma',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:36](https://www.youtube.com/watch?v=Jb9R7WTh63s&t=576s)',
       'relevance': 'Attributed practitioner commentary on vacant & infill land flipping, GIS '
                    'parcel underwriting, minor subdivisions, and title-insured dispositions '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '8 uh per day, kind of like eight to 10 per week depending on the cold caller, '
               'depending on the list, depending on your phone numbers, depending on '
               "compliance. Like there's a lot of variables at play, right?",
       'timestamp': 576,
       'timestamp_label': '[00:09:36]',
       'timestamp_seconds': 576,
       'tip': '8 uh per day, kind of like eight to 10 per week depending on the cold caller, '
              'depending on the list, depending on your phone numbers, depending on '
              "compliance. Like there's a lot of variables at play, right?",
       'title': 'The 4-Part Deal Acquisition System Every Land Business Needs (Ajay Sharma)',
       'url': 'https://www.youtube.com/watch?v=Jb9R7WTh63s&t=576s',
       'video_id': 'Jb9R7WTh63s'}]}
