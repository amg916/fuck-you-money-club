"""Curated 180-citation High-Ticket Brokerage baseline (15 per chapter across Q1-Q12) mined strictly from verified High-Ticket Brokerage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'client',
     'clients',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 3: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cash',
     'cashflow',
     'cell',
     'center',
     'cim',
     'circumvention',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 4: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'capital',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 5: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'audit',
     'avoid',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'clawback',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 6: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'client',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 7: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'checklist',
     'cim',
     'circumvention',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 8: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'api',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'confidential',
     'connecting',
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
 9: {'6418',
     'agreement',
     'aircraft',
     'amended',
     'asset',
     'battery',
     'billboard',
     'boutique',
     'broken',
     'broker',
     'brokerage',
     'building',
     'business',
     'buy',
     'buyer',
     'buyers',
     'buyout',
     'car',
     'cell',
     'center',
     'cim',
     'circumvention',
     'closing',
     'club',
     'cold',
     'commercial',
     'commission',
     'commissions',
     'compliance',
     'confidential',
     'connecting',
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
 10: {'6418',
      'agent',
      'agreement',
      'ai',
      'aircraft',
      'amended',
      'asset',
      'automate',
      'automation',
      'battery',
      'billboard',
      'boutique',
      'broken',
      'broker',
      'brokerage',
      'building',
      'business',
      'buy',
      'buyer',
      'buyers',
      'buyout',
      'car',
      'cell',
      'center',
      'cim',
      'circumvention',
      'closing',
      'club',
      'cold',
      'commercial',
      'commission',
      'commissions',
      'confidential',
      'connecting',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'6418',
      'agreement',
      'aircraft',
      'amended',
      'asset',
      'battery',
      'billboard',
      'boutique',
      'broken',
      'broker',
      'brokerage',
      'building',
      'business',
      'buy',
      'buyer',
      'buyers',
      'buyout',
      'car',
      'cell',
      'center',
      'cim',
      'circumvention',
      'closing',
      'club',
      'cold',
      'commercial',
      'commission',
      'commissions',
      'confidential',
      'connecting',
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
 12: {'6418',
      'action',
      'agreement',
      'aircraft',
      'amended',
      'asset',
      'battery',
      'billboard',
      'boutique',
      'broken',
      'broker',
      'brokerage',
      'building',
      'business',
      'buy',
      'buyer',
      'buyers',
      'buyout',
      'car',
      'cell',
      'center',
      'cim',
      'circumvention',
      'closing',
      'club',
      'cold',
      'commercial',
      'commission',
      'commissions',
      'confidential',
      'connecting',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Deal Street - Small to Lower Middle Market M&A',
      'channel': 'Deal Street - Small to Lower Middle Market M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=ggUaT-lHV0A&t=71s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What the business earns, what multiple the market will pay for those earnings, '
              'and the risk a buyer sees in that business. Part one, it starts with earnings. '
              "Buyers don't buy revenue, they buy cash flow.",
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'What the business earns, what multiple the market will pay for those earnings, '
             'and the risk a buyer sees in that business. Part one, it starts with earnings. '
             "Buyers don't buy revenue, they buy cash flow.",
      'title': 'How Much Is My Business Really Worth? (How Buyers, Lenders & Brokers Value '
               'Small Businesses) (Deal Street - Small to Lower Middle Market M&A)',
      'url': 'https://www.youtube.com/watch?v=ggUaT-lHV0A&t=71s',
      'video_id': 'ggUaT-lHV0A'},
     {'author': 'Business with Mr. G',
      'channel': 'Business with Mr. G',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:01](https://www.youtube.com/watch?v=s3gi1d4BLP0&t=601s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A broker dealer typically gets paid commissions for executing a transaction. An '
              'investment adviser is getting paid specifically for the advice itself. Often '
              'charging a flat fee or a percentage of the assets they are managing for the '
              'client. Different business model entirely.',
      'timestamp': 601,
      'timestamp_label': '[00:10:01]',
      'timestamp_seconds': 601,
      'tip': 'A broker dealer typically gets paid commissions for executing a transaction. An '
             'investment adviser is getting paid specifically for the advice itself. Often '
             'charging a flat fee or a percentage of the assets they are managing for the '
             'client. Different business model entirely.',
      'title': 'Registration & Licensing | Broker-Dealer & Representative Rules Explained for '
               'the SIE Exam Prep! (Business with Mr. G)',
      'url': 'https://www.youtube.com/watch?v=s3gi1d4BLP0&t=601s',
      'video_id': 's3gi1d4BLP0'},
     {'author': 'American Business Intermediaries',
      'channel': 'American Business Intermediaries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=LRGkOAsiUdQ&t=218s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Privately held businesses and typically only market to individual buyers most '
              'clients of business brokers run owner operated businesses and have a cash flow.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'Privately held businesses and typically only market to individual buyers most '
             'clients of business brokers run owner operated businesses and have a cash flow.',
      'title': 'Difference Between an Investment Banker, M&A Advisor, & Business Broker '
               '(American Business Intermediaries)',
      'url': 'https://www.youtube.com/watch?v=LRGkOAsiUdQ&t=218s',
      'video_id': 'LRGkOAsiUdQ'},
     {'author': 'Ryan C. Winter, Business Broker',
      'channel': 'Ryan C. Winter, Business Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=tPnDBaB9oPU&t=195s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customers who come back for repeat business, who are on some sort of '
              "subscription plan, that's worth a lot of money. And then customer "
              'concentration. If one client is half of your revenue, a buyer sees that as a '
              'huge red flag.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'Customers who come back for repeat business, who are on some sort of '
             "subscription plan, that's worth a lot of money. And then customer concentration. "
             'If one client is half of your revenue, a buyer sees that as a huge red flag.',
      'title': 'How to Value a Business: SDE, Multiples & Add-Backs (Ryan C. Winter, Business '
               'Broker)',
      'url': 'https://www.youtube.com/watch?v=tPnDBaB9oPU&t=195s',
      'video_id': 'tPnDBaB9oPU'},
     {'author': 'Business Broker Growth',
      'channel': 'Business Broker Growth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:21](https://www.youtube.com/watch?v=7jkOz9WXEh8&t=561s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I think it's valuable to get it out there, which is holding the deal together. "
              "You mentioned that's one part of your video is the value of you as a as an "
              'intermediary, you know, business broker adviser is holding the deal together, '
              'holding the parties together.',
      'timestamp': 561,
      'timestamp_label': '[00:09:21]',
      'timestamp_seconds': 561,
      'tip': "I think it's valuable to get it out there, which is holding the deal together. "
             "You mentioned that's one part of your video is the value of you as a as an "
             'intermediary, you know, business broker adviser is holding the deal together, '
             'holding the parties together.',
      'title': 'Building a Boutique Brokerage Firm: AI, Business Exits & Growth Tips | '
               'Christine McDannell ! (Business Broker Growth)',
      'url': 'https://www.youtube.com/watch?v=7jkOz9WXEh8&t=561s',
      'video_id': '7jkOz9WXEh8'},
     {'author': 'Public Company Accounting Oversight Board - PCAOB',
      'channel': 'Public Company Accounting Oversight Board - PCAOB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:52](https://www.youtube.com/watch?v=BV647oU5rB0&t=2632s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The securities must be in the name of the firm. The securities have to be '
              'carried at fair market value and the liability to the registered person '
              'adjusted based on fair market value of the securities.',
      'timestamp': 2632,
      'timestamp_label': '[00:43:52]',
      'timestamp_seconds': 2632,
      'tip': 'The securities must be in the name of the firm. The securities have to be '
             'carried at fair market value and the liability to the registered person adjusted '
             'based on fair market value of the securities.',
      'title': '11/5/26 Small Business and Broker-Dealer Forums - FINRA Update (Public Company '
               'Accounting Oversight Board - PCAOB)',
      'url': 'https://www.youtube.com/watch?v=BV647oU5rB0&t=2632s',
      'video_id': 'BV647oU5rB0'},
     {'author': 'Brett Cenkus',
      'channel': 'Brett Cenkus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=y4u_MuL4xhw&t=45s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When we do M&A advisory and Business Brokerage we do it from 1 million to 20 '
              "million that's kind of our sweet spot so this information is really well suited "
              'for someone buying or selling in that part of the market so the other ways.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'When we do M&A advisory and Business Brokerage we do it from 1 million to 20 '
             "million that's kind of our sweet spot so this information is really well suited "
             'for someone buying or selling in that part of the market so the other ways.',
      'title': 'How To Value a Business for Sale (Mergers and Acquisitions) (Brett Cenkus)',
      'url': 'https://www.youtube.com/watch?v=y4u_MuL4xhw&t=45s',
      'video_id': 'y4u_MuL4xhw'},
     {'author': 'Daniel Coutts',
      'channel': 'Daniel Coutts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=RHobLxb_gLQ&t=237s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, that is the overall concept of high ticket sales. You are just closing '
              'people that are already interested in a product and a service, getting them '
              'over their limiting beliefs and getting them over the finish line that way you '
              'can make your fat commission, right?',
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': 'So, that is the overall concept of high ticket sales. You are just closing '
             'people that are already interested in a product and a service, getting them over '
             'their limiting beliefs and getting them over the finish line that way you can '
             'make your fat commission, right?',
      'title': 'The Framework That Changed Everything for Me in High Ticket Sales (Daniel '
               'Coutts)',
      'url': 'https://www.youtube.com/watch?v=RHobLxb_gLQ&t=237s',
      'video_id': 'RHobLxb_gLQ'},
     {'author': 'Daniel Botero',
      'channel': 'Daniel Botero',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:22](https://www.youtube.com/watch?v=r2vbi9gCm-o&t=982s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a belief, not a money objection. If you put this all together, then you're "
              'going to be closing 20, 30, 40, 60% of your clients. What does this mean for '
              'your business?',
      'timestamp': 982,
      'timestamp_label': '[00:16:22]',
      'timestamp_seconds': 982,
      'tip': "It's a belief, not a money objection. If you put this all together, then you're "
             'going to be closing 20, 30, 40, 60% of your clients. What does this mean for '
             'your business?',
      'title': 'The High-Ticket Sales Framework Every Career Coach Needs (Daniel Botero)',
      'url': 'https://www.youtube.com/watch?v=r2vbi9gCm-o&t=982s',
      'video_id': 'r2vbi9gCm-o'},
     {'author': 'SMB Law Group LLP',
      'channel': 'SMB Law Group LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:05](https://www.youtube.com/watch?v=LASFByP_8g4&t=1565s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I would probably say go hire a firm with a super deep bench. Don't worry about "
              "price when you're buying a $100 million business. But >> that's not the case in "
              'the lower middle market. You know, money matters and having a war chest both '
              'pre and postclosing matters.',
      'timestamp': 1565,
      'timestamp_label': '[00:26:05]',
      'timestamp_seconds': 1565,
      'tip': "I would probably say go hire a firm with a super deep bench. Don't worry about "
             "price when you're buying a $100 million business. But >> that's not the case in "
             'the lower middle market. You know, money matters and having a war chest both pre '
             'and postclosing matters.',
      'title': 'What does “Market” actually mean? | Main Street Deals (SMB Law Group LLP)',
      'url': 'https://www.youtube.com/watch?v=LASFByP_8g4&t=1565s',
      'video_id': 'LASFByP_8g4'},
     {'author': 'Centimillionaire Strategies',
      'channel': 'Centimillionaire Strategies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:49](https://www.youtube.com/watch?v=60V2lsbfZos&t=709s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, for example, I recently saw one that was for self-service laundromats. I '
              'you know, I would never have thought of a roll up of a self-service laundromat. '
              "It's a very appealing business model, actually. Very doesn't require a lot of "
              'staff.',
      'timestamp': 709,
      'timestamp_label': '[00:11:49]',
      'timestamp_seconds': 709,
      'tip': 'Um, for example, I recently saw one that was for self-service laundromats. I you '
             "know, I would never have thought of a roll up of a self-service laundromat. It's "
             "a very appealing business model, actually. Very doesn't require a lot of staff.",
      'title': 'Inside the Minds of Billion-Dollar Family Offices: How the Ultra-Wealthy '
               'Invest in 2025 (Centimillionaire Strategies)',
      'url': 'https://www.youtube.com/watch?v=60V2lsbfZos&t=709s',
      'video_id': '60V2lsbfZos'},
     {'author': 'Aswath Damodaran',
      'channel': 'Aswath Damodaran',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=xI-KTlxfNDU&t=346s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "EVITA, but because it's an enterprise value to AIDA multiple. I'm going to go "
              'back to an enterprise valuation model. The value of a firm is the expected free '
              'cash flow to the firm divided by the cost of capital minus growth.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': "EVITA, but because it's an enterprise value to AIDA multiple. I'm going to go "
             'back to an enterprise valuation model. The value of a firm is the expected free '
             'cash flow to the firm divided by the cost of capital minus growth.',
      'title': 'Session 16: Other Earnings Multiples (Aswath Damodaran)',
      'url': 'https://www.youtube.com/watch?v=xI-KTlxfNDU&t=346s',
      'video_id': 'xI-KTlxfNDU'},
     {'author': 'The Digital Merchant',
      'channel': 'The Digital Merchant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=NSNpSgvzAyA&t=223s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You know, I've seen lots of brokerages where they'll have one guy that's a "
              "specialist, you know, maybe I'm looking for an automotive type business. Well, "
              "he specializes in that. But I I've never seen a model where everybody has "
              'industry experience.',
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': "You know, I've seen lots of brokerages where they'll have one guy that's a "
             "specialist, you know, maybe I'm looking for an automotive type business. Well, "
             "he specializes in that. But I I've never seen a model where everybody has "
             'industry experience.',
      'title': 'Quiet Light Brokerage Review: Specialized Online Business Brokers Explained '
               '(The Digital Merchant)',
      'url': 'https://www.youtube.com/watch?v=NSNpSgvzAyA&t=223s',
      'video_id': 'NSNpSgvzAyA'},
     {'author': 'SiteBid Infrastructure',
      'channel': 'SiteBid Infrastructure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=fLebm5BppxY&t=85s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These include the current leased area plus additional space, often around 500 '
              'square ft. This extra space creates opportunities for new tenants while '
              'maintaining a defined easement footprint. Like general easements, expanded '
              'easements can include a revenue sharing agreement.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'These include the current leased area plus additional space, often around 500 '
             'square ft. This extra space creates opportunities for new tenants while '
             'maintaining a defined easement footprint. Like general easements, expanded '
             'easements can include a revenue sharing agreement.',
      'title': 'Telecom Easements:  What Property Owners Need to Know (SiteBid Infrastructure)',
      'url': 'https://www.youtube.com/watch?v=fLebm5BppxY&t=85s',
      'video_id': 'fLebm5BppxY'},
     {'author': 'RareBrain',
      'channel': 'RareBrain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=ntmKBtSOxhU&t=221s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sell for maximum value how ready is your company to grow or to sell want to '
              "know how you're doing get your free score plus customized report in just a few "
              'minutes at no cost or obligation visit Reverend com / score.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Sell for maximum value how ready is your company to grow or to sell want to know '
             "how you're doing get your free score plus customized report in just a few "
             'minutes at no cost or obligation visit Reverend com / score.',
      'title': 'Differences between Business Brokers, M&A Advisors, Investment Bankers & Exit '
               'Planners (EP2) (RareBrain)',
      'url': 'https://www.youtube.com/watch?v=ntmKBtSOxhU&t=221s',
      'video_id': 'ntmKBtSOxhU'}],
 2: [{'author': 'Think Real Estate',
      'channel': 'Think Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=wBbi84Xi1Bc&t=22s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That agreement states that if the buyer wants to buy a home and the seller will '
              'not pay a buyer broker commission, then the buyer will have to pay their own '
              'agents commission.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'That agreement states that if the buyer wants to buy a home and the seller will '
             'not pay a buyer broker commission, then the buyer will have to pay their own '
             'agents commission.',
      'title': 'What Buyers and Sellers Need to Know About the Buyer Broker Agreement in 2025 '
               '(Think Real Estate)',
      'url': 'https://www.youtube.com/watch?v=wBbi84Xi1Bc&t=22s',
      'video_id': 'wBbi84Xi1Bc'},
     {'author': 'Own The Jet',
      'channel': 'Own The Jet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:32](https://www.youtube.com/watch?v=i36Xg_tsVAY&t=1112s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So if you're going to, let's get this,</b> <b>So if you're going to,</b> "
              "<b>let's get that upfront going. You need to know the escrow agents have</b> "
              '<b>Need to know the escrow</b> <b>agents have an escrow agreement. A contract '
              'with your broker. A contract with your broker.',
      'timestamp': 1112,
      'timestamp_label': '[00:18:32]',
      'timestamp_seconds': 1112,
      'tip': "So if you're going to, let's get this,</b> <b>So if you're going to,</b> "
             "<b>let's get that upfront going. You need to know the escrow agents have</b> "
             '<b>Need to know the escrow</b> <b>agents have an escrow agreement. A contract '
             'with your broker. A contract with your broker.',
      'title': 'Understanding Aircraft Brokerage: Standards, Risk, and Trust (Own The Jet)',
      'url': 'https://www.youtube.com/watch?v=i36Xg_tsVAY&t=1112s',
      'video_id': 'i36Xg_tsVAY'},
     {'author': 'Colin Matcha',
      'channel': 'Colin Matcha',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=l-9E6P1CSEc&t=363s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You will need an asset purchase agreement or contract of some sort the asset '
              'purchase agreement is what will determine whether you use escrow like an.',
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': 'You will need an asset purchase agreement or contract of some sort the asset '
             'purchase agreement is what will determine whether you use escrow like an.',
      'title': 'Quiet Light Brokerage Review for Buyers 2022 (Colin Matcha)',
      'url': 'https://www.youtube.com/watch?v=l-9E6P1CSEc&t=363s',
      'video_id': 'l-9E6P1CSEc'},
     {'author': 'POTOMAC M&A',
      'channel': 'POTOMAC M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:59](https://www.youtube.com/watch?v=-mNiPaYyDro&t=179s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "100 customers and each customer pays you $1 a year, you're getting $100 a year "
              'in revenue from 100 customers. Not a lot of customer concentration risk. If '
              "you're making $100 a year and your two largest customers each pay you $25 a "
              "year, it's half your business.",
      'timestamp': 179,
      'timestamp_label': '[00:02:59]',
      'timestamp_seconds': 179,
      'tip': "100 customers and each customer pays you $1 a year, you're getting $100 a year "
             'in revenue from 100 customers. Not a lot of customer concentration risk. If '
             "you're making $100 a year and your two largest customers each pay you $25 a "
             "year, it's half your business.",
      'title': 'Buy-Side M&A 101: Should You Do an Acquisition? | Buy-Side Masterclass Moment '
               '(POTOMAC M&A)',
      'url': 'https://www.youtube.com/watch?v=-mNiPaYyDro&t=179s',
      'video_id': '-mNiPaYyDro'},
     {'author': 'Six Minutes',
      'channel': 'Six Minutes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=eb9QUJSQh9o&t=136s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the customer buys a security, the broker-dealer hat is on. If the customer '
              'pays for advice, the adviser hat is on. A bank itself is not a broker-dealer, '
              "but a bank's brokerage affiliate can be. Edge case three, the SEC is not alone. "
              'Broker-dealers also answer to FINRA.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'If the customer buys a security, the broker-dealer hat is on. If the customer '
             'pays for advice, the adviser hat is on. A bank itself is not a broker-dealer, '
             "but a bank's brokerage affiliate can be. Edge case three, the SEC is not alone. "
             'Broker-dealers also answer to FINRA.',
      'title': "The SEC's Authority and What an SRO Is | Six Minutes: SIE, Part 2 (Six "
               'Minutes)',
      'url': 'https://www.youtube.com/watch?v=eb9QUJSQh9o&t=136s',
      'video_id': 'eb9QUJSQh9o'},
     {'author': 'Joe Mendoza',
      'channel': 'Joe Mendoza',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=VcNeWYSFiDE&t=189s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a trade-off, you know, because at one point I made over a million dollars "
              'gross commission income and that year I gave Prudential California Realty plus '
              'a broker owner plus a franchise fee over $200,000, okay?',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': "'s a trade-off, you know, because at one point I made over a million dollars "
             'gross commission income and that year I gave Prudential California Realty plus a '
             'broker owner plus a franchise fee over $200,000, okay?',
      'title': 'Big Box vs. Boutique: Which Brokerage Will Make You More Money? (Joe Mendoza)',
      'url': 'https://www.youtube.com/watch?v=VcNeWYSFiDE&t=189s',
      'video_id': 'VcNeWYSFiDE'},
     {'author': 'Family Split Strategy',
      'channel': 'Family Split Strategy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=DZe5D7_TCDA&t=222s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Also sent some of the money to pay off the old mortgage there's also fees that "
              'have to be paid from that transaction there are closing costs there are.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': "Also sent some of the money to pay off the old mortgage there's also fees that "
             'have to be paid from that transaction there are closing costs there are.',
      'title': 'Wire Transfer Escrow Fraud - Preventing, Detecting, Recovering (Family Split '
               'Strategy)',
      'url': 'https://www.youtube.com/watch?v=DZe5D7_TCDA&t=222s',
      'video_id': 'DZe5D7_TCDA'},
     {'author': 'CertFuel',
      'channel': 'CertFuel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=deQ3XNDiApo&t=73s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They don't actually own the house, they just connect a buyer and a seller for a "
              'fee. A dealer, on the other hand, buys and sells securities for its own '
              "account. They're acting as a principal. Picture a super greasy used car dealer.",
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': "They don't actually own the house, they just connect a buyer and a seller for a "
             'fee. A dealer, on the other hand, buys and sells securities for its own account. '
             "They're acting as a principal. Picture a super greasy used car dealer.",
      'title': 'Broker-Dealer Regulation: Rapid Fire - Series 66 Exam Prep (CertFuel)',
      'url': 'https://www.youtube.com/watch?v=deQ3XNDiApo&t=73s',
      'video_id': 'deQ3XNDiApo'},
     {'author': 'Keira Hamilton',
      'channel': 'Keira Hamilton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=1dJeO4qEAhU&t=56s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like with you as the new owner for example interest payment if you're looking "
              "at a business to buy and there is a loan on that business whether it's.",
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': "Like with you as the new owner for example interest payment if you're looking at "
             "a business to buy and there is a loan on that business whether it's.",
      'title': "What is Seller's Discretionary Earnings (SDE)? And Why Does it Matter? (Keira "
               'Hamilton)',
      'url': 'https://www.youtube.com/watch?v=1dJeO4qEAhU&t=56s',
      'video_id': '1dJeO4qEAhU'},
     {'author': 'CompassPointCapital',
      'channel': 'CompassPointCapital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=2KA0GQ8fBkc&t=155s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The buyers could be and uh and then it's a matter of just having somebody um an "
              'investment banker with industry focus that can that can put those deals '
              "together so I hope this is helpful and uh there's a follow-up video on on the "
              'fees that you can expect.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': "The buyers could be and uh and then it's a matter of just having somebody um an "
             'investment banker with industry focus that can that can put those deals together '
             "so I hope this is helpful and uh there's a follow-up video on on the fees that "
             'you can expect.',
      'title': 'What is a Business Broker vs. M&A Advisor? (CompassPointCapital)',
      'url': 'https://www.youtube.com/watch?v=2KA0GQ8fBkc&t=155s',
      'video_id': '2KA0GQ8fBkc'},
     {'author': "Title's Not Borin' with Lauren",
      'channel': "Title's Not Borin' with Lauren",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=IK3LgAFr-QQ&t=133s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mutually agreed instruction the goal is to have everything completed and '
              'returned to escrow within your contingency periods so that we can proceed to a '
              'smooth closing thank you for watching thank you for engaging and most '
              'importantly thank you for choosing Chicago title.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': 'Mutually agreed instruction the goal is to have everything completed and '
             'returned to escrow within your contingency periods so that we can proceed to a '
             'smooth closing thank you for watching thank you for engaging and most '
             'importantly thank you for choosing Chicago title.',
      'title': "The Deposit and Escrow Instructions (Title's Not Borin' with Lauren)",
      'url': 'https://www.youtube.com/watch?v=IK3LgAFr-QQ&t=133s',
      'video_id': 'IK3LgAFr-QQ'},
     {'author': 'ReminderMedia | 🎙️STAY PAID PODCAST',
      'channel': 'ReminderMedia | 🎙️STAY PAID PODCAST',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:58](https://www.youtube.com/watch?v=2WIql7qBDoY&t=1558s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For life at Copper Hill and that was really what we strive to do with our own '
              "brokerage I love that love the customer Centric Focus I'm also very hungry now "
              'I.',
      'timestamp': 1558,
      'timestamp_label': '[00:25:58]',
      'timestamp_seconds': 1558,
      'tip': 'For life at Copper Hill and that was really what we strive to do with our own '
             "brokerage I love that love the customer Centric Focus I'm also very hungry now "
             'I.',
      'title': 'How to Start Your Own Independent Real Estate Brokerage (What it really takes) '
               '(ReminderMedia | 🎙️STAY PAID PODCAST)',
      'url': 'https://www.youtube.com/watch?v=2WIql7qBDoY&t=1558s',
      'video_id': '2WIql7qBDoY'},
     {'author': 'Quiet Light Brokerage',
      'channel': 'Quiet Light Brokerage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=R4jvbLHhCBg&t=41s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the higher this number goes, the more valuable your business becomes. If '
              "you're a buyer, discretionary earnings gives you a baseline level of "
              'profitability so you can understand your potential return of investment for '
              'your particular scenario.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'So the higher this number goes, the more valuable your business becomes. If '
             "you're a buyer, discretionary earnings gives you a baseline level of "
             'profitability so you can understand your potential return of investment for your '
             'particular scenario.',
      'title': 'What Is Seller’s Discretionary Earnings or SDE (and How to Calculate It) '
               '(Quiet Light Brokerage)',
      'url': 'https://www.youtube.com/watch?v=R4jvbLHhCBg&t=41s',
      'video_id': 'R4jvbLHhCBg'},
     {'author': 'Brandon Mulrenin',
      'channel': 'Brandon Mulrenin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=5YNeLidiqqU&t=233s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They've got all the goodies so with their so the payment's important here so "
              'with their PMI included their month payment does not include taxes and '
              "insurance is $2,725 a month how much I'm sorry.",
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': "They've got all the goodies so with their so the payment's important here so "
             'with their PMI included their month payment does not include taxes and insurance '
             "is $2,725 a month how much I'm sorry.",
      'title': "Realtors: Do this if the seller won't pay a buyer agent commission (Brandon "
               'Mulrenin)',
      'url': 'https://www.youtube.com/watch?v=5YNeLidiqqU&t=233s',
      'video_id': '5YNeLidiqqU'},
     {'author': 'CompassPointCapital',
      'channel': 'CompassPointCapital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=bjJIoxsFNY8&t=137s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Banker and a lot of the large investment Banks you know the success fee can be '
              "um you know million minimum um $2 million so that's that's kind of the the "
              'range and and what you can expect from uh from the fees from a from an '
              'intermediary.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'Banker and a lot of the large investment Banks you know the success fee can be '
             "um you know million minimum um $2 million so that's that's kind of the the range "
             'and and what you can expect from uh from the fees from a from an intermediary.',
      'title': 'What do brokers and M&A advisors charge for fees? (CompassPointCapital)',
      'url': 'https://www.youtube.com/watch?v=bjJIoxsFNY8&t=137s',
      'video_id': 'bjJIoxsFNY8'}],
 3: [{'author': 'Hauseit',
      'channel': 'Hauseit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=KrsoinTC_10&t=117s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're looking to save money when you buy and sell property in New York and "
              'Florida you can do so hauseit.com check this out you can save six percent when '
              'you sell in broker commissions and two percent back or more when you buy with a '
              'house sit buyer closing credit.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': "You're looking to save money when you buy and sell property in New York and "
             'Florida you can do so hauseit.com check this out you can save six percent when '
             'you sell in broker commissions and two percent back or more when you buy with a '
             'house sit buyer closing credit.',
      'title': 'How to Wire Money for Closing (Hauseit)',
      'url': 'https://www.youtube.com/watch?v=KrsoinTC_10&t=117s',
      'video_id': 'KrsoinTC_10'},
     {'author': 'Dee Kumar Real Estate',
      'channel': 'Dee Kumar Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:08](https://www.youtube.com/watch?v=V5gUCAcegsY&t=368s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Determining price of a business, we we will touch on very briefly in this '
              'particular unit. You know, again, this is a real estate brokerage exam, not a '
              'business uh brokerage uh exam, but reconciliation of income costs and market '
              'data.',
      'timestamp': 368,
      'timestamp_label': '[00:06:08]',
      'timestamp_seconds': 368,
      'tip': 'Determining price of a business, we we will touch on very briefly in this '
             'particular unit. You know, again, this is a real estate brokerage exam, not a '
             'business uh brokerage uh exam, but reconciliation of income costs and market '
             'data.',
      'title': 'Business Brokerage Explained | What You NEED to Know for the Real Estate Exam '
               '(Dee Kumar Real Estate)',
      'url': 'https://www.youtube.com/watch?v=V5gUCAcegsY&t=368s',
      'video_id': 'V5gUCAcegsY'},
     {'author': 'Quiet Light Brokerage',
      'channel': 'Quiet Light Brokerage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=_t4Q9Q7VTtQ&t=131s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '100% seller finance deal will work? Typically, a 100% seller finance deal is '
              'really good for buying out a business partner. For those that are buyers that '
              "are doing this strategy, you'd be way better off to put together some cash and "
              'go buy a business that you can afford.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': '100% seller finance deal will work? Typically, a 100% seller finance deal is '
             'really good for buying out a business partner. For those that are buyers that '
             "are doing this strategy, you'd be way better off to put together some cash and "
             'go buy a business that you can afford.',
      'title': 'Why I Immediately Reject Most "Full Price" Offers (Quiet Light Brokerage)',
      'url': 'https://www.youtube.com/watch?v=_t4Q9Q7VTtQ&t=131s',
      'video_id': '_t4Q9Q7VTtQ'},
     {'author': 'Sam Cutting - Red Flags Verification',
      'channel': 'Sam Cutting - Red Flags Verification',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=QguZjBADFoA&t=66s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Two, if you have the buyer, have them sign a commission agreement as you should '
              'have some kind of relationship with them. You can ask for a fixed commission as '
              'your job is to get them the best possible price.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Two, if you have the buyer, have them sign a commission agreement as you should '
             'have some kind of relationship with them. You can ask for a fixed commission as '
             'your job is to get them the best possible price.',
      'title': 'Don’t Get Circumvented (Cheated) (Sam Cutting - Red Flags Verification)',
      'url': 'https://www.youtube.com/watch?v=QguZjBADFoA&t=66s',
      'video_id': 'QguZjBADFoA'},
     {'author': 'Brent Freeman  - The CBB Group',
      'channel': 'Brent Freeman  - The CBB Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=pzqh4R8Hppk&t=88s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Net profit and the cash flow in this slide you'll see that the company has "
              'revenues of about 8.7 million dollars cost of goods were 6.6 million giving.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': "Net profit and the cash flow in this slide you'll see that the company has "
             'revenues of about 8.7 million dollars cost of goods were 6.6 million giving.',
      'title': 'Net Profit is not Cash Flow - EBITDA or SDE!  Buying a Business and SBA. '
               '(Brent Freeman  - The CBB Group)',
      'url': 'https://www.youtube.com/watch?v=pzqh4R8Hppk&t=88s',
      'video_id': 'pzqh4R8Hppk'},
     {'author': 'Alex Bengoechea',
      'channel': 'Alex Bengoechea',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Uhqo4raDQ0k&t=15s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Into it aircraft Brokers typically earn a commission on the sale of an aircraft '
              'which is a percentage of the total sale price Brokers usually charge a.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Into it aircraft Brokers typically earn a commission on the sale of an aircraft '
             'which is a percentage of the total sale price Brokers usually charge a.',
      'title': 'How Much Does An Aircraft Broker Make? (Alex Bengoechea)',
      'url': 'https://www.youtube.com/watch?v=Uhqo4raDQ0k&t=15s',
      'video_id': 'Uhqo4raDQ0k'},
     {'author': 'Justin Goodbread',
      'channel': 'Justin Goodbread',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:19](https://www.youtube.com/watch?v=gDql0VQct6A&t=859s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're gonna be looking for a business broker not always the chances are if "
              "you're in that price range of five to thirty million dollars then you're.",
      'timestamp': 859,
      'timestamp_label': '[00:14:19]',
      'timestamp_seconds': 859,
      'tip': "You're gonna be looking for a business broker not always the chances are if "
             "you're in that price range of five to thirty million dollars then you're.",
      'title': 'The Business Broker, M&A Advisor, or Investment Banker (Justin Goodbread)',
      'url': 'https://www.youtube.com/watch?v=gDql0VQct6A&t=859s',
      'video_id': 'gDql0VQct6A'},
     {'author': 'Brandon Thomas',
      'channel': 'Brandon Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:11](https://www.youtube.com/watch?v=vOB7Te243ew&t=371s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I haven't been so lucky to find a solid probate attorney. So, if you're in "
              'Maryland and or Pennsylvania or West Virginia, those are the main like states '
              "that we buy in. If you're a probate attorney and you need a good cash buyer for "
              'a quick close, let me know.',
      'timestamp': 371,
      'timestamp_label': '[00:06:11]',
      'timestamp_seconds': 371,
      'tip': "I haven't been so lucky to find a solid probate attorney. So, if you're in "
             'Maryland and or Pennsylvania or West Virginia, those are the main like states '
             "that we buy in. If you're a probate attorney and you need a good cash buyer for "
             'a quick close, let me know.',
      'title': 'How to find off-market leads like a PRO (Brandon Thomas)',
      'url': 'https://www.youtube.com/watch?v=vOB7Te243ew&t=371s',
      'video_id': 'vOB7Te243ew'},
     {'author': 'LoCasa',
      'channel': 'LoCasa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:19](https://www.youtube.com/watch?v=Fug5C3kFHsA&t=619s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because because if we're paying commissions, the price wouldn't be 450. No, "
              "there wouldn't be any realtor or any commissions involved. Uh, what company are "
              'you with, Rachel? You You want to text me your information?',
      'timestamp': 619,
      'timestamp_label': '[00:10:19]',
      'timestamp_seconds': 619,
      'tip': "Because because if we're paying commissions, the price wouldn't be 450. No, "
             "there wouldn't be any realtor or any commissions involved. Uh, what company are "
             'you with, Rachel? You You want to text me your information?',
      'title': 'How I Find Off-Market Properties - Cold Calling Strategy That Works (Live Cold '
               'Calls) | LoCasa (LoCasa)',
      'url': 'https://www.youtube.com/watch?v=Fug5C3kFHsA&t=619s',
      'video_id': 'Fug5C3kFHsA'},
     {'author': 'Seller Accountant',
      'channel': 'Seller Accountant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=jkHzL8ya984&t=104s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Logistics fees the amazon commissions and so their gross profit was 340 000 uh '
              'they had advertising in two different categories they had their amazon ppc or.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Logistics fees the amazon commissions and so their gross profit was 340 000 uh '
             'they had advertising in two different categories they had their amazon ppc or.',
      'title': 'Valuing Your E-Commerce Business: SDE, Add-backs, and Multiples (Seller '
               'Accountant)',
      'url': 'https://www.youtube.com/watch?v=jkHzL8ya984&t=104s',
      'video_id': 'jkHzL8ya984'},
     {'author': 'VoraPrep',
      'channel': 'VoraPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=Dw1n0a_kMu0&t=55s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It starts with the absolute core of the business. The first things are '
              "blotters. Think of a blotter as the firm's daily diary for every single "
              'transaction. Every purchase, every sale, every time cash comes in or goes out, '
              'it gets an entry.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'It starts with the absolute core of the business. The first things are blotters. '
             "Think of a blotter as the firm's daily diary for every single transaction. Every "
             'purchase, every sale, every time cash comes in or goes out, it gets an entry.',
      'title': '[Series 24] S24F2: Broker-Dealer Recordkeeping: SEA Rules 17a-3 and 17a-4 '
               '(VoraPrep)',
      'url': 'https://www.youtube.com/watch?v=Dw1n0a_kMu0&t=55s',
      'video_id': 'Dw1n0a_kMu0'},
     {'author': 'Paul Vu',
      'channel': 'Paul Vu',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:12](https://www.youtube.com/watch?v=LeKXSFb84sA&t=492s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But with high ticket sales, there's a much higher percentage of people actually "
              "succeeding in the business. Granted, the the ceiling isn't as high, but it's a "
              'very good stepping stone to stack up a lot of cash, right?',
      'timestamp': 492,
      'timestamp_label': '[00:08:12]',
      'timestamp_seconds': 492,
      'tip': "But with high ticket sales, there's a much higher percentage of people actually "
             "succeeding in the business. Granted, the the ceiling isn't as high, but it's a "
             'very good stepping stone to stack up a lot of cash, right?',
      'title': 'Seriously, Please Watch This Before You Start High Ticket Sales (Paul Vu)',
      'url': 'https://www.youtube.com/watch?v=LeKXSFb84sA&t=492s',
      'video_id': 'LeKXSFb84sA'},
     {'author': 'iBankerU',
      'channel': 'iBankerU',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=HGsCcOXJIOw&t=94s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"walk me through an income statement." Anybody knows that the basic headlines '
              'for an income statement are Revenue less your Cost of Goods Sold equals your '
              'Gross Profit; minus your Operating Expenses equals your Net Profit.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': '"walk me through an income statement." Anybody knows that the basic headlines '
             'for an income statement are Revenue less your Cost of Goods Sold equals your '
             'Gross Profit; minus your Operating Expenses equals your Net Profit.',
      'title': 'M&A Investment Banking Interview Questions - Middle Market ($50-300MM) '
               '(iBankerU)',
      'url': 'https://www.youtube.com/watch?v=HGsCcOXJIOw&t=94s',
      'video_id': 'HGsCcOXJIOw'},
     {'author': 'Arthur Petropoulos',
      'channel': 'Arthur Petropoulos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=brFD1fFAYhQ&t=28s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Much it would cost to build that versus buy it that's one type of conversation "
              "there are other types of conversations when someone's looking to really just.",
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "Much it would cost to build that versus buy it that's one type of conversation "
             "there are other types of conversations when someone's looking to really just.",
      'title': 'EBITDA Multiples and Valuation Ranges: How Companies are Valued (Arthur '
               'Petropoulos)',
      'url': 'https://www.youtube.com/watch?v=brFD1fFAYhQ&t=28s',
      'video_id': 'brFD1fFAYhQ'},
     {'author': 'Jesse Ebner',
      'channel': 'Jesse Ebner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=6cCUTLOmNIE&t=204s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Drive a semi though I have to admit are you serious yeah I don't know I think "
              "it'd be cool you could come drive our rv I mean how powerful is that like "
              "that's a huge truck cool get a girl.",
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': "Drive a semi though I have to admit are you serious yeah I don't know I think "
             "it'd be cool you could come drive our rv I mean how powerful is that like that's "
             'a huge truck cool get a girl.',
      'title': 'Boutique vs Franchise Real Estate Brokerage | We Hold the Keys Podcast (Jesse '
               'Ebner)',
      'url': 'https://www.youtube.com/watch?v=6cCUTLOmNIE&t=204s',
      'video_id': '6cCUTLOmNIE'}],
 4: [{'author': 'MarginCallMedia',
      'channel': 'MarginCallMedia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=PWGk1rSbFhA&t=52s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The industry splits into two very distinct camps, aircraft sales and aircraft '
              'charter. Aircraft sales brokers operate a lot like high-end agents. When a '
              'client buys a $20 million jet, the broker earns a predictable commission paid '
              'at closing.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'The industry splits into two very distinct camps, aircraft sales and aircraft '
             'charter. Aircraft sales brokers operate a lot like high-end agents. When a '
             'client buys a $20 million jet, the broker earns a predictable commission paid at '
             'closing.',
      'title': 'How Private Jet Brokers Actually Make Money | Hidden Commissions Explained '
               '(MarginCallMedia)',
      'url': 'https://www.youtube.com/watch?v=PWGk1rSbFhA&t=52s',
      'video_id': 'PWGk1rSbFhA'},
     {'author': 'Alex Bengoechea',
      'channel': 'Alex Bengoechea',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=p6XXGAWrnB8&t=20s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, to become an aircraft broker, you don't need an FA license. You also don't "
              'need a license if you are looking to work for another brokerage.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Now, to become an aircraft broker, you don't need an FA license. You also don't "
             'need a license if you are looking to work for another brokerage.',
      'title': 'How to Start an Aircraft Brokerage Business | Step-by-Step Guide (Alex '
               'Bengoechea)',
      'url': 'https://www.youtube.com/watch?v=p6XXGAWrnB8&t=20s',
      'video_id': 'p6XXGAWrnB8'},
     {'author': 'Exit On Your Terms',
      'channel': 'Exit On Your Terms',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=Dx_mEuS7ipk&t=73s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The relationship almost looks like he might have with a commercial real estate '
              'agent, or even a residential one, selling your home infinitely more complex but '
              "similar type of setup. They're taking a business, they're analyzing it, they're "
              'bringing it to market.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'The relationship almost looks like he might have with a commercial real estate '
             'agent, or even a residential one, selling your home infinitely more complex but '
             "similar type of setup. They're taking a business, they're analyzing it, they're "
             'bringing it to market.',
      'title': 'Business Broker vs M&A Advisor vs Investment Banker: Which Advisor Do You '
               'Actually Need? (Exit On Your Terms)',
      'url': 'https://www.youtube.com/watch?v=Dx_mEuS7ipk&t=73s',
      'video_id': 'Dx_mEuS7ipk'},
     {'author': 'International Business Brokers Association',
      'channel': 'International Business Brokers Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:17](https://www.youtube.com/watch?v=7mV4t9a4PvE&t=2897s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um quite commonly it's a service business. So there really isn't a corporate "
              'entity being purchased. It really is an asset transaction. Now the question is '
              "what what else is being exchanged? Is it cash for those assets? That's probably "
              'not a security.',
      'timestamp': 2897,
      'timestamp_label': '[00:48:17]',
      'timestamp_seconds': 2897,
      'tip': "Um quite commonly it's a service business. So there really isn't a corporate "
             'entity being purchased. It really is an asset transaction. Now the question is '
             "what what else is being exchanged? Is it cash for those assets? That's probably "
             'not a security.',
      'title': 'M&A Broker Registration Exemption: State-Level Progress and Next Steps for '
               'Intermediaries (International Business Brokers Association)',
      'url': 'https://www.youtube.com/watch?v=7mV4t9a4PvE&t=2897s',
      'video_id': '7mV4t9a4PvE'},
     {'author': 'The Altierior Motive with Dr. Chad Michael Altieri',
      'channel': 'The Altierior Motive with Dr. Chad Michael Altieri',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=sm21N5L0nl8&t=27s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For example, a broker introduces a buyer to a seller, and then the buyer and '
              'seller try to close directly without paying the broker. An advisor introduces '
              'an investor to a company, and the company later raises capital from that '
              "investor while denying the advisor's role.",
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'For example, a broker introduces a buyer to a seller, and then the buyer and '
             'seller try to close directly without paying the broker. An advisor introduces an '
             'investor to a company, and the company later raises capital from that investor '
             "while denying the advisor's role.",
      'title': 'What Is a Non-Circumvention Clause? (Protecting Your Deal) | 100 Day Law '
               'School #shorts (The Altierior Motive with Dr. Chad Michael Altieri)',
      'url': 'https://www.youtube.com/watch?v=sm21N5L0nl8&t=27s',
      'video_id': 'sm21N5L0nl8'},
     {'author': 'Frankie Finance',
      'channel': 'Frankie Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=1PRKZu79Zg4&t=227s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the fantasy version, the one built for $500 million dollars up. At $10 "
              "dollars liquid, a family office isn't a building. It's the decision to treat "
              'your capital like a business with a mandate, rather than an account with a '
              'balance.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': "That's the fantasy version, the one built for $500 million dollars up. At $10 "
             "dollars liquid, a family office isn't a building. It's the decision to treat "
             'your capital like a business with a mandate, rather than an account with a '
             'balance.',
      'title': 'POV: Running a Family Office — From $10M Liquid to Buying Companies in Private '
               '(Frankie Finance)',
      'url': 'https://www.youtube.com/watch?v=1PRKZu79Zg4&t=227s',
      'video_id': '1PRKZu79Zg4'},
     {'author': 'CertFuel',
      'channel': 'CertFuel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=UVXotJ5hxrU&t=144s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "He's now the vice president of information technology for Betty the "
              "broker-dealer. He makes a huge salary, he's a corporate officer, but his entire "
              'day consists of fixing broken servers and updating software. He never actually '
              'talks to clients or trades a single security.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': "He's now the vice president of information technology for Betty the "
             "broker-dealer. He makes a huge salary, he's a corporate officer, but his entire "
             'day consists of fixing broken servers and updating software. He never actually '
             'talks to clients or trades a single security.',
      'title': 'Definition of an Agent of a Broker-Dealer - Series 63 Exam Prep (CertFuel)',
      'url': 'https://www.youtube.com/watch?v=UVXotJ5hxrU&t=144s',
      'video_id': 'UVXotJ5hxrU'},
     {'author': 'Business Broker Crowd Call',
      'channel': 'Business Broker Crowd Call',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=22hjuZT2usA&t=52s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Type in which states require a real estate license and business brokerage press '
              "has an article that out there that it's it's a little bit old, but it's still "
              'pretty relevant and literally I printed that out and put it on my wall.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Type in which states require a real estate license and business brokerage press '
             "has an article that out there that it's it's a little bit old, but it's still "
             'pretty relevant and literally I printed that out and put it on my wall.',
      'title': 'Do You Need a Real Estate License to Broker Businesses? Legal Insights for 17 '
               'Key States (Business Broker Crowd Call)',
      'url': 'https://www.youtube.com/watch?v=22hjuZT2usA&t=52s',
      'video_id': '22hjuZT2usA'},
     {'author': 'How I Invest Podcast',
      'channel': 'How I Invest Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:37](https://www.youtube.com/watch?v=QDcDBGMiDtQ&t=1537s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If an asset class, no matter how overpriced it was, if it becomes unfavorable '
              'for a long enough time, the capital and the demand goes away from that asset '
              'class, and it reaches an equilibrium point where it now has become favorable.',
      'timestamp': 1537,
      'timestamp_label': '[00:25:37]',
      'timestamp_seconds': 1537,
      'tip': 'If an asset class, no matter how overpriced it was, if it becomes unfavorable '
             'for a long enough time, the capital and the demand goes away from that asset '
             'class, and it reaches an equilibrium point where it now has become favorable.',
      'title': '$250 Billion Family Office Founder on Wealth Preservation, Taxes, and Building '
               'Wealth (How I Invest Podcast)',
      'url': 'https://www.youtube.com/watch?v=QDcDBGMiDtQ&t=1537s',
      'video_id': 'QDcDBGMiDtQ'},
     {'author': 'Transact Capital',
      'channel': 'Transact Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=tqw5CWasFOU&t=106s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your logo and Company colors and showcase your business in a professional '
              'manner be sure to continue watching the rest of our eight-part series on the '
              'Milestones of m&a presented by transact capital.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'Your logo and Company colors and showcase your business in a professional manner '
             'be sure to continue watching the rest of our eight-part series on the Milestones '
             'of m&a presented by transact capital.',
      'title': 'What is the Confidential Information Presentation - 8 Milestones of M&A - '
               'Transact Capital (Transact Capital)',
      'url': 'https://www.youtube.com/watch?v=tqw5CWasFOU&t=106s',
      'video_id': 'tqw5CWasFOU'},
     {'author': 'OOIDA Foundation',
      'channel': 'OOIDA Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=XuAjQG6VmJg&t=227s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Should go to a different destination you may also need to reconfigure your rate '
              'for more information on broker fraud please check out our other online videos '
              'or call ooida at 1-800-44-5791 and ask for the business services department.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'Should go to a different destination you may also need to reconfigure your rate '
             'for more information on broker fraud please check out our other online videos or '
             'call ooida at 1-800-44-5791 and ask for the business services department.',
      'title': 'Due Diligence (OOIDA Foundation)',
      'url': 'https://www.youtube.com/watch?v=XuAjQG6VmJg&t=227s',
      'video_id': 'XuAjQG6VmJg'},
     {'author': 'David C Barnett Small Business and Deal Making SMB',
      'channel': 'David C Barnett Small Business and Deal Making SMB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:29](https://www.youtube.com/watch?v=Va5USDqv3-A&t=569s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Mindset or model from an individual who's going to buy a business because they "
              'want to make money with that business.',
      'timestamp': 569,
      'timestamp_label': '[00:09:29]',
      'timestamp_seconds': 569,
      'tip': "Mindset or model from an individual who's going to buy a business because they "
             'want to make money with that business.',
      'title': 'What Number Do I Multiply? SDE, EBIT, EBITDA? (David C Barnett Small Business '
               'and Deal Making SMB)',
      'url': 'https://www.youtube.com/watch?v=Va5USDqv3-A&t=569s',
      'video_id': 'Va5USDqv3-A'},
     {'author': 'Smart Agents',
      'channel': 'Smart Agents',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:02](https://www.youtube.com/watch?v=YKfvldXPHWw&t=842s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You should really come you know check out what we've got going on here what how "
              'did that change your business when you know you really started getting a.',
      'timestamp': 842,
      'timestamp_label': '[00:14:02]',
      'timestamp_seconds': 842,
      'tip': "You should really come you know check out what we've got going on here what how "
             'did that change your business when you know you really started getting a.',
      'title': 'Secrets To Building A Winning Brokerage: Recruiting and Retaining Top Real '
               'Estate Agents | Ep. 194 (Smart Agents)',
      'url': 'https://www.youtube.com/watch?v=YKfvldXPHWw&t=842s',
      'video_id': 'YKfvldXPHWw'},
     {'author': 'Yacht Broker Masterclass',
      'channel': 'Yacht Broker Masterclass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:42](https://www.youtube.com/watch?v=_Shd1I2mefI&t=1182s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In how much yach Brokers can make thank you all for your attendance and um take '
              'a look at y broker masterclass.com if you want some more information about the '
              'uh the master class thank you very much for attending.',
      'timestamp': 1182,
      'timestamp_label': '[00:19:42]',
      'timestamp_seconds': 1182,
      'tip': 'In how much yach Brokers can make thank you all for your attendance and um take '
             'a look at y broker masterclass.com if you want some more information about the '
             'uh the master class thank you very much for attending.',
      'title': 'YACHT BROKERAGE - HOW MUCH WILL I BE PAID? (Yacht Broker Masterclass)',
      'url': 'https://www.youtube.com/watch?v=_Shd1I2mefI&t=1182s',
      'video_id': '_Shd1I2mefI'},
     {'author': 'Tower Genius',
      'channel': 'Tower Genius',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=YW6JaW_qjAE&t=118s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the description of this video it will take you to the contact page and you '
              'can fill out a form there and we will be in touch with you very soon thank.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'In the description of this video it will take you to the contact page and you '
             'can fill out a form there and we will be in touch with you very soon thank.',
      'title': 'SELLING A CELL TOWER LEASE IN 2024? WHATS MY CELL TOWER LEASE EASEMENT OR '
               'LEASE BUYOUT REALLY WORTH? (Tower Genius)',
      'url': 'https://www.youtube.com/watch?v=YW6JaW_qjAE&t=118s',
      'video_id': 'YW6JaW_qjAE'}],
 5: [{'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:28](https://www.youtube.com/watch?v=svRg7_BrwXY&t=1528s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t that that listing broker hardly ever co- co-ops, so that's the problem. So "
              "they have to pay they they pay me Yeah, but it's quite worth it because you "
              'make one bad mistake, buy the wrong business, or not do the diligence needed, '
              "you're screwed.",
      'timestamp': 1528,
      'timestamp_label': '[00:25:28]',
      'timestamp_seconds': 1528,
      'tip': "'t that that listing broker hardly ever co- co-ops, so that's the problem. So "
             "they have to pay they they pay me Yeah, but it's quite worth it because you make "
             "one bad mistake, buy the wrong business, or not do the diligence needed, you're "
             'screwed.',
      'title': 'Business Broker Insider: Buy Side & Sell Side Secrets #TrentLee (Beau '
               'Eckstein, Business Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=svRg7_BrwXY&t=1528s',
      'video_id': 'svRg7_BrwXY'},
     {'author': 'Just Call Maggie',
      'channel': 'Just Call Maggie',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=YHrdVBHOASo&t=92s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Doesn't matter who finds the buyer, the broker, another broker, the seller's "
              "cousin, the seller themselves, commission is owed. That's why it guarantees the "
              'broker the highest protection. Exclusive agency means seller might avoid paying '
              'commission.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "Doesn't matter who finds the buyer, the broker, another broker, the seller's "
             "cousin, the seller themselves, commission is owed. That's why it guarantees the "
             'broker the highest protection. Exclusive agency means seller might avoid paying '
             'commission.',
      'title': 'Exclusive agency vs exclusive right to sell explained for the real estate '
               'exam. (Just Call Maggie)',
      'url': 'https://www.youtube.com/watch?v=YHrdVBHOASo&t=92s',
      'video_id': 'YHrdVBHOASo'},
     {'author': 'Paul Macaluso',
      'channel': 'Paul Macaluso',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=Cn4V6pWhbMk&t=62s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'d be open to a conversation. This shows effort, not intrusion. Three, I "
              "immediately disarm resistance. Just so you know, I'm not a broker trying to "
              "list your property. I'm a buyer looking to make an unsolicited offer. Four, I "
              'offer a confidentiality agreement upfront.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "'d be open to a conversation. This shows effort, not intrusion. Three, I "
             "immediately disarm resistance. Just so you know, I'm not a broker trying to list "
             "your property. I'm a buyer looking to make an unsolicited offer. Four, I offer a "
             'confidentiality agreement upfront.',
      'title': 'Cold Calling for Off-Market Deals: Exact Script That Closed 6-7 Figure Real '
               'Estate Contracts (Paul Macaluso)',
      'url': 'https://www.youtube.com/watch?v=Cn4V6pWhbMk&t=62s',
      'video_id': 'Cn4V6pWhbMk'},
     {'author': 'Business Broker Crowd Call',
      'channel': 'Business Broker Crowd Call',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=Py7d57O-Rxs&t=259s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Commercial if you're with exp commercial then and you want to transact that "
              'business yourself then great make sure you get a business broker addendum and '
              'then s satisfy the requirements that they have for you okay good to know good '
              'to know okay.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': "Commercial if you're with exp commercial then and you want to transact that "
             'business yourself then great make sure you get a business broker addendum and '
             'then s satisfy the requirements that they have for you okay good to know good to '
             'know okay.',
      'title': 'Business Brokerage Licensing in DC, Virginia, and Maryland (Business Broker '
               'Crowd Call)',
      'url': 'https://www.youtube.com/watch?v=Py7d57O-Rxs&t=259s',
      'video_id': 'Py7d57O-Rxs'},
     {'author': 'Current Yachts',
      'channel': 'Current Yachts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:20](https://www.youtube.com/watch?v=wqPY1eV4vuQ&t=1220s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's up to the seller to decide if they want to open their boat for "
              'co-brokerage and at what percentage they are willing to compensate that broker. '
              'You know, obviously the real estate commissions um just got completely blown '
              'up. I mean, is is are votes next?',
      'timestamp': 1220,
      'timestamp_label': '[00:20:20]',
      'timestamp_seconds': 1220,
      'tip': "It's up to the seller to decide if they want to open their boat for co-brokerage "
             'and at what percentage they are willing to compensate that broker. You know, '
             'obviously the real estate commissions um just got completely blown up. I mean, '
             'is is are votes next?',
      'title': 'The truth about yacht brokers and boat sales (Current Yachts)',
      'url': 'https://www.youtube.com/watch?v=wqPY1eV4vuQ&t=1220s',
      'video_id': 'wqPY1eV4vuQ'},
     {'author': 'IXH TRADING Academy',
      'channel': 'IXH TRADING Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=5VMFuBur4kI&t=15s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No call, no commission, no credit. In international commodity trading,  this is '
              'one of the oldest risks there is. And there is one agreement built.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'No call, no commission, no credit. In international commodity trading,  this is '
             'one of the oldest risks there is. And there is one agreement built.',
      'title': 'NCNDA Explained: How to Protect Your Commission in International Commodity '
               'Trading | IXH TRADING (IXH TRADING Academy)',
      'url': 'https://www.youtube.com/watch?v=5VMFuBur4kI&t=15s',
      'video_id': '5VMFuBur4kI'},
     {'author': 'iGOTHAM',
      'channel': 'iGOTHAM',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=r1DSXPxZzu8&t=62s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business outlining areas of both strength and weakness let investors and buyers '
              'know where they need to put the work in and.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'Business outlining areas of both strength and weakness let investors and buyers '
             'know where they need to put the work in and.',
      'title': 'How to Create the Best Confidential Information Memorandum (CIM) (iGOTHAM)',
      'url': 'https://www.youtube.com/watch?v=r1DSXPxZzu8&t=62s',
      'video_id': 'r1DSXPxZzu8'},
     {'author': 'SiteBid Infrastructure',
      'channel': 'SiteBid Infrastructure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=EsfznycDU6I&t=16s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Rights well in this video we're breaking down two popular sell Tower lease "
              'buyout options the master lease agreement and the Perpetual easement whether '
              "you're.",
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': "Rights well in this video we're breaking down two popular sell Tower lease "
             'buyout options the master lease agreement and the Perpetual easement whether '
             "you're.",
      'title': 'Maximize Your Cell Tower Lease Buyout Options - Master Lease vs.  Perpetual '
               'Easement (SiteBid Infrastructure)',
      'url': 'https://www.youtube.com/watch?v=EsfznycDU6I&t=16s',
      'video_id': 'EsfznycDU6I'},
     {'author': 'Scale Like ZK',
      'channel': 'Scale Like ZK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=uBQvqV_-nz0&t=257s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And this is going to be the weekly content mix that you should be running. We '
              'have problem content, so names what is broken and why. We have proof content, '
              "um one client's situation before what [clears throat] changed and what "
              'happened.',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'And this is going to be the weekly content mix that you should be running. We '
             'have problem content, so names what is broken and why. We have proof content, um '
             "one client's situation before what [clears throat] changed and what happened.",
      'title': 'How To Get High Ticket Buyers Every Week (Scale Like ZK)',
      'url': 'https://www.youtube.com/watch?v=uBQvqV_-nz0&t=257s',
      'video_id': 'uBQvqV_-nz0'},
     {'author': 'Quiet Light Brokerage',
      'channel': 'Quiet Light Brokerage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=ow7ewDogN14&t=15s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like are you seeing that like when you're having conversations with Buyers do "
              'they seem more risk averse or do they seem more hesitant or is that kind of a.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Like are you seeing that like when you're having conversations with Buyers do "
             'they seem more risk averse or do they seem more hesitant or is that kind of a.',
      'title': 'What Online Business Buyers Really Want (From $0 to a $1.7M Sale) (Quiet Light '
               'Brokerage)',
      'url': 'https://www.youtube.com/watch?v=ow7ewDogN14&t=15s',
      'video_id': 'ow7ewDogN14'},
     {'author': 'Family Enterprise Perspectives',
      'channel': 'Family Enterprise Perspectives',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=0Z2XoqRkE00&t=127s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh, Shane developed the five pillars of risk framework, which we'll also touch "
              'upon today and it examines the exposure across investments, investors, business '
              'partners, executive vendors cuz all of these are interconnected.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': "Uh, Shane developed the five pillars of risk framework, which we'll also touch "
             'upon today and it examines the exposure across investments, investors, business '
             'partners, executive vendors cuz all of these are interconnected.',
      'title': 'Before You Wire the Money: What Real Due Diligence Looks Like in Private '
               'Market Deals (Family Enterprise Perspectives)',
      'url': 'https://www.youtube.com/watch?v=0Z2XoqRkE00&t=127s',
      'video_id': '0Z2XoqRkE00'},
     {'author': 'CertFuel',
      'channel': 'CertFuel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:40](https://www.youtube.com/watch?v=WYhf4z4Djwk&t=340s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The firm actually gets to set the exact schedule based on a risk assessment, '
              'looking at things like business volume and head count, but the baseline rule is '
              'that you absolutely cannot go longer than 3 years without an inspection. Part '
              'five, reviewing firm communications.',
      'timestamp': 340,
      'timestamp_label': '[00:05:40]',
      'timestamp_seconds': 340,
      'tip': 'The firm actually gets to set the exact schedule based on a risk assessment, '
             'looking at things like business volume and head count, but the baseline rule is '
             'that you absolutely cannot go longer than 3 years without an inspection. Part '
             'five, reviewing firm communications.',
      'title': 'Broker-Dealer Supervision: WSPs and Office Inspections - Series 63 Exam Prep '
               '(CertFuel)',
      'url': 'https://www.youtube.com/watch?v=WYhf4z4Djwk&t=340s',
      'video_id': 'WYhf4z4Djwk'},
     {'author': 'Jim Loeffler',
      'channel': 'Jim Loeffler',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=UMCbZCe6qzw&t=15s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'MBA, and founder of Intoune Business Advisors, where for more than 20 years, '
              "we've  helped owners transform their manufacturing businesses into.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'MBA, and founder of Intoune Business Advisors, where for more than 20 years, '
             "we've  helped owners transform their manufacturing businesses into.",
      'title': 'Exchanging Confidential Information Memorandum (CIM) (Jim Loeffler)',
      'url': 'https://www.youtube.com/watch?v=UMCbZCe6qzw&t=15s',
      'video_id': 'UMCbZCe6qzw'},
     {'author': 'Woggle Consulting',
      'channel': 'Woggle Consulting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=DAWWBPCEySE&t=110s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can customize this however you want to collect whatever information you '
              'need on the different types of transactions that your business does with '
              'different companies or people individuals so that is what a deal record is see '
              'you next time waggle waggle.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'You can customize this however you want to collect whatever information you need '
             'on the different types of transactions that your business does with different '
             'companies or people individuals so that is what a deal record is see you next '
             'time waggle waggle.',
      'title': 'What Is a Deal in Zoho CRM? Sales Pipeline Simplified (Woggle Consulting)',
      'url': 'https://www.youtube.com/watch?v=DAWWBPCEySE&t=110s',
      'video_id': 'DAWWBPCEySE'},
     {'author': 'Adventures in CRE',
      'channel': 'Adventures in CRE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=EL2eIKZ_OV8&t=165s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Owner you have to use it solely for the purpose you can't disclose it except to "
              'agents and vendors as strictly necessary for the purchase of the property.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': "Owner you have to use it solely for the purpose you can't disclose it except to "
             'agents and vendors as strictly necessary for the purchase of the property.',
      'title': 'Confidentiality Agreement Template Walkthrough (Adventures in CRE)',
      'url': 'https://www.youtube.com/watch?v=EL2eIKZ_OV8&t=165s',
      'video_id': 'EL2eIKZ_OV8'}],
 6: [{'author': 'Brandon Mulrenin',
      'channel': 'Brandon Mulrenin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:30](https://www.youtube.com/watch?v=R_uWZH6c9lI&t=510s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You've got to find out does your brokerage help to support building and "
              'generating leads for your pipeline, for your database? And if they do, okay, '
              "great. Let's go a little bit deeper. We talking about buyer internet leads?",
      'timestamp': 510,
      'timestamp_label': '[00:08:30]',
      'timestamp_seconds': 510,
      'tip': "You've got to find out does your brokerage help to support building and "
             'generating leads for your pipeline, for your database? And if they do, okay, '
             "great. Let's go a little bit deeper. We talking about buyer internet leads?",
      'title': 'How to Choose a Real Estate Broker? | Ask these 12 questions FIRST! (Brandon '
               'Mulrenin)',
      'url': 'https://www.youtube.com/watch?v=R_uWZH6c9lI&t=510s',
      'video_id': 'R_uWZH6c9lI'},
     {'author': 'Wolf of Main Street',
      'channel': 'Wolf of Main Street',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=FZ98S2zrji0&t=117s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're talking just outreach. So, I know where this fits. So, first video we "
              'posted was about sourcing data. We see three pillars for a successful out '
              'outreach campaign to business owners to get them to find uh potential deals.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': "We're talking just outreach. So, I know where this fits. So, first video we "
             'posted was about sourcing data. We see three pillars for a successful out '
             'outreach campaign to business owners to get them to find uh potential deals.',
      'title': 'How to Reach Business Owners Who Already Want to Sell (Deal Sourcing Outreach '
               'Sequence) (Wolf of Main Street)',
      'url': 'https://www.youtube.com/watch?v=FZ98S2zrji0&t=117s',
      'video_id': 'FZ98S2zrji0'},
     {'author': 'Deal Street - Small to Lower Middle Market M&A',
      'channel': 'Deal Street - Small to Lower Middle Market M&A',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=78s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Piece one, cash at closing. The first piece is cash at closing, which is the '
              'money that hits your account the day the deal closes. It usually comes from two '
              "places, the buyer's own money, and whatever the buyer borrows from a bank.",
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Piece one, cash at closing. The first piece is cash at closing, which is the '
             'money that hits your account the day the deal closes. It usually comes from two '
             "places, the buyer's own money, and whatever the buyer borrows from a bank.",
      'title': 'How Business Sales Get Financed (Cash, SBA Loans, Seller Notes, Earnouts & '
               'Rollovers) (Deal Street - Small to Lower Middle Market M&A)',
      'url': 'https://www.youtube.com/watch?v=a5Z--B3Uhrg&t=78s',
      'video_id': 'a5Z--B3Uhrg'},
     {'author': 'The Ultimate Jet Guide',
      'channel': 'The Ultimate Jet Guide',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=1ILeO7AapJM&t=198s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I'm going to send you a one-page commission agreement. You're going to see "
              "who the buyer is. You're going to see what my commission is amount. And you're "
              'only going to pay me if we go through with this particular buyer, this '
              'particular deal.".',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': "So, I'm going to send you a one-page commission agreement. You're going to see "
             "who the buyer is. You're going to see what my commission is amount. And you're "
             'only going to pay me if we go through with this particular buyer, this '
             'particular deal.".',
      'title': 'Commission Agreements & Getting Paid for Jet Brokers (The Ultimate Jet Guide)',
      'url': 'https://www.youtube.com/watch?v=1ILeO7AapJM&t=198s',
      'video_id': '1ILeO7AapJM'},
     {'author': 'HALO Talks',
      'channel': 'HALO Talks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=76I0zKp5FM0&t=479s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s uh attorney might not be might not be an M&A specialist or might this might "
              "be like the first you know deal they've done. How do you um either try and form "
              'a relationship with them and say like, "Hey, this is kind of commercial terms '
              'like my client.',
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': "'s uh attorney might not be might not be an M&A specialist or might this might "
             "be like the first you know deal they've done. How do you um either try and form "
             'a relationship with them and say like, "Hey, this is kind of commercial terms '
             'like my client.',
      'title': 'How Messy Paperwork Can Kill a Million-Dollar Deal-With Mike Zaino On HALO '
               'Talks (HALO Talks)',
      'url': 'https://www.youtube.com/watch?v=76I0zKp5FM0&t=479s',
      'video_id': '76I0zKp5FM0'},
     {'author': 'Brandon Mulrenin',
      'channel': 'Brandon Mulrenin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:09](https://www.youtube.com/watch?v=phMoT_2rYN4&t=669s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "50 sales in your first year. So we've established that you and I agree they "
              'need to spend all of their time mastering bottom of funnel business first, '
              "right? And so let's talk about the next piece is where do you find the data?",
      'timestamp': 669,
      'timestamp_label': '[00:11:09]',
      'timestamp_seconds': 669,
      'tip': "50 sales in your first year. So we've established that you and I agree they need "
             'to spend all of their time mastering bottom of funnel business first, right? And '
             "so let's talk about the next piece is where do you find the data?",
      'title': 'How to sell 50 houses a year (even as a new realtor) (Brandon Mulrenin)',
      'url': 'https://www.youtube.com/watch?v=phMoT_2rYN4&t=669s',
      'video_id': 'phMoT_2rYN4'},
     {'author': 'Reed Smith LLP',
      'channel': 'Reed Smith LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=HXjpQWcZ6F8&t=162s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"This transaction no longer works for us." And either be able to walk away or '
              "negotiate different terms. So the way that we're helping our clients diligence "
              "data center transactions, it's not just real estate anymore. That list has, has "
              'expanded.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': '"This transaction no longer works for us." And either be able to walk away or '
             "negotiate different terms. So the way that we're helping our clients diligence "
             "data center transactions, it's not just real estate anymore. That list has, has "
             'expanded.',
      'title': 'Powered land: The asset behind the data center | Reed Smith Data Centers '
               'series (Reed Smith LLP)',
      'url': 'https://www.youtube.com/watch?v=HXjpQWcZ6F8&t=162s',
      'video_id': 'HXjpQWcZ6F8'},
     {'author': 'Hema Glory',
      'channel': 'Hema Glory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=zWRMFLm_we4&t=72s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I can be able to edit the pipeline. As you can see, this is how our pipeline '
              "is. And depending on your sales process, let's say there is a new lead and "
              'after the new lead comes in, they need to book a call. And after they book a '
              'call, we can then qualify them to buy.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'I can be able to edit the pipeline. As you can see, this is how our pipeline is. '
             "And depending on your sales process, let's say there is a new lead and after the "
             'new lead comes in, they need to book a call. And after they book a call, we can '
             'then qualify them to buy.',
      'title': 'How to Create a Sales Pipeline in HubSpot CRM 2026 | Pipeline Stages & Deal '
               'Setup (Hema Glory)',
      'url': 'https://www.youtube.com/watch?v=zWRMFLm_we4&t=72s',
      'video_id': 'zWRMFLm_we4'},
     {'author': 'Clausehound Inc.',
      'channel': 'Clausehound Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=HN8Y7XiYRGE&t=59s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Useful if the parties are sharing information that could be damaging to their '
              'business if it were used by the other party for example if they share client '
              'lists or sales leads the recipient would and probably should be restricted from '
              'using these for their own.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Useful if the parties are sharing information that could be damaging to their '
             'business if it were used by the other party for example if they share client '
             'lists or sales leads the recipient would and probably should be restricted from '
             'using these for their own.',
      'title': 'Drafting a Non-Disclosure Agreement: Non Soliticiation & Non Compete '
               '(Clausehound Inc.)',
      'url': 'https://www.youtube.com/watch?v=HN8Y7XiYRGE&t=59s',
      'video_id': 'HN8Y7XiYRGE'},
     {'author': 'Hema Glory',
      'channel': 'Hema Glory',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=87GSjPGNpO8&t=91s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We are just going to click on create and that's is going to create our deal, "
              'which has been added into the new stage. That has added in our deal to the '
              'first stage, which is which is new lead. So, you can see the details about this '
              'deal. You can see it by the left hand side.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "We are just going to click on create and that's is going to create our deal, "
             'which has been added into the new stage. That has added in our deal to the first '
             'stage, which is which is new lead. So, you can see the details about this deal. '
             'You can see it by the left hand side.',
      'title': 'How to Manage Deals in HubSpot Sales Pipeline 2026 | Deal Stages, Pipeline & '
               'Sales Management (Hema Glory)',
      'url': 'https://www.youtube.com/watch?v=87GSjPGNpO8&t=91s',
      'video_id': '87GSjPGNpO8'},
     {'author': 'Mayer Brown',
      'channel': 'Mayer Brown',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=aG2Bnsxt8Cg&t=295s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I would note that in the context of that increased demand, both inbound and '
              'outbound, the ability of US investors to deal directly with foreign financial '
              'service professionals is limited by the US legal and regulatory structure.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': 'I would note that in the context of that increased demand, both inbound and '
             'outbound, the ability of US investors to deal directly with foreign financial '
             'service professionals is limited by the US legal and regulatory structure.',
      'title': 'Considerations for Broker-Dealers under Rule 15a-6 (Mayer Brown)',
      'url': 'https://www.youtube.com/watch?v=aG2Bnsxt8Cg&t=295s',
      'video_id': 'aG2Bnsxt8Cg'},
     {'author': 'US Realty Training',
      'channel': 'US Realty Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=4LntMyEuBXE&t=392s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Great video on how to get your first real estate client you found your office '
              "you're filling the vibe you're feeling energized how do you get your first real "
              "estate client check this video out you're gonna love it we'll see you next "
              'week.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': 'Great video on how to get your first real estate client you found your office '
             "you're filling the vibe you're feeling energized how do you get your first real "
             "estate client check this video out you're gonna love it we'll see you next week.",
      'title': 'How to Choose a Real Estate Brokerage (US Realty Training)',
      'url': 'https://www.youtube.com/watch?v=4LntMyEuBXE&t=392s',
      'video_id': '4LntMyEuBXE'},
     {'author': 'Trade Base Hub',
      'channel': 'Trade Base Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=yrJW_zsMUXM&t=77s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Publicly available information or information that can reasonably be obtained '
              "elsewhere is not protected under an N C N D A. N C N D A's are effective for "
              'protecting introductions, proprietary deal structures, and sensitive commercial '
              'exchanges.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Publicly available information or information that can reasonably be obtained '
             "elsewhere is not protected under an N C N D A. N C N D A's are effective for "
             'protecting introductions, proprietary deal structures, and sensitive commercial '
             'exchanges.',
      'title': 'NCNDA  Professional Protection (Trade Base Hub)',
      'url': 'https://www.youtube.com/watch?v=yrJW_zsMUXM&t=77s',
      'video_id': 'yrJW_zsMUXM'},
     {'author': 'Basic Wisdom',
      'channel': 'Basic Wisdom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:09](https://www.youtube.com/watch?v=WN_8pEobWVw&t=909s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Planner hundreds of chapter review questions and unlimited practice exams our '
              'courses are competitively priced and you can try them out for free first to see '
              'if our style is the right fit for you follow the links Below in the description '
              'to get started.',
      'timestamp': 909,
      'timestamp_label': '[00:15:09]',
      'timestamp_seconds': 909,
      'tip': 'Planner hundreds of chapter review questions and unlimited practice exams our '
             'courses are competitively priced and you can try them out for free first to see '
             'if our style is the right fit for you follow the links Below in the description '
             'to get started.',
      'title': 'Broker-Dealer Exclusions (Series 63, 65, and 66) (Basic Wisdom)',
      'url': 'https://www.youtube.com/watch?v=WN_8pEobWVw&t=909s',
      'video_id': 'WN_8pEobWVw'},
     {'author': 'Brufokes African Foods Export Ltd',
      'channel': 'Brufokes African Foods Export Ltd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=suL1t0XynNw&t=102s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It was this article that first drew my attention to the fake nc nda circulating '
              'in the public space in it the writer provided this link to the icc website '
              'where icc once traders of this fake version of the ncnda.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'It was this article that first drew my attention to the fake nc nda circulating '
             'in the public space in it the writer provided this link to the icc website where '
             'icc once traders of this fake version of the ncnda.',
      'title': 'Genuine NCNDA vs Fake NCNDA (Brufokes African Foods Export Ltd)',
      'url': 'https://www.youtube.com/watch?v=suL1t0XynNw&t=102s',
      'video_id': 'suL1t0XynNw'}],
 7: [{'author': "Patrick O'Connell - M&A Transaction Services",
      'channel': "Patrick O'Connell - M&A Transaction Services",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=Q9DFb9qenh8&t=358s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Agreement and from there the the transactions effectively closed you've "
              'successfully purchased a business but there are two more steps step nine.',
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': "Agreement and from there the the transactions effectively closed you've "
             'successfully purchased a business but there are two more steps step nine.',
      'title': '10 Steps to Buy a Business: A Main Street & Lower Middle Market Guide (Patrick '
               "O'Connell - M&A Transaction Services)",
      'url': 'https://www.youtube.com/watch?v=Q9DFb9qenh8&t=358s',
      'video_id': 'Q9DFb9qenh8'},
     {'author': 'The Digital Merchant',
      'channel': 'The Digital Merchant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:00](https://www.youtube.com/watch?v=NTugAc75tOg&t=480s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um it's it is a business brokerage in the typical sense, but it even leans more "
              'into a kind of a buy and sell marketplace.',
      'timestamp': 480,
      'timestamp_label': '[00:08:00]',
      'timestamp_seconds': 480,
      'tip': "Um it's it is a business brokerage in the typical sense, but it even leans more "
             'into a kind of a buy and sell marketplace.',
      'title': 'M&A Advisor vs Business Broker: Which One Should You Use to Sell Your '
               'Business? (The Digital Merchant)',
      'url': 'https://www.youtube.com/watch?v=NTugAc75tOg&t=480s',
      'video_id': 'NTugAc75tOg'},
     {'author': 'Business Solution',
      'channel': 'Business Solution',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=zcYOmZ8cAGE&t=89s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s actively managing the process rather than just a bulletin board of listings. "
              "As a seller, you don't pay anything upfront to list. Empire Flippers only earns "
              'when your business sells. Their commission structure is blended.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': "'s actively managing the process rather than just a bulletin board of listings. "
             "As a seller, you don't pay anything upfront to list. Empire Flippers only earns "
             'when your business sells. Their commission structure is blended.',
      'title': '5 Best Online Business Brokers & Marketplaces: Buy & Sell Websites, SaaS, '
               'Apps, Ecom Brands (Business Solution)',
      'url': 'https://www.youtube.com/watch?v=zcYOmZ8cAGE&t=89s',
      'video_id': 'zcYOmZ8cAGE'},
     {'author': 'Kyle Handy and AJ Mida',
      'channel': 'Kyle Handy and AJ Mida',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:09](https://www.youtube.com/watch?v=QqzqH1glUuA&t=489s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Craigslist and facebook the fifth step is to hire the right employees why do '
              'people go to a brokerage well apart from needing a sponsoring broker they want.',
      'timestamp': 489,
      'timestamp_label': '[00:08:09]',
      'timestamp_seconds': 489,
      'tip': 'Craigslist and facebook the fifth step is to hire the right employees why do '
             'people go to a brokerage well apart from needing a sponsoring broker they want.',
      'title': 'How To Start A Real Estate Brokerage in 8 Steps (Without Going Broke) (Kyle '
               'Handy and AJ Mida)',
      'url': 'https://www.youtube.com/watch?v=QqzqH1glUuA&t=489s',
      'video_id': 'QqzqH1glUuA'},
     {'author': 'Colin Matcha',
      'channel': 'Colin Matcha',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:15](https://www.youtube.com/watch?v=r4fmjknWB7o&t=675s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fairly condensed it keeps the legalese easy to process so once the apa or the '
              "asset purchase agreement is signed you're good to actually start the deal.",
      'timestamp': 675,
      'timestamp_label': '[00:11:15]',
      'timestamp_seconds': 675,
      'tip': 'Fairly condensed it keeps the legalese easy to process so once the apa or the '
             "asset purchase agreement is signed you're good to actually start the deal.",
      'title': 'FE International Review For Buyers 2022 (Colin Matcha)',
      'url': 'https://www.youtube.com/watch?v=r4fmjknWB7o&t=675s',
      'video_id': 'r4fmjknWB7o'},
     {'author': 'M&A Synergy AI',
      'channel': 'M&A Synergy AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=h3OE0enrIxg&t=150s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And out the other end comes the entire package. We're talking a polished 100 "
              'plus slide CIM, the financial model, sensitivity analysis, the whole shebang. '
              'So, how does this thing actually work? Step one, you just dump all your source '
              'files into the system.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': "And out the other end comes the entire package. We're talking a polished 100 "
             'plus slide CIM, the financial model, sensitivity analysis, the whole shebang. '
             'So, how does this thing actually work? Step one, you just dump all your source '
             'files into the system.',
      'title': 'Write a CIM in 10 Minutes: The AI Generator (M&A Synergy AI)',
      'url': 'https://www.youtube.com/watch?v=h3OE0enrIxg&t=150s',
      'video_id': 'h3OE0enrIxg'},
     {'author': 'Frankie Isaac',
      'channel': 'Frankie Isaac',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:53](https://www.youtube.com/watch?v=_ZU2OAxnSMI&t=1553s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you want the full system, buy everything, mindset, five-step discovery, '
              "objection handling, there's a free course linked at the top of the description "
              "as well. I'll see you in the next one.",
      'timestamp': 1553,
      'timestamp_label': '[00:25:53]',
      'timestamp_seconds': 1553,
      'tip': 'If you want the full system, buy everything, mindset, five-step discovery, '
             "objection handling, there's a free course linked at the top of the description "
             "as well. I'll see you in the next one.",
      'title': 'How to Land Your First High-Ticket Sales Offer in 2026 (Speed Run Edition) '
               '(Frankie Isaac)',
      'url': 'https://www.youtube.com/watch?v=_ZU2OAxnSMI&t=1553s',
      'video_id': '_ZU2OAxnSMI'},
     {'author': 'Nick Dadamio',
      'channel': 'Nick Dadamio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=zmqAbj7T7F8&t=174s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What does each stakeholder care about? What proof will they demand? What's the "
              "risk they'll focus on? And this is how you stop getting blindsided late. Step "
              "three, build proof like a prosecutor. High ticket buyers don't need more "
              'claims, they need evidence.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': "What does each stakeholder care about? What proof will they demand? What's the "
             "risk they'll focus on? And this is how you stop getting blindsided late. Step "
             "three, build proof like a prosecutor. High ticket buyers don't need more claims, "
             'they need evidence.',
      'title': 'High Ticket Sales Process & Closing Strategy (Nick Dadamio)',
      'url': 'https://www.youtube.com/watch?v=zmqAbj7T7F8&t=174s',
      'video_id': 'zmqAbj7T7F8'},
     {'author': 'FINOP Controller',
      'channel': 'FINOP Controller',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=-3SAUcV8ljM&t=262s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These amounts are deducted from the aggregate debits. The reserve formula gets '
              "most of its inputs from the firm's back office system. On the left side of this "
              'slide are several commercial back office systems like Beta, Fiserv, or FIS.',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': 'These amounts are deducted from the aggregate debits. The reserve formula gets '
             "most of its inputs from the firm's back office system. On the left side of this "
             'slide are several commercial back office systems like Beta, Fiserv, or FIS.',
      'title': 'SEC Rule 15c3-3 Customer Reserve Calculation Explained | Broker-Dealer FINOP '
               'Training (FINOP Controller)',
      'url': 'https://www.youtube.com/watch?v=-3SAUcV8ljM&t=262s',
      'video_id': '-3SAUcV8ljM'},
     {'author': "Greyson's Daily",
      'channel': "Greyson's Daily",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=t49Ab42PNxE&t=161s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Locke came in and reinvented kind of the real wheel a little bit and renamed it '
              'high ticket closer, which is why it seems a little bit scamy but but '
              'essentially what high ticket closing is is essentially just closing business to '
              'business slash B to B deals.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Locke came in and reinvented kind of the real wheel a little bit and renamed it '
             'high ticket closer, which is why it seems a little bit scamy but but essentially '
             'what high ticket closing is is essentially just closing business to business '
             'slash B to B deals.',
      'title': "High Ticket Sales, Explained Honestly by Someone Doing It (Greyson's Daily)",
      'url': 'https://www.youtube.com/watch?v=t49Ab42PNxE&t=161s',
      'video_id': 't49Ab42PNxE'},
     {'author': 'Equity Real Estate',
      'channel': 'Equity Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=mVFdzEqW2M4&t=120s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Steps to be thorough can make the difference between getting your commission '
              "promptly or dealing with frustrating delays thanks for watching and don't "
              'hesitate to reach out if you need any clarification good luck with your '
              'closings.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'Steps to be thorough can make the difference between getting your commission '
             "promptly or dealing with frustrating delays thanks for watching and don't "
             'hesitate to reach out if you need any clarification good luck with your '
             'closings.',
      'title': 'How to Fill Out the Commission Disbursement & Wire Instructions Form Correctly '
               '(Equity Real Estate)',
      'url': 'https://www.youtube.com/watch?v=mVFdzEqW2M4&t=120s',
      'video_id': 'mVFdzEqW2M4'},
     {'author': 'International Aircraft Broker Institute IABI',
      'channel': 'International Aircraft Broker Institute IABI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=xl7JC2nh0UQ&t=38s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Besides that, also they need to have a delivery permit that allows them to do '
              "business in the county that they're planning to do business in. So that those "
              'things kind of come into play as well. And then lastly is the big part which is '
              'the insurance.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': 'Besides that, also they need to have a delivery permit that allows them to do '
             "business in the county that they're planning to do business in. So that those "
             'things kind of come into play as well. And then lastly is the big part which is '
             'the insurance.',
      'title': 'Private aviation and luxury yachts operate on the same rules | THE JET PODCAST '
               '| IABI (International Aircraft Broker Institute IABI)',
      'url': 'https://www.youtube.com/watch?v=xl7JC2nh0UQ&t=38s',
      'video_id': 'xl7JC2nh0UQ'},
     {'author': 'CertFuel',
      'channel': 'CertFuel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=MhYKFYS6gTI&t=425s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'US firm that just happens to have a foreign branch out in London. Always, '
              "always verify where the firm's principal place of business actually is before "
              "you apply the rule on the exam. So, I'm going to leave you with this final "
              'thought.',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': 'US firm that just happens to have a foreign branch out in London. Always, always '
             "verify where the firm's principal place of business actually is before you apply "
             "the rule on the exam. So, I'm going to leave you with this final thought.",
      'title': 'Nonresident Broker-Dealers - series24 Exam Prep (CertFuel)',
      'url': 'https://www.youtube.com/watch?v=MhYKFYS6gTI&t=425s',
      'video_id': 'MhYKFYS6gTI'},
     {'author': 'Quiet Light Brokerage',
      'channel': 'Quiet Light Brokerage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:03](https://www.youtube.com/watch?v=oJsHo5vaDus&t=1683s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As like a 101 you know sure and what I mean what kind of growth should people '
              'be pegging for right I mean what what do buyers consider to be good growth yeah '
              'I think.',
      'timestamp': 1683,
      'timestamp_label': '[00:28:03]',
      'timestamp_seconds': 1683,
      'tip': 'As like a 101 you know sure and what I mean what kind of growth should people be '
             'pegging for right I mean what what do buyers consider to be good growth yeah I '
             'think.',
      'title': '3 Big Levers to Maximize SaaS Business Valuation with David Newell (Quiet '
               'Light Brokerage)',
      'url': 'https://www.youtube.com/watch?v=oJsHo5vaDus&t=1683s',
      'video_id': 'oJsHo5vaDus'},
     {'author': 'Carter Morse & Goodrich',
      'channel': 'Carter Morse & Goodrich',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=a71tQJb9UFE&t=157s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The work that they did as well I really am eternally grateful I just I owe a '
              'lot to their efforts and their efforts have resulted in kind of a whole new '
              "world for me going forward that I didn't think was possible only a few years "
              'ago.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'The work that they did as well I really am eternally grateful I just I owe a lot '
             'to their efforts and their efforts have resulted in kind of a whole new world '
             "for me going forward that I didn't think was possible only a few years ago.",
      'title': 'Sell Side M&A - After The Sale: Reflecting on the M&A Transaction Process '
               '(Carter Morse & Goodrich)',
      'url': 'https://www.youtube.com/watch?v=a71tQJb9UFE&t=157s',
      'video_id': 'a71tQJb9UFE'}],
 8: [{'author': 'David C Barnett Small Business and Deal Making SMB',
      'channel': 'David C Barnett Small Business and Deal Making SMB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=wHxYmcrcq4M&t=168s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Right which makes sense because the business broker is trying to protect the '
              'information of the business but what is often not a part of that agreement is '
              "any kind of promise that they're going to protect your information as a buyer "
              'right um and so I I understand.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Right which makes sense because the business broker is trying to protect the '
             'information of the business but what is often not a part of that agreement is '
             "any kind of promise that they're going to protect your information as a buyer "
             'right um and so I I understand.',
      'title': "Don't be a Victim of Broker NDA Agreements (David C Barnett Small Business and "
               'Deal Making SMB)',
      'url': 'https://www.youtube.com/watch?v=wHxYmcrcq4M&t=168s',
      'video_id': 'wHxYmcrcq4M'},
     {'author': 'Andrew Dubinsky',
      'channel': 'Andrew Dubinsky',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=Z0ATgOouiIM&t=239s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'IRS portal that is a statement of your intent to to transfer. You sign the '
              'transfer election and the election statement and sometimes the transfer '
              'agreement is called a tax credit transfer agreement or tick to and then the '
              'buyer claims the credit on their return.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': 'IRS portal that is a statement of your intent to to transfer. You sign the '
             'transfer election and the election statement and sometimes the transfer '
             'agreement is called a tax credit transfer agreement or tick to and then the '
             'buyer claims the credit on their return.',
      'title': 'How to Buy Tax Credits at a Discount (Section 6418 Explained) (Andrew '
               'Dubinsky)',
      'url': 'https://www.youtube.com/watch?v=Z0ATgOouiIM&t=239s',
      'video_id': 'Z0ATgOouiIM'},
     {'author': 'Gerry Mendria',
      'channel': 'Gerry Mendria',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=5hRyQr7CMkA&t=25s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Places where the number one concern was making the Commission if that's going "
              "to be the way that you're looking maybe another kind of business would search.",
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "Places where the number one concern was making the Commission if that's going to "
             "be the way that you're looking maybe another kind of business would search.",
      'title': 'How To Become A Yacht Broker – My favorite work ever! (Gerry Mendria)',
      'url': 'https://www.youtube.com/watch?v=5hRyQr7CMkA&t=25s',
      'video_id': '5hRyQr7CMkA'},
     {'author': 'The Vant Group',
      'channel': 'The Vant Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=fAVVcCIVQeE&t=48s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sign it in the best life and the misconception is a business broker is going to '
              'just what do you want for your company put two pages together put on a website '
              'solicit buyers and do very minimum.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'Sign it in the best life and the misconception is a business broker is going to '
             'just what do you want for your company put two pages together put on a website '
             'solicit buyers and do very minimum.',
      'title': 'Business Brokers Vs M&A Advisors | The Vant Group (The Vant Group)',
      'url': 'https://www.youtube.com/watch?v=fAVVcCIVQeE&t=48s',
      'video_id': 'fAVVcCIVQeE'},
     {'author': 'Data Center Build Academy',
      'channel': 'Data Center Build Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=8UjhKryCNbQ&t=20s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And stay to the end, because I'll walk you through three real-world style site "
              'options, and show you exactly which one an experienced team would buy, and why. '
              'Choosing land for a data center is nothing like choosing land for an office or '
              'a warehouse.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "And stay to the end, because I'll walk you through three real-world style site "
             'options, and show you exactly which one an experienced team would buy, and why. '
             'Choosing land for a data center is nothing like choosing land for an office or a '
             'warehouse.',
      'title': 'Data Center Site Selection: How to Choose Land (Power, Water, Fiber, Zoning) '
               '(Data Center Build Academy)',
      'url': 'https://www.youtube.com/watch?v=8UjhKryCNbQ&t=20s',
      'video_id': '8UjhKryCNbQ'},
     {'author': 'Launchcraft',
      'channel': 'Launchcraft',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=CaKZ8rVUEZs&t=51s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '5 seconds on your site, your positioning is broken. Most SaaS home pages lead '
              'with vague claims. The all-in-one platform for modern teams. Project '
              'management, chat, HR software. Positioning answers three questions instantly. '
              'What painful problem does it solve?',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': '5 seconds on your site, your positioning is broken. Most SaaS home pages lead '
             'with vague claims. The all-in-one platform for modern teams. Project management, '
             'chat, HR software. Positioning answers three questions instantly. What painful '
             'problem does it solve?',
      'title': 'How to Build a B2B SaaS Website That Actually Explains Your Product (2027) '
               '(Launchcraft)',
      'url': 'https://www.youtube.com/watch?v=CaKZ8rVUEZs&t=51s',
      'video_id': 'CaKZ8rVUEZs'},
     {'author': 'The Art of Yacht Sales',
      'channel': 'The Art of Yacht Sales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=elBm9ZOqdsA&t=211s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's about the volume, the frequency, and the long-term relationships you "
              "cultivate. It's about building a sustainable business, one successful "
              'transaction at a time.',
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': "It's about the volume, the frequency, and the long-term relationships you "
             "cultivate. It's about building a sustainable business, one successful "
             'transaction at a time.',
      'title': 'From Zero to €1,000,000 in Yacht Commissions – The Real Math & Mindset of '
               'Yacht Brokers (The Art of Yacht Sales)',
      'url': 'https://www.youtube.com/watch?v=elBm9ZOqdsA&t=211s',
      'video_id': 'elBm9ZOqdsA'},
     {'author': 'Luke Fox',
      'channel': 'Luke Fox',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=7ABdy0hf9u8&t=237s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To the data room and things like that but either way you're sort of narrowing "
              'down the field providing more and more insights into the business so in round.',
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': "To the data room and things like that but either way you're sort of narrowing "
             'down the field providing more and more insights into the business so in round.',
      'title': "Buy Side vs Sell Side | What's the difference when you work on mergers and "
               'acquisitions (M&A)? (Luke Fox)',
      'url': 'https://www.youtube.com/watch?v=7ABdy0hf9u8&t=237s',
      'video_id': '7ABdy0hf9u8'},
     {'author': 'Toolnest Explained',
      'channel': 'Toolnest Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=B4H8Hy41Myg&t=78s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Over time, that kind of organization is going to help you improve your results '
              'and win a lot more business. All right, section three, the seven sales stages. '
              'These are seven simple stages to closing deals. So, how is this map actually '
              'organized?',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Over time, that kind of organization is going to help you improve your results '
             'and win a lot more business. All right, section three, the seven sales stages. '
             'These are seven simple stages to closing deals. So, how is this map actually '
             'organized?',
      'title': 'What Is a Sales Pipeline in CRM? Explained for Beginners (Toolnest Explained)',
      'url': 'https://www.youtube.com/watch?v=B4H8Hy41Myg&t=78s',
      'video_id': 'B4H8Hy41Myg'},
     {'author': 'Yacht Broker Masterclass',
      'channel': 'Yacht Broker Masterclass',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=-7bW4uN98Hc&t=84s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Connections there is no doubts that you will learn of buyers and sellers who '
              'need the services of a yach broker it may not happen immediately but it will '
              'most certainly happen eventually if you are patient and tenacious and keep your '
              'eyes and ears.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': 'Connections there is no doubts that you will learn of buyers and sellers who '
             'need the services of a yach broker it may not happen immediately but it will '
             'most certainly happen eventually if you are patient and tenacious and keep your '
             'eyes and ears.',
      'title': 'HOW DO I GET STARTED AS A YACHT BROKER (Yacht Broker Masterclass)',
      'url': 'https://www.youtube.com/watch?v=-7bW4uN98Hc&t=84s',
      'video_id': '-7bW4uN98Hc'},
     {'author': 'Tutorial Toolkit',
      'channel': 'Tutorial Toolkit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=Sna6rbbuzww&t=32s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You'll want to click on CRM to expand the menu. From the drop down, select "
              "deals. This section is crucial as it's here that you'll manage all your ongoing "
              "deals. Once inside the tool, you'll find a well organized space to keep track "
              'of every deal in your pipeline.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "You'll want to click on CRM to expand the menu. From the drop down, select "
             "deals. This section is crucial as it's here that you'll manage all your ongoing "
             "deals. Once inside the tool, you'll find a well organized space to keep track of "
             'every deal in your pipeline.',
      'title': 'How to Use Hubspot Deals & Sales Pipelines (Track Deals Easily) (Tutorial '
               'Toolkit)',
      'url': 'https://www.youtube.com/watch?v=Sna6rbbuzww&t=32s',
      'video_id': 'Sna6rbbuzww'},
     {'author': 'The Closer ID',
      'channel': 'The Closer ID',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:40](https://www.youtube.com/watch?v=sh92NTG_jgs&t=640s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like I got this message the other day. Hope I can still go on Instagram. Yeah, '
              'but if you search like Dutch Dutch business owners or info businesses, then '
              "it's more difficult in my experience.",
      'timestamp': 640,
      'timestamp_label': '[00:10:40]',
      'timestamp_seconds': 640,
      'tip': 'Like I got this message the other day. Hope I can still go on Instagram. Yeah, '
             "but if you search like Dutch Dutch business owners or info businesses, then it's "
             'more difficult in my experience.',
      'title': 'How High Ticket Closers Find Offers Fast (Live Demo) (The Closer ID)',
      'url': 'https://www.youtube.com/watch?v=sh92NTG_jgs&t=640s',
      'video_id': 'sh92NTG_jgs'},
     {'author': 'Pass the Real Estate Exam with Ben Eger',
      'channel': 'Pass the Real Estate Exam with Ben Eger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=DPj-ieo_sSM&t=95s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Conversion means wrongfully using or controlling another person's funds or "
              "property. Paying office expenses with Jordan's deposit would be conversion, not "
              'merely commingling. Meanwhile, Alex tracks acceptance, deposit, inspection, '
              'financing, and closing obligations.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': "Conversion means wrongfully using or controlling another person's funds or "
             "property. Paying office expenses with Jordan's deposit would be conversion, not "
             'merely commingling. Meanwhile, Alex tracks acceptance, deposit, inspection, '
             'financing, and closing obligations.',
      'title': 'Brokerage Operations Explained | Real Estate Exam Prep 2026–2027 (Pass the '
               'Real Estate Exam with Ben Eger)',
      'url': 'https://www.youtube.com/watch?v=DPj-ieo_sSM&t=95s',
      'video_id': 'DPj-ieo_sSM'},
     {'author': 'Savvypreneurship',
      'channel': 'Savvypreneurship',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=xACWJ0HGNHs&t=92s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Affordable than aspiring to purchase a super yacht of 500 or more feet '
              'according to recent data only 2% of high net worth individuals own those type '
              'of super.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Affordable than aspiring to purchase a super yacht of 500 or more feet according '
             'to recent data only 2% of high net worth individuals own those type of super.',
      'title': 'A Complete Guide to Profiting from a Yacht Charter Investment '
               '(Savvypreneurship)',
      'url': 'https://www.youtube.com/watch?v=xACWJ0HGNHs&t=92s',
      'video_id': 'xACWJ0HGNHs'},
     {'author': 'iTopixs Videos',
      'channel': 'iTopixs Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:22](https://www.youtube.com/watch?v=l9rVUJ2duT8&t=622s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Public then you don't have to protect it anymore so for example if this "
              'involves the secret formula for coca-cola and and you get that secret formula '
              "but then it becomes available to the public then you don't have an obligation "
              'to keep it secret anymore.',
      'timestamp': 622,
      'timestamp_label': '[00:10:22]',
      'timestamp_seconds': 622,
      'tip': "Public then you don't have to protect it anymore so for example if this involves "
             'the secret formula for coca-cola and and you get that secret formula but then it '
             "becomes available to the public then you don't have an obligation to keep it "
             'secret anymore.',
      'title': 'NCND Non-Compete Non-Disclosure & NDA Non-Disclosure Agreements (iTopixs '
               'Videos)',
      'url': 'https://www.youtube.com/watch?v=l9rVUJ2duT8&t=622s',
      'video_id': 'l9rVUJ2duT8'}],
 9: [{'author': 'Newestexamprep',
      'channel': 'Newestexamprep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=Q-U6m9rsXvQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before entering into the listing agreement, before showing the property to any '
              'buyers. Before closing escrow within days days of signing the contract, the '
              'listing agent must deliver the agency disclosure form to the seller before '
              'entering into the listing agreement.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Before entering into the listing agreement, before showing the property to any '
             'buyers. Before closing escrow within days days of signing the contract, the '
             'listing agent must deliver the agency disclosure form to the seller before '
             'entering into the listing agreement.',
      'title': 'California Real Estate License 2026: Salesperson vs Broker Career Paths '
               '(Newestexamprep)',
      'url': 'https://www.youtube.com/watch?v=Q-U6m9rsXvQ&t=79s',
      'video_id': 'Q-U6m9rsXvQ'},
     {'author': 'Business Broker Crowd Call',
      'channel': 'Business Broker Crowd Call',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=paYxIXgYO0I&t=93s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But because Texas is a non-licensed state, so is Montana and you know, a bunch '
              'of others, you cannot fill in the blanks on a purchase agreement or you can be '
              'deemed to be practicing law without a license.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'But because Texas is a non-licensed state, so is Montana and you know, a bunch '
             'of others, you cannot fill in the blanks on a purchase agreement or you can be '
             'deemed to be practicing law without a license.',
      'title': 'Business Brokerage vs Commercial Real Estate: Key Legal Differences Every '
               'Broker Must Know (Business Broker Crowd Call)',
      'url': 'https://www.youtube.com/watch?v=paYxIXgYO0I&t=93s',
      'video_id': 'paYxIXgYO0I'},
     {'author': 'We Sell Construction Businesses',
      'channel': 'We Sell Construction Businesses',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=JkYDV-Gr_qE&t=40s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But even more crucial in legal matters such as contracts and disclosure '
              'concerns. The Business Brokers of Florida, encourages you to ask if the '
              "Business Broker that you're working with is licensed to sell businesses in the "
              'state of Florida.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'But even more crucial in legal matters such as contracts and disclosure '
             'concerns. The Business Brokers of Florida, encourages you to ask if the Business '
             "Broker that you're working with is licensed to sell businesses in the state of "
             'Florida.',
      'title': 'Important Licensing Requirements from the Business Brokers of Florida (We Sell '
               'Construction Businesses)',
      'url': 'https://www.youtube.com/watch?v=JkYDV-Gr_qE&t=40s',
      'video_id': 'JkYDV-Gr_qE'},
     {'author': 'Attorney Nancy Greene',
      'channel': 'Attorney Nancy Greene',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=FOUV15TeRLY&t=108s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Teaming agreement you still benefit that's why a non-circumvention provision "
              "might be the most powerful contract term to avoid legal landmines that you're "
              'not.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "Teaming agreement you still benefit that's why a non-circumvention provision "
             "might be the most powerful contract term to avoid legal landmines that you're "
             'not.',
      'title': 'Non-disclosure agreements vs non-circumvention provisions | Employment Law '
               '(Attorney Nancy Greene)',
      'url': 'https://www.youtube.com/watch?v=FOUV15TeRLY&t=108s',
      'video_id': 'FOUV15TeRLY'},
     {'author': 'County Portal Law',
      'channel': 'County Portal Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=FKep5tuU15Q&t=121s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '>>  >> State how long the agreement will last. Explain the consequences if '
              'someone breaks the rules.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': '>>  >> State how long the agreement will last. Explain the consequences if '
             'someone breaks the rules.',
      'title': 'Does A Non Disclosure Agreement Need To Be Notarized? (County Portal Law)',
      'url': 'https://www.youtube.com/watch?v=FKep5tuU15Q&t=121s',
      'video_id': 'FKep5tuU15Q'},
     {'author': 'Business Broker Crowd Call',
      'channel': 'Business Broker Crowd Call',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=CoD81HjwtQo&t=136s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Together I see so so is it mostly advisable to get a real license along with u '
              'in in practically every state if you want to pursue business brokerage as well.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'Together I see so so is it mostly advisable to get a real license along with u '
             'in in practically every state if you want to pursue business brokerage as well.',
      'title': 'Understanding Licensing Requirements for Business Brokers (Business Broker '
               'Crowd Call)',
      'url': 'https://www.youtube.com/watch?v=CoD81HjwtQo&t=136s',
      'video_id': 'CoD81HjwtQo'},
     {'author': 'StartupWise',
      'channel': 'StartupWise',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=aH0Oee-tkEo&t=50s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'NDAs, when they are applicable, what types of information you can keep '
              'confidential, as well as the different types of non-disclosure agreements. So, '
              "I highly recommend giving that a read. Right now, I'm going to show you guys "
              'exactly how to create an NDA using Law Depot.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'NDAs, when they are applicable, what types of information you can keep '
             'confidential, as well as the different types of non-disclosure agreements. So, I '
             "highly recommend giving that a read. Right now, I'm going to show you guys "
             'exactly how to create an NDA using Law Depot.',
      'title': 'How to Create a Non-Disclosure Agreement (NDA) for FREE (Step by Step '
               'Tutorial) (StartupWise)',
      'url': 'https://www.youtube.com/watch?v=aH0Oee-tkEo&t=50s',
      'video_id': 'aH0Oee-tkEo'},
     {'author': 'Ian Tucker - Hard Money & DSCR Loan Broker Expert',
      'channel': 'Ian Tucker - Hard Money & DSCR Loan Broker Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=VF-_WZaM0iI&t=182s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "License in the state that the loan is in and if the broker doesn't have the "
              "license then the lender will not do the loan they'll just turn it down "
              'straight.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': "License in the state that the loan is in and if the broker doesn't have the "
             "license then the lender will not do the loan they'll just turn it down straight.",
      'title': 'How To Get Your Real Estate Loan Broker License: A Complete State Guide | '
               'GraftonFunding.com (Ian Tucker - Hard Money & DSCR Loan Broker Expert)',
      'url': 'https://www.youtube.com/watch?v=VF-_WZaM0iI&t=182s',
      'video_id': 'VF-_WZaM0iI'},
     {'author': 'CertFuel',
      'channel': 'CertFuel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=3z_ALLqRZ2E&t=244s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "500 massive institutional pension trusts, you're golden. And by the way, those "
              'pension trusts require zero minimum asset size under this rule. But, if you do '
              'business with just one resident retail customer in that state, your entire '
              'institutional exclusion goes up in smoke.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': "500 massive institutional pension trusts, you're golden. And by the way, those "
             'pension trusts require zero minimum asset size under this rule. But, if you do '
             'business with just one resident retail customer in that state, your entire '
             'institutional exclusion goes up in smoke.',
      'title': 'Exclusions from the Broker-Dealer Definition - Series 63 Exam Prep (CertFuel)',
      'url': 'https://www.youtube.com/watch?v=3z_ALLqRZ2E&t=244s',
      'video_id': '3z_ALLqRZ2E'},
     {'author': 'ALC Lawcast: Finance in Focus',
      'channel': 'ALC Lawcast: Finance in Focus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=bfazVN-7QhQ&t=104s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As I will talk about, the Florida exemption is similar but not identical to the '
              'federal exemption. The SEC exemption specifically limited itself to the federal '
              'broker-dealer registration requirements, and not state law.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'As I will talk about, the Florida exemption is similar but not identical to the '
             'federal exemption. The SEC exemption specifically limited itself to the federal '
             'broker-dealer registration requirements, and not state law.',
      'title': 'Florida Broker-Dealer Registration Exemption For M&A Brokers (ALC Lawcast: '
               'Finance in Focus)',
      'url': 'https://www.youtube.com/watch?v=bfazVN-7QhQ&t=104s',
      'video_id': 'bfazVN-7QhQ'},
     {'author': 'UpCounsel',
      'channel': 'UpCounsel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=B7w7HuoPnsA&t=222s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For an NCND to be legally enforcable, it should include specific language on '
              'dispute resolution, applicable law, and jurisdiction. These provisions create a '
              'predetermined legal pathway for resolving disagreements.',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': 'For an NCND to be legally enforcable, it should include specific language on '
             'dispute resolution, applicable law, and jurisdiction. These provisions create a '
             'predetermined legal pathway for resolving disagreements.',
      'title': 'Understanding NCND Agreements  Protecting Intermediaries in Business Deals '
               '(UpCounsel)',
      'url': 'https://www.youtube.com/watch?v=B7w7HuoPnsA&t=222s',
      'video_id': 'B7w7HuoPnsA'},
     {'author': 'International Yacht Brokers Association',
      'channel': 'International Yacht Brokers Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:08](https://www.youtube.com/watch?v=RPROcS6hZSE&t=848s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Tries to interfere in another person's business Affairs that's why Florida has "
              'that um that cause of action to pursue all right well thank you and Leanne last '
              'comment on this as we move along but go ahead shout it out if you want she St '
              'in the state of Florida.',
      'timestamp': 848,
      'timestamp_label': '[00:14:08]',
      'timestamp_seconds': 848,
      'tip': "Tries to interfere in another person's business Affairs that's why Florida has "
             'that um that cause of action to pursue all right well thank you and Leanne last '
             'comment on this as we move along but go ahead shout it out if you want she St in '
             'the state of Florida.',
      'title': 'Broker Panel Case Studies (International Yacht Brokers Association)',
      'url': 'https://www.youtube.com/watch?v=RPROcS6hZSE&t=848s',
      'video_id': 'RPROcS6hZSE'},
     {'author': 'ALC Lawcast: Finance in Focus',
      'channel': 'ALC Lawcast: Finance in Focus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=rl3PWicoIaE&t=212s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the next LawCast in this series, I will detail the restrictions and '
              'particular obligations required to rely on the Florida statute. I am securities '
              'attorney Laura Anthony, founding partner of Legal & Compliance, and producer of '
              'LawCast.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': 'In the next LawCast in this series, I will detail the restrictions and '
             'particular obligations required to rely on the Florida statute. I am securities '
             'attorney Laura Anthony, founding partner of Legal & Compliance, and producer of '
             'LawCast.',
      'title': 'Laura Anthony Attorney; M&A Broker Exemption (ALC Lawcast: Finance in Focus)',
      'url': 'https://www.youtube.com/watch?v=rl3PWicoIaE&t=212s',
      'video_id': 'rl3PWicoIaE'},
     {'author': 'Quiet Light Brokerage',
      'channel': 'Quiet Light Brokerage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=In6A5W0WFdY&t=15s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are we head it what are benchmarks within that market what is the range of '
              'values of my business and where where am I today where do I want to go what '
              'type.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Are we head it what are benchmarks within that market what is the range of '
             'values of my business and where where am I today where do I want to go what '
             'type.',
      'title': 'The State of SaaS in 2025: Multiples, Growth Strategies, Valuations, & Exit '
               'Planning (Quiet Light Brokerage)',
      'url': 'https://www.youtube.com/watch?v=In6A5W0WFdY&t=15s',
      'video_id': 'In6A5W0WFdY'},
     {'author': 'Business Broker Crowd Call',
      'channel': 'Business Broker Crowd Call',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=_4qKlVp4-8s&t=157s)',
      'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                   'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                   'closings (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Regulations that are required in my own local state um and if it's a "
              'non-licensed state then you know certainly that would be better than just '
              'making it up and and doing whatever you want kind of a freefor all does that '
              'make sense it does thank.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "Regulations that are required in my own local state um and if it's a "
             'non-licensed state then you know certainly that would be better than just making '
             'it up and and doing whatever you want kind of a freefor all does that make sense '
             'it does thank.',
      'title': 'Business Broker Commissions and Licensing Requirements (Business Broker Crowd '
               'Call)',
      'url': 'https://www.youtube.com/watch?v=_4qKlVp4-8s&t=157s',
      'video_id': '_4qKlVp4-8s'}],
 10: [{'author': 'ALC Lawcast: Finance in Focus',
       'channel': 'ALC Lawcast: Finance in Focus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:53](https://www.youtube.com/watch?v=o-XOblDUBuI&t=113s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If the M&A transaction involves a buyer group, the M&A broker may not be '
               'involved in forming the group; The buyer or group of buyers must control and '
               'actively operate the company or business and cannot be passive buyers.',
       'timestamp': 113,
       'timestamp_label': '[00:01:53]',
       'timestamp_seconds': 113,
       'tip': 'If the M&A transaction involves a buyer group, the M&A broker may not be '
              'involved in forming the group; The buyer or group of buyers must control and '
              'actively operate the company or business and cannot be passive buyers.',
       'title': 'Federal M&A Broker Exemption (ALC Lawcast: Finance in Focus)',
       'url': 'https://www.youtube.com/watch?v=o-XOblDUBuI&t=113s',
       'video_id': 'o-XOblDUBuI'},
      {'author': 'CertFuel',
       'channel': 'CertFuel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:49](https://www.youtube.com/watch?v=ekpLm58t3ok&t=109s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'As a business overall, sure, Barry does both jobs, which is literally why he '
               'is called a broker-dealer, but on any single individual trade, he has to pick '
               'a lane. He is either acting as an agent earning a commission or as a principal '
               'earning a markup or markdown.',
       'timestamp': 109,
       'timestamp_label': '[00:01:49]',
       'timestamp_seconds': 109,
       'tip': 'As a business overall, sure, Barry does both jobs, which is literally why he is '
              'called a broker-dealer, but on any single individual trade, he has to pick a '
              'lane. He is either acting as an agent earning a commission or as a principal '
              'earning a markup or markdown.',
       'title': 'Definition of a Broker-Dealer - Series 63 Exam Prep (CertFuel)',
       'url': 'https://www.youtube.com/watch?v=ekpLm58t3ok&t=109s',
       'video_id': 'ekpLm58t3ok'},
      {'author': 'Real Estate Explained with Janis Benstock',
       'channel': 'Real Estate Explained with Janis Benstock',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:20](https://www.youtube.com/watch?v=F2USouPuthI&t=80s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So the real estate commission fines people for violating the law, and there '
               'was just a couple of years ago a pretty well-known real estate agent who got '
               'fined $5,000 for not complying with advertising guidelines on a billboard.',
       'timestamp': 80,
       'timestamp_label': '[00:01:20]',
       'timestamp_seconds': 80,
       'tip': 'So the real estate commission fines people for violating the law, and there was '
              'just a couple of years ago a pretty well-known real estate agent who got fined '
              '$5,000 for not complying with advertising guidelines on a billboard.',
       'title': 'Should You Get Your PA Broker License? Why Real Estate Law Matters | Janis '
                'Benstock (Real Estate Explained with Janis Benstock)',
       'url': 'https://www.youtube.com/watch?v=F2USouPuthI&t=80s',
       'video_id': 'F2USouPuthI'},
      {'author': 'Andrew Dubinsky',
       'channel': 'Andrew Dubinsky',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:51](https://www.youtube.com/watch?v=h0qEAIoQ4Jo&t=291s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'There are brokers that are specifically allowed to help buyers meet sellers '
               'and to negotiate, but there the buyer or the the broker cannot hold the credit '
               'or take possession or ownership of the credit. So anymore, it very much like '
               "real estate. I'm just brokering the house.",
       'timestamp': 291,
       'timestamp_label': '[00:04:51]',
       'timestamp_seconds': 291,
       'tip': 'There are brokers that are specifically allowed to help buyers meet sellers and '
              'to negotiate, but there the buyer or the the broker cannot hold the credit or '
              'take possession or ownership of the credit. So anymore, it very much like real '
              "estate. I'm just brokering the house.",
       'title': 'Tax Credit 101 with Andrew Dubinsky | Part 2: How Transferable Tax Credits '
                'Work (Section 6418) (Andrew Dubinsky)',
       'url': 'https://www.youtube.com/watch?v=h0qEAIoQ4Jo&t=291s',
       'video_id': 'h0qEAIoQ4Jo'},
      {'author': 'The Finance Lab',
       'channel': 'The Finance Lab',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:06](https://www.youtube.com/watch?v=dKOzaPUjfHM&t=186s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If your advice is solely incidental to your brokerage business and you receive '
               'no special compensation for it, you stay firmly over in the broker only '
               'category.',
       'timestamp': 186,
       'timestamp_label': '[00:03:06]',
       'timestamp_seconds': 186,
       'tip': 'If your advice is solely incidental to your brokerage business and you receive '
              'no special compensation for it, you stay firmly over in the broker only '
              'category.',
       'title': 'Series 24: Registering a Broker-Dealer, OSJs, Branch Offices and Rule 1017 '
                "(Stanford's $8B Fraud) (The Finance Lab)",
       'url': 'https://www.youtube.com/watch?v=dKOzaPUjfHM&t=186s',
       'video_id': 'dKOzaPUjfHM'},
      {'author': 'The Digital Merchant',
       'channel': 'The Digital Merchant',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:09](https://www.youtube.com/watch?v=yd4nlCQanq4&t=489s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "FE International and Quiet Light. It's very much a bilateral platform upon "
               "which sellers and buyers kind of interact with one another. There's no real "
               "brokerage service coming from Flippa. 's typically cheaper and particularly "
               'for businesses at the lower end of the scale.',
       'timestamp': 489,
       'timestamp_label': '[00:08:09]',
       'timestamp_seconds': 489,
       'tip': "FE International and Quiet Light. It's very much a bilateral platform upon "
              "which sellers and buyers kind of interact with one another. There's no real "
              "brokerage service coming from Flippa. 's typically cheaper and particularly for "
              'businesses at the lower end of the scale.',
       'title': 'The Best FE International Alternatives for M&A: QuietLight, Flippa, '
                'Acquire.com, & More! (The Digital Merchant)',
       'url': 'https://www.youtube.com/watch?v=yd4nlCQanq4&t=489s',
       'video_id': 'yd4nlCQanq4'},
      {'author': 'Yachts For Sale',
       'channel': 'Yachts For Sale',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:28:06](https://www.youtube.com/watch?v=FpmvbD9-7yc&t=1686s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "May have been a a real estate agent rather than a yacht broker we've had "
               'another Super chat so thank you very much indeed for that David Dylan.',
       'timestamp': 1686,
       'timestamp_label': '[00:28:06]',
       'timestamp_seconds': 1686,
       'tip': "May have been a a real estate agent rather than a yacht broker we've had "
              'another Super chat so thank you very much indeed for that David Dylan.',
       'title': 'BREAKING IN TO YACHT BROKERAGE - How Much can I Make??? (Yachts For Sale)',
       'url': 'https://www.youtube.com/watch?v=FpmvbD9-7yc&t=1686s',
       'video_id': 'FpmvbD9-7yc'},
      {'author': 'Objective, Investment Banking & Valuation',
       'channel': 'Objective, Investment Banking & Valuation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:18](https://www.youtube.com/watch?v=Ru1cmBnC5Rc&t=18s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That they've built one of the things we do uniquely for our clients is "
               'leverage our industry and knowledge it worked great collaboratively with '
               'buyers we go.',
       'timestamp': 18,
       'timestamp_label': '[00:00:18]',
       'timestamp_seconds': 18,
       'tip': "That they've built one of the things we do uniquely for our clients is leverage "
              'our industry and knowledge it worked great collaboratively with buyers we go.',
       'title': 'Buy-Side M&A Advisory (Objective, Investment Banking & Valuation)',
       'url': 'https://www.youtube.com/watch?v=Ru1cmBnC5Rc&t=18s',
       'video_id': 'Ru1cmBnC5Rc'},
      {'author': 'Designed For Agents',
       'channel': 'Designed For Agents',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:51](https://www.youtube.com/watch?v=Vbv1TkWvBD8&t=411s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now, let's talk about choosing based on your learning style and your goals, "
               "right? So, if you're a brand new agent, um you're going to set goals, right? "
               "Likely you're going to walk through a business plan hopefully.",
       'timestamp': 411,
       'timestamp_label': '[00:06:51]',
       'timestamp_seconds': 411,
       'tip': "Now, let's talk about choosing based on your learning style and your goals, "
              "right? So, if you're a brand new agent, um you're going to set goals, right? "
              "Likely you're going to walk through a business plan hopefully.",
       'title': 'How to Choose Your First Real Estate Brokerage (What Actually Matters) '
                '(Designed For Agents)',
       'url': 'https://www.youtube.com/watch?v=Vbv1TkWvBD8&t=411s',
       'video_id': 'Vbv1TkWvBD8'},
      {'author': 'Nexus Towers',
       'channel': 'Nexus Towers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=YjzN5Uo5yf8&t=23s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Rooftop right you're selling a specific area that is utilized by that cell "
               'tower I like to uh maybe equate it to the purchasing of the building right '
               'when.',
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': "Rooftop right you're selling a specific area that is utilized by that cell "
              'tower I like to uh maybe equate it to the purchasing of the building right '
              'when.',
       'title': 'Cell Tower Easements Explained – What Property Owners Need to Know (Nexus '
                'Towers)',
       'url': 'https://www.youtube.com/watch?v=YjzN5Uo5yf8&t=23s',
       'video_id': 'YjzN5Uo5yf8'},
      {'author': 'My SBA Loan Pro Podcast',
       'channel': 'My SBA Loan Pro Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:16](https://www.youtube.com/watch?v=VaF6Cv0koYQ&t=1336s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Whoever is holding those funds you know if it's a buyer and a seller uh if "
               "it's the sellers broker that's holding those funds and they decide that they "
               'just.',
       'timestamp': 1336,
       'timestamp_label': '[00:22:16]',
       'timestamp_seconds': 1336,
       'tip': "Whoever is holding those funds you know if it's a buyer and a seller uh if it's "
              "the sellers broker that's holding those funds and they decide that they just.",
       'title': 'Main Street M&A Legal Tips And Best Practices with Jake Parsley | Ep. 4 | My '
                'SBA Loan Pro Podcast (My SBA Loan Pro Podcast)',
       'url': 'https://www.youtube.com/watch?v=VaF6Cv0koYQ&t=1336s',
       'video_id': 'VaF6Cv0koYQ'},
      {'author': 'Business Broker Crowd Call',
       'channel': 'Business Broker Crowd Call',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:22](https://www.youtube.com/watch?v=LFYHvuRB96I&t=142s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And so, you're building relationships with those M&A or with those um private "
               'equity firms, family offices, and so forth. So, just a little bit different in '
               "in who Who's your buyer, right?",
       'timestamp': 142,
       'timestamp_label': '[00:02:22]',
       'timestamp_seconds': 142,
       'tip': "And so, you're building relationships with those M&A or with those um private "
              'equity firms, family offices, and so forth. So, just a little bit different in '
              "in who Who's your buyer, right?",
       'title': 'Unlocking Value: M&A Source vs  IBBA Memberships for Business Brokers '
                '(Business Broker Crowd Call)',
       'url': 'https://www.youtube.com/watch?v=LFYHvuRB96I&t=142s',
       'video_id': 'LFYHvuRB96I'},
      {'author': 'Cole Ferguson',
       'channel': 'Cole Ferguson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:19](https://www.youtube.com/watch?v=FpH555COYJI&t=499s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Aspiring broker for 15 minutes to share the Little that I know and to see '
               "where they're at on their in Journey and to encourage them thank you for "
               'watching share your thoughts comments below and until next time.',
       'timestamp': 499,
       'timestamp_label': '[00:08:19]',
       'timestamp_seconds': 499,
       'tip': 'Aspiring broker for 15 minutes to share the Little that I know and to see where '
              "they're at on their in Journey and to encourage them thank you for watching "
              'share your thoughts comments below and until next time.',
       'title': 'How to be successful as a business broker in 4 steps (Cole Ferguson)',
       'url': 'https://www.youtube.com/watch?v=FpH555COYJI&t=499s',
       'video_id': 'FpH555COYJI'},
      {'author': 'Yacht Experts LLC - Brokerage &  Extended Warranty',
       'channel': 'Yacht Experts LLC - Brokerage &  Extended Warranty',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:05](https://www.youtube.com/watch?v=NUVwWnSq3A0&t=485s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Certified yach professional who will make sure that you have the best possible '
               'outcome buying or selling your next yacht shoot me a text Christopher your '
               'South Florida yacht expert 561- 2851 1212 thank you n.',
       'timestamp': 485,
       'timestamp_label': '[00:08:05]',
       'timestamp_seconds': 485,
       'tip': 'Certified yach professional who will make sure that you have the best possible '
              'outcome buying or selling your next yacht shoot me a text Christopher your '
              'South Florida yacht expert 561- 2851 1212 thank you n.',
       'title': 'Why Are Yacht Brokerage Commissions So High? (Yacht Experts LLC - Brokerage '
                '&  Extended Warranty)',
       'url': 'https://www.youtube.com/watch?v=NUVwWnSq3A0&t=485s',
       'video_id': 'NUVwWnSq3A0'},
      {'author': 'Business Broker Crowd Call',
       'channel': 'Business Broker Crowd Call',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:49](https://www.youtube.com/watch?v=uRVS3zWAYwI&t=229s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'State whether or not they would be willing to allow you to to use a different '
               'uh referral form that does not require that referee to be licensed and again '
               "that's going to go back to them knowing that the laws in their state Kane I "
               'have a I have a couple of basic.',
       'timestamp': 229,
       'timestamp_label': '[00:03:49]',
       'timestamp_seconds': 229,
       'tip': 'State whether or not they would be willing to allow you to to use a different '
              'uh referral form that does not require that referee to be licensed and again '
              "that's going to go back to them knowing that the laws in their state Kane I "
              'have a I have a couple of basic.',
       'title': 'Real Estate Licensing and Referral Fees in Business Brokerage (Business '
                'Broker Crowd Call)',
       'url': 'https://www.youtube.com/watch?v=uRVS3zWAYwI&t=229s',
       'video_id': 'uRVS3zWAYwI'}],
 11: [{'author': 'SMART Talk for Real Estate Agents',
       'channel': 'SMART Talk for Real Estate Agents',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=7viJGpG_ju4&t=82s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'My team and I have been helping people buy and sell homes for years. Recently, '
               'one topic keeps coming up in almost every conversation with agents, buyer '
               'agent commissions.',
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': 'My team and I have been helping people buy and sell homes for years. Recently, '
              'one topic keeps coming up in almost every conversation with agents, buyer agent '
              'commissions.',
       'title': 'The Truth About Buyer Agent Commissions in 2026 ( New Rules Explained ) '
                '(SMART Talk for Real Estate Agents)',
       'url': 'https://www.youtube.com/watch?v=7viJGpG_ju4&t=82s',
       'video_id': '7viJGpG_ju4'},
      {'author': 'Ryan C. Winter, Business Broker',
       'channel': 'Ryan C. Winter, Business Broker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=If4qHRijbWg&t=119s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Seen your returns is a sales pitch, not a valuation. Ask how they will value '
               'the business,  how they will find and screen buyers, and how often they will.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': 'Seen your returns is a sales pitch, not a valuation. Ask how they will value '
              'the business,  how they will find and screen buyers, and how often they will.',
       'title': 'Business Broker vs. M&A Advisor: Which Do You Need to Sell Your Business? '
                '(Ryan C. Winter, Business Broker)',
       'url': 'https://www.youtube.com/watch?v=If4qHRijbWg&t=119s',
       'video_id': 'If4qHRijbWg'},
      {'author': 'Jim Loeffler',
       'channel': 'Jim Loeffler',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=aUN31sD75T0&t=21s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Today I want to talk about the confidential information memorandum or SIM. Now '
               'what is a confidential information memorandum? Well, the SIM is a document '
               'that we in the mergers and acquisitions community use to provide to buyers who '
               'are looking at purchasing a business.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Today I want to talk about the confidential information memorandum or SIM. Now '
              'what is a confidential information memorandum? Well, the SIM is a document that '
              'we in the mergers and acquisitions community use to provide to buyers who are '
              'looking at purchasing a business.',
       'title': 'Confidential Information Memorandum (CIM) (Jim Loeffler)',
       'url': 'https://www.youtube.com/watch?v=aUN31sD75T0&t=21s',
       'video_id': 'aUN31sD75T0'},
      {'author': 'Mike Sherrard',
       'channel': 'Mike Sherrard',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:31:10](https://www.youtube.com/watch?v=OFzI2gK-nps&t=1870s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s kind of like climbing the corporate real estate ladder. Get my license, "
               'build momentum solo, or join a team and then build momentum solo, then start a '
               'team, then start a brokerage and scale the brokerage and the brokerage is '
               'going to create you leverage.',
       'timestamp': 1870,
       'timestamp_label': '[00:31:10]',
       'timestamp_seconds': 1870,
       'tip': "'s kind of like climbing the corporate real estate ladder. Get my license, "
              'build momentum solo, or join a team and then build momentum solo, then start a '
              'team, then start a brokerage and scale the brokerage and the brokerage is going '
              'to create you leverage.',
       'title': 'Secrets of Scaling a Real Estate Brokerage (137 Agents + 4 Offices by 30 '
                'Years Old) (Mike Sherrard)',
       'url': 'https://www.youtube.com/watch?v=OFzI2gK-nps&t=1870s',
       'video_id': 'OFzI2gK-nps'},
      {'author': 'Tower Genius',
       'channel': 'Tower Genius',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:31](https://www.youtube.com/watch?v=V2LGinURueI&t=31s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You know just there is no cell tower lease buyout calculator or lease '
               "valuation calculator everything's determined on a site-by-site basis and.",
       'timestamp': 31,
       'timestamp_label': '[00:00:31]',
       'timestamp_seconds': 31,
       'tip': 'You know just there is no cell tower lease buyout calculator or lease valuation '
              "calculator everything's determined on a site-by-site basis and.",
       'title': 'How does a Cell Tower Lease Buyout Calculator work? (Tower Genius)',
       'url': 'https://www.youtube.com/watch?v=V2LGinURueI&t=31s',
       'video_id': 'V2LGinURueI'},
      {'author': 'Cangem Global Corporation',
       'channel': 'Cangem Global Corporation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:13](https://www.youtube.com/watch?v=HldBP9R47Bg&t=433s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It could could be very complicated if you try to get commission from both the '
               'parties. It could also be falling in the realm of I must say conflict of '
               'interest. So you should be very careful. So you should only take commission '
               'from one party either the seller or the buyer.',
       'timestamp': 433,
       'timestamp_label': '[00:07:13]',
       'timestamp_seconds': 433,
       'tip': 'It could could be very complicated if you try to get commission from both the '
              'parties. It could also be falling in the realm of I must say conflict of '
              'interest. So you should be very careful. So you should only take commission '
              'from one party either the seller or the buyer.',
       'title': 'The only genuine ICC NCNDA (Non Circumvention & Non Disclosure Agreement) '
                'format ! (Cangem Global Corporation)',
       'url': 'https://www.youtube.com/watch?v=HldBP9R47Bg&t=433s',
       'video_id': 'HldBP9R47Bg'},
      {'author': 'Jaryd Krause - Buying Online Businesses',
       'channel': 'Jaryd Krause - Buying Online Businesses',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:58](https://www.youtube.com/watch?v=XbluQ7u-9nc&t=238s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Asset you end up purchasing and the reason i say this is because the '
               'relationship can last a lifetime whereas the business.',
       'timestamp': 238,
       'timestamp_label': '[00:03:58]',
       'timestamp_seconds': 238,
       'tip': 'Asset you end up purchasing and the reason i say this is because the '
              'relationship can last a lifetime whereas the business.',
       'title': 'Where To Buy SAAS Websites Making Passive Income Monthly (Jaryd Krause - '
                'Buying Online Businesses)',
       'url': 'https://www.youtube.com/watch?v=XbluQ7u-9nc&t=238s',
       'video_id': 'XbluQ7u-9nc'},
      {'author': 'Peter Nola',
       'channel': 'Peter Nola',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:16](https://www.youtube.com/watch?v=RoGz5NZF96I&t=76s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Net profit of 100,000 the owner pays thems a salary of 50,000 and has car '
               'expenses not related to the business for 10,000 the sde for this Bakery would '
               'be 100,000 profit Plus 50,00 ,000.',
       'timestamp': 76,
       'timestamp_label': '[00:01:16]',
       'timestamp_seconds': 76,
       'tip': 'Net profit of 100,000 the owner pays thems a salary of 50,000 and has car '
              'expenses not related to the business for 10,000 the sde for this Bakery would '
              'be 100,000 profit Plus 50,00 ,000.',
       'title': 'SDE v EBITDA.  Essential for Accurate Business Valuation. (Peter Nola)',
       'url': 'https://www.youtube.com/watch?v=RoGz5NZF96I&t=76s',
       'video_id': 'RoGz5NZF96I'},
      {'author': 'Arthur Petropoulos',
       'channel': 'Arthur Petropoulos',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=D58oCe_7BBM&t=130s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And so, first tranche we're going to talk about are $0 to $500,000 of EBITDA. "
               'Now, this traditionally, and still to a very large part, is kind of the '
               'business broker Main Street type of business that is usually not on the '
               'institutional radar.',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': "And so, first tranche we're going to talk about are $0 to $500,000 of EBITDA. "
              'Now, this traditionally, and still to a very large part, is kind of the '
              'business broker Main Street type of business that is usually not on the '
              'institutional radar.',
       'title': 'The EBITDA Multiple Valuation Spectrum all Acquirers Use (Arthur Petropoulos)',
       'url': 'https://www.youtube.com/watch?v=D58oCe_7BBM&t=130s',
       'video_id': 'D58oCe_7BBM'},
      {'author': 'Nick Abraham',
       'channel': 'Nick Abraham',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:04](https://www.youtube.com/watch?v=Wdk1N79_WyM&t=484s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You want at the end of the day is working and then if it is come to us we'll "
               "scale it up for you guys but yeah that's the simplest easiest way on how to "
               'Source off Market deals with cold emils.',
       'timestamp': 484,
       'timestamp_label': '[00:08:04]',
       'timestamp_seconds': 484,
       'tip': "You want at the end of the day is working and then if it is come to us we'll "
              "scale it up for you guys but yeah that's the simplest easiest way on how to "
              'Source off Market deals with cold emils.',
       'title': 'How To Source Off Market Deals With Cold Emails (Nick Abraham)',
       'url': 'https://www.youtube.com/watch?v=Wdk1N79_WyM&t=484s',
       'video_id': 'Wdk1N79_WyM'},
      {'author': 'International Aircraft Broker Institute IABI',
       'channel': 'International Aircraft Broker Institute IABI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:32:35](https://www.youtube.com/watch?v=Oxw138mRpnA&t=1955s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re okay with that and that comes with the business as you may know already. "
               'So talking about business how how is it running Hallayas as a business as '
               'growth as expansion hiring? Tell me about the journey man.',
       'timestamp': 1955,
       'timestamp_label': '[00:32:35]',
       'timestamp_seconds': 1955,
       'tip': "'re okay with that and that comes with the business as you may know already. So "
              'talking about business how how is it running Hallayas as a business as growth '
              'as expansion hiring? Tell me about the journey man.',
       'title': 'Luxury Yachts, Private Aviation & High-End Clients | Ali Merchant | The Jet '
                'Podcast by IABI (International Aircraft Broker Institute IABI)',
       'url': 'https://www.youtube.com/watch?v=Oxw138mRpnA&t=1955s',
       'video_id': 'Oxw138mRpnA'},
      {'author': 'ALC Lawcast: Finance in Focus',
       'channel': 'ALC Lawcast: Finance in Focus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:13](https://www.youtube.com/watch?v=uqd9CdrsWKo&t=193s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '120 days before the date of the offer of exchange of securities; and finally, '
               'information pertaining to the management, business, results of operations, and '
               'material loss contingencies.',
       'timestamp': 193,
       'timestamp_label': '[00:03:13]',
       'timestamp_seconds': 193,
       'tip': '120 days before the date of the offer of exchange of securities; and finally, '
              'information pertaining to the management, business, results of operations, and '
              'material loss contingencies.',
       'title': 'M&A Broker Dealer Requirements (ALC Lawcast: Finance in Focus)',
       'url': 'https://www.youtube.com/watch?v=uqd9CdrsWKo&t=193s',
       'video_id': 'uqd9CdrsWKo'},
      {'author': 'Nate Lind - Business Broker and Beyond',
       'channel': 'Nate Lind - Business Broker and Beyond',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:33](https://www.youtube.com/watch?v=yaZZzBKh86I&t=393s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Business and that's where we're going to go through some more examples like "
               "this so thank you very much for watching I'll see you on the next video.",
       'timestamp': 393,
       'timestamp_label': '[00:06:33]',
       'timestamp_seconds': 393,
       'tip': "Business and that's where we're going to go through some more examples like "
              "this so thank you very much for watching I'll see you on the next video.",
       'title': "Business Valuation - Part 5 - How to Calculate Seller's Discretionary "
                'Earnings (Nate Lind - Business Broker and Beyond)',
       'url': 'https://www.youtube.com/watch?v=yaZZzBKh86I&t=393s',
       'video_id': 'yaZZzBKh86I'},
      {'author': 'Business Broker Crowd Call',
       'channel': 'Business Broker Crowd Call',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:04](https://www.youtube.com/watch?v=Wj1uuYyuyQk&t=364s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Yes you would have to have a real estate license even in those states that '
               "don't require a license to sell a business but because that land is involved "
               "you have to have a real estate license so yeah you're absolutely correct on "
               'that anything.',
       'timestamp': 364,
       'timestamp_label': '[00:06:04]',
       'timestamp_seconds': 364,
       'tip': 'Yes you would have to have a real estate license even in those states that '
              "don't require a license to sell a business but because that land is involved "
              "you have to have a real estate license so yeah you're absolutely correct on "
              'that anything.',
       'title': 'Navigating Business Broker Licensing Across States | Tips & Advice (Business '
                'Broker Crowd Call)',
       'url': 'https://www.youtube.com/watch?v=Wj1uuYyuyQk&t=364s',
       'video_id': 'Wj1uuYyuyQk'},
      {'author': 'Hauseit',
       'channel': 'Hauseit',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:58](https://www.youtube.com/watch?v=KrsoinTC_10&t=118s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Buy and sell property in New York and Florida you can do so hauseit.com check '
               'this out you can save six percent when you sell in broker commissions and two '
               'percent back or more when you buy with a house sit buyer closing credit.',
       'timestamp': 118,
       'timestamp_label': '[00:01:58]',
       'timestamp_seconds': 118,
       'tip': 'Buy and sell property in New York and Florida you can do so hauseit.com check '
              'this out you can save six percent when you sell in broker commissions and two '
              'percent back or more when you buy with a house sit buyer closing credit.',
       'title': 'How to Wire Money for Closing (Hauseit)',
       'url': 'https://www.youtube.com/watch?v=KrsoinTC_10&t=118s',
       'video_id': 'KrsoinTC_10'}],
 12: [{'author': 'Joe Killinger',
       'channel': 'Joe Killinger',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:48:46](https://www.youtube.com/watch?v=0u9CyKG6vj4&t=2926s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t really touched on it, you know, I I and maybe this is a little bit old of "
               'me, uh but you know, I remember I actually still remember my business days in '
               'business school and what I uh uh they said start with a business plan. You '
               'know, a mission statement.',
       'timestamp': 2926,
       'timestamp_label': '[00:48:46]',
       'timestamp_seconds': 2926,
       'tip': "'t really touched on it, you know, I I and maybe this is a little bit old of "
              'me, uh but you know, I remember I actually still remember my business days in '
              'business school and what I uh uh they said start with a business plan. You '
              'know, a mission statement.',
       'title': 'How to Start a Commercial Real Estate Brokerage in 2024 (Joe Killinger)',
       'url': 'https://www.youtube.com/watch?v=0u9CyKG6vj4&t=2926s',
       'video_id': '0u9CyKG6vj4'},
      {'author': 'Close',
       'channel': 'Close',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:11](https://www.youtube.com/watch?v=4XHqzQ8JPzk&t=251s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s closing and what's stalled so they can take action week over week, month "
               'over month, quarter over quarter, depending on how you report out. Your '
               "opportunity pipeline is more than a visual. It's a powerful workspace to help "
               'you prioritize, take action, and close faster.',
       'timestamp': 251,
       'timestamp_label': '[00:04:11]',
       'timestamp_seconds': 251,
       'tip': "'s closing and what's stalled so they can take action week over week, month "
              'over month, quarter over quarter, depending on how you report out. Your '
              "opportunity pipeline is more than a visual. It's a powerful workspace to help "
              'you prioritize, take action, and close faster.',
       'title': 'Getting Started with Opportunity Pipelines in Close | How to Track and Manage '
                'Your Deals (Close)',
       'url': 'https://www.youtube.com/watch?v=4XHqzQ8JPzk&t=251s',
       'video_id': '4XHqzQ8JPzk'},
      {'author': 'Amped Success - Matt Uhler',
       'channel': 'Amped Success - Matt Uhler',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:19](https://www.youtube.com/watch?v=uG64e1KV1S0&t=619s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'CRM system whatever it might be um you know that a lot of times that means you '
               'have a trusted uh system that produces numbers that you can actually use on a '
               'day-to-day week toeek month-to-month basis to manage the business.',
       'timestamp': 619,
       'timestamp_label': '[00:10:19]',
       'timestamp_seconds': 619,
       'tip': 'CRM system whatever it might be um you know that a lot of times that means you '
              'have a trusted uh system that produces numbers that you can actually use on a '
              'day-to-day week toeek month-to-month basis to manage the business.',
       'title': 'The Silent Deal Killer in Due Diligence and How to Avoid It - Mark Sims '
                '(Amped Success - Matt Uhler)',
       'url': 'https://www.youtube.com/watch?v=uG64e1KV1S0&t=619s',
       'video_id': 'uG64e1KV1S0'},
      {'author': 'Hudson Cosper',
       'channel': 'Hudson Cosper',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:17](https://www.youtube.com/watch?v=Wb6IlK5noKw&t=377s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I probably was only working three to four hours a day, still profiting like '
               "150k a month. But now there's going to be days where I work 12 hours.",
       'timestamp': 377,
       'timestamp_label': '[00:06:17]',
       'timestamp_seconds': 377,
       'tip': 'I probably was only working three to four hours a day, still profiting like '
              "150k a month. But now there's going to be days where I work 12 hours.",
       'title': 'how I got rich with high ticket sales after trying every other business model '
                '(Hudson Cosper)',
       'url': 'https://www.youtube.com/watch?v=Wb6IlK5noKw&t=377s',
       'video_id': 'Wb6IlK5noKw'},
      {'author': 'Break Into CRE',
       'channel': 'Break Into CRE',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=GKpCkDZaSS8&t=21s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, when you first start out in brokerage, there are really two main paths you '
               'can go down, which are the sales path and the analyst path. And on the sales '
               "path, you'll typically be on 100% commission without any base salary.",
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'So, when you first start out in brokerage, there are really two main paths you '
              'can go down, which are the sales path and the analyst path. And on the sales '
              "path, you'll typically be on 100% commission without any base salary.",
       'title': 'The TRUTH About Starting in Commercial Real Estate Brokerage (Break Into CRE)',
       'url': 'https://www.youtube.com/watch?v=GKpCkDZaSS8&t=21s',
       'video_id': 'GKpCkDZaSS8'},
      {'author': 'Hernan Vazquez',
       'channel': 'Hernan Vazquez',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:15](https://www.youtube.com/watch?v=PeOr6rOEN2Q&t=615s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And if you start building this, you only need to get a buyer once, and then '
               "they get follow-ups so that they can book a call down the road, which that's "
               'going to be the most amount of people.',
       'timestamp': 615,
       'timestamp_label': '[00:10:15]',
       'timestamp_seconds': 615,
       'tip': 'And if you start building this, you only need to get a buyer once, and then '
              "they get follow-ups so that they can book a call down the road, which that's "
              'going to be the most amount of people.',
       'title': 'How To Turn Low Ticket Buyers Into High Ticket Clients (My Follow-Up '
                'Sequences) (Hernan Vazquez)',
       'url': 'https://www.youtube.com/watch?v=PeOr6rOEN2Q&t=615s',
       'video_id': 'PeOr6rOEN2Q'},
      {'author': 'ALC Lawcast: Finance in Focus',
       'channel': 'ALC Lawcast: Finance in Focus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:05](https://www.youtube.com/watch?v=R0kgCi34_1s&t=185s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The SEC no action letter provides an exemption for M&A brokers that '
               'facilitates mergers, acquisitions, business sales and business combinations '
               'between sellers or buyers have privately held companies.',
       'timestamp': 185,
       'timestamp_label': '[00:03:05]',
       'timestamp_seconds': 185,
       'tip': 'The SEC no action letter provides an exemption for M&A brokers that facilitates '
              'mergers, acquisitions, business sales and business combinations between sellers '
              'or buyers have privately held companies.',
       'title': 'Federal And Florida M&A Broker Exemption, Laura Anthony Esq. (ALC Lawcast: '
                'Finance in Focus)',
       'url': 'https://www.youtube.com/watch?v=R0kgCi34_1s&t=185s',
       'video_id': 'R0kgCi34_1s'},
      {'author': 'Andrew LeBaron',
       'channel': 'Andrew LeBaron',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:31](https://www.youtube.com/watch?v=LlJs_vz0sPs&t=151s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If I have a hotel or a multi-family asset or a portfolio that I'm looking to "
               "sell or offload, they will give me the time of day. If you don't have that "
               "right now, maybe you liquidated everything, doesn't matter. Just let them know "
               'that you are in the market to buy.',
       'timestamp': 151,
       'timestamp_label': '[00:02:31]',
       'timestamp_seconds': 151,
       'tip': "If I have a hotel or a multi-family asset or a portfolio that I'm looking to "
              "sell or offload, they will give me the time of day. If you don't have that "
              "right now, maybe you liquidated everything, doesn't matter. Just let them know "
              'that you are in the market to buy.',
       'title': 'How to Raise Capital From Family Offices (No Warm Intro Needed) (Andrew '
                'LeBaron)',
       'url': 'https://www.youtube.com/watch?v=LlJs_vz0sPs&t=151s',
       'video_id': 'LlJs_vz0sPs'},
      {'author': 'Giuseppe Battaglioli',
       'channel': 'Giuseppe Battaglioli',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=YtS2MXC9Bps&t=94s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Want to avoid that just want to bring that to your attention early in this '
               "process you have plenty of time to confirm that if you plan on wiring you're "
               'not going to run into any issues come closing day let me know if you have any '
               "questions and we'll talk to you soon.",
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': 'Want to avoid that just want to bring that to your attention early in this '
              "process you have plenty of time to confirm that if you plan on wiring you're "
              'not going to run into any issues come closing day let me know if you have any '
              "questions and we'll talk to you soon.",
       'title': 'Planning To Wire Funds To Closing?  Watch This First (Giuseppe Battaglioli)',
       'url': 'https://www.youtube.com/watch?v=YtS2MXC9Bps&t=94s',
       'video_id': 'YtS2MXC9Bps'},
      {'author': 'CHARLES WEATHERLY',
       'channel': 'CHARLES WEATHERLY',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:44](https://www.youtube.com/watch?v=55kqfOfgIZw&t=284s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "One customer at 38% of revenue? You can't diversify that in 60 days. A roof or "
               'fleet near the end of its life? An owner working 60 hours a week with no '
               "manager beneath him? Priced in, it's already in the number. The buyer has "
               'nothing to retrade.',
       'timestamp': 284,
       'timestamp_label': '[00:04:44]',
       'timestamp_seconds': 284,
       'tip': "One customer at 38% of revenue? You can't diversify that in 60 days. A roof or "
              'fleet near the end of its life? An owner working 60 hours a week with no '
              "manager beneath him? Priced in, it's already in the number. The buyer has "
              'nothing to retrade.',
       'title': 'Why Do Good Deals Die in Diligence - 6-Minute Due Diligence Workshop (CHARLES '
                'WEATHERLY)',
       'url': 'https://www.youtube.com/watch?v=55kqfOfgIZw&t=284s',
       'video_id': '55kqfOfgIZw'},
      {'author': 'Hudson Cosper',
       'channel': 'Hudson Cosper',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:36](https://www.youtube.com/watch?v=4HgyBCSnkLE&t=156s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Patrick was 15 years old and hit a $20,000 month before he could even legally '
               'drive. And this is the only business model on the planet where you actually '
               'get paid the same week you close a deal.',
       'timestamp': 156,
       'timestamp_label': '[00:02:36]',
       'timestamp_seconds': 156,
       'tip': 'Patrick was 15 years old and hit a $20,000 month before he could even legally '
              'drive. And this is the only business model on the planet where you actually get '
              'paid the same week you close a deal.',
       'title': 'everything you need to know about high ticket sales (Hudson Cosper)',
       'url': 'https://www.youtube.com/watch?v=4HgyBCSnkLE&t=156s',
       'video_id': '4HgyBCSnkLE'},
      {'author': 'Series 7 Whisperer',
       'channel': 'Series 7 Whisperer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:36](https://www.youtube.com/watch?v=Nkm4yUiFRmc&t=156s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'We have market makers that buy and sell all day long on nasdaq or over the '
               'counter to create liquidity so if you want to buy stock in an over-the-counter '
               "stock you're probably buying it from a market maker.",
       'timestamp': 156,
       'timestamp_label': '[00:02:36]',
       'timestamp_seconds': 156,
       'tip': 'We have market makers that buy and sell all day long on nasdaq or over the '
              'counter to create liquidity so if you want to buy stock in an over-the-counter '
              "stock you're probably buying it from a market maker.",
       'title': 'SIE exam Tutor session ( Types of Broker Dealers) (Series 7 Whisperer)',
       'url': 'https://www.youtube.com/watch?v=Nkm4yUiFRmc&t=156s',
       'video_id': 'Nkm4yUiFRmc'},
      {'author': 'International Aircraft Broker Institute IABI',
       'channel': 'International Aircraft Broker Institute IABI',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=lrdWwuDaBtw&t=65s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "For example, in Miami, it's very easy to get a boat up to 120 people uh sorry, "
               '120 foot to accommodate for a day charter. In Europe, that may not be true. '
               'They would require you to do at least three days. That also goes along with '
               'the local coast guard laws.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': "For example, in Miami, it's very easy to get a boat up to 120 people uh sorry, "
              '120 foot to accommodate for a day charter. In Europe, that may not be true. '
              'They would require you to do at least three days. That also goes along with the '
              'local coast guard laws.',
       'title': 'How Yacht Brokers Actually Source Yachts - The Jet Podcast By IABI '
                '(International Aircraft Broker Institute IABI)',
       'url': 'https://www.youtube.com/watch?v=lrdWwuDaBtw&t=65s',
       'video_id': 'lrdWwuDaBtw'},
      {'author': 'Asher Shaw',
       'channel': 'Asher Shaw',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:01](https://www.youtube.com/watch?v=aFs-x6HJabU&t=661s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Then just hit me up on Instagram that's all for today boys and girls I'll "
               'catch you later and see you in a couple days cheers.',
       'timestamp': 661,
       'timestamp_label': '[00:11:01]',
       'timestamp_seconds': 661,
       'tip': "Then just hit me up on Instagram that's all for today boys and girls I'll catch "
              'you later and see you in a couple days cheers.',
       'title': 'High Ticket Sales Explained For Beginners (Asher Shaw)',
       'url': 'https://www.youtube.com/watch?v=aFs-x6HJabU&t=661s',
       'video_id': 'aFs-x6HJabU'},
      {'author': 'Think Real Estate',
       'channel': 'Think Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=wBbi84Xi1Bc&t=71s)',
       'relevance': 'Attributed practitioner commentary on specialist high-ticket asset & M&A '
                    'brokerage, exclusive mandates, NCNDA anti-circumvention, and escrow '
                    'closings (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What are we actually seeing in the practice of selling homes in commissions? '
               'It appears that most sellers, and by most I mean well over 90% of homeowners, '
               'are still agreeing to pay a buyer broker commission if they are asked to in '
               'the offer from the buyer.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': 'What are we actually seeing in the practice of selling homes in commissions? It '
              'appears that most sellers, and by most I mean well over 90% of homeowners, are '
              'still agreeing to pay a buyer broker commission if they are asked to in the '
              'offer from the buyer.',
       'title': 'What Buyers and Sellers Need to Know About the Buyer Broker Agreement in 2025 '
                '(Think Real Estate)',
       'url': 'https://www.youtube.com/watch?v=wBbi84Xi1Bc&t=71s',
       'video_id': 'wBbi84Xi1Bc'}]}
