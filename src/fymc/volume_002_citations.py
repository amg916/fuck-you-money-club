"""Curated 180-citation surplus-native baseline (15 per chapter across Q1-Q12) mined from the 261-video FYMC corpus (189 core + 72 dedicated surplus-recovery transcripts)."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'auction',
     'constitutional',
     'deed',
     'equity',
     'excess',
     'fifth',
     'foreclosure',
     'hennepin',
     'lane',
     'lanes',
     'mortgage',
     'overage',
     'overages',
     'proceeds',
     'surplus',
     'takings',
     'tax',
     'trustee',
     'tyler'},
 2: {'balance',
     'check',
     'claimant',
     'clerk',
     'comptroller',
     'county',
     'court',
     'custodian',
     'disbursement',
     'entitled',
     'escrow',
     'funds',
     'holder',
     'ledger',
     'owner',
     'registry',
     'stale',
     'treasurer',
     'trustee',
     'warrant'},
 3: {'assignment',
     'attorney',
     'cap',
     'caps',
     'commission',
     'contingency',
     'economics',
     'fee',
     'fees',
     'margin',
     'percentage',
     'profit',
     'revenue',
     'split',
     'spread',
     'statute'},
 4: {'attorney',
     'bank',
     'bond',
     'budget',
     'business',
     'capital',
     'company',
     'cost',
     'costs',
     'counsel',
     'entity',
     'expense',
     'expenses',
     'filing',
     'firm',
     'insurance',
     'lawyer',
     'lean',
     'llc',
     'notary',
     'overhead',
     'partner',
     'pilot',
     'reserve',
     'retainer',
     'setup',
     'startup'},
 5: {'bankruptcy',
     'deceased',
     'encumbrance',
     'heirs',
     'hoa',
     'irs',
     'judgment',
     'junior',
     'lien',
     'liens',
     'mortgage',
     'priority',
     'probate',
     'redemption',
     'senior',
     'surviving',
     'trap',
     'upset',
     'wipeout'},
 6: {'auction',
     'calendar',
     'clerk',
     'county',
     'docket',
     'filter',
     'foia',
     'lead',
     'leads',
     'list',
     'lists',
     'public',
     'qualify',
     'records',
     'request',
     'sourcing',
     'sunshine',
     'threshold'},
 7: {'affidavit',
     'attorney',
     'chain',
     'claim',
     'counsel',
     'deed',
     'documents',
     'dossier',
     'encumbrance',
     'exhibit',
     'filing',
     'heir',
     'heirs',
     'motion',
     'order',
     'packet',
     'probate',
     'proof',
     'title',
     'vesting'},
 8: {'assessor',
     'database',
     'datatree',
     'gis',
     'locate',
     'obituary',
     'pacer',
     'parcel',
     'phone',
     'portal',
     'recorder',
     'regrid',
     'relatives',
     'search',
     'skip',
     'stack',
     'tlo',
     'trace',
     'tracing'},
 9: {'agreement',
     'attorney',
     'call',
     'calling',
     'cold',
     'compliance',
     'contract',
     'disclosure',
     'letter',
     'mail',
     'objection',
     'outreach',
     'phone',
     'power',
     'rebuttal',
     'scam',
     'script',
     'solicitation',
     'statute',
     'trust',
     'waiting'},
 10: {'alerts',
      'automation',
      'batch',
      'case',
      'crm',
      'data',
      'dataset',
      'import',
      'ocr',
      'pdf',
      'pipeline',
      'process',
      'scraper',
      'scraping',
      'sheet',
      'software',
      'spreadsheet',
      'study',
      'system',
      'tracking',
      'workflow'},
 11: {'acquisition',
      'caller',
      'closing',
      'counsel',
      'delegate',
      'desk',
      'hire',
      'hiring',
      'kpi',
      'manager',
      'operations',
      'researcher',
      'role',
      'scale',
      'scaling',
      'sop',
      'team',
      'training',
      'va'},
 12: {'action',
      'audit',
      'checklist',
      'client',
      'close',
      'consistency',
      'day',
      'days',
      'deal',
      'discipline',
      'execution',
      'first',
      'focus',
      'goal',
      'launch',
      'mindset',
      'month',
      'ninety',
      'plan',
      'roadmap',
      'start',
      'steps',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'BizMove',
      'channel': 'BizMove',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=01plOr9pFjQ&t=22s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'Starting a tax overage business can be a lucrative venture if done correctly. '
              'Tax overages, also called tax lien surplus or excess proceeds, arise when a '
              'property is sold at a tax sale for more than the amount owed in taxes and fees.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Starting a tax overage business can be a lucrative venture if done correctly. '
             'Tax overages, also called tax lien surplus or excess proceeds, arise when a '
             'property is sold at a tax sale for more than the amount owed in taxes and fees.',
      'title': 'How to Start a Tax Overage Business | Complete and Easy to Follow Guide '
               '(BizMove)',
      'url': 'https://www.youtube.com/watch?v=01plOr9pFjQ&t=22s',
      'video_id': '01plOr9pFjQ'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=v0-thxE7IK4&t=88s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'When a house goes through foreclosure and sells for more at the auction than '
              'was owed on the debt, the extra money, called surplus funds or excess proceeds, '
              'does not belong to the bank and does not belong to the county or the state.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'When a house goes through foreclosure and sells for more at the auction than was '
             'owed on the debt, the extra money, called surplus funds or excess proceeds, does '
             'not belong to the bank and does not belong to the county or the state.',
      'title': 'How To Find Surplus Funds Lists In 2026 (For Free) (Surplus Funds Secrets)',
      'url': 'https://www.youtube.com/watch?v=v0-thxE7IK4&t=88s',
      'video_id': 'v0-thxE7IK4'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=6UiKunbtUa0&t=58s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'California, the overage is called excess proceeds, you know, and on the east '
              "coast, it may be called surplus funds. So, there's different I've included in "
              "this training, there's different words and names for overages, but if you use, "
              "you know, different words, it's okay.",
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'California, the overage is called excess proceeds, you know, and on the east '
             "coast, it may be called surplus funds. So, there's different I've included in "
             "this training, there's different words and names for overages, but if you use, "
             "you know, different words, it's okay.",
      'title': 'How To Find Excess Proceeds List In 2025 (Proven Strategies) (Overage '
               'Acquisition)',
      'url': 'https://www.youtube.com/watch?v=6UiKunbtUa0&t=58s',
      'video_id': '6UiKunbtUa0'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=131s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'A tax sale overage is not the same as a mortgage foreclosure surplus. One '
              'county lets you email everything. The next one, they actually want originals. '
              'They want the papers actually mailed in. And if you send a copy, it simply gets '
              'rejected.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'A tax sale overage is not the same as a mortgage foreclosure surplus. One county '
             'lets you email everything. The next one, they actually want originals. They want '
             'the papers actually mailed in. And if you send a copy, it simply gets rejected.',
      'title': 'Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=131s',
      'video_id': 'MVCNlj7HQBQ'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:45](https://www.youtube.com/watch?v=CqlbwGPmv64&t=405s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'And it works the same way whether it was a mortgage foreclosure or a tax sale. '
              'The numbers just come from different places. Know your numbers and the rules '
              'before you dial. Open with the auction results, then pause. Walk through the '
              'math and use words like possible.',
      'timestamp': 405,
      'timestamp_label': '[00:06:45]',
      'timestamp_seconds': 405,
      'tip': 'And it works the same way whether it was a mortgage foreclosure or a tax sale. '
             'The numbers just come from different places. Know your numbers and the rules '
             'before you dial. Open with the auction results, then pause. Walk through the '
             'math and use words like possible.',
      'title': 'Surplus Funds Cold Calling Script: How to Not Sound Like a Scam (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=CqlbwGPmv64&t=405s',
      'video_id': 'CqlbwGPmv64'},
     {'author': 'Consumer Action Law Group',
      'channel': 'Consumer Action Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=gUeG4eQdMy8&t=163s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'Done correctly if you call my firm we help by figuring out if there is a '
              'surplus we research the title we look for sale proceeds we look for the trustee '
              'and we can give you a time frame as to whether the funds have been deposited '
              'with the court.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Done correctly if you call my firm we help by figuring out if there is a surplus '
             'we research the title we look for sale proceeds we look for the trustee and we '
             'can give you a time frame as to whether the funds have been deposited with the '
             'court.',
      'title': 'How to Claim Surplus Funds from Foreclosure (Step by Step Tutorial) (Consumer '
               'Action Law Group)',
      'url': 'https://www.youtube.com/watch?v=gUeG4eQdMy8&t=163s',
      'video_id': 'gUeG4eQdMy8'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:25](https://www.youtube.com/watch?v=d5TLZqkPX14&t=565s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': "All right, so now you know there's going to be an auction. So you could go to "
              "the auction, so let's just go to the auction and have an example, okay? So, a "
              "tax overage is what we're covering today, okay? You want to know how to claim "
              'the money.',
      'timestamp': 565,
      'timestamp_label': '[00:09:25]',
      'timestamp_seconds': 565,
      'tip': "All right, so now you know there's going to be an auction. So you could go to "
             "the auction, so let's just go to the auction and have an example, okay? So, a "
             "tax overage is what we're covering today, okay? You want to know how to claim "
             'the money.',
      'title': 'How To Claim Tax Sale Overages (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=d5TLZqkPX14&t=565s',
      'video_id': 'd5TLZqkPX14'},
     {'author': 'Tax Sale Academy',
      'channel': 'Tax Sale Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=snu6i8Dp6h8&t=168s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': "Tight budget that's it for today folks for more information on tax on investing "
              'or from profiting from these excess proceeds visit tax all academy.com again '
              "that's tax all academy.com have wonderful day folks take care okay.",
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': "Tight budget that's it for today folks for more information on tax on investing "
             'or from profiting from these excess proceeds visit tax all academy.com again '
             "that's tax all academy.com have wonderful day folks take care okay.",
      'title': 'Tax Sale Excess Proceeds (Tax Sale Academy)',
      'url': 'https://www.youtube.com/watch?v=snu6i8Dp6h8&t=168s',
      'video_id': 'snu6i8Dp6h8'},
     {'author': 'Tax Deed Surplus & Lien-Research Records',
      'channel': 'Tax Deed Surplus & Lien-Research Records',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=y94Ncg0WHn0&t=51s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': "So now that we have the tax deed date, we're going to put in May 18th. This "
              'shows you all of the tax deed auctions from that date and everything going '
              "forward. We're only looking for the ones that sold uh or went up for auction on "
              'May 18th.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "So now that we have the tax deed date, we're going to put in May 18th. This "
             'shows you all of the tax deed auctions from that date and everything going '
             "forward. We're only looking for the ones that sold uh or went up for auction on "
             'May 18th.',
      'title': 'Polk County Tax Deed Surplus (Tax Deed Surplus & Lien-Research Records)',
      'url': 'https://www.youtube.com/watch?v=y94Ncg0WHn0&t=51s',
      'video_id': 'y94Ncg0WHn0'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=T2gvkByDlFU&t=176s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': "So, I've gotten so involved in this piece of the business, I created a new "
              'podcast called the reverse mortgage podcast cuz so many of them were reverse '
              'mortgages were going into foreclosure. And they had some equity, maybe not a '
              'lot.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': "So, I've gotten so involved in this piece of the business, I created a new "
             'podcast called the reverse mortgage podcast cuz so many of them were reverse '
             'mortgages were going into foreclosure. And they had some equity, maybe not a '
             'lot.',
      'title': '🚨 Probate Property Headed to Foreclosure Auction… Is It Worth Pursuing? '
               '(Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=T2gvkByDlFU&t=176s',
      'video_id': 'T2gvkByDlFU'},
     {'author': 'Attorney Jack',
      'channel': 'Attorney Jack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:29](https://www.youtube.com/watch?v=KKKIgl--DNo&t=149s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'Remember, there are many times that people paid their mortgage or their tax '
              'liens for years, and then at the last minute due to some unfortunate situation '
              'or a death, uh the these the mortgage or the taxes were not paid. But, the '
              'equity is still there in the property.',
      'timestamp': 149,
      'timestamp_label': '[00:02:29]',
      'timestamp_seconds': 149,
      'tip': 'Remember, there are many times that people paid their mortgage or their tax '
             'liens for years, and then at the last minute due to some unfortunate situation '
             'or a death, uh the these the mortgage or the taxes were not paid. But, the '
             'equity is still there in the property.',
      'title': 'Foreclosure - Surplus Funds Recovery - Attorney Assistance (Attorney Jack)',
      'url': 'https://www.youtube.com/watch?v=KKKIgl--DNo&t=149s',
      'video_id': 'KKKIgl--DNo'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=0pjP-Sr15PA&t=52s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'Opening bid for a mortgage foreclosure sometimes can be 2/3 of the appraisal '
              'amount or 2/3 of the final judgment amount. Sometimes, it could also just be a '
              'dollar amount that a trustee or a non-judicial sale feels as deemable for the '
              'foreclosure, for the actual auction.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': 'Opening bid for a mortgage foreclosure sometimes can be 2/3 of the appraisal '
             'amount or 2/3 of the final judgment amount. Sometimes, it could also just be a '
             'dollar amount that a trustee or a non-judicial sale feels as deemable for the '
             'foreclosure, for the actual auction.',
      'title': 'Are You Doing Mortgage Foreclosure Surplus Funds Recovery? (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=0pjP-Sr15PA&t=52s',
      'video_id': '0pjP-Sr15PA'},
     {'author': 'Nick Fullmer- Overage Syndicate',
      'channel': 'Nick Fullmer- Overage Syndicate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=KOYBZFn2k7w&t=90s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': "In certain states, you're gonna wanna know who was on the mortgage as well, "
              'because in some states, Minnesota for example, the law actually says that the '
              'surplus belongs to the mortgager, not necessarily the person on the deed.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': "In certain states, you're gonna wanna know who was on the mortgage as well, "
             'because in some states, Minnesota for example, the law actually says that the '
             'surplus belongs to the mortgager, not necessarily the person on the deed.',
      'title': 'Overages & Surplus Fund Debt & Title Research: Not As Easy As It Seems.  Two '
               'tips To Help (Nick Fullmer- Overage Syndicate)',
      'url': 'https://www.youtube.com/watch?v=KOYBZFn2k7w&t=90s',
      'video_id': 'KOYBZFn2k7w'},
     {'author': 'William Whitman, Esquire',
      'channel': 'William Whitman, Esquire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=0xk7lNvAgn0&t=163s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': 'If I wanted to get further information on a company that was owed surplus funds '
              'or excess proceeds searching at the state Secretary of State or Department of '
              'Corporations or Revenue site for additional publicly available information.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'If I wanted to get further information on a company that was owed surplus funds '
             'or excess proceeds searching at the state Secretary of State or Department of '
             'Corporations or Revenue site for additional publicly available information.',
      'title': 'Will Whitman, Esquire explains how to locate companies owed surplus funds '
               '(William Whitman, Esquire)',
      'url': 'https://www.youtube.com/watch?v=0xk7lNvAgn0&t=163s',
      'video_id': '0xk7lNvAgn0'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=i7mng3-o1u0&t=123s)',
      'relevance': 'Attributed practitioner commentary on tax-sale overages, mortgage '
                   'foreclosure excess proceeds, and post-Tyler statutory lanes; verify '
                   'against governing state statute.',
      'source_type': 'video_pro_tip',
      'text': "So, there's good language and there's bad language. Bad language, I'm calling "
              "about a foreclosure. A better version would be, I'm calling regarding money "
              'that be money that might be owed to your estate tied from a foreclosure tax '
              'sale auction.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "So, there's good language and there's bad language. Bad language, I'm calling "
             "about a foreclosure. A better version would be, I'm calling regarding money that "
             'be money that might be owed to your estate tied from a foreclosure tax sale '
             'auction.',
      'title': 'Avoid These Mistakes In Surplus Funds Cold Calling (Surplus Funds Secrets)',
      'url': 'https://www.youtube.com/watch?v=i7mng3-o1u0&t=123s',
      'video_id': 'i7mng3-o1u0'}],
 2: [{'author': 'Dreams & Dollars: The Everyday Entrepreneur',
      'channel': 'Dreams & Dollars: The Everyday Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=pSC1FfAjNuo&t=212s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'Step six, file with the correct office court registry, trustee, or county '
              'finance. Step seven, some areas require a brief hearing show up with originals '
              'and a clear timeline. Step eight, receive funds via check or a once approved.',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': 'Step six, file with the correct office court registry, trustee, or county '
             'finance. Step seven, some areas require a brief hearing show up with originals '
             'and a clear timeline. Step eight, receive funds via check or a once approved.',
      'title': 'Beginners Guide to Surplus Funds: How to Claim Money After Foreclosure- '
               'Step-by-Step Tutorial (Dreams & Dollars: The Everyday Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=pSC1FfAjNuo&t=212s',
      'video_id': 'pSC1FfAjNuo'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=8-8koApqnYA&t=74s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': "Here's the whole business model in one breath. The owner loses a property at "
              'foreclosure auction or tax sale. The property sells for more than what was '
              'owed. The county, the court, or the trustee holds the difference. The former '
              'owner is legally entitled to that money.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "Here's the whole business model in one breath. The owner loses a property at "
             'foreclosure auction or tax sale. The property sells for more than what was owed. '
             'The county, the court, or the trustee holds the difference. The former owner is '
             'legally entitled to that money.',
      'title': 'How to Start a Surplus Funds Business in 2026 (Step by Step) (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=8-8koApqnYA&t=74s',
      'video_id': '8-8koApqnYA'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=v0-thxE7IK4&t=163s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'Mortgage foreclosures typically sit with the court. The clerk of courts runs '
              'the foreclosure sales, and the extra funds typically land in the court '
              'registry. Many clerks publish exactly what funds are left over. Type the county '
              'name and surplus funds or excess proceeds.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Mortgage foreclosures typically sit with the court. The clerk of courts runs the '
             'foreclosure sales, and the extra funds typically land in the court registry. '
             'Many clerks publish exactly what funds are left over. Type the county name and '
             'surplus funds or excess proceeds.',
      'title': 'How To Find Surplus Funds Lists In 2026 (For Free) (Surplus Funds Secrets)',
      'url': 'https://www.youtube.com/watch?v=v0-thxE7IK4&t=163s',
      'video_id': 'v0-thxE7IK4'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=q2gk3WmK5xs&t=284s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': "'re entitled to surplus funds and provide concrete proof. This includes sales "
              'results from foreclosure auctions, county maintained lists of surplus funds, or '
              "court documents confirming their entitlement. Don't just tell them they have "
              'money.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': "'re entitled to surplus funds and provide concrete proof. This includes sales "
             'results from foreclosure auctions, county maintained lists of surplus funds, or '
             "court documents confirming their entitlement. Don't just tell them they have "
             'money.',
      'title': 'The Most Overlooked Surplus Funds Recovery Business You Can Start With $0 '
               '(Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=q2gk3WmK5xs&t=284s',
      'video_id': 'q2gk3WmK5xs'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=0pjP-Sr15PA&t=155s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': '" You want to see proof of that payment. You want to see disbursement history '
              "because they have a superior lien or they're first entitled, doesn't mean that "
              'the trustee did indeed hand over those surplus funds.',
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': '" You want to see proof of that payment. You want to see disbursement history '
             "because they have a superior lien or they're first entitled, doesn't mean that "
             'the trustee did indeed hand over those surplus funds.',
      'title': 'Are You Doing Mortgage Foreclosure Surplus Funds Recovery? (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=0pjP-Sr15PA&t=155s',
      'video_id': '0pjP-Sr15PA'},
     {'author': 'Surplus_Prosperity',
      'channel': 'Surplus_Prosperity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=MYo3k2Sxj1Q&t=62s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'And the law in most states is very clear about who that money belongs to. It '
              'belongs to the former owner. In this case, is likely you or a relative of '
              'yours. The county or the court is holding it right now.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'And the law in most states is very clear about who that money belongs to. It '
             'belongs to the former owner. In this case, is likely you or a relative of yours. '
             'The county or the court is holding it right now.',
      'title': 'What Are Surplus Funds? How to Claim Money Owed to You After Foreclosure or '
               'Tax Sale (Surplus_Prosperity)',
      'url': 'https://www.youtube.com/watch?v=MYo3k2Sxj1Q&t=62s',
      'video_id': 'MYo3k2Sxj1Q'},
     {'author': 'Consumer Action Law Group',
      'channel': 'Consumer Action Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=gUeG4eQdMy8&t=166s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'Help by figuring out if there is a surplus we research the title we look for '
              'sale proceeds we look for the trustee and we can give you a time frame as to '
              'whether the funds have been deposited with the court.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'Help by figuring out if there is a surplus we research the title we look for '
             'sale proceeds we look for the trustee and we can give you a time frame as to '
             'whether the funds have been deposited with the court.',
      'title': 'How to Claim Surplus Funds from Foreclosure (Step by Step Tutorial) (Consumer '
               'Action Law Group)',
      'url': 'https://www.youtube.com/watch?v=gUeG4eQdMy8&t=166s',
      'video_id': 'gUeG4eQdMy8'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:03](https://www.youtube.com/watch?v=LdemHPCk0dk&t=423s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'So check the foreclosure file, the county records, and a free property data '
              'site like Propwire. Then ask the office and ask the owner of the house. And '
              'treat it all as an estimate. Always say possible funds or estimated surplus. '
              'Never promise them a number.',
      'timestamp': 423,
      'timestamp_label': '[00:07:03]',
      'timestamp_seconds': 423,
      'tip': 'So check the foreclosure file, the county records, and a free property data site '
             'like Propwire. Then ask the office and ask the owner of the house. And treat it '
             'all as an estimate. Always say possible funds or estimated surplus. Never '
             'promise them a number.',
      'title': 'How to Check for Liens Before You Call About Surplus Funds (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=LdemHPCk0dk&t=423s',
      'video_id': 'LdemHPCk0dk'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=lzU09FRqmhg&t=91s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'So the money gets deposited with the clerk of court, and generally, you can get '
              "lists of monies on deposit. It's called the registry of court, just by "
              "requesting it from the clerk of court, and you're going to see all kinds of "
              'monies on deposit.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'So the money gets deposited with the clerk of court, and generally, you can get '
             "lists of monies on deposit. It's called the registry of court, just by "
             "requesting it from the clerk of court, and you're going to see all kinds of "
             'monies on deposit.',
      'title': "How To Claim Surplus Funds From Foreclosure (Bob Diamond - America's Tax Sale "
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=lzU09FRqmhg&t=91s',
      'video_id': 'lzU09FRqmhg'},
     {'author': 'Haynes Law Group',
      'channel': 'Haynes Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=Uj-vrJWHKQo&t=25s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'Florida statute 4532 subsection 1b to actually um be and so had a hearing last '
              'week in front of um Broward County judge. Uh I represented the former owner of '
              'a property. The surplus amount was about $252 uh,000. So significant the there '
              'was a city lean against the property.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Florida statute 4532 subsection 1b to actually um be and so had a hearing last '
             'week in front of um Broward County judge. Uh I represented the former owner of a '
             'property. The surplus amount was about $252 uh,000. So significant the there was '
             'a city lean against the property.',
      'title': 'Florida Foreclosure Surplus Funds Update: What is a Subordinate Lien Holder? '
               '(Haynes Law Group)',
      'url': 'https://www.youtube.com/watch?v=Uj-vrJWHKQo&t=25s',
      'video_id': 'Uj-vrJWHKQo'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:08](https://www.youtube.com/watch?v=R8B06ovsDXI&t=368s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'Judicial, this means that the county conducts the sale. So, this can be like '
              'the sheriff or the clerk of courts. This means a trustee or a foreclosure '
              'attorney. Well, whoever conducts the sale typically releases the funds.',
      'timestamp': 368,
      'timestamp_label': '[00:06:08]',
      'timestamp_seconds': 368,
      'tip': 'Judicial, this means that the county conducts the sale. So, this can be like the '
             'sheriff or the clerk of courts. This means a trustee or a foreclosure attorney. '
             'Well, whoever conducts the sale typically releases the funds.',
      'title': 'How to start a Surplus Funds Business (45 min raw free game) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=R8B06ovsDXI&t=368s',
      'video_id': 'R8B06ovsDXI'},
     {'author': 'BizMove',
      'channel': 'BizMove',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=01plOr9pFjQ&t=35s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'The original property owner may be entitled to claim those surplus funds, and '
              'your business can help locate, notify, and assist those owners in reclaiming '
              'their money for a fee.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'The original property owner may be entitled to claim those surplus funds, and '
             'your business can help locate, notify, and assist those owners in reclaiming '
             'their money for a fee.',
      'title': 'How to Start a Tax Overage Business | Complete and Easy to Follow Guide '
               '(BizMove)',
      'url': 'https://www.youtube.com/watch?v=01plOr9pFjQ&t=35s',
      'video_id': '01plOr9pFjQ'},
     {'author': 'AFX Research LLC',
      'channel': 'AFX Research LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:26](https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=86s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': 'Most counties have online databases you can search by address or owner name. '
              'Harris County, Travis County, Dallas County — they all have public record '
              'portals where this information lives. Next, check the County Tax '
              "Assessor-Collector's website.",
      'timestamp': 86,
      'timestamp_label': '[00:01:26]',
      'timestamp_seconds': 86,
      'tip': 'Most counties have online databases you can search by address or owner name. '
             'Harris County, Travis County, Dallas County — they all have public record '
             'portals where this information lives. Next, check the County Tax '
             "Assessor-Collector's website.",
      'title': 'HOW TO FIND LIENS & TITLE SEARCH IN TEXAS (AFX Research LLC)',
      'url': 'https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=86s',
      'video_id': 'HPyO3dkjbCQ'},
     {'author': 'ohiocommerce',
      'channel': 'ohiocommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=o1cc3hUtIv4&t=88s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': "So first we're going to go to unclaimed funds. You don't want to forget that. "
              "And please check our site often. So, there are several ways. If you're on our "
              'site, you can go to how you claim funds.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': "So first we're going to go to unclaimed funds. You don't want to forget that. "
             "And please check our site often. So, there are several ways. If you're on our "
             'site, you can go to how you claim funds.',
      'title': 'Watch our Demo on How to Claim Your Ohio Unclaimed Funds (ohiocommerce)',
      'url': 'https://www.youtube.com/watch?v=o1cc3hUtIv4&t=88s',
      'video_id': 'o1cc3hUtIv4'},
     {'author': 'Lenny the Lawyer-Live',
      'channel': 'Lenny the Lawyer-Live',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=dn1b-e6bUyo&t=283s)',
      'relevance': 'Attributed practitioner commentary on county custodians, clerk/treasurer '
                   'ledgers, stale warrants, and balance verification; verify directly with '
                   'custodian records.',
      'source_type': 'video_pro_tip',
      'text': "In the background you might have heard the cat he's not interested in surplus "
              "funds he's just interested in food thank you for your time we value your time "
              'we know your time is not replaceable but money is so bear that in mind.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': "In the background you might have heard the cat he's not interested in surplus "
             "funds he's just interested in food thank you for your time we value your time we "
             'know your time is not replaceable but money is so bear that in mind.',
      'title': 'How Can You Get Surplus Funds After Your House is Sold at Foreclosure In 2023? '
               '(Lenny the Lawyer-Live)',
      'url': 'https://www.youtube.com/watch?v=dn1b-e6bUyo&t=283s',
      'video_id': 'dn1b-e6bUyo'}],
 3: [{'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:57](https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=417s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': "I haven't done this business for a long time. I'm an attorney, so my documents "
              'are very strong, but you need a fee agreement, a power of attorney, an '
              'assignment, letter of direction to the county. You need a bunch of documents '
              'like that, and a few others.',
      'timestamp': 417,
      'timestamp_label': '[00:06:57]',
      'timestamp_seconds': 417,
      'tip': "I haven't done this business for a long time. I'm an attorney, so my documents "
             'are very strong, but you need a fee agreement, a power of attorney, an '
             'assignment, letter of direction to the county. You need a bunch of documents '
             'like that, and a few others.',
      'title': "Tax Sale Overages Course (Bob Diamond - America's Tax Sale Attorney)",
      'url': 'https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=417s',
      'video_id': 'qGPsbhsEAVQ'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:13](https://www.youtube.com/watch?v=DK8BPV7WVvI&t=793s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': "My fee was $52,000 which was 25%. Tip 22, put the attorney fees on the client's "
              'side of the math. Some claims need an attorney and that cost can eat into your '
              "fee if you're not careful. Caesar Santos had his client agree to pay all "
              "attorney fees out of the client's share.",
      'timestamp': 793,
      'timestamp_label': '[00:13:13]',
      'timestamp_seconds': 793,
      'tip': "My fee was $52,000 which was 25%. Tip 22, put the attorney fees on the client's "
             'side of the math. Some claims need an attorney and that cost can eat into your '
             "fee if you're not careful. Caesar Santos had his client agree to pay all "
             "attorney fees out of the client's share.",
      'title': 'Give Me 17 Minutes, I’ll Give You 10,000 Hours of Surplus Funds Knowledge '
               '(Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=DK8BPV7WVvI&t=793s',
      'video_id': 'DK8BPV7WVvI'},
     {'author': 'Attorney Jack',
      'channel': 'Attorney Jack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=KKKIgl--DNo&t=202s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'There is absolutely no upfront money or cost for you. The law firm takes care '
              'of any other attorney fees, clerk fees, or any type of assessments that may '
              'need to be done to be able to access these funds.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': 'There is absolutely no upfront money or cost for you. The law firm takes care of '
             'any other attorney fees, clerk fees, or any type of assessments that may need to '
             'be done to be able to access these funds.',
      'title': 'Foreclosure - Surplus Funds Recovery - Attorney Assistance (Attorney Jack)',
      'url': 'https://www.youtube.com/watch?v=KKKIgl--DNo&t=202s',
      'video_id': 'KKKIgl--DNo'},
     {'author': 'Surplus_Prosperity',
      'channel': 'Surplus_Prosperity',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:45](https://www.youtube.com/watch?v=MYo3k2Sxj1Q&t=165s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'We handle the paperwork in the entire claim process. And we do all of it on a '
              "contingency, meaning we don't charge you a single dollar upfront. If we find "
              "funds and we recover them, we take a percentage. If we don't recover anything, "
              'you owe us nothing.',
      'timestamp': 165,
      'timestamp_label': '[00:02:45]',
      'timestamp_seconds': 165,
      'tip': 'We handle the paperwork in the entire claim process. And we do all of it on a '
             "contingency, meaning we don't charge you a single dollar upfront. If we find "
             "funds and we recover them, we take a percentage. If we don't recover anything, "
             'you owe us nothing.',
      'title': 'What Are Surplus Funds? How to Claim Money Owed to You After Foreclosure or '
               'Tax Sale (Surplus_Prosperity)',
      'url': 'https://www.youtube.com/watch?v=MYo3k2Sxj1Q&t=165s',
      'video_id': 'MYo3k2Sxj1Q'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:44](https://www.youtube.com/watch?v=AAF69oF79DU&t=1244s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'What if you guys split the marketing campaign, you split the cost of the leads '
              'and the marketing, and then you split the revenue off the deals? And you get in '
              "that way, just set a proper expectation that I'm not asking you to be my "
              'business partner.',
      'timestamp': 1244,
      'timestamp_label': '[00:20:44]',
      'timestamp_seconds': 1244,
      'tip': 'What if you guys split the marketing campaign, you split the cost of the leads '
             'and the marketing, and then you split the revenue off the deals? And you get in '
             "that way, just set a proper expectation that I'm not asking you to be my "
             'business partner.',
      'title': 'Sub-to strategy for probate investing | Probate foreclosures | Probate real '
               'estate marketing tips (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=AAF69oF79DU&t=1244s',
      'video_id': 'AAF69oF79DU'},
     {'author': 'Hutch & Holmes',
      'channel': 'Hutch & Holmes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=L2oKpjOoh20&t=134s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'You need to know the laws and if there is anything that need you need to know '
              'when it comes to those uh those types of uh documents. When is an attorney '
              "going to be needed if at all? Okay, so here's your last assignment. Um choose "
              'one state and research the process.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'You need to know the laws and if there is anything that need you need to know '
             'when it comes to those uh those types of uh documents. When is an attorney going '
             "to be needed if at all? Okay, so here's your last assignment. Um choose one "
             'state and research the process.',
      'title': 'How to Recover Foreclosure Surplus Funds (3-Step System) (Hutch & Holmes)',
      'url': 'https://www.youtube.com/watch?v=L2oKpjOoh20&t=134s',
      'video_id': 'L2oKpjOoh20'},
     {'author': 'Dreams & Dollars: The Everyday Entrepreneur',
      'channel': 'Dreams & Dollars: The Everyday Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:51](https://www.youtube.com/watch?v=pSC1FfAjNuo&t=291s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'Check the state business database and any attorney partnerships. Tip three, '
              "understand the fee structure. Contingency means they're paid only if you are. "
              'Tip four, read the contract fully, know the term, your rights, and how to '
              'cancel.',
      'timestamp': 291,
      'timestamp_label': '[00:04:51]',
      'timestamp_seconds': 291,
      'tip': 'Check the state business database and any attorney partnerships. Tip three, '
             "understand the fee structure. Contingency means they're paid only if you are. "
             'Tip four, read the contract fully, know the term, your rights, and how to '
             'cancel.',
      'title': 'Beginners Guide to Surplus Funds: How to Claim Money After Foreclosure- '
               'Step-by-Step Tutorial (Dreams & Dollars: The Everyday Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=pSC1FfAjNuo&t=291s',
      'video_id': 'pSC1FfAjNuo'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=TTfaOSBvLDc&t=308s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': "Now, there's just some general information about the stars. Well, now the state "
              "has a 10% commission cap, the commission cap, at least for me, isn't nearly as "
              'important as this bottom part getting bulk leads because he has 10, 20%. There '
              "are some states that they don't care.",
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': "Now, there's just some general information about the stars. Well, now the state "
             "has a 10% commission cap, the commission cap, at least for me, isn't nearly as "
             'important as this bottom part getting bulk leads because he has 10, 20%. There '
             "are some states that they don't care.",
      'title': 'State Funds Tutorial Delaware: Registering As A Property Locator For The State '
               'Of Delaware. (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=TTfaOSBvLDc&t=308s',
      'video_id': 'TTfaOSBvLDc'},
     {'author': 'Emend The Mass Media Group',
      'channel': 'Emend The Mass Media Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:09](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=789s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'Are you charging a fee to assist the owner with the claim or did you enter into '
              'a contract with a professional finder? If yes, then you\'ll have that option. " '
              "And once you put in all the applicable information, you're going to hit that "
              'next button.',
      'timestamp': 789,
      'timestamp_label': '[00:13:09]',
      'timestamp_seconds': 789,
      'tip': 'Are you charging a fee to assist the owner with the claim or did you enter into '
             'a contract with a professional finder? If yes, then you\'ll have that option. " '
             "And once you put in all the applicable information, you're going to hit that "
             'next button.',
      'title': 'CA Unclaimed Property - Are you missing out? - Tutorial (Emend The Mass Media '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=ijLtjR0tTd8&t=789s',
      'video_id': 'ijLtjR0tTd8'},
     {'author': 'Rent Own Sell',
      'channel': 'Rent Own Sell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=VBvaq5etzV4&t=163s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': "Like agent fees and possibly court costs furthermore if you're planning on "
              "financing the purchase be aware that some lenders won't approve your loan "
              'application until you can provide a clear title.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': "Like agent fees and possibly court costs furthermore if you're planning on "
             "financing the purchase be aware that some lenders won't approve your loan "
             'application until you can provide a clear title.',
      'title': 'How to Check for Property Liens - Complete Guide (Rent Own Sell)',
      'url': 'https://www.youtube.com/watch?v=VBvaq5etzV4&t=163s',
      'video_id': 'VBvaq5etzV4'},
     {'author': 'Nick Fullmer- Overage Syndicate',
      'channel': 'Nick Fullmer- Overage Syndicate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:20](https://www.youtube.com/watch?v=vd__NHmQYgM&t=1580s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': '"I wasn\'t expecting a response." Now, I wanted to say that\'s why my fees are '
              'are where they\'re at because you can get in touch with me. I just said, "Let '
              'me look at the case again and I\'ll get back to you tomorrow." So, we were '
              'texting this morning back and forth.',
      'timestamp': 1580,
      'timestamp_label': '[00:26:20]',
      'timestamp_seconds': 1580,
      'tip': '"I wasn\'t expecting a response." Now, I wanted to say that\'s why my fees are '
             'are where they\'re at because you can get in touch with me. I just said, "Let me '
             'look at the case again and I\'ll get back to you tomorrow." So, we were texting '
             'this morning back and forth.',
      'title': '8 Surplus Funds Deals Within 3 Months of Starting The Business (Nick Fullmer- '
               'Overage Syndicate)',
      'url': 'https://www.youtube.com/watch?v=vd__NHmQYgM&t=1580s',
      'video_id': 'vd__NHmQYgM'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:27](https://www.youtube.com/watch?v=GK-4kFznJlA&t=1287s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': "I mentioned the the the vetted group of PIs that we're a part of. It's 800 uh "
              'PIs spread out all over the United [clears throat] States. But, I I developed a '
              'lot of relationships over 25 years as an FBI agent uh to include those in in '
              'foreign areas.',
      'timestamp': 1287,
      'timestamp_label': '[00:21:27]',
      'timestamp_seconds': 1287,
      'tip': "I mentioned the the the vetted group of PIs that we're a part of. It's 800 uh "
             'PIs spread out all over the United [clears throat] States. But, I I developed a '
             'lot of relationships over 25 years as an FBI agent uh to include those in in '
             'foreign areas.',
      'title': 'How Ex-FBI Agents Skip Trace Anyone for Real Estate Deals (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=GK-4kFznJlA&t=1287s',
      'video_id': 'GK-4kFznJlA'},
     {'author': 'Sternberg Law Group',
      'channel': 'Sternberg Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=z6jQuGWdtDY&t=147s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': '550, you need to hire an attorney, you can call us, sternberglegalgroup. We '
              'need to then go to the foreclosure trustee, and we need to work with them to '
              'make sure all the liens are paid off, and that extra $200,000 is transferred to '
              'you by way of a check.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': '550, you need to hire an attorney, you can call us, sternberglegalgroup. We need '
             'to then go to the foreclosure trustee, and we need to work with them to make '
             'sure all the liens are paid off, and that extra $200,000 is transferred to you '
             'by way of a check.',
      'title': 'Surplus Funds After Foreclosure Explained | What Homeowners Must Know | '
               'Sternberg Law Group (Sternberg Law Group)',
      'url': 'https://www.youtube.com/watch?v=z6jQuGWdtDY&t=147s',
      'video_id': 'z6jQuGWdtDY'},
     {'author': 'Haynes Law Group',
      'channel': 'Haynes Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=Uj-vrJWHKQo&t=126s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': 'Again, Florida statute 4532 subsection 1B states a subordinate lean holder '
              'means the holder of a subordinate lean shown on the face of the pleadings as an '
              'incumbrance on the property.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Again, Florida statute 4532 subsection 1B states a subordinate lean holder means '
             'the holder of a subordinate lean shown on the face of the pleadings as an '
             'incumbrance on the property.',
      'title': 'Florida Foreclosure Surplus Funds Update: What is a Subordinate Lien Holder? '
               '(Haynes Law Group)',
      'url': 'https://www.youtube.com/watch?v=Uj-vrJWHKQo&t=126s',
      'video_id': 'Uj-vrJWHKQo'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:48](https://www.youtube.com/watch?v=1Pp-cjYnY2k&t=408s)',
      'relevance': 'Attributed practitioner commentary on contingency fee caps, assignment '
                   'restrictions, and net recovery unit economics; verify statutory ceilings '
                   'before contracting.',
      'source_type': 'video_pro_tip',
      'text': "It's kind of like being a contingent-fee attorney without having to go to law "
              'school, without having long lawsuits or anything like that. But you get paid '
              'crazy money because you bring so much help to people.',
      'timestamp': 408,
      'timestamp_label': '[00:06:48]',
      'timestamp_seconds': 408,
      'tip': "It's kind of like being a contingent-fee attorney without having to go to law "
             'school, without having long lawsuits or anything like that. But you get paid '
             'crazy money because you bring so much help to people.',
      'title': "How To Become A Surplus Funds Recovery Agent (Bob Diamond - America's Tax Sale "
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=1Pp-cjYnY2k&t=408s',
      'video_id': '1Pp-cjYnY2k'}],
 4: [{'author': 'Hutch & Holmes',
      'channel': 'Hutch & Holmes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=L2oKpjOoh20&t=84s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'Uh but when notary is needed, which is pretty much required in this business, '
              'the claimant can find their own notary or you may partner with a notary or do '
              "what I suggest is become a notary. And when legal work is needed, that's when "
              'you get the attorney involved.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': 'Uh but when notary is needed, which is pretty much required in this business, '
             'the claimant can find their own notary or you may partner with a notary or do '
             "what I suggest is become a notary. And when legal work is needed, that's when "
             'you get the attorney involved.',
      'title': 'How to Recover Foreclosure Surplus Funds (3-Step System) (Hutch & Holmes)',
      'url': 'https://www.youtube.com/watch?v=L2oKpjOoh20&t=84s',
      'video_id': 'L2oKpjOoh20'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:12](https://www.youtube.com/watch?v=R8B06ovsDXI&t=972s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "We're going to help them with the notary filing cost and we're going to help "
              "them with what's called due diligence, which is essentially confirming "
              "entitlement. So, we're going to gather all the documents that they're entitled.",
      'timestamp': 972,
      'timestamp_label': '[00:16:12]',
      'timestamp_seconds': 972,
      'tip': "We're going to help them with the notary filing cost and we're going to help "
             "them with what's called due diligence, which is essentially confirming "
             "entitlement. So, we're going to gather all the documents that they're entitled.",
      'title': 'How to start a Surplus Funds Business (45 min raw free game) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=R8B06ovsDXI&t=972s',
      'video_id': 'R8B06ovsDXI'},
     {'author': 'William Whitman, Esquire',
      'channel': 'William Whitman, Esquire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=0xk7lNvAgn0&t=52s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "Entity if that's where you were and that takes me to the Pennsylvania "
              'Department of State there is a business entity search and on the business '
              "filing Services page there's a free business search feature I search themein "
              'properties.',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "Entity if that's where you were and that takes me to the Pennsylvania Department "
             'of State there is a business entity search and on the business filing Services '
             "page there's a free business search feature I search themein properties.",
      'title': 'Will Whitman, Esquire explains how to locate companies owed surplus funds '
               '(William Whitman, Esquire)',
      'url': 'https://www.youtube.com/watch?v=0xk7lNvAgn0&t=52s',
      'video_id': '0xk7lNvAgn0'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=4O5XeYwMAts&t=233s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "Doesn't really have any cost to it. There's no cost to apply or anything. You "
              "don't have to hire a lawyer, just fill in the form. Thankfully, that's the "
              "majority of states, and that's generally the process. So it's one of the things "
              'that makes this business so attractive.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': "Doesn't really have any cost to it. There's no cost to apply or anything. You "
             "don't have to hire a lawyer, just fill in the form. Thankfully, that's the "
             "majority of states, and that's generally the process. So it's one of the things "
             'that makes this business so attractive.',
      'title': "How To Find Tax Sale Overages (Bob Diamond - America's Tax Sale Attorney)",
      'url': 'https://www.youtube.com/watch?v=4O5XeYwMAts&t=233s',
      'video_id': '4O5XeYwMAts'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:10](https://www.youtube.com/watch?v=8-8koApqnYA&t=310s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'When you search how to start this business, you get the same list every time. '
              'Form an LLC, get an EIN, open a bank account, build a website, get a logo, a '
              'CRM. Then, near the bottom, go find leads and make calls.',
      'timestamp': 310,
      'timestamp_label': '[00:05:10]',
      'timestamp_seconds': 310,
      'tip': 'When you search how to start this business, you get the same list every time. '
             'Form an LLC, get an EIN, open a bank account, build a website, get a logo, a '
             'CRM. Then, near the bottom, go find leads and make calls.',
      'title': 'How to Start a Surplus Funds Business in 2026 (Step by Step) (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=8-8koApqnYA&t=310s',
      'video_id': '8-8koApqnYA'},
     {'author': 'Rent Own Sell',
      'channel': 'Rent Own Sell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=VBvaq5etzV4&t=161s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'Shell out more money to cover expenses like agent fees and possibly court costs '
              "furthermore if you're planning on financing the purchase be aware that some "
              "lenders won't approve your loan application until you can provide a clear "
              'title.',
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': 'Shell out more money to cover expenses like agent fees and possibly court costs '
             "furthermore if you're planning on financing the purchase be aware that some "
             "lenders won't approve your loan application until you can provide a clear title.",
      'title': 'How to Check for Property Liens - Complete Guide (Rent Own Sell)',
      'url': 'https://www.youtube.com/watch?v=VBvaq5etzV4&t=161s',
      'video_id': 'VBvaq5etzV4'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=bpxSOg1_xbE&t=168s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'Additionally, understand that every state has its own rules about third-party '
              'surplus funds recovery. In some states, non- attorneys are limited in what they '
              'can do or they may need to work with a licensed attorney when filing claims.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Additionally, understand that every state has its own rules about third-party '
             'surplus funds recovery. In some states, non- attorneys are limited in what they '
             'can do or they may need to work with a licensed attorney when filing claims.',
      'title': 'Top 5 Things Nobody Tells You About the Surplus Funds Recovery Business '
               '(Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=bpxSOg1_xbE&t=168s',
      'video_id': 'bpxSOg1_xbE'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:57](https://www.youtube.com/watch?v=xqpLsq3JVlU&t=357s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "What what you do is you just in fact I've had um documents notoriize. You just "
              'find an notary in that country. You have to prove their dealings and you have '
              'to prove that they did business in the United States.',
      'timestamp': 357,
      'timestamp_label': '[00:05:57]',
      'timestamp_seconds': 357,
      'tip': "What what you do is you just in fact I've had um documents notoriize. You just "
             'find an notary in that country. You have to prove their dealings and you have to '
             'prove that they did business in the United States.',
      'title': 'Cold Calling for Surplus Funds: What Actually Works (Surplus Institute / David '
               'Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=xqpLsq3JVlU&t=357s',
      'video_id': 'xqpLsq3JVlU'},
     {'author': 'Noble Notary & Legal Document Preparers',
      'channel': 'Noble Notary & Legal Document Preparers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=DM0kjEZlbSk&t=227s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "If you check lean holder, you've got to break down the exact math for the "
              "county. What was the original amount of the lean? What's the current amount "
              'owed today? Are there specific attorney fees or interest or costs due?',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': "If you check lean holder, you've got to break down the exact math for the "
             "county. What was the original amount of the lean? What's the current amount owed "
             'today? Are there specific attorney fees or interest or costs due?',
      'title': 'Florida Tax Deed Surplus Claim Forms:  How to Claim Excess Funds (Noble Notary '
               '& Legal Document Preparers)',
      'url': 'https://www.youtube.com/watch?v=DM0kjEZlbSk&t=227s',
      'video_id': 'DM0kjEZlbSk'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=q2gk3WmK5xs&t=102s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'Otherwise, you can hire a professional to help you with it. This LLC protects '
              'your personal assets and makes your business legitimate, while the EIN acts as '
              "your company's tax identification number.",
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': 'Otherwise, you can hire a professional to help you with it. This LLC protects '
             'your personal assets and makes your business legitimate, while the EIN acts as '
             "your company's tax identification number.",
      'title': 'The Most Overlooked Surplus Funds Recovery Business You Can Start With $0 '
               '(Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=q2gk3WmK5xs&t=102s',
      'video_id': 'q2gk3WmK5xs'},
     {'author': 'My Lawyer In Spain',
      'channel': 'My Lawyer In Spain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:44](https://www.youtube.com/watch?v=ywaYY4cPtAY&t=1604s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'Now we\'re going to use a firm that we\'re familiar with." As long as the firm '
              'is legitimate and bonafidey. Um, then we would kind of recommend them to the '
              'family. If it needs a lawyer in the UK or and Spain, we can assist with that as '
              'well.',
      'timestamp': 1604,
      'timestamp_label': '[00:26:44]',
      'timestamp_seconds': 1604,
      'tip': 'Now we\'re going to use a firm that we\'re familiar with." As long as the firm '
             'is legitimate and bonafidey. Um, then we would kind of recommend them to the '
             'family. If it needs a lawyer in the UK or and Spain, we can assist with that as '
             'well.',
      'title': 'Unclaimed Estates & Abandoned Properties in Spain - tracing Heirs Worldwide '
               '(My Lawyer In Spain)',
      'url': 'https://www.youtube.com/watch?v=ywaYY4cPtAY&t=1604s',
      'video_id': 'ywaYY4cPtAY'},
     {'author': 'Private Investigator Videos',
      'channel': 'Private Investigator Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:34](https://www.youtube.com/watch?v=GWuQIN0aSwQ&t=154s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "Don't take it the word of the auction company or even the property owner what's "
              'on the property you want to know for sure based on an official certified title '
              "abstract what's on the property what's not and then you can make your "
              'decisions.',
      'timestamp': 154,
      'timestamp_label': '[00:02:34]',
      'timestamp_seconds': 154,
      'tip': "Don't take it the word of the auction company or even the property owner what's "
             'on the property you want to know for sure based on an official certified title '
             "abstract what's on the property what's not and then you can make your decisions.",
      'title': 'What liens remain on a title search after foreclosure? (Private Investigator '
               'Videos)',
      'url': 'https://www.youtube.com/watch?v=GWuQIN0aSwQ&t=154s',
      'video_id': 'GWuQIN0aSwQ'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:20](https://www.youtube.com/watch?v=FgFrlIpbscs&t=800s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "Now, the last one is relational abandonment, which could be the creditor's "
              'relationship to this investment. It could be the defunct entity. So, their '
              'relationship with that business is now abandoned. It could be the heirs '
              'fighting.',
      'timestamp': 800,
      'timestamp_label': '[00:13:20]',
      'timestamp_seconds': 800,
      'tip': "Now, the last one is relational abandonment, which could be the creditor's "
             'relationship to this investment. It could be the defunct entity. So, their '
             'relationship with that business is now abandoned. It could be the heirs '
             'fighting.',
      'title': 'How to Find Curative Title Deals Nobody Else Is Chasing (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=FgFrlIpbscs&t=800s',
      'video_id': 'FgFrlIpbscs'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=Qn63DtrxFts&t=156s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': "'t want them to work anymore. Um a few weeks ago I called on a notary to do a "
              'job and the notary specialized in working with real estate agents. And the '
              'notary was like, "Hey, look, I had to get out of the business and take a day '
              'job.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': "'t want them to work anymore. Um a few weeks ago I called on a notary to do a "
             'job and the notary specialized in working with real estate agents. And the '
             'notary was like, "Hey, look, I had to get out of the business and take a day '
             'job.',
      'title': 'How to Build a Nationwide Notary Team (Step-by-Step) (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=Qn63DtrxFts&t=156s',
      'video_id': 'Qn63DtrxFts'},
     {'author': 'Attorney Jack',
      'channel': 'Attorney Jack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=KKKIgl--DNo&t=218s)',
      'relevance': 'Attributed practitioner commentary on lean firm setup, startup capital, '
                   'notary/records costs, and lawful attorney co-counsel structures; confirm '
                   'state bar rules.',
      'source_type': 'video_pro_tip',
      'text': 'The law firm takes care of any other attorney fees, clerk fees, or any type of '
              'assessments that may need to be done to be able to access these funds. Reach '
              'out to us today if you or a family member has gone through a foreclosure in any '
              'state in the United States.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'The law firm takes care of any other attorney fees, clerk fees, or any type of '
             'assessments that may need to be done to be able to access these funds. Reach out '
             'to us today if you or a family member has gone through a foreclosure in any '
             'state in the United States.',
      'title': 'Foreclosure - Surplus Funds Recovery - Attorney Assistance (Attorney Jack)',
      'url': 'https://www.youtube.com/watch?v=KKKIgl--DNo&t=218s',
      'video_id': 'KKKIgl--DNo'}],
 5: [{'author': 'AFX Research LLC',
      'channel': 'AFX Research LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=53s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "Mortgage liens are placed by lenders. Mechanic's liens are filed by contractors "
              "who weren't paid for their work. Judgment liens come from court rulings against "
              'the property owner. HOA liens can be filed for unpaid dues. And IRS liens cover '
              'unpaid federal taxes.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "Mortgage liens are placed by lenders. Mechanic's liens are filed by contractors "
             "who weren't paid for their work. Judgment liens come from court rulings against "
             'the property owner. HOA liens can be filed for unpaid dues. And IRS liens cover '
             'unpaid federal taxes.',
      'title': 'HOW TO FIND LIENS & TITLE SEARCH IN TEXAS (AFX Research LLC)',
      'url': 'https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=53s',
      'video_id': 'HPyO3dkjbCQ'},
     {'author': 'Noble Notary & Legal Document Preparers',
      'channel': 'Noble Notary & Legal Document Preparers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=DM0kjEZlbSk&t=126s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': 'Second are the lean holders. So think mortgage lenders or an HOA that recorded '
              'a lean or maybe someone who won a court judgment against the property. Third, '
              'you have court-appointed personal representatives like probate administrators '
              'handling an estate.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Second are the lean holders. So think mortgage lenders or an HOA that recorded a '
             'lean or maybe someone who won a court judgment against the property. Third, you '
             'have court-appointed personal representatives like probate administrators '
             'handling an estate.',
      'title': 'Florida Tax Deed Surplus Claim Forms:  How to Claim Excess Funds (Noble Notary '
               '& Legal Document Preparers)',
      'url': 'https://www.youtube.com/watch?v=DM0kjEZlbSk&t=126s',
      'video_id': 'DM0kjEZlbSk'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=LdemHPCk0dk&t=74s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': 'HOA liens, judgment liens, which is when somebody sued the owner and won, tax '
              'liens from the IRS or state, and city liens like unpaid water bills or code '
              "fines. Now here's where it gets interesting. The type of sale changes who gets "
              'paid.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': 'HOA liens, judgment liens, which is when somebody sued the owner and won, tax '
             'liens from the IRS or state, and city liens like unpaid water bills or code '
             "fines. Now here's where it gets interesting. The type of sale changes who gets "
             'paid.',
      'title': 'How to Check for Liens Before You Call About Surplus Funds (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=LdemHPCk0dk&t=74s',
      'video_id': 'LdemHPCk0dk'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=195s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "Now there's another lien that everybody's worried about, and that's the I-R-S "
              'lien. That lien will remain on the property for 120 days, if the county has '
              "notified the IRS that they're gonna have an auction. So most of the I-R-S liens "
              'will fall off the property.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': "Now there's another lien that everybody's worried about, and that's the I-R-S "
             'lien. That lien will remain on the property for 120 days, if the county has '
             "notified the IRS that they're gonna have an auction. So most of the I-R-S liens "
             'will fall off the property.',
      'title': 'How To Do A Title Search On A Property Yourself Before You Bid At Tax Sale '
               'Auctions (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=195s',
      'video_id': 'xtdWFaJY8Xc'},
     {'author': 'Nick Fullmer- Overage Syndicate',
      'channel': 'Nick Fullmer- Overage Syndicate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=KOYBZFn2k7w&t=108s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': 'Little details like that you need to be aware of. Now, this right here, we also '
              'want to know what liens existed on the property at the time of the sale, '
              'because lien holders have priority over homeowners.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'Little details like that you need to be aware of. Now, this right here, we also '
             'want to know what liens existed on the property at the time of the sale, because '
             'lien holders have priority over homeowners.',
      'title': 'Overages & Surplus Fund Debt & Title Research: Not As Easy As It Seems.  Two '
               'tips To Help (Nick Fullmer- Overage Syndicate)',
      'url': 'https://www.youtube.com/watch?v=KOYBZFn2k7w&t=108s',
      'video_id': 'KOYBZFn2k7w'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:26](https://www.youtube.com/watch?v=FJj3hN2KbIg&t=506s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "'s liens on GSCCA, make sure you go further in your research, check to see if "
              "the client is still alive or deceased. If they're deceased, search the "
              'obituary. You can go to the probate court, perform a search as well, and then '
              'you market.',
      'timestamp': 506,
      'timestamp_label': '[00:08:26]',
      'timestamp_seconds': 506,
      'tip': "'s liens on GSCCA, make sure you go further in your research, check to see if "
             "the client is still alive or deceased. If they're deceased, search the obituary. "
             'You can go to the probate court, perform a search as well, and then you market.',
      'title': 'How to Do Surplus Funds in Georgia (Step-by-Step Guide) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=FJj3hN2KbIg&t=506s',
      'video_id': 'FJj3hN2KbIg'},
     {'author': 'Sternberg Law Group',
      'channel': 'Sternberg Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:23](https://www.youtube.com/watch?v=z6jQuGWdtDY&t=143s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': '750,000, the payoffs between the first mortgage and the second mortgage and '
              'your tax lien was 550, you need to hire an attorney, you can call us, '
              'sternberglegalgroup.',
      'timestamp': 143,
      'timestamp_label': '[00:02:23]',
      'timestamp_seconds': 143,
      'tip': '750,000, the payoffs between the first mortgage and the second mortgage and your '
             'tax lien was 550, you need to hire an attorney, you can call us, '
             'sternberglegalgroup.',
      'title': 'Surplus Funds After Foreclosure Explained | What Homeowners Must Know | '
               'Sternberg Law Group (Sternberg Law Group)',
      'url': 'https://www.youtube.com/watch?v=z6jQuGWdtDY&t=143s',
      'video_id': 'z6jQuGWdtDY'},
     {'author': 'Attorney Jack',
      'channel': 'Attorney Jack',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=KKKIgl--DNo&t=142s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': 'Remember, there are many times that people paid their mortgage or their tax '
              'liens for years, and then at the last minute due to some unfortunate situation '
              'or a death, uh the these the mortgage or the taxes were not paid.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'Remember, there are many times that people paid their mortgage or their tax '
             'liens for years, and then at the last minute due to some unfortunate situation '
             'or a death, uh the these the mortgage or the taxes were not paid.',
      'title': 'Foreclosure - Surplus Funds Recovery - Attorney Assistance (Attorney Jack)',
      'url': 'https://www.youtube.com/watch?v=KKKIgl--DNo&t=142s',
      'video_id': 'KKKIgl--DNo'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:48](https://www.youtube.com/watch?v=5LDDkiUTmXI&t=948s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "'s a chance that those liens might that mortgage might still be on those those "
              "sold properties. Um so I love how you guys are thinking this doesn't make "
              "sense. And this is where we talk about like how I've made so much money with "
              'curiosity, right?',
      'timestamp': 948,
      'timestamp_label': '[00:15:48]',
      'timestamp_seconds': 948,
      'tip': "'s a chance that those liens might that mortgage might still be on those those "
             "sold properties. Um so I love how you guys are thinking this doesn't make sense. "
             "And this is where we talk about like how I've made so much money with curiosity, "
             'right?',
      'title': "How a Curative Title Investor Finds & Solves Deals Others Can't (Courtney "
               'Fricke)',
      'url': 'https://www.youtube.com/watch?v=5LDDkiUTmXI&t=948s',
      'video_id': '5LDDkiUTmXI'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=1Pp-cjYnY2k&t=375s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': 'You might have the wrong person. Sometimes we get junior instead of senior — '
              "that's our most common problem, where it's like, oh, we got the son instead of "
              'the father. We gotta go get the father to sign up. You may have a competing '
              'claimant.',
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': 'You might have the wrong person. Sometimes we get junior instead of senior — '
             "that's our most common problem, where it's like, oh, we got the son instead of "
             'the father. We gotta go get the father to sign up. You may have a competing '
             'claimant.',
      'title': "How To Become A Surplus Funds Recovery Agent (Bob Diamond - America's Tax Sale "
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=1Pp-cjYnY2k&t=375s',
      'video_id': '1Pp-cjYnY2k'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:49](https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=709s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': '" Or you need um you know, the price you know, you have the price at at X '
              "number, but they owe too much, you know, liens, judgments, whatever. Well, I'm "
              "tracking down lien lien holders and creditors and I'm trying to do whatever I "
              'can to to make the deal work.',
      'timestamp': 709,
      'timestamp_label': '[00:11:49]',
      'timestamp_seconds': 709,
      'tip': '" Or you need um you know, the price you know, you have the price at at X '
             "number, but they owe too much, you know, liens, judgments, whatever. Well, I'm "
             "tracking down lien lien holders and creditors and I'm trying to do whatever I "
             'can to to make the deal work.',
      'title': 'Before You Go From Wholesaling to Curative Title, Watch This (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=709s',
      'video_id': 'z6h2w5h7oTQ'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:36](https://www.youtube.com/watch?v=suJSu-vn6yI&t=696s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "'ll either file the claim yourself or use an attorney. On mortgage foreclosures "
              "that are judicial, and on probate cases where the owner is deceased, you'll "
              'want to use an attorney. On tax sales where the county has a claim form online, '
              'you can often file this by yourself.',
      'timestamp': 696,
      'timestamp_label': '[00:11:36]',
      'timestamp_seconds': 696,
      'tip': "'ll either file the claim yourself or use an attorney. On mortgage foreclosures "
             "that are judicial, and on probate cases where the owner is deceased, you'll want "
             'to use an attorney. On tax sales where the county has a claim form online, you '
             'can often file this by yourself.',
      'title': 'How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=suJSu-vn6yI&t=696s',
      'video_id': 'suJSu-vn6yI'},
     {'author': 'ohiocommerce',
      'channel': 'ohiocommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:44](https://www.youtube.com/watch?v=dFKMkAIKskU&t=344s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': 'Parent would be a NEX ofin a child would be a NEX ofin and a sibling um not in '
              'that particular order but that is the four main major next of again anybody '
              'beyond that may need to go to court to determine that they are the person that '
              'can represent that deceased loved.',
      'timestamp': 344,
      'timestamp_label': '[00:05:44]',
      'timestamp_seconds': 344,
      'tip': 'Parent would be a NEX ofin a child would be a NEX ofin and a sibling um not in '
             'that particular order but that is the four main major next of again anybody '
             'beyond that may need to go to court to determine that they are the person that '
             'can represent that deceased loved.',
      'title': 'What Documentation is Needed for Unclaimed Funds (ohiocommerce)',
      'url': 'https://www.youtube.com/watch?v=dFKMkAIKskU&t=344s',
      'video_id': 'dFKMkAIKskU'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=ieI6zKICpKo&t=139s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "'s going to help out a lot. The fact that it's a probate is going to be a pain "
              "in the you know what, but we'll we'll we'll get that situated for you if you're "
              "wanting us to do that. We'd gladly work with you on that. Go ahead and start "
              'the paperwork then, okay?',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': "'s going to help out a lot. The fact that it's a probate is going to be a pain "
             "in the you know what, but we'll we'll we'll get that situated for you if you're "
             "wanting us to do that. We'd gladly work with you on that. Go ahead and start the "
             'paperwork then, okay?',
      'title': '$16,000 Live Cold Calling Commission (Surplus Institute / David Church / '
               'Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=ieI6zKICpKo&t=139s',
      'video_id': 'ieI6zKICpKo'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=smhFDkvMwkM&t=207s)',
      'relevance': 'Attributed practitioner commentary on surviving vs. wiped-out liens, '
                   'junior encumbrance priority, upset-bid windows, and probate/bankruptcy '
                   'traps; verify via title search.',
      'source_type': 'video_pro_tip',
      'text': "'t seem like it'd be that big of a priority 'cause then it just problems, well, "
              "how much is it? And just again, it's just one other thing to get some to the "
              "next step. After they have acknowledged that, I'll say, Alright.",
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': "'t seem like it'd be that big of a priority 'cause then it just problems, well, "
             "how much is it? And just again, it's just one other thing to get some to the "
             "next step. After they have acknowledged that, I'll say, Alright.",
      'title': 'Best Cold Calling Script For Surplus Funds. overage syndicate surplus funds '
               'cold calling (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=smhFDkvMwkM&t=207s',
      'video_id': 'smhFDkvMwkM'}],
 6: [{'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:12](https://www.youtube.com/watch?v=YCb5jYZX_A8&t=312s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'Checking county lists, watching auction calendars, digging through court '
              'records, checking liens, skip tracing, it can easily be 10 to 20 hours per week '
              "or more. And that's before you've made a single call. Tax sales, the county "
              'surplus list.',
      'timestamp': 312,
      'timestamp_label': '[00:05:12]',
      'timestamp_seconds': 312,
      'tip': 'Checking county lists, watching auction calendars, digging through court '
             'records, checking liens, skip tracing, it can easily be 10 to 20 hours per week '
             "or more. And that's before you've made a single call. Tax sales, the county "
             'surplus list.',
      'title': 'How to Find Surplus Funds Lists (Tax Sales and Foreclosures) (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=YCb5jYZX_A8&t=312s',
      'video_id': 'YCb5jYZX_A8'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:57](https://www.youtube.com/watch?v=v0-thxE7IK4&t=297s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': "You just need to know how to get it and what to do. It's sitting there "
              "somewhere in a case management system. Just nobody's asked for it. Every state "
              'has public records law. Under that law, you can legally request this list and '
              'the office generally has to respond.',
      'timestamp': 297,
      'timestamp_label': '[00:04:57]',
      'timestamp_seconds': 297,
      'tip': "You just need to know how to get it and what to do. It's sitting there somewhere "
             "in a case management system. Just nobody's asked for it. Every state has public "
             'records law. Under that law, you can legally request this list and the office '
             'generally has to respond.',
      'title': 'How To Find Surplus Funds Lists In 2026 (For Free) (Surplus Funds Secrets)',
      'url': 'https://www.youtube.com/watch?v=v0-thxE7IK4&t=297s',
      'video_id': 'v0-thxE7IK4'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:26](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=506s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'Plenty of times people get sent the the um satisfaction for their mortgage in '
              "the mail, but then they don't go bring it to the court the the public records "
              'at the county clerk to then release the mortgage.',
      'timestamp': 506,
      'timestamp_label': '[00:08:26]',
      'timestamp_seconds': 506,
      'tip': 'Plenty of times people get sent the the um satisfaction for their mortgage in '
             "the mail, but then they don't go bring it to the court the the public records at "
             'the county clerk to then release the mortgage.',
      'title': '5 Curative Title Terms Every Investor Should Understand (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=sf2hUucsNZ8&t=506s',
      'video_id': 'sf2hUucsNZ8'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=296s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'But you need to get some research done before you bid at a tax defaulted '
              'auction. All of this is at the county records. The county records are the '
              'public records.',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'But you need to get some research done before you bid at a tax defaulted '
             'auction. All of this is at the county records. The county records are the public '
             'records.',
      'title': 'How To Do A Title Search On A Property Yourself Before You Bid At Tax Sale '
               'Auctions (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=296s',
      'video_id': 'xtdWFaJY8Xc'},
     {'author': 'Tax Deed Surplus & Lien-Research Records',
      'channel': 'Tax Deed Surplus & Lien-Research Records',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=y94Ncg0WHn0&t=26s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'You can also use our auction calendar which has of course Pulk County and all '
              'the other counties and just do a search here for Pulk and that will show you '
              'the next one coming up or the previous ones. So now that we have the tax deed '
              "date, we're going to put in May 18th.",
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': 'You can also use our auction calendar which has of course Pulk County and all '
             'the other counties and just do a search here for Pulk and that will show you the '
             'next one coming up or the previous ones. So now that we have the tax deed date, '
             "we're going to put in May 18th.",
      'title': 'Polk County Tax Deed Surplus (Tax Deed Surplus & Lien-Research Records)',
      'url': 'https://www.youtube.com/watch?v=y94Ncg0WHn0&t=26s',
      'video_id': 'y94Ncg0WHn0'},
     {'author': 'Noble Notary & Legal Document Preparers',
      'channel': 'Noble Notary & Legal Document Preparers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:33](https://www.youtube.com/watch?v=DM0kjEZlbSk&t=273s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'The good news is you can usually find all of this by just searching your '
              "county's online public records portal. Doing this tells the clerk exactly where "
              'to look in their archives to verify your claim is 100% legitimate. Section '
              'five, gathering supporting documentation.',
      'timestamp': 273,
      'timestamp_label': '[00:04:33]',
      'timestamp_seconds': 273,
      'tip': 'The good news is you can usually find all of this by just searching your '
             "county's online public records portal. Doing this tells the clerk exactly where "
             'to look in their archives to verify your claim is 100% legitimate. Section five, '
             'gathering supporting documentation.',
      'title': 'Florida Tax Deed Surplus Claim Forms:  How to Claim Excess Funds (Noble Notary '
               '& Legal Document Preparers)',
      'url': 'https://www.youtube.com/watch?v=DM0kjEZlbSk&t=273s',
      'video_id': 'DM0kjEZlbSk'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=6UiKunbtUa0&t=394s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': "Let's say we'll take Los Angeles County. And then when you click on Los Angeles "
              "County, it'll take you to a page like this. What information you're looking for "
              "is the auction folder right here. So click on that and it'll give you a list of "
              'the properties that have been sold.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': "Let's say we'll take Los Angeles County. And then when you click on Los Angeles "
             "County, it'll take you to a page like this. What information you're looking for "
             "is the auction folder right here. So click on that and it'll give you a list of "
             'the properties that have been sold.',
      'title': 'How To Find Excess Proceeds List In 2025 (Proven Strategies) (Overage '
               'Acquisition)',
      'url': 'https://www.youtube.com/watch?v=6UiKunbtUa0&t=394s',
      'video_id': '6UiKunbtUa0'},
     {'author': 'Next Level VA',
      'channel': 'Next Level VA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:15](https://www.youtube.com/watch?v=2e4YGOesnUY&t=1455s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'A list that results from a type of a sale that is referred to as an upset sale '
              "it's called an upset sale because in this type of a sale the last highest "
              'bidder at the auction can still get outbid by another investor during the upset '
              'bid period which follows the sale.',
      'timestamp': 1455,
      'timestamp_label': '[00:24:15]',
      'timestamp_seconds': 1455,
      'tip': 'A list that results from a type of a sale that is referred to as an upset sale '
             "it's called an upset sale because in this type of a sale the last highest bidder "
             'at the auction can still get outbid by another investor during the upset bid '
             'period which follows the sale.',
      'title': 'Excess Proceeds List, Tax Sale Overages List, Surplus Funds List (Free '
               'resources + 10 examples) (Next Level VA)',
      'url': 'https://www.youtube.com/watch?v=2e4YGOesnUY&t=1455s',
      'video_id': '2e4YGOesnUY'},
     {'author': 'AFX Research LLC',
      'channel': 'AFX Research LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=77s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': "Start with the County Clerk's Office. Every county in Texas maintains property "
              'records — deeds, lien documents, easements, and the full chain of title. Most '
              'counties have online databases you can search by address or owner name.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': "Start with the County Clerk's Office. Every county in Texas maintains property "
             'records — deeds, lien documents, easements, and the full chain of title. Most '
             'counties have online databases you can search by address or owner name.',
      'title': 'HOW TO FIND LIENS & TITLE SEARCH IN TEXAS (AFX Research LLC)',
      'url': 'https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=77s',
      'video_id': 'HPyO3dkjbCQ'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:04](https://www.youtube.com/watch?v=8-8koApqnYA&t=544s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'Volusia County, Florida is 24 pages of the same thing. Public, free, and most '
              'people never open it. Something to be aware of though, not every county posts a '
              'list. Harris County, Texas, publishes nothing. Their page says email the court '
              'registry to request a listing.',
      'timestamp': 544,
      'timestamp_label': '[00:09:04]',
      'timestamp_seconds': 544,
      'tip': 'Volusia County, Florida is 24 pages of the same thing. Public, free, and most '
             'people never open it. Something to be aware of though, not every county posts a '
             'list. Harris County, Texas, publishes nothing. Their page says email the court '
             'registry to request a listing.',
      'title': 'How to Start a Surplus Funds Business in 2026 (Step by Step) (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=8-8koApqnYA&t=544s',
      'video_id': '8-8koApqnYA'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=TTfaOSBvLDc&t=475s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': "'t ever try to reinvent the rule book, you do everything exactly how they want, "
              'and you should be good to go. The State does offer walk leads : Now on the wet. '
              'On the website, it says you have to do a manual search, but you can send in a '
              'FOIA request to get bulk data.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': "'t ever try to reinvent the rule book, you do everything exactly how they want, "
             'and you should be good to go. The State does offer walk leads : Now on the wet. '
             'On the website, it says you have to do a manual search, but you can send in a '
             'FOIA request to get bulk data.',
      'title': 'State Funds Tutorial Delaware: Registering As A Property Locator For The State '
               'Of Delaware. (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=TTfaOSBvLDc&t=475s',
      'video_id': 'TTfaOSBvLDc'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:15](https://www.youtube.com/watch?v=d5TLZqkPX14&t=435s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'On the auction list are properties that the property owner has forfeited. You '
              "see, if you don't pay your property tax, you automatically forfeit your "
              'privilege to have property in that county.',
      'timestamp': 435,
      'timestamp_label': '[00:07:15]',
      'timestamp_seconds': 435,
      'tip': 'On the auction list are properties that the property owner has forfeited. You '
             "see, if you don't pay your property tax, you automatically forfeit your "
             'privilege to have property in that county.',
      'title': 'How To Claim Tax Sale Overages (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=d5TLZqkPX14&t=435s',
      'video_id': 'd5TLZqkPX14'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=124s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'We were able to find that this property did sell for more, okay? The county '
              'provides the excess proceeds list. Excess Elite provided the lead with all the '
              'skip tracing, and then we were able to go in and perform our due diligence.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'We were able to find that this property did sell for more, okay? The county '
             'provides the excess proceeds list. Excess Elite provided the lead with all the '
             'skip tracing, and then we were able to go in and perform our due diligence.',
      'title': 'Amador county Tax Sale Surplus Funds Case Study (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=124s',
      'video_id': '4-lZwuXtY6Y'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:09](https://www.youtube.com/watch?v=W-FX20iI9Jk&t=909s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': 'And then I want you to look at when was the the last deed recorded. So, you '
              'know, was it last year? And then I want you to look at that actual deed. This '
              'is going to go into your clerk court, your public records.',
      'timestamp': 909,
      'timestamp_label': '[00:15:09]',
      'timestamp_seconds': 909,
      'tip': 'And then I want you to look at when was the the last deed recorded. So, you '
             'know, was it last year? And then I want you to look at that actual deed. This is '
             'going to go into your clerk court, your public records.',
      'title': 'How to Get Your First Curative Title Deal: A Step-by-Step Guide (Courtney '
               'Fricke)',
      'url': 'https://www.youtube.com/watch?v=W-FX20iI9Jk&t=909s',
      'video_id': 'W-FX20iI9Jk'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:52](https://www.youtube.com/watch?v=q2gk3WmK5xs&t=232s)',
      'relevance': 'Attributed practitioner commentary on county surplus list sourcing, '
                   'FOIA/public-records requests, and pre-outreach deal qualification '
                   'thresholds.',
      'source_type': 'video_pro_tip',
      'text': "Option B is manual lead generation. If you're starting out and can't spend much "
              'money yet, this is your route. First of all, go to your browser and search for '
              'the excess proceeds list for the respective county.',
      'timestamp': 232,
      'timestamp_label': '[00:03:52]',
      'timestamp_seconds': 232,
      'tip': "Option B is manual lead generation. If you're starting out and can't spend much "
             'money yet, this is your route. First of all, go to your browser and search for '
             'the excess proceeds list for the respective county.',
      'title': 'The Most Overlooked Surplus Funds Recovery Business You Can Start With $0 '
               '(Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=q2gk3WmK5xs&t=232s',
      'video_id': 'q2gk3WmK5xs'}],
 7: [{'author': 'Dreams & Dollars: The Everyday Entrepreneur',
      'channel': 'Dreams & Dollars: The Everyday Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=pSC1FfAjNuo&t=225s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'Step eight, receive funds via check or a once approved. Pro tip, include a copy '
              'of the deed or title report tying you to the property at the time of sale. If '
              'the owner passed away, heirs may claim be ready to show probate or airship '
              'documentation.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'Step eight, receive funds via check or a once approved. Pro tip, include a copy '
             'of the deed or title report tying you to the property at the time of sale. If '
             'the owner passed away, heirs may claim be ready to show probate or airship '
             'documentation.',
      'title': 'Beginners Guide to Surplus Funds: How to Claim Money After Foreclosure- '
               'Step-by-Step Tutorial (Dreams & Dollars: The Everyday Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=pSC1FfAjNuo&t=225s',
      'video_id': 'pSC1FfAjNuo'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:32](https://www.youtube.com/watch?v=7AHHRIbWG80&t=272s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': "So, this isn't a legal motion or filing. It's simply us representing the client "
              "as a limited power of attorney. We're inquiring and confirming the surplus. "
              "We're filling out the claim form, things of that nature, and we get paid for "
              'our services.',
      'timestamp': 272,
      'timestamp_label': '[00:04:32]',
      'timestamp_seconds': 272,
      'tip': "So, this isn't a legal motion or filing. It's simply us representing the client "
             "as a limited power of attorney. We're inquiring and confirming the surplus. "
             "We're filling out the claim form, things of that nature, and we get paid for our "
             'services.',
      'title': 'Surplus Funds Case Study Texas Mortgage Foreclosure (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=7AHHRIbWG80&t=272s',
      'video_id': '7AHHRIbWG80'},
     {'author': 'Noble Notary & Legal Document Preparers',
      'channel': 'Noble Notary & Legal Document Preparers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=DM0kjEZlbSk&t=234s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': "What's the current amount owed today? Are there specific attorney fees or "
              'interest or costs due? Now, on the flip side, if you check former title holder, '
              'you need to state exactly how you acquired the property in the first place. Was '
              'it a deed, a court judgment?',
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': "What's the current amount owed today? Are there specific attorney fees or "
             'interest or costs due? Now, on the flip side, if you check former title holder, '
             'you need to state exactly how you acquired the property in the first place. Was '
             'it a deed, a court judgment?',
      'title': 'Florida Tax Deed Surplus Claim Forms:  How to Claim Excess Funds (Noble Notary '
               '& Legal Document Preparers)',
      'url': 'https://www.youtube.com/watch?v=DM0kjEZlbSk&t=234s',
      'video_id': 'DM0kjEZlbSk'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:44](https://www.youtube.com/watch?v=W5g3Gia5jX4&t=404s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'I often want to provide a solution because plenty of times you have people in '
              'the industry who either the person in industry themselves has given up on a '
              "file or their client has given up. For example, maybe it's a probate attorney "
              'who is dealing with fighting heirs.',
      'timestamp': 404,
      'timestamp_label': '[00:06:44]',
      'timestamp_seconds': 404,
      'tip': 'I often want to provide a solution because plenty of times you have people in '
             'the industry who either the person in industry themselves has given up on a file '
             "or their client has given up. For example, maybe it's a probate attorney who is "
             'dealing with fighting heirs.',
      'title': 'How I Actually Find Curative Title Leads (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=W5g3Gia5jX4&t=404s',
      'video_id': 'W5g3Gia5jX4'},
     {'author': 'AFX Research LLC',
      'channel': 'AFX Research LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=73s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'So how do you find out if a property has liens in Texas? Start with the County '
              "Clerk's Office. Every county in Texas maintains property records — deeds, lien "
              'documents, easements, and the full chain of title.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'So how do you find out if a property has liens in Texas? Start with the County '
             "Clerk's Office. Every county in Texas maintains property records — deeds, lien "
             'documents, easements, and the full chain of title.',
      'title': 'HOW TO FIND LIENS & TITLE SEARCH IN TEXAS (AFX Research LLC)',
      'url': 'https://www.youtube.com/watch?v=HPyO3dkjbCQ&t=73s',
      'video_id': 'HPyO3dkjbCQ'},
     {'author': 'ohiocommerce',
      'channel': 'ohiocommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:07](https://www.youtube.com/watch?v=8nmo4S1v3Co&t=847s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'She forgot that she had to submit these documents to us. She got an email after '
              '30 days. Our email said, "Hey, Maryanne, we need you to provide some documents '
              'uh in order to complete your claim." And so Maryanne\'s story is to be '
              'continued.',
      'timestamp': 847,
      'timestamp_label': '[00:14:07]',
      'timestamp_seconds': 847,
      'tip': 'She forgot that she had to submit these documents to us. She got an email after '
             '30 days. Our email said, "Hey, Maryanne, we need you to provide some documents '
             'uh in order to complete your claim." And so Maryanne\'s story is to be '
             'continued.',
      'title': 'Ohio Unclaimed Funds: How to Claim Your Cash in 3 Steps (HB 96 Deadline '
               'Explained) Webinar 2-5-2026 (ohiocommerce)',
      'url': 'https://www.youtube.com/watch?v=8nmo4S1v3Co&t=847s',
      'video_id': '8nmo4S1v3Co'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:37](https://www.youtube.com/watch?v=AAF69oF79DU&t=277s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': "Tenants in common or some other form of title. You may have probate step mom's "
              "estate to get it to dad's estate and then probate that estate. So what her "
              'attorney has told her is that there was rights of survivorship.',
      'timestamp': 277,
      'timestamp_label': '[00:04:37]',
      'timestamp_seconds': 277,
      'tip': "Tenants in common or some other form of title. You may have probate step mom's "
             "estate to get it to dad's estate and then probate that estate. So what her "
             'attorney has told her is that there was rights of survivorship.',
      'title': 'Sub-to strategy for probate investing | Probate foreclosures | Probate real '
               'estate marketing tips (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=AAF69oF79DU&t=277s',
      'video_id': 'AAF69oF79DU'},
     {'author': 'My Lawyer In Spain',
      'channel': 'My Lawyer In Spain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:12](https://www.youtube.com/watch?v=ywaYY4cPtAY&t=852s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': "They won't release it to the beneficiary or to the cousin but to the the "
              "lawyer. You've got to prove that you've actually got a legal interest in the "
              'case in order to to receive a copy of that will. Um, wills are private '
              'documents here.',
      'timestamp': 852,
      'timestamp_label': '[00:14:12]',
      'timestamp_seconds': 852,
      'tip': "They won't release it to the beneficiary or to the cousin but to the the lawyer. "
             "You've got to prove that you've actually got a legal interest in the case in "
             'order to to receive a copy of that will. Um, wills are private documents here.',
      'title': 'Unclaimed Estates & Abandoned Properties in Spain - tracing Heirs Worldwide '
               '(My Lawyer In Spain)',
      'url': 'https://www.youtube.com/watch?v=ywaYY4cPtAY&t=852s',
      'video_id': 'ywaYY4cPtAY'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:08](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=608s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': "'s how you actually claim surplus funds for heirs. For starters, you need the "
              'death certificate. You can get that from county records, or you can use a '
              '[snorts] site called VitalChek. You also need proof that your client is the '
              'rightful heir.',
      'timestamp': 608,
      'timestamp_label': '[00:10:08]',
      'timestamp_seconds': 608,
      'tip': "'s how you actually claim surplus funds for heirs. For starters, you need the "
             'death certificate. You can get that from county records, or you can use a '
             '[snorts] site called VitalChek. You also need proof that your client is the '
             'rightful heir.',
      'title': 'Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=608s',
      'video_id': 'MVCNlj7HQBQ'},
     {'author': 'William Whitman, Esquire',
      'channel': 'William Whitman, Esquire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=0xk7lNvAgn0&t=85s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'Entity it is where it was formed and an address so if we wanted to look at '
              'additional information the actual file we could request those documents and we '
              "could see what additional filings there were in this case there's only an "
              'initial filing.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Entity it is where it was formed and an address so if we wanted to look at '
             'additional information the actual file we could request those documents and we '
             "could see what additional filings there were in this case there's only an "
             'initial filing.',
      'title': 'Will Whitman, Esquire explains how to locate companies owed surplus funds '
               '(William Whitman, Esquire)',
      'url': 'https://www.youtube.com/watch?v=0xk7lNvAgn0&t=85s',
      'video_id': '0xk7lNvAgn0'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:40](https://www.youtube.com/watch?v=v0-thxE7IK4&t=400s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'Is there a filing deadline? Who has the legal right to claim these funds? Which '
              'can get genuinely complicated when the original owner has passed away. Then, it '
              'becomes a question about the heirs. This is where people get hurt.',
      'timestamp': 400,
      'timestamp_label': '[00:06:40]',
      'timestamp_seconds': 400,
      'tip': 'Is there a filing deadline? Who has the legal right to claim these funds? Which '
             'can get genuinely complicated when the original owner has passed away. Then, it '
             'becomes a question about the heirs. This is where people get hurt.',
      'title': 'How To Find Surplus Funds Lists In 2026 (For Free) (Surplus Funds Secrets)',
      'url': 'https://www.youtube.com/watch?v=v0-thxE7IK4&t=400s',
      'video_id': 'v0-thxE7IK4'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:21](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=681s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': '" And the real opportunity is to figure out whether that problem can be solved. '
              'And again, that involves understanding and skill. So, one of the documents that '
              'frequently appears when ownership gets messy is a quick claim deed.',
      'timestamp': 681,
      'timestamp_label': '[00:11:21]',
      'timestamp_seconds': 681,
      'tip': '" And the real opportunity is to figure out whether that problem can be solved. '
             'And again, that involves understanding and skill. So, one of the documents that '
             'frequently appears when ownership gets messy is a quick claim deed.',
      'title': '5 Curative Title Terms Every Investor Should Understand (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=sf2hUucsNZ8&t=681s',
      'video_id': 'sf2hUucsNZ8'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:09](https://www.youtube.com/watch?v=onebNbNQSBM&t=1749s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'One of the reasons I dislike probate states more than I like affidavit of '
              "heirship states is because there's a process you have to go through. If I make "
              'an agreement with someone, it sounds crazy, but if I make an agreement at 8:00 '
              'a. I can have them closed by 5:00 p.',
      'timestamp': 1749,
      'timestamp_label': '[00:29:09]',
      'timestamp_seconds': 1749,
      'tip': 'One of the reasons I dislike probate states more than I like affidavit of '
             "heirship states is because there's a process you have to go through. If I make "
             'an agreement with someone, it sounds crazy, but if I make an agreement at 8:00 '
             'a. I can have them closed by 5:00 p.',
      'title': 'Curative Title Explained by a Florida Probate Attorney (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=onebNbNQSBM&t=1749s',
      'video_id': 'onebNbNQSBM'},
     {'author': 'claimtaxsaleoverages',
      'channel': 'claimtaxsaleoverages',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=e309errLsBw&t=137s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'Properties with unpaid taxes are sold to recover the owed amounts deadline for '
              'reclaiming funds this refers to the specific time frame within which you must '
              'file a claim to recover your overages if you miss this deadline you may forfeit '
              'your right to reclaim the funds.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'Properties with unpaid taxes are sold to recover the owed amounts deadline for '
             'reclaiming funds this refers to the specific time frame within which you must '
             'file a claim to recover your overages if you miss this deadline you may forfeit '
             'your right to reclaim the funds.',
      'title': 'Claim Tax Sale Overages/Surplus Funds - Step-by-Step Guide '
               '(claimtaxsaleoverages)',
      'url': 'https://www.youtube.com/watch?v=e309errLsBw&t=137s',
      'video_id': 'e309errLsBw'},
     {'author': 'Tax Deed Surplus & Lien-Research Records',
      'channel': 'Tax Deed Surplus & Lien-Research Records',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=y94Ncg0WHn0&t=130s)',
      'relevance': 'Attributed practitioner commentary on title-chain verification, '
                   'probate/heirship proof, claim dossiers, and judicial motion handoffs with '
                   'licensed counsel.',
      'source_type': 'video_pro_tip',
      'text': 'And also, this is the same page where you would do the taxdeed research where '
              'you can see the documents for the sale. So for this one for example, I would '
              'just click view and you can go through and and see all the documents from that '
              'tax deed option.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'And also, this is the same page where you would do the taxdeed research where '
             'you can see the documents for the sale. So for this one for example, I would '
             'just click view and you can go through and and see all the documents from that '
             'tax deed option.',
      'title': 'Polk County Tax Deed Surplus (Tax Deed Surplus & Lien-Research Records)',
      'url': 'https://www.youtube.com/watch?v=y94Ncg0WHn0&t=130s',
      'video_id': 'y94Ncg0WHn0'}],
 8: [{'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:09](https://www.youtube.com/watch?v=q2gk3WmK5xs&t=249s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'To track these individuals from a parcel number, you would need skip tracing '
              'tools like True People Search, been verified, and Intellius. If you want to '
              'learn more about it, watch the video linked in the description.',
      'timestamp': 249,
      'timestamp_label': '[00:04:09]',
      'timestamp_seconds': 249,
      'tip': 'To track these individuals from a parcel number, you would need skip tracing '
             'tools like True People Search, been verified, and Intellius. If you want to '
             'learn more about it, watch the video linked in the description.',
      'title': 'The Most Overlooked Surplus Funds Recovery Business You Can Start With $0 '
               '(Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=q2gk3WmK5xs&t=249s',
      'video_id': 'q2gk3WmK5xs'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=suJSu-vn6yI&t=426s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'The best option is to use Excess Leads, which is the best software in the game. '
              'You can get daily leads across the entire country, both tax sales and mortgage '
              'foreclosures, and every lead comes with skip trace phone numbers, DNC '
              'compliance, relatives numbers, and emails.',
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': 'The best option is to use Excess Leads, which is the best software in the game. '
             'You can get daily leads across the entire country, both tax sales and mortgage '
             'foreclosures, and every lead comes with skip trace phone numbers, DNC '
             'compliance, relatives numbers, and emails.',
      'title': 'How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=suJSu-vn6yI&t=426s',
      'video_id': 'suJSu-vn6yI'},
     {'author': 'Nick Fullmer- Overage Syndicate',
      'channel': 'Nick Fullmer- Overage Syndicate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=KOYBZFn2k7w&t=323s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'Third thing you could do is actually call the county recorder, give them the '
              'property address, give them the parcel number, and see if they will do a due '
              "diligence search for you. If it's just one case, just one-off case you're "
              'looking at, they might do that for you as well.',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': 'Third thing you could do is actually call the county recorder, give them the '
             'property address, give them the parcel number, and see if they will do a due '
             "diligence search for you. If it's just one case, just one-off case you're "
             'looking at, they might do that for you as well.',
      'title': 'Overages & Surplus Fund Debt & Title Research: Not As Easy As It Seems.  Two '
               'tips To Help (Nick Fullmer- Overage Syndicate)',
      'url': 'https://www.youtube.com/watch?v=KOYBZFn2k7w&t=323s',
      'video_id': 'KOYBZFn2k7w'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:51](https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=1131s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': "I mean, you could skip trace anybody. We've got people that are doing um What "
              'is it? Unclaimed funds, uh debt collection, some property managers that deal '
              "with evictions, um just stuff Any It It's skip tracing skip tracing.",
      'timestamp': 1131,
      'timestamp_label': '[00:18:51]',
      'timestamp_seconds': 1131,
      'tip': "I mean, you could skip trace anybody. We've got people that are doing um What is "
             'it? Unclaimed funds, uh debt collection, some property managers that deal with '
             "evictions, um just stuff Any It It's skip tracing skip tracing.",
      'title': "Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer)",
      'url': 'https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=1131s',
      'video_id': 'dJ-LTFmMsTg'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=250s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'Think about your own phone. How many unknown calls do you answer on the first '
              'try? So why would your client be any different? One call is not an attempt, but '
              "three touches is a real attempt. And don't stop with the client. Your skip "
              'trace also gives you a few relatives.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'Think about your own phone. How many unknown calls do you answer on the first '
             'try? So why would your client be any different? One call is not an attempt, but '
             "three touches is a real attempt. And don't stop with the client. Your skip trace "
             'also gives you a few relatives.',
      'title': 'Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=DMdtmrWAO6c&t=250s',
      'video_id': 'DMdtmrWAO6c'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=YCb5jYZX_A8&t=254s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'From there, the real research starts. Court records, second mortgages, other '
              "liens, back taxes, the cost of the sale, figuring out who's actually entitled "
              "to what's left, then skip tracing to find a current phone number for the "
              'homeowner or the heirs.',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': 'From there, the real research starts. Court records, second mortgages, other '
             "liens, back taxes, the cost of the sale, figuring out who's actually entitled to "
             "what's left, then skip tracing to find a current phone number for the homeowner "
             'or the heirs.',
      'title': 'How to Find Surplus Funds Lists (Tax Sales and Foreclosures) (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=YCb5jYZX_A8&t=254s',
      'video_id': 'YCb5jYZX_A8'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:47](https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=227s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'Skip trace those people and see if they have a relationship with the owner. '
              "Depending on the skip tracing platform, you can even get somebody's driver's "
              'license number and then you can send a sheriff to their property to do a quote '
              'unquote welfare checkup.',
      'timestamp': 227,
      'timestamp_label': '[00:03:47]',
      'timestamp_seconds': 227,
      'tip': 'Skip trace those people and see if they have a relationship with the owner. '
             "Depending on the skip tracing platform, you can even get somebody's driver's "
             'license number and then you can send a sheriff to their property to do a quote '
             'unquote welfare checkup.',
      'title': 'Unclaimed Funds: Lead Sourcing Masterclass (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=227s',
      'video_id': 'h4Qz3EvAAnw'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=205s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': "'s left over, like this list that has probably 50 leads on it, $3,341,087. Once "
              'you get the list, then what you have to do is learn how to get the contact '
              "information for the people. That's a process called skip tracing.",
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': "'s left over, like this list that has probably 50 leads on it, $3,341,087. Once "
             'you get the list, then what you have to do is learn how to get the contact '
             "information for the people. That's a process called skip tracing.",
      'title': "Tax Sale Overages Course (Bob Diamond - America's Tax Sale Attorney)",
      'url': 'https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=205s',
      'video_id': 'qGPsbhsEAVQ'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:21](https://www.youtube.com/watch?v=xqpLsq3JVlU&t=1101s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'Landlines almost never work on any skip tracing service, but the older you get, '
              'the more the landline will work. The guy is 76, so he probably does have a '
              "couple of land. Um, it's po I'm sorry, let me say that again. It's possible "
              'that his landline does work.',
      'timestamp': 1101,
      'timestamp_label': '[00:18:21]',
      'timestamp_seconds': 1101,
      'tip': 'Landlines almost never work on any skip tracing service, but the older you get, '
             'the more the landline will work. The guy is 76, so he probably does have a '
             "couple of land. Um, it's po I'm sorry, let me say that again. It's possible that "
             'his landline does work.',
      'title': 'Cold Calling for Surplus Funds: What Actually Works (Surplus Institute / David '
               'Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=xqpLsq3JVlU&t=1101s',
      'video_id': 'xqpLsq3JVlU'},
     {'author': 'Surplus Funds List',
      'channel': 'Surplus Funds List',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:10](https://www.youtube.com/watch?v=lOnYUxDdOdI&t=250s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'You can uh also update the status on the client portal so the homeowner can go '
              'on your site and search for the case and they will see the detail as to what is '
              'the progress on the case without waiting on you um to get them an update.',
      'timestamp': 250,
      'timestamp_label': '[00:04:10]',
      'timestamp_seconds': 250,
      'tip': 'You can uh also update the status on the client portal so the homeowner can go '
             'on your site and search for the case and they will see the detail as to what is '
             'the progress on the case without waiting on you um to get them an update.',
      'title': 'How to Run a Surplus Funds Business with One CRM: Full 2026 Walkthrough '
               '(Surplus Funds List)',
      'url': 'https://www.youtube.com/watch?v=lOnYUxDdOdI&t=250s',
      'video_id': 'lOnYUxDdOdI'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=bpxSOg1_xbE&t=157s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'So, always check if a claim has already been filed before. Some counties have '
              'online portals where you can search by case number or property address, or you '
              'can always make a phone call to the county office and verify.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'So, always check if a claim has already been filed before. Some counties have '
             'online portals where you can search by case number or property address, or you '
             'can always make a phone call to the county office and verify.',
      'title': 'Top 5 Things Nobody Tells You About the Surplus Funds Recovery Business '
               '(Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=bpxSOg1_xbE&t=157s',
      'video_id': 'bpxSOg1_xbE'},
     {'author': 'PA Treasury Department',
      'channel': 'PA Treasury Department',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:33](https://www.youtube.com/watch?v=eRjGqaIOHWI&t=453s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': 'Email topmail patreasury.gov and our unclaimed property staff will be happy to '
              "assist you if you'd like to search for unclaimed property in other states visit "
              'missingmoney.com thank.',
      'timestamp': 453,
      'timestamp_label': '[00:07:33]',
      'timestamp_seconds': 453,
      'tip': 'Email topmail patreasury.gov and our unclaimed property staff will be happy to '
             "assist you if you'd like to search for unclaimed property in other states visit "
             'missingmoney.com thank.',
      'title': 'How To File a Claim - PA Treasury Unclaimed Property Tutorial (PA Treasury '
               'Department)',
      'url': 'https://www.youtube.com/watch?v=eRjGqaIOHWI&t=453s',
      'video_id': 'eRjGqaIOHWI'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:18](https://www.youtube.com/watch?v=8-8koApqnYA&t=558s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': "Their page says email the court registry to request a listing. And there's a $5 "
              'research fee to look up a case by phone. So once you have your list, you find '
              "the people, you're gonna skip trace them, look for heirs where the owner has "
              'passed and build a short list.',
      'timestamp': 558,
      'timestamp_label': '[00:09:18]',
      'timestamp_seconds': 558,
      'tip': "Their page says email the court registry to request a listing. And there's a $5 "
             'research fee to look up a case by phone. So once you have your list, you find '
             "the people, you're gonna skip trace them, look for heirs where the owner has "
             'passed and build a short list.',
      'title': 'How to Start a Surplus Funds Business in 2026 (Step by Step) (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=8-8koApqnYA&t=558s',
      'video_id': '8-8koApqnYA'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=zMW-iFWYX9w&t=283s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': "And when you when a person thinks, I'm going to skip trace someone and say, all "
              "right, I'm going to skip trace, I don't know, Aaron Rodgers. You go you put the "
              'name in the first field. Aaron first name or last name last name first, '
              'whatever.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': "And when you when a person thinks, I'm going to skip trace someone and say, all "
             "right, I'm going to skip trace, I don't know, Aaron Rodgers. You go you put the "
             'name in the first field. Aaron first name or last name last name first, '
             'whatever.',
      'title': 'Curative Title Research: How She Finds Missing Owners (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=zMW-iFWYX9w&t=283s',
      'video_id': 'zMW-iFWYX9w'},
     {'author': 'Emend The Mass Media Group',
      'channel': 'Emend The Mass Media Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:01](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=961s)',
      'relevance': 'Attributed practitioner commentary on skip-tracing stacks, '
                   'recorder/assessor portals, PACER bankruptcy checks, and right-party '
                   'contact verification.',
      'source_type': 'video_pro_tip',
      'text': "So, you're going to go ahead and select that or probably like push it or "
              "something like that. So, you're going to push that option and it's going to "
              'take you uh to a search page.',
      'timestamp': 961,
      'timestamp_label': '[00:16:01]',
      'timestamp_seconds': 961,
      'tip': "So, you're going to go ahead and select that or probably like push it or "
             "something like that. So, you're going to push that option and it's going to take "
             'you uh to a search page.',
      'title': 'CA Unclaimed Property - Are you missing out? - Tutorial (Emend The Mass Media '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=ijLtjR0tTd8&t=961s',
      'video_id': 'ijLtjR0tTd8'}],
 9: [{'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=alaKJIcbbLw&t=252s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "You've got to have your script down. The last thing, and the majority of my "
              'business, if you really want to know, comes from people calling me back cuz '
              "most people won't pick up their phone. And again, that's a common objection I "
              'hear. So, I do leave a detailed message.',
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': "You've got to have your script down. The last thing, and the majority of my "
             'business, if you really want to know, comes from people calling me back cuz most '
             "people won't pick up their phone. And again, that's a common objection I hear. "
             'So, I do leave a detailed message.',
      'title': 'Cold Calling for Surplus Funds in 2025: The Script That Actually Works! '
               '(Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=alaKJIcbbLw&t=252s',
      'video_id': 'alaKJIcbbLw'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:02](https://www.youtube.com/watch?v=smhFDkvMwkM&t=242s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "And when is a good time for a Zoom or a phone call? 's something about being "
              "able to see the other person you're talking to that just gives you an extra "
              "level of credibility and trust, so I always shoot for a Zoom call, and that's "
              'the second.',
      'timestamp': 242,
      'timestamp_label': '[00:04:02]',
      'timestamp_seconds': 242,
      'tip': "And when is a good time for a Zoom or a phone call? 's something about being "
             "able to see the other person you're talking to that just gives you an extra "
             "level of credibility and trust, so I always shoot for a Zoom call, and that's "
             'the second.',
      'title': 'Best Cold Calling Script For Surplus Funds. overage syndicate surplus funds '
               'cold calling (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=smhFDkvMwkM&t=242s',
      'video_id': 'smhFDkvMwkM'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=Zh5fus4SGzc&t=163s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "We do have a power dialer on XS Elite and that's when you're calling each "
              "number one by one. So it's not just auto blast calling. Everybody is just "
              "calling one by one so we're in compliance. So I had the attorney that "
              'specializes in TCPA and DNC.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': "We do have a power dialer on XS Elite and that's when you're calling each number "
             "one by one. So it's not just auto blast calling. Everybody is just calling one "
             "by one so we're in compliance. So I had the attorney that specializes in TCPA "
             'and DNC.',
      'title': 'What Nobody Tells You About The Surplus Funds Recovery Business (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=Zh5fus4SGzc&t=163s',
      'video_id': 'Zh5fus4SGzc'},
     {'author': 'Alfred Taren',
      'channel': 'Alfred Taren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=CqlbwGPmv64&t=70s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': 'And if somebody asks you not to call again, make a note and just stop calling. '
              "Don't use robocalls or autodialers on cell phones without the right permission. "
              "And in some places, there's a waiting period after the sale before you're "
              'allowed to contact the owner.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'And if somebody asks you not to call again, make a note and just stop calling. '
             "Don't use robocalls or autodialers on cell phones without the right permission. "
             "And in some places, there's a waiting period after the sale before you're "
             'allowed to contact the owner.',
      'title': 'Surplus Funds Cold Calling Script: How to Not Sound Like a Scam (Alfred Taren)',
      'url': 'https://www.youtube.com/watch?v=CqlbwGPmv64&t=70s',
      'video_id': 'CqlbwGPmv64'},
     {'author': "Bob Diamond - America's Tax Sale Attorney",
      'channel': "Bob Diamond - America's Tax Sale Attorney",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:28](https://www.youtube.com/watch?v=1Pp-cjYnY2k&t=328s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': 'You get their contact information and you reach out to them. You might be '
              'sending them a letter. You might be picking up the phone and calling them. You '
              'might be sending them a message on Facebook. The ways that we can get '
              'information these days — very easy.',
      'timestamp': 328,
      'timestamp_label': '[00:05:28]',
      'timestamp_seconds': 328,
      'tip': 'You get their contact information and you reach out to them. You might be '
             'sending them a letter. You might be picking up the phone and calling them. You '
             'might be sending them a message on Facebook. The ways that we can get '
             'information these days — very easy.',
      'title': "How To Become A Surplus Funds Recovery Agent (Bob Diamond - America's Tax Sale "
               'Attorney)',
      'url': 'https://www.youtube.com/watch?v=1Pp-cjYnY2k&t=328s',
      'video_id': '1Pp-cjYnY2k'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:53](https://www.youtube.com/watch?v=zMW-iFWYX9w&t=2633s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "And we didn't know, you know, any of this until now. So, then um we realized "
              "Larry that the the dad's friend assigned their purchase agreement. I said, hey, "
              'he only has limited power of attorney for the insurance claim, not to sign the '
              'real the real estate.',
      'timestamp': 2633,
      'timestamp_label': '[00:43:53]',
      'timestamp_seconds': 2633,
      'tip': "And we didn't know, you know, any of this until now. So, then um we realized "
             "Larry that the the dad's friend assigned their purchase agreement. I said, hey, "
             'he only has limited power of attorney for the insurance claim, not to sign the '
             'real the real estate.',
      'title': 'Curative Title Research: How She Finds Missing Owners (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=zMW-iFWYX9w&t=2633s',
      'video_id': 'zMW-iFWYX9w'},
     {'author': 'Dexter Brown',
      'channel': 'Dexter Brown',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:14](https://www.youtube.com/watch?v=0FZrtOY2H5w&t=434s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': 'You want to be a part of this you can just have discussion with them or we can '
              "hop on the three-way phone call and I can kind of go over it again um but we'll "
              'need them to sign for the small succession okay gotcha.',
      'timestamp': 434,
      'timestamp_label': '[00:07:14]',
      'timestamp_seconds': 434,
      'tip': 'You want to be a part of this you can just have discussion with them or we can '
             "hop on the three-way phone call and I can kind of go over it again um but we'll "
             'need them to sign for the small succession okay gotcha.',
      'title': 'Live Call with client DEAL CLOSED | Surplus Funds Excess Funds Overages '
               '(Dexter Brown)',
      'url': 'https://www.youtube.com/watch?v=0FZrtOY2H5w&t=434s',
      'video_id': '0FZrtOY2H5w'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=i7mng3-o1u0&t=28s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "Where are you calling from? Why wouldn't the county call me if there's money "
              'for me? Why would there be money for me? " That\'s the psychology that they\'re '
              "going to be dealing with right off the bat, especially if they don't know about "
              'these funds.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "Where are you calling from? Why wouldn't the county call me if there's money for "
             'me? Why would there be money for me? " That\'s the psychology that they\'re '
             "going to be dealing with right off the bat, especially if they don't know about "
             'these funds.',
      'title': 'Avoid These Mistakes In Surplus Funds Cold Calling (Surplus Funds Secrets)',
      'url': 'https://www.youtube.com/watch?v=i7mng3-o1u0&t=28s',
      'video_id': 'i7mng3-o1u0'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=72s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "I'm giving you my entire cold calling system. First, how to find the phone "
              'numbers that actually work because most people fail before they even dial. '
              'Second, the exact call flow that my team uses word for word. And third, how to '
              'handle the rebuttals that kill most beginners.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': "I'm giving you my entire cold calling system. First, how to find the phone "
             'numbers that actually work because most people fail before they even dial. '
             'Second, the exact call flow that my team uses word for word. And third, how to '
             'handle the rebuttals that kill most beginners.',
      'title': 'Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=DMdtmrWAO6c&t=72s',
      'video_id': 'DMdtmrWAO6c'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:25](https://www.youtube.com/watch?v=_RTcaTMOwlY&t=325s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "'s kind of pull the curtain back a little bit more and look at this thing from "
              "the 5,000-ft view, right? Contract that you're going to have people sign, we "
              "call it an an agreement. A contract's a scary trigger word.",
      'timestamp': 325,
      'timestamp_label': '[00:05:25]',
      'timestamp_seconds': 325,
      'tip': "'s kind of pull the curtain back a little bit more and look at this thing from "
             "the 5,000-ft view, right? Contract that you're going to have people sign, we "
             "call it an an agreement. A contract's a scary trigger word.",
      'title': 'Mastering Unclaimed Funds Contracts: A Complete Beginners Guide (Surplus Funds '
               '101)',
      'url': 'https://www.youtube.com/watch?v=_RTcaTMOwlY&t=325s',
      'video_id': '_RTcaTMOwlY'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:27](https://www.youtube.com/watch?v=MsxVzoHQCNk&t=567s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "Many you know how many claims are in here and and it's just it's really nice "
              "plus I'm helping out a family which I love too so I'm helping someone I'm "
              'getting help in the process and this is great this is the perfect phone call '
              "I'm looking right now.",
      'timestamp': 567,
      'timestamp_label': '[00:09:27]',
      'timestamp_seconds': 567,
      'tip': "Many you know how many claims are in here and and it's just it's really nice "
             "plus I'm helping out a family which I love too so I'm helping someone I'm "
             "getting help in the process and this is great this is the perfect phone call I'm "
             'looking right now.',
      'title': 'Surplus Funds The PERFECT Cold Call! (Surplus Institute / David Church / '
               'Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=MsxVzoHQCNk&t=567s',
      'video_id': 'MsxVzoHQCNk'},
     {'author': 'SurplusFundsRiches',
      'channel': 'SurplusFundsRiches',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:24](https://www.youtube.com/watch?v=4W8c0I28pxQ&t=1524s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': 'Usually use an attachment for that so now we know when I bought it now what '
              "about debt well that's just as easy what we see next or rather same day is this "
              'again we have a d this is called a deed of trust let me move this a little bit.',
      'timestamp': 1524,
      'timestamp_label': '[00:25:24]',
      'timestamp_seconds': 1524,
      'tip': 'Usually use an attachment for that so now we know when I bought it now what '
             "about debt well that's just as easy what we see next or rather same day is this "
             'again we have a d this is called a deed of trust let me move this a little bit.',
      'title': 'Free Surplus Funds Training - Indepth, full hour! SurplusFundsRiches '
               '(SurplusFundsRiches)',
      'url': 'https://www.youtube.com/watch?v=4W8c0I28pxQ&t=1524s',
      'video_id': '4W8c0I28pxQ'},
     {'author': 'Nick Fullmer- Overage Syndicate',
      'channel': 'Nick Fullmer- Overage Syndicate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=vd__NHmQYgM&t=173s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "I think I've got eight under contract and like seven or eight contracts still "
              "out waiting to come back in. Now, that's with going to Montana in June and then "
              'my wife dragging me to Cape Cod in July for 10 days.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "I think I've got eight under contract and like seven or eight contracts still "
             "out waiting to come back in. Now, that's with going to Montana in June and then "
             'my wife dragging me to Cape Cod in July for 10 days.',
      'title': '8 Surplus Funds Deals Within 3 Months of Starting The Business (Nick Fullmer- '
               'Overage Syndicate)',
      'url': 'https://www.youtube.com/watch?v=vd__NHmQYgM&t=173s',
      'video_id': 'vd__NHmQYgM'},
     {'author': 'Surplus Funds Secrets',
      'channel': 'Surplus Funds Secrets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=HtbOqZK2He8&t=58s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': 'Surplus funds, they need clarity first. "I\'m reaching out about funds that may '
              'be owed to you or your family\'s estate. Is this a good time to talk?" '
              "Immediately frames the call. There's a real job to the person calling these "
              "individuals, and it's not sales right away.",
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'Surplus funds, they need clarity first. "I\'m reaching out about funds that may '
             'be owed to you or your family\'s estate. Is this a good time to talk?" '
             "Immediately frames the call. There's a real job to the person calling these "
             "individuals, and it's not sales right away.",
      'title': 'Why Most Surplus Funds Calls Fail (And What To Say Instead) (Surplus Funds '
               'Secrets)',
      'url': 'https://www.youtube.com/watch?v=HtbOqZK2He8&t=58s',
      'video_id': 'HtbOqZK2He8'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=GH5TN_iIdMs&t=142s)',
      'relevance': 'Attributed practitioner commentary on claimant outreach scripts, cold-call '
                   'objection handling, direct-mail packets, and statutory solicitation '
                   'disclosures.',
      'source_type': 'video_pro_tip',
      'text': "And so many investors are like, wait, I've kind of heard that word before in my "
              "contract where there's like that curative title phase. 's a part of like a an "
              'extension deadline or whatever with your tit like with your uh purchase '
              'agreement.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': "And so many investors are like, wait, I've kind of heard that word before in my "
             "contract where there's like that curative title phase. 's a part of like a an "
             'extension deadline or whatever with your tit like with your uh purchase '
             'agreement.',
      'title': 'Curative Title Explained: How Investors Make Money When Deals Can’t Close '
               '(Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=GH5TN_iIdMs&t=142s',
      'video_id': 'GH5TN_iIdMs'}],
 10: [{'author': 'BizMove',
       'channel': 'BizMove',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:00](https://www.youtube.com/watch?v=01plOr9pFjQ&t=180s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': 'If you want to generate custom queries or process large data files, tools like '
               'ChatGPT can assist in writing scripts or parsing data. For example, prompt: '
               '“Help me write a Python script to extract owner names and surplus amounts from '
               'a tax sale results PDF.',
       'timestamp': 180,
       'timestamp_label': '[00:03:00]',
       'timestamp_seconds': 180,
       'tip': 'If you want to generate custom queries or process large data files, tools like '
              'ChatGPT can assist in writing scripts or parsing data. For example, prompt: '
              '“Help me write a Python script to extract owner names and surplus amounts from '
              'a tax sale results PDF.',
       'title': 'How to Start a Tax Overage Business | Complete and Easy to Follow Guide '
                '(BizMove)',
       'url': 'https://www.youtube.com/watch?v=01plOr9pFjQ&t=180s',
       'video_id': '01plOr9pFjQ'},
      {'author': 'Surplus Funds List',
       'channel': 'Surplus Funds List',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:58](https://www.youtube.com/watch?v=lOnYUxDdOdI&t=178s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "That's all it takes to put the leads inside your workspace from our system. "
               "You don't have to download, you don't have to import back.",
       'timestamp': 178,
       'timestamp_label': '[00:02:58]',
       'timestamp_seconds': 178,
       'tip': "That's all it takes to put the leads inside your workspace from our system. You "
              "don't have to download, you don't have to import back.",
       'title': 'How to Run a Surplus Funds Business with One CRM: Full 2026 Walkthrough '
                '(Surplus Funds List)',
       'url': 'https://www.youtube.com/watch?v=lOnYUxDdOdI&t=178s',
       'video_id': 'lOnYUxDdOdI'},
      {'author': 'Dreams & Dollars: The Everyday Entrepreneur',
       'channel': 'Dreams & Dollars: The Everyday Entrepreneur',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:56](https://www.youtube.com/watch?v=pSC1FfAjNuo&t=116s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': 'You can also call the county clerk or trustee handling the sale. Search for '
               'reports of sale, case numbers, and any surplus notices tied to your address. '
               'Create a simple tracking sheet. Sale price, debt, the calculated surplus, and '
               'filing deadlines.',
       'timestamp': 116,
       'timestamp_label': '[00:01:56]',
       'timestamp_seconds': 116,
       'tip': 'You can also call the county clerk or trustee handling the sale. Search for '
              'reports of sale, case numbers, and any surplus notices tied to your address. '
              'Create a simple tracking sheet. Sale price, debt, the calculated surplus, and '
              'filing deadlines.',
       'title': 'Beginners Guide to Surplus Funds: How to Claim Money After Foreclosure- '
                'Step-by-Step Tutorial (Dreams & Dollars: The Everyday Entrepreneur)',
       'url': 'https://www.youtube.com/watch?v=pSC1FfAjNuo&t=116s',
       'video_id': 'pSC1FfAjNuo'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:26](https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=326s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': 'That same process doing it manually would take hours, probably days to do for '
               'the exact same amount of data. And so, I just like the speed the bulk leads '
               'give you. So those are the two big differences between the lead types.',
       'timestamp': 326,
       'timestamp_label': '[00:05:26]',
       'timestamp_seconds': 326,
       'tip': 'That same process doing it manually would take hours, probably days to do for '
              'the exact same amount of data. And so, I just like the speed the bulk leads '
              'give you. So those are the two big differences between the lead types.',
       'title': 'Unclaimed Funds: Lead Sourcing Masterclass (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=326s',
       'video_id': 'h4Qz3EvAAnw'},
      {'author': "Bob Diamond - America's Tax Sale Attorney",
       'channel': "Bob Diamond - America's Tax Sale Attorney",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=4O5XeYwMAts&t=66s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "You'll see all of those terms and just click on it. And typically there's "
               'either a PDF document or an Excel spreadsheet where it lists all the monies '
               "that they're holding, and that's the overages money.",
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': "You'll see all of those terms and just click on it. And typically there's "
              'either a PDF document or an Excel spreadsheet where it lists all the monies '
              "that they're holding, and that's the overages money.",
       'title': "How To Find Tax Sale Overages (Bob Diamond - America's Tax Sale Attorney)",
       'url': 'https://www.youtube.com/watch?v=4O5XeYwMAts&t=66s',
       'video_id': '4O5XeYwMAts'},
      {'author': 'Haynes Law Group',
       'channel': 'Haynes Law Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=Uj-vrJWHKQo&t=50s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': 'Um this is an old case but the surplus was just like I stated litigated last '
               "week and we so that was a you know we're in April of 2025. This is a case that "
               'was filed in 2011. Um at the time the case was filed in 2011, the city had a '
               'lean on the property.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'Um this is an old case but the surplus was just like I stated litigated last '
              "week and we so that was a you know we're in April of 2025. This is a case that "
              'was filed in 2011. Um at the time the case was filed in 2011, the city had a '
              'lean on the property.',
       'title': 'Florida Foreclosure Surplus Funds Update: What is a Subordinate Lien Holder? '
                '(Haynes Law Group)',
       'url': 'https://www.youtube.com/watch?v=Uj-vrJWHKQo&t=50s',
       'video_id': 'Uj-vrJWHKQo'},
      {'author': 'Nick Fullmer- Overage Syndicate',
       'channel': 'Nick Fullmer- Overage Syndicate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:34](https://www.youtube.com/watch?v=vd__NHmQYgM&t=694s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "And long story short, we ended up collecting on this lady's money. And, you "
               'know, that was a great case because she left she left us like a nice review. '
               'This was this was the review she left.',
       'timestamp': 694,
       'timestamp_label': '[00:11:34]',
       'timestamp_seconds': 694,
       'tip': "And long story short, we ended up collecting on this lady's money. And, you "
              'know, that was a great case because she left she left us like a nice review. '
              'This was this was the review she left.',
       'title': '8 Surplus Funds Deals Within 3 Months of Starting The Business (Nick Fullmer- '
                'Overage Syndicate)',
       'url': 'https://www.youtube.com/watch?v=vd__NHmQYgM&t=694s',
       'video_id': 'vd__NHmQYgM'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=W5g3Gia5jX4&t=54s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "'s talk about how deals come from one of three sources. So, the first source "
               "is data list. And when I talk about a data list, I'm talking like a "
               "spreadsheet of a lot of data that's, you know, you then have to sort through "
               'and then start getting in touch with those owners.',
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': "'s talk about how deals come from one of three sources. So, the first source is "
              "data list. And when I talk about a data list, I'm talking like a spreadsheet of "
              "a lot of data that's, you know, you then have to sort through and then start "
              'getting in touch with those owners.',
       'title': 'How I Actually Find Curative Title Leads (Courtney Fricke)',
       'url': 'https://www.youtube.com/watch?v=W5g3Gia5jX4&t=54s',
       'video_id': 'W5g3Gia5jX4'},
      {'author': 'Surplus Funds Secrets',
       'channel': 'Surplus Funds Secrets',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=HtbOqZK2He8&t=101s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "If a person hears foreclosure right off the bat, they usually think that's a "
               'bad thing. They think debt, case, courts, banks, nothing too positive for '
               "them. They pretty much think you're calling to collect money.",
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': "If a person hears foreclosure right off the bat, they usually think that's a "
              'bad thing. They think debt, case, courts, banks, nothing too positive for them. '
              "They pretty much think you're calling to collect money.",
       'title': 'Why Most Surplus Funds Calls Fail (And What To Say Instead) (Surplus Funds '
                'Secrets)',
       'url': 'https://www.youtube.com/watch?v=HtbOqZK2He8&t=101s',
       'video_id': 'HtbOqZK2He8'},
      {'author': 'ohiocommerce',
       'channel': 'ohiocommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:01](https://www.youtube.com/watch?v=8nmo4S1v3Co&t=541s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "'s been a great experience for everyone to be able to know where they are in "
               'the process. And with our new system, we have a new law that happened last '
               'year. You may have heard about it. And so what does that mean to you? This is '
               'a very important slide.',
       'timestamp': 541,
       'timestamp_label': '[00:09:01]',
       'timestamp_seconds': 541,
       'tip': "'s been a great experience for everyone to be able to know where they are in "
              'the process. And with our new system, we have a new law that happened last '
              'year. You may have heard about it. And so what does that mean to you? This is a '
              'very important slide.',
       'title': 'Ohio Unclaimed Funds: How to Claim Your Cash in 3 Steps (HB 96 Deadline '
                'Explained) Webinar 2-5-2026 (ohiocommerce)',
       'url': 'https://www.youtube.com/watch?v=8nmo4S1v3Co&t=541s',
       'video_id': '8nmo4S1v3Co'},
      {'author': 'Dexter Brown',
       'channel': 'Dexter Brown',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:48](https://www.youtube.com/watch?v=0FZrtOY2H5w&t=348s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "Actually look into the case because they can't legally start pulling dockets "
               "and all that stuff without you or some like a family member knowing so you'll "
               'be assigned on to say hey I acknowledge.',
       'timestamp': 348,
       'timestamp_label': '[00:05:48]',
       'timestamp_seconds': 348,
       'tip': "Actually look into the case because they can't legally start pulling dockets "
              "and all that stuff without you or some like a family member knowing so you'll "
              'be assigned on to say hey I acknowledge.',
       'title': 'Live Call with client DEAL CLOSED | Surplus Funds Excess Funds Overages '
                '(Dexter Brown)',
       'url': 'https://www.youtube.com/watch?v=0FZrtOY2H5w&t=348s',
       'video_id': '0FZrtOY2H5w'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=ES6y4iF-bBM&t=54s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "You just go click on the link below and it's an instant download. 're just "
               'getting started to run your state funds business, the : Very first thing you '
               'guys is a CRM stands for customer relationship software for you guys that are '
               'brand new.',
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': "You just go click on the link below and it's an instant download. 're just "
              'getting started to run your state funds business, the : Very first thing you '
              'guys is a CRM stands for customer relationship software for you guys that are '
              'brand new.',
       'title': 'State Funds Tutorial: 5 Tech Tools For Your State Funds Business (Surplus '
                'Funds 101)',
       'url': 'https://www.youtube.com/watch?v=ES6y4iF-bBM&t=54s',
       'video_id': 'ES6y4iF-bBM'},
      {'author': 'Alfred Taren',
       'channel': 'Alfred Taren',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=ouYE5P3UJdQ&t=21s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': "For context, I've done this since 2013, over 2,000 cases completed, and I "
               'delivered over a hundred million dollars to families across the country. First '
               'thing to understand, there is no such thing as the surplus funds claims '
               'process.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "For context, I've done this since 2013, over 2,000 cases completed, and I "
              'delivered over a hundred million dollars to families across the country. First '
              'thing to understand, there is no such thing as the surplus funds claims '
              'process.',
       'title': 'Surplus Funds Claim Process Explained (What Nobody Tells You) (Alfred Taren)',
       'url': 'https://www.youtube.com/watch?v=ouYE5P3UJdQ&t=21s',
       'video_id': 'ouYE5P3UJdQ'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:51](https://www.youtube.com/watch?v=lFoZDRAGylo&t=111s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': 'If you want to get paid consistently, you need to stack up your pipeline and '
               'put in the work every single week. Surplus funds recovery depends on the '
               'schedule of the court system, and payout time frames can vary. And when it '
               'takes too long, people panic.',
       'timestamp': 111,
       'timestamp_label': '[00:01:51]',
       'timestamp_seconds': 111,
       'tip': 'If you want to get paid consistently, you need to stack up your pipeline and '
              'put in the work every single week. Surplus funds recovery depends on the '
              'schedule of the court system, and payout time frames can vary. And when it '
              'takes too long, people panic.',
       'title': 'How Much Money Can You *REALISTICALLY* Make With Surplus Funds Recovery '
                '(Money Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=lFoZDRAGylo&t=111s',
       'video_id': 'lFoZDRAGylo'},
      {'author': 'Hutch & Holmes',
       'channel': 'Hutch & Holmes',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:52](https://www.youtube.com/watch?v=L2oKpjOoh20&t=52s)',
       'relevance': 'Attributed practitioner commentary on county PDF ingestion, CRM pipeline '
                    'tracking, deadline automation, and repeatable deal-desk operations.',
       'source_type': 'video_pro_tip',
       'text': 'You inform the person of the information that you found and that money is owed '
               'to them. And then you will assist them with the process based on what your '
               "state will allow you to do. Now, if you're a notary, you may be able to "
               'notarize certain documents.',
       'timestamp': 52,
       'timestamp_label': '[00:00:52]',
       'timestamp_seconds': 52,
       'tip': 'You inform the person of the information that you found and that money is owed '
              'to them. And then you will assist them with the process based on what your '
              "state will allow you to do. Now, if you're a notary, you may be able to "
              'notarize certain documents.',
       'title': 'How to Recover Foreclosure Surplus Funds (3-Step System) (Hutch & Holmes)',
       'url': 'https://www.youtube.com/watch?v=L2oKpjOoh20&t=52s',
       'video_id': 'L2oKpjOoh20'}],
 11: [{'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:19](https://www.youtube.com/watch?v=ASO1JUOWTjA&t=199s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "I hire them, so I don't have to fire them as quickly. Another thing is the VA "
               "doesn't show you pictures of their workstation.",
       'timestamp': 199,
       'timestamp_label': '[00:03:19]',
       'timestamp_seconds': 199,
       'tip': "I hire them, so I don't have to fire them as quickly. Another thing is the VA "
              "doesn't show you pictures of their workstation.",
       'title': 'State Funds Tutorial Virtual Assistants: Top 3 Hiring Mistakes While Growing '
                'Your Surplus Business (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=ASO1JUOWTjA&t=199s',
       'video_id': 'ASO1JUOWTjA'},
      {'author': 'ohiocommerce',
       'channel': 'ohiocommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:56](https://www.youtube.com/watch?v=8nmo4S1v3Co&t=656s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "So, right now we do have 48,000 claims waiting to be processed. So, it's "
               'important for you to understand that we are hiring more team members '
               "internally to take care of everyone's claim and get them reviewed.",
       'timestamp': 656,
       'timestamp_label': '[00:10:56]',
       'timestamp_seconds': 656,
       'tip': "So, right now we do have 48,000 claims waiting to be processed. So, it's "
              'important for you to understand that we are hiring more team members internally '
              "to take care of everyone's claim and get them reviewed.",
       'title': 'Ohio Unclaimed Funds: How to Claim Your Cash in 3 Steps (HB 96 Deadline '
                'Explained) Webinar 2-5-2026 (ohiocommerce)',
       'url': 'https://www.youtube.com/watch?v=8nmo4S1v3Co&t=656s',
       'video_id': '8nmo4S1v3Co'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:44](https://www.youtube.com/watch?v=2agNOU2taXA&t=764s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "You know we're very tra my acquisition team very very common. Uh we we buy a "
               'lot of inherited properties like a lot. Um it is a problem in New Orleans. We '
               "do have a lot of like intergenerational transfers that don't happen legally.",
       'timestamp': 764,
       'timestamp_label': '[00:12:44]',
       'timestamp_seconds': 764,
       'tip': "You know we're very tra my acquisition team very very common. Uh we we buy a "
              'lot of inherited properties like a lot. Um it is a problem in New Orleans. We '
              "do have a lot of like intergenerational transfers that don't happen legally.",
       'title': 'Curative Title for Wholesalers: How He Turned a Dead Lead Into a Deal '
                '(Courtney Fricke)',
       'url': 'https://www.youtube.com/watch?v=2agNOU2taXA&t=764s',
       'video_id': '2agNOU2taXA'},
      {'author': 'Sternberg Law Group',
       'channel': 'Sternberg Law Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:19](https://www.youtube.com/watch?v=z6jQuGWdtDY&t=139s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': 'So, if the amount was 750,000, the payoffs between the first mortgage and the '
               'second mortgage and your tax lien was 550, you need to hire an attorney, you '
               'can call us, sternberglegalgroup.',
       'timestamp': 139,
       'timestamp_label': '[00:02:19]',
       'timestamp_seconds': 139,
       'tip': 'So, if the amount was 750,000, the payoffs between the first mortgage and the '
              'second mortgage and your tax lien was 550, you need to hire an attorney, you '
              'can call us, sternberglegalgroup.',
       'title': 'Surplus Funds After Foreclosure Explained | What Homeowners Must Know | '
                'Sternberg Law Group (Sternberg Law Group)',
       'url': 'https://www.youtube.com/watch?v=z6jQuGWdtDY&t=139s',
       'video_id': 'z6jQuGWdtDY'},
      {'author': 'Surplus Funds List',
       'channel': 'Surplus Funds List',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:33](https://www.youtube.com/watch?v=lOnYUxDdOdI&t=333s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': 'The desk uh allows you to organize your tasks that you need to perform '
               'throughout your day, whether overdue today or a coming, you can move them from '
               'stages.',
       'timestamp': 333,
       'timestamp_label': '[00:05:33]',
       'timestamp_seconds': 333,
       'tip': 'The desk uh allows you to organize your tasks that you need to perform '
              'throughout your day, whether overdue today or a coming, you can move them from '
              'stages.',
       'title': 'How to Run a Surplus Funds Business with One CRM: Full 2026 Walkthrough '
                '(Surplus Funds List)',
       'url': 'https://www.youtube.com/watch?v=lOnYUxDdOdI&t=333s',
       'video_id': 'lOnYUxDdOdI'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:01](https://www.youtube.com/watch?v=alaKJIcbbLw&t=181s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': 'And your script you should know like the back of your hand, and you should say '
               'it to yourself 20 times. I always sell my phone number, my Google voice that I '
               "use this day. I have it on my desk visible when I'm making calls cuz sometimes "
               'I start giving my cell phone number.',
       'timestamp': 181,
       'timestamp_label': '[00:03:01]',
       'timestamp_seconds': 181,
       'tip': 'And your script you should know like the back of your hand, and you should say '
              'it to yourself 20 times. I always sell my phone number, my Google voice that I '
              "use this day. I have it on my desk visible when I'm making calls cuz sometimes "
              'I start giving my cell phone number.',
       'title': 'Cold Calling for Surplus Funds in 2025: The Script That Actually Works! '
                '(Surplus Institute / David Church / Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=alaKJIcbbLw&t=181s',
       'video_id': 'alaKJIcbbLw'},
      {'author': 'Logan Fullmer',
       'channel': 'Logan Fullmer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:10:57](https://www.youtube.com/watch?v=onebNbNQSBM&t=4257s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': 'Brandon Schwab is a killer out there when it comes to all these deals. I mean, '
               "he's been doing it at such a high volume. And and he understands that like "
               'look, you just got to get the deals, you got to understand like who to look '
               'for, have the team.',
       'timestamp': 4257,
       'timestamp_label': '[01:10:57]',
       'timestamp_seconds': 4257,
       'tip': 'Brandon Schwab is a killer out there when it comes to all these deals. I mean, '
              "he's been doing it at such a high volume. And and he understands that like "
              'look, you just got to get the deals, you got to understand like who to look '
              'for, have the team.',
       'title': 'Curative Title Explained by a Florida Probate Attorney (Logan Fullmer)',
       'url': 'https://www.youtube.com/watch?v=onebNbNQSBM&t=4257s',
       'video_id': 'onebNbNQSBM'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:18](https://www.youtube.com/watch?v=vs2o6Zz48Oc&t=1398s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "Thinking about this saying hey it might be for you but if you don't take "
               'action now the one-on-one training may not be something that you can access '
               "later click that button and I'll see you guys on the other side.",
       'timestamp': 1398,
       'timestamp_label': '[00:23:18]',
       'timestamp_seconds': 1398,
       'tip': "Thinking about this saying hey it might be for you but if you don't take action "
              'now the one-on-one training may not be something that you can access later '
              "click that button and I'll see you guys on the other side.",
       'title': 'How The Surplus Funds Recovery Business Works 🤑 [Step By Step Training] '
                '(Money Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=vs2o6Zz48Oc&t=1398s',
       'video_id': 'vs2o6Zz48Oc'},
      {'author': 'BizMove',
       'channel': 'BizMove',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:07](https://www.youtube.com/watch?v=01plOr9pFjQ&t=427s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': 'AI SEO tools like Ubersuggest’s free tier to identify opportunities and '
               'threats. Conclusion Starting a tax overage business can be complex, but '
               'leveraging free AI tools can dramatically simplify research, marketing, '
               'communication, and operations.',
       'timestamp': 427,
       'timestamp_label': '[00:07:07]',
       'timestamp_seconds': 427,
       'tip': 'AI SEO tools like Ubersuggest’s free tier to identify opportunities and '
              'threats. Conclusion Starting a tax overage business can be complex, but '
              'leveraging free AI tools can dramatically simplify research, marketing, '
              'communication, and operations.',
       'title': 'How to Start a Tax Overage Business | Complete and Easy to Follow Guide '
                '(BizMove)',
       'url': 'https://www.youtube.com/watch?v=01plOr9pFjQ&t=427s',
       'video_id': '01plOr9pFjQ'},
      {'author': 'Hutch & Holmes',
       'channel': 'Hutch & Holmes',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:54](https://www.youtube.com/watch?v=L2oKpjOoh20&t=174s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': 'So, clarity first, leads second. If you need help getting more clarity on this '
               "business ain't cuz you're interested in it, here's what you can do. Join the "
               'free Facebook community. Uh there I have monthly training going on, live '
               "Q&A's, uh business building support.",
       'timestamp': 174,
       'timestamp_label': '[00:02:54]',
       'timestamp_seconds': 174,
       'tip': 'So, clarity first, leads second. If you need help getting more clarity on this '
              "business ain't cuz you're interested in it, here's what you can do. Join the "
              "free Facebook community. Uh there I have monthly training going on, live Q&A's, "
              'uh business building support.',
       'title': 'How to Recover Foreclosure Surplus Funds (3-Step System) (Hutch & Holmes)',
       'url': 'https://www.youtube.com/watch?v=L2oKpjOoh20&t=174s',
       'video_id': 'L2oKpjOoh20'},
      {'author': 'Surplus_Prosperity',
       'channel': 'Surplus_Prosperity',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:24](https://www.youtube.com/watch?v=MYo3k2Sxj1Q&t=264s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "It'll take you about, it'll take you less than two minutes to fill it out. "
               "From there, my team reviews it and we'll reach out to you and let you know "
               'what we find.',
       'timestamp': 264,
       'timestamp_label': '[00:04:24]',
       'timestamp_seconds': 264,
       'tip': "It'll take you about, it'll take you less than two minutes to fill it out. From "
              "there, my team reviews it and we'll reach out to you and let you know what we "
              'find.',
       'title': 'What Are Surplus Funds? How to Claim Money Owed to You After Foreclosure or '
                'Tax Sale (Surplus_Prosperity)',
       'url': 'https://www.youtube.com/watch?v=MYo3k2Sxj1Q&t=264s',
       'video_id': 'MYo3k2Sxj1Q'},
      {'author': 'Overage Acquisition',
       'channel': 'Overage Acquisition',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:09](https://www.youtube.com/watch?v=6UiKunbtUa0&t=69s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "I've included in this training, there's different words and names for "
               "overages, but if you use, you know, different words, it's okay. The browser "
               "will know what you're looking for just by the other keywords. And then you "
               'want to include the date.',
       'timestamp': 69,
       'timestamp_label': '[00:01:09]',
       'timestamp_seconds': 69,
       'tip': "I've included in this training, there's different words and names for overages, "
              "but if you use, you know, different words, it's okay. The browser will know "
              "what you're looking for just by the other keywords. And then you want to "
              'include the date.',
       'title': 'How To Find Excess Proceeds List In 2025 (Proven Strategies) (Overage '
                'Acquisition)',
       'url': 'https://www.youtube.com/watch?v=6UiKunbtUa0&t=69s',
       'video_id': '6UiKunbtUa0'},
      {'author': "Bob Diamond - America's Tax Sale Attorney",
       'channel': "Bob Diamond - America's Tax Sale Attorney",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:09](https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=549s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "Court is the judicial system, so that's why it's a judicial claim. Now, when "
               "you have to do those you're going to hire an attorney to do the claim for you, "
               "because you can't represent someone else in court.",
       'timestamp': 549,
       'timestamp_label': '[00:09:09]',
       'timestamp_seconds': 549,
       'tip': "Court is the judicial system, so that's why it's a judicial claim. Now, when "
              "you have to do those you're going to hire an attorney to do the claim for you, "
              "because you can't represent someone else in court.",
       'title': "Tax Sale Overages Course (Bob Diamond - America's Tax Sale Attorney)",
       'url': 'https://www.youtube.com/watch?v=qGPsbhsEAVQ&t=549s',
       'video_id': 'qGPsbhsEAVQ'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:10](https://www.youtube.com/watch?v=1AMk1-SB5ic&t=310s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "Free training on Thursday night the link to registers down below and I'm also "
               'putting up a link for my free Facebook group if you want to join that if you '
               "haven't feel free to join that as well and I'll see you all around thanks.",
       'timestamp': 310,
       'timestamp_label': '[00:05:10]',
       'timestamp_seconds': 310,
       'tip': "Free training on Thursday night the link to registers down below and I'm also "
              'putting up a link for my free Facebook group if you want to join that if you '
              "haven't feel free to join that as well and I'll see you all around thanks.",
       'title': "Unclaimed Funds: How to Get Your Client's Documents in Order⚡️Unclaimed fund "
                'Client Document finding (Surplus Institute / David Church / Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=1AMk1-SB5ic&t=310s',
       'video_id': '1AMk1-SB5ic'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:48](https://www.youtube.com/watch?v=AAF69oF79DU&t=348s)',
       'relevance': 'Attributed practitioner commentary on small-team division of labor across '
                    'research VAs, acquisition specialists, and state-licensed co-counsel.',
       'source_type': 'video_pro_tip',
       'text': "And what is her intent does she want to hold it or sell it. So it's a listing "
               'appointment. And she needs to do it quick. So why do I, so I can pull the '
               'deed, I can find out the information and what do I need to tell her she needs '
               'to do to lead - Hire a probate attorney.',
       'timestamp': 348,
       'timestamp_label': '[00:05:48]',
       'timestamp_seconds': 348,
       'tip': "And what is her intent does she want to hold it or sell it. So it's a listing "
              'appointment. And she needs to do it quick. So why do I, so I can pull the deed, '
              'I can find out the information and what do I need to tell her she needs to do '
              'to lead - Hire a probate attorney.',
       'title': 'Sub-to strategy for probate investing | Probate foreclosures | Probate real '
                'estate marketing tips (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=AAF69oF79DU&t=348s',
       'video_id': 'AAF69oF79DU'}],
 12: [{'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:29](https://www.youtube.com/watch?v=lFoZDRAGylo&t=209s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "Now, I'm not going to lie to you and tell you that you'll close 10 deals in "
               'your first month. If you put in 2 to 3 hours a day, call it an hour of '
               "research and maybe a couple of hours of phone calls, you'll be able to call "
               'around 200 people a day.',
       'timestamp': 209,
       'timestamp_label': '[00:03:29]',
       'timestamp_seconds': 209,
       'tip': "Now, I'm not going to lie to you and tell you that you'll close 10 deals in "
              'your first month. If you put in 2 to 3 hours a day, call it an hour of research '
              "and maybe a couple of hours of phone calls, you'll be able to call around 200 "
              'people a day.',
       'title': 'How Much Money Can You *REALISTICALLY* Make With Surplus Funds Recovery '
                '(Money Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=lFoZDRAGylo&t=209s',
       'video_id': 'lFoZDRAGylo'},
      {'author': "Bob Diamond - America's Tax Sale Attorney",
       'channel': "Bob Diamond - America's Tax Sale Attorney",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:16](https://www.youtube.com/watch?v=lzU09FRqmhg&t=376s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "United States, and they just add up, you know, day after day at 1500 that's "
               "what, 70 552 weeks a year. So that's about 1500 sales per day. That's about "
               "7500 sales per week. That's about 30,000 sales per month.",
       'timestamp': 376,
       'timestamp_label': '[00:06:16]',
       'timestamp_seconds': 376,
       'tip': "United States, and they just add up, you know, day after day at 1500 that's "
              "what, 70 552 weeks a year. So that's about 1500 sales per day. That's about "
              "7500 sales per week. That's about 30,000 sales per month.",
       'title': "How To Claim Surplus Funds From Foreclosure (Bob Diamond - America's Tax Sale "
                'Attorney)',
       'url': 'https://www.youtube.com/watch?v=lzU09FRqmhg&t=376s',
       'video_id': 'lzU09FRqmhg'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:49](https://www.youtube.com/watch?v=ieI6zKICpKo&t=169s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "'s having a good CRM, which I have a CRM video that I use. I like either "
               'Trello or ClickUp, but I hope this helps. Um just a couple of the yeses I got '
               "today. Literally, a 16,000 day in commission is huge. It's a nice way to start "
               'the week.',
       'timestamp': 169,
       'timestamp_label': '[00:02:49]',
       'timestamp_seconds': 169,
       'tip': "'s having a good CRM, which I have a CRM video that I use. I like either Trello "
              'or ClickUp, but I hope this helps. Um just a couple of the yeses I got today. '
              "Literally, a 16,000 day in commission is huge. It's a nice way to start the "
              'week.',
       'title': '$16,000 Live Cold Calling Commission (Surplus Institute / David Church / '
                'Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=ieI6zKICpKo&t=169s',
       'video_id': 'ieI6zKICpKo'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:18](https://www.youtube.com/watch?v=foMCyYJ4LgY&t=258s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "Okay, one cancellation a week, nine calls one cancel. It's a pretty good ratio "
               'right there, very first thought is she has the highest overall cells average. '
               'Okay, so she can successfully close most transactions or people that she '
               "speaks well, that's really good.",
       'timestamp': 258,
       'timestamp_label': '[00:04:18]',
       'timestamp_seconds': 258,
       'tip': "Okay, one cancellation a week, nine calls one cancel. It's a pretty good ratio "
              'right there, very first thought is she has the highest overall cells average. '
              'Okay, so she can successfully close most transactions or people that she speaks '
              "well, that's really good.",
       'title': 'State Funds Tutorial: What To Do When A Deal Cancels While Working Your State '
                'Funds Business. (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=foMCyYJ4LgY&t=258s',
       'video_id': 'foMCyYJ4LgY'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:31:41](https://www.youtube.com/watch?v=W-FX20iI9Jk&t=1901s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "'t know what you don't know. So ultimately the first deal does not make you a "
               "title expert overnight. And I don't want you to present yourself as one "
               'either, right? You want to be able to start learning that pattern recognition '
               'of recognizing problems.',
       'timestamp': 1901,
       'timestamp_label': '[00:31:41]',
       'timestamp_seconds': 1901,
       'tip': "'t know what you don't know. So ultimately the first deal does not make you a "
              "title expert overnight. And I don't want you to present yourself as one either, "
              'right? You want to be able to start learning that pattern recognition of '
              'recognizing problems.',
       'title': 'How to Get Your First Curative Title Deal: A Step-by-Step Guide (Courtney '
                'Fricke)',
       'url': 'https://www.youtube.com/watch?v=W-FX20iI9Jk&t=1901s',
       'video_id': 'W-FX20iI9Jk'},
      {'author': 'Logan Fullmer',
       'channel': 'Logan Fullmer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:52:38](https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3158s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "But, they also it's important to remember that I need to get this deal to "
               'cycle. I need to get it these sellers paid. I need to close my problems out. I '
               "need to resell it, make some money. And if I'm doing one or two deals at a "
               'time, I need one to close every 30 days.',
       'timestamp': 3158,
       'timestamp_label': '[00:52:38]',
       'timestamp_seconds': 3158,
       'tip': "But, they also it's important to remember that I need to get this deal to "
              'cycle. I need to get it these sellers paid. I need to close my problems out. I '
              "need to resell it, make some money. And if I'm doing one or two deals at a "
              'time, I need one to close every 30 days.',
       'title': "Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer)",
       'url': 'https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3158s',
       'video_id': 'dJ-LTFmMsTg'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:35](https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=95s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "I've said an account that they had. That's going to tell the person I'm not a "
               'some sort of telemarketer from Africa calling. I get call backs all day long '
               'on that. Not everybody calls me back, but my marketing system is five new '
               'leads 5 days a week.',
       'timestamp': 95,
       'timestamp_label': '[00:01:35]',
       'timestamp_seconds': 95,
       'tip': "I've said an account that they had. That's going to tell the person I'm not a "
              'some sort of telemarketer from Africa calling. I get call backs all day long on '
              'that. Not everybody calls me back, but my marketing system is five new leads 5 '
              'days a week.',
       'title': 'How To Find family members of a deceased person! (Surplus Institute / David '
                'Church / Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=95s',
       'video_id': 'eiQ53kxE6ZA'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=-QzABvCmtVc&t=59s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "Now, let's go ahead and jump in to the deal. But before we do, today's "
               'conversation is important because one of the first steps in learning how to do '
               'the curative title deals is to learn how to spot the problems like the title '
               'issues and the ownership issues.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': "Now, let's go ahead and jump in to the deal. But before we do, today's "
              'conversation is important because one of the first steps in learning how to do '
              'the curative title deals is to learn how to spot the problems like the title '
              'issues and the ownership issues.',
       'title': 'How to Underwrite a Curative Title Deal (And Know When to Walk Away) '
                '(Courtney Fricke)',
       'url': 'https://www.youtube.com/watch?v=-QzABvCmtVc&t=59s',
       'video_id': '-QzABvCmtVc'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:27](https://www.youtube.com/watch?v=t4w_wFimZ9A&t=447s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': 'So bring up all the objections that client has and resolve all of those '
               "potential issues that might stall a deal : Guy, this is how you're gonna wanna "
               'start clearing objections, so you wanna be able to know what they might say, '
               'and bring it up ahead of time.',
       'timestamp': 447,
       'timestamp_label': '[00:07:27]',
       'timestamp_seconds': 447,
       'tip': 'So bring up all the objections that client has and resolve all of those '
              "potential issues that might stall a deal : Guy, this is how you're gonna wanna "
              'start clearing objections, so you wanna be able to know what they might say, '
              'and bring it up ahead of time.',
       'title': 'State Funds Tutorial: Cold Calling Objections vs. Complaints. Surplus Funds '
                '101 (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=t4w_wFimZ9A&t=447s',
       'video_id': 't4w_wFimZ9A'},
      {'author': 'Ted Thomas',
       'channel': 'Ted Thomas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:44](https://www.youtube.com/watch?v=d5TLZqkPX14&t=584s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "I don't know what the market value is but we got a tax value. All right, okay "
               'so the auction will start at the back taxes, so very close to that, all right, '
               "however someone else bids it up. They're willing to pay 45,000 for the "
               'property.',
       'timestamp': 584,
       'timestamp_label': '[00:09:44]',
       'timestamp_seconds': 584,
       'tip': "I don't know what the market value is but we got a tax value. All right, okay "
              'so the auction will start at the back taxes, so very close to that, all right, '
              "however someone else bids it up. They're willing to pay 45,000 for the "
              'property.',
       'title': 'How To Claim Tax Sale Overages (Ted Thomas)',
       'url': 'https://www.youtube.com/watch?v=d5TLZqkPX14&t=584s',
       'video_id': 'd5TLZqkPX14'},
      {'author': 'ohiocommerce',
       'channel': 'ohiocommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:45](https://www.youtube.com/watch?v=GrE0UUh_3BI&t=105s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': 'Want you to know that this is your BBB BBB is your first line of resource to '
               'check out businesses to file complaints to get solutions to start your '
               'businesses to have business resourc our es all around this is your BBB next.',
       'timestamp': 105,
       'timestamp_label': '[00:01:45]',
       'timestamp_seconds': 105,
       'tip': 'Want you to know that this is your BBB BBB is your first line of resource to '
              'check out businesses to file complaints to get solutions to start your '
              'businesses to have business resourc our es all around this is your BBB next.',
       'title': 'Claiming your Unclaimed Funds (ohiocommerce)',
       'url': 'https://www.youtube.com/watch?v=GrE0UUh_3BI&t=105s',
       'video_id': 'GrE0UUh_3BI'},
      {'author': 'Spencer Vann',
       'channel': 'Spencer Vann',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=ZEobF_ck678&t=119s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "Routine looks like it's really simple it's about five minutes so the first "
               "thing I'll do is I'll sit in my chair I'll sit in good posture okay and I will "
               'take deep breaths.',
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': "Routine looks like it's really simple it's about five minutes so the first "
              "thing I'll do is I'll sit in my chair I'll sit in good posture okay and I will "
              'take deep breaths.',
       'title': 'Surplus Fund Cold Calls: How to ACTUALLY close deals (99% have no clue) '
                '(Spencer Vann)',
       'url': 'https://www.youtube.com/watch?v=ZEobF_ck678&t=119s',
       'video_id': 'ZEobF_ck678'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:13](https://www.youtube.com/watch?v=T2gvkByDlFU&t=73s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "Here in California, um there's a law that was if it was a primary residence "
               'for either living or deceased, um you can get, you know, a guaranteed 90-day '
               'extension with listing. And another 90 days if you can fall in the escrow.',
       'timestamp': 73,
       'timestamp_label': '[00:01:13]',
       'timestamp_seconds': 73,
       'tip': "Here in California, um there's a law that was if it was a primary residence for "
              'either living or deceased, um you can get, you know, a guaranteed 90-day '
              'extension with listing. And another 90 days if you can fall in the escrow.',
       'title': '🚨 Probate Property Headed to Foreclosure Auction… Is It Worth Pursuing? '
                '(Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=T2gvkByDlFU&t=73s',
       'video_id': 'T2gvkByDlFU'},
      {'author': 'Michael Curtis',
       'channel': 'Michael Curtis',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:56](https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=356s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "Below this video if you're on youtube um if you're on my website just share "
               'the page um let others know about the site thanks for watching and I hope this '
               'video did help you in some way and I thank you for watching and you have a '
               'really wonderful day take care now bye.',
       'timestamp': 356,
       'timestamp_label': '[00:05:56]',
       'timestamp_seconds': 356,
       'tip': "Below this video if you're on youtube um if you're on my website just share the "
              'page um let others know about the site thanks for watching and I hope this '
              'video did help you in some way and I thank you for watching and you have a '
              'really wonderful day take care now bye.',
       'title': 'Michigan Unclaimed Property - This is How You Make an Unclaimed Property '
                'Claim (Michael Curtis)',
       'url': 'https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=356s',
       'video_id': 'Fn04U_Yfuzg'},
      {'author': 'SurplusFundsRiches',
       'channel': 'SurplusFundsRiches',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:03:22](https://www.youtube.com/watch?v=4W8c0I28pxQ&t=3802s)',
       'relevance': 'Attributed practitioner commentary on 30-60-90 day launch execution, '
                    'weekly cohort KPIs, and pre-submission compliance audits.',
       'source_type': 'video_pro_tip',
       'text': "That list at least three four times a week so you know what you're dealing "
               "with and you're never gonna get oopsie we already had that file.",
       'timestamp': 3802,
       'timestamp_label': '[01:03:22]',
       'timestamp_seconds': 3802,
       'tip': "That list at least three four times a week so you know what you're dealing with "
              "and you're never gonna get oopsie we already had that file.",
       'title': 'Free Surplus Funds Training - Indepth, full hour! SurplusFundsRiches '
                '(SurplusFundsRiches)',
       'url': 'https://www.youtube.com/watch?v=4W8c0I28pxQ&t=3802s',
       'video_id': '4W8c0I28pxQ'}]}
