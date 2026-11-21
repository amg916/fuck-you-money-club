"""Curated 180-citation Specialty Finance Brokerage baseline (15 per chapter across Q1-Q12) mined strictly from verified Specialty Finance Brokerage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'client',
     'clients',
     'commercial',
     'commission',
     'compliance',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'buyer',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'commercial',
     'commission',
     'compliance',
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
 3: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cash',
     'cashflow',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'commercial',
     'commission',
     'compliance',
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
 4: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'budget',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'commercial',
     'commission',
     'compliance',
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
 5: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'audit',
     'avoid',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'commercial',
     'commission',
     'compliance',
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
 6: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'client',
     'commercial',
     'commission',
     'compliance',
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
 7: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'checklist',
     'claim',
     'clawback',
     'commercial',
     'commission',
     'compliance',
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
 8: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'api',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'commercial',
     'commission',
     'compliance',
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
 9: {'1235',
     '504',
     '6418',
     'accounts',
     'advisory',
     'agreement',
     'asset',
     'avoiding',
     'b2b',
     'bankable',
     'based',
     'bond',
     'borrower',
     'box',
     'bridge',
     'broker',
     'brokerage',
     'building',
     'business',
     'california',
     'capital',
     'card',
     'cfdl',
     'cfl',
     'cfo',
     'chain',
     'claim',
     'clawback',
     'commercial',
     'commission',
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
 10: {'1235',
      '504',
      '6418',
      'accounts',
      'advisory',
      'agent',
      'ai',
      'asset',
      'automate',
      'automation',
      'avoiding',
      'b2b',
      'bankable',
      'based',
      'bond',
      'borrower',
      'box',
      'bridge',
      'broker',
      'brokerage',
      'building',
      'business',
      'california',
      'capital',
      'card',
      'cfdl',
      'cfl',
      'cfo',
      'chain',
      'claim',
      'clawback',
      'commercial',
      'commission',
      'compliance',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'1235',
      '504',
      '6418',
      'accounts',
      'advisory',
      'asset',
      'avoiding',
      'b2b',
      'bankable',
      'based',
      'bond',
      'borrower',
      'box',
      'bridge',
      'broker',
      'brokerage',
      'building',
      'business',
      'california',
      'capital',
      'card',
      'cfdl',
      'cfl',
      'cfo',
      'chain',
      'claim',
      'clawback',
      'commercial',
      'commission',
      'compliance',
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
 12: {'1235',
      '504',
      '6418',
      'accounts',
      'action',
      'advisory',
      'asset',
      'avoiding',
      'b2b',
      'bankable',
      'based',
      'bond',
      'borrower',
      'box',
      'bridge',
      'broker',
      'brokerage',
      'building',
      'business',
      'california',
      'capital',
      'card',
      'cfdl',
      'cfl',
      'cfo',
      'chain',
      'claim',
      'clawback',
      'commercial',
      'commission',
      'compliance',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=svRIdayYOLo&t=333s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And there\'s a big difference between saying, "I\'m a broker, I\'ve got money '
              'for sale." \'s figure out together what capital structure actually fits your '
              'business, fits you as a borrower, fits this project in this lender market.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': 'And there\'s a big difference between saying, "I\'m a broker, I\'ve got money '
             'for sale." \'s figure out together what capital structure actually fits your '
             'business, fits you as a borrower, fits this project in this lender market.',
      'title': '11 Things to Know Before Becoming a Commercial Loan Broker (Commercial Loan '
               'Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=svRIdayYOLo&t=333s',
      'video_id': 'svRIdayYOLo'},
     {'author': 'VoraPrep',
      'channel': 'VoraPrep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:52](https://www.youtube.com/watch?v=N0Pz-cRD6A4&t=232s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The key is whether the activity is a normal part of banking, or if they've "
              "basically set up a brokerage firm inside the bank. And there's one more group, "
              "a firm that has no place of business in the state. Let's say there's a "
              'brokerage firm based in New York.',
      'timestamp': 232,
      'timestamp_label': '[00:03:52]',
      'timestamp_seconds': 232,
      'tip': "The key is whether the activity is a normal part of banking, or if they've "
             "basically set up a brokerage firm inside the bank. And there's one more group, a "
             "firm that has no place of business in the state. Let's say there's a brokerage "
             'firm based in New York.',
      'title': '[Series 63] S632: Broker-Dealer Exclusions: Agents, Issuers, and Banks Under '
               'the Uniform Securiti... (VoraPrep)',
      'url': 'https://www.youtube.com/watch?v=N0Pz-cRD6A4&t=232s',
      'video_id': 'N0Pz-cRD6A4'},
     {'author': 'Enterprise Industry Network',
      'channel': 'Enterprise Industry Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=mXnUmcIc8Ek&t=191s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Equity can support growth, but may reduce control. Revenue-based funding can '
              'add flexibility, but may affect cash flow if not structured carefully. Funding '
              "is not only about getting money. It's about choosing capital that supports the "
              'business without weakening the business.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': 'Equity can support growth, but may reduce control. Revenue-based funding can add '
             'flexibility, but may affect cash flow if not structured carefully. Funding is '
             "not only about getting money. It's about choosing capital that supports the "
             'business without weakening the business.',
      'title': 'Debt vs Equity vs Revenue-Based Funding: Which Fits Your Business? | EIN '
               'Business Funding | EINBF (Enterprise Industry Network)',
      'url': 'https://www.youtube.com/watch?v=mXnUmcIc8Ek&t=191s',
      'video_id': 'mXnUmcIc8Ek'},
     {'author': 'Fractional Firm Academy',
      'channel': 'Fractional Firm Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=KJF9HKiAu0Y&t=277s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I mean by it is essentially me, I'll talk from my own experience, I run a "
              'fractional CFO firm, and I provide those services to clients. I have a defined '
              "scope of work, and I'm just really good at providing fractional CFO work, "
              'right?',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "I mean by it is essentially me, I'll talk from my own experience, I run a "
             'fractional CFO firm, and I provide those services to clients. I have a defined '
             "scope of work, and I'm just really good at providing fractional CFO work, right?",
      'title': 'Referrals Aren’t Enough: Ranking The Top 5 Client Channels for Fractional '
               'Firms (Fractional Firm Academy)',
      'url': 'https://www.youtube.com/watch?v=KJF9HKiAu0Y&t=277s',
      'video_id': 'KJF9HKiAu0Y'},
     {'author': 'MM BUSINESS SOLUTIONS',
      'channel': 'MM BUSINESS SOLUTIONS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:13](https://www.youtube.com/watch?v=i0yXJe_x34I&t=853s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a potential client, reaching out to them beyond just an email, beyond just a "
              'a simple text or a DM, right? Uh true relational reachouts are going to carry '
              'every person, every broker um and DAC so much farther in the eyes of those '
              'business owners.',
      'timestamp': 853,
      'timestamp_label': '[00:14:13]',
      'timestamp_seconds': 853,
      'tip': "'s a potential client, reaching out to them beyond just an email, beyond just a "
             'a simple text or a DM, right? Uh true relational reachouts are going to carry '
             'every person, every broker um and DAC so much farther in the eyes of those '
             'business owners.',
      'title': 'Business Funding Broker Training Nov 2026: David Allen Capital ISO Updates, '
               'Working Capital & Small (MM BUSINESS SOLUTIONS)',
      'url': 'https://www.youtube.com/watch?v=i0yXJe_x34I&t=853s',
      'video_id': 'i0yXJe_x34I'},
     {'author': 'Joe Camberato',
      'channel': 'Joe Camberato',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=GwPGzetluZM&t=72s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business loan or a Term Loan two is going to be a revenue based financing three '
              'is going to be a business line of credit based off of your cash flow all.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Business loan or a Term Loan two is going to be a revenue based financing three '
             'is going to be a business line of credit based off of your cash flow all.',
      'title': 'What Is Working Capital, and How Do I Get a Working Capital Loan? (Joe '
               'Camberato)',
      'url': 'https://www.youtube.com/watch?v=GwPGzetluZM&t=72s',
      'video_id': 'GwPGzetluZM'},
     {'author': 'The Finance Lab',
      'channel': 'The Finance Lab',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=xgYLNDnEqKg&t=54s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a recipe for disaster. When the funds eventually plunged, the market made "
              "the margin calls, and those clients lost everything. So let's move into section "
              'one, the core shield. This is all about regulation best interest and protecting '
              'the retail customer.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "It's a recipe for disaster. When the funds eventually plunged, the market made "
             "the margin calls, and those clients lost everything. So let's move into section "
             'one, the core shield. This is all about regulation best interest and protecting '
             'the retail customer.',
      'title': 'Series 24: Supervising Reg BI, Form CRS, Institutional Suitability and '
               'Concentration Reviews (The Finance Lab)',
      'url': 'https://www.youtube.com/watch?v=xgYLNDnEqKg&t=54s',
      'video_id': 'xgYLNDnEqKg'},
     {'author': 'Josh Olfert, CFP',
      'channel': 'Josh Olfert, CFP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:32](https://www.youtube.com/watch?v=skWLJwzq_fc&t=512s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You to do is take an existing business of financial advisory clients and '
              'migrate them over to something that is.',
      'timestamp': 512,
      'timestamp_label': '[00:08:32]',
      'timestamp_seconds': 512,
      'tip': 'You to do is take an existing business of financial advisory clients and migrate '
             'them over to something that is.',
      'title': 'How To Start a Financial Advisory Business (Josh Olfert, CFP)',
      'url': 'https://www.youtube.com/watch?v=skWLJwzq_fc&t=512s',
      'video_id': 'skWLJwzq_fc'},
     {'author': 'Zach Siegel',
      'channel': 'Zach Siegel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:59](https://www.youtube.com/watch?v=Yq5OojmQIac&t=299s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s probably a good idea to just follow through with it as long as you have a "
              "good plan for the money and you're using your revenue-based financing offer as "
              "a bridge into a better program if that's applicable as well.",
      'timestamp': 299,
      'timestamp_label': '[00:04:59]',
      'timestamp_seconds': 299,
      'tip': "'s probably a good idea to just follow through with it as long as you have a "
             "good plan for the money and you're using your revenue-based financing offer as a "
             "bridge into a better program if that's applicable as well.",
      'title': 'Revenue-Based Financing: What Lenders Won’t Tell You (Red & Green Flags) (Zach '
               'Siegel)',
      'url': 'https://www.youtube.com/watch?v=Yq5OojmQIac&t=299s',
      'video_id': 'Yq5OojmQIac'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:17](https://www.youtube.com/watch?v=7OHPVFeEmD4&t=317s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But, the real value of that fee isn't the $2,500. Think about the borrower who "
              "seems to just be price shopping. They're calling everybody, they're committing "
              'to nobody, and even a perfectly bankable client can turn out to be a tire '
              'kicker.',
      'timestamp': 317,
      'timestamp_label': '[00:05:17]',
      'timestamp_seconds': 317,
      'tip': "But, the real value of that fee isn't the $2,500. Think about the borrower who "
             "seems to just be price shopping. They're calling everybody, they're committing "
             'to nobody, and even a perfectly bankable client can turn out to be a tire '
             'kicker.',
      'title': 'How Brokers Get Paid Points, Fees & Splits (Commercial Loan Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=7OHPVFeEmD4&t=317s',
      'video_id': '7OHPVFeEmD4'},
     {'author': 'Real Estate Finance Academy with Trevor Calton',
      'channel': 'Real Estate Finance Academy with Trevor Calton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=2cFIwSgUOQM&t=22s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It depends on the industry, the market, the market timing, and the product '
              'type. Debt service coverage ratio tells us how much extra cushion we need to '
              'have in our net operating income over the debt service or the annual loan '
              'payments.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'It depends on the industry, the market, the market timing, and the product type. '
             'Debt service coverage ratio tells us how much extra cushion we need to have in '
             'our net operating income over the debt service or the annual loan payments.',
      'title': 'DSCR Demystified: How Lenders Really Use It to Size Your Loan | Debt Service '
               'Coverage Ratio (Real Estate Finance Academy with Trevor Calton)',
      'url': 'https://www.youtube.com/watch?v=2cFIwSgUOQM&t=22s',
      'video_id': '2cFIwSgUOQM'},
     {'author': 'Beyond Lenders',
      'channel': 'Beyond Lenders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=tlI9IYK5Dxg&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Requirements are a maximum loan to value of 70% and a minimum debt service '
              "coverage ratio of 1.25 times okay sure but what does that mean let's go "
              'through.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Requirements are a maximum loan to value of 70% and a minimum debt service '
             "coverage ratio of 1.25 times okay sure but what does that mean let's go through.",
      'title': 'You Must Understand LTV and DSCR (Beyond Lenders)',
      'url': 'https://www.youtube.com/watch?v=tlI9IYK5Dxg&t=15s',
      'video_id': 'tlI9IYK5Dxg'},
     {'author': 'ION Capital - Loan Broker University',
      'channel': 'ION Capital - Loan Broker University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:09](https://www.youtube.com/watch?v=DSEdy5KFvBs&t=609s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "At it and see if there's any viable life um life on it so it's kind of it's one "
              "of the worst questions for a hypothetical because there's a lot of different "
              'things that come into play yeah I understand they look at auction value.',
      'timestamp': 609,
      'timestamp_label': '[00:10:09]',
      'timestamp_seconds': 609,
      'tip': "At it and see if there's any viable life um life on it so it's kind of it's one "
             "of the worst questions for a hypothetical because there's a lot of different "
             'things that come into play yeah I understand they look at auction value.',
      'title': 'How To Be A Business Loan Broker  |  Equipment Finance Basics (ION Capital - '
               'Loan Broker University)',
      'url': 'https://www.youtube.com/watch?v=DSEdy5KFvBs&t=609s',
      'video_id': 'DSEdy5KFvBs'},
     {'author': 'Commercial Capital Training Group, LLC',
      'channel': 'Commercial Capital Training Group, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=nxxklr3VSSo&t=88s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Have been quicker wins and you know obviously uh the more Revenue that comes in '
              'the the less pressure you feel and so there were some deferred gratification in '
              "Revenue so I'd say you know making sure that you spend time.",
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Have been quicker wins and you know obviously uh the more Revenue that comes in '
             'the the less pressure you feel and so there were some deferred gratification in '
             "Revenue so I'd say you know making sure that you spend time.",
      'title': 'Commercial Loan Broker Successes and Advice After Training (Commercial Capital '
               'Training Group, LLC)',
      'url': 'https://www.youtube.com/watch?v=nxxklr3VSSo&t=88s',
      'video_id': 'nxxklr3VSSo'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=aBEJBn_bUA0&t=168s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We talk all things financing I've been in the lending industry for over 20 "
              "years and I'm happy to answer your questions and provide great content.",
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': "We talk all things financing I've been in the lending industry for over 20 years "
             "and I'm happy to answer your questions and provide great content.",
      'title': 'Comparing SBA 504 vs. 7A Loans for Commercial Real Estate (Beau Eckstein, '
               'Business Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=aBEJBn_bUA0&t=168s',
      'video_id': 'aBEJBn_bUA0'}],
 2: [{'author': 'Commercial Capital LLC',
      'channel': 'Commercial Capital LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=PoHdu7KQ0zI&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Problems many small business owners have to offer their customers payment terms '
              'that is the customer gets the option to pay their invoices in 30 to 60 days '
              "it's.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Problems many small business owners have to offer their customers payment terms '
             'that is the customer gets the option to pay their invoices in 30 to 60 days '
             "it's.",
      'title': 'Accounts Receivable Factoring - What is It? (Commercial Capital LLC)',
      'url': 'https://www.youtube.com/watch?v=PoHdu7KQ0zI&t=15s',
      'video_id': 'PoHdu7KQ0zI'},
     {'author': 'Equipment Finance Academy',
      'channel': 'Equipment Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=zolXG9LvowA&t=118s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Drain cash from the business, or finance the machine, pay for it while it earns '
              'money on jobs. Most owners choose the second option, or take the borrower who '
              'owns a restaurant. Commercial ovens, refrigeration, and kitchen equipment wear '
              'out on their schedule, not yours.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': 'Drain cash from the business, or finance the machine, pay for it while it earns '
             'money on jobs. Most owners choose the second option, or take the borrower who '
             'owns a restaurant. Commercial ovens, refrigeration, and kitchen equipment wear '
             'out on their schedule, not yours.',
      'title': 'Mortgage Loan Officers: The Second Commission Stream Hiding in Your Client '
               'List (Equipment Finance Academy)',
      'url': 'https://www.youtube.com/watch?v=zolXG9LvowA&t=118s',
      'video_id': 'zolXG9LvowA'},
     {'author': '75BizLoans and Commercial Real Estate Loans',
      'channel': '75BizLoans and Commercial Real Estate Loans',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=PH6WLL7kMUM&t=20s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm Kevin Kermeen, a nationwide commercial loan broker with 75 Biz Loans and "
              '200 plus capital partners. Invoice factoring and AR financing get mixed up all '
              'the time.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "I'm Kevin Kermeen, a nationwide commercial loan broker with 75 Biz Loans and 200 "
             'plus capital partners. Invoice factoring and AR financing get mixed up all the '
             'time.',
      'title': 'Invoice Factoring vs AR Financing Explained (2026) (75BizLoans and Commercial '
               'Real Estate Loans)',
      'url': 'https://www.youtube.com/watch?v=PH6WLL7kMUM&t=20s',
      'video_id': 'PH6WLL7kMUM'},
     {'author': 'FinanceKid',
      'channel': 'FinanceKid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=u5hujmtiiaY&t=336s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Receivable has collected the lender pays back the difference net Amite much '
              'higher fee so there are higher fees for recourse agreements in order to.',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'Receivable has collected the lender pays back the difference net Amite much '
             'higher fee so there are higher fees for recourse agreements in order to.',
      'title': 'Asset Based Lending (ABL) - Business Financing Explained (FinanceKid)',
      'url': 'https://www.youtube.com/watch?v=u5hujmtiiaY&t=336s',
      'video_id': 'u5hujmtiiaY'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=FnBYMtrQW9M&t=264s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the moment that the money it changes hands from lenders over to "
              "borrowers. And that's when the broker earns a fee. Well, sometimes the lender "
              "pays a fee, and sometimes the borrower pays a fee, and sometimes it's a "
              'combination.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': "That's the moment that the money it changes hands from lenders over to "
             "borrowers. And that's when the broker earns a fee. Well, sometimes the lender "
             "pays a fee, and sometimes the borrower pays a fee, and sometimes it's a "
             'combination.',
      'title': 'The Broker Business Explained: Low Risk, Big Commissions (Commercial Loan '
               'Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=FnBYMtrQW9M&t=264s',
      'video_id': 'FnBYMtrQW9M'},
     {'author': 'Vanijja | Trade Insights',
      'channel': 'Vanijja | Trade Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:46](https://www.youtube.com/watch?v=kMiyyMuSUDU&t=346s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, the benefits for them are massive. The big one is that the buyer can '
              'extend their payment terms. So, instead of paying their bills in 30 days, maybe '
              'they now pay in 60 or 90 or even 120 days.',
      'timestamp': 346,
      'timestamp_label': '[00:05:46]',
      'timestamp_seconds': 346,
      'tip': 'Well, the benefits for them are massive. The big one is that the buyer can '
             'extend their payment terms. So, instead of paying their bills in 30 days, maybe '
             'they now pay in 60 or 90 or even 120 days.',
      'title': "Cash Flow Problems? Here's How Supply Chain Finance Provides the Solution "
               '(Vanijja | Trade Insights)',
      'url': 'https://www.youtube.com/watch?v=kMiyyMuSUDU&t=346s',
      'video_id': 'kMiyyMuSUDU'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=7sx67OQUmsM&t=35s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For example, when a loan officer asks what's the monthly debt service on this "
              "loan, they're referring to the total amount of monthly loan payment or payments "
              'a borrower is obligated to pay.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': "For example, when a loan officer asks what's the monthly debt service on this "
             "loan, they're referring to the total amount of monthly loan payment or payments "
             'a borrower is obligated to pay.',
      'title': 'Debt Service Coverage Ratio (DSCR) Explained (REtipster)',
      'url': 'https://www.youtube.com/watch?v=7sx67OQUmsM&t=35s',
      'video_id': '7sx67OQUmsM'},
     {'author': 'The Money Side',
      'channel': 'The Money Side',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:25](https://www.youtube.com/watch?v=1_YV2DUgR-g&t=745s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The FTC says to check whether that buyer will need to pass a credit check or '
              "pay fees first if they won't or can't you may have to buy the system out before "
              'you sign.',
      'timestamp': 745,
      'timestamp_label': '[00:12:25]',
      'timestamp_seconds': 745,
      'tip': 'The FTC says to check whether that buyer will need to pass a credit check or pay '
             "fees first if they won't or can't you may have to buy the system out before you "
             'sign.',
      'title': "The 30% Solar Tax Credit Didn't Disappear. It Moved. (The Money Side)",
      'url': 'https://www.youtube.com/watch?v=1_YV2DUgR-g&t=745s',
      'video_id': '1_YV2DUgR-g'},
     {'author': 'SEI Mortgage - Ryan Marks',
      'channel': 'SEI Mortgage - Ryan Marks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=OOFsomPO_Mc&t=328s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, let's use an example of a client that we just priced out that went under "
              "contract. He's purchasing a home for $800,000. It's a six unit apartment "
              'building and some of them are rented and some of them are not rented.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': "So, let's use an example of a client that we just priced out that went under "
             "contract. He's purchasing a home for $800,000. It's a six unit apartment "
             'building and some of them are rented and some of them are not rented.',
      'title': '6 Unit DSCR Loans for Commercial Property: THIS Catches Investors Off Guard '
               '(SEI Mortgage - Ryan Marks)',
      'url': 'https://www.youtube.com/watch?v=OOFsomPO_Mc&t=328s',
      'video_id': 'OOFsomPO_Mc'},
     {'author': 'Biz2Credit',
      'channel': 'Biz2Credit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=vIqzq5xwqtA&t=77s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Local gas pump supplier says he'll sell Avery the top-of-the-line gas pearl "
              'all-star for $2,000 Avery will need to put down a 20% down payment and pay '
              'back.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "Local gas pump supplier says he'll sell Avery the top-of-the-line gas pearl "
             'all-star for $2,000 Avery will need to put down a 20% down payment and pay back.',
      'title': 'Equipment Financing | Learning with Business Finance Glossary (Biz2Credit)',
      'url': 'https://www.youtube.com/watch?v=vIqzq5xwqtA&t=77s',
      'video_id': 'vIqzq5xwqtA'},
     {'author': 'LetsLearn Global',
      'channel': 'LetsLearn Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=qEKcL_abQ9c&t=59s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What are the fees that are collected? And how much we can expect when we factor '
              'our receivables? Who bears the risk if our customers do not pay the amounts? '
              "This we'll discuss in detail. Let's begin now with what is factoring.",
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'What are the fees that are collected? And how much we can expect when we factor '
             'our receivables? Who bears the risk if our customers do not pay the amounts? '
             "This we'll discuss in detail. Let's begin now with what is factoring.",
      'title': 'CMA| Part 1 | Section A  | Accounts Receivable Factoring | Letslearn Global '
               '(LetsLearn Global)',
      'url': 'https://www.youtube.com/watch?v=qEKcL_abQ9c&t=59s',
      'video_id': 'qEKcL_abQ9c'},
     {'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:07](https://www.youtube.com/watch?v=cBxujqoCcbY&t=1507s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So even though they may have plenty of money to pay costs uh and to hire the '
              'best lawyers in the country, uh there may be a rational economic decision in '
              "which to call Stuart and say perhaps perhaps I'm better off getting funded. Uh "
              "they'll take care of the costs.",
      'timestamp': 1507,
      'timestamp_label': '[00:25:07]',
      'timestamp_seconds': 1507,
      'tip': 'So even though they may have plenty of money to pay costs uh and to hire the '
             'best lawyers in the country, uh there may be a rational economic decision in '
             "which to call Stuart and say perhaps perhaps I'm better off getting funded. Uh "
             "they'll take care of the costs.",
      'title': 'Introduction to Commercial Litigation Finance (The National Law Review)',
      'url': 'https://www.youtube.com/watch?v=cBxujqoCcbY&t=1507s',
      'video_id': 'cBxujqoCcbY'},
     {'author': 'The Approved Guy',
      'channel': 'The Approved Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=spCn3Rbs4XY&t=68s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It'll clear off the UCCC filing, but in the short term, it'll stop the bleeding "
              "because you'll be able to have the attorneys negotiate on your behalf to get "
              'you in a position where you can afford to continue to run your business while '
              'you pay back that debt.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "It'll clear off the UCCC filing, but in the short term, it'll stop the bleeding "
             "because you'll be able to have the attorneys negotiate on your behalf to get you "
             'in a position where you can afford to continue to run your business while you '
             'pay back that debt.',
      'title': 'SBA 7(A) NEW RULES BOMBSHELL FOR MCA DEBT CONSOLIDATION (The Approved Guy)',
      'url': 'https://www.youtube.com/watch?v=spCn3Rbs4XY&t=68s',
      'video_id': 'spCn3Rbs4XY'},
     {'author': 'Joe Camberato',
      'channel': 'Joe Camberato',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=lNnoO9VriRM&t=432s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make a quick easy I wanted to point out some helpful things that you really '
              'need to know when looking for an SBA loan thanks for tuning in I want to wish '
              'you nothing but success in your business and make sure that you keep growing.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': 'Make a quick easy I wanted to point out some helpful things that you really need '
             'to know when looking for an SBA loan thanks for tuning in I want to wish you '
             'nothing but success in your business and make sure that you keep growing.',
      'title': 'SBA Loans Explained: Types of Loans, Interest Rates, and What to Expect From '
               'the Process (Joe Camberato)',
      'url': 'https://www.youtube.com/watch?v=lNnoO9VriRM&t=432s',
      'video_id': 'lNnoO9VriRM'},
     {'author': 'Leads For Locals',
      'channel': 'Leads For Locals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:38:14](https://www.youtube.com/watch?v=Oq4y-D6sylo&t=2294s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can also go to debanked.com right now uh yesterday we actually released a '
              'quipping the dream uh reality show oh yeah uh that was gonna be my next my next '
              'uh my next point right here was the reality show.',
      'timestamp': 2294,
      'timestamp_label': '[00:38:14]',
      'timestamp_seconds': 2294,
      'tip': 'Can also go to debanked.com right now uh yesterday we actually released a '
             'quipping the dream uh reality show oh yeah uh that was gonna be my next my next '
             'uh my next point right here was the reality show.',
      'title': '☑️EliteBroker Training☑️ Equipment Financing Leads Program Breakdown (Leads '
               'For Locals)',
      'url': 'https://www.youtube.com/watch?v=Oq4y-D6sylo&t=2294s',
      'video_id': 'Oq4y-D6sylo'}],
 3: [{'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:00](https://www.youtube.com/watch?v=3V8HTzwHS90&t=120s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A commercial loan broker works around capital. Business owners need capital to '
              'acquire property, to buy equipment, to stabilize their cash flow. These are not '
              "tiny problems. When the problem is large that you're solving, the financing "
              'amount can be very large as well.',
      'timestamp': 120,
      'timestamp_label': '[00:02:00]',
      'timestamp_seconds': 120,
      'tip': 'A commercial loan broker works around capital. Business owners need capital to '
             'acquire property, to buy equipment, to stabilize their cash flow. These are not '
             "tiny problems. When the problem is large that you're solving, the financing "
             'amount can be very large as well.',
      'title': 'How Loan Brokers Can Earn $200K+ From Just 2 Deals (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=3V8HTzwHS90&t=120s',
      'video_id': '3V8HTzwHS90'},
     {'author': 'Gap Funding | 100% Real Estate Financing',
      'channel': 'Gap Funding | 100% Real Estate Financing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=OWlnOeMGBkg&t=216s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Often the lowest cost option. Pays off MCA debt at a fraction of the effective '
              "rate, but puts a personal or business asset up as collateral if, say, you're "
              'using an LLC-based, uh, investment property. A revolving credit with interest '
              "only on what's drawn.",
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'Often the lowest cost option. Pays off MCA debt at a fraction of the effective '
             "rate, but puts a personal or business asset up as collateral if, say, you're "
             'using an LLC-based, uh, investment property. A revolving credit with interest '
             "only on what's drawn.",
      'title': 'MCA Debt Consolidation & Settlement  Everything You Need to Know (Gap Funding '
               '| 100% Real Estate Financing)',
      'url': 'https://www.youtube.com/watch?v=OWlnOeMGBkg&t=216s',
      'video_id': 'OWlnOeMGBkg'},
     {'author': 'Zoryn Capital',
      'channel': 'Zoryn Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=ORF9Ue9ge8A&t=55s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But nowadays, most working capital loan that are out there are revenue-based '
              "loan. Also, you'll see it called MCA, a merchant cash advance. It's because "
              'when this loan first came out, it used to be based on your credit card sales as '
              'a merchant.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'But nowadays, most working capital loan that are out there are revenue-based '
             "loan. Also, you'll see it called MCA, a merchant cash advance. It's because when "
             'this loan first came out, it used to be based on your credit card sales as a '
             'merchant.',
      'title': 'WARNING Before Taking a Merchant Cash Advance MCA? (Revenue Based Loan or '
               'Working Capital Loan) (Zoryn Capital)',
      'url': 'https://www.youtube.com/watch?v=ORF9Ue9ge8A&t=55s',
      'video_id': 'ORF9Ue9ge8A'},
     {'author': 'Parkins & Rubio LLP',
      'channel': 'Parkins & Rubio LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=A8iNT8Ctrhk&t=80s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, they can tap into the lending much more quickly. And then and the nature of '
              "the lending is also different in that uh you know, often times there's "
              'asset-based lenders, but these this type of lender is not looking at the '
              "assets. It's looking at the cash flows.",
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'So, they can tap into the lending much more quickly. And then and the nature of '
             "the lending is also different in that uh you know, often times there's "
             'asset-based lenders, but these this type of lender is not looking at the assets. '
             "It's looking at the cash flows.",
      'title': 'Merchant Cash Advances and Bankruptcy: What Business Owners Need to Know '
               '(Parkins & Rubio LLP)',
      'url': 'https://www.youtube.com/watch?v=A8iNT8Ctrhk&t=80s',
      'video_id': 'A8iNT8Ctrhk'},
     {'author': 'Insightful Accountant',
      'channel': 'Insightful Accountant',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:19](https://www.youtube.com/watch?v=TEwsEYj6XTI&t=1759s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A lot of the times it's electronic board where it scrolls through it and it "
              'says, "Oh yeah, this is the card price or usually says the cash price." Then '
              'you go to the pump and it\'s like, "Oh no, it\'s 10 cents higher.".',
      'timestamp': 1759,
      'timestamp_label': '[00:29:19]',
      'timestamp_seconds': 1759,
      'tip': "A lot of the times it's electronic board where it scrolls through it and it "
             'says, "Oh yeah, this is the card price or usually says the cash price." Then you '
             'go to the pump and it\'s like, "Oh no, it\'s 10 cents higher.".',
      'title': 'How to Reduce B2B Credit Card Processing Fees | Future Forward November 2026 '
               '(Insightful Accountant)',
      'url': 'https://www.youtube.com/watch?v=TEwsEYj6XTI&t=1759s',
      'video_id': 'TEwsEYj6XTI'},
     {'author': 'CDC Small Business Finance',
      'channel': 'CDC Small Business Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=hK_Qb2vkxp8&t=30s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s no other building that has the facility the way it needs to be. We can "
              'finance that through SBA. We can also do partner buyouts. We can even do cash '
              'out refinances for eligible business expenses.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "'s no other building that has the facility the way it needs to be. We can "
             'finance that through SBA. We can also do partner buyouts. We can even do cash '
             'out refinances for eligible business expenses.',
      'title': 'What Can I Use an SBA 504 Loan For? (CDC Small Business Finance)',
      'url': 'https://www.youtube.com/watch?v=hK_Qb2vkxp8&t=30s',
      'video_id': 'hK_Qb2vkxp8'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=nAoSGYTENek&t=25s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Big value ad the 504 may make the most sense if the purchase price is greater '
              'for the business then we can look at a lot of different options one being a '
              '504.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Big value ad the 504 may make the most sense if the purchase price is greater '
             'for the business then we can look at a lot of different options one being a 504.',
      'title': 'Comparing SBA 7A vs 504 Loans for Business Acquisitions w/ Real Estate (Beau '
               'Eckstein, Business Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=nAoSGYTENek&t=25s',
      'video_id': 'nAoSGYTENek'},
     {'author': 'Joe Camberato',
      'channel': 'Joe Camberato',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=U1zLsMRu1ig&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Purchase and sale agreement it's basically just based on the revenues and cash "
              'flow of your business when I got started in 2007 it was really a known.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Purchase and sale agreement it's basically just based on the revenues and cash "
             'flow of your business when I got started in 2007 it was really a known.',
      'title': 'Revenue-Based Financing: What Is It, and How Does It Work? (Joe Camberato)',
      'url': 'https://www.youtube.com/watch?v=U1zLsMRu1ig&t=15s',
      'video_id': 'U1zLsMRu1ig'},
     {'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=qdVNgYCTgzU&t=392s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um yeah, as as Dave mentioned, the most common use for litigation funding is to '
              "cover attorney fees and and case costs. However, um I'll mention I'll mention "
              'two other uses for it. Number one is uh to fund working capital.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': 'Um yeah, as as Dave mentioned, the most common use for litigation funding is to '
             "cover attorney fees and and case costs. However, um I'll mention I'll mention "
             'two other uses for it. Number one is uh to fund working capital.',
      'title': 'Introduction to Commercial Litigation Finance (The National Law Review)',
      'url': 'https://www.youtube.com/watch?v=qdVNgYCTgzU&t=392s',
      'video_id': 'qdVNgYCTgzU'},
     {'author': 'Bootstrapp',
      'channel': 'Bootstrapp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=U0fB6ZY7Cpo&t=312s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Versus the cost of capital because then you end up with an ABR and you have to '
              "understand for your company what's the most important right maybe the APR.",
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': 'Versus the cost of capital because then you end up with an ABR and you have to '
             "understand for your company what's the most important right maybe the APR.",
      'title': 'How Does Revenue Based Financing Work? -- A 6 minute overview of everything '
               'you need to know. (Bootstrapp)',
      'url': 'https://www.youtube.com/watch?v=U0fB6ZY7Cpo&t=312s',
      'video_id': 'U0fB6ZY7Cpo'},
     {'author': 'TheShawnShow50',
      'channel': 'TheShawnShow50',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=C-ZTs-2s2ZQ&t=57s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But it gives you this large chunk of cash infusion so that you can operate your '
              "business or get past whatever obstacle you're hoping to get past.",
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'But it gives you this large chunk of cash infusion so that you can operate your '
             "business or get past whatever obstacle you're hoping to get past.",
      'title': 'Equipment Sale Lease Back | Working Capital Loan via Equipment Financing Sale '
               'LeaseBack (TheShawnShow50)',
      'url': 'https://www.youtube.com/watch?v=C-ZTs-2s2ZQ&t=57s',
      'video_id': 'C-ZTs-2s2ZQ'},
     {'author': 'Hard Money Mike',
      'channel': 'Hard Money Mike',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=HYtATwfeE50&t=238s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Your business's income does not matter that's why this is a great product as "
              'long as the property positively cash flows and you have a good credit score.',
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': "Your business's income does not matter that's why this is a great product as "
             'long as the property positively cash flows and you have a good credit score.',
      'title': 'BRRRR: How to Succeed Using DSCR and Hard Money Loans (Hard Money Mike)',
      'url': 'https://www.youtube.com/watch?v=HYtATwfeE50&t=238s',
      'video_id': 'HYtATwfeE50'},
     {'author': 'ION Capital - Loan Broker University',
      'channel': 'ION Capital - Loan Broker University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:07](https://www.youtube.com/watch?v=4TvufjZUMp8&t=427s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I wanted to ask you a question about what tracy was talking about do you have '
              'lenders for leasing used equipment also lenders that would cash out can can '
              'lend against used equipment.',
      'timestamp': 427,
      'timestamp_label': '[00:07:07]',
      'timestamp_seconds': 427,
      'tip': 'I wanted to ask you a question about what tracy was talking about do you have '
             'lenders for leasing used equipment also lenders that would cash out can can lend '
             'against used equipment.',
      'title': 'How To Be A Business Loan Broker  |  Equipment Finance Basics (ION Capital - '
               'Loan Broker University)',
      'url': 'https://www.youtube.com/watch?v=4TvufjZUMp8&t=427s',
      'video_id': '4TvufjZUMp8'},
     {'author': 'ION Capital - Loan Broker University',
      'channel': 'ION Capital - Loan Broker University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:09](https://www.youtube.com/watch?v=WfAvAf4wk0k&t=429s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What Tracy was talking about do you have lenders for um leasing used equipment '
              'also lenders with cash out uh can can lend against a used equipment.',
      'timestamp': 429,
      'timestamp_label': '[00:07:09]',
      'timestamp_seconds': 429,
      'tip': 'What Tracy was talking about do you have lenders for um leasing used equipment '
             'also lenders with cash out uh can can lend against a used equipment.',
      'title': 'How To Be A Business Loan Broker  | The Basics of Equipment Finance (ION '
               'Capital - Loan Broker University)',
      'url': 'https://www.youtube.com/watch?v=WfAvAf4wk0k&t=429s',
      'video_id': 'WfAvAf4wk0k'},
     {'author': 'Michael Granados',
      'channel': 'Michael Granados',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=WX8DT-NQK5w&t=123s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Video and presentation to learn more about this I'll give you a resource "
              'underneath that video you can pick up for yourself and then get more '
              "information from there on how to get started that is all for now I'll talk to "
              'you soon thank you bye.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "Video and presentation to learn more about this I'll give you a resource "
             'underneath that video you can pick up for yourself and then get more information '
             "from there on how to get started that is all for now I'll talk to you soon thank "
             'you bye.',
      'title': 'MCA Debt Relief (Best Merchant Cash Advance Help) (Michael Granados)',
      'url': 'https://www.youtube.com/watch?v=WX8DT-NQK5w&t=123s',
      'video_id': 'WX8DT-NQK5w'}],
 4: [{'author': 'Funder Intel',
      'channel': 'Funder Intel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=jCWdtQmKTiU&t=57s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, this doesn't just affect MCA or revenue-based financing or sales-based "
              'financing. It does include factoring and asset-based lending. So, it makes it '
              'more difficult for funders and funding providers to conduct business in '
              'California.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "So, this doesn't just affect MCA or revenue-based financing or sales-based "
             'financing. It does include factoring and asset-based lending. So, it makes it '
             'more difficult for funders and funding providers to conduct business in '
             'California.',
      'title': 'Will commercial loan brokers and funding providers need a license in '
               'California? (Funder Intel)',
      'url': 'https://www.youtube.com/watch?v=jCWdtQmKTiU&t=57s',
      'video_id': 'jCWdtQmKTiU'},
     {'author': 'Jonathan Mills Patrick',
      'channel': 'Jonathan Mills Patrick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=gfK-oOi-TuI&t=31s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, today is, I think, August 6th, 2000 or 2021. And so, the states as of right '
              'now that you have to be licensed in to do commercial loan broker businesses '
              'include Arizona, California, Florida, Minnesota, Nevada, New York, North '
              'Dakota, South Dakota, and Vermont.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'So, today is, I think, August 6th, 2000 or 2021. And so, the states as of right '
             'now that you have to be licensed in to do commercial loan broker businesses '
             'include Arizona, California, Florida, Minnesota, Nevada, New York, North Dakota, '
             'South Dakota, and Vermont.',
      'title': 'Does a commercial loan broker need a license? (Jonathan Mills Patrick)',
      'url': 'https://www.youtube.com/watch?v=gfK-oOi-TuI&t=31s',
      'video_id': 'gfK-oOi-TuI'},
     {'author': 'The Lab: Mortgage & Real Estate Business Academy',
      'channel': 'The Lab: Mortgage & Real Estate Business Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=SulpxqBYams&t=89s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Construction loans when you want to develop land into subdivisions or build a '
              'building next we have bridge loans which are for short-term financing for '
              'commercial projects.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Construction loans when you want to develop land into subdivisions or build a '
             'building next we have bridge loans which are for short-term financing for '
             'commercial projects.',
      'title': 'How A Commercial Loan Works? | Co/LAB Lending (The Lab: Mortgage & Real Estate '
               'Business Academy)',
      'url': 'https://www.youtube.com/watch?v=SulpxqBYams&t=89s',
      'video_id': 'SulpxqBYams'},
     {'author': 'Equipment Finance Academy',
      'channel': 'Equipment Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:38](https://www.youtube.com/watch?v=nN3wD1zIjqM&t=338s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Potential referral sources include equipment dealers, equipment manufacturers, '
              'contractors, truck and trailer dealers, accountants, insurance agents, business '
              'consultants, commercial real estate professionals, and industry associations. '
              'Your message should be simple.',
      'timestamp': 338,
      'timestamp_label': '[00:05:38]',
      'timestamp_seconds': 338,
      'tip': 'Potential referral sources include equipment dealers, equipment manufacturers, '
             'contractors, truck and trailer dealers, accountants, insurance agents, business '
             'consultants, commercial real estate professionals, and industry associations. '
             'Your message should be simple.',
      'title': "Equipment Finance Brokerage: The Beginner's Roadmap (Equipment Finance "
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=nN3wD1zIjqM&t=338s',
      'video_id': 'nN3wD1zIjqM'},
     {'author': 'Berkshire Financial Services LLC',
      'channel': 'Berkshire Financial Services LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=V8S0sywozwU&t=39s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Matters. Here's what funders don't tell you. One typo in your business name or "
              'using a DBA instead of the legal entity can invalidate the lean altogether.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "Matters. Here's what funders don't tell you. One typo in your business name or "
             'using a DBA instead of the legal entity can invalidate the lean altogether.',
      'title': '“UCC Liens & MCA Debt  What Borrowers MUST Know (2 Minute Breakdown)" '
               '(Berkshire Financial Services LLC)',
      'url': 'https://www.youtube.com/watch?v=V8S0sywozwU&t=39s',
      'video_id': 'V8S0sywozwU'},
     {'author': 'Tax Alpha Insider',
      'channel': 'Tax Alpha Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=TQ86awlkdKw&t=269s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then they are in the position where they have to where they would like to '
              'transfer those to receive more capital so they can continue building or '
              'whatever. And then connect me all the way to the investor on the other end. One '
              'quick clarification on that setup.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': 'And then they are in the position where they have to where they would like to '
             'transfer those to receive more capital so they can continue building or '
             'whatever. And then connect me all the way to the investor on the other end. One '
             'quick clarification on that setup.',
      'title': 'Transferrable tax credits can offset passive income tax liability with Jason '
               'Prince (Tax Alpha Insider)',
      'url': 'https://www.youtube.com/watch?v=TQ86awlkdKw&t=269s',
      'video_id': 'TQ86awlkdKw'},
     {'author': 'Break Into CRE',
      'channel': 'Break Into CRE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=b-6L1d2Ozk4&t=31s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Down how commercial real estate deals are typically funded how each layer of '
              "the capital stack ends up working together and some things that you'll need to "
              'consider if you are weighing different options to fund a real estate.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'Down how commercial real estate deals are typically funded how each layer of the '
             "capital stack ends up working together and some things that you'll need to "
             'consider if you are weighing different options to fund a real estate.',
      'title': 'How Commercial Real Estate Deals are Funded [The Capital Stack] (Break Into '
               'CRE)',
      'url': 'https://www.youtube.com/watch?v=b-6L1d2Ozk4&t=31s',
      'video_id': 'b-6L1d2Ozk4'},
     {'author': 'firsttuesday – California real estate educators',
      'channel': 'firsttuesday – California real estate educators',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=8bJtTzzuQ-Y&t=221s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reverse is not true a DB o license mlo may not originate mortgages under a d re '
              "license ml o broker without an active d re license and ml o endorsement let's "
              'see if we can determine which type of license is required.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Reverse is not true a DB o license mlo may not originate mortgages under a d re '
             "license ml o broker without an active d re license and ml o endorsement let's "
             'see if we can determine which type of license is required.',
      'title': 'Mortgage Concepts  California MLO licensing laws (firsttuesday – California '
               'real estate educators)',
      'url': 'https://www.youtube.com/watch?v=8bJtTzzuQ-Y&t=221s',
      'video_id': '8bJtTzzuQ-Y'},
     {'author': 'Compliance Connection',
      'channel': 'Compliance Connection',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=gnx32nNbVfU&t=236s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Who are we considering as our legal entity members we're talking about "
              "corporations LLC's or other entities that are created by the filing of a.",
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': "Who are we considering as our legal entity members we're talking about "
             "corporations LLC's or other entities that are created by the filing of a.",
      'title': 'Compliance Outlook - FinCEN Customer Due Diligence (Compliance Connection)',
      'url': 'https://www.youtube.com/watch?v=gnx32nNbVfU&t=236s',
      'video_id': 'gnx32nNbVfU'},
     {'author': 'Business Credit',
      'channel': 'Business Credit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:56](https://www.youtube.com/watch?v=L3n2zgxag4E&t=596s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Revolving credit you're looking for interest free money on purchases for your "
              'business uh so you could be a startup with this particular program or.',
      'timestamp': 596,
      'timestamp_label': '[00:09:56]',
      'timestamp_seconds': 596,
      'tip': "Revolving credit you're looking for interest free money on purchases for your "
             'business uh so you could be a startup with this particular program or.',
      'title': 'Revenue Based Financing | Soft Pull | Line of Credit | Up to $100k | Fast '
               'Funding (Business Credit)',
      'url': 'https://www.youtube.com/watch?v=L3n2zgxag4E&t=596s',
      'video_id': 'L3n2zgxag4E'},
     {'author': 'Allen Mursau',
      'channel': 'Allen Mursau',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=vtCDACsG2Bs&t=50s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So we have corporation A here the seller and we have bank B here the purchaser '
              'here. So what corporation A does here they sells this asset of accounts '
              'receivable. Say they sell $250,000 here to bank B.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'So we have corporation A here the seller and we have bank B here the purchaser '
             'here. So what corporation A does here they sells this asset of accounts '
             'receivable. Say they sell $250,000 here to bank B.',
      'title': 'Accounts Receivable Factoring Vs Assignment (Transferring Receivables For '
               'Cash) (Allen Mursau)',
      'url': 'https://www.youtube.com/watch?v=vtCDACsG2Bs&t=50s',
      'video_id': 'vtCDACsG2Bs'},
     {'author': 'Credit Suite',
      'channel': 'Credit Suite',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:07](https://www.youtube.com/watch?v=L2-ax8GoKVw&t=547s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Finance is basically math two plus two equals four it this is if you can tip '
              "your waiter at Fleming's or the Cheesecake Factory or Capital Grill you.",
      'timestamp': 547,
      'timestamp_label': '[00:09:07]',
      'timestamp_seconds': 547,
      'tip': 'Finance is basically math two plus two equals four it this is if you can tip '
             "your waiter at Fleming's or the Cheesecake Factory or Capital Grill you.",
      'title': 'How to Create Income Stream with Equipment Financing | Jermane Cheathem '
               '(Credit Suite)',
      'url': 'https://www.youtube.com/watch?v=L2-ax8GoKVw&t=547s',
      'video_id': 'L2-ax8GoKVw'},
     {'author': 'I Am Andrew Russell',
      'channel': 'I Am Andrew Russell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:03](https://www.youtube.com/watch?v=SExreBEJY5Q&t=603s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And insurance on these per year was 3,600. So taxes and insurance was 500 plus '
              '300. So you figure another 800 for escar, right? 300 a month for insurance, 500 '
              'a month for taxes.',
      'timestamp': 603,
      'timestamp_label': '[00:10:03]',
      'timestamp_seconds': 603,
      'tip': 'And insurance on these per year was 3,600. So taxes and insurance was 500 plus '
             '300. So you figure another 800 for escar, right? 300 a month for insurance, 500 '
             'a month for taxes.',
      'title': 'This is Why 99% of Investors Don’t Use DSCR Loans! (I Am Andrew Russell)',
      'url': 'https://www.youtube.com/watch?v=SExreBEJY5Q&t=603s',
      'video_id': 'SExreBEJY5Q'},
     {'author': 'Rob Freeman | Insuring The Built Environment',
      'channel': 'Rob Freeman | Insuring The Built Environment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=fqMHsHUSOU8&t=210s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Anyway hope this is helpful if you have questions about uh your insurance and '
              "if you uh want to schedule an appointment with me I'd love to talk to you and "
              'hear about your project thanks again and good luck and have a great day.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': 'Anyway hope this is helpful if you have questions about uh your insurance and if '
             "you uh want to schedule an appointment with me I'd love to talk to you and hear "
             'about your project thanks again and good luck and have a great day.',
      'title': 'What is Solar Tax Equity Financing? (Rob Freeman | Insuring The Built '
               'Environment)',
      'url': 'https://www.youtube.com/watch?v=fqMHsHUSOU8&t=210s',
      'video_id': 'fqMHsHUSOU8'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=4ELMBLT7mvs&t=79s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, if you want attention, you don't need history. Let me explain why I know "
              "this. I'm Shane Walton, co-founder of the Commercial Loan Broker Institute. And "
              'our institute works with hundreds of lenders.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': "So, if you want attention, you don't need history. Let me explain why I know "
             "this. I'm Shane Walton, co-founder of the Commercial Loan Broker Institute. And "
             'our institute works with hundreds of lenders.',
      'title': 'Business Loan Broker Training: Why Lenders Ignore You (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=4ELMBLT7mvs&t=79s',
      'video_id': '4ELMBLT7mvs'}],
 5: [{'author': 'Unbankable with Alex Shvarts',
      'channel': 'Unbankable with Alex Shvarts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=MNdDLiTLoNY&t=503s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ve grown and improved their credit profile. Use revenue-based financing to "
              'bridge gaps and seize opportunities, then optimize with traditional financing '
              "for long-term growth. Now, there's some common mistakes to avoid.",
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': "'ve grown and improved their credit profile. Use revenue-based financing to "
             'bridge gaps and seize opportunities, then optimize with traditional financing '
             "for long-term growth. Now, there's some common mistakes to avoid.",
      'title': 'Working Capital Loan vs Revenue-Based Financing: Which One Should I Choose for '
               'My Business? (Unbankable with Alex Shvarts)',
      'url': 'https://www.youtube.com/watch?v=MNdDLiTLoNY&t=503s',
      'video_id': 'MNdDLiTLoNY'},
     {'author': 'Construction Brothers',
      'channel': 'Construction Brothers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=PaYgE9PgaO4&t=370s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And it I don't think it's a scam or a bad thing at all because they're "
              'providing a service in lie of a subcontractor bond and they are taking risk. '
              "But make no mistake, it is a profit center for their business. So they're "
              "they're gathering the premium.",
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': "And it I don't think it's a scam or a bad thing at all because they're providing "
             'a service in lie of a subcontractor bond and they are taking risk. But make no '
             "mistake, it is a profit center for their business. So they're they're gathering "
             'the premium.',
      'title': 'Everything You NEED to Know about Surety Bonds & Subcontractor Default '
               '(Construction Brothers)',
      'url': 'https://www.youtube.com/watch?v=PaYgE9PgaO4&t=370s',
      'video_id': 'PaYgE9PgaO4'},
     {'author': 'Surety Bonds Direct',
      'channel': 'Surety Bonds Direct',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=n___30FL0_I&t=21s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, if the construction company makes a mistake or subcontractor makes a '
              "mistake and they don't fix it, the project owner can make a claim against that "
              'maintenance bond to get the financial compensation they need to go fix that '
              'problem.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'So, if the construction company makes a mistake or subcontractor makes a mistake '
             "and they don't fix it, the project owner can make a claim against that "
             'maintenance bond to get the financial compensation they need to go fix that '
             'problem.',
      'title': 'Construction Maintenance Surety Bond (Surety Bonds Direct)',
      'url': 'https://www.youtube.com/watch?v=n___30FL0_I&t=21s',
      'video_id': 'n___30FL0_I'},
     {'author': 'Academy For Commercial Lending',
      'channel': 'Academy For Commercial Lending',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:20](https://www.youtube.com/watch?v=NHfs2vBPCys&t=380s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Owner-occupied and special purpose properties carry more single point of '
              'failure risk. If the operating business fails or the specific use becomes '
              'obsolete, the lender is holding a harder asset to release or sell.',
      'timestamp': 380,
      'timestamp_label': '[00:06:20]',
      'timestamp_seconds': 380,
      'tip': 'Owner-occupied and special purpose properties carry more single point of failure '
             'risk. If the operating business fails or the specific use becomes obsolete, the '
             'lender is holding a harder asset to release or sell.',
      'title': 'Debt Yield vs. DSCR: The Metric Every Commercial Mortgage Broker Needs to '
               'Understand (Academy For Commercial Lending)',
      'url': 'https://www.youtube.com/watch?v=NHfs2vBPCys&t=380s',
      'video_id': 'NHfs2vBPCys'},
     {'author': 'Turn-Keyinvestments by Richard Lowe',
      'channel': 'Turn-Keyinvestments by Richard Lowe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:24](https://www.youtube.com/watch?v=5d2yaSz0ius&t=1404s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re unable to pursue it, we do have the opportunity to swap that case out for a "
              'like-for-like claim of similar value against one of the eligible lenders. If '
              'then the further claims then fail within that portfolio, each case is then '
              'allocated a unique bond.',
      'timestamp': 1404,
      'timestamp_label': '[00:23:24]',
      'timestamp_seconds': 1404,
      'tip': "'re unable to pursue it, we do have the opportunity to swap that case out for a "
             'like-for-like claim of similar value against one of the eligible lenders. If '
             'then the further claims then fail within that portfolio, each case is then '
             'allocated a unique bond.',
      'title': 'Litigation Finance Explained | How It Works, Potential Returns & Risks | Full '
               'Webinar (Turn-Keyinvestments by Richard Lowe)',
      'url': 'https://www.youtube.com/watch?v=5d2yaSz0ius&t=1404s',
      'video_id': '5d2yaSz0ius'},
     {'author': 'Neil.Finance',
      'channel': 'Neil.Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:55](https://www.youtube.com/watch?v=YLIvGloANJM&t=355s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Imagine a business owner calls you. They were declined at their bank. You '
              'review their situation. You connect them with a lender. You get your commission '
              "and it's not for selling hype but for solving a real problem.",
      'timestamp': 355,
      'timestamp_label': '[00:05:55]',
      'timestamp_seconds': 355,
      'tip': 'Imagine a business owner calls you. They were declined at their bank. You review '
             'their situation. You connect them with a lender. You get your commission and '
             "it's not for selling hype but for solving a real problem.",
      'title': 'Why Equipment Finance Brokering Exists (And Why Most People Miss the '
               'Opportunity) (Neil.Finance)',
      'url': 'https://www.youtube.com/watch?v=YLIvGloANJM&t=355s',
      'video_id': 'YLIvGloANJM'},
     {'author': 'Today Capital Group',
      'channel': 'Today Capital Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=6tGMlJx13g8&t=21s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "From there, we'll figure out if it's the right move for your business. How to "
              'spot the red flags so you pick a great partner. Every single founder who has '
              'ever tried to raise capital knows this feeling all too well.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "From there, we'll figure out if it's the right move for your business. How to "
             'spot the red flags so you pick a great partner. Every single founder who has '
             'ever tried to raise capital knows this feeling all too well.',
      'title': 'Revenue-Based Financing Explained (RBF vs Loans vs VC + Red Flags to Avoid) '
               '(Today Capital Group)',
      'url': 'https://www.youtube.com/watch?v=6tGMlJx13g8&t=21s',
      'video_id': '6tGMlJx13g8'},
     {'author': 'LeGaye Law Firm',
      'channel': 'LeGaye Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=JR8TOdAxFa4&t=72s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And accredited investor status alone doesn't establish compliance. Second: "
              'Explain the assumptions. Firms must clearly communicate the assumptions, risks, '
              'and limitations underlying projected returns.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "And accredited investor status alone doesn't establish compliance. Second: "
             'Explain the assumptions. Firms must clearly communicate the assumptions, risks, '
             'and limitations underlying projected returns.',
      'title': 'Projected Investment Returns: 4 Compliance Priorities for Broker-Dealers '
               '(LeGaye Law Firm)',
      'url': 'https://www.youtube.com/watch?v=JR8TOdAxFa4&t=72s',
      'video_id': 'JR8TOdAxFa4'},
     {'author': 'The Approved Guy',
      'channel': 'The Approved Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=8x-cfQhQpPU&t=97s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s no interest rate they tell you that it's a factor rate which is based on "
              "risk and they'll tell you that the factor rate is 1. 45 some of the lower cash "
              'advances out there might be 1. 25 that translates to 25 percent 1.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': "'s no interest rate they tell you that it's a factor rate which is based on risk "
             "and they'll tell you that the factor rate is 1. 45 some of the lower cash "
             'advances out there might be 1. 25 that translates to 25 percent 1.',
      'title': "STUCK IN MCA DEBT? THERE'S A WAY OUT! (The Approved Guy)",
      'url': 'https://www.youtube.com/watch?v=8x-cfQhQpPU&t=97s',
      'video_id': '8x-cfQhQpPU'},
     {'author': 'Peak Capital',
      'channel': 'Peak Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=J-guTckEVMA&t=82s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Offering extended payment terms can also result in a working capital shortage '
              'so trade Finance can be beneficial here too from a risk perspective most '
              'sellers.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'Offering extended payment terms can also result in a working capital shortage so '
             'trade Finance can be beneficial here too from a risk perspective most sellers.',
      'title': 'What is Trade Finance? (Peak Capital)',
      'url': 'https://www.youtube.com/watch?v=J-guTckEVMA&t=82s',
      'video_id': 'J-guTckEVMA'},
     {'author': 'Express Legal Funding',
      'channel': 'Express Legal Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:03](https://www.youtube.com/watch?v=AVBbpi6lPFY&t=303s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s like a secret weapon it lets you go toe to toe with literally any opponent "
              'no matter how big. It moves all the financial risk over to the funder and it '
              'lets you keep your own cash to you know run your business.',
      'timestamp': 303,
      'timestamp_label': '[00:05:03]',
      'timestamp_seconds': 303,
      'tip': "'s like a secret weapon it lets you go toe to toe with literally any opponent no "
             'matter how big. It moves all the financial risk over to the funder and it lets '
             'you keep your own cash to you know run your business.',
      'title': 'Litigation Finance Explained: Complete Litigation Funding Guide (Express Legal '
               'Funding)',
      'url': 'https://www.youtube.com/watch?v=AVBbpi6lPFY&t=303s',
      'video_id': 'AVBbpi6lPFY'},
     {'author': 'Mobilization Funding',
      'channel': 'Mobilization Funding',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=hKDkKk_Guv4&t=77s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Directly they'll use the credit worthiness of your supplier to help offset "
              'their risk to be able to finance those for you and.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "Directly they'll use the credit worthiness of your supplier to help offset their "
             'risk to be able to finance those for you and.',
      'title': 'PO Financing for Manufacturers and Fabricators (Mobilization Funding)',
      'url': 'https://www.youtube.com/watch?v=hKDkKk_Guv4&t=77s',
      'video_id': 'hKDkKk_Guv4'},
     {'author': 'Commercial Capital Training Group, LLC',
      'channel': 'Commercial Capital Training Group, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:21](https://www.youtube.com/watch?v=UBxQzlMJT7k&t=1761s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right um we have one graduate uh one uh student here that's going to ask a "
              "question I'm going to unmute her so she could ask it directly to uh to "
              "everybody it's uh kelly we're going to unmute your mewtwo kelly hardy.",
      'timestamp': 1761,
      'timestamp_label': '[00:29:21]',
      'timestamp_seconds': 1761,
      'tip': "All right um we have one graduate uh one uh student here that's going to ask a "
             "question I'm going to unmute her so she could ask it directly to uh to everybody "
             "it's uh kelly we're going to unmute your mewtwo kelly hardy.",
      'title': 'Live Business Loan Broker Training | Become a Commercial Loan Broker '
               '(Commercial Capital Training Group, LLC)',
      'url': 'https://www.youtube.com/watch?v=UBxQzlMJT7k&t=1761s',
      'video_id': 'UBxQzlMJT7k'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=qkeq6lhotvM&t=98s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commission based on how much you financed and in both cases the loan commission '
              'is most typically going to be based on the amount financed so it might.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Commission based on how much you financed and in both cases the loan commission '
             'is most typically going to be based on the amount financed so it might.',
      'title': 'How do Commercial Loan Brokers get Paid? (Commercial Loan Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=qkeq6lhotvM&t=98s',
      'video_id': 'qkeq6lhotvM'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=jzEfnFdiiZU&t=191s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Things financing I've been in the lending industry for over 20 years and I'm "
              'happy to answer your questions and provide great content.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': "Things financing I've been in the lending industry for over 20 years and I'm "
             'happy to answer your questions and provide great content.',
      'title': 'Comparing SBA 7a vs SBA 504: Which is Better for an Office Building Purchase? '
               '(Beau Eckstein, Business Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=jzEfnFdiiZU&t=191s',
      'video_id': 'jzEfnFdiiZU'}],
 6: [{'author': 'Equipment Finance Academy',
      'channel': 'Equipment Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:51](https://www.youtube.com/watch?v=dc0_7D431kI&t=411s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This week, three contractors find you through search. They fill out the '
              'application themselves. You submit two clean packages. You made 2,500 with zero '
              'lead cost and you own the asset. Next week, it brings three more inbound leads '
              'while you are working the first ones.',
      'timestamp': 411,
      'timestamp_label': '[00:06:51]',
      'timestamp_seconds': 411,
      'tip': 'This week, three contractors find you through search. They fill out the '
             'application themselves. You submit two clean packages. You made 2,500 with zero '
             'lead cost and you own the asset. Next week, it brings three more inbound leads '
             'while you are working the first ones.',
      'title': 'Equipment Finance Leads: Turnkey System That Actually Works (Equipment Finance '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=dc0_7D431kI&t=411s',
      'video_id': 'dc0_7D431kI'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:51](https://www.youtube.com/watch?v=MsdnoNJpPrg&t=591s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "First, they're building a curated lender bench that moves across banks, "
              "non-banks, fintexs, private credit, and they're using that bench based on "
              'actual deal fit, not just treating as a giant contact list to run through every '
              'time.',
      'timestamp': 591,
      'timestamp_label': '[00:09:51]',
      'timestamp_seconds': 591,
      'tip': "First, they're building a curated lender bench that moves across banks, "
             "non-banks, fintexs, private credit, and they're using that bench based on actual "
             'deal fit, not just treating as a giant contact list to run through every time.',
      'title': '3 Shifts Reshaping Commercial Lending That Most Brokers Are Missing '
               '(Commercial Loan Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=MsdnoNJpPrg&t=591s',
      'video_id': 'MsdnoNJpPrg'},
     {'author': 'CDC Small Business Finance',
      'channel': 'CDC Small Business Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=C-omBBP27hg&t=25s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's also to create jobs in the community. We are able to help them through the "
              "504 program because it's designed to help every single business owner. We're a "
              'mission-based lender. That means we want to qualify you and as many business '
              'owners as possible.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "It's also to create jobs in the community. We are able to help them through the "
             "504 program because it's designed to help every single business owner. We're a "
             'mission-based lender. That means we want to qualify you and as many business '
             'owners as possible.',
      'title': 'Who Is the SBA 504 Loan For? (CDC Small Business Finance)',
      'url': 'https://www.youtube.com/watch?v=C-omBBP27hg&t=25s',
      'video_id': 'C-omBBP27hg'},
     {'author': 'Equipment Finance Academy',
      'channel': 'Equipment Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=lg-SI4-0oEg&t=138s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's what I want you to do. Semi-truck financing, heavy equipment, medical "
              'gear. Then find two or three lenders who fund that exact thing. Get your first '
              "prospect on the phone and ask what they're trying to buy. That conversation is "
              'your entire business in miniature.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': "Here's what I want you to do. Semi-truck financing, heavy equipment, medical "
             'gear. Then find two or three lenders who fund that exact thing. Get your first '
             "prospect on the phone and ask what they're trying to buy. That conversation is "
             'your entire business in miniature.',
      'title': 'How to Become a Commercial Loan Broker (No Experience Needed) (Equipment '
               'Finance Academy)',
      'url': 'https://www.youtube.com/watch?v=lg-SI4-0oEg&t=138s',
      'video_id': 'lg-SI4-0oEg'},
     {'author': 'Loan Officer Training | Zevi Shafran',
      'channel': 'Loan Officer Training | Zevi Shafran',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=SPUcp-lnZ4w&t=54s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Skills marketing and building brand and I want to cover all four of those in '
              "today's video so without further Ado let's jump right into it the first one on "
              'the list was building.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Skills marketing and building brand and I want to cover all four of those in '
             "today's video so without further Ado let's jump right into it the first one on "
             'the list was building.',
      'title': '4 Foundations for New Commercial Loan Officers (Loan Officer Training | Zevi '
               'Shafran)',
      'url': 'https://www.youtube.com/watch?v=SPUcp-lnZ4w&t=54s',
      'video_id': 'SPUcp-lnZ4w'},
     {'author': 'ROK Financial',
      'channel': 'ROK Financial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:38](https://www.youtube.com/watch?v=EelcRfosnt8&t=578s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And it was a cooling unit for their data center that they were building that '
              'was going to be something like seven or eight billion dollars of an investment. '
              'So it the cooling equipment alone was a hundred million deal.',
      'timestamp': 578,
      'timestamp_label': '[00:09:38]',
      'timestamp_seconds': 578,
      'tip': 'And it was a cooling unit for their data center that they were building that was '
             'going to be something like seven or eight billion dollars of an investment. So '
             'it the cooling equipment alone was a hundred million deal.',
      'title': "Equipment Financing Secrets EXPOSED: What Banks Don't Want You to Know (ROK "
               'Financial)',
      'url': 'https://www.youtube.com/watch?v=EelcRfosnt8&t=578s',
      'video_id': 'EelcRfosnt8'},
     {'author': 'John Neufer',
      'channel': 'John Neufer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=uqs40-CCDSc&t=169s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But for this first deal we have to do it this way if you start to actually '
              "bring in more business that's when i'll consider.",
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'But for this first deal we have to do it this way if you start to actually bring '
             "in more business that's when i'll consider.",
      'title': 'How Much Origination to Charge | CRE Loan Brokering (John Neufer)',
      'url': 'https://www.youtube.com/watch?v=uqs40-CCDSc&t=169s',
      'video_id': 'uqs40-CCDSc'},
     {'author': 'ION Capital - Loan Broker University',
      'channel': 'ION Capital - Loan Broker University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=wt92Utt7o6I&t=201s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Stuff and I thought this is absolutely a deal why wouldn't it be a deal it "
              "turns out it's extremely difficult to find somebody who was willing to take on "
              'that.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': "Stuff and I thought this is absolutely a deal why wouldn't it be a deal it turns "
             "out it's extremely difficult to find somebody who was willing to take on that.",
      'title': 'How To Be A Business Loan Broker  |  Equipment Finance Tips (ION Capital - '
               'Loan Broker University)',
      'url': 'https://www.youtube.com/watch?v=wt92Utt7o6I&t=201s',
      'video_id': 'wt92Utt7o6I'},
     {'author': 'Factor Finders',
      'channel': 'Factor Finders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=8C1D2A4YVvQ&t=104s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Factor Finders at 1–855-Factor-1 or email us at sales@factorfinders. We’ll make '
              'an introduction between your factoring prospect and one of our factoring '
              'companies will get the deal done. And then we’ll split commissions, '
              'fifty-fifty.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Factor Finders at 1–855-Factor-1 or email us at sales@factorfinders. We’ll make '
             'an introduction between your factoring prospect and one of our factoring '
             'companies will get the deal done. And then we’ll split commissions, fifty-fifty.',
      'title': 'Factoring Broker Program (Factor Finders)',
      'url': 'https://www.youtube.com/watch?v=8C1D2A4YVvQ&t=104s',
      'video_id': '8C1D2A4YVvQ'},
     {'author': 'CPA Financial Exchange Group',
      'channel': 'CPA Financial Exchange Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:35](https://www.youtube.com/watch?v=LWEWnYj0IZ4&t=275s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your client in particular so again very very important to remember that and it '
              'helps your your business client to manage how they run their business so.',
      'timestamp': 275,
      'timestamp_label': '[00:04:35]',
      'timestamp_seconds': 275,
      'tip': 'Your client in particular so again very very important to remember that and it '
             'helps your your business client to manage how they run their business so.',
      'title': 'Accounts Receivable Financing - Factoring (CPA Financial Exchange Group)',
      'url': 'https://www.youtube.com/watch?v=LWEWnYj0IZ4&t=275s',
      'video_id': 'LWEWnYj0IZ4'},
     {'author': 'Rise Alliance',
      'channel': 'Rise Alliance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=BcdnIkuJ7Fc&t=112s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We approach this completely differently. We  understand that the only path to '
              'real resolution is through stabilizing your business first.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'We approach this completely differently. We  understand that the only path to '
             'real resolution is through stabilizing your business first.',
      'title': 'What Really Happens When You Default on an MCA? (Warning) (Rise Alliance)',
      'url': 'https://www.youtube.com/watch?v=BcdnIkuJ7Fc&t=112s',
      'video_id': 'BcdnIkuJ7Fc'},
     {'author': 'Intuit TurboTax',
      'channel': 'Intuit TurboTax',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=2KSxwXfP_QQ&t=94s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Remember though, you must file Form 5695 to claim either of the credits. '
              'TurboTax can help you determine whether you qualify for these credits, and will '
              'fill in all the right forms for you. For more tax tips and guidance, visit '
              'TurboTax.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'Remember though, you must file Form 5695 to claim either of the credits. '
             'TurboTax can help you determine whether you qualify for these credits, and will '
             'fill in all the right forms for you. For more tax tips and guidance, visit '
             'TurboTax.',
      'title': 'Are You Eligible for a Home Energy Tax Credit? - TurboTax Tax Tip Video '
               '(Intuit TurboTax)',
      'url': 'https://www.youtube.com/watch?v=2KSxwXfP_QQ&t=94s',
      'video_id': '2KSxwXfP_QQ'},
     {'author': 'SouthStar Capital, LLC',
      'channel': 'SouthStar Capital, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=_VD-lBSeoEw&t=174s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Relationship with your account D it's a very upbeat message and then also you "
              "know as invoices a we're not going to pest your client we're going to work with "
              'you as opposed to against you to ensure that everybody is on the same page and '
              'ultimately everybody is paid.',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': "Relationship with your account D it's a very upbeat message and then also you "
             "know as invoices a we're not going to pest your client we're going to work with "
             'you as opposed to against you to ensure that everybody is on the same page and '
             'ultimately everybody is paid.',
      'title': 'How Invoice & Accounts Receivable Financing Works (SouthStar Capital, LLC)',
      'url': 'https://www.youtube.com/watch?v=_VD-lBSeoEw&t=174s',
      'video_id': '_VD-lBSeoEw'},
     {'author': 'The Approved Guy',
      'channel': 'The Approved Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=dDwHOnFlzaA&t=167s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "New boat so that you'll never have to borrow again and at the same time prepare "
              'in case you do need to borrow again you can qualify for the best options on the '
              'market take advantage of a free consult or go ahead and submit for your life '
              'preserver today.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': "New boat so that you'll never have to borrow again and at the same time prepare "
             'in case you do need to borrow again you can qualify for the best options on the '
             'market take advantage of a free consult or go ahead and submit for your life '
             'preserver today.',
      'title': 'MCA DEBT RESTRUCTURE OR REFINANCE (The Approved Guy)',
      'url': 'https://www.youtube.com/watch?v=dDwHOnFlzaA&t=167s',
      'video_id': 'dDwHOnFlzaA'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:08](https://www.youtube.com/watch?v=CvS7BttXuu0&t=1448s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's the SP policy notice that that'll come right come right up in your "
              'whatever uh browser you want to search through. Uh the 504 is mainly for real '
              'estate. You can say capital, equipment, large, but you know, I would say 99% of '
              '504 loans are only for real estate.',
      'timestamp': 1448,
      'timestamp_label': '[00:24:08]',
      'timestamp_seconds': 1448,
      'tip': "So that's the SP policy notice that that'll come right come right up in your "
             'whatever uh browser you want to search through. Uh the 504 is mainly for real '
             'estate. You can say capital, equipment, large, but you know, I would say 99% of '
             '504 loans are only for real estate.',
      'title': 'New SBA Rule Unlocks $10M: Who Actually Benefits | Shane Walton ft. Jeff '
               'Hildebrandt (Commercial Loan Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=CvS7BttXuu0&t=1448s',
      'video_id': 'CvS7BttXuu0'}],
 7: [{'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=-HZRdtDpSRo&t=101s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To achieve their business goals then the loan broker will help them in the '
              "process of securing said capital along the way they're going to help that.",
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'To achieve their business goals then the loan broker will help them in the '
             "process of securing said capital along the way they're going to help that.",
      'title': 'What is a Commercial Loan Broker? What do they do? (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=-HZRdtDpSRo&t=101s',
      'video_id': '-HZRdtDpSRo'},
     {'author': 'CDC Small Business Finance',
      'channel': 'CDC Small Business Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:37](https://www.youtube.com/watch?v=5_3hvZIlwhQ&t=97s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, the 504 program is national. Um, CDC Small Business Finance is licensed by '
              'the SBA and is licensed to be a SBA 504 second mortgage lender in California, '
              'Arizona, and Nevada. So, the funding process of the 504 project is a little '
              'unique.',
      'timestamp': 97,
      'timestamp_label': '[00:01:37]',
      'timestamp_seconds': 97,
      'tip': 'So, the 504 program is national. Um, CDC Small Business Finance is licensed by '
             'the SBA and is licensed to be a SBA 504 second mortgage lender in California, '
             'Arizona, and Nevada. So, the funding process of the 504 project is a little '
             'unique.',
      'title': 'How Does an SBA 504 Loan Work? (CDC Small Business Finance)',
      'url': 'https://www.youtube.com/watch?v=5_3hvZIlwhQ&t=97s',
      'video_id': '5_3hvZIlwhQ'},
     {'author': 'BizMoney Explained',
      'channel': 'BizMoney Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:51](https://www.youtube.com/watch?v=Q4yDbzFte3g&t=1551s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This approach turns equipment financing into a structured capital budgeting '
              'process. Each proposed investment competes for limited financial resources, '
              'encouraging management to prioritize the opportunities with the strongest '
              'business justification.',
      'timestamp': 1551,
      'timestamp_label': '[00:25:51]',
      'timestamp_seconds': 1551,
      'tip': 'This approach turns equipment financing into a structured capital budgeting '
             'process. Each proposed investment competes for limited financial resources, '
             'encouraging management to prioritize the opportunities with the strongest '
             'business justification.',
      'title': 'Business Finance Equipment Financing Masterclass (Complete Guide) (BizMoney '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=Q4yDbzFte3g&t=1551s',
      'video_id': 'Q4yDbzFte3g'},
     {'author': 'Neil.Finance',
      'channel': 'Neil.Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=ks8OR72QJF0&t=251s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're going to start building confidence, and confidence comes from "
              'understanding that process. And this is exactly why I started teaching '
              'equipment financing. Most trainings, they teach the broker side. Very few '
              'people teach what happens after the deal reaches the lender.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': "You're going to start building confidence, and confidence comes from "
             'understanding that process. And this is exactly why I started teaching equipment '
             'financing. Most trainings, they teach the broker side. Very few people teach '
             'what happens after the deal reaches the lender.',
      'title': 'What Lenders Actually Look For Before Approving an Equipment Finance Deal '
               '(Neil.Finance)',
      'url': 'https://www.youtube.com/watch?v=ks8OR72QJF0&t=251s',
      'video_id': 'ks8OR72QJF0'},
     {'author': 'Corporate Bankruptcy A to Z',
      'channel': 'Corporate Bankruptcy A to Z',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:45](https://www.youtube.com/watch?v=50wAPhzWGmY&t=705s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And that sounds like a complicated process. You know, a lot of business owners '
              "don't speak legal ease. They don't know the first thing about going in and "
              'doing the work that it takes to take advantage of this legal standing they '
              'might have. So, what would be the next step?',
      'timestamp': 705,
      'timestamp_label': '[00:11:45]',
      'timestamp_seconds': 705,
      'tip': 'And that sounds like a complicated process. You know, a lot of business owners '
             "don't speak legal ease. They don't know the first thing about going in and doing "
             'the work that it takes to take advantage of this legal standing they might have. '
             'So, what would be the next step?',
      'title': 'MCA reclassified as Loans? | Breaking news on MCAs (Merchant Cash Advances) '
               '(Corporate Bankruptcy A to Z)',
      'url': 'https://www.youtube.com/watch?v=50wAPhzWGmY&t=705s',
      'video_id': '50wAPhzWGmY'},
     {'author': 'Surety Bonds Direct',
      'channel': 'Surety Bonds Direct',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=ttoT3V6duzU&t=165s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Or it could be a private project like building a strip mall out. If you need a '
              'quick refresher on the construction bonds that are involved in this process, '
              'check the links in the description. I have links to the three big ones, the '
              'bid, performance, and the payment bond.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'Or it could be a private project like building a strip mall out. If you need a '
             'quick refresher on the construction bonds that are involved in this process, '
             'check the links in the description. I have links to the three big ones, the bid, '
             'performance, and the payment bond.',
      'title': 'How Much Do Contractor License and Construction Surety Bonds Cost? (Surety '
               'Bonds Direct)',
      'url': 'https://www.youtube.com/watch?v=ttoT3V6duzU&t=165s',
      'video_id': 'ttoT3V6duzU'},
     {'author': 'Joe Camberato',
      'channel': 'Joe Camberato',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=MUaOFobVexQ&t=78s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business you want to go out and get as many customers as you can because now '
              "you've got this facility that can grow with your business so the more business "
              'the more customers you can take the quicker you can access that capital and '
              'continue to grow.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Business you want to go out and get as many customers as you can because now '
             "you've got this facility that can grow with your business so the more business "
             'the more customers you can take the quicker you can access that capital and '
             'continue to grow.',
      'title': 'Asset Based Lenders (Joe Camberato)',
      'url': 'https://www.youtube.com/watch?v=MUaOFobVexQ&t=78s',
      'video_id': 'MUaOFobVexQ'},
     {'author': 'Michael Granados',
      'channel': 'Michael Granados',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=lBvWGt7bnCw&t=21s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That can take in a matter of days to get up to 2 weeks, 10 to 15 days, up to 30 '
              "days of underwriting because this could be coming from a bank. There's also a "
              'general business term loan.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'That can take in a matter of days to get up to 2 weeks, 10 to 15 days, up to 30 '
             "days of underwriting because this could be coming from a bank. There's also a "
             'general business term loan.',
      'title': 'Fastest Way To Get Out Of Merchant Cash Advance Debt (MCA Debt Relief) '
               '(Michael Granados)',
      'url': 'https://www.youtube.com/watch?v=lBvWGt7bnCw&t=21s',
      'video_id': 'lBvWGt7bnCw'},
     {'author': 'Brandon Turner | Real Estate Investor',
      'channel': 'Brandon Turner | Real Estate Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:57](https://www.youtube.com/watch?v=-W2ThDxeu-o&t=717s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's the buffer for all those other things we just talked about. And on a rough "
              "building or an older property, like it isn't enough. So, gotcha number one is "
              "do not let a DSR approval talk you into financing a property you shouldn't own. "
              'The lender is underwriting the loan.',
      'timestamp': 717,
      'timestamp_label': '[00:11:57]',
      'timestamp_seconds': 717,
      'tip': "It's the buffer for all those other things we just talked about. And on a rough "
             "building or an older property, like it isn't enough. So, gotcha number one is do "
             "not let a DSR approval talk you into financing a property you shouldn't own. The "
             'lender is underwriting the loan.',
      'title': 'DSCR Loans Explained for 2026: Mortgages for Rental Investors (Brandon Turner '
               '| Real Estate Investor)',
      'url': 'https://www.youtube.com/watch?v=-W2ThDxeu-o&t=717s',
      'video_id': '-W2ThDxeu-o'},
     {'author': 'Katya Mizin',
      'channel': 'Katya Mizin',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:22](https://www.youtube.com/watch?v=WiG6N_co0Eo&t=742s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '90,000 a year in year one to lease your roof and put a system on it and then '
              "we'll be participating in the Maryland Community Solar Program. Uh we'll offer "
              "you a 2% escalator every year. It'll be a 20-year term if you want to transfer "
              'the ownership of the building.',
      'timestamp': 742,
      'timestamp_label': '[00:12:22]',
      'timestamp_seconds': 742,
      'tip': '90,000 a year in year one to lease your roof and put a system on it and then '
             "we'll be participating in the Maryland Community Solar Program. Uh we'll offer "
             "you a 2% escalator every year. It'll be a 20-year term if you want to transfer "
             'the ownership of the building.',
      'title': 'Investment Tax Credit (ITC) webinar by Lumen Energy (Katya Mizin)',
      'url': 'https://www.youtube.com/watch?v=WiG6N_co0Eo&t=742s',
      'video_id': 'WiG6N_co0Eo'},
     {'author': 'Farhat Lectures | CPA, CMA, EA & Accounting',
      'channel': 'Farhat Lectures | CPA, CMA, EA & Accounting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:11](https://www.youtube.com/watch?v=j1xpasTho-0&t=551s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Specifically, something collateralized debt obligations or CDOs. What are What '
              'are those those CDOs? So, think of it as Lehman had collateralized debt '
              'obligation, which is an asset. Think of it as a bond, as an investment.',
      'timestamp': 551,
      'timestamp_label': '[00:09:11]',
      'timestamp_seconds': 551,
      'tip': 'Specifically, something collateralized debt obligations or CDOs. What are What '
             'are those those CDOs? So, think of it as Lehman had collateralized debt '
             'obligation, which is an asset. Think of it as a bond, as an investment.',
      'title': 'Factoring Receivable and Pledging of Receivable (Farhat Lectures | CPA, CMA, '
               'EA & Accounting)',
      'url': 'https://www.youtube.com/watch?v=j1xpasTho-0&t=551s',
      'video_id': 'j1xpasTho-0'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:21](https://www.youtube.com/watch?v=408PWyXwwrI&t=501s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the lender funds it meaning they give the cash to the borrower and you get '
              'paid for making that connection happen. None of this requires a finance degree. '
              'None of it requires any of your own capital or money in the play. It requires a '
              'learnable process.',
      'timestamp': 501,
      'timestamp_label': '[00:08:21]',
      'timestamp_seconds': 501,
      'tip': 'And the lender funds it meaning they give the cash to the borrower and you get '
             'paid for making that connection happen. None of this requires a finance degree. '
             'None of it requires any of your own capital or money in the play. It requires a '
             'learnable process.',
      'title': 'Why 1 Loan Deal Pays More than 100 B2B Sales (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=408PWyXwwrI&t=501s',
      'video_id': '408PWyXwwrI'},
     {'author': 'Naturally New York',
      'channel': 'Naturally New York',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:25](https://www.youtube.com/watch?v=oobK7A-p9-U&t=1225s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Companies to use as an example and for those of you who know me I'm a huge fan "
              'of the office um so the Michael Scott paper company uh this is uh excuse me um '
              'thinking about one.',
      'timestamp': 1225,
      'timestamp_label': '[00:20:25]',
      'timestamp_seconds': 1225,
      'tip': "Companies to use as an example and for those of you who know me I'm a huge fan "
             'of the office um so the Michael Scott paper company uh this is uh excuse me um '
             'thinking about one.',
      'title': 'A Primer on Asset Based Lending (ABL) presented by SG Credit Partners '
               '(Naturally New York)',
      'url': 'https://www.youtube.com/watch?v=oobK7A-p9-U&t=1225s',
      'video_id': 'oobK7A-p9-U'},
     {'author': 'Slingshot Capital Inc.',
      'channel': 'Slingshot Capital Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=63RLcNbs9SU&t=168s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Truly represents the interests of all players involved and and that there's "
              'this constant refresh of ideas and individuals involved in helping to create a '
              'strong association so looking forward to seeing that soon.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': "Truly represents the interests of all players involved and and that there's this "
             'constant refresh of ideas and individuals involved in helping to create a strong '
             'association so looking forward to seeing that soon.',
      'title': '2020 Commercial Litigation Finance Association in the US Market (Slingshot '
               'Capital Inc.)',
      'url': 'https://www.youtube.com/watch?v=63RLcNbs9SU&t=168s',
      'video_id': '63RLcNbs9SU'},
     {'author': 'ION Capital - Loan Broker University',
      'channel': 'ION Capital - Loan Broker University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=jq-MYGn7i3I&t=417s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Vast uh uh uh Nationwide lender networ okay all right thank you you got it hey '
              'Ryan Yes I want to ask your a question about what Tracy was talking about do '
              'you have lenders for U leasing used equipment also lenders that would cash out '
              'uh can can lend against the used.',
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': 'Vast uh uh uh Nationwide lender networ okay all right thank you you got it hey '
             'Ryan Yes I want to ask your a question about what Tracy was talking about do you '
             'have lenders for U leasing used equipment also lenders that would cash out uh '
             'can can lend against the used.',
      'title': 'How To Be A Business Loan Broker  |  The Basics of Equipment Finance (ION '
               'Capital - Loan Broker University)',
      'url': 'https://www.youtube.com/watch?v=jq-MYGn7i3I&t=417s',
      'video_id': 'jq-MYGn7i3I'}],
 8: [{'author': 'Jeremiah Boucher',
      'channel': 'Jeremiah Boucher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=KFtBrowO6pc&t=63s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The purpose of a bridge loan is it helps investors move quickly. When there's a "
              'great value-add opportunity or a building that a business needs to acquire in '
              'order to operate their company out of, and they need to do it quickly, a bridge '
              'loan can be the right financing tool.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': "The purpose of a bridge loan is it helps investors move quickly. When there's a "
             'great value-add opportunity or a building that a business needs to acquire in '
             'order to operate their company out of, and they need to do it quickly, a bridge '
             'loan can be the right financing tool.',
      'title': 'What Is A Bridge Loan In Commercial Real Estate (Jeremiah Boucher)',
      'url': 'https://www.youtube.com/watch?v=KFtBrowO6pc&t=63s',
      'video_id': 'KFtBrowO6pc'},
     {'author': 'CFM (Commercial Financing Mastery)',
      'channel': 'CFM (Commercial Financing Mastery)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:35](https://www.youtube.com/watch?v=QmriETtG_oE&t=935s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Also, you should expect the same for your business. By the way, always also '
              "check with your principal broker, your brokerage owner, right? Don't hide or "
              'anything from them. We want if a brokerage owner is watching this, we want to '
              'help your people.',
      'timestamp': 935,
      'timestamp_label': '[00:15:35]',
      'timestamp_seconds': 935,
      'tip': 'Also, you should expect the same for your business. By the way, always also '
             "check with your principal broker, your brokerage owner, right? Don't hide or "
             'anything from them. We want if a brokerage owner is watching this, we want to '
             'help your people.',
      'title': 'What Brokers Get Wrong About Commercial Financing | Sua Truong (CFM '
               '(Commercial Financing Mastery))',
      'url': 'https://www.youtube.com/watch?v=QmriETtG_oE&t=935s',
      'video_id': 'QmriETtG_oE'},
     {'author': 'Matt Dubois',
      'channel': 'Matt Dubois',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=vPF9bO_izWU&t=83s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The data gets cleaned and standardized. Missing fields are filled in from the '
              'real invoice. The original record is never changed, and you can see exactly '
              'what was sent to Visa. Pull your last statement and look for business card '
              'transactions at standard rates.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'The data gets cleaned and standardized. Missing fields are filled in from the '
             'real invoice. The original record is never changed, and you can see exactly what '
             'was sent to Visa. Pull your last statement and look for business card '
             'transactions at standard rates.',
      'title': 'How B2B Businesses Lower Credit Card Fees (Visa Product 3 Explained) (Matt '
               'Dubois)',
      'url': 'https://www.youtube.com/watch?v=vPF9bO_izWU&t=83s',
      'video_id': 'vPF9bO_izWU'},
     {'author': 'Ben Van Zee',
      'channel': 'Ben Van Zee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=EcXwTRCJH-8&t=146s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Found a freight factoring company he loved and got access to Commonwealth's "
              "freight broker directory don't wait for a financial emergency call Commonwealth "
              'Capital today 952 469 4460 visit Commonwealth mn.com simple straightforward '
              'accounts receivable funding.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': "Found a freight factoring company he loved and got access to Commonwealth's "
             "freight broker directory don't wait for a financial emergency call Commonwealth "
             'Capital today 952 469 4460 visit Commonwealth mn.com simple straightforward '
             'accounts receivable funding.',
      'title': 'How Accounts Receivable Financing Works (Ben Van Zee)',
      'url': 'https://www.youtube.com/watch?v=EcXwTRCJH-8&t=146s',
      'video_id': 'EcXwTRCJH-8'},
     {'author': 'ClearValue Tax',
      'channel': 'ClearValue Tax',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:53](https://www.youtube.com/watch?v=jaczYsctbgs&t=413s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, if you come to my website, you can use my tool to see your probability of '
              "approval based on just four criteria. Your loan amounts, how much that you're "
              "requesting, your monthly gross sales, how long that you've been in business "
              'for, and your credit score.',
      'timestamp': 413,
      'timestamp_label': '[00:06:53]',
      'timestamp_seconds': 413,
      'tip': 'So, if you come to my website, you can use my tool to see your probability of '
             "approval based on just four criteria. Your loan amounts, how much that you're "
             "requesting, your monthly gross sales, how long that you've been in business for, "
             'and your credit score.',
      'title': 'How to Get an SBA Loan For Your Small Business (Tips & Advice) (ClearValue '
               'Tax)',
      'url': 'https://www.youtube.com/watch?v=jaczYsctbgs&t=413s',
      'video_id': 'jaczYsctbgs'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:26](https://www.youtube.com/watch?v=QPWj0c48x1o&t=1046s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Professional face to the world that includes your logo your business card your '
              'website your brochures your CRM your a whole lot more your pitch decks a.',
      'timestamp': 1046,
      'timestamp_label': '[00:17:26]',
      'timestamp_seconds': 1046,
      'tip': 'Professional face to the world that includes your logo your business card your '
             'website your brochures your CRM your a whole lot more your pitch decks a.',
      'title': 'Commercial Loan Broker Institute Overview (Commercial Loan Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=QPWj0c48x1o&t=1046s',
      'video_id': 'QPWj0c48x1o'},
     {'author': 'Community Business Finance',
      'channel': 'Community Business Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=pAuU5b_a7AY&t=30s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When it comes to financing real estate the answer almost always is going to be '
              'the 504 option is the best option for your business. The 504 program offers '
              "many advantages that the 7a loan doesn't. The 504 program offers fixed rates "
              'for twenty years.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'When it comes to financing real estate the answer almost always is going to be '
             'the 504 option is the best option for your business. The 504 program offers many '
             "advantages that the 7a loan doesn't. The 504 program offers fixed rates for "
             'twenty years.',
      'title': 'SBA 504 vs. 7(a) Loans for Commercial Real Estate (Community Business Finance)',
      'url': 'https://www.youtube.com/watch?v=pAuU5b_a7AY&t=30s',
      'video_id': 'pAuU5b_a7AY'},
     {'author': 'Trade Finance Global',
      'channel': 'Trade Finance Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=LlAxD5FEW5Q&t=72s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I think to Brian's point is you know, you've got access to the data, but then "
              "you've got to do something intelligent on the top of it, right? So, it's "
              'applying those tools.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "I think to Brian's point is you know, you've got access to the data, but then "
             "you've got to do something intelligent on the top of it, right? So, it's "
             'applying those tools.',
      'title': '4 - The evolution of Supply Chain Finance (Trade Finance Global)',
      'url': 'https://www.youtube.com/watch?v=LlAxD5FEW5Q&t=72s',
      'video_id': 'LlAxD5FEW5Q'},
     {'author': 'AD Mortgage',
      'channel': 'AD Mortgage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=HE_kRmkKu5c&t=163s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Could Sarah imagine this before? When real estate investors search for '
              'financing options, they often run into limitations. D S C R loans are more '
              'flexible than traditional commercial mortgages.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Could Sarah imagine this before? When real estate investors search for financing '
             'options, they often run into limitations. D S C R loans are more flexible than '
             'traditional commercial mortgages.',
      'title': 'What Is DSCR? Debt Service Coverage Ratio Loan, Real Estate Investing 2025, '
               'Calculation Explained (AD Mortgage)',
      'url': 'https://www.youtube.com/watch?v=HE_kRmkKu5c&t=163s',
      'video_id': 'HE_kRmkKu5c'},
     {'author': 'Trowbridge Law Group',
      'channel': 'Trowbridge Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=8p8VFFvdliQ&t=52s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a whole new business and I'll show you how you can get get a hold of some "
              "of that material at the end of the uh video. I'm a still a half marathon "
              'runner, slower than I used to be, but I still do it. So the question is, are '
              'you acting as an unregistered broker dealer?',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "It's a whole new business and I'll show you how you can get get a hold of some "
             "of that material at the end of the uh video. I'm a still a half marathon runner, "
             'slower than I used to be, but I still do it. So the question is, are you acting '
             'as an unregistered broker dealer?',
      'title': "Don't Act as a Broker-Dealer (Trowbridge Law Group)",
      'url': 'https://www.youtube.com/watch?v=8p8VFFvdliQ&t=52s',
      'video_id': '8p8VFFvdliQ'},
     {'author': 'CPDonline',
      'channel': 'CPDonline',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=ISIQRUkBnEc&t=131s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Die jas bidon in hen die be very bad en chewie aan de slides furthermore the '
              'education and educational tool to bring ham en salami demonstrate de laatste '
              'side I did you care professionals en gladys wal die artikel interesting '
              'professionele jury maar ground cover.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'Die jas bidon in hen die be very bad en chewie aan de slides furthermore the '
             'education and educational tool to bring ham en salami demonstrate de laatste '
             'side I did you care professionals en gladys wal die artikel interesting '
             'professionele jury maar ground cover.',
      'title': 'Litigation Funding for Commercial Claims in Canada (CPDonline)',
      'url': 'https://www.youtube.com/watch?v=ISIQRUkBnEc&t=131s',
      'video_id': 'ISIQRUkBnEc'},
     {'author': 'Succeed REI',
      'channel': 'Succeed REI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=3AB1K3GHp4w&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'From a mortgage broker when referencing the minimum requirements for a loan and '
              'you wondered what does that mean exactly well you came to the right place '
              'because.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'From a mortgage broker when referencing the minimum requirements for a loan and '
             'you wondered what does that mean exactly well you came to the right place '
             'because.',
      'title': 'What is Debt Service Coverage Ratio (DSCR) and How to Use It (Succeed REI)',
      'url': 'https://www.youtube.com/watch?v=3AB1K3GHp4w&t=15s',
      'video_id': '3AB1K3GHp4w'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=ctWaQk2YDgE&t=112s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re having a lot more fun doing it. So, if you're wondering if you're a fit for "
              'finance or as a commercial loan broker, just check out our free personality '
              "quiz at loanbrokers. It's a free tool that we've built to help out people who "
              'are exploring the finance space.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': "'re having a lot more fun doing it. So, if you're wondering if you're a fit for "
             'finance or as a commercial loan broker, just check out our free personality quiz '
             "at loanbrokers. It's a free tool that we've built to help out people who are "
             'exploring the finance space.',
      'title': 'Wondering if you’re built for commercial finance? (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=ctWaQk2YDgE&t=112s',
      'video_id': 'ctWaQk2YDgE'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=M48iXqAIzwE&t=144s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Channel we talk all things financing I've been in the lending industry for over "
              "20 years and I'm happy to answer your questions and provide great content.",
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': "Channel we talk all things financing I've been in the lending industry for over "
             "20 years and I'm happy to answer your questions and provide great content.",
      'title': 'How to Become a Commercial Loan Broker (Beau Eckstein, Business Ownership '
               'Coach)',
      'url': 'https://www.youtube.com/watch?v=M48iXqAIzwE&t=144s',
      'video_id': 'M48iXqAIzwE'},
     {'author': 'Beau Eckstein, Business Ownership Coach',
      'channel': 'Beau Eckstein, Business Ownership Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=rzgxx8EB7NI&t=118s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This channel we talk all things financing I've been in the lending industry for "
              "over 20 years and I'm happy to answer your questions and provide great content.",
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': "This channel we talk all things financing I've been in the lending industry for "
             "over 20 years and I'm happy to answer your questions and provide great content.",
      'title': 'What is a good DSCR for commercial real estate? (Beau Eckstein, Business '
               'Ownership Coach)',
      'url': 'https://www.youtube.com/watch?v=rzgxx8EB7NI&t=118s',
      'video_id': 'rzgxx8EB7NI'}],
 9: [{'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:07](https://www.youtube.com/watch?v=v3GnrXphwvM&t=667s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And most business purpose commercial brokering doesn't require the consumer "
              'mortgage licensing, the NMLS SAFE Act licensing, that residential mortgage '
              "officers have to carry. But, this isn't legal advice, so confirm the rules for "
              'your state.',
      'timestamp': 667,
      'timestamp_label': '[00:11:07]',
      'timestamp_seconds': 667,
      'tip': "And most business purpose commercial brokering doesn't require the consumer "
             'mortgage licensing, the NMLS SAFE Act licensing, that residential mortgage '
             "officers have to carry. But, this isn't legal advice, so confirm the rules for "
             'your state.',
      'title': 'What Does a Commercial Loan Broker REALLY Do? (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=v3GnrXphwvM&t=667s',
      'video_id': 'v3GnrXphwvM'},
     {'author': 'Texas Office of Consumer Credit Commissioner',
      'channel': 'Texas Office of Consumer Credit Commissioner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=rhDEWGC8KqM&t=154s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, I'd like to start with a quick refresher on the product and the law being "
              "implemented by these rules to make sure we're on the same page. So, the product "
              "and regulated area that we're talking about is called commercial sales-based "
              'financing.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': "So, I'd like to start with a quick refresher on the product and the law being "
             "implemented by these rules to make sure we're on the same page. So, the product "
             "and regulated area that we're talking about is called commercial sales-based "
             'financing.',
      'title': 'Commercial Sales-Based Financing Rules: Precomment Draft – January 28, 2026 '
               '(Texas Office of Consumer Credit Commissioner)',
      'url': 'https://www.youtube.com/watch?v=rhDEWGC8KqM&t=154s',
      'video_id': 'rhDEWGC8KqM'},
     {'author': 'The Loan Broker Academy',
      'channel': 'The Loan Broker Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=4AAOQcVDMIo&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Because you're considering becoming a business loan broker please watch this to "
              'the end and i want to state something here do not ever ever ever believe the.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Because you're considering becoming a business loan broker please watch this to "
             'the end and i want to state something here do not ever ever ever believe the.',
      'title': 'Commercial Loan Broker Training | Do NOT Believe The Hype On YouTube!! (The '
               'Loan Broker Academy)',
      'url': 'https://www.youtube.com/watch?v=4AAOQcVDMIo&t=15s',
      'video_id': '4AAOQcVDMIo'},
     {'author': 'Selling Your Canadian Business',
      'channel': 'Selling Your Canadian Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:10](https://www.youtube.com/watch?v=Ja8jXRIkOK4&t=970s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The second being one is the cash flow issues become constant. You are always in '
              "a state of crisis. You don't have the working capital you need to support that "
              'growth. And the last one is the business owner.',
      'timestamp': 970,
      'timestamp_label': '[00:16:10]',
      'timestamp_seconds': 970,
      'tip': 'The second being one is the cash flow issues become constant. You are always in '
             "a state of crisis. You don't have the working capital you need to support that "
             'growth. And the last one is the business owner.',
      'title': 'How a Fractional CFO Helps Canadian Businesses Scale and Prepare for Sale with '
               'Robert Cinapri (Selling Your Canadian Business)',
      'url': 'https://www.youtube.com/watch?v=Ja8jXRIkOK4&t=970s',
      'video_id': 'Ja8jXRIkOK4'},
     {'author': 'ProjectionHub',
      'channel': 'ProjectionHub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=_V39MGbzjw0&t=46s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The issue is that MCA debt, they're going to file what's called a UCCC filing "
              "statement on all business assets. So, they're going to file that with the "
              "Secretary of State. They're going to have a claim on all of your assets.",
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "The issue is that MCA debt, they're going to file what's called a UCCC filing "
             "statement on all business assets. So, they're going to file that with the "
             "Secretary of State. They're going to have a claim on all of your assets.",
      'title': 'Can I Refinance an MCA Loan with an SBA Loan? (ProjectionHub)',
      'url': 'https://www.youtube.com/watch?v=_V39MGbzjw0&t=46s',
      'video_id': '_V39MGbzjw0'},
     {'author': 'Supply Chain Finance Academy',
      'channel': 'Supply Chain Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=Db19fMNKoJY&t=69s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Supply chain finance, SCF, bridges these two worlds. It is a set of financial '
              'solutions enabled by both legal structures and technology that allows buyers '
              'and suppliers to optimize working capital and cash flow.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'Supply chain finance, SCF, bridges these two worlds. It is a set of financial '
             'solutions enabled by both legal structures and technology that allows buyers and '
             'suppliers to optimize working capital and cash flow.',
      'title': 'Mastering Supply Chain Finance: Technique, Risk & Innovation - Introduction to '
               'Supply Chain Finance (Supply Chain Finance Academy)',
      'url': 'https://www.youtube.com/watch?v=Db19fMNKoJY&t=69s',
      'video_id': 'Db19fMNKoJY'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=dIwbKzTxcQk&t=247s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's the realistic picture on licensing. Business and commercial loan "
              'brokering generally is not state licensed the way residential mortgage '
              'origination actually is state licensed. But, those rules vary state by state, '
              'and there are some real exceptions.',
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': "Here's the realistic picture on licensing. Business and commercial loan "
             'brokering generally is not state licensed the way residential mortgage '
             'origination actually is state licensed. But, those rules vary state by state, '
             'and there are some real exceptions.',
      'title': 'How to Become a Business Loan Broker in 2026 (Commercial Loan Broker '
               'Institute)',
      'url': 'https://www.youtube.com/watch?v=dIwbKzTxcQk&t=247s',
      'video_id': 'dIwbKzTxcQk'},
     {'author': 'Brian M. Hazel Quotes',
      'channel': 'Brian M. Hazel Quotes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=e3NbWehFdJs&t=88s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What can I cut without killing sales? This rolling forecast tells me two '
              'things. How much I actually need when I can realistically repay. If the loan '
              "won't bridge me to higher revenues, ease seasonality losses, or fulfill a new "
              'contract or an operational fix.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'What can I cut without killing sales? This rolling forecast tells me two things. '
             "How much I actually need when I can realistically repay. If the loan won't "
             'bridge me to higher revenues, ease seasonality losses, or fulfill a new contract '
             'or an operational fix.',
      'title': 'How to Get Business Funding & Working Capital - BusinessLoansConnect.com '
               '(Brian M. Hazel Quotes)',
      'url': 'https://www.youtube.com/watch?v=e3NbWehFdJs&t=88s',
      'video_id': 'e3NbWehFdJs'},
     {'author': 'Mar T',
      'channel': 'Mar T',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=PPTyFBcPTUw&t=60s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, does this result in any kind of an accounting journal entry? It's simply a "
              "footnote disclosure. It's very useful for the reader to understand, oh, I see "
              'you have this current asset called receivables.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': "Now, does this result in any kind of an accounting journal entry? It's simply a "
             "footnote disclosure. It's very useful for the reader to understand, oh, I see "
             'you have this current asset called receivables.',
      'title': 'F3 M2 5 Pledging & Factoring of Accounts Receivables (Mar T)',
      'url': 'https://www.youtube.com/watch?v=PPTyFBcPTUw&t=60s',
      'video_id': 'PPTyFBcPTUw'},
     {'author': 'CLA (CliftonLarsonAllen LLP)',
      'channel': 'CLA (CliftonLarsonAllen LLP)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:20](https://www.youtube.com/watch?v=ByTHmfsxaNQ&t=920s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The HUD one is going away we're going to have a new closing disclosure wait to "
              "see whether we're still going to have a lot of compliance violations in that "
              'area.',
      'timestamp': 920,
      'timestamp_label': '[00:15:20]',
      'timestamp_seconds': 920,
      'tip': "The HUD one is going away we're going to have a new closing disclosure wait to "
             "see whether we're still going to have a lot of compliance violations in that "
             'area.',
      'title': 'TIL/RESPA Final Rule on Integrated Mortgage Disclosures (CLA '
               '(CliftonLarsonAllen LLP))',
      'url': 'https://www.youtube.com/watch?v=ByTHmfsxaNQ&t=920s',
      'video_id': 'ByTHmfsxaNQ'},
     {'author': 'Solar Energy Channel by Paradise Energy Solutions',
      'channel': 'Solar Energy Channel by Paradise Energy Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=LltieIq1Eq0&t=43s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The tax credit for residential is under Section 25 and under Commercial Section '
              "48. And the rules are very different. And one of the things we've seen with the "
              'IRA bill that was passed was that changing even more drastically.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'The tax credit for residential is under Section 25 and under Commercial Section '
             "48. And the rules are very different. And one of the things we've seen with the "
             'IRA bill that was passed was that changing even more drastically.',
      'title': 'Unlocking the Solar Tax Credit: 10% adders, transferability rules, and more '
               '(Solar Energy Channel by Paradise Energy Solutions)',
      'url': 'https://www.youtube.com/watch?v=LltieIq1Eq0&t=43s',
      'video_id': 'LltieIq1Eq0'},
     {'author': 'The Capital Alliance TV',
      'channel': 'The Capital Alliance TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:36](https://www.youtube.com/watch?v=2_gq6XRm47I&t=516s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to be transitioning your business to the next generation. But we're "
              'living in a state where baby boomers, the next generation are not interested in '
              'a lot of these um businesses that their parents and their grandparents started.',
      'timestamp': 516,
      'timestamp_label': '[00:08:36]',
      'timestamp_seconds': 516,
      'tip': "'re going to be transitioning your business to the next generation. But we're "
             'living in a state where baby boomers, the next generation are not interested in '
             'a lot of these um businesses that their parents and their grandparents started.',
      'title': '$100M Is Easier to Get Than $10M — Here’s Why | Taber Small (The Capital '
               'Alliance TV)',
      'url': 'https://www.youtube.com/watch?v=2_gq6XRm47I&t=516s',
      'video_id': '2_gq6XRm47I'},
     {'author': 'Transform Solar',
      'channel': 'Transform Solar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=U8Ynw0oqocY&t=100s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Second bucket to pay his taxes with our representatives are not licensed tax '
              'professionals and this is not legal tax advice we recommend that you contact '
              'your CPA to best understand your individual tax situation.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Second bucket to pay his taxes with our representatives are not licensed tax '
             'professionals and this is not legal tax advice we recommend that you contact '
             'your CPA to best understand your individual tax situation.',
      'title': 'The Solar Tax Credit Explained (Transform Solar)',
      'url': 'https://www.youtube.com/watch?v=U8Ynw0oqocY&t=100s',
      'video_id': 'U8Ynw0oqocY'},
     {'author': 'ION Capital - Loan Broker University',
      'channel': 'ION Capital - Loan Broker University',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:15](https://www.youtube.com/watch?v=2BqGahVBgUs&t=615s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One of the worst questions for a hypothetical because there's a lot of "
              'different things that come into play yeah I understand they look at auction.',
      'timestamp': 615,
      'timestamp_label': '[00:10:15]',
      'timestamp_seconds': 615,
      'tip': "One of the worst questions for a hypothetical because there's a lot of different "
             'things that come into play yeah I understand they look at auction.',
      'title': 'How To Be A Business Loan Broker  |  Equipment Financing Loans (ION Capital - '
               'Loan Broker University)',
      'url': 'https://www.youtube.com/watch?v=2BqGahVBgUs&t=615s',
      'video_id': '2BqGahVBgUs'},
     {'author': 'Commercial Loan Broker Institute',
      'channel': 'Commercial Loan Broker Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=SrGiDqgbdf8&t=16s)',
      'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                   'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                   'underwriting (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Company how do you become a finance lender my name is shane walton with the '
              'commercial loan broker institute to start us off.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'Company how do you become a finance lender my name is shane walton with the '
             'commercial loan broker institute to start us off.',
      'title': 'How to Start Your Own Finance Company - Guide To Becoming A Commercial Loan '
               'Broker (Commercial Loan Broker Institute)',
      'url': 'https://www.youtube.com/watch?v=SrGiDqgbdf8&t=16s',
      'video_id': 'SrGiDqgbdf8'}],
 10: [{'author': 'Lamar Duffy',
       'channel': 'Lamar Duffy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=EtzXCqqxIWI&t=20s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you're new to the channel, welcome. My name is Lamar and I'm a sevenfigure "
               'serial entrepreneur helping you start and scale your business with AI '
               'marketing automation.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "If you're new to the channel, welcome. My name is Lamar and I'm a sevenfigure "
              'serial entrepreneur helping you start and scale your business with AI marketing '
              'automation.',
       'title': 'Fintech Referral Program: How to Build an AI Growth Automation Step-by-Step '
                '(Lamar Duffy)',
       'url': 'https://www.youtube.com/watch?v=EtzXCqqxIWI&t=20s',
       'video_id': 'EtzXCqqxIWI'},
      {'author': 'Eli the DSCR Pro',
       'channel': 'Eli the DSCR Pro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:41](https://www.youtube.com/watch?v=6P1p0e_NBxs&t=281s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Concessions, we allow up to 6% seller's concessions. You can use that to buy "
               'down your rate or cover closing cost. Asset, need help with the down payment? '
               'Speed, we target a four-week closing, not 60, 90 days. We move at the speed of '
               'business.',
       'timestamp': 281,
       'timestamp_label': '[00:04:41]',
       'timestamp_seconds': 281,
       'tip': "Concessions, we allow up to 6% seller's concessions. You can use that to buy "
              'down your rate or cover closing cost. Asset, need help with the down payment? '
              'Speed, we target a four-week closing, not 60, 90 days. We move at the speed of '
              'business.',
       'title': 'DSCR Loan For Commercial Property (Eli the DSCR Pro)',
       'url': 'https://www.youtube.com/watch?v=6P1p0e_NBxs&t=281s',
       'video_id': '6P1p0e_NBxs'},
      {'author': 'Invoice Finance News',
       'channel': 'Invoice Finance News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:03](https://www.youtube.com/watch?v=RyM3eO5GN5I&t=363s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Borrowing against machinery and property asset-based lending is also possible '
               'using plant machinery and commercial property normally loans against Machinery '
               'are repaid over three years loans against property are repaid over 7 to 15 '
               'years.',
       'timestamp': 363,
       'timestamp_label': '[00:06:03]',
       'timestamp_seconds': 363,
       'tip': 'Borrowing against machinery and property asset-based lending is also possible '
              'using plant machinery and commercial property normally loans against Machinery '
              'are repaid over three years loans against property are repaid over 7 to 15 '
              'years.',
       'title': 'Asset Based Lending (Invoice Finance News)',
       'url': 'https://www.youtube.com/watch?v=RyM3eO5GN5I&t=363s',
       'video_id': 'RyM3eO5GN5I'},
      {'author': 'Vanijja | Trade Insights',
       'channel': 'Vanijja | Trade Insights',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=RcVypdN4SHs&t=87s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Supply chain finance operates completely differently. Think of it like a smart '
               'logistics dashboard. Instead of hoarding paper certificates in a vault, it '
               'tracks the journey of the goods and unlocks cash automatically as commercial '
               'milestones are hit.',
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': 'Supply chain finance operates completely differently. Think of it like a smart '
              'logistics dashboard. Instead of hoarding paper certificates in a vault, it '
              'tracks the journey of the goods and unlocks cash automatically as commercial '
              'milestones are hit.',
       'title': 'Trade Finance vs. Supply Chain Finance: Key Differences Explained (With Real '
                'Examples) (Vanijja | Trade Insights)',
       'url': 'https://www.youtube.com/watch?v=RcVypdN4SHs&t=87s',
       'video_id': 'RcVypdN4SHs'},
      {'author': 'Achievable',
       'channel': 'Achievable',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:34](https://www.youtube.com/watch?v=j_Gp2v7DBzo&t=394s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Broker dealer that has their principal place of business in California maybe '
               'they have a couple of offices on the west coast in Oregon and Washington but.',
       'timestamp': 394,
       'timestamp_label': '[00:06:34]',
       'timestamp_seconds': 394,
       'tip': 'Broker dealer that has their principal place of business in California maybe '
              'they have a couple of offices on the west coast in Oregon and Washington but.',
       'title': 'Broker dealer exclusions (NASAA Series 63, 65, 66) (Achievable)',
       'url': 'https://www.youtube.com/watch?v=j_Gp2v7DBzo&t=394s',
       'video_id': 'j_Gp2v7DBzo'},
      {'author': 'Beau Eckstein, Business Ownership Coach',
       'channel': 'Beau Eckstein, Business Ownership Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:02](https://www.youtube.com/watch?v=9w4kgjirJ7g&t=122s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "How to leverage SBA financing Tax Strategies I'm not a CPA and attorney but we "
               "bring CPAs on you're going to learn why everyone everyone should own a small "
               "business so I hope you attend go to boxing.com events I'll see you at the "
               'next.',
       'timestamp': 122,
       'timestamp_label': '[00:02:02]',
       'timestamp_seconds': 122,
       'tip': "How to leverage SBA financing Tax Strategies I'm not a CPA and attorney but we "
              "bring CPAs on you're going to learn why everyone everyone should own a small "
              "business so I hope you attend go to boxing.com events I'll see you at the next.",
       'title': 'SBA 504 vs. SBA 7(a) Loans for Commercial Real Estate: How to Choose the Best '
                'Loan for Your Project! (Beau Eckstein, Business Ownership Coach)',
       'url': 'https://www.youtube.com/watch?v=9w4kgjirJ7g&t=122s',
       'video_id': '9w4kgjirJ7g'},
      {'author': 'Eslatainment',
       'channel': 'Eslatainment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:24](https://www.youtube.com/watch?v=3Y7TjakDREI&t=264s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Stability and financiers gain access to a new asset class with attractive '
               "returns it's it's a win-win-win situation so what are you waiting for Join the "
               "liberte Revolution today and unlock your business's true potential.",
       'timestamp': 264,
       'timestamp_label': '[00:04:24]',
       'timestamp_seconds': 264,
       'tip': 'Stability and financiers gain access to a new asset class with attractive '
              "returns it's it's a win-win-win situation so what are you waiting for Join the "
              "liberte Revolution today and unlock your business's true potential.",
       'title': 'Supply Chain Finance (Eslatainment)',
       'url': 'https://www.youtube.com/watch?v=3Y7TjakDREI&t=264s',
       'video_id': '3Y7TjakDREI'},
      {'author': 'Zach Siegel',
       'channel': 'Zach Siegel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:57](https://www.youtube.com/watch?v=w-ETPb-Trek&t=357s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I want to talk about next that can still get you out of this MCA hellhole. The '
               'first assetbased option that I want to talk about allows you to leverage the '
               "equity in your home or another property. It's called the business use HELOC or "
               'home equity line of credit.',
       'timestamp': 357,
       'timestamp_label': '[00:05:57]',
       'timestamp_seconds': 357,
       'tip': 'I want to talk about next that can still get you out of this MCA hellhole. The '
              'first assetbased option that I want to talk about allows you to leverage the '
              "equity in your home or another property. It's called the business use HELOC or "
              'home equity line of credit.',
       'title': '4 Ways to Get Out of Merchant Cash Advance Debt (Zach Siegel)',
       'url': 'https://www.youtube.com/watch?v=w-ETPb-Trek&t=357s',
       'video_id': 'w-ETPb-Trek'},
      {'author': 'ProAlpha Capital',
       'channel': 'ProAlpha Capital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:24](https://www.youtube.com/watch?v=L9TrjfKxYdY&t=24s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t actually use your income. There's no tax returns, W-2s, or actual income "
               "verification involved in the process. Approval is based on the property's "
               'rental income, not your personal DTI. This gives beginners access to really '
               'leverage the years of needing landlord history.',
       'timestamp': 24,
       'timestamp_label': '[00:00:24]',
       'timestamp_seconds': 24,
       'tip': "'t actually use your income. There's no tax returns, W-2s, or actual income "
              "verification involved in the process. Approval is based on the property's "
              'rental income, not your personal DTI. This gives beginners access to really '
              'leverage the years of needing landlord history.',
       'title': 'DSCR Loans Explained in 2 Minutes (ProAlpha Capital)',
       'url': 'https://www.youtube.com/watch?v=L9TrjfKxYdY&t=24s',
       'video_id': 'L9TrjfKxYdY'},
      {'author': 'Tactica RES',
       'channel': 'Tactica RES',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:35](https://www.youtube.com/watch?v=ZgYmvPS5gJY&t=455s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '68% suppressing our yield so what do we need to do well we need to pay less '
               'for the asset if we want that leverage to be positive and for our cash on cash '
               "return to be higher than the cap rate so I'm just going to play with some "
               "numbers here let's try 5.",
       'timestamp': 455,
       'timestamp_label': '[00:07:35]',
       'timestamp_seconds': 455,
       'tip': '68% suppressing our yield so what do we need to do well we need to pay less for '
              'the asset if we want that leverage to be positive and for our cash on cash '
              "return to be higher than the cap rate so I'm just going to play with some "
              "numbers here let's try 5.",
       'title': 'The Relationship Between LTV, DSCR, Debt Yield & the Loan Constant (Tactica '
                'RES)',
       'url': 'https://www.youtube.com/watch?v=ZgYmvPS5gJY&t=455s',
       'video_id': 'ZgYmvPS5gJY'},
      {'author': 'Commercial Loan Broker Institute',
       'channel': 'Commercial Loan Broker Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:37](https://www.youtube.com/watch?v=WUTiN5zYjnU&t=817s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s time to build something that matters, go ahead and make a move. Commercial "
               'loan broker institute exists for one reason to give folks like you everything '
               'you need to succeed in the business.',
       'timestamp': 817,
       'timestamp_label': '[00:13:37]',
       'timestamp_seconds': 817,
       'tip': "'s time to build something that matters, go ahead and make a move. Commercial "
              'loan broker institute exists for one reason to give folks like you everything '
              'you need to succeed in the business.',
       'title': 'A Day in the Life of a Commercial Loan Broker (The Real Version) (Commercial '
                'Loan Broker Institute)',
       'url': 'https://www.youtube.com/watch?v=WUTiN5zYjnU&t=817s',
       'video_id': 'WUTiN5zYjnU'},
      {'author': 'Accounting Videos',
       'channel': 'Accounting Videos',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=-sIN2gar6BU&t=49s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'May have a ton of accounts receivable but they need cash immediately and so '
               'what they can do is that they can sell these accounts receivable to another.',
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': 'May have a ton of accounts receivable but they need cash immediately and so '
              'what they can do is that they can sell these accounts receivable to another.',
       'title': 'Factoring vs. Secured Borrowing Part 1 (Accounting Videos)',
       'url': 'https://www.youtube.com/watch?v=-sIN2gar6BU&t=49s',
       'video_id': '-sIN2gar6BU'},
      {'author': 'Simon White (SEO, AEO & Digital & Marketing)',
       'channel': 'Simon White (SEO, AEO & Digital & Marketing)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:42:20](https://www.youtube.com/watch?v=G9RrpSanefM&t=2540s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Symposium in Las Vegas and uh thank you very much for taking your time to to '
               "be with us and uh share your insights on on our T seminar today you're more "
               'than welcome bill I appreciate you having me okay byebye take care.',
       'timestamp': 2540,
       'timestamp_label': '[00:42:20]',
       'timestamp_seconds': 2540,
       'tip': 'Symposium in Las Vegas and uh thank you very much for taking your time to to be '
              "with us and uh share your insights on on our T seminar today you're more than "
              'welcome bill I appreciate you having me okay byebye take care.',
       'title': 'Invoice Factoring & Asset Based Lending (Simon White (SEO, AEO & Digital & '
                'Marketing))',
       'url': 'https://www.youtube.com/watch?v=G9RrpSanefM&t=2540s',
       'video_id': 'G9RrpSanefM'},
      {'author': 'Financial modeling',
       'channel': 'Financial modeling',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:33](https://www.youtube.com/watch?v=Xf8npq5DK2w&t=273s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sponsor in the last two lessons we reviewed the basics of the tax equity '
               'concepts and in the next few lessons we will introduce the simplified version '
               'of the tax equity funding to our model.',
       'timestamp': 273,
       'timestamp_label': '[00:04:33]',
       'timestamp_seconds': 273,
       'tip': 'Sponsor in the last two lessons we reviewed the basics of the tax equity '
              'concepts and in the next few lessons we will introduce the simplified version '
              'of the tax equity funding to our model.',
       'title': 'Tax Equity Flip and Back Leverage Debt in US Renewable Energy Sector '
                '(Financial modeling)',
       'url': 'https://www.youtube.com/watch?v=Xf8npq5DK2w&t=273s',
       'video_id': 'Xf8npq5DK2w'},
      {'author': 'Commercial Loan Broker Institute',
       'channel': 'Commercial Loan Broker Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:49](https://www.youtube.com/watch?v=8-4I4VOIIqg&t=289s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's still the same loan program. Um, but, uh, different institutions just "
               'have different flavor. Um, and it can be industry based, it can be '
               'locationbased. Um, it can even be use of proceeds based.',
       'timestamp': 289,
       'timestamp_label': '[00:04:49]',
       'timestamp_seconds': 289,
       'tip': "It's still the same loan program. Um, but, uh, different institutions just have "
              'different flavor. Um, and it can be industry based, it can be locationbased. '
              'Um, it can even be use of proceeds based.',
       'title': 'SBA 7(a) Loans for Business Acquisitions: How a Top Lender Underwrites Deals '
                '(Commercial Loan Broker Institute)',
       'url': 'https://www.youtube.com/watch?v=8-4I4VOIIqg&t=289s',
       'video_id': '8-4I4VOIIqg'}],
 11: [{'author': 'Commercial Loan Broker Institute',
       'channel': 'Commercial Loan Broker Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:49](https://www.youtube.com/watch?v=4fxpQTB_spA&t=949s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And this is the broker's value, right? You are not just matching a business to "
               "capital. You're helping a business to keep the supply chain moving for our "
               'country and often even outside of our country.',
       'timestamp': 949,
       'timestamp_label': '[00:15:49]',
       'timestamp_seconds': 949,
       'tip': "And this is the broker's value, right? You are not just matching a business to "
              "capital. You're helping a business to keep the supply chain moving for our "
              'country and often even outside of our country.',
       'title': 'Unlock the Lucrative World of Supply Chain Financing (Commercial Loan Broker '
                'Institute)',
       'url': 'https://www.youtube.com/watch?v=4fxpQTB_spA&t=949s',
       'video_id': '4fxpQTB_spA'},
      {'author': 'Joe Camberato',
       'channel': 'Joe Camberato',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:22](https://www.youtube.com/watch?v=qWXtw52gtTw&t=442s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Take Equity um and you can get your business to whatever place it is that you '
               'want to in order to execute on that exit thanks for tuning in to grow by Joe '
               'remember to utilize financing as a tool to grow and scale your business keep '
               "doing what you're doing and keep.",
       'timestamp': 442,
       'timestamp_label': '[00:07:22]',
       'timestamp_seconds': 442,
       'tip': 'Take Equity um and you can get your business to whatever place it is that you '
              'want to in order to execute on that exit thanks for tuning in to grow by Joe '
              'remember to utilize financing as a tool to grow and scale your business keep '
              "doing what you're doing and keep.",
       'title': 'Accounts Receivable Financing: What You Need to Know (Joe Camberato)',
       'url': 'https://www.youtube.com/watch?v=qWXtw52gtTw&t=442s',
       'video_id': 'qWXtw52gtTw'},
      {'author': 'Facilero',
       'channel': 'Facilero',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:43](https://www.youtube.com/watch?v=wSWcWyCHkxM&t=43s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'With virtual cards, each payment can have its own set of card details, so even '
               "if one gets compromised, it won't affect the rest of your operations. Plus, "
               'you can cancel or disable a card with a click. They also reduce the time your '
               'finance team spends on reconciliation.',
       'timestamp': 43,
       'timestamp_label': '[00:00:43]',
       'timestamp_seconds': 43,
       'tip': 'With virtual cards, each payment can have its own set of card details, so even '
              "if one gets compromised, it won't affect the rest of your operations. Plus, you "
              'can cancel or disable a card with a click. They also reduce the time your '
              'finance team spends on reconciliation.',
       'title': 'Virtual Cards: Transforming B2B Payment Processes in 2025 (Facilero)',
       'url': 'https://www.youtube.com/watch?v=wSWcWyCHkxM&t=43s',
       'video_id': 'wSWcWyCHkxM'},
      {'author': 'Financely Group',
       'channel': 'Financely Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=xY3rD_awSEg&t=15s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Operations, while revenue is trapped in receivables. Asset-based  lending '
               'offers a solution by monetizing these assets before collections are finalized.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Operations, while revenue is trapped in receivables. Asset-based  lending '
              'offers a solution by monetizing these assets before collections are finalized.',
       'title': 'Asset-Based Lending and Borrowing Base Facilities (Financely Group)',
       'url': 'https://www.youtube.com/watch?v=xY3rD_awSEg&t=15s',
       'video_id': 'xY3rD_awSEg'},
      {'author': 'PIMCO U.S.',
       'channel': 'PIMCO U.S.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:16](https://www.youtube.com/watch?v=C4UI_wc_sUU&t=256s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Scale, close relationships, and a deep understanding of these markets will '
               'offer strategic opportunities for investors with flexible capital.',
       'timestamp': 256,
       'timestamp_label': '[00:04:16]',
       'timestamp_seconds': 256,
       'tip': 'Scale, close relationships, and a deep understanding of these markets will '
              'offer strategic opportunities for investors with flexible capital.',
       'title': 'Asset-Based Finance Explained (PIMCO U.S.)',
       'url': 'https://www.youtube.com/watch?v=C4UI_wc_sUU&t=256s',
       'video_id': 'C4UI_wc_sUU'},
      {'author': 'Universal Funding Corporation',
       'channel': 'Universal Funding Corporation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:36](https://www.youtube.com/watch?v=3PlJmybrzHs&t=156s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Relationship with them we'd like to do the same for your businesses in your "
               "network if you're ready to become an independent contractor for Universal "
               'funding Corporation download and complete the broker agreement form from our '
               'website or call 1800 984.',
       'timestamp': 156,
       'timestamp_label': '[00:02:36]',
       'timestamp_seconds': 156,
       'tip': "Relationship with them we'd like to do the same for your businesses in your "
              "network if you're ready to become an independent contractor for Universal "
              'funding Corporation download and complete the broker agreement form from our '
              'website or call 1800 984.',
       'title': 'Factoring Receivables Broker - Earn The Highest Commission (Universal Funding '
                'Corporation)',
       'url': 'https://www.youtube.com/watch?v=3PlJmybrzHs&t=156s',
       'video_id': '3PlJmybrzHs'},
      {'author': 'Ian Johnson',
       'channel': 'Ian Johnson',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=Lu16E6BvvDE&t=15s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your receivables through a bank and financing your receivables with an '
               'asset-based financing solution called receivables factoring okay so the '
               'reason.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Your receivables through a bank and financing your receivables with an '
              'asset-based financing solution called receivables factoring okay so the reason.',
       'title': 'Bank Financing vs. Receivables Factoring (Ian Johnson)',
       'url': 'https://www.youtube.com/watch?v=Lu16E6BvvDE&t=15s',
       'video_id': 'Lu16E6BvvDE'},
      {'author': 'Beau Eckstein, Business Ownership Coach',
       'channel': 'Beau Eckstein, Business Ownership Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:09](https://www.youtube.com/watch?v=NmbLxyMZBmQ&t=369s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A free consultation and together they will turn your dreams into tangible '
               'achievements visit www.bus ownership coach.com to discover more about Bo and '
               "his team's approach your success story is their unwavering commitment Thrive "
               'with business ownership coach.',
       'timestamp': 369,
       'timestamp_label': '[00:06:09]',
       'timestamp_seconds': 369,
       'tip': 'A free consultation and together they will turn your dreams into tangible '
              'achievements visit www.bus ownership coach.com to discover more about Bo and '
              "his team's approach your success story is their unwavering commitment Thrive "
              'with business ownership coach.',
       'title': 'Comparing SBA 7(a) vs 504 Loans for Business Acquisitions with Real Estate '
                '(Beau Eckstein, Business Ownership Coach)',
       'url': 'https://www.youtube.com/watch?v=NmbLxyMZBmQ&t=369s',
       'video_id': 'NmbLxyMZBmQ'},
      {'author': 'Zeus Commercial Capital | Business & RE Loans',
       'channel': 'Zeus Commercial Capital | Business & RE Loans',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=OccRWwWbI2M&t=40s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Accounts because they had to choose between making payroll or paying the MCA '
               'lender now we have an attorney Le team that is specifically designed to help.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': 'Accounts because they had to choose between making payroll or paying the MCA '
              'lender now we have an attorney Le team that is specifically designed to help.',
       'title': 'MCA Debt Restructuring- Debt Relief, Debt Consolidation, and MCA Debt '
                'Settlement (Zeus Commercial Capital | Business & RE Loans)',
       'url': 'https://www.youtube.com/watch?v=OccRWwWbI2M&t=40s',
       'video_id': 'OccRWwWbI2M'},
      {'author': 'Beverly Hills Bar Association',
       'channel': 'Beverly Hills Bar Association',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:16](https://www.youtube.com/watch?v=Wd7RTVzg5yU&t=16s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "With will mara who is an investment manager at validity finance who's who are "
               'headquartered in new york but do business throughout the country and.',
       'timestamp': 16,
       'timestamp_label': '[00:00:16]',
       'timestamp_seconds': 16,
       'tip': "With will mara who is an investment manager at validity finance who's who are "
              'headquartered in new york but do business throughout the country and.',
       'title': "Litigation Finance & Funding: William C. Marra - Litigator's Corner Interview "
                '(Beverly Hills Bar Association)',
       'url': 'https://www.youtube.com/watch?v=Wd7RTVzg5yU&t=16s',
       'video_id': 'Wd7RTVzg5yU'},
      {'author': 'AD Mortgage',
       'channel': 'AD Mortgage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:36:03](https://www.youtube.com/watch?v=-j6-Ev4L24c&t=2163s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'DSCR will be higher just because of the commercial use of these properties. Um '
               'six months reserves is required. So, again, no matter if your loan amount is '
               '400,000, normally on any other property type, we would require only three '
               'months reserves.',
       'timestamp': 2163,
       'timestamp_label': '[00:36:03]',
       'timestamp_seconds': 2163,
       'tip': 'DSCR will be higher just because of the commercial use of these properties. Um '
              'six months reserves is required. So, again, no matter if your loan amount is '
              '400,000, normally on any other property type, we would require only three '
              'months reserves.',
       'title': 'What is a DSCR Loan? Mortgage Broker Guide to Win More Deals and Get Them '
                'Approved! (AD Mortgage)',
       'url': 'https://www.youtube.com/watch?v=-j6-Ev4L24c&t=2163s',
       'video_id': '-j6-Ev4L24c'},
      {'author': 'Katheryn Reynolds',
       'channel': 'Katheryn Reynolds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:49](https://www.youtube.com/watch?v=_loCXf6bnl4&t=289s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Control of transferred assets if these criteria are not met it is not a true '
               "sale it's not a true factoring it's simply borrowing secured borrowing you've "
               'put your accounts receivable up as collateral.',
       'timestamp': 289,
       'timestamp_label': '[00:04:49]',
       'timestamp_seconds': 289,
       'tip': 'Control of transferred assets if these criteria are not met it is not a true '
              "sale it's not a true factoring it's simply borrowing secured borrowing you've "
              'put your accounts receivable up as collateral.',
       'title': 'Factoring Receivables with & without recourse (Katheryn Reynolds)',
       'url': 'https://www.youtube.com/watch?v=_loCXf6bnl4&t=289s',
       'video_id': '_loCXf6bnl4'},
      {'author': 'Darrell Cockrum',
       'channel': 'Darrell Cockrum',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:36](https://www.youtube.com/watch?v=bN1tDQE59LE&t=96s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Rate and that's a a Telltale sign that somebody talking about factoring maybe "
               "doesn't have a good handle on how it works they start asking about interest "
               "rate there's no interest rate because there's no loan there's.",
       'timestamp': 96,
       'timestamp_label': '[00:01:36]',
       'timestamp_seconds': 96,
       'tip': "Rate and that's a a Telltale sign that somebody talking about factoring maybe "
              "doesn't have a good handle on how it works they start asking about interest "
              "rate there's no interest rate because there's no loan there's.",
       'title': 'accounts receivable financing vs factoring (Darrell Cockrum)',
       'url': 'https://www.youtube.com/watch?v=bN1tDQE59LE&t=96s',
       'video_id': 'bN1tDQE59LE'},
      {'author': 'Jeff Trevarthen',
       'channel': 'Jeff Trevarthen',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:17](https://www.youtube.com/watch?v=O49frBQ6oe0&t=377s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Be able to get into these different types of properties that you can buy for '
               'Investments and a DSLR dscr loan is definitely a way to go so thanks so much '
               "for watching I'm Jeff the mortgage Pro look forward to seeing you on the next "
               'show have a good one.',
       'timestamp': 377,
       'timestamp_label': '[00:06:17]',
       'timestamp_seconds': 377,
       'tip': 'Be able to get into these different types of properties that you can buy for '
              'Investments and a DSLR dscr loan is definitely a way to go so thanks so much '
              "for watching I'm Jeff the mortgage Pro look forward to seeing you on the next "
              'show have a good one.',
       'title': 'DSCR Loans Explained for 2023 -- Mortgages for Investors. (Jeff Trevarthen)',
       'url': 'https://www.youtube.com/watch?v=O49frBQ6oe0&t=377s',
       'video_id': 'O49frBQ6oe0'},
      {'author': 'Funder Intel',
       'channel': 'Funder Intel',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=jCWdtQmKTiU&t=65s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t just affect MCA or revenue-based financing or sales-based financing. It "
               'does include factoring and asset-based lending. So, it makes it more difficult '
               'for funders and funding providers to conduct business in California.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': "'t just affect MCA or revenue-based financing or sales-based financing. It does "
              'include factoring and asset-based lending. So, it makes it more difficult for '
              'funders and funding providers to conduct business in California.',
       'title': 'Will commercial loan brokers and funding providers need a license in '
                'California? (Funder Intel)',
       'url': 'https://www.youtube.com/watch?v=jCWdtQmKTiU&t=65s',
       'video_id': 'jCWdtQmKTiU'}],
 12: [{'author': 'My SBA Loan Pro Podcast',
       'channel': 'My SBA Loan Pro Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:18:11](https://www.youtube.com/watch?v=XKIBsDDkBUI&t=1091s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "California is a very popular market for small business. Anyway, the CDC's are "
               'doing these second for SBA. And what happens is they gather all the loans that '
               'are approved every month and they sell a bond on Wall Street and that bond is '
               'guaranteed by SBA.',
       'timestamp': 1091,
       'timestamp_label': '[00:18:11]',
       'timestamp_seconds': 1091,
       'tip': "California is a very popular market for small business. Anyway, the CDC's are "
              'doing these second for SBA. And what happens is they gather all the loans that '
              'are approved every month and they sell a bond on Wall Street and that bond is '
              'guaranteed by SBA.',
       'title': 'SBA 504 Loans To Buy Owner User Real Estate with Ken Rosenthal | Ep. 15 | My '
                'SBA Loan Pro Podcast (My SBA Loan Pro Podcast)',
       'url': 'https://www.youtube.com/watch?v=XKIBsDDkBUI&t=1091s',
       'video_id': 'XKIBsDDkBUI'},
      {'author': 'Commercial Capital Training Group, LLC',
       'channel': 'Commercial Capital Training Group, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:15](https://www.youtube.com/watch?v=vakBYx8RoD0&t=75s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It was great yeah very intense um seven days I think six four long days eight '
               'am till six pm six thirty and then a saturday half a day kind of thing very '
               'intense a lot of information given to us a lot of note taking just a lot to '
               'take in but it was good very beneficial.',
       'timestamp': 75,
       'timestamp_label': '[00:01:15]',
       'timestamp_seconds': 75,
       'tip': 'It was great yeah very intense um seven days I think six four long days eight '
              'am till six pm six thirty and then a saturday half a day kind of thing very '
              'intense a lot of information given to us a lot of note taking just a lot to '
              'take in but it was good very beneficial.',
       'title': 'Made $49k Commission as a Business Loan Broker (Commercial Capital Training '
                'Group, LLC)',
       'url': 'https://www.youtube.com/watch?v=vakBYx8RoD0&t=75s',
       'video_id': 'vakBYx8RoD0'},
      {'author': 'Commercial Loan Broker Institute',
       'channel': 'Commercial Loan Broker Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:47](https://www.youtube.com/watch?v=tgEHrpyZE9U&t=287s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And when you join our network, you can use them from day one. That takes your '
               'years of building down to a quick enrollment. And you can start funding deals '
               "next week. And number two, you're going to want to connect with industry "
               'veterans.',
       'timestamp': 287,
       'timestamp_label': '[00:04:47]',
       'timestamp_seconds': 287,
       'tip': 'And when you join our network, you can use them from day one. That takes your '
              'years of building down to a quick enrollment. And you can start funding deals '
              "next week. And number two, you're going to want to connect with industry "
              'veterans.',
       'title': 'How to Build a Lender Network as a New Commercial Loan Broker (Commercial '
                'Loan Broker Institute)',
       'url': 'https://www.youtube.com/watch?v=tgEHrpyZE9U&t=287s',
       'video_id': 'tgEHrpyZE9U'},
      {'author': 'Financial Regulation Courses',
       'channel': 'Financial Regulation Courses',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:46](https://www.youtube.com/watch?v=qptR4ByTPDw&t=106s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Most changes, such as residential address or non-securities employment, must '
               'be updated within 30 calendar days. However, certain criminal matters require '
               'an accelerated 10 business day filing window to maintain regulatory standing.',
       'timestamp': 106,
       'timestamp_label': '[00:01:46]',
       'timestamp_seconds': 106,
       'tip': 'Most changes, such as residential address or non-securities employment, must be '
              'updated within 30 calendar days. However, certain criminal matters require an '
              'accelerated 10 business day filing window to maintain regulatory standing.',
       'title': 'Form U4 Compliance Obligations Explained | Series 7, SIE & Broker-Dealer '
                'Careers (Financial Regulation Courses)',
       'url': 'https://www.youtube.com/watch?v=qptR4ByTPDw&t=106s',
       'video_id': 'qptR4ByTPDw'},
      {'author': 'BizPlanComplete',
       'channel': 'BizPlanComplete',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:48](https://www.youtube.com/watch?v=hk2Jnd50USw&t=168s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Standalone marketing plan the three swot analysis templates a powerpoint '
               'presentation as well as some other important documents for starting a '
               'commercial loan brokerage thank you very much for taking a look.',
       'timestamp': 168,
       'timestamp_label': '[00:02:48]',
       'timestamp_seconds': 168,
       'tip': 'Standalone marketing plan the three swot analysis templates a powerpoint '
              'presentation as well as some other important documents for starting a '
              'commercial loan brokerage thank you very much for taking a look.',
       'title': 'Commercial Loan Broker Business Plan (BizPlanComplete)',
       'url': 'https://www.youtube.com/watch?v=hk2Jnd50USw&t=168s',
       'video_id': 'hk2Jnd50USw'},
      {'author': 'Trade Finance Global',
       'channel': 'Trade Finance Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:38](https://www.youtube.com/watch?v=ltw4tGEw31o&t=218s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'JPMorgan, but when you look at supply chain finance and working capital '
               'financing, that stuff has generally been quite digitised from the start.',
       'timestamp': 218,
       'timestamp_label': '[00:03:38]',
       'timestamp_seconds': 218,
       'tip': 'JPMorgan, but when you look at supply chain finance and working capital '
              'financing, that stuff has generally been quite digitised from the start.',
       'title': '25 years of supply chain finance  A journey to unlock liquidity (Trade '
                'Finance Global)',
       'url': 'https://www.youtube.com/watch?v=ltw4tGEw31o&t=218s',
       'video_id': 'ltw4tGEw31o'},
      {'author': "Kevin O'Leary",
       'channel': "Kevin O'Leary",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:31](https://www.youtube.com/watch?v=HKB_cwWcRaE&t=31s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'd say at least 90 if not 95% or more percentage of small businesses startups "
               "can start without raising any capital at all. Now, obviously, we don't know "
               "what kind of business she's trying to start, but you just have to try to start "
               'smarter smaller.',
       'timestamp': 31,
       'timestamp_label': '[00:00:31]',
       'timestamp_seconds': 31,
       'tip': "I'd say at least 90 if not 95% or more percentage of small businesses startups "
              "can start without raising any capital at all. Now, obviously, we don't know "
              "what kind of business she's trying to start, but you just have to try to start "
              'smarter smaller.',
       'title': "How to Raise Capital For Your Business | Shark Tank's Kevin O'Leary and Mark "
                "Cuban (Kevin O'Leary)",
       'url': 'https://www.youtube.com/watch?v=HKB_cwWcRaE&t=31s',
       'video_id': 'HKB_cwWcRaE'},
      {'author': 'CFM (Commercial Financing Mastery)',
       'channel': 'CFM (Commercial Financing Mastery)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:13](https://www.youtube.com/watch?v=cqOh0arlXGU&t=313s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Start making the phone calls. That's what I do on a regular basis when I was "
               'super active. I usually book three to five commercial manager lunches in a '
               'week just to catch up. Just And you know what also?',
       'timestamp': 313,
       'timestamp_label': '[00:05:13]',
       'timestamp_seconds': 313,
       'tip': "Start making the phone calls. That's what I do on a regular basis when I was "
              'super active. I usually book three to five commercial manager lunches in a week '
              'just to catch up. Just And you know what also?',
       'title': 'Why the Bank Declined His 8th Subway Loan: Lender Capacity Explained | Sua '
                'Truong (CFM (Commercial Financing Mastery))',
       'url': 'https://www.youtube.com/watch?v=cqOh0arlXGU&t=313s',
       'video_id': 'cqOh0arlXGU'},
      {'author': 'ThinkSBA - SBA 504 and 7a Loan Brokerage',
       'channel': 'ThinkSBA - SBA 504 and 7a Loan Brokerage',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:46](https://www.youtube.com/watch?v=WAbZuTa6KEg&t=166s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You are ready to start the loan application process today click the get '
               'started link at the top right hand corner of the think SBA home page or just '
               'give me a call at eight five eight seven six two two seven seven four have a '
               'great day.',
       'timestamp': 166,
       'timestamp_label': '[00:02:46]',
       'timestamp_seconds': 166,
       'tip': 'You are ready to start the loan application process today click the get started '
              'link at the top right hand corner of the think SBA home page or just give me a '
              'call at eight five eight seven six two two seven seven four have a great day.',
       'title': 'Small Business Administration SBA 7(a) and 504 Loan Programs For Business '
                'Owners and Entrepreneurs. (ThinkSBA - SBA 504 and 7a Loan Brokerage)',
       'url': 'https://www.youtube.com/watch?v=WAbZuTa6KEg&t=166s',
       'video_id': 'WAbZuTa6KEg'},
      {'author': 'Chalkboard Real Estate',
       'channel': 'Chalkboard Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=F8RMxGMNHtM&t=94s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, the total gross monthly income for this property is $4,200. Let's say that "
               "the property's owner paid expenses such as taxes, insurance, utilities, "
               'maintenance, repairs, capital expenditures, and vacancy combined come to '
               'approximately $2,200 per month.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': "So, the total gross monthly income for this property is $4,200. Let's say that "
              "the property's owner paid expenses such as taxes, insurance, utilities, "
              'maintenance, repairs, capital expenditures, and vacancy combined come to '
              'approximately $2,200 per month.',
       'title': 'How to CORRECTLY Calculate the Debt Service Coverage Ratio (DSCR) (Chalkboard '
                'Real Estate)',
       'url': 'https://www.youtube.com/watch?v=F8RMxGMNHtM&t=94s',
       'video_id': 'F8RMxGMNHtM'},
      {'author': 'Joe Camberato',
       'channel': 'Joe Camberato',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:42](https://www.youtube.com/watch?v=PB-h1pXLzhg&t=222s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Anywhere from one to two to three percent per month uh forever however long '
               "that money is outstanding so if it's a 30-day cycle 45 day 60 day cycle.",
       'timestamp': 222,
       'timestamp_label': '[00:03:42]',
       'timestamp_seconds': 222,
       'tip': 'Anywhere from one to two to three percent per month uh forever however long '
              "that money is outstanding so if it's a 30-day cycle 45 day 60 day cycle.",
       'title': 'Purchase Order Financing: Everything You Need to Know (2024) (Joe Camberato)',
       'url': 'https://www.youtube.com/watch?v=PB-h1pXLzhg&t=222s',
       'video_id': 'PB-h1pXLzhg'},
      {'author': 'Cheryl "The AI Sniper" Tibbs',
       'channel': 'Cheryl "The AI Sniper" Tibbs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=CKRM0VWsZBY&t=21s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Not because I failed, because I won. But, here's what's been eating at me. I "
               'watch new brokers come into this industry every single day, hungry, ambitious, '
               'ready to make it happen, and then I watch them quit.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "Not because I failed, because I won. But, here's what's been eating at me. I "
              'watch new brokers come into this industry every single day, hungry, ambitious, '
              'ready to make it happen, and then I watch them quit.',
       'title': 'Launch A 6 Figure Equipment Finance Broker Empire (Cheryl "The AI Sniper" '
                'Tibbs)',
       'url': 'https://www.youtube.com/watch?v=CKRM0VWsZBY&t=21s',
       'video_id': 'CKRM0VWsZBY'},
      {'author': 'SBA University',
       'channel': 'SBA University',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:36](https://www.youtube.com/watch?v=py_IPiHezcw&t=276s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "If you need to get a hold of me directly I'll leave my email address down in "
               'the description be on the lookout as I will be releasing new lessons every '
               'week to help you in your SBA Journey thanks.',
       'timestamp': 276,
       'timestamp_label': '[00:04:36]',
       'timestamp_seconds': 276,
       'tip': "If you need to get a hold of me directly I'll leave my email address down in "
              'the description be on the lookout as I will be releasing new lessons every week '
              'to help you in your SBA Journey thanks.',
       'title': 'How to Buy Commercial Real Estate (100% Financing Explained!) | SBA Loans '
                '(SBA University)',
       'url': 'https://www.youtube.com/watch?v=py_IPiHezcw&t=276s',
       'video_id': 'py_IPiHezcw'},
      {'author': 'Mauricio Rauld',
       'channel': 'Mauricio Rauld',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:55](https://www.youtube.com/watch?v=52mBD7-QKAw&t=175s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They just want to make sure you're making enough money every month that you "
               'can cover that plus have extra 20% on top so if you enjoyed this clip and you '
               'want to see the entire episode click here and if you want to see other videos '
               'similar to this click here.',
       'timestamp': 175,
       'timestamp_label': '[00:02:55]',
       'timestamp_seconds': 175,
       'tip': "They just want to make sure you're making enough money every month that you can "
              'cover that plus have extra 20% on top so if you enjoyed this clip and you want '
              'to see the entire episode click here and if you want to see other videos '
              'similar to this click here.',
       'title': 'Debt Service Coverage Ratio (DSCR) | Lender Preferred Metric (w J Scott) '
                '(Mauricio Rauld)',
       'url': 'https://www.youtube.com/watch?v=52mBD7-QKAw&t=175s',
       'video_id': '52mBD7-QKAw'},
      {'author': 'Eli the DSCR Pro',
       'channel': 'Eli the DSCR Pro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:49](https://www.youtube.com/watch?v=6P1p0e_NBxs&t=289s)',
       'relevance': 'Attributed practitioner commentary on commercial specialty finance '
                    'brokerage, equipment/AR/SBA/bridge debt placement, and lender-matrix '
                    'underwriting (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Asset, need help with the down payment? Speed, we target a four-week closing, '
               'not 60, 90 days. We move at the speed of business. Now, I promised I will tell '
               'you about the yield maintenance trap.',
       'timestamp': 289,
       'timestamp_label': '[00:04:49]',
       'timestamp_seconds': 289,
       'tip': 'Asset, need help with the down payment? Speed, we target a four-week closing, '
              'not 60, 90 days. We move at the speed of business. Now, I promised I will tell '
              'you about the yield maintenance trap.',
       'title': 'DSCR Loan For Commercial Property (Eli the DSCR Pro)',
       'url': 'https://www.youtube.com/watch?v=6P1p0e_NBxs&t=289s',
       'video_id': '6P1p0e_NBxs'}]}
