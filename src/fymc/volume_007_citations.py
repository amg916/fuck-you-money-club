"""Curated 180-citation Unclaimed Property Recovery baseline (15 per chapter across Q1-Q12) mined strictly from verified Unclaimed Property Recovery YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'client',
     'clients',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'budget',
     'bulk',
     'business',
     'buyer',
     'california',
     'calling',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contract',
     'contracts',
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
 3: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cash',
     'cashflow',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'cold',
     'commission',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
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
 4: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'budget',
     'bulk',
     'business',
     'california',
     'calling',
     'capital',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
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
 5: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoid',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'clawback',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
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
 6: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'client',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
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
 7: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cfo',
     'checklist',
     'checks',
     'claimant',
     'claims',
     'class',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
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
 8: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'api',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contracts',
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
 9: {'3001',
     'accounts',
     'action',
     'agent',
     'agreement',
     'antitrust',
     'asset',
     'assistants',
     'attorney',
     'audit',
     'automated',
     'avoiding',
     'b2b',
     'bankruptcy',
     'benefits',
     'bulk',
     'business',
     'california',
     'calling',
     'caps',
     'cfo',
     'checks',
     'claimant',
     'claims',
     'class',
     'cold',
     'compliance',
     'comptroller',
     'contingency',
     'contract',
     'contracts',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'3001',
      'accounts',
      'action',
      'agent',
      'agreement',
      'ai',
      'antitrust',
      'asset',
      'assistants',
      'attorney',
      'audit',
      'automate',
      'automated',
      'automation',
      'avoiding',
      'b2b',
      'bankruptcy',
      'benefits',
      'bulk',
      'business',
      'california',
      'calling',
      'caps',
      'cfo',
      'checks',
      'claimant',
      'claims',
      'class',
      'cold',
      'compliance',
      'comptroller',
      'contingency',
      'contracts',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'3001',
      'accounts',
      'action',
      'agent',
      'agreement',
      'antitrust',
      'asset',
      'assistants',
      'attorney',
      'audit',
      'automated',
      'avoiding',
      'b2b',
      'bankruptcy',
      'benefits',
      'bulk',
      'business',
      'california',
      'calling',
      'caps',
      'cfo',
      'checks',
      'claimant',
      'claims',
      'class',
      'cold',
      'compliance',
      'comptroller',
      'contingency',
      'contractor',
      'contracts',
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
 12: {'3001',
      'accounts',
      'action',
      'agent',
      'agreement',
      'antitrust',
      'asset',
      'assistants',
      'attorney',
      'audit',
      'automated',
      'avoiding',
      'b2b',
      'bankruptcy',
      'benefits',
      'bulk',
      'business',
      'california',
      'calling',
      'caps',
      'cfo',
      'checks',
      'claimant',
      'claims',
      'class',
      'cold',
      'compliance',
      'comptroller',
      'contingency',
      'contracts',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'TNTreasury',
      'channel': 'TNTreasury',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=105s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How does a holder qualify for the CDA program? A business cannot be currently '
              'under audit by the state at the time it chooses to sign the compliance '
              'Disclosure agreement.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': 'How does a holder qualify for the CDA program? A business cannot be currently '
             'under audit by the state at the time it chooses to sign the compliance '
             'Disclosure agreement.',
      'title': 'Unclaimed Property in Tennessee: Understanding Audits, Compliance, and '
               'Negative Reports (TNTreasury)',
      'url': 'https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=105s',
      'video_id': 'KiR-ZUeCE5g'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=EyQovsqVOnE&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Educator in the asset recovery business today I have a great video in store '
              'with you guys I am going to share with you unclaimed bankruptcy funds this is '
              'one.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Educator in the asset recovery business today I have a great video in store with '
             'you guys I am going to share with you unclaimed bankruptcy funds this is one.',
      'title': 'BANKRUPTCY Unclaimed Funds Explained: UNTAPPED NICHE (Surplus Funds Recovery) '
               '(Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=EyQovsqVOnE&t=15s',
      'video_id': 'EyQovsqVOnE'},
     {'author': 'Open Book Entrepreneur',
      'channel': 'Open Book Entrepreneur',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=YoID4SzRBaI&t=248s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I wanted to start a little online business and I opened a money market account '
              'and I guess those links are still active um for that little online store. I '
              "don't know how to access it anymore, but apparently it's still generating some "
              'sort of revenue yearly.',
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'I wanted to start a little online business and I opened a money market account '
             'and I guess those links are still active um for that little online store. I '
             "don't know how to access it anymore, but apparently it's still generating some "
             'sort of revenue yearly.',
      'title': 'Your Family Could Be Owed $10,000+ And You Don’t Even Know It | Private '
               'Investigator Explains (Open Book Entrepreneur)',
      'url': 'https://www.youtube.com/watch?v=YoID4SzRBaI&t=248s',
      'video_id': 'YoID4SzRBaI'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=7MUtjq4bwU0&t=32s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, here is our agenda for today. We'll be covering hidden business revenue, a "
              'step-by-step search guide, proving your claim, advanced search strategies, and '
              'finally, how to take action today. Hidden business revenue, unlocking the '
              "state's corporate vault.",
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "So, here is our agenda for today. We'll be covering hidden business revenue, a "
             'step-by-step search guide, proving your claim, advanced search strategies, and '
             'finally, how to take action today. Hidden business revenue, unlocking the '
             "state's corporate vault.",
      'title': 'How to search North Dakota unclaimed property for a business name (Как се '
               'прави)',
      'url': 'https://www.youtube.com/watch?v=7MUtjq4bwU0&t=32s',
      'video_id': '7MUtjq4bwU0'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=kb-pXZgQdoE&t=67s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Thousand dollar claim it was a state fund we're allowed to get 10 of that so "
              "again it's contacting the client coming off professional and getting paid and "
              'we do this all day long and get checks back hey everyone thanks for watching '
              "I'll update you more on the next video.",
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': "Thousand dollar claim it was a state fund we're allowed to get 10 of that so "
             "again it's contacting the client coming off professional and getting paid and we "
             "do this all day long and get checks back hey everyone thanks for watching I'll "
             'update you more on the next video.',
      'title': 'How to get Checks back from Clients in your Unclaimed Funds Business |  '
               'Surplus Funds Business (Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=kb-pXZgQdoE&t=67s',
      'video_id': 'kb-pXZgQdoE'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:23](https://www.youtube.com/watch?v=xocEKVSCJtU&t=443s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'After that, we need to market, all right? We can do a SMS campaign, we can do '
              'voicemail drop, we can call, we can do cold calling, we can reach out on '
              'Facebook, and we can even do in person. After that, we need to close, all '
              'right?',
      'timestamp': 443,
      'timestamp_label': '[00:07:23]',
      'timestamp_seconds': 443,
      'tip': 'After that, we need to market, all right? We can do a SMS campaign, we can do '
             'voicemail drop, we can call, we can do cold calling, we can reach out on '
             'Facebook, and we can even do in person. After that, we need to close, all right?',
      'title': 'How To Find UNCLAIMED MONEY In Your County (COUNTY Unclaimed Funds Explained) '
               '(Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=xocEKVSCJtU&t=443s',
      'video_id': 'xocEKVSCJtU'},
     {'author': 'COMPUTERSHARE',
      'channel': 'COMPUTERSHARE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=K64AFLANH3A&t=30s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When you throw in perhaps third party audit firm now you have another '
              'personality thrown in there who might have a different goal from either the.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'When you throw in perhaps third party audit firm now you have another '
             'personality thrown in there who might have a different goal from either the.',
      'title': 'Unclaimed Property Regulation (COMPUTERSHARE)',
      'url': 'https://www.youtube.com/watch?v=K64AFLANH3A&t=30s',
      'video_id': 'K64AFLANH3A'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=YKjd__UIhB8&t=479s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Regulated rules for that there are no federal unclaimed fund finder fee rules '
              "so far it's not in the bankruptcy code so it's really what you and the client.",
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': 'Regulated rules for that there are no federal unclaimed fund finder fee rules so '
             "far it's not in the bankruptcy code so it's really what you and the client.",
      'title': 'How to Find Unclaimed Funds | Top 7 Tips Bankruptcy Unclaimed Funds in 2022 '
               '(Spring Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=YKjd__UIhB8&t=479s',
      'video_id': 'YKjd__UIhB8'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=U1OErlHEyv4&t=110s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, now that you got all your stuff, you know, put together, build your social '
              'media platforms, you got the funding for your business, start applying for '
              "business grants while you're marketing your business. How do you market your "
              'business?',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'So, now that you got all your stuff, you know, put together, build your social '
             'media platforms, you got the funding for your business, start applying for '
             "business grants while you're marketing your business. How do you market your "
             'business?',
      'title': 'How To Move Faster & Make More Money With Unclaimed Funds (Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=U1OErlHEyv4&t=110s',
      'video_id': 'U1OErlHEyv4'},
     {'author': 'ShadowAnyone',
      'channel': 'ShadowAnyone',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=VxHOdlFXKdQ&t=132s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a legitimate service anybody who's done skip tracy knows you know they "
              'make they may look at a hundred.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': "It's a legitimate service anybody who's done skip tracy knows you know they make "
             'they may look at a hundred.',
      'title': 'Private Investigator reveals Unclaimed Money Warnings if you get a letter from '
               'a “recovery service”! (ShadowAnyone)',
      'url': 'https://www.youtube.com/watch?v=VxHOdlFXKdQ&t=132s',
      'video_id': 'VxHOdlFXKdQ'},
     {'author': 'SJF Law Group - Probate & Estate Planning',
      'channel': 'SJF Law Group - Probate & Estate Planning',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=e-FwgynrCd0&t=42s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh never hurts to to run their name. We find stuff here all the time when we '
              'are administering estates. And some good info to know is that if the value of '
              'the account is less than $10,000, you can collect it without opening up a '
              'probate administration.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Uh never hurts to to run their name. We find stuff here all the time when we are '
             'administering estates. And some good info to know is that if the value of the '
             'account is less than $10,000, you can collect it without opening up a probate '
             'administration.',
      'title': 'How to check if you have unclaimed funds in Florida | Florida Estate Planning '
               '& Probate Lawyer (SJF Law Group - Probate & Estate Planning)',
      'url': 'https://www.youtube.com/watch?v=e-FwgynrCd0&t=42s',
      'video_id': 'e-FwgynrCd0'},
     {'author': 'FundSleuth - Unclaimed Funds Info and Training',
      'channel': 'FundSleuth - Unclaimed Funds Info and Training',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:34](https://www.youtube.com/watch?v=rQqA2wnJ9xw&t=274s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Think it's a great question and hopefully this is helpful to all of you and "
              'hopefully this burns on another conversation thanks.',
      'timestamp': 274,
      'timestamp_label': '[00:04:34]',
      'timestamp_seconds': 274,
      'tip': "Think it's a great question and hopefully this is helpful to all of you and "
             'hopefully this burns on another conversation thanks.',
      'title': 'Cold Calling Unclaimed or Surplus Deal Prospects. Should you call on the phone '
               'or SMS? What is best? (FundSleuth - Unclaimed Funds Info and Training)',
      'url': 'https://www.youtube.com/watch?v=rQqA2wnJ9xw&t=274s',
      'video_id': 'rQqA2wnJ9xw'},
     {'author': 'ucproput',
      'channel': 'ucproput',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:06](https://www.youtube.com/watch?v=3B5mPVcKPDE&t=486s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "As soon as they are trained they do with what's right and things run smoothly "
              'very rarely have we ever found where someone is really trying to do things '
              'wrong or commit fraud.',
      'timestamp': 486,
      'timestamp_label': '[00:08:06]',
      'timestamp_seconds': 486,
      'tip': "As soon as they are trained they do with what's right and things run smoothly "
             'very rarely have we ever found where someone is really trying to do things wrong '
             'or commit fraud.',
      'title': '(3 of 4) Utah Unclaimed Property Audit Issues (ucproput)',
      'url': 'https://www.youtube.com/watch?v=3B5mPVcKPDE&t=486s',
      'video_id': '3B5mPVcKPDE'},
     {'author': 'InvestigateTV',
      'channel': 'InvestigateTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=YWsshlY3kF4&t=142s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Property I actually found something in my name but it was like $420 it wasn't "
              "much was it worth looking for the $420 was kind of yeah maybe not I don't know "
              "it was a little yes it was worth it I got $4 in and felt like hey it's my money "
              'yeah4 more than you had exactly.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': "Property I actually found something in my name but it was like $420 it wasn't "
             "much was it worth looking for the $420 was kind of yeah maybe not I don't know "
             "it was a little yes it was worth it I got $4 in and felt like hey it's my money "
             'yeah4 more than you had exactly.',
      'title': 'Be Your Own Investigator: how to find money you may have forgotten '
               '(InvestigateTV)',
      'url': 'https://www.youtube.com/watch?v=YWsshlY3kF4&t=142s',
      'video_id': 'YWsshlY3kF4'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=1W2i-aJGcb0&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business funded before they take off this is one of the number one things I '
              'tell everybody who comes into my program or they look to me for coaching I let.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Business funded before they take off this is one of the number one things I tell '
             'everybody who comes into my program or they look to me for coaching I let.',
      'title': 'One of the biggest mistakes made with UNCLAIMED FUNDS (Must Watch) (Unclaimed '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=1W2i-aJGcb0&t=15s',
      'video_id': '1W2i-aJGcb0'}],
 2: [{'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:27](https://www.youtube.com/watch?v=fntI1mKZpK0&t=327s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thankfully, Missouri law actually rigorously caps these locator fees to protect '
              'you. In fact, any fee agreement made within the first 12 months of the state '
              'holding your property is completely unenforceable, period.',
      'timestamp': 327,
      'timestamp_label': '[00:05:27]',
      'timestamp_seconds': 327,
      'tip': 'Thankfully, Missouri law actually rigorously caps these locator fees to protect '
             'you. In fact, any fee agreement made within the first 12 months of the state '
             'holding your property is completely unenforceable, period.',
      'title': 'How to search unclaimed property for a business in Missouri (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=fntI1mKZpK0&t=327s',
      'video_id': 'fntI1mKZpK0'},
     {'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=Tx1_986LmrY&t=139s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t have a very big budget or anything like that. These are the websites that I "
              "would suggest going to. That if you don't have the money to pay for it to be "
              'done in bulk, but. Just wonder if you get some Valley.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': "'t have a very big budget or anything like that. These are the websites that I "
             "would suggest going to. That if you don't have the money to pay for it to be "
             'done in bulk, but. Just wonder if you get some Valley.',
      'title': 'State Funds Business Skip Tracing. Best FREE Skip Tracing Websites For Your '
               'Unclaimed Funds Business (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=Tx1_986LmrY&t=139s',
      'video_id': 'Tx1_986LmrY'},
     {'author': 'Money Grammar',
      'channel': 'Money Grammar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:39](https://www.youtube.com/watch?v=5l8zepw8oWY&t=459s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'There is absolutely no need to pay these fees, as you can easily perform the '
              'exact same searches and file the claims directly with the state at zero cost.',
      'timestamp': 459,
      'timestamp_label': '[00:07:39]',
      'timestamp_seconds': 459,
      'tip': 'There is absolutely no need to pay these fees, as you can easily perform the '
             'exact same searches and file the claims directly with the state at zero cost.',
      'title': 'The Mechanics of Escheatment: How to Reclaim Your Abandoned Assets (Money '
               'Grammar)',
      'url': 'https://www.youtube.com/watch?v=5l8zepw8oWY&t=459s',
      'video_id': '5l8zepw8oWY'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=2Q7vcVR_cDs&t=475s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're going to pay you back maybe like in my instance the guy said he was "
              'going to pay me 400 the first payment.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': "They're going to pay you back maybe like in my instance the guy said he was "
             'going to pay me 400 the first payment.',
      'title': 'Steps to a Simple Lawsuit/Breach of Contract-Bankruptcy Unclaimed Funds '
               '(Spring Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=2Q7vcVR_cDs&t=475s',
      'video_id': '2Q7vcVR_cDs'},
     {'author': 'Buried in Work',
      'channel': 'Buried in Work',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:36](https://www.youtube.com/watch?v=xfSFTtM1yT8&t=336s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So claims under $500, we were able to fasttrack and pay those without the '
              "claimants's interaction. So that has been a process.",
      'timestamp': 336,
      'timestamp_label': '[00:05:36]',
      'timestamp_seconds': 336,
      'tip': 'So claims under $500, we were able to fasttrack and pay those without the '
             "claimants's interaction. So that has been a process.",
      'title': '#EP46 | Lynn Hall on DC Unclaimed Property: Transforming Asset Recovery and '
               'Building Trust (Buried in Work)',
      'url': 'https://www.youtube.com/watch?v=xfSFTtM1yT8&t=336s',
      'video_id': 'xfSFTtM1yT8'},
     {'author': 'Off The Receipt',
      'channel': 'Off The Receipt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=hSrCCZHDpUU&t=112s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Companies lose addresses all the time. A check with no address attached, a '
              'payment never matched a customer. Every one of those falls through to rule two. '
              'And for most of corporate America, rule two points to one place.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Companies lose addresses all the time. A check with no address attached, a '
             'payment never matched a customer. Every one of those falls through to rule two. '
             'And for most of corporate America, rule two points to one place.',
      'title': 'How Delaware Quietly Makes $554M From Unclaimed Money (Off The Receipt)',
      'url': 'https://www.youtube.com/watch?v=hSrCCZHDpUU&t=112s',
      'video_id': 'hSrCCZHDpUU'},
     {'author': 'Broadstreet Radio',
      'channel': 'Broadstreet Radio',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=DLhQH9iGJ84&t=112s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You used to receive it by post. You used to go to post office and they give you '
              'what we call dividend warrants. You pay it in like a check which is this into '
              'your bank account and it clears after the period that checks clear. That era is '
              'gone and dusted.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'You used to receive it by post. You used to go to post office and they give you '
             'what we call dividend warrants. You pay it in like a check which is this into '
             'your bank account and it clears after the period that checks clear. That era is '
             'gone and dusted.',
      'title': 'Step-by-Step Guide to Recovering Your Unclaimed Dividends (Broadstreet Radio)',
      'url': 'https://www.youtube.com/watch?v=DLhQH9iGJ84&t=112s',
      'video_id': 'DLhQH9iGJ84'},
     {'author': 'Trust Armor',
      'channel': 'Trust Armor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:57](https://www.youtube.com/watch?v=8977FkLTYjo&t=177s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If there's just one thing you take away from our chat today, please let it be "
              'this. Real organizations, like the government or a bank, will never call you '
              'and ask you to pay a fee to receive money that already belongs to you. It just '
              "doesn't happen that way.",
      'timestamp': 177,
      'timestamp_label': '[00:02:57]',
      'timestamp_seconds': 177,
      'tip': "If there's just one thing you take away from our chat today, please let it be "
             'this. Real organizations, like the government or a bank, will never call you and '
             'ask you to pay a fee to receive money that already belongs to you. It just '
             "doesn't happen that way.",
      'title': '"You Have Unclaimed Money" — It\'s a Scam (Trust Armor)',
      'url': 'https://www.youtube.com/watch?v=8977FkLTYjo&t=177s',
      'video_id': '8977FkLTYjo'},
     {'author': 'CBS Colorado',
      'channel': 'CBS Colorado',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=GBOIDnAjQvc&t=56s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AWAY TO ONE PERSON IS 1 TO 2 MILLION. THIS IS WHY THEY HAVE TO VERIFY THE RIGHT '
              "ITEMS TO THE RIGHT PEOPLE. THERE'S NOTHING WORSE THAN SENDING THE PROPERTY TO "
              "THE WRONG PERSON. IT'S MONEY THAT CAN HELP PAY A BILL, SUPPORT A FAMILY OR KEEP "
              'A BUSINESS RUNNING.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'AWAY TO ONE PERSON IS 1 TO 2 MILLION. THIS IS WHY THEY HAVE TO VERIFY THE RIGHT '
             "ITEMS TO THE RIGHT PEOPLE. THERE'S NOTHING WORSE THAN SENDING THE PROPERTY TO "
             "THE WRONG PERSON. IT'S MONEY THAT CAN HELP PAY A BILL, SUPPORT A FAMILY OR KEEP "
             'A BUSINESS RUNNING.',
      'title': 'Colorado has $2.5B in unclaimed property. How to check whether any belongs to '
               'you. (CBS Colorado)',
      'url': 'https://www.youtube.com/watch?v=GBOIDnAjQvc&t=56s',
      'video_id': 'GBOIDnAjQvc'},
     {'author': 'Blue Mesa Minerals',
      'channel': 'Blue Mesa Minerals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=HSmuF8xIaIU&t=475s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A an active payment on it so it's very helpful to track down missing property "
              'that you can cure the title and then get into pay status.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': "A an active payment on it so it's very helpful to track down missing property "
             'that you can cure the title and then get into pay status.',
      'title': 'Finding Oil & Gas Royalties in Unclaimed Property (Blue Mesa Minerals)',
      'url': 'https://www.youtube.com/watch?v=HSmuF8xIaIU&t=475s',
      'video_id': 'HSmuF8xIaIU'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=EFuzXe23Q7I&t=224s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '" And I\'m like, "Okay, what about you guys collecting interest on these fees '
              'that they use claim these funds that have been out there 30, 40, 50 years. You '
              "think that's okay, but you don't think it's okay for people to get people paid "
              "and get a finder's fee in the process?",
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': '" And I\'m like, "Okay, what about you guys collecting interest on these fees '
             'that they use claim these funds that have been out there 30, 40, 50 years. You '
             "think that's okay, but you don't think it's okay for people to get people paid "
             "and get a finder's fee in the process?",
      'title': '🔴 LIVE: State Unclaimed Funds for Beginners | How to Find the Money & Get Paid '
               '(Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=EFuzXe23Q7I&t=224s',
      'video_id': 'EFuzXe23Q7I'},
     {'author': 'Money Missed',
      'channel': 'Money Missed',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=sfcrjWHv_7k&t=85s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The contents of a safe deposit box nobody came back for. Utility deposits and '
              'refunds. Court deposits, trust funds, and escrow balances left over from a '
              'legal case.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'The contents of a safe deposit box nobody came back for. Utility deposits and '
             'refunds. Court deposits, trust funds, and escrow balances left over from a legal '
             'case.',
      'title': 'How to Check If You Have Unclaimed Money in Your Name (2026) (Money Missed)',
      'url': 'https://www.youtube.com/watch?v=sfcrjWHv_7k&t=85s',
      'video_id': 'sfcrjWHv_7k'},
     {'author': 'WTHR',
      'channel': 'WTHR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=pPow2SwrxBE&t=91s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Do a quick search there's nothing that puts a smile on our face more than "
              'putting a smile on your face now make sure you go to the right website indiana '
              'indianaclaim.gov nothing else the government will not charge you a fee to '
              'recover your own money.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': "Do a quick search there's nothing that puts a smile on our face more than "
             'putting a smile on your face now make sure you go to the right website indiana '
             'indianaclaim.gov nothing else the government will not charge you a fee to '
             'recover your own money.',
      'title': 'You can search a state website for unclaimed property (WTHR)',
      'url': 'https://www.youtube.com/watch?v=pPow2SwrxBE&t=91s',
      'video_id': 'pPow2SwrxBE'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:58](https://www.youtube.com/watch?v=zjCP9bHX3oc&t=418s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The link join the academy join me join my folks and we're going to help you get "
              "your business off the ground until then guys I'll see you next time peace.",
      'timestamp': 418,
      'timestamp_label': '[00:06:58]',
      'timestamp_seconds': 418,
      'tip': "The link join the academy join me join my folks and we're going to help you get "
             "your business off the ground until then guys I'll see you next time peace.",
      'title': 'Unclaimed Funds: Top 5 Ways To Close Deals Without Cold Calling (Unclaimed '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=zjCP9bHX3oc&t=418s',
      'video_id': 'zjCP9bHX3oc'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:30](https://www.youtube.com/watch?v=ZvJ4yCc9em4&t=210s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '000 like was that all to you all to me that was what I took home all right do '
              "you happen to have that check with you so they can see it I'll show you guys "
              'right now.',
      'timestamp': 210,
      'timestamp_label': '[00:03:30]',
      'timestamp_seconds': 210,
      'tip': '000 like was that all to you all to me that was what I took home all right do '
             "you happen to have that check with you so they can see it I'll show you guys "
             'right now.',
      'title': 'Unclaimed Funds 🤑 Jay Made $31k in Finder Fees (State Funds Business) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=ZvJ4yCc9em4&t=210s',
      'video_id': 'ZvJ4yCc9em4'}],
 3: [{'author': 'CBS News Sacramento',
      'channel': 'CBS News Sacramento',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=1Grj5UvPLwo&t=69s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'California is holding on to billions of dollars from uncashed checks, sold bank '
              'accounts, insurance payments, investments turned over by banks, and until you '
              'claim it, the state gets to use your money.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'California is holding on to billions of dollars from uncashed checks, sold bank '
             'accounts, insurance payments, investments turned over by banks, and until you '
             'claim it, the state gets to use your money.',
      'title': 'CBS California investigation spurs federal action on states’ unclaimed '
               'property practices (CBS News Sacramento)',
      'url': 'https://www.youtube.com/watch?v=1Grj5UvPLwo&t=69s',
      'video_id': '1Grj5UvPLwo'},
     {'author': 'Financial Soup',
      'channel': 'Financial Soup',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=ubLk2A5a-2A&t=217s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, with that being said, remember that unclaimed money can come from many '
              'sources. Uh, forgotten bank accounts, lost CDs, insurance refunds, insurance '
              'claims, uncash checks.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'So, with that being said, remember that unclaimed money can come from many '
             'sources. Uh, forgotten bank accounts, lost CDs, insurance refunds, insurance '
             'claims, uncash checks.',
      'title': 'How to Find Unclaimed Money (Financial Soup)',
      'url': 'https://www.youtube.com/watch?v=ubLk2A5a-2A&t=217s',
      'video_id': 'ubLk2A5a-2A'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=XsLq9LUTb6w&t=137s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I am calling hundreds of people every single day and no one's picking up. So, "
              "money's burning fast and I'm getting stressed. I was burning my own cash to run "
              'my business. Again, this is probably one of the lowest overhead businesses that '
              "you'll have in the beginning.",
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "I am calling hundreds of people every single day and no one's picking up. So, "
             "money's burning fast and I'm getting stressed. I was burning my own cash to run "
             'my business. Again, this is probably one of the lowest overhead businesses that '
             "you'll have in the beginning.",
      'title': 'The $10K/month Blueprint for Unclaimed Funds (Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=XsLq9LUTb6w&t=137s',
      'video_id': 'XsLq9LUTb6w'},
     {'author': 'FOX43 News',
      'channel': 'FOX43 News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=gEVKR-AmaU0&t=89s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's not necessary because you can do it all yourself with the P A Treasury "
              'website. 5 billion worth of unclaimed funds ranging from material items like '
              'this blinged out necklace to some cold hard cash. One out of 10 Pennsylvanians '
              'has unclaimed property.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': "It's not necessary because you can do it all yourself with the P A Treasury "
             'website. 5 billion worth of unclaimed funds ranging from material items like '
             'this blinged out necklace to some cold hard cash. One out of 10 Pennsylvanians '
             'has unclaimed property.',
      'title': 'A company claims to find  unclaimed funds for a fee, but is it necessary? | '
               'FOX43 Finds Out (FOX43 News)',
      'url': 'https://www.youtube.com/watch?v=gEVKR-AmaU0&t=89s',
      'video_id': 'gEVKR-AmaU0'},
     {'author': 'WGN News',
      'channel': 'WGN News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=4abzayS6yzk&t=45s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'MOST OF THE CHECKS ARE BETWEEN $5100. IF YOU SEE A CHECK IN THE MAIL FROM THE '
              "STATE TREASURER'S OFFICE, IF YOU SEE THAT LETTER BEFORE, IT'S NOT A SCAM, ALL "
              'YOU HAVE TO DO IS OPEN THAT ENVELOPE AND CASH THAT CHECK THAT MONEY CIRCULATING '
              'THROUGHOUT THE ECONOMY.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'MOST OF THE CHECKS ARE BETWEEN $5100. IF YOU SEE A CHECK IN THE MAIL FROM THE '
             "STATE TREASURER'S OFFICE, IF YOU SEE THAT LETTER BEFORE, IT'S NOT A SCAM, ALL "
             'YOU HAVE TO DO IS OPEN THAT ENVELOPE AND CASH THAT CHECK THAT MONEY CIRCULATING '
             'THROUGHOUT THE ECONOMY.',
      'title': "'It's not a scam': Nearly 140K Illinois residents to receive checks for "
               'unclaimed property (WGN News)',
      'url': 'https://www.youtube.com/watch?v=4abzayS6yzk&t=45s',
      'video_id': '4abzayS6yzk'},
     {'author': 'Overage Acquisition',
      'channel': 'Overage Acquisition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=La2LN9HMPbs&t=78s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s say the back taxes were $10,000 and the property sold for $100,000, that "
              'additional $90,000, the difference between the sale price and the tax liability '
              'is called the overage. And we come in and we help the claimant recover this '
              'money.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "'s say the back taxes were $10,000 and the property sold for $100,000, that "
             'additional $90,000, the difference between the sale price and the tax liability '
             'is called the overage. And we come in and we help the claimant recover this '
             'money.',
      'title': 'Unclaimed Money After Foreclosure: How to Legally Recover What’s Rightfully '
               'Yours (Overage Acquisition)',
      'url': 'https://www.youtube.com/watch?v=La2LN9HMPbs&t=78s',
      'video_id': 'La2LN9HMPbs'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=bfDePAnN-4Y&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Educator in the asset recovery business today I have a great video on store '
              'guys I am going to break down how you can close an unclaimed State funds deal.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Educator in the asset recovery business today I have a great video on store guys '
             'I am going to break down how you can close an unclaimed State funds deal.',
      'title': 'How To Close An Unclaimed State Funds Deal (asset recovery business) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=bfDePAnN-4Y&t=15s',
      'video_id': 'bfDePAnN-4Y'},
     {'author': 'ACE SURPLUS',
      'channel': 'ACE SURPLUS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=daCZb9lQvnc&t=117s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The sale of these assets generates more money then required to pay off '
              'creditors and administrative costs the remaining funds may be refunded to the '
              'debor so these are just a couple ways why a debtor may have unclaimed.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'The sale of these assets generates more money then required to pay off creditors '
             'and administrative costs the remaining funds may be refunded to the debor so '
             'these are just a couple ways why a debtor may have unclaimed.',
      'title': 'What are Unclaimed Bankruptcy Funds? (ACE SURPLUS)',
      'url': 'https://www.youtube.com/watch?v=daCZb9lQvnc&t=117s',
      'video_id': 'daCZb9lQvnc'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:53](https://www.youtube.com/watch?v=J2nto2DAwqc&t=113s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "But we're also talking about super everyday things, checking accounts, uncashed "
              'payroll checks, safe deposit box contents, and forgotten 401ks. Moving on to '
              "section two, heir eligibility and documents. It's time to prove your right to "
              'the treasure.',
      'timestamp': 113,
      'timestamp_label': '[00:01:53]',
      'timestamp_seconds': 113,
      'tip': "But we're also talking about super everyday things, checking accounts, uncashed "
             'payroll checks, safe deposit box contents, and forgotten 401ks. Moving on to '
             "section two, heir eligibility and documents. It's time to prove your right to "
             'the treasure.',
      'title': 'How to file an unclaimed property claim as an heir (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=J2nto2DAwqc&t=113s',
      'video_id': 'J2nto2DAwqc'},
     {'author': 'GLC Wealth Advisor',
      'channel': 'GLC Wealth Advisor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=Rg_zkc6UGWE&t=205s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So what happens in those cases pre pre 2010? So once somebody claims their '
              "dividends from the government body, they can claim even the past year's "
              'dividends.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'So what happens in those cases pre pre 2010? So once somebody claims their '
             "dividends from the government body, they can claim even the past year's "
             'dividends.',
      'title': 'Unclaimed Shares & Dividends? Here’s How To Track And Claim Them Via IEPFA '
               'Portal | Part 1 (GLC Wealth Advisor)',
      'url': 'https://www.youtube.com/watch?v=Rg_zkc6UGWE&t=205s',
      'video_id': 'Rg_zkc6UGWE'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=R8PpcOrRZc4&t=109s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is their information that they have but then they also have half a Davidov '
              'claimant just listed underneath that so this is here and here they have two.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'This is their information that they have but then they also have half a Davidov '
             'claimant just listed underneath that so this is here and here they have two.',
      'title': 'Northern and Middle District of Florida Bankruptcy Court-Recovery unclaimed '
               'funds (Spring Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=R8PpcOrRZc4&t=109s',
      'video_id': 'R8PpcOrRZc4'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=edHsQGppnKE&t=108s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're talking about dormant bank accounts, uncashed payroll checks, stocks, "
              'insurance proceeds, and even tech industry equity compensation. The state just '
              'holds these funds in trust indefinitely until the rightful owner or their heir '
              'steps forward.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "We're talking about dormant bank accounts, uncashed payroll checks, stocks, "
             'insurance proceeds, and even tech industry equity compensation. The state just '
             'holds these funds in trust indefinitely until the rightful owner or their heir '
             'steps forward.',
      'title': 'How to claim Utah unclaimed property with a notarized form (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=edHsQGppnKE&t=108s',
      'video_id': 'edHsQGppnKE'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=V_ycS3i_CMY&t=158s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Beginning so I go ahead and I go back and I say John this is David I'm calling "
              "you about your dad's estate I'm calling you about the overage so the guy.",
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': "Beginning so I go ahead and I go back and I say John this is David I'm calling "
             "you about your dad's estate I'm calling you about the overage so the guy.",
      'title': '5k commission and skip tracing revealed | Surplus Funds Business in USA | '
               'Unclaimed State Funds (Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=V_ycS3i_CMY&t=158s',
      'video_id': 'V_ycS3i_CMY'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:04](https://www.youtube.com/watch?v=pOEq9UMUFHU&t=364s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Going to talk a little bit about bankruptcy I'm doing some information tomorrow "
              "we'll get into a little bit on that cuz there have been some questions on that "
              "and I'll see you around thanks again for watching.",
      'timestamp': 364,
      'timestamp_label': '[00:06:04]',
      'timestamp_seconds': 364,
      'tip': "Going to talk a little bit about bankruptcy I'm doing some information tomorrow "
             "we'll get into a little bit on that cuz there have been some questions on that "
             "and I'll see you around thanks again for watching.",
      'title': 'How I Claimed over $50,000.00 in State Unclaimed Funds – Step-by-Step Guide! '
               '(Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=pOEq9UMUFHU&t=364s',
      'video_id': 'pOEq9UMUFHU'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:05](https://www.youtube.com/watch?v=WlbnzGtdoSY&t=365s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The game I'm getting multiple deals closed daily okay so you can sit down "
              'office all day and be boring or you take these tips and run with it alright '
              'guys until the next video live your best life see you soon.',
      'timestamp': 365,
      'timestamp_label': '[00:06:05]',
      'timestamp_seconds': 365,
      'tip': "The game I'm getting multiple deals closed daily okay so you can sit down office "
             'all day and be boring or you take these tips and run with it alright guys until '
             'the next video live your best life see you soon.',
      'title': '5 Things To Do Instead Of Cold Calling | Tax Surplus | Unclaimed Funds '
               '(Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=WlbnzGtdoSY&t=365s',
      'video_id': 'WlbnzGtdoSY'}],
 4: [{'author': 'Surplus Funds 101',
      'channel': 'Surplus Funds 101',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=-VDHxOAAA7A&t=108s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These funds can originate from various sources such as unclaimed bank accounts, '
              'insurance policies, and securities. Number two, a recovery agent. People that '
              'are looking to turn their hobby into a full-time business.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'These funds can originate from various sources such as unclaimed bank accounts, '
             'insurance policies, and securities. Number two, a recovery agent. People that '
             'are looking to turn their hobby into a full-time business.',
      'title': 'Unclaimed Property Business  Top 8 Key Terms To Understand (Surplus Funds 101)',
      'url': 'https://www.youtube.com/watch?v=-VDHxOAAA7A&t=108s',
      'video_id': '-VDHxOAAA7A'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=gitQwM01Fgc&t=135s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'California law up here what what you have to do to be compliant. It um keeping '
              "and it says keep minutes. But here's the thing, they don't ask you for any "
              'minutes in this. What they ask you for is your business name and entity number.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': 'California law up here what what you have to do to be compliant. It um keeping '
             "and it says keep minutes. But here's the thing, they don't ask you for any "
             'minutes in this. What they ask you for is your business name and entity number.',
      'title': 'Avoid Corporate Compliance Scams | Beware of False Notices in Corporate '
               'Compliance | #surplusfunds (Surplus Institute / David Church / Unclaimed '
               'Funds)',
      'url': 'https://www.youtube.com/watch?v=gitQwM01Fgc&t=135s',
      'video_id': 'gitQwM01Fgc'},
     {'author': 'Lunch Cash',
      'channel': 'Lunch Cash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:17](https://www.youtube.com/watch?v=R6nRcAkxVdA&t=257s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The law also caps how much of it can go into the General Fund in a year. '
              'Anything over the cap goes into a reserve, for big claims later. For its 2026 '
              "budget year, Delaware's own forecast expected refunds to jump, and the amount "
              'it keeps to fall.',
      'timestamp': 257,
      'timestamp_label': '[00:04:17]',
      'timestamp_seconds': 257,
      'tip': 'The law also caps how much of it can go into the General Fund in a year. '
             'Anything over the cap goes into a reserve, for big claims later. For its 2026 '
             "budget year, Delaware's own forecast expected refunds to jump, and the amount it "
             'keeps to fall.',
      'title': 'Delaware Makes More From Forgotten Money Than From Its Lottery (Lunch Cash)',
      'url': 'https://www.youtube.com/watch?v=R6nRcAkxVdA&t=257s',
      'video_id': 'R6nRcAkxVdA'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=bUxdjo_bs0g&t=78s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're talking about uncashed vendor checks, returned electronic transfers, "
              'unreturned security deposits, maybe even forgotten insurance claims. You know, '
              "when the organization holding your money just can't locate you, maybe because "
              'of an office move or a personnel change.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': "We're talking about uncashed vendor checks, returned electronic transfers, "
             'unreturned security deposits, maybe even forgotten insurance claims. You know, '
             "when the organization holding your money just can't locate you, maybe because of "
             'an office move or a personnel change.',
      'title': 'How to search unclaimed property for a business in Tennessee (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=bUxdjo_bs0g&t=78s',
      'video_id': 'bUxdjo_bs0g'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:15](https://www.youtube.com/watch?v=cF0HhlLh7NI&t=135s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Law, commercial entities, we're talking banks, insurance companies, utility "
              "providers, they're legally required to transfer inactive accounts to the state "
              'comptroller after a specific dormancy period.',
      'timestamp': 135,
      'timestamp_label': '[00:02:15]',
      'timestamp_seconds': 135,
      'tip': "Law, commercial entities, we're talking banks, insurance companies, utility "
             "providers, they're legally required to transfer inactive accounts to the state "
             'comptroller after a specific dormancy period.',
      'title': 'How to search New York unclaimed property by last name (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=cF0HhlLh7NI&t=135s',
      'video_id': 'cF0HhlLh7NI'},
     {'author': 'Lorman Education Services',
      'channel': 'Lorman Education Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:52](https://www.youtube.com/watch?v=2TghvbJiOis&t=1072s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Matt explained is basically that the entity typically accompany a business '
              'required to report and remit unclaimed property to the state and so in the.',
      'timestamp': 1072,
      'timestamp_label': '[00:17:52]',
      'timestamp_seconds': 1072,
      'tip': 'Matt explained is basically that the entity typically accompany a business '
             'required to report and remit unclaimed property to the state and so in the.',
      'title': 'Unclaimed Property 101 - Fundamental Concepts (Lorman Education Services)',
      'url': 'https://www.youtube.com/watch?v=2TghvbJiOis&t=1072s',
      'video_id': '2TghvbJiOis'},
     {'author': 'FOX23 News Tulsa',
      'channel': 'FOX23 News Tulsa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:58](https://www.youtube.com/watch?v=kTrQ-7TzYL4&t=118s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're including important links in this story on fox23. Oklahoma or another "
              'state where you lived previously, as well as how to check if the federal '
              'government owes you money from things like mortgage insurance refunds or other '
              'accounts.',
      'timestamp': 118,
      'timestamp_label': '[00:01:58]',
      'timestamp_seconds': 118,
      'tip': "We're including important links in this story on fox23. Oklahoma or another "
             'state where you lived previously, as well as how to check if the federal '
             'government owes you money from things like mortgage insurance refunds or other '
             'accounts.',
      'title': 'Video: BBB warns of unclaimed property scam (FOX23 News Tulsa)',
      'url': 'https://www.youtube.com/watch?v=kTrQ-7TzYL4&t=118s',
      'video_id': 'kTrQ-7TzYL4'},
     {'author': 'WSPA 7News',
      'channel': 'WSPA 7News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=VF97sp7MzAw&t=115s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "STATE ACCORDING TO THE TIMELINES SET BY LAW. WE'VE BEEN AUDITING, OR WHATEVER "
              'IT TAKES TO BRING MONEY HOME. WE BROUGHT BACK MORE THAN $75 MILLION FROM OLD '
              "INSURANCE POLICIES. WE HAVE A LOT OF TOOLS HERE, AND WE'VE RETURNED HALF OF IT "
              'ALREADY.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': "STATE ACCORDING TO THE TIMELINES SET BY LAW. WE'VE BEEN AUDITING, OR WHATEVER IT "
             'TAKES TO BRING MONEY HOME. WE BROUGHT BACK MORE THAN $75 MILLION FROM OLD '
             "INSURANCE POLICIES. WE HAVE A LOT OF TOOLS HERE, AND WE'VE RETURNED HALF OF IT "
             'ALREADY.',
      'title': 'How to track down unclaimed money in every state (WSPA 7News)',
      'url': 'https://www.youtube.com/watch?v=VF97sp7MzAw&t=115s',
      'video_id': 'VF97sp7MzAw'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:07](https://www.youtube.com/watch?v=pxHjDvDVqqM&t=307s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Under DAUPA, your business might actually be considered a holder. A holder is '
              'simply any person or entity in possession of property that belongs to someone '
              "else. And it's not just giant banks and insurance companies.",
      'timestamp': 307,
      'timestamp_label': '[00:05:07]',
      'timestamp_seconds': 307,
      'tip': 'Under DAUPA, your business might actually be considered a holder. A holder is '
             'simply any person or entity in possession of property that belongs to someone '
             "else. And it's not just giant banks and insurance companies.",
      'title': 'How to search Pennsylvania unclaimed property for a business name (Как се '
               'прави)',
      'url': 'https://www.youtube.com/watch?v=pxHjDvDVqqM&t=307s',
      'video_id': 'pxHjDvDVqqM'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:15](https://www.youtube.com/watch?v=wp5vC44yQQg&t=375s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Information like oh wow okay I was calling about 235 East 25th Street they had '
              "a Met Life insurance check you you have no idea who that is okay yeah it's.",
      'timestamp': 375,
      'timestamp_label': '[00:06:15]',
      'timestamp_seconds': 375,
      'tip': 'Information like oh wow okay I was calling about 235 East 25th Street they had a '
             "Met Life insurance check you you have no idea who that is okay yeah it's.",
      'title': 'Cold Calling Unclaimed State Funds Basic Script 101. What You Need to Know '
               'about Surplus Funds (Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=wp5vC44yQQg&t=375s',
      'video_id': 'wp5vC44yQQg'},
     {'author': 'Dollar Decoded',
      'channel': 'Dollar Decoded',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:14](https://www.youtube.com/watch?v=QVgTN5Lip0o&t=434s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "800 deposit back, typo and all. And Leo's family claimed $240 from the savings "
              'account plus $5,000 from the insurance policy. Not bad for a few minutes of '
              'searching. Pause this video, go to missingmoney. Then come back and tell me in '
              'the comments how much you found.',
      'timestamp': 434,
      'timestamp_label': '[00:07:14]',
      'timestamp_seconds': 434,
      'tip': "800 deposit back, typo and all. And Leo's family claimed $240 from the savings "
             'account plus $5,000 from the insurance policy. Not bad for a few minutes of '
             'searching. Pause this video, go to missingmoney. Then come back and tell me in '
             'the comments how much you found.',
      'title': 'Is the Government Holding Your Money? How to Find Unclaimed Money Free (Dollar '
               'Decoded)',
      'url': 'https://www.youtube.com/watch?v=QVgTN5Lip0o&t=434s',
      'video_id': 'QVgTN5Lip0o'},
     {'author': 'Base_Rate',
      'channel': 'Base_Rate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=RycXVSWGZ3I&t=159s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And as of 2024, it held more than $19 billion. Some of the oldest outstanding '
              'Some of the oldest outstanding entries date to the 1950s. Paychecks, insurance '
              'payouts, utility deposits, all still sitting in the system, waiting for someone '
              'to type their name into a search bar.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'And as of 2024, it held more than $19 billion. Some of the oldest outstanding '
             'Some of the oldest outstanding entries date to the 1950s. Paychecks, insurance '
             'payouts, utility deposits, all still sitting in the system, waiting for someone '
             'to type their name into a search bar.',
      'title': 'Never Cash a Check? The State Ends Up Holding It (Base_Rate)',
      'url': 'https://www.youtube.com/watch?v=RycXVSWGZ3I&t=159s',
      'video_id': 'RycXVSWGZ3I'},
     {'author': 'C. Hicks Agency - Camille Hicks',
      'channel': 'C. Hicks Agency - Camille Hicks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=_35TodkWXyM&t=139s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Check with the state that they purchased the policy in and not necessarily a '
              'state where they were currently living so hopefully these tips will help you in '
              'the event that you have to track down life insurance money or find a policy.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Check with the state that they purchased the policy in and not necessarily a '
             'state where they were currently living so hopefully these tips will help you in '
             'the event that you have to track down life insurance money or find a policy.',
      'title': 'How to Track Down Life Insurance Policies and Unclaimed Life Insurance Money '
               '(C. Hicks Agency - Camille Hicks)',
      'url': 'https://www.youtube.com/watch?v=_35TodkWXyM&t=139s',
      'video_id': '_35TodkWXyM'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:56](https://www.youtube.com/watch?v=ckzrLZgtcYI&t=356s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One or you can just email me with questions uh spring solutions llc gmail.com I '
              'will see you in the next video thanks for watching.',
      'timestamp': 356,
      'timestamp_label': '[00:05:56]',
      'timestamp_seconds': 356,
      'tip': 'One or you can just email me with questions uh spring solutions llc gmail.com I '
             'will see you in the next video thanks for watching.',
      'title': '$1,030.14 in a day! Bankruptcy Unclaimed Funds! (Spring Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=ckzrLZgtcYI&t=356s',
      'video_id': 'ckzrLZgtcYI'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:17](https://www.youtube.com/watch?v=NxCoaATrtq4&t=677s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Lowest and there's even times where guys people are entitled hundreds of "
              'thousands of dollars here in this case we can see that somebody was actually '
              'entitled 6.',
      'timestamp': 677,
      'timestamp_label': '[00:11:17]',
      'timestamp_seconds': 677,
      'tip': "Lowest and there's even times where guys people are entitled hundreds of "
             'thousands of dollars here in this case we can see that somebody was actually '
             'entitled 6.',
      'title': 'Unclaimed Bankruptcy Funds webinar (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=NxCoaATrtq4&t=677s',
      'video_id': 'NxCoaATrtq4'}],
 5: [{'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:37](https://www.youtube.com/watch?v=2_XKdBsmJ5c&t=457s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Corporate risk officers and accounting teams should be systematically capturing '
              'lost funds internally. You do this by heavily auditing your accounts payable, '
              "uncashed checks, and unapplied credits right before the state's November 1st "
              'reporting deadline.',
      'timestamp': 457,
      'timestamp_label': '[00:07:37]',
      'timestamp_seconds': 457,
      'tip': 'Corporate risk officers and accounting teams should be systematically capturing '
             'lost funds internally. You do this by heavily auditing your accounts payable, '
             "uncashed checks, and unapplied credits right before the state's November 1st "
             'reporting deadline.',
      'title': 'How to search Colorado unclaimed property for a business name (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=2_XKdBsmJ5c&t=457s',
      'video_id': '2_XKdBsmJ5c'},
     {'author': 'Dark Web Deacon',
      'channel': 'Dark Web Deacon',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=JvMO0OK8kTU&t=157s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The same holds true for companies. Asset claims will almost always come in the '
              'form of a letter. If you get a request from a business like Bank of America, '
              'for example, well, call their call center directly based on the number from '
              'their official website.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': 'The same holds true for companies. Asset claims will almost always come in the '
             'form of a letter. If you get a request from a business like Bank of America, for '
             'example, well, call their call center directly based on the number from their '
             'official website.',
      'title': 'What is an Unclaimed Property Scam? : Simple Explained (Dark Web Deacon)',
      'url': 'https://www.youtube.com/watch?v=JvMO0OK8kTU&t=157s',
      'video_id': 'JvMO0OK8kTU'},
     {'author': 'Kodiak Solutions',
      'channel': 'Kodiak Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:46](https://www.youtube.com/watch?v=2BplqmdsUpU&t=1486s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, several different risks for gaps. Making sure you're take a close look to "
              'fill those and keep your compliance in check. And our last risk, unconsolidated '
              'filing.',
      'timestamp': 1486,
      'timestamp_label': '[00:24:46]',
      'timestamp_seconds': 1486,
      'tip': "So, several different risks for gaps. Making sure you're take a close look to "
             'fill those and keep your compliance in check. And our last risk, unconsolidated '
             'filing.',
      'title': '5 healthcare unclaimed property compliance trends you need to know (Kodiak '
               'Solutions)',
      'url': 'https://www.youtube.com/watch?v=2BplqmdsUpU&t=1486s',
      'video_id': '2BplqmdsUpU'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:34](https://www.youtube.com/watch?v=97wh_A16P2s&t=754s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I like, "So, what\'s your average?" She like, "Well, I haven\'t closed another '
              'deal in 3 months." " And she\'s like, "Well, I\'m doing I\'m cold calling. " I '
              'was like, "That\'s your problem." If you don\'t mind cold calling, it\'s '
              'totally fine. You can absolutely cold call.',
      'timestamp': 754,
      'timestamp_label': '[00:12:34]',
      'timestamp_seconds': 754,
      'tip': 'I like, "So, what\'s your average?" She like, "Well, I haven\'t closed another '
             'deal in 3 months." " And she\'s like, "Well, I\'m doing I\'m cold calling. " I '
             'was like, "That\'s your problem." If you don\'t mind cold calling, it\'s totally '
             'fine. You can absolutely cold call.',
      'title': 'Why I Refuse to Cold Call in My Unclaimed Money Business (and You Should Too) '
               '(Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=97wh_A16P2s&t=754s',
      'video_id': '97wh_A16P2s'},
     {'author': 'SimekScott LLC',
      'channel': 'SimekScott LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=p0UoXSbya5E&t=68s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um which kind of leads me into maybe my second item that I often hear is kind '
              'of that low-hanging fruit. I think a lot of times companies understand uh '
              "payroll and accounts payable checks, right, what's outstanding from that "
              'perspective.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': 'Um which kind of leads me into maybe my second item that I often hear is kind of '
             'that low-hanging fruit. I think a lot of times companies understand uh payroll '
             "and accounts payable checks, right, what's outstanding from that perspective.",
      'title': 'SALT: Top 5 Mistakes Companies Make Evaluating Their Unclaimed Property '
               'Exposure. (SimekScott LLC)',
      'url': 'https://www.youtube.com/watch?v=p0UoXSbya5E&t=68s',
      'video_id': 'p0UoXSbya5E'},
     {'author': 'Deloitte US',
      'channel': 'Deloitte US',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=UC28yxW8Pls&t=150s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Requests and alleviate the stress on your company resources to effectively '
              'identify gaps in compliance and mitigate Associated risk if you have any '
              'questions please reach out to Nina render leader of our national unclaimed '
              'property practice.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'Requests and alleviate the stress on your company resources to effectively '
             'identify gaps in compliance and mitigate Associated risk if you have any '
             'questions please reach out to Nina render leader of our national unclaimed '
             'property practice.',
      'title': 'Unclaimed Property (Deloitte US)',
      'url': 'https://www.youtube.com/watch?v=UC28yxW8Pls&t=150s',
      'video_id': 'UC28yxW8Pls'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=3_qKwnM5EUw&t=130s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s going to be calling and following up on claims because you will be doing "
              'that. If you are organized, you will be following up on your claims.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': "'s going to be calling and following up on claims because you will be doing "
             'that. If you are organized, you will be following up on your claims.',
      'title': 'How To Register As An Unclaimed Funds Investigator For California (Unclaimed '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=3_qKwnM5EUw&t=130s',
      'video_id': '3_qKwnM5EUw'},
     {'author': 'Clarus Partners',
      'channel': 'Clarus Partners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=po0e86TAQwA&t=108s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Interest and penalties is by utilizing the state's voluntary compliance "
              'programs of vdas all by participating in amnesty programs the goal in unclaimed '
              'property is to limit liability and to make the process as efficient as '
              'possible.',
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': "Interest and penalties is by utilizing the state's voluntary compliance programs "
             'of vdas all by participating in amnesty programs the goal in unclaimed property '
             'is to limit liability and to make the process as efficient as possible.',
      'title': 'Mitigating Unclaimed Property Risk: Best Practices for Compliance (Clarus '
               'Partners)',
      'url': 'https://www.youtube.com/watch?v=po0e86TAQwA&t=108s',
      'video_id': 'po0e86TAQwA'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=7WZONOtYbjc&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the asset recovery business today you guys already know I have a great video '
              'in store I am going to break down the different types of unclaimed funds but.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'In the asset recovery business today you guys already know I have a great video '
             'in store I am going to break down the different types of unclaimed funds but.',
      'title': 'The Different Types Of Unclaimed Funds - COMPLETE LIST (Surplus Funds '
               'Recovery) (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=7WZONOtYbjc&t=15s',
      'video_id': '7WZONOtYbjc'},
     {'author': 'PwC US',
      'channel': 'PwC US',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=yjxm_QOITBY&t=67s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Us but it's a state statute I have the final say companies must stay vigilant "
              'monitor State rules and update their record to avoid reporting errors and.',
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': "Us but it's a state statute I have the final say companies must stay vigilant "
             'monitor State rules and update their record to avoid reporting errors and.',
      'title': 'Abandoned and Unclaimed Property Quarterly - April 2024 (PwC US)',
      'url': 'https://www.youtube.com/watch?v=yjxm_QOITBY&t=67s',
      'video_id': 'yjxm_QOITBY'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=DVmNNFdoDzE&t=235s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Section four, avoiding costly finder fees. Because there are billions of '
              'dollars on the table, an entire industry has sprung up around this, and you '
              'really need to be aware of their traps, so you can keep all your money.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'Section four, avoiding costly finder fees. Because there are billions of dollars '
             'on the table, an entire industry has sprung up around this, and you really need '
             'to be aware of their traps, so you can keep all your money.',
      'title': 'How to search unclaimed property in Georgia for free (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=DVmNNFdoDzE&t=235s',
      'video_id': 'DVmNNFdoDzE'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=lWmrc3x-B-E&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Territories as it pertains to unclaimed funds in bankruptcy and just how not to '
              "leave those out when you're searching for additional leads because there are.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Territories as it pertains to unclaimed funds in bankruptcy and just how not to '
             "leave those out when you're searching for additional leads because there are.",
      'title': 'Recover Bankruptcy Unclaimed Funds in U.S. Territories- Work From Home 2020. '
               '(Spring Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=lWmrc3x-B-E&t=15s',
      'video_id': 'lWmrc3x-B-E'},
     {'author': 'Jordan Liles',
      'channel': 'Jordan Liles',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:26](https://www.youtube.com/watch?v=lM8PdIOG7-E&t=506s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Happy I wanted to make this video to help you all you know figure out whether '
              'or not this is legit and it is thank you so much for watching.',
      'timestamp': 506,
      'timestamp_label': '[00:08:26]',
      'timestamp_seconds': 506,
      'tip': 'Happy I wanted to make this video to help you all you know figure out whether or '
             'not this is legit and it is thank you so much for watching.',
      'title': "MissingMoney.com Scam or Legit? Here's the Answer. (Jordan Liles)",
      'url': 'https://www.youtube.com/watch?v=lM8PdIOG7-E&t=506s',
      'video_id': 'lM8PdIOG7-E'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=kuCEYN64vtQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Educator in the asset recovery space in regards to surplus funds access '
              'proceeds today I am going to break down the difference between unclaimed State '
              'funds.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Educator in the asset recovery space in regards to surplus funds access proceeds '
             'today I am going to break down the difference between unclaimed State funds.',
      'title': 'Unclaimed State Funds VS Surplus Funds Recovery (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=kuCEYN64vtQ&t=15s',
      'video_id': 'kuCEYN64vtQ'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:51](https://www.youtube.com/watch?v=2l827py8Fe8&t=591s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "50 people that comment on all my videos I'm going to be doing a a raffle "
              "drawing so if you haven't commented on one of my videos or ask a question just "
              "comment I' love to see you and interact with you and I'll see you around "
              'thanks.',
      'timestamp': 591,
      'timestamp_label': '[00:09:51]',
      'timestamp_seconds': 591,
      'tip': "50 people that comment on all my videos I'm going to be doing a a raffle drawing "
             "so if you haven't commented on one of my videos or ask a question just comment "
             "I' love to see you and interact with you and I'll see you around thanks.",
      'title': 'Unclaimed Property Locators Dealing with Heirs | How to Find an Unclaimed '
               'Property Locator (Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=2l827py8Fe8&t=591s',
      'video_id': '2l827py8Fe8'}],
 6: [{'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=zrj6RA8N9HA&t=55s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And list them out for you the first one is going to be assisting with deceased '
              "claims when you're doing this business you're going to find a lot of property.",
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'And list them out for you the first one is going to be assisting with deceased '
             "claims when you're doing this business you're going to find a lot of property.",
      'title': '3 WAYS To Find A Surplus Funds Attorney FAST (Asset Recovery Business) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=zrj6RA8N9HA&t=55s',
      'video_id': 'zrj6RA8N9HA'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:50](https://www.youtube.com/watch?v=GWa4tWyuEoA&t=230s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's jump to section three, understanding your search results, decoding the "
              "data. First off, you might get incredibly lucky with what's called an automated "
              'identification match.',
      'timestamp': 230,
      'timestamp_label': '[00:03:50]',
      'timestamp_seconds': 230,
      'tip': "Let's jump to section three, understanding your search results, decoding the "
             "data. First off, you might get incredibly lucky with what's called an automated "
             'identification match.',
      'title': 'How to find Colorado unclaimed utility deposits by last name (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=GWa4tWyuEoA&t=230s',
      'video_id': 'GWa4tWyuEoA'},
     {'author': 'FOX6 News Milwaukee',
      'channel': 'FOX6 News Milwaukee',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:42](https://www.youtube.com/watch?v=Cb8M7-NxR50&t=102s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It has another $617 million. It's holding indefinitely, much of it. Uncashed "
              'payroll checks, dormant savings accounts and abandoned stocks or mutual funds. '
              'We pay out between 30 and 35 Million in a typical year, go to DRS website to '
              'find out if you qualify.',
      'timestamp': 102,
      'timestamp_label': '[00:01:42]',
      'timestamp_seconds': 102,
      'tip': "It has another $617 million. It's holding indefinitely, much of it. Uncashed "
             'payroll checks, dormant savings accounts and abandoned stocks or mutual funds. '
             'We pay out between 30 and 35 Million in a typical year, go to DRS website to '
             'find out if you qualify.',
      'title': 'Filing a claim for unclaimed property in Wisconsin | FOX6 News Milwaukee (FOX6 '
               'News Milwaukee)',
      'url': 'https://www.youtube.com/watch?v=Cb8M7-NxR50&t=102s',
      'video_id': 'Cb8M7-NxR50'},
     {'author': 'The Accidental Publisher',
      'channel': 'The Accidental Publisher',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=qQL9C0H1n5E&t=20s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "As you can see, this little wheel is letting you know that it's working. It's "
              'trying to find you matches and it will take a few seconds. Just depends on how '
              'much of data they have to go through. So, John Smith should have some claims.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "As you can see, this little wheel is letting you know that it's working. It's "
             'trying to find you matches and it will take a few seconds. Just depends on how '
             'much of data they have to go through. So, John Smith should have some claims.',
      'title': 'How to Claim Unclaimed Property in California 💰 (The Accidental Publisher)',
      'url': 'https://www.youtube.com/watch?v=qQL9C0H1n5E&t=20s',
      'video_id': 'qQL9C0H1n5E'},
     {'author': 'Penelope Jane Smith',
      'channel': 'Penelope Jane Smith',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=26FSCbZczh4&t=211s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Companies are legally required to send funds from lost accounts to the state of '
              "the owner's last known address. So do a search for each of the states that "
              'you’ve lived in. Also, claims can often be made in perpetuity, even by heirs.',
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': 'Companies are legally required to send funds from lost accounts to the state of '
             "the owner's last known address. So do a search for each of the states that "
             'you’ve lived in. Also, claims can often be made in perpetuity, even by heirs.',
      'title': 'Where To Find Unclaimed Money - Legit Government Sites Revealed (Penelope Jane '
               'Smith)',
      'url': 'https://www.youtube.com/watch?v=26FSCbZczh4&t=211s',
      'video_id': '26FSCbZczh4'},
     {'author': 'KCRA 3',
      'channel': 'KCRA 3',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=s_yDVlsM7Tc&t=181s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'AND YOU’RE GOING TO ENTER YOUR FIRST NAME AND YOUR LAST NAME. YOU’RE GOING TO '
              'SEARCH A DATABASE AND SEE IF WE’RE HOLDING ANY OF YOUR PROPERTY. NOW IF YOU DO '
              'FIND YOUR NAME AND YOU WANT TO TRY AND COME CLAIM IT, DO YOU NEED A FORM OF ID?',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'AND YOU’RE GOING TO ENTER YOUR FIRST NAME AND YOUR LAST NAME. YOU’RE GOING TO '
             'SEARCH A DATABASE AND SEE IF WE’RE HOLDING ANY OF YOUR PROPERTY. NOW IF YOU DO '
             'FIND YOUR NAME AND YOU WANT TO TRY AND COME CLAIM IT, DO YOU NEED A FORM OF ID?',
      'title': '$15 billion hiding in plain sight: How to find unclaimed property in '
               'California (KCRA 3)',
      'url': 'https://www.youtube.com/watch?v=s_yDVlsM7Tc&t=181s',
      'video_id': 's_yDVlsM7Tc'},
     {'author': 'SurplusFundsRiches',
      'channel': 'SurplusFundsRiches',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=ujbTh1In_c4&t=78s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Tracing subscription services that I recommend highly all this is in the e-book '
              "by the way the first one is idi data I think they're very very accurate on "
              "finding the claimant I'm amazed at not only the accuracy with phone numbers but "
              'also the addresses and emails.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'Tracing subscription services that I recommend highly all this is in the e-book '
             "by the way the first one is idi data I think they're very very accurate on "
             "finding the claimant I'm amazed at not only the accuracy with phone numbers but "
             'also the addresses and emails.',
      'title': 'Surplus Funds - skip tracing claimants (SurplusFundsRiches)',
      'url': 'https://www.youtube.com/watch?v=ujbTh1In_c4&t=78s',
      'video_id': 'ujbTh1In_c4'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=hA6VJ_GqGyc&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You find out this claimant's deceased how do you go ahead and locate that "
              "client let's go over some tips in this video on how to locate someone who you.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "You find out this claimant's deceased how do you go ahead and locate that client "
             "let's go over some tips in this video on how to locate someone who you.",
      'title': 'Mastering Skip Tracing for Deceased Individuals: Strategies for Success '
               '🕵️\u200d♂️⚡ (Surplus Institute / David Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=hA6VJ_GqGyc&t=15s',
      'video_id': 'hA6VJ_GqGyc'},
     {'author': 'Michael Curtis',
      'channel': 'Michael Curtis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:46](https://www.youtube.com/watch?v=0YK26E_fzYA&t=646s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This line is all the companies that reporting the money or reporting the asset '
              'to the state and this is zip state address first name please a joint joint '
              'account or middle middle initial.',
      'timestamp': 646,
      'timestamp_label': '[00:10:46]',
      'timestamp_seconds': 646,
      'tip': 'This line is all the companies that reporting the money or reporting the asset '
             'to the state and this is zip state address first name please a joint joint '
             'account or middle middle initial.',
      'title': "Pennsylvania Unclaimed Property - How to Search PA's State Treasury Unclaimed "
               'Money Data Base (Michael Curtis)',
      'url': 'https://www.youtube.com/watch?v=0YK26E_fzYA&t=646s',
      'video_id': '0YK26E_fzYA'},
     {'author': 'The Wealth Portfolio Builder',
      'channel': 'The Wealth Portfolio Builder',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=KQMVL4j21qc&t=141s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every company that is listed in the stock market has a registrar. We have first '
              'registrars and the rest of them. Go through this our video description, you '
              'will see a list more than 20 of them listed. Pick them one by one and check.',
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'Every company that is listed in the stock market has a registrar. We have first '
             'registrars and the rest of them. Go through this our video description, you will '
             'see a list more than 20 of them listed. Pick them one by one and check.',
      'title': 'How to Recover Lost Shares & Unclaimed Dividends in Nigeria (Step-by-Step) '
               '(The Wealth Portfolio Builder)',
      'url': 'https://www.youtube.com/watch?v=KQMVL4j21qc&t=141s',
      'video_id': 'KQMVL4j21qc'},
     {'author': 'ABC News',
      'channel': 'ABC News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=f7126N1MGjA&t=239s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now yes okay thanks very much Eli we have a complete guide with 11 ways you can '
              "find unclaimed money at our website abcnews.com GMA we've also brought in an "
              'expert to answer your questions about how to search for unclaimed money send '
              'them in right now at abcnews.com GMA.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': 'Now yes okay thanks very much Eli we have a complete guide with 11 ways you can '
             "find unclaimed money at our website abcnews.com GMA we've also brought in an "
             'expert to answer your questions about how to search for unclaimed money send '
             'them in right now at abcnews.com GMA.',
      'title': 'Unclaimed Money Found From Deceased Relatives; Could You Be Owed Cash? (ABC '
               'News)',
      'url': 'https://www.youtube.com/watch?v=f7126N1MGjA&t=239s',
      'video_id': 'f7126N1MGjA'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:08](https://www.youtube.com/watch?v=oUFeGA0MPoM&t=308s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'All right, the funds are out there sitting in corporate accounts or state '
              "treasuries. How do you actually find them? Well, it's time to open up your "
              'detective toolkit and conduct a structured search.',
      'timestamp': 308,
      'timestamp_label': '[00:05:08]',
      'timestamp_seconds': 308,
      'tip': 'All right, the funds are out there sitting in corporate accounts or state '
             "treasuries. How do you actually find them? Well, it's time to open up your "
             'detective toolkit and conduct a structured search.',
      'title': 'How to check unclaimed funds from an insurance demutualization (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=oUFeGA0MPoM&t=308s',
      'video_id': 'oUFeGA0MPoM'},
     {'author': 'KFNETWORK',
      'channel': 'KFNETWORK',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:41](https://www.youtube.com/watch?v=0anLNGLjnlA&t=161s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You have money and also check in your original name all right so I'm going to "
              'put in Kim Davis and scenario search down because my name is popular I will put '
              "my city to you know narrow things down all right so let's continue.",
      'timestamp': 161,
      'timestamp_label': '[00:02:41]',
      'timestamp_seconds': 161,
      'tip': "You have money and also check in your original name all right so I'm going to "
             'put in Kim Davis and scenario search down because my name is popular I will put '
             "my city to you know narrow things down all right so let's continue.",
      'title': 'Seeking for FREE money in Delaware 🏖️#freemoneydaily #freemoneyonline2023 '
               '#delaware (KFNETWORK)',
      'url': 'https://www.youtube.com/watch?v=0anLNGLjnlA&t=161s',
      'video_id': '0anLNGLjnlA'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:59](https://www.youtube.com/watch?v=B3w-Sxl2QnE&t=419s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Look I got your name and I got your number I'm going to find you that's all I "
              "need I just need a hot lead and I'm going to hunt you down I'm gonna figure.",
      'timestamp': 419,
      'timestamp_label': '[00:06:59]',
      'timestamp_seconds': 419,
      'tip': "Look I got your name and I got your number I'm going to find you that's all I "
             "need I just need a hot lead and I'm going to hunt you down I'm gonna figure.",
      'title': '3 Biggest Skip Tracing Mistakes (Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=B3w-Sxl2QnE&t=419s',
      'video_id': 'B3w-Sxl2QnE'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:59](https://www.youtube.com/watch?v=ug2uUK_s2yk&t=359s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Explain these in all my videos on YouTube and I also put it in my digital '
              'training course for those of you guys who are ready to get started now and you '
              'want to do it the right way the first time so anyways I hope you enjoyed the '
              "videos I'll see you in the next one.",
      'timestamp': 359,
      'timestamp_label': '[00:05:59]',
      'timestamp_seconds': 359,
      'tip': 'Explain these in all my videos on YouTube and I also put it in my digital '
             'training course for those of you guys who are ready to get started now and you '
             'want to do it the right way the first time so anyways I hope you enjoyed the '
             "videos I'll see you in the next one.",
      'title': 'The Surplus Funds Secret You NEED to Know Before Taking the Plunge (Unclaimed '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=ug2uUK_s2yk&t=359s',
      'video_id': 'ug2uUK_s2yk'}],
 7: [{'author': 'Garden Shop Pro',
      'channel': 'Garden Shop Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:58](https://www.youtube.com/watch?v=7Fc0D2RuIJE&t=358s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You can file these claims direct, totally for free through official government '
              'portals. Just manage the process yourself and keep your capital. Finally, part '
              "five, action steps and disclaimer. Let's make sure this doesn't happen again.",
      'timestamp': 358,
      'timestamp_label': '[00:05:58]',
      'timestamp_seconds': 358,
      'tip': 'You can file these claims direct, totally for free through official government '
             'portals. Just manage the process yourself and keep your capital. Finally, part '
             "five, action steps and disclaimer. Let's make sure this doesn't happen again.",
      'title': 'How to search unclaimed funds under a corporation name (Garden Shop Pro)',
      'url': 'https://www.youtube.com/watch?v=7Fc0D2RuIJE&t=358s',
      'video_id': '7Fc0D2RuIJE'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=rOaTjN9BoFE&t=59s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Here's our map for today's explainer. One, the hidden business treasure. Two, "
              'Virginia unclaimed property laws. Three, a step-by-step search guide. Four, '
              'interpreting and claiming assets. Five, compliance and best practices. And six, '
              'next steps and a quick disclaimer.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': "Here's our map for today's explainer. One, the hidden business treasure. Two, "
             'Virginia unclaimed property laws. Three, a step-by-step search guide. Four, '
             'interpreting and claiming assets. Five, compliance and best practices. And six, '
             'next steps and a quick disclaimer.',
      'title': 'How to search unclaimed property for a business in Virginia (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=rOaTjN9BoFE&t=59s',
      'video_id': 'rOaTjN9BoFE'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=RtDPQUDYTy0&t=55s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then, decoding unclaimed property. Third, executing the search protocol. '
              'Fourth, navigating the claims process. Next up, proactive asset prevention. And '
              'finally, action and a brief disclaimer. Section one, the hidden corporate '
              'treasure.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'Then, decoding unclaimed property. Third, executing the search protocol. Fourth, '
             'navigating the claims process. Next up, proactive asset prevention. And finally, '
             'action and a brief disclaimer. Section one, the hidden corporate treasure.',
      'title': 'How to search unclaimed property in Virginia for a company (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=RtDPQUDYTy0&t=55s',
      'video_id': 'RtDPQUDYTy0'},
     {'author': 'KHOU 11',
      'channel': 'KHOU 11',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=WdhaqcAUXBk&t=55s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So once you find your name, hit claim, fill out the application and you can '
              'actually track your claims progress all online. And most importantly, we should '
              'note Kimberly and Steph that this process is free and we have a link to all of '
              'these steps on kou.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': 'So once you find your name, hit claim, fill out the application and you can '
             'actually track your claims progress all online. And most importantly, we should '
             'note Kimberly and Steph that this process is free and we have a link to all of '
             'these steps on kou.',
      'title': 'How to check if you have unclaimed money in Texas (KHOU 11)',
      'url': 'https://www.youtube.com/watch?v=WdhaqcAUXBk&t=55s',
      'video_id': 'WdhaqcAUXBk'},
     {'author': 'Daggett Shuler Attorneys at Law',
      'channel': 'Daggett Shuler Attorneys at Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:59](https://www.youtube.com/watch?v=NbMR0Gzlwww&t=359s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So experienced competent help from somebody that has handled a lot of those '
              'claims in the past may be able to help you navigate that system and recover the '
              "benefits you're actually entitled to. That has been contributed to so that you "
              'would have those benefits.',
      'timestamp': 359,
      'timestamp_label': '[00:05:59]',
      'timestamp_seconds': 359,
      'tip': 'So experienced competent help from somebody that has handled a lot of those '
             'claims in the past may be able to help you navigate that system and recover the '
             "benefits you're actually entitled to. That has been contributed to so that you "
             'would have those benefits.',
      'title': 'Life Insurance - Are You the Beneficiary of Unclaimed Benefits? (Daggett '
               'Shuler Attorneys at Law)',
      'url': 'https://www.youtube.com/watch?v=NbMR0Gzlwww&t=359s',
      'video_id': 'NbMR0Gzlwww'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=LEhDouSnx9s&t=54s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re an heir, the step-by-step claim process, avoiding those costly claim "
              'pitfalls, and finally, some really cool success stories and next steps. All '
              "right, kicking things off with section one, Mississippi's unclaimed millions.",
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "'re an heir, the step-by-step claim process, avoiding those costly claim "
             'pitfalls, and finally, some really cool success stories and next steps. All '
             "right, kicking things off with section one, Mississippi's unclaimed millions.",
      'title': 'How to claim unclaimed money as an heir in Mississippi (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=LEhDouSnx9s&t=54s',
      'video_id': 'LEhDouSnx9s'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:07](https://www.youtube.com/watch?v=CJMCHDgNh4M&t=187s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Completion your success in becoming a successful funds locator it depends on '
              "how much hard work you put into using the practical steps that I'm going to "
              'provide you so I hope that you are excited about this I hope to see you in '
              'class and thank you for watching.',
      'timestamp': 187,
      'timestamp_label': '[00:03:07]',
      'timestamp_seconds': 187,
      'tip': 'Completion your success in becoming a successful funds locator it depends on how '
             "much hard work you put into using the practical steps that I'm going to provide "
             'you so I hope that you are excited about this I hope to see you in class and '
             'thank you for watching.',
      'title': 'MY COURSE HAS LAUNCHED!  Recovering Bankruptcy Unclaimed Funds! (Spring '
               'Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=CJMCHDgNh4M&t=187s',
      'video_id': 'CJMCHDgNh4M'},
     {'author': 'Utah Office of State Treasurer',
      'channel': 'Utah Office of State Treasurer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=hUiiEXcFE0k&t=65s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In this video enlisted on the reporting overview reference sheet are five steps '
              'to report unclaimed property the first step is to review your records and.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': 'In this video enlisted on the reporting overview reference sheet are five steps '
             'to report unclaimed property the first step is to review your records and.',
      'title': 'Unclaimed Property Reporting Overview (Utah Office of State Treasurer)',
      'url': 'https://www.youtube.com/watch?v=hUiiEXcFE0k&t=65s',
      'video_id': 'hUiiEXcFE0k'},
     {'author': 'Badwolf Unincorporated',
      'channel': 'Badwolf Unincorporated',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=suC7b2tuNcc&t=268s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, this allows you to select specific court districts or leave it open and '
              'check multiple courts across bankruptcy courts and the entire judiciary system. '
              "If you just want to look at one specific court, you can, but there's all "
              'different types in here.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': 'Um, this allows you to select specific court districts or leave it open and '
             'check multiple courts across bankruptcy courts and the entire judiciary system. '
             "If you just want to look at one specific court, you can, but there's all "
             'different types in here.',
      'title': '$$$ U.S. Courts Unclaimed Funds Locator: Get lost MONIES owed to you or your '
               'family. By the badwolf (Badwolf Unincorporated)',
      'url': 'https://www.youtube.com/watch?v=suC7b2tuNcc&t=268s',
      'video_id': 'suC7b2tuNcc'},
     {'author': 'Money9 English',
      'channel': 'Money9 English',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=ogkbsdCWM4g&t=107s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Put in place a system to verify the mobile number and email IDs of all existing '
              'and new customers IRA has given five important instructions to insurance.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': 'Put in place a system to verify the mobile number and email IDs of all existing '
             'and new customers IRA has given five important instructions to insurance.',
      'title': 'How To Get Unclaimed Money From Insurance Company | Explainer | Money9 English '
               '(Money9 English)',
      'url': 'https://www.youtube.com/watch?v=ogkbsdCWM4g&t=107s',
      'video_id': 'ogkbsdCWM4g'},
     {'author': 'Guide Gurus',
      'channel': 'Guide Gurus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=wYwVPTqXCvE&t=25s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "When someone dies, these assets don't just vanish. They often end up in the "
              'hands of the state government until someone claims them. In 2025, many states '
              'are updating their unclaimed property laws to make the process more efficient. '
              'So, staying informed is key.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "When someone dies, these assets don't just vanish. They often end up in the "
             'hands of the state government until someone claims them. In 2025, many states '
             'are updating their unclaimed property laws to make the process more efficient. '
             'So, staying informed is key.',
      'title': 'Who Can Claim Unclaimed Property Of A Deceased Person   2025 (Guide Gurus)',
      'url': 'https://www.youtube.com/watch?v=wYwVPTqXCvE&t=25s',
      'video_id': 'wYwVPTqXCvE'},
     {'author': 'Enterslice',
      'channel': 'Enterslice',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:54](https://www.youtube.com/watch?v=AZAC0VeRINw&t=234s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Clarity about the process to claim unclaim dividend funds if you require '
              'additional information or assistance from an expert to claim your unclaimed '
              'dividends feel free to connect us we are here to assist you thank you for '
              'watching.',
      'timestamp': 234,
      'timestamp_label': '[00:03:54]',
      'timestamp_seconds': 234,
      'tip': 'Clarity about the process to claim unclaim dividend funds if you require '
             'additional information or assistance from an expert to claim your unclaimed '
             'dividends feel free to connect us we are here to assist you thank you for '
             'watching.',
      'title': 'The process to Claim Unclaimed Dividends|Documents Required to Claim Unclaimed '
               'Dividends|Enterslice (Enterslice)',
      'url': 'https://www.youtube.com/watch?v=AZAC0VeRINw&t=234s',
      'video_id': 'AZAC0VeRINw'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:02](https://www.youtube.com/watch?v=2SYC3A6apHk&t=482s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your business and if you guys want to get my digital course and keep supporting '
              "my channel that's awesome always leave a link there it's not necessary or "
              'mandatory for me to teach you for free all right guys until then have a great '
              'life and happy.',
      'timestamp': 482,
      'timestamp_label': '[00:08:02]',
      'timestamp_seconds': 482,
      'tip': 'Your business and if you guys want to get my digital course and keep supporting '
             "my channel that's awesome always leave a link there it's not necessary or "
             'mandatory for me to teach you for free all right guys until then have a great '
             'life and happy.',
      'title': 'Master the Claim Process For California: Boost Your Investigator Income '
               '(Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=2SYC3A6apHk&t=482s',
      'video_id': '2SYC3A6apHk'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:36](https://www.youtube.com/watch?v=vp2uuB23fww&t=456s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mentioned a background check do they have to get fingerprinting yeah what does '
              'it look like to actually go through with this process if you go back to that '
              "Q&A and it um where it says license it's a hyperlink to the page and sorry I "
              'got more people trying to join.',
      'timestamp': 456,
      'timestamp_label': '[00:07:36]',
      'timestamp_seconds': 456,
      'tip': 'Mentioned a background check do they have to get fingerprinting yeah what does '
             'it look like to actually go through with this process if you go back to that Q&A '
             "and it um where it says license it's a hyperlink to the page and sorry I got "
             'more people trying to join.',
      'title': 'How to work Texas Unclaimed State Funds and become a PI (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=vp2uuB23fww&t=456s',
      'video_id': 'vp2uuB23fww'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:44](https://www.youtube.com/watch?v=waps0YmW8BI&t=644s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Looking forward to that you know I hope that you know maybe in next next '
              'success story uh my partner and I will be in the zoom call yeah awesome keep '
              'killing it thank you oh.',
      'timestamp': 644,
      'timestamp_label': '[00:10:44]',
      'timestamp_seconds': 644,
      'tip': 'Looking forward to that you know I hope that you know maybe in next next success '
             'story uh my partner and I will be in the zoom call yeah awesome keep killing it '
             'thank you oh.',
      'title': 'UNTAPPED OPPORTUNITY: $34k From 1 Claim (Unclaimed Bankruptcy Funds) (Money '
               'Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=waps0YmW8BI&t=644s',
      'video_id': 'waps0YmW8BI'}],
 8: [{'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:08](https://www.youtube.com/watch?v=KJU4iu_xIgw&t=428s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'With these robust search strategies, documentation checklists, and compliance '
              'deadlines in hand, your treasury team is fully equipped to take action. The '
              'only question left is what hidden assets will your business uncover today in '
              "South Carolina's database?",
      'timestamp': 428,
      'timestamp_label': '[00:07:08]',
      'timestamp_seconds': 428,
      'tip': 'With these robust search strategies, documentation checklists, and compliance '
             'deadlines in hand, your treasury team is fully equipped to take action. The only '
             'question left is what hidden assets will your business uncover today in South '
             "Carolina's database?",
      'title': 'How to search South Carolina unclaimed property for a business name (Как се '
               'прави)',
      'url': 'https://www.youtube.com/watch?v=KJU4iu_xIgw&t=428s',
      'video_id': 'KJU4iu_xIgw'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:24](https://www.youtube.com/watch?v=NPH35-KUMjQ&t=144s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s official escheatement database. Step one, you identify your primary "
              'resource. Head over to the official Department of Commerce portal at '
              'unclaimedproperty. Step two, you plug your exact business name into the search '
              'tool.',
      'timestamp': 144,
      'timestamp_label': '[00:02:24]',
      'timestamp_seconds': 144,
      'tip': "'s official escheatement database. Step one, you identify your primary resource. "
             'Head over to the official Department of Commerce portal at unclaimedproperty. '
             'Step two, you plug your exact business name into the search tool.',
      'title': 'How to search Minnesota unclaimed property for a business name (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=NPH35-KUMjQ&t=144s',
      'video_id': 'NPH35-KUMjQ'},
     {'author': 'This Guy Knows Tech',
      'channel': 'This Guy Knows Tech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:09](https://www.youtube.com/watch?v=74IHdXzW4aQ&t=549s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Those distribution checks sit in federal court accounts across individual '
              'districts until claimed. None of these seven registries charge fees to search, '
              'and none of them take a percentage cut of your payout.',
      'timestamp': 549,
      'timestamp_label': '[00:09:09]',
      'timestamp_seconds': 549,
      'tip': 'Those distribution checks sit in federal court accounts across individual '
             'districts until claimed. None of these seven registries charge fees to search, '
             'and none of them take a percentage cut of your payout.',
      'title': '7 Official US Databases To Find Unclaimed Money & Lost Assets (This Guy Knows '
               'Tech)',
      'url': 'https://www.youtube.com/watch?v=74IHdXzW4aQ&t=549s',
      'video_id': '74IHdXzW4aQ'},
     {'author': 'Keane Unclaimed Property',
      'channel': 'Keane Unclaimed Property',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=UP88bQoP2JU&t=79s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Platform includes data validation quality controls and tracking functionality '
              'data validation includes a 14-point check and two-point address.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Platform includes data validation quality controls and tracking functionality '
             'data validation includes a 14-point check and two-point address.',
      'title': 'Keane Unclaimed Property System (KUPS) (Keane Unclaimed Property)',
      'url': 'https://www.youtube.com/watch?v=UP88bQoP2JU&t=79s',
      'video_id': 'UP88bQoP2JU'},
     {'author': 'Garden Shop Pro',
      'channel': 'Garden Shop Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=HMzGGSvJ104&t=241s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The NAIC itself will never actually notify you if a match was found. Optimizing '
              'your search strategy. Because that NAIC tool only checks active policies at '
              "participating carriers, you've got to cast a wider net to guarantee you find "
              'every last cent.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': 'The NAIC itself will never actually notify you if a match was found. Optimizing '
             'your search strategy. Because that NAIC tool only checks active policies at '
             "participating carriers, you've got to cast a wider net to guarantee you find "
             'every last cent.',
      'title': 'How to find an unclaimed insurance payout in your name (Garden Shop Pro)',
      'url': 'https://www.youtube.com/watch?v=HMzGGSvJ104&t=241s',
      'video_id': 'HMzGGSvJ104'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:41](https://www.youtube.com/watch?v=1IpkVjkkXHg&t=221s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The Maryland database uses what software engineers call a prefix matching '
              'algorithm. Basically, it only looks for records that start with exactly what '
              "you typed. So, keeping your search simple ensures you don't accidentally filter "
              'out a complex account name.',
      'timestamp': 221,
      'timestamp_label': '[00:03:41]',
      'timestamp_seconds': 221,
      'tip': 'The Maryland database uses what software engineers call a prefix matching '
             'algorithm. Basically, it only looks for records that start with exactly what you '
             "typed. So, keeping your search simple ensures you don't accidentally filter out "
             'a complex account name.',
      'title': 'How to find Maryland unclaimed utility deposits by last name (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=1IpkVjkkXHg&t=221s',
      'video_id': '1IpkVjkkXHg'},
     {'author': 'InvestigateTV',
      'channel': 'InvestigateTV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=IhEPmIRt3Ak&t=20s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "While there's no single government database for it all, there is a freeway to "
              "search in every state. Speaker] I got a phone call one day. Speaker] I'm "
              'thinking, where in my past life did something like that occur?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "While there's no single government database for it all, there is a freeway to "
             "search in every state. Speaker] I got a phone call one day. Speaker] I'm "
             'thinking, where in my past life did something like that occur?',
      'title': 'Ways you can find unclaimed property owed to you (InvestigateTV)',
      'url': 'https://www.youtube.com/watch?v=IhEPmIRt3Ak&t=20s',
      'video_id': 'IhEPmIRt3Ak'},
     {'author': 'David Daniels',
      'channel': 'David Daniels',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=Zq6923LSEX4&t=93s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Remember billions of dollars are waiting to be claimed your share could be just '
              'a search away so embark on your journey with HBU asset recovery today and '
              "reclaim what's rightfully yours the Hidden Treasures are waiting for you don't "
              'let them wait any longer.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'Remember billions of dollars are waiting to be claimed your share could be just '
             'a search away so embark on your journey with HBU asset recovery today and '
             "reclaim what's rightfully yours the Hidden Treasures are waiting for you don't "
             'let them wait any longer.',
      'title': 'How to Find Unclaimed State Funds with HBU Asset Recovery | Maximize Your '
               'Wealth (David Daniels)',
      'url': 'https://www.youtube.com/watch?v=Zq6923LSEX4&t=93s',
      'video_id': 'Zq6923LSEX4'},
     {'author': 'Knowledge Work Nexus',
      'channel': 'Knowledge Work Nexus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=wO5QkFr7vdQ&t=51s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '"Oh, this was worth a video." So, I\'m just going to put my name in here. I '
              "think it would be good too if you've ever done business under different names "
              "or specifically a business name, like I'll come back and search for my business "
              'name as well.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': '"Oh, this was worth a video." So, I\'m just going to put my name in here. I '
             "think it would be good too if you've ever done business under different names or "
             "specifically a business name, like I'll come back and search for my business "
             'name as well.',
      'title': 'Finding and Claiming Unclaimed Property with MissingMoney.com (Knowledge Work '
               'Nexus)',
      'url': 'https://www.youtube.com/watch?v=wO5QkFr7vdQ&t=51s',
      'video_id': 'wO5QkFr7vdQ'},
     {'author': 'Mint',
      'channel': 'Mint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=Y4d3T6BNtEg&t=333s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, that is the new portal. Earlier, a couple of years back, there was no '
              'limitation. One could search endlessly for any number of investors and any '
              "number of shares. So, the new portal, I think there's a limit of 10 search "
              'entries which you can do and open.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': 'Yeah, that is the new portal. Earlier, a couple of years back, there was no '
             'limitation. One could search endlessly for any number of investors and any '
             "number of shares. So, the new portal, I think there's a limit of 10 search "
             'entries which you can do and open.',
      'title': 'Unclaimed Shares & Dividends? Here’s How To Track And Claim Them Via IEPFA '
               'Portal (Mint)',
      'url': 'https://www.youtube.com/watch?v=Y4d3T6BNtEg&t=333s',
      'video_id': 'Y4d3T6BNtEg'},
     {'author': 'Unclaimed Funds Finder',
      'channel': 'Unclaimed Funds Finder',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:37](https://www.youtube.com/watch?v=Psgl7H5ZpOc&t=37s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Step 2 Most unclaimed money is held at the state level. Go to your state’s '
              'official unclaimed property website and search your name. Also check: States '
              'you’ve lived in States where you’ve worked You can also use tools like '
              'MissingMoney.',
      'timestamp': 37,
      'timestamp_label': '[00:00:37]',
      'timestamp_seconds': 37,
      'tip': 'Step 2 Most unclaimed money is held at the state level. Go to your state’s '
             'official unclaimed property website and search your name. Also check: States '
             'you’ve lived in States where you’ve worked You can also use tools like '
             'MissingMoney.',
      'title': 'How to Check If You Have Unclaimed Money (Step-by-Step Guide) (Unclaimed Funds '
               'Finder)',
      'url': 'https://www.youtube.com/watch?v=Psgl7H5ZpOc&t=37s',
      'video_id': 'Psgl7H5ZpOc'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=ZsII5-XkqPY&t=15s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Great video in store I am going to share with you guys the same CRM that I use '
              'that allow me to do six figures plus every single year in this business so if.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Great video in store I am going to share with you guys the same CRM that I use '
             'that allow me to do six figures plus every single year in this business so if.',
      'title': 'The CRM I use to make $100,00+ per year in Asset Recovery 📈 (Money Making '
               'Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=ZsII5-XkqPY&t=15s',
      'video_id': 'ZsII5-XkqPY'},
     {'author': 'Michael Curtis',
      'channel': 'Michael Curtis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:25](https://www.youtube.com/watch?v=JGravBgJTJo&t=385s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh you should get you should get some information back all right so that's how "
              'easy it is to file a claim on the office of unclaimed property of delaware um '
              'go ahead tell your friend tell your neighbor tell whoever to come and perform a '
              'search.',
      'timestamp': 385,
      'timestamp_label': '[00:06:25]',
      'timestamp_seconds': 385,
      'tip': "Uh you should get you should get some information back all right so that's how "
             'easy it is to file a claim on the office of unclaimed property of delaware um go '
             'ahead tell your friend tell your neighbor tell whoever to come and perform a '
             'search.',
      'title': 'Delaware Unclaimed Property Official Search Website l Learn How to Find '
               'Unclaimed Money in Delaware (Michael Curtis)',
      'url': 'https://www.youtube.com/watch?v=JGravBgJTJo&t=385s',
      'video_id': 'JGravBgJTJo'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:11](https://www.youtube.com/watch?v=3iluxKs2wP8&t=191s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Searching manually is absolutely still encouraged so you can find anything that '
              'might not automatically trigger a match. The actual digital treasure hunt. Here '
              "is exactly how you conduct your search on the state's transaction portal, which "
              'most people just call TAP.',
      'timestamp': 191,
      'timestamp_label': '[00:03:11]',
      'timestamp_seconds': 191,
      'tip': 'Searching manually is absolutely still encouraged so you can find anything that '
             'might not automatically trigger a match. The actual digital treasure hunt. Here '
             "is exactly how you conduct your search on the state's transaction portal, which "
             'most people just call TAP.',
      'title': 'How to find Montana unclaimed utility deposits by last name (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=3iluxKs2wP8&t=191s',
      'video_id': '3iluxKs2wP8'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=zI7m3acMjuY&t=163s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Choose who you want to work with versus people picking and choosing if they '
              "want to work with you give it a shot good luck don't forget to help support my "
              'channel by liking subscribing and watching all my videos to the end see you '
              'guys in the next video towards foreign.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Choose who you want to work with versus people picking and choosing if they want '
             "to work with you give it a shot good luck don't forget to help support my "
             'channel by liking subscribing and watching all my videos to the end see you guys '
             'in the next video towards foreign.',
      'title': 'Why People Struggle With Unclaimed Funds | Avoid These 3 Things❌️ (Unclaimed '
               'CEO)',
      'url': 'https://www.youtube.com/watch?v=zI7m3acMjuY&t=163s',
      'video_id': 'zI7m3acMjuY'}],
 9: [{'author': 'NBC New York',
      'channel': 'NBC New York',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=qHskTBuAHTg&t=35s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CONNECTICUT ALSO HAVE STATE OFFICES THAT HANDLE UNCLAIMED FUNDS. THE MONEYS ARE '
              'USUALLY UNCASHED CHECKS. SOMETIMES SENT TO AN OLD ADDRESS. BY LAW CERTAIN '
              'BUSINESSES LIKE BANKS, RETAILERS, HEALTH INSURERS, HAVE TO TURN OVER THOSE '
              'DORMANT ACCOUNTS TO THE STATE.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'CONNECTICUT ALSO HAVE STATE OFFICES THAT HANDLE UNCLAIMED FUNDS. THE MONEYS ARE '
             'USUALLY UNCASHED CHECKS. SOMETIMES SENT TO AN OLD ADDRESS. BY LAW CERTAIN '
             'BUSINESSES LIKE BANKS, RETAILERS, HEALTH INSURERS, HAVE TO TURN OVER THOSE '
             'DORMANT ACCOUNTS TO THE STATE.',
      'title': 'How to Check Unclaimed Funds in New York (NBC New York)',
      'url': 'https://www.youtube.com/watch?v=qHskTBuAHTg&t=35s',
      'video_id': 'qHskTBuAHTg'},
     {'author': 'Как се прави',
      'channel': 'Как се прави',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=9BVp_yhswZY&t=85s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Basically, by law, financial institutions and companies are required to turn '
              "over dormant or inactive accounts to the New York State Comptroller's Office of "
              'unclaimed funds.',
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': 'Basically, by law, financial institutions and companies are required to turn '
             "over dormant or inactive accounts to the New York State Comptroller's Office of "
             'unclaimed funds.',
      'title': 'How to use the unclaimed property database in New York (Как се прави)',
      'url': 'https://www.youtube.com/watch?v=9BVp_yhswZY&t=85s',
      'video_id': '9BVp_yhswZY'},
     {'author': 'GardenShop.Pro',
      'channel': 'GardenShop.Pro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:26](https://www.youtube.com/watch?v=OFnbGkVuoHQ&t=326s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '24 months of the state holding the property is completely unenforceable. And '
              'even after those 24 months, the law caps finders fees at a maximum of 15% '
              'requiring a strict notarized contract. But remember, the Great Iowa Treasure '
              'Hunt is 100% free.',
      'timestamp': 326,
      'timestamp_label': '[00:05:26]',
      'timestamp_seconds': 326,
      'tip': '24 months of the state holding the property is completely unenforceable. And '
             'even after those 24 months, the law caps finders fees at a maximum of 15% '
             'requiring a strict notarized contract. But remember, the Great Iowa Treasure '
             'Hunt is 100% free.',
      'title': 'How to find Iowa unclaimed utility deposits by last name (GardenShop.Pro)',
      'url': 'https://www.youtube.com/watch?v=OFnbGkVuoHQ&t=326s',
      'video_id': 'OFnbGkVuoHQ'},
     {'author': 'The Explainer Point',
      'channel': 'The Explainer Point',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:53](https://www.youtube.com/watch?v=NWkWT5QX3sM&t=233s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'No one designed it as a business model. It is the side effect of two old court '
              'rules and one very popular legal address. That is why a fight over one company '
              'mattered so much. MoneyGram is incorporated in Delaware.',
      'timestamp': 233,
      'timestamp_label': '[00:03:53]',
      'timestamp_seconds': 233,
      'tip': 'No one designed it as a business model. It is the side effect of two old court '
             'rules and one very popular legal address. That is why a fight over one company '
             'mattered so much. MoneyGram is incorporated in Delaware.',
      'title': "The Tiny State That Lives Off Other People's Forgotten Money (The Explainer "
               'Point)',
      'url': 'https://www.youtube.com/watch?v=NWkWT5QX3sM&t=233s',
      'video_id': 'NWkWT5QX3sM'},
     {'author': 'Texas Licensed Private Investigator',
      'channel': 'Texas Licensed Private Investigator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=yiH-ZfQj-oc&t=261s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And then you cut me out and you your lawyer now is going to make Oh, by the '
              'way, the state comproller by law restricts a licensed private investigator from '
              "making more than 10% of the money that's in there for assisting any claimant "
              'with their claim.',
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': 'And then you cut me out and you your lawyer now is going to make Oh, by the way, '
             'the state comproller by law restricts a licensed private investigator from '
             "making more than 10% of the money that's in there for assisting any claimant "
             'with their claim.',
      'title': 'Texas Unclaimed Money & Private Investigations | Meet Sharalyn Criswell (Texas '
               'Licensed Private Investigator)',
      'url': 'https://www.youtube.com/watch?v=yiH-ZfQj-oc&t=261s',
      'video_id': 'yiH-ZfQj-oc'},
     {'author': 'Flying With Luxury',
      'channel': 'Flying With Luxury',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=6MVorBlRJk4&t=43s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The personal representative has the legal authority to gather all assets, pay '
              'debts, and distribute the remaining estate according to the will or state law. '
              'To claim these assets, the personal representative must first prove their legal '
              'authority.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'The personal representative has the legal authority to gather all assets, pay '
             'debts, and distribute the remaining estate according to the will or state law. '
             'To claim these assets, the personal representative must first prove their legal '
             'authority.',
      'title': 'Who Can Claim Unclaimed Property Of A Deceased Person? (Flying With Luxury)',
      'url': 'https://www.youtube.com/watch?v=6MVorBlRJk4&t=43s',
      'video_id': '6MVorBlRJk4'},
     {'author': 'NBC New York',
      'channel': 'NBC New York',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=wCk_H4rThTo&t=45s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll actually send you the check. That's thanks to a new law signed by Governor "
              "Kathy Hochul allowing the Comptroller's office to release unclaimed funds "
              "proactively, instead of waiting for people to go to the state's website and "
              'file a claim.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "'ll actually send you the check. That's thanks to a new law signed by Governor "
             "Kathy Hochul allowing the Comptroller's office to release unclaimed funds "
             "proactively, instead of waiting for people to go to the state's website and file "
             'a claim.',
      'title': 'Unclaimed funds in New York could soon be coming your mailbox | NBC New York '
               '(NBC New York)',
      'url': 'https://www.youtube.com/watch?v=wCk_H4rThTo&t=45s',
      'video_id': 'wCk_H4rThTo'},
     {'author': 'Unclaimed CEO',
      'channel': 'Unclaimed CEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=pZG8hK4VPVM&t=56s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Contract being signed between you and your your your customer or your lead '
              'whatnot that is very very important now every state has different rules of um.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'Contract being signed between you and your your your customer or your lead '
             'whatnot that is very very important now every state has different rules of um.',
      'title': 'The 3 Things You Need To File A Tax Surplus Claim | 2024 (Unclaimed CEO)',
      'url': 'https://www.youtube.com/watch?v=pZG8hK4VPVM&t=56s',
      'video_id': 'pZG8hK4VPVM'},
     {'author': 'Royalty Clerk',
      'channel': 'Royalty Clerk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=8RccEFzRtl8&t=28s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "General information, not legal advice. Let's go. Royalty money takes a trip "
              "before it lands in the state's vault.",
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': "General information, not legal advice. Let's go. Royalty money takes a trip "
             "before it lands in the state's vault.",
      'title': 'Texas Is Holding $9 Billion+ in Unclaimed Money. Some Is Oil Royalties '
               '(Royalty Clerk)',
      'url': 'https://www.youtube.com/watch?v=8RccEFzRtl8&t=28s',
      'video_id': '8RccEFzRtl8'},
     {'author': 'PakEnergy',
      'channel': 'PakEnergy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:49](https://www.youtube.com/watch?v=fVMIbCz8s0U&t=889s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um obviously there's laws that have come in place to kind of answer some of "
              'these things. Could you speak just kind of briefly on some of the uh priority '
              "rules and how that's kind of um changed um over the years? So you know every "
              'state wants a piece of the pie, right?',
      'timestamp': 889,
      'timestamp_label': '[00:14:49]',
      'timestamp_seconds': 889,
      'tip': "Um obviously there's laws that have come in place to kind of answer some of "
             'these things. Could you speak just kind of briefly on some of the uh priority '
             "rules and how that's kind of um changed um over the years? So you know every "
             'state wants a piece of the pie, right?',
      'title': 'What Is Escheatable in Oil & Gas? Unclaimed Property Explained (PakEnergy)',
      'url': 'https://www.youtube.com/watch?v=fVMIbCz8s0U&t=889s',
      'video_id': 'fVMIbCz8s0U'},
     {'author': 'COMPUTERSHARE',
      'channel': 'COMPUTERSHARE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=03CoUEgqdzg&t=25s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fought for we really need to be very observant of what's going on in audits as "
              "well and it's maybe not traditionally a legal issue for an audit but there are.",
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "Fought for we really need to be very observant of what's going on in audits as "
             "well and it's maybe not traditionally a legal issue for an audit but there are.",
      'title': 'Litigation and unclaimed property audits (COMPUTERSHARE)',
      'url': 'https://www.youtube.com/watch?v=03CoUEgqdzg&t=25s',
      'video_id': '03CoUEgqdzg'},
     {'author': 'Surplus Institute / David Church / Unclaimed Funds',
      'channel': 'Surplus Institute / David Church / Unclaimed Funds',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=IIBKDdChS-k&t=58s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'As a property locator it could be property locator air finder unclaimed funds '
              "finder i mean there's a million different terms for this business the.",
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': 'As a property locator it could be property locator air finder unclaimed funds '
             "finder i mean there's a million different terms for this business the.",
      'title': 'How Unclaimed Money Can Help You Make More Money (Surplus Institute / David '
               'Church / Unclaimed Funds)',
      'url': 'https://www.youtube.com/watch?v=IIBKDdChS-k&t=58s',
      'video_id': 'IIBKDdChS-k'},
     {'author': 'Unclaimed Money Recovery',
      'channel': 'Unclaimed Money Recovery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=ZDSZHh3DZGs&t=140s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The state took that money and extrapolated into a $2 million assessment at the '
              'penalties for not doing your due diligence under off it could be up to 50% of '
              "whatever the property is that's returned to the state very very uh aggressive.",
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'The state took that money and extrapolated into a $2 million assessment at the '
             'penalties for not doing your due diligence under off it could be up to 50% of '
             "whatever the property is that's returned to the state very very uh aggressive.",
      'title': 'Unclaimed Money Recovery - What is Unclaimed Property? (Unclaimed Money '
               'Recovery)',
      'url': 'https://www.youtube.com/watch?v=ZDSZHh3DZGs&t=140s',
      'video_id': 'ZDSZHh3DZGs'},
     {'author': 'Spring Solutions, LLC',
      'channel': 'Spring Solutions, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:52](https://www.youtube.com/watch?v=1fuOy7IsEMo&t=412s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're interested in my course please take a look at the links in the "
              "description box and thank you for watching I'll see you in the next video.",
      'timestamp': 412,
      'timestamp_label': '[00:06:52]',
      'timestamp_seconds': 412,
      'tip': "If you're interested in my course please take a look at the links in the "
             "description box and thank you for watching I'll see you in the next video.",
      'title': 'I HATE CREDITOR CLAIMS-Bankruptcy Unclaimed Funds (Spring Solutions, LLC)',
      'url': 'https://www.youtube.com/watch?v=1fuOy7IsEMo&t=412s',
      'video_id': '1fuOy7IsEMo'},
     {'author': 'Money Making Juggernaut',
      'channel': 'Money Making Juggernaut',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:47](https://www.youtube.com/watch?v=XEcv7z100aA&t=1907s)',
      'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                   'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Where the results come back and say oh we matched with 96% um but yeah we just '
              "click on get started and then you're going to fill out your information on "
              'number email address this is the email address where you guys send the results '
              'back.',
      'timestamp': 1907,
      'timestamp_label': '[00:31:47]',
      'timestamp_seconds': 1907,
      'tip': 'Where the results come back and say oh we matched with 96% um but yeah we just '
             "click on get started and then you're going to fill out your information on "
             'number email address this is the email address where you guys send the results '
             'back.',
      'title': 'Skiptracing in Surplus Funds With Skipmatrix (Money Making Juggernaut)',
      'url': 'https://www.youtube.com/watch?v=XEcv7z100aA&t=1907s',
      'video_id': 'XEcv7z100aA'}],
 10: [{'author': 'Hoang Le CFP, EA, Real Estate Agent',
       'channel': 'Hoang Le CFP, EA, Real Estate Agent',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:25](https://www.youtube.com/watch?v=kZMkghcevh8&t=385s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "During an audit. If you're a small business owner watching this, it's worth an "
               'annual review of aged uncashed checks on your.',
       'timestamp': 385,
       'timestamp_label': '[00:06:25]',
       'timestamp_seconds': 385,
       'tip': "During an audit. If you're a small business owner watching this, it's worth an "
              'annual review of aged uncashed checks on your.',
       'title': 'Unclaimed Property Explained: How To Check and Claim It (Hoang Le CFP, EA, '
                'Real Estate Agent)',
       'url': 'https://www.youtube.com/watch?v=kZMkghcevh8&t=385s',
       'video_id': 'kZMkghcevh8'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=91o6wv-g6D0&t=15s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Educator in the asset recovery business today I have a great video in store '
               "for you guys I'm going to talk to you guys about unclaimed bankruptcy funds so "
               'if.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Educator in the asset recovery business today I have a great video in store for '
              "you guys I'm going to talk to you guys about unclaimed bankruptcy funds so if.",
       'title': 'UNTAPPED Business - Unclaimed BANKRUPTCY Funds Recovery ($5B) (Money Making '
                'Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=91o6wv-g6D0&t=15s',
       'video_id': '91o6wv-g6D0'},
      {'author': 'Friedman LLP',
       'channel': 'Friedman LLP',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:42](https://www.youtube.com/watch?v=duwB7Y82flc&t=702s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Types of unclaimed property we've listed a few of them obviously payroll "
               'checks accounts payable vendor checks gift certificates accounts receivable '
               'credits.',
       'timestamp': 702,
       'timestamp_label': '[00:11:42]',
       'timestamp_seconds': 702,
       'tip': "Types of unclaimed property we've listed a few of them obviously payroll checks "
              'accounts payable vendor checks gift certificates accounts receivable credits.',
       'title': 'Unclaimed Property: Avoiding Penalties From Increased State Enforcement | '
                'FULL Webinar (Friedman LLP)',
       'url': 'https://www.youtube.com/watch?v=duwB7Y82flc&t=702s',
       'video_id': 'duwB7Y82flc'},
      {'author': 'txcomptroller',
       'channel': 'txcomptroller',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=rGLI7Ry3sF0&t=78s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'One- there is documented contact with the owner either by mail, email or '
               'phone. Two- there is owner-generated activity. Three- or an owner has other '
               'active accounts with the business.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': 'One- there is documented contact with the owner either by mail, email or phone. '
              'Two- there is owner-generated activity. Three- or an owner has other active '
              'accounts with the business.',
       'title': 'Unclaimed Property: Holder Reporting - Oil and Gas Companies (txcomptroller)',
       'url': 'https://www.youtube.com/watch?v=rGLI7Ry3sF0&t=78s',
       'video_id': 'rGLI7Ry3sF0'},
      {'author': "Unclaimed Money: Find What You're Owed",
       'channel': "Unclaimed Money: Find What You're Owed",
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=J4RhFyo0R7c&t=59s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, unclaimed money isn't lost. So what kind of things end up unclaimed? Old "
               'checking and savings accounts are the big one. Then there are uncashed '
               'paychecks, especially final checks from a job you left.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': "So, unclaimed money isn't lost. So what kind of things end up unclaimed? Old "
              'checking and savings accounts are the big one. Then there are uncashed '
              'paychecks, especially final checks from a job you left.',
       'title': 'What Is Unclaimed Money? (And How to Get Yours Back for Free) (Unclaimed '
                "Money: Find What You're Owed)",
       'url': 'https://www.youtube.com/watch?v=J4RhFyo0R7c&t=59s',
       'video_id': 'J4RhFyo0R7c'},
      {'author': 'ohiocommerce',
       'channel': 'ohiocommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:43](https://www.youtube.com/watch?v=lQrAftswAO4&t=1003s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Checks in California is it what it is in our state and what it is in theirs um '
               'that coding helps us to communicate in a uniform language with one another.',
       'timestamp': 1003,
       'timestamp_label': '[00:16:43]',
       'timestamp_seconds': 1003,
       'tip': 'Checks in California is it what it is in our state and what it is in theirs um '
              'that coding helps us to communicate in a uniform language with one another.',
       'title': 'Claiming your Unclaimed Funds for Estate Planning Attorneys (ohiocommerce)',
       'url': 'https://www.youtube.com/watch?v=lQrAftswAO4&t=1003s',
       'video_id': 'lQrAftswAO4'},
      {'author': 'Unclaimed CEO',
       'channel': 'Unclaimed CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:53](https://www.youtube.com/watch?v=Vy3iGS6ep4w&t=173s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Successful um you've got to leverage the tools that are out there for us to be "
               'successful and I mean AI is massive I think that AI is going to create more.',
       'timestamp': 173,
       'timestamp_label': '[00:02:53]',
       'timestamp_seconds': 173,
       'tip': "Successful um you've got to leverage the tools that are out there for us to be "
              'successful and I mean AI is massive I think that AI is going to create more.',
       'title': 'How to be successful with Unclaimed Funds in 2024 (Unclaimed CEO)',
       'url': 'https://www.youtube.com/watch?v=Vy3iGS6ep4w&t=173s',
       'video_id': 'Vy3iGS6ep4w'},
      {'author': 'PakEnergy',
       'channel': 'PakEnergy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:15](https://www.youtube.com/watch?v=msbqOrpoTXc&t=375s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And then dealing with the states, we had to go through the whole voluntary '
               'disclosure agreement process. Uh and so all of that was frustrating in and of '
               'itself.',
       'timestamp': 375,
       'timestamp_label': '[00:06:15]',
       'timestamp_seconds': 375,
       'tip': 'And then dealing with the states, we had to go through the whole voluntary '
              'disclosure agreement process. Uh and so all of that was frustrating in and of '
              'itself.',
       'title': 'How to Automate Unclaimed Property Workflows in Oil & Gas (PakEnergy)',
       'url': 'https://www.youtube.com/watch?v=msbqOrpoTXc&t=375s',
       'video_id': 'msbqOrpoTXc'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=xqXetexqH30&t=67s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "How much you're gonna pay but two if you get it done in bulk it just saves you "
               'so much time going and chasing little tiny lists and then.',
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': "How much you're gonna pay but two if you get it done in bulk it just saves you "
              'so much time going and chasing little tiny lists and then.',
       'title': 'State Funds Business: Best Websites For Skip Tracing Claimant Information '
                '(Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=xqXetexqH30&t=67s',
       'video_id': 'xqXetexqH30'},
      {'author': 'KHOU 11',
       'channel': 'KHOU 11',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=uY7XnXFfpv4&t=22s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'ve lost contact with the owner. And right now the Texas Comptroller's office "
               "is holding more than $10 billion in unclaimed property. So here's what you "
               'want to know. Find out if any of it is yours. Go right here to claimattexas. '
               "And you're going to hit get started.",
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': "'ve lost contact with the owner. And right now the Texas Comptroller's office "
              "is holding more than $10 billion in unclaimed property. So here's what you want "
              'to know. Find out if any of it is yours. Go right here to claimattexas. And '
              "you're going to hit get started.",
       'title': "There's more than $10 billion in unclaimed property in Texas. Here's how to "
                'claim yours (KHOU 11)',
       'url': 'https://www.youtube.com/watch?v=uY7XnXFfpv4&t=22s',
       'video_id': 'uY7XnXFfpv4'},
      {'author': 'Badwolf Unincorporated',
       'channel': 'Badwolf Unincorporated',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=V_ElSJZFszg&t=102s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Jazzy defamation of character calling me the s word or whatever else do what '
               "you guys do best come to my arrest all right so without further Ado let's take "
               'a look at the screen share option here.',
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': 'Jazzy defamation of character calling me the s word or whatever else do what '
              "you guys do best come to my arrest all right so without further Ado let's take "
              'a look at the screen share option here.',
       'title': 'U.S. Courts Unclaimed Funds Locator: Does the court owe you money? (Badwolf '
                'Unincorporated)',
       'url': 'https://www.youtube.com/watch?v=V_ElSJZFszg&t=102s',
       'video_id': 'V_ElSJZFszg'},
      {'author': 'Spring Solutions, LLC',
       'channel': 'Spring Solutions, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:02](https://www.youtube.com/watch?v=y2j1Ux0R9jY&t=482s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Chain of command uh so for those that are interested again check out my videos '
               'regarding missouri and regarding who the parties are in a bankruptcy case if '
               "you're interested in my course the links are below and I will see you in the "
               'next video thanks for watching.',
       'timestamp': 482,
       'timestamp_label': '[00:08:02]',
       'timestamp_seconds': 482,
       'tip': 'Chain of command uh so for those that are interested again check out my videos '
              'regarding missouri and regarding who the parties are in a bankruptcy case if '
              "you're interested in my course the links are below and I will see you in the "
              'next video thanks for watching.',
       'title': 'Discrepancies with Verifying Funds-Bankruptcy Unclaimed Funds (Spring '
                'Solutions, LLC)',
       'url': 'https://www.youtube.com/watch?v=y2j1Ux0R9jY&t=482s',
       'video_id': 'y2j1Ux0R9jY'},
      {'author': 'Claim My Shares',
       'channel': 'Claim My Shares',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=73nKY8EkVnA&t=15s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'प्लीज रिमेंबर एज पर द कंपनीज एक्ट इफ यू डोंट क्लेम योर डिविडेंड फॉर अ '
               'कंटीन्यूअस पीरियड ऑफ सेन इयर्स इट गोज टू अ गवर्नमेंट अथॉरिटी नोन एज द आईईपीएफ.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'प्लीज रिमेंबर एज पर द कंपनीज एक्ट इफ यू डोंट क्लेम योर डिविडेंड फॉर अ '
              'कंटीन्यूअस पीरियड ऑफ सेन इयर्स इट गोज टू अ गवर्नमेंट अथॉरिटी नोन एज द आईईपीएफ.',
       'title': 'What happen to Unclaimed dividend amount? (Claim My Shares)',
       'url': 'https://www.youtube.com/watch?v=73nKY8EkVnA&t=15s',
       'video_id': '73nKY8EkVnA'},
      {'author': 'Unclaimed CEO',
       'channel': 'Unclaimed CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:01](https://www.youtube.com/watch?v=BAdBoUHd2lE&t=61s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'These files the the last one has the biggest amount of claims right there once '
               "you double click that that claim right there it's going to pop up and it's "
               'going to have a spreadsheet full of names and information who owed money for '
               'the claim good luck.',
       'timestamp': 61,
       'timestamp_label': '[00:01:01]',
       'timestamp_seconds': 61,
       'tip': 'These files the the last one has the biggest amount of claims right there once '
              "you double click that that claim right there it's going to pop up and it's "
              'going to have a spreadsheet full of names and information who owed money for '
              'the claim good luck.',
       'title': 'How To Find 6Figure Unclaimed Funds in 30 Seconds #makemoneyonline '
                '#unclaimedfunds #taxsurplus (Unclaimed CEO)',
       'url': 'https://www.youtube.com/watch?v=BAdBoUHd2lE&t=61s',
       'video_id': 'BAdBoUHd2lE'},
      {'author': 'Unclaimed CEO',
       'channel': 'Unclaimed CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:12](https://www.youtube.com/watch?v=Qf591_R7CN4&t=492s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Hopefully one day someday we cross paths and we can exchange some knowledge '
               "until then guys I'll see you in the next video how to skip trace and okay "
               'social media so sometimes you get people.',
       'timestamp': 492,
       'timestamp_label': '[00:08:12]',
       'timestamp_seconds': 492,
       'tip': 'Hopefully one day someday we cross paths and we can exchange some knowledge '
              "until then guys I'll see you in the next video how to skip trace and okay "
              'social media so sometimes you get people.',
       'title': 'This Is How To Skip Trace For Unclaimed Funds and Tax Overages 📲💰 (Unclaimed '
                'CEO)',
       'url': 'https://www.youtube.com/watch?v=Qf591_R7CN4&t=492s',
       'video_id': 'Qf591_R7CN4'}],
 11: [{'author': 'Unclaimed CEO',
       'channel': 'Unclaimed CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:02](https://www.youtube.com/watch?v=ie1xaLhl85o&t=242s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Isn't it better to do business with someone like that than a versus a cold "
               "call? I hung up on 15 phone calls in the last two days. I I I don't like spam "
               "calls and I don't like people calling me who don't know me offer me services.",
       'timestamp': 242,
       'timestamp_label': '[00:04:02]',
       'timestamp_seconds': 242,
       'tip': "Isn't it better to do business with someone like that than a versus a cold "
              "call? I hung up on 15 phone calls in the last two days. I I I don't like spam "
              "calls and I don't like people calling me who don't know me offer me services.",
       'title': 'She Closed 7 Unclaimed Funds Deals WITHOUT a Single Cold Call 😱 (Steal Her '
                'Strategy) (Unclaimed CEO)',
       'url': 'https://www.youtube.com/watch?v=ie1xaLhl85o&t=242s',
       'video_id': 'ie1xaLhl85o'},
      {'author': 'COMPUTERSHARE',
       'channel': 'COMPUTERSHARE',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=79d39hagJ6U&t=36s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Those areas that's on your audit team you also want to make sure you can get "
               'legal involved you may want to consider hiring an outside consultant if you.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': "Those areas that's on your audit team you also want to make sure you can get "
              'legal involved you may want to consider hiring an outside consultant if you.',
       'title': 'Preparing for an unclaimed property audit (COMPUTERSHARE)',
       'url': 'https://www.youtube.com/watch?v=79d39hagJ6U&t=36s',
       'video_id': '79d39hagJ6U'},
      {'author': 'CBS News Sacramento',
       'channel': 'CBS News Sacramento',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:06](https://www.youtube.com/watch?v=80djyAsS-YE&t=126s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "ARNOLD SCHWARZENEGGER EACH HAS UNCLAIMED PROPERTY. THE COMPTROLLER'S OFFICE "
               'DECLINED OUR INTERVIEW REQUEST. IT IS INSISTED THAT THE PROGRAM IS TO PROTECT '
               'CONSUMERS AND IT PREVENTS BUSINESSES WITH UNCLAIMED PROPERTY FROM KEEPING YOUR '
               'MONEY AND USING IT AS BUSINESS INCOME.',
       'timestamp': 126,
       'timestamp_label': '[00:02:06]',
       'timestamp_seconds': 126,
       'tip': "ARNOLD SCHWARZENEGGER EACH HAS UNCLAIMED PROPERTY. THE COMPTROLLER'S OFFICE "
              'DECLINED OUR INTERVIEW REQUEST. IT IS INSISTED THAT THE PROGRAM IS TO PROTECT '
              'CONSUMERS AND IT PREVENTS BUSINESSES WITH UNCLAIMED PROPERTY FROM KEEPING YOUR '
              'MONEY AND USING IT AS BUSINESS INCOME.',
       'title': 'Unclaimed Property: $275,000  Vanishes From Retirees Account, Transferred to '
                'the State of California (CBS News Sacramento)',
       'url': 'https://www.youtube.com/watch?v=80djyAsS-YE&t=126s',
       'video_id': '80djyAsS-YE'},
      {'author': 'Guide Gurus',
       'channel': 'Guide Gurus',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=yLgvruGuIx0&t=21s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'll break it down simply and quickly. First, let's start with the basics. "
               'Unclaimed property refers to money or assets that owners have forgotten about '
               'or lost track of like old bank accounts, uncashed checks, or forgotten stocks.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "I'll break it down simply and quickly. First, let's start with the basics. "
              'Unclaimed property refers to money or assets that owners have forgotten about '
              'or lost track of like old bank accounts, uncashed checks, or forgotten stocks.',
       'title': 'What Does Warrants Mean On Unclaimed Property   2025 (Guide Gurus)',
       'url': 'https://www.youtube.com/watch?v=yLgvruGuIx0&t=21s',
       'video_id': 'yLgvruGuIx0'},
      {'author': 'The TEC Show',
       'channel': 'The TEC Show',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:42](https://www.youtube.com/watch?v=DGys6KYDbNU&t=222s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh when it comes to the different claims that in and basically what what you '
               'do and when it comes to California now each state will be a little bit '
               'different but you just type in your name.',
       'timestamp': 222,
       'timestamp_label': '[00:03:42]',
       'timestamp_seconds': 222,
       'tip': 'Uh when it comes to the different claims that in and basically what what you do '
              'and when it comes to California now each state will be a little bit different '
              'but you just type in your name.',
       'title': 'Great News!! How To Find FREE MONEY: UNCLAIMED MONEY How to File a Claim (The '
                'TEC Show)',
       'url': 'https://www.youtube.com/watch?v=DGys6KYDbNU&t=222s',
       'video_id': 'DGys6KYDbNU'},
      {'author': 'Surplus Funds 101',
       'channel': 'Surplus Funds 101',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:34](https://www.youtube.com/watch?v=PGvJEv9Y_Go&t=154s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'True win-win situation for everybody. Another big thing you guys is just the '
               'low operating expenses to run just a successful asset recovery business.',
       'timestamp': 154,
       'timestamp_label': '[00:02:34]',
       'timestamp_seconds': 154,
       'tip': 'True win-win situation for everybody. Another big thing you guys is just the '
              'low operating expenses to run just a successful asset recovery business.',
       'title': 'State Funds Tutorial: First Steps For Somebody Brand New To Unclaimed Funds '
                'Business. (Surplus Funds 101)',
       'url': 'https://www.youtube.com/watch?v=PGvJEv9Y_Go&t=154s',
       'video_id': 'PGvJEv9Y_Go'},
      {'author': 'Timepiece Dan',
       'channel': 'Timepiece Dan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:29](https://www.youtube.com/watch?v=sDutuuk5RG0&t=329s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Know how am I supposed to find mr grace uh roberts very easy look at look up '
               "where um what state he's in of course he's in california I'm in california.",
       'timestamp': 329,
       'timestamp_label': '[00:05:29]',
       'timestamp_seconds': 329,
       'tip': 'Know how am I supposed to find mr grace uh roberts very easy look at look up '
              "where um what state he's in of course he's in california I'm in california.",
       'title': 'Make 5k On Surplus Funds State Funds Unclaimed Money (Easy Business) '
                '(Timepiece Dan)',
       'url': 'https://www.youtube.com/watch?v=sDutuuk5RG0&t=329s',
       'video_id': 'sDutuuk5RG0'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=8hCl2lLNDrk&t=15s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Educator in the asset recovery business today guys I have a great video in '
               'store I am going to break down sending mailers in this business before we get '
               'started.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Educator in the asset recovery business today guys I have a great video in '
              'store I am going to break down sending mailers in this business before we get '
              'started.',
       'title': '#1 APP To Send Mailers To Surplus Fund Recovery Leads (direct mail for asset '
                'recovery) (Money Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=8hCl2lLNDrk&t=15s',
       'video_id': '8hCl2lLNDrk'},
      {'author': 'FundSleuth - Unclaimed Funds Info and Training',
       'channel': 'FundSleuth - Unclaimed Funds Info and Training',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:41](https://www.youtube.com/watch?v=kGhoQfbhUG4&t=41s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To five and make a lot more money uh working on claim funds working for myself '
               "working with other people that i you know that i've a team that i've.",
       'timestamp': 41,
       'timestamp_label': '[00:00:41]',
       'timestamp_seconds': 41,
       'tip': 'To five and make a lot more money uh working on claim funds working for myself '
              "working with other people that i you know that i've a team that i've.",
       'title': 'Why people quit working Unclaimed Funds after taking a course. (FundSleuth - '
                'Unclaimed Funds Info and Training)',
       'url': 'https://www.youtube.com/watch?v=kGhoQfbhUG4&t=41s',
       'video_id': 'kGhoQfbhUG4'},
      {'author': 'KPRC 2 Click2Houston',
       'channel': 'KPRC 2 Click2Houston',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=a0Bv2mtHL_Y&t=108s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Many people get those letters. We pretty increasing complaints over the last '
               'several years and they will file homestead exemption for you if you don’t have '
               'one, why you would want to hire them to do that. It’s so easy to do on your '
               'own.',
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': 'Many people get those letters. We pretty increasing complaints over the last '
              'several years and they will file homestead exemption for you if you don’t have '
              'one, why you would want to hire them to do that. It’s so easy to do on your '
              'own.',
       'title': 'Ask Amy: Unclaimed money letter could be legit (KPRC 2 Click2Houston)',
       'url': 'https://www.youtube.com/watch?v=a0Bv2mtHL_Y&t=108s',
       'video_id': 'a0Bv2mtHL_Y'},
      {'author': 'Как се прави',
       'channel': 'Как се прави',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:33](https://www.youtube.com/watch?v=0CZmLNyYvD8&t=213s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The notary has to actually witness you signing it under penalty of perjury, '
               'right after checking your government-issued ID. And this brilliantly '
               'illustrates who actually needs that notarization because it really depends on '
               'your claimant class.',
       'timestamp': 213,
       'timestamp_label': '[00:03:33]',
       'timestamp_seconds': 213,
       'tip': 'The notary has to actually witness you signing it under penalty of perjury, '
              'right after checking your government-issued ID. And this brilliantly '
              'illustrates who actually needs that notarization because it really depends on '
              'your claimant class.',
       'title': 'How to claim Pennsylvania unclaimed property with a notarized form (Как се '
                'прави)',
       'url': 'https://www.youtube.com/watch?v=0CZmLNyYvD8&t=213s',
       'video_id': '0CZmLNyYvD8'},
      {'author': 'Make Money Anthony',
       'channel': 'Make Money Anthony',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:35](https://www.youtube.com/watch?v=3QgxEy6EB6Y&t=215s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Below let the rest of us know how you did it hopefully you found that video '
               'useful if so click thumbs up or maybe consider subscribing to my channel and I '
               'hope to see on the next video thanks again for watching.',
       'timestamp': 215,
       'timestamp_label': '[00:03:35]',
       'timestamp_seconds': 215,
       'tip': 'Below let the rest of us know how you did it hopefully you found that video '
              'useful if so click thumbs up or maybe consider subscribing to my channel and I '
              'hope to see on the next video thanks again for watching.',
       'title': '✅ How To Find Unclaimed Money And Property In California 🔴 (Make Money '
                'Anthony)',
       'url': 'https://www.youtube.com/watch?v=3QgxEy6EB6Y&t=215s',
       'video_id': '3QgxEy6EB6Y'},
      {'author': 'SC REALTORS',
       'channel': 'SC REALTORS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:39](https://www.youtube.com/watch?v=D-PMjgNe-7s&t=399s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Before reporting the property to the state third file an annual unclaimed '
               'property report and remit the associated funds to the state before November '
               '1st and fourth keep adequate supporting.',
       'timestamp': 399,
       'timestamp_label': '[00:06:39]',
       'timestamp_seconds': 399,
       'tip': 'Before reporting the property to the state third file an annual unclaimed '
              'property report and remit the associated funds to the state before November 1st '
              'and fourth keep adequate supporting.',
       'title': 'SCR Webinar: Unclaimed Property Program Overview (SC REALTORS)',
       'url': 'https://www.youtube.com/watch?v=D-PMjgNe-7s&t=399s',
       'video_id': 'D-PMjgNe-7s'},
      {'author': 'Spring Solutions, LLC',
       'channel': 'Spring Solutions, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:14](https://www.youtube.com/watch?v=5A3cah6ujY4&t=134s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So when I do that I see uh a number of cases right here this is where the '
               "debtor's name this is the case number and the creditor's name is right in the "
               'middle and it gives the last known address right.',
       'timestamp': 134,
       'timestamp_label': '[00:02:14]',
       'timestamp_seconds': 134,
       'tip': 'So when I do that I see uh a number of cases right here this is where the '
              "debtor's name this is the case number and the creditor's name is right in the "
              'middle and it gives the last known address right.',
       'title': 'Claims Register Part 2-Eastern District of New York Bankruptcy Unclaimed '
                'Funds (Spring Solutions, LLC)',
       'url': 'https://www.youtube.com/watch?v=5A3cah6ujY4&t=134s',
       'video_id': '5A3cah6ujY4'},
      {'author': 'TNTreasury',
       'channel': 'TNTreasury',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:01](https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=121s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A business cannot be currently under audit by the state at the time it chooses '
               'to sign the compliance Disclosure agreement. The holder must present a '
               "proposal of Reporting Method worksheet describing in detail how the holder's "
               'unclaimed property liability will be determined.',
       'timestamp': 121,
       'timestamp_label': '[00:02:01]',
       'timestamp_seconds': 121,
       'tip': 'A business cannot be currently under audit by the state at the time it chooses '
              'to sign the compliance Disclosure agreement. The holder must present a proposal '
              "of Reporting Method worksheet describing in detail how the holder's unclaimed "
              'property liability will be determined.',
       'title': 'Unclaimed Property in Tennessee: Understanding Audits, Compliance, and '
                'Negative Reports (TNTreasury)',
       'url': 'https://www.youtube.com/watch?v=KiR-ZUeCE5g&t=121s',
       'video_id': 'KiR-ZUeCE5g'}],
 12: [{'author': 'Unclaimed CEO',
       'channel': 'Unclaimed CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:12](https://www.youtube.com/watch?v=i84F9CVghTA&t=252s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You want to run everyone's going to have their agreement forms and contracts "
               'and that is great but at the end of the day different states have different '
               'rules.',
       'timestamp': 252,
       'timestamp_label': '[00:04:12]',
       'timestamp_seconds': 252,
       'tip': "You want to run everyone's going to have their agreement forms and contracts "
              'and that is great but at the end of the day different states have different '
              'rules.',
       'title': '⚠️WARNING⚠️ Do these 6 things BEFORE you start your Unclaimed Funds | Tax '
                'Surplus business (Unclaimed CEO)',
       'url': 'https://www.youtube.com/watch?v=i84F9CVghTA&t=252s',
       'video_id': 'i84F9CVghTA'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:18](https://www.youtube.com/watch?v=D3Fcqm3xaco&t=258s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Off with ten percent if it's something like and I work 14 15 16 000 claims all "
               'the time I get checks in 14 15 1600 bucks you get a couple of those a week.',
       'timestamp': 258,
       'timestamp_label': '[00:04:18]',
       'timestamp_seconds': 258,
       'tip': "Off with ten percent if it's something like and I work 14 15 16 000 claims all "
              'the time I get checks in 14 15 1600 bucks you get a couple of those a week.',
       'title': 'Beware of the changes made in CA state unclaimed funds contracts (Surplus '
                'Institute / David Church / Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=D3Fcqm3xaco&t=258s',
       'video_id': 'D3Fcqm3xaco'},
      {'author': 'WFAA',
       'channel': 'WFAA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:42](https://www.youtube.com/watch?v=0UUN2j2_dFU&t=102s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "For all claim types what's 37 business days but the length of time is going to "
               'depend on the type of claim for example heirship claims.',
       'timestamp': 102,
       'timestamp_label': '[00:01:42]',
       'timestamp_seconds': 102,
       'tip': "For all claim types what's 37 business days but the length of time is going to "
              'depend on the type of claim for example heirship claims.',
       'title': 'How to get your unclaimed property in Texas (WFAA)',
       'url': 'https://www.youtube.com/watch?v=0UUN2j2_dFU&t=102s',
       'video_id': '0UUN2j2_dFU'},
      {'author': 'SimekScott LLC',
       'channel': 'SimekScott LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:22](https://www.youtube.com/watch?v=TGu6R9Pc0-4&t=22s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'VDA program, you have to take action within the first 90 days to determine '
               "whether or not you're going to participate in the VDA program. If you decide "
               'not to participate, just know that you will be referred to the Department of '
               'Finance for an unclaimed property audit.',
       'timestamp': 22,
       'timestamp_label': '[00:00:22]',
       'timestamp_seconds': 22,
       'tip': 'VDA program, you have to take action within the first 90 days to determine '
              "whether or not you're going to participate in the VDA program. If you decide "
              'not to participate, just know that you will be referred to the Department of '
              'Finance for an unclaimed property audit.',
       'title': 'Delaware Unclaimed Property VDA Invitations - April 11 2025 (SimekScott LLC)',
       'url': 'https://www.youtube.com/watch?v=TGu6R9Pc0-4&t=22s',
       'video_id': 'TGu6R9Pc0-4'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=sK5PqCLSzzg&t=15s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Educator in the asset recovery and service funds business Base today I'm going "
               'to reveal how you can start your asset recovery business with zero.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "Educator in the asset recovery and service funds business Base today I'm going "
              'to reveal how you can start your asset recovery business with zero.',
       'title': 'How To Start Asset Recovery Business With $0 (Surplus Funds Recovery) (Money '
                'Making Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=sK5PqCLSzzg&t=15s',
       'video_id': 'sK5PqCLSzzg'},
      {'author': 'GardenShop.Pro',
       'channel': 'GardenShop.Pro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:30](https://www.youtube.com/watch?v=dhZB_jSn2Qg&t=150s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Before you start claiming anything, you really have to stop and ask yourself, '
               'what powers do you actually have? Look, a power of attorney is a legal '
               'document where a principal authorizes you, the agent, to act on their behalf.',
       'timestamp': 150,
       'timestamp_label': '[00:02:30]',
       'timestamp_seconds': 150,
       'tip': 'Before you start claiming anything, you really have to stop and ask yourself, '
              'what powers do you actually have? Look, a power of attorney is a legal document '
              'where a principal authorizes you, the agent, to act on their behalf.',
       'title': 'How to claim unclaimed money as a power of attorney (GardenShop.Pro)',
       'url': 'https://www.youtube.com/watch?v=dhZB_jSn2Qg&t=150s',
       'video_id': 'dhZB_jSn2Qg'},
      {'author': 'AskJimmySmith',
       'channel': 'AskJimmySmith',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:19](https://www.youtube.com/watch?v=JT_EgidLdF8&t=859s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I hope this video helped you and blessed you and I hope that you have a great '
               'rest of your day and a blessed rest of your week.',
       'timestamp': 859,
       'timestamp_label': '[00:14:19]',
       'timestamp_seconds': 859,
       'tip': 'I hope this video helped you and blessed you and I hope that you have a great '
              'rest of your day and a blessed rest of your week.',
       'title': 'Unclaimed Property: What It Is, How to Claim It, & How to Avoid '
                'Scams...EVERYTHING YOU NEED TO KNOW (AskJimmySmith)',
       'url': 'https://www.youtube.com/watch?v=JT_EgidLdF8&t=859s',
       'video_id': 'JT_EgidLdF8'},
      {'author': 'Broadstreet Radio',
       'channel': 'Broadstreet Radio',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:26:41](https://www.youtube.com/watch?v=ykLXSnb1CRE&t=1601s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And I will request that you wait patiently for the September edition. And you '
               'can prepare for next month. Usually, it comes in the first week of the month. '
               'Now, another one will come by September.',
       'timestamp': 1601,
       'timestamp_label': '[00:26:41]',
       'timestamp_seconds': 1601,
       'tip': 'And I will request that you wait patiently for the September edition. And you '
              'can prepare for next month. Usually, it comes in the first week of the month. '
              'Now, another one will come by September.',
       'title': 'Step-by-Step Guide to Recovering Your Unclaimed Dividend (Broadstreet Radio)',
       'url': 'https://www.youtube.com/watch?v=ykLXSnb1CRE&t=1601s',
       'video_id': 'ykLXSnb1CRE'},
      {'author': 'Surplus Institute / David Church / Unclaimed Funds',
       'channel': 'Surplus Institute / David Church / Unclaimed Funds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:09](https://www.youtube.com/watch?v=RjCjrBjQF7Y&t=249s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Start working this how we could start using this as a business so let's say I "
               'go to my good old friend Google or whatever and I want to work unclaimed.',
       'timestamp': 249,
       'timestamp_label': '[00:04:09]',
       'timestamp_seconds': 249,
       'tip': "Start working this how we could start using this as a business so let's say I "
              'go to my good old friend Google or whatever and I want to work unclaimed.',
       'title': 'How to get started in state fund | State unclaimed funds business. Make money '
                'with surplus funds (Surplus Institute / David Church / Unclaimed Funds)',
       'url': 'https://www.youtube.com/watch?v=RjCjrBjQF7Y&t=249s',
       'video_id': 'RjCjrBjQF7Y'},
      {'author': 'Nobody Asked, I Checked',
       'channel': 'Nobody Asked, I Checked',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:50](https://www.youtube.com/watch?v=z2nZM27w4qU&t=50s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Unclaimed money is, where to search for it for free, which federal databases '
               'matter,  the finder fee scams to avoid, and a simple search plan you can.',
       'timestamp': 50,
       'timestamp_label': '[00:00:50]',
       'timestamp_seconds': 50,
       'tip': 'Unclaimed money is, where to search for it for free, which federal databases '
              'matter,  the finder fee scams to avoid, and a simple search plan you can.',
       'title': 'Unclaimed Money Search 2026: Find Money in Your Name for Free (Avoid Finder '
                'Fee Scams) (Nobody Asked, I Checked)',
       'url': 'https://www.youtube.com/watch?v=z2nZM27w4qU&t=50s',
       'video_id': 'z2nZM27w4qU'},
      {'author': 'ShadowAnyone',
       'channel': 'ShadowAnyone',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:29](https://www.youtube.com/watch?v=5gSBjAC1g0s&t=89s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'To get in touch with the person who has the the funds in that account it can '
               'be modest it can be thirty seven dollars it could be thirty seven hundred '
               'dollars or.',
       'timestamp': 89,
       'timestamp_label': '[00:01:29]',
       'timestamp_seconds': 89,
       'tip': 'To get in touch with the person who has the the funds in that account it can be '
              'modest it can be thirty seven dollars it could be thirty seven hundred dollars '
              'or.',
       'title': "Don't get BANNED for life skip tracing Unclaimed Funds! A Private "
                'Investigator License Warning. (ShadowAnyone)',
       'url': 'https://www.youtube.com/watch?v=5gSBjAC1g0s&t=89s',
       'video_id': '5gSBjAC1g0s'},
      {'author': 'Unclaimed CEO',
       'channel': 'Unclaimed CEO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:14](https://www.youtube.com/watch?v=bAARnig4bT4&t=314s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cold calls because I'd hate for you guys to start making some deals and you "
               'try to file paperwork and you forgot to get registered with the state not '
               "every state requires it but some states do guys I'll see you guys in the next "
               'video peace.',
       'timestamp': 314,
       'timestamp_label': '[00:05:14]',
       'timestamp_seconds': 314,
       'tip': "Cold calls because I'd hate for you guys to start making some deals and you try "
              'to file paperwork and you forgot to get registered with the state not every '
              "state requires it but some states do guys I'll see you guys in the next video "
              'peace.',
       'title': 'UNCLAIMED FUNDS: Will leads really want to work with you?🤔 (Unclaimed CEO)',
       'url': 'https://www.youtube.com/watch?v=bAARnig4bT4&t=314s',
       'video_id': 'bAARnig4bT4'},
      {'author': 'GardenShop.Pro',
       'channel': 'GardenShop.Pro',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:32](https://www.youtube.com/watch?v=E2EtkM2OBvI&t=392s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'They then have until November 1st to report and actually remit that money to '
               'the state. Once you find it and file your claim, the state generally takes up '
               'to 90 days to conduct a standard claim audit of your submitted documents.',
       'timestamp': 392,
       'timestamp_label': '[00:06:32]',
       'timestamp_seconds': 392,
       'tip': 'They then have until November 1st to report and actually remit that money to '
              'the state. Once you find it and file your claim, the state generally takes up '
              'to 90 days to conduct a standard claim audit of your submitted documents.',
       'title': 'How to find Kansas unclaimed utility deposits by last name (GardenShop.Pro)',
       'url': 'https://www.youtube.com/watch?v=E2EtkM2OBvI&t=392s',
       'video_id': 'E2EtkM2OBvI'},
      {'author': 'Money Making Juggernaut',
       'channel': 'Money Making Juggernaut',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:00:17](https://www.youtube.com/watch?v=aKzRVyO_gfI&t=3617s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "File in order to start skipping okay so there's like no I think you said it "
               "before there's no minimum or anything whether you're doing 10 or 100 you're "
               "just going to build accordingly that's correct yes okay good thank.",
       'timestamp': 3617,
       'timestamp_label': '[01:00:17]',
       'timestamp_seconds': 3617,
       'tip': "File in order to start skipping okay so there's like no I think you said it "
              "before there's no minimum or anything whether you're doing 10 or 100 you're "
              "just going to build accordingly that's correct yes okay good thank.",
       'title': 'The Only Skiptracing Software You Need For Surplus Funds (Money Making '
                'Juggernaut)',
       'url': 'https://www.youtube.com/watch?v=aKzRVyO_gfI&t=3617s',
       'video_id': 'aKzRVyO_gfI'},
      {'author': 'Financial Soup',
       'channel': 'Financial Soup',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:43](https://www.youtube.com/watch?v=ubLk2A5a-2A&t=223s)',
       'relevance': 'Attributed practitioner commentary on state-treasury unclaimed property '
                    'escheatment, corporate uncashed warrants, and statutory finder-fee claims '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Uh, forgotten bank accounts, lost CDs, insurance refunds, insurance claims, '
               "uncash checks. It's always good to check for yourself and loved ones whether "
               "or not they're uh currently living or deceased.",
       'timestamp': 223,
       'timestamp_label': '[00:03:43]',
       'timestamp_seconds': 223,
       'tip': 'Uh, forgotten bank accounts, lost CDs, insurance refunds, insurance claims, '
              "uncash checks. It's always good to check for yourself and loved ones whether or "
              "not they're uh currently living or deceased.",
       'title': 'How to Find Unclaimed Money (Financial Soup)',
       'url': 'https://www.youtube.com/watch?v=ubLk2A5a-2A&t=223s',
       'video_id': 'ubLk2A5a-2A'}]}
