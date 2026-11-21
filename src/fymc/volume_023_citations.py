"""Curated 180-citation Mineral Rights baseline (15 per chapter across Q1-Q12) mined strictly from verified Mineral Rights YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'business',
     'buying',
     'calculation',
     'chain',
     'clause',
     'client',
     'clients',
     'commission',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'enverus',
     'estate',
     'firm',
     'flipping',
     'forced',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'budget',
     'buyer',
     'buying',
     'calculation',
     'chain',
     'clause',
     'commission',
     'contract',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'customer',
     'decimal',
     'decision',
     'decline',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'enverus',
     'escrow',
     'estate',
     'fee',
     'fees',
     'flipping',
     'forced',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'buying',
     'calculation',
     'cash',
     'cashflow',
     'chain',
     'clause',
     'commission',
     'corporation',
     'cost',
     'costs',
     'county',
     'curative',
     'curve',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'economics',
     'enverus',
     'estate',
     'flipping',
     'forced',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'budget',
     'buying',
     'calculation',
     'capital',
     'chain',
     'clause',
     'commission',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'entity',
     'enverus',
     'estate',
     'flipping',
     'forced',
     'insurance',
     'lean',
     'license',
     'llc',
     'setup',
     'software',
     'stack',
     'startup',
     'tools'},
 5: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'audit',
     'avoid',
     'bearing',
     'bonus',
     'buying',
     'calculation',
     'chain',
     'clause',
     'clawback',
     'commission',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'dispute',
     'division',
     'docket',
     'drilling',
     'edge',
     'enverus',
     'estate',
     'fail',
     'flipping',
     'forced',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'buying',
     'calculation',
     'chain',
     'clause',
     'client',
     'commission',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'data',
     'deal',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'enverus',
     'estate',
     'find',
     'first',
     'flipping',
     'forced',
     'lead',
     'leads',
     'list',
     'outbound',
     'prospect',
     'qualify',
     'search',
     'sourcing'},
 7: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'buying',
     'calculation',
     'chain',
     'checklist',
     'clause',
     'commission',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'decimal',
     'decline',
     'delivery',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'enverus',
     'estate',
     'execution',
     'flipping',
     'forced',
     'process',
     'quality',
     'sop',
     'step',
     'steps',
     'system',
     'underwriting',
     'verify',
     'workflow'},
 8: {'acquisition',
     'acres',
     'aggregators',
     'allowance',
     'analysis',
     'api',
     'appraisal',
     'bearing',
     'bonus',
     'buying',
     'calculation',
     'chain',
     'clause',
     'commission',
     'corporation',
     'cost',
     'county',
     'crm',
     'curative',
     'curve',
     'data',
     'database',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'division',
     'docket',
     'drilling',
     'enverus',
     'estate',
     'flipping',
     'forced',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'acquisition',
     'acres',
     'aggregators',
     'agreement',
     'allowance',
     'analysis',
     'appraisal',
     'bearing',
     'bonus',
     'buying',
     'calculation',
     'chain',
     'clause',
     'commission',
     'compliance',
     'contract',
     'corporation',
     'cost',
     'county',
     'curative',
     'curve',
     'decimal',
     'decline',
     'depletion',
     'desk',
     'direct',
     'disclosure',
     'division',
     'docket',
     'drilling',
     'enverus',
     'estate',
     'flipping',
     'forced',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'acquisition',
      'acres',
      'agent',
      'aggregators',
      'ai',
      'allowance',
      'analysis',
      'appraisal',
      'automate',
      'automation',
      'bearing',
      'bonus',
      'buying',
      'calculation',
      'chain',
      'clause',
      'commission',
      'corporation',
      'cost',
      'county',
      'curative',
      'curve',
      'dashboard',
      'decimal',
      'decline',
      'depletion',
      'desk',
      'direct',
      'division',
      'docket',
      'drilling',
      'enverus',
      'estate',
      'flipping',
      'forced',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'acquisition',
      'acres',
      'aggregators',
      'allowance',
      'analysis',
      'appraisal',
      'bearing',
      'bonus',
      'buying',
      'calculation',
      'chain',
      'clause',
      'commission',
      'contractor',
      'corporation',
      'cost',
      'county',
      'curative',
      'curve',
      'decimal',
      'decline',
      'depletion',
      'desk',
      'direct',
      'division',
      'docket',
      'drilling',
      'enverus',
      'estate',
      'exit',
      'flipping',
      'forced',
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
 12: {'acquisition',
      'acres',
      'action',
      'aggregators',
      'allowance',
      'analysis',
      'appraisal',
      'bearing',
      'bonus',
      'buying',
      'calculation',
      'chain',
      'clause',
      'commission',
      'corporation',
      'cost',
      'county',
      'curative',
      'curve',
      'day',
      'days',
      'decimal',
      'decline',
      'depletion',
      'desk',
      'direct',
      'division',
      'docket',
      'drilling',
      'enverus',
      'estate',
      'flipping',
      'forced',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'LMJ Land Services',
      'channel': 'LMJ Land Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=IBxLIQjDNto&t=129s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If it doesn't tie, something is wrong, and I go back to the deeds. On my "
              'report, each figure shows its math and the instrument it comes from, by volume '
              'and page. Net mineral acres for bonus and leasing. The royalty decimal for the '
              'division order.',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': "If it doesn't tie, something is wrong, and I go back to the deeds. On my report, "
             'each figure shows its math and the instrument it comes from, by volume and page. '
             'Net mineral acres for bonus and leasing. The royalty decimal for the division '
             'order.',
      'title': 'Net Mineral Acres, Royalty Decimal and NPRI: Three Different Numbers | LMJ '
               'Chalk Talk Ep 22 (LMJ Land Services)',
      'url': 'https://www.youtube.com/watch?v=IBxLIQjDNto&t=129s',
      'video_id': 'IBxLIQjDNto'},
     {'author': 'Neil Jesani Tax Advisors',
      'channel': 'Neil Jesani Tax Advisors',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=FagQvbKX71g&t=50s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The part that is not an intangible drilling cost is eligible for depreciation '
              "under section 168. Much like anything that's eligible for depreciation, it is "
              'also eligible for bonus depreciation. Currently, bonus depreciation is 40% of '
              'the assets placed in service.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'The part that is not an intangible drilling cost is eligible for depreciation '
             "under section 168. Much like anything that's eligible for depreciation, it is "
             'also eligible for bonus depreciation. Currently, bonus depreciation is 40% of '
             'the assets placed in service.',
      'title': 'How to MAXIMIZE OIL\xa0&\xa0GAS TAX DEDUCTIONS (Neil Jesani Tax Advisors)',
      'url': 'https://www.youtube.com/watch?v=FagQvbKX71g&t=50s',
      'video_id': 'FagQvbKX71g'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=p0bOEBxdOFs&t=160s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One basin, one county, one formation. And remember that minerals that never get '
              'developed have zero value. So, you go where the operators are actually '
              'drilling. And this is the hardest part of the whole business.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'One basin, one county, one formation. And remember that minerals that never get '
             'developed have zero value. So, you go where the operators are actually drilling. '
             'And this is the hardest part of the whole business.',
      'title': 'What Landman Gets Completely Wrong (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=p0bOEBxdOFs&t=160s',
      'video_id': 'p0bOEBxdOFs'},
     {'author': 'Mr. Business',
      'channel': 'Mr. Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:29](https://www.youtube.com/watch?v=hIerB5MQ52U&t=1169s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Understand the geology, the operator, the lease terms, and the decline curve. '
              'Have a lawyer verify title, model the cash flows under different oil prices, '
              'and only invest money you can afford to have tied up and potentially lose.',
      'timestamp': 1169,
      'timestamp_label': '[00:19:29]',
      'timestamp_seconds': 1169,
      'tip': 'Understand the geology, the operator, the lease terms, and the decline curve. '
             'Have a lawyer verify title, model the cash flows under different oil prices, and '
             'only invest money you can afford to have tied up and potentially lose.',
      'title': 'The Economics of Owning an Oil Well Royalty Interest (Mr. Business)',
      'url': 'https://www.youtube.com/watch?v=hIerB5MQ52U&t=1169s',
      'video_id': 'hIerB5MQ52U'},
     {'author': 'PetroPeak Investments LLC',
      'channel': 'PetroPeak Investments LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=zHSS1bvXiNk&t=91s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That lease can include an upfront upfront bonus payment and a royalty '
              'percentage that determines how much of the production revenue the mineral owner '
              "receives. Let's say you own 100 mineral acres, and an operator offers a lease "
              'with a 20% royalty.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'That lease can include an upfront upfront bonus payment and a royalty percentage '
             'that determines how much of the production revenue the mineral owner receives. '
             "Let's say you own 100 mineral acres, and an operator offers a lease with a 20% "
             'royalty.',
      'title': 'Mineral vs. Royalty: Stop Making This Investment Mistake (PetroPeak '
               'Investments LLC)',
      'url': 'https://www.youtube.com/watch?v=zHSS1bvXiNk&t=91s',
      'video_id': 'zHSS1bvXiNk'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:19](https://www.youtube.com/watch?v=IrkmOVOU8E8&t=859s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's always been assumed, Matt, that the wastewater was owned by the operator, "
              "but this is because it's always been seen as a burden and a cost to dispose of "
              "this. Um, and now that there's value found in it, it's kind of shaking the "
              'waters here.',
      'timestamp': 859,
      'timestamp_label': '[00:14:19]',
      'timestamp_seconds': 859,
      'tip': "It's always been assumed, Matt, that the wastewater was owned by the operator, "
             "but this is because it's always been seen as a burden and a cost to dispose of "
             "this. Um, and now that there's value found in it, it's kind of shaking the "
             'waters here.',
      'title': 'MRP 299:  Mineral Rights News September 2025 (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=IrkmOVOU8E8&t=859s',
      'video_id': 'IrkmOVOU8E8'},
     {'author': 'Bison Interests',
      'channel': 'Bison Interests',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:03](https://www.youtube.com/watch?v=5sPOq_WPRHQ&t=1563s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And people are still putting tons of money in these ETFs, which is amazing. We '
              "think that there's just so much value in being careful, value-oriented stock "
              'pickers versus broad passive market exposure or even ownership of these sector '
              'ETFs.',
      'timestamp': 1563,
      'timestamp_label': '[00:26:03]',
      'timestamp_seconds': 1563,
      'tip': 'And people are still putting tons of money in these ETFs, which is amazing. We '
             "think that there's just so much value in being careful, value-oriented stock "
             'pickers versus broad passive market exposure or even ownership of these sector '
             'ETFs.',
      'title': 'Facing Into the Storm: Investing in Small Cap Oil Companies (Bison Interests)',
      'url': 'https://www.youtube.com/watch?v=5sPOq_WPRHQ&t=1563s',
      'video_id': '5sPOq_WPRHQ'},
     {'author': 'Eckard Enterprises | Oil & Gas Investing',
      'channel': 'Eckard Enterprises | Oil & Gas Investing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=OoeKDlEjyqc&t=23s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you have successful wells, the income you generate from investing in oil and '
              'gas allows 15% of your income to be taxfree. Do I get big tax deductions? Do I '
              'get tax write offs this year? The Internal Revenue Service provided way back in '
              '1986 in the Tax Reform Act.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': 'If you have successful wells, the income you generate from investing in oil and '
             'gas allows 15% of your income to be taxfree. Do I get big tax deductions? Do I '
             'get tax write offs this year? The Internal Revenue Service provided way back in '
             '1986 in the Tax Reform Act.',
      'title': 'Preserve Wealth & Maximize Deductions Through Oil & Gas Working Interest '
               '(Eckard Enterprises | Oil & Gas Investing)',
      'url': 'https://www.youtube.com/watch?v=OoeKDlEjyqc&t=23s',
      'video_id': 'OoeKDlEjyqc'},
     {'author': 'Tracy Lenz',
      'channel': 'Tracy Lenz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:47](https://www.youtube.com/watch?v=HGUBxgz_6Ak&t=1427s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our engineering model, which is working towards getting an on demand value that '
              'you can pull for any minerals right now.',
      'timestamp': 1427,
      'timestamp_label': '[00:23:47]',
      'timestamp_seconds': 1427,
      'tip': 'Our engineering model, which is working towards getting an on demand value that '
             'you can pull for any minerals right now.',
      'title': "Oil & Gas Lease Royalties: Beginner's Guide for Mineral Owners (with "
               'examples!) (Tracy Lenz)',
      'url': 'https://www.youtube.com/watch?v=HGUBxgz_6Ak&t=1427s',
      'video_id': 'HGUBxgz_6Ak'},
     {'author': 'Blue Mesa Minerals',
      'channel': 'Blue Mesa Minerals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:36](https://www.youtube.com/watch?v=SfX6ycoYg24&t=516s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That I'll just send their form back it's fine um but if they've got some "
              "interesting language in there I'm going to use the model form.",
      'timestamp': 516,
      'timestamp_label': '[00:08:36]',
      'timestamp_seconds': 516,
      'tip': "That I'll just send their form back it's fine um but if they've got some "
             "interesting language in there I'm going to use the model form.",
      'title': 'Oil and Gas Division Orders (Blue Mesa Minerals)',
      'url': 'https://www.youtube.com/watch?v=SfX6ycoYg24&t=516s',
      'video_id': 'SfX6ycoYg24'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=WvlIfeyW4-Q&t=172s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thousands of Acres of mineral rights every single year how do we do it well we '
              'provide a valuable service to Mineral owners across the country liquidity.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'Thousands of Acres of mineral rights every single year how do we do it well we '
             'provide a valuable service to Mineral owners across the country liquidity.',
      'title': 'Can Mineral Rights Make You Rich? (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=WvlIfeyW4-Q&t=172s',
      'video_id': 'WvlIfeyW4-Q'},
     {'author': 'UHD Continuing and Professional Education',
      'channel': 'UHD Continuing and Professional Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:27](https://www.youtube.com/watch?v=oHKF06pFkh0&t=627s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "On each of the leases separately from one another in other words you can't "
              "co-mingle them and think that you're going to come back to the same number that "
              'you calculated by simply taking the gross and subtracting the burdens.',
      'timestamp': 627,
      'timestamp_label': '[00:10:27]',
      'timestamp_seconds': 627,
      'tip': "On each of the leases separately from one another in other words you can't "
             "co-mingle them and think that you're going to come back to the same number that "
             'you calculated by simply taking the gross and subtracting the burdens.',
      'title': 'Calculating the Oil Company’s Net Revenue Interest (UHD Continuing and '
               'Professional Education)',
      'url': 'https://www.youtube.com/watch?v=oHKF06pFkh0&t=627s',
      'video_id': 'oHKF06pFkh0'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:39](https://www.youtube.com/watch?v=HkEK5QVZAJ0&t=99s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So now Charlie owns this 3% royalty interest. B did not give away any of his '
              'minerals, so he still owns 100% of the minerals. But then Charlie conveys 100% '
              'of the minerals to David. So, now B no longer owns this 100%. Net revenue '
              'interest or mineral interest.',
      'timestamp': 99,
      'timestamp_label': '[00:01:39]',
      'timestamp_seconds': 99,
      'tip': 'So now Charlie owns this 3% royalty interest. B did not give away any of his '
             'minerals, so he still owns 100% of the minerals. But then Charlie conveys 100% '
             'of the minerals to David. So, now B no longer owns this 100%. Net revenue '
             'interest or mineral interest.',
      'title': 'Situation #5 WI & NRI Calculations p  70 AAPL  Study Guide (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=HkEK5QVZAJ0&t=99s',
      'video_id': 'HkEK5QVZAJ0'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=WIqkczvqoz0&t=307s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's no contact information and there's no physical address listed for the "
              'business most legitimate mineral buying companies.',
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': "There's no contact information and there's no physical address listed for the "
             'business most legitimate mineral buying companies.',
      'title': 'Watch This Before Selling Mineral Rights! | Types of Mineral Buyers and Who to '
               'Avoid! (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=WIqkczvqoz0&t=307s',
      'video_id': 'WIqkczvqoz0'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:42](https://www.youtube.com/watch?v=M3eFdVkW_mY&t=1002s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So that business situation or business scenario must really be there you know '
              'for the operator to pursue um you know national forest lands.',
      'timestamp': 1002,
      'timestamp_label': '[00:16:42]',
      'timestamp_seconds': 1002,
      'tip': 'So that business situation or business scenario must really be there you know '
             'for the operator to pursue um you know national forest lands.',
      'title': 'MRP 319:  Mineral Rights News February 2026 (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=M3eFdVkW_mY&t=1002s',
      'video_id': 'M3eFdVkW_mY'}],
 2: [{'author': 'National Association of Royalty Owners',
      'channel': 'National Association of Royalty Owners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:11](https://www.youtube.com/watch?v=o8FqhVu6MNM&t=371s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The well name, legal description, county and state, and the family member's "
              'name, who they may have in their records. Ask specific questions such as how a '
              'division order decimal was calculated or which sales month a payment covers.',
      'timestamp': 371,
      'timestamp_label': '[00:06:11]',
      'timestamp_seconds': 371,
      'tip': "The well name, legal description, county and state, and the family member's "
             'name, who they may have in their records. Ask specific questions such as how a '
             'division order decimal was calculated or which sales month a payment covers.',
      'title': 'Mineral Rights Explained: What You Own and Where to Start (National '
               'Association of Royalty Owners)',
      'url': 'https://www.youtube.com/watch?v=o8FqhVu6MNM&t=371s',
      'video_id': 'o8FqhVu6MNM'},
     {'author': 'New Mexico Oil Conservation Commission',
      'channel': 'New Mexico Oil Conservation Commission',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=-7pNwWErBfk&t=152s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The good news is New Mexicans overwhelmingly support fixing this. Nearly nine '
              'in 10 voters say oil and gas corporations should pay the full cost of cleanup. '
              'Even our own state land office and oil conservation division support the '
              'proposed rule changes.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'The good news is New Mexicans overwhelmingly support fixing this. Nearly nine in '
             '10 voters say oil and gas corporations should pay the full cost of cleanup. Even '
             'our own state land office and oil conservation division support the proposed '
             'rule changes.',
      'title': 'OCC Rulemaking Hearing Part 15  10 27 25 (New Mexico Oil Conservation '
               'Commission)',
      'url': 'https://www.youtube.com/watch?v=-7pNwWErBfk&t=152s',
      'video_id': '-7pNwWErBfk'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:41](https://www.youtube.com/watch?v=YeBHUAmigMw&t=641s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Worth at the time the company exxon in this case gave it had middleton signed a '
              "division order that said I'm going to pay you based on the contract price not "
              "on the market value price so that's kind of like the terror rule like what they "
              'have in oklahoma.',
      'timestamp': 641,
      'timestamp_label': '[00:10:41]',
      'timestamp_seconds': 641,
      'tip': 'Worth at the time the company exxon in this case gave it had middleton signed a '
             "division order that said I'm going to pay you based on the contract price not on "
             "the market value price so that's kind of like the terror rule like what they "
             'have in oklahoma.',
      'title': 'Oil & Gas 17A: Division Orders (Energy Law Professor)',
      'url': 'https://www.youtube.com/watch?v=YeBHUAmigMw&t=641s',
      'video_id': 'YeBHUAmigMw'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=ifwy0MQE0b4&t=86s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So we would render drilling and division order title opinions right back to the '
              'oil and gas company. So, why does the oil and gas company do all this work '
              'beforehand? Because they need to know who to pay.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'So we would render drilling and division order title opinions right back to the '
             'oil and gas company. So, why does the oil and gas company do all this work '
             'beforehand? Because they need to know who to pay.',
      'title': 'What Landmen Actually Do (No One Explains This) (Steven Hatcher | Minerals '
               'Guy)',
      'url': 'https://www.youtube.com/watch?v=ifwy0MQE0b4&t=86s',
      'video_id': 'ifwy0MQE0b4'},
     {'author': 'The Byte-Size Brief',
      'channel': 'The Byte-Size Brief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:06](https://www.youtube.com/watch?v=Kwv0e2yhRmA&t=726s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That Tetris analogy perfectly explains their cost advantage. Look, if you own '
              "two non-adjacent parcels of land separated by a competitor's lease, you have to "
              'pay two separate drilling crews to set up two separate rigs and drill two '
              'individual one-mile vertical wells.',
      'timestamp': 726,
      'timestamp_label': '[00:12:06]',
      'timestamp_seconds': 726,
      'tip': 'That Tetris analogy perfectly explains their cost advantage. Look, if you own '
             "two non-adjacent parcels of land separated by a competitor's lease, you have to "
             'pay two separate drilling crews to set up two separate rigs and drill two '
             'individual one-mile vertical wells.',
      'title': 'Permian Resources (PR): How They Beat Negative Gas Prices (The Byte-Size '
               'Brief)',
      'url': 'https://www.youtube.com/watch?v=Kwv0e2yhRmA&t=726s',
      'video_id': 'Kwv0e2yhRmA'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:06](https://www.youtube.com/watch?v=PjGnR-YfLy4&t=366s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Quarter of section 10. hiroshima drilling leases all 160 acres northwest uh is '
              '160 acres from harry truman for a 1 8 royalty payment so what we can do here is '
              "now we can look at before the lease harry truman owns well let's put his name "
              "here he's the mineral owner.",
      'timestamp': 366,
      'timestamp_label': '[00:06:06]',
      'timestamp_seconds': 366,
      'tip': 'Quarter of section 10. hiroshima drilling leases all 160 acres northwest uh is '
             '160 acres from harry truman for a 1 8 royalty payment so what we can do here is '
             "now we can look at before the lease harry truman owns well let's put his name "
             "here he's the mineral owner.",
      'title': 'III  GWI & NRI in an Oil & Gas Lease   One Owner Example 1 (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=PjGnR-YfLy4&t=366s',
      'video_id': 'PjGnR-YfLy4'},
     {'author': 'Richard Winblad',
      'channel': 'Richard Winblad',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=iD4uCjptCXM&t=221s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before receiving payments is violative of public policy and they ruled for the '
              "mineral interest owner here's my favorite part the company withholding payments "
              'was require required to pay the owners attorney fees and costs.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'Before receiving payments is violative of public policy and they ruled for the '
             "mineral interest owner here's my favorite part the company withholding payments "
             'was require required to pay the owners attorney fees and costs.',
      'title': 'Don’t Sign that Division Order! (Richard Winblad)',
      'url': 'https://www.youtube.com/watch?v=iD4uCjptCXM&t=221s',
      'video_id': 'iD4uCjptCXM'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:25](https://www.youtube.com/watch?v=y5etlsUEcO0&t=1105s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'d be interested but we need marketable title and here's what has to happen on "
              "the buyer side. You know this is a a business decision and that they're looking "
              'into what this might cost and and where it stands currently.',
      'timestamp': 1105,
      'timestamp_label': '[00:18:25]',
      'timestamp_seconds': 1105,
      'tip': "'d be interested but we need marketable title and here's what has to happen on "
             "the buyer side. You know this is a a business decision and that they're looking "
             'into what this might cost and and where it stands currently.',
      'title': 'MRP 310:  Strategic Portfolio Management: How to Sell Mineral Rights at Peak '
               'Value (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=y5etlsUEcO0&t=1105s',
      'video_id': 'y5etlsUEcO0'},
     {'author': 'Venergy Momentum Oil & Gas',
      'channel': 'Venergy Momentum Oil & Gas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=175xk8ZQHpI&t=163s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The surface while keeping the mineral rights however to do this one would need '
              'to specifically withhold or as we say reserve the mineral rights during the '
              'sale this is very important because whatever rights are not reserved during a '
              'sale will pass to the buyer.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'The surface while keeping the mineral rights however to do this one would need '
             'to specifically withhold or as we say reserve the mineral rights during the sale '
             'this is very important because whatever rights are not reserved during a sale '
             'will pass to the buyer.',
      'title': 'Q&A for Mineral and Royalty Owners (Venergy Momentum Oil & Gas)',
      'url': 'https://www.youtube.com/watch?v=175xk8ZQHpI&t=163s',
      'video_id': '175xk8ZQHpI'},
     {'author': 'Railroad Commission of Texas',
      'channel': 'Railroad Commission of Texas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=dgKvg8N8xd8&t=130s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At rrc.texas.gov once approved authenticated users can add files to a docket or '
              'case and may download additional information to enhance the efficiency of the '
              'user and agency an in-depth user guide can be found within the application '
              'questions contact us at publicassist.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'At rrc.texas.gov once approved authenticated users can add files to a docket or '
             'case and may download additional information to enhance the efficiency of the '
             'user and agency an in-depth user guide can be found within the application '
             'questions contact us at publicassist.',
      'title': 'Introducing RRC CASES (Railroad Commission of Texas)',
      'url': 'https://www.youtube.com/watch?v=dgKvg8N8xd8&t=130s',
      'video_id': 'dgKvg8N8xd8'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=B5fBIyi1-hw&t=153s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pays for that override the oil and gas company pays for it so the payment of '
              "the override is taken out of this 7 8 net revenue interest so now they're going "
              'to have to deduct 0.03 to get the oil and gas companies total net revenue '
              'interest.',
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': 'Pays for that override the oil and gas company pays for it so the payment of the '
             "override is taken out of this 7 8 net revenue interest so now they're going to "
             'have to deduct 0.03 to get the oil and gas companies total net revenue interest.',
      'title': 'Situation #3 WI & NRI Calculations AAPL Study Guide PG 70 (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=B5fBIyi1-hw&t=153s',
      'video_id': 'B5fBIyi1-hw'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:35](https://www.youtube.com/watch?v=inopKiaG-3A&t=395s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And working interests as well and so what it will include is the decimal '
              'ownership and the type of interest and this is something you need to pay.',
      'timestamp': 395,
      'timestamp_label': '[00:06:35]',
      'timestamp_seconds': 395,
      'tip': 'And working interests as well and so what it will include is the decimal '
             'ownership and the type of interest and this is something you need to pay.',
      'title': 'MRP 16: What You Need to Know about Oil & Gas Division Orders (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=inopKiaG-3A&t=395s',
      'video_id': 'inopKiaG-3A'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=QKOAcxHhi_I&t=76s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Talking about the Shale Revolution and the birth of the professional mineral '
              "buyer so let's jump in in the mid-2000s there was a rebirth of.",
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': 'Talking about the Shale Revolution and the birth of the professional mineral '
             "buyer so let's jump in in the mid-2000s there was a rebirth of.",
      'title': 'Own Mineral Rights? | Learn about the Shale Revolution and the Market for Oil '
               'and Gas Royalties! (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=QKOAcxHhi_I&t=76s',
      'video_id': 'QKOAcxHhi_I'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:51](https://www.youtube.com/watch?v=RR2BlQf14H8&t=1791s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And companies are beginning to reinvest and drilling new wells they're going to "
              "be looking at private land or that fee acreage and so that's.",
      'timestamp': 1791,
      'timestamp_label': '[00:29:51]',
      'timestamp_seconds': 1791,
      'tip': "And companies are beginning to reinvest and drilling new wells they're going to "
             "be looking at private land or that fee acreage and so that's.",
      'title': 'MRP 70: 5 Tips if You Are Thinking About Selling Mineral Rights (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=RR2BlQf14H8&t=1791s',
      'video_id': 'RR2BlQf14H8'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:02](https://www.youtube.com/watch?v=5hXDw_OFeQc&t=722s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Guide.com you can also reach me by email Stephen minerals guide.com with any '
              "questions thanks again and we'll see you next time.",
      'timestamp': 722,
      'timestamp_label': '[00:12:02]',
      'timestamp_seconds': 722,
      'tip': 'Guide.com you can also reach me by email Stephen minerals guide.com with any '
             "questions thanks again and we'll see you next time.",
      'title': 'How To Locate Your Minerals On A Map (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=5hXDw_OFeQc&t=722s',
      'video_id': '5hXDw_OFeQc'}],
 3: [{'author': 'LMJ Land Services',
      'channel': 'LMJ Land Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=sLCs9xQypFE&t=64s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I find the completion depths on the Railroad Commission forms. On our demo '
              'deal, lease three covers the south half of the southeast quarter of section 59, '
              "80 acres. It's only production is from a unit that takes in 40 of them. The "
              'lease has an acreage Pugh clause.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'I find the completion depths on the Railroad Commission forms. On our demo deal, '
             'lease three covers the south half of the southeast quarter of section 59, 80 '
             "acres. It's only production is from a unit that takes in 40 of them. The lease "
             'has an acreage Pugh clause.',
      'title': 'The Pugh Clause in an Acquisition | LMJ Chalk Talk (LMJ Land Services)',
      'url': 'https://www.youtube.com/watch?v=sLCs9xQypFE&t=64s',
      'video_id': 'sLCs9xQypFE'},
     {'author': 'PetroPeak Investments LLC',
      'channel': 'PetroPeak Investments LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=vcDs5GtSP6Q&t=211s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, why are investors interested in oil and gas minerals? They can provide '
              'direct exposure to oil and natural gas production. They can generate ongoing '
              "cash distributions. They don't generally require the mineral owner to fund "
              'drilling or operating costs.',
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': 'So, why are investors interested in oil and gas minerals? They can provide '
             'direct exposure to oil and natural gas production. They can generate ongoing '
             "cash distributions. They don't generally require the mineral owner to fund "
             'drilling or operating costs.',
      'title': 'How Mineral Owners Get Paid (The Truth About Royalties) (PetroPeak Investments '
               'LLC)',
      'url': 'https://www.youtube.com/watch?v=vcDs5GtSP6Q&t=211s',
      'video_id': 'vcDs5GtSP6Q'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:37](https://www.youtube.com/watch?v=yWZaJ-ItXKQ&t=577s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's going to be a 1/32 interest and so we know that that calculation is "
              '0.03 one to five sorry I went off the map there but that is what the landowners '
              "decimal is going to be if they are only part of a unit we're going to basically "
              'take their net acres.',
      'timestamp': 577,
      'timestamp_label': '[00:09:37]',
      'timestamp_seconds': 577,
      'tip': "So that's going to be a 1/32 interest and so we know that that calculation is "
             '0.03 one to five sorry I went off the map there but that is what the landowners '
             "decimal is going to be if they are only part of a unit we're going to basically "
             'take their net acres.',
      'title': 'Working Interest & Net Revenue Interests in Oil & Gas Lease Calculations (Land '
               'Training www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=yWZaJ-ItXKQ&t=577s',
      'video_id': 'yWZaJ-ItXKQ'},
     {'author': 'The Wealth Transfer Podcast',
      'channel': 'The Wealth Transfer Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:36](https://www.youtube.com/watch?v=mcQ5KsrbKzc&t=1656s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The, the other thing I'll, I'll mention too, you know, one, when we talk about "
              'IDC funds, that is specific to non-op working interests. So minerals do not '
              "have drilling costs. As I mentioned in the beginning, you don't have cost "
              'exposure.',
      'timestamp': 1656,
      'timestamp_label': '[00:27:36]',
      'timestamp_seconds': 1656,
      'tip': "The, the other thing I'll, I'll mention too, you know, one, when we talk about "
             'IDC funds, that is specific to non-op working interests. So minerals do not have '
             "drilling costs. As I mentioned in the beginning, you don't have cost exposure.",
      'title': 'Oil, Gas, Mineral Rights & Royalties: A Guide to Protecting & Transferring '
               'Family Wealth | Tim Pawul (The Wealth Transfer Podcast)',
      'url': 'https://www.youtube.com/watch?v=mcQ5KsrbKzc&t=1656s',
      'video_id': 'mcQ5KsrbKzc'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:53](https://www.youtube.com/watch?v=5Cx7zTkAJdw&t=1733s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But since you mentioned that there has been drilling and production going on '
              "for 26 years now, it's uh possible that if you weren't leased, that you were "
              'forced pooled, it was it part of a compulsory unit.',
      'timestamp': 1733,
      'timestamp_label': '[00:28:53]',
      'timestamp_seconds': 1733,
      'tip': 'But since you mentioned that there has been drilling and production going on for '
             "26 years now, it's uh possible that if you weren't leased, that you were forced "
             'pooled, it was it part of a compulsory unit.',
      'title': 'MRP 358: Listener Questions November 2026 (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=5Cx7zTkAJdw&t=1733s',
      'video_id': '5Cx7zTkAJdw'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:46](https://www.youtube.com/watch?v=WPeA0rs7SLA&t=406s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Brown owns a mineral interest in a 160 acres of land he leases his land to '
              'Cajun drilling for a 1 8 royalty interest Cajun drilling requests a well permit '
              'for gas and forms a 640 acre pooled unit this could be a pooling Unit Drilling '
              'and spacing unit.',
      'timestamp': 406,
      'timestamp_label': '[00:06:46]',
      'timestamp_seconds': 406,
      'tip': 'Brown owns a mineral interest in a 160 acres of land he leases his land to Cajun '
             'drilling for a 1 8 royalty interest Cajun drilling requests a well permit for '
             'gas and forms a 640 acre pooled unit this could be a pooling Unit Drilling and '
             'spacing unit.',
      'title': 'IV NRI Calculations of Mineral Owner Pooled Unit Problem 1 (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=WPeA0rs7SLA&t=406s',
      'video_id': 'WPeA0rs7SLA'},
     {'author': 'KXAN',
      'channel': 'KXAN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=d7YKQPVyHYc&t=92s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "PRICES AND RESTORING TRANSPARENCY TO THE COMMISSION DURING LAST FEBRUARY'S "
              'WINTER STORM. NATURAL GAS PRICES WENT UP HUNDREDS OF TIMES OVERNIGHT. AND THE '
              "RAILROAD COMMISSION'S JOB IS TO PROTECT CONSUMERS AND MAKE SURE THAT PRICE "
              "GOUGING OR NEFARIOUS BEHAVIOR DIDN'T HAPPEN.",
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "PRICES AND RESTORING TRANSPARENCY TO THE COMMISSION DURING LAST FEBRUARY'S "
             'WINTER STORM. NATURAL GAS PRICES WENT UP HUNDREDS OF TIMES OVERNIGHT. AND THE '
             "RAILROAD COMMISSION'S JOB IS TO PROTECT CONSUMERS AND MAKE SURE THAT PRICE "
             "GOUGING OR NEFARIOUS BEHAVIOR DIDN'T HAPPEN.",
      'title': "What does the Texas Railroad Commissioner do, and who's running? (KXAN)",
      'url': 'https://www.youtube.com/watch?v=d7YKQPVyHYc&t=92s',
      'video_id': 'd7YKQPVyHYc'},
     {'author': 'Landman Class',
      'channel': 'Landman Class',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:56](https://www.youtube.com/watch?v=ibeQr-rDmZ4&t=656s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thirteen times six miles east to get to that particular Township inside that '
              'temp will be working on section ten section 10 is 640 acres so section.',
      'timestamp': 656,
      'timestamp_label': '[00:10:56]',
      'timestamp_seconds': 656,
      'tip': 'Thirteen times six miles east to get to that particular Township inside that '
             'temp will be working on section ten section 10 is 640 acres so section.',
      'title': 'Basic Title - Landman Training (Landman Class)',
      'url': 'https://www.youtube.com/watch?v=ibeQr-rDmZ4&t=656s',
      'video_id': 'ibeQr-rDmZ4'},
     {'author': 'GeoFins',
      'channel': 'GeoFins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:39](https://www.youtube.com/watch?v=xL3_8adbQ4Q&t=339s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2016 assessment of it just the Midland Basin portion alone already outsized the '
              'entire combined Bakken and Three Forks estimate from 2013 by a wide margin '
              "before the Delaware Basin's own numbers had even been calculated.",
      'timestamp': 339,
      'timestamp_label': '[00:05:39]',
      'timestamp_seconds': 339,
      'tip': '2016 assessment of it just the Midland Basin portion alone already outsized the '
             'entire combined Bakken and Three Forks estimate from 2013 by a wide margin '
             "before the Delaware Basin's own numbers had even been calculated.",
      'title': "This Hidden Oil Field Beneath Texas's Permian Basin Could Change Everything "
               '(GeoFins)',
      'url': 'https://www.youtube.com/watch?v=xL3_8adbQ4Q&t=339s',
      'video_id': 'xL3_8adbQ4Q'},
     {'author': 'WXYZ-TV Detroit | Channel 7',
      'channel': 'WXYZ-TV Detroit | Channel 7',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=Wvs9BxP1JfA&t=87s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The city has a temporary moratorium on drilling until late April meantime the '
              'city of southfield telling us they will request a temporary restraining order '
              'if necessary so much more on this could still play out live in southfield Simon '
              'shake at 7 Action News.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': 'The city has a temporary moratorium on drilling until late April meantime the '
             'city of southfield telling us they will request a temporary restraining order if '
             'necessary so much more on this could still play out live in southfield Simon '
             'shake at 7 Action News.',
      'title': 'Michigan DEQ allows permit to drill for oil in Southfield (WXYZ-TV Detroit | '
               'Channel 7)',
      'url': 'https://www.youtube.com/watch?v=Wvs9BxP1JfA&t=87s',
      'video_id': 'Wvs9BxP1JfA'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:35:37](https://www.youtube.com/watch?v=dM8LufO_Emg&t=2137s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Shared with each landowner at a 1/8 share so these are the some some of the '
              "kinds of disputes that can arise and in our next lesson we're going to see some "
              'of the other very complex disputes that can arise in pricing a natural gas '
              'royalty.',
      'timestamp': 2137,
      'timestamp_label': '[00:35:37]',
      'timestamp_seconds': 2137,
      'tip': 'Shared with each landowner at a 1/8 share so these are the some some of the '
             "kinds of disputes that can arise and in our next lesson we're going to see some "
             'of the other very complex disputes that can arise in pricing a natural gas '
             'royalty.',
      'title': 'Introduction to Royalties (Oil & Gas 14.1) (Energy Law Professor)',
      'url': 'https://www.youtube.com/watch?v=dM8LufO_Emg&t=2137s',
      'video_id': 'dM8LufO_Emg'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=ehsvjfRcJIM&t=195s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Estate and the surface estate could be separated and finally the last concept '
              'that I think is important to discuss is the concept that the mineral estate is.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'Estate and the surface estate could be separated and finally the last concept '
             'that I think is important to discuss is the concept that the mineral estate is.',
      'title': 'Selling Mineral Rights? | Learn about the History of Mineral Buying and How to '
               'Protect Yourself! (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=ehsvjfRcJIM&t=195s',
      'video_id': 'ehsvjfRcJIM'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:06](https://www.youtube.com/watch?v=zoP-dgL5D7M&t=1446s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It is there kind of a standard cost that you see or a range of costs that you '
              'see when working for middle right owners and individuals or and i know that '
              'can.',
      'timestamp': 1446,
      'timestamp_label': '[00:24:06]',
      'timestamp_seconds': 1446,
      'tip': 'It is there kind of a standard cost that you see or a range of costs that you '
             'see when working for middle right owners and individuals or and i know that can.',
      'title': 'MRP 11: Oil and Gas Title Defects and Curative Measures (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=zoP-dgL5D7M&t=1446s',
      'video_id': 'zoP-dgL5D7M'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:04](https://www.youtube.com/watch?v=86mQK92f7Bg&t=1144s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Based on that that's that cash flow analysis and so that's something that could "
              'take an experienced person um a couple hours to perform.',
      'timestamp': 1144,
      'timestamp_label': '[00:19:04]',
      'timestamp_seconds': 1144,
      'tip': "Based on that that's that cash flow analysis and so that's something that could "
             'take an experienced person um a couple hours to perform.',
      'title': 'MRP 4: How Mineral Rights are Valued (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=86mQK92f7Bg&t=1144s',
      'video_id': '86mQK92f7Bg'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:05](https://www.youtube.com/watch?v=DcdI-1zyjQo&t=245s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You have any questions for us you can reach us on the website mineralsguide.com '
              "and you can also reach me personally by email Steven mineralsguy.com we'll see "
              'you in the next episode.',
      'timestamp': 245,
      'timestamp_label': '[00:04:05]',
      'timestamp_seconds': 245,
      'tip': 'You have any questions for us you can reach us on the website mineralsguide.com '
             "and you can also reach me personally by email Steven mineralsguy.com we'll see "
             'you in the next episode.',
      'title': 'Mineral Rights Management 101 | How to Manage Your Mineral Rights Like the '
               "Pro's (Steven Hatcher | Minerals Guy)",
      'url': 'https://www.youtube.com/watch?v=DcdI-1zyjQo&t=245s',
      'video_id': 'DcdI-1zyjQo'}],
 4: [{'author': 'Danomics',
      'channel': 'Danomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=gleafhkBQWg&t=15s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "How to use the decline curve calculation flow tools that we've recently "
              "developed so as you're aware denomix has a production analysis module that "
              'allows.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "How to use the decline curve calculation flow tools that we've recently "
             "developed so as you're aware denomix has a production analysis module that "
             'allows.',
      'title': 'Decline Curve Analysis with Danomics Flows (Danomics)',
      'url': 'https://www.youtube.com/watch?v=gleafhkBQWg&t=15s',
      'video_id': 'gleafhkBQWg'},
     {'author': 'Enverus',
      'channel': 'Enverus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:17](https://www.youtube.com/watch?v=hYa6oTD7seU&t=1217s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Obtaining meaningful disk spacing distances the creation of wellness using the '
              'well targeting and decline curve tools can be quite powerful.',
      'timestamp': 1217,
      'timestamp_label': '[00:20:17]',
      'timestamp_seconds': 1217,
      'tip': 'Obtaining meaningful disk spacing distances the creation of wellness using the '
             'well targeting and decline curve tools can be quite powerful.',
      'title': 'Well Spacing in Enverus Subsurface Studio (ESS) [HOW TO] (Enverus)',
      'url': 'https://www.youtube.com/watch?v=hYa6oTD7seU&t=1217s',
      'video_id': 'hYa6oTD7seU'},
     {'author': 'Royalty Clerk',
      'channel': 'Royalty Clerk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=SAMqfyu0Ovo&t=77s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Say your lease gives a 1/5 royalty. You own 10 net mineral acres and the unit '
              'is 640 acres. That tiny number should match the decimal on your division order '
              'and on every check stub. If it ever changes, ask why. Older leases often carry '
              '1/8.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Say your lease gives a 1/5 royalty. You own 10 net mineral acres and the unit is '
             '640 acres. That tiny number should match the decimal on your division order and '
             'on every check stub. If it ever changes, ask why. Older leases often carry 1/8.',
      'title': 'How Oil & Gas Royalties Are Calculated: The Full Math, Barrel to Check '
               '(Royalty Clerk)',
      'url': 'https://www.youtube.com/watch?v=SAMqfyu0Ovo&t=77s',
      'video_id': 'SAMqfyu0Ovo'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:27](https://www.youtube.com/watch?v=XdquVDjbEAk&t=1167s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You would think, okay, well, you know, the US can stop drilling very quickly. '
              'Well, these companies have those capital budget cycles like Justin mentioned.',
      'timestamp': 1167,
      'timestamp_label': '[00:19:27]',
      'timestamp_seconds': 1167,
      'tip': 'You would think, okay, well, you know, the US can stop drilling very quickly. '
             'Well, these companies have those capital budget cycles like Justin mentioned.',
      'title': 'MRP 312:  Mineral Rights News December 2025 (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=XdquVDjbEAk&t=1167s',
      'video_id': 'XdquVDjbEAk'},
     {'author': 'Tracy Lenz',
      'channel': 'Tracy Lenz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:24](https://www.youtube.com/watch?v=NYvxAlVlAmQ&t=1764s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um the basis still goes down, but it never um runs out. So unfortunately, for '
              "those of y'all who are doing retrospective appraisals in order to figure out "
              'what your cost basis was, so you know how much to you have to pay on capital '
              "gains tax if you've made a sale.",
      'timestamp': 1764,
      'timestamp_label': '[00:29:24]',
      'timestamp_seconds': 1764,
      'tip': 'Um the basis still goes down, but it never um runs out. So unfortunately, for '
             "those of y'all who are doing retrospective appraisals in order to figure out "
             'what your cost basis was, so you know how much to you have to pay on capital '
             "gains tax if you've made a sale.",
      'title': 'Percentage Depletion for Mineral Owners: The 15% Deduction You Should Know (+ '
               'Live Q&A!) (Tracy Lenz)',
      'url': 'https://www.youtube.com/watch?v=NYvxAlVlAmQ&t=1764s',
      'video_id': 'NYvxAlVlAmQ'},
     {'author': 'Minerals & Royalties Authority LLC',
      'channel': 'Minerals & Royalties Authority LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=9p4KYSjq9r0&t=41s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Franco-Nevada and Alliance and Cresset. But then add into that layer all of '
              'these groups doing CVs, doing longer-terms insurance companies, which is kind '
              'of an offshoot of what Apollo is doing, Six Street is longer big capital to buy '
              'these things.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'Franco-Nevada and Alliance and Cresset. But then add into that layer all of '
             'these groups doing CVs, doing longer-terms insurance companies, which is kind of '
             'an offshoot of what Apollo is doing, Six Street is longer big capital to buy '
             'these things.',
      'title': 'Why More Mineral Assets May Never Get Sold (Minerals & Royalties Authority '
               'LLC)',
      'url': 'https://www.youtube.com/watch?v=9p4KYSjq9r0&t=41s',
      'video_id': '9p4KYSjq9r0'},
     {'author': 'CourthouseAcademy',
      'channel': 'CourthouseAcademy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:33](https://www.youtube.com/watch?v=822U1_i8V5Q&t=2073s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I had an IT gentlemen welcome off us a few months ago and he said Paul I want '
              'you to I want you to run a lot one in Harris County and I said well okay.',
      'timestamp': 2073,
      'timestamp_label': '[00:34:33]',
      'timestamp_seconds': 2073,
      'tip': 'I had an IT gentlemen welcome off us a few months ago and he said Paul I want '
             'you to I want you to run a lot one in Harris County and I said well okay.',
      'title': 'Landman Tools for Today (CourthouseAcademy)',
      'url': 'https://www.youtube.com/watch?v=822U1_i8V5Q&t=2073s',
      'video_id': '822U1_i8V5Q'},
     {'author': 'Untold Shifts',
      'channel': 'Untold Shifts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=mhaDQdLWgw0&t=53s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The courthouse. You're 23. You're sitting in a county courthouse basement at 8 "
              'in the morning and your entire job is reading.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "The courthouse. You're 23. You're sitting in a county courthouse basement at 8 "
             'in the morning and your entire job is reading.',
      'title': 'Your Life as Every Level of a Landman (Untold Shifts)',
      'url': 'https://www.youtube.com/watch?v=mhaDQdLWgw0&t=53s',
      'video_id': 'mhaDQdLWgw0'},
     {'author': 'UHD Continuing and Professional Education',
      'channel': 'UHD Continuing and Professional Education',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=QKj_eILAG2k&t=247s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Acres look at the name of that track Northeast quarter it tells us how to do '
              'the math we simply take the gross Acres 640 and look at the name again we '
              'divide.',
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': 'Acres look at the name of that track Northeast quarter it tells us how to do the '
             'math we simply take the gross Acres 640 and look at the name again we divide.',
      'title': 'Calculating Royalty Interests (UHD Continuing and Professional Education)',
      'url': 'https://www.youtube.com/watch?v=QKj_eILAG2k&t=247s',
      'video_id': 'QKj_eILAG2k'},
     {'author': 'TopDogEngineer',
      'channel': 'TopDogEngineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:46](https://www.youtube.com/watch?v=4mzbNb16NQc&t=586s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our oil rate so that this function on the left-hand side equals zero and it '
              'updated re you our of our gas and our reserves and all of that the rate time '
              "forecast so I hope you enjoyed the video and I'll see you next time adios.",
      'timestamp': 586,
      'timestamp_label': '[00:09:46]',
      'timestamp_seconds': 586,
      'tip': 'Our oil rate so that this function on the left-hand side equals zero and it '
             'updated re you our of our gas and our reserves and all of that the rate time '
             "forecast so I hope you enjoyed the video and I'll see you next time adios.",
      'title': 'Decline Curve Analysis: Economic Rate Oil + Gas (TopDogEngineer)',
      'url': 'https://www.youtube.com/watch?v=4mzbNb16NQc&t=586s',
      'video_id': '4mzbNb16NQc'},
     {'author': 'Susan Jessup',
      'channel': 'Susan Jessup',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:41](https://www.youtube.com/watch?v=sldaaowniGM&t=2201s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Types of cases out there but they're few and they're far between generally the "
              'APO land man is honest trustworthy man or woman that strives to live by the '
              'code of ethics to which each one of us are bound.',
      'timestamp': 2201,
      'timestamp_label': '[00:36:41]',
      'timestamp_seconds': 2201,
      'tip': "Types of cases out there but they're few and they're far between generally the "
             'APO land man is honest trustworthy man or woman that strives to live by the code '
             'of ethics to which each one of us are bound.',
      'title': "Ethics in Negotiations & Title Curative, A Landman's Perspective (Susan "
               'Jessup)',
      'url': 'https://www.youtube.com/watch?v=sldaaowniGM&t=2201s',
      'video_id': 'sldaaowniGM'},
     {'author': 'Sebastian Cosme',
      'channel': 'Sebastian Cosme',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=-fWjBQtg9r4&t=124s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Occur but pretty much in a nutshell this is the do hi Rule and make sure that '
              "when you run title in the courthouse you're paying attention to what you're "
              "running title on um this industry everything's important so that's it see you "
              'later.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'Occur but pretty much in a nutshell this is the do hi Rule and make sure that '
             "when you run title in the courthouse you're paying attention to what you're "
             "running title on um this industry everything's important so that's it see you "
             'later.',
      'title': 'Landman Class / Basic Title (Sebastian Cosme)',
      'url': 'https://www.youtube.com/watch?v=-fWjBQtg9r4&t=124s',
      'video_id': '-fWjBQtg9r4'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:19](https://www.youtube.com/watch?v=b97Q2qy5uEo&t=439s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Known as a hubendum clause is typically located in the third full paragraph the '
              'lease following the property description and in most cases it goes something '
              'like.',
      'timestamp': 439,
      'timestamp_label': '[00:07:19]',
      'timestamp_seconds': 439,
      'tip': 'Known as a hubendum clause is typically located in the third full paragraph the '
             'lease following the property description and in most cases it goes something '
             'like.',
      'title': 'Mineral Rights Management 101: EP 3 | 4 Questions About Your Oil & Gas Lease '
               '(Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=b97Q2qy5uEo&t=439s',
      'video_id': 'b97Q2qy5uEo'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=JVbDAxk_YTU&t=20s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Alpha owns a 100% minerals I'm going to underline 100% minerals and conveys to "
              'Bravo now this is in quotes this is in the actual conveyance instrument 2.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Alpha owns a 100% minerals I'm going to underline 100% minerals and conveys to "
             'Bravo now this is in quotes this is in the actual conveyance instrument 2.',
      'title': 'Situation #4 WI & NRI Calculations p  70 AAPL Study Guide (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=JVbDAxk_YTU&t=20s',
      'video_id': 'JVbDAxk_YTU'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:51](https://www.youtube.com/watch?v=ptrz57qzl54&t=2991s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2D seismic and then try to decide if you got a drilling drillable location or '
              'you need to come back and shoot 3D and then come back with what we call as a '
              'standard language of a 3D seismic option.',
      'timestamp': 2991,
      'timestamp_label': '[00:49:51]',
      'timestamp_seconds': 2991,
      'tip': '2D seismic and then try to decide if you got a drilling drillable location or '
             'you need to come back and shoot 3D and then come back with what we call as a '
             'standard language of a 3D seismic option.',
      'title': 'MRP 357: Helium Shortage and the Opportunity for Mineral Owners with CEO, Tim '
               'Rynott (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=ptrz57qzl54&t=2991s',
      'video_id': 'ptrz57qzl54'}],
 5: [{'author': 'Mr. Business',
      'channel': 'Mr. Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:59](https://www.youtube.com/watch?v=8gaFGCKNpnk&t=1079s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Regulatory and political risk. Changes in drilling regulations, permitting, '
              'taxes, or environmental policy can affect development. Tax law, including the '
              'depletion rules we discussed, can also change.',
      'timestamp': 1079,
      'timestamp_label': '[00:17:59]',
      'timestamp_seconds': 1079,
      'tip': 'Regulatory and political risk. Changes in drilling regulations, permitting, '
             'taxes, or environmental policy can affect development. Tax law, including the '
             'depletion rules we discussed, can also change.',
      'title': 'How Oil Well Royalties Work: Income, Decline Curves, Taxes & Risks (Mr. '
               'Business)',
      'url': 'https://www.youtube.com/watch?v=8gaFGCKNpnk&t=1079s',
      'video_id': '8gaFGCKNpnk'},
     {'author': 'Mineral View',
      'channel': 'Mineral View',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=KYu7M4t5LAk&t=157s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A decimal discrepancy of that size, whether from a data entry mistake, a title '
              'issue, or a unit boundary question, is worth catching before you sign. Here is '
              'the formula every mineral owner should know. This is the base calculation.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'A decimal discrepancy of that size, whether from a data entry mistake, a title '
             'issue, or a unit boundary question, is worth catching before you sign. Here is '
             'the formula every mineral owner should know. This is the base calculation.',
      'title': "Don't Sign Your Division Order Until You Check This Number (Mineral View)",
      'url': 'https://www.youtube.com/watch?v=KYu7M4t5LAk&t=157s',
      'video_id': 'KYu7M4t5LAk'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:52](https://www.youtube.com/watch?v=W5PjbHVyvWU&t=1072s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Negotiations fail to give eomi control over this whole 160 acres they could '
              'also go and seek forced.',
      'timestamp': 1072,
      'timestamp_label': '[00:17:52]',
      'timestamp_seconds': 1072,
      'tip': 'Negotiations fail to give eomi control over this whole 160 acres they could also '
             'go and seek forced.',
      'title': 'Oil & Gas 06: Intro to Pooling (Energy Law Professor)',
      'url': 'https://www.youtube.com/watch?v=W5PjbHVyvWU&t=1072s',
      'video_id': 'W5PjbHVyvWU'},
     {'author': 'Carbon Strata Solutions',
      'channel': 'Carbon Strata Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=a-Ltd9yb7JI&t=105s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would several branches create value exceeding additional complexity? Even if a '
              'horizontal well improves potential contact, it may be harder to drill, clean, '
              'case, or complete. Good engineering compares the benefit with the cost and '
              'risk.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'Would several branches create value exceeding additional complexity? Even if a '
             'horizontal well improves potential contact, it may be harder to drill, clean, '
             'case, or complete. Good engineering compares the benefit with the cost and risk.',
      'title': 'Vertical vs Horizontal Drilling | Directional & Multilateral Wells Explained | '
               'Lesson 7 (Carbon Strata Solutions)',
      'url': 'https://www.youtube.com/watch?v=a-Ltd9yb7JI&t=105s',
      'video_id': 'a-Ltd9yb7JI'},
     {'author': 'NARO',
      'channel': 'NARO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=W3POOsq6ka0&t=165s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Numbers you can figure out your your royalty interest if I get a division order '
              "and it doesn't have that number that I've calculated I'm going to call that "
              "division order uh department and I'm going to say you guys have made a mistake "
              "or convince me that I'm wrong okay.",
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'Numbers you can figure out your your royalty interest if I get a division order '
             "and it doesn't have that number that I've calculated I'm going to call that "
             "division order uh department and I'm going to say you guys have made a mistake "
             "or convince me that I'm wrong okay.",
      'title': 'Mineral Ownership 101| Part 5 Division Orders (NARO)',
      'url': 'https://www.youtube.com/watch?v=W3POOsq6ka0&t=165s',
      'video_id': 'W3POOsq6ka0'},
     {'author': 'Infinity Investments Real Estate - Steve Peterson',
      'channel': 'Infinity Investments Real Estate - Steve Peterson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=Ij8eFGyDOC4&t=149s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Them drilling for like a bit of work well actually that's I'm glad you asked "
              "that question in that way because we don't share in the risk yes we you know.",
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': "Them drilling for like a bit of work well actually that's I'm glad you asked "
             "that question in that way because we don't share in the risk yes we you know.",
      'title': 'What You Need To Know About Investing In Mineral Rights (Oil, Gas, Coal, and '
               'more) (Infinity Investments Real Estate - Steve Peterson)',
      'url': 'https://www.youtube.com/watch?v=Ij8eFGyDOC4&t=149s',
      'video_id': 'Ij8eFGyDOC4'},
     {'author': 'GeoScope',
      'channel': 'GeoScope',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=oSSTf7vpnpU&t=121s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Black shale gives gas shows. But the flare burns a few hours and dies, and you '
              'keep drilling. It was so reliably unproductive, it became a landmark. You knew '
              'where you were the moment you hit it. It also had a category, and the category '
              'was the problem.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Black shale gives gas shows. But the flare burns a few hours and dies, and you '
             'keep drilling. It was so reliably unproductive, it became a landmark. You knew '
             'where you were the moment you hit it. It also had a category, and the category '
             'was the problem.',
      'title': 'The Largest Single Natural Gas Deposit Ever Discovered in America (GeoScope)',
      'url': 'https://www.youtube.com/watch?v=oSSTf7vpnpU&t=121s',
      'video_id': 'oSSTf7vpnpU'},
     {'author': 'Cashflow Ninja',
      'channel': 'Cashflow Ninja',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=uhffuS4DlLQ&t=212s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Some of the additional risks of having to go out and drill the well and some of '
              "those other things so it's it's actually uh transferred by deed so uh there "
              'are.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': 'Some of the additional risks of having to go out and drill the well and some of '
             "those other things so it's it's actually uh transferred by deed so uh there are.",
      'title': 'Matt Sands Shares How To Invest In Mineral Rights & Royalties (Cashflow Ninja)',
      'url': 'https://www.youtube.com/watch?v=uhffuS4DlLQ&t=212s',
      'video_id': 'uhffuS4DlLQ'},
     {'author': 'KXAN',
      'channel': 'KXAN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=AyWdpWCeHUE&t=20s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'TALKING ABOUT TEXAS MISSION AND A HALF HOUR CONVERSATION. DEMOCRATIC RAILROAD '
              'COMMISSION CANDIDATE JON ROSENTHAL SPOKE TO JOURNALIST JEFF CRILLEY ABOUT HIS '
              'CAMPAIGN. THIS WAS SUPPOSED TO BE A DEBATE.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'TALKING ABOUT TEXAS MISSION AND A HALF HOUR CONVERSATION. DEMOCRATIC RAILROAD '
             'COMMISSION CANDIDATE JON ROSENTHAL SPOKE TO JOURNALIST JEFF CRILLEY ABOUT HIS '
             'CAMPAIGN. THIS WAS SUPPOSED TO BE A DEBATE.',
      'title': 'Anticipated debate between Texas Railroad Commission candidates turns into '
               'one-sided conversation (KXAN)',
      'url': 'https://www.youtube.com/watch?v=AyWdpWCeHUE&t=20s',
      'video_id': 'AyWdpWCeHUE'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:28](https://www.youtube.com/watch?v=z9gHz7FYvRk&t=868s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Recovery oil of oil and gas to be able to calculate that cost depletion but '
              'your CPA can tell you if if this is actually going to be potentially worth.',
      'timestamp': 868,
      'timestamp_label': '[00:14:28]',
      'timestamp_seconds': 868,
      'tip': 'Recovery oil of oil and gas to be able to calculate that cost depletion but your '
             'CPA can tell you if if this is actually going to be potentially worth.',
      'title': 'MRP 234:  Mineral Rights and Royalties Tax Strategies (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=z9gHz7FYvRk&t=868s',
      'video_id': 'z9gHz7FYvRk'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:13](https://www.youtube.com/watch?v=pjP04Ns4pww&t=193s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Equal the net revenue interest all you have to remember is that we have to '
              "reduce that royalty by their actual percentage of Interest okay so now let's "
              'look at the problem.',
      'timestamp': 193,
      'timestamp_label': '[00:03:13]',
      'timestamp_seconds': 193,
      'tip': 'Equal the net revenue interest all you have to remember is that we have to '
             "reduce that royalty by their actual percentage of Interest okay so now let's "
             'look at the problem.',
      'title': 'V NRI Joint Ownership Undivided Interests   Same RI Problem 1 (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=pjP04Ns4pww&t=193s',
      'video_id': 'pjP04Ns4pww'},
     {'author': 'Range Resources Corporation',
      'channel': 'Range Resources Corporation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:05](https://www.youtube.com/watch?v=8M30VzyjEpk&t=2945s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All means go to Ranger resources.com another excellent website is the marcelis '
              'coalition.org on behalf of everyone at range resources thank you so very much '
              'for the opportunity to show you what it is that we do here in Pennsylvania.',
      'timestamp': 2945,
      'timestamp_label': '[00:49:05]',
      'timestamp_seconds': 2945,
      'tip': 'All means go to Ranger resources.com another excellent website is the marcelis '
             'coalition.org on behalf of everyone at range resources thank you so very much '
             'for the opportunity to show you what it is that we do here in Pennsylvania.',
      'title': 'Range Resources Marcellus Shale Field Tour (Range Resources Corporation)',
      'url': 'https://www.youtube.com/watch?v=8M30VzyjEpk&t=2945s',
      'video_id': '8M30VzyjEpk'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:36](https://www.youtube.com/watch?v=WBGDgooXnq8&t=1896s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Otherwise force majeure uh is here at paragraph 11 and we'll see there can be "
              'lots of debate and litigation about whether the oil and gas company really '
              'should have been able to anticipate this problem are rising.',
      'timestamp': 1896,
      'timestamp_label': '[00:31:36]',
      'timestamp_seconds': 1896,
      'tip': "Otherwise force majeure uh is here at paragraph 11 and we'll see there can be "
             'lots of debate and litigation about whether the oil and gas company really '
             'should have been able to anticipate this problem are rising.',
      'title': 'Oil & Gas 09A: Intro to the Oil & Gas Lease (Energy Law Professor)',
      'url': 'https://www.youtube.com/watch?v=WBGDgooXnq8&t=1896s',
      'video_id': 'WBGDgooXnq8'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:21](https://www.youtube.com/watch?v=Z_HlEDh8-rw&t=561s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Questions for us you can reach us on the website minerals guide.com you can '
              "also reach me by email stepen minerals guide.com thanks and we'll see you the "
              'next next episode.',
      'timestamp': 561,
      'timestamp_label': '[00:09:21]',
      'timestamp_seconds': 561,
      'tip': 'Questions for us you can reach us on the website minerals guide.com you can also '
             "reach me by email stepen minerals guide.com thanks and we'll see you the next "
             'next episode.',
      'title': 'Minerals Management Series: Everything You Need To Know About Division Orders '
               '(Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=Z_HlEDh8-rw&t=561s',
      'video_id': 'Z_HlEDh8-rw'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=cO3OBCezwjw&t=197s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That they don't revert back to the surface right ownership and then how to "
              'manage multiple errors how to avoid disputes between your airs how to convey.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': "That they don't revert back to the surface right ownership and then how to "
             'manage multiple errors how to avoid disputes between your airs how to convey.',
      'title': 'MRP 203:  How to Navigate Inheritance Issues with Minerals and Royalties (Matt '
               'Sands)',
      'url': 'https://www.youtube.com/watch?v=cO3OBCezwjw&t=197s',
      'video_id': 'cO3OBCezwjw'}],
 6: [{'author': 'Royalty Clerk',
      'channel': 'Royalty Clerk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=blbomhUd0sA&t=187s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A decimal that changes with no letter from the operator is worth a question. '
              'Here is how to check yours. Find your division order and your lease. The lease '
              'gives the royalty fraction. Find your net mineral acres in your deed or a title '
              'opinion.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': 'A decimal that changes with no letter from the operator is worth a question. '
             'Here is how to check yours. Find your division order and your lease. The lease '
             'gives the royalty fraction. Find your net mineral acres in your deed or a title '
             'opinion.',
      'title': 'What Your Decimal Interest Means (and How to Check It) (Royalty Clerk)',
      'url': 'https://www.youtube.com/watch?v=blbomhUd0sA&t=187s',
      'video_id': 'blbomhUd0sA'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:21](https://www.youtube.com/watch?v=GS_N0TTrBPY&t=861s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To find it the other way would be to search by the API number which is the '
              "these numbers here again same with Texas where you don't need to enter the "
              'first.',
      'timestamp': 861,
      'timestamp_label': '[00:14:21]',
      'timestamp_seconds': 861,
      'tip': 'To find it the other way would be to search by the API number which is the these '
             "numbers here again same with Texas where you don't need to enter the first.",
      'title': 'How to Use the Oklahoma Corporation Commission Website to Find Your Mineral '
               'Rights (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=GS_N0TTrBPY&t=861s',
      'video_id': 'GS_N0TTrBPY'},
     {'author': 'AFX Videos',
      'channel': 'AFX Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=JpHijIsWFL4&t=110s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You may not know that these mineral rights were split off a title search is '
              'only gonna show this part of the transaction this mineral rights ownership is '
              'gonna run on a separate chain of title in order to find that you have to catch '
              'it when it separates from that main.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'You may not know that these mineral rights were split off a title search is only '
             'gonna show this part of the transaction this mineral rights ownership is gonna '
             'run on a separate chain of title in order to find that you have to catch it when '
             'it separates from that main.',
      'title': 'Important information about mineral rights and title searches | AFX (AFX '
               'Videos)',
      'url': 'https://www.youtube.com/watch?v=JpHijIsWFL4&t=110s',
      'video_id': 'JpHijIsWFL4'},
     {'author': 'Protect Wealth Academy',
      'channel': 'Protect Wealth Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:37](https://www.youtube.com/watch?v=J21M9DVmwY8&t=817s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh the first one is cost, and this is what the real big guys have to use. You '
              "know, it's it's it's fine as far as the the cost depletion goes, but it will "
              'eventually stop. So, once the investment is recovered, then the cost depletion '
              'stops.',
      'timestamp': 817,
      'timestamp_label': '[00:13:37]',
      'timestamp_seconds': 817,
      'tip': 'Uh the first one is cost, and this is what the real big guys have to use. You '
             "know, it's it's it's fine as far as the the cost depletion goes, but it will "
             'eventually stop. So, once the investment is recovered, then the cost depletion '
             'stops.',
      'title': 'Tax Advantages of Investing in Oil, Gas & Mineral Rights (Protect Wealth '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=J21M9DVmwY8&t=817s',
      'video_id': 'J21M9DVmwY8'},
     {'author': 'Modern Land Investor',
      'channel': 'Modern Land Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:57](https://www.youtube.com/watch?v=1c2UBDuXhrk&t=717s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s maybe not really worth anything. That that kind of leads me to to two big "
              'questions, right? I which are direct directly transferable in just traditional '
              'real estate where you have due diligence and then you have title, right?',
      'timestamp': 717,
      'timestamp_label': '[00:11:57]',
      'timestamp_seconds': 717,
      'tip': "'s maybe not really worth anything. That that kind of leads me to to two big "
             'questions, right? I which are direct directly transferable in just traditional '
             'real estate where you have due diligence and then you have title, right?',
      'title': 'Exploring Mineral Rights with Matt Sands: A Guide for Land Investors (Modern '
               'Land Investor)',
      'url': 'https://www.youtube.com/watch?v=1c2UBDuXhrk&t=717s',
      'video_id': '1c2UBDuXhrk'},
     {'author': 'Mergers & Inquisitions / Breaking Into Wall Street',
      'channel': 'Mergers & Inquisitions / Breaking Into Wall Street',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:50](https://www.youtube.com/watch?v=2tJpxiIqFSM&t=1070s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'B factor and the initial production rate and the decline rate in the first year '
              "and all that. So they're not really giving us enough information to go through "
              'the full analysis that I just showed you. And this is a very common issue.',
      'timestamp': 1070,
      'timestamp_label': '[00:17:50]',
      'timestamp_seconds': 1070,
      'tip': 'B factor and the initial production rate and the decline rate in the first year '
             "and all that. So they're not really giving us enough information to go through "
             'the full analysis that I just showed you. And this is a very common issue.',
      'title': 'Type Curves in Oil & Gas Modeling: Modeling Master Key or Academic Curiosity? '
               '(Mergers & Inquisitions / Breaking Into Wall Street)',
      'url': 'https://www.youtube.com/watch?v=2tJpxiIqFSM&t=1070s',
      'video_id': '2tJpxiIqFSM'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=MsMdpB0pFnc&t=47s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you understand real estate and you already have the skills to build a list '
              'and do the marketing to negotiate the price and get the deal under contract and '
              'to dispo the deal and get paid, you would make a killer mineral rights broker.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'If you understand real estate and you already have the skills to build a list '
             'and do the marketing to negotiate the price and get the deal under contract and '
             'to dispo the deal and get paid, you would make a killer mineral rights broker.',
      'title': 'Flips Pay Once. Royalties Pay Forever. (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=MsMdpB0pFnc&t=47s',
      'video_id': 'MsMdpB0pFnc'},
     {'author': 'Tracy Lenz',
      'channel': 'Tracy Lenz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=37dcxhS1a6E&t=124s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So that's 10 net acres because 10% times 100 is 10. So that's net mineral "
              'acres. But as we learned from our first question, uh things could be leased at '
              'different rates. So if I have those 10 net acres leased at 25% royalty versus '
              '12 1.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': "So that's 10 net acres because 10% times 100 is 10. So that's net mineral acres. "
             'But as we learned from our first question, uh things could be leased at '
             'different rates. So if I have those 10 net acres leased at 25% royalty versus 12 '
             '1.',
      'title': 'Net Royalty Acres vs. Net Mineral Acres (Q&A clip) (Tracy Lenz)',
      'url': 'https://www.youtube.com/watch?v=37dcxhS1a6E&t=124s',
      'video_id': '37dcxhS1a6E'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:24](https://www.youtube.com/watch?v=1HDBzjGoDdc&t=564s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Size of that drilling spacing unit so the first step that we want to do is we '
              "want to look at these Wells and find out the well status and how much they've.",
      'timestamp': 564,
      'timestamp_label': '[00:09:24]',
      'timestamp_seconds': 564,
      'tip': 'Size of that drilling spacing unit so the first step that we want to do is we '
             "want to look at these Wells and find out the well status and how much they've.",
      'title': 'How to Find Oil & Gas Info for North Dakota (For Free!) (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=1HDBzjGoDdc&t=564s',
      'video_id': '1HDBzjGoDdc'},
     {'author': 'Daniel Lewis',
      'channel': 'Daniel Lewis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:28](https://www.youtube.com/watch?v=qZGXdB7E1lE&t=148s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Throughout Oklahoma our goal is to help you get the best deal possible for '
              'whatever amount you wish to sell call us now at four oh five four two one zero '
              'six eight zero or fill out the form on our website to get a quote and your '
              'questions answered today.',
      'timestamp': 148,
      'timestamp_label': '[00:02:28]',
      'timestamp_seconds': 148,
      'tip': 'Throughout Oklahoma our goal is to help you get the best deal possible for '
             'whatever amount you wish to sell call us now at four oh five four two one zero '
             'six eight zero or fill out the form on our website to get a quote and your '
             'questions answered today.',
      'title': 'Sell Mineral Rights Oklahoma Oil and Gas Leases Royalty Income from Mineral '
               'Rights (Daniel Lewis)',
      'url': 'https://www.youtube.com/watch?v=qZGXdB7E1lE&t=148s',
      'video_id': 'qZGXdB7E1lE'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:42](https://www.youtube.com/watch?v=lCpJ3rpcfvY&t=1422s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Shell revolution when the Udica was first discovered and he was like this is '
              'the this is the the the center of the core of the core of the Udica is right '
              'over Harrison County Belmont County as well.',
      'timestamp': 1422,
      'timestamp_label': '[00:23:42]',
      'timestamp_seconds': 1422,
      'tip': 'Shell revolution when the Udica was first discovered and he was like this is the '
             'this is the the the center of the core of the core of the Udica is right over '
             'Harrison County Belmont County as well.',
      'title': 'What Does A Landman Actually Do? | Behind The Scenes Of A Real Deal (Steven '
               'Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=lCpJ3rpcfvY&t=1422s',
      'video_id': 'lCpJ3rpcfvY'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:01](https://www.youtube.com/watch?v=6w9YvetItDc&t=61s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fraction in the oil and gas lease so what we're going to do is we're going to "
              'say okay land owner royalty owner if you have if the oil and gas company has '
              "$1,000 worth of profits what we're going to do is we're going to take that "
              'decimal that times.',
      'timestamp': 61,
      'timestamp_label': '[00:01:01]',
      'timestamp_seconds': 61,
      'tip': "Fraction in the oil and gas lease so what we're going to do is we're going to "
             'say okay land owner royalty owner if you have if the oil and gas company has '
             "$1,000 worth of profits what we're going to do is we're going to take that "
             'decimal that times.',
      'title': 'Calculating The Money Decimal in an Oil & Gas Lease www.landtraining.net (Land '
               'Training www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=6w9YvetItDc&t=61s',
      'video_id': '6w9YvetItDc'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=e1rml2NIbco&t=159s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A course to show you everything that you need to know to become a successful '
              'landman in Mineral buyer and if you want to be the first to access this course '
              "shoot me an email at stepen minerals guide.com and I'll add you to the weight "
              'list.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'A course to show you everything that you need to know to become a successful '
             'landman in Mineral buyer and if you want to be the first to access this course '
             "shoot me an email at stepen minerals guide.com and I'll add you to the weight "
             'list.',
      'title': 'Want a High-Paying Career in Oil & Gas? Become a Landman – Here’s How (Steven '
               'Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=e1rml2NIbco&t=159s',
      'video_id': 'e1rml2NIbco'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:23](https://www.youtube.com/watch?v=Yy7az5T7_vs&t=383s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that yields 16 net acres so the number 16 is the first number that we'll "
              'need in calculating that nri.',
      'timestamp': 383,
      'timestamp_label': '[00:06:23]',
      'timestamp_seconds': 383,
      'tip': "And that yields 16 net acres so the number 16 is the first number that we'll "
             'need in calculating that nri.',
      'title': 'MRP 3: How to Calculate your Net Revenue Interest in 3 Simple Steps (Matt '
               'Sands)',
      'url': 'https://www.youtube.com/watch?v=Yy7az5T7_vs&t=383s',
      'video_id': 'Yy7az5T7_vs'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:06](https://www.youtube.com/watch?v=pjmqehPUgL8&t=606s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because they had recognized recognized the overriding royalty but doing the '
              'research the first thing we had to do was dive in.',
      'timestamp': 606,
      'timestamp_label': '[00:10:06]',
      'timestamp_seconds': 606,
      'tip': 'Because they had recognized recognized the overriding royalty but doing the '
             'research the first thing we had to do was dive in.',
      'title': 'MRP 43: Overriding Royalty Interests (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=pjmqehPUgL8&t=606s',
      'video_id': 'pjmqehPUgL8'}],
 7: [{'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:17](https://www.youtube.com/watch?v=VYytHJ0lMVw&t=1337s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a hyperbolic and then the second part where it's an exponential and that's "
              'the process that is used for um performing a decline curve analysis on most '
              'wells today and Matt not to leave out natural gas or um other plant products.',
      'timestamp': 1337,
      'timestamp_label': '[00:22:17]',
      'timestamp_seconds': 1337,
      'tip': "'s a hyperbolic and then the second part where it's an exponential and that's "
             'the process that is used for um performing a decline curve analysis on most '
             'wells today and Matt not to leave out natural gas or um other plant products.',
      'title': "MRP 293:  Why Your Royalty Checks Keep Dropping (And How to Predict What's "
               'Next) (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=VYytHJ0lMVw&t=1337s',
      'video_id': 'VYytHJ0lMVw'},
     {'author': 'The Crude Files',
      'channel': 'The Crude Files',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:39](https://www.youtube.com/watch?v=R-AasPj-Y5E&t=279s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That steel and cement sleeve is what separates the oil well from the freshwater '
              "aquifers above. It's one of the most important and most regulated steps in the "
              'entire process. Step two, the blowout preventer. On top of the wellhead goes a '
              'massive stack of valves, the BOP.',
      'timestamp': 279,
      'timestamp_label': '[00:04:39]',
      'timestamp_seconds': 279,
      'tip': 'That steel and cement sleeve is what separates the oil well from the freshwater '
             "aquifers above. It's one of the most important and most regulated steps in the "
             'entire process. Step two, the blowout preventer. On top of the wellhead goes a '
             'massive stack of valves, the BOP.',
      'title': 'THE COST OF DRILLING AN OIL WELL | 8 Million and NO GUARANTEES (The Crude '
               'Files)',
      'url': 'https://www.youtube.com/watch?v=R-AasPj-Y5E&t=279s',
      'video_id': 'R-AasPj-Y5E'},
     {'author': 'Royalty Clerk',
      'channel': 'Royalty Clerk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=DN-VIoSmyF0&t=218s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Settlements and payments. So, before you sign, five steps. One, read every '
              'clause against the list. Two, rebuild the decimal from your lease.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'Settlements and payments. So, before you sign, five steps. One, read every '
             'clause against the list. Two, rebuild the decimal from your lease.',
      'title': 'Texas Division Orders: What You Can Sign and Refuse (Royalty Clerk)',
      'url': 'https://www.youtube.com/watch?v=DN-VIoSmyF0&t=218s',
      'video_id': 'DN-VIoSmyF0'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:51](https://www.youtube.com/watch?v=u4xA0UNrxQs&t=531s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And it's very similar to researching documents in the county records in terms "
              'of going back, you know, each step up that chain or up that family tree in this '
              'case, looking for those names. So you know the names of your grandparents.',
      'timestamp': 531,
      'timestamp_label': '[00:08:51]',
      'timestamp_seconds': 531,
      'tip': "And it's very similar to researching documents in the county records in terms of "
             'going back, you know, each step up that chain or up that family tree in this '
             'case, looking for those names. So you know the names of your grandparents.',
      'title': 'MRP 288:  Our Favorite Tools for Managing Your Minerals in 2025 (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=u4xA0UNrxQs&t=531s',
      'video_id': 'u4xA0UNrxQs'},
     {'author': 'Drilling Contractor Magazine',
      'channel': 'Drilling Contractor Magazine',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=40uE_5Fvn_A&t=146s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Planning phase but also needs to be translated during the execution after well '
              'as well so I would say plan plan plan great well Denise thanks for speaking '
              "with us again you're welcome and thank you viewers for joining us today at "
              'drilling contractor.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'Planning phase but also needs to be translated during the execution after well '
             'as well so I would say plan plan plan great well Denise thanks for speaking with '
             "us again you're welcome and thank you viewers for joining us today at drilling "
             'contractor.',
      'title': 'Horizontal drilling optimization, high build rates lead to record wells in '
               'Marcellus Shale (Drilling Contractor Magazine)',
      'url': 'https://www.youtube.com/watch?v=40uE_5Fvn_A&t=146s',
      'video_id': '40uE_5Fvn_A'},
     {'author': 'FutureWise Energy',
      'channel': 'FutureWise Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=nbj7-lPJ59w&t=147s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Point Pleasant Formation sitting just under the Utica proper. It has more '
              'carbonate, less clay, and better rock quality for horizontal drilling and '
              'fracking.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'Point Pleasant Formation sitting just under the Utica proper. It has more '
             'carbonate, less clay, and better rock quality for horizontal drilling and '
             'fracking.',
      'title': 'Utica Shale Explained: The $114B Oil Play Under Ohio (And Your Power Bill) '
               '(FutureWise Energy)',
      'url': 'https://www.youtube.com/watch?v=nbj7-lPJ59w&t=147s',
      'video_id': 'nbj7-lPJ59w'},
     {'author': 'Passive Income MD',
      'channel': 'Passive Income MD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:16](https://www.youtube.com/watch?v=41VgsNOdrto&t=676s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And who's going to be able to put together a system that allows individual "
              'investors to go drill wells that cost $10 million at a time?',
      'timestamp': 676,
      'timestamp_label': '[00:11:16]',
      'timestamp_seconds': 676,
      'tip': "And who's going to be able to put together a system that allows individual "
             'investors to go drill wells that cost $10 million at a time?',
      'title': 'Working Interests in Oil & Gas: Cash Flow and Tax Breaks for Physicians | PIMD '
               'Podcast (Passive Income MD)',
      'url': 'https://www.youtube.com/watch?v=41VgsNOdrto&t=676s',
      'video_id': '41VgsNOdrto'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:37](https://www.youtube.com/watch?v=7sPTlHr4F7A&t=697s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But with fracking, remember there's two steps. You got to drill that well, and "
              'then you have to fracture it. And why take that second step which releases a '
              "lot of oil and gas until you're actually ready to produce that gas on the "
              'market?',
      'timestamp': 697,
      'timestamp_label': '[00:11:37]',
      'timestamp_seconds': 697,
      'tip': "But with fracking, remember there's two steps. You got to drill that well, and "
             'then you have to fracture it. And why take that second step which releases a lot '
             "of oil and gas until you're actually ready to produce that gas on the market?",
      'title': 'Oil & Gas 12A: Constructive Production & Shut-In Royalties (Energy Law '
               'Professor)',
      'url': 'https://www.youtube.com/watch?v=7sPTlHr4F7A&t=697s',
      'video_id': '7sPTlHr4F7A'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=1hz9VkFL01Y&t=173s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Acquisition and it's the very same system that I've used to do 18 deals within "
              "the past 6 months and here's the very best best part you do not need a.",
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "Acquisition and it's the very same system that I've used to do 18 deals within "
             "the past 6 months and here's the very best best part you do not need a.",
      'title': 'So You Want to Be a Landman... How to Make the TV Show a Reality (Steven '
               'Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=1hz9VkFL01Y&t=173s',
      'video_id': '1hz9VkFL01Y'},
     {'author': "AAPL America's Landman",
      'channel': "AAPL America's Landman",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=AJGoTBiN9oQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Energy industry moving forward no two days ever look the same for a land man '
              'each Journey promises a new outcome and a step further into a multi-faceted '
              'career.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Energy industry moving forward no two days ever look the same for a land man '
             'each Journey promises a new outcome and a step further into a multi-faceted '
             'career.',
      'title': "The Path of the Landman — Powering the World (AAPL America's Landman)",
      'url': 'https://www.youtube.com/watch?v=AJGoTBiN9oQ&t=79s',
      'video_id': 'AJGoTBiN9oQ'},
     {'author': 'Enverus',
      'channel': 'Enverus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=2rbY0Lt22CU&t=170s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Development of undeveloped inventory noting how children Wells are '
              'significantly impacted compared to parent or coom completed wells in fact these '
              "typ curves can be grouped and Bin into any and all of the spacing metrics we've "
              'covered here in this video.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': 'Development of undeveloped inventory noting how children Wells are significantly '
             'impacted compared to parent or coom completed wells in fact these typ curves can '
             "be grouped and Bin into any and all of the spacing metrics we've covered here in "
             'this video.',
      'title': 'Enverus Spacing - A Holistic View on Well Spacing & Performance (Enverus)',
      'url': 'https://www.youtube.com/watch?v=2rbY0Lt22CU&t=170s',
      'video_id': '2rbY0Lt22CU'},
     {'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:19](https://www.youtube.com/watch?v=PNLVi6Ee0KM&t=559s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Only owns a 50% interest in that 1/8 and the reason is because most leases have '
              'a clause in there called the proportionate reduction Clause oops sorry '
              'reduction.',
      'timestamp': 559,
      'timestamp_label': '[00:09:19]',
      'timestamp_seconds': 559,
      'tip': 'Only owns a 50% interest in that 1/8 and the reason is because most leases have '
             'a clause in there called the proportionate reduction Clause oops sorry '
             'reduction.',
      'title': 'Calculating Undivided Interest - Different Royalties.avi (Land Training '
               'www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=PNLVi6Ee0KM&t=559s',
      'video_id': 'PNLVi6Ee0KM'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=yfXV7bIliEk&t=159s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then I had a um a free estate document storage checklist. So that lists '
              'your um basically your essential documents and then the way that you go about '
              "organizing those. And so we'll link to that in the show notes.",
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'And then I had a um a free estate document storage checklist. So that lists your '
             'um basically your essential documents and then the way that you go about '
             "organizing those. And so we'll link to that in the show notes.",
      'title': "MRP 314: Organize Your Mineral Legacy Before It's Too Late (Matt Sands)",
      'url': 'https://www.youtube.com/watch?v=yfXV7bIliEk&t=159s',
      'video_id': 'yfXV7bIliEk'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:07](https://www.youtube.com/watch?v=_MHogbd2xzU&t=1387s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And if you haven't done that so far and you you acquired it long ago, then it's "
              'always a good time to figure it out because again, each one of these can be '
              'different and some very confusing. So, step one is to identify every county '
              'where you own a mineral interest.',
      'timestamp': 1387,
      'timestamp_label': '[00:23:07]',
      'timestamp_seconds': 1387,
      'tip': "And if you haven't done that so far and you you acquired it long ago, then it's "
             'always a good time to figure it out because again, each one of these can be '
             'different and some very confusing. So, step one is to identify every county '
             'where you own a mineral interest.',
      'title': "MRP 342:  Property Taxes on Mineral Rights and What Happens If You Don't Pay "
               '(Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=_MHogbd2xzU&t=1387s',
      'video_id': '_MHogbd2xzU'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:10](https://www.youtube.com/watch?v=3AnqzZSRGtg&t=790s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Construed as investment legal or tax advice all information is believed to be '
              'from reliable sources however we make no representation as to its completeness '
              'or accuracy.',
      'timestamp': 790,
      'timestamp_label': '[00:13:10]',
      'timestamp_seconds': 790,
      'tip': 'Construed as investment legal or tax advice all information is believed to be '
             'from reliable sources however we make no representation as to its completeness '
             'or accuracy.',
      'title': 'MRP 2: What’s the Difference Between Minerals and Royalties? (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=3AnqzZSRGtg&t=790s',
      'video_id': '3AnqzZSRGtg'}],
 8: [{'author': 'OCD Pecos Hall',
      'channel': 'OCD Pecos Hall',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:44](https://www.youtube.com/watch?v=Gyi9ijeMNgA&t=1304s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s clearly on a different decline trajectory than uh the lost mine uh is. Um "
              "now, we don't have the data to be able to do the full analysis on what the "
              'reserves would be of this um with with high-res data.',
      'timestamp': 1304,
      'timestamp_label': '[00:21:44]',
      'timestamp_seconds': 1304,
      'tip': "'s clearly on a different decline trajectory than uh the lost mine uh is. Um "
             "now, we don't have the data to be able to do the full analysis on what the "
             'reserves would be of this um with with high-res data.',
      'title': 'OCD Special Docket October 27, 2026, DAY 3 PART 2 (OCD Pecos Hall)',
      'url': 'https://www.youtube.com/watch?v=Gyi9ijeMNgA&t=1304s',
      'video_id': 'Gyi9ijeMNgA'},
     {'author': 'Duahbed Consult',
      'channel': 'Duahbed Consult',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=bZGu6nyMvTA&t=20s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Speaker: the depreciation, depletion, and amortization recognized, and the '
              'Speaker: following revenue were in dengue cost sixty thousand. Speaker: '
              'Acquisition cost one hundred thousand. Speaker: Exploratory dry hose one. '
              'Speaker: One million four hundred thousand.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Speaker: the depreciation, depletion, and amortization recognized, and the '
             'Speaker: following revenue were in dengue cost sixty thousand. Speaker: '
             'Acquisition cost one hundred thousand. Speaker: Exploratory dry hose one. '
             'Speaker: One million four hundred thousand.',
      'title': 'Oil and Gas Accounting 102: Practical Case Study | Income Statement & Balance '
               'Sheet (Duahbed Consult)',
      'url': 'https://www.youtube.com/watch?v=bZGu6nyMvTA&t=20s',
      'video_id': 'bZGu6nyMvTA'},
     {'author': 'RE: REAL ESTATE PODCAST',
      'channel': 'RE: REAL ESTATE PODCAST',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:13](https://www.youtube.com/watch?v=gsOnEm_adKI&t=1333s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, not every county is the best or or every parish is the best in Louisiana, '
              "but they're all working their way to to getting there. And there's some there's "
              'some third-party companies, uh like for example, Texas File or um Drilling '
              'Info.',
      'timestamp': 1333,
      'timestamp_label': '[00:22:13]',
      'timestamp_seconds': 1333,
      'tip': 'Now, not every county is the best or or every parish is the best in Louisiana, '
             "but they're all working their way to to getting there. And there's some there's "
             'some third-party companies, uh like for example, Texas File or um Drilling Info.',
      'title': 'Who Owns the Minerals Under Your Louisiana Land? A Landman Explains | RE: Real '
               'Estate Podcast (RE: REAL ESTATE PODCAST)',
      'url': 'https://www.youtube.com/watch?v=gsOnEm_adKI&t=1333s',
      'video_id': 'gsOnEm_adKI'},
     {'author': 'Alpha Seven Energy',
      'channel': 'Alpha Seven Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=gjm7ZmMazmc&t=284s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'See this is the outline of texas this is the individual sections if we go into '
              "this out of the way if we type in the api number so we're going to paste that "
              "and we're going to search.",
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'See this is the outline of texas this is the individual sections if we go into '
             "this out of the way if we type in the api number so we're going to paste that "
             "and we're going to search.",
      'title': 'Railroad Commission of Texas Permit Discussion (Alpha Seven Energy)',
      'url': 'https://www.youtube.com/watch?v=gjm7ZmMazmc&t=284s',
      'video_id': 'gjm7ZmMazmc'},
     {'author': 'Offshore Engineering Academy',
      'channel': 'Offshore Engineering Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=YPFuHij-FYk&t=72s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And what's really fascinating here is that we are defining a vital function "
              "based entirely on empty space. I mean, the annulus isn't a tool you can just "
              "pick up and hold in your hands. So, how does this actually work when we're "
              'drilling?',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "And what's really fascinating here is that we are defining a vital function "
             "based entirely on empty space. I mean, the annulus isn't a tool you can just "
             "pick up and hold in your hands. So, how does this actually work when we're "
             'drilling?',
      'title': 'What Is the Annulus? The Most Important Space in a Well | Drilling Ep 4 '
               '(Offshore Engineering Academy)',
      'url': 'https://www.youtube.com/watch?v=YPFuHij-FYk&t=72s',
      'video_id': 'YPFuHij-FYk'},
     {'author': 'Energy Window Insights',
      'channel': 'Energy Window Insights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=aY0LJMEZzZo&t=209s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'PMCD on its own because it works without returns. Some can be combined and the '
              'decision depends on the well data. The criterion by criterion comparison, the '
              'selection matrix and the decision tree are in guide 01, drilling and well '
              'intervention in depleted reservoirs.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'PMCD on its own because it works without returns. Some can be combined and the '
             'decision depends on the well data. The criterion by criterion comparison, the '
             'selection matrix and the decision tree are in guide 01, drilling and well '
             'intervention in depleted reservoirs.',
      'title': 'The 6 options to drill or intervene depleted wells | Conventional, MPD, UBD, '
               'UBCTD and PMCD (Energy Window Insights)',
      'url': 'https://www.youtube.com/watch?v=aY0LJMEZzZo&t=209s',
      'video_id': 'aY0LJMEZzZo'},
     {'author': 'Money Moves With K',
      'channel': 'Money Moves With K',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:28](https://www.youtube.com/watch?v=8JwnQSZGjU0&t=388s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Make sure that is in the search engine. And also, you could just put this into '
              "Google, oil and gas asset clearinghouse. It'll pull up the same information, "
              'okay? The last place to look for mineral rights is the county clerk or the '
              'county recorder.',
      'timestamp': 388,
      'timestamp_label': '[00:06:28]',
      'timestamp_seconds': 388,
      'tip': 'Make sure that is in the search engine. And also, you could just put this into '
             "Google, oil and gas asset clearinghouse. It'll pull up the same information, "
             'okay? The last place to look for mineral rights is the county clerk or the '
             'county recorder.',
      'title': '5 Secret Websites To Find Mineral Rights For Sale That No One Talks About! '
               '(Money Moves With K)',
      'url': 'https://www.youtube.com/watch?v=8JwnQSZGjU0&t=388s',
      'video_id': '8JwnQSZGjU0'},
     {'author': 'Tracy Lenz',
      'channel': 'Tracy Lenz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=yEKUUQ-zkaU&t=149s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're going to be looking at the Reaves County, Delaware side of things. So "
              "here's this whole basin. And on the right, you have the Midland Basin in the "
              'middle you have the Central Basin platform. And then on the left you have the '
              'Delaware Basin.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': "We're going to be looking at the Reaves County, Delaware side of things. So "
             "here's this whole basin. And on the right, you have the Midland Basin in the "
             'middle you have the Central Basin platform. And then on the left you have the '
             'Delaware Basin.',
      'title': 'WALKTHROUGH (pt 1): Permian Basin geology, legal descriptions, locating the '
               'minerals (Tracy Lenz)',
      'url': 'https://www.youtube.com/watch?v=yEKUUQ-zkaU&t=149s',
      'video_id': 'yEKUUQ-zkaU'},
     {'author': 'British Columbia Energy Regulator',
      'channel': 'British Columbia Energy Regulator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=qSA8EoDzhKo&t=156s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is taken out of the hole for tool and bit changes and put back in this process '
              'is called tripping pipe when the targeted distance is reached the drill pipe '
              'and bit are removed from the wellbore one last time.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'Is taken out of the hole for tool and bit changes and put back in this process '
             'is called tripping pipe when the targeted distance is reached the drill pipe and '
             'bit are removed from the wellbore one last time.',
      'title': 'Horizontal Drilling and Stimulation Process (British Columbia Energy '
               'Regulator)',
      'url': 'https://www.youtube.com/watch?v=qSA8EoDzhKo&t=156s',
      'video_id': 'qSA8EoDzhKo'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:40](https://www.youtube.com/watch?v=gFgW6n9nb-c&t=520s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And then it'll also zoom in on on that particular well for you if that's "
              'another way that you want to search for this if you know the API number of '
              'that.',
      'timestamp': 520,
      'timestamp_label': '[00:08:40]',
      'timestamp_seconds': 520,
      'tip': "And then it'll also zoom in on on that particular well for you if that's another "
             'way that you want to search for this if you know the API number of that.',
      'title': 'How To Use the Texas Railroad Commission Website to Find Your Mineral Rights '
               '(Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=gFgW6n9nb-c&t=520s',
      'video_id': 'gFgW6n9nb-c'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=USmNwOWurpk&t=15s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of most leases which is the granting clause which tells you what land it covers '
              'what minerals.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Of most leases which is the granting clause which tells you what land it covers '
             'what minerals.',
      'title': 'Oil & Gas 09B: The Granting Clause (Energy Law Professor)',
      'url': 'https://www.youtube.com/watch?v=USmNwOWurpk&t=15s',
      'video_id': 'USmNwOWurpk'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=Sz-1-E8zTqU&t=80s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "About minerals as an asset on your personal balance sheet and we've talked "
              "about this concept of opportunity cost let's dive into some reasons that I've.",
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "About minerals as an asset on your personal balance sheet and we've talked about "
             "this concept of opportunity cost let's dive into some reasons that I've.",
      'title': 'Thinking about Selling Mineral Rights? | Reasons to Sell Oil and Gas Mineral '
               'Rights and Royalties! (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=Sz-1-E8zTqU&t=80s',
      'video_id': 'Sz-1-E8zTqU'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:07](https://www.youtube.com/watch?v=yFLZSA3QGGI&t=787s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, uh you know, the fact that that you have this oil company and and it was '
              'across multiple counties and it looks like they have executed 17 search '
              'warrants across Reeves, Rockwall, Kaufman, and Hunt counties in Texas and then '
              'Garvin County, Oklahoma.',
      'timestamp': 787,
      'timestamp_label': '[00:13:07]',
      'timestamp_seconds': 787,
      'tip': 'But, uh you know, the fact that that you have this oil company and and it was '
             'across multiple counties and it looks like they have executed 17 search warrants '
             'across Reeves, Rockwall, Kaufman, and Hunt counties in Texas and then Garvin '
             'County, Oklahoma.',
      'title': 'MRP 356: Mineral Rights News November 2026 (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=yFLZSA3QGGI&t=787s',
      'video_id': 'yFLZSA3QGGI'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=WZxmCcTgeWk&t=269s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Working on a course that shares our secrets on how we buy mineral rights all '
              'across the country if you want to get on our weight list shoot me an email at '
              'Steven minerals guy.com.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': 'Working on a course that shares our secrets on how we buy mineral rights all '
             'across the country if you want to get on our weight list shoot me an email at '
             'Steven minerals guy.com.',
      'title': 'Oil and Gas Royalty Basics; How They Work (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=WZxmCcTgeWk&t=269s',
      'video_id': 'WZxmCcTgeWk'},
     {'author': 'Danomics',
      'channel': 'Danomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=gleafhkBQWg&t=116s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To the database you're looking for we then have our decline curve analysis "
              "block here we'll select our well headers so.",
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "To the database you're looking for we then have our decline curve analysis block "
             "here we'll select our well headers so.",
      'title': 'Decline Curve Analysis with Danomics Flows (Danomics)',
      'url': 'https://www.youtube.com/watch?v=gleafhkBQWg&t=116s',
      'video_id': 'gleafhkBQWg'}],
 9: [{'author': 'Land Training www.landtraining.net',
      'channel': 'Land Training www.landtraining.net',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=n2pg2-Q06P8&t=117s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Greg, Peter, and Bobby each own an undivided interest in this 160 acres. But '
              'now we want to drill a well. And the state conservation commission says, well, '
              'you can only drill one well. And they have different rules, but in this case, '
              "we'll say um it's a gas well.",
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Greg, Peter, and Bobby each own an undivided interest in this 160 acres. But now '
             'we want to drill a well. And the state conservation commission says, well, you '
             "can only drill one well. And they have different rules, but in this case, we'll "
             "say um it's a gas well.",
      'title': 'Unit:  Calculating Undivided Interests with Different Royalties in a Unit '
               '(Land Training www.landtraining.net)',
      'url': 'https://www.youtube.com/watch?v=n2pg2-Q06P8&t=117s',
      'video_id': 'n2pg2-Q06P8'},
     {'author': 'Sovereign Energy Partners',
      'channel': 'Sovereign Energy Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=J9jZGFyolV0&t=258s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, and this is the key distinction, they do not pay for drilling or operating '
              'costs. So, in practical terms, this means no upfront capital tied to drilling, '
              'no exposure to cost overruns, no ongoing operating expenses.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': 'But, and this is the key distinction, they do not pay for drilling or operating '
             'costs. So, in practical terms, this means no upfront capital tied to drilling, '
             'no exposure to cost overruns, no ongoing operating expenses.',
      'title': 'Working Interest vs Royalty Interest Explained | Risk, Cash Flow & Returns '
               'Compared (Sovereign Energy Partners)',
      'url': 'https://www.youtube.com/watch?v=J9jZGFyolV0&t=258s',
      'video_id': 'J9jZGFyolV0'},
     {'author': 'Tips from Mark Sokolow',
      'channel': 'Tips from Mark Sokolow',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:26](https://www.youtube.com/watch?v=XvpPKXAYhlQ&t=386s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '120 days after the termination of the lease and if the wells are abandoned we '
              'expect them to follow the rules of the railroad commission in the state of '
              'texas.',
      'timestamp': 386,
      'timestamp_label': '[00:06:26]',
      'timestamp_seconds': 386,
      'tip': '120 days after the termination of the lease and if the wells are abandoned we '
             'expect them to follow the rules of the railroad commission in the state of '
             'texas.',
      'title': 'Oil and Gas Leases by Mark Sokolow (Tips from Mark Sokolow)',
      'url': 'https://www.youtube.com/watch?v=XvpPKXAYhlQ&t=386s',
      'video_id': 'XvpPKXAYhlQ'},
     {'author': 'New Mexico Oil Conservation Commission',
      'channel': 'New Mexico Oil Conservation Commission',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:28:57](https://www.youtube.com/watch?v=gfqoliQ78bk&t=5337s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Will you please state your name and role in this proceeding for the commission? '
              'Yes, my name is Clayton Spor and I am the uh industry legal expert for NEMoga '
              'for this hearing in front of the commission.',
      'timestamp': 5337,
      'timestamp_label': '[01:28:57]',
      'timestamp_seconds': 5337,
      'tip': 'Will you please state your name and role in this proceeding for the commission? '
             'Yes, my name is Clayton Spor and I am the uh industry legal expert for NEMoga '
             'for this hearing in front of the commission.',
      'title': 'OCC Rulemaking Hearing Part 22   10 30 25 (New Mexico Oil Conservation '
               'Commission)',
      'url': 'https://www.youtube.com/watch?v=gfqoliQ78bk&t=5337s',
      'video_id': 'gfqoliQ78bk'},
     {'author': 'Royalty Clerk',
      'channel': 'Royalty Clerk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=q5XqULtWaUQ&t=172s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Recorded in the county's deed records, it becomes part of the chain of title. "
              'And once it has been on record for 5 years, Texas law treats it as prima facie '
              'evidence of the facts in it. Someone with personal knowledge of the family.',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': "Recorded in the county's deed records, it becomes part of the chain of title. "
             'And once it has been on record for 5 years, Texas law treats it as prima facie '
             'evidence of the facts in it. Someone with personal knowledge of the family.',
      'title': 'Inherited Mineral Rights in Texas: The Affidavit of Heirship, Step by Step '
               '(Royalty Clerk)',
      'url': 'https://www.youtube.com/watch?v=q5XqULtWaUQ&t=172s',
      'video_id': 'q5XqULtWaUQ'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:01](https://www.youtube.com/watch?v=iVFjOPF8JW0&t=841s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You know when we make purchase offers we prefer to state that in terms of '
              'dollars per net mineral acres.',
      'timestamp': 841,
      'timestamp_label': '[00:14:01]',
      'timestamp_seconds': 841,
      'tip': 'You know when we make purchase offers we prefer to state that in terms of '
             'dollars per net mineral acres.',
      'title': 'MRP 18: What is the Difference Between a Net Mineral Acre (NMA) and a Net '
               'Royalty Acre(NRA)? (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=iVFjOPF8JW0&t=841s',
      'video_id': 'iVFjOPF8JW0'},
     {'author': 'Commission Shift',
      'channel': 'Commission Shift',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=GXqMsH_dUSM&t=72s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Texans, but we think voters deserve the truth. Texans need the transparency to '
              'know who is controlling what first. The Railroad Commission of Texas must '
              'transform in order to meet our state and countries changing energy needs and '
              'that all starts with their name.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'Texans, but we think voters deserve the truth. Texans need the transparency to '
             'know who is controlling what first. The Railroad Commission of Texas must '
             'transform in order to meet our state and countries changing energy needs and '
             'that all starts with their name.',
      'title': 'What is the Railroad Commission? (Commission Shift)',
      'url': 'https://www.youtube.com/watch?v=GXqMsH_dUSM&t=72s',
      'video_id': 'GXqMsH_dUSM'},
     {'author': 'ComboCurve',
      'channel': 'ComboCurve',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=k4f-XlIpXZU&t=114s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Something I was looking up upon my research is that in terms of drilling rigs, '
              'it comes in second to the Permian, which is kind of surprising. I mean, you '
              "know, I thought we were the oil and gas industry. We're not the gas and oil "
              'industry.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': 'Something I was looking up upon my research is that in terms of drilling rigs, '
             'it comes in second to the Permian, which is kind of surprising. I mean, you '
             "know, I thought we were the oil and gas industry. We're not the gas and oil "
             'industry.',
      'title': 'Breaking Down the Haynesville Shale’s Top Wells (ComboCurve)',
      'url': 'https://www.youtube.com/watch?v=k4f-XlIpXZU&t=114s',
      'video_id': 'k4f-XlIpXZU'},
     {'author': 'UBCFA - University at Buffalo Center for the Arts',
      'channel': 'UBCFA - University at Buffalo Center for the Arts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:58](https://www.youtube.com/watch?v=_C039ie8UHw&t=598s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The puzzling things that that that really puzzles me I did this presentation or '
              'I did a presentation to a law firm in Syracuse a few years a.',
      'timestamp': 598,
      'timestamp_label': '[00:09:58]',
      'timestamp_seconds': 598,
      'tip': 'The puzzling things that that that really puzzles me I did this presentation or '
             'I did a presentation to a law firm in Syracuse a few years a.',
      'title': 'The Marcellus Shale Lecture Series: Greg Sovas on Permitting and Regulation '
               '(April 21) (UBCFA - University at Buffalo Center for the Arts)',
      'url': 'https://www.youtube.com/watch?v=_C039ie8UHw&t=598s',
      'video_id': '_C039ie8UHw'},
     {'author': 'Energy Law Professor',
      'channel': 'Energy Law Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=jZoApbdkCu0&t=147s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We'll look at a case on that so the uh but although it doesn't generally change "
              'your legal rights it can change things a little bit particularly in how your.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': "We'll look at a case on that so the uh but although it doesn't generally change "
             'your legal rights it can change things a little bit particularly in how your.',
      'title': 'Division Orders (Oil & Gas 17.2) (Energy Law Professor)',
      'url': 'https://www.youtube.com/watch?v=jZoApbdkCu0&t=147s',
      'video_id': 'jZoApbdkCu0'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:40](https://www.youtube.com/watch?v=tJr4jiz31fw&t=1300s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And Matt, what what would be your advice to somebody who is trying to figure '
              "out what set of rules they should be following? Yeah, it's very state "
              'dependent.',
      'timestamp': 1300,
      'timestamp_label': '[00:21:40]',
      'timestamp_seconds': 1300,
      'tip': 'And Matt, what what would be your advice to somebody who is trying to figure out '
             "what set of rules they should be following? Yeah, it's very state dependent.",
      'title': "MRP 285: The Mineral Owner's Guide to Division Orders (Matt Sands)",
      'url': 'https://www.youtube.com/watch?v=tJr4jiz31fw&t=1300s',
      'video_id': 'tJr4jiz31fw'},
     {'author': 'Blue Mesa Minerals',
      'channel': 'Blue Mesa Minerals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=08zWLxyGaag&t=194s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just are politically or socially opposed to supporting fossil fuels or they '
              "need the money so there's a lot of reasons that people decide they don't want "
              'to keep the minerals and that can be a good source as well.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': 'Just are politically or socially opposed to supporting fossil fuels or they need '
             "the money so there's a lot of reasons that people decide they don't want to keep "
             'the minerals and that can be a good source as well.',
      'title': 'How to Buy Mineral Rights and Oil & Gas Royalties (Blue Mesa Minerals)',
      'url': 'https://www.youtube.com/watch?v=08zWLxyGaag&t=194s',
      'video_id': '08zWLxyGaag'},
     {'author': 'Steven Hatcher | Minerals Guy',
      'channel': 'Steven Hatcher | Minerals Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=CiR-w5lHfvI&t=260s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Participate for a share of production so if you're driving down the road and "
              "you see a drilling rig within two to three miles from your home there's a.",
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': "Participate for a share of production so if you're driving down the road and you "
             "see a drilling rig within two to three miles from your home there's a.",
      'title': 'How are Mineral Rights Valued? | How Oil and Gas Activity Impacts the Value of '
               'Your Mineral Rights (Steven Hatcher | Minerals Guy)',
      'url': 'https://www.youtube.com/watch?v=CiR-w5lHfvI&t=260s',
      'video_id': 'CiR-w5lHfvI'},
     {'author': 'Matt Sands',
      'channel': 'Matt Sands',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:34](https://www.youtube.com/watch?v=S680WOmo72o&t=814s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's the Southwest quarter of this particular section 27 160 acres and again "
              'you have a full legal description here on this particular section this.',
      'timestamp': 814,
      'timestamp_label': '[00:13:34]',
      'timestamp_seconds': 814,
      'tip': "It's the Southwest quarter of this particular section 27 160 acres and again you "
             'have a full legal description here on this particular section this.',
      'title': 'MRP 226:  How to Use the Texas Railroad Commission Website (Matt Sands)',
      'url': 'https://www.youtube.com/watch?v=S680WOmo72o&t=814s',
      'video_id': 'S680WOmo72o'},
     {'author': 'LMJ Land Services',
      'channel': 'LMJ Land Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=IBxLIQjDNto&t=135s)',
      'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and royalty '
                   '(`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                   'institutional flips (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On my report, each figure shows its math and the instrument it comes from, by '
              'volume and page. Net mineral acres for bonus and leasing. The royalty decimal '
              "for the division order. And the N P R I, with the exact language quoted. I'm "
              'Michele Johnson with LMJ Land Services.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'On my report, each figure shows its math and the instrument it comes from, by '
             'volume and page. Net mineral acres for bonus and leasing. The royalty decimal '
             "for the division order. And the N P R I, with the exact language quoted. I'm "
             'Michele Johnson with LMJ Land Services.',
      'title': 'Net Mineral Acres, Royalty Decimal and NPRI: Three Different Numbers | LMJ '
               'Chalk Talk Ep 22 (LMJ Land Services)',
      'url': 'https://www.youtube.com/watch?v=IBxLIQjDNto&t=135s',
      'video_id': 'IBxLIQjDNto'}],
 10: [{'author': 'ADKF | With You All The Way',
       'channel': 'ADKF | With You All The Way',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:34](https://www.youtube.com/watch?v=GPDm8NftR5U&t=34s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, depletion is a pretty complex calculation. There's two different types of "
               "depletion. There's both cost depletion and statutory depletion or you'll hear "
               'percentage depletion is what its called. Percentage depletion is probably the '
               'easiest to understand.',
       'timestamp': 34,
       'timestamp_label': '[00:00:34]',
       'timestamp_seconds': 34,
       'tip': "So, depletion is a pretty complex calculation. There's two different types of "
              "depletion. There's both cost depletion and statutory depletion or you'll hear "
              'percentage depletion is what its called. Percentage depletion is probably the '
              'easiest to understand.',
       'title': 'How the Depletion Allowance Works in Oil & Gas (ADKF | With You All The Way)',
       'url': 'https://www.youtube.com/watch?v=GPDm8NftR5U&t=34s',
       'video_id': 'GPDm8NftR5U'},
      {'author': 'KAPPA Engineering',
       'channel': 'KAPPA Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=tPB4O0ryZww&t=21s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The citrine project for this demonstration contains several Wells drawn from '
               'four different reservoirs this video showcases a quick method to perform '
               'decline curve analysis on all the wells in a working set field H Wells go to '
               'the analysis tab.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'The citrine project for this demonstration contains several Wells drawn from '
              'four different reservoirs this video showcases a quick method to perform '
              'decline curve analysis on all the wells in a working set field H Wells go to '
              'the analysis tab.',
       'title': 'CITRINE - WORKFLOW- Decline Curve Analysis (KAPPA Engineering)',
       'url': 'https://www.youtube.com/watch?v=tPB4O0ryZww&t=21s',
       'video_id': 'tPB4O0ryZww'},
      {'author': 'Petro Learn',
       'channel': 'Petro Learn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:03](https://www.youtube.com/watch?v=Xr_kSHJguTM&t=303s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But with advancements in automation and AI-driven drilling technologies, the '
               'future of directional drilling looks bright. So, that s a quick look at how '
               'directional drilling is revolutionizing the oil and gas industry!',
       'timestamp': 303,
       'timestamp_label': '[00:05:03]',
       'timestamp_seconds': 303,
       'tip': 'But with advancements in automation and AI-driven drilling technologies, the '
              'future of directional drilling looks bright. So, that s a quick look at how '
              'directional drilling is revolutionizing the oil and gas industry!',
       'title': 'Exploring Directional Drilling: The Key to Modern Oil and Gas Drilling (Petro '
                'Learn)',
       'url': 'https://www.youtube.com/watch?v=Xr_kSHJguTM&t=303s',
       'video_id': 'Xr_kSHJguTM'},
      {'author': 'Tracy Lenz',
       'channel': 'Tracy Lenz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=9zqL93Kdy1I&t=47s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What this is describing is if you were to put a fence around this tract, it '
               'would bound in 320 acres. And let me show you what that looks like on a map. '
               "So we're now looking at Dawson County, section 39 of BLOCK 35, Township four "
               'and of the Tempe Survey.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': 'What this is describing is if you were to put a fence around this tract, it '
              'would bound in 320 acres. And let me show you what that looks like on a map. So '
              "we're now looking at Dawson County, section 39 of BLOCK 35, Township four and "
              'of the Tempe Survey.',
       'title': "What's the difference? Gross vs. Net Mineral Acres (Tracy Lenz)",
       'url': 'https://www.youtube.com/watch?v=9zqL93Kdy1I&t=47s',
       'video_id': '9zqL93Kdy1I'},
      {'author': 'Texas First Court of Appeals',
       'channel': 'Texas First Court of Appeals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:27](https://www.youtube.com/watch?v=oigm_h7P_sc&t=27s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Good afternoon and please be seated. Welcome to the first court of appeals. We '
               'have one case on the docket this afternoon. It is 0124516 Oasis Pipeline '
               'versus Penn Virginia Oil and Gas.',
       'timestamp': 27,
       'timestamp_label': '[00:00:27]',
       'timestamp_seconds': 27,
       'tip': 'Good afternoon and please be seated. Welcome to the first court of appeals. We '
              'have one case on the docket this afternoon. It is 0124516 Oasis Pipeline versus '
              'Penn Virginia Oil and Gas.',
       'title': '(09-17-2026) Case No. 01-24-00516-CV Oasis Pipeline, LP v. Penn Virginia Oil '
                '& Gas, L.P. (Texas First Court of Appeals)',
       'url': 'https://www.youtube.com/watch?v=oigm_h7P_sc&t=27s',
       'video_id': 'oigm_h7P_sc'},
      {'author': 'Eckard Enterprises | Oil & Gas Investing',
       'channel': 'Eckard Enterprises | Oil & Gas Investing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:09](https://www.youtube.com/watch?v=S-yENwSQhi0&t=69s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Number one, I don't like buying speculative mineral rights. I don't want to "
               'lose a single dime. So, with that being said, I want to buy existing proven '
               'producing mineral rights. I want a well- drilled direct offsets.',
       'timestamp': 69,
       'timestamp_label': '[00:01:09]',
       'timestamp_seconds': 69,
       'tip': "Number one, I don't like buying speculative mineral rights. I don't want to "
              'lose a single dime. So, with that being said, I want to buy existing proven '
              'producing mineral rights. I want a well- drilled direct offsets.',
       'title': '5 Fundamentals of Buying Mineral Rights (Eckard Enterprises | Oil & Gas '
                'Investing)',
       'url': 'https://www.youtube.com/watch?v=S-yENwSQhi0&t=69s',
       'video_id': 'S-yENwSQhi0'},
      {'author': 'Steven Hatcher | Minerals Guy',
       'channel': 'Steven Hatcher | Minerals Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=H6l9yCZoYDQ&t=78s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Okay, so here's where you are right here. You have no prior knowledge. Maybe "
               "you've got a real estate background, you're a real estate agent, a mortgage "
               'broker, a real estate investor, wholesaler.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': "Okay, so here's where you are right here. You have no prior knowledge. Maybe "
              "you've got a real estate background, you're a real estate agent, a mortgage "
              'broker, a real estate investor, wholesaler.',
       'title': 'Becoming A Landman: Expectations vs. Reality (Steven Hatcher | Minerals Guy)',
       'url': 'https://www.youtube.com/watch?v=H6l9yCZoYDQ&t=78s',
       'video_id': 'H6l9yCZoYDQ'},
      {'author': 'behoge13',
       'channel': 'behoge13',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:35](https://www.youtube.com/watch?v=le24nqd0H0M&t=1355s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They'll get a royalty payment on it okay so that's good faith and also gives "
               'me an opportunity to talk about the Pew CLA uh two are more good leases so in '
               'this case um lease a had a pooling clause and Lease B did not have a pulling '
               'clause.',
       'timestamp': 1355,
       'timestamp_label': '[00:22:35]',
       'timestamp_seconds': 1355,
       'tip': "They'll get a royalty payment on it okay so that's good faith and also gives me "
              'an opportunity to talk about the Pew CLA uh two are more good leases so in this '
              'case um lease a had a pooling clause and Lease B did not have a pulling clause.',
       'title': 'Pooling & Unitization Webinar (behoge13)',
       'url': 'https://www.youtube.com/watch?v=le24nqd0H0M&t=1355s',
       'video_id': 'le24nqd0H0M'},
      {'author': 'Minerals & Royalties Authority LLC',
       'channel': 'Minerals & Royalties Authority LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:02](https://www.youtube.com/watch?v=xL8qooqAeq0&t=62s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But you kind of think to yourself, why don't these guys ever sell? It's kind "
               "of what you said, these assets are so good. And you get to a point and it's of "
               'scale, where now you just recap and bring in yield investors to own it for the '
               'next 10 or 15 years.',
       'timestamp': 62,
       'timestamp_label': '[00:01:02]',
       'timestamp_seconds': 62,
       'tip': "But you kind of think to yourself, why don't these guys ever sell? It's kind of "
              "what you said, these assets are so good. And you get to a point and it's of "
              'scale, where now you just recap and bring in yield investors to own it for the '
              'next 10 or 15 years.',
       'title': 'Why the Biggest Mineral Portfolios May Never Be Sold (Minerals & Royalties '
                'Authority LLC)',
       'url': 'https://www.youtube.com/watch?v=xL8qooqAeq0&t=62s',
       'video_id': 'xL8qooqAeq0'},
      {'author': 'Francis Ramos II',
       'channel': 'Francis Ramos II',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:59](https://www.youtube.com/watch?v=u3kTgNXLIGI&t=239s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Let me know in the comments down below or leave me a like it really helps out '
               'any feedback I get I will try to take it and put it back into the show and '
               "make it better until next time this is Francis that we'll see you in the next "
               'video peace.',
       'timestamp': 239,
       'timestamp_label': '[00:03:59]',
       'timestamp_seconds': 239,
       'tip': 'Let me know in the comments down below or leave me a like it really helps out '
              'any feedback I get I will try to take it and put it back into the show and make '
              "it better until next time this is Francis that we'll see you in the next video "
              'peace.',
       'title': 'Life of a Well and Decline Curve Analysis (Francis Ramos II)',
       'url': 'https://www.youtube.com/watch?v=u3kTgNXLIGI&t=239s',
       'video_id': 'u3kTgNXLIGI'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:12](https://www.youtube.com/watch?v=NkT15qxxGYM&t=372s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And having that knowledge can help you leverage AI to do it quicker and '
               "faster, but you really still got to know what you're looking at. And you have "
               "to know what data to give it. I think that's one of the parts too that it can "
               'be easily missed.',
       'timestamp': 372,
       'timestamp_label': '[00:06:12]',
       'timestamp_seconds': 372,
       'tip': 'And having that knowledge can help you leverage AI to do it quicker and faster, '
              "but you really still got to know what you're looking at. And you have to know "
              "what data to give it. I think that's one of the parts too that it can be easily "
              'missed.',
       'title': 'MRP 334:  Finally Know What You Own: Use AI to Turn Your Old Deeds Into a '
                'Complete Mineral Rights... (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=NkT15qxxGYM&t=372s',
       'video_id': 'NkT15qxxGYM'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:46](https://www.youtube.com/watch?v=FDXztudBSFk&t=466s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If they do that for third-party customers, and this is in like an interstate '
               'pipeline situation, even though the private companies will build and operate '
               'these, um, they can sometimes leverage eminent domain.',
       'timestamp': 466,
       'timestamp_label': '[00:07:46]',
       'timestamp_seconds': 466,
       'tip': 'If they do that for third-party customers, and this is in like an interstate '
              'pipeline situation, even though the private companies will build and operate '
              'these, um, they can sometimes leverage eminent domain.',
       'title': 'MRP 352:  Mineral Rights News October 2026 (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=FDXztudBSFk&t=466s',
       'video_id': 'FDXztudBSFk'},
      {'author': 'Land Training www.landtraining.net',
       'channel': 'Land Training www.landtraining.net',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:27](https://www.youtube.com/watch?v=eZU5hvGcngg&t=567s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Lease okay and that's going to leave the oil and gas company with the "
               "remaining 1316 okay and all we're doing is taking this 100% minus the 316 so "
               "if the 100% was 1616 which is one then we're going to deduct from that 316 and "
               "that's going to give.",
       'timestamp': 567,
       'timestamp_label': '[00:09:27]',
       'timestamp_seconds': 567,
       'tip': "Lease okay and that's going to leave the oil and gas company with the remaining "
              "1316 okay and all we're doing is taking this 100% minus the 316 so if the 100% "
              "was 1616 which is one then we're going to deduct from that 316 and that's going "
              'to give.',
       'title': 'Calculating WI and NRI in an Oil & Gas Lease by Alyce Hoge (Land Training '
                'www.landtraining.net)',
       'url': 'https://www.youtube.com/watch?v=eZU5hvGcngg&t=567s',
       'video_id': 'eZU5hvGcngg'},
      {'author': 'Steven Hatcher | Minerals Guy',
       'channel': 'Steven Hatcher | Minerals Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:59](https://www.youtube.com/watch?v=hZZNvuvGfkc&t=179s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Spite your face we release videos on this channel every single week that cover '
               "all things minerals and if there's leasing activity in your area and you want "
               'liquidity now click the link below to find out what your minerals could be '
               'worth.',
       'timestamp': 179,
       'timestamp_label': '[00:02:59]',
       'timestamp_seconds': 179,
       'tip': 'Spite your face we release videos on this channel every single week that cover '
              "all things minerals and if there's leasing activity in your area and you want "
              'liquidity now click the link below to find out what your minerals could be '
              'worth.',
       'title': 'Landman vs. Landowner: Who Really Has the Power? (Steven Hatcher | Minerals '
                'Guy)',
       'url': 'https://www.youtube.com/watch?v=hZZNvuvGfkc&t=179s',
       'video_id': 'hZZNvuvGfkc'},
      {'author': 'Neil Jesani Tax Advisors',
       'channel': 'Neil Jesani Tax Advisors',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=FagQvbKX71g&t=47s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '85,000 in the year of investment. The second piece comes from depreciation. '
               'The part that is not an intangible drilling cost is eligible for depreciation '
               "under section 168. Much like anything that's eligible for depreciation, it is "
               'also eligible for bonus depreciation.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': '85,000 in the year of investment. The second piece comes from depreciation. The '
              'part that is not an intangible drilling cost is eligible for depreciation under '
              "section 168. Much like anything that's eligible for depreciation, it is also "
              'eligible for bonus depreciation.',
       'title': 'How to MAXIMIZE OIL\xa0&\xa0GAS TAX DEDUCTIONS (Neil Jesani Tax Advisors)',
       'url': 'https://www.youtube.com/watch?v=FagQvbKX71g&t=47s',
       'video_id': 'FagQvbKX71g'}],
 11: [{'author': 'Eckard Enterprises | Oil & Gas Investing',
       'channel': 'Eckard Enterprises | Oil & Gas Investing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:24](https://www.youtube.com/watch?v=nn1juJ3_-WA&t=624s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Accurately acquisition I hope this explains the decline curve and what goes on '
               'behind the scenes and why decline curves really are a positive to me not a '
               'negative because I want all that money up front just like you thanks.',
       'timestamp': 624,
       'timestamp_label': '[00:10:24]',
       'timestamp_seconds': 624,
       'tip': 'Accurately acquisition I hope this explains the decline curve and what goes on '
              'behind the scenes and why decline curves really are a positive to me not a '
              'negative because I want all that money up front just like you thanks.',
       'title': 'What the Decline Curve Means for Mineral Investments with Troy W. Eckard - '
                'Mineral Royalties 101 (Eckard Enterprises | Oil & Gas Investing)',
       'url': 'https://www.youtube.com/watch?v=nn1juJ3_-WA&t=624s',
       'video_id': 'nn1juJ3_-WA'},
      {'author': 'The Byte-Size Brief',
       'channel': 'The Byte-Size Brief',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:24](https://www.youtube.com/watch?v=fqGTqf-VpBc&t=504s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The strategic trade-off here is clear, and these are the exact execution risks '
               'we must track. Increased inventory and scale come at the direct cost of higher '
               'capital intensity.',
       'timestamp': 504,
       'timestamp_label': '[00:08:24]',
       'timestamp_seconds': 504,
       'tip': 'The strategic trade-off here is clear, and these are the exact execution risks '
              'we must track. Increased inventory and scale come at the direct cost of higher '
              'capital intensity.',
       'title': 'Permian Resources: Record Cash Flow vs. Waha Gas Crisis (The Byte-Size Brief)',
       'url': 'https://www.youtube.com/watch?v=fqGTqf-VpBc&t=504s',
       'video_id': 'fqGTqf-VpBc'},
      {'author': 'Energy Law Professor',
       'channel': 'Energy Law Professor',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:21](https://www.youtube.com/watch?v=aPa6sCIUG-M&t=441s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So for the dry hole and cessation of operations clause at the beginning, it '
               'says you can do additional drilling or reworking. But for the no production at '
               'the end of the primary term, it just says drilling or reworking operations.',
       'timestamp': 441,
       'timestamp_label': '[00:07:21]',
       'timestamp_seconds': 441,
       'tip': 'So for the dry hole and cessation of operations clause at the beginning, it '
              'says you can do additional drilling or reworking. But for the no production at '
              'the end of the primary term, it just says drilling or reworking operations.',
       'title': 'Cessation, Dry Hole, & Continuous Operations Clauses (Oil & Gas 12.2) (Energy '
                'Law Professor)',
       'url': 'https://www.youtube.com/watch?v=aPa6sCIUG-M&t=441s',
       'video_id': 'aPa6sCIUG-M'},
      {'author': 'Energy Vision Global',
       'channel': 'Energy Vision Global',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:07](https://www.youtube.com/watch?v=fihgFZ8xpQo&t=427s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So in practical terms, vertical wells means simplicity and direct access. '
               'Deviated whale means directional flexibility and horizontal veil means greater '
               'reservoir exposure. Now why does this matter in real operations?',
       'timestamp': 427,
       'timestamp_label': '[00:07:07]',
       'timestamp_seconds': 427,
       'tip': 'So in practical terms, vertical wells means simplicity and direct access. '
              'Deviated whale means directional flexibility and horizontal veil means greater '
              'reservoir exposure. Now why does this matter in real operations?',
       'title': 'Vertical, Deviated & Horizontal Wells Explained | Drilling Manual (Energy '
                'Vision Global)',
       'url': 'https://www.youtube.com/watch?v=fihgFZ8xpQo&t=427s',
       'video_id': 'fihgFZ8xpQo'},
      {'author': 'Oliva Gibbs',
       'channel': 'Oliva Gibbs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:09](https://www.youtube.com/watch?v=QPk4GTvt5YU&t=729s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The white parties brought the trespass to try title action after Endeavor '
               'energy began to pay royalties from its drilling operations to both parties in.',
       'timestamp': 729,
       'timestamp_label': '[00:12:09]',
       'timestamp_seconds': 729,
       'tip': 'The white parties brought the trespass to try title action after Endeavor '
              'energy began to pay royalties from its drilling operations to both parties in.',
       'title': 'Fixed & Floating Non-Participating Royalty Interests Issues in Texas & Ohio '
                '(Oliva Gibbs)',
       'url': 'https://www.youtube.com/watch?v=QPk4GTvt5YU&t=729s',
       'video_id': 'QPk4GTvt5YU'},
      {'author': 'Steven Hatcher | Minerals Guy',
       'channel': 'Steven Hatcher | Minerals Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:28](https://www.youtube.com/watch?v=I-uVEypiL9w&t=148s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Almost unlimited so how do you go about buying mineral rights well first you '
               'have to know where to look similar to surface real estate when it comes to.',
       'timestamp': 148,
       'timestamp_label': '[00:02:28]',
       'timestamp_seconds': 148,
       'tip': 'Almost unlimited so how do you go about buying mineral rights well first you '
              'have to know where to look similar to surface real estate when it comes to.',
       'title': 'How To Buy Mineral Rights (Get Into This $800B Industry) (Steven Hatcher | '
                'Minerals Guy)',
       'url': 'https://www.youtube.com/watch?v=I-uVEypiL9w&t=148s',
       'video_id': 'I-uVEypiL9w'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:15](https://www.youtube.com/watch?v=qru8bh4mMms&t=615s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'People may be familiar with an overriding royalty and this is very similar to '
               "that and that it's a non-cost bearing uh royalty in other words we.",
       'timestamp': 615,
       'timestamp_label': '[00:10:15]',
       'timestamp_seconds': 615,
       'tip': 'People may be familiar with an overriding royalty and this is very similar to '
              "that and that it's a non-cost bearing uh royalty in other words we.",
       'title': 'MRP 263:  What You Should Know About Fixed vs Floating NPRIs (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=qru8bh4mMms&t=615s',
       'video_id': 'qru8bh4mMms'},
      {'author': 'Hart Energy',
       'channel': 'Hart Energy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:30](https://www.youtube.com/watch?v=KynEhshipEg&t=330s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Chevron fast canola and ranch we mud log every well we drill so we have a set '
               'of cuttings for every well we stored those cuttings at the international '
               'sample library do paleontology or geochemical analysis on those cuttings.',
       'timestamp': 330,
       'timestamp_label': '[00:05:30]',
       'timestamp_seconds': 330,
       'tip': 'Chevron fast canola and ranch we mud log every well we drill so we have a set '
              'of cuttings for every well we stored those cuttings at the international sample '
              'library do paleontology or geochemical analysis on those cuttings.',
       'title': 'IndustryVoice: Permian Basin: A Solution Story - Part 1 "The Source of '
                'Success" (Hart Energy)',
       'url': 'https://www.youtube.com/watch?v=KynEhshipEg&t=330s',
       'video_id': 'KynEhshipEg'},
      {'author': 'Whitson Academy',
       'channel': 'Whitson Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:23](https://www.youtube.com/watch?v=qdJuFyTh5yU&t=143s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, to help with that, I've come up with a very uh rigorous special snowflake "
               'to a shale to a shale scale that we will use across all of these different '
               'parameters.',
       'timestamp': 143,
       'timestamp_label': '[00:02:23]',
       'timestamp_seconds': 143,
       'tip': "So, to help with that, I've come up with a very uh rigorous special snowflake "
              'to a shale to a shale scale that we will use across all of these different '
              'parameters.',
       'title': 'Quantifying Shale Performance Drivers Across 100,000 Wells | Ryan Hassen, '
                'whitson | whitCon 2026 (Whitson Academy)',
       'url': 'https://www.youtube.com/watch?v=qdJuFyTh5yU&t=143s',
       'video_id': 'qdJuFyTh5yU'},
      {'author': 'HenryFord25',
       'channel': 'HenryFord25',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=NAcWqXJVAcs&t=91s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '$5 million down to maintain it at 27.5% I believe we should study this and '
               'other allowances tax expense dividend expenses and all the rest and make a '
               'determination of how we can stimulate growth how we can provide the revenues '
               'needed to move our country forward.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': '$5 million down to maintain it at 27.5% I believe we should study this and '
              'other allowances tax expense dividend expenses and all the rest and make a '
              'determination of how we can stimulate growth how we can provide the revenues '
              'needed to move our country forward.',
       'title': 'Closing Tax Loopholes: Fairness in Oil Depletion Allowance (HenryFord25)',
       'url': 'https://www.youtube.com/watch?v=NAcWqXJVAcs&t=91s',
       'video_id': 'NAcWqXJVAcs'},
      {'author': 'Land Training www.landtraining.net',
       'channel': 'Land Training www.landtraining.net',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:17](https://www.youtube.com/watch?v=l8BabqqR8og&t=557s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Zero and now what did we say the eight 80 was 16 * 5 I believe we said 6 * 5 '
               "is 30 8 that's right so 8125 is what 1316 decimal converts to let me clean up "
               'my mess here.',
       'timestamp': 557,
       'timestamp_label': '[00:09:17]',
       'timestamp_seconds': 557,
       'tip': 'Zero and now what did we say the eight 80 was 16 * 5 I believe we said 6 * 5 is '
              "30 8 that's right so 8125 is what 1316 decimal converts to let me clean up my "
              'mess here.',
       'title': 'Converting Royalty Fractions to Decimals by Alyce Hoge of Land Training '
                'www.landtraining.net (Land Training www.landtraining.net)',
       'url': 'https://www.youtube.com/watch?v=l8BabqqR8og&t=557s',
       'video_id': 'l8BabqqR8og'},
      {'author': 'Tracy Lenz',
       'channel': 'Tracy Lenz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:18](https://www.youtube.com/watch?v=mHolW0RfGQ0&t=618s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's what I do I'm an appraiser I'm a petroleum engineer I have that "
               'background my contact information is in the description below my company name '
               'is pecan tree oil and gas I am the owner support female small business thank '
               "you and I'll see you in the next video.",
       'timestamp': 618,
       'timestamp_label': '[00:10:18]',
       'timestamp_seconds': 618,
       'tip': "That's what I do I'm an appraiser I'm a petroleum engineer I have that "
              'background my contact information is in the description below my company name '
              'is pecan tree oil and gas I am the owner support female small business thank '
              "you and I'll see you in the next video.",
       'title': 'Working Interest vs Royalty Interest in Oil & Gas - Which is Better for You? '
                '(Tracy Lenz)',
       'url': 'https://www.youtube.com/watch?v=mHolW0RfGQ0&t=618s',
       'video_id': 'mHolW0RfGQ0'},
      {'author': 'Steven Hatcher | Minerals Guy',
       'channel': 'Steven Hatcher | Minerals Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:34](https://www.youtube.com/watch?v=hp69lw89Z-I&t=454s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Going to be leased right to an oil and gas operator an oil company who's "
               'actually going to be conducting those operations now the oil and gas lease is.',
       'timestamp': 454,
       'timestamp_label': '[00:07:34]',
       'timestamp_seconds': 454,
       'tip': "Going to be leased right to an oil and gas operator an oil company who's "
              'actually going to be conducting those operations now the oil and gas lease is.',
       'title': 'Mineral Rights Explained By Oil and Gas Attorney | Mineral Rights 101 | What '
                'Are Mineral Rights? (Steven Hatcher | Minerals Guy)',
       'url': 'https://www.youtube.com/watch?v=hp69lw89Z-I&t=454s',
       'video_id': 'hp69lw89Z-I'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:02](https://www.youtube.com/watch?v=IZpkZEGcVjk&t=1322s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '"Hey, we\'re going to start drilling more wells because of the higher oil '
               'prices." Yeah, especially if we\'re adding a rig in the Haynesville and the '
               "Granite Wash versus other basins where they're more oil-focused.",
       'timestamp': 1322,
       'timestamp_label': '[00:22:02]',
       'timestamp_seconds': 1322,
       'tip': '"Hey, we\'re going to start drilling more wells because of the higher oil '
              'prices." Yeah, especially if we\'re adding a rig in the Haynesville and the '
              "Granite Wash versus other basins where they're more oil-focused.",
       'title': 'MRP 331:  Mineral Rights News May 2026 (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=IZpkZEGcVjk&t=1322s',
       'video_id': 'IZpkZEGcVjk'},
      {'author': 'ADKF | With You All The Way',
       'channel': 'ADKF | With You All The Way',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=GPDm8NftR5U&t=26s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, Austin, you mentioned depletion earlier. Tell me, how does the depletion '
               'allowance work in oil and gas properties and how it is calculated? So, '
               "depletion is a pretty complex calculation. There's two different types of "
               'depletion.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': 'So, Austin, you mentioned depletion earlier. Tell me, how does the depletion '
              'allowance work in oil and gas properties and how it is calculated? So, '
              "depletion is a pretty complex calculation. There's two different types of "
              'depletion.',
       'title': 'How the Depletion Allowance Works in Oil & Gas (ADKF | With You All The Way)',
       'url': 'https://www.youtube.com/watch?v=GPDm8NftR5U&t=26s',
       'video_id': 'GPDm8NftR5U'}],
 12: [{'author': 'Expand Energy',
       'channel': 'Expand Energy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=zhTs0NrEVgE&t=21s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'During the drilling process, the rig typically is in constant operation 24 '
               'hours a day, 7 days a week for approximately 21 to 28 days. As an added '
               'precaution, in some areas, a protective mat covers 2/3 of the pad site.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'During the drilling process, the rig typically is in constant operation 24 '
              'hours a day, 7 days a week for approximately 21 to 28 days. As an added '
              'precaution, in some areas, a protective mat covers 2/3 of the pad site.',
       'title': 'Horizontal Drilling Method (Expand Energy)',
       'url': 'https://www.youtube.com/watch?v=zhTs0NrEVgE&t=21s',
       'video_id': 'zhTs0NrEVgE'},
      {'author': 'Oil & Gas Industry VDA',
       'channel': 'Oil & Gas Industry VDA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=7tXxUXv528A&t=20s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'During the drilling process, the rig is in constant operation 24 hours a day, '
               '7 days a week for approximately 21 to 28 days. As an added precaution in some '
               'areas, a protective mat covers 2/3 of the pad site.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'During the drilling process, the rig is in constant operation 24 hours a day, 7 '
              'days a week for approximately 21 to 28 days. As an added precaution in some '
              'areas, a protective mat covers 2/3 of the pad site.',
       'title': 'Chesapeake Energy horizontal drilling method | Oil & Gas Industry (Oil & Gas '
                'Industry VDA)',
       'url': 'https://www.youtube.com/watch?v=7tXxUXv528A&t=20s',
       'video_id': '7tXxUXv528A'},
      {'author': 'Toby Mathis Esq | Tax Planning & Asset Protection',
       'channel': 'Toby Mathis Esq | Tax Planning & Asset Protection',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:19](https://www.youtube.com/watch?v=TfG5auc0OXc&t=379s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So if I invest $100,000, I could be doing that towards the end of the year so '
               'long as they start the actual drilling within 90 days of the end of the year, '
               'you would get it for the year that you made the investment.',
       'timestamp': 379,
       'timestamp_label': '[00:06:19]',
       'timestamp_seconds': 379,
       'tip': 'So if I invest $100,000, I could be doing that towards the end of the year so '
              'long as they start the actual drilling within 90 days of the end of the year, '
              'you would get it for the year that you made the investment.',
       'title': 'How To GET Massive TAX Deductions From Oil And Gas Investments (Toby Mathis '
                'Esq | Tax Planning & Asset Protection)',
       'url': 'https://www.youtube.com/watch?v=TfG5auc0OXc&t=379s',
       'video_id': 'TfG5auc0OXc'},
      {'author': 'Railroad Commission of Texas',
       'channel': 'Railroad Commission of Texas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:54](https://www.youtube.com/watch?v=dDocusqGT08&t=234s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "This page contains links to the railroad commission's current online "
               'applications launch an application by clicking on the logo or learn more using '
               'the link at the bottom of each tile which will direct you to that '
               "application's information page.",
       'timestamp': 234,
       'timestamp_label': '[00:03:54]',
       'timestamp_seconds': 234,
       'tip': "This page contains links to the railroad commission's current online "
              'applications launch an application by clicking on the logo or learn more using '
              "the link at the bottom of each tile which will direct you to that application's "
              'information page.',
       'title': '#TxRRC Web Tour (Railroad Commission of Texas)',
       'url': 'https://www.youtube.com/watch?v=dDocusqGT08&t=234s',
       'video_id': 'dDocusqGT08'},
      {'author': 'WXYZ-TV Detroit | Channel 7',
       'channel': 'WXYZ-TV Detroit | Channel 7',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:12](https://www.youtube.com/watch?v=K4HrSTGgbFs&t=72s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Did go out to the word of faith baptist church on Sunday they plan to do so '
               'every Sunday and look for ways to stop this oil drilling from happening for '
               'now live in southfield breanne Paul marini 7 Action News thank you for that '
               'well.',
       'timestamp': 72,
       'timestamp_label': '[00:01:12]',
       'timestamp_seconds': 72,
       'tip': 'Did go out to the word of faith baptist church on Sunday they plan to do so '
              'every Sunday and look for ways to stop this oil drilling from happening for now '
              'live in southfield breanne Paul marini 7 Action News thank you for that well.',
       'title': 'Protests of Southfield oil drilling permit (WXYZ-TV Detroit | Channel 7)',
       'url': 'https://www.youtube.com/watch?v=K4HrSTGgbFs&t=72s',
       'video_id': 'K4HrSTGgbFs'},
      {'author': 'Steven Hatcher | Minerals Guy',
       'channel': 'Steven Hatcher | Minerals Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:57](https://www.youtube.com/watch?v=kA4imCIrIU0&t=57s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'t have to worry about running for your life every day. So, what does a "
               'landman really do? Landmen are the deal makers and deal finders in the oil and '
               'gas industry. I spend my days doing research, reading, and looking at '
               'acquisition opportunities for my business.',
       'timestamp': 57,
       'timestamp_label': '[00:00:57]',
       'timestamp_seconds': 57,
       'tip': "'t have to worry about running for your life every day. So, what does a landman "
              'really do? Landmen are the deal makers and deal finders in the oil and gas '
              'industry. I spend my days doing research, reading, and looking at acquisition '
              'opportunities for my business.',
       'title': '3 Things You Need to Know Before Becoming a Landman (Steven Hatcher | '
                'Minerals Guy)',
       'url': 'https://www.youtube.com/watch?v=kA4imCIrIU0&t=57s',
       'video_id': 'kA4imCIrIU0'},
      {'author': 'Whitson Academy',
       'channel': 'Whitson Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:50:23](https://www.youtube.com/watch?v=r0aIro_ccSI&t=3023s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um, I would even go a little bit further and have target injection volumes in '
               "mind. So when you, let's say I have a compressor, I have the ability to inject "
               'X amount of scuffs per day. But the goal should be in 30 days, how much can I '
               'get to the reservoir.',
       'timestamp': 3023,
       'timestamp_label': '[00:50:23]',
       'timestamp_seconds': 3023,
       'tip': 'Um, I would even go a little bit further and have target injection volumes in '
              "mind. So when you, let's say I have a compressor, I have the ability to inject "
              'X amount of scuffs per day. But the goal should be in 30 days, how much can I '
              'get to the reservoir.',
       'title': '[whitson webinar] Advancing Gas EOR in Shale: Lessons from a Chevron-led '
                'Permian Pilot (Whitson Academy)',
       'url': 'https://www.youtube.com/watch?v=r0aIro_ccSI&t=3023s',
       'video_id': 'r0aIro_ccSI'},
      {'author': 'Commission Shift',
       'channel': 'Commission Shift',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:01](https://www.youtube.com/watch?v=fqz-wQBuZ2A&t=481s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And um you know, the most important thing at the end of the day to the '
               "railroad commission is that um they're they're you know, they're supposed to "
               'protect uh safety and private property.',
       'timestamp': 481,
       'timestamp_label': '[00:08:01]',
       'timestamp_seconds': 481,
       'tip': 'And um you know, the most important thing at the end of the day to the railroad '
              "commission is that um they're they're you know, they're supposed to protect uh "
              'safety and private property.',
       'title': 'Recap of the Railroad Commission of Texas Open Meeting, June 20th, 2025 '
                '(Commission Shift)',
       'url': 'https://www.youtube.com/watch?v=fqz-wQBuZ2A&t=481s',
       'video_id': 'fqz-wQBuZ2A'},
      {'author': 'Land Training www.landtraining.net',
       'channel': 'Land Training www.landtraining.net',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:16](https://www.youtube.com/watch?v=wUqopw4hh2o&t=436s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Them and so Bobby's interest is a 0.125 .125 royalty interest times 25 mineral "
               'interest times the number of acres in the least tract divided by the total '
               "unit Acres okay let's start over 0.125 times 0.25.",
       'timestamp': 436,
       'timestamp_label': '[00:07:16]',
       'timestamp_seconds': 436,
       'tip': "Them and so Bobby's interest is a 0.125 .125 royalty interest times 25 mineral "
              'interest times the number of acres in the least tract divided by the total unit '
              "Acres okay let's start over 0.125 times 0.25.",
       'title': 'VII NRI Co Tenants Different RI in a Spacing Unit Prob 1 (Land Training '
                'www.landtraining.net)',
       'url': 'https://www.youtube.com/watch?v=wUqopw4hh2o&t=436s',
       'video_id': 'wUqopw4hh2o'},
      {'author': 'LandApp by LandGate',
       'channel': 'LandApp by LandGate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:58](https://www.youtube.com/watch?v=r7MMN5ueVCs&t=118s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Rights list your mineral rights for sale or release for free on land Gates '
               "Marketplace today it's a fantastic way to start receiving offers and unlock "
               'the hidden value Beneath Your Land go to landgate tocom or click the link in '
               'the video description to get started.',
       'timestamp': 118,
       'timestamp_label': '[00:01:58]',
       'timestamp_seconds': 118,
       'tip': 'Rights list your mineral rights for sale or release for free on land Gates '
              "Marketplace today it's a fantastic way to start receiving offers and unlock the "
              'hidden value Beneath Your Land go to landgate tocom or click the link in the '
              'video description to get started.',
       'title': "Mineral Rights vs. Mineral Royalties - What's the Difference? 💰 (LandApp by "
                'LandGate)',
       'url': 'https://www.youtube.com/watch?v=r7MMN5ueVCs&t=118s',
       'video_id': 'r7MMN5ueVCs'},
      {'author': 'Blue Mesa Minerals',
       'channel': 'Blue Mesa Minerals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:01](https://www.youtube.com/watch?v=PAfHHmByY2I&t=421s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can add it and sort of add to it as more information becomes available but '
               "this spreadsheet is something you're going to be referring to reasonably often "
               'so you definitely need to have it organized and this is the way you start I '
               'hope this has been helpful.',
       'timestamp': 421,
       'timestamp_label': '[00:07:01]',
       'timestamp_seconds': 421,
       'tip': 'You can add it and sort of add to it as more information becomes available but '
              "this spreadsheet is something you're going to be referring to reasonably often "
              'so you definitely need to have it organized and this is the way you start I '
              'hope this has been helpful.',
       'title': 'How to locate your mineral rights on a map (and research oil and gas wells) '
                '(Blue Mesa Minerals)',
       'url': 'https://www.youtube.com/watch?v=PAfHHmByY2I&t=421s',
       'video_id': 'PAfHHmByY2I'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=oHhvtjxLX9c&t=117s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Day weekend, and that's marks the start of the summer driving season, and "
               "that's usually when you'll see a little bit higher gas prices just because of "
               'demand, but, you know, obviously, the uh oil supply situation has been causing '
               'an extra impact this year.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "Day weekend, and that's marks the start of the summer driving season, and "
              "that's usually when you'll see a little bit higher gas prices just because of "
              'demand, but, you know, obviously, the uh oil supply situation has been causing '
              'an extra impact this year.',
       'title': 'MRP 335:  Mineral Rights News June 2026 (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=oHhvtjxLX9c&t=117s',
       'video_id': 'oHhvtjxLX9c'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:22:12](https://www.youtube.com/watch?v=KwKa_52Hpqk&t=1332s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And the other question, you know, logical question is so if we expect to see '
               'oil prices higher for longer, you know, when are we going to start seeing an '
               'increase in drilling?',
       'timestamp': 1332,
       'timestamp_label': '[00:22:12]',
       'timestamp_seconds': 1332,
       'tip': 'And the other question, you know, logical question is so if we expect to see '
              'oil prices higher for longer, you know, when are we going to start seeing an '
              'increase in drilling?',
       'title': 'MRP 327:  Mineral Rights News April 2026 (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=KwKa_52Hpqk&t=1332s',
       'video_id': 'KwKa_52Hpqk'},
      {'author': 'Matt Sands',
       'channel': 'Matt Sands',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:33](https://www.youtube.com/watch?v=n2MrqKJ_h80&t=933s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re looking at it week to week, there's a growth here. Yeah, when we reported "
               "this last month, we had 551 land rigs, now we're at 572, so we're up about 4% "
               'just under 4% uh month to month.',
       'timestamp': 933,
       'timestamp_label': '[00:15:33]',
       'timestamp_seconds': 933,
       'tip': "'re looking at it week to week, there's a growth here. Yeah, when we reported "
              "this last month, we had 551 land rigs, now we're at 572, so we're up about 4% "
              'just under 4% uh month to month.',
       'title': 'MRP 345:  Mineral Rights News August 2026 (Matt Sands)',
       'url': 'https://www.youtube.com/watch?v=n2MrqKJ_h80&t=933s',
       'video_id': 'n2MrqKJ_h80'},
      {'author': 'Royalty Clerk',
       'channel': 'Royalty Clerk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:51](https://www.youtube.com/watch?v=blbomhUd0sA&t=231s)',
       'relevance': 'Attributed practitioner commentary on oil & gas mineral rights and '
                    'royalty (`NMA`/`NPRI`) underwriting, pooling-docket curve-jumping, and '
                    'institutional flips (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Please send me the division order for this lease showing my decimal interest, '
               'the unit acres you used, and how my net mineral acres were counted. And if the '
               'decimal is wrong, ask for corrected payments back to the first month it was '
               'wrong.',
       'timestamp': 231,
       'timestamp_label': '[00:03:51]',
       'timestamp_seconds': 231,
       'tip': 'Please send me the division order for this lease showing my decimal interest, '
              'the unit acres you used, and how my net mineral acres were counted. And if the '
              'decimal is wrong, ask for corrected payments back to the first month it was '
              'wrong.',
       'title': 'What Your Decimal Interest Means (and How to Check It) (Royalty Clerk)',
       'url': 'https://www.youtube.com/watch?v=blbomhUd0sA&t=231s',
       'video_id': 'blbomhUd0sA'}]}
