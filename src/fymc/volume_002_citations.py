"""Curated 180-citation baseline (15 per chapter across Q1-Q12) mined from the 189-video corpus for Volume 002 (Surplus Funds Recovery)."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'auction',
     'deed',
     'excess',
     'foreclosure',
     'lane',
     'lanes',
     'mortgage',
     'overage',
     'overages',
     'proceeds',
     'surplus',
     'tax',
     'trustee'},
 2: {'claimant',
     'clerk',
     'county',
     'court',
     'custodian',
     'disbursement',
     'entitled',
     'escrow',
     'funds',
     'holder',
     'owner',
     'treasurer',
     'trustee'},
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
     'split'},
 4: {'bond',
     'budget',
     'capital',
     'cost',
     'costs',
     'entity',
     'insurance',
     'lean',
     'llc',
     'notary',
     'pilot',
     'reserve',
     'setup',
     'startup'},
 5: {'bankruptcy',
     'deceased',
     'heirs',
     'hoa',
     'irs',
     'junior',
     'lien',
     'liens',
     'mortgage',
     'priority',
     'senior',
     'surviving',
     'trap',
     'wipeout'},
 6: {'auction',
     'calendar',
     'clerk',
     'county',
     'docket',
     'filter',
     'lead',
     'leads',
     'list',
     'lists',
     'qualify',
     'records',
     'sourcing',
     'threshold'},
 7: {'affidavit',
     'chain',
     'claim',
     'deed',
     'documents',
     'encumbrance',
     'heir',
     'heirs',
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
     'obituary',
     'pacer',
     'parcel',
     'portal',
     'recorder',
     'regrid',
     'search',
     'skip',
     'stack',
     'tracing'},
 9: {'agreement',
     'attorney',
     'call',
     'calling',
     'compliance',
     'contract',
     'disclosure',
     'mail',
     'outreach',
     'power',
     'script',
     'solicitation',
     'statute',
     'waiting'},
 10: {'alerts',
      'automation',
      'batch',
      'case',
      'crm',
      'dataset',
      'import',
      'ocr',
      'pipeline',
      'scraper',
      'scraping',
      'software',
      'study',
      'workflow'},
 11: {'acquisition',
      'caller',
      'counsel',
      'delegate',
      'desk',
      'hire',
      'kpi',
      'operations',
      'researcher',
      'scale',
      'scaling',
      'sop',
      'team',
      'va'},
 12: {'action',
      'checklist',
      'day',
      'days',
      'execution',
      'first',
      'launch',
      'milestone',
      'pilot',
      'plan',
      'roadmap',
      'sprint',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=133s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'A tax sale overage is not the same as a mortgage foreclosure surplus. One county '
              'lets you email everything. The next one, they actually want originals. They want '
              'the papers actually mailed in. And if you send a copy, it ',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': 'A tax sale overage is not the same as a mortgage foreclosure surplus. One county '
             'lets you email everything. The next one, they actually want originals. They want the '
             'papers actually mailed in. And if you send a copy, it ',
      'title': 'Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=133s',
      'video_id': 'MVCNlj7HQBQ'},
     {'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:34](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=334s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'Yes, the mortgage and the deed of trust are gonna be wiped out by the county. The '
              "point is, you need to check on these things if you're gonna be a good buyer at the "
              'auction. All right. This research can be done at the co',
      'timestamp': 334,
      'timestamp_label': '[00:05:34]',
      'timestamp_seconds': 334,
      'tip': 'Yes, the mortgage and the deed of trust are gonna be wiped out by the county. The '
             "point is, you need to check on these things if you're gonna be a good buyer at the "
             'auction. All right. This research can be done at the co',
      'title': 'How To Do A Title Search On A Property Yourself Before You Bid At Tax Sale '
               'Auctions (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=334s',
      'video_id': 'xtdWFaJY8Xc'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=q95klfFm9mE&t=210s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'going to depend on the type of foreclosure for example in Florida on the tax sales '
              'side lean holders only have 120 days after the notice of sale notification has been '
              'actually submitted to actually file a claim if they d',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': 'going to depend on the type of foreclosure for example in Florida on the tax sales '
             'side lean holders only have 120 days after the notice of sale notification has been '
             'actually submitted to actually file a claim if they d',
      'title': "2 Ways To Check If There's a Lien On a Property (For Surplus Funds Recovery) "
               '(Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=q95klfFm9mE&t=210s',
      'video_id': 'q95klfFm9mE'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:43](https://www.youtube.com/watch?v=W-FX20iI9Jk&t=1543s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "active litigation. Um you know, I would say if you're familiar with mortgage "
              'foreclosures, that would be okay, but or or maybe property tax foreclosure '
              'processes, but be careful of jumping into something highly complex f',
      'timestamp': 1543,
      'timestamp_label': '[00:25:43]',
      'timestamp_seconds': 1543,
      'tip': "active litigation. Um you know, I would say if you're familiar with mortgage "
             'foreclosures, that would be okay, but or or maybe property tax foreclosure '
             'processes, but be careful of jumping into something highly complex f',
      'title': 'How to Get Your First Curative Title Deal: A Step-by-Step Guide (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=W-FX20iI9Jk&t=1543s',
      'video_id': 'W-FX20iI9Jk'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=MiiGrCZZAZk&t=27s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'law firm to have the claim filed. Also, mortgage foreclosures being non-judicial, '
              "you're going through a trustee, not the county. All right? So, this check, "
              '$210,000, was issued to the law firm that we went through. I us',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'law firm to have the claim filed. Also, mortgage foreclosures being non-judicial, '
             "you're going through a trustee, not the county. All right? So, this check, $210,000, "
             'was issued to the law firm that we went through. I us',
      'title': '$200,000 California Foreclosure Heir Claim Case Study (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MiiGrCZZAZk&t=27s',
      'video_id': 'MiiGrCZZAZk'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=88s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'Now, we were able to locate this lead on excess elite.com, and we were able to find '
              'that there was only one month remaining for us to get a claim in. If we did not '
              'file that claim, the homeowner would have had no opportu',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Now, we were able to locate this lead on excess elite.com, and we were able to find '
             'that there was only one month remaining for us to get a claim in. If we did not file '
             'that claim, the homeowner would have had no opportu',
      'title': 'Amador county Tax Sale Surplus Funds Case Study (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=88s',
      'video_id': '4-lZwuXtY6Y'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:04](https://www.youtube.com/watch?v=TBB8OPPFSsM&t=1324s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'property and they would have what was called a deed of distribution which would '
              'then take the property the farm out of the estate and then The Heirs would divide '
              "up the proceeds so there's a lot of value and here's some ",
      'timestamp': 1324,
      'timestamp_label': '[00:22:04]',
      'timestamp_seconds': 1324,
      'tip': 'property and they would have what was called a deed of distribution which would then '
             'take the property the farm out of the estate and then The Heirs would divide up the '
             "proceeds so there's a lot of value and here's some ",
      'title': 'What’s in a Probate Record and How to Use it for Genealogical Research– James '
               'Tanner (10 Sep 2023) (BYU Library Family History Center)',
      'url': 'https://www.youtube.com/watch?v=TBB8OPPFSsM&t=1324s',
      'video_id': 'TBB8OPPFSsM'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=-s07juX_8jE&t=24s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "have selected here and then finding a data set of interest let's say that we're "
              'interested in one of these tax foreclosure data sets which are unique to detroit '
              'click on the plus icon and that will add it to the map and ',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': "have selected here and then finding a data set of interest let's say that we're "
             'interested in one of these tax foreclosure data sets which are unique to detroit '
             'click on the plus icon and that will add it to the map and ',
      'title': 'Using Datasets - Regrid Property App (Web)',
      'url': 'https://www.youtube.com/watch?v=-s07juX_8jE&t=24s',
      'video_id': '-s07juX_8jE'},
     {'author': 'SurplusFundsRiches',
      'channel': 'SurplusFundsRiches',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=1N1Z99kUvRw&t=105s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'ownership to the owner who owned it at the time of the sale was recorded in 1960 or '
              'earlier you pretty much you know that person on the deed is dead just so you know '
              'why they were probably 20 years old at the time that w',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'ownership to the owner who owned it at the time of the sale was recorded in 1960 or '
             'earlier you pretty much you know that person on the deed is dead just so you know '
             'why they were probably 20 years old at the time that w',
      'title': 'Surplus Funds: Owner Died - STILL CLAIM! (SurplusFundsRiches)',
      'url': 'https://www.youtube.com/watch?v=1N1Z99kUvRw&t=105s',
      'video_id': '1N1Z99kUvRw'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:01](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=541s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'this active or is this something that is not is no longer active. It could be a '
              'missing heir, it could be a tax sale issue, a forged deed allegation. It could be a '
              'boundary dispute, an improperly prepared deed, or a prob',
      'timestamp': 541,
      'timestamp_label': '[00:09:01]',
      'timestamp_seconds': 541,
      'tip': 'this active or is this something that is not is no longer active. It could be a '
             'missing heir, it could be a tax sale issue, a forged deed allegation. It could be a '
             'boundary dispute, an improperly prepared deed, or a prob',
      'title': '5 Curative Title Terms Every Investor Should Understand (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=sf2hUucsNZ8&t=541s',
      'video_id': 'sf2hUucsNZ8'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=T2gvkByDlFU&t=104s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "like there's an opportunity there cuz people have a problem. And if you spend some "
              'time and design a solution, then you get paid. If that makes sense. >> Yeah, um it '
              "does, right? It's just maybe it's a limiting belief th",
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': "like there's an opportunity there cuz people have a problem. And if you spend some "
             'time and design a solution, then you get paid. If that makes sense. >> Yeah, um it '
             "does, right? It's just maybe it's a limiting belief th",
      'title': '🚨 Probate Property Headed to Foreclosure Auction… Is It Worth Pursuing? (Probate '
               'Mastery)',
      'url': 'https://www.youtube.com/watch?v=T2gvkByDlFU&t=104s',
      'video_id': 'T2gvkByDlFU'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:01](https://www.youtube.com/watch?v=xAiBXreoVY0&t=1s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "Unclaimed funds California, here's what you need to know. As of 2024, there is 13 "
              "billion dollars in unclaimed funds that are sitting at the state level. There's "
              'also 76 million active accounts, which means you will neve',
      'timestamp': 1,
      'timestamp_label': '[00:00:01]',
      'timestamp_seconds': 1,
      'tip': "Unclaimed funds California, here's what you need to know. As of 2024, there is 13 "
             "billion dollars in unclaimed funds that are sitting at the state level. There's also "
             '76 million active accounts, which means you will neve',
      'title': 'California Unclaimed Funds: What You Need To Know To Be A Property Investigator '
               '#unclaimedassets (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=xAiBXreoVY0&t=1s',
      'video_id': 'xAiBXreoVY0'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=JmuqGo9wYkg&t=74s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "and two weeks off i'd fly all across the united states you know did it for a long "
              'time you know every single year i would never throw away my room keys i accumulate '
              'stacks like huge ones like this i could barely grip the',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "and two weeks off i'd fly all across the united states you know did it for a long "
             'time you know every single year i would never throw away my room keys i accumulate '
             'stacks like huge ones like this i could barely grip the',
      'title': 'State Funds Tutorial: How To Make Cold Calls If You Have A Full Time Job. (Surplus '
               'Funds 101)',
      'url': 'https://www.youtube.com/watch?v=JmuqGo9wYkg&t=74s',
      'video_id': 'JmuqGo9wYkg'},
     {'author': 'National Housing Resource Center',
      'channel': 'National Housing Resource Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:34](https://www.youtube.com/watch?v=VFSnbIIfy-M&t=1594s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'HPNP link that you mentioned. >> Thanks. Okay. So, uh this is a person who is '
              'working with a client who was given a property that she shared with a partner for '
              "20 years through a transfer on death deed. Uh lost mitt won'",
      'timestamp': 1594,
      'timestamp_label': '[00:26:34]',
      'timestamp_seconds': 1594,
      'tip': 'HPNP link that you mentioned. >> Thanks. Okay. So, uh this is a person who is '
             'working with a client who was given a property that she shared with a partner for 20 '
             "years through a transfer on death deed. Uh lost mitt won'",
      'title': 'Preserving Homeownership: A Guide to Heirs Property for Housing Counselors '
               '(National Housing Resource Center)',
      'url': 'https://www.youtube.com/watch?v=VFSnbIIfy-M&t=1594s',
      'video_id': 'VFSnbIIfy-M'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:50](https://www.youtube.com/watch?v=Yt91gmZt8sE&t=1730s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'a deed of distribution from the estate and so the property had to be probated so '
              'what happens so for example let me give an example of something that might happen '
              "so back to john doe or jane doe at this case we'll call i",
      'timestamp': 1730,
      'timestamp_label': '[00:28:50]',
      'timestamp_seconds': 1730,
      'tip': 'a deed of distribution from the estate and so the property had to be probated so '
             'what happens so for example let me give an example of something that might happen so '
             "back to john doe or jane doe at this case we'll call i",
      'title': 'Discovering Your Ancestors Using Probate Records- James Tanner (BYU Library Family '
               'History Center)',
      'url': 'https://www.youtube.com/watch?v=Yt91gmZt8sE&t=1730s',
      'video_id': 'Yt91gmZt8sE'}],
 2: [{'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=30s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "result in a surplus. We were able to identify the surplus, identify who's actually "
              'entitled, assist them on filing, and we get paid directly from the county. Now, for '
              'our services, we did charge a 30% success fee for hel',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "result in a surplus. We were able to identify the surplus, identify who's actually "
             'entitled, assist them on filing, and we get paid directly from the county. Now, for '
             'our services, we did charge a 30% success fee for hel',
      'title': 'Amador county Tax Sale Surplus Funds Case Study (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=30s',
      'video_id': '4-lZwuXtY6Y'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=FNbqvZGEzeE&t=108s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'entitled to Surplus a great way to show them is that the property sold for a higher '
              "amount so once we get that first step done we've established how and when the "
              'counties are having their sales we now now want to see if ',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'entitled to Surplus a great way to show them is that the property sold for a higher '
             "amount so once we get that first step done we've established how and when the "
             'counties are having their sales we now now want to see if ',
      'title': 'How To Become a Surplus Funds Expert FOR 1 COUNTY (Asset Recovery Business) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=FNbqvZGEzeE&t=108s',
      'video_id': 'FNbqvZGEzeE'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:21](https://www.youtube.com/watch?v=suJSu-vn6yI&t=681s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'want to show them the sale results, the county list, or court document, and be '
              "transparent about everything. This isn't a secretive business. The more open you "
              'are, the more clients trust you. Finally, to close a deal, o',
      'timestamp': 681,
      'timestamp_label': '[00:11:21]',
      'timestamp_seconds': 681,
      'tip': 'want to show them the sale results, the county list, or court document, and be '
             "transparent about everything. This isn't a secretive business. The more open you "
             'are, the more clients trust you. Finally, to close a deal, o',
      'title': 'How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=suJSu-vn6yI&t=681s',
      'video_id': 'suJSu-vn6yI'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:56:17](https://www.youtube.com/watch?v=Yt91gmZt8sE&t=3377s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "from and so that's where the estate was was determined to have the county the "
              'estate was determined to have um jurisdiction the court was this the court where '
              'the state had where the court had jurisdiction over the estat',
      'timestamp': 3377,
      'timestamp_label': '[00:56:17]',
      'timestamp_seconds': 3377,
      'tip': "from and so that's where the estate was was determined to have the county the estate "
             'was determined to have um jurisdiction the court was this the court where the state '
             'had where the court had jurisdiction over the estat',
      'title': 'Discovering Your Ancestors Using Probate Records- James Tanner (BYU Library Family '
               'History Center)',
      'url': 'https://www.youtube.com/watch?v=Yt91gmZt8sE&t=3377s',
      'video_id': 'Yt91gmZt8sE'},
     {'author': 'Mid-Continent Public Library',
      'channel': 'Mid-Continent Public Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=uAcku9kesK4&t=251s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'own probate court, which is a civil court. Um they can also be found um in the '
              'smaller counties just in the circuit court as in Missouri or county courts. Uh in '
              "Pennsylvania, you're they're orphan courts. Um it's just a ",
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': 'own probate court, which is a civil court. Um they can also be found um in the '
             'smaller counties just in the circuit court as in Missouri or county courts. Uh in '
             "Pennsylvania, you're they're orphan courts. Um it's just a ",
      'title': 'U.S. Probate Records for Genealogy  |  Midwest Genealogy Center (Mid-Continent '
               'Public Library)',
      'url': 'https://www.youtube.com/watch?v=uAcku9kesK4&t=251s',
      'video_id': 'uAcku9kesK4'},
     {'author': 'SurplusFundsRiches',
      'channel': 'SurplusFundsRiches',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=1N1Z99kUvRw&t=25s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "looming on the horizon right now is a tsunami of deaths coming up here's why first "
              "let's look at home ownership rates among the 65 to 74 year olds they have the "
              'highest home ownership rate is almost of almost 80 percent ',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "looming on the horizon right now is a tsunami of deaths coming up here's why first "
             "let's look at home ownership rates among the 65 to 74 year olds they have the "
             'highest home ownership rate is almost of almost 80 percent ',
      'title': 'Surplus Funds: Owner Died - STILL CLAIM! (SurplusFundsRiches)',
      'url': 'https://www.youtube.com/watch?v=1N1Z99kUvRw&t=25s',
      'video_id': '1N1Z99kUvRw'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:00](https://www.youtube.com/watch?v=_RTcaTMOwlY&t=660s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'property ID, the description, um the overall or the amount that account is worth, '
              'and then down below, I always just put total, and then the overall amount right '
              'here. Then right right below here is the claimant address ',
      'timestamp': 660,
      'timestamp_label': '[00:11:00]',
      'timestamp_seconds': 660,
      'tip': 'property ID, the description, um the overall or the amount that account is worth, '
             'and then down below, I always just put total, and then the overall amount right '
             'here. Then right right below here is the claimant address ',
      'title': 'Mastering Unclaimed Funds Contracts: A Complete Beginners Guide (Surplus Funds '
               '101)',
      'url': 'https://www.youtube.com/watch?v=_RTcaTMOwlY&t=660s',
      'video_id': '_RTcaTMOwlY'},
     {'author': 'ohiocommerce',
      'channel': 'ohiocommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:58](https://www.youtube.com/watch?v=GrE0UUh_3BI&t=2218s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "this sometimes I mean not trying to talk for the probate court but I don't know "
              'what the whole real process is but I know we always get that um they can go to the '
              'probate say I have newly discovered assets I need to reop',
      'timestamp': 2218,
      'timestamp_label': '[00:36:58]',
      'timestamp_seconds': 2218,
      'tip': "this sometimes I mean not trying to talk for the probate court but I don't know what "
             'the whole real process is but I know we always get that um they can go to the '
             'probate say I have newly discovered assets I need to reop',
      'title': 'Claiming your Unclaimed Funds (ohiocommerce)',
      'url': 'https://www.youtube.com/watch?v=GrE0UUh_3BI&t=2218s',
      'video_id': 'GrE0UUh_3BI'},
     {'author': 'PA Treasury Department',
      'channel': 'PA Treasury Department',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:09](https://www.youtube.com/watch?v=eRjGqaIOHWI&t=129s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "receive funds via a or direct deposit to your bank account select yes or no let's "
              'walk through these steps to be paid by a after selecting yes you will be presented '
              'with a claimant login screen to register for an account',
      'timestamp': 129,
      'timestamp_label': '[00:02:09]',
      'timestamp_seconds': 129,
      'tip': "receive funds via a or direct deposit to your bank account select yes or no let's "
             'walk through these steps to be paid by a after selecting yes you will be presented '
             'with a claimant login screen to register for an account',
      'title': 'How To File a Claim - PA Treasury Unclaimed Property Tutorial (PA Treasury '
               'Department)',
      'url': 'https://www.youtube.com/watch?v=eRjGqaIOHWI&t=129s',
      'video_id': 'eRjGqaIOHWI'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:10](https://www.youtube.com/watch?v=Dutmzc9gb30&t=850s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "everything, everything's approved, the judge then signs the court orders, and those "
              "court orders get recorded eventually in the county, and if they don't, we have to "
              'get certified copies and record them. But once they ge',
      'timestamp': 850,
      'timestamp_label': '[00:14:10]',
      'timestamp_seconds': 850,
      'tip': "everything, everything's approved, the judge then signs the court orders, and those "
             "court orders get recorded eventually in the county, and if they don't, we have to "
             'get certified copies and record them. But once they ge',
      'title': 'Florida Probate Explained: What Happens When Someone Dies Owning Real Estate? '
               '(Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=Dutmzc9gb30&t=850s',
      'video_id': 'Dutmzc9gb30'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:29](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=569s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'When he finally started grinding, he cold called a 78-year-old claimant, mailed him '
              'real court proof, worked through the client, all of their hesitations, and even '
              'over Christmas, he earned a $12,000 fee on a $83,000 sur',
      'timestamp': 569,
      'timestamp_label': '[00:09:29]',
      'timestamp_seconds': 569,
      'tip': 'When he finally started grinding, he cold called a 78-year-old claimant, mailed him '
             'real court proof, worked through the client, all of their hesitations, and even over '
             'Christmas, he earned a $12,000 fee on a $83,000 sur',
      'title': 'Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=DMdtmrWAO6c&t=569s',
      'video_id': 'DMdtmrWAO6c'},
     {'author': 'Five-minute genealogy',
      'channel': 'Five-minute genealogy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=hsFQHg-SMN4&t=92s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'the county you need. let’s look at Lancaster Cty, Pennsylvania for sources where '
              'the author is something like “Pennsylvania. Orphan’s Court” rather than a person’s '
              "name. When you see a person's name, it means it's a book",
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': 'the county you need. let’s look at Lancaster Cty, Pennsylvania for sources where the '
             'author is something like “Pennsylvania. Orphan’s Court” rather than a person’s name. '
             "When you see a person's name, it means it's a book",
      'title': 'Finding probate records by browsing through images on FamilySearch.org '
               '(Five-minute genealogy)',
      'url': 'https://www.youtube.com/watch?v=hsFQHg-SMN4&t=92s',
      'video_id': 'hsFQHg-SMN4'},
     {'author': 'Allen County Public Library',
      'channel': 'Allen County Public Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:00:09](https://www.youtube.com/watch?v=t_t1v7TPbFA&t=3609s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "actually court record on it. Um but uh yeah, if if there's nobody close um and and "
              "I'll kind of make a caveat with that. So, there could still be an heir at law, but "
              "let's say there's not. I happen to notice a question o",
      'timestamp': 3609,
      'timestamp_label': '[01:00:09]',
      'timestamp_seconds': 3609,
      'tip': "actually court record on it. Um but uh yeah, if if there's nobody close um and and "
             "I'll kind of make a caveat with that. So, there could still be an heir at law, but "
             "let's say there's not. I happen to notice a question o",
      'title': 'What Happens After Death: Finding and Using Probate Records (Allen County Public '
               'Library)',
      'url': 'https://www.youtube.com/watch?v=t_t1v7TPbFA&t=3609s',
      'video_id': 't_t1v7TPbFA'},
     {'author': "California State Controller's Office",
      'channel': "California State Controller's Office",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=1ahhduhMdd0&t=35s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'no Probate was required for an estate, or that the Administrator or Personal '
              'Representative of the estate has provided consent in writing stating the claimant '
              'is entitled to the Unclaimed Property. At the top of the form',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'no Probate was required for an estate, or that the Administrator or Personal '
             'Representative of the estate has provided consent in writing stating the claimant is '
             'entitled to the Unclaimed Property. At the top of the form',
      'title': "Declaration Under Probate Code 13101 Tutorial (California State Controller's "
               'Office)',
      'url': 'https://www.youtube.com/watch?v=1ahhduhMdd0&t=35s',
      'video_id': '1ahhduhMdd0'},
     {'author': "California State Controller's Office",
      'channel': "California State Controller's Office",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=cMCrrRkehJk&t=31s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'with no Will, Trust, or other Estate Plan, and Probate was not required. This form '
              'provides detail about the family of the deceased owner, to determine how any funds '
              'that belonged to the owner should be distributed. At t',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': 'with no Will, Trust, or other Estate Plan, and Probate was not required. This form '
             'provides detail about the family of the deceased owner, to determine how any funds '
             'that belonged to the owner should be distributed. At t',
      'title': "Table of Heirship Tutorial (California State Controller's Office)",
      'url': 'https://www.youtube.com/watch?v=cMCrrRkehJk&t=31s',
      'video_id': 'cMCrrRkehJk'}],
 3: [{'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:38](https://www.youtube.com/watch?v=CyAfgfoF-eo&t=458s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'have adopted a uniform probate code the main reason for adopting the uniform code '
              'was to abolish the percentage attorneys fees charged by attorneys against the '
              'estate historically the attorneys charged a fee of anything ',
      'timestamp': 458,
      'timestamp_label': '[00:07:38]',
      'timestamp_seconds': 458,
      'tip': 'have adopted a uniform probate code the main reason for adopting the uniform code '
             'was to abolish the percentage attorneys fees charged by attorneys against the estate '
             'historically the attorneys charged a fee of anything ',
      'title': 'Probate  Part 2, Wills by James Tanner (BYU Library Family History Center)',
      'url': 'https://www.youtube.com/watch?v=CyAfgfoF-eo&t=458s',
      'video_id': 'CyAfgfoF-eo'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:41](https://www.youtube.com/watch?v=TTMtgtc31k4&t=281s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "will tell you there are some states out there that don't have a state commission "
              "cap in those States I wouldn't go above 40% okay I think 40% is a really really "
              "healthy fee and that's probably more on the top end I I'm u",
      'timestamp': 281,
      'timestamp_label': '[00:04:41]',
      'timestamp_seconds': 281,
      'tip': "will tell you there are some states out there that don't have a state commission cap "
             "in those States I wouldn't go above 40% okay I think 40% is a really really healthy "
             "fee and that's probably more on the top end I I'm u",
      'title': 'How To Become An Unclaimed Property Investigator (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=TTMtgtc31k4&t=281s',
      'video_id': 'TTMtgtc31k4'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:37](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=757s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'talk percentage and never mention dollars. Don\'t say, "Our fee would be about '
              '$4,000." say because this is a legal claim with filing fees and attorneys, our fee '
              'is 25%. And that covers everything. Let them do their own m',
      'timestamp': 757,
      'timestamp_label': '[00:12:37]',
      'timestamp_seconds': 757,
      'tip': 'talk percentage and never mention dollars. Don\'t say, "Our fee would be about '
             '$4,000." say because this is a legal claim with filing fees and attorneys, our fee '
             'is 25%. And that covers everything. Let them do their own m',
      'title': 'Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=DMdtmrWAO6c&t=757s',
      'video_id': 'DMdtmrWAO6c'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=TTfaOSBvLDc&t=320s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'Well, now the state has a 10% commission cap, the commission cap, at least for me, '
              "isn't nearly as important as this bottom part getting bulk leads because he has 10, "
              "20%... That's about standard. There are some states t",
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': 'Well, now the state has a 10% commission cap, the commission cap, at least for me, '
             "isn't nearly as important as this bottom part getting bulk leads because he has 10, "
             "20%... That's about standard. There are some states t",
      'title': 'State Funds Tutorial Delaware: Registering As A Property Locator For The State Of '
               'Delaware. (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=TTfaOSBvLDc&t=320s',
      'video_id': 'TTfaOSBvLDc'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=6yIKsJMj6Gk&t=194s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': '0:03:15.0 S1: Here are the answers, those things... So as far as an investigator '
              'commission capas, usually the biggest thing, how much am I gonna get paid? The '
              "State of New Mexico. They don't have a cap. I know a lot of ",
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': '0:03:15.0 S1: Here are the answers, those things... So as far as an investigator '
             'commission capas, usually the biggest thing, how much am I gonna get paid? The State '
             "of New Mexico. They don't have a cap. I know a lot of ",
      'title': 'State Funds Tutorial New Mexico: How To Register As A Property Locator In The '
               'State Of New Mexico. (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=6yIKsJMj6Gk&t=194s',
      'video_id': '6yIKsJMj6Gk'},
     {'author': 'All The Leads',
      'channel': 'All The Leads',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:22](https://www.youtube.com/watch?v=xumwh2SPKv4&t=1762s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "some don't take anything until the estate's all the way closed and they take a "
              'percentage of um of the state value so they can take a fee out of the estate when '
              "it's settled uh they don't need to be paid up front it's ju",
      'timestamp': 1762,
      'timestamp_label': '[00:29:22]',
      'timestamp_seconds': 1762,
      'tip': "some don't take anything until the estate's all the way closed and they take a "
             'percentage of um of the state value so they can take a fee out of the estate when '
             "it's settled uh they don't need to be paid up front it's ju",
      'title': 'All The Leads Probate Mastermind #447',
      'url': 'https://www.youtube.com/watch?v=xumwh2SPKv4&t=1762s',
      'video_id': 'xumwh2SPKv4'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=FNbqvZGEzeE&t=255s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "understand to be an expert in that county is understanding the state's law is there "
              'any cap on fees that you can charge for surplus funds recovery do they have any '
              'stipulations is there a waiting period do they work with',
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': "understand to be an expert in that county is understanding the state's law is there "
             'any cap on fees that you can charge for surplus funds recovery do they have any '
             'stipulations is there a waiting period do they work with',
      'title': 'How To Become a Surplus Funds Expert FOR 1 COUNTY (Asset Recovery Business) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=FNbqvZGEzeE&t=255s',
      'video_id': 'FNbqvZGEzeE'},
     {'author': 'Security and Investigations Leadership Channel',
      'channel': 'Security and Investigations Leadership Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=nI1xm6ZA2qo&t=87s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "the person that's deceased so the money will go to the state of California "
              "controller's office what you can do as a private investigator is you can do this "
              'you can charge a fee up to 10 percent and find this money for th',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "the person that's deceased so the money will go to the state of California "
             "controller's office what you can do as a private investigator is you can do this you "
             'can charge a fee up to 10 percent and find this money for th',
      'title': '✅ 💰 CALIFORNIA Unclaimed Property Investigations - Tips from a Licensed Private '
               'Investigator! (Security and Investigations Leadership Channel)',
      'url': 'https://www.youtube.com/watch?v=nI1xm6ZA2qo&t=87s',
      'video_id': 'nI1xm6ZA2qo'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=RmtbOq_vtuU&t=25s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'with Florida real estate attorney who focuses on probate. His name is Al Nicoleti. '
              "Maybe you've heard of him. Al does a great job talking about all things probate and "
              'even the curative world. And yes, he is a Florida att',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'with Florida real estate attorney who focuses on probate. His name is Al Nicoleti. '
             "Maybe you've heard of him. Al does a great job talking about all things probate and "
             'even the curative world. And yes, he is a Florida att',
      'title': 'How to Find Heirs for a Florida Probate Property (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=RmtbOq_vtuU&t=25s',
      'video_id': 'RmtbOq_vtuU'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:06](https://www.youtube.com/watch?v=1BlzkVdGPAo&t=426s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "Of course. And what can you tell them? It's not that bad. It's not as bad as you "
              "think. How valuable is that? Pretty valuable! Yeah, I think it's pretty valuable. "
              "And if an attorney has a client, you think they're, they'",
      'timestamp': 426,
      'timestamp_label': '[00:07:06]',
      'timestamp_seconds': 426,
      'tip': "Of course. And what can you tell them? It's not that bad. It's not as bad as you "
             "think. How valuable is that? Pretty valuable! Yeah, I think it's pretty valuable. "
             "And if an attorney has a client, you think they're, they'",
      'title': 'I got free probate leads from the courthouse! Plus SOI and referral marketing | '
               'Podcast Episode 85 (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=1BlzkVdGPAo&t=426s',
      'video_id': '1BlzkVdGPAo'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:48](https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=2808s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "gone, antidotal knowledge. You don't know how we would write a contract or a how to "
              "negotiate to a fees or even work with title or make sure it's even many to close or "
              'not. So the real estate knowledge is missing, but yo',
      'timestamp': 2808,
      'timestamp_label': '[00:46:48]',
      'timestamp_seconds': 2808,
      'tip': "gone, antidotal knowledge. You don't know how we would write a contract or a how to "
             "negotiate to a fees or even work with title or make sure it's even many to close or "
             'not. So the real estate knowledge is missing, but yo',
      'title': 'Differentiating Yourself From The Competition: How To HASHTAG Your ELEVATOR PITCH '
               '|  #10 (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=OrEz4Qk-EZ0&t=2808s',
      'video_id': 'OrEz4Qk-EZ0'},
     {'author': 'FarmersGov',
      'channel': 'FarmersGov',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:18](https://www.youtube.com/watch?v=whDzDrFNADQ&t=378s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'what guidance, would you share with them on how to select that attorney and vet '
              "them. So that's always tricky so one of the issues that we run into with heir "
              "property is. there's No two pieces of land in the entire world",
      'timestamp': 378,
      'timestamp_label': '[00:06:18]',
      'timestamp_seconds': 378,
      'tip': 'what guidance, would you share with them on how to select that attorney and vet '
             "them. So that's always tricky so one of the issues that we run into with heir "
             "property is. there's No two pieces of land in the entire world",
      'title': 'USDA FSA Resources for Heirs: Join FSA as we talk with the Experts (Episode 1-Full '
               'Version) (FarmersGov)',
      'url': 'https://www.youtube.com/watch?v=whDzDrFNADQ&t=378s',
      'video_id': 'whDzDrFNADQ'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:03](https://www.youtube.com/watch?v=GK-4kFznJlA&t=1503s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "legal fees or catch up on some bills. >> Yeah, exactly. Yeah, he's not coming back "
              'here and there [clears throat] was no way for him to legally work that deal, but '
              'the client was able to to make it happen and so he was h',
      'timestamp': 1503,
      'timestamp_label': '[00:25:03]',
      'timestamp_seconds': 1503,
      'tip': "legal fees or catch up on some bills. >> Yeah, exactly. Yeah, he's not coming back "
             'here and there [clears throat] was no way for him to legally work that deal, but the '
             'client was able to to make it happen and so he was h',
      'title': 'How Ex-FBI Agents Skip Trace Anyone for Real Estate Deals (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=GK-4kFznJlA&t=1503s',
      'video_id': 'GK-4kFznJlA'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=336s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'important, because if your fee is too high, the entire agreement can get thrown '
              'out. Next, you need one of the two things, either an assignment of interest where '
              'the owner hands their claim fully over to you, or a limite',
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'important, because if your fee is too high, the entire agreement can get thrown out. '
             'Next, you need one of the two things, either an assignment of interest where the '
             'owner hands their claim fully over to you, or a limite',
      'title': 'Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=336s',
      'video_id': 'MVCNlj7HQBQ'},
     {'author': 'Five-minute genealogy',
      'channel': 'Five-minute genealogy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=pGyFJ46jwTE&t=163s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'it could or could not be split up. If it couldn’t be partitioned, Jacob could '
              'buy-out his siblings’ share of their fathers’ real estate. It’s hard to provide '
              'specific advice here, since every state will have different la',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'it could or could not be split up. If it couldn’t be partitioned, Jacob could '
             'buy-out his siblings’ share of their fathers’ real estate. It’s hard to provide '
             'specific advice here, since every state will have different la',
      'title': 'Primary sources: Intestate probate documents (Five-minute genealogy)',
      'url': 'https://www.youtube.com/watch?v=pGyFJ46jwTE&t=163s',
      'video_id': 'pGyFJ46jwTE'}],
 4: [{'author': 'Genealogy TV',
      'channel': 'Genealogy TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=10DuXkEoTRA&t=203s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'open this up because we always want to drill into the actual record. And this is '
              "the same information that I have already captured. So, we have an administrator's "
              'bond and a guardian bond. Now, I had already transcribed ',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'open this up because we always want to drill into the actual record. And this is the '
             "same information that I have already captured. So, we have an administrator's bond "
             'and a guardian bond. Now, I had already transcribed ',
      'title': 'Targeted Genealogical Research: Probate Example (Genealogy TV)',
      'url': 'https://www.youtube.com/watch?v=10DuXkEoTRA&t=203s',
      'video_id': '10DuXkEoTRA'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:38](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=698s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'other entity records birth before and for a time period after the death of the '
              'ancestor you can really find that the probate actions could be filed up two years '
              'after the date of death sometimes the heirs simply did not ',
      'timestamp': 698,
      'timestamp_label': '[00:11:38]',
      'timestamp_seconds': 698,
      'tip': 'other entity records birth before and for a time period after the death of the '
             'ancestor you can really find that the probate actions could be filed up two years '
             'after the date of death sometimes the heirs simply did not ',
      'title': 'Probate   Part 6  "Finding Probate Documents" by James Tanner (BYU Library Family '
               'History Center)',
      'url': 'https://www.youtube.com/watch?v=oZiYbKNvxJY&t=698s',
      'video_id': 'oZiYbKNvxJY'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:28](https://www.youtube.com/watch?v=07zaZ3sQwi8&t=388s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'the court required a bond of the the deceased wife that would not be the practice '
              'and the courts more or current court proceedings it would have ever it would be '
              'however in older court probate matters would have been the',
      'timestamp': 388,
      'timestamp_label': '[00:06:28]',
      'timestamp_seconds': 388,
      'tip': 'the court required a bond of the the deceased wife that would not be the practice '
             'and the courts more or current court proceedings it would have ever it would be '
             'however in older court probate matters would have been the',
      'title': 'Probate  Part 7, "Example of a Probate File" by James Tanner (BYU Library Family '
               'History Center)',
      'url': 'https://www.youtube.com/watch?v=07zaZ3sQwi8&t=388s',
      'video_id': '07zaZ3sQwi8'},
     {'author': 'Allen County Public Library',
      'channel': 'Allen County Public Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:51](https://www.youtube.com/watch?v=t_t1v7TPbFA&t=651s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'the executor of the will. Well, you the court may require you to post a bond and '
              "actually pony up some money to the court that they're going to hang on to just in "
              "case you don't actually fulfill your duties. One way to g",
      'timestamp': 651,
      'timestamp_label': '[00:10:51]',
      'timestamp_seconds': 651,
      'tip': 'the executor of the will. Well, you the court may require you to post a bond and '
             "actually pony up some money to the court that they're going to hang on to just in "
             "case you don't actually fulfill your duties. One way to g",
      'title': 'What Happens After Death: Finding and Using Probate Records (Allen County Public '
               'Library)',
      'url': 'https://www.youtube.com/watch?v=t_t1v7TPbFA&t=651s',
      'video_id': 't_t1v7TPbFA'},
     {'author': 'Emend The Mass Media Group',
      'channel': 'Emend The Mass Media Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=ijLtjR0tTd8&t=91s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'financial institutions, and insurance companies referred to as holders to annually '
              "report and deliver property to the state controllers's office if there has been no "
              'activity on the [music] account or contract or contact',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'financial institutions, and insurance companies referred to as holders to annually '
             "report and deliver property to the state controllers's office if there has been no "
             'activity on the [music] account or contract or contact',
      'title': 'CA Unclaimed Property - Are you missing out? - Tutorial (Emend The Mass Media '
               'Group)',
      'url': 'https://www.youtube.com/watch?v=ijLtjR0tTd8&t=91s',
      'video_id': 'ijLtjR0tTd8'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=Qn63DtrxFts&t=124s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'would suggest doing is creating an event on your Google Calendar once a week where '
              'you spend 15 to 30 minutes just finding new notaries. You know, um and then have '
              'have that event have notifications and reminders to make',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'would suggest doing is creating an event on your Google Calendar once a week where '
             'you spend 15 to 30 minutes just finding new notaries. You know, um and then have '
             'have that event have notifications and reminders to make',
      'title': 'How to Build a Nationwide Notary Team (Step-by-Step) (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=Qn63DtrxFts&t=124s',
      'video_id': 'Qn63DtrxFts'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:43](https://www.youtube.com/watch?v=_8vyoTSh7Rs&t=403s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'One of the other questions I get, do I need to have an LLC or a business will? In '
              "the state of California, you don't... You can put all these deals in your own name, "
              'I always suggest, once you have some money coming in, ',
      'timestamp': 403,
      'timestamp_label': '[00:06:43]',
      'timestamp_seconds': 403,
      'tip': 'One of the other questions I get, do I need to have an LLC or a business will? In '
             "the state of California, you don't... You can put all these deals in your own name, "
             'I always suggest, once you have some money coming in, ',
      'title': 'State Funds California: Registration Process & Requirements To Work Unclaimed '
               'Funds. (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=_8vyoTSh7Rs&t=403s',
      'video_id': '_8vyoTSh7Rs'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:59](https://www.youtube.com/watch?v=W5g3Gia5jX4&t=1079s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "foreclosures, um with tax auctions, uh tax liens, things like that. You've got "
              'broken chains of title, uh whether this, you know, something was not deeded '
              'properly. You could have a bad legal description, uh notary issue',
      'timestamp': 1079,
      'timestamp_label': '[00:17:59]',
      'timestamp_seconds': 1079,
      'tip': "foreclosures, um with tax auctions, uh tax liens, things like that. You've got "
             'broken chains of title, uh whether this, you know, something was not deeded '
             'properly. You could have a bad legal description, uh notary issue',
      'title': 'How I Actually Find Curative Title Leads (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=W5g3Gia5jX4&t=1079s',
      'video_id': 'W5g3Gia5jX4'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:12](https://www.youtube.com/watch?v=GH5TN_iIdMs&t=252s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "where they can't sell their property because they can't, you know, they don't know "
              "who owns it or there's some lean on there that they don't know how to get rid of. "
              "So that's kind of my my elevator pitch for that. >> And",
      'timestamp': 252,
      'timestamp_label': '[00:04:12]',
      'timestamp_seconds': 252,
      'tip': "where they can't sell their property because they can't, you know, they don't know "
             "who owns it or there's some lean on there that they don't know how to get rid of. So "
             "that's kind of my my elevator pitch for that. >> And",
      'title': 'Curative Title Explained: How Investors Make Money When Deals Can’t Close '
               '(Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=GH5TN_iIdMs&t=252s',
      'video_id': 'GH5TN_iIdMs'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=EVN-9bqTEtM&t=94s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "i'll want to extract it into a regular folder and you can see here that shapefiles "
              "come in a multi-file setup so what i'll do is i'll select all and now i'm going to "
              "tab over to my blank arc project and i'll simply click",
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "i'll want to extract it into a regular folder and you can see here that shapefiles "
             "come in a multi-file setup so what i'll do is i'll select all and now i'm going to "
             "tab over to my blank arc project and i'll simply click",
      'title': 'Exporting Regrid Data to ArcGIS - Regrid Property App (Web)',
      'url': 'https://www.youtube.com/watch?v=EVN-9bqTEtM&t=94s',
      'video_id': 'EVN-9bqTEtM'},
     {'author': 'MD Ag Law Education Initiative',
      'channel': 'MD Ag Law Education Initiative',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:58:12](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=3492s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'So now, heirs property owners can also decide to form a business entity like an '
              'LLC, a limited liability company, or a corporation. and transfer the property to '
              'the LLC or corporation. And there are fees, right, for...',
      'timestamp': 3492,
      'timestamp_label': '[00:58:12]',
      'timestamp_seconds': 3492,
      'tip': 'So now, heirs property owners can also decide to form a business entity like an LLC, '
             'a limited liability company, or a corporation. and transfer the property to the LLC '
             'or corporation. And there are fees, right, for...',
      'title': "Resolving Heirs' Property (MD Ag Law Education Initiative)",
      'url': 'https://www.youtube.com/watch?v=TP6n8TBsCGs&t=3492s',
      'video_id': 'TP6n8TBsCGs'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:55](https://www.youtube.com/watch?v=ES6y4iF-bBM&t=355s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "0:05:56.0 S2: The regardless of professional email address, you guys... It's not "
              'gonna cost you anything to do. It really helps out merrier 0:06:06.1 S1: Area and '
              'basic office supplies. When you were talking to people on',
      'timestamp': 355,
      'timestamp_label': '[00:05:55]',
      'timestamp_seconds': 355,
      'tip': "0:05:56.0 S2: The regardless of professional email address, you guys... It's not "
             'gonna cost you anything to do. It really helps out merrier 0:06:06.1 S1: Area and '
             'basic office supplies. When you were talking to people on',
      'title': 'State Funds Tutorial: 5 Tech Tools For Your State Funds Business (Surplus Funds '
               '101)',
      'url': 'https://www.youtube.com/watch?v=ES6y4iF-bBM&t=355s',
      'video_id': 'ES6y4iF-bBM'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:22](https://www.youtube.com/watch?v=2agNOU2taXA&t=1582s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "ATM. You can't always be taking withdrawals. you you've got a deposit as well. Were "
              'there any costs that were unknown in in the transaction for you? >> I mean the like '
              'I mean there were no costs or unknown but like the a',
      'timestamp': 1582,
      'timestamp_label': '[00:26:22]',
      'timestamp_seconds': 1582,
      'tip': "ATM. You can't always be taking withdrawals. you you've got a deposit as well. Were "
             'there any costs that were unknown in in the transaction for you? >> I mean the like '
             'I mean there were no costs or unknown but like the a',
      'title': 'Curative Title for Wholesalers: How He Turned a Dead Lead Into a Deal (Courtney '
               'Fricke)',
      'url': 'https://www.youtube.com/watch?v=2agNOU2taXA&t=1582s',
      'video_id': '2agNOU2taXA'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=coUYfNbBvq0&t=217s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "a first mortgage or how are you carrying these? Christie: Yeah, no, they're "
              "literally just signing a contract. They're not party to the LLC and they're not "
              "well in one of them, they are in another, we have two others we'",
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': "a first mortgage or how are you carrying these? Christie: Yeah, no, they're "
             "literally just signing a contract. They're not party to the LLC and they're not well "
             "in one of them, they are in another, we have two others we'",
      'title': 'How to JV a probate deal with the estate as your partner | Probate Investing | '
               'Chad Corbett Probate (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=coUYfNbBvq0&t=217s',
      'video_id': 'coUYfNbBvq0'},
     {'author': 'NOLA City Archives',
      'channel': 'NOLA City Archives',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:09](https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=309s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'necessarily allowed in the process of law so I do recommend that everybody when '
              "they get their Wills done if they actually go to a notary or a lawyer who's uh very "
              'knowledgeable about writing well what happens if you die',
      'timestamp': 309,
      'timestamp_label': '[00:05:09]',
      'timestamp_seconds': 309,
      'tip': 'necessarily allowed in the process of law so I do recommend that everybody when they '
             "get their Wills done if they actually go to a notary or a lawyer who's uh very "
             'knowledgeable about writing well what happens if you die',
      'title': "Heirs' Property with Jonathan Reynolds of Louisiana Appleseed (NOLA City Archives)",
      'url': 'https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=309s',
      'video_id': 'JPgk0Y7ZzuY'}],
 5: [{'author': 'Ted Thomas',
      'channel': 'Ted Thomas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:54](https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=174s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'All right. So you wanna learn to do the basic research. All right. Now all of of '
              'these liens will stay on the property, except the title report will show that the '
              'deed of trust lien, and the mortgage, will be wiped out. ',
      'timestamp': 174,
      'timestamp_label': '[00:02:54]',
      'timestamp_seconds': 174,
      'tip': 'All right. So you wanna learn to do the basic research. All right. Now all of of '
             'these liens will stay on the property, except the title report will show that the '
             'deed of trust lien, and the mortgage, will be wiped out. ',
      'title': 'How To Do A Title Search On A Property Yourself Before You Bid At Tax Sale '
               'Auctions (Ted Thomas)',
      'url': 'https://www.youtube.com/watch?v=xtdWFaJY8Xc&t=174s',
      'video_id': 'xtdWFaJY8Xc'},
     {'author': 'HeirSearch',
      'channel': 'HeirSearch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=aOXjjN53MT8&t=39s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "of the listed relatives surviving them we must determine the decedent's lawful "
              'heirs one helpful tool for this purpose is our consanguinity chart this chart '
              'outlines the relation between a decedent and their family membe',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "of the listed relatives surviving them we must determine the decedent's lawful heirs "
             'one helpful tool for this purpose is our consanguinity chart this chart outlines the '
             'relation between a decedent and their family membe',
      'title': 'HeirSearch | Consanguinity Chart Walk-Through',
      'url': 'https://www.youtube.com/watch?v=aOXjjN53MT8&t=39s',
      'video_id': 'aOXjjN53MT8'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:08](https://www.youtube.com/watch?v=l8J2d1WwudY&t=1688s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "heirs to file for the claim? Sometimes they don't need all this courtappointed "
              'stuff. They just need all of the heirs to approve and death certificate. All right? '
              'And also understand that this is a very typical scenario ',
      'timestamp': 1688,
      'timestamp_label': '[00:28:08]',
      'timestamp_seconds': 1688,
      'tip': "heirs to file for the claim? Sometimes they don't need all this courtappointed "
             'stuff. They just need all of the heirs to approve and death certificate. All right? '
             'And also understand that this is a very typical scenario ',
      'title': 'How To Work Deceased Claims - Step-By-Step (Surplus Funds Recovery) (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=l8J2d1WwudY&t=1688s',
      'video_id': 'l8J2d1WwudY'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:20](https://www.youtube.com/watch?v=coUYfNbBvq0&t=680s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "Chad Corbett: That's why I'm suggesting that because we want to have clear general "
              'warranty deed proof out. The only lien we hope that comes up is that one first '
              "mortgage four for 60,000 bucks. If that's the case, then t",
      'timestamp': 680,
      'timestamp_label': '[00:11:20]',
      'timestamp_seconds': 680,
      'tip': "Chad Corbett: That's why I'm suggesting that because we want to have clear general "
             'warranty deed proof out. The only lien we hope that comes up is that one first '
             "mortgage four for 60,000 bucks. If that's the case, then t",
      'title': 'How to JV a probate deal with the estate as your partner | Probate Investing | '
               'Chad Corbett Probate (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=coUYfNbBvq0&t=680s',
      'video_id': 'coUYfNbBvq0'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=pQwwvYbUYrU&t=203s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "a wetland or an environmental issue. Maybe there's a phantom mortgage or liens or "
              "code enforcement or back taxes. Maybe it's going up for auction. There's so many "
              'things to know and think about with a probate deal becaus',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': "a wetland or an environmental issue. Maybe there's a phantom mortgage or liens or "
             "code enforcement or back taxes. Maybe it's going up for auction. There's so many "
             'things to know and think about with a probate deal becaus',
      'title': 'The Probate Mistake New Real Estate Investors Make (Florida Attorney Case Study) '
               '(Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=pQwwvYbUYrU&t=203s',
      'video_id': 'pQwwvYbUYrU'},
     {'author': 'NOLA City Archives',
      'channel': 'NOLA City Archives',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:09](https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=369s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "should the person not have parents and siblings a surviving spouse and then that's "
              'when we get into the whole big family tree if a person is having these things '
              "that's where we get into like a Brewster's Millions type si",
      'timestamp': 369,
      'timestamp_label': '[00:06:09]',
      'timestamp_seconds': 369,
      'tip': "should the person not have parents and siblings a surviving spouse and then that's "
             "when we get into the whole big family tree if a person is having these things that's "
             "where we get into like a Brewster's Millions type si",
      'title': "Heirs' Property with Jonathan Reynolds of Louisiana Appleseed (NOLA City Archives)",
      'url': 'https://www.youtube.com/watch?v=JPgk0Y7ZzuY&t=369s',
      'video_id': 'JPgk0Y7ZzuY'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:21](https://www.youtube.com/watch?v=lKsfBAioCYU&t=801s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'price down to release the property, not the owner, not the owner. The owner is '
              'still subject to IRS liens. Exactly, partial release from the from the property '
              "itself. >> So for people that don't understand that means the",
      'timestamp': 801,
      'timestamp_label': '[00:13:21]',
      'timestamp_seconds': 801,
      'tip': 'price down to release the property, not the owner, not the owner. The owner is still '
             'subject to IRS liens. Exactly, partial release from the from the property itself. >> '
             "So for people that don't understand that means the",
      'title': 'Title Search Explained: The Hidden Liens Investors Miss (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=lKsfBAioCYU&t=801s',
      'video_id': 'lKsfBAioCYU'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=q95klfFm9mE&t=235s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "mortgage foreclosure side in Florida they're limited to 60 days so you're going to "
              "have to reach out to your county you're going to have to ask them a few questions "
              'you can call them you can email them and you can figure',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': "mortgage foreclosure side in Florida they're limited to 60 days so you're going to "
             "have to reach out to your county you're going to have to ask them a few questions "
             'you can call them you can email them and you can figure',
      'title': "2 Ways To Check If There's a Lien On a Property (For Surplus Funds Recovery) "
               '(Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=q95klfFm9mE&t=235s',
      'video_id': 'q95klfFm9mE'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:52](https://www.youtube.com/watch?v=7120UjJPqZM&t=172s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'probate cases involve disagreements among the heirs or even issues raised by third '
              'parties such as creditors in these cases the court treats the will contest matter '
              'or the probate matter just as they would any other laws',
      'timestamp': 172,
      'timestamp_label': '[00:02:52]',
      'timestamp_seconds': 172,
      'tip': 'probate cases involve disagreements among the heirs or even issues raised by third '
             'parties such as creditors in these cases the court treats the will contest matter or '
             'the probate matter just as they would any other laws',
      'title': 'Probate  Part 3,  "Wording of Wills"  by James Tanner (BYU Library Family History '
               'Center)',
      'url': 'https://www.youtube.com/watch?v=7120UjJPqZM&t=172s',
      'video_id': '7120UjJPqZM'},
     {'author': 'My Lawyer In Spain',
      'channel': 'My Lawyer In Spain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:18](https://www.youtube.com/watch?v=ywaYY4cPtAY&t=1338s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "of client that comes to you first. If it's an heir that comes to you or someone "
              "who's got an empty property, can you just explain, you know, what what charges so "
              "that people don't don't because I mean when they come to l",
      'timestamp': 1338,
      'timestamp_label': '[00:22:18]',
      'timestamp_seconds': 1338,
      'tip': "of client that comes to you first. If it's an heir that comes to you or someone "
             "who's got an empty property, can you just explain, you know, what what charges so "
             "that people don't don't because I mean when they come to l",
      'title': 'Unclaimed Estates & Abandoned Properties in Spain - tracing Heirs Worldwide (My '
               'Lawyer In Spain)',
      'url': 'https://www.youtube.com/watch?v=ywaYY4cPtAY&t=1338s',
      'video_id': 'ywaYY4cPtAY'},
     {'author': 'Gary Foster',
      'channel': 'Gary Foster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:31](https://www.youtube.com/watch?v=Xzst9ZSC1M0&t=331s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'make sure that all of the heirs in the will have been contacted and have received '
              'the assets that were given to them and have signed or received a receipt for those '
              'a primary air or a friend of the court petitions to pro',
      'timestamp': 331,
      'timestamp_label': '[00:05:31]',
      'timestamp_seconds': 331,
      'tip': 'make sure that all of the heirs in the will have been contacted and have received '
             'the assets that were given to them and have signed or received a receipt for those a '
             'primary air or a friend of the court petitions to pro',
      'title': 'Using Land and Probate Records in Family History Research Laurie Bradshaw (Gary '
               'Foster)',
      'url': 'https://www.youtube.com/watch?v=Xzst9ZSC1M0&t=331s',
      'video_id': 'Xzst9ZSC1M0'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:09](https://www.youtube.com/watch?v=5LDDkiUTmXI&t=189s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'attorneys. Um well, first of all, explain his family situation, you know, my sister '
              'died then her son died, you know, and so there\'s heirs I don\'t understand." So, '
              'that\'s we got and then I said, "Well, what have you guys',
      'timestamp': 189,
      'timestamp_label': '[00:03:09]',
      'timestamp_seconds': 189,
      'tip': 'attorneys. Um well, first of all, explain his family situation, you know, my sister '
             'died then her son died, you know, and so there\'s heirs I don\'t understand." So, '
             'that\'s we got and then I said, "Well, what have you guys',
      'title': "How a Curative Title Investor Finds & Solves Deals Others Can't (Courtney Fricke)",
      'url': 'https://www.youtube.com/watch?v=5LDDkiUTmXI&t=189s',
      'video_id': '5LDDkiUTmXI'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:53](https://www.youtube.com/watch?v=FgFrlIpbscs&t=473s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'hedge funds. Um but, the ones that we do have, a lot of them deal in the tax lien '
              'space in Louisiana because of the interest you can earn. And I had heard before '
              'that by attending local investor meetups, by working netwo',
      'timestamp': 473,
      'timestamp_label': '[00:07:53]',
      'timestamp_seconds': 473,
      'tip': 'hedge funds. Um but, the ones that we do have, a lot of them deal in the tax lien '
             'space in Louisiana because of the interest you can earn. And I had heard before that '
             'by attending local investor meetups, by working netwo',
      'title': 'How to Find Curative Title Deals Nobody Else Is Chasing (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=FgFrlIpbscs&t=473s',
      'video_id': 'FgFrlIpbscs'},
     {'author': 'LSBA Access To Justice',
      'channel': 'LSBA Access To Justice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:39](https://www.youtube.com/watch?v=59C1meISvlc&t=339s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'people would want their property to go should they pass okay the state of Louisiana '
              "says should a person pass and they don't have a will their property goes to their "
              'descendants your descendants would be your children or',
      'timestamp': 339,
      'timestamp_label': '[00:05:39]',
      'timestamp_seconds': 339,
      'tip': 'people would want their property to go should they pass okay the state of Louisiana '
             "says should a person pass and they don't have a will their property goes to their "
             'descendants your descendants would be your children or',
      'title': "Law Talks: Heirs' Property 1-21-2025 (LSBA Access To Justice)",
      'url': 'https://www.youtube.com/watch?v=59C1meISvlc&t=339s',
      'video_id': '59C1meISvlc'},
     {'author': 'Farm Aid',
      'channel': 'Farm Aid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:27:20](https://www.youtube.com/watch?v=OODJe43FyEs&t=5240s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'of local to their state or region. Um so I think it it will depend on which '
              "university um maybe >> okay and we'll definitely make sure that everybody has "
              "access to the slides um and that you all have uh you'll be able to",
      'timestamp': 5240,
      'timestamp_label': '[01:27:20]',
      'timestamp_seconds': 5240,
      'tip': 'of local to their state or region. Um so I think it it will depend on which '
             "university um maybe >> okay and we'll definitely make sure that everybody has access "
             "to the slides um and that you all have uh you'll be able to",
      'title': "Heirs' Property Training (Webinar from DBAN) (Farm Aid)",
      'url': 'https://www.youtube.com/watch?v=OODJe43FyEs&t=5240s',
      'video_id': 'OODJe43FyEs'}],
 6: [{'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:04](https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=184s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'business. Now you guys, I have a lot of people that just massively talk manual '
              "search leads. And I get it. You don't have the leverage button you can tap with "
              'manually search leads, but you can get so much data on one in',
      'timestamp': 184,
      'timestamp_label': '[00:03:04]',
      'timestamp_seconds': 184,
      'tip': 'business. Now you guys, I have a lot of people that just massively talk manual '
             "search leads. And I get it. You don't have the leverage button you can tap with "
             'manually search leads, but you can get so much data on one in',
      'title': 'Unclaimed Funds: Lead Sourcing Masterclass (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=184s',
      'video_id': 'h4Qz3EvAAnw'},
     {'author': 'Ancestry',
      'channel': 'Ancestry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:32](https://www.youtube.com/watch?v=lOmly79G2Tk&t=212s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "docket volume four and five. I'm interested in docket 5. So I'm going to go ahead "
              'and click on this. It takes me to the very first page of that particular set of '
              'images. What I need to do is use the film strip navigation',
      'timestamp': 212,
      'timestamp_label': '[00:03:32]',
      'timestamp_seconds': 212,
      'tip': "docket volume four and five. I'm interested in docket 5. So I'm going to go ahead "
             'and click on this. It takes me to the very first page of that particular set of '
             'images. What I need to do is use the film strip navigation',
      'title': "Finding Probate Records That Aren't Indexed | Ancestry",
      'url': 'https://www.youtube.com/watch?v=lOmly79G2Tk&t=212s',
      'video_id': 'lOmly79G2Tk'},
     {'author': 'Five-minute genealogy',
      'channel': 'Five-minute genealogy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:05](https://www.youtube.com/watch?v=hsFQHg-SMN4&t=185s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'more complicated than in Lancaster. The case number here is pretty important: '
              'Belmont County put most probate records into files by decedent, though wills are '
              'still recorded chronologically in books like they were in Lan',
      'timestamp': 185,
      'timestamp_label': '[00:03:05]',
      'timestamp_seconds': 185,
      'tip': 'more complicated than in Lancaster. The case number here is pretty important: '
             'Belmont County put most probate records into files by decedent, though wills are '
             'still recorded chronologically in books like they were in Lan',
      'title': 'Finding probate records by browsing through images on FamilySearch.org '
               '(Five-minute genealogy)',
      'url': 'https://www.youtube.com/watch?v=hsFQHg-SMN4&t=185s',
      'video_id': 'hsFQHg-SMN4'},
     {'author': 'The Genealogy Professional Podcast',
      'channel': 'The Genealogy Professional Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:43](https://www.youtube.com/watch?v=7v_UB7hKgKg&t=343s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'record repositories one in the National Library one the National Archives so '
              'oftentimes people list themselves on those lists to get themselves going with '
              "clients but you don't have to register we're trading as is the ex",
      'timestamp': 343,
      'timestamp_label': '[00:05:43]',
      'timestamp_seconds': 343,
      'tip': 'record repositories one in the National Library one the National Archives so '
             'oftentimes people list themselves on those lists to get themselves going with '
             "clients but you don't have to register we're trading as is the ex",
      'title': "TGP 19 - Eileen O'Duill - Probate Research (The Genealogy Professional Podcast)",
      'url': 'https://www.youtube.com/watch?v=7v_UB7hKgKg&t=343s',
      'video_id': '7v_UB7hKgKg'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:00](https://www.youtube.com/watch?v=Gwcf300h1sA&t=1860s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'the same for Wales and the family research Wiki refers you to search just in Wales '
              'not the counties for probate information but it does list the counties and their '
              'corresponding courts ancestry.com has 282,000 99 records',
      'timestamp': 1860,
      'timestamp_label': '[00:31:00]',
      'timestamp_seconds': 1860,
      'tip': 'the same for Wales and the family research Wiki refers you to search just in Wales '
             'not the counties for probate information but it does list the counties and their '
             'corresponding courts ancestry.com has 282,000 99 records',
      'title': 'Finding Wills in England and Wales Online, Part 3: Ecclesiastical Probate Courts, '
               'pre-1858 (3-24) (BYU Library Family History Center)',
      'url': 'https://www.youtube.com/watch?v=Gwcf300h1sA&t=1860s',
      'video_id': 'Gwcf300h1sA'},
     {'author': 'FamilySearch',
      'channel': 'FamilySearch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:15](https://www.youtube.com/watch?v=Gv4Mibtn8CM&t=495s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'buying are they family names that you know make a list of all the people who '
              'participated in the sales and see where they fit in the family did neighbors come '
              'to buy you may be able to find these people in the census now',
      'timestamp': 495,
      'timestamp_label': '[00:08:15]',
      'timestamp_seconds': 495,
      'tip': 'buying are they family names that you know make a list of all the people who '
             'participated in the sales and see where they fit in the family did neighbors come to '
             'buy you may be able to find these people in the census now',
      'title': "Analyzing Probate Records: Finding Our Ancestor's Stories (FamilySearch)",
      'url': 'https://www.youtube.com/watch?v=Gv4Mibtn8CM&t=495s',
      'video_id': 'Gv4Mibtn8CM'},
     {'author': 'Ancestry',
      'channel': 'Ancestry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:56](https://www.youtube.com/watch?v=bcOlApV2Fng&t=236s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'database states that they started keeping records in 17 98 does not mean that every '
              'single county has records back to that particular date okay every county is going '
              'to have a different date range within that same time p',
      'timestamp': 236,
      'timestamp_label': '[00:03:56]',
      'timestamp_seconds': 236,
      'tip': 'database states that they started keeping records in 17 98 does not mean that every '
             'single county has records back to that particular date okay every county is going to '
             'have a different date range within that same time p',
      'title': 'Getting Started With Probate Records | Ancestry',
      'url': 'https://www.youtube.com/watch?v=bcOlApV2Fng&t=236s',
      'video_id': 'bcOlApV2Fng'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:23](https://www.youtube.com/watch?v=2agNOU2taXA&t=323s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "up and list it, we don't argue with them because they might. Some people do, but "
              "you know, I've been doing this business a while. I have learned that lots don't. "
              'So, so we will follow up just to see what happens cuz we k',
      'timestamp': 323,
      'timestamp_label': '[00:05:23]',
      'timestamp_seconds': 323,
      'tip': "up and list it, we don't argue with them because they might. Some people do, but you "
             "know, I've been doing this business a while. I have learned that lots don't. So, so "
             'we will follow up just to see what happens cuz we k',
      'title': 'Curative Title for Wholesalers: How He Turned a Dead Lead Into a Deal (Courtney '
               'Fricke)',
      'url': 'https://www.youtube.com/watch?v=2agNOU2taXA&t=323s',
      'video_id': '2agNOU2taXA'},
     {'author': 'probatedata',
      'channel': 'probatedata',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:38](https://www.youtube.com/watch?v=AZazHyPY6xU&t=278s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "and to get it up to 100. What's the filter you guys recommend I use to get it to "
              "100? [snorts] And then Ronald, I'll answer your question a minute. Ronald's asking, "
              "can you modify by zip code? The answer is yes. Pete's s",
      'timestamp': 278,
      'timestamp_label': '[00:04:38]',
      'timestamp_seconds': 278,
      'tip': "and to get it up to 100. What's the filter you guys recommend I use to get it to "
             "100? [snorts] And then Ronald, I'll answer your question a minute. Ronald's asking, "
             "can you modify by zip code? The answer is yes. Pete's s",
      'title': 'How to Find the Best Probate Leads First (probatedata)',
      'url': 'https://www.youtube.com/watch?v=AZazHyPY6xU&t=278s',
      'video_id': 'AZazHyPY6xU'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:05](https://www.youtube.com/watch?v=oZiYbKNvxJY&t=425s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'tremendous effort going forward to digitize and make records available online that '
              'may be different between two counties one County and the state may have their '
              'records digitized whereas another County in the same state ',
      'timestamp': 425,
      'timestamp_label': '[00:07:05]',
      'timestamp_seconds': 425,
      'tip': 'tremendous effort going forward to digitize and make records available online that '
             'may be different between two counties one County and the state may have their '
             'records digitized whereas another County in the same state ',
      'title': 'Probate   Part 6  "Finding Probate Documents" by James Tanner (BYU Library Family '
               'History Center)',
      'url': 'https://www.youtube.com/watch?v=oZiYbKNvxJY&t=425s',
      'video_id': 'oZiYbKNvxJY'},
     {'author': 'NALP - National Association of Licenced Paralegals',
      'channel': 'NALP - National Association of Licenced Paralegals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:56](https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1016s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "clients overseas as well so so yeah we don't only pluck from the government list "
              "and also we don't only work with private clients the lists as you mentioned it can "
              'just be in a state representative that wants to come to ',
      'timestamp': 1016,
      'timestamp_label': '[00:16:56]',
      'timestamp_seconds': 1016,
      'tip': "clients overseas as well so so yeah we don't only pluck from the government list and "
             "also we don't only work with private clients the lists as you mentioned it can just "
             'be in a state representative that wants to come to ',
      'title': 'NALP webinar, May 2024 - what is it like working in the Probate Research Industry '
               '(NALP - National Association of Licenced Paralegals)',
      'url': 'https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1016s',
      'video_id': 'zz_ksXmJqyI'},
     {'author': 'FamilySearch',
      'channel': 'FamilySearch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:16](https://www.youtube.com/watch?v=fCvgh_QabMY&t=1216s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "you why this could be important so in this case we're looking in spencer county "
              'kentucky which is one of those places where a lot of their records got destroyed at '
              "the end of the civil war in 1865 and there's very few re",
      'timestamp': 1216,
      'timestamp_label': '[00:20:16]',
      'timestamp_seconds': 1216,
      'tip': "you why this could be important so in this case we're looking in spencer county "
             'kentucky which is one of those places where a lot of their records got destroyed at '
             "the end of the civil war in 1865 and there's very few re",
      'title': 'Records Analysis: Level up Your Probate Skills (FamilySearch)',
      'url': 'https://www.youtube.com/watch?v=fCvgh_QabMY&t=1216s',
      'video_id': 'fCvgh_QabMY'},
     {'author': 'Mid-Continent Public Library',
      'channel': 'Mid-Continent Public Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:20](https://www.youtube.com/watch?v=uAcku9kesK4&t=560s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'conclusion. Uh things were paid and so on. This will was a valid will it from '
              'Jackson County uh John B. Nolan. He actually wrote the will in October of 1896. He '
              'died June 3rd, uh, 1901. Heirs had it in court the 19th of ',
      'timestamp': 560,
      'timestamp_label': '[00:09:20]',
      'timestamp_seconds': 560,
      'tip': 'conclusion. Uh things were paid and so on. This will was a valid will it from '
             'Jackson County uh John B. Nolan. He actually wrote the will in October of 1896. He '
             'died June 3rd, uh, 1901. Heirs had it in court the 19th of ',
      'title': 'U.S. Probate Records for Genealogy  |  Midwest Genealogy Center (Mid-Continent '
               'Public Library)',
      'url': 'https://www.youtube.com/watch?v=uAcku9kesK4&t=560s',
      'video_id': 'uAcku9kesK4'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:32:23](https://www.youtube.com/watch?v=TBB8OPPFSsM&t=1943s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'records long before you started getting in a car or taking a plane fight someplace '
              'to to look for records in the county directly you may find that the records when '
              "you get to the place where you're looking that the recor",
      'timestamp': 1943,
      'timestamp_label': '[00:32:23]',
      'timestamp_seconds': 1943,
      'tip': 'records long before you started getting in a car or taking a plane fight someplace '
             'to to look for records in the county directly you may find that the records when you '
             "get to the place where you're looking that the recor",
      'title': 'What’s in a Probate Record and How to Use it for Genealogical Research– James '
               'Tanner (10 Sep 2023) (BYU Library Family History Center)',
      'url': 'https://www.youtube.com/watch?v=TBB8OPPFSsM&t=1943s',
      'video_id': 'TBB8OPPFSsM'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:30](https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=330s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "never been willing to risk it over a damn paycheck. I think what you'll find with a "
              "lot of companies out there that are pushing these lists. If they don't teach the "
              "right methodology, they're going to mess up a lot of pe",
      'timestamp': 330,
      'timestamp_label': '[00:05:30]',
      'timestamp_seconds': 330,
      'tip': "never been willing to risk it over a damn paycheck. I think what you'll find with a "
             "lot of companies out there that are pushing these lists. If they don't teach the "
             "right methodology, they're going to mess up a lot of pe",
      'title': 'Pre Probate Leads vs Probate Leads: How do you market to them and why cold calling '
               "isn't the best (Probate Mastery)",
      'url': 'https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=330s',
      'video_id': '4Z6pgZnoWi4'}],
 7: [{'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=sf2hUucsNZ8&t=375s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'opened. The deed was never recorded transferring ownership from John, her dad, to '
              'Mary, his daughter, his heir. Mary may have acted like the owner for 20 years, but '
              'the chain of proper chain of title was never properly u',
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': 'opened. The deed was never recorded transferring ownership from John, her dad, to '
             'Mary, his daughter, his heir. Mary may have acted like the owner for 20 years, but '
             'the chain of proper chain of title was never properly u',
      'title': '5 Curative Title Terms Every Investor Should Understand (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=sf2hUucsNZ8&t=375s',
      'video_id': 'sf2hUucsNZ8'},
     {'author': 'Center for Community Progress',
      'channel': 'Center for Community Progress',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:16](https://www.youtube.com/watch?v=DG4Uhckk-fU&t=436s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'uh that has passed to an heir. Um either there was a will or some kind of estate '
              'plan, but there was further action needed to record or take title to a deed and '
              'that was never done or if there is no will or estate plan o',
      'timestamp': 436,
      'timestamp_label': '[00:07:16]',
      'timestamp_seconds': 436,
      'tip': 'uh that has passed to an heir. Um either there was a will or some kind of estate '
             'plan, but there was further action needed to record or take title to a deed and that '
             'was never done or if there is no will or estate plan o',
      'title': "Heirs' Property 101 (Center for Community Progress)",
      'url': 'https://www.youtube.com/watch?v=DG4Uhckk-fU&t=436s',
      'video_id': 'DG4Uhckk-fU'},
     {'author': 'Five-minute genealogy',
      'channel': 'Five-minute genealogy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=A437gHrrk2s&t=296s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'repository for the probate books that contain the docs you want. Sometimes, you can '
              'order them from the county directly. Other times, a local historical society may '
              'have the documents and are set-up to help you acquire t',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'repository for the probate books that contain the docs you want. Sometimes, you can '
             'order them from the county directly. Other times, a local historical society may '
             'have the documents and are set-up to help you acquire t',
      'title': 'Finding repositories for probate records (Five-minute genealogy)',
      'url': 'https://www.youtube.com/watch?v=A437gHrrk2s&t=296s',
      'video_id': 'A437gHrrk2s'},
     {'author': 'Five-minute genealogy',
      'channel': 'Five-minute genealogy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=pGyFJ46jwTE&t=226s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'important of which is that children will almost always be listed in birth order. '
              'One common exception is if the first-born son has special legal rights: in this '
              'case, he may be listed ahead of any older sisters. Intestat',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': 'important of which is that children will almost always be listed in birth order. One '
             'common exception is if the first-born son has special legal rights: in this case, he '
             'may be listed ahead of any older sisters. Intestat',
      'title': 'Primary sources: Intestate probate documents (Five-minute genealogy)',
      'url': 'https://www.youtube.com/watch?v=pGyFJ46jwTE&t=226s',
      'video_id': 'pGyFJ46jwTE'},
     {'author': 'Five-minute genealogy',
      'channel': 'Five-minute genealogy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:01](https://www.youtube.com/watch?v=NYz_-ZkJbBE&t=301s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'are siblings. Settlements can also help when the recipient of one of the decedent’s '
              'bequests passed away. The settlement will list out the bequest and then name all '
              'the people who received it—that will be heirs of the re',
      'timestamp': 301,
      'timestamp_label': '[00:05:01]',
      'timestamp_seconds': 301,
      'tip': 'are siblings. Settlements can also help when the recipient of one of the decedent’s '
             'bequests passed away. The settlement will list out the bequest and then name all the '
             'people who received it—that will be heirs of the re',
      'title': 'Primary Sources: testate probate documents (Five-minute genealogy)',
      'url': 'https://www.youtube.com/watch?v=NYz_-ZkJbBE&t=301s',
      'video_id': 'NYz_-ZkJbBE'},
     {'author': 'Ancestry Aimee',
      'channel': 'Ancestry Aimee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:05](https://www.youtube.com/watch?v=0c5trJYJTyQ&t=785s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'in the video that i just did on deed research i talked about the fact that ancestry '
              'has quite a lot of these land records and some of their records are actually '
              'referencing documents that are in microfilm at family searc',
      'timestamp': 785,
      'timestamp_label': '[00:13:05]',
      'timestamp_seconds': 785,
      'tip': 'in the video that i just did on deed research i talked about the fact that ancestry '
             'has quite a lot of these land records and some of their records are actually '
             'referencing documents that are in microfilm at family searc',
      'title': 'How to Find Wills and Probate Records for Free and What They Can Tell Us (Ancestry '
               'Aimee)',
      'url': 'https://www.youtube.com/watch?v=0c5trJYJTyQ&t=785s',
      'video_id': '0c5trJYJTyQ'},
     {'author': 'FamilySearch',
      'channel': 'FamilySearch',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:28](https://www.youtube.com/watch?v=fCvgh_QabMY&t=1048s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'and then the brothers they all are coming together and they figured out how to '
              'divide the land and now they have to together deed off parts of the land to each of '
              'the different inheritance inheritors the different heirs ',
      'timestamp': 1048,
      'timestamp_label': '[00:17:28]',
      'timestamp_seconds': 1048,
      'tip': 'and then the brothers they all are coming together and they figured out how to '
             'divide the land and now they have to together deed off parts of the land to each of '
             'the different inheritance inheritors the different heirs ',
      'title': 'Records Analysis: Level up Your Probate Skills (FamilySearch)',
      'url': 'https://www.youtube.com/watch?v=fCvgh_QabMY&t=1048s',
      'video_id': 'fCvgh_QabMY'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:31](https://www.youtube.com/watch?v=TA4mtGUeNo8&t=1891s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'Father owns it. So you do something to change the title. You have the deed that '
              "it's. Provides for registered deeds and not coming into that will allow upon death "
              "to transfer, but has a standard deed, not that's what pro",
      'timestamp': 1891,
      'timestamp_label': '[00:31:31]',
      'timestamp_seconds': 1891,
      'tip': 'Father owns it. So you do something to change the title. You have the deed that '
             "it's. Provides for registered deeds and not coming into that will allow upon death "
             "to transfer, but has a standard deed, not that's what pro",
      'title': 'Probate Data and Property Lookups: Live Real Estate Coaching with Probate Mastery',
      'url': 'https://www.youtube.com/watch?v=TA4mtGUeNo8&t=1891s',
      'video_id': 'TA4mtGUeNo8'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:54](https://www.youtube.com/watch?v=zMW-iFWYX9w&t=1674s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': ">> And we got to thinking, this is the best we've got. >> Yeah. >> So we did our "
              'best to put together an affidavit of heirship because we were worried that if we '
              'went into a probate court and said, "Let\'s just do an admi',
      'timestamp': 1674,
      'timestamp_label': '[00:27:54]',
      'timestamp_seconds': 1674,
      'tip': ">> And we got to thinking, this is the best we've got. >> Yeah. >> So we did our "
             'best to put together an affidavit of heirship because we were worried that if we '
             'went into a probate court and said, "Let\'s just do an admi',
      'title': 'Curative Title Research: How She Finds Missing Owners (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=zMW-iFWYX9w&t=1674s',
      'video_id': 'zMW-iFWYX9w'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:27](https://www.youtube.com/watch?v=onebNbNQSBM&t=807s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'of the heirs and stuff, right? But in this one lot that they did find, they were '
              'able to locate the family, but when they located the family and they pulled the '
              'title work, they found out that there was an unresolved uh ',
      'timestamp': 807,
      'timestamp_label': '[00:13:27]',
      'timestamp_seconds': 807,
      'tip': 'of the heirs and stuff, right? But in this one lot that they did find, they were '
             'able to locate the family, but when they located the family and they pulled the '
             'title work, they found out that there was an unresolved uh ',
      'title': 'Curative Title Explained by a Florida Probate Attorney (Logan Fullmer)',
      'url': 'https://www.youtube.com/watch?v=onebNbNQSBM&t=807s',
      'video_id': 'onebNbNQSBM'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:53](https://www.youtube.com/watch?v=Odf2VQ3AZsg&t=713s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'the letters of testamentary. Today. We can sell that house. We can go to a purchase '
              "agreement. And even to closing this week, we don't need court approval. We don't "
              'need anything. We just need to connect chain of title a',
      'timestamp': 713,
      'timestamp_label': '[00:11:53]',
      'timestamp_seconds': 713,
      'tip': 'the letters of testamentary. Today. We can sell that house. We can go to a purchase '
             "agreement. And even to closing this week, we don't need court approval. We don't "
             'need anything. We just need to connect chain of title a',
      'title': 'Hyperlocal real estate marketing at probate court & How to buy a probate property '
               'as a sub2 deal (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=Odf2VQ3AZsg&t=713s',
      'video_id': 'Odf2VQ3AZsg'},
     {'author': 'National Housing Resource Center',
      'channel': 'National Housing Resource Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:38](https://www.youtube.com/watch?v=JsPL1vXcgCI&t=2378s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'on death but anyway in all states there is this instrument which is a deed from me '
              'to me and my heir or whoever with right of survivorship and if you have that you '
              "also don't have to go through probate so anyway these ar",
      'timestamp': 2378,
      'timestamp_label': '[00:39:38]',
      'timestamp_seconds': 2378,
      'tip': 'on death but anyway in all states there is this instrument which is a deed from me '
             'to me and my heir or whoever with right of survivorship and if you have that you '
             "also don't have to go through probate so anyway these ar",
      'title': 'TRAINING  Using Successor in Interest to Save the Family Home (National Housing '
               'Resource Center)',
      'url': 'https://www.youtube.com/watch?v=JsPL1vXcgCI&t=2378s',
      'video_id': 'JsPL1vXcgCI'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:33](https://www.youtube.com/watch?v=07zaZ3sQwi8&t=573s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'the court go there is usually a petition and then in order and then a notice or a '
              'notice and a petition in order and in any case there is always some kind of notice '
              'given to the heirs about the proceedings that are that ',
      'timestamp': 573,
      'timestamp_label': '[00:09:33]',
      'timestamp_seconds': 573,
      'tip': 'the court go there is usually a petition and then in order and then a notice or a '
             'notice and a petition in order and in any case there is always some kind of notice '
             'given to the heirs about the proceedings that are that ',
      'title': 'Probate  Part 7, "Example of a Probate File" by James Tanner (BYU Library Family '
               'History Center)',
      'url': 'https://www.youtube.com/watch?v=07zaZ3sQwi8&t=573s',
      'video_id': '07zaZ3sQwi8'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:53](https://www.youtube.com/watch?v=RmtbOq_vtuU&t=353s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'right? going looking at the deed and seeing information that that talks about the '
              'marital status, right? Um what again marriage records could be important and if you '
              'know they live in other places, looking at the marriag',
      'timestamp': 353,
      'timestamp_label': '[00:05:53]',
      'timestamp_seconds': 353,
      'tip': 'right? going looking at the deed and seeing information that that talks about the '
             'marital status, right? Um what again marriage records could be important and if you '
             'know they live in other places, looking at the marriag',
      'title': 'How to Find Heirs for a Florida Probate Property (Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=RmtbOq_vtuU&t=353s',
      'video_id': 'RmtbOq_vtuU'},
     {'author': 'MD Ag Law Education Initiative',
      'channel': 'MD Ag Law Education Initiative',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:52](https://www.youtube.com/watch?v=TP6n8TBsCGs&t=1012s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "Okay. So In order to understand how the UPHPA might help resolve your heir's "
              "property issues, it's important to speak with an attorney, of course, who's "
              'licensed to practice law in the state where the land, where the rea',
      'timestamp': 1012,
      'timestamp_label': '[00:16:52]',
      'timestamp_seconds': 1012,
      'tip': "Okay. So In order to understand how the UPHPA might help resolve your heir's "
             "property issues, it's important to speak with an attorney, of course, who's licensed "
             'to practice law in the state where the land, where the rea',
      'title': "Resolving Heirs' Property (MD Ag Law Education Initiative)",
      'url': 'https://www.youtube.com/watch?v=TP6n8TBsCGs&t=1012s',
      'video_id': 'TP6n8TBsCGs'}],
 8: [{'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=y5XZp-4n_uc&t=33s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "You don't have a parcel number. You don't have anything else, just a name. "
              'Preferably you know what state and county that person or busines is in but even if '
              "you don't have that, you still can most likely find them in Da",
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': "You don't have a parcel number. You don't have anything else, just a name. "
             'Preferably you know what state and county that person or busines is in but even if '
             "you don't have that, you still can most likely find them in Da",
      'title': 'DataTree Hacks: How to Search and Find Property Owners Nationwide (REtipster)',
      'url': 'https://www.youtube.com/watch?v=y5XZp-4n_uc&t=33s',
      'video_id': 'y5XZp-4n_uc'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:14](https://www.youtube.com/watch?v=2ThZ61aal9k&t=254s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'when you click on advanced search. And one thing that DataTree allows you to used '
              'as a filtering option is right down here under assessor information where it says '
              'delinquent, and you can click yes. And the idea behind t',
      'timestamp': 254,
      'timestamp_label': '[00:04:14]',
      'timestamp_seconds': 254,
      'tip': 'when you click on advanced search. And one thing that DataTree allows you to used as '
             'a filtering option is right down here under assessor information where it says '
             'delinquent, and you can click yes. And the idea behind t',
      'title': 'DataTree Hacks: TaxSource Reports and Property Tax Verification (REtipster)',
      'url': 'https://www.youtube.com/watch?v=2ThZ61aal9k&t=254s',
      'video_id': '2ThZ61aal9k'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:19](https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=19s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "D on it which shows that they're deceased. Here's what I do and I've had some real "
              "success in doing this. So, I'm going to go over about a five-step system with you "
              'that I do. First of all, when I run the skip tracing, t',
      'timestamp': 19,
      'timestamp_label': '[00:00:19]',
      'timestamp_seconds': 19,
      'tip': "D on it which shows that they're deceased. Here's what I do and I've had some real "
             "success in doing this. So, I'm going to go over about a five-step system with you "
             'that I do. First of all, when I run the skip tracing, t',
      'title': 'How To Find family members of a deceased person! (Surplus Institute / David Church '
               '/ Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=eiQ53kxE6ZA&t=19s',
      'video_id': 'eiQ53kxE6ZA'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:56](https://www.youtube.com/watch?v=aUiod-Jy68U&t=416s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'go on any future deed, getting transferred to anybody else. And it also shows us '
              'how they were holding title together. This is another very important thing that '
              'might not be evident without doing an actual title search, ',
      'timestamp': 416,
      'timestamp_label': '[00:06:56]',
      'timestamp_seconds': 416,
      'tip': 'go on any future deed, getting transferred to anybody else. And it also shows us how '
             'they were holding title together. This is another very important thing that might '
             'not be evident without doing an actual title search, ',
      'title': 'DataTree Hacks: Find Full Legal Descriptions and Title Vesting Information '
               '(REtipster)',
      'url': 'https://www.youtube.com/watch?v=aUiod-Jy68U&t=416s',
      'video_id': 'aUiod-Jy68U'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=32s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'our premium parcel data into arcgis online you can do the same to configure web '
              'apps hosted on agol the first and key step is to use our token and url to link the '
              'feature service to the arcgis online environment so to do',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'our premium parcel data into arcgis online you can do the same to configure web apps '
             'hosted on agol the first and key step is to use our token and url to link the '
             'feature service to the arcgis online environment so to do',
      'title': 'Feature Service Product Demo (Regrid)',
      'url': 'https://www.youtube.com/watch?v=X-_cLY3_96Y&t=32s',
      'video_id': 'X-_cLY3_96Y'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:23:29](https://www.youtube.com/watch?v=EToN9mWFZWc&t=1409s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "we're sharing with you will have boundary data on it so that's one of our core "
              "requirements here is anything that's coming through in any of these formats we're "
              'going to have boundaries for it for the ownership percent t',
      'timestamp': 1409,
      'timestamp_label': '[00:23:29]',
      'timestamp_seconds': 1409,
      'tip': "we're sharing with you will have boundary data on it so that's one of our core "
             "requirements here is anything that's coming through in any of these formats we're "
             'going to have boundaries for it for the ownership percent t',
      'title': 'Regrid Parcel Data - Overview & Coverage',
      'url': 'https://www.youtube.com/watch?v=EToN9mWFZWc&t=1409s',
      'video_id': 'EToN9mWFZWc'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:07](https://www.youtube.com/watch?v=1Wm_NPEagT8&t=247s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'of segment of the parcel uh we also have a bunch of things like elevation Contours '
              "that you can turn on if you're interested in those types of things under here "
              "that's uh pretty much the quick rundown uh remember you can",
      'timestamp': 247,
      'timestamp_label': '[00:04:07]',
      'timestamp_seconds': 247,
      'tip': 'of segment of the parcel uh we also have a bunch of things like elevation Contours '
             "that you can turn on if you're interested in those types of things under here that's "
             'uh pretty much the quick rundown uh remember you can',
      'title': 'Quick Start - The Regrid Property App (Web)',
      'url': 'https://www.youtube.com/watch?v=1Wm_NPEagT8&t=247s',
      'video_id': '1Wm_NPEagT8'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:43](https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=463s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'using both free and paid services to locate the current information for the '
              'claimants enhancing your chances of successful contact. Okay. Now remember you '
              'always get what you pay for skip tracing. Okay. Now, you can get ',
      'timestamp': 463,
      'timestamp_label': '[00:07:43]',
      'timestamp_seconds': 463,
      'tip': 'using both free and paid services to locate the current information for the '
             'claimants enhancing your chances of successful contact. Okay. Now remember you '
             'always get what you pay for skip tracing. Okay. Now, you can get ',
      'title': 'Unclaimed Funds: Lead Sourcing Masterclass (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=h4Qz3EvAAnw&t=463s',
      'video_id': 'h4Qz3EvAAnw'},
     {'author': 'Logan Fullmer',
      'channel': 'Logan Fullmer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:53:01](https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3181s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'it?" "13 months." Man, I hope you\'re doing something else to keep your bills paid '
              "along the way. >> Yeah. No, exactly. I mean, I don't Yeah, I don't think the number "
              'of heirs or that plaque that you get or credibility yo',
      'timestamp': 3181,
      'timestamp_label': '[00:53:01]',
      'timestamp_seconds': 3181,
      'tip': 'it?" "13 months." Man, I hope you\'re doing something else to keep your bills paid '
             "along the way. >> Yeah. No, exactly. I mean, I don't Yeah, I don't think the number "
             'of heirs or that plaque that you get or credibility yo',
      'title': "Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer)",
      'url': 'https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3181s',
      'video_id': 'dJ-LTFmMsTg'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:36](https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=276s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'match using a parcel id so i want to change that and re-run this matching process '
              "and see if changing the partial number will help so i'll click parcel number and "
              "then for these other fields i'm actually just going to se",
      'timestamp': 276,
      'timestamp_label': '[00:04:36]',
      'timestamp_seconds': 276,
      'tip': 'match using a parcel id so i want to change that and re-run this matching process '
             "and see if changing the partial number will help so i'll click parcel number and "
             "then for these other fields i'm actually just going to se",
      'title': 'Troubleshooting Data Import - Regrid Property App (Web)',
      'url': 'https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=276s',
      'video_id': 'VAtPDJ1KDjw'},
     {'author': 'Genealogy TV',
      'channel': 'Genealogy TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:02](https://www.youtube.com/watch?v=zIOhXZZxDDM&t=722s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'between especially you can pull together probably a whole major probate package '
              'between ancestry and family search you may even be able to continue to do more '
              'searching on family search to pull this in so I can download ',
      'timestamp': 722,
      'timestamp_label': '[00:12:02]',
      'timestamp_seconds': 722,
      'tip': 'between especially you can pull together probably a whole major probate package '
             'between ancestry and family search you may even be able to continue to do more '
             'searching on family search to pull this in so I can download ',
      'title': 'Find More Wills and Probate Records for Using Both Ancestry and FamilySearch '
               'Together (Genealogy TV)',
      'url': 'https://www.youtube.com/watch?v=zIOhXZZxDDM&t=722s',
      'video_id': 'zIOhXZZxDDM'},
     {'author': 'ohiocommerce',
      'channel': 'ohiocommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=o1cc3hUtIv4&t=64s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'a moment to think about that. You or someone you know probably has lost or '
              "forgotten money. So today I'm going to demonstrate our new system and show you how "
              'to go to our website, claim your funds, search for your proper',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'a moment to think about that. You or someone you know probably has lost or forgotten '
             "money. So today I'm going to demonstrate our new system and show you how to go to "
             'our website, claim your funds, search for your proper',
      'title': 'Watch our Demo on How to Claim Your Ohio Unclaimed Funds (ohiocommerce)',
      'url': 'https://www.youtube.com/watch?v=o1cc3hUtIv4&t=64s',
      'video_id': 'o1cc3hUtIv4'},
     {'author': 'Rachel Ezzell Berry',
      'channel': 'Rachel Ezzell Berry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=hpvnOFjxwaM&t=225s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "to a screen with search results or you'll receive a message in red font that no "
              'documents were found that matched the specified criteria this could be for more '
              "than one reason it could in fact be that we don't have any d",
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': "to a screen with search results or you'll receive a message in red font that no "
             'documents were found that matched the specified criteria this could be for more than '
             "one reason it could in fact be that we don't have any d",
      'title': 'DelcoPA ROW | Searching for Probated Estates Online (Rachel Ezzell Berry)',
      'url': 'https://www.youtube.com/watch?v=hpvnOFjxwaM&t=225s',
      'video_id': 'hpvnOFjxwaM'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:11](https://www.youtube.com/watch?v=RVakKAvFa_M&t=311s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "token here I'm going to remove the previous token but I'm going to go ahead and "
              "paste our token that we created just before this we're gonna I'm gonna enter that "
              "here it then goes and adds our token to the snippet um we'",
      'timestamp': 311,
      'timestamp_label': '[00:05:11]',
      'timestamp_seconds': 311,
      'tip': "token here I'm going to remove the previous token but I'm going to go ahead and "
             "paste our token that we created just before this we're gonna I'm gonna enter that "
             "here it then goes and adds our token to the snippet um we'",
      'title': "Quick Start Regrid's Interactive API Sandbox Guide",
      'url': 'https://www.youtube.com/watch?v=RVakKAvFa_M&t=311s',
      'video_id': 'RVakKAvFa_M'},
     {'author': 'Regrid',
      'channel': 'Regrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:42](https://www.youtube.com/watch?v=cKYlwRY3aVw&t=222s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "attributes that you're trying to filter on by clicking the little x to the left of "
              'their criteria in the box',
      'timestamp': 222,
      'timestamp_label': '[00:03:42]',
      'timestamp_seconds': 222,
      'tip': "attributes that you're trying to filter on by clicking the little x to the left of "
             'their criteria in the box',
      'title': 'Regrid Mapping Platform - Filter Data',
      'url': 'https://www.youtube.com/watch?v=cKYlwRY3aVw&t=222s',
      'video_id': 'cKYlwRY3aVw'}],
 9: [{'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:30](https://www.youtube.com/watch?v=DMdtmrWAO6c&t=810s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'shows up, you say, "You don\'t have to take my word for it. I\'m going to send you '
              'three things right now. the auction results with your name on it, the state statute '
              'that says these funds legally belong to you and my comp',
      'timestamp': 810,
      'timestamp_label': '[00:13:30]',
      'timestamp_seconds': 810,
      'tip': 'shows up, you say, "You don\'t have to take my word for it. I\'m going to send you '
             'three things right now. the auction results with your name on it, the state statute '
             'that says these funds legally belong to you and my comp',
      'title': 'Surplus Funds Recovery Cold Calling - STEP-BY-STEP SCRIPT (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=DMdtmrWAO6c&t=810s',
      'video_id': 'DMdtmrWAO6c'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=1AMk1-SB5ic&t=37s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "checklist of everything I need from my client that really helps out let's say I "
              'need five items I need a contingency agreement I need an assignment of Interest I '
              "need a power of attorney I need a copy of the driver's lic",
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': "checklist of everything I need from my client that really helps out let's say I need "
             'five items I need a contingency agreement I need an assignment of Interest I need a '
             "power of attorney I need a copy of the driver's lic",
      'title': "Unclaimed Funds: How to Get Your Client's Documents in Order⚡️Unclaimed fund "
               'Client Document finding (Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=1AMk1-SB5ic&t=37s',
      'video_id': '1AMk1-SB5ic'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=ApkuK7OOL9w&t=21s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "brand new you're just getting started you don't know what to say when you're "
              "talking to somebody and I have a free calling script there's a link in the "
              'description you can just put your information down and you can get i',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "brand new you're just getting started you don't know what to say when you're talking "
             "to somebody and I have a free calling script there's a link in the description you "
             'can just put your information down and you can get i',
      'title': 'State Funds Tutorial Top 4 Tech Tools Needed For Your State Funds Business '
               '(Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=ApkuK7OOL9w&t=21s',
      'video_id': 'ApkuK7OOL9w'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:11](https://www.youtube.com/watch?v=XHOqG0CY1KA&t=851s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'okay and another thing this is huge i say this in all my videos you guys follow up '
              "follow up follow up with leads okay most of these leads they're going to be "
              'converted after probably the third phone call maybe more mayb',
      'timestamp': 851,
      'timestamp_label': '[00:14:11]',
      'timestamp_seconds': 851,
      'tip': 'okay and another thing this is huge i say this in all my videos you guys follow up '
             "follow up follow up with leads okay most of these leads they're going to be "
             'converted after probably the third phone call maybe more mayb',
      'title': 'Unclaimed Funds Tutorial: Cold Calling Basics For Your Unclaimed Funds Business. '
               'state funds. (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=XHOqG0CY1KA&t=851s',
      'video_id': 'XHOqG0CY1KA'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:20](https://www.youtube.com/watch?v=U_Eh790rq3o&t=1220s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "issue we will do a longer contract period. Um but we don't always do that. We do "
              "automatically extend up to 90 days for curative title issues. That's standard in "
              'our in our agreement cuz we know things come up. So we it ',
      'timestamp': 1220,
      'timestamp_label': '[00:20:20]',
      'timestamp_seconds': 1220,
      'tip': "issue we will do a longer contract period. Um but we don't always do that. We do "
             "automatically extend up to 90 days for curative title issues. That's standard in our "
             'in our agreement cuz we know things come up. So we it ',
      'title': 'How Wholesalers Can Turn Title Problems Into Profitable Curative Deals (Courtney '
               'Fricke)',
      'url': 'https://www.youtube.com/watch?v=U_Eh790rq3o&t=1220s',
      'video_id': 'U_Eh790rq3o'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:09](https://www.youtube.com/watch?v=PDnxvvPI7jU&t=249s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "No, we haven't. We've called a few different companies and she has this social and "
              'birthday and name of course, and private call a few companies. But some of them '
              "won't talk to her without the policy number. Right. So th",
      'timestamp': 249,
      'timestamp_label': '[00:04:09]',
      'timestamp_seconds': 249,
      'tip': "No, we haven't. We've called a few different companies and she has this social and "
             'birthday and name of course, and private call a few companies. But some of them '
             "won't talk to her without the policy number. Right. So th",
      'title': 'Calling probates, probate marketing, and selling probate property: Live probate '
               'class w/ Bill Gross (Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=PDnxvvPI7jU&t=249s',
      'video_id': 'PDnxvvPI7jU'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:13](https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=253s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'So. I do not believe in direct marketing, in outbound direct mail and cold calling '
              "pre-probate lists. I just don't. And I probably never will because I think you have "
              'a greater opportunity to harm your reputation than yo',
      'timestamp': 253,
      'timestamp_label': '[00:04:13]',
      'timestamp_seconds': 253,
      'tip': 'So. I do not believe in direct marketing, in outbound direct mail and cold calling '
             "pre-probate lists. I just don't. And I probably never will because I think you have "
             'a greater opportunity to harm your reputation than yo',
      'title': 'Pre Probate Leads vs Probate Leads: How do you market to them and why cold calling '
               "isn't the best (Probate Mastery)",
      'url': 'https://www.youtube.com/watch?v=4Z6pgZnoWi4&t=253s',
      'video_id': '4Z6pgZnoWi4'},
     {'author': 'Courtney Fricke',
      'channel': 'Courtney Fricke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=pQwwvYbUYrU&t=124s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'I remember hitting the buttony the button, Courtney, and I was like, "Here we go." '
              'The next day, I remember I got a call from the investor and they said, "Whoa, whoa, '
              'whoa, whoa, did you file the probates?" And I was lik',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'I remember hitting the buttony the button, Courtney, and I was like, "Here we go." '
             'The next day, I remember I got a call from the investor and they said, "Whoa, whoa, '
             'whoa, whoa, did you file the probates?" And I was lik',
      'title': 'The Probate Mistake New Real Estate Investors Make (Florida Attorney Case Study) '
               '(Courtney Fricke)',
      'url': 'https://www.youtube.com/watch?v=pQwwvYbUYrU&t=124s',
      'video_id': 'pQwwvYbUYrU'},
     {'author': 'BYU Library Family History Center',
      'channel': 'BYU Library Family History Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=Xe2NEfqDwTQ&t=226s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'law they mean that there is a statute prohibiting the action however that does not '
              'apply to civil cases so generally speaking something in a civil case would not be '
              'against the law it would just be the ruling of the cour',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': 'law they mean that there is a statute prohibiting the action however that does not '
             'apply to civil cases so generally speaking something in a civil case would not be '
             'against the law it would just be the ruling of the cour',
      'title': 'Probate  Part 5,  " What are Probate Procedures" by James Tanner (BYU Library '
               'Family History Center)',
      'url': 'https://www.youtube.com/watch?v=Xe2NEfqDwTQ&t=226s',
      'video_id': 'Xe2NEfqDwTQ'},
     {'author': 'Daniel Curran',
      'channel': 'Daniel Curran',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:06](https://www.youtube.com/watch?v=AKvEFJHf5K0&t=1566s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'solicitor employees to do a certain area of work should be in in compliance with '
              "the SRA code even so far as where that touches upon that area of work so we're "
              "always aware of that and we're always trying to make sure th",
      'timestamp': 1566,
      'timestamp_label': '[00:26:06]',
      'timestamp_seconds': 1566,
      'tip': 'solicitor employees to do a certain area of work should be in in compliance with the '
             "SRA code even so far as where that touches upon that area of work so we're always "
             "aware of that and we're always trying to make sure th",
      'title': 'Daniel Curran Finders International - Todays Wills & Probate Podcast',
      'url': 'https://www.youtube.com/watch?v=AKvEFJHf5K0&t=1566s',
      'video_id': 'AKvEFJHf5K0'},
     {'author': 'Boyes Turner',
      'channel': 'Boyes Turner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:37](https://www.youtube.com/watch?v=SLqhAWEXEv4&t=1117s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "assets from abroad and these can massively we always say it's not like these are "
              "things there's no mystery in that in many ways but they're very timec consuming and "
              'it could be just a judgment call of how a sista wants t',
      'timestamp': 1117,
      'timestamp_label': '[00:18:37]',
      'timestamp_seconds': 1117,
      'tip': "assets from abroad and these can massively we always say it's not like these are "
             "things there's no mystery in that in many ways but they're very timec consuming and "
             'it could be just a judgment call of how a sista wants t',
      'title': 'Probate Detectives (Boyes Turner)',
      'url': 'https://www.youtube.com/watch?v=SLqhAWEXEv4&t=1117s',
      'video_id': 'SLqhAWEXEv4'},
     {'author': 'Probate TV',
      'channel': 'Probate TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:52](https://www.youtube.com/watch?v=le9BUKYDl1A&t=52s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "printed on the letter, don't automatically trust it. The number may be fake. >> "
              '[music] >> It could connect to an automated message which scammers can use to '
              'impersonate HMCTS in a follow-up call. >> [music] >> Stop, che',
      'timestamp': 52,
      'timestamp_label': '[00:00:52]',
      'timestamp_seconds': 52,
      'tip': "printed on the letter, don't automatically trust it. The number may be fake. >> "
             '[music] >> It could connect to an automated message which scammers can use to '
             'impersonate HMCTS in a follow-up call. >> [music] >> Stop, che',
      'title': 'How to Spot a Fake Probate Letter | 3 Steps to Avoid Scams (Probate TV)',
      'url': 'https://www.youtube.com/watch?v=le9BUKYDl1A&t=52s',
      'video_id': 'le9BUKYDl1A'},
     {'author': 'Probate Mastery',
      'channel': 'Probate Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:19:47](https://www.youtube.com/watch?v=7xCfSyqYEys&t=4787s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'that I would really buy a house tenants in common unless it was maybe a business '
              "partner. Uh tenants in common means that the survivor keeps their let's call it "
              'half and then the deedence half goes to heirs. That can get',
      'timestamp': 4787,
      'timestamp_label': '[01:19:47]',
      'timestamp_seconds': 4787,
      'tip': 'that I would really buy a house tenants in common unless it was maybe a business '
             "partner. Uh tenants in common means that the survivor keeps their let's call it half "
             'and then the deedence half goes to heirs. That can get',
      'title': 'Probate Process for Real Estate Agents & Investors: 12 Steps From Filing to Sale '
               '(Probate Mastery)',
      'url': 'https://www.youtube.com/watch?v=7xCfSyqYEys&t=4787s',
      'video_id': '7xCfSyqYEys'},
     {'author': 'REtipster',
      'channel': 'REtipster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=9RvXCiHUzlo&t=104s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': "But let's say you're trying to pull a list of property owners, whether it's for "
              'marketing purposes or direct mail or anything like that. And you want to find only '
              'the people who own multiple properties. Well, we would go',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': "But let's say you're trying to pull a list of property owners, whether it's for "
             'marketing purposes or direct mail or anything like that. And you want to find only '
             'the people who own multiple properties. Well, we would go',
      'title': 'DataTree Hacks: How to Find Portfolio Owners With Multiple Properties (REtipster)',
      'url': 'https://www.youtube.com/watch?v=9RvXCiHUzlo&t=104s',
      'video_id': '9RvXCiHUzlo'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:26](https://www.youtube.com/watch?v=MiiGrCZZAZk&t=146s)',
      'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                   'claim execution; verify against local statute.',
      'source_type': 'video_pro_tip',
      'text': 'sent over proof, we got them under contract, and we handed over to an attorney. All '
              "right? XCES Elite is super powerful. It's how I operate my entire business at such "
              "a high level. Now, here's how we reached out and let'",
      'timestamp': 146,
      'timestamp_label': '[00:02:26]',
      'timestamp_seconds': 146,
      'tip': 'sent over proof, we got them under contract, and we handed over to an attorney. All '
             "right? XCES Elite is super powerful. It's how I operate my entire business at such a "
             "high level. Now, here's how we reached out and let'",
      'title': '$200,000 California Foreclosure Heir Claim Case Study (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=MiiGrCZZAZk&t=146s',
      'video_id': 'MiiGrCZZAZk'}],
 10: [{'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:55](https://www.youtube.com/watch?v=MiiGrCZZAZk&t=115s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'that, which justifies us getting our 25% fee on such a large claim. Now, how did I '
               'get this deal? Everything was through XCES Elite. XCES Elite truly is the number '
               'one CRM for this business. They have the leading databas',
       'timestamp': 115,
       'timestamp_label': '[00:01:55]',
       'timestamp_seconds': 115,
       'tip': 'that, which justifies us getting our 25% fee on such a large claim. Now, how did I '
              'get this deal? Everything was through XCES Elite. XCES Elite truly is the number '
              'one CRM for this business. They have the leading databas',
       'title': '$200,000 California Foreclosure Heir Claim Case Study (Money Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=MiiGrCZZAZk&t=115s',
       'video_id': 'MiiGrCZZAZk'},
      {'author': 'Five-minute genealogy',
       'channel': 'Five-minute genealogy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:03](https://www.youtube.com/watch?v=YNOLd8LZB48&t=63s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'as well as a son Doctor Benjamin Franklin M. Huggins. Fun fact: Doctor wasn’t a '
               'title, it was actually the poor guy’s first name. What a mouthful. Anyway, the '
               'probate file noted that William owned land in Frederick Count',
       'timestamp': 63,
       'timestamp_label': '[00:01:03]',
       'timestamp_seconds': 63,
       'tip': 'as well as a son Doctor Benjamin Franklin M. Huggins. Fun fact: Doctor wasn’t a '
              'title, it was actually the poor guy’s first name. What a mouthful. Anyway, the '
              'probate file noted that William owned land in Frederick Count',
       'title': 'Probate case study: Illegitimacy and conflicting surnames (Five-minute genealogy)',
       'url': 'https://www.youtube.com/watch?v=YNOLd8LZB48&t=63s',
       'video_id': 'YNOLd8LZB48'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:09](https://www.youtube.com/watch?v=ES6y4iF-bBM&t=69s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "when you're just getting started to run your state funds business, the 0:01:13.1 "
               'S1: Very first thing you guys is a CRM stands for customer relationship software '
               'for you guys that are brand new. 0:01:21.0 S2: Pretty much',
       'timestamp': 69,
       'timestamp_label': '[00:01:09]',
       'timestamp_seconds': 69,
       'tip': "when you're just getting started to run your state funds business, the 0:01:13.1 "
              'S1: Very first thing you guys is a CRM stands for customer relationship software '
              'for you guys that are brand new. 0:01:21.0 S2: Pretty much',
       'title': 'State Funds Tutorial: 5 Tech Tools For Your State Funds Business (Surplus Funds '
                '101)',
       'url': 'https://www.youtube.com/watch?v=ES6y4iF-bBM&t=69s',
       'video_id': 'ES6y4iF-bBM'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:16](https://www.youtube.com/watch?v=-QzABvCmtVc&t=616s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "you do, well, it's the one that you don't do. So, before you leave, I want you to "
               "watch this next video. It's going to be here on the screen. And we've really just "
               'talked about a case study of a lead that came my way tha',
       'timestamp': 616,
       'timestamp_label': '[00:10:16]',
       'timestamp_seconds': 616,
       'tip': "you do, well, it's the one that you don't do. So, before you leave, I want you to "
              "watch this next video. It's going to be here on the screen. And we've really just "
              'talked about a case study of a lead that came my way tha',
       'title': 'How to Underwrite a Curative Title Deal (And Know When to Walk Away) (Courtney '
                'Fricke)',
       'url': 'https://www.youtube.com/watch?v=-QzABvCmtVc&t=616s',
       'video_id': '-QzABvCmtVc'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:12](https://www.youtube.com/watch?v=nYQaov_liDw&t=432s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "who, um was ultimately the one who'd been dragging this along. But you said that "
               'they never really had fee simple interest. Can you explain that? What do you mean '
               'by that? >> Yeah, so when the ownership divests, each hei',
       'timestamp': 432,
       'timestamp_label': '[00:07:12]',
       'timestamp_seconds': 432,
       'tip': "who, um was ultimately the one who'd been dragging this along. But you said that "
              'they never really had fee simple interest. Can you explain that? What do you mean '
              'by that? >> Yeah, so when the ownership divests, each hei',
       'title': 'How Matt Solved a 10 Heir Title Nightmare (A Curative Title Case Study) (Courtney '
                'Fricke)',
       'url': 'https://www.youtube.com/watch?v=nYQaov_liDw&t=432s',
       'video_id': 'nYQaov_liDw'},
      {'author': 'Regrid',
       'channel': 'Regrid',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:42](https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=342s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "you know anything that's out of place in this case i'm looking for blanks in the "
               "parcel numbers and going down here i don't see any blanks it's possible that "
               "there's something else going on here so there's a couple thing",
       'timestamp': 342,
       'timestamp_label': '[00:05:42]',
       'timestamp_seconds': 342,
       'tip': "you know anything that's out of place in this case i'm looking for blanks in the "
              "parcel numbers and going down here i don't see any blanks it's possible that "
              "there's something else going on here so there's a couple thing",
       'title': 'Troubleshooting Data Import - Regrid Property App (Web)',
       'url': 'https://www.youtube.com/watch?v=VAtPDJ1KDjw&t=342s',
       'video_id': 'VAtPDJ1KDjw'},
      {'author': 'Brian Evins',
       'channel': 'Brian Evins',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=sX_SYXDaDeA&t=117s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "there's really there's only a few data points that were after after the case "
               "number right we're after the estate of that person obviously and the most "
               'important data is the PRS first and last name the PRS address mailing',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': "there's really there's only a few data points that were after after the case number "
              "right we're after the estate of that person obviously and the most important data "
              'is the PRS first and last name the PRS address mailing',
       'title': 'Scraping Data--Probate--Public Notice (Brian Evins)',
       'url': 'https://www.youtube.com/watch?v=sX_SYXDaDeA&t=117s',
       'video_id': 'sX_SYXDaDeA'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:30](https://www.youtube.com/watch?v=ApkuK7OOL9w&t=210s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "advanced people listening to this they're going to say no David you're wrong what "
               'you need to do is have an automation trigger on your auto dealer that pushes a '
               "lead information in your CRM and yes that's true that's how",
       'timestamp': 210,
       'timestamp_label': '[00:03:30]',
       'timestamp_seconds': 210,
       'tip': "advanced people listening to this they're going to say no David you're wrong what "
              'you need to do is have an automation trigger on your auto dealer that pushes a lead '
              "information in your CRM and yes that's true that's how",
       'title': 'State Funds Tutorial Top 4 Tech Tools Needed For Your State Funds Business '
                '(Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=ApkuK7OOL9w&t=210s',
       'video_id': 'ApkuK7OOL9w'},
      {'author': 'Five-minute genealogy',
       'channel': 'Five-minute genealogy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:58](https://www.youtube.com/watch?v=7_oRhXnhlag&t=238s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "That wasn't the case at all. That's how you got educated. Let's look at an example "
               'of how to misinterpret guardianship. Here’s an excerpt from a genealogy of the '
               'Slough family in Pennsylvania. The story is that a wicked ',
       'timestamp': 238,
       'timestamp_label': '[00:03:58]',
       'timestamp_seconds': 238,
       'tip': "That wasn't the case at all. That's how you got educated. Let's look at an example "
              'of how to misinterpret guardianship. Here’s an excerpt from a genealogy of the '
              'Slough family in Pennsylvania. The story is that a wicked ',
       'title': 'Primary Sources: Understanding guardianship in probate proceedings (Five-minute '
                'genealogy)',
       'url': 'https://www.youtube.com/watch?v=7_oRhXnhlag&t=238s',
       'video_id': '7_oRhXnhlag'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:30](https://www.youtube.com/watch?v=Gk0D4wVEXmc&t=210s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'SE right next to us right now. Right. 0:03:32.2 S2: Well, when you go into the '
               "Apple store, they're gonna tell you about the new iPhone and it has this updated "
               'camera, it has all these other new techy apps included in Ya',
       'timestamp': 210,
       'timestamp_label': '[00:03:30]',
       'timestamp_seconds': 210,
       'tip': 'SE right next to us right now. Right. 0:03:32.2 S2: Well, when you go into the '
              "Apple store, they're gonna tell you about the new iPhone and it has this updated "
              'camera, it has all these other new techy apps included in Ya',
       'title': 'Surplus Funds 101 Tutorial: Top 4 FREE Software Platforms For Your State Funds '
                'Business',
       'url': 'https://www.youtube.com/watch?v=Gk0D4wVEXmc&t=210s',
       'video_id': 'Gk0D4wVEXmc'},
      {'author': 'Texas Probate Real Estate',
       'channel': 'Texas Probate Real Estate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:57](https://www.youtube.com/watch?v=n8jP0gweIR4&t=837s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "lawyer. They don't understand how the law works, the different kinds of statutes, "
               'how they apply to their case. Um, are they do you find them getting into trouble? '
               "What's the result of that? >> I won. >> Okay. Okay. Oh, ",
       'timestamp': 837,
       'timestamp_label': '[00:13:57]',
       'timestamp_seconds': 837,
       'tip': "lawyer. They don't understand how the law works, the different kinds of statutes, "
              'how they apply to their case. Um, are they do you find them getting into trouble? '
              "What's the result of that? >> I won. >> Okay. Okay. Oh, ",
       'title': 'Affidavits of Heirship and Other Texas Probate Pitfalls | TPRE Podcast Ep 3 '
                '(Texas Probate Real Estate)',
       'url': 'https://www.youtube.com/watch?v=n8jP0gweIR4&t=837s',
       'video_id': 'n8jP0gweIR4'},
      {'author': 'Regrid',
       'channel': 'Regrid',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:40](https://www.youtube.com/watch?v=6nMKiCCsK60&t=100s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "as the field names for each of the columns uh that's been pulled from the sheet "
               'that you had as well as the file type or rather sorry the column type um this has '
               "gone through the testing and we can see it's 100% matched ",
       'timestamp': 100,
       'timestamp_label': '[00:01:40]',
       'timestamp_seconds': 100,
       'tip': "as the field names for each of the columns uh that's been pulled from the sheet "
              'that you had as well as the file type or rather sorry the column type um this has '
              "gone through the testing and we can see it's 100% matched ",
       'title': 'Import Your Own Property Data - Regrid Property App (Web)',
       'url': 'https://www.youtube.com/watch?v=6nMKiCCsK60&t=100s',
       'video_id': '6nMKiCCsK60'},
      {'author': 'probatedata',
       'channel': 'probatedata',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:30](https://www.youtube.com/watch?v=nRRFhMEip8c&t=210s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'And now we got to pick the uh filing fr- uh at the case filing date, right? So, '
               'this is really important. This is where uh some of you might make mistakes and you '
               "might end up with like tens of thousands of cases. You'll",
       'timestamp': 210,
       'timestamp_label': '[00:03:30]',
       'timestamp_seconds': 210,
       'tip': 'And now we got to pick the uh filing fr- uh at the case filing date, right? So, '
              'this is really important. This is where uh some of you might make mistakes and you '
              "might end up with like tens of thousands of cases. You'll",
       'title': 'How to Find Old Probate Leads (probatedata)',
       'url': 'https://www.youtube.com/watch?v=nRRFhMEip8c&t=210s',
       'video_id': 'nRRFhMEip8c'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:40](https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=280s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'entitled, we shoot over the agreement form. They choose us, we contact the county, '
               'we make sure we have all of our requirements, all of our documents, you follow up '
               'with the county, and then you get paid. All right? So, ',
       'timestamp': 280,
       'timestamp_label': '[00:04:40]',
       'timestamp_seconds': 280,
       'tip': 'entitled, we shoot over the agreement form. They choose us, we contact the county, '
              'we make sure we have all of our requirements, all of our documents, you follow up '
              'with the county, and then you get paid. All right? So, ',
       'title': 'Amador county Tax Sale Surplus Funds Case Study (Money Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=4-lZwuXtY6Y&t=280s',
       'video_id': '4-lZwuXtY6Y'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:51](https://www.youtube.com/watch?v=pQwwvYbUYrU&t=51s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'member that owned the property in their sole name and I said, "Okay, great. We got '
               'one person on title. This shouldn\'t be that bad." We walked through the whole '
               'analysis and it ended up being a very linear chain of proba',
       'timestamp': 51,
       'timestamp_label': '[00:00:51]',
       'timestamp_seconds': 51,
       'tip': 'member that owned the property in their sole name and I said, "Okay, great. We got '
              'one person on title. This shouldn\'t be that bad." We walked through the whole '
              'analysis and it ended up being a very linear chain of proba',
       'title': 'The Probate Mistake New Real Estate Investors Make (Florida Attorney Case Study) '
                '(Courtney Fricke)',
       'url': 'https://www.youtube.com/watch?v=pQwwvYbUYrU&t=51s',
       'video_id': 'pQwwvYbUYrU'}],
 11: [{'author': 'Hull & Hull LLP',
       'channel': 'Hull & Hull LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=X-Q-bm1y9no&t=88s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'there are sort of two types of researchers both of which are necessary and '
               'sometimes uh required in different situations I mean you can hire a fee for '
               "service researcher who has got genealogical searching that they'll go",
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'there are sort of two types of researchers both of which are necessary and '
              'sometimes uh required in different situations I mean you can hire a fee for service '
              "researcher who has got genealogical searching that they'll go",
       'title': 'Locating Heirs (Hull & Hull LLP)',
       'url': 'https://www.youtube.com/watch?v=X-Q-bm1y9no&t=88s',
       'video_id': 'X-Q-bm1y9no'},
      {'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=GfyX48eCbRY&t=55s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'This is the kind of information that a title researcher would be doing at a title '
               'company. They may not use DataTree specifically, but just as a first pass, this '
               'would tell them most of what they need to know. Whereas if',
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': 'This is the kind of information that a title researcher would be doing at a title '
              'company. They may not use DataTree specifically, but just as a first pass, this '
              'would tell them most of what they need to know. Whereas if',
       'title': 'DataTree Hacks: How to Do Title Research and Hire Abstractor Services (REtipster)',
       'url': 'https://www.youtube.com/watch?v=GfyX48eCbRY&t=55s',
       'video_id': 'GfyX48eCbRY'},
      {'author': 'NALP - National Association of Licenced Paralegals',
       'channel': 'NALP - National Association of Licenced Paralegals',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:34](https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1174s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'opening a case working on it as a team so teamwork and then closing a case out and '
               'ultimately the beneficiaries receiving their inheritance so yeah super rewarding '
               "really good job for dinner parties when you're speaking ",
       'timestamp': 1174,
       'timestamp_label': '[00:19:34]',
       'timestamp_seconds': 1174,
       'tip': 'opening a case working on it as a team so teamwork and then closing a case out and '
              'ultimately the beneficiaries receiving their inheritance so yeah super rewarding '
              "really good job for dinner parties when you're speaking ",
       'title': 'NALP webinar, May 2024 - what is it like working in the Probate Research Industry '
                '(NALP - National Association of Licenced Paralegals)',
       'url': 'https://www.youtube.com/watch?v=zz_ksXmJqyI&t=1174s',
       'video_id': 'zz_ksXmJqyI'},
      {'author': "California State Controller's Office",
       'channel': "California State Controller's Office",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:12](https://www.youtube.com/watch?v=1ahhduhMdd0&t=192s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "state holidays. The California State Controller's team is committed to helping "
               'rightful owners receive their property. Please help spread the word by sharing '
               'this tutorial with family and friends who may have unclaimed p',
       'timestamp': 192,
       'timestamp_label': '[00:03:12]',
       'timestamp_seconds': 192,
       'tip': "state holidays. The California State Controller's team is committed to helping "
              'rightful owners receive their property. Please help spread the word by sharing this '
              'tutorial with family and friends who may have unclaimed p',
       'title': "Declaration Under Probate Code 13101 Tutorial (California State Controller's "
                'Office)',
       'url': 'https://www.youtube.com/watch?v=1ahhduhMdd0&t=192s',
       'video_id': '1ahhduhMdd0'},
      {'author': "California State Controller's Office",
       'channel': "California State Controller's Office",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:00](https://www.youtube.com/watch?v=cMCrrRkehJk&t=240s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "state holidays. The California State Controller's team is committed to helping "
               'rightful owners receive their property. Please help spread the word by sharing '
               'this tutorial with family and friends who may have unclaimed p',
       'timestamp': 240,
       'timestamp_label': '[00:04:00]',
       'timestamp_seconds': 240,
       'tip': "state holidays. The California State Controller's team is committed to helping "
              'rightful owners receive their property. Please help spread the word by sharing this '
              'tutorial with family and friends who may have unclaimed p',
       'title': "Table of Heirship Tutorial (California State Controller's Office)",
       'url': 'https://www.youtube.com/watch?v=cMCrrRkehJk&t=240s',
       'video_id': 'cMCrrRkehJk'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=ASO1JUOWTjA&t=121s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'they either go to online jobs, Ph dot com, or some regroup in a Facebook area, and '
               "they hire their very first virtual assistant. Doesn't work out for him. And so "
               "here are some of the things that they don't do that I do. ",
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'they either go to online jobs, Ph dot com, or some regroup in a Facebook area, and '
              "they hire their very first virtual assistant. Doesn't work out for him. And so here "
              "are some of the things that they don't do that I do. ",
       'title': 'State Funds Tutorial Virtual Assistants: Top 3 Hiring Mistakes While Growing Your '
                'Surplus Business (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=ASO1JUOWTjA&t=121s',
       'video_id': 'ASO1JUOWTjA'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:37:42](https://www.youtube.com/watch?v=AAF69oF79DU&t=2262s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "There was a lady, one of our original subscribers. I never thought we'd sell a "
               'county with two leads because we have a minimum of 200 bucks. Cause we have to pay '
               'mileage and researcher fees and all that. She bought Wrigh',
       'timestamp': 2262,
       'timestamp_label': '[00:37:42]',
       'timestamp_seconds': 2262,
       'tip': "There was a lady, one of our original subscribers. I never thought we'd sell a "
              'county with two leads because we have a minimum of 200 bucks. Cause we have to pay '
              'mileage and researcher fees and all that. She bought Wrigh',
       'title': 'Sub-to strategy for probate investing | Probate foreclosures | Probate real '
                'estate marketing tips (Probate Mastery)',
       'url': 'https://www.youtube.com/watch?v=AAF69oF79DU&t=2262s',
       'video_id': 'AAF69oF79DU'},
      {'author': 'National Housing Resource Center',
       'channel': 'National Housing Resource Center',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:00:20](https://www.youtube.com/watch?v=ME2xl7cczH8&t=3620s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "there might be VA or USDA loans too and I don't think they're in this slide deck "
               'but um nclc has on its website information um about how to figure out you know '
               'what kind of loan your borrower has and always really really',
       'timestamp': 3620,
       'timestamp_label': '[01:00:20]',
       'timestamp_seconds': 3620,
       'tip': "there might be VA or USDA loans too and I don't think they're in this slide deck "
              'but um nclc has on its website information um about how to figure out you know what '
              'kind of loan your borrower has and always really really',
       'title': 'Successor in Interest and Tangled Title (National Housing Resource Center)',
       'url': 'https://www.youtube.com/watch?v=ME2xl7cczH8&t=3620s',
       'video_id': 'ME2xl7cczH8'},
      {'author': 'REtipster',
       'channel': 'REtipster',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:56](https://www.youtube.com/watch?v=ntT8V0gnpAs&t=836s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'would be to hire somebody to drive by the property and take some pictures for you, '
               "just to verify what's going on on that property right now. I think nine times out "
               "of 10 you're gonna find that it looks pretty much the s",
       'timestamp': 836,
       'timestamp_label': '[00:13:56]',
       'timestamp_seconds': 836,
       'tip': 'would be to hire somebody to drive by the property and take some pictures for you, '
              "just to verify what's going on on that property right now. I think nine times out "
              "of 10 you're gonna find that it looks pretty much the s",
       'title': 'The Fastest Way to Research Any Property in the United States (REtipster)',
       'url': 'https://www.youtube.com/watch?v=ntT8V0gnpAs&t=836s',
       'video_id': 'ntT8V0gnpAs'},
      {'author': 'Five-minute genealogy',
       'channel': 'Five-minute genealogy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:20](https://www.youtube.com/watch?v=A437gHrrk2s&t=320s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'As a last resort, if you can’t make the trip, you could hire a process server. '
               'I’ve done that, but… a process server is accustomed to finding modern court '
               'documents on deadline or serving subpoenas to people who don’t wa',
       'timestamp': 320,
       'timestamp_label': '[00:05:20]',
       'timestamp_seconds': 320,
       'tip': 'As a last resort, if you can’t make the trip, you could hire a process server. I’ve '
              'done that, but… a process server is accustomed to finding modern court documents on '
              'deadline or serving subpoenas to people who don’t wa',
       'title': 'Finding repositories for probate records (Five-minute genealogy)',
       'url': 'https://www.youtube.com/watch?v=A437gHrrk2s&t=320s',
       'video_id': 'A437gHrrk2s'},
      {'author': 'The Genealogy Professional Podcast',
       'channel': 'The Genealogy Professional Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:33:02](https://www.youtube.com/watch?v=7v_UB7hKgKg&t=1982s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'a minute American who came here and was reasonably knowledgeable about Irish '
               'research it still have to you know find their way around and get going and would '
               'more than likely hopefully team up with someone already workin',
       'timestamp': 1982,
       'timestamp_label': '[00:33:02]',
       'timestamp_seconds': 1982,
       'tip': 'a minute American who came here and was reasonably knowledgeable about Irish '
              'research it still have to you know find their way around and get going and would '
              'more than likely hopefully team up with someone already workin',
       'title': "TGP 19 - Eileen O'Duill - Probate Research (The Genealogy Professional Podcast)",
       'url': 'https://www.youtube.com/watch?v=7v_UB7hKgKg&t=1982s',
       'video_id': '7v_UB7hKgKg'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:55](https://www.youtube.com/watch?v=Qn63DtrxFts&t=175s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "I was working with there's their deals got cut in half by like 75% and so they "
               "can't pay me anymore and they don't have the business. And so, I can do things for "
               'you on the weekend if you\'d like." And I mean, at that poi',
       'timestamp': 175,
       'timestamp_label': '[00:02:55]',
       'timestamp_seconds': 175,
       'tip': "I was working with there's their deals got cut in half by like 75% and so they "
              "can't pay me anymore and they don't have the business. And so, I can do things for "
              'you on the weekend if you\'d like." And I mean, at that poi',
       'title': 'How to Build a Nationwide Notary Team (Step-by-Step) (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=Qn63DtrxFts&t=175s',
       'video_id': 'Qn63DtrxFts'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:26:34](https://www.youtube.com/watch?v=U_Eh790rq3o&t=1594s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'this is a distinction here. So, some of my closing thoughts are, you know, that '
               "this can be a beneficial side to people's wholesaling operations without them "
               'having to completely shut everything with their operation down',
       'timestamp': 1594,
       'timestamp_label': '[00:26:34]',
       'timestamp_seconds': 1594,
       'tip': 'this is a distinction here. So, some of my closing thoughts are, you know, that '
              "this can be a beneficial side to people's wholesaling operations without them "
              'having to completely shut everything with their operation down',
       'title': 'How Wholesalers Can Turn Title Problems Into Profitable Curative Deals (Courtney '
                'Fricke)',
       'url': 'https://www.youtube.com/watch?v=U_Eh790rq3o&t=1594s',
       'video_id': 'U_Eh790rq3o'},
      {'author': 'Regrid',
       'channel': 'Regrid',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:10](https://www.youtube.com/watch?v=X-_cLY3_96Y&t=190s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "drop down so for example let's say that we want to style the properties on a "
               'gradated scale based on their acreage we can do that here so we first choose the '
               'field in this case loveland calculated acres then we go down t',
       'timestamp': 190,
       'timestamp_label': '[00:03:10]',
       'timestamp_seconds': 190,
       'tip': "drop down so for example let's say that we want to style the properties on a "
              'gradated scale based on their acreage we can do that here so we first choose the '
              'field in this case loveland calculated acres then we go down t',
       'title': 'Feature Service Product Demo (Regrid)',
       'url': 'https://www.youtube.com/watch?v=X-_cLY3_96Y&t=190s',
       'video_id': 'X-_cLY3_96Y'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:44:16](https://www.youtube.com/watch?v=DcB4tJku4-A&t=2656s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "don't really you know do I wanna I see that but but the thing here I appreciate is "
               "um I appreciate where you're drawing number one your experience from but also the "
               'the the values and uh stuff a lot of people have alignm',
       'timestamp': 2656,
       'timestamp_label': '[00:44:16]',
       'timestamp_seconds': 2656,
       'tip': "don't really you know do I wanna I see that but but the thing here I appreciate is "
              "um I appreciate where you're drawing number one your experience from but also the "
              'the the values and uh stuff a lot of people have alignm',
       'title': 'Curative Title + Creative Finance: The Combo Most Investors Miss (Courtney '
                'Fricke)',
       'url': 'https://www.youtube.com/watch?v=DcB4tJku4-A&t=2656s',
       'video_id': 'DcB4tJku4-A'}],
 12: [{'author': 'Logan Fullmer',
       'channel': 'Logan Fullmer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:50:00](https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3000s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'like three times a day for seven days. He said by then we abandon the lead. '
               "They'll call them over 20 something times in the first seven days. That's their "
               "process. He said that's how we work. That's how that's just thei",
       'timestamp': 3000,
       'timestamp_label': '[00:50:00]',
       'timestamp_seconds': 3000,
       'tip': "like three times a day for seven days. He said by then we abandon the lead. They'll "
              "call them over 20 something times in the first seven days. That's their process. He "
              "said that's how we work. That's how that's just thei",
       'title': "Skip Tracing for Curative Title: Find Owners Others Can't (Logan Fullmer)",
       'url': 'https://www.youtube.com/watch?v=dJ-LTFmMsTg&t=3000s',
       'video_id': 'dJ-LTFmMsTg'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:55](https://www.youtube.com/watch?v=suJSu-vn6yI&t=55s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "your first signed client. And I'm also going to show you the mistakes that will "
               "cost you deals if you don't catch them early. So, stick around because by the end "
               "of this, you'll have everything that you need to launch yo",
       'timestamp': 55,
       'timestamp_label': '[00:00:55]',
       'timestamp_seconds': 55,
       'tip': "your first signed client. And I'm also going to show you the mistakes that will "
              "cost you deals if you don't catch them early. So, stick around because by the end "
              "of this, you'll have everything that you need to launch yo",
       'title': 'How to start a Surplus Funds Recovery Business in 2026 (for beginners) (Money '
                'Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=suJSu-vn6yI&t=55s',
       'video_id': 'suJSu-vn6yI'},
      {'author': 'ohiocommerce',
       'channel': 'ohiocommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:05](https://www.youtube.com/watch?v=dFKMkAIKskU&t=5s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'and we want people to know that we want to give you your money back we are not '
               'attempting to be a hindrance we are here every day trying to give dollars back so '
               'first on our list would be your personal identification tha',
       'timestamp': 5,
       'timestamp_label': '[00:00:05]',
       'timestamp_seconds': 5,
       'tip': 'and we want people to know that we want to give you your money back we are not '
              'attempting to be a hindrance we are here every day trying to give dollars back so '
              'first on our list would be your personal identification tha',
       'title': 'What Documentation is Needed for Unclaimed Funds (ohiocommerce)',
       'url': 'https://www.youtube.com/watch?v=dFKMkAIKskU&t=5s',
       'video_id': 'dFKMkAIKskU'},
      {'author': 'Probate Mastery',
       'channel': 'Probate Mastery',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:23](https://www.youtube.com/watch?v=T2gvkByDlFU&t=83s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'guaranteed 90-day extension with listing. And another 90 days if you can fall in '
               'the escrow. So, there are attorneys that do that, and they charge $4,500 for that '
               'process. I found an attorney you can do it for 600 bucks.',
       'timestamp': 83,
       'timestamp_label': '[00:01:23]',
       'timestamp_seconds': 83,
       'tip': 'guaranteed 90-day extension with listing. And another 90 days if you can fall in '
              'the escrow. So, there are attorneys that do that, and they charge $4,500 for that '
              'process. I found an attorney you can do it for 600 bucks.',
       'title': '🚨 Probate Property Headed to Foreclosure Auction… Is It Worth Pursuing? (Probate '
                'Mastery)',
       'url': 'https://www.youtube.com/watch?v=T2gvkByDlFU&t=83s',
       'video_id': 'T2gvkByDlFU'},
      {'author': 'Biz Matthew',
       'channel': 'Biz Matthew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:53](https://www.youtube.com/watch?v=W0bwM9N_98Y&t=53s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'uh you know taking the time out of your busy day to come on and to bless the '
               'audience with your knowledge and and about prop stream um first thing i want to '
               'talk about are acts about you know for my audience you know the',
       'timestamp': 53,
       'timestamp_label': '[00:00:53]',
       'timestamp_seconds': 53,
       'tip': 'uh you know taking the time out of your busy day to come on and to bless the '
              'audience with your knowledge and and about prop stream um first thing i want to '
              'talk about are acts about you know for my audience you know the',
       'title': 'Probates List on Propstream Wholesale Real Estate (Biz Matthew)',
       'url': 'https://www.youtube.com/watch?v=W0bwM9N_98Y&t=53s',
       'video_id': 'W0bwM9N_98Y'},
      {'author': 'BYU Library Family History Center',
       'channel': 'BYU Library Family History Center',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:47](https://www.youtube.com/watch?v=CyAfgfoF-eo&t=227s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'happened in the probate action a lot simpler the first step of course would be to '
               "search online for the records it's important to understand that the people who "
               'want to preserve and use probate records are not necessaril',
       'timestamp': 227,
       'timestamp_label': '[00:03:47]',
       'timestamp_seconds': 227,
       'tip': 'happened in the probate action a lot simpler the first step of course would be to '
              "search online for the records it's important to understand that the people who want "
              'to preserve and use probate records are not necessaril',
       'title': 'Probate  Part 2, Wills by James Tanner (BYU Library Family History Center)',
       'url': 'https://www.youtube.com/watch?v=CyAfgfoF-eo&t=227s',
       'video_id': 'CyAfgfoF-eo'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=78s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "themselves. The only reason they're not doing it is simply because they don't know "
               "how, and that's why they're working with us. So, here's the plan. First, we'll "
               "talk about the paperwork that proves that you're even allo",
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': "themselves. The only reason they're not doing it is simply because they don't know "
              "how, and that's why they're working with us. So, here's the plan. First, we'll talk "
              "about the paperwork that proves that you're even allo",
       'title': 'Surplus Funds Recovery: COMPLETE Document List (2026 UPDATE) (Money Making '
                'Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=MVCNlj7HQBQ&t=78s',
       'video_id': 'MVCNlj7HQBQ'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=1AMk1-SB5ic&t=94s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'you have it and you have all your ducks in a row hey a couple quick announcements '
               "first of all my power's still out don't know if you can tell we've been out for a "
               "couple days now hopefully by tomorrow they'll how it tur",
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': 'you have it and you have all your ducks in a row hey a couple quick announcements '
              "first of all my power's still out don't know if you can tell we've been out for a "
              "couple days now hopefully by tomorrow they'll how it tur",
       'title': "Unclaimed Funds: How to Get Your Client's Documents in Order⚡️Unclaimed fund "
                'Client Document finding (Surplus Institute / David Church / Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=1AMk1-SB5ic&t=94s',
       'video_id': '1AMk1-SB5ic'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:52](https://www.youtube.com/watch?v=W-FX20iI9Jk&t=1672s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'they posted about it, right? Uh I know that I was just looking at one and every '
               "Mother's Day they've posted missing their mother, right? So, [gasps] um, again, I "
               "don't want you to just assume just because it's in the obi",
       'timestamp': 1672,
       'timestamp_label': '[00:27:52]',
       'timestamp_seconds': 1672,
       'tip': 'they posted about it, right? Uh I know that I was just looking at one and every '
              "Mother's Day they've posted missing their mother, right? So, [gasps] um, again, I "
              "don't want you to just assume just because it's in the obi",
       'title': 'How to Get Your First Curative Title Deal: A Step-by-Step Guide (Courtney Fricke)',
       'url': 'https://www.youtube.com/watch?v=W-FX20iI9Jk&t=1672s',
       'video_id': 'W-FX20iI9Jk'},
      {'author': 'Genealogy TV',
       'channel': 'Genealogy TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:02](https://www.youtube.com/watch?v=jydLZrDuzCM&t=902s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "13 and I sell you my land when I'm 21 I can go to court and say you took advantage "
               "of me and I can void that transaction because I was underage so if I don't do that "
               "it's a perfectly legal sale but up till the day that I",
       'timestamp': 902,
       'timestamp_label': '[00:15:02]',
       'timestamp_seconds': 902,
       'tip': "13 and I sell you my land when I'm 21 I can go to court and say you took advantage "
              "of me and I can void that transaction because I was underage so if I don't do that "
              "it's a perfectly legal sale but up till the day that I",
       'title': "Understanding Wills, Probate, Estate Records, and Women's Rights for Genealogy "
                '(Genealogy TV)',
       'url': 'https://www.youtube.com/watch?v=jydLZrDuzCM&t=902s',
       'video_id': 'jydLZrDuzCM'},
      {'author': 'Michael Curtis',
       'channel': 'Michael Curtis',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:30](https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=270s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'fill it out um claim form will not get submitted so you must fill everything out '
               'clearly the page is secure with the lock indicating at the top um once you hit '
               'once to finish this information um first name last name you ',
       'timestamp': 270,
       'timestamp_label': '[00:04:30]',
       'timestamp_seconds': 270,
       'tip': 'fill it out um claim form will not get submitted so you must fill everything out '
              'clearly the page is secure with the lock indicating at the top um once you hit once '
              'to finish this information um first name last name you ',
       'title': 'Michigan Unclaimed Property - This is How You Make an Unclaimed Property Claim '
                '(Michael Curtis)',
       'url': 'https://www.youtube.com/watch?v=Fn04U_Yfuzg&t=270s',
       'video_id': 'Fn04U_Yfuzg'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=t4w_wFimZ9A&t=130s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'Okay, so the very first thing is, what is a complaint? A complaint is just a way '
               'of communicating something 0:02:17.6 S1: From somebody that has something that '
               "they don't like, we live in a world right now where people a",
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'Okay, so the very first thing is, what is a complaint? A complaint is just a way of '
              'communicating something 0:02:17.6 S1: From somebody that has something that they '
              "don't like, we live in a world right now where people a",
       'title': 'State Funds Tutorial: Cold Calling Objections vs. Complaints. Surplus Funds 101',
       'url': 'https://www.youtube.com/watch?v=t4w_wFimZ9A&t=130s',
       'video_id': 't4w_wFimZ9A'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=foMCyYJ4LgY&t=176s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': 'quantity and quality of leads and their production for a full work week and just '
               "how I evaluate cancellations and how many somebody should have or shouldn't have, "
               "but really quick... Let's just go over this. 0:03:09.9 S1",
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'quantity and quality of leads and their production for a full work week and just '
              "how I evaluate cancellations and how many somebody should have or shouldn't have, "
              "but really quick... Let's just go over this. 0:03:09.9 S1",
       'title': 'State Funds Tutorial: What To Do When A Deal Cancels While Working Your State '
                'Funds Business. (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=foMCyYJ4LgY&t=176s',
       'video_id': 'foMCyYJ4LgY'},
      {'author': 'ohiocommerce',
       'channel': 'ohiocommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:42](https://www.youtube.com/watch?v=8nmo4S1v3Co&t=1242s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': "four documents in the first group, that's one step to getting your claim faster "
               'cuz we need all of those regardless of what other documentation we might require. '
               'Next slide, please. So, our new website does allow you to ',
       'timestamp': 1242,
       'timestamp_label': '[00:20:42]',
       'timestamp_seconds': 1242,
       'tip': "four documents in the first group, that's one step to getting your claim faster cuz "
              'we need all of those regardless of what other documentation we might require. Next '
              'slide, please. So, our new website does allow you to ',
       'title': 'Ohio Unclaimed Funds: How to Claim Your Cash in 3 Steps (HB 96 Deadline '
                'Explained) Webinar 2-5-2026 (ohiocommerce)',
       'url': 'https://www.youtube.com/watch?v=8nmo4S1v3Co&t=1242s',
       'video_id': '8nmo4S1v3Co'},
      {'author': 'Courtney Fricke',
       'channel': 'Courtney Fricke',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:44](https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=1244s)',
       'relevance': 'Matched corpus commentary on surplus funds, lien priority, skip tracing, or '
                    'claim execution; verify against local statute.',
       'source_type': 'video_pro_tip',
       'text': '"Okay, Courtney, I understand this. I\'m I\'m listening to what you\'re saying, '
               'but how do I actually get my first curative title deal?" That\'s exactly where I '
               "want you to go next. See, I have a video where I'll put out on ",
       'timestamp': 1244,
       'timestamp_label': '[00:20:44]',
       'timestamp_seconds': 1244,
       'tip': '"Okay, Courtney, I understand this. I\'m I\'m listening to what you\'re saying, but '
              'how do I actually get my first curative title deal?" That\'s exactly where I want '
              "you to go next. See, I have a video where I'll put out on ",
       'title': 'Before You Go From Wholesaling to Curative Title, Watch This (Courtney Fricke)',
       'url': 'https://www.youtube.com/watch?v=z6h2w5h7oTQ&t=1244s',
       'video_id': 'z6h2w5h7oTQ'}]}
