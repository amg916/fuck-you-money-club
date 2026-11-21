"""Curated 180-citation Tax Lien Investing baseline (15 per chapter across Q1-Q12) mined strictly from verified Tax Lien Investing YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'business',
     'certificate',
     'certificates',
     'certified',
     'check',
     'client',
     'clients',
     'code',
     'comparison',
     'compounding',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deed',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'budget',
     'buyer',
     'certificate',
     'certificates',
     'certified',
     'check',
     'code',
     'comparison',
     'compounding',
     'contract',
     'costs',
     'counter',
     'county',
     'curve',
     'customer',
     'data',
     'days',
     'decision',
     'deed',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'cash',
     'cashflow',
     'certificate',
     'certificates',
     'certified',
     'check',
     'code',
     'commission',
     'comparison',
     'compounding',
     'cost',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deed',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'budget',
     'capital',
     'certificate',
     'certificates',
     'certified',
     'check',
     'code',
     'comparison',
     'compounding',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deed',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
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
 5: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'audit',
     'automatic',
     'avoid',
     'bankruptcy',
     'bid',
     'brownfield',
     'certificate',
     'certificates',
     'certified',
     'check',
     'clawback',
     'code',
     'comparison',
     'compounding',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deed',
     'desk',
     'diligence',
     'directed',
     'dispute',
     'down',
     'driven',
     'edge',
     'fail',
     'mistake',
     'mistakes',
     'problem',
     'risk',
     'risks',
     'trap',
     'traps'},
 6: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'certificate',
     'certificates',
     'certified',
     'check',
     'client',
     'code',
     'comparison',
     'compounding',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deal',
     'deed',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
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
 7: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'certificate',
     'certificates',
     'certified',
     'check',
     'checklist',
     'code',
     'comparison',
     'compounding',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deed',
     'delivery',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
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
 8: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'api',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'certificate',
     'certificates',
     'certified',
     'check',
     'code',
     'comparison',
     'compounding',
     'costs',
     'counter',
     'county',
     'crm',
     'curve',
     'data',
     'database',
     'days',
     'deed',
     'desk',
     'diligence',
     'directed',
     'down',
     'driven',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'120',
     '362',
     '401k',
     'action',
     'aerial',
     'agreement',
     'arizona',
     'auctions',
     'automatic',
     'bankruptcy',
     'bid',
     'brownfield',
     'certificate',
     'certificates',
     'certified',
     'check',
     'code',
     'comparison',
     'compliance',
     'compounding',
     'contract',
     'costs',
     'counter',
     'county',
     'curve',
     'data',
     'days',
     'deed',
     'desk',
     'diligence',
     'directed',
     'disclosure',
     'down',
     'driven',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'120',
      '362',
      '401k',
      'action',
      'aerial',
      'agent',
      'ai',
      'arizona',
      'auctions',
      'automate',
      'automatic',
      'automation',
      'bankruptcy',
      'bid',
      'brownfield',
      'certificate',
      'certificates',
      'certified',
      'check',
      'code',
      'comparison',
      'compounding',
      'costs',
      'counter',
      'county',
      'curve',
      'dashboard',
      'data',
      'days',
      'deed',
      'desk',
      'diligence',
      'directed',
      'down',
      'driven',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'120',
      '362',
      '401k',
      'action',
      'aerial',
      'arizona',
      'auctions',
      'automatic',
      'bankruptcy',
      'bid',
      'brownfield',
      'certificate',
      'certificates',
      'certified',
      'check',
      'code',
      'comparison',
      'compounding',
      'contractor',
      'costs',
      'counter',
      'county',
      'curve',
      'data',
      'days',
      'deed',
      'desk',
      'diligence',
      'directed',
      'down',
      'driven',
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
 12: {'120',
      '362',
      '401k',
      'action',
      'aerial',
      'arizona',
      'auctions',
      'automatic',
      'bankruptcy',
      'bid',
      'brownfield',
      'certificate',
      'certificates',
      'certified',
      'check',
      'code',
      'comparison',
      'compounding',
      'costs',
      'counter',
      'county',
      'curve',
      'data',
      'day',
      'days',
      'deed',
      'desk',
      'diligence',
      'directed',
      'down',
      'driven',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Lien Ledger',
      'channel': 'Lien Ledger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:12](https://www.youtube.com/watch?v=ul1onF24UbM&t=432s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In Florida, you can bid on certificates and later on deeds. One cheap lien '
              "teaches you a county's process better than 10 videos. Before any bid, do three "
              "things. Check the property's value. Check the state's redemption rules. Skip "
              'vacant lots and ruined buildings.',
      'timestamp': 432,
      'timestamp_label': '[00:07:12]',
      'timestamp_seconds': 432,
      'tip': 'In Florida, you can bid on certificates and later on deeds. One cheap lien '
             "teaches you a county's process better than 10 videos. Before any bid, do three "
             "things. Check the property's value. Check the state's redemption rules. Skip "
             'vacant lots and ruined buildings.',
      'title': 'Tax Liens vs Tax Deeds: Which One Should You Buy? (Lien Ledger)',
      'url': 'https://www.youtube.com/watch?v=ul1onF24UbM&t=432s',
      'video_id': 'ul1onF24UbM'},
     {'author': 'Tax Lien School Highlights - Dustin Hahn',
      'channel': 'Tax Lien School Highlights - Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=prp5x8F5I60&t=57s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so, all we got to do is click on the parcel ID here. It's going to take us "
              "right to the county website. 5 acres with an opening bid of yeah 2492. What's "
              "it actually worth though? So the actual market value the county is saying it's "
              'worth about 10 grand.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "And so, all we got to do is click on the parcel ID here. It's going to take us "
             "right to the county website. 5 acres with an opening bid of yeah 2492. What's it "
             "actually worth though? So the actual market value the county is saying it's "
             'worth about 10 grand.',
      'title': 'Florida Tax Deed Auctions on RealAuction: How to Check Real Value Fast (Tax '
               'Lien School Highlights - Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=prp5x8F5I60&t=57s',
      'video_id': 'prp5x8F5I60'},
     {'author': 'Smart Capital',
      'channel': 'Smart Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:24](https://www.youtube.com/watch?v=TL6AIsoe5m0&t=1164s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's the worked example I promised. Imagine a single-family home in a Florida "
              'county. Conservative market value, $200,000. Delinquent tax lien opening bid, '
              '$8,000.',
      'timestamp': 1164,
      'timestamp_label': '[00:19:24]',
      'timestamp_seconds': 1164,
      'tip': "Here's the worked example I promised. Imagine a single-family home in a Florida "
             'county. Conservative market value, $200,000. Delinquent tax lien opening bid, '
             '$8,000.',
      'title': 'Tax Lien Investing for Beginners: 8-18% Interest? Risks & Auction Mistakes '
               '(Smart Capital)',
      'url': 'https://www.youtube.com/watch?v=TL6AIsoe5m0&t=1164s',
      'video_id': 'TL6AIsoe5m0'},
     {'author': 'Tax Sales Rebels',
      'channel': 'Tax Sales Rebels',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=dO80b3ivtWM&t=48s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So here it tells me it's a residential area. It tells me that the land in "
              'itself is 4,000, the building 15,000. So total this is estimated market value '
              'according to the county, right? You can still make some profit here.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': "So here it tells me it's a residential area. It tells me that the land in itself "
             'is 4,000, the building 15,000. So total this is estimated market value according '
             'to the county, right? You can still make some profit here.',
      'title': 'How to Check if a Tax Sale House Is Still There Before You Bid (Tax Sales '
               'Rebels)',
      'url': 'https://www.youtube.com/watch?v=dO80b3ivtWM&t=48s',
      'video_id': 'dO80b3ivtWM'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:44](https://www.youtube.com/watch?v=rmXwIKKIDiw&t=764s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "3000 properties that are for sale, and I've been to tax auctions where they "
              "have 30 to 50,000 tax lien certificates. My point is, it's really a business of "
              "abundance. You can buy 'em over the counter. You can buy 'em at the auction.",
      'timestamp': 764,
      'timestamp_label': '[00:12:44]',
      'timestamp_seconds': 764,
      'tip': "3000 properties that are for sale, and I've been to tax auctions where they have "
             "30 to 50,000 tax lien certificates. My point is, it's really a business of "
             "abundance. You can buy 'em over the counter. You can buy 'em at the auction.",
      'title': 'Over The Counter Tax Lien Certificates What Are They How It Works (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=rmXwIKKIDiw&t=764s',
      'video_id': 'rmXwIKKIDiw'},
     {'author': 'Advanta IRA',
      'channel': 'Advanta IRA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:40](https://www.youtube.com/watch?v=RDk1Gksh9R4&t=2860s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh california new york um they're just high value states that your their tax "
              'deed states um where the this is going to be a hot you might as well just try '
              'to find a regular deal on the market um uh any other state.',
      'timestamp': 2860,
      'timestamp_label': '[00:47:40]',
      'timestamp_seconds': 2860,
      'tip': "Uh california new york um they're just high value states that your their tax "
             'deed states um where the this is going to be a hot you might as well just try to '
             'find a regular deal on the market um uh any other state.',
      'title': 'Learn About Tax Lien Investing with Chantelle Owens (Advanta IRA)',
      'url': 'https://www.youtube.com/watch?v=RDk1Gksh9R4&t=2860s',
      'video_id': 'RDk1Gksh9R4'},
     {'author': 'IRS Notices Explained',
      'channel': 'IRS Notices Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=B1e8xDSixVg&t=168s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, what's really interesting about form 1227 is its specific intent. When you "
              "submit this application under Internal Revenue Code 6323J, you aren't just "
              'paying down debt. A successful withdrawal completely removes the notice of '
              'federal tax lien from the public record.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': "Now, what's really interesting about form 1227 is its specific intent. When you "
             "submit this application under Internal Revenue Code 6323J, you aren't just "
             'paying down debt. A successful withdrawal completely removes the notice of '
             'federal tax lien from the public record.',
      'title': 'IRS Tax Lien Explained - Credit, Property, and Release Options (IRS Notices '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=B1e8xDSixVg&t=168s',
      'video_id': 'B1e8xDSixVg'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:13](https://www.youtube.com/watch?v=ES5ZPyHRFMM&t=373s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "True sometimes you'll go to a tax deed sale and things might get bit up to "
              'market value all right no big deal find another auction remember in this.',
      'timestamp': 373,
      'timestamp_label': '[00:06:13]',
      'timestamp_seconds': 373,
      'tip': "True sometimes you'll go to a tax deed sale and things might get bit up to "
             'market value all right no big deal find another auction remember in this.',
      'title': 'Tax Deed investing 101 - Buying $50 Property (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=ES5ZPyHRFMM&t=373s',
      'video_id': 'ES5ZPyHRFMM'},
     {'author': 'Tax Lien School Highlights - Dustin Hahn',
      'channel': 'Tax Lien School Highlights - Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=wemMjCnrX34&t=44s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t deal with the homeowner. You lend the money to the county because the county "
              'is a business. They need to pay their school teachers, their fire trucks, pave '
              'the roads, all that sort of stuff and they count on property tax revenue.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "'t deal with the homeowner. You lend the money to the county because the county "
             'is a business. They need to pay their school teachers, their fire trucks, pave '
             'the roads, all that sort of stuff and they count on property tax revenue.',
      'title': 'Tax Liens vs Tax Deeds - Which To Start With on a Small Budget (Tax Lien '
               'School Highlights - Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=wemMjCnrX34&t=44s',
      'video_id': 'wemMjCnrX34'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:05](https://www.youtube.com/watch?v=2B3hCb362oA&t=305s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It will save you a lot of time and a lot of money in the long run so hope '
              "you've enjoyed the video for more information about the very lucrative tax sell "
              'business check out my website at the tax sell academy.com have a great day '
              'folks bye-bye.',
      'timestamp': 305,
      'timestamp_label': '[00:05:05]',
      'timestamp_seconds': 305,
      'tip': "It will save you a lot of time and a lot of money in the long run so hope you've "
             'enjoyed the video for more information about the very lucrative tax sell '
             'business check out my website at the tax sell academy.com have a great day folks '
             'bye-bye.',
      'title': 'Tax Deed & Tax Sale Research Using GIS! (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=2B3hCb362oA&t=305s',
      'video_id': '2B3hCb362oA'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=tXVBp8vbkT4&t=101s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can earn 18 to 36 percent interest tax liens you can buy tax deed property up '
              "to 90 below market value but just debunking that video that I've seen so.",
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'Can earn 18 to 36 percent interest tax liens you can buy tax deed property up to '
             "90 below market value but just debunking that video that I've seen so.",
      'title': 'Pay The Back Taxes, Get The Property - Tax Lien Lie EXPOSED (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=tXVBp8vbkT4&t=101s',
      'video_id': 'tXVBp8vbkT4'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:08](https://www.youtube.com/watch?v=2g2qJcuuey4&t=188s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cheapest route for more information on the very lucrative tax sale business '
              "check out my website at the tax el academy.com and while you're there download "
              'your FREE copy of the tax sale blueprint have a wonderful day.',
      'timestamp': 188,
      'timestamp_label': '[00:03:08]',
      'timestamp_seconds': 188,
      'tip': 'Cheapest route for more information on the very lucrative tax sale business '
             "check out my website at the tax el academy.com and while you're there download "
             'your FREE copy of the tax sale blueprint have a wonderful day.',
      'title': 'The Tax Foreclosure Certification Process - A Suit to Quiet Title Alternative '
               '(Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=2g2qJcuuey4&t=188s',
      'video_id': '2g2qJcuuey4'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=I9YP4P0-OM0&t=62s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Pennsylvania or pivot to New York and you'll just find better opportunities. "
              'Before you go, I have a free gift for you called the Tax Deed Freedom Blueprint '
              'and this thing is going to show you how to buy tax deed property for 30 to 60% '
              'below market value mortgage free.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "Pennsylvania or pivot to New York and you'll just find better opportunities. "
             'Before you go, I have a free gift for you called the Tax Deed Freedom Blueprint '
             'and this thing is going to show you how to buy tax deed property for 30 to 60% '
             'below market value mortgage free.',
      'title': 'Can You Really Earn 0% Interest on Tax Liens? (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=I9YP4P0-OM0&t=62s',
      'video_id': 'I9YP4P0-OM0'},
     {'author': 'Logan Allec',
      'channel': 'Logan Allec',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=Fl9ZtNoyzj8&t=258s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's say you ow let's say you owe the S IRS $100,000 and you have $200,000 of "
              "equity in your home okay um and let's say you're able to get placed into CNC "
              'status.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': "Let's say you ow let's say you owe the S IRS $100,000 and you have $200,000 of "
             "equity in your home okay um and let's say you're able to get placed into CNC "
             'status.',
      'title': 'Will the IRS Withdraw Your Tax Lien If You Get Into CNC Status? (Logan Allec)',
      'url': 'https://www.youtube.com/watch?v=Fl9ZtNoyzj8&t=258s',
      'video_id': 'Fl9ZtNoyzj8'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=QQ4bx7vLNS4&t=470s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "One here from Linus from Tick Tock Ted and she's asking are there any extra "
              'fees or costs associated with buying a tax lien in Illinois.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': "One here from Linus from Tick Tock Ted and she's asking are there any extra fees "
             'or costs associated with buying a tax lien in Illinois.',
      'title': 'A Treasure HIDDEN IN PLAIN SIGHT: Illinois Tax Liens - Ted Explains (Ted '
               'Thomas)',
      'url': 'https://www.youtube.com/watch?v=QQ4bx7vLNS4&t=470s',
      'video_id': 'QQ4bx7vLNS4'}],
 2: [{'author': 'Global Estate Hub LLC',
      'channel': 'Global Estate Hub LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:21](https://www.youtube.com/watch?v=q4Kqh7Vleyg&t=201s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'From that exact moment, the IRS has exactly 120 days to decide if they want to '
              "redeem the property. There's some fine print to pay attention to. While 120 "
              'days is the federal standard under Title 28 of the US Code, you always have to '
              'check your local laws.',
      'timestamp': 201,
      'timestamp_label': '[00:03:21]',
      'timestamp_seconds': 201,
      'tip': 'From that exact moment, the IRS has exactly 120 days to decide if they want to '
             "redeem the property. There's some fine print to pay attention to. While 120 days "
             'is the federal standard under Title 28 of the US Code, you always have to check '
             'your local laws.',
      'title': 'IRS Right of Redemption Explained: Avoid This Foreclosure Trap! (Global Estate '
               'Hub LLC)',
      'url': 'https://www.youtube.com/watch?v=q4Kqh7Vleyg&t=201s',
      'video_id': 'q4Kqh7Vleyg'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=x3XX9ysKcUA&t=353s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "For example, I've gone to auctions and been on a certificate on a huge stopping "
              'center. They owed 100 thousand dollars in taxes and I bid, I said, "I\'ll pay '
              'the 100 thousand dollars of the taxes. " Because the certificate was going to '
              'pay 16 percent.',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': "For example, I've gone to auctions and been on a certificate on a huge stopping "
             'center. They owed 100 thousand dollars in taxes and I bid, I said, "I\'ll pay '
             'the 100 thousand dollars of the taxes. " Because the certificate was going to '
             'pay 16 percent.',
      'title': 'What Is The Difference Between A Tax Lien And A Tax Deed? (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=x3XX9ysKcUA&t=353s',
      'video_id': 'x3XX9ysKcUA'},
     {'author': 'Quiet Title Michigan',
      'channel': 'Quiet Title Michigan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:55](https://www.youtube.com/watch?v=kJRxvYeK_eU&t=595s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Procedural action we often will put a flat fee of $1400 plus costs a more '
              "complicated matters we may charge different fees if you've got questions or "
              'want to learn more or have specific issues.',
      'timestamp': 595,
      'timestamp_label': '[00:09:55]',
      'timestamp_seconds': 595,
      'tip': 'Procedural action we often will put a flat fee of $1400 plus costs a more '
             "complicated matters we may charge different fees if you've got questions or want "
             'to learn more or have specific issues.',
      'title': 'Quiet Title Process and Timeline (Quiet Title Michigan)',
      'url': 'https://www.youtube.com/watch?v=kJRxvYeK_eU&t=595s',
      'video_id': 'kJRxvYeK_eU'},
     {'author': 'Bankruptcy Explained',
      'channel': 'Bankruptcy Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=m1B_j8n-b9E&t=257s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And how do I stop having to pay these debts that are going to be discharged in '
              'bankruptcy?" You\'re going to file your bankruptcy case, you know, make your '
              'mortgage payment, make your rent payment, pay your utilities, right?',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'And how do I stop having to pay these debts that are going to be discharged in '
             'bankruptcy?" You\'re going to file your bankruptcy case, you know, make your '
             'mortgage payment, make your rent payment, pay your utilities, right?',
      'title': 'Chapter 7 Bankruptcy Process: The Automatic Stay | 50 Bankruptcy Lawyers '
               '(Bankruptcy Explained)',
      'url': 'https://www.youtube.com/watch?v=m1B_j8n-b9E&t=257s',
      'video_id': 'm1B_j8n-b9E'},
     {'author': 'Stacked Legal',
      'channel': 'Stacked Legal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:38](https://www.youtube.com/watch?v=XgowlA2cjZA&t=398s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '002 of the Texas Civil Practice and Remedies Code, a proved violation may '
              'support the greater of $10,000 or actual damages, plus court costs, reasonable '
              'legal fees, and exemplary damages. The person must have known the claim was '
              'fraudulent and intended harm.',
      'timestamp': 398,
      'timestamp_label': '[00:06:38]',
      'timestamp_seconds': 398,
      'tip': '002 of the Texas Civil Practice and Remedies Code, a proved violation may '
             'support the greater of $10,000 or actual damages, plus court costs, reasonable '
             'legal fees, and exemplary damages. The person must have known the claim was '
             'fraudulent and intended harm.',
      'title': 'How to Clear a Title in Texas: Liens, Closing Problems, Quiet Title (Stacked '
               'Legal)',
      'url': 'https://www.youtube.com/watch?v=XgowlA2cjZA&t=398s',
      'video_id': 'XgowlA2cjZA'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:50](https://www.youtube.com/watch?v=0AibTtKKPPU&t=590s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, I can tell you right now, he knows exactly how much he owes you. But you '
              'say, "Well he\'s gonna owe me whatever I paid, plus the 25% penalty, plus if '
              'the county has any associated fees." " So he now is gonna pay you, or he is '
              'gonna pay for that tax deed.',
      'timestamp': 590,
      'timestamp_label': '[00:09:50]',
      'timestamp_seconds': 590,
      'tip': 'Well, I can tell you right now, he knows exactly how much he owes you. But you '
             'say, "Well he\'s gonna owe me whatever I paid, plus the 25% penalty, plus if the '
             'county has any associated fees." " So he now is gonna pay you, or he is gonna '
             'pay for that tax deed.',
      'title': 'What Are The Tax Deed States With No Redemption Period (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=0AibTtKKPPU&t=590s',
      'video_id': '0AibTtKKPPU'},
     {'author': 'Saen Higgins',
      'channel': 'Saen Higgins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:58](https://www.youtube.com/watch?v=EXkUbWWenl0&t=238s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For this argument, when the property owner comes down, to pay off the property '
              "taxes, they go to the county, they don't even know they have a lien. I don't "
              "know I bought a lien on the property. The county's already warned him, because "
              "hey, I know I'm late.",
      'timestamp': 238,
      'timestamp_label': '[00:03:58]',
      'timestamp_seconds': 238,
      'tip': 'For this argument, when the property owner comes down, to pay off the property '
             "taxes, they go to the county, they don't even know they have a lien. I don't "
             "know I bought a lien on the property. The county's already warned him, because "
             "hey, I know I'm late.",
      'title': 'How To Foreclose On A Tax Lien Property (Saen Higgins)',
      'url': 'https://www.youtube.com/watch?v=EXkUbWWenl0&t=238s',
      'video_id': 'EXkUbWWenl0'},
     {'author': 'Premier Wealth Builders',
      'channel': 'Premier Wealth Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=RvfjpH1PWxE&t=58s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Bid up premium whoever pays the highest amount of money will win the proper '
              "whoever pays the highest amount of money will win the property so let's talk "
              'about a couple of States.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Bid up premium whoever pays the highest amount of money will win the proper '
             "whoever pays the highest amount of money will win the property so let's talk "
             'about a couple of States.',
      'title': 'Tax Deed vs Tax Lien: Which State Strategy Makes the Most Money? (Premier '
               'Wealth Builders)',
      'url': 'https://www.youtube.com/watch?v=RvfjpH1PWxE&t=58s',
      'video_id': 'RvfjpH1PWxE'},
     {'author': 'Bob Jablonsky',
      'channel': 'Bob Jablonsky',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=EpqtO6uiV_E&t=84s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '25,000 or less when you request a withdrawal. This includes the assessed tax, '
              'penalties, and interest. If you owe more than $25,000, you may be able to pay '
              'it down to $25,000 and then request a withdrawal.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': '25,000 or less when you request a withdrawal. This includes the assessed tax, '
             'penalties, and interest. If you owe more than $25,000, you may be able to pay it '
             'down to $25,000 and then request a withdrawal.',
      'title': 'How to Withdraw an IRS Tax Lien When You Owe $25,000 or Less (Bob Jablonsky)',
      'url': 'https://www.youtube.com/watch?v=EpqtO6uiV_E&t=84s',
      'video_id': 'EpqtO6uiV_E'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=akAZkzeH2PY&t=57s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Oh, we don\'t do tax liens here." Ask them the question and say, "Well, what '
              'happens in your county when people don\'t pay their property taxes?" And '
              'they\'ll say, "Oh, that\'s the tax defaulted list." Or if you\'re in a deed '
              "state, they'll say that's the sheriff's sale.",
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': '"Oh, we don\'t do tax liens here." Ask them the question and say, "Well, what '
             'happens in your county when people don\'t pay their property taxes?" And '
             'they\'ll say, "Oh, that\'s the tax defaulted list." Or if you\'re in a deed '
             "state, they'll say that's the sheriff's sale.",
      'title': "Tax Liens vs. Tax Deeds: What's the Difference? (Dustin Hahn)",
      'url': 'https://www.youtube.com/watch?v=akAZkzeH2PY&t=57s',
      'video_id': 'akAZkzeH2PY'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:53](https://www.youtube.com/watch?v=7BP12s9Jn2c&t=593s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Four five years you probably have to pay to get it re-certified so keep that in '
              "mind now let's look at another factor.",
      'timestamp': 593,
      'timestamp_label': '[00:09:53]',
      'timestamp_seconds': 593,
      'tip': 'Four five years you probably have to pay to get it re-certified so keep that in '
             "mind now let's look at another factor.",
      'title': 'Quiet Title Vs Tax Foreclosure Certification (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=7BP12s9Jn2c&t=593s',
      'video_id': '7BP12s9Jn2c'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:33](https://www.youtube.com/watch?v=dI48opW6bWQ&t=2553s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So far all the lanes we've been looking at are really a 36 dollar lien I mean "
              "you know go ahead and go down to the cheapest amount and you know let's not "
              'look at maybe you know like a 200 lien or something.',
      'timestamp': 2553,
      'timestamp_label': '[00:42:33]',
      'timestamp_seconds': 2553,
      'tip': "So far all the lanes we've been looking at are really a 36 dollar lien I mean "
             "you know go ahead and go down to the cheapest amount and you know let's not look "
             'at maybe you know like a 200 lien or something.',
      'title': 'TAX LIEN ONLINE AUCTIONS REVIEWED! RESEARCH TAX & ASSESSOR RECORDS (Tax Sale '
               'Secrets)',
      'url': 'https://www.youtube.com/watch?v=dI48opW6bWQ&t=2553s',
      'video_id': 'dI48opW6bWQ'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=K4wAHGQcqzQ&t=167s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can from their sites from there you can determine if they handle everything '
              'themselves or if they contract it out to a third party Auction Company to learn '
              'more about Indiana tax foreclosure laws head on over to Google and just type in '
              'Indiana code.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'You can from their sites from there you can determine if they handle everything '
             'themselves or if they contract it out to a third party Auction Company to learn '
             'more about Indiana tax foreclosure laws head on over to Google and just type in '
             'Indiana code.',
      'title': 'Indiana Tax Sales - Tax Liens (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=K4wAHGQcqzQ&t=167s',
      'video_id': 'K4wAHGQcqzQ'},
     {'author': 'Saen Higgins',
      'channel': 'Saen Higgins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=IH1JGgxRwIg&t=219s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Eye on how this stuff works in so much detail there so there's your little "
              "bonus you guys have been great I'm hoping that was helpful peace out God bless.",
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': "Eye on how this stuff works in so much detail there so there's your little bonus "
             "you guys have been great I'm hoping that was helpful peace out God bless.",
      'title': 'Tax Lien vs Tax Deed [What You Actually Need To Know] (Saen Higgins)',
      'url': 'https://www.youtube.com/watch?v=IH1JGgxRwIg&t=219s',
      'video_id': 'IH1JGgxRwIg'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:43](https://www.youtube.com/watch?v=jwFVT7nCrg8&t=223s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Let alone I have trouble spelling the word saying it sometimes is hard as well '
              "but it's going to be able to do and check for leans to make sure.",
      'timestamp': 223,
      'timestamp_label': '[00:03:43]',
      'timestamp_seconds': 223,
      'tip': 'Let alone I have trouble spelling the word saying it sometimes is hard as well '
             "but it's going to be able to do and check for leans to make sure.",
      'title': 'Tax Lien Investing With Artificial Intelligence 101 (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=jwFVT7nCrg8&t=223s',
      'video_id': 'jwFVT7nCrg8'}],
 3: [{'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=DPKvfqp7T9g&t=103s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That means there's 169 auctions this year. Okay, now, most homeowners will "
              'redeem the tax deed. The county sells those deeds at auction. Now, some of them '
              'will do it very quickly. 10 days, 25 days, whatever. Others wait all the way '
              "'til 365.",
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "That means there's 169 auctions this year. Okay, now, most homeowners will "
             'redeem the tax deed. The county sells those deeds at auction. Now, some of them '
             'will do it very quickly. 10 days, 25 days, whatever. Others wait all the way '
             "'til 365.",
      'title': 'Is Georgia A Tax Lien Or Tax Deed State? (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=DPKvfqp7T9g&t=103s',
      'video_id': 'DPKvfqp7T9g'},
     {'author': 'Realauction',
      'channel': 'Realauction',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=_Ge3YGeNsFg&t=122s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Click on the certificate year to see the certificates within. Please note '
              'between Florida and Arizona, the differences to be known is that Florida has a '
              'maximum interest rate of 18% of which you are purchasing at and Arizona has a '
              'maximum of 16% upon return or redemption.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Click on the certificate year to see the certificates within. Please note '
             'between Florida and Arizona, the differences to be known is that Florida has a '
             'maximum interest rate of 18% of which you are purchasing at and Arizona has a '
             'maximum of 16% upon return or redemption.',
      'title': 'County Held, State Held Sale: Tax Lien *NEW* (Realauction)',
      'url': 'https://www.youtube.com/watch?v=_Ge3YGeNsFg&t=122s',
      'video_id': '_Ge3YGeNsFg'},
     {'author': 'Tax Sale Resources',
      'channel': 'Tax Sale Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=46pI-T2mHZs&t=475s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Is selling for so if you want to narrow down the auctions to to go to um that's "
              "that's an excellent way to do that yeah um I was just I actually brought up our "
              'Arizona um to uh report here let me just hit it up really fast.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': "Is selling for so if you want to narrow down the auctions to to go to um that's "
             "that's an excellent way to do that yeah um I was just I actually brought up our "
             'Arizona um to uh report here let me just hit it up really fast.',
      'title': 'Guide to Arizona Tax Lien Investing (Tax Sale Resources)',
      'url': 'https://www.youtube.com/watch?v=46pI-T2mHZs&t=475s',
      'video_id': '46pI-T2mHZs'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:46](https://www.youtube.com/watch?v=SwH4FFj8oZc&t=46s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you do the math, that's like $49,500 in profit before closing costs, which "
              'is 100x return, which is wild. And so this is a real story. This is true and it '
              "wasn't actually sold by the homeowner. And so this was sold by the county "
              'through a tax sale.',
      'timestamp': 46,
      'timestamp_label': '[00:00:46]',
      'timestamp_seconds': 46,
      'tip': "If you do the math, that's like $49,500 in profit before closing costs, which is "
             '100x return, which is wild. And so this is a real story. This is true and it '
             "wasn't actually sold by the homeowner. And so this was sold by the county "
             'through a tax sale.',
      'title': 'He Bought a $500 Tax Sale House and Sold It for $50,000! (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=SwH4FFj8oZc&t=46s',
      'video_id': 'SwH4FFj8oZc'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:01:47](https://www.youtube.com/watch?v=IMGzMnzQiZQ&t=3707s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Price and we can see any of these all of these different tax Lans that are '
              'available by Price these are all over-the-counter tax Lans now I am looking for '
              'a certain price of tax Lan I looked up a couple of tax Lans earlier.',
      'timestamp': 3707,
      'timestamp_label': '[01:01:47]',
      'timestamp_seconds': 3707,
      'tip': 'Price and we can see any of these all of these different tax Lans that are '
             'available by Price these are all over-the-counter tax Lans now I am looking for '
             'a certain price of tax Lan I looked up a couple of tax Lans earlier.',
      'title': 'The Truth About Online Tax Lien Auctions (Watch Before You Bid) (Tax Sale '
               'Secrets)',
      'url': 'https://www.youtube.com/watch?v=IMGzMnzQiZQ&t=3707s',
      'video_id': 'IMGzMnzQiZQ'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:52](https://www.youtube.com/watch?v=jDYlxXpw-e4&t=1432s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Always know how many they got in that county so I got enough now I want to look '
              "at my margin and if you try to buy for just 20 cents on the dollar it's.",
      'timestamp': 1432,
      'timestamp_label': '[00:23:52]',
      'timestamp_seconds': 1432,
      'tip': 'Always know how many they got in that county so I got enough now I want to look '
             "at my margin and if you try to buy for just 20 cents on the dollar it's.",
      'title': 'Ted Talks: Tax Liens, Tax Deeds, and You w/ Ted Thomas | REtipster 196 '
               '(REtipster)',
      'url': 'https://www.youtube.com/watch?v=jDYlxXpw-e4&t=1432s',
      'video_id': 'jDYlxXpw-e4'},
     {'author': 'Teach Me! Personal Finance',
      'channel': 'Teach Me! Personal Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:19](https://www.youtube.com/watch?v=Yxne6RuhWyg&t=379s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Information further down on the form uh in item 10 you're going to check the "
              'appropriate box whether or not this is an open lien.',
      'timestamp': 379,
      'timestamp_label': '[00:06:19]',
      'timestamp_seconds': 379,
      'tip': "Information further down on the form uh in item 10 you're going to check the "
             'appropriate box whether or not this is an open lien.',
      'title': 'IRS Form 12277 walkthrough (Application for Withdrawal of Filed Notice of '
               'Federal Tax Lien (Teach Me! Personal Finance)',
      'url': 'https://www.youtube.com/watch?v=Yxne6RuhWyg&t=379s',
      'video_id': 'Yxne6RuhWyg'},
     {'author': 'Tax Lien Bootcamp',
      'channel': 'Tax Lien Bootcamp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=wyAiYLlWM6A&t=113s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Four shebang you have to come to the boot camp you would wonder like you have '
              "to put it facing unit here or there's one here so you got lucky today anybody "
              'show me how much it costs to replace an AC using how much it costs to paint and '
              'exterior.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': 'Four shebang you have to come to the boot camp you would wonder like you have to '
             "put it facing unit here or there's one here so you got lucky today anybody show "
             'me how much it costs to replace an AC using how much it costs to paint and '
             'exterior.',
      'title': 'Ga Tax Lien Bootcamp Lead Instructor Case Study on Tax Lien Property (Tax Lien '
               'Bootcamp)',
      'url': 'https://www.youtube.com/watch?v=wyAiYLlWM6A&t=113s',
      'video_id': 'wyAiYLlWM6A'},
     {'author': 'IAAO',
      'channel': 'IAAO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=1rrID1N_BEY&t=80s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That GIS has in the assessor's office but I typically like to boil it down to "
              'two main things more fair and equitable valuations at a reduced cost I think '
              'one.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': "That GIS has in the assessor's office but I typically like to boil it down to "
             'two main things more fair and equitable valuations at a reduced cost I think '
             'one.',
      'title': 'How Assessors Use GIS (IAAO)',
      'url': 'https://www.youtube.com/watch?v=1rrID1N_BEY&t=80s',
      'video_id': '1rrID1N_BEY'},
     {'author': 'Law Offices of Darrin T. Mish, P.A.',
      'channel': 'Law Offices of Darrin T. Mish, P.A.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=1Ovbn9aeSCU&t=76s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Equity and assets then the then bankruptcy Council can often negotiate the '
              'release of your federal tax Lan as well if you have questions about federal tax '
              'leans or anything related to IRS problems call us at 888438 6474 or or visit '
              'our website at get IRS Al.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': 'Equity and assets then the then bankruptcy Council can often negotiate the '
             'release of your federal tax Lan as well if you have questions about federal tax '
             'leans or anything related to IRS problems call us at 888438 6474 or or visit our '
             'website at get IRS Al.',
      'title': 'IRS Notice of Federal Tax Lien: What It Means and How to Remove It (Law '
               'Offices of Darrin T. Mish, P.A.)',
      'url': 'https://www.youtube.com/watch?v=1Ovbn9aeSCU&t=76s',
      'video_id': '1Ovbn9aeSCU'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=Mp1_eOyha6A&t=27s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Two of our new Dallas County on Miami Dade County we're gonna start with Dallas "
              "County click on this here so he's gonna load for us and then from there.",
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': "Two of our new Dallas County on Miami Dade County we're gonna start with Dallas "
             "County click on this here so he's gonna load for us and then from there.",
      'title': 'Tax Sale Investing With GIS - Tax Lien and Tax Deed Research (Tax Sale '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=Mp1_eOyha6A&t=27s',
      'video_id': 'Mp1_eOyha6A'},
     {'author': 'Platinum Investment Properties Group - Tax Liens',
      'channel': 'Platinum Investment Properties Group - Tax Liens',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:54:32](https://www.youtube.com/watch?v=AcKbZeNuPr4&t=3272s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sir uh what kind of restrictions are there for foreign investors regarding '
              'American Ira Investments uh and a follow-up can I establish an IRA uh through '
              'an American.',
      'timestamp': 3272,
      'timestamp_label': '[00:54:32]',
      'timestamp_seconds': 3272,
      'tip': 'Sir uh what kind of restrictions are there for foreign investors regarding '
             'American Ira Investments uh and a follow-up can I establish an IRA uh through an '
             'American.',
      'title': '2015 12 09 19 03 Basics of Tax Lien Deed Investing using your Self Direct IRA '
               '(Platinum Investment Properties Group - Tax Liens)',
      'url': 'https://www.youtube.com/watch?v=AcKbZeNuPr4&t=3272s',
      'video_id': 'AcKbZeNuPr4'},
     {'author': 'Justin Colby',
      'channel': 'Justin Colby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:29](https://www.youtube.com/watch?v=xhw2pgi-46E&t=2369s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If you thought this was worth sharing then please do share this with at least '
              'two of your friends and be ready for the next episode Tony I appreciate you '
              "everybody thanks Justin appreciate you too man bye y'all see you on the next "
              'episode Peace.',
      'timestamp': 2369,
      'timestamp_label': '[00:39:29]',
      'timestamp_seconds': 2369,
      'tip': 'If you thought this was worth sharing then please do share this with at least '
             'two of your friends and be ready for the next episode Tony I appreciate you '
             "everybody thanks Justin appreciate you too man bye y'all see you on the next "
             'episode Peace.',
      'title': 'The Hidden Gem of Tax Lien Investing with 33-Year Expert | Tony Martinez '
               '(Justin Colby)',
      'url': 'https://www.youtube.com/watch?v=xhw2pgi-46E&t=2369s',
      'video_id': 'xhw2pgi-46E'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:51](https://www.youtube.com/watch?v=xEagXpsTPCw&t=231s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Auction is the first Tuesday of every single month giving you plenty of '
              'opportunity to get into this business Harris County Houston is going to be the '
              'largest one 4.88 million population average home price.',
      'timestamp': 231,
      'timestamp_label': '[00:03:51]',
      'timestamp_seconds': 231,
      'tip': 'Auction is the first Tuesday of every single month giving you plenty of '
             'opportunity to get into this business Harris County Houston is going to be the '
             'largest one 4.88 million population average home price.',
      'title': 'Top 6 Tax Deed State For Dirt Cheap Property (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=xEagXpsTPCw&t=231s',
      'video_id': 'xEagXpsTPCw'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=vMMozg0xaSA&t=392s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Shipping cost which is less than five bucks if you're in the United States you "
              'take your hooks and make it a successful day see ya.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': "Shipping cost which is less than five bucks if you're in the United States you "
             'take your hooks and make it a successful day see ya.',
      'title': 'File Your Own Suit to Quiet Title for Tax Deeds (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=vMMozg0xaSA&t=392s',
      'video_id': 'vMMozg0xaSA'}],
 4: [{'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:14](https://www.youtube.com/watch?v=YVYW5E5cTUI&t=794s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re either going to get the deed right away at the tax sale or it's going to be "
              '60 days. Henry County may be the one that does 60 days whereas Macon-Bibb or '
              "Forsyth may give it to you right away, but it's going to be one of those. "
              'Potentially 28 grand opening bid.',
      'timestamp': 794,
      'timestamp_label': '[00:13:14]',
      'timestamp_seconds': 794,
      'tip': "'re either going to get the deed right away at the tax sale or it's going to be "
             '60 days. Henry County may be the one that does 60 days whereas Macon-Bibb or '
             "Forsyth may give it to you right away, but it's going to be one of those. "
             'Potentially 28 grand opening bid.',
      'title': 'How To Find OTC Tax Deeds From Home? (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=YVYW5E5cTUI&t=794s',
      'video_id': 'YVYW5E5cTUI'},
     {'author': 'The Devine Law Group',
      'channel': 'The Devine Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=qAoyeFTuxms&t=162s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re bidding a percentage rate of what they want to get paid back on that lean. "
              'So, if I um am a $100 delinquent on my taxes and the county treasurer auctions '
              'off that $100, anyone bidding on it is going to bid a percentage rate of what '
              'they want to get paid back.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': "'re bidding a percentage rate of what they want to get paid back on that lean. "
             'So, if I um am a $100 delinquent on my taxes and the county treasurer auctions '
             'off that $100, anyone bidding on it is going to bid a percentage rate of what '
             'they want to get paid back.',
      'title': 'Tax Enforcement After Tyler v. Hennepin County (The Devine Law Group)',
      'url': 'https://www.youtube.com/watch?v=qAoyeFTuxms&t=162s',
      'video_id': 'qAoyeFTuxms'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:55](https://www.youtube.com/watch?v=jWaS4Y2Z1Mg&t=295s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Deed auctions tax lean certificates could be on every kind of property '
              'obviously homes you could have it on farms and ranches you could have it on a.',
      'timestamp': 295,
      'timestamp_label': '[00:04:55]',
      'timestamp_seconds': 295,
      'tip': 'Deed auctions tax lean certificates could be on every kind of property obviously '
             'homes you could have it on farms and ranches you could have it on a.',
      'title': 'Tax Deed vs Tax Lien: Differences Explained Simply (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=jWaS4Y2Z1Mg&t=295s',
      'video_id': 'jWaS4Y2Z1Mg'},
     {'author': 'CamaPlan Self Directed IRA',
      'channel': 'CamaPlan Self Directed IRA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:28](https://www.youtube.com/watch?v=DHgFebJCtQU&t=2068s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On how to do their due diligence how to bid at the tax sale and i also helped '
              'him develop a software for.',
      'timestamp': 2068,
      'timestamp_label': '[00:34:28]',
      'timestamp_seconds': 2068,
      'tip': 'On how to do their due diligence how to bid at the tax sale and i also helped '
             'him develop a software for.',
      'title': 'Episode 19: Evaluating the Risks and Returns of Tax Lien Investing with Joanne '
               'Musa (CamaPlan Self Directed IRA)',
      'url': 'https://www.youtube.com/watch?v=DHgFebJCtQU&t=2068s',
      'video_id': 'DHgFebJCtQU'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=qEuYpfZ_Qgg&t=53s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh but if the person has to make payments, that's occasionally will happen. So "
              "you'll have bankruptcies that you won't even know there was a bankruptcy "
              "involved on the tax lean because you're just going to get your check and you "
              'just need to redeemed.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "Uh but if the person has to make payments, that's occasionally will happen. So "
             "you'll have bankruptcies that you won't even know there was a bankruptcy "
             "involved on the tax lean because you're just going to get your check and you "
             'just need to redeemed.',
      'title': "Tax Lien Bankruptcy Myth Busted! It's Not What You Think (Tax Sale Secrets)",
      'url': 'https://www.youtube.com/watch?v=qEuYpfZ_Qgg&t=53s',
      'video_id': 'qEuYpfZ_Qgg'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=FgLt0Zd5dxo&t=394s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every one of these systems but instead of a lean being sold against the '
              'property to a third party the county basically holds that lean themselves.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': 'Every one of these systems but instead of a lean being sold against the property '
             'to a third party the county basically holds that lean themselves.',
      'title': 'Tax Liens, Deeds, Redeemable Deeds or Surplus? (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=FgLt0Zd5dxo&t=394s',
      'video_id': 'FgLt0Zd5dxo'},
     {'author': 'Tranquillity',
      'channel': 'Tranquillity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=VdRy2aZvV-Y&t=185s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All you have to do is do a little bit of research here and there and go to the '
              'county office and do a little bit more research and you can get these amazing '
              'certificates with great returns.',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'All you have to do is do a little bit of research here and there and go to the '
             'county office and do a little bit more research and you can get these amazing '
             'certificates with great returns.',
      'title': 'Maximizing Returns: The Power of Investing in Tax Liens (Tranquillity)',
      'url': 'https://www.youtube.com/watch?v=VdRy2aZvV-Y&t=185s',
      'video_id': 'VdRy2aZvV-Y'},
     {'author': 'Tax Sale Support',
      'channel': 'Tax Sale Support',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:26](https://www.youtube.com/watch?v=sH-Esa2i1zE&t=2966s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s included, which actually is pretty helpful. We do get the the address here, "
              "uh, and the their estimated value. So, they're estimating the value of the "
              'property to be about $300,000. So, that $2,500, you know, opening bid amount or '
              'lean amount is tiny.',
      'timestamp': 2966,
      'timestamp_label': '[00:49:26]',
      'timestamp_seconds': 2966,
      'tip': "'s included, which actually is pretty helpful. We do get the the address here, "
             "uh, and the their estimated value. So, they're estimating the value of the "
             'property to be about $300,000. So, that $2,500, you know, opening bid amount or '
             'lean amount is tiny.',
      'title': 'TAX SALE TITANS PODCAST EPISODE 21: TAX LIENS & TAX DEEDS (Tax Sale Support)',
      'url': 'https://www.youtube.com/watch?v=sH-Esa2i1zE&t=2966s',
      'video_id': 'sH-Esa2i1zE'},
     {'author': 'Realauction',
      'channel': 'Realauction',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=hKsLdKqVOE0&t=92s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On the bid menu, you will have the choice of bidding in percent or bidding in '
              'dollars. If you choose to bid in percent, simply enter the percent of interest '
              "you're willing to accept for the lean and click bid to submit your bid.",
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'On the bid menu, you will have the choice of bidding in percent or bidding in '
             'dollars. If you choose to bid in percent, simply enter the percent of interest '
             "you're willing to accept for the lean and click bid to submit your bid.",
      'title': 'Bidding: Tax Lien New Jersey (Realauction)',
      'url': 'https://www.youtube.com/watch?v=hKsLdKqVOE0&t=92s',
      'video_id': 'hKsLdKqVOE0'},
     {'author': 'CamaPlan Self Directed IRA',
      'channel': 'CamaPlan Self Directed IRA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=U08uLxrDVE4&t=235s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Founders and managers of gamma self-directed IRA LLC and I have investments in '
              'real estate in multiple states and I do tax liens in multiple states and am a '
              'third-generation investor going back to my mom and dad and their mom aunts and '
              'dads.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'Founders and managers of gamma self-directed IRA LLC and I have investments in '
             'real estate in multiple states and I do tax liens in multiple states and am a '
             'third-generation investor going back to my mom and dad and their mom aunts and '
             'dads.',
      'title': 'Investing in Tax Liens with a Self Directed IRA (CamaPlan Self Directed IRA)',
      'url': 'https://www.youtube.com/watch?v=U08uLxrDVE4&t=235s',
      'video_id': 'U08uLxrDVE4'},
     {'author': 'The Ramsey Show Highlights',
      'channel': 'The Ramsey Show Highlights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:37](https://www.youtube.com/watch?v=KytTy1-RC5I&t=457s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '24-year-old got on Tik Tok and thought he found a way to make easy money and '
              "I'm just here to say no you You' be better off delivering pizza you'd end up "
              'with more create your free every dooll budget today the simplest way to budget '
              'for your life.',
      'timestamp': 457,
      'timestamp_label': '[00:07:37]',
      'timestamp_seconds': 457,
      'tip': "24-year-old got on Tik Tok and thought he found a way to make easy money and I'm "
             "just here to say no you You' be better off delivering pizza you'd end up with "
             'more create your free every dooll budget today the simplest way to budget for '
             'your life.',
      'title': 'The Truth About Tax Lien Investing (The Ramsey Show Highlights)',
      'url': 'https://www.youtube.com/watch?v=KytTy1-RC5I&t=457s',
      'video_id': 'KytTy1-RC5I'},
     {'author': 'Lenny the Lawyer-Live',
      'channel': 'Lenny the Lawyer-Live',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=zaxbNjHaHww&t=227s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Unlike in this video which is for informational purposes only make sure you '
              'call to 973-798-6131 with leonard boyer of boyer coffee llc to talk about your '
              'tax lien foreclosure situation and we look forward to helping you thank you and '
              'have a good evening.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'Unlike in this video which is for informational purposes only make sure you call '
             'to 973-798-6131 with leonard boyer of boyer coffee llc to talk about your tax '
             'lien foreclosure situation and we look forward to helping you thank you and have '
             'a good evening.',
      'title': 'How To Fight Tax Lien Foreclosure (Lenny the Lawyer-Live)',
      'url': 'https://www.youtube.com/watch?v=zaxbNjHaHww&t=227s',
      'video_id': 'zaxbNjHaHww'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:51](https://www.youtube.com/watch?v=vA4ImBMyenY&t=171s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'County I did not want that property and I did not want to deal with it okay so '
              'coming back to the lean some of the risks again are you need to do an.',
      'timestamp': 171,
      'timestamp_label': '[00:02:51]',
      'timestamp_seconds': 171,
      'tip': 'County I did not want that property and I did not want to deal with it okay so '
             'coming back to the lean some of the risks again are you need to do an.',
      'title': 'A Warning To Tax Lien & Deed Investors | Risks! (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=vA4ImBMyenY&t=171s',
      'video_id': 'vA4ImBMyenY'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=MzL0xEaYnUI&t=15s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Claim hey everybody we're here with Ted Thomas the tax lean certificate and tax "
              "need Authority and today Ted's going to be telling us about what a quiet title.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Claim hey everybody we're here with Ted Thomas the tax lean certificate and tax "
             "need Authority and today Ted's going to be telling us about what a quiet title.",
      'title': 'Quiet title, what is it and what do I do with it? (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=MzL0xEaYnUI&t=15s',
      'video_id': 'MzL0xEaYnUI'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=cnd7EM15dyk&t=139s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "See what they're experiencing and then I'll give you a you know at least a "
              'starting point that you can continually adjust and that way you know that all '
              "at the end of the day you'll have that formulas you're looking for so hopefully "
              'this helps yeah.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': "See what they're experiencing and then I'll give you a you know at least a "
             'starting point that you can continually adjust and that way you know that all at '
             "the end of the day you'll have that formulas you're looking for so hopefully "
             'this helps yeah.',
      'title': 'Formula for Tax Lien Premiums (Viewer Question) (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=cnd7EM15dyk&t=139s',
      'video_id': 'cnd7EM15dyk'}],
 5: [{'author': 'Lien Ledger',
      'channel': 'Lien Ledger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=H9fPhqUYPfc&t=466s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Check every property before you bid. Many counties now run their auctions '
              'online, so you can research and bid from home. But that also means more '
              "competition. Start small in one county and learn how it's auction works.",
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': 'Check every property before you bid. Many counties now run their auctions '
             'online, so you can research and bid from home. But that also means more '
             "competition. Start small in one county and learn how it's auction works.",
      'title': 'How Tax Lien Investing Actually Works (Lien Ledger)',
      'url': 'https://www.youtube.com/watch?v=H9fPhqUYPfc&t=466s',
      'video_id': 'H9fPhqUYPfc'},
     {'author': 'Tax Lien School Highlights - Dustin Hahn',
      'channel': 'Tax Lien School Highlights - Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=M8AxkDXoffk&t=109s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So scrolling down, we've got uh for it. So, this one is going to be actually "
              'insane. This is going to be an insane auction. So, this is Lake County, Indiana '
              'Commissioners Certificate Sale.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "So scrolling down, we've got uh for it. So, this one is going to be actually "
             'insane. This is going to be an insane auction. So, this is Lake County, Indiana '
             'Commissioners Certificate Sale.',
      'title': 'ZeusAuction Tax Liens: How to Find Online Auctions With Less Competition (Tax '
               'Lien School Highlights - Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=M8AxkDXoffk&t=109s',
      'video_id': 'M8AxkDXoffk'},
     {'author': 'Clarity Tax Relief',
      'channel': 'Clarity Tax Relief',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=oPKD4zP1XUQ&t=259s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'On the transcript, is there a code? Code 582 for the lien filed. A later '
              "release shows as code 583. So a lien's on the property. Paying in full triggers "
              'a Certificate of Release within 30 days.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': 'On the transcript, is there a code? Code 582 for the lien filed. A later release '
             "shows as code 583. So a lien's on the property. Paying in full triggers a "
             'Certificate of Release within 30 days.',
      'title': 'IRS Notice of Federal Tax Lien Filings Statistics (2026) (Clarity Tax Relief)',
      'url': 'https://www.youtube.com/watch?v=oPKD4zP1XUQ&t=259s',
      'video_id': 'oPKD4zP1XUQ'},
     {'author': 'Canopy',
      'channel': 'Canopy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=stcKbUxhc84&t=126s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The IRS will withdraw the lien if the tax that eventually prompted the lien was '
              'assessed in error, or if the lien was filed without giving the taxpayer proper '
              'notice. This is extremely rare, as the IRS has multiple fail-safes in place to '
              'avoid these kinds of mistakes.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'The IRS will withdraw the lien if the tax that eventually prompted the lien was '
             'assessed in error, or if the lien was filed without giving the taxpayer proper '
             'notice. This is extremely rare, as the IRS has multiple fail-safes in place to '
             'avoid these kinds of mistakes.',
      'title': 'Quick Tips | Filling Out IRS Form 12277: Application for Withdrawal of Federal '
               'Tax Lien (Canopy)',
      'url': 'https://www.youtube.com/watch?v=stcKbUxhc84&t=126s',
      'video_id': 'stcKbUxhc84'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=JcAwqIfK0vo&t=66s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, these certificates pay 16%, 18%, 24% all the way up to 36% and the check '
              "is going to come from the local government. Now, you can't invest with Ted "
              "Thomas. You're going to invest for the county, you're going to get a check back "
              'from the county.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'Now, these certificates pay 16%, 18%, 24% all the way up to 36% and the check is '
             "going to come from the local government. Now, you can't invest with Ted Thomas. "
             "You're going to invest for the county, you're going to get a check back from the "
             'county.',
      'title': 'What Is Tax Lien Certificate Investing? (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=JcAwqIfK0vo&t=66s',
      'video_id': 'JcAwqIfK0vo'},
     {'author': 'Community Living HQ',
      'channel': 'Community Living HQ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:23](https://www.youtube.com/watch?v=NZlx21J6n-c&t=503s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Appeals demonstrated that problem 5 days earlier. Four owners sought proceeds '
              'from properties sold during 2014 foreclosures. They argued later decisions and '
              'legislation made their claims timely.',
      'timestamp': 503,
      'timestamp_label': '[00:08:23]',
      'timestamp_seconds': 503,
      'tip': 'Appeals demonstrated that problem 5 days earlier. Four owners sought proceeds '
             'from properties sold during 2014 foreclosures. They argued later decisions and '
             'legislation made their claims timely.',
      'title': 'The Equity the County Kept (Community Living HQ)',
      'url': 'https://www.youtube.com/watch?v=NZlx21J6n-c&t=503s',
      'video_id': 'NZlx21J6n-c'},
     {'author': 'Tax Lien School Highlights - Dustin Hahn',
      'channel': 'Tax Lien School Highlights - Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:06](https://www.youtube.com/watch?v=VK7ChKB-gNU&t=246s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, of the 50 or so deals we've done there, we've never been >> If you like "
              'this video and you want to get started with tax liens and deeds and avoid some '
              'mistakes, I have a free gift for you called the ABCs of tax lien and deed '
              'investing.',
      'timestamp': 246,
      'timestamp_label': '[00:04:06]',
      'timestamp_seconds': 246,
      'tip': "So, of the 50 or so deals we've done there, we've never been >> If you like this "
             'video and you want to get started with tax liens and deeds and avoid some '
             'mistakes, I have a free gift for you called the ABCs of tax lien and deed '
             'investing.',
      'title': "Tax Lien vs Tax Deed States - Kentucky's 11-Year Liens and the Texas 25% Myth "
               '(Tax Lien School Highlights - Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=VK7ChKB-gNU&t=246s',
      'video_id': 'VK7ChKB-gNU'},
     {'author': 'PRO-SE LEGAL SCHOOL',
      'channel': 'PRO-SE LEGAL SCHOOL',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:26](https://www.youtube.com/watch?v=N5hkQOZjHyU&t=806s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Complaint the HOA requested the court allow it to to be able to use the amount '
              "in dispute as a credit bid to purchase the property at chef sell now that's "
              "that's pretty sketchy.",
      'timestamp': 806,
      'timestamp_label': '[00:13:26]',
      'timestamp_seconds': 806,
      'tip': 'Complaint the HOA requested the court allow it to to be able to use the amount '
             "in dispute as a credit bid to purchase the property at chef sell now that's "
             "that's pretty sketchy.",
      'title': 'HOA Lien Foreclosure -Learn Why The Court Lack Jurisdiction (PRO-SE LEGAL '
               'SCHOOL)',
      'url': 'https://www.youtube.com/watch?v=N5hkQOZjHyU&t=806s',
      'video_id': 'N5hkQOZjHyU'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:18](https://www.youtube.com/watch?v=41UuQtBLiBo&t=498s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I finish up I want to make sure that you avoid 2 big mistakes. Big mistake '
              "number 1, don't buy any property that you haven't seen. There's been no sight "
              "or no boots on the ground, don't buy the property.",
      'timestamp': 498,
      'timestamp_label': '[00:08:18]',
      'timestamp_seconds': 498,
      'tip': 'I finish up I want to make sure that you avoid 2 big mistakes. Big mistake '
             "number 1, don't buy any property that you haven't seen. There's been no sight or "
             "no boots on the ground, don't buy the property.",
      'title': 'Is Texas A Tax Lien Or Tax Deed State (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=41UuQtBLiBo&t=498s',
      'video_id': '41UuQtBLiBo'},
     {'author': 'NuView Trust',
      'channel': 'NuView Trust',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:03](https://www.youtube.com/watch?v=Hqqt5H7mS3o&t=1923s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Get the maximum rate allowable so you know again it's all risk reward right if "
              "you're comfortable taking more risk because you have the likelihood of earning "
              '18 percent great you know but you got more risk of losing your money.',
      'timestamp': 1923,
      'timestamp_label': '[00:32:03]',
      'timestamp_seconds': 1923,
      'tip': "Get the maximum rate allowable so you know again it's all risk reward right if "
             "you're comfortable taking more risk because you have the likelihood of earning "
             '18 percent great you know but you got more risk of losing your money.',
      'title': 'Tax Liens & Tax Deed Investments In Your  Self-Directed IRA (NuView Trust)',
      'url': 'https://www.youtube.com/watch?v=Hqqt5H7mS3o&t=1923s',
      'video_id': 'Hqqt5H7mS3o'},
     {'author': 'The Residential Buyer',
      'channel': 'The Residential Buyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=2S4mkxCrOhM&t=203s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Somehow um you might be able to avoid buying a literal meth lab or something '
              "right so whether you're a real estate investor or a homeowner facing "
              'foreclosure the next best move is probably talking to a foreclosure attorney or '
              'even a real estate investor like ourselves.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'Somehow um you might be able to avoid buying a literal meth lab or something '
             "right so whether you're a real estate investor or a homeowner facing foreclosure "
             'the next best move is probably talking to a foreclosure attorney or even a real '
             'estate investor like ourselves.',
      'title': 'Property Tax Sales: Tax Lien Certificates vs Tax Deed States (The Residential '
               'Buyer)',
      'url': 'https://www.youtube.com/watch?v=2S4mkxCrOhM&t=203s',
      'video_id': '2S4mkxCrOhM'},
     {'author': 'Dan Britt',
      'channel': 'Dan Britt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=eZJCPENFp3o&t=234s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "IRS your rights and your property are in Jeopardy you're at risk you should not "
              'ignore any IRS notice particularly a notice of federal tax lean but you do have '
              'options contact a qualified professional for help.',
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': "IRS your rights and your property are in Jeopardy you're at risk you should not "
             'ignore any IRS notice particularly a notice of federal tax lean but you do have '
             'options contact a qualified professional for help.',
      'title': 'IRS Notice Federal Tax Lien - What is it? What does it mean to me? What can I '
               'do? (Dan Britt)',
      'url': 'https://www.youtube.com/watch?v=eZJCPENFp3o&t=234s',
      'video_id': 'eZJCPENFp3o'},
     {'author': 'Ross Budrakey',
      'channel': 'Ross Budrakey',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:40:05](https://www.youtube.com/watch?v=VmzztAnZ71w&t=2405s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '$1,400 okay 1,400 going once going twice $2,000 how much $4,000 $5,000 going '
              'once $8,000 going once going twice 13 $15,000 legs going $20,000 $20,000 going '
              'once going twice 22,000 going once going twice.',
      'timestamp': 2405,
      'timestamp_label': '[00:40:05]',
      'timestamp_seconds': 2405,
      'tip': '$1,400 okay 1,400 going once going twice $2,000 how much $4,000 $5,000 going '
             'once $8,000 going once going twice 13 $15,000 legs going $20,000 $20,000 going '
             'once going twice 22,000 going once going twice.',
      'title': 'Introduction to Tax Lien Investing Webinar (Ross Budrakey)',
      'url': 'https://www.youtube.com/watch?v=VmzztAnZ71w&t=2405s',
      'video_id': 'VmzztAnZ71w'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:25](https://www.youtube.com/watch?v=fIPCLCdZlAU&t=685s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Funding when they need it um and you know and if they didn't have the tax so "
              "you know they really wouldn't have that whole enforcement mechanism in place "
              'yeah for sure.',
      'timestamp': 685,
      'timestamp_label': '[00:11:25]',
      'timestamp_seconds': 685,
      'tip': "Funding when they need it um and you know and if they didn't have the tax so you "
             "know they really wouldn't have that whole enforcement mechanism in place yeah "
             'for sure.',
      'title': 'Tax Lien Investing 101: Tax Certificates Auctions Explained! TAX SALE TIP OF '
               'THE WEEK (Tax Sale Secrets)',
      'url': 'https://www.youtube.com/watch?v=fIPCLCdZlAU&t=685s',
      'video_id': 'fIPCLCdZlAU'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:31](https://www.youtube.com/watch?v=rYcTmrny9JQ&t=451s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The best ones out there and it'll get you started so thanks for tuning in I "
              "really appreciate it we'll see you in the next one.",
      'timestamp': 451,
      'timestamp_label': '[00:07:31]',
      'timestamp_seconds': 451,
      'tip': "The best ones out there and it'll get you started so thanks for tuning in I "
             "really appreciate it we'll see you in the next one.",
      'title': 'The Best Tax Lien State? 36% ROI With Illinois Tax Liens. (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=rYcTmrny9JQ&t=451s',
      'video_id': 'rYcTmrny9JQ'}],
 6: [{'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=2M5EFWdf-is&t=154s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Health certificates County held Deeds lands available over-the-counter liens '
              'over-the-counter beads you want to make sure you check all those names and '
              'also.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'Health certificates County held Deeds lands available over-the-counter liens '
             'over-the-counter beads you want to make sure you check all those names and also.',
      'title': 'Having Trouble Finding Over The Counter Tax Liens? Try this.... (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=2M5EFWdf-is&t=154s',
      'video_id': '2M5EFWdf-is'},
     {'author': 'Over The Counter Tax Deeds',
      'channel': 'Over The Counter Tax Deeds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:47](https://www.youtube.com/watch?v=RxbJj9wFJXI&t=47s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You want to ask them what is the process of a finding your list of properties '
              'of taxdeed properties that did not sell at auction. You want to ask them where '
              'can I find your specific list of over-the-counter taxdeed properties that did '
              'not sell at auction.',
      'timestamp': 47,
      'timestamp_label': '[00:00:47]',
      'timestamp_seconds': 47,
      'tip': 'You want to ask them what is the process of a finding your list of properties of '
             'taxdeed properties that did not sell at auction. You want to ask them where can '
             'I find your specific list of over-the-counter taxdeed properties that did not '
             'sell at auction.',
      'title': "OTC Tax Deed Opportunities You Need to Grab Now (Before It's Too Late) (Over "
               'The Counter Tax Deeds)',
      'url': 'https://www.youtube.com/watch?v=RxbJj9wFJXI&t=47s',
      'video_id': 'RxbJj9wFJXI'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:51](https://www.youtube.com/watch?v=B0WBR5swuac&t=651s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Really simple, clean business. I prefer this one, because to me, the down and '
              'dirty of wrestling for the tax deed properties turned out for me, it was just '
              "like, I don't wanna deal with this anymore. I wanna deal with contractors. "
              'Tenants, toilets, disaffected former owners.',
      'timestamp': 651,
      'timestamp_label': '[00:10:51]',
      'timestamp_seconds': 651,
      'tip': 'Really simple, clean business. I prefer this one, because to me, the down and '
             'dirty of wrestling for the tax deed properties turned out for me, it was just '
             "like, I don't wanna deal with this anymore. I wanna deal with contractors. "
             'Tenants, toilets, disaffected former owners.',
      'title': "How Does Cook County Tax Sale Work? (Bob Diamond - America's Tax Sale "
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=B0WBR5swuac&t=651s',
      'video_id': 'B0WBR5swuac'},
     {'author': 'Tax Sale Support',
      'channel': 'Tax Sale Support',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=0TBV3XkrRmo&t=311s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Starting bid of one hundred and sixty thousand dollars now that seems like it's "
              "pretty steep for a tax deed so we're already here let's see if we can find out "
              'information about this property or why the the taxes might be so high.',
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': "Starting bid of one hundred and sixty thousand dollars now that seems like it's "
             "pretty steep for a tax deed so we're already here let's see if we can find out "
             'information about this property or why the the taxes might be so high.',
      'title': 'Tax Lien & Tax Deed "Online Auctions" Training! (Tax Sale Support)',
      'url': 'https://www.youtube.com/watch?v=0TBV3XkrRmo&t=311s',
      'video_id': '0TBV3XkrRmo'},
     {'author': 'Saen Higgins',
      'channel': 'Saen Higgins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:56](https://www.youtube.com/watch?v=nbHUraglUQo&t=596s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Get me your email information. I'll get you links to all of the information you "
              'need to know to do this successfully and get your first deal in the next 30 to '
              '60 days. This is Saen Higgins saying, God bless and good luck.',
      'timestamp': 596,
      'timestamp_label': '[00:09:56]',
      'timestamp_seconds': 596,
      'tip': "Get me your email information. I'll get you links to all of the information you "
             'need to know to do this successfully and get your first deal in the next 30 to '
             '60 days. This is Saen Higgins saying, God bless and good luck.',
      'title': 'How To Buy Over-The-Counter Tax Deeds (Saen Higgins)',
      'url': 'https://www.youtube.com/watch?v=nbHUraglUQo&t=596s',
      'video_id': 'nbHUraglUQo'},
     {'author': 'Kevin Bupp - Cash Flow Investor',
      'channel': 'Kevin Bupp - Cash Flow Investor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:05](https://www.youtube.com/watch?v=UyiZp8ocowM&t=1325s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So who has the county list? And so conducting due diligence could also involve '
              "getting what's for sale. This is not too dissimilar from like getting the "
              'foreclosure list, right, and going to the or doing pre-foreclosure, that kind '
              'of stuff.',
      'timestamp': 1325,
      'timestamp_label': '[00:22:05]',
      'timestamp_seconds': 1325,
      'tip': 'So who has the county list? And so conducting due diligence could also involve '
             "getting what's for sale. This is not too dissimilar from like getting the "
             'foreclosure list, right, and going to the or doing pre-foreclosure, that kind of '
             'stuff.',
      'title': 'How to Invest in Tax Liens in 2026 (13%-18% Annual Returns) | Ep. 1002 (Kevin '
               'Bupp - Cash Flow Investor)',
      'url': 'https://www.youtube.com/watch?v=UyiZp8ocowM&t=1325s',
      'video_id': 'UyiZp8ocowM'},
     {'author': 'Tax Deed Wolf',
      'channel': 'Tax Deed Wolf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=sY8o7KeLptY&t=63s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It called list of lands available you may hear it even called Surplus right '
              'regardless of where you live the first step to finding some of these '
              'properties.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'It called list of lands available you may hear it even called Surplus right '
             'regardless of where you live the first step to finding some of these properties.',
      'title': 'How To Buy Over The Counter Tax Deeds | Tax Deed Academy (Tax Deed Wolf)',
      'url': 'https://www.youtube.com/watch?v=sY8o7KeLptY&t=63s',
      'video_id': 'sY8o7KeLptY'},
     {'author': 'Logan Allec',
      'channel': 'Logan Allec',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:39](https://www.youtube.com/watch?v=joIEfxnWZzE&t=459s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'IRS will get paid out of the proceeds of the transaction or the lien gets '
              "handled some other way first. Okay, I'll talk a little bit about that in a bit. "
              "Um uh you know, in bankruptcy, right? The lien where you know, I'm not a "
              'bankruptcy attorney, okay?',
      'timestamp': 459,
      'timestamp_label': '[00:07:39]',
      'timestamp_seconds': 459,
      'tip': 'IRS will get paid out of the proceeds of the transaction or the lien gets '
             "handled some other way first. Okay, I'll talk a little bit about that in a bit. "
             "Um uh you know, in bankruptcy, right? The lien where you know, I'm not a "
             'bankruptcy attorney, okay?',
      'title': 'IRS Tax Lien Explained: What It Means and 4 Ways to Deal With It (Logan Allec)',
      'url': 'https://www.youtube.com/watch?v=joIEfxnWZzE&t=459s',
      'video_id': 'joIEfxnWZzE'},
     {'author': 'realestatewealthguy',
      'channel': 'realestatewealthguy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=PRTEvlETNdk&t=141s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Differently and uh but these days uh more and more counties are actually making '
              'online participation available uh which makes things uh very convenient so '
              "you're just going to need to find.",
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'Differently and uh but these days uh more and more counties are actually making '
             'online participation available uh which makes things uh very convenient so '
             "you're just going to need to find.",
      'title': 'Tax Lien Certificate Investing (realestatewealthguy)',
      'url': 'https://www.youtube.com/watch?v=PRTEvlETNdk&t=141s',
      'video_id': 'PRTEvlETNdk'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:58](https://www.youtube.com/watch?v=RgLErVu5_Kk&t=2398s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All we did you know in fact when we first got started we you know we'd attend "
              "auctions we didn't have any business being at the.",
      'timestamp': 2398,
      'timestamp_label': '[00:39:58]',
      'timestamp_seconds': 2398,
      'tip': "All we did you know in fact when we first got started we you know we'd attend "
             "auctions we didn't have any business being at the.",
      'title': 'How to Buy Tax Deed LAND Online & OTC Right NOW! (Tax Sale Secrets)',
      'url': 'https://www.youtube.com/watch?v=RgLErVu5_Kk&t=2398s',
      'video_id': 'RgLErVu5_Kk'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=g0bsPf3Jwo4&t=60s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Unsold list in other words the county will still have these properties in their '
              "inventory but they're no longer on the list so what you have to do is you.",
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Unsold list in other words the county will still have these properties in their '
             "inventory but they're no longer on the list so what you have to do is you.",
      'title': "Over The Counter Tax Deed Sales (OTC) - What realtors don't want you to know! "
               '(Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=g0bsPf3Jwo4&t=60s',
      'video_id': 'g0bsPf3Jwo4'},
     {'author': 'Personal Finance Tips',
      'channel': 'Personal Finance Tips',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:08](https://www.youtube.com/watch?v=vD0IitWLjZE&t=968s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The the best way that I can I can answer it uh you know if we focus on a '
              "specific state it's easier to give a more exact answer yeah I guess I'm trying "
              'to just understand like why um maybe even in your example that you just gave.',
      'timestamp': 968,
      'timestamp_label': '[00:16:08]',
      'timestamp_seconds': 968,
      'tip': 'The the best way that I can I can answer it uh you know if we focus on a '
             "specific state it's easier to give a more exact answer yeah I guess I'm trying "
             'to just understand like why um maybe even in your example that you just gave.',
      'title': 'How tax lien investing works and how to buy tax lien certificates (HYW066) '
               '(Personal Finance Tips)',
      'url': 'https://www.youtube.com/watch?v=vD0IitWLjZE&t=968s',
      'video_id': 'vD0IitWLjZE'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=a81g1szr71Y&t=233s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Property in the Google Maps what you can do is add it to your list so let's say "
              "you're done with your res search and tomorrow you want to pick it up or the.",
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': "Property in the Google Maps what you can do is add it to your list so let's say "
             "you're done with your res search and tomorrow you want to pick it up or the.",
      'title': 'Tax Deed Research Made Easy: 3 Must-Use Free Online Sources (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=a81g1szr71Y&t=233s',
      'video_id': 'a81g1szr71Y'},
     {'author': 'Tax Sale Resources',
      'channel': 'Tax Sale Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=tMIwxs2U5JM&t=15s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Leverage million dollar blueprint and today i want to talk about two different '
              'types of tax dates you have your straight tax deeds and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Leverage million dollar blueprint and today i want to talk about two different '
             'types of tax dates you have your straight tax deeds and.',
      'title': "Tax Deeds and Redeemable Tax Deeds...So, what's the difference? (Tax Sale "
               'Resources)',
      'url': 'https://www.youtube.com/watch?v=tMIwxs2U5JM&t=15s',
      'video_id': 'tMIwxs2U5JM'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:54](https://www.youtube.com/watch?v=XLUuBoGUOj8&t=654s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Could listen to start that over again and you could have you could have a mini '
              "course and you could be getting started today I'm Ted Thomas see you on the "
              'next video.',
      'timestamp': 654,
      'timestamp_label': '[00:10:54]',
      'timestamp_seconds': 654,
      'tip': 'Could listen to start that over again and you could have you could have a mini '
             "course and you could be getting started today I'm Ted Thomas see you on the next "
             'video.',
      'title': 'Over the Counter Tax Lien Certificate Sales (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=XLUuBoGUOj8&t=654s',
      'video_id': 'XLUuBoGUOj8'}],
 7: [{'author': 'Saen Higgins',
      'channel': 'Saen Higgins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:03](https://www.youtube.com/watch?v=Lcz3UJEz_oM&t=243s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "At the end of two years, I don't foreclose on it. I call the county, and they "
              'foreclose on it for me, but at the end of the foreclosure, that process means '
              'it goes to a tax deed sale, and I am the opening bid.',
      'timestamp': 243,
      'timestamp_label': '[00:04:03]',
      'timestamp_seconds': 243,
      'tip': "At the end of two years, I don't foreclose on it. I call the county, and they "
             'foreclose on it for me, but at the end of the foreclosure, that process means it '
             'goes to a tax deed sale, and I am the opening bid.',
      'title': 'How To Buy Tax Lien Certificates In Florida (Saen Higgins)',
      'url': 'https://www.youtube.com/watch?v=Lcz3UJEz_oM&t=243s',
      'video_id': 'Lcz3UJEz_oM'},
     {'author': 'Realauction',
      'channel': 'Realauction',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=cleRXY7vybQ&t=126s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Additionally, each county or municipality in Arizona will have a different '
              'method of auction. Most will use what we call the proxy bid system in which the '
              'auction engine will attempt to win for you at the closest bid increment '
              'available.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Additionally, each county or municipality in Arizona will have a different '
             'method of auction. Most will use what we call the proxy bid system in which the '
             'auction engine will attempt to win for you at the closest bid increment '
             'available.',
      'title': 'Bidding: Tax Lien Arizona (Realauction)',
      'url': 'https://www.youtube.com/watch?v=cleRXY7vybQ&t=126s',
      'video_id': 'cleRXY7vybQ'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=0adTzNpuLtk&t=42s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s usually based on whatever the state laws signify the property enforcement "
              'that property tax enforcement system is being. So, yeah, tax lien certificates, '
              'tax deed foreclosures, and tax redemption deeds. What exactly are tax liens?',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': "'s usually based on whatever the state laws signify the property enforcement "
             'that property tax enforcement system is being. So, yeah, tax lien certificates, '
             'tax deed foreclosures, and tax redemption deeds. What exactly are tax liens?',
      'title': 'Tax Liens vs. Tax Deeds vs. Redemption Deeds: Which is Best? (Tax Sale '
               'Secrets)',
      'url': 'https://www.youtube.com/watch?v=0adTzNpuLtk&t=42s',
      'video_id': '0adTzNpuLtk'},
     {'author': 'FLIP-Tech',
      'channel': 'FLIP-Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:35](https://www.youtube.com/watch?v=QWmH7uEe2g8&t=755s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So does it take into account uh the different auction platform? Yes, because '
              'you so because of how auctions work. Remember the idea behind flip is to make '
              "tax lean and tax deed investing is to simplify it. It's not to overwhelm the "
              'process.',
      'timestamp': 755,
      'timestamp_label': '[00:12:35]',
      'timestamp_seconds': 755,
      'tip': 'So does it take into account uh the different auction platform? Yes, because you '
             'so because of how auctions work. Remember the idea behind flip is to make tax '
             "lean and tax deed investing is to simplify it. It's not to overwhelm the "
             'process.',
      'title': 'From Confused to Confident: Tax Lien Investing Explained + FLIP Demo '
               '(FLIP-Tech)',
      'url': 'https://www.youtube.com/watch?v=QWmH7uEe2g8&t=755s',
      'video_id': 'QWmH7uEe2g8'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=bFO7QIn_w3U&t=55s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '18% so that can be a really good rate of return. But as with many things in '
              "Illinois, it can get complicated. So the way that you bid is, it's called a bid "
              'down process.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': '18% so that can be a really good rate of return. But as with many things in '
             "Illinois, it can get complicated. So the way that you bid is, it's called a bid "
             'down process.',
      'title': "How Does A Tax Sale Work In Illinois? (Bob Diamond - America's Tax Sale "
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=bFO7QIn_w3U&t=55s',
      'video_id': 'bFO7QIn_w3U'},
     {'author': 'Julia M. Spencer',
      'channel': 'Julia M. Spencer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=q7Fb-u0lpiY&t=146s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I can't remember so i'm doing this one again i kind of look at tax sales as a "
              'three-step process the first step being.',
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': "I can't remember so i'm doing this one again i kind of look at tax sales as a "
             'three-step process the first step being.',
      'title': 'Tax Certificates/ Liens/ Deeds- Where to Start? (Julia M. Spencer)',
      'url': 'https://www.youtube.com/watch?v=q7Fb-u0lpiY&t=146s',
      'video_id': 'q7Fb-u0lpiY'},
     {'author': 'Jose Luiz Morales',
      'channel': 'Jose Luiz Morales',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:49](https://www.youtube.com/watch?v=B0yvMIdmaaQ&t=949s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They'll sign off and we'll submit a letter with that um with that uh listing "
              'agreement what is the uh uh Quiet Title action process look like it depends on.',
      'timestamp': 949,
      'timestamp_label': '[00:15:49]',
      'timestamp_seconds': 949,
      'tip': "They'll sign off and we'll submit a letter with that um with that uh listing "
             'agreement what is the uh uh Quiet Title action process look like it depends on.',
      'title': 'Can You Remove Someone From a Deed? - How Quiet Title Action Works (Jose Luiz '
               'Morales)',
      'url': 'https://www.youtube.com/watch?v=B0yvMIdmaaQ&t=949s',
      'video_id': 'B0yvMIdmaaQ'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=_nIeKBXnmws&t=20s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Penllis County Tax Deed for November 19th, 2025. And right off the bat, I see a '
              'pretty interesting property. Um, and some of these counties, you can click on '
              "this and it will pull up the property appraisers information. Let's see if it "
              'works here.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Penllis County Tax Deed for November 19th, 2025. And right off the bat, I see a '
             'pretty interesting property. Um, and some of these counties, you can click on '
             "this and it will pull up the property appraisers information. Let's see if it "
             'works here.',
      'title': 'From Paper to Property: Step-by-Step GIS Method for Tax Sales (Tax Sale '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=_nIeKBXnmws&t=20s',
      'video_id': '_nIeKBXnmws'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:42:13](https://www.youtube.com/watch?v=nM1XxTC-5JY&t=2533s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re experts at is making it so that you can learn it step-by-step and make sure "
              "that you don't make mistakes. Okay, the county is very interested in you not "
              'making a mistake. Because now they got a conflict taking place. So, the bidding '
              'process is straightforward.',
      'timestamp': 2533,
      'timestamp_label': '[00:42:13]',
      'timestamp_seconds': 2533,
      'tip': "'re experts at is making it so that you can learn it step-by-step and make sure "
             "that you don't make mistakes. Okay, the county is very interested in you not "
             'making a mistake. Because now they got a conflict taking place. So, the bidding '
             'process is straightforward.',
      'title': 'I Bought a Tax Lien. Where’s My House? | Beginner’s Guide New Edition Part 1 '
               '(Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=nM1XxTC-5JY&t=2533s',
      'video_id': 'nM1XxTC-5JY'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=bsVbyBCB2sA&t=16s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "An over-the-counter tax deed so basically it's been seized by the government "
              'you can go there you can buy it the big benefit is you can buy these.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': "An over-the-counter tax deed so basically it's been seized by the government you "
             'can go there you can buy it the big benefit is you can buy these.',
      'title': 'Tax Deeds vs. Tax Liens: Breaking Down the Pros and Cons (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=bsVbyBCB2sA&t=16s',
      'video_id': 'bsVbyBCB2sA'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=eNKIUQC6io0&t=168s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A lot of these auctions these days are going to happen which is very cool. You '
              'can do them from anywhere in the world. We have people in Australia doing this '
              'stuff in Idaho or Iowa depending on where they want to do tax liens. So that is '
              'the beauty of this business.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'A lot of these auctions these days are going to happen which is very cool. You '
             'can do them from anywhere in the world. We have people in Australia doing this '
             'stuff in Idaho or Iowa depending on where they want to do tax liens. So that is '
             'the beauty of this business.',
      'title': 'Beginner Tax Lien Investing (Step By Step) (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=eNKIUQC6io0&t=168s',
      'video_id': 'eNKIUQC6io0'},
     {'author': 'Fallon Collen',
      'channel': 'Fallon Collen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:46](https://www.youtube.com/watch?v=RYrcnhZN5IM&t=106s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'An appropriate investment alternative for you I am a private investor that '
              "wants to earn a better return than what I can at the bank and I'm willing to "
              "share my journey with you so join me inside the course and let's get started "
              'today.',
      'timestamp': 106,
      'timestamp_label': '[00:01:46]',
      'timestamp_seconds': 106,
      'tip': 'An appropriate investment alternative for you I am a private investor that wants '
             "to earn a better return than what I can at the bank and I'm willing to share my "
             "journey with you so join me inside the course and let's get started today.",
      'title': 'Investing in Real Estate Tax Lien Certificates: Case Study - learn Real Estate '
               'Investing (Fallon Collen)',
      'url': 'https://www.youtube.com/watch?v=RYrcnhZN5IM&t=106s',
      'video_id': 'RYrcnhZN5IM'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:25](https://www.youtube.com/watch?v=PSfIJ8cKE5I&t=505s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a learning process so right below me you can see that and right down there "
              'in the description hit the link and take advantage of that free gift from Ted '
              'and thank you for watching foreign.',
      'timestamp': 505,
      'timestamp_label': '[00:08:25]',
      'timestamp_seconds': 505,
      'tip': "It's a learning process so right below me you can see that and right down there "
             'in the description hit the link and take advantage of that free gift from Ted '
             'and thank you for watching foreign.',
      'title': 'Tax Lien Vs. Tax Deed: Which One Is Right for You? (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=PSfIJ8cKE5I&t=505s',
      'video_id': 'PSfIJ8cKE5I'},
     {'author': 'Saen Higgins',
      'channel': 'Saen Higgins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=z3AT7UeX52o&t=154s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Been helpful I look forward to seeing all you Floridians in Florida that you '
              "say Floridians Floridians Floridians let's just talk like friendly I will "
              "arrest you anyways um always love it when I'm there I'm there a lot so ciao "
              'peace thanks.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': 'Been helpful I look forward to seeing all you Floridians in Florida that you say '
             "Floridians Floridians Floridians let's just talk like friendly I will arrest you "
             "anyways um always love it when I'm there I'm there a lot so ciao peace thanks.",
      'title': 'How To: Florida Tax Lien Investing - 18% Returns in 2 Years (Saen Higgins)',
      'url': 'https://www.youtube.com/watch?v=z3AT7UeX52o&t=154s',
      'video_id': 'z3AT7UeX52o'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:24](https://www.youtube.com/watch?v=obD0PGbTJCI&t=504s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Successful click on the description below to grab my free gift so you can learn '
              "more and how to take advantage of this 200y old system I'll see you on the next "
              "video I'm Ted Thomas.",
      'timestamp': 504,
      'timestamp_label': '[00:08:24]',
      'timestamp_seconds': 504,
      'tip': 'Successful click on the description below to grab my free gift so you can learn '
             "more and how to take advantage of this 200y old system I'll see you on the next "
             "video I'm Ted Thomas.",
      'title': 'Tax Lien Sale New Jersey: Your Path to 18% Annually! (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=obD0PGbTJCI&t=504s',
      'video_id': 'obD0PGbTJCI'}],
 8: [{'author': 'Cal Ewing',
      'channel': 'Cal Ewing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=rDGjWMwISOY&t=184s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The county and then you want to go down here you have the map of the United '
              "States and I'm gonna click on Arizona now up here you're gonna have a scroll.",
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'The county and then you want to go down here you have the map of the United '
             "States and I'm gonna click on Arizona now up here you're gonna have a scroll.",
      'title': 'Tax Lien Due Diligence: How to Research US County Tax Lien Auctions (Cal '
               'Ewing)',
      'url': 'https://www.youtube.com/watch?v=rDGjWMwISOY&t=184s',
      'video_id': 'rDGjWMwISOY'},
     {'author': 'Tax Lien Bestie | Sabrina',
      'channel': 'Tax Lien Bestie | Sabrina',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=G8iotxNSgRg&t=358s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, so after you win at the auction, what next? Here's what you'll need "
              'to do. These rules include, but are not limited to, record the tax certificate. '
              "It's your responsibility, and you have 90 days to record it with the county "
              'clerk to maintain its validity.',
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': "All right, so after you win at the auction, what next? Here's what you'll need "
             'to do. These rules include, but are not limited to, record the tax certificate. '
             "It's your responsibility, and you have 90 days to record it with the county "
             'clerk to maintain its validity.',
      'title': 'New Jersey Tax Liens EXPLAINED! Massive Opportunity! (Tax Lien Bestie | '
               'Sabrina)',
      'url': 'https://www.youtube.com/watch?v=G8iotxNSgRg&t=358s',
      'video_id': 'G8iotxNSgRg'},
     {'author': 'Legal Lens',
      'channel': 'Legal Lens',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:58](https://www.youtube.com/watch?v=MCyu08cBm-c&t=538s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "8 years to get another one. So, here's the bottom line. Bankruptcy is a legal "
              'tool, not a moral failure. The automatic stay can stop collectors the moment '
              "you file. Most people keep everything they own, but know your state's "
              'exemptions before you file.',
      'timestamp': 538,
      'timestamp_label': '[00:08:58]',
      'timestamp_seconds': 538,
      'tip': "8 years to get another one. So, here's the bottom line. Bankruptcy is a legal "
             'tool, not a moral failure. The automatic stay can stop collectors the moment you '
             "file. Most people keep everything they own, but know your state's exemptions "
             'before you file.',
      'title': 'What Happens When You File for Bankruptcy (Step by Step) (Legal Lens)',
      'url': 'https://www.youtube.com/watch?v=MCyu08cBm-c&t=538s',
      'video_id': 'MCyu08cBm-c'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:58](https://www.youtube.com/watch?v=08d72pEpig4&t=478s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Automatic stay is a powerful tool to help debtors get a breather while a '
              "bankruptcy proceeding goes forward in another presentation we'll continue "
              'discussing the automatic stay and its limitations.',
      'timestamp': 478,
      'timestamp_label': '[00:07:58]',
      'timestamp_seconds': 478,
      'tip': 'Automatic stay is a powerful tool to help debtors get a breather while a '
             "bankruptcy proceeding goes forward in another presentation we'll continue "
             'discussing the automatic stay and its limitations.',
      'title': 'The Bankruptcy Process: The Automatic Stay Part 1 (LawShelf)',
      'url': 'https://www.youtube.com/watch?v=08d72pEpig4&t=478s',
      'video_id': '08d72pEpig4'},
     {'author': 'All Things Spatial',
      'channel': 'All Things Spatial',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:25](https://www.youtube.com/watch?v=w_jhkHET_rg&t=1105s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The panel folds under the map, and the tab links move to the bottom. The Tools '
              "tab shows how a model runs on your organization's own data. It uses a custom "
              'web tool in ArcGIS Online.',
      'timestamp': 1105,
      'timestamp_label': '[00:18:25]',
      'timestamp_seconds': 1105,
      'tip': 'The panel folds under the map, and the tab links move to the bottom. The Tools '
             "tab shows how a model runs on your organization's own data. It uses a custom web "
             'tool in ArcGIS Online.',
      'title': 'Web GIS Tutorial: Parcels, Map Layers, Analysis and Utility Networks (All '
               'Things Spatial)',
      'url': 'https://www.youtube.com/watch?v=w_jhkHET_rg&t=1105s',
      'video_id': 'w_jhkHET_rg'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:27](https://www.youtube.com/watch?v=mwdmkHEw0Rc&t=447s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Incredibly lucrative business make sure you check out our our training platform '
              'at taxel academy.com we would love to have you in our community hey take care '
              'folks bye-bye.',
      'timestamp': 447,
      'timestamp_label': '[00:07:27]',
      'timestamp_seconds': 447,
      'tip': 'Incredibly lucrative business make sure you check out our our training platform '
             'at taxel academy.com we would love to have you in our community hey take care '
             'folks bye-bye.',
      'title': 'Arizona Tax Lien Law Changes That Affect ALL Investors (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=mwdmkHEw0Rc&t=447s',
      'video_id': 'mwdmkHEw0Rc'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=LsEFs7uqzbA&t=139s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, large population counties can have a lot of tax lien certificate, small '
              "population counties, they'll still have tax auctions but not quite so many. "
              'Indiana is a tax lien state, that means the state legislature made the rule '
              'that they sell tax lien certificates.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'So, large population counties can have a lot of tax lien certificate, small '
             "population counties, they'll still have tax auctions but not quite so many. "
             'Indiana is a tax lien state, that means the state legislature made the rule that '
             'they sell tax lien certificates.',
      'title': 'Is Indiana A Tax Lien State? (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=LsEFs7uqzbA&t=139s',
      'video_id': 'LsEFs7uqzbA'},
     {'author': 'Tax Sale Resources',
      'channel': 'Tax Sale Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:29](https://www.youtube.com/watch?v=HU2epaRqEZE&t=269s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then just filter down to I want to see Nationwide Parcels that are equal to '
              'deed and redeemable deed and I want to see.',
      'timestamp': 269,
      'timestamp_label': '[00:04:29]',
      'timestamp_seconds': 269,
      'tip': 'And then just filter down to I want to see Nationwide Parcels that are equal to '
             'deed and redeemable deed and I want to see.',
      'title': 'Tax Sale Resources Research Platform Walk Through (Tax Sale Resources)',
      'url': 'https://www.youtube.com/watch?v=HU2epaRqEZE&t=269s',
      'video_id': 'HU2epaRqEZE'},
     {'author': 'Tax Lien School Highlights - Dustin Hahn',
      'channel': 'Tax Lien School Highlights - Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=mHvzzGVcYdI&t=89s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So yeah, worst states, California. You know, one of the worst states that comes '
              "to mind is New Jersey. Josh, can you just explain a little bit why we don't "
              'like New Jersey? Yeah, so in bid down the interest rate and it can go all the '
              'way to zero.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'So yeah, worst states, California. You know, one of the worst states that comes '
             "to mind is New Jersey. Josh, can you just explain a little bit why we don't like "
             'New Jersey? Yeah, so in bid down the interest rate and it can go all the way to '
             'zero.',
      'title': 'The Worst States for Tax Liens and Tax Deeds - and Where To Go Instead (Tax '
               'Lien School Highlights - Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=mHvzzGVcYdI&t=89s',
      'video_id': 'mHvzzGVcYdI'},
     {'author': 'Lawyer Greg McIntyre',
      'channel': 'Lawyer Greg McIntyre',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:14](https://www.youtube.com/watch?v=fhcWO24GS_w&t=374s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your wisdom with us regarding Quiet Title action thanks appreciate and stay '
              'tuned for our next part in our litigation series thank you for watching the LW '
              'report peace.',
      'timestamp': 374,
      'timestamp_label': '[00:06:14]',
      'timestamp_seconds': 374,
      'tip': 'Your wisdom with us regarding Quiet Title action thanks appreciate and stay '
             'tuned for our next part in our litigation series thank you for watching the LW '
             'report peace.',
      'title': 'Quiet Title Actions (Lawyer Greg McIntyre)',
      'url': 'https://www.youtube.com/watch?v=fhcWO24GS_w&t=374s',
      'video_id': 'fhcWO24GS_w'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:04](https://www.youtube.com/watch?v=iCR-rdsQrUg&t=304s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Regard but they can be confusing and it can be competitive and some of these '
              'sales they you bid down the interest rates so you know some institutions.',
      'timestamp': 304,
      'timestamp_label': '[00:05:04]',
      'timestamp_seconds': 304,
      'tip': 'Regard but they can be confusing and it can be competitive and some of these '
             'sales they you bid down the interest rates so you know some institutions.',
      'title': 'The Pros and Cons of Tax Lien Investing (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=iCR-rdsQrUg&t=304s',
      'video_id': 'iCR-rdsQrUg'},
     {'author': 'Gerald Harris',
      'channel': 'Gerald Harris',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:19:02](https://www.youtube.com/watch?v=nMj50Itu21Q&t=1142s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Without even stepping foot on it so there's just so much more available online "
              "and that's why we can do it successfully now from canada ted really fills out "
              'the full picture he wants you to be successful.',
      'timestamp': 1142,
      'timestamp_label': '[00:19:02]',
      'timestamp_seconds': 1142,
      'tip': "Without even stepping foot on it so there's just so much more available online "
             "and that's why we can do it successfully now from canada ted really fills out "
             'the full picture he wants you to be successful.',
      'title': "A Beginner's Guide to Investing in Tax Lien Certificates for New Real Estate "
               'Investors (Gerald Harris)',
      'url': 'https://www.youtube.com/watch?v=nMj50Itu21Q&t=1142s',
      'video_id': 'nMj50Itu21Q'},
     {'author': 'Tax Sale Resources',
      'channel': 'Tax Sale Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=6hRZuHmCM0M&t=170s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Taxol finders they're doing everything to get new investors into the platform "
              'so that you could be a better investor until your next investment into our next '
              "video as always happy investing we'll see you on the next video.",
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': "Taxol finders they're doing everything to get new investors into the platform so "
             'that you could be a better investor until your next investment into our next '
             "video as always happy investing we'll see you on the next video.",
      'title': 'What is tax deed and tax lien premium bidding (Tax Sale Resources)',
      'url': 'https://www.youtube.com/watch?v=6hRZuHmCM0M&t=170s',
      'video_id': '6hRZuHmCM0M'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:44](https://www.youtube.com/watch?v=rQco9s4XodM&t=644s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Timeframe it doesn't actually go through a true foreclosure when we consider "
              "foreclosure judicially it's not like that it doesn't actually go through that "
              "foreclosure it's just simply the lender you know removing the ownership rights "
              'from the from the borrower.',
      'timestamp': 644,
      'timestamp_label': '[00:10:44]',
      'timestamp_seconds': 644,
      'tip': "Timeframe it doesn't actually go through a true foreclosure when we consider "
             "foreclosure judicially it's not like that it doesn't actually go through that "
             "foreclosure it's just simply the lender you know removing the ownership rights "
             'from the from the borrower.',
      'title': 'Judicial vs. Nonjudicial Foreclosures Explained (Tax Sale Secrets)',
      'url': 'https://www.youtube.com/watch?v=rQco9s4XodM&t=644s',
      'video_id': 'rQco9s4XodM'},
     {'author': 'Global Estate Hub LLC',
      'channel': 'Global Estate Hub LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=q4Kqh7Vleyg&t=210s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There's some fine print to pay attention to. While 120 days is the federal "
              'standard under Title 28 of the US Code, you always have to check your local '
              'laws. The rule is actually 120 days or the period allowable under state law, '
              'whichever is longer.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': "There's some fine print to pay attention to. While 120 days is the federal "
             'standard under Title 28 of the US Code, you always have to check your local '
             'laws. The rule is actually 120 days or the period allowable under state law, '
             'whichever is longer.',
      'title': 'IRS Right of Redemption Explained: Avoid This Foreclosure Trap! (Global Estate '
               'Hub LLC)',
      'url': 'https://www.youtube.com/watch?v=q4Kqh7Vleyg&t=210s',
      'video_id': 'q4Kqh7Vleyg'}],
 9: [{'author': 'Real Estate Ninja',
      'channel': 'Real Estate Ninja',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=w8WivuvhKRI&t=209s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t always require taking out large loans. That said, research is critical. "
              'Properties can have issues. Some leans may take time to resolve. Rules vary '
              'widely by state and even by county. Education and due diligence matter a lot '
              'here.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': "'t always require taking out large loans. That said, research is critical. "
             'Properties can have issues. Some leans may take time to resolve. Rules vary '
             'widely by state and even by county. Education and due diligence matter a lot '
             'here.',
      'title': 'A Low-Cost Way Into Real Estate | Tax Lien Investing Explained (Real Estate '
               'Ninja)',
      'url': 'https://www.youtube.com/watch?v=w8WivuvhKRI&t=209s',
      'video_id': 'w8WivuvhKRI'},
     {'author': 'The Deed | Real Estate',
      'channel': 'The Deed | Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:29](https://www.youtube.com/watch?v=sb6T0Xe5siY&t=449s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And third, has your state updated its surplus rules since the Tyler decision '
              'came down in 2023? Write down the county name. Those two details are what a '
              'counselor or a clerk will ask for first.',
      'timestamp': 449,
      'timestamp_label': '[00:07:29]',
      'timestamp_seconds': 449,
      'tip': 'And third, has your state updated its surplus rules since the Tyler decision '
             'came down in 2023? Write down the county name. Those two details are what a '
             'counselor or a clerk will ask for first.',
      'title': 'Tyler v. Hennepin County: A $2,300 Tax Debt, a $40,000 Condo (The Deed | Real '
               'Estate)',
      'url': 'https://www.youtube.com/watch?v=sb6T0Xe5siY&t=449s',
      'video_id': 'sb6T0Xe5siY'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=TRZbdE4y2sc&t=323s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, now I don't make all the rules, but all the enforcement is done by "
              'the board of supervisors and the county commissioners. All the rules, the '
              "statutes are made at the state level. So we're just gonna follow the law and do "
              'it the correct way.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': "All right, now I don't make all the rules, but all the enforcement is done by "
             'the board of supervisors and the county commissioners. All the rules, the '
             "statutes are made at the state level. So we're just gonna follow the law and do "
             'it the correct way.',
      'title': 'Do It Yourself Quiet Title (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=TRZbdE4y2sc&t=323s',
      'video_id': 'TRZbdE4y2sc'},
     {'author': 'The Jackie Jackson | Tax Deed & Real Estate Coach',
      'channel': 'The Jackie Jackson | Tax Deed & Real Estate Coach',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:16](https://www.youtube.com/watch?v=fbdN21IB-I0&t=256s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, in the state of Florida, state of Florida is both a lien as well as a '
              'deed state. That means that we have both auctions all the time, right? Now, '
              "Florida's lien auctions, tax liens, what that means is that Mr.",
      'timestamp': 256,
      'timestamp_label': '[00:04:16]',
      'timestamp_seconds': 256,
      'tip': 'Well, in the state of Florida, state of Florida is both a lien as well as a deed '
             "state. That means that we have both auctions all the time, right? Now, Florida's "
             'lien auctions, tax liens, what that means is that Mr.',
      'title': 'How to Buy County-Held Tax Liens on LienHub (Florida Example) (The Jackie '
               'Jackson | Tax Deed & Real Estate Coach)',
      'url': 'https://www.youtube.com/watch?v=fbdN21IB-I0&t=256s',
      'video_id': 'fbdN21IB-I0'},
     {'author': 'Red Lotus Chic',
      'channel': 'Red Lotus Chic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=ehSkuiHT060&t=261s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'A deed is in a nutshell a deed is the legal document that is signed and '
              'delivered to the county that actually transfers the property and the legal.',
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': 'A deed is in a nutshell a deed is the legal document that is signed and '
             'delivered to the county that actually transfers the property and the legal.',
      'title': 'Introduction to Tax Lien and Tax Deed Investing 101 (Red Lotus Chic)',
      'url': 'https://www.youtube.com/watch?v=ehSkuiHT060&t=261s',
      'video_id': 'ehSkuiHT060'},
     {'author': 'Tax Sale Resources',
      'channel': 'Tax Sale Resources',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=d67aVfAEUxg&t=136s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Nebraska legal aid brought a defense and counter claims and they added in the '
              'county the County Treasurer and our attorney general claiming that the.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': 'Nebraska legal aid brought a defense and counter claims and they added in the '
             'county the County Treasurer and our attorney general claiming that the.',
      'title': 'Tyler v. Hennepin County and the Impact on Nebraska Tax Sales (Tax Sale '
               'Resources)',
      'url': 'https://www.youtube.com/watch?v=d67aVfAEUxg&t=136s',
      'video_id': 'd67aVfAEUxg'},
     {'author': 'Quiet Title Michigan',
      'channel': 'Quiet Title Michigan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=7yD_brKdgXk&t=20s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Property and getting the deed hi my name is Darren Findlay and I'm an attorney "
              'and I run a law firm out of Royal Oak Michigan that does quiet title work '
              'statewide throughout the state of Michigan.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Property and getting the deed hi my name is Darren Findlay and I'm an attorney "
             'and I run a law firm out of Royal Oak Michigan that does quiet title work '
             'statewide throughout the state of Michigan.',
      'title': 'How to Buy Tax Sale Properties and when to Quiet Title  - (877) YOUR-FIRM '
               '(Quiet Title Michigan)',
      'url': 'https://www.youtube.com/watch?v=7yD_brKdgXk&t=20s',
      'video_id': '7yD_brKdgXk'},
     {'author': 'Dustin Hahn',
      'channel': 'Dustin Hahn',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=uiH28IFKgC4&t=121s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'States you can buy over-the-counter liens in a lean state but we want to deal '
              'with Deeds okay so an over-the-counter deed is a property that.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'States you can buy over-the-counter liens in a lean state but we want to deal '
             'with Deeds okay so an over-the-counter deed is a property that.',
      'title': 'How 2 Buy Dirt Cheap Over The Counter Tax Deeds Today (Dustin Hahn)',
      'url': 'https://www.youtube.com/watch?v=uiH28IFKgC4&t=121s',
      'video_id': 'uiH28IFKgC4'},
     {'author': 'Oral Arguments, with Context',
      'channel': 'Oral Arguments, with Context',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:30](https://www.youtube.com/watch?v=SgoM18e6gXQ&t=1470s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's the Supreme Court's decision in Jackson. Mere approval isn't compulsion. "
              "That's the Supreme Court's decision in Bloom. Brentwood entwinement is entirely "
              "absent. And heavy regulation doesn't create state action under Halek. The "
              'petition should be denied.',
      'timestamp': 1470,
      'timestamp_label': '[00:24:30]',
      'timestamp_seconds': 1470,
      'tip': "That's the Supreme Court's decision in Jackson. Mere approval isn't compulsion. "
             "That's the Supreme Court's decision in Bloom. Brentwood entwinement is entirely "
             "absent. And heavy regulation doesn't create state action under Halek. The "
             'petition should be denied.',
      'title': 'Jones v. SEC — 5th Cir. (Nov 2, 2026) (Oral Arguments, with Context)',
      'url': 'https://www.youtube.com/watch?v=SgoM18e6gXQ&t=1470s',
      'video_id': 'SgoM18e6gXQ'},
     {'author': 'Premier Wealth Builders',
      'channel': 'Premier Wealth Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=AYiTxfuCWHk&t=64s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But after three years, it can be someone else can pay the taxes that were paid '
              'earlier, and then they can >> no, no, no, no. So what state are you talking '
              'about? You said that you bought it for three, four years. So the way the rules '
              'work, >> Okay.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'But after three years, it can be someone else can pay the taxes that were paid '
             'earlier, and then they can >> no, no, no, no. So what state are you talking '
             'about? You said that you bought it for three, four years. So the way the rules '
             'work, >> Okay.',
      'title': 'Are You Losing Money on Tax Liens? The Truth About Supplemental Taxes (Premier '
               'Wealth Builders)',
      'url': 'https://www.youtube.com/watch?v=AYiTxfuCWHk&t=64s',
      'video_id': 'AYiTxfuCWHk'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=0I_mhnrF0So&t=187s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Overview of over bid and premium tax lien states hopefully this helped you for '
              'more information on textile investing head on over to tanks all academy.com '
              "that's tax law academy.com take care folks buh-bye.",
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': 'Overview of over bid and premium tax lien states hopefully this helped you for '
             'more information on textile investing head on over to tanks all academy.com '
             "that's tax law academy.com take care folks buh-bye.",
      'title': 'Tax Lien Overbid Auction Process (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=0I_mhnrF0So&t=187s',
      'video_id': '0I_mhnrF0So'},
     {'author': '4closurehelp777',
      'channel': '4closurehelp777',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:02](https://www.youtube.com/watch?v=YmgFMy7GMNk&t=302s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Jurisdiction and venue basically have to say you know you have to have that on '
              'your complaint jurisdiction means what is the court in this is the state court '
              'real estate settlement.',
      'timestamp': 302,
      'timestamp_label': '[00:05:02]',
      'timestamp_seconds': 302,
      'tip': 'Jurisdiction and venue basically have to say you know you have to have that on '
             'your complaint jurisdiction means what is the court in this is the state court '
             'real estate settlement.',
      'title': 'how to file a quiet title complaint and lis pendens (4closurehelp777)',
      'url': 'https://www.youtube.com/watch?v=YmgFMy7GMNk&t=302s',
      'video_id': 'YmgFMy7GMNk'},
     {'author': 'Tax Sale Secrets',
      'channel': 'Tax Sale Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:36:28](https://www.youtube.com/watch?v=AO4ZqaMio7s&t=5788s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Interested in this particular auction you're going to want to go through review "
              'the terms of sale uh you know just review all of this information we go ahead '
              'and click on the the uh auditor right.',
      'timestamp': 5788,
      'timestamp_label': '[01:36:28]',
      'timestamp_seconds': 5788,
      'tip': "Interested in this particular auction you're going to want to go through review "
             'the terms of sale uh you know just review all of this information we go ahead '
             'and click on the the uh auditor right.',
      'title': 'Tax Lien Certificates vs Tax Deeds: Online Auction SECRETS! (Tax Sale Secrets)',
      'url': 'https://www.youtube.com/watch?v=AO4ZqaMio7s&t=5788s',
      'video_id': 'AO4ZqaMio7s'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=D8YYUGD6y9I&t=283s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Investment training course offer click on that join button once you're over on "
              "the side again that's tax law Jaime comm and click on join hey take care folks "
              'bye.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': "Investment training course offer click on that join button once you're over on "
             "the side again that's tax law Jaime comm and click on join hey take care folks "
             'bye.',
      'title': 'Redeemable Tax Deeds Vs Tax Liens (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=D8YYUGD6y9I&t=283s',
      'video_id': 'D8YYUGD6y9I'},
     {'author': 'Lien Ledger',
      'channel': 'Lien Ledger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:07](https://www.youtube.com/watch?v=ul1onF24UbM&t=367s)',
      'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                   'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                   'foreclosure rules (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Owners are entitled to their surplus equity. For buyers, it means auction rules '
              "keep shifting. Check your state's surplus rules before you bid. Every county "
              'runs its own auction. Different rules, deadlines, and deposits. Read the '
              "county's terms before you bring a dollar.",
      'timestamp': 367,
      'timestamp_label': '[00:06:07]',
      'timestamp_seconds': 367,
      'tip': 'Owners are entitled to their surplus equity. For buyers, it means auction rules '
             "keep shifting. Check your state's surplus rules before you bid. Every county "
             'runs its own auction. Different rules, deadlines, and deposits. Read the '
             "county's terms before you bring a dollar.",
      'title': 'Tax Liens vs Tax Deeds: Which One Should You Buy? (Lien Ledger)',
      'url': 'https://www.youtube.com/watch?v=ul1onF24UbM&t=367s',
      'video_id': 'ul1onF24UbM'}],
 10: [{'author': 'The Jackie Jackson | Tax Deed & Real Estate Coach',
       'channel': 'The Jackie Jackson | Tax Deed & Real Estate Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:44](https://www.youtube.com/watch?v=Pz2ZCMuIox4&t=584s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'County because they give you the property address the assessed value the '
               'parcel ID the opening bid the certificate number all of these things.',
       'timestamp': 584,
       'timestamp_label': '[00:09:44]',
       'timestamp_seconds': 584,
       'tip': 'County because they give you the property address the assessed value the parcel '
              'ID the opening bid the certificate number all of these things.',
       'title': 'Where Are Tax Deed Auctions Held? How I Find Online County Sales (The Jackie '
                'Jackson | Tax Deed & Real Estate Coach)',
       'url': 'https://www.youtube.com/watch?v=Pz2ZCMuIox4&t=584s',
       'video_id': 'Pz2ZCMuIox4'},
      {'author': 'Behind The Servicing',
       'channel': 'Behind The Servicing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:16](https://www.youtube.com/watch?v=au90-c2Pwvo&t=136s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It carries devastating statutory fangs. Under section 362 K, an individual '
               'injured by any willful violation of the automatic stay shall recover actual '
               'damages, including costs and attorney fees, and in appropriate circumstances '
               'may recover punitive damages.',
       'timestamp': 136,
       'timestamp_label': '[00:02:16]',
       'timestamp_seconds': 136,
       'tip': 'It carries devastating statutory fangs. Under section 362 K, an individual '
              'injured by any willful violation of the automatic stay shall recover actual '
              'damages, including costs and attorney fees, and in appropriate circumstances '
              'may recover punitive damages.',
       'title': 'Episode 01 Automatic Stay Guillotine (Behind The Servicing)',
       'url': 'https://www.youtube.com/watch?v=au90-c2Pwvo&t=136s',
       'video_id': 'au90-c2Pwvo'},
      {'author': 'Tax Sale Lists',
       'channel': 'Tax Sale Lists',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:33](https://www.youtube.com/watch?v=ymnkPFHPY40&t=33s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What are Over the Counter or OTC liens Over the counter liens, also known as '
               'OTC liens sound, when you listen to some gurus, to be the way to go. All you '
               'do is send a check to the county and they sell you a lien. These are liens '
               'that did not sell at the tax sale.',
       'timestamp': 33,
       'timestamp_label': '[00:00:33]',
       'timestamp_seconds': 33,
       'tip': 'What are Over the Counter or OTC liens Over the counter liens, also known as '
              'OTC liens sound, when you listen to some gurus, to be the way to go. All you do '
              'is send a check to the county and they sell you a lien. These are liens that '
              'did not sell at the tax sale.',
       'title': 'Tax Lien Investing - Over The Counter (OTC) Tax Liens (Tax Sale Lists)',
       'url': 'https://www.youtube.com/watch?v=ymnkPFHPY40&t=33s',
       'video_id': 'ymnkPFHPY40'},
      {'author': 'Dustin Hahn',
       'channel': 'Dustin Hahn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=TnDzVaeksNc&t=78s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s a chance you could do it, too. But you need to take action. That's how you "
               "know we're not an AI video here. All right, let's get to it. So, Florida is a "
               'great state for over-thec counter properties.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': "'s a chance you could do it, too. But you need to take action. That's how you "
              "know we're not an AI video here. All right, let's get to it. So, Florida is a "
              'great state for over-thec counter properties.',
       'title': 'Top 5 OTC Tax Deed States Today! Dirt Cheap Property Here (Dustin Hahn)',
       'url': 'https://www.youtube.com/watch?v=TnDzVaeksNc&t=78s',
       'video_id': 'TnDzVaeksNc'},
      {'author': 'Florida Trust, Real Estate, Probate, & Foreclosure',
       'channel': 'Florida Trust, Real Estate, Probate, & Foreclosure',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:47](https://www.youtube.com/watch?v=RlQwxNYiqok&t=827s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's who cares if it's attached to the complaint? That's not summary judgment "
               'evidence. There is an affidavit of the clerk, a certificate of mailing '
               'notices, which provides that the notices were mailed to the horns by both '
               'certified mail and requested >> record.',
       'timestamp': 827,
       'timestamp_label': '[00:13:47]',
       'timestamp_seconds': 827,
       'tip': "It's who cares if it's attached to the complaint? That's not summary judgment "
              'evidence. There is an affidavit of the clerk, a certificate of mailing notices, '
              'which provides that the notices were mailed to the horns by both certified mail '
              'and requested >> record.',
       'title': '🏠 Tax Deed Challenge: Defective Notice, Rushed Auction & Summary Judgment '
                'Without Evidence (Florida Trust, Real Estate, Probate, & Foreclosure)',
       'url': 'https://www.youtube.com/watch?v=RlQwxNYiqok&t=827s',
       'video_id': 'RlQwxNYiqok'},
      {'author': 'TaxLienLady',
       'channel': 'TaxLienLady',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:22](https://www.youtube.com/watch?v=7ybooMbrE58&t=382s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That we could go to more tax sales I started training people to do due '
               'diligence in bid at the tax sales for me and meanwhile I was building my own '
               'portfolio of tax leans and later tax.',
       'timestamp': 382,
       'timestamp_label': '[00:06:22]',
       'timestamp_seconds': 382,
       'tip': 'That we could go to more tax sales I started training people to do due '
              'diligence in bid at the tax sales for me and meanwhile I was building my own '
              'portfolio of tax leans and later tax.',
       'title': 'The Truth About Tax Lien Investing (TaxLienLady)',
       'url': 'https://www.youtube.com/watch?v=7ybooMbrE58&t=382s',
       'video_id': '7ybooMbrE58'},
      {'author': 'IRS FBAR Tax Attorney | Offshore Reporting Defense',
       'channel': 'IRS FBAR Tax Attorney | Offshore Reporting Defense',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:53](https://www.youtube.com/watch?v=D-ia73OSPG0&t=173s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If your income barely covers living expenses, you can request CNC. Collection '
               'activity pauses, but this is temporary. The IRS reviews your finances '
               'periodically and the lien stays in place. Choosing the wrong path costs you '
               'time and leverage.',
       'timestamp': 173,
       'timestamp_label': '[00:02:53]',
       'timestamp_seconds': 173,
       'tip': 'If your income barely covers living expenses, you can request CNC. Collection '
              'activity pauses, but this is temporary. The IRS reviews your finances '
              'periodically and the lien stays in place. Choosing the wrong path costs you '
              'time and leverage.',
       'title': "Federal Tax Lien Filed Against You? Here's Exactly What to Do in 2026 (IRS "
                'FBAR Tax Attorney | Offshore Reporting Defense)',
       'url': 'https://www.youtube.com/watch?v=D-ia73OSPG0&t=173s',
       'video_id': 'D-ia73OSPG0'},
      {'author': 'Tax Sale Secrets',
       'channel': 'Tax Sale Secrets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:06](https://www.youtube.com/watch?v=-1glwzvZBoQ&t=1146s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Uh you know, that we can see. We've got all of these here. You know, these are "
               'all auctions opening up in the next 3 to 4 weeks. Yeah, and the auction takes '
               'place about 30 days after it opens. Give or take a couple of days.',
       'timestamp': 1146,
       'timestamp_label': '[00:19:06]',
       'timestamp_seconds': 1146,
       'tip': "Uh you know, that we can see. We've got all of these here. You know, these are "
              'all auctions opening up in the next 3 to 4 weeks. Yeah, and the auction takes '
              'place about 30 days after it opens. Give or take a couple of days.',
       'title': 'NEW JERSEY TAX LIEN SALE: Everything You Need to Know (Tax Sale Secrets)',
       'url': 'https://www.youtube.com/watch?v=-1glwzvZBoQ&t=1146s',
       'video_id': '-1glwzvZBoQ'},
      {'author': 'Tax Sale Support',
       'channel': 'Tax Sale Support',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:34](https://www.youtube.com/watch?v=5t3VbtPlElc&t=874s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Still so many counties throughout the u.s. that are that are still relying on '
               "live live auctions so they're basically still relying on the number of people.",
       'timestamp': 874,
       'timestamp_label': '[00:14:34]',
       'timestamp_seconds': 874,
       'tip': 'Still so many counties throughout the u.s. that are that are still relying on '
              "live live auctions so they're basically still relying on the number of people.",
       'title': 'Tax Lien & Tax Deed "Over the Counter" OTC Training! (Tax Sale Support)',
       'url': 'https://www.youtube.com/watch?v=5t3VbtPlElc&t=874s',
       'video_id': '5t3VbtPlElc'},
      {'author': 'Tax Sale Resources',
       'channel': 'Tax Sale Resources',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:58](https://www.youtube.com/watch?v=XbThUArmcIE&t=238s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Button don't forget don't forget to hit the notification bell stay up to date "
               "on what's going on and check out taxol resources and until next time have a "
               'great investment.',
       'timestamp': 238,
       'timestamp_label': '[00:03:58]',
       'timestamp_seconds': 238,
       'tip': "Button don't forget don't forget to hit the notification bell stay up to date "
              "on what's going on and check out taxol resources and until next time have a "
              'great investment.',
       'title': 'Why Do Investors Bid Down Florida Tax Lien Interest Rate To 0.25? (Tax Sale '
                'Resources)',
       'url': 'https://www.youtube.com/watch?v=XbThUArmcIE&t=238s',
       'video_id': 'XbThUArmcIE'},
      {'author': 'Ted Thomas',
       'channel': 'Ted Thomas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=KoANRHO6Uko&t=88s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Buy one and you give your money to the county and then the county gives you a '
               "tax lien certificate so I hope that explains it okay well now we've got some.",
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'Buy one and you give your money to the county and then the county gives you a '
              "tax lien certificate so I hope that explains it okay well now we've got some.",
       'title': 'MAKING MONEY FROM HOME: Tax Lien Auctions Online Guide! (Ted Thomas)',
       'url': 'https://www.youtube.com/watch?v=KoANRHO6Uko&t=88s',
       'video_id': 'KoANRHO6Uko'},
      {'author': 'Former IRS Agent Representation   4.2M Views',
       'channel': 'Former IRS Agent Representation   4.2M Views',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:31](https://www.youtube.com/watch?v=Y2mRqIi8jqY&t=331s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Questions give me a call you need representation give me a call if the answer '
               'this information was good please give me a subscription we really thrive on '
               'those because YouTube does thank you very much leave questions and comments up '
               'there I thank you for listening.',
       'timestamp': 331,
       'timestamp_label': '[00:05:31]',
       'timestamp_seconds': 331,
       'tip': 'Questions give me a call you need representation give me a call if the answer '
              'this information was good please give me a subscription we really thrive on '
              'those because YouTube does thank you very much leave questions and comments up '
              'there I thank you for listening.',
       'title': 'Everything You Need To Know About FEDERAL TAX LIEN Explained By a Former IRS '
                'Agent (Former IRS Agent Representation   4.2M Views)',
       'url': 'https://www.youtube.com/watch?v=Y2mRqIi8jqY&t=331s',
       'video_id': 'Y2mRqIi8jqY'},
      {'author': 'Logan Allec',
       'channel': 'Logan Allec',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:31](https://www.youtube.com/watch?v=_kLMdX9sR6Y&t=571s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Here and it shows up little a little calendar here that you can uh you can '
               "book yourself on so anyway folks thanks so much for watching and I'll see you "
               'next video bye.',
       'timestamp': 571,
       'timestamp_label': '[00:09:31]',
       'timestamp_seconds': 571,
       'tip': 'Here and it shows up little a little calendar here that you can uh you can book '
              "yourself on so anyway folks thanks so much for watching and I'll see you next "
              'video bye.',
       'title': 'Does a Notice of Federal Tax Lien Appear on Your Credit Report? (Logan Allec)',
       'url': 'https://www.youtube.com/watch?v=_kLMdX9sR6Y&t=571s',
       'video_id': '_kLMdX9sR6Y'},
      {'author': 'Tax Sale Academy',
       'channel': 'Tax Sale Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:00](https://www.youtube.com/watch?v=yUKmyPRuIsY&t=180s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The iceberg as far as what we offer for training for new tanks sell investors '
               'if you like more information on investing in text falton real estate head on '
               "our attacks all academy.com that's tax all academy.com have a water when I "
               'folks take care.',
       'timestamp': 180,
       'timestamp_label': '[00:03:00]',
       'timestamp_seconds': 180,
       'tip': 'The iceberg as far as what we offer for training for new tanks sell investors '
              'if you like more information on investing in text falton real estate head on '
              "our attacks all academy.com that's tax all academy.com have a water when I "
              'folks take care.',
       'title': 'Tax Sale Tip: Google Street View For Area Trends (Tax Deed & Lien Investing) '
                '(Tax Sale Academy)',
       'url': 'https://www.youtube.com/watch?v=yUKmyPRuIsY&t=180s',
       'video_id': 'yUKmyPRuIsY'},
      {'author': 'Personal Bankruptcy Law Atlanta',
       'channel': 'Personal Bankruptcy Law Atlanta',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=MoTnCzda1JA&t=102s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Ahead and start foreclosure proceedings and this is a clear violation of the '
               "automatic stay because if you're in bankruptcy uh you cannot take any action.",
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'Ahead and start foreclosure proceedings and this is a clear violation of the '
              "automatic stay because if you're in bankruptcy uh you cannot take any action.",
       'title': 'Bankruptcy Court Refuses to Award Damages for Automatic Stay Violation '
                '(Personal Bankruptcy Law Atlanta)',
       'url': 'https://www.youtube.com/watch?v=MoTnCzda1JA&t=102s',
       'video_id': 'MoTnCzda1JA'}],
 11: [{'author': 'Personal Bankruptcy Law Atlanta',
       'channel': 'Personal Bankruptcy Law Atlanta',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:14](https://www.youtube.com/watch?v=MoTnCzda1JA&t=314s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'About pursuing a claim uh for damages under Section 362 of the bankruptcy code '
               'uh that you really make sure that you have some actual actual damages and the.',
       'timestamp': 314,
       'timestamp_label': '[00:05:14]',
       'timestamp_seconds': 314,
       'tip': 'About pursuing a claim uh for damages under Section 362 of the bankruptcy code '
              'uh that you really make sure that you have some actual actual damages and the.',
       'title': 'Bankruptcy Court Refuses to Award Damages for Automatic Stay Violation '
                '(Personal Bankruptcy Law Atlanta)',
       'url': 'https://www.youtube.com/watch?v=MoTnCzda1JA&t=314s',
       'video_id': 'MoTnCzda1JA'},
      {'author': 'Ted Thomas',
       'channel': 'Ted Thomas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:06](https://www.youtube.com/watch?v=O8MWhOJE6Oc&t=126s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The county will sell the property without a mortgage or a deed of trust loan. '
               'However, there could be other challenges of property. So to make sure the '
               "other challenges are cleared that's why they came up with a quiet title "
               'action.',
       'timestamp': 126,
       'timestamp_label': '[00:02:06]',
       'timestamp_seconds': 126,
       'tip': 'The county will sell the property without a mortgage or a deed of trust loan. '
              'However, there could be other challenges of property. So to make sure the other '
              "challenges are cleared that's why they came up with a quiet title action.",
       'title': 'What Is a Quiet Title Action by the Tax Lien Certificates & Tax Deeds '
                'Authority (Ted Thomas)',
       'url': 'https://www.youtube.com/watch?v=O8MWhOJE6Oc&t=126s',
       'video_id': 'O8MWhOJE6Oc'},
      {'author': 'Dustin Hahn',
       'channel': 'Dustin Hahn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=hK5QVUgFulI&t=99s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Rate so they'll say 18 16% bid down I'll take 7% okay unless it's an overthe "
               'counter then you get the full interest rate but in Maryland what they say is.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': "Rate so they'll say 18 16% bid down I'll take 7% okay unless it's an overthe "
              'counter then you get the full interest rate but in Maryland what they say is.',
       'title': 'Earn Solid 6-20% ROI As A Beginner In Maryland Tax Liens! (Dustin Hahn)',
       'url': 'https://www.youtube.com/watch?v=hK5QVUgFulI&t=99s',
       'video_id': 'hK5QVUgFulI'},
      {'author': 'Next Generation',
       'channel': 'Next Generation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=l9-Us7KWWPM&t=15s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Nicholas started his career in the title industry in 1986 as a title '
               'abstractor in hunted County in 1990 he was hired as a chief title examiner and '
               'manager of.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Nicholas started his career in the title industry in 1986 as a title abstractor '
              'in hunted County in 1990 he was hired as a chief title examiner and manager of.',
       'title': 'Tax Lien Investments and Self-Directed Retirement Plans (Next Generation)',
       'url': 'https://www.youtube.com/watch?v=l9-Us7KWWPM&t=15s',
       'video_id': 'l9-Us7KWWPM'},
      {'author': 'onlinetaxsales',
       'channel': 'onlinetaxsales',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:11](https://www.youtube.com/watch?v=OU-LqZt4nCs&t=491s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The power of not only investing in tax Lan certificates in different states at '
               'different interest rates uh but the power of what we call compounding.',
       'timestamp': 491,
       'timestamp_label': '[00:08:11]',
       'timestamp_seconds': 491,
       'tip': 'The power of not only investing in tax Lan certificates in different states at '
              'different interest rates uh but the power of what we call compounding.',
       'title': 'LIVE "Actual" County Tax Sale Research - How to Research & Purchase Tax Liens '
                '& Tax Deeds (onlinetaxsales)',
       'url': 'https://www.youtube.com/watch?v=OU-LqZt4nCs&t=491s',
       'video_id': 'OU-LqZt4nCs'},
      {'author': 'Alex Goldovsky',
       'channel': 'Alex Goldovsky',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:59](https://www.youtube.com/watch?v=O6HhpnnQADM&t=719s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ve got to be able to move through in a you know, if we can do our goal is to "
               'have a conversion cycle of these type of assets in 120 to 150 days.',
       'timestamp': 719,
       'timestamp_label': '[00:11:59]',
       'timestamp_seconds': 719,
       'tip': "'ve got to be able to move through in a you know, if we can do our goal is to "
              'have a conversion cycle of these type of assets in 120 to 150 days.',
       'title': 'Podcast EP 59: Tax Liens, HOA Liens & Title Traps Every Investor Must Know '
                '(Alex Goldovsky)',
       'url': 'https://www.youtube.com/watch?v=O6HhpnnQADM&t=719s',
       'video_id': 'O6HhpnnQADM'},
      {'author': 'skwcentraltraining',
       'channel': 'skwcentraltraining',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:48](https://www.youtube.com/watch?v=e-CuINE8x-g&t=48s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Municipality which is panal county and Arizona or I'm sorry Pima County okay "
               'then the banks will foreclose now since the bank bailout in.',
       'timestamp': 48,
       'timestamp_label': '[00:00:48]',
       'timestamp_seconds': 48,
       'tip': "Municipality which is panal county and Arizona or I'm sorry Pima County okay "
              'then the banks will foreclose now since the bank bailout in.',
       'title': 'SKW Central | Tax Lien investing part 3 (skwcentraltraining)',
       'url': 'https://www.youtube.com/watch?v=e-CuINE8x-g&t=48s',
       'video_id': 'e-CuINE8x-g'},
      {'author': 'Esri Industries',
       'channel': 'Esri Industries',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:10](https://www.youtube.com/watch?v=rcW3BV0Kzh0&t=250s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The public so as I mentioned the first webinar covered field operations one '
               "way to think about today's webinar is that we have now collected our parcel "
               "data in the field and we're ready to manage it day by day.",
       'timestamp': 250,
       'timestamp_label': '[00:04:10]',
       'timestamp_seconds': 250,
       'tip': 'The public so as I mentioned the first webinar covered field operations one way '
              "to think about today's webinar is that we have now collected our parcel data in "
              "the field and we're ready to manage it day by day.",
       'title': 'Esri Land Administration Latin American Webinar Series, Webinar #2 Parcel '
                'Management With GIS (Esri Industries)',
       'url': 'https://www.youtube.com/watch?v=rcW3BV0Kzh0&t=250s',
       'video_id': 'rcW3BV0Kzh0'},
      {'author': 'Tax Sale Secrets',
       'channel': 'Tax Sale Secrets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:13](https://www.youtube.com/watch?v=GxMaS0YFT1Y&t=493s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Over-the-counter you don't want to go through all of these next you know five "
               'steps and and and have it be on a property that is no longer available.',
       'timestamp': 493,
       'timestamp_label': '[00:08:13]',
       'timestamp_seconds': 493,
       'tip': "Over-the-counter you don't want to go through all of these next you know five "
              'steps and and and have it be on a property that is no longer available.',
       'title': 'Tax Deed Research Masterclass: County Records to CMA! (Tax Sale Secrets)',
       'url': 'https://www.youtube.com/watch?v=GxMaS0YFT1Y&t=493s',
       'video_id': 'GxMaS0YFT1Y'},
      {'author': 'Florida Trust, Real Estate, Probate, & Foreclosure',
       'channel': 'Florida Trust, Real Estate, Probate, & Foreclosure',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:20](https://www.youtube.com/watch?v=zPDMr-7eAOc&t=140s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Effective code enforcement program that allows you to contribute to the goals '
               'of the community which is to put property into productive and constructive use '
               'and to see that communities are revitalized.',
       'timestamp': 140,
       'timestamp_label': '[00:02:20]',
       'timestamp_seconds': 140,
       'tip': 'Effective code enforcement program that allows you to contribute to the goals '
              'of the community which is to put property into productive and constructive use '
              'and to see that communities are revitalized.',
       'title': '🏠 Lien Clearing 101: How Code Enforcement Transforms Blight Into Opportunity '
                '| Part 1 (Florida Trust, Real Estate, Probate, & Foreclosure)',
       'url': 'https://www.youtube.com/watch?v=zPDMr-7eAOc&t=140s',
       'video_id': 'zPDMr-7eAOc'},
      {'author': 'Jason Porter',
       'channel': 'Jason Porter',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=bnQAJL9-zo0&t=101s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Until you look at the flood zone and the flood zone shows that these things '
               "for half the year are probably going to be underwater so they're worthless "
               'right one mistake in tax debt investing you could lose a ton of money so do it '
               "right that's tip number two get your gis.",
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'Until you look at the flood zone and the flood zone shows that these things for '
              "half the year are probably going to be underwater so they're worthless right "
              'one mistake in tax debt investing you could lose a ton of money so do it right '
              "that's tip number two get your gis.",
       'title': 'Tax Deed Tip #2 - GIS Mapping - It’s a MUST. (Jason Porter)',
       'url': 'https://www.youtube.com/watch?v=bnQAJL9-zo0&t=101s',
       'video_id': 'bnQAJL9-zo0'},
      {'author': 'Rent To Retirement',
       'channel': 'Rent To Retirement',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:54](https://www.youtube.com/watch?v=iOoZ743spRo&t=354s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Rent retirement will be here to help you understand real estate further your '
               'overall financial education and show you the path to a successful future in '
               'real estate investing.',
       'timestamp': 354,
       'timestamp_label': '[00:05:54]',
       'timestamp_seconds': 354,
       'tip': 'Rent retirement will be here to help you understand real estate further your '
              'overall financial education and show you the path to a successful future in '
              'real estate investing.',
       'title': 'PROS AND CONS OF TAX LIEN INVESTING (Rent To Retirement)',
       'url': 'https://www.youtube.com/watch?v=iOoZ743spRo&t=354s',
       'video_id': 'iOoZ743spRo'},
      {'author': 'Advanta IRA',
       'channel': 'Advanta IRA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:45](https://www.youtube.com/watch?v=c3YDDPR5wVo&t=885s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Thousand one hundred going once thirteen thousand going once thirteen thousand '
               "going twice fourteen thousand fourteen thousand 15 100 15 000 ain't playing no "
               'more twenty thousand going once twenty thousand going twice so that renegade.',
       'timestamp': 885,
       'timestamp_label': '[00:14:45]',
       'timestamp_seconds': 885,
       'tip': 'Thousand one hundred going once thirteen thousand going once thirteen thousand '
              "going twice fourteen thousand fourteen thousand 15 100 15 000 ain't playing no "
              'more twenty thousand going once twenty thousand going twice so that renegade.',
       'title': 'Learn How to Invest in Tax Liens and Deeds (Advanta IRA)',
       'url': 'https://www.youtube.com/watch?v=c3YDDPR5wVo&t=885s',
       'video_id': 'c3YDDPR5wVo'},
      {'author': 'Dustin Hahn',
       'channel': 'Dustin Hahn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=cI-GhiUY6pg&t=20s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "The big benefit is you can buy these properties, they're mortgage-free because "
               'when you buy at a tax deed sale, it is the priority lien and it wipes out the '
               'mortgage, which is awesome. So, what are the cons of tax deed investing?',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "The big benefit is you can buy these properties, they're mortgage-free because "
              'when you buy at a tax deed sale, it is the priority lien and it wipes out the '
              'mortgage, which is awesome. So, what are the cons of tax deed investing?',
       'title': 'Tax Deeds vs. Tax Liens: Breaking Down the Pros and Cons (Dustin Hahn)',
       'url': 'https://www.youtube.com/watch?v=cI-GhiUY6pg&t=20s',
       'video_id': 'cI-GhiUY6pg'},
      {'author': 'Tax Sale Lists',
       'channel': 'Tax Sale Lists',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=ymnkPFHPY40&t=37s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Over the counter liens, also known as OTC liens sound, when you listen to some '
               'gurus, to be the way to go. All you do is send a check to the county and they '
               'sell you a lien. These are liens that did not sell at the tax sale.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': 'Over the counter liens, also known as OTC liens sound, when you listen to some '
              'gurus, to be the way to go. All you do is send a check to the county and they '
              'sell you a lien. These are liens that did not sell at the tax sale.',
       'title': 'Tax Lien Investing - Over The Counter (OTC) Tax Liens (Tax Sale Lists)',
       'url': 'https://www.youtube.com/watch?v=ymnkPFHPY40&t=37s',
       'video_id': 'ymnkPFHPY40'}],
 12: [{'author': 'Read The Corner',
       'channel': 'Read The Corner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:17](https://www.youtube.com/watch?v=FEsG-qPFvMc&t=617s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Skill one: read the corner. Then count the 30 days from the right day. And '
               'mail the request well before the last one. Check your own letter and the '
               "official IRS site yourself. Your letter's dates beat any video's examples. A "
               'margin note from the desk.',
       'timestamp': 617,
       'timestamp_label': '[00:10:17]',
       'timestamp_seconds': 617,
       'tip': 'Skill one: read the corner. Then count the 30 days from the right day. And mail '
              'the request well before the last one. Check your own letter and the official '
              "IRS site yourself. Your letter's dates beat any video's examples. A margin note "
              'from the desk.',
       'title': 'IRS Notice of Federal Tax Lien? DO NOT Skip the 30-Day Hearing (Read The '
                'Corner)',
       'url': 'https://www.youtube.com/watch?v=FEsG-qPFvMc&t=617s',
       'video_id': 'FEsG-qPFvMc'},
      {'author': 'Saen Higgins',
       'channel': 'Saen Higgins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:31](https://www.youtube.com/watch?v=HjwUaTY_CAk&t=451s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '90 days, or 120 days or one payment a year, whatever the case, it might be, '
               "but most of them are going to be by four o'clock that day. So you need to find "
               'out how, when and then the most important factor is where where is the auction '
               'being held?',
       'timestamp': 451,
       'timestamp_label': '[00:07:31]',
       'timestamp_seconds': 451,
       'tip': '90 days, or 120 days or one payment a year, whatever the case, it might be, but '
              "most of them are going to be by four o'clock that day. So you need to find out "
              'how, when and then the most important factor is where where is the auction '
              'being held?',
       'title': 'How To Buy Tax Liens Over-The-Counter (Saen Higgins)',
       'url': 'https://www.youtube.com/watch?v=HjwUaTY_CAk&t=451s',
       'video_id': 'HjwUaTY_CAk'},
      {'author': 'HOA Insights',
       'channel': 'HOA Insights',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:22](https://www.youtube.com/watch?v=YD_WDRyFt4Q&t=382s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Every week we break down another HOA rule, fee, or right in plain English '
               'before it costs you money. And tell us in the comments, has your HOA ever sent '
               'you a letter you did not understand? This video is general information only.',
       'timestamp': 382,
       'timestamp_label': '[00:06:22]',
       'timestamp_seconds': 382,
       'tip': 'Every week we break down another HOA rule, fee, or right in plain English '
              'before it costs you money. And tell us in the comments, has your HOA ever sent '
              'you a letter you did not understand? This video is general information only.',
       'title': 'HOA Liens Explained – Can They Take Your House? (HOA Insights)',
       'url': 'https://www.youtube.com/watch?v=YD_WDRyFt4Q&t=382s',
       'video_id': 'YD_WDRyFt4Q'},
      {'author': 'The Quiet Math',
       'channel': 'The Quiet Math',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:01](https://www.youtube.com/watch?v=0FOLJutyMHY&t=661s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So here's one thing worth doing this week. If your parents or anyone you love "
               'paid off their mortgage, ask them a single question. Who pays the property tax '
               "now? Then sit down together and find their county treasurer's website.",
       'timestamp': 661,
       'timestamp_label': '[00:11:01]',
       'timestamp_seconds': 661,
       'tip': "So here's one thing worth doing this week. If your parents or anyone you love "
              'paid off their mortgage, ask them a single question. Who pays the property tax '
              "now? Then sit down together and find their county treasurer's website.",
       'title': 'Why Retirees Are Losing Paid-Off Homes Over $3,000 Tax Bills (The Quiet Math)',
       'url': 'https://www.youtube.com/watch?v=0FOLJutyMHY&t=661s',
       'video_id': '0FOLJutyMHY'},
      {'author': 'Tax Lien School Highlights - Dustin Hahn',
       'channel': 'Tax Lien School Highlights - Dustin Hahn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:22](https://www.youtube.com/watch?v=Ayjol9fgpNg&t=82s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, different words, different places. From here, we can scroll down and we've "
               'got over the counter liens. So, remember, the redemption period, you can start '
               'foreclosing on these six months after the sale.',
       'timestamp': 82,
       'timestamp_label': '[00:01:22]',
       'timestamp_seconds': 82,
       'tip': "So, different words, different places. From here, we can scroll down and we've "
              'got over the counter liens. So, remember, the redemption period, you can start '
              'foreclosing on these six months after the sale.',
       'title': 'Maryland OTC Tax Liens - 6 Months To Foreclose, 2 Years Before They Expire '
                '(Tax Lien School Highlights - Dustin Hahn)',
       'url': 'https://www.youtube.com/watch?v=Ayjol9fgpNg&t=82s',
       'video_id': 'Ayjol9fgpNg'},
      {'author': 'Dustin Hahn',
       'channel': 'Dustin Hahn',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=eJhR4GkZ7Qo&t=36s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'County that has over the counter tax liens I actually bought one month and a '
               "half ago how's it redeemed yet I did buy one and you can click here and it's.",
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': 'County that has over the counter tax liens I actually bought one month and a '
              "half ago how's it redeemed yet I did buy one and you can click here and it's.",
       'title': 'Tax Lien & Deed Property Research - Using GIS/Parcel Viewers (Dustin Hahn)',
       'url': 'https://www.youtube.com/watch?v=eJhR4GkZ7Qo&t=36s',
       'video_id': 'eJhR4GkZ7Qo'},
      {'author': 'Tax Sale Resources',
       'channel': 'Tax Sale Resources',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=3thEKo1DOwU&t=66s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Day the goal is to help you become a better investor increase your portfolio '
               'and make more money brian thank you for joining us as always help us out here '
               'the question that the audience wants to know is what is bit down ownership '
               'interest.',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': 'Day the goal is to help you become a better investor increase your portfolio '
              'and make more money brian thank you for joining us as always help us out here '
              'the question that the audience wants to know is what is bit down ownership '
              'interest.',
       'title': 'What is the Bid Down Ownership Bidding Process? (Tax Sale Resources)',
       'url': 'https://www.youtube.com/watch?v=3thEKo1DOwU&t=66s',
       'video_id': '3thEKo1DOwU'},
      {'author': 'Stop IRS Problems | Tax Law Offices',
       'channel': 'Stop IRS Problems | Tax Law Offices',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:07](https://www.youtube.com/watch?v=MLaWCy3MlMQ&t=187s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And there's some technical rules behind that. We'll get into that in another "
               "video. It could even affect someone's ability to discharge their taxes in "
               "bankruptcy if there's a lien tied to real estate that they plan to retain "
               'after bankruptcy.',
       'timestamp': 187,
       'timestamp_label': '[00:03:07]',
       'timestamp_seconds': 187,
       'tip': "And there's some technical rules behind that. We'll get into that in another "
              "video. It could even affect someone's ability to discharge their taxes in "
              "bankruptcy if there's a lien tied to real estate that they plan to retain after "
              'bankruptcy.',
       'title': 'How to Get IRS to Withdraw or Remove a Federal Tax Lien - Tips for Filling '
                'Out IRS Form 12277 (Stop IRS Problems | Tax Law Offices)',
       'url': 'https://www.youtube.com/watch?v=MLaWCy3MlMQ&t=187s',
       'video_id': 'MLaWCy3MlMQ'},
      {'author': 'LCO Law LLC | Estate Planning & Real Estate Law',
       'channel': 'LCO Law LLC | Estate Planning & Real Estate Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:49](https://www.youtube.com/watch?v=GoBskUnMJ5k&t=229s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What they are willing to reimburse you on um if you do tender payment in '
               'advance and satisfaction of other liens or make any repairs to the properties '
               'during the 120 day period good luck out there investors.',
       'timestamp': 229,
       'timestamp_label': '[00:03:49]',
       'timestamp_seconds': 229,
       'tip': 'What they are willing to reimburse you on um if you do tender payment in '
              'advance and satisfaction of other liens or make any repairs to the properties '
              'during the 120 day period good luck out there investors.',
       'title': 'IRS Redemption at Foreclosure - What will they refund me on? (LCO Law LLC | '
                'Estate Planning & Real Estate Law)',
       'url': 'https://www.youtube.com/watch?v=GoBskUnMJ5k&t=229s',
       'video_id': 'GoBskUnMJ5k'},
      {'author': 'The Jackie Jackson | Tax Deed & Real Estate Coach',
       'channel': 'The Jackie Jackson | Tax Deed & Real Estate Coach',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:50](https://www.youtube.com/watch?v=XaihRHU__R4&t=1190s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Is great but other people telling you that I'm great is greater anyway thank "
               "you again for this tax day Tuesday and it's been awesome it's been real I'll "
               'talk to you guys soon see you next week ciao.',
       'timestamp': 1190,
       'timestamp_label': '[00:19:50]',
       'timestamp_seconds': 1190,
       'tip': "Is great but other people telling you that I'm great is greater anyway thank "
              "you again for this tax day Tuesday and it's been awesome it's been real I'll "
              'talk to you guys soon see you next week ciao.',
       'title': '6 Ways to Invest in Tax Deeds and Tax Liens (Florida Examples) (The Jackie '
                'Jackson | Tax Deed & Real Estate Coach)',
       'url': 'https://www.youtube.com/watch?v=XaihRHU__R4&t=1190s',
       'video_id': 'XaihRHU__R4'},
      {'author': 'Tax Sale Academy',
       'channel': 'Tax Sale Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:34](https://www.youtube.com/watch?v=JIdC6p9dM-k&t=154s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Academy.com so head on over check out those videos browsers there's a wealth "
               'of information on the website and again the address is tax I like Adam e.com I '
               "really hope you've enjoyed this video folks have a great day take care bye "
               'bye.',
       'timestamp': 154,
       'timestamp_label': '[00:02:34]',
       'timestamp_seconds': 154,
       'tip': "Academy.com so head on over check out those videos browsers there's a wealth of "
              'information on the website and again the address is tax I like Adam e.com I '
              "really hope you've enjoyed this video folks have a great day take care bye bye.",
       'title': 'Tax Liens vs Tax Deeds (Tax Sale Academy)',
       'url': 'https://www.youtube.com/watch?v=JIdC6p9dM-k&t=154s',
       'video_id': 'JIdC6p9dM-k'},
      {'author': 'Ted Thomas',
       'channel': 'Ted Thomas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=EBswPIFAXTY&t=94s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Could push them down from 16% in Arizona all the way down to 0.5% same in '
               "Florida the lowest bidder will be the winner of that auction it's important "
               'to.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': 'Could push them down from 16% in Arizona all the way down to 0.5% same in '
              "Florida the lowest bidder will be the winner of that auction it's important to.",
       'title': 'What is a Tax Lien Foreclosure Explained Simply (Ted Thomas)',
       'url': 'https://www.youtube.com/watch?v=EBswPIFAXTY&t=94s',
       'video_id': 'EBswPIFAXTY'},
      {'author': 'Tax Lien Bestie | Sabrina',
       'channel': 'Tax Lien Bestie | Sabrina',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=VH9CbLJ5Erk&t=87s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Tax Lane investing you either gain the property or you make more money than '
               'you started with if you want to know the interest rate in your estate drop it '
               'below in the comment section and I will be happy to help you good luck and '
               'happy investing.',
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': 'Tax Lane investing you either gain the property or you make more money than you '
              'started with if you want to know the interest rate in your estate drop it below '
              'in the comment section and I will be happy to help you good luck and happy '
              'investing.',
       'title': 'Tax Lien Investing For Beginners ‼️ (Tax Lien Bestie | Sabrina)',
       'url': 'https://www.youtube.com/watch?v=VH9CbLJ5Erk&t=87s',
       'video_id': 'VH9CbLJ5Erk'},
      {'author': 'Tax Sale Academy',
       'channel': 'Tax Sale Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:58](https://www.youtube.com/watch?v=oKQjnGAQlGs&t=718s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That we offer through the tax sell academy.com we would love to have you join '
               "our community take care and we'll see you next time right here on the tax cell "
               'podcast make it a successful day bye-bye.',
       'timestamp': 718,
       'timestamp_label': '[00:11:58]',
       'timestamp_seconds': 718,
       'tip': 'That we offer through the tax sell academy.com we would love to have you join '
              "our community take care and we'll see you next time right here on the tax cell "
              'podcast make it a successful day bye-bye.',
       'title': 'Tax Liens vs. Tax Deeds: Which Is the Better Investment for You? (Tax Sale '
                'Academy)',
       'url': 'https://www.youtube.com/watch?v=oKQjnGAQlGs&t=718s',
       'video_id': 'oKQjnGAQlGs'},
      {'author': 'Lien Ledger',
       'channel': 'Lien Ledger',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:55](https://www.youtube.com/watch?v=H9fPhqUYPfc&t=475s)',
       'relevance': 'Attributed practitioner commentary on statutory tax-lien certificate & '
                    'redeemable-deed investing, auction bid-down math, and post-*Tyler* '
                    'foreclosure rules (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Many counties now run their auctions online, so you can research and bid from '
               'home. But that also means more competition. Start small in one county and '
               "learn how it's auction works. And never bid on a lien you wouldn't be "
               'comfortable owning.',
       'timestamp': 475,
       'timestamp_label': '[00:07:55]',
       'timestamp_seconds': 475,
       'tip': 'Many counties now run their auctions online, so you can research and bid from '
              'home. But that also means more competition. Start small in one county and learn '
              "how it's auction works. And never bid on a lien you wouldn't be comfortable "
              'owning.',
       'title': 'How Tax Lien Investing Actually Works (Lien Ledger)',
       'url': 'https://www.youtube.com/watch?v=H9fPhqUYPfc&t=475s',
       'video_id': 'H9fPhqUYPfc'}]}
