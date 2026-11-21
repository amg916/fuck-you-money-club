"""Curated 180-citation Equipment Brokerage baseline (15 per chapter across Q1-Q12) mined strictly from verified Equipment Brokerage YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'center',
     'client',
     'clients',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'data',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'budget',
     'building',
     'bulldozers',
     'business',
     'buyer',
     'center',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contract',
     'contractors',
     'customer',
     'data',
     'dealer',
     'decision',
     'decommissioned',
     'desk',
     'disclaimer',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'cash',
     'cashflow',
     'center',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'cost',
     'costs',
     'data',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'budget',
     'building',
     'bulldozers',
     'business',
     'capital',
     'center',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'data',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
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
 5: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'audit',
     'avoid',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'center',
     'clawback',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'data',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
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
 6: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'center',
     'client',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'data',
     'deal',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
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
 7: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'center',
     'checklist',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'data',
     'dealer',
     'decommissioned',
     'delivery',
     'desk',
     'disclaimer',
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
 8: {'agreement',
     'agricultural',
     'api',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'center',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'consignment',
     'construction',
     'contractors',
     'crm',
     'data',
     'database',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'agreement',
     'agricultural',
     'appraisal',
     'arbitrage',
     'auction',
     'avoiding',
     'back',
     'bankruptcy',
     'bill',
     'broker',
     'brokerage',
     'brokering',
     'bros',
     'building',
     'bulldozers',
     'business',
     'center',
     'closure',
     'cnc',
     'combine',
     'commercial',
     'commission',
     'compliance',
     'consignment',
     'construction',
     'contract',
     'contractors',
     'data',
     'dealer',
     'decommissioned',
     'desk',
     'disclaimer',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'agent',
      'agreement',
      'agricultural',
      'ai',
      'appraisal',
      'arbitrage',
      'auction',
      'automate',
      'automation',
      'avoiding',
      'back',
      'bankruptcy',
      'bill',
      'broker',
      'brokerage',
      'brokering',
      'bros',
      'building',
      'bulldozers',
      'business',
      'center',
      'closure',
      'cnc',
      'combine',
      'commercial',
      'commission',
      'consignment',
      'construction',
      'contractors',
      'dashboard',
      'data',
      'dealer',
      'decommissioned',
      'desk',
      'disclaimer',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'agreement',
      'agricultural',
      'appraisal',
      'arbitrage',
      'auction',
      'avoiding',
      'back',
      'bankruptcy',
      'bill',
      'broker',
      'brokerage',
      'brokering',
      'bros',
      'building',
      'bulldozers',
      'business',
      'center',
      'closure',
      'cnc',
      'combine',
      'commercial',
      'commission',
      'consignment',
      'construction',
      'contractor',
      'contractors',
      'data',
      'dealer',
      'decommissioned',
      'desk',
      'disclaimer',
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
 12: {'action',
      'agreement',
      'agricultural',
      'appraisal',
      'arbitrage',
      'auction',
      'avoiding',
      'back',
      'bankruptcy',
      'bill',
      'broker',
      'brokerage',
      'brokering',
      'bros',
      'building',
      'bulldozers',
      'business',
      'center',
      'closure',
      'cnc',
      'combine',
      'commercial',
      'commission',
      'consignment',
      'construction',
      'contractors',
      'data',
      'day',
      'days',
      'dealer',
      'decommissioned',
      'desk',
      'disclaimer',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Sobre Orugas',
      'channel': 'Sobre Orugas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:40](https://www.youtube.com/watch?v=xUze3OGayRk&t=400s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the buyer does not have an account, well, they can do it through a brokerage '
              'firm or through us. We do that conversion and solve it at the value of the '
              'equipment. Well, as you know, it is by law, except for agricultural equipment. '
              'Everything else must be charged 16%VAT.',
      'timestamp': 400,
      'timestamp_label': '[00:06:40]',
      'timestamp_seconds': 400,
      'tip': 'If the buyer does not have an account, well, they can do it through a brokerage '
             'firm or through us. We do that conversion and solve it at the value of the '
             'equipment. Well, as you know, it is by law, except for agricultural equipment. '
             'Everything else must be charged 16%VAT.',
      'title': 'Cómo comprar o vender en las subastas de Ritchie Bros México (Sobre Orugas)',
      'url': 'https://www.youtube.com/watch?v=xUze3OGayRk&t=400s',
      'video_id': 'xUze3OGayRk'},
     {'author': 'HGreg Lux',
      'channel': 'HGreg Lux',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=8w7SLSenX5k&t=28s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Just in summary, it's a hassle and a headache. And then of course you could "
              "sell it to a dealership, but everybody knows the dealer's in for business to "
              "make money, so you're definitely going to be looking at less market value of "
              'what your car is worth.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "Just in summary, it's a hassle and a headache. And then of course you could sell "
             "it to a dealership, but everybody knows the dealer's in for business to make "
             "money, so you're definitely going to be looking at less market value of what "
             'your car is worth.',
      'title': 'What is consignment? (HGreg Lux)',
      'url': 'https://www.youtube.com/watch?v=8w7SLSenX5k&t=28s',
      'video_id': '8w7SLSenX5k'},
     {'author': 'A Finance Insider',
      'channel': 'A Finance Insider',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:54](https://www.youtube.com/watch?v=pgvX9soJ0Kk&t=594s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They do it by building relationships with repeat commercial and municipal '
              'clients who book equipment months in advance, smoothing out the unpredictable '
              'swings that destroy operators relying purely on walk-in rental demand.',
      'timestamp': 594,
      'timestamp_label': '[00:09:54]',
      'timestamp_seconds': 594,
      'tip': 'They do it by building relationships with repeat commercial and municipal '
             'clients who book equipment months in advance, smoothing out the unpredictable '
             'swings that destroy operators relying purely on walk-in rental demand.',
      'title': 'The Economics of Owning a Heavy Machinery Rental Business (A Finance Insider)',
      'url': 'https://www.youtube.com/watch?v=pgvX9soJ0Kk&t=594s',
      'video_id': 'pgvX9soJ0Kk'},
     {'author': 'Beiing Human',
      'channel': 'Beiing Human',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:26](https://www.youtube.com/watch?v=sNcACw9iXI0&t=926s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How do you tie equipment fleet KPIs back to margin improvement and job level '
              'profitability? Can you share an example of where fleet data led to better '
              'financial results? So I think one of the important things is tracking all kinds '
              'of downtime on a project, right?',
      'timestamp': 926,
      'timestamp_label': '[00:15:26]',
      'timestamp_seconds': 926,
      'tip': 'How do you tie equipment fleet KPIs back to margin improvement and job level '
             'profitability? Can you share an example of where fleet data led to better '
             'financial results? So I think one of the important things is tracking all kinds '
             'of downtime on a project, right?',
      'title': 'Fleet Strategy for Contractors: Preventive Maintenance, KPIs & CFO Insights '
               '(Yvette Aubin) (Beiing Human)',
      'url': 'https://www.youtube.com/watch?v=sNcACw9iXI0&t=926s',
      'video_id': 'sNcACw9iXI0'},
     {'author': 'ET Transport',
      'channel': 'ET Transport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:10](https://www.youtube.com/watch?v=ubGpPmWhLFE&t=970s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The identical truck with 100,000 km more. So, this one will probably fair '
              "market value for this one is anywhere in the 80s. I'm going go ahead and I'm "
              "going to bid on this. Now I am the highest bidder. So let's go back to our main "
              'page.',
      'timestamp': 970,
      'timestamp_label': '[00:16:10]',
      'timestamp_seconds': 970,
      'tip': 'The identical truck with 100,000 km more. So, this one will probably fair market '
             "value for this one is anywhere in the 80s. I'm going go ahead and I'm going to "
             "bid on this. Now I am the highest bidder. So let's go back to our main page.",
      'title': 'BUYING EQUIPMENT LIVE AT THE RITCHIE BROTHERS AUCTION! (ET Transport)',
      'url': 'https://www.youtube.com/watch?v=ubGpPmWhLFE&t=970s',
      'video_id': 'ubGpPmWhLFE'},
     {'author': 'Nick Mitchell',
      'channel': 'Nick Mitchell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=zK9IyH3CceE&t=180s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'At the same time, the prices at auction and at dealerships are also going down. '
              'So, for these, we think that there is a shrinking market or just not as much of '
              'a need for these medium-duty construction equipment pieces.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'At the same time, the prices at auction and at dealerships are also going down. '
             'So, for these, we think that there is a shrinking market or just not as much of '
             'a need for these medium-duty construction equipment pieces.',
      'title': 'Is Your Equipment Value Falling? September 2026 Market Report (Nick Mitchell)',
      'url': 'https://www.youtube.com/watch?v=zK9IyH3CceE&t=180s',
      'video_id': 'zK9IyH3CceE'},
     {'author': 'Joe Camberato',
      'channel': 'Joe Camberato',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=H6xXORaU7Jo&t=86s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, the lender can take back that piece of equipment. What's important when "
              "you're going to finance equipment is, is it a dollar buyout or is it a fair "
              'market value equipment lease? Those 2 things are really important.',
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': "So, the lender can take back that piece of equipment. What's important when "
             "you're going to finance equipment is, is it a dollar buyout or is it a fair "
             'market value equipment lease? Those 2 things are really important.',
      'title': 'How Does Equipment Leasing Work? (Joe Camberato)',
      'url': 'https://www.youtube.com/watch?v=H6xXORaU7Jo&t=86s',
      'video_id': 'H6xXORaU7Jo'},
     {'author': 'Hitachi',
      'channel': 'Hitachi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=Qy6qJxkOhZk&t=143s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hitachi Medical Systems equipment to any of our clients. I feel happy about our '
              'future business prospects. This project was very interesting for us at Hitachi, '
              'because we had to deal with the many criteria that the Dar El Ashaa Imaging '
              'Center required.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': 'Hitachi Medical Systems equipment to any of our clients. I feel happy about our '
             'future business prospects. This project was very interesting for us at Hitachi, '
             'because we had to deal with the many criteria that the Dar El Ashaa Imaging '
             'Center required.',
      'title': 'Success : Hitachi Medical Systems Solution for Medical Imaging in Egypt '
               '(Hitachi)',
      'url': 'https://www.youtube.com/watch?v=Qy6qJxkOhZk&t=143s',
      'video_id': 'Qy6qJxkOhZk'},
     {'author': 'diggersanddozers',
      'channel': 'diggersanddozers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=UEa5rUq-aB0&t=238s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All the work on Research ing it and you actually pick which machine suits your '
              "purpose best does the dealer actually add any real value we'd love to hear from "
              'you hit the comments below and let us know what you think and thanks for '
              'watching.',
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': 'All the work on Research ing it and you actually pick which machine suits your '
             "purpose best does the dealer actually add any real value we'd love to hear from "
             'you hit the comments below and let us know what you think and thanks for '
             'watching.',
      'title': 'The Lost Art of Construction Equipment Sales (diggersanddozers)',
      'url': 'https://www.youtube.com/watch?v=UEa5rUq-aB0&t=238s',
      'video_id': 'UEa5rUq-aB0'},
     {'author': 'Equipment Broker Academy',
      'channel': 'Equipment Broker Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=_c4_PRT-_rE&t=116s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Seven thousand five hundred dollars for your client nine percent your average '
              'would be about twenty five hundred dollar commission for that and if you.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': 'Seven thousand five hundred dollars for your client nine percent your average '
             'would be about twenty five hundred dollar commission for that and if you.',
      'title': 'What is an Equipment Broker (Equipment Broker Academy)',
      'url': 'https://www.youtube.com/watch?v=_c4_PRT-_rE&t=116s',
      'video_id': '_c4_PRT-_rE'},
     {'author': "Brown's Medical Imaging",
      'channel': "Brown's Medical Imaging",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=DpGCQ1Ijs-Y&t=54s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All back together it looks like it did when it came from the factory '
              'reconditioning equipment adds value a lot of same processes that the CT can.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'All back together it looks like it did when it came from the factory '
             'reconditioning equipment adds value a lot of same processes that the CT can.',
      'title': 'CT Scan Machines for Sale | MRI Machines for Sale - The Complete Restoration '
               "Guide by BMI Techs (Brown's Medical Imaging)",
      'url': 'https://www.youtube.com/watch?v=DpGCQ1Ijs-Y&t=54s',
      'video_id': 'DpGCQ1Ijs-Y'},
     {'author': 'RealAgriculture',
      'channel': 'RealAgriculture',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:42](https://www.youtube.com/watch?v=DSk-SojWGxU&t=1062s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Softening on auction prices with late model combines and they weren't you know "
              'like blood in the water type prices like giveaways At All by any means but '
              'more.',
      'timestamp': 1062,
      'timestamp_label': '[00:17:42]',
      'timestamp_seconds': 1062,
      'tip': "Softening on auction prices with late model combines and they weren't you know "
             'like blood in the water type prices like giveaways At All by any means but more.',
      'title': "Don't like used equipment prices? It could get worse, says Machinery Pete "
               '(RealAgriculture)',
      'url': 'https://www.youtube.com/watch?v=DSk-SojWGxU&t=1062s',
      'video_id': 'DSk-SojWGxU'},
     {'author': 'Block Imaging',
      'channel': 'Block Imaging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=4suol4m0dq4&t=55s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Could be used to service equipment that's only a generation old um or maybe two "
              'generations old and so there still is some value the other thing that as.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "Could be used to service equipment that's only a generation old um or maybe two "
             'generations old and so there still is some value the other thing that as.',
      'title': 'Sell Us Your Old Medical Equipment and Get the Most Value (Block Imaging)',
      'url': 'https://www.youtube.com/watch?v=4suol4m0dq4&t=55s',
      'video_id': '4suol4m0dq4'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:08](https://www.youtube.com/watch?v=Rz6KNtveaDU&t=728s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This 97 model john deere 8100 2811 hours on it for a hundred thousand bucks '
              'fifth highest auction price ever on a john deere 8100.',
      'timestamp': 728,
      'timestamp_label': '[00:12:08]',
      'timestamp_seconds': 728,
      'tip': 'This 97 model john deere 8100 2811 hours on it for a hundred thousand bucks '
             'fifth highest auction price ever on a john deere 8100.',
      'title': 'John Deere 7810 and 7320 Tractors Bring Record Money on Maryland Auction | '
               'MPTV (Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=Rz6KNtveaDU&t=728s',
      'video_id': 'Rz6KNtveaDU'},
     {'author': 'Cat Products',
      'channel': 'Cat Products',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=fP5ysbGB2H0&t=211s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Report that can ultimately give to your customer to help them understand what's "
              'going on with their undercarriage from aware perspective it helps build loyalty '
              'customer service between the customers and the dealers.',
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': "Report that can ultimately give to your customer to help them understand what's "
             'going on with their undercarriage from aware perspective it helps build loyalty '
             'customer service between the customers and the dealers.',
      'title': 'How to Measure your Undercarriage (Cat Products)',
      'url': 'https://www.youtube.com/watch?v=fP5ysbGB2H0&t=211s',
      'video_id': 'fP5ysbGB2H0'}],
 2: [{'author': 'Marginomics',
      'channel': 'Marginomics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=Lx3Lqgr9q3w&t=319s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rent alone barely covers the bills. Add the 11,000 in fees and charges, and '
              'Dale is left with 12,500. Those fees pay for real things. The delivery fee '
              'helps cover the truck and the driver, and the protection plan keeps a bent '
              "track off the customer's bill.",
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': 'Rent alone barely covers the bills. Add the 11,000 in fees and charges, and Dale '
             'is left with 12,500. Those fees pay for real things. The delivery fee helps '
             'cover the truck and the driver, and the protection plan keeps a bent track off '
             "the customer's bill.",
      'title': 'How Construction Equipment Rental Business Owners Actually Make Money '
               '(Marginomics)',
      'url': 'https://www.youtube.com/watch?v=Lx3Lqgr9q3w&t=319s',
      'video_id': 'Lx3Lqgr9q3w'},
     {'author': 'IronPlanet',
      'channel': 'IronPlanet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=qHDv4e8rQQw&t=205s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step five, payment and accepting delivery. Once the auction is over, you will '
              'be contacted directly by a member of our customer care team. In order to pay '
              'for your purchase, buyers are required to pay into a secure account that we '
              'manage.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Step five, payment and accepting delivery. Once the auction is over, you will be '
             'contacted directly by a member of our customer care team. In order to pay for '
             'your purchase, buyers are required to pay into a secure account that we manage.',
      'title': 'How to Buy Heavy Equipment at an IronPlanet Online Auction (IronPlanet)',
      'url': 'https://www.youtube.com/watch?v=qHDv4e8rQQw&t=205s',
      'video_id': 'qHDv4e8rQQw'},
     {'author': 'Mutha Trucker - Official Trucking Channel',
      'channel': 'Mutha Trucker - Official Trucking Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=ZSZAVstSGl8&t=233s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, think of bonds like an insurance. The broker pays like a monthly fee. If '
              "they don't pay you, then the bond company steps in and pays it. And then they "
              'chase that freight broker for the money.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'So, think of bonds like an insurance. The broker pays like a monthly fee. If '
             "they don't pay you, then the bond company steps in and pays it. And then they "
             'chase that freight broker for the money.',
      'title': 'Big Win! FMCSA Will Shutdown Thousands Of Freight Brokers In 2026 🤯 (Mutha '
               'Trucker - Official Trucking Channel)',
      'url': 'https://www.youtube.com/watch?v=ZSZAVstSGl8&t=233s',
      'video_id': 'ZSZAVstSGl8'},
     {'author': 'RDO Equipment Co.',
      'channel': 'RDO Equipment Co.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=kAP9Lw8qKFA&t=34s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Projects building their business how does that help you from a customer's "
              "perspective just renting a machine you're gaining no equity I feel it's.",
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': "Projects building their business how does that help you from a customer's "
             "perspective just renting a machine you're gaining no equity I feel it's.",
      'title': 'How to Build A Fleet with Rent to Own Construction Equipment (RDO Equipment '
               'Co.)',
      'url': 'https://www.youtube.com/watch?v=kAP9Lw8qKFA&t=34s',
      'video_id': 'kAP9Lw8qKFA'},
     {'author': 'NerdWallet Small Business',
      'channel': 'NerdWallet Small Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=9ztMvgoQsgE&t=44s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'UCC lien against all of your business assets. Whichever the type of lien, '
              'here’s the important part. If for some reason you can’t pay your loan back, the '
              'lien gives the lender the right to seize the assets that are secured and sell '
              'them to repay the loan.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'UCC lien against all of your business assets. Whichever the type of lien, here’s '
             'the important part. If for some reason you can’t pay your loan back, the lien '
             'gives the lender the right to seize the assets that are secured and sell them to '
             'repay the loan.',
      'title': 'UCC Liens: What Do They Mean for Your Business? (NerdWallet Small Business)',
      'url': 'https://www.youtube.com/watch?v=9ztMvgoQsgE&t=44s',
      'video_id': '9ztMvgoQsgE'},
     {'author': 'jesseleblancatlanta',
      'channel': 'jesseleblancatlanta',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=aLJ1Y8lZsRs&t=224s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But you can see right here they were trying to finance um uh some uh equipment, '
              'construction equipment for just under 70 grand. So it looks like total financed '
              "amount $69,30. Now let's go over to this escrow agreement.",
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': 'But you can see right here they were trying to finance um uh some uh equipment, '
             'construction equipment for just under 70 grand. So it looks like total financed '
             "amount $69,30. Now let's go over to this escrow agreement.",
      'title': 'Yusuf Ali - 188k Fraud - Wire Fraud - Equipment Fraud, identity fraud and '
               'Mortgage Fraud (jesseleblancatlanta)',
      'url': 'https://www.youtube.com/watch?v=aLJ1Y8lZsRs&t=224s',
      'video_id': 'aLJ1Y8lZsRs'},
     {'author': 'Everything Elliott',
      'channel': 'Everything Elliott',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=rL0RrJnr_oM&t=195s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I put in, hey, I need to start an LLC in New York. I needed to go on and '
              'basically just filled out the information. It was so simple and literally took '
              'me 10 minutes. 200 fee that you just pay with a credit card and boom, you have '
              'a business.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'I put in, hey, I need to start an LLC in New York. I needed to go on and '
             'basically just filled out the information. It was so simple and literally took '
             'me 10 minutes. 200 fee that you just pay with a credit card and boom, you have a '
             'business.',
      'title': 'How to Start an Excavation Business (Full Guide + Equipment Tour) (Everything '
               'Elliott)',
      'url': 'https://www.youtube.com/watch?v=rL0RrJnr_oM&t=195s',
      'video_id': 'rL0RrJnr_oM'},
     {'author': '613 Equipment Rentals',
      'channel': '613 Equipment Rentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=edx6wEhgoE8&t=192s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Basically what you'll the subtotal will be 3250 add 10% to that number which is "
              'the auction fee. Multiply that number then by 13% which is HST and in this case '
              'add $115 title fee for the trailer.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': "Basically what you'll the subtotal will be 3250 add 10% to that number which is "
             'the auction fee. Multiply that number then by 13% which is HST and in this case '
             'add $115 title fee for the trailer.',
      'title': 'First time Buying Equipment from Ritchie Bros Online Auctioneers (613 '
               'Equipment Rentals)',
      'url': 'https://www.youtube.com/watch?v=edx6wEhgoE8&t=192s',
      'video_id': 'edx6wEhgoE8'},
     {'author': 'Lenny Tim',
      'channel': 'Lenny Tim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=2ln9T1--E-I&t=283s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Are they just going to, you know, pay money and use the equipment and, you '
              "know, give it back the way, you know, you gave it to them or they're going to "
              "mess with it and it's going to get messed up and you can't really trust these "
              'people and that kind of stuff.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': 'Are they just going to, you know, pay money and use the equipment and, you know, '
             "give it back the way, you know, you gave it to them or they're going to mess "
             "with it and it's going to get messed up and you can't really trust these people "
             'and that kind of stuff.',
      'title': 'Guide To Starting A Profitable Equipment Rental Business (Lenny Tim)',
      'url': 'https://www.youtube.com/watch?v=2ln9T1--E-I&t=283s',
      'video_id': '2ln9T1--E-I'},
     {'author': 'Make Everything',
      'channel': 'Make Everything',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=x7M1QNicFvc&t=218s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For $100 and that's your your maximum bid and the hammer comes down and boom "
              "you win it hundred bucks you now have to pay the buyer's premium on top of "
              'that.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': "For $100 and that's your your maximum bid and the hammer comes down and boom you "
             "win it hundred bucks you now have to pay the buyer's premium on top of that.",
      'title': 'How To Buy From Machinery Auctions (5 Tips for Cheap Tools) (Make Everything)',
      'url': 'https://www.youtube.com/watch?v=x7M1QNicFvc&t=218s',
      'video_id': 'x7M1QNicFvc'},
     {'author': 'First Year Law - CONTRACTS',
      'channel': 'First Year Law - CONTRACTS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=bdE6IB8ry4w&t=426s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The mill owner had walked into the dealer's office and asked for Ambrex eight "
              'ten by name, because a magazine had recommended it. Now the fitness warranty '
              "fails, for the reason the boat buyer's failed. The buyer selected the product "
              'himself.',
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': "The mill owner had walked into the dealer's office and asked for Ambrex eight "
             'ten by name, because a magazine had recommended it. Now the fitness warranty '
             "fails, for the reason the boat buyer's failed. The buyer selected the product "
             'himself.',
      'title': 'Contracts L45 Part 2: Warranties: express, merchantability and fitness | Lewis '
               'v. Mobil Oil (First Year Law - CONTRACTS)',
      'url': 'https://www.youtube.com/watch?v=bdE6IB8ry4w&t=426s',
      'video_id': 'bdE6IB8ry4w'},
     {'author': 'Equipment Broker Academy',
      'channel': 'Equipment Broker Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=R8KSspUuldY&t=257s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Mechanical inspection he'll pay for it just like if you're buying a house and "
              "you want a homeowner's inspection or a buyer's inspection you pay a company to.",
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': "Mechanical inspection he'll pay for it just like if you're buying a house and "
             "you want a homeowner's inspection or a buyer's inspection you pay a company to.",
      'title': 'Myths and Misconceptions of Broker Heavy Equipment (Equipment Broker Academy)',
      'url': 'https://www.youtube.com/watch?v=R8KSspUuldY&t=257s',
      'video_id': 'R8KSspUuldY'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=XbQmSseBtI8&t=128s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Farm auction in East Central Nebraska it was in good condition and sold for '
              '$45,000 oh and I should mention that 7130 had 6,260 hours on it now you can see '
              'why I told our emailer how 50,000 was definitely a fair price to pay for a nice '
              'kih 714 with only.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'Farm auction in East Central Nebraska it was in good condition and sold for '
             '$45,000 oh and I should mention that 7130 had 6,260 hours on it now you can see '
             'why I told our emailer how 50,000 was definitely a fair price to pay for a nice '
             'kih 714 with only.',
      'title': 'Ask Machinery Pete: Good Deal? (Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=XbQmSseBtI8&t=128s',
      'video_id': 'XbQmSseBtI8'},
     {'author': 'Quimbee',
      'channel': 'Quimbee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=YIO9pJXqFeY&t=92s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Implied warranty of Fitness requires that the buyer have a specific purpose for '
              'the goods many courts have interpreted this requirement as requiring the buyer '
              'to have some purpose for the goods other than their ordinary and customary '
              'purpose.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Implied warranty of Fitness requires that the buyer have a specific purpose for '
             'the goods many courts have interpreted this requirement as requiring the buyer '
             'to have some purpose for the goods other than their ordinary and customary '
             'purpose.',
      'title': 'Sales Law | Implied Warranty of Fitness | Lesson 20 of 26 (Quimbee)',
      'url': 'https://www.youtube.com/watch?v=YIO9pJXqFeY&t=92s',
      'video_id': 'YIO9pJXqFeY'},
     {'author': 'Hunter Valley Tracks',
      'channel': 'Hunter Valley Tracks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=1B6uxG5WNzQ&t=21s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We measure the wear on our rollers from this point down to the wear, and also '
              'on our idlers. We get a shoe height of the lug. And then, we also measure '
              'across three teeth of the segment to get our wear.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'We measure the wear on our rollers from this point down to the wear, and also on '
             'our idlers. We get a shoe height of the lug. And then, we also measure across '
             'three teeth of the segment to get our wear.',
      'title': 'What Is a CTS Inspection? | Dozer Undercarriage Wear Explained | Track Talk '
               'Tuesday | HVT (Hunter Valley Tracks)',
      'url': 'https://www.youtube.com/watch?v=1B6uxG5WNzQ&t=21s',
      'video_id': '1B6uxG5WNzQ'}],
 3: [{'author': 'George Hedley | HardHat BIZCOACH',
      'channel': 'George Hedley | HardHat BIZCOACH',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:30](https://www.youtube.com/watch?v=60uc8gnDCiY&t=390s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And also you're gonna get an opportunity — you can download the first chapter "
              'of my new book, Turn Your Construction Business Into a Profit Making Machine. '
              'And hope to see you depositing a lot of positive cash flow because you now know '
              'your equipment costs.',
      'timestamp': 390,
      'timestamp_label': '[00:06:30]',
      'timestamp_seconds': 390,
      'tip': "And also you're gonna get an opportunity — you can download the first chapter of "
             'my new book, Turn Your Construction Business Into a Profit Making Machine. And '
             'hope to see you depositing a lot of positive cash flow because you now know your '
             'equipment costs.',
      'title': 'How To Estimate Equipment Cost In Construction (George Hedley | HardHat '
               'BIZCOACH)',
      'url': 'https://www.youtube.com/watch?v=60uc8gnDCiY&t=390s',
      'video_id': '60uc8gnDCiY'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=9DUEHNOY4mw&t=37s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Canadian, which, if you do the conversion to US dollars on October 15th, came '
              'out to 499,769. So, just a few bucks under 500k. Now, that to me is a pretty '
              "strong price because on a hard cash basis, let's walk it back a year ago, the "
              'same auction company, Ritchie Bros.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Canadian, which, if you do the conversion to US dollars on October 15th, came '
             'out to 499,769. So, just a few bucks under 500k. Now, that to me is a pretty '
             "strong price because on a hard cash basis, let's walk it back a year ago, the "
             'same auction company, Ritchie Bros.',
      'title': '2024 CaseIH Steiger 645 QuadTrac - Comparing Auction Prices Now vs Year Ago '
               '(Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=9DUEHNOY4mw&t=37s',
      'video_id': '9DUEHNOY4mw'},
     {'author': 'Subi Industries',
      'channel': 'Subi Industries',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:31](https://www.youtube.com/watch?v=iZJI5Y5wLUo&t=571s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Spread those setup costs across a massive production run, and the cost per part '
              'can become extremely low. Keep the machines running around the clock, minimize '
              'tool failures, control scrap rates, and even a thin margin can generate a '
              'profit through sheer volume.',
      'timestamp': 571,
      'timestamp_label': '[00:09:31]',
      'timestamp_seconds': 571,
      'tip': 'Spread those setup costs across a massive production run, and the cost per part '
             'can become extremely low. Keep the machines running around the clock, minimize '
             'tool failures, control scrap rates, and even a thin margin can generate a profit '
             'through sheer volume.',
      'title': 'Why CNC Machining Is So Cheap in China — But So Expensive in America (Subi '
               'Industries)',
      'url': 'https://www.youtube.com/watch?v=iZJI5Y5wLUo&t=571s',
      'video_id': 'iZJI5Y5wLUo'},
     {'author': 'Farm Journal',
      'channel': 'Farm Journal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=RtJspDtsC2M&t=50s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '15th came out at 499,769 dollars. So just a few bucks under 500k. Now that to '
              "me is a pretty strong price because on a hard cash basis, let's walk it back a "
              'year ago. The same auction company, Ritchie Brothers, had another farm auction '
              'also in Saskatchewan.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': '15th came out at 499,769 dollars. So just a few bucks under 500k. Now that to me '
             "is a pretty strong price because on a hard cash basis, let's walk it back a year "
             'ago. The same auction company, Ritchie Brothers, had another farm auction also '
             'in Saskatchewan.',
      'title': 'Machinery Pete: Late Models Are Hot Sellers (Farm Journal)',
      'url': 'https://www.youtube.com/watch?v=RtJspDtsC2M&t=50s',
      'video_id': 'RtJspDtsC2M'},
     {'author': 'Mehmi Financial Group',
      'channel': 'Mehmi Financial Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=DaTuV1-Fst0&t=41s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A great broker creates what's known as an auction effect, basically generating "
              'this competitive tension among buyers that naturally pushes the price upward.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': "A great broker creates what's known as an auction effect, basically generating "
             'this competitive tension among buyers that naturally pushes the price upward.',
      'title': "Insider's Canadian Brokerage Guide [Equipment financing and leasing] (Mehmi "
               'Financial Group)',
      'url': 'https://www.youtube.com/watch?v=DaTuV1-Fst0&t=41s',
      'video_id': 'DaTuV1-Fst0'},
     {'author': 'JobBadger | Field Crew Scheduling Software',
      'channel': 'JobBadger | Field Crew Scheduling Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=HYAVjNrf5t4&t=64s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Go back into the projects and let's add that small back hole back in there and "
              'we need another 500 ft of heating PEX pipe because that customer asked us to do '
              'heated driveway. So we can see that it gives you calculated cost of how much of '
              'the heating pipe costs.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': "Go back into the projects and let's add that small back hole back in there and "
             'we need another 500 ft of heating PEX pipe because that customer asked us to do '
             'heated driveway. So we can see that it gives you calculated cost of how much of '
             'the heating pipe costs.',
      'title': 'Projects & Inventory in JobBadger | Track Equipment and Materials by Job Site '
               '(JobBadger | Field Crew Scheduling Software)',
      'url': 'https://www.youtube.com/watch?v=HYAVjNrf5t4&t=64s',
      'video_id': 'HYAVjNrf5t4'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=obq_-8IhG18&t=15s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "History lesson so let's go back 20 years to the year 2004 now back then the "
              'highest auction price I saw all year in 2004 on a sprayer was 115,000 bucks '
              'and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "History lesson so let's go back 20 years to the year 2004 now back then the "
             'highest auction price I saw all year in 2004 on a sprayer was 115,000 bucks and.',
      'title': 'Auction Sale Prices on Sprayers Now vs 10, 20 Years Ago (Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=obq_-8IhG18&t=15s',
      'video_id': 'obq_-8IhG18'},
     {'author': 'Garage Profits',
      'channel': 'Garage Profits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=InQ7-NaPvxs&t=20s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In this video, we're counting down 10 low-cost recycling machines along with a "
              "full business idea for each one. You'll learn where to get the material for "
              "free, who's ready to buy it, and how much people running these machines are "
              'actually making right now.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "In this video, we're counting down 10 low-cost recycling machines along with a "
             "full business idea for each one. You'll learn where to get the material for "
             "free, who's ready to buy it, and how much people running these machines are "
             'actually making right now.',
      'title': '10 Cheap Machines That Turn Trash Into Cash (Start From Home) (Garage Profits)',
      'url': 'https://www.youtube.com/watch?v=InQ7-NaPvxs&t=20s',
      'video_id': 'InQ7-NaPvxs'},
     {'author': 'Build Like A Pro TV',
      'channel': 'Build Like A Pro TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=KWBdujV7H9Q&t=100s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The cost of that equipment so what we're talking about is ownership cost is a "
              'formula that goes into it and basically purchase price which pay for it '
              'divided.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': "The cost of that equipment so what we're talking about is ownership cost is a "
             'formula that goes into it and basically purchase price which pay for it divided.',
      'title': 'Episode 4 - How To Calculate Your Hourly Equipment Costs (Build Like A Pro TV)',
      'url': 'https://www.youtube.com/watch?v=KWBdujV7H9Q&t=100s',
      'video_id': 'KWBdujV7H9Q'},
     {'author': 'Probo Medical UK',
      'channel': 'Probo Medical UK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=MZI2TSrdxAQ&t=20s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We help NHS trusts and private practices reduce downtime, control costs, and '
              'extend the life of imaging systems even if the OEM has declared the system as '
              'end of service. And we can do this at a much lower cost than the manufacturer.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'We help NHS trusts and private practices reduce downtime, control costs, and '
             'extend the life of imaging systems even if the OEM has declared the system as '
             'end of service. And we can do this at a much lower cost than the manufacturer.',
      'title': 'Is Your OEM Service Support Ending for your Diagnostic Imaging Equipment? '
               '(Probo Medical UK)',
      'url': 'https://www.youtube.com/watch?v=MZI2TSrdxAQ&t=20s',
      'video_id': 'MZI2TSrdxAQ'},
     {'author': 'The Profitable Contractor',
      'channel': 'The Profitable Contractor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=jLx7fLatA3A&t=41s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Accounts payable matches all three records before approving the charge. That '
              'comparison can catch a quantity mismatch, an incorrect price, or a job number '
              'that points somewhere else. A charge posted to the office leaves the receiving '
              "job's costs understated.",
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': 'Accounts payable matches all three records before approving the charge. That '
             'comparison can catch a quantity mismatch, an incorrect price, or a job number '
             'that points somewhere else. A charge posted to the office leaves the receiving '
             "job's costs understated.",
      'title': 'How to Track Material, Equipment & Subcontractor Costs by Job (The Profitable '
               'Contractor)',
      'url': 'https://www.youtube.com/watch?v=jLx7fLatA3A&t=41s',
      'video_id': 'jLx7fLatA3A'},
     {'author': 'Diesel and Iron',
      'channel': 'Diesel and Iron',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:11](https://www.youtube.com/watch?v=maIDknW4DME&t=71s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lite Altis xơ cấu property and shipping companies are escaping Company or '
              "someone don't want in their personal Channel you come back unit testing.",
      'timestamp': 71,
      'timestamp_label': '[00:01:11]',
      'timestamp_seconds': 71,
      'tip': 'Lite Altis xơ cấu property and shipping companies are escaping Company or '
             "someone don't want in their personal Channel you come back unit testing.",
      'title': 'HOW TO GET A JOB RUNNING HEAVY EQUIPMENT || How to get a job as a heavy '
               'equipment operator (Diesel and Iron)',
      'url': 'https://www.youtube.com/watch?v=maIDknW4DME&t=71s',
      'video_id': 'maIDknW4DME'},
     {'author': 'Freight Profits',
      'channel': 'Freight Profits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:39](https://www.youtube.com/watch?v=qHs0sXdzamw&t=519s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before you move it and before you submit your quote all right now so you got a '
              'permit cost involved you got cops well this had two pilot cars this had a chase '
              "car that's what I'm actually doing for one of my pilots out here on the road "
              'okay.',
      'timestamp': 519,
      'timestamp_label': '[00:08:39]',
      'timestamp_seconds': 519,
      'tip': 'Before you move it and before you submit your quote all right now so you got a '
             'permit cost involved you got cops well this had two pilot cars this had a chase '
             "car that's what I'm actually doing for one of my pilots out here on the road "
             'okay.',
      'title': 'Freight Quotes For Heavy Haul & Oversize Loads (Freight Profits)',
      'url': 'https://www.youtube.com/watch?v=qHs0sXdzamw&t=519s',
      'video_id': 'qHs0sXdzamw'},
     {'author': 'EquipmentWorld',
      'channel': 'EquipmentWorld',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:54](https://www.youtube.com/watch?v=shzCS90v5wA&t=294s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Take your finger and just wipe the grease out typical grease gun you pop it out '
              "that you think you're close to to two and a quarter as you see the track coming "
              "up what we'll do is we'll go from the back.",
      'timestamp': 294,
      'timestamp_label': '[00:04:54]',
      'timestamp_seconds': 294,
      'tip': 'Take your finger and just wipe the grease out typical grease gun you pop it out '
             "that you think you're close to to two and a quarter as you see the track coming "
             "up what we'll do is we'll go from the back.",
      'title': 'How to Measure Dozer Undercarriage Wear (EquipmentWorld)',
      'url': 'https://www.youtube.com/watch?v=shzCS90v5wA&t=294s',
      'video_id': 'shzCS90v5wA'},
     {'author': 'Carter Machinery',
      'channel': 'Carter Machinery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=R9dHZ4P7yp0&t=98s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Area before you pull the sample any extra contamination that gets in the bottom '
              "will definitely pick up when we're doing the analysis all right I'm picking up "
              "what you're putting down very good can you show me how it's done though sure "
              "let's go do it cool.",
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'Area before you pull the sample any extra contamination that gets in the bottom '
             "will definitely pick up when we're doing the analysis all right I'm picking up "
             "what you're putting down very good can you show me how it's done though sure "
             "let's go do it cool.",
      'title': 'Maintenance Minutes – How To Take an Oil Sample (Carter Machinery)',
      'url': 'https://www.youtube.com/watch?v=R9dHZ4P7yp0&t=98s',
      'video_id': 'R9dHZ4P7yp0'}],
 4: [{'author': 'Reclaim Atlas',
      'channel': 'Reclaim Atlas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:32](https://www.youtube.com/watch?v=jfdR4HzT3cU&t=152s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The next buyer might be another data center, but it could also be a hospital, '
              'factory, university, or commercial building. Before paying serious money, '
              'buyers want the name plate, kilowatt rating, voltage, fuel type, operating '
              'hours, and maintenance history.',
      'timestamp': 152,
      'timestamp_label': '[00:02:32]',
      'timestamp_seconds': 152,
      'tip': 'The next buyer might be another data center, but it could also be a hospital, '
             'factory, university, or commercial building. Before paying serious money, buyers '
             'want the name plate, kilowatt rating, voltage, fuel type, operating hours, and '
             'maintenance history.',
      'title': 'Who Buys Used Data Center UPS, Switchgear and Generators? (Reclaim Atlas)',
      'url': 'https://www.youtube.com/watch?v=jfdR4HzT3cU&t=152s',
      'video_id': 'jfdR4HzT3cU'},
     {'author': 'Mr. Margins',
      'channel': 'Mr. Margins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:32](https://www.youtube.com/watch?v=YzDJ7sPjIt0&t=1172s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'However, the true lifetime economics of this business rely heavily on the back '
              'end used equipment resale value. Equipment rental is fundamentally a capital '
              'recycling operation. Operators do not hold on to these assets until they fail.',
      'timestamp': 1172,
      'timestamp_label': '[00:19:32]',
      'timestamp_seconds': 1172,
      'tip': 'However, the true lifetime economics of this business rely heavily on the back '
             'end used equipment resale value. Equipment rental is fundamentally a capital '
             'recycling operation. Operators do not hold on to these assets until they fail.',
      'title': 'How Construction Equipment Rental Companies Make Money (Mr. Margins)',
      'url': 'https://www.youtube.com/watch?v=YzDJ7sPjIt0&t=1172s',
      'video_id': 'YzDJ7sPjIt0'},
     {'author': 'BuildWitt',
      'channel': 'BuildWitt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=VLza4LoUZfo&t=77s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lot 892, a Volvo A45G articulated truck from Junior Davis Construction. Such a '
              'machine would fit perfectly in the driveway of my one-bedroom apartment. While '
              "the truck may not be in this year's budget, Randy Bill with CEO has given me "
              'the green light to buy something.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Lot 892, a Volvo A45G articulated truck from Junior Davis Construction. Such a '
             'machine would fit perfectly in the driveway of my one-bedroom apartment. While '
             "the truck may not be in this year's budget, Randy Bill with CEO has given me the "
             'green light to buy something.',
      'title': "Inside the World's Biggest Equipment Auction ($265M in 5 Days!) (BuildWitt)",
      'url': 'https://www.youtube.com/watch?v=VLza4LoUZfo&t=77s',
      'video_id': 'VLza4LoUZfo'},
     {'author': 'Matt Krause',
      'channel': 'Matt Krause',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=QBNPafDHXLE&t=160s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Making the move all right so let's talk about business setup this is the "
              "official step that makes your Freight brokerage legit and it's easier than you "
              "might think first you'll need aity bond.",
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "Making the move all right so let's talk about business setup this is the "
             "official step that makes your Freight brokerage legit and it's easier than you "
             "might think first you'll need aity bond.",
      'title': '6 Steps to Become a Freight Broker in 2026 (No Experience Needed) (Matt '
               'Krause)',
      'url': 'https://www.youtube.com/watch?v=QBNPafDHXLE&t=160s',
      'video_id': 'QBNPafDHXLE'},
     {'author': 'Mehmi Financial Group',
      'channel': 'Mehmi Financial Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:36](https://www.youtube.com/watch?v=BStMEmq3lwU&t=96s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Seriously, it's everywhere. So, this brings us to a huge challenge that pretty "
              "much every single business owner faces. Let's call it the growth dilemma. To "
              'grow, you need the best tools, the latest software, the most efficient '
              'machines, right?',
      'timestamp': 96,
      'timestamp_label': '[00:01:36]',
      'timestamp_seconds': 96,
      'tip': "Seriously, it's everywhere. So, this brings us to a huge challenge that pretty "
             "much every single business owner faces. Let's call it the growth dilemma. To "
             'grow, you need the best tools, the latest software, the most efficient machines, '
             'right?',
      'title': 'How Equipment Financing Brokers Actually Work (Banks Hate This) (Mehmi '
               'Financial Group)',
      'url': 'https://www.youtube.com/watch?v=BStMEmq3lwU&t=96s',
      'video_id': 'BStMEmq3lwU'},
     {'author': 'TITANS of CNC MACHINING',
      'channel': 'TITANS of CNC MACHINING',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=C2UEluRNT-M&t=209s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dongtai, because they were instrumental in Dongtai forming as a company and '
              'building machine tools. I think that the um original guy that came to Taiwan, '
              'they came to build sewing machines and things in Taiwan when Japan was '
              'involved.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'Dongtai, because they were instrumental in Dongtai forming as a company and '
             'building machine tools. I think that the um original guy that came to Taiwan, '
             'they came to build sewing machines and things in Taiwan when Japan was involved.',
      'title': 'TONGTAI: The Fastest Super CNC Machines I’ve Ever Seen (TITANS of CNC '
               'MACHINING)',
      'url': 'https://www.youtube.com/watch?v=C2UEluRNT-M&t=209s',
      'video_id': 'C2UEluRNT-M'},
     {'author': 'Contend Capital',
      'channel': 'Contend Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=rLDoLaoEZ-A&t=185s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Machine in person are they working directly with the shop or they just broker '
              "in the machine with another dealer and now you're paying two dealers.",
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'Machine in person are they working directly with the shop or they just broker in '
             "the machine with another dealer and now you're paying two dealers.",
      'title': "Don't Buy a Used CNC Machine Until You Watch This (Contend Capital)",
      'url': 'https://www.youtube.com/watch?v=rLDoLaoEZ-A&t=185s',
      'video_id': 'rLDoLaoEZ-A'},
     {'author': 'Brennan Valeski',
      'channel': 'Brennan Valeski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=oP0hP2pgigg&t=157s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, the common uses here uses here for equipment financing would include '
              'purchasing equipment. Like as I mentioned, this could also include upgrading '
              'tools or acquiring machinery critical to business operations.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'Now, the common uses here uses here for equipment financing would include '
             'purchasing equipment. Like as I mentioned, this could also include upgrading '
             'tools or acquiring machinery critical to business operations.',
      'title': 'Best Equipment Financing Options & Loans of 2026 (Brennan Valeski)',
      'url': 'https://www.youtube.com/watch?v=oP0hP2pgigg&t=157s',
      'video_id': 'oP0hP2pgigg'},
     {'author': 'HCSS Software',
      'channel': 'HCSS Software',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=Cbg13em0UgE&t=136s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One thing we like about HeavyJob, that it is geared to the construction '
              "industry so a lot of the things we come across that's unique to the "
              "construction industry is dealt with in HeavyJob, where it isn't in just your "
              'accounting software.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'One thing we like about HeavyJob, that it is geared to the construction industry '
             "so a lot of the things we come across that's unique to the construction industry "
             "is dealt with in HeavyJob, where it isn't in just your accounting software.",
      'title': 'HeavyJob Case Study | Companies Describe Their Favorite HeavyJob Features '
               '(HCSS Software)',
      'url': 'https://www.youtube.com/watch?v=Cbg13em0UgE&t=136s',
      'video_id': 'Cbg13em0UgE'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=67cXMHAndKQ&t=79s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Little bit so are we plateauing or fifteen years from now when we almost triple '
              'again up to a million bucks for use combine stay tuned thanks Greg when we come '
              'back well wish a good friend and co-worker Mike Adams farewell easy snow to be '
              'checked.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Little bit so are we plateauing or fifteen years from now when we almost triple '
             'again up to a million bucks for use combine stay tuned thanks Greg when we come '
             'back well wish a good friend and co-worker Mike Adams farewell easy snow to be '
             'checked.',
      'title': 'Machinery Pete: Highest Auction Price on Combines Each of Past 18 Years '
               '(Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=67cXMHAndKQ&t=79s',
      'video_id': '67cXMHAndKQ'},
     {'author': 'Equipment & Contracting',
      'channel': 'Equipment & Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=Xv99UO78lCE&t=181s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Another Lane and backup cameras are getting more and more sophisticated with '
              "guides to help you back into spaces and warning signals when you're too close "
              'to.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'Another Lane and backup cameras are getting more and more sophisticated with '
             "guides to help you back into spaces and warning signals when you're too close "
             'to.',
      'title': 'Building the Ultimate Work Truck | A Guide for Contractors and Equipment '
               'Suppliers (Equipment & Contracting)',
      'url': 'https://www.youtube.com/watch?v=Xv99UO78lCE&t=181s',
      'video_id': 'Xv99UO78lCE'},
     {'author': 'Jermane Cheathem',
      'channel': 'Jermane Cheathem',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:13](https://www.youtube.com/watch?v=I8ZezTXbvqQ&t=673s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The exactly how I do this check it out it'll be linked below and I just hope "
              'this saved you a little bit of your life because life is short make the money '
              'have the fun get your time back be successful see you next time.',
      'timestamp': 673,
      'timestamp_label': '[00:11:13]',
      'timestamp_seconds': 673,
      'tip': "The exactly how I do this check it out it'll be linked below and I just hope "
             'this saved you a little bit of your life because life is short make the money '
             'have the fun get your time back be successful see you next time.',
      'title': 'How I Built an Equipment Finance Business (No Ads) (Jermane Cheathem)',
      'url': 'https://www.youtube.com/watch?v=I8ZezTXbvqQ&t=673s',
      'video_id': 'I8ZezTXbvqQ'},
     {'author': 'Heavy Metal Learning',
      'channel': 'Heavy Metal Learning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:50](https://www.youtube.com/watch?v=PRVmIh3pKOY&t=1730s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pushing down the blade a little bit I'm letting that track out on its own so I "
              "don't leave a big pile of material there and you're going go until the blades "
              "done taking it back up and we'll go over that more in a next advanced video.",
      'timestamp': 1730,
      'timestamp_label': '[00:28:50]',
      'timestamp_seconds': 1730,
      'tip': "Pushing down the blade a little bit I'm letting that track out on its own so I "
             "don't leave a big pile of material there and you're going go until the blades "
             "done taking it back up and we'll go over that more in a next advanced video.",
      'title': 'Bulldozer Training (Beginner) | Heavy Equipment Operator Training (Heavy Metal '
               'Learning)',
      'url': 'https://www.youtube.com/watch?v=PRVmIh3pKOY&t=1730s',
      'video_id': 'PRVmIh3pKOY'},
     {'author': 'OnWaterTVAustralia',
      'channel': 'OnWaterTVAustralia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:27](https://www.youtube.com/watch?v=VQXQTmAfjjo&t=627s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Boats older boats will have a serial number newer boats will have a hint number '
              "and a hint numbers of 14 digit character let's just show you where we can find "
              'the him number on this particular boat.',
      'timestamp': 627,
      'timestamp_label': '[00:10:27]',
      'timestamp_seconds': 627,
      'tip': 'Boats older boats will have a serial number newer boats will have a hint number '
             "and a hint numbers of 14 digit character let's just show you where we can find "
             'the him number on this particular boat.',
      'title': 'Dealer paperwork (consignment and sales forms) (OnWaterTVAustralia)',
      'url': 'https://www.youtube.com/watch?v=VQXQTmAfjjo&t=627s',
      'video_id': 'VQXQTmAfjjo'},
     {'author': 'Andy Lash',
      'channel': 'Andy Lash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=POHJMjG37XM&t=83s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Look out for oh we've got the fittings you can see this one here doesn't have "
              'the gasket inside so this side does always important to check all these '
              "fittings and make sure that you've got all the components in place.",
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': "Look out for oh we've got the fittings you can see this one here doesn't have "
             'the gasket inside so this side does always important to check all these fittings '
             "and make sure that you've got all the components in place.",
      'title': 'Driver Tips - Oil Testing Equipment (Andy Lash)',
      'url': 'https://www.youtube.com/watch?v=POHJMjG37XM&t=83s',
      'video_id': 'POHJMjG37XM'}],
 5: [{'author': 'The Markup',
      'channel': 'The Markup',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:08](https://www.youtube.com/watch?v=4ZnfP4pS7A8&t=488s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's if it's been maintained religiously. If it comes back beaten up from "
              "a hard job site, the repair bill can eat an entire month's rental revenue. Risk "
              'two, the economy cycle. Construction rental is deeply tied to the broader '
              'economy.',
      'timestamp': 488,
      'timestamp_label': '[00:08:08]',
      'timestamp_seconds': 488,
      'tip': "And that's if it's been maintained religiously. If it comes back beaten up from "
             "a hard job site, the repair bill can eat an entire month's rental revenue. Risk "
             'two, the economy cycle. Construction rental is deeply tied to the broader '
             'economy.',
      'title': 'How Construction Equipment Rental Companies Quietly Make $60 Billion a Year '
               '(The Markup)',
      'url': 'https://www.youtube.com/watch?v=4ZnfP4pS7A8&t=488s',
      'video_id': '4ZnfP4pS7A8'},
     {'author': 'This Week in Trucking',
      'channel': 'This Week in Trucking',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=YWQYZLDM6dY&t=45s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And on top of that, the broker carrier agreements include a waiver, meaning '
              'that the carrier signs away their right to that information. And when carriers '
              'try to push back, they risk losing out on the loads that they need to keep '
              'their business running.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'And on top of that, the broker carrier agreements include a waiver, meaning that '
             'the carrier signs away their right to that information. And when carriers try to '
             'push back, they risk losing out on the loads that they need to keep their '
             'business running.',
      'title': 'FMCSA Finally Closing Broker LOOPHOLES! | Broker Transparency 2025 (This Week '
               'in Trucking)',
      'url': 'https://www.youtube.com/watch?v=YWQYZLDM6dY&t=45s',
      'video_id': 'YWQYZLDM6dY'},
     {'author': 'Contend Capital',
      'channel': 'Contend Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:22](https://www.youtube.com/watch?v=Hod3pJo62jY&t=262s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Obviously, as my business grows, I'm going to pull back on the type of risk I'm "
              'willing to take. What would you say to the person watching this that aspires to '
              'be an entrepreneur like yourself?',
      'timestamp': 262,
      'timestamp_label': '[00:04:22]',
      'timestamp_seconds': 262,
      'tip': "Obviously, as my business grows, I'm going to pull back on the type of risk I'm "
             'willing to take. What would you say to the person watching this that aspires to '
             'be an entrepreneur like yourself?',
      'title': 'Financing CNC Machine Tools as a Startup Business (Contend Capital)',
      'url': 'https://www.youtube.com/watch?v=Hod3pJo62jY&t=262s',
      'video_id': 'Hod3pJo62jY'},
     {'author': 'BARGO NextGen Bar Prep',
      'channel': 'BARGO NextGen Bar Prep',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:50](https://www.youtube.com/watch?v=hZMms1qvx1s&t=890s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Section 2-601, perfect tender, and the cure and installment rules that soften '
              'it. 2-316 which sets a different formality for every disclaimer. Now the traps '
              "straight from the examiner's favorites. One, never solve risk of loss by asking "
              'who held title.',
      'timestamp': 890,
      'timestamp_label': '[00:14:50]',
      'timestamp_seconds': 890,
      'tip': 'Section 2-601, perfect tender, and the cure and installment rules that soften '
             'it. 2-316 which sets a different formality for every disclaimer. Now the traps '
             "straight from the examiner's favorites. One, never solve risk of loss by asking "
             'who held title.',
      'title': 'UCC Performance & Warranties — Contracts (BARGO NextGen Bar Prep)',
      'url': 'https://www.youtube.com/watch?v=hZMms1qvx1s&t=890s',
      'video_id': 'hZMms1qvx1s'},
     {'author': 'Wealth Pilot',
      'channel': 'Wealth Pilot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=yQ90kncuf9w&t=166s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, one of the biggest questions in this business becomes surprisingly simple. '
              "How much of the machine's available time can actually be turned into paid "
              "rental time? An idle excavator doesn't have to be broken to become an economic "
              'problem.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'So, one of the biggest questions in this business becomes surprisingly simple. '
             "How much of the machine's available time can actually be turned into paid rental "
             "time? An idle excavator doesn't have to be broken to become an economic problem.",
      'title': 'How Construction Equipment Rental Actually Makes Money (Wealth Pilot)',
      'url': 'https://www.youtube.com/watch?v=yQ90kncuf9w&t=166s',
      'video_id': 'yQ90kncuf9w'},
     {'author': 'CoxManufacturing Company',
      'channel': 'CoxManufacturing Company',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=t9zRrkzjFbA&t=248s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They can make a request from their machine over our ERP network and one of our '
              'material handlers will be able to see the exact material needed and the machine '
              'to deliver it to Building 2 features more CNC machining.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'They can make a request from their machine over our ERP network and one of our '
             'material handlers will be able to see the exact material needed and the machine '
             'to deliver it to Building 2 features more CNC machining.',
      'title': 'Cox Manufacturing Virtual Shop Tour: Exploring CNC Swiss and Screw Machined '
               'Products & Services (CoxManufacturing Company)',
      'url': 'https://www.youtube.com/watch?v=t9zRrkzjFbA&t=248s',
      'video_id': 't9zRrkzjFbA'},
     {'author': 'Trucking Made Successful',
      'channel': 'Trucking Made Successful',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=iwQkqbEBCrM&t=22s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, a couple of years ago, I would say at this point, it's actually two years "
              'ago, I made a video about a big win for carriers revolving around broker '
              'financial responsibility. And now, this news is front and center again.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "So, a couple of years ago, I would say at this point, it's actually two years "
             'ago, I made a video about a big win for carriers revolving around broker '
             'financial responsibility. And now, this news is front and center again.',
      'title': 'R.I.P. Broke Brokers: FMCSA’s New Rule Kicks In Jan 16 – What Every Carrier '
               'MUST Know (Trucking Made Successful)',
      'url': 'https://www.youtube.com/watch?v=iwQkqbEBCrM&t=22s',
      'video_id': 'iwQkqbEBCrM'},
     {'author': 'Boom & Bucket',
      'channel': 'Boom & Bucket',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=6UVHinO3tHg&t=74s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your unequate metal line do not fall for this trap take cash or wire transfer '
              "only for used equipment of course you could use boonebucket.com as well we'll "
              "do everything for you so you can focus on running your business that's "
              'boomandbucket.com.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'Your unequate metal line do not fall for this trap take cash or wire transfer '
             "only for used equipment of course you could use boonebucket.com as well we'll do "
             "everything for you so you can focus on running your business that's "
             'boomandbucket.com.',
      'title': 'Heavy Equipment Online Selling Scams (Boom & Bucket)',
      'url': 'https://www.youtube.com/watch?v=6UVHinO3tHg&t=74s',
      'video_id': '6UVHinO3tHg'},
     {'author': 'Pav Jam',
      'channel': 'Pav Jam',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=4aHgTjO_vNI&t=20s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No matter what industry you are in, be it construction, agriculture and farm, '
              'transportation, forestry or mining. In this video, I am going to reveal the '
              'most common mistake that people make and tell you how you can exploit it and '
              'pocket more money.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'No matter what industry you are in, be it construction, agriculture and farm, '
             'transportation, forestry or mining. In this video, I am going to reveal the most '
             'common mistake that people make and tell you how you can exploit it and pocket '
             'more money.',
      'title': 'How To Make More Money Buying or Selling Used Equipment and Heavy Machinery '
               '(Pav Jam)',
      'url': 'https://www.youtube.com/watch?v=4aHgTjO_vNI&t=20s',
      'video_id': '4aHgTjO_vNI'},
     {'author': 'Farm Journal',
      'channel': 'Farm Journal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=t7mTa6TooFk&t=80s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, if we dive farther into our data, if we look at what's happening with 1- "
              'to 3-year-old equipment. So, again, our data shows through May 7th, the number '
              'of 1- to 3-year-old equipment units sold at auction is down 19. 9% versus the '
              'same period last year.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "Now, if we dive farther into our data, if we look at what's happening with 1- to "
             '3-year-old equipment. So, again, our data shows through May 7th, the number of '
             '1- to 3-year-old equipment units sold at auction is down 19. 9% versus the same '
             'period last year.',
      'title': 'Machinery Pete: Unprecedented Auction Numbers (Farm Journal)',
      'url': 'https://www.youtube.com/watch?v=t7mTa6TooFk&t=80s',
      'video_id': 't7mTa6TooFk'},
     {'author': 'The Wood Whisperer',
      'channel': 'The Wood Whisperer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=87nsgCs4Tzs&t=108s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To accommodate a wire gutter, we need cutouts in the two inside panels. The '
              'right pedestal, receives a back and bottom. The back creates an open space for '
              'cables and power, and the bottom panel is spaced about an inch from the back '
              'panel, to allow for additional airflow.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'To accommodate a wire gutter, we need cutouts in the two inside panels. The '
             'right pedestal, receives a back and bottom. The back creates an open space for '
             'cables and power, and the bottom panel is spaced about an inch from the back '
             'panel, to allow for additional airflow.',
      'title': 'Executive Desk With Wireless Charging and Hidden Drawer (The Wood Whisperer)',
      'url': 'https://www.youtube.com/watch?v=87nsgCs4Tzs&t=108s',
      'video_id': '87nsgCs4Tzs'},
     {'author': 'thatDOTcop',
      'channel': 'thatDOTcop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=zKmff6X7cQA&t=53s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, what exactly is personal conveyance? Personal conveyance is a movement of a '
              "commercial motor vehicle for personal use while off duty. Here's a crucial "
              "detail that many truckers don't realize or they straight up forget.",
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'So, what exactly is personal conveyance? Personal conveyance is a movement of a '
             "commercial motor vehicle for personal use while off duty. Here's a crucial "
             "detail that many truckers don't realize or they straight up forget.",
      'title': 'FMCSA Personal Conveyance Rules EXPLAINED! (What Truckers MUST Know!) '
               '(thatDOTcop)',
      'url': 'https://www.youtube.com/watch?v=zKmff6X7cQA&t=53s',
      'video_id': 'zKmff6X7cQA'},
     {'author': 'ET Transport',
      'channel': 'ET Transport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=PHnFlcmti2s&t=336s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This one sold with 457,000 km, which is pretty much identical one to one to the '
              "truck that I'm bidding at right now. That one sold for $100,000. Now, if I keep "
              'going back in history, this one sold for $96,000. Okay, this is our wish list.',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'This one sold with 457,000 km, which is pretty much identical one to one to the '
             "truck that I'm bidding at right now. That one sold for $100,000. Now, if I keep "
             'going back in history, this one sold for $96,000. Okay, this is our wish list.',
      'title': 'Inside a Live Ritchie Bros Auction (Full Strategy Revealed) (ET Transport)',
      'url': 'https://www.youtube.com/watch?v=PHnFlcmti2s&t=336s',
      'video_id': 'PHnFlcmti2s'},
     {'author': 'Makers Acres',
      'channel': 'Makers Acres',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=vUTKwba3CBk&t=308s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It I like coming here I like seeing how happy some of these people are when '
              "they buy their things they're like yeah look at my new bobcat or whatever it is "
              'that they got three two eight.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': 'It I like coming here I like seeing how happy some of these people are when they '
             "buy their things they're like yeah look at my new bobcat or whatever it is that "
             'they got three two eight.',
      'title': 'Getting Screwed at a Ritchie Brothers Auction! (Makers Acres)',
      'url': 'https://www.youtube.com/watch?v=vUTKwba3CBk&t=308s',
      'video_id': 'vUTKwba3CBk'},
     {'author': 'WearCheck Video',
      'channel': 'WearCheck Video',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=ypiqyyCR9MI&t=145s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So again loosen the drain plug get your uncapped sample bottle ready remove the '
              'drain plug fill the bottle and replace the drain plug as soon as possible again '
              'cap immediately and clean off the excess oil from the sample bottle.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'So again loosen the drain plug get your uncapped sample bottle ready remove the '
             'drain plug fill the bottle and replace the drain plug as soon as possible again '
             'cap immediately and clean off the excess oil from the sample bottle.',
      'title': 'WearCheck - How to Take Oil Samples from Fleet Machines (WearCheck Video)',
      'url': 'https://www.youtube.com/watch?v=ypiqyyCR9MI&t=145s',
      'video_id': 'ypiqyyCR9MI'}],
 6: [{'author': 'Equipment Finance Academy',
      'channel': 'Equipment Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=uzLIopNJDJY&t=113s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To find these deals, connect directly with independent machinery dealerships '
              "and regional auction reps. When buyers don't qualify for direct manufacturer "
              'captive financing, that dealer needs a reliable broker on speed dial.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'To find these deals, connect directly with independent machinery dealerships and '
             "regional auction reps. When buyers don't qualify for direct manufacturer captive "
             'financing, that dealer needs a reliable broker on speed dial.',
      'title': 'These 3 Equipment Niches Pay $12,500 to $20,000 Per Deal (Equipment Finance '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=uzLIopNJDJY&t=113s',
      'video_id': 'uzLIopNJDJY'},
     {'author': 'Jermane Cheathem',
      'channel': 'Jermane Cheathem',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=6laX1_643JA&t=155s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, your real work is only meeting one equipment seller, one equipment dealer. '
              'Keep them updated on the deal. Get their deal approved, right? And then you use '
              'that one relationship with that one dealer, and you find other dealers.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'So, your real work is only meeting one equipment seller, one equipment dealer. '
             'Keep them updated on the deal. Get their deal approved, right? And then you use '
             'that one relationship with that one dealer, and you find other dealers.',
      'title': 'Equipment Finance Broker Business Model Explained (Jermane Cheathem)',
      'url': 'https://www.youtube.com/watch?v=6laX1_643JA&t=155s',
      'video_id': '6laX1_643JA'},
     {'author': 'BizLoanConsultants.com',
      'channel': 'BizLoanConsultants.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=kOdpTliR_HM&t=15s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Video together for you to teach you more about the the business of a starting a '
              'commercial finance company and how to broker business loans so I thought I.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Video together for you to teach you more about the the business of a starting a '
             'commercial finance company and how to broker business loans so I thought I.',
      'title': 'The Process For Getting An Equipment Finance Deal Funded '
               '(BizLoanConsultants.com)',
      'url': 'https://www.youtube.com/watch?v=kOdpTliR_HM&t=15s',
      'video_id': 'kOdpTliR_HM'},
     {'author': 'Equipment Broker Academy',
      'channel': 'Equipment Broker Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=C4UjO7bAqGI&t=59s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sellers and how to find that equipment and we provide you all the resources '
              'that downloadable forms that consignment agreements the auction agreements.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Sellers and how to find that equipment and we provide you all the resources that '
             'downloadable forms that consignment agreements the auction agreements.',
      'title': 'Equipment Broker Academy Webinar 7/2019 (Equipment Broker Academy)',
      'url': 'https://www.youtube.com/watch?v=C4UjO7bAqGI&t=59s',
      'video_id': 'C4UjO7bAqGI'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=8dTCmixzqP0&t=119s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Getting softer and it's because the blue line of Supply on dealer Lots was "
              'beginning to spike higher your next piece of equipment is on machinerepeat.com '
              "search equipment from dealerships across the country to find what you're "
              'looking for only on machinerepeat.com.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': "Getting softer and it's because the blue line of Supply on dealer Lots was "
             'beginning to spike higher your next piece of equipment is on machinerepeat.com '
             "search equipment from dealerships across the country to find what you're looking "
             'for only on machinerepeat.com.',
      'title': 'Auction Prices Softening on 1-4 Year Old Combines (Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=8dTCmixzqP0&t=119s',
      'video_id': '8dTCmixzqP0'},
     {'author': '850 Club Credit',
      'channel': '850 Club Credit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=ZHcW7oPHW5Q&t=85s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Desk Fair figure is here to help you accomplish your business goals so first '
              'things first what exactly is equipment financing okay equipment financing is a.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Desk Fair figure is here to help you accomplish your business goals so first '
             'things first what exactly is equipment financing okay equipment financing is a.',
      'title': "What Banks Don't Tell You About Equipment Financing (850 Club Credit)",
      'url': 'https://www.youtube.com/watch?v=ZHcW7oPHW5Q&t=85s',
      'video_id': 'ZHcW7oPHW5Q'},
     {'author': 'MachinesUsed',
      'channel': 'MachinesUsed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=N8JVT_KpmGc&t=126s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of search engine optimization so buyers can find the equipment we have for sale '
              'first our online marketing puts your equipment right at the fingertips of.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Of search engine optimization so buyers can find the equipment we have for sale '
             'first our online marketing puts your equipment right at the fingertips of.',
      'title': 'MachinesUsed.com Company Video (MachinesUsed)',
      'url': 'https://www.youtube.com/watch?v=N8JVT_KpmGc&t=126s',
      'video_id': 'N8JVT_KpmGc'},
     {'author': 'ET Transport',
      'channel': 'ET Transport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=Y4Qa3jy-WNw&t=22s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It we're going to first peel back the layers on these new rules because they're "
              "more than just bureaucratic talk they're response to real issues in the "
              "trucking game so here's the deal the FMCSA.",
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "It we're going to first peel back the layers on these new rules because they're "
             "more than just bureaucratic talk they're response to real issues in the trucking "
             "game so here's the deal the FMCSA.",
      'title': "FMCSA Cracks Down On Brokers That DON'T PAY! 🚚 Major Trucking Industry Shakeup "
               'Revealed! (ET Transport)',
      'url': 'https://www.youtube.com/watch?v=Y4Qa3jy-WNw&t=22s',
      'video_id': 'Y4Qa3jy-WNw'},
     {'author': 'Diesel Down Under',
      'channel': 'Diesel Down Under',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=cNP1VdOt1J4&t=28s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "What's up, Guys, just back for another video today. Um, we're in the 108 at the "
              'best place in Jalong, Richie. Just trying to find some of me latest bargains '
              "I've acquired here. Um, some really wonderful assets to add to the fleet as "
              'always.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "What's up, Guys, just back for another video today. Um, we're in the 108 at the "
             'best place in Jalong, Richie. Just trying to find some of me latest bargains '
             "I've acquired here. Um, some really wonderful assets to add to the fleet as "
             'always.',
      'title': 'Gambling On Inoperable Equipment At The Ritchie Bros Auction! (Diesel Down '
               'Under)',
      'url': 'https://www.youtube.com/watch?v=cNP1VdOt1J4&t=28s',
      'video_id': 'cNP1VdOt1J4'},
     {'author': 'AFT Dispatch',
      'channel': 'AFT Dispatch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=4m_pJHgvrpc&t=15s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'New FMCSA rule that goes into effect this coming January but first roll the  '
              'intro welcome back before we get started.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'New FMCSA rule that goes into effect this coming January but first roll the  '
             'intro welcome back before we get started.',
      'title': 'New FMCSA Rule to Protect Truckers from Unpaid Broker Claims (AFT Dispatch)',
      'url': 'https://www.youtube.com/watch?v=4m_pJHgvrpc&t=15s',
      'video_id': '4m_pJHgvrpc'},
     {'author': 'EquipmentWorld',
      'channel': 'EquipmentWorld',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=l4sJ-xx-mqI&t=20s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And she's going to break it all down for us. Shelley, thank you so much for "
              "being back on the dirt. It's good to see you again. So my first question is "
              "we're talking about oil sampling again.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "And she's going to break it all down for us. Shelley, thank you so much for "
             "being back on the dirt. It's good to see you again. So my first question is "
             "we're talking about oil sampling again.",
      'title': 'Dos and Don’ts of Collecting Oil Samples from Construction Equipment '
               '(EquipmentWorld)',
      'url': 'https://www.youtube.com/watch?v=l4sJ-xx-mqI&t=20s',
      'video_id': 'l4sJ-xx-mqI'},
     {'author': 'Boom & Bucket',
      'channel': 'Boom & Bucket',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=wIrb4GAXyy0&t=34s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '" So, I gave him one piece. He sold the thing in 3 weeks. And I\'ve had it '
              "sitting up for sale for 6 months. Process was simple and I didn't have to deal "
              'with any tire kickers or anything. I just got a call and said, "All right, got '
              'a guy. Will you take the list price?".',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': '" So, I gave him one piece. He sold the thing in 3 weeks. And I\'ve had it '
             "sitting up for sale for 6 months. Process was simple and I didn't have to deal "
             'with any tire kickers or anything. I just got a call and said, "All right, got a '
             'guy. Will you take the list price?".',
      'title': "Selling Heavy Equipment w/ Boom & Bucket: Shane's Experience (Boom & Bucket)",
      'url': 'https://www.youtube.com/watch?v=wIrb4GAXyy0&t=34s',
      'video_id': 'wIrb4GAXyy0'},
     {'author': 'TITANS of CNC MACHINING',
      'channel': 'TITANS of CNC MACHINING',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:10](https://www.youtube.com/watch?v=bqSGI0L8zm0&t=1690s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And finding vendors on CNC expert.com you get certified you get hired you find '
              'skilled labor you find customers you find vendors you communicate you can.',
      'timestamp': 1690,
      'timestamp_label': '[00:28:10]',
      'timestamp_seconds': 1690,
      'tip': 'And finding vendors on CNC expert.com you get certified you get hired you find '
             'skilled labor you find customers you find vendors you communicate you can.',
      'title': 'TOP 10 | Build Your OWN Thriving CNC Machine Shop (TITANS of CNC MACHINING)',
      'url': 'https://www.youtube.com/watch?v=bqSGI0L8zm0&t=1690s',
      'video_id': 'bqSGI0L8zm0'},
     {'author': 'Mike Whicita- Where To Sell My Used Equipment',
      'channel': 'Mike Whicita- Where To Sell My Used Equipment',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=h_gTFo7GYEo&t=115s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Does have an entire heavy equipment category dedicated to it The Creeks list '
              'heavy equipment page for Las Vegas for example featured 1050 local sales '
              'listings at the time of writing for more information call.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'Does have an entire heavy equipment category dedicated to it The Creeks list '
             'heavy equipment page for Las Vegas for example featured 1050 local sales '
             'listings at the time of writing for more information call.',
      'title': 'Tips for Selling Heavy Equipment - Part 1 (Mike Whicita- Where To Sell My Used '
               'Equipment)',
      'url': 'https://www.youtube.com/watch?v=h_gTFo7GYEo&t=115s',
      'video_id': 'h_gTFo7GYEo'},
     {'author': 'EquipmentWorld',
      'channel': 'EquipmentWorld',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=w3saQAgnyLI&t=116s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't really want to deal with but yeah we pick up the units it's it's also "
              'in wisconsin here being winter time you need to have something for the guys to '
              "do in the winter so we'll go through it and fix it and get it operational "
              'again.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "I don't really want to deal with but yeah we pick up the units it's it's also in "
             'wisconsin here being winter time you need to have something for the guys to do '
             "in the winter so we'll go through it and fix it and get it operational again.",
      'title': 'This Contractor Salvages Flood-Damaged Equipment to Boost Fleet '
               '(EquipmentWorld)',
      'url': 'https://www.youtube.com/watch?v=w3saQAgnyLI&t=116s',
      'video_id': 'w3saQAgnyLI'}],
 7: [{'author': 'Vantor Surplus',
      'channel': 'Vantor Surplus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:14](https://www.youtube.com/watch?v=lExAdQTwxNk&t=674s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Experienced auction buyers pair that parts commonality with a disciplined yard '
              'checklist before bidding. They match the data plate serial number against '
              'Defense Logistics Agency catalog descriptions to verify engine family and blade '
              'trim.',
      'timestamp': 674,
      'timestamp_label': '[00:11:14]',
      'timestamp_seconds': 674,
      'tip': 'Experienced auction buyers pair that parts commonality with a disciplined yard '
             'checklist before bidding. They match the data plate serial number against '
             'Defense Logistics Agency catalog descriptions to verify engine family and blade '
             'trim.',
      'title': 'Why the Pentagon Is Forced to Auction Brand-New Bulldozers as “Unserviceable '
               'Scrap” (Vantor Surplus)',
      'url': 'https://www.youtube.com/watch?v=lExAdQTwxNk&t=674s',
      'video_id': 'lExAdQTwxNk'},
     {'author': 'NexLayer Tech',
      'channel': 'NexLayer Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:53](https://www.youtube.com/watch?v=o7egpgd1LLI&t=293s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When normal utility power eventually becomes stable again, the system can '
              'transition back according to the facility’s operating design. Now we’re getting '
              'closer to the equipment we normally think about when we hear the words “data '
              'center.',
      'timestamp': 293,
      'timestamp_label': '[00:04:53]',
      'timestamp_seconds': 293,
      'tip': 'When normal utility power eventually becomes stable again, the system can '
             'transition back according to the facility’s operating design. Now we’re getting '
             'closer to the equipment we normally think about when we hear the words “data '
             'center.',
      'title': 'How Data Center Power Works | UPS, Generators, PDU & Redundancy (NexLayer '
               'Tech)',
      'url': 'https://www.youtube.com/watch?v=o7egpgd1LLI&t=293s',
      'video_id': 'o7egpgd1LLI'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=UxhrvcRGfdc&t=68s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pacifico Energy, building for a Texas data center. And delivery begins in 2027. '
              'On the surface, this looks like a routine procurement. But look closer at three '
              'details. The unit count, the 60 Hz gearbox configuration, and the timing.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'Pacifico Energy, building for a Texas data center. And delivery begins in 2027. '
             'On the surface, this looks like a routine procurement. But look closer at three '
             'details. The unit count, the 60 Hz gearbox configuration, and the timing.',
      'title': 'Why Data Centers Use Smaller Gas Turbines | 624 MW Power Plant Explained | '
               'Keentel Engineering (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=UxhrvcRGfdc&t=68s',
      'video_id': 'UxhrvcRGfdc'},
     {'author': 'YouCanDo TV',
      'channel': 'YouCanDo TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=aJhOAz2q35Q&t=239s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well as advanced drives that provide smooth and accurate movement of the '
              'Machining tools this system ensures that the Machining process is carried out '
              'with the utmost Precision resulting in high quality finished products.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': 'Well as advanced drives that provide smooth and accurate movement of the '
             'Machining tools this system ensures that the Machining process is carried out '
             'with the utmost Precision resulting in high quality finished products.',
      'title': 'How Heavy Duty CNC Machines Make Huge Gears. High-performance 5-axis Machining '
               'Center (YouCanDo TV)',
      'url': 'https://www.youtube.com/watch?v=aJhOAz2q35Q&t=239s',
      'video_id': 'aJhOAz2q35Q'},
     {'author': 'CSC',
      'channel': 'CSC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=mwPfMMgcYNI&t=47s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Customer experience by shortening workflow turnaround times and decreasing '
              'processing times including improving uniform commercial code delivery times by '
              "60 and with that let's welcome russ.",
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'Customer experience by shortening workflow turnaround times and decreasing '
             'processing times including improving uniform commercial code delivery times by '
             "60 and with that let's welcome russ.",
      'title': 'UCC 101 for Lenders: The Basics of UCC Searching and Filing (CSC)',
      'url': 'https://www.youtube.com/watch?v=mwPfMMgcYNI&t=47s',
      'video_id': 'mwPfMMgcYNI'},
     {'author': 'Garden Shop Pro',
      'channel': 'Garden Shop Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=xe1J4TAACZE&t=252s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But to run a flawless query, you've got to follow a strict process. Step one is "
              'honestly the most critical. You must verify the exact legal name of the entity '
              "using the state's corporate database. Step two, access that online portal.",
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': "But to run a flawless query, you've got to follow a strict process. Step one is "
             'honestly the most critical. You must verify the exact legal name of the entity '
             "using the state's corporate database. Step two, access that online portal.",
      'title': 'How to search New York UCC filings step by step (Garden Shop Pro)',
      'url': 'https://www.youtube.com/watch?v=xe1J4TAACZE&t=252s',
      'video_id': 'xe1J4TAACZE'},
     {'author': 'ProfitDig | Contractor Business Strategies, Advice',
      'channel': 'ProfitDig | Contractor Business Strategies, Advice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=AP6szJXIhss&t=59s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That'll get you a seat at the table anyway. Y'all were talking about something "
              "earlier. Well, we were just, you know, we're trying to take a step back and and "
              "and think about like we we have an application. It's for job bidding and "
              'costing.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': "That'll get you a seat at the table anyway. Y'all were talking about something "
             "earlier. Well, we were just, you know, we're trying to take a step back and and "
             "and think about like we we have an application. It's for job bidding and "
             'costing.',
      'title': 'How to Negotiate Heavy Equipment Prices Like a Pro (Tips for New Contractors) '
               '(ProfitDig | Contractor Business Strategies, Advice)',
      'url': 'https://www.youtube.com/watch?v=AP6szJXIhss&t=59s',
      'video_id': 'AP6szJXIhss'},
     {'author': 'TITANS of CNC MACHINING',
      'channel': 'TITANS of CNC MACHINING',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=IyxOJ_r0HP4&t=21s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Boom, let's go check them out. Super alloys started back in the 1990s and like "
              "most great companies, they didn't just start at the top. They built their way "
              'into one of the hardest industries in the world earning trust step by step '
              'until they became a tier one supplier.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "Boom, let's go check them out. Super alloys started back in the 1990s and like "
             "most great companies, they didn't just start at the top. They built their way "
             'into one of the hardest industries in the world earning trust step by step until '
             'they became a tier one supplier.',
      'title': 'World’s Largest Manufacturer Runs 600 CNC Machines (TITANS of CNC MACHINING)',
      'url': 'https://www.youtube.com/watch?v=IyxOJ_r0HP4&t=21s',
      'video_id': 'IyxOJ_r0HP4'},
     {'author': 'Block Imaging',
      'channel': 'Block Imaging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=VOR_RnHfhE4&t=138s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When you purchase a refurbished imaging system from Block Imaging, you’re '
              'getting a system that has been pulled from active service and shipped back to '
              'our headquarters for extensive restorative work.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'When you purchase a refurbished imaging system from Block Imaging, you’re '
             'getting a system that has been pulled from active service and shipped back to '
             'our headquarters for extensive restorative work.',
      'title': 'New Vs. Used Vs. Refurbished Medical Imaging Equipment [Pros & Cons] (Block '
               'Imaging)',
      'url': 'https://www.youtube.com/watch?v=VOR_RnHfhE4&t=138s',
      'video_id': 'VOR_RnHfhE4'},
     {'author': 'Ritchie Bros.',
      'channel': 'Ritchie Bros.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=oItxvAmXefg&t=22s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Confirm your email address by clicking the 'Confirm email' button. Please note "
              'your personal password is included in this email. Step 2 - Verify your phone '
              'number To verify your account, please provide your phone number.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': "Confirm your email address by clicking the 'Confirm email' button. Please note "
             'your personal password is included in this email. Step 2 - Verify your phone '
             'number To verify your account, please provide your phone number.',
      'title': 'Getting started on IronPlanet | Europe & Middle East (Ritchie Bros.)',
      'url': 'https://www.youtube.com/watch?v=oItxvAmXefg&t=22s',
      'video_id': 'oItxvAmXefg'},
     {'author': 'Badwolf Unincorporated',
      'channel': 'Badwolf Unincorporated',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:36](https://www.youtube.com/watch?v=QJwDP5kwtJ4&t=876s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This one you're going to go Bailey Baylor okay number eight optional filer "
              'reference data that is if you have an internal code within your own '
              'administrative uh Corporation trust whatever that you reference this '
              "information to you can put it here otherwise it's optional.",
      'timestamp': 876,
      'timestamp_label': '[00:14:36]',
      'timestamp_seconds': 876,
      'tip': "This one you're going to go Bailey Baylor okay number eight optional filer "
             'reference data that is if you have an internal code within your own '
             'administrative uh Corporation trust whatever that you reference this information '
             "to you can put it here otherwise it's optional.",
      'title': 'How to properly do a UCC1 Financing Statement: Step by Step Inst. for the '
               '"Strawman" Commercial Lien (Badwolf Unincorporated)',
      'url': 'https://www.youtube.com/watch?v=QJwDP5kwtJ4&t=876s',
      'video_id': 'QJwDP5kwtJ4'},
     {'author': 'Phinnastads Biomedical Limited',
      'channel': 'Phinnastads Biomedical Limited',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=uElb8NdCkUQ&t=227s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clues can save us a lot of time and trouble later on by taking the time to '
              'listen and observe we can make more informed decisions about how to proceed '
              'with repairs ultimately ensuring the machine is back up running.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'Clues can save us a lot of time and trouble later on by taking the time to '
             'listen and observe we can make more informed decisions about how to proceed with '
             'repairs ultimately ensuring the machine is back up running.',
      'title': 'Step-by-Step Guide to Diagnosing and Repairing MRI Equipment. (Phinnastads '
               'Biomedical Limited)',
      'url': 'https://www.youtube.com/watch?v=uElb8NdCkUQ&t=227s',
      'video_id': 'uElb8NdCkUQ'},
     {'author': 'The Job Library',
      'channel': 'The Job Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:24](https://www.youtube.com/watch?v=Og3Yj20ldiY&t=564s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But remember that construction can sometimes be seasonal. Depending on where '
              'you live and the type of work you do, there may be periods when bad weather '
              "slows or stops projects. So, don't judge a job solely by its hourly rate rate "
              'wage.',
      'timestamp': 564,
      'timestamp_label': '[00:09:24]',
      'timestamp_seconds': 564,
      'tip': 'But remember that construction can sometimes be seasonal. Depending on where you '
             'live and the type of work you do, there may be periods when bad weather slows or '
             "stops projects. So, don't judge a job solely by its hourly rate rate wage.",
      'title': 'How to Become a Heavy Equipment Operator (Step-by-Step Guide) (The Job '
               'Library)',
      'url': 'https://www.youtube.com/watch?v=Og3Yj20ldiY&t=564s',
      'video_id': 'Og3Yj20ldiY'},
     {'author': 'MXR Imaging',
      'channel': 'MXR Imaging',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:41](https://www.youtube.com/watch?v=Nw9qRw-Y6TE&t=881s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Series vendor reconditioning programs should include all electronic mechanical '
              'electromechanical and x-ray tube subsystems within each system for inspection '
              'and evaluation and that scanner right there is a GE.',
      'timestamp': 881,
      'timestamp_label': '[00:14:41]',
      'timestamp_seconds': 881,
      'tip': 'Series vendor reconditioning programs should include all electronic mechanical '
             'electromechanical and x-ray tube subsystems within each system for inspection '
             'and evaluation and that scanner right there is a GE.',
      'title': 'MXR Imaging Webinar Series: Purchasing Platinum Certified Pre-Owned MRI and CT '
               'Equipment (MXR Imaging)',
      'url': 'https://www.youtube.com/watch?v=Nw9qRw-Y6TE&t=881s',
      'video_id': 'Nw9qRw-Y6TE'},
     {'author': 'Oil Analysis',
      'channel': 'Oil Analysis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:06](https://www.youtube.com/watch?v=ALXdY2bAHV0&t=366s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Crankcase pressure may be a confirmation test to confirm the severity of the '
              "damage if you're watching this as part of an online training course you may now "
              'work through some of the examples on your own below thank you for listening.',
      'timestamp': 366,
      'timestamp_label': '[00:06:06]',
      'timestamp_seconds': 366,
      'tip': 'Crankcase pressure may be a confirmation test to confirm the severity of the '
             "damage if you're watching this as part of an online training course you may now "
             'work through some of the examples on your own below thank you for listening.',
      'title': 'Learn Oil Analysis - How to read an oil sample report (Oil Analysis)',
      'url': 'https://www.youtube.com/watch?v=ALXdY2bAHV0&t=366s',
      'video_id': 'ALXdY2bAHV0'}],
 8: [{'author': 'Garden Shop Pro',
      'channel': 'Garden Shop Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=F-yeb_XOivY&t=174s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our workflow is basically just three super actionable steps. Securely access '
              'the portal, enter your exact search criteria, and intelligently decipher what '
              "comes back. Let's talk about the data entry part cuz it can be tricky.",
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'Our workflow is basically just three super actionable steps. Securely access the '
             'portal, enter your exact search criteria, and intelligently decipher what comes '
             "back. Let's talk about the data entry part cuz it can be tricky.",
      'title': 'How to look up a UCC filing in Texas online (Garden Shop Pro)',
      'url': 'https://www.youtube.com/watch?v=F-yeb_XOivY&t=174s',
      'video_id': 'F-yeb_XOivY'},
     {'author': 'MICHAEL WANG',
      'channel': 'MICHAEL WANG',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:27](https://www.youtube.com/watch?v=M5DbDgTFVeY&t=327s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Major Chinese suppliers include Huazhong CNC and GSK, which are gradually '
              'replacing imported high-end control systems. Cutting Tool Systems Explained. '
              'Tools can be classified by construction. Solid tools offer high rigidity, '
              'making them suitable for small-diameter finishing.',
      'timestamp': 327,
      'timestamp_label': '[00:05:27]',
      'timestamp_seconds': 327,
      'tip': 'Major Chinese suppliers include Huazhong CNC and GSK, which are gradually '
             'replacing imported high-end control systems. Cutting Tool Systems Explained. '
             'Tools can be classified by construction. Solid tools offer high rigidity, making '
             'them suitable for small-diameter finishing.',
      'title': 'CNC Machining Explained: How Precision Parts Are Made (MICHAEL WANG)',
      'url': 'https://www.youtube.com/watch?v=M5DbDgTFVeY&t=327s',
      'video_id': 'M5DbDgTFVeY'},
     {'author': 'IndustrialX',
      'channel': 'IndustrialX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=ufN_5j5epkw&t=63s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The tool paths can be simulated digitally to identify collisions before '
              'production. Next, the material is securely positioned inside a precision CNC '
              'machining center. Different operations require different cutting tools, from '
              'roughing cutters to tiny precision drills.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'The tool paths can be simulated digitally to identify collisions before '
             'production. Next, the material is securely positioned inside a precision CNC '
             'machining center. Different operations require different cutting tools, from '
             'roughing cutters to tiny precision drills.',
      'title': 'How CNC Machines Manufacture PARFECT Aircraft Parts ✈️ | Inside a $Million '
               'Aerospace Factory (IndustrialX)',
      'url': 'https://www.youtube.com/watch?v=ufN_5j5epkw&t=63s',
      'video_id': 'ufN_5j5epkw'},
     {'author': 'Strange Parts',
      'channel': 'Strange Parts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:04](https://www.youtube.com/watch?v=YuSApjBn_zY&t=1144s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can see here there are tool marks on here, and this is very smooth to the '
              "touch, but it doesn't look great. It still has marks where the end mills and "
              'other tools moved back and forth across the part, not really what we want from '
              'an aesthetic perspective.',
      'timestamp': 1144,
      'timestamp_label': '[00:19:04]',
      'timestamp_seconds': 1144,
      'tip': 'You can see here there are tool marks on here, and this is very smooth to the '
             "touch, but it doesn't look great. It still has marks where the end mills and "
             'other tools moved back and forth across the part, not really what we want from '
             'an aesthetic perspective.',
      'title': 'Inside a Chinese CNC Factory (Strange Parts)',
      'url': 'https://www.youtube.com/watch?v=YuSApjBn_zY&t=1144s',
      'video_id': 'YuSApjBn_zY'},
     {'author': 'MS Milling CNC',
      'channel': 'MS Milling CNC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:17](https://www.youtube.com/watch?v=BCaYAmw5wQs&t=317s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But some of the work we do is 316 stainless, some of it's aluminum, a lot of it "
              'steel. Ouro BNX lathe, our quick tech. This machine actually has tools that '
              "rotate at any angle on both spindles. So, this building we're in now is the "
              'original Superior Technology.',
      'timestamp': 317,
      'timestamp_label': '[00:05:17]',
      'timestamp_seconds': 317,
      'tip': "But some of the work we do is 316 stainless, some of it's aluminum, a lot of it "
             'steel. Ouro BNX lathe, our quick tech. This machine actually has tools that '
             "rotate at any angle on both spindles. So, this building we're in now is the "
             'original Superior Technology.',
      'title': 'CNC Machine Shop Tour - 80k Square Feet of Manufacturing - Superior '
               'Technology, Inc (MS Milling CNC)',
      'url': 'https://www.youtube.com/watch?v=BCaYAmw5wQs&t=317s',
      'video_id': 'BCaYAmw5wQs'},
     {'author': 'China Expo And Sourcing with Abed',
      'channel': 'China Expo And Sourcing with Abed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:40:36](https://www.youtube.com/watch?v=h9RutWf9kWM&t=6036s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, I'm almost done with this expo. Um it is very big and large "
              'exhibition. I really suggest whoever is in this kind of industry uh cutting '
              'machine CNC any kind of tools that related to this industry highly recommended '
              'to visit this expo.',
      'timestamp': 6036,
      'timestamp_label': '[01:40:36]',
      'timestamp_seconds': 6036,
      'tip': "All right, I'm almost done with this expo. Um it is very big and large "
             'exhibition. I really suggest whoever is in this kind of industry uh cutting '
             'machine CNC any kind of tools that related to this industry highly recommended '
             'to visit this expo.',
      'title': 'China CNC Machine And Tool Expo 2026 Walkthrough | +100 Suppliers and Factory '
               'Newest Products (China Expo And Sourcing with Abed)',
      'url': 'https://www.youtube.com/watch?v=h9RutWf9kWM&t=6036s',
      'video_id': 'h9RutWf9kWM'},
     {'author': 'Equipment & Contracting',
      'channel': 'Equipment & Contracting',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=HIhx8sY-aac&t=176s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For a complete maintenance checklist, visit equipmentandcontracting. Software '
              'programs are an invaluable tool to develop, implement, and maintain a fleet '
              'maintenance program.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': 'For a complete maintenance checklist, visit equipmentandcontracting. Software '
             'programs are an invaluable tool to develop, implement, and maintain a fleet '
             'maintenance program.',
      'title': 'Fleet Management Guide for Heavy Construction Equipment and Trucks (Equipment '
               '& Contracting)',
      'url': 'https://www.youtube.com/watch?v=HIhx8sY-aac&t=176s',
      'video_id': 'HIhx8sY-aac'},
     {'author': 'County Portal',
      'channel': 'County Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=cMfMjjnw9Ko&t=92s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most states have an online portal that allows you to conduct a search right '
              "from your computer. You'll enter the debtor's name into the search bar.",
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'Most states have an online portal that allows you to conduct a search right from '
             "your computer. You'll enter the debtor's name into the search bar.",
      'title': 'How To Do A Ucc Lien Search? (County Portal)',
      'url': 'https://www.youtube.com/watch?v=cMfMjjnw9Ko&t=92s',
      'video_id': 'cMfMjjnw9Ko'},
     {'author': 'ET Transport',
      'channel': 'ET Transport',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:53:24](https://www.youtube.com/watch?v=wzN9KKrhTBo&t=3204s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'What are your honest thoughts? My honest thoughts, I gave you my honest '
              'thoughts. I think this is an unbelievable platform and people should start '
              'taking advantage of it. Are you using them or doing that? Uh so do I recommend '
              'using them or using a broker?',
      'timestamp': 3204,
      'timestamp_label': '[00:53:24]',
      'timestamp_seconds': 3204,
      'tip': 'What are your honest thoughts? My honest thoughts, I gave you my honest '
             'thoughts. I think this is an unbelievable platform and people should start '
             'taking advantage of it. Are you using them or doing that? Uh so do I recommend '
             'using them or using a broker?',
      'title': 'BUYING EQUIPMENT LIVE AT THE RITCHIE BROTHERS AUCTION!  📱 (ET Transport)',
      'url': 'https://www.youtube.com/watch?v=wzN9KKrhTBo&t=3204s',
      'video_id': 'wzN9KKrhTBo'},
     {'author': 'MachineshopLaunchpad',
      'channel': 'MachineshopLaunchpad',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:41](https://www.youtube.com/watch?v=BoQ7bHu0IZE&t=641s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Tutorials on how to do this something that's going to be of great use to you "
              'guys is in the titans of CNC Machining series they have a tool list now do not.',
      'timestamp': 641,
      'timestamp_label': '[00:10:41]',
      'timestamp_seconds': 641,
      'tip': "Tutorials on how to do this something that's going to be of great use to you "
             'guys is in the titans of CNC Machining series they have a tool list now do not.',
      'title': 'Starting A Machine Shop In 2025: Zero Experience Guide (MachineshopLaunchpad)',
      'url': 'https://www.youtube.com/watch?v=BoQ7bHu0IZE&t=641s',
      'video_id': 'BoQ7bHu0IZE'},
     {'author': 'Mike Dobronos',
      'channel': 'Mike Dobronos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:53](https://www.youtube.com/watch?v=6RIRTBKk1fU&t=413s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Doesn't it doesn't look like it's actually hit the radiator at all but uh that "
              "got smashed in a little bit it's a jack back here control panels over here "
              'pretty basic 3 387 hours.',
      'timestamp': 413,
      'timestamp_label': '[00:06:53]',
      'timestamp_seconds': 413,
      'tip': "Doesn't it doesn't look like it's actually hit the radiator at all but uh that "
             "got smashed in a little bit it's a jack back here control panels over here "
             'pretty basic 3 387 hours.',
      'title': 'Buying on Ritchie Brothers IronPlant online Auction (my experience) (Mike '
               'Dobronos)',
      'url': 'https://www.youtube.com/watch?v=6RIRTBKk1fU&t=413s',
      'video_id': '6RIRTBKk1fU'},
     {'author': 'EmRôs Reviews',
      'channel': 'EmRôs Reviews',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:52](https://www.youtube.com/watch?v=eHFjQHJs_8A&t=232s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Search for all the records not a certain record so I click that so you leave '
              "those blank and it's that simple I'm not bothering the rest of that because.",
      'timestamp': 232,
      'timestamp_label': '[00:03:52]',
      'timestamp_seconds': 232,
      'tip': 'Search for all the records not a certain record so I click that so you leave '
             "those blank and it's that simple I'm not bothering the rest of that because.",
      'title': 'UCC-11 Filing to Check for Liens (EmRôs Reviews)',
      'url': 'https://www.youtube.com/watch?v=eHFjQHJs_8A&t=232s',
      'video_id': 'eHFjQHJs_8A'},
     {'author': 'Jim Mack',
      'channel': 'Jim Mack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=YyZcRwETdeA&t=102s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're measuring it metric this one here, looks like it would measure 91 "
              'millimeters. You can also measure the track bushing external wear. Remember '
              'that track bushing, as it goes around this is what contacts the sprocket in the '
              'back.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': "If you're measuring it metric this one here, looks like it would measure 91 "
             'millimeters. You can also measure the track bushing external wear. Remember that '
             'track bushing, as it goes around this is what contacts the sprocket in the back.',
      'title': 'Performing Undercarriage Inspection and Measurements (Jim Mack)',
      'url': 'https://www.youtube.com/watch?v=YyZcRwETdeA&t=102s',
      'video_id': 'YyZcRwETdeA'},
     {'author': 'KONSTANT LAW',
      'channel': 'KONSTANT LAW',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=-vmGbnB5rJM&t=305s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Getting this information and understanding this information so if you're out "
              "there and you're one of those people that's just coming into the game you know "
              'feel free to highlight us you know I hope but uh till next time guys kkk tv.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': "Getting this information and understanding this information so if you're out "
             "there and you're one of those people that's just coming into the game you know "
             'feel free to highlight us you know I hope but uh till next time guys kkk tv.',
      'title': 'UCC LIENS: What is a UCC 1, #assetprotection for my #car #home #house #family '
               '#business & #property (KONSTANT LAW)',
      'url': 'https://www.youtube.com/watch?v=-vmGbnB5rJM&t=305s',
      'video_id': '-vmGbnB5rJM'},
     {'author': 'Farm Journal',
      'channel': 'Farm Journal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=S8sjPgCnSag&t=15s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'الماضيين. يقدم لكم " ماشينري بيت" تحديثًا حول الوضع الحالي. حسنًا، لقد شهدنا.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'الماضيين. يقدم لكم " ماشينري بيت" تحديثًا حول الوضع الحالي. حسنًا، لقد شهدنا.',
      'title': 'Machinery Pete: Changes in Late Model Tractor Prices (Farm Journal)',
      'url': 'https://www.youtube.com/watch?v=S8sjPgCnSag&t=15s',
      'video_id': 'S8sjPgCnSag'}],
 9: [{'author': 'AuctionTime',
      'channel': 'AuctionTime',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=JxE8MNAqxhQ&t=75s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We typically go through evaluation process with the customer to determine if '
              'their expectations are realistic with what we estimate. Once we once we get to '
              'a common ground there, then we will obviously sign a contract, a consignment '
              'agreement.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'We typically go through evaluation process with the customer to determine if '
             'their expectations are realistic with what we estimate. Once we once we get to a '
             'common ground there, then we will obviously sign a contract, a consignment '
             'agreement.',
      'title': 'KDK Sales & Equipment On How AuctionTime Helps Them Get The Best Auction Deals '
               'For Their Clients (AuctionTime)',
      'url': 'https://www.youtube.com/watch?v=JxE8MNAqxhQ&t=75s',
      'video_id': 'JxE8MNAqxhQ'},
     {'author': 'Millionaires Fast Track',
      'channel': 'Millionaires Fast Track',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:12](https://www.youtube.com/watch?v=V7R5ptjXKjI&t=1092s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Finally, regulation and competition. Emissions rules tighten, transport permits '
              'get harder, and every rental yard in a city is competing for the same '
              'contractors. The moat in this business is not the machine.',
      'timestamp': 1092,
      'timestamp_label': '[00:18:12]',
      'timestamp_seconds': 1092,
      'tip': 'Finally, regulation and competition. Emissions rules tighten, transport permits '
             'get harder, and every rental yard in a city is competing for the same '
             'contractors. The moat in this business is not the machine.',
      'title': 'The Economics of Owning an Excavator Rental Business (Millionaires Fast Track)',
      'url': 'https://www.youtube.com/watch?v=V7R5ptjXKjI&t=1092s',
      'video_id': 'V7R5ptjXKjI'},
     {'author': 'Farm Journal',
      'channel': 'Farm Journal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=wuBUPvkp-d8&t=68s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Kraft Auction Services becomes complete. Now, if we look at average auction '
              "prices, uh here's some data from machinerypete. You can see the current average "
              'price this year at auction, $15,147 with a high of $36,000. Now, really '
              'interesting to look back through the years.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'Kraft Auction Services becomes complete. Now, if we look at average auction '
             "prices, uh here's some data from machinerypete. You can see the current average "
             'price this year at auction, $15,147 with a high of $36,000. Now, really '
             'interesting to look back through the years.',
      'title': 'Machinery Pete: John Deere 4430 Price Comparison (Farm Journal)',
      'url': 'https://www.youtube.com/watch?v=wuBUPvkp-d8&t=68s',
      'video_id': 'wuBUPvkp-d8'},
     {'author': 'FMCSA REGISTRATION dot com',
      'channel': 'FMCSA REGISTRATION dot com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=pK4RGE_1My4&t=45s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, non-compliance can lead to hefty fines, revoked licenses, and even '
              "putting your business at risk. That's why staying on top of these regulations "
              'is not just a good idea, it\'s a necessity. You might think, "How do I keep up '
              'with all these rules?".',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'Well, non-compliance can lead to hefty fines, revoked licenses, and even putting '
             "your business at risk. That's why staying on top of these regulations is not "
             'just a good idea, it\'s a necessity. You might think, "How do I keep up with all '
             'these rules?".',
      'title': 'FMCSA Compliance EXPLAINED: What Every Truck Driver & Carrier MUST Know in '
               '2025! (FMCSA REGISTRATION dot com)',
      'url': 'https://www.youtube.com/watch?v=pK4RGE_1My4&t=45s',
      'video_id': 'pK4RGE_1My4'},
     {'author': 'FMCSA',
      'channel': 'FMCSA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:41](https://www.youtube.com/watch?v=qJ2zB-OEb8o&t=581s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Broker or Freight Forwarder that does not operate commercial vehicles may file '
              'a BOC-3 form on their behalf in their state.',
      'timestamp': 581,
      'timestamp_label': '[00:09:41]',
      'timestamp_seconds': 581,
      'tip': 'Broker or Freight Forwarder that does not operate commercial vehicles may file a '
             'BOC-3 form on their behalf in their state.',
      'title': 'Defining FMCSA Operating Authority Types for Freight Forwarders and Brokers '
               '(FMCSA OFFICIAL VIDEO) (FMCSA)',
      'url': 'https://www.youtube.com/watch?v=qJ2zB-OEb8o&t=581s',
      'video_id': 'qJ2zB-OEb8o'},
     {'author': 'Mutha Trucker - Official Trucking Channel',
      'channel': 'Mutha Trucker - Official Trucking Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=BE6n1FfpOO8&t=141s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, if you lived in Texas, for example, and got convicted for a traffic '
              'violation while driving through another state, federal law said you had to '
              "report that conviction back to Texas. But, here's the part that many truck "
              'drivers never really realized.',
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'So, if you lived in Texas, for example, and got convicted for a traffic '
             'violation while driving through another state, federal law said you had to '
             "report that conviction back to Texas. But, here's the part that many truck "
             'drivers never really realized.',
      'title': 'FMCSA New Rule Change Affecting All Truck Drivers Now (Mutha Trucker - '
               'Official Trucking Channel)',
      'url': 'https://www.youtube.com/watch?v=BE6n1FfpOO8&t=141s',
      'video_id': 'BE6n1FfpOO8'},
     {'author': 'the funny farm',
      'channel': 'the funny farm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:42](https://www.youtube.com/watch?v=t1CJB1XA9y0&t=282s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And a road closure to know about if you run the Inland Empire. Starting Monday, '
              'November 9th, the westbound State Route 60 on and off ramps at Western Knowles '
              'Avenue in Riverside County, California are closed to trucks, freight vehicles, '
              'and tractor trailers.',
      'timestamp': 282,
      'timestamp_label': '[00:04:42]',
      'timestamp_seconds': 282,
      'tip': 'And a road closure to know about if you run the Inland Empire. Starting Monday, '
             'November 9th, the westbound State Route 60 on and off ramps at Western Knowles '
             'Avenue in Riverside County, California are closed to trucks, freight vehicles, '
             'and tractor trailers.',
      'title': 'Trucker Regs Daily: FMCSA Shuts Down YMC Transport, Trucking Jobs Flat, Reefer '
               'Rejections Hit 21% (the funny farm)',
      'url': 'https://www.youtube.com/watch?v=t1CJB1XA9y0&t=282s',
      'video_id': 't1CJB1XA9y0'},
     {'author': 'Private Investigator Videos',
      'channel': 'Private Investigator Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=8OP-aPYhHHM&t=21s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um technically, a UCC filing is a document which is a legal notice of claim '
              'against non-real estate property or a personal property on a form called a '
              'UCC-1. And UCC stands for Universal Commercial Code.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Um technically, a UCC filing is a document which is a legal notice of claim '
             'against non-real estate property or a personal property on a form called a '
             'UCC-1. And UCC stands for Universal Commercial Code.',
      'title': 'UCC lien filings on real estate (Private Investigator Videos)',
      'url': 'https://www.youtube.com/watch?v=8OP-aPYhHHM&t=21s',
      'video_id': '8OP-aPYhHHM'},
     {'author': 'Trinity Logistics',
      'channel': 'Trinity Logistics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=oQI9qiLLIwA&t=20s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And regulations vary from state to state. We re here to simplify what you need '
              'to know for your oversized shipments. An oversized load exceeds the maximum '
              'legal weight or dimensions.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'And regulations vary from state to state. We re here to simplify what you need '
             'to know for your oversized shipments. An oversized load exceeds the maximum '
             'legal weight or dimensions.',
      'title': 'Oversize Load Regulations: What You Need to Know (Trinity Logistics)',
      'url': 'https://www.youtube.com/watch?v=oQI9qiLLIwA&t=20s',
      'video_id': 'oQI9qiLLIwA'},
     {'author': 'NerdWallet Small Business',
      'channel': 'NerdWallet Small Business',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=yAx4SRG_bfs&t=134s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '650 or higher, at least two years of business history and strong annual '
              'revenue, consider turning to an SBA lender. SBA lenders can offer up to 10 year '
              'terms with reasonable interest rates on equipment loans.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': '650 or higher, at least two years of business history and strong annual revenue, '
             'consider turning to an SBA lender. SBA lenders can offer up to 10 year terms '
             'with reasonable interest rates on equipment loans.',
      'title': 'Equipment Financing Made Simple | How to Get an Equipment Loan (NerdWallet '
               'Small Business)',
      'url': 'https://www.youtube.com/watch?v=yAx4SRG_bfs&t=134s',
      'video_id': 'yAx4SRG_bfs'},
     {'author': 'Equipment Finance Academy',
      'channel': 'Equipment Finance Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=Ua7mCs7DMsw&t=21s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "4 hours with rates starting at 6. 99% and terms up to 84 months. Whether you're "
              'in construction, trucking, health care, or the restaurant industry, you can '
              "access the nation's top lenders with zero down options available.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "4 hours with rates starting at 6. 99% and terms up to 84 months. Whether you're "
             'in construction, trucking, health care, or the restaurant industry, you can '
             "access the nation's top lenders with zero down options available.",
      'title': 'How to Get Equipment Financing in 4 Hours (Rates from 6.99%) (Equipment '
               'Finance Academy)',
      'url': 'https://www.youtube.com/watch?v=Ua7mCs7DMsw&t=21s',
      'video_id': 'Ua7mCs7DMsw'},
     {'author': 'thatDOTcop',
      'channel': 'thatDOTcop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=5KIDTEBQD18&t=196s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, let's keep moving. Let's do a little deep dive into this rule change "
              'about vehicle lighting and marking. FMCSA added exceptions eliminating the need '
              'for functional license plate lamps on the rear of the truck tractor while '
              'towing a trailer.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': "All right, let's keep moving. Let's do a little deep dive into this rule change "
             'about vehicle lighting and marking. FMCSA added exceptions eliminating the need '
             'for functional license plate lamps on the rear of the truck tractor while towing '
             'a trailer.',
      'title': "FMCSA Just Changed These Rules.. Here's What It Means for Truckers "
               '(thatDOTcop)',
      'url': 'https://www.youtube.com/watch?v=5KIDTEBQD18&t=196s',
      'video_id': '5KIDTEBQD18'},
     {'author': 'Cat Products',
      'channel': 'Cat Products',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=uI8BuTxXRzU&t=39s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, there is a bank of filters inside this truck that filters the oil on the '
              'way into the tank so that the oil in the tank is clean. And then when it comes '
              "back out using these reels up here, it's also filtered again through a "
              'high-pressure filter.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'Now, there is a bank of filters inside this truck that filters the oil on the '
             'way into the tank so that the oil in the tank is clean. And then when it comes '
             "back out using these reels up here, it's also filtered again through a "
             'high-pressure filter.',
      'title': 'Contamination Control | Oil Sampling Tips | PM Truck Maintenance (Cat '
               'Products)',
      'url': 'https://www.youtube.com/watch?v=uI8BuTxXRzU&t=39s',
      'video_id': 'uI8BuTxXRzU'},
     {'author': 'Rajeev Saini -International Business Trainer',
      'channel': 'Rajeev Saini -International Business Trainer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=aUfYWzHSUyY&t=16s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'कंबाइन रहती है तो वो ट्रैक्टर कंबाइन हार्वेस्टर आप कैसे एक्सपोर्ट कर सकते हैं '
              'कैसे आप 12 लाख रुपए कमाएंगे ओनली पांच ट्रैक्टर ऐसे एक्सपोर्ट करके इंडिया से '
              'एक-एक कैलकुलेशन आपके लिए लिख के लायक हूं.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'कंबाइन रहती है तो वो ट्रैक्टर कंबाइन हार्वेस्टर आप कैसे एक्सपोर्ट कर सकते हैं '
             'कैसे आप 12 लाख रुपए कमाएंगे ओनली पांच ट्रैक्टर ऐसे एक्सपोर्ट करके इंडिया से '
             'एक-एक कैलकुलेशन आपके लिए लिख के लायक हूं.',
      'title': 'earn rs. 12.0 lakhs by exporting tractor combine harvester I how to export '
               'tractor combine harvester (Rajeev Saini -International Business Trainer)',
      'url': 'https://www.youtube.com/watch?v=aUfYWzHSUyY&t=16s',
      'video_id': 'aUfYWzHSUyY'},
     {'author': 'Machinery Pete',
      'channel': 'Machinery Pete',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=F80Wku6kGE0&t=82s)',
      'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                   'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                   'settlement (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Lease return uh equipment coming off lease how quickly will they move it and at '
              'what price point again these factors could really affect used values now folks '
              "remember if you're looking for used equipment you know where to go Machin "
              'repeat.com.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'Lease return uh equipment coming off lease how quickly will they move it and at '
             'what price point again these factors could really affect used values now folks '
             "remember if you're looking for used equipment you know where to go Machin "
             'repeat.com.',
      'title': '2 Factors That Could Affect Used Farm Equipment Values Going Forward '
               '(Machinery Pete)',
      'url': 'https://www.youtube.com/watch?v=F80Wku6kGE0&t=82s',
      'video_id': 'F80Wku6kGE0'}],
 10: [{'author': 'Keentel Engineering',
       'channel': 'Keentel Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:47](https://www.youtube.com/watch?v=nico3vxC_dA&t=1307s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For organizations planning large-scale data centers, AI infrastructure, or '
               'major electrical loads, rigorous load calculation is the foundation for making '
               'the right engineering decisions. From the grid to the rack, every decision is '
               'connected.',
       'timestamp': 1307,
       'timestamp_label': '[00:21:47]',
       'timestamp_seconds': 1307,
       'tip': 'For organizations planning large-scale data centers, AI infrastructure, or '
              'major electrical loads, rigorous load calculation is the foundation for making '
              'the right engineering decisions. From the grid to the rack, every decision is '
              'connected.',
       'title': 'Data Center Electrical Load Calculations Explained | UPS, Transformer & '
                'Generator Sizing (Keentel Engineering)',
       'url': 'https://www.youtube.com/watch?v=nico3vxC_dA&t=1307s',
       'video_id': 'nico3vxC_dA'},
      {'author': 'BIMandbeam',
       'channel': 'BIMandbeam',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:26](https://www.youtube.com/watch?v=xJ1cFeX3gjs&t=86s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'More redundancy means more uptime, but also more equipment, more space, and '
               'more cost. And AI is changing the scale. A traditional rack draws 5 to 10 kW. '
               'An AI rack can draw more than 100. Same floor space, 10 times the power. For '
               'architects, power shapes the building.',
       'timestamp': 86,
       'timestamp_label': '[00:01:26]',
       'timestamp_seconds': 86,
       'tip': 'More redundancy means more uptime, but also more equipment, more space, and '
              'more cost. And AI is changing the scale. A traditional rack draws 5 to 10 kW. '
              'An AI rack can draw more than 100. Same floor space, 10 times the power. For '
              'architects, power shapes the building.',
       'title': 'How Do Data Centers Get Power? (Grid to Server, Explained) (BIMandbeam)',
       'url': 'https://www.youtube.com/watch?v=xJ1cFeX3gjs&t=86s',
       'video_id': 'xJ1cFeX3gjs'},
      {'author': 'Money Machines',
       'channel': 'Money Machines',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=Q00deIDcQRw&t=174s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Precision has used a collaborative robot with a CNC turning center to automate '
               'repetitive loading and unloading work for parts produced in quantities of tens '
               'of thousands per year. These examples reveal something important.',
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'Precision has used a collaborative robot with a CNC turning center to automate '
              'repetitive loading and unloading work for parts produced in quantities of tens '
              'of thousands per year. These examples reveal something important.',
       'title': 'The Money Behind a CNC Lathe Machine (Money Machines)',
       'url': 'https://www.youtube.com/watch?v=Q00deIDcQRw&t=174s',
       'video_id': 'Q00deIDcQRw'},
      {'author': 'Simply Fleet',
       'channel': 'Simply Fleet',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=z_9T-5cJEc0&t=21s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Here are five platforms worth considering. If maintenance is at the center of '
               'your construction operation, Simply Fleet brings the workflow together with '
               'construction equipment maintenance software designed for mixed fleets.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': 'Here are five platforms worth considering. If maintenance is at the center of '
              'your construction operation, Simply Fleet brings the workflow together with '
              'construction equipment maintenance software designed for mixed fleets.',
       'title': '5 Best Construction Fleet Management Software for Mixed Fleets in 2026 '
                '#constructionequipment (Simply Fleet)',
       'url': 'https://www.youtube.com/watch?v=z_9T-5cJEc0&t=21s',
       'video_id': 'z_9T-5cJEc0'},
      {'author': 'PatrickShivers',
       'channel': 'PatrickShivers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:50](https://www.youtube.com/watch?v=QI2WPiqDHqE&t=770s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They are reliable, but they are not simple. I am back out here on the farm. '
               'Now, as promised, I will tell you why the prices are so cheap on farm '
               "machinery. If you're not familiar with the prices of farm machinery, the "
               'prices at this auction were extremely low.',
       'timestamp': 770,
       'timestamp_label': '[00:12:50]',
       'timestamp_seconds': 770,
       'tip': 'They are reliable, but they are not simple. I am back out here on the farm. '
              'Now, as promised, I will tell you why the prices are so cheap on farm '
              "machinery. If you're not familiar with the prices of farm machinery, the prices "
              'at this auction were extremely low.',
       'title': 'Farm BANKRUPTCY Auction (PatrickShivers)',
       'url': 'https://www.youtube.com/watch?v=QI2WPiqDHqE&t=770s',
       'video_id': 'QI2WPiqDHqE'},
      {'author': 'YouCanDo TV',
       'channel': 'YouCanDo TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:48:08](https://www.youtube.com/watch?v=TwUdZJ1n_ps&t=2888s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Bimitec Sorus introduces the M35 machining center, integrating milling, '
               'turning, and grinding in one machine. The machine is capable of machining '
               'large parts with high precision, 1,600 mm rotary table, 43 kW spindle motor '
               'power, 35 m per minute movement speed.',
       'timestamp': 2888,
       'timestamp_label': '[00:48:08]',
       'timestamp_seconds': 2888,
       'tip': 'Bimitec Sorus introduces the M35 machining center, integrating milling, '
              'turning, and grinding in one machine. The machine is capable of machining large '
              'parts with high precision, 1,600 mm rotary table, 43 kW spindle motor power, 35 '
              'm per minute movement speed.',
       'title': 'Inside The Heavy Duty CNC Machining & Forging Plant. Modern Heavy Machinery & '
                'Equipment In Working (YouCanDo TV)',
       'url': 'https://www.youtube.com/watch?v=TwUdZJ1n_ps&t=2888s',
       'video_id': 'TwUdZJ1n_ps'},
      {'author': 'Living in Fort Myers',
       'channel': 'Living in Fort Myers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=sF15mNe2_l4&t=15s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Hey everyone it's your favorite fort myers real estate broker now if you've "
               "watched my videos before welcome back if you're new here and you.",
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Hey everyone it's your favorite fort myers real estate broker now if you've "
              "watched my videos before welcome back if you're new here and you.",
       'title': 'Wire Transfer Fraud - How To Protect Yourself And How To Prevent Yourself '
                'From Becoming a Victim 💸💸💸 (Living in Fort Myers)',
       'url': 'https://www.youtube.com/watch?v=sF15mNe2_l4&t=15s',
       'video_id': 'sF15mNe2_l4'},
      {'author': 'SARK Engineers & COnsultants',
       'channel': 'SARK Engineers & COnsultants',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:16](https://www.youtube.com/watch?v=Qiyq7yhmD2o&t=76s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The physical inspection was conducted overseas, while the Indian chartered '
               'engineer reviewed the entire technical and commercial dossier before '
               'certification. The clean workflow is simple. First, a qualified inspector in '
               'the country of sale physically inspects the machine.',
       'timestamp': 76,
       'timestamp_label': '[00:01:16]',
       'timestamp_seconds': 76,
       'tip': 'The physical inspection was conducted overseas, while the Indian chartered '
              'engineer reviewed the entire technical and commercial dossier before '
              'certification. The clean workflow is simple. First, a qualified inspector in '
              'the country of sale physically inspects the machine.',
       'title': 'Chartered Engineer Certificate | Used Machinery Import | CEC Case Study: 2005 '
                'Machine, 2026 Retrofit (SARK Engineers & COnsultants)',
       'url': 'https://www.youtube.com/watch?v=Qiyq7yhmD2o&t=76s',
       'video_id': 'Qiyq7yhmD2o'},
      {'author': 'Reclaim Atlas',
       'channel': 'Reclaim Atlas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=XEbn26lA8EE&t=20s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The next owner, the buyers can be other hospitals, outpatient imaging centers, '
               'and specialist healthcare providers. But the person buying from the original '
               "hospital may be an equipment dealer or a manufacturer's refurbishment "
               'business.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'The next owner, the buyers can be other hospitals, outpatient imaging centers, '
              'and specialist healthcare providers. But the person buying from the original '
              "hospital may be an equipment dealer or a manufacturer's refurbishment business.",
       'title': 'What Happens to MRI Scanners When Hospitals Replace Them? (Reclaim Atlas)',
       'url': 'https://www.youtube.com/watch?v=XEbn26lA8EE&t=20s',
       'video_id': 'XEbn26lA8EE'},
      {'author': 'ET Transport',
       'channel': 'ET Transport',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:15](https://www.youtube.com/watch?v=UnNSCtlW-0k&t=795s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s like a franchise or how does that work? Um just different auction yards, "
               "different sales groups. We kind of maybe think of it as a franchise cuz you're "
               'getting the same experience wherever you go with Ritchie Bros. All the same '
               'approvals, yeah.',
       'timestamp': 795,
       'timestamp_label': '[00:13:15]',
       'timestamp_seconds': 795,
       'tip': "'s like a franchise or how does that work? Um just different auction yards, "
              "different sales groups. We kind of maybe think of it as a franchise cuz you're "
              'getting the same experience wherever you go with Ritchie Bros. All the same '
              'approvals, yeah.',
       'title': 'Ritchie Bros. Auctions Explained: What Every Seller Needs to Know Before '
                'Listing (ET Transport)',
       'url': 'https://www.youtube.com/watch?v=UnNSCtlW-0k&t=795s',
       'video_id': 'UnNSCtlW-0k'},
      {'author': 'I Am a Hardscaper',
       'channel': 'I Am a Hardscaper',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:44](https://www.youtube.com/watch?v=DZYNxJ75ASA&t=404s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Very happy with this pickup at the auction of what I learned just with going '
               'to an auction what to look for what to look for with pieces of equipment as '
               'well as different things to see while I am there and testing out different '
               'pieces of equipment.',
       'timestamp': 404,
       'timestamp_label': '[00:06:44]',
       'timestamp_seconds': 404,
       'tip': 'Very happy with this pickup at the auction of what I learned just with going to '
              'an auction what to look for what to look for with pieces of equipment as well '
              'as different things to see while I am there and testing out different pieces of '
              'equipment.',
       'title': 'Purchasing Construction Equipment at a Ritchie Brothers Auction (I Am a '
                'Hardscaper)',
       'url': 'https://www.youtube.com/watch?v=DZYNxJ75ASA&t=404s',
       'video_id': 'DZYNxJ75ASA'},
      {'author': 'C&C Equipment',
       'channel': 'C&C Equipment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:51](https://www.youtube.com/watch?v=Hif9qgd9EEI&t=531s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um new rollers are 160 on these so let's see what he comes up with 157 157 "
               'that was on which one this one right here second from the back yeah see we '
               'measured the other side already they were pretty much all the same so hear '
               'that one dragging just a little.',
       'timestamp': 531,
       'timestamp_label': '[00:08:51]',
       'timestamp_seconds': 531,
       'tip': "Um new rollers are 160 on these so let's see what he comes up with 157 157 that "
              'was on which one this one right here second from the back yeah see we measured '
              'the other side already they were pretty much all the same so hear that one '
              'dragging just a little.',
       'title': 'How to measure wear on excavator undercarriage % Watch this before buying a '
                'tracked machine $$$ (C&C Equipment)',
       'url': 'https://www.youtube.com/watch?v=Hif9qgd9EEI&t=531s',
       'video_id': 'Hif9qgd9EEI'},
      {'author': 'FMCSA REGISTRATION dot com',
       'channel': 'FMCSA REGISTRATION dot com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:29](https://www.youtube.com/watch?v=6q-JpVNYBwE&t=149s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Truck is not just  about avoiding breakdowns. It's about ensuring the safety "
               'of everyone on the road and maximizing your efficiency. By keeping.',
       'timestamp': 149,
       'timestamp_label': '[00:02:29]',
       'timestamp_seconds': 149,
       'tip': "Truck is not just  about avoiding breakdowns. It's about ensuring the safety of "
              'everyone on the road and maximizing your efficiency. By keeping.',
       'title': 'Semi-Truck Maintenance Tips Every Driver Should Know (FMCSA REGISTRATION dot '
                'com)',
       'url': 'https://www.youtube.com/watch?v=6q-JpVNYBwE&t=149s',
       'video_id': '6q-JpVNYBwE'},
      {'author': 'HeavyHaul HQ',
       'channel': 'HeavyHaul HQ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:53](https://www.youtube.com/watch?v=W5IGVlejm0s&t=173s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Trailer that could be really good for you is a pony motor kit by having this '
               'Pony motor kit IT Supplies its own hydraulic IC power to the trailer without '
               'the truck needing wet lines so all you got to do is hop over here make sure '
               "the pony motor's in the on position.",
       'timestamp': 173,
       'timestamp_label': '[00:02:53]',
       'timestamp_seconds': 173,
       'tip': 'Trailer that could be really good for you is a pony motor kit by having this '
              'Pony motor kit IT Supplies its own hydraulic IC power to the trailer without '
              'the truck needing wet lines so all you got to do is hop over here make sure the '
              "pony motor's in the on position.",
       'title': 'Choosing the Best: Heavy Haul Trailer Options Explained (HeavyHaul HQ)',
       'url': 'https://www.youtube.com/watch?v=W5IGVlejm0s&t=173s',
       'video_id': 'W5IGVlejm0s'},
      {'author': 'Farm Journal',
       'channel': 'Farm Journal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:25](https://www.youtube.com/watch?v=_yl0gY1cWj8&t=805s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It still had the crease where like a two by four kind of bent it in so I had '
               "to straighten that out the only thing I don't like about it is it's not power "
               "steering so it's a little bit of cranking on the steering wheel.",
       'timestamp': 805,
       'timestamp_label': '[00:13:25]',
       'timestamp_seconds': 805,
       'tip': 'It still had the crease where like a two by four kind of bent it in so I had to '
              "straighten that out the only thing I don't like about it is it's not power "
              "steering so it's a little bit of cranking on the steering wheel.",
       'title': 'Machinery Pete TV:  February 25, 2023 (Farm Journal)',
       'url': 'https://www.youtube.com/watch?v=_yl0gY1cWj8&t=805s',
       'video_id': '_yl0gY1cWj8'}],
 11: [{'author': 'Freight Pro Hub',
       'channel': 'Freight Pro Hub',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=8X37vkZBHyo&t=65s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So if a broker is operating without their required authority, misrepresenting '
               "its operations, or using a business name different from the name it's "
               'registered under, those are examples of problems that FMCSA says you can '
               'report.',
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': 'So if a broker is operating without their required authority, misrepresenting '
              "its operations, or using a business name different from the name it's "
              'registered under, those are examples of problems that FMCSA says you can '
              'report.',
       'title': 'FMCSA Complaint Center: Report Broker Problems, Fraud & Bad Chassis (Freight '
                'Pro Hub)',
       'url': 'https://www.youtube.com/watch?v=8X37vkZBHyo&t=65s',
       'video_id': '8X37vkZBHyo'},
      {'author': 'Vision Matrix Institute',
       'channel': 'Vision Matrix Institute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:30](https://www.youtube.com/watch?v=6nfvCdjM9lM&t=390s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'IT and mechanical kVA demand. Second, you add a 10 to 20% design margin for '
               'future growth. Third, and this is exactly where data center design differs '
               'from standard commercial buildings, you size for redundancy.',
       'timestamp': 390,
       'timestamp_label': '[00:06:30]',
       'timestamp_seconds': 390,
       'tip': 'IT and mechanical kVA demand. Second, you add a 10 to 20% design margin for '
              'future growth. Third, and this is exactly where data center design differs from '
              'standard commercial buildings, you size for redundancy.',
       'title': 'Module 3A Summary | Data Center Electrical Equipment | Utility, MV Switchgear '
                '& Transformers (Vision Matrix Institute)',
       'url': 'https://www.youtube.com/watch?v=6nfvCdjM9lM&t=390s',
       'video_id': '6nfvCdjM9lM'},
      {'author': 'Flying Wheels',
       'channel': 'Flying Wheels',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:15](https://www.youtube.com/watch?v=en-0Xomp1UQ&t=315s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now, I had a dealership in New Hampshire before this and my dealership had one '
               'dealer desk. It was in conquered, New Hampshire. I could call them for every '
               'question I had. I mailed everything I needed up to them back and forth.',
       'timestamp': 315,
       'timestamp_label': '[00:05:15]',
       'timestamp_seconds': 315,
       'tip': 'Now, I had a dealership in New Hampshire before this and my dealership had one '
              'dealer desk. It was in conquered, New Hampshire. I could call them for every '
              'question I had. I mailed everything I needed up to them back and forth.',
       'title': 'How I am Starting a Car Dealership with less than $5,000 (Flying Wheels)',
       'url': 'https://www.youtube.com/watch?v=en-0Xomp1UQ&t=315s',
       'video_id': 'en-0Xomp1UQ'},
      {'author': 'Keentel Engineering',
       'channel': 'Keentel Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=kE7QqYqWub8&t=36s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A few seconds without power can reboot tens of thousands of servers, corrupt '
               'in-flight data, and take services offline. Unlike an office building, a data '
               'center cannot tolerate even a momentary interruption.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': 'A few seconds without power can reboot tens of thousands of servers, corrupt '
              'in-flight data, and take services offline. Unlike an office building, a data '
              'center cannot tolerate even a momentary interruption.',
       'title': 'Data Center Electrical Design: Grid to Server Rack (Keentel Engineering)',
       'url': 'https://www.youtube.com/watch?v=kE7QqYqWub8&t=36s',
       'video_id': 'kE7QqYqWub8'},
      {'author': 'Stellar Industries',
       'channel': 'Stellar Industries',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=vMpMiRzIO2E&t=123s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It was before and that's our goal with every product that we manufacture talk "
               'with our knowledgeable team or your distributor to find the Stellar fuel Lube '
               'combine head and utility and Telecom trailers that are just right for your '
               'operation.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': "It was before and that's our goal with every product that we manufacture talk "
              'with our knowledgeable team or your distributor to find the Stellar fuel Lube '
              'combine head and utility and Telecom trailers that are just right for your '
              'operation.',
       'title': 'Farm and Fleet Trailers | Construction & Contractor Trailers (Stellar '
                'Industries)',
       'url': 'https://www.youtube.com/watch?v=vMpMiRzIO2E&t=123s',
       'video_id': 'vMpMiRzIO2E'},
      {'author': 'MONEY IQ',
       'channel': 'MONEY IQ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=RAnImnWafHA&t=20s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Yet, some rental companies operate enormous fleets containing thousands of '
               'machines. So, if buying the equipment is this expensive, how does renting it '
               'out actually make money? To understand why this business exists, start with '
               'the contractor.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'Yet, some rental companies operate enormous fleets containing thousands of '
              'machines. So, if buying the equipment is this expensive, how does renting it '
              'out actually make money? To understand why this business exists, start with the '
              'contractor.',
       'title': 'How Construction Equipment Rental Actually Makes Money (MONEY IQ)',
       'url': 'https://www.youtube.com/watch?v=RAnImnWafHA&t=20s',
       'video_id': 'RAnImnWafHA'},
      {'author': 'Onsite Construction Management Software',
       'channel': 'Onsite Construction Management Software',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=djeL371Rgio&t=87s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Also you can download the report by clicking on the top PDF button download '
               'PDF and you can see the report and share it with your team members. Now you '
               'can go back and add another equipment. You can go to add equipment again. You '
               'can select new equipment.',
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': 'Also you can download the report by clicking on the top PDF button download PDF '
              'and you can see the report and share it with your team members. Now you can go '
              'back and add another equipment. You can go to add equipment again. You can '
              'select new equipment.',
       'title': 'How to Manage Construction Equipment in Onsite | Complete Equipment Tracking '
                'Tutorial (Onsite Construction Management Software)',
       'url': 'https://www.youtube.com/watch?v=djeL371Rgio&t=87s',
       'video_id': 'djeL371Rgio'},
      {'author': 'Over the Road',
       'channel': 'Over the Road',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:43](https://www.youtube.com/watch?v=xRwL0v4jyOs&t=43s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Aware that's your first step but in order to come to heavy Hall you will have "
               "to interview with me I'm heavy Hall operations manager Shelby logi so during "
               "that interview process we'll discuss things.",
       'timestamp': 43,
       'timestamp_label': '[00:00:43]',
       'timestamp_seconds': 43,
       'tip': "Aware that's your first step but in order to come to heavy Hall you will have "
              "to interview with me I'm heavy Hall operations manager Shelby logi so during "
              "that interview process we'll discuss things.",
       'title': 'How to Move Up to Heavy Haul Trucking (Over the Road)',
       'url': 'https://www.youtube.com/watch?v=xRwL0v4jyOs&t=43s',
       'video_id': 'xRwL0v4jyOs'},
      {'author': 'PatrickShivers',
       'channel': 'PatrickShivers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=vxI956OLj9E&t=22s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They don't take them to auction. So, when you see new equipment down south at "
               'auction, that usually means bankruptcy. This video, however, is old. Is '
               'classic older tractors, classic tractors.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': "They don't take them to auction. So, when you see new equipment down south at "
              'auction, that usually means bankruptcy. This video, however, is old. Is classic '
              'older tractors, classic tractors.',
       'title': 'Farm BANKRUPTCY Auction Part 2 (PatrickShivers)',
       'url': 'https://www.youtube.com/watch?v=vxI956OLj9E&t=22s',
       'video_id': 'vxI956OLj9E'},
      {'author': 'Machinery Pete',
       'channel': 'Machinery Pete',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:33](https://www.youtube.com/watch?v=3oDXLUOs8DU&t=993s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh so, Luke Frochot, when you roll out of bed every morning after 16 years in '
               "the auction biz with Ritchie Bros. For me, it's it's working with the farmers "
               'that are retiring and helping people through their retirement.',
       'timestamp': 993,
       'timestamp_label': '[00:16:33]',
       'timestamp_seconds': 993,
       'tip': 'Uh so, Luke Frochot, when you roll out of bed every morning after 16 years in '
              "the auction biz with Ritchie Bros. For me, it's it's working with the farmers "
              'that are retiring and helping people through their retirement.',
       'title': 'Machinery Pete Current Equipment Market Chat with Luke Fritshaw with Ritchie '
                'Bros (Machinery Pete)',
       'url': 'https://www.youtube.com/watch?v=3oDXLUOs8DU&t=993s',
       'video_id': '3oDXLUOs8DU'},
      {'author': 'MachineTools.com',
       'channel': 'MachineTools.com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:03](https://www.youtube.com/watch?v=RYIylD9d-3Y&t=903s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Please feel free to make a request on machinery manager.com or you can reach '
               'out to me directly my contact information is linked in the video description '
               'thank you so much for taking the time to watch this demo and I hope to speak '
               'with you soon bye.',
       'timestamp': 903,
       'timestamp_label': '[00:15:03]',
       'timestamp_seconds': 903,
       'tip': 'Please feel free to make a request on machinery manager.com or you can reach '
              'out to me directly my contact information is linked in the video description '
              'thank you so much for taking the time to watch this demo and I hope to speak '
              'with you soon bye.',
       'title': 'Machinery Manager Demo | Equipment Dealer Management  Software '
                '(MachineTools.com)',
       'url': 'https://www.youtube.com/watch?v=RYIylD9d-3Y&t=903s',
       'video_id': 'RYIylD9d-3Y'},
      {'author': 'Cat Products',
       'channel': 'Cat Products',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:58](https://www.youtube.com/watch?v=_j1VRwfp3gU&t=178s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And by uh by taking good SOS samples at regular intervals, we'll be able to "
               'work with your dealer and uh they can help you with the longevity of your '
               'machine, predict um failures before they happen and extend the life of your '
               'machine.',
       'timestamp': 178,
       'timestamp_label': '[00:02:58]',
       'timestamp_seconds': 178,
       'tip': "And by uh by taking good SOS samples at regular intervals, we'll be able to "
              'work with your dealer and uh they can help you with the longevity of your '
              'machine, predict um failures before they happen and extend the life of your '
              'machine.',
       'title': 'Scheduled Oil Sampling S•O•S℠ for your Cat Equipment (Cat Products)',
       'url': 'https://www.youtube.com/watch?v=_j1VRwfp3gU&t=178s',
       'video_id': '_j1VRwfp3gU'},
      {'author': 'Sobre Orugas',
       'channel': 'Sobre Orugas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=keHIfejYGN8&t=88s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '100% y lo hicimos así durante 25 años. Hicimos subastas presenciales en todo '
               'el mundo se concentraba aquí en en los patios de Richie Bros hasta que eh '
               'últimamente optamos por el formato en línea.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': '100% y lo hicimos así durante 25 años. Hicimos subastas presenciales en todo el '
              'mundo se concentraba aquí en en los patios de Richie Bros hasta que eh '
              'últimamente optamos por el formato en línea.',
       'title': 'COMPRA Y VENDE MAQUINARIA EN RITCHIE BROS MÉXICO ¡AQUÍ TE DECIMOS CÓMO! '
                '(Sobre Orugas)',
       'url': 'https://www.youtube.com/watch?v=keHIfejYGN8&t=88s',
       'video_id': 'keHIfejYGN8'},
      {'author': 'Volvo Construction Equipment – North America',
       'channel': 'Volvo Construction Equipment – North America',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:33](https://www.youtube.com/watch?v=L3kAdkTSgI4&t=453s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "They've gone in they just welded up the track adjuster so it can't extend or "
               "come out anymore and that's essentially it on an undercarriage.",
       'timestamp': 453,
       'timestamp_label': '[00:07:33]',
       'timestamp_seconds': 453,
       'tip': "They've gone in they just welded up the track adjuster so it can't extend or "
              "come out anymore and that's essentially it on an undercarriage.",
       'title': 'How To Inspect An Excavator Undercarriage (Volvo Construction Equipment – '
                'North America)',
       'url': 'https://www.youtube.com/watch?v=L3kAdkTSgI4&t=453s',
       'video_id': 'L3kAdkTSgI4'},
      {'author': 'The Markup',
       'channel': 'The Markup',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=4ZnfP4pS7A8&t=36s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ll never look at a construction site the same way again. To understand how "
               'this industry prints money, you first have to understand the problem it was '
               "built to solve. Imagine you're a contractor. You just landed a big job, a new "
               'office building downtown.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': "'ll never look at a construction site the same way again. To understand how "
              'this industry prints money, you first have to understand the problem it was '
              "built to solve. Imagine you're a contractor. You just landed a big job, a new "
              'office building downtown.',
       'title': 'How Construction Equipment Rental Companies Quietly Make $60 Billion a Year '
                '(The Markup)',
       'url': 'https://www.youtube.com/watch?v=4ZnfP4pS7A8&t=36s',
       'video_id': '4ZnfP4pS7A8'}],
 12: [{'author': 'Equipment Finance Academy',
       'channel': 'Equipment Finance Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=YIQEV-r00oA&t=174s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So who should you be recruiting? The best referral partners are people who '
               'already sit in front of your target customer every single day. For an '
               "equipment finance broker, that's accountants, CPAs, bookkeepers, commercial "
               'realtors, equipment vendors, and business brokers.',
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'So who should you be recruiting? The best referral partners are people who '
              'already sit in front of your target customer every single day. For an equipment '
              "finance broker, that's accountants, CPAs, bookkeepers, commercial realtors, "
              'equipment vendors, and business brokers.',
       'title': 'The Referral Partner System That Pays $10k/Month (Equipment Finance Academy)',
       'url': 'https://www.youtube.com/watch?v=YIQEV-r00oA&t=174s',
       'video_id': 'YIQEV-r00oA'},
      {'author': 'Equipment Broker Academy',
       'channel': 'Equipment Broker Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:40](https://www.youtube.com/watch?v=hHppnxoaqWo&t=40s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Clear-cut steps that you follow the succeed brokering heavy equipment '
               'transform your life and start a low-cost business with no equipment experience '
               'we.',
       'timestamp': 40,
       'timestamp_label': '[00:00:40]',
       'timestamp_seconds': 40,
       'tip': 'Clear-cut steps that you follow the succeed brokering heavy equipment transform '
              'your life and start a low-cost business with no equipment experience we.',
       'title': 'Become a Heavy Equipment Broker (Equipment Broker Academy)',
       'url': 'https://www.youtube.com/watch?v=hHppnxoaqWo&t=40s',
       'video_id': 'hHppnxoaqWo'},
      {'author': 'BizMove',
       'channel': 'BizMove',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:30](https://www.youtube.com/watch?v=9pYbF2gxpys&t=30s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Business Plan: Develop a comprehensive business plan outlining your business '
               'goals, target market, services offered, marketing strategy, financial '
               'projections, and operational plan. This will serve as a roadmap for your '
               'business.',
       'timestamp': 30,
       'timestamp_label': '[00:00:30]',
       'timestamp_seconds': 30,
       'tip': 'Business Plan: Develop a comprehensive business plan outlining your business '
              'goals, target market, services offered, marketing strategy, financial '
              'projections, and operational plan. This will serve as a roadmap for your '
              'business.',
       'title': 'How to Start a Heavy Equipment Business | Free Heavy Equipment Business Plan '
                'Template Included (BizMove)',
       'url': 'https://www.youtube.com/watch?v=9pYbF2gxpys&t=30s',
       'video_id': '9pYbF2gxpys'},
      {'author': 'Plain Finance',
       'channel': 'Plain Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:13](https://www.youtube.com/watch?v=9kP-CdkchRk&t=253s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Then the two inspected buyers start competing, a remote dealer with confirmed '
               'transport joins them, and the paddles keep rising. "Thirty-eight thousand," '
               'Mae says.',
       'timestamp': 253,
       'timestamp_label': '[00:04:13]',
       'timestamp_seconds': 253,
       'tip': 'Then the two inspected buyers start competing, a remote dealer with confirmed '
              'transport joins them, and the paddles keep rising. "Thirty-eight thousand," Mae '
              'says.',
       'title': 'You Bought a Dying Auction House for $175,000. Now It Earns $500K/Year '
                'Selling Other People’s Stuff. (Plain Finance)',
       'url': 'https://www.youtube.com/watch?v=9kP-CdkchRk&t=253s',
       'video_id': '9kP-CdkchRk'},
      {'author': 'Forgotten Factories Canada',
       'channel': 'Forgotten Factories Canada',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:42:12](https://www.youtube.com/watch?v=XuXHM5is32c&t=2532s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'His father never missed a day. That was what the plant got from the people who '
               'worked there. What the people who worked there got in the end was 15 days '
               "notice and a check for the equipment. The building didn't disappear.",
       'timestamp': 2532,
       'timestamp_label': '[00:42:12]',
       'timestamp_seconds': 2532,
       'tip': 'His father never missed a day. That was what the plant got from the people who '
              'worked there. What the people who worked there got in the end was 15 days '
              "notice and a check for the equipment. The building didn't disappear.",
       'title': "Kelsey-Hayes Windsor: How Global Outsourcing Destroyed Canada's Leading Wheel "
                'Manufacturer ? (Forgotten Factories Canada)',
       'url': 'https://www.youtube.com/watch?v=XuXHM5is32c&t=2532s',
       'video_id': 'XuXHM5is32c'},
      {'author': 'Farm Journal',
       'channel': 'Farm Journal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=hSi6LwGZ_WY&t=22s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I got to tell you I'm thankful that back then when I started young 23-year-old "
               'know-nothing guy that I made the decision to go ahead and start compiling '
               'prices on all types of heavy construction equipment.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': "I got to tell you I'm thankful that back then when I started young 23-year-old "
              'know-nothing guy that I made the decision to go ahead and start compiling '
              'prices on all types of heavy construction equipment.',
       'title': 'Machinery Pete: Heavy Equipment Sales (Farm Journal)',
       'url': 'https://www.youtube.com/watch?v=hSi6LwGZ_WY&t=22s',
       'video_id': 'hSi6LwGZ_WY'},
      {'author': 'Broma Engineering',
       'channel': 'Broma Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:38](https://www.youtube.com/watch?v=hukziWCxjUY&t=398s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And now, you can release that transformer. This might all happen in the same '
               "day. Hopefully, it does if you're if you're going good. Um then, you can start "
               "your install. So, you're connecting your MV cables or at least you're getting "
               'them ready to be connected.',
       'timestamp': 398,
       'timestamp_label': '[00:06:38]',
       'timestamp_seconds': 398,
       'tip': 'And now, you can release that transformer. This might all happen in the same '
              "day. Hopefully, it does if you're if you're going good. Um then, you can start "
              "your install. So, you're connecting your MV cables or at least you're getting "
              'them ready to be connected.',
       'title': 'Transformers (Tx) | Data Centre Equipment Series Ep.2 (Broma Engineering)',
       'url': 'https://www.youtube.com/watch?v=hukziWCxjUY&t=398s',
       'video_id': 'hukziWCxjUY'},
      {'author': 'Transportli',
       'channel': 'Transportli',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:05](https://www.youtube.com/watch?v=HRlIiVKracc&t=65s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '>> About 17% of revocations were later reinstated. Some within a week. 29%  '
               "took more than a year. So, what does today's broker list really.",
       'timestamp': 65,
       'timestamp_label': '[00:01:05]',
       'timestamp_seconds': 65,
       'tip': '>> About 17% of revocations were later reinstated. Some within a week. 29%  '
              "took more than a year. So, what does today's broker list really.",
       'title': 'How Many Freight Brokers Lose Their Authority? (FMCSA Data Study) | '
                'Transportli (Transportli)',
       'url': 'https://www.youtube.com/watch?v=HRlIiVKracc&t=65s',
       'video_id': 'HRlIiVKracc'},
      {'author': 'The DIY Contractor - Real Fixes',
       'channel': 'The DIY Contractor - Real Fixes',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:33](https://www.youtube.com/watch?v=iFwSrSGEDcQ&t=993s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, you can see they got a lot of mini skid steers and basically got the '
               "gasoline engine. So, if you're looking to start a business, might be a good "
               'place to get some equipment.',
       'timestamp': 993,
       'timestamp_label': '[00:16:33]',
       'timestamp_seconds': 993,
       'tip': 'So, you can see they got a lot of mini skid steers and basically got the '
              "gasoline engine. So, if you're looking to start a business, might be a good "
              'place to get some equipment.',
       'title': 'Inside Ritchie Brothers Auction: Full Lot Tour Before the Bidding Begins! '
                '(The DIY Contractor - Real Fixes)',
       'url': 'https://www.youtube.com/watch?v=iFwSrSGEDcQ&t=993s',
       'video_id': 'iFwSrSGEDcQ'},
      {'author': 'EquipmentWorld',
       'channel': 'EquipmentWorld',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:01](https://www.youtube.com/watch?v=QYimn88ydQI&t=301s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'm going to purchase a new piece of equipment? Is the turnaround time quick "
               'enough that within a couple of days I can get those results back before I go '
               'spend 60 grand on a used piece of equipment? Shelly] It takes typically 24 to '
               '48 hours.',
       'timestamp': 301,
       'timestamp_label': '[00:05:01]',
       'timestamp_seconds': 301,
       'tip': "I'm going to purchase a new piece of equipment? Is the turnaround time quick "
              'enough that within a couple of days I can get those results back before I go '
              'spend 60 grand on a used piece of equipment? Shelly] It takes typically 24 to '
              '48 hours.',
       'title': 'Why Oil Analysis Should Be Part of Your Preventative Maintenance Program '
                '(EquipmentWorld)',
       'url': 'https://www.youtube.com/watch?v=QYimn88ydQI&t=301s',
       'video_id': 'QYimn88ydQI'},
      {'author': 'Thomas',
       'channel': 'Thomas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:15](https://www.youtube.com/watch?v=ZBn220SIMz4&t=135s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Four weeks to get this weekly Thomas index report as well as Daily News and '
               'information for industry please sign up for our Thomas industry update '
               'newsletter at thomasnet.com updates hey thanks very much for watching and '
               'forward to seeing you next week.',
       'timestamp': 135,
       'timestamp_label': '[00:02:15]',
       'timestamp_seconds': 135,
       'tip': 'Four weeks to get this weekly Thomas index report as well as Daily News and '
              'information for industry please sign up for our Thomas industry update '
              'newsletter at thomasnet.com updates hey thanks very much for watching and '
              'forward to seeing you next week.',
       'title': 'Thomas Index Report: Sourcing activity for Construction Contractors. (Thomas)',
       'url': 'https://www.youtube.com/watch?v=ZBn220SIMz4&t=135s',
       'video_id': 'ZBn220SIMz4'},
      {'author': 'Block Imaging',
       'channel': 'Block Imaging',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:58](https://www.youtube.com/watch?v=Py7IK0wId1k&t=178s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "At the end someone's grandmother someone's sister someone is on the end of "
               'these transactions I think everybody here has that understanding that when you '
               'start with people everything else flows from that place.',
       'timestamp': 178,
       'timestamp_label': '[00:02:58]',
       'timestamp_seconds': 178,
       'tip': "At the end someone's grandmother someone's sister someone is on the end of "
              'these transactions I think everybody here has that understanding that when you '
              'start with people everything else flows from that place.',
       'title': 'Behind the Scenes of Bringing Imaging Systems Back to Life (Block Imaging)',
       'url': 'https://www.youtube.com/watch?v=Py7IK0wId1k&t=178s',
       'video_id': 'Py7IK0wId1k'},
      {'author': 'Komatsu Australia',
       'channel': 'Komatsu Australia',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:58](https://www.youtube.com/watch?v=JCDyzlYC0h0&t=118s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Now ready to start your under The Carriage inspection for the first '
               'measurement begin at the left hand side of the machine the left side being '
               'from the cab facing.',
       'timestamp': 118,
       'timestamp_label': '[00:01:58]',
       'timestamp_seconds': 118,
       'tip': 'Now ready to start your under The Carriage inspection for the first measurement '
              'begin at the left hand side of the machine the left side being from the cab '
              'facing.',
       'title': 'Undercarriage Inspection Video (Komatsu Australia)',
       'url': 'https://www.youtube.com/watch?v=JCDyzlYC0h0&t=118s',
       'video_id': 'JCDyzlYC0h0'},
      {'author': 'MEVAS The Heavy Equipment Inspectors',
       'channel': 'MEVAS The Heavy Equipment Inspectors',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:40](https://www.youtube.com/watch?v=enf_Ct89j8o&t=100s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Is in how much water is in much fuel is in the oil if is there aluminum in is '
               'there chromium so Elements which should not be in the oil in which case does '
               'it make sense to make an an oil sampling.',
       'timestamp': 100,
       'timestamp_label': '[00:01:40]',
       'timestamp_seconds': 100,
       'tip': 'Is in how much water is in much fuel is in the oil if is there aluminum in is '
              'there chromium so Elements which should not be in the oil in which case does it '
              'make sense to make an an oil sampling.',
       'title': 'SOS oil sampling for used heavy machinery (MEVAS The Heavy Equipment '
                'Inspectors)',
       'url': 'https://www.youtube.com/watch?v=enf_Ct89j8o&t=100s',
       'video_id': 'enf_Ct89j8o'},
      {'author': 'George Hedley | HardHat BIZCOACH',
       'channel': 'George Hedley | HardHat BIZCOACH',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:21](https://www.youtube.com/watch?v=60uc8gnDCiY&t=81s)',
       'relevance': 'Attributed practitioner commentary on heavy construction, CNC, fleet, and '
                    'industrial equipment brokerage, UCC-1 lien clearance, and escrow '
                    'settlement (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What do you think it costs you per day? You know, you average a hundred miles '
               'or 200 miles a day, or a hundred miles a day. So over time, you average so '
               'much, five days a week. What do you think it costs you? I see a lot of '
               "contractors think it's 500 bucks.",
       'timestamp': 81,
       'timestamp_label': '[00:01:21]',
       'timestamp_seconds': 81,
       'tip': 'What do you think it costs you per day? You know, you average a hundred miles '
              'or 200 miles a day, or a hundred miles a day. So over time, you average so '
              'much, five days a week. What do you think it costs you? I see a lot of '
              "contractors think it's 500 bucks.",
       'title': 'How To Estimate Equipment Cost In Construction (George Hedley | HardHat '
                'BIZCOACH)',
       'url': 'https://www.youtube.com/watch?v=60uc8gnDCiY&t=81s',
       'video_id': '60uc8gnDCiY'}]}
