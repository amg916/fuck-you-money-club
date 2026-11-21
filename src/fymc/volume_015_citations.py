"""Curated 180-citation Judgment Recovery baseline (15 per chapter across Q1-Q12) mined strictly from verified Judgment Recovery YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'3001',
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'champerty',
     'civil',
     'claims',
     'client',
     'clients',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'counsel',
     'court',
     'debt',
     'debtor',
     'debtors',
     'discovery',
     'distressed',
     'docket',
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
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'budget',
     'building',
     'business',
     'buyer',
     'buying',
     'champerty',
     'civil',
     'claims',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'contract',
     'counsel',
     'court',
     'customer',
     'debt',
     'debtor',
     'debtors',
     'decision',
     'discovery',
     'distressed',
     'docket',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'3001',
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'cash',
     'cashflow',
     'champerty',
     'civil',
     'claims',
     'collectability',
     'collection',
     'commercial',
     'commission',
     'consumer',
     'contingency',
     'cost',
     'costs',
     'counsel',
     'court',
     'debt',
     'debtor',
     'debtors',
     'discovery',
     'distressed',
     'docket',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'3001',
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'budget',
     'building',
     'business',
     'buying',
     'capital',
     'champerty',
     'civil',
     'claims',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'counsel',
     'court',
     'debt',
     'debtor',
     'debtors',
     'discovery',
     'distressed',
     'docket',
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
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'audit',
     'avoid',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'champerty',
     'civil',
     'claims',
     'clawback',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'counsel',
     'court',
     'debt',
     'debtor',
     'debtors',
     'discovery',
     'dispute',
     'distressed',
     'docket',
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
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'champerty',
     'civil',
     'claims',
     'client',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'counsel',
     'court',
     'data',
     'deal',
     'debt',
     'debtor',
     'debtors',
     'discovery',
     'distressed',
     'docket',
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
     'abstract',
     'accounts',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'champerty',
     'checklist',
     'civil',
     'claims',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'counsel',
     'court',
     'debt',
     'debtor',
     'debtors',
     'delivery',
     'discovery',
     'distressed',
     'docket',
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
     'abstract',
     'accounts',
     'api',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'champerty',
     'civil',
     'claims',
     'collectability',
     'collection',
     'commercial',
     'consumer',
     'contingency',
     'counsel',
     'court',
     'crm',
     'data',
     'database',
     'debt',
     'debtor',
     'debtors',
     'discovery',
     'distressed',
     'docket',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'3001',
     'abstract',
     'accounts',
     'agreement',
     'asset',
     'assignee',
     'assignees',
     'assignment',
     'attorneys',
     'b2b',
     'bank',
     'bankruptcy',
     'building',
     'business',
     'buying',
     'champerty',
     'civil',
     'claims',
     'collectability',
     'collection',
     'commercial',
     'compliance',
     'consumer',
     'contingency',
     'contract',
     'counsel',
     'court',
     'debt',
     'debtor',
     'debtors',
     'disclosure',
     'discovery',
     'distressed',
     'docket',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'3001',
      'abstract',
      'accounts',
      'agent',
      'ai',
      'asset',
      'assignee',
      'assignees',
      'assignment',
      'attorneys',
      'automate',
      'automation',
      'b2b',
      'bank',
      'bankruptcy',
      'building',
      'business',
      'buying',
      'champerty',
      'civil',
      'claims',
      'collectability',
      'collection',
      'commercial',
      'consumer',
      'contingency',
      'counsel',
      'court',
      'dashboard',
      'debt',
      'debtor',
      'debtors',
      'discovery',
      'distressed',
      'docket',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'3001',
      'abstract',
      'accounts',
      'asset',
      'assignee',
      'assignees',
      'assignment',
      'attorneys',
      'b2b',
      'bank',
      'bankruptcy',
      'building',
      'business',
      'buying',
      'champerty',
      'civil',
      'claims',
      'collectability',
      'collection',
      'commercial',
      'consumer',
      'contingency',
      'contractor',
      'counsel',
      'court',
      'debt',
      'debtor',
      'debtors',
      'discovery',
      'distressed',
      'docket',
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
      'abstract',
      'accounts',
      'action',
      'asset',
      'assignee',
      'assignees',
      'assignment',
      'attorneys',
      'b2b',
      'bank',
      'bankruptcy',
      'building',
      'business',
      'buying',
      'champerty',
      'civil',
      'claims',
      'collectability',
      'collection',
      'commercial',
      'consumer',
      'contingency',
      'counsel',
      'court',
      'day',
      'days',
      'debt',
      'debtor',
      'debtors',
      'discovery',
      'distressed',
      'docket',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Thomas Higgins Limited',
      'channel': 'Thomas Higgins Limited',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=MxMjZqkhltA&t=33s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Commercial debt collection is the process of recovering unpaid invoices that a '
              'business known as the creditor is owed by another business, a local authority '
              "or a soul trader referred to as the debtor. So what's the difference between "
              'commercial and consumer debt?',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Commercial debt collection is the process of recovering unpaid invoices that a '
             'business known as the creditor is owed by another business, a local authority or '
             "a soul trader referred to as the debtor. So what's the difference between "
             'commercial and consumer debt?',
      'title': 'Thomas Higgins Limited - What Is the Process of Commercial Debt Collection? '
               '(Thomas Higgins Limited)',
      'url': 'https://www.youtube.com/watch?v=MxMjZqkhltA&t=33s',
      'video_id': 'MxMjZqkhltA'},
     {'author': 'FinanceKid',
      'channel': 'FinanceKid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:18](https://www.youtube.com/watch?v=9CYRQ14FrFw&t=1698s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rules that the firm was insolvent as defined by a negative at net asset value '
              'the right to claim loss carryforwards may be preserved also if a debtor.',
      'timestamp': 1698,
      'timestamp_label': '[00:28:18]',
      'timestamp_seconds': 1698,
      'tip': 'Rules that the firm was insolvent as defined by a negative at net asset value '
             'the right to claim loss carryforwards may be preserved also if a debtor.',
      'title': 'Restructuring Through Bankruptcy - Basics Of Corporate Bankruptcy (FinanceKid)',
      'url': 'https://www.youtube.com/watch?v=9CYRQ14FrFw&t=1698s',
      'video_id': '9CYRQ14FrFw'},
     {'author': 'Evanns Collection Law Firm',
      'channel': 'Evanns Collection Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=XOwPGudMeaY&t=123s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Solve that mystery and that's what we do here and that's what we specialize in "
              "he'll pass up on money he'll go through hoops he'll spend the firm's money if "
              "it means uh doing what's best for the client what I really like to do is make "
              'debtors.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "Solve that mystery and that's what we do here and that's what we specialize in "
             "he'll pass up on money he'll go through hoops he'll spend the firm's money if it "
             "means uh doing what's best for the client what I really like to do is make "
             'debtors.',
      'title': 'Judgment Enforcement | Evanns Collection Law Firm (Evanns Collection Law Firm)',
      'url': 'https://www.youtube.com/watch?v=XOwPGudMeaY&t=123s',
      'video_id': 'XOwPGudMeaY'},
     {'author': 'Franchise Brokers Association',
      'channel': 'Franchise Brokers Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=YqjXCyNkUZ8&t=87s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, and you're so much more than a debt collector. You're an asset "
              "investigator, and you could basically just go in there' and take the person's "
              "assets and take the person's stuff. So it's really an amazing business "
              'opportunity that we offer here.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "Um, and you're so much more than a debt collector. You're an asset investigator, "
             "and you could basically just go in there' and take the person's assets and take "
             "the person's stuff. So it's really an amazing business opportunity that we offer "
             'here.',
      'title': 'How to Make Money Collecting Unpaid Court Judgments: Honest Review (Franchise '
               'Brokers Association)',
      'url': 'https://www.youtube.com/watch?v=YqjXCyNkUZ8&t=87s',
      'video_id': 'YqjXCyNkUZ8'},
     {'author': 'County Portal Law',
      'channel': 'County Portal Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=Nl9nVJJo6Xs&t=40s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The sheriff delivers the writ to the debtor's bank. The bank must freeze the "
              "debtor's accounts immediately up to the amount of.",
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': "The sheriff delivers the writ to the debtor's bank. The bank must freeze the "
             "debtor's accounts immediately up to the amount of.",
      'title': 'What Happens After A Writ Of Execution? (County Portal Law)',
      'url': 'https://www.youtube.com/watch?v=Nl9nVJJo6Xs&t=40s',
      'video_id': 'Nl9nVJJo6Xs'},
     {'author': 'Florida Trust, Real Estate, Probate, & Foreclosure',
      'channel': 'Florida Trust, Real Estate, Probate, & Foreclosure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:33:52](https://www.youtube.com/watch?v=2xja5hdZ134&t=2032s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've groped through this record, even the docket sheet, there was no hearing. "
              'The settlement agreement was never before the court. Did your client uh approve '
              "the proposed order that was sent to the trial judge? We don't have a record of "
              'this, your honor.',
      'timestamp': 2032,
      'timestamp_label': '[00:33:52]',
      'timestamp_seconds': 2032,
      'tip': "I've groped through this record, even the docket sheet, there was no hearing. "
             'The settlement agreement was never before the court. Did your client uh approve '
             "the proposed order that was sent to the trial judge? We don't have a record of "
             'this, your honor.',
      'title': '💼 A Final Judgment With No Reserved Jurisdiction — Vacating It Under Rule '
               '1.540(b) (Florida Trust, Real Estate, Probate, & Foreclosure)',
      'url': 'https://www.youtube.com/watch?v=2xja5hdZ134&t=2032s',
      'video_id': '2xja5hdZ134'},
     {'author': 'Jacobs Berger, LLC',
      'channel': 'Jacobs Berger, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=rbjp5kojsQA&t=72s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The value of a house or bank account or brokerage account was incorrectly '
              'stated and all of the calculations flowing from that were incorrect the court '
              'can vacate.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'The value of a house or bank account or brokerage account was incorrectly stated '
             'and all of the calculations flowing from that were incorrect the court can '
             'vacate.',
      'title': 'Vacating a Consent Order or Settlement Agreement in New Jersey (Jacobs Berger, '
               'LLC)',
      'url': 'https://www.youtube.com/watch?v=rbjp5kojsQA&t=72s',
      'video_id': 'rbjp5kojsQA'},
     {'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=eA9c0DMpp60&t=20s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh this is the first of three episodes for advanced bankruptcy transactions. '
              'This episode is entitled Representing Asset Purchasers in Bankruptcy. Again, I '
              "am your moderator. I'm a partner with the firm of Getz Platner LLP.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Uh this is the first of three episodes for advanced bankruptcy transactions. '
             'This episode is entitled Representing Asset Purchasers in Bankruptcy. Again, I '
             "am your moderator. I'm a partner with the firm of Getz Platner LLP.",
      'title': 'Purchasing Assets in Bankruptcy (The National Law Review)',
      'url': 'https://www.youtube.com/watch?v=eA9c0DMpp60&t=20s',
      'video_id': 'eA9c0DMpp60'},
     {'author': 'Professor Stevenson',
      'channel': 'Professor Stevenson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:00](https://www.youtube.com/watch?v=kBmxVj9hiWo&t=300s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ongoing relationship with that you always use so for example when you have '
              'clients who have a matter before a federal agency you have a dc firm that you '
              "always use something like that okay let's go to the next rule for provision.",
      'timestamp': 300,
      'timestamp_label': '[00:05:00]',
      'timestamp_seconds': 300,
      'tip': 'Ongoing relationship with that you always use so for example when you have '
             'clients who have a matter before a federal agency you have a dc firm that you '
             "always use something like that okay let's go to the next rule for provision.",
      'title': 'Model Rule 5.5 pt.1 - Unauthorized Practice of Law (Professor Stevenson)',
      'url': 'https://www.youtube.com/watch?v=kBmxVj9hiWo&t=300s',
      'video_id': 'kBmxVj9hiWo'},
     {'author': 'Credit Commerce & Currency',
      'channel': 'Credit Commerce & Currency',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=TEEr5IdEtHY&t=251s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Qualifications of your firm and the specific lender certain collateral is '
              'subject to a UCC line leans under the Uniform Commercial Code can be placed by.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': 'Qualifications of your firm and the specific lender certain collateral is '
             'subject to a UCC line leans under the Uniform Commercial Code can be placed by.',
      'title': 'What Should I Do If a UCC Lien Has Been Filed Against My Business (Credit '
               'Commerce & Currency)',
      'url': 'https://www.youtube.com/watch?v=TEEr5IdEtHY&t=251s',
      'video_id': 'TEEr5IdEtHY'},
     {'author': 'KillDebt & ParkerGPT: The New Way To Law',
      'channel': 'KillDebt & ParkerGPT: The New Way To Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:32:44](https://www.youtube.com/watch?v=RwXTJhX-rxo&t=5564s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Something it's for this affidavit would be your clients Mr Ward student loan "
              "debt all right uh uh you're not saying that you're saying it's an account I'm "
              'say my brain this is this how I operate I apologize I know your brain maybe.',
      'timestamp': 5564,
      'timestamp_label': '[01:32:44]',
      'timestamp_seconds': 5564,
      'tip': "Something it's for this affidavit would be your clients Mr Ward student loan "
             "debt all right uh uh you're not saying that you're saying it's an account I'm "
             'say my brain this is this how I operate I apologize I know your brain maybe.',
      'title': 'How To Take a Deposition of a Collection Attorney in a Debt Collection Case - '
               'Part 1 (KillDebt & ParkerGPT: The New Way To Law)',
      'url': 'https://www.youtube.com/watch?v=RwXTJhX-rxo&t=5564s',
      'video_id': 'RwXTJhX-rxo'},
     {'author': 'North Texas Paralegal Institute',
      'channel': 'North Texas Paralegal Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=nFhwr1E6-NE&t=38s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '03 makes the supervising lawyer responsible for your conduct. Three tasks stay '
              'with the lawyer. You do not tell a prospect the firm has taken the case, and '
              'you do not sign the representation agreement. You do not quote a contingency '
              'percentage, an hourly rate, or a discount.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': '03 makes the supervising lawyer responsible for your conduct. Three tasks stay '
             'with the lawyer. You do not tell a prospect the firm has taken the case, and you '
             'do not sign the representation agreement. You do not quote a contingency '
             'percentage, an hourly rate, or a discount.',
      'title': 'Favor or UPL? Unauthorized Practice & Paralegal Supervision in Texas | Free '
               'NTPI Lesson (North Texas Paralegal Institute)',
      'url': 'https://www.youtube.com/watch?v=nFhwr1E6-NE&t=38s',
      'video_id': 'nFhwr1E6-NE'},
     {'author': 'Pankauski Lazarus P.L.L.C.',
      'channel': 'Pankauski Lazarus P.L.L.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=GU3ZAAqrvR8&t=260s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trust litigation or any civil litigation involving offers of judgment or '
              "proposals for settlement my name is john from kowski I'm an estate litigation "
              'attorney with the pink house key law firm ww kowski law firm calm in west palm '
              'beach thank you for listening.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Trust litigation or any civil litigation involving offers of judgment or '
             "proposals for settlement my name is john from kowski I'm an estate litigation "
             'attorney with the pink house key law firm ww kowski law firm calm in west palm '
             'beach thank you for listening.',
      'title': 'Florida Estate Litigation Proposals of Settlement & Offers of Judgment '
               '(Pankauski Lazarus P.L.L.C.)',
      'url': 'https://www.youtube.com/watch?v=GU3ZAAqrvR8&t=260s',
      'video_id': 'GU3ZAAqrvR8'},
     {'author': 'Dylan Raquel Real Estate',
      'channel': 'Dylan Raquel Real Estate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=7NXn3JN88l8&t=284s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In over 300 transactions and I would love to be of service to you if I can in '
              'any way I hope you found this helpful and I hope you will pass it on to other '
              'Realtors that you think might benefit from it as well thanks for watching.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'In over 300 transactions and I would love to be of service to you if I can in '
             'any way I hope you found this helpful and I hope you will pass it on to other '
             'Realtors that you think might benefit from it as well thanks for watching.',
      'title': 'How to remove a judgment or lien from a Preliminary Title Report - Be a Better '
               'Realtor (Dylan Raquel Real Estate)',
      'url': 'https://www.youtube.com/watch?v=7NXn3JN88l8&t=284s',
      'video_id': '7NXn3JN88l8'},
     {'author': 'Mr. Grey Judgment Enforcement',
      'channel': 'Mr. Grey Judgment Enforcement',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=09e6Gzw3S0U&t=33s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Other stuff I'm doing but I will help you because I feel for you but I can't do "
              'it for a 50 50 split because he wanted a 50 50 split I said waters just give me '
              "the judgment and then when I have the judgment dead or exam I'll video it and "
              "I'll make him cry.",
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': "Other stuff I'm doing but I will help you because I feel for you but I can't do "
             'it for a 50 50 split because he wanted a 50 50 split I said waters just give me '
             "the judgment and then when I have the judgment dead or exam I'll video it and "
             "I'll make him cry.",
      'title': 'Justice by making debtors cry in Judgment Debtor Exams  Judgment enforcement '
               '(Mr. Grey Judgment Enforcement)',
      'url': 'https://www.youtube.com/watch?v=09e6Gzw3S0U&t=33s',
      'video_id': '09e6Gzw3S0U'}],
 2: [{'author': 'Verdict',
      'channel': 'Verdict',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:14](https://www.youtube.com/watch?v=aWnv0AR52jY&t=314s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If the credit agreement, the lease, or the business contract you signed says '
              "the loser pays the winner's fees, and an enormous number of them say exactly "
              "that, the court will enforce that clause. There's also a federal trap called "
              'Rule 68.',
      'timestamp': 314,
      'timestamp_label': '[00:05:14]',
      'timestamp_seconds': 314,
      'tip': 'If the credit agreement, the lease, or the business contract you signed says the '
             "loser pays the winner's fees, and an enormous number of them say exactly that, "
             "the court will enforce that clause. There's also a federal trap called Rule 68.",
      'title': '# What Happens If You Lose a Civil Lawsuit? Judgment & Garnishment Explained '
               '(Verdict)',
      'url': 'https://www.youtube.com/watch?v=aWnv0AR52jY&t=314s',
      'video_id': 'aWnv0AR52jY'},
     {'author': 'Capital Decode',
      'channel': 'Capital Decode',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:18](https://www.youtube.com/watch?v=yhlRryGjPSU&t=198s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So the most practical alternative left on the table is trying to reach a '
              'private agreement with existing lenders to renegotiate those debt terms '
              'completely out of court. So the big decision right now is weighing an outofc '
              'court fix against a formal bankruptcy.',
      'timestamp': 198,
      'timestamp_label': '[00:03:18]',
      'timestamp_seconds': 198,
      'tip': 'So the most practical alternative left on the table is trying to reach a private '
             'agreement with existing lenders to renegotiate those debt terms completely out '
             'of court. So the big decision right now is weighing an outofc court fix against '
             'a formal bankruptcy.',
      'title': 'WHEN THINGS BREAK | Financial Restructuring, Bankruptcy & Distressed Debt | '
               'Episode 23 (Capital Decode)',
      'url': 'https://www.youtube.com/watch?v=yhlRryGjPSU&t=198s',
      'video_id': 'yhlRryGjPSU'},
     {'author': 'LeanLaw - Your Legal Revenue Operations Partner',
      'channel': 'LeanLaw - Your Legal Revenue Operations Partner',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:49](https://www.youtube.com/watch?v=pmUaXhIL3eA&t=589s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And what it's going to do is it created the invoice and synced it over to "
              'QuickBooks and then we have recorded the $10,000 payment into the trust account '
              "for Matt Hooper. So, now we'll say, okay, we're ready to pay our fee from the "
              'trust account.',
      'timestamp': 589,
      'timestamp_label': '[00:09:49]',
      'timestamp_seconds': 589,
      'tip': "And what it's going to do is it created the invoice and synced it over to "
             'QuickBooks and then we have recorded the $10,000 payment into the trust account '
             "for Matt Hooper. So, now we'll say, okay, we're ready to pay our fee from the "
             'trust account.',
      'title': 'LeanLaw Walkthrough: Contingency Case Flow (SettleFlow) (LeanLaw - Your Legal '
               'Revenue Operations Partner)',
      'url': 'https://www.youtube.com/watch?v=pmUaXhIL3eA&t=589s',
      'video_id': 'pmUaXhIL3eA'},
     {'author': 'Judgment Recovery Training Online',
      'channel': 'Judgment Recovery Training Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=L2dopNFjS6s&t=202s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fees that they have to pay me now sometimes if they don't want to split 50 50 i "
              'make them pay me an assignment fee.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "Fees that they have to pay me now sometimes if they don't want to split 50 50 i "
             'make them pay me an assignment fee.',
      'title': 'How To Complete A Judgment Assignment Agreement (Judgment Recovery Training '
               'Online)',
      'url': 'https://www.youtube.com/watch?v=L2dopNFjS6s&t=202s',
      'video_id': 'L2dopNFjS6s'},
     {'author': 'The Real Estate Classroom',
      'channel': 'The Real Estate Classroom',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:02](https://www.youtube.com/watch?v=dwH7f7RGYC4&t=182s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'These liens can typically force the sale to satisfy a debt. So for example, we '
              'talked about that mortgage or that deed of trust. When you borrow money from '
              "the bank, if you don't make the payment, then the bank can force the sale of "
              'that property to pay off that loan.',
      'timestamp': 182,
      'timestamp_label': '[00:03:02]',
      'timestamp_seconds': 182,
      'tip': 'These liens can typically force the sale to satisfy a debt. So for example, we '
             'talked about that mortgage or that deed of trust. When you borrow money from the '
             "bank, if you don't make the payment, then the bank can force the sale of that "
             'property to pay off that loan.',
      'title': 'What Is A Lien | Real Estate Exam Prep (The Real Estate Classroom)',
      'url': 'https://www.youtube.com/watch?v=dwH7f7RGYC4&t=182s',
      'video_id': 'dwH7f7RGYC4'},
     {'author': 'Debt Collectors International',
      'channel': 'Debt Collectors International',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=ZSpyirZPi9E&t=131s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Direct questions instead of asking where do you bank they will ask what card or '
              'account did you pay your last utility bill from having an attorney that '
              "specializes in handling debtor's examinations is necessary for any actionable "
              'information to be obtained.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': 'Direct questions instead of asking where do you bank they will ask what card or '
             'account did you pay your last utility bill from having an attorney that '
             "specializes in handling debtor's examinations is necessary for any actionable "
             'information to be obtained.',
      'title': 'Debtors Examination (Debt Collectors International)',
      'url': 'https://www.youtube.com/watch?v=ZSpyirZPi9E&t=131s',
      'video_id': 'ZSpyirZPi9E'},
     {'author': 'Retrievables Collection Attorneys',
      'channel': 'Retrievables Collection Attorneys',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=YT8Fu3qHWM0&t=63s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Direct transfers or digital wallets can ease the payment process and expedite '
              'collections tip three incentivize early payments consider offering discounts '
              "for early payments or impose fees for late payments it's a simple but effective "
              'way to motivate timely.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Direct transfers or digital wallets can ease the payment process and expedite '
             'collections tip three incentivize early payments consider offering discounts for '
             "early payments or impose fees for late payments it's a simple but effective way "
             'to motivate timely.',
      'title': 'Mastering B2B Debt Collection Fast & Effective Commercial Debt Recovery '
               '(Retrievables Collection Attorneys)',
      'url': 'https://www.youtube.com/watch?v=YT8Fu3qHWM0&t=63s',
      'video_id': 'YT8Fu3qHWM0'},
     {'author': 'Former IRS Agent Representation   4.2M Views',
      'channel': 'Former IRS Agent Representation   4.2M Views',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=wSIheT1KrFw&t=137s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Going to ask you for a payment agreement but here's the big aha what you think "
              'you can pay or whether you thinking your hardship is completely dependent on '
              'the.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "Going to ask you for a payment agreement but here's the big aha what you think "
             'you can pay or whether you thinking your hardship is completely dependent on '
             'the.',
      'title': 'Preventing IRS Bank Levy and Wage Garnishment: Tips to Halt Enforcement '
               'Actions Immediately (Former IRS Agent Representation   4.2M Views)',
      'url': 'https://www.youtube.com/watch?v=wSIheT1KrFw&t=137s',
      'video_id': 'wSIheT1KrFw'},
     {'author': 'Rules of Tomorrow with Tom Howard',
      'channel': 'Rules of Tomorrow with Tom Howard',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=6mmBEFEMc8g&t=176s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Very often judgments arise because a contract has gone bad because somebody '
              "can't afford to pay for it and therefore before you go and start suing and "
              'then.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': 'Very often judgments arise because a contract has gone bad because somebody '
             "can't afford to pay for it and therefore before you go and start suing and then.",
      'title': 'Enforcement of Judgments - Citation to Discover Assets (Rules of Tomorrow with '
               'Tom Howard)',
      'url': 'https://www.youtube.com/watch?v=6mmBEFEMc8g&t=176s',
      'video_id': '6mmBEFEMc8g'},
     {'author': 'PrepAgent',
      'channel': 'PrepAgent',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=dccNDC1WYF4&t=88s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Consent of the owner an example would be a judgment lean or mechanics lean a '
              "judgment lean is a Court's final decision on the right of the obligator.",
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': 'Consent of the owner an example would be a judgment lean or mechanics lean a '
             "judgment lean is a Court's final decision on the right of the obligator.",
      'title': 'liens - Pass your Real Estate Exam! (PrepAgent)',
      'url': 'https://www.youtube.com/watch?v=dccNDC1WYF4&t=88s',
      'video_id': 'dccNDC1WYF4'},
     {'author': 'Real Estate Exam Questions',
      'channel': 'Real Estate Exam Questions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=KgBg-x2ZZ4w&t=33s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Landlord and tenant b a claim against the property for the payment of a debt a '
              'real estate lean is a legal claim against a property as collateral for the '
              'payment of a debt such as a mortgage or unpaid taxes.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': 'Landlord and tenant b a claim against the property for the payment of a debt a '
             'real estate lean is a legal claim against a property as collateral for the '
             'payment of a debt such as a mortgage or unpaid taxes.',
      'title': '20 Real Estate Exam Questions On Liens - Must Know Questions To Pass  The Real '
               'Estate Exam! (Real Estate Exam Questions)',
      'url': 'https://www.youtube.com/watch?v=KgBg-x2ZZ4w&t=33s',
      'video_id': 'KgBg-x2ZZ4w'},
     {'author': 'Lex Animata Law Visualized | Hesham Elrafei',
      'channel': 'Lex Animata Law Visualized | Hesham Elrafei',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=YB6KKY7Q7ts&t=123s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That the defendant had the right to fair trial was served with notice of the '
              'proceedings for the chance to defend himself before the court and to appeal the '
              'judge decision and lastly that the judgment is not contrary to the public '
              'policy of the enforcing country.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': 'That the defendant had the right to fair trial was served with notice of the '
             'proceedings for the chance to defend himself before the court and to appeal the '
             'judge decision and lastly that the judgment is not contrary to the public policy '
             'of the enforcing country.',
      'title': 'International Law | Recognition & Enforcement of Foreign Judgments | Lex '
               'Animata by Hesham Elrafei (Lex Animata Law Visualized | Hesham Elrafei)',
      'url': 'https://www.youtube.com/watch?v=YB6KKY7Q7ts&t=123s',
      'video_id': 'YB6KKY7Q7ts'},
     {'author': 'The Business Disputes Register',
      'channel': 'The Business Disputes Register',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:11](https://www.youtube.com/watch?v=bgQht-y6jWY&t=131s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They care about reputation then they'll be highly motivated to contact you to "
              'reach a settlement and ask you to remove the dispute from the register which '
              "you will only do if they settle your invoice you're in control for more "
              'information see disputesregister.org.',
      'timestamp': 131,
      'timestamp_label': '[00:02:11]',
      'timestamp_seconds': 131,
      'tip': "They care about reputation then they'll be highly motivated to contact you to "
             'reach a settlement and ask you to remove the dispute from the register which you '
             "will only do if they settle your invoice you're in control for more information "
             'see disputesregister.org.',
      'title': 'Unpaid Invoice - 4 Best Actions to Take Immediately to Get Clients to Pay in '
               'the USA (The Business Disputes Register)',
      'url': 'https://www.youtube.com/watch?v=bgQht-y6jWY&t=131s',
      'video_id': 'bgQht-y6jWY'},
     {'author': 'Jacob Blank',
      'channel': 'Jacob Blank',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:16](https://www.youtube.com/watch?v=cbgT8jQuacQ&t=316s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Month and the skip tracing is free that's right it comes with the the phone "
              'numbers it comes with the contact information no longer pay for skip tracing '
              'just use Co reality resource and use.',
      'timestamp': 316,
      'timestamp_label': '[00:05:16]',
      'timestamp_seconds': 316,
      'tip': "Month and the skip tracing is free that's right it comes with the the phone "
             'numbers it comes with the contact information no longer pay for skip tracing '
             'just use Co reality resource and use.',
      'title': 'How To Skip Trace For FREE! Wholesaling Real Estate Step By Step 2025 (Jacob '
               'Blank)',
      'url': 'https://www.youtube.com/watch?v=cbgT8jQuacQ&t=316s',
      'video_id': 'cbgT8jQuacQ'},
     {'author': 'Fight Employment Discrimination',
      'channel': 'Fight Employment Discrimination',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=X9i8o5iRl9M&t=116s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You only have this one so know it inside and out nasa's motion for summary "
              'judgment said that they had accommodated me and on paper they had they had '
              'evidence my signature on a form that said I was being accommodated case closed '
              'nasa said we have a signed form.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': "You only have this one so know it inside and out nasa's motion for summary "
             'judgment said that they had accommodated me and on paper they had they had '
             'evidence my signature on a form that said I was being accommodated case closed '
             'nasa said we have a signed form.',
      'title': "How to Defeat Your Employer's Motion for Summary Judgement at EEOC - "
               'Employment Discrimination (Fight Employment Discrimination)',
      'url': 'https://www.youtube.com/watch?v=X9i8o5iRl9M&t=116s',
      'video_id': 'X9i8o5iRl9M'}],
 3: [{'author': 'Santiago Cueto | Miami Business Litigation Lawyer',
      'channel': 'Santiago Cueto | Miami Business Litigation Lawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=W9UHSaFUIn8&t=202s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "A warrant for their arrest. This is not a traffic ticket. Beyond the debtor's "
              'examination, you should also be running asset searches. A good asset search '
              'will reveal bank accounts, brokerage accounts, real property, vehicles, '
              'business filings, and UCC liens.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "A warrant for their arrest. This is not a traffic ticket. Beyond the debtor's "
             'examination, you should also be running asset searches. A good asset search will '
             'reveal bank accounts, brokerage accounts, real property, vehicles, business '
             'filings, and UCC liens.',
      'title': "Judgment-Proof Debtor THINKS They're Safe | Here's Why They're Wrong (Santiago "
               'Cueto | Miami Business Litigation Lawyer)',
      'url': 'https://www.youtube.com/watch?v=W9UHSaFUIn8&t=202s',
      'video_id': 'W9UHSaFUIn8'},
     {'author': 'Fairmax Law , a Debt Relief Law Firm',
      'channel': 'Fairmax Law , a Debt Relief Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=2eXm6HnwE1g&t=63s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Creditor may not get anything even if the debt is valid for debtors this can be '
              'good news it limits the claims that must be paid through the bankruptcy.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Creditor may not get anything even if the debt is valid for debtors this can be '
             'good news it limits the claims that must be paid through the bankruptcy.',
      'title': 'Bankruptcy Claims Bar Date: Why Deadlines Matter (Fairmax Law , a Debt Relief '
               'Law Firm)',
      'url': 'https://www.youtube.com/watch?v=2eXm6HnwE1g&t=63s',
      'video_id': '2eXm6HnwE1g'},
     {'author': 'Private Investigator Videos',
      'channel': 'Private Investigator Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=q-khGCaOPck&t=466s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Phone number a debtor faced with losing those might come up with some cash so '
              'they can stay in business real estate vehicles you can seize.',
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': 'Phone number a debtor faced with losing those might come up with some cash so '
             'they can stay in business real estate vehicles you can seize.',
      'title': 'Steps To Collect Court Judgment Debt Assets (Private Investigator Videos)',
      'url': 'https://www.youtube.com/watch?v=q-khGCaOPck&t=466s',
      'video_id': 'q-khGCaOPck'},
     {'author': 'Law Office of Jeffrey B. Kelly',
      'channel': 'Law Office of Jeffrey B. Kelly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:44](https://www.youtube.com/watch?v=9Ihk-KKwFBU&t=524s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '401(k) and you cash it out, number one, now you have tax debt. Number two, now '
              "you've got cash in the bank account and the wildcard exemption is $5,000 for an "
              'individual and $10,000 for a married couple.',
      'timestamp': 524,
      'timestamp_label': '[00:08:44]',
      'timestamp_seconds': 524,
      'tip': '401(k) and you cash it out, number one, now you have tax debt. Number two, now '
             "you've got cash in the bank account and the wildcard exemption is $5,000 for an "
             'individual and $10,000 for a married couple.',
      'title': 'Bankruptcy Mistakes that Can Destroy Your Case (Law Office of Jeffrey B. '
               'Kelly)',
      'url': 'https://www.youtube.com/watch?v=9Ihk-KKwFBU&t=524s',
      'video_id': '9Ihk-KKwFBU'},
     {'author': 'Zindo',
      'channel': 'Zindo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:07](https://www.youtube.com/watch?v=Xpf-6IU1qtQ&t=67s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'When businesses are faced with these old choices, they typically just write off '
              "the debt because they don't want to deal with it. Doesn't cost you anything "
              "upfront and preserves your business's reputation.",
      'timestamp': 67,
      'timestamp_label': '[00:01:07]',
      'timestamp_seconds': 67,
      'tip': 'When businesses are faced with these old choices, they typically just write off '
             "the debt because they don't want to deal with it. Doesn't cost you anything "
             "upfront and preserves your business's reputation.",
      'title': 'How Do You Fix Cash Flow Problems Caused by Unpaid Invoices? (Zindo)',
      'url': 'https://www.youtube.com/watch?v=Xpf-6IU1qtQ&t=67s',
      'video_id': 'Xpf-6IU1qtQ'},
     {'author': 'Small Claims Judgment Collection Marketplace',
      'channel': 'Small Claims Judgment Collection Marketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=qBdmGDT7sLE&t=101s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mail our documents to enforce your customers case we give you the forms letters '
              'and know-how so you can earn that fifty percent contingency Commission visit us '
              "at small claims processing com you'll be glad you did again that small claims "
              'processing com.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': 'Mail our documents to enforce your customers case we give you the forms letters '
             'and know-how so you can earn that fifty percent contingency Commission visit us '
             "at small claims processing com you'll be glad you did again that small claims "
             'processing com.',
      'title': 'Small Claims Judgment Recovery Business Course (Small Claims Judgment '
               'Collection Marketplace)',
      'url': 'https://www.youtube.com/watch?v=qBdmGDT7sLE&t=101s',
      'video_id': 'qBdmGDT7sLE'},
     {'author': 'Default Investor Association',
      'channel': 'Default Investor Association',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:43](https://www.youtube.com/watch?v=fjA8sRRh0ZI&t=1063s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Enough to satisfy my judgment no it's barely going to cover a little bit of "
              "profit and my attorneys fees and my cost from my rig I'll get some money but "
              'not.',
      'timestamp': 1063,
      'timestamp_label': '[00:17:43]',
      'timestamp_seconds': 1063,
      'tip': "Enough to satisfy my judgment no it's barely going to cover a little bit of "
             "profit and my attorneys fees and my cost from my rig I'll get some money but "
             'not.',
      'title': 'Final Judgment Recovery Intro Class - Part 1 of 2  of Full Class (Default '
               'Investor Association)',
      'url': 'https://www.youtube.com/watch?v=fjA8sRRh0ZI&t=1063s',
      'video_id': 'fjA8sRRh0ZI'},
     {'author': 'LTS Law Firm Channel',
      'channel': 'LTS Law Firm Channel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=cv-rg7aHsRE&t=156s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Business locations, receivables, and other attachable  assets based on lawful '
              'sources and available evidence. Five, supporting documents and costs.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'Business locations, receivables, and other attachable  assets based on lawful '
             'sources and available evidence. Five, supporting documents and costs.',
      'title': 'The Role of Vietnam’s Civil Judgment Enforcement Agency in Debt Recovery | LTS '
               'LAW FIRM (LTS Law Firm Channel)',
      'url': 'https://www.youtube.com/watch?v=cv-rg7aHsRE&t=156s',
      'video_id': 'cv-rg7aHsRE'},
     {'author': 'BlackBeltBarrister',
      'channel': 'BlackBeltBarrister',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:31](https://www.youtube.com/watch?v=EKjVl_JQ5QE&t=91s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Become a judgment debtor in other words you owe the judgment creditor a debt '
              'under the judgment as a judgment.',
      'timestamp': 91,
      'timestamp_label': '[00:01:31]',
      'timestamp_seconds': 91,
      'tip': 'Become a judgment debtor in other words you owe the judgment creditor a debt '
             'under the judgment as a judgment.',
      'title': 'Enforcing a Foreign Judgment - Where Do You Start? | BlackBeltBarrister '
               '(BlackBeltBarrister)',
      'url': 'https://www.youtube.com/watch?v=EKjVl_JQ5QE&t=91s',
      'video_id': 'EKjVl_JQ5QE'},
     {'author': 'The Global Process Server',
      'channel': 'The Global Process Server',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=SUlnLzzcvIk&t=62s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Those answers decide everything else, including timing, translation, cost, and '
              'whether alternative methods are allowed. What happens if you skip the treaty? '
              'Service can be quashed, a default judgment can be vacated, a foreign court may '
              'refuse to enforce your judgment.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'Those answers decide everything else, including timing, translation, cost, and '
             'whether alternative methods are allowed. What happens if you skip the treaty? '
             'Service can be quashed, a default judgment can be vacated, a foreign court may '
             'refuse to enforce your judgment.',
      'title': 'What Happens When Your Defendant Lives in Another Country #lawtok #lawyer '
               '#shorts (The Global Process Server)',
      'url': 'https://www.youtube.com/watch?v=SUlnLzzcvIk&t=62s',
      'video_id': 'SUlnLzzcvIk'},
     {'author': 'Receivables Info | Debt Collection News',
      'channel': 'Receivables Info | Debt Collection News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:44](https://www.youtube.com/watch?v=miiZfl53MAc&t=644s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Well, they should always be attacking at least one or more of those cuz if you '
              'look back at the old Bill Bartmann days when the banks had limited themselves '
              'to only debt sales, they were overly reliant that cash flow through one '
              'organization.',
      'timestamp': 644,
      'timestamp_label': '[00:10:44]',
      'timestamp_seconds': 644,
      'tip': 'Well, they should always be attacking at least one or more of those cuz if you '
             'look back at the old Bill Bartmann days when the banks had limited themselves to '
             'only debt sales, they were overly reliant that cash flow through one '
             'organization.',
      'title': 'Credit Issuer Compliance Tools You Should Be Using in 2025 | Ep.238 '
               '(Receivables Info | Debt Collection News)',
      'url': 'https://www.youtube.com/watch?v=miiZfl53MAc&t=644s',
      'video_id': 'miiZfl53MAc'},
     {'author': 'Law Librarianship: Legal Research',
      'channel': 'Law Librarianship: Legal Research',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:35](https://www.youtube.com/watch?v=7vopi99AK4A&t=1055s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Physically marking up noting up in the margins where references to later case '
              "are referred to so it's very very messy indeed but the citator do that work "
              'for.',
      'timestamp': 1055,
      'timestamp_label': '[00:17:35]',
      'timestamp_seconds': 1055,
      'tip': 'Physically marking up noting up in the margins where references to later case '
             "are referred to so it's very very messy indeed but the citator do that work for.",
      'title': 'QUT Law Week 6 Class: Introduction to case law - Part 2 and tips for '
               'Assignment Two (Law Librarianship: Legal Research)',
      'url': 'https://www.youtube.com/watch?v=7vopi99AK4A&t=1055s',
      'video_id': '7vopi99AK4A'},
     {'author': 'The Real Estate Lawyer',
      'channel': 'The Real Estate Lawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=RFKcDlW0gQU&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Against you well unfortunately if you have a judgment against you it means that '
              'you have been sued in the Civil context and that you have lost so that.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Against you well unfortunately if you have a judgment against you it means that '
             'you have been sued in the Civil context and that you have lost so that.',
      'title': 'Judgment Liens: What Every Homeowner Needs to Know (The Real Estate Lawyer)',
      'url': 'https://www.youtube.com/watch?v=RFKcDlW0gQU&t=15s',
      'video_id': 'RFKcDlW0gQU'},
     {'author': 'OffshoreAlert',
      'channel': 'OffshoreAlert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=2ApchMyxmWg&t=59s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The one downstairs you probably could have seen the material and they told us '
              'we could not have handout material because they were going to give you '
              'everything online after the conference so bear with us the best you can on that '
              "and we'll go ahead and get started here.",
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'The one downstairs you probably could have seen the material and they told us we '
             'could not have handout material because they were going to give you everything '
             "online after the conference so bear with us the best you can on that and we'll "
             'go ahead and get started here.',
      'title': 'Debt Collection: How to Locate Bank Accounts & Other Assets to Enforce '
               'Judgments (OffshoreAlert)',
      'url': 'https://www.youtube.com/watch?v=2ApchMyxmWg&t=59s',
      'video_id': '2ApchMyxmWg'},
     {'author': 'The Proper Person',
      'channel': 'The Proper Person',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:46](https://www.youtube.com/watch?v=djAI4TQ1S00&t=226s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Communication back and forth with those viewers so it's good idea that I just "
              'kind of keep that going so again if anyone has any experience with any of those '
              "things that I mentioned feel free to post in the comments below with that I'll "
              'go ahead and in this video.',
      'timestamp': 226,
      'timestamp_label': '[00:03:46]',
      'timestamp_seconds': 226,
      'tip': "Communication back and forth with those viewers so it's good idea that I just "
             'kind of keep that going so again if anyone has any experience with any of those '
             "things that I mentioned feel free to post in the comments below with that I'll "
             'go ahead and in this video.',
      'title': 'Legal Nuts And Bolts: Registering Foreign Judgment (The Proper Person)',
      'url': 'https://www.youtube.com/watch?v=djAI4TQ1S00&t=226s',
      'video_id': 'djAI4TQ1S00'}],
 4: [{'author': 'People Locator Skip Tracing',
      'channel': 'People Locator Skip Tracing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=6mK0uU9RBO8&t=69s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'LLC, partnership, or other business entity? What is the nature of their '
              'involvement? What is their ownership percentage? Do they receive any '
              'compensation, distributions, or benefits from the entity? What assets does the '
              'entity hold? Bank accounts and financial institutions.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'LLC, partnership, or other business entity? What is the nature of their '
             'involvement? What is their ownership percentage? Do they receive any '
             'compensation, distributions, or benefits from the entity? What assets does the '
             'entity hold? Bank accounts and financial institutions.',
      'title': 'Debtor Examination Questions to Ask (People Locator Skip Tracing)',
      'url': 'https://www.youtube.com/watch?v=6mK0uU9RBO8&t=69s',
      'video_id': '6mK0uU9RBO8'},
     {'author': 'Fair Capital',
      'channel': 'Fair Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=svZlO-c19tA&t=95s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thanks for the recommendation. I had to spend another year chasing those. '
              "They're ready for you in the conference room. You focus on your business. Fair "
              'Capital will focus on recovering your unpaid invoices. Get your free debt '
              'collection quote today.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': 'Thanks for the recommendation. I had to spend another year chasing those. '
             "They're ready for you in the conference room. You focus on your business. Fair "
             'Capital will focus on recovering your unpaid invoices. Get your free debt '
             'collection quote today.',
      'title': 'Another Excuse. Same Unpaid Invoice. | Fair Capital (Fair Capital)',
      'url': 'https://www.youtube.com/watch?v=svZlO-c19tA&t=95s',
      'video_id': 'svZlO-c19tA'},
     {'author': 'Danny Klein',
      'channel': 'Danny Klein',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=3AJVt6F_pYQ&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "To call I'm going to jack up your credit I'm going to garnish your wages we're "
              "going to Levy your bank accounts we're going to lean your property let's avoid.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "To call I'm going to jack up your credit I'm going to garnish your wages we're "
             "going to Levy your bank accounts we're going to lean your property let's avoid.",
      'title': 'The Undeniable Podcast | Secrets Behind the Debt Collection Business | Mike '
               'Martinez Episode 6 (Danny Klein)',
      'url': 'https://www.youtube.com/watch?v=3AJVt6F_pYQ&t=15s',
      'video_id': '3AJVt6F_pYQ'},
     {'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:43](https://www.youtube.com/watch?v=lSw0SJbVp-A&t=283s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll see transactions in equity type claims? It's a good question and and for "
              "our purpose, remember when you're thinking of secured claims, you might be "
              'thinking of secured bank debt or bonds that are going to be trading among '
              'broker dealers in a big boy um network.',
      'timestamp': 283,
      'timestamp_label': '[00:04:43]',
      'timestamp_seconds': 283,
      'tip': "'ll see transactions in equity type claims? It's a good question and and for our "
             "purpose, remember when you're thinking of secured claims, you might be thinking "
             'of secured bank debt or bonds that are going to be trading among broker dealers '
             'in a big boy um network.',
      'title': 'Bankruptcy Claims Trading (The National Law Review)',
      'url': 'https://www.youtube.com/watch?v=lSw0SJbVp-A&t=283s',
      'video_id': 'lSw0SJbVp-A'},
     {'author': 'Casengine App',
      'channel': 'Casengine App',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=5rA-sJpvgAY&t=218s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every asset moves through a fixed sequence, and the row menu only ever offers '
              "the step that is actually available. This trade license is pending, so it's "
              'only action is record investigation. The bank account is found, so it offers '
              'apply attachment.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'Every asset moves through a fixed sequence, and the row menu only ever offers '
             "the step that is actually available. This trade license is pending, so it's only "
             'action is record investigation. The bank account is found, so it offers apply '
             'attachment.',
      'title': 'CASENGINE Execution Module: Enforce Judgments & Recover Debts (Casengine App)',
      'url': 'https://www.youtube.com/watch?v=5rA-sJpvgAY&t=218s',
      'video_id': '5rA-sJpvgAY'},
     {'author': 'OffshoreAlert',
      'channel': 'OffshoreAlert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:55:25](https://www.youtube.com/watch?v=ruQAKGpCYE8&t=3325s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Go to New York, make the argument that, uh, it is likely that at some point '
              'assets are going to come through New York. So, So a New York state court '
              'judgment, and then take post asset post judgment discovery on the New York '
              'judgment you just obtained.',
      'timestamp': 3325,
      'timestamp_label': '[00:55:25]',
      'timestamp_seconds': 3325,
      'tip': 'Go to New York, make the argument that, uh, it is likely that at some point '
             'assets are going to come through New York. So, So a New York state court '
             'judgment, and then take post asset post judgment discovery on the New York '
             'judgment you just obtained.',
      'title': 'How To Enforce Foreign Judgments in the USA & How US based Agencies Can Reach '
               'Offshore Activity   Of (OffshoreAlert)',
      'url': 'https://www.youtube.com/watch?v=ruQAKGpCYE8&t=3325s',
      'video_id': 'ruQAKGpCYE8'},
     {'author': 'Nigerian Law School Lectures',
      'channel': 'Nigerian Law School Lectures',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:25](https://www.youtube.com/watch?v=b-12dpeHnyA&t=985s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, if the court decided to tell my brother, "Stop building on that land until '
              'this matter is determined." That is called interlocutory order.',
      'timestamp': 985,
      'timestamp_label': '[00:16:25]',
      'timestamp_seconds': 985,
      'tip': 'So, if the court decided to tell my brother, "Stop building on that land until '
             'this matter is determined." That is called interlocutory order.',
      'title': 'Week 14: Closing Address & Judgment EXPLAINED | Nigerian Law School Civil '
               'Litigation (Nigerian Law School Lectures)',
      'url': 'https://www.youtube.com/watch?v=b-12dpeHnyA&t=985s',
      'video_id': 'b-12dpeHnyA'},
     {'author': 'Thomson Reuters',
      'channel': 'Thomson Reuters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:15](https://www.youtube.com/watch?v=hAq3ZiEtqk0&t=255s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Protection for the Homestead Property does not apply for secured creditors such '
              'as the bank that holds the mortgage on the home for bankruptcy cases filed '
              'after April 1st 2019 federal bankruptcy law Shields a home from sale if the '
              "owner's equity does not exceed.",
      'timestamp': 255,
      'timestamp_label': '[00:04:15]',
      'timestamp_seconds': 255,
      'tip': 'Protection for the Homestead Property does not apply for secured creditors such '
             'as the bank that holds the mortgage on the home for bankruptcy cases filed after '
             "April 1st 2019 federal bankruptcy law Shields a home from sale if the owner's "
             'equity does not exceed.',
      'title': 'Financial Literacy: Understanding and Managing Debt–Segment 7: Garnishments, '
               'Liens, & Judgements (Thomson Reuters)',
      'url': 'https://www.youtube.com/watch?v=hAq3ZiEtqk0&t=255s',
      'video_id': 'hAq3ZiEtqk0'},
     {'author': 'Skip Tracers',
      'channel': 'Skip Tracers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:02](https://www.youtube.com/watch?v=UqntxJnXdto&t=662s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Fields whether it's serving court documents locating hidden assets or finding "
              'those hard-to-reach Witnesses skip tracers LLC is here to help you navigate the '
              'complexities of your cases for more information visit www.ipers.org.',
      'timestamp': 662,
      'timestamp_label': '[00:11:02]',
      'timestamp_seconds': 662,
      'tip': "Fields whether it's serving court documents locating hidden assets or finding "
             'those hard-to-reach Witnesses skip tracers LLC is here to help you navigate the '
             'complexities of your cases for more information visit www.ipers.org.',
      'title': 'Skip Tracer Files | Episode 1 | Court Process Serving, Skip Tracing & Asset '
               'Location Secrets (Skip Tracers)',
      'url': 'https://www.youtube.com/watch?v=UqntxJnXdto&t=662s',
      'video_id': 'UqntxJnXdto'},
     {'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:11](https://www.youtube.com/watch?v=R3nWxu374QE&t=851s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s financial interest in that business entity, not the managerial interest. 't "
              'take over their LLC and start, you know, running the business, but you are '
              'entitled to their financial interest.',
      'timestamp': 851,
      'timestamp_label': '[00:14:11]',
      'timestamp_seconds': 851,
      'tip': "'s financial interest in that business entity, not the managerial interest. 't "
             'take over their LLC and start, you know, running the business, but you are '
             'entitled to their financial interest.',
      'title': 'Enforcement Post Judgment Proceedings and Collections (The National Law '
               'Review)',
      'url': 'https://www.youtube.com/watch?v=R3nWxu374QE&t=851s',
      'video_id': 'R3nWxu374QE'},
     {'author': 'Arbeit U',
      'channel': 'Arbeit U',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:52](https://www.youtube.com/watch?v=d5DXPK2ggSk&t=352s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah yeah I feel like I see and hear a lot of people just like I have the right '
              "information out and it just goes right into the software and like that's it so "
              'I think that is a really that was a good answer.',
      'timestamp': 352,
      'timestamp_label': '[00:05:52]',
      'timestamp_seconds': 352,
      'tip': 'Yeah yeah I feel like I see and hear a lot of people just like I have the right '
             "information out and it just goes right into the software and like that's it so I "
             'think that is a really that was a good answer.',
      'title': 'Debt Collection 101: Tips for Successful Skiptracing at Scale (Arbeit U)',
      'url': 'https://www.youtube.com/watch?v=d5DXPK2ggSk&t=352s',
      'video_id': 'd5DXPK2ggSk'},
     {'author': 'Lawyer Tips by The Sterling Firm #lawyer #law',
      'channel': 'Lawyer Tips by The Sterling Firm #lawyer #law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:26](https://www.youtube.com/watch?v=UV-WyQ1-NC4&t=626s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Will notify the Judgment creditor if a claim of exemption has been filed with '
              'the court the Judgment creditor May then oppose the exemption otherwise if '
              'there is no opposition filed the subject property will be released from Levy.',
      'timestamp': 626,
      'timestamp_label': '[00:10:26]',
      'timestamp_seconds': 626,
      'tip': 'Will notify the Judgment creditor if a claim of exemption has been filed with '
             'the court the Judgment creditor May then oppose the exemption otherwise if there '
             'is no opposition filed the subject property will be released from Levy.',
      'title': 'POST-JUDGMENT: HOW TO COLLECT YOUR MONEY? POST JUDGMENT COLLECTION METHOD | '
               '#LAWYER #LAWFIRM (Lawyer Tips by The Sterling Firm #lawyer #law)',
      'url': 'https://www.youtube.com/watch?v=UV-WyQ1-NC4&t=626s',
      'video_id': 'UV-WyQ1-NC4'},
     {'author': 'The Credit Repair Shop',
      'channel': 'The Credit Repair Shop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:59](https://www.youtube.com/watch?v=--FOsBTlu2E&t=839s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Activities letter and debt validation letter thank you for your time this is '
              'Stephen A Williams president and founder the credit prayers shop.com say hi to '
              'Pokemon.',
      'timestamp': 839,
      'timestamp_label': '[00:13:59]',
      'timestamp_seconds': 839,
      'tip': 'Activities letter and debt validation letter thank you for your time this is '
             'Stephen A Williams president and founder the credit prayers shop.com say hi to '
             'Pokemon.',
      'title': 'Statute Of Limitation for a Judgment #thecreditrepairshop #judgment (The '
               'Credit Repair Shop)',
      'url': 'https://www.youtube.com/watch?v=--FOsBTlu2E&t=839s',
      'video_id': '--FOsBTlu2E'},
     {'author': 'AceOfCoins',
      'channel': 'AceOfCoins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:03](https://www.youtube.com/watch?v=3qP0K9KK5G8&t=363s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Calling me about it yeah yeah exactly yeah and someone asking about shares '
              'sorry go ahead did you have anymore no thank you good questions thanks Karen '
              'all right.',
      'timestamp': 363,
      'timestamp_label': '[00:06:03]',
      'timestamp_seconds': 363,
      'tip': 'Calling me about it yeah yeah exactly yeah and someone asking about shares sorry '
             'go ahead did you have anymore no thank you good questions thanks Karen all '
             'right.',
      'title': 'Debt collections and post judgment discovery (AceOfCoins)',
      'url': 'https://www.youtube.com/watch?v=3qP0K9KK5G8&t=363s',
      'video_id': '3qP0K9KK5G8'},
     {'author': 'AssetProtectionTraining.com',
      'channel': 'AssetProtectionTraining.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:32](https://www.youtube.com/watch?v=HqKU9rVRjNI&t=392s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Your life and stop the professional takers if you spend 10% of the time you '
              'spend making money protecting it you will be safe and you will sleep well at '
              'night thank you very much for listening.',
      'timestamp': 392,
      'timestamp_label': '[00:06:32]',
      'timestamp_seconds': 392,
      'tip': 'Your life and stop the professional takers if you spend 10% of the time you '
             'spend making money protecting it you will be safe and you will sleep well at '
             'night thank you very much for listening.',
      'title': 'Who Enforces US Judgments Abroad - No Country (AssetProtectionTraining.com)',
      'url': 'https://www.youtube.com/watch?v=HqKU9rVRjNI&t=392s',
      'video_id': 'HqKU9rVRjNI'}],
 5: [{'author': 'Collect Back Rent Training Course',
      'channel': 'Collect Back Rent Training Course',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=5T2nU_IZTXs&t=111s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Judgment assignment business with literally no money then collecting on the '
              'judgments in all 50 states you can have a debt collection attorney but in.',
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': 'Judgment assignment business with literally no money then collecting on the '
             'judgments in all 50 states you can have a debt collection attorney but in.',
      'title': 'Buying & Collecting on Judgments (Collect Back Rent Training Course)',
      'url': 'https://www.youtube.com/watch?v=5T2nU_IZTXs&t=111s',
      'video_id': '5T2nU_IZTXs'},
     {'author': 'Lee Aitken',
      'channel': 'Lee Aitken',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:50](https://www.youtube.com/watch?v=wTrr0cp_Pug&t=470s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll see of course here um buying and selling debts a very large business. Also, "
              "buying and selling claims as a very large business. Um, but we've got a bit of "
              'a problem because in a sense, uh, a claim may be too small to actually '
              'litigate.',
      'timestamp': 470,
      'timestamp_label': '[00:07:50]',
      'timestamp_seconds': 470,
      'tip': "'ll see of course here um buying and selling debts a very large business. Also, "
             "buying and selling claims as a very large business. Um, but we've got a bit of a "
             'problem because in a sense, uh, a claim may be too small to actually litigate.',
      'title': 'Askaree Equity - Introduction to legal and equitable assignment (Lee Aitken)',
      'url': 'https://www.youtube.com/watch?v=wTrr0cp_Pug&t=470s',
      'video_id': 'wTrr0cp_Pug'},
     {'author': 'Simple Explain',
      'channel': 'Simple Explain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=cZtaubxDzMA&t=80s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first and most obvious option is to repay the debt. If they pay off their '
              'obligation, the creditor will remove the lien by filing a release. Debtors can '
              'also avoid a non-consensual lien in bankruptcy under certain conditions.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'The first and most obvious option is to repay the debt. If they pay off their '
             'obligation, the creditor will remove the lien by filing a release. Debtors can '
             'also avoid a non-consensual lien in bankruptcy under certain conditions.',
      'title': 'Judgment Lien: Definition, Examples, Vs. Property Lien (Simple Explain)',
      'url': 'https://www.youtube.com/watch?v=cZtaubxDzMA&t=80s',
      'video_id': 'cZtaubxDzMA'},
     {'author': 'Court Kutchehry',
      'channel': 'Court Kutchehry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=E-XLFQLiAEE&t=20s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before we read a single section, we must understand the problem that this Act '
              'was designed to solve. Viewers, imagine a bank in the 1980s. A borrower has '
              'defaulted on a large loan. The bank files a suit, a civil suit for recovery.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Before we read a single section, we must understand the problem that this Act '
             'was designed to solve. Viewers, imagine a bank in the 1980s. A borrower has '
             'defaulted on a large loan. The bank files a suit, a civil suit for recovery.',
      'title': 'Why Was the DRT Act Needed? 8 Years in Civil Court vs 180 Days in DRT | DRT '
               'Act Explained Ep 1 (Court Kutchehry)',
      'url': 'https://www.youtube.com/watch?v=E-XLFQLiAEE&t=20s',
      'video_id': 'E-XLFQLiAEE'},
     {'author': 'Taurus Collections (UK) Ltd',
      'channel': 'Taurus Collections (UK) Ltd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:02](https://www.youtube.com/watch?v=PQz21Mf4OZc&t=362s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's a win or lose situation. A judge isn't there to craft a creative business "
              "solution. They're though to apply the law. And another thing, court judgments "
              'are public record. Oh, so anyone could look it up. Your dispute becomes '
              'searchable online.',
      'timestamp': 362,
      'timestamp_label': '[00:06:02]',
      'timestamp_seconds': 362,
      'tip': "It's a win or lose situation. A judge isn't there to craft a creative business "
             "solution. They're though to apply the law. And another thing, court judgments "
             'are public record. Oh, so anyone could look it up. Your dispute becomes '
             'searchable online.',
      'title': 'Invoice Recovery: Mediation Versus Litigation Analysis (Taurus Collections '
               '(UK) Ltd)',
      'url': 'https://www.youtube.com/watch?v=PQz21Mf4OZc&t=362s',
      'video_id': 'PQz21Mf4OZc'},
     {'author': 'Saul Ewing LLP',
      'channel': 'Saul Ewing LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:38](https://www.youtube.com/watch?v=MM_dCPRf9LE&t=1898s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In this case, on the same day, a consumer sent a dispute letter to Equifax and '
              "the consumer's council sent the debt collector a representation letter. Two "
              'weeks go by, but the debt collector did not immediately process the '
              'representation.',
      'timestamp': 1898,
      'timestamp_label': '[00:31:38]',
      'timestamp_seconds': 1898,
      'tip': 'In this case, on the same day, a consumer sent a dispute letter to Equifax and '
             "the consumer's council sent the debt collector a representation letter. Two "
             'weeks go by, but the debt collector did not immediately process the '
             'representation.',
      'title': 'Disputes, Damages, & Default Judgments - 2026 CFS Annual Webinar: Panel 1 '
               '(Saul Ewing LLP)',
      'url': 'https://www.youtube.com/watch?v=MM_dCPRf9LE&t=1898s',
      'video_id': 'MM_dCPRf9LE'},
     {'author': 'Consumer Warrior',
      'channel': 'Consumer Warrior',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=7TbwIGMYgYE&t=20s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll help you resolve your serious debt problem. All right, let's talk about "
              'winning your debt collection lawsuit. Now in most of these lawsuits, when the '
              "debt collector files a suit against you, a lot of them go to a default 'cause "
              "people don't respond.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "'ll help you resolve your serious debt problem. All right, let's talk about "
             'winning your debt collection lawsuit. Now in most of these lawsuits, when the '
             "debt collector files a suit against you, a lot of them go to a default 'cause "
             "people don't respond.",
      'title': 'How to Win Your Debt Collection Lawsuit Without Going to Trial (Consumer '
               'Warrior)',
      'url': 'https://www.youtube.com/watch?v=7TbwIGMYgYE&t=20s',
      'video_id': '7TbwIGMYgYE'},
     {'author': 'Alabama Consumer Protection Lawyers',
      'channel': 'Alabama Consumer Protection Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=xF2ZuR2-O4o&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cover in this video are the seven mistakes that we often see people make when '
              "they're testifying in a debt collection trial so let me set stage for.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Cover in this video are the seven mistakes that we often see people make when '
             "they're testifying in a debt collection trial so let me set stage for.",
      'title': '7 mistakes when testifying in a debt collection trial (Alabama Consumer '
               'Protection Lawyers)',
      'url': 'https://www.youtube.com/watch?v=xF2ZuR2-O4o&t=15s',
      'video_id': 'xF2ZuR2-O4o'},
     {'author': 'David Babel',
      'channel': 'David Babel',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:22](https://www.youtube.com/watch?v=q6PjSqG-sF4&t=202s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Bankruptcy attorney to evaluate if you'll be able to avoid that judgment during "
              'the course of the bankruptcy it is a lot more complicated expensive and may not '
              'be permissible if commenced after the conclusion of the bankruptcy case know '
              'your rights.',
      'timestamp': 202,
      'timestamp_label': '[00:03:22]',
      'timestamp_seconds': 202,
      'tip': "Bankruptcy attorney to evaluate if you'll be able to avoid that judgment during "
             'the course of the bankruptcy it is a lot more complicated expensive and may not '
             'be permissible if commenced after the conclusion of the bankruptcy case know '
             'your rights.',
      'title': 'Did You Know - Judgment Liens On Your Primary Residence (David Babel)',
      'url': 'https://www.youtube.com/watch?v=q6PjSqG-sF4&t=202s',
      'video_id': 'q6PjSqG-sF4'},
     {'author': 'Five Minute Legal Master Series',
      'channel': 'Five Minute Legal Master Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=gLlOpG3V6GY&t=196s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Claim be sure to make an educated choice rather than ignoring it and losing by '
              'default we hope you have enjoyed this episode of the five minute legal master '
              "series where expert board-certified attorneys help you master today's important "
              'legal topics.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': 'Claim be sure to make an educated choice rather than ignoring it and losing by '
             'default we hope you have enjoyed this episode of the five minute legal master '
             "series where expert board-certified attorneys help you master today's important "
             'legal topics.',
      'title': 'The Five Minute Legal Master: The Bankruptcy Claims Process (Five Minute Legal '
               'Master Series)',
      'url': 'https://www.youtube.com/watch?v=gLlOpG3V6GY&t=196s',
      'video_id': 'gLlOpG3V6GY'},
     {'author': 'Mr. Grey Judgment Enforcement',
      'channel': 'Mr. Grey Judgment Enforcement',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=499-NK9hWnc&t=28s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Interesting um the judge um saw me and about four or five of my managing '
              'associates come walking in and said who are all these people the judgment '
              'debtor tells you the ambulance.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'Interesting um the judge um saw me and about four or five of my managing '
             'associates come walking in and said who are all these people the judgment debtor '
             'tells you the ambulance.',
      'title': 'Judgment Debtor Exam and Bank Levy Strategy for Court Judgments (Mr. Grey '
               'Judgment Enforcement)',
      'url': 'https://www.youtube.com/watch?v=499-NK9hWnc&t=28s',
      'video_id': '499-NK9hWnc'},
     {'author': 'Courtroom 1401, Daley Center',
      'channel': 'Courtroom 1401, Daley Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:21](https://www.youtube.com/watch?v=RHS2h5dUkHk&t=261s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The Judgment creditor is not required to appear in court until the citation to '
              'the deor is served an unserved citation cannot be continued so do not send the '
              'court a continuance order for an unserved citation.',
      'timestamp': 261,
      'timestamp_label': '[00:04:21]',
      'timestamp_seconds': 261,
      'tip': 'The Judgment creditor is not required to appear in court until the citation to '
             'the deor is served an unserved citation cannot be continued so do not send the '
             'court a continuance order for an unserved citation.',
      'title': 'Video #6 Filing a Citation to Discover Assets to Debtor (Courtroom 1401, Daley '
               'Center)',
      'url': 'https://www.youtube.com/watch?v=RHS2h5dUkHk&t=261s',
      'video_id': 'RHS2h5dUkHk'},
     {'author': 'Richardson Law Offices',
      'channel': 'Richardson Law Offices',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=wibZgw9EKZ4&t=216s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Garnish your wages that sort of thing feel free to give my office a call at '
              "856-432-4113 and we'll talk a little bit more about it and see whether I can "
              'help you get on track with that debt.',
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'Garnish your wages that sort of thing feel free to give my office a call at '
             "856-432-4113 and we'll talk a little bit more about it and see whether I can "
             'help you get on track with that debt.',
      'title': 'Does Statute of Limitations Stop a Collections Suit (Richardson Law Offices)',
      'url': 'https://www.youtube.com/watch?v=wibZgw9EKZ4&t=216s',
      'video_id': 'wibZgw9EKZ4'},
     {'author': 'Meet Jermaine (Clear &Strategic)',
      'channel': 'Meet Jermaine (Clear &Strategic)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:11](https://www.youtube.com/watch?v=XSfDS_s1URg&t=431s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Rights until next time stay informed and stay protected I will put a copy of '
              'this actual case in the description below thanks a lot and as always you be '
              'great.',
      'timestamp': 431,
      'timestamp_label': '[00:07:11]',
      'timestamp_seconds': 431,
      'tip': 'Rights until next time stay informed and stay protected I will put a copy of '
             'this actual case in the description below thanks a lot and as always you be '
             'great.',
      'title': 'Avoid This Credit Dispute Mistake! #FDCPA Law Suit Case Study '
               '#askadebtcollector #advice #law (Meet Jermaine (Clear &Strategic))',
      'url': 'https://www.youtube.com/watch?v=XSfDS_s1URg&t=431s',
      'video_id': 'XSfDS_s1URg'},
     {'author': 'Attorney Thoughts',
      'channel': 'Attorney Thoughts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=QgFvjr6fOpg&t=130s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Enforcement of foreign judgments Act of 1986 in order to comply with the Act a '
              'copy of the original judgment must be registered with the clerk of the courts '
              'in the related jurisdiction along with an affidavit containing essential '
              'information.',
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'Enforcement of foreign judgments Act of 1986 in order to comply with the Act a '
             'copy of the original judgment must be registered with the clerk of the courts in '
             'the related jurisdiction along with an affidavit containing essential '
             'information.',
      'title': 'What is the Enforcement of Foreign Judgments? (Attorney Thoughts)',
      'url': 'https://www.youtube.com/watch?v=QgFvjr6fOpg&t=130s',
      'video_id': 'QgFvjr6fOpg'}],
 6: [{'author': 'The National Law Review',
      'channel': 'The National Law Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:43](https://www.youtube.com/watch?v=dGbPfDmUGhk&t=1123s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So for instance, if you see Silver Point, which I I don't know if they're still "
              'your client, David, but they were at various times. Um if you see Silver Point '
              "in a case buying something, well, you know, it's pretty easy to find price "
              'discovery and just beat them by a point.',
      'timestamp': 1123,
      'timestamp_label': '[00:18:43]',
      'timestamp_seconds': 1123,
      'tip': "So for instance, if you see Silver Point, which I I don't know if they're still "
             'your client, David, but they were at various times. Um if you see Silver Point '
             "in a case buying something, well, you know, it's pretty easy to find price "
             'discovery and just beat them by a point.',
      'title': 'Advanced Bankruptcy Transactions: Bankruptcy Claims Trading (The National Law '
               'Review)',
      'url': 'https://www.youtube.com/watch?v=dGbPfDmUGhk&t=1123s',
      'video_id': 'dGbPfDmUGhk'},
     {'author': 'KillDebt & ParkerGPT: The New Way To Law',
      'channel': 'KillDebt & ParkerGPT: The New Way To Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=YYdsx06msa0&t=159s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You'll find a videos and letters on how to do that Shazam uh videos I've done "
              "on demystifying validation. There's plenty of ways to do that, but let's put "
              "that letter back again. That's your average debt collection letter that a "
              'client of mine received.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': "You'll find a videos and letters on how to do that Shazam uh videos I've done on "
             "demystifying validation. There's plenty of ways to do that, but let's put that "
             "letter back again. That's your average debt collection letter that a client of "
             'mine received.',
      'title': 'The Power of the FDCPA 1692e and 1692f Against Debt Collectors (KillDebt & '
               'ParkerGPT: The New Way To Law)',
      'url': 'https://www.youtube.com/watch?v=YYdsx06msa0&t=159s',
      'video_id': 'YYdsx06msa0'},
     {'author': 'OffshoreAlert',
      'channel': 'OffshoreAlert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:16](https://www.youtube.com/watch?v=j34w1ZyVNSc&t=196s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '25 000 in payments before you find it and decide that you may need to liquidate '
              'that asset now if the construction business is.',
      'timestamp': 196,
      'timestamp_label': '[00:03:16]',
      'timestamp_seconds': 196,
      'tip': '25 000 in payments before you find it and decide that you may need to liquidate '
             'that asset now if the construction business is.',
      'title': 'Debt Collection: How To Locate Bank Accounts & Other Assets To Enforce '
               'Judgments (OffshoreAlert)',
      'url': 'https://www.youtube.com/watch?v=j34w1ZyVNSc&t=196s',
      'video_id': 'j34w1ZyVNSc'},
     {'author': 'Martin Kravchenko',
      'channel': 'Martin Kravchenko',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:53](https://www.youtube.com/watch?v=aB0whCtGI5k&t=593s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Search loads the results and as you can see we start getting the data now we '
              'need we need to get 50 of them on this first page fantastic clicks pation goes '
              'to the second.',
      'timestamp': 593,
      'timestamp_label': '[00:09:53]',
      'timestamp_seconds': 593,
      'tip': 'Search loads the results and as you can see we start getting the data now we '
             'need we need to get 50 of them on this first page fantastic clicks pation goes '
             'to the second.',
      'title': 'Web Scraping for Law Firms - STOP manually tracking court dates and dockets '
               '(Martin Kravchenko)',
      'url': 'https://www.youtube.com/watch?v=aB0whCtGI5k&t=593s',
      'video_id': 'aB0whCtGI5k'},
     {'author': 'County Portal',
      'channel': 'County Portal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=IDWN8CuNtfA&t=20s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'First, you need to understand that bankruptcy is a federal matter. This means '
              'the records are not at your local county courthouse. They are held by the '
              'federal court system.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'First, you need to understand that bankruptcy is a federal matter. This means '
             'the records are not at your local county courthouse. They are held by the '
             'federal court system.',
      'title': 'How To Find Bankruptcy Court Records? (County Portal)',
      'url': 'https://www.youtube.com/watch?v=IDWN8CuNtfA&t=20s',
      'video_id': 'IDWN8CuNtfA'},
     {'author': 'TheJRInstitute',
      'channel': 'TheJRInstitute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=HCKxJmuEUR8&t=103s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Expose the secrets that the books on the subject don't talk about I will share "
              'with you how you can make over six figures a year in this business without ever '
              "collecting a court judgment yourself don't waste an another minute take the "
              'first step and visit.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': "Expose the secrets that the books on the subject don't talk about I will share "
             'with you how you can make over six figures a year in this business without ever '
             "collecting a court judgment yourself don't waste an another minute take the "
             'first step and visit.',
      'title': 'Unlocking the Truth - How to Make $100,000 a year in the Judgment Recovery '
               'Business (TheJRInstitute)',
      'url': 'https://www.youtube.com/watch?v=HCKxJmuEUR8&t=103s',
      'video_id': 'HCKxJmuEUR8'},
     {'author': 'Receivables Info | Debt Collection News',
      'channel': 'Receivables Info | Debt Collection News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=PSWN-POX4Uc&t=21s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I think we're going to find out on this phone call today. Our panelists today "
              'include Mr. Joey Wilkins is currently the chief compliance officer and general '
              'counsel for USVE. Youerve is a high volume, high-tech process serving company '
              'uh specializing in the collection space.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "I think we're going to find out on this phone call today. Our panelists today "
             'include Mr. Joey Wilkins is currently the chief compliance officer and general '
             'counsel for USVE. Youerve is a high volume, high-tech process serving company uh '
             'specializing in the collection space.',
      'title': 'Skiptracing 2024: Relationship-Based, but Backed by Data! | RI Webinar '
               '(Receivables Info | Debt Collection News)',
      'url': 'https://www.youtube.com/watch?v=PSWN-POX4Uc&t=21s',
      'video_id': 'PSWN-POX4Uc'},
     {'author': 'Consumer Warrior',
      'channel': 'Consumer Warrior',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:41](https://www.youtube.com/watch?v=YmCEqLCbD3s&t=581s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, how do we deal with this? If you're dealing with bank levy, if you're "
              'dealing with a wage garnishment, is there anything you can do if you find '
              'yourself uh in that kind of situation?',
      'timestamp': 581,
      'timestamp_label': '[00:09:41]',
      'timestamp_seconds': 581,
      'tip': "Now, how do we deal with this? If you're dealing with bank levy, if you're "
             'dealing with a wage garnishment, is there anything you can do if you find '
             'yourself uh in that kind of situation?',
      'title': "Bank Levy vs. Wage Garnishment... What's the Difference? (Consumer Warrior)",
      'url': 'https://www.youtube.com/watch?v=YmCEqLCbD3s&t=581s',
      'video_id': 'YmCEqLCbD3s'},
     {'author': 'Sacramento County Public Law Library',
      'channel': 'Sacramento County Public Law Library',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=HrhPbWDRBVU&t=175s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh the procedure that the court uses is also subject to change so be sure to '
              "check the signature line that you see the first one that's uh going to receive.",
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': 'Uh the procedure that the court uses is also subject to change so be sure to '
             "check the signature line that you see the first one that's uh going to receive.",
      'title': 'Enforcement of Judgments: Part 3: Finding Assets (Sacramento County Public Law '
               'Library)',
      'url': 'https://www.youtube.com/watch?v=HrhPbWDRBVU&t=175s',
      'video_id': 'HrhPbWDRBVU'},
     {'author': 'verdict sentencestv',
      'channel': 'verdict sentencestv',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=HPD6TM130zk&t=132s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Nicole Lewis and Jose Martinez, proof that y'all have any jurisdiction. Well, "
              "I'll take the information from Urban Oaks, but we'll find out. Wolschlag, "
              "please tell me first, why don't we address the jurisdictional issue?",
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': "Nicole Lewis and Jose Martinez, proof that y'all have any jurisdiction. Well, "
             "I'll take the information from Urban Oaks, but we'll find out. Wolschlag, please "
             "tell me first, why don't we address the jurisdictional issue?",
      'title': 'Sovereign Citizen Says “We Don’t Accept The Law!” — Judge Delivers Final '
               'Reality Check (verdict sentencestv)',
      'url': 'https://www.youtube.com/watch?v=HPD6TM130zk&t=132s',
      'video_id': 'HPD6TM130zk'},
     {'author': 'Consumer Law 101 by Attorney Aaron Swift',
      'channel': 'Consumer Law 101 by Attorney Aaron Swift',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:18](https://www.youtube.com/watch?v=owpVxkqEbEk&t=918s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can be debt forgiveness trade line deletion material damages which leads you '
              'know a lot of fees and fees to be paid to our affiliate Partners um so again '
              "that's a gold silver bronze case example under fdcpa.",
      'timestamp': 918,
      'timestamp_label': '[00:15:18]',
      'timestamp_seconds': 918,
      'tip': 'Can be debt forgiveness trade line deletion material damages which leads you '
             'know a lot of fees and fees to be paid to our affiliate Partners um so again '
             "that's a gold silver bronze case example under fdcpa.",
      'title': 'Debt Collector Lawsuits (FDCPA): Examples and Outcomes by Attorney Aaron Swift '
               '(Consumer Law 101 by Attorney Aaron Swift)',
      'url': 'https://www.youtube.com/watch?v=owpVxkqEbEk&t=918s',
      'video_id': 'owpVxkqEbEk'},
     {'author': 'Private Investigator Videos',
      'channel': 'Private Investigator Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=gyWC9jWNaXQ&t=134s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Against a person typically a lien is against an asset or a piece of property '
              "whether it's real estate or otherwise it's important to get good legal advice "
              'from attorney to find out how that may affect your proposed interest in a '
              'property.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': 'Against a person typically a lien is against an asset or a piece of property '
             "whether it's real estate or otherwise it's important to get good legal advice "
             'from attorney to find out how that may affect your proposed interest in a '
             'property.',
      'title': 'What is the difference between a judgement and a lien? (Private Investigator '
               'Videos)',
      'url': 'https://www.youtube.com/watch?v=gyWC9jWNaXQ&t=134s',
      'video_id': 'gyWC9jWNaXQ'},
     {'author': 'Westgate Law',
      'channel': 'Westgate Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:35](https://www.youtube.com/watch?v=Nb1quOaLNWk&t=155s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'If yet can be proactive and not reactive you can deal with it before the worst '
              'case scenario happens give us a call today at 888 hundred eight nine one one '
              "nine nine five and you'll talk to me personally today to address your issues.",
      'timestamp': 155,
      'timestamp_label': '[00:02:35]',
      'timestamp_seconds': 155,
      'tip': 'If yet can be proactive and not reactive you can deal with it before the worst '
             'case scenario happens give us a call today at 888 hundred eight nine one one '
             "nine nine five and you'll talk to me personally today to address your issues.",
      'title': 'How To Stop Wage Garnishments and Bank Levies | Bankruptcy Law (Westgate Law)',
      'url': 'https://www.youtube.com/watch?v=Nb1quOaLNWk&t=155s',
      'video_id': 'Nb1quOaLNWk'},
     {'author': 'Five Minute Legal Master Series',
      'channel': 'Five Minute Legal Master Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:25](https://www.youtube.com/watch?v=_O0Yt0qGF-k&t=145s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Herself they can be required to bring books and records with them so that the '
              'lawyer can actually sit down with this deposition and go through the checkbook '
              'or go through the quicken data file or the quickbooks data file.',
      'timestamp': 145,
      'timestamp_label': '[00:02:25]',
      'timestamp_seconds': 145,
      'tip': 'Herself they can be required to bring books and records with them so that the '
             'lawyer can actually sit down with this deposition and go through the checkbook '
             'or go through the quicken data file or the quickbooks data file.',
      'title': 'Post Judgment Discovery of Assets (Five Minute Legal Master Series)',
      'url': 'https://www.youtube.com/watch?v=_O0Yt0qGF-k&t=145s',
      'video_id': '_O0Yt0qGF-k'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:26](https://www.youtube.com/watch?v=fQZc8moX-c4&t=386s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Pursuing them are skill intensive tasks this presentation has provided an '
              'overview of some of the options available to judgment creditors.',
      'timestamp': 386,
      'timestamp_label': '[00:06:26]',
      'timestamp_seconds': 386,
      'tip': 'Pursuing them are skill intensive tasks this presentation has provided an '
             'overview of some of the options available to judgment creditors.',
      'title': 'Post Judgment Collection Methods (LawShelf)',
      'url': 'https://www.youtube.com/watch?v=fQZc8moX-c4&t=386s',
      'video_id': 'fQZc8moX-c4'}],
 7: [{'author': 'Cross the River, Find the Treasure',
      'channel': 'Cross the River, Find the Treasure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=TiGcICs90xE&t=36s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Learn from our step-by-step do-it-yourself course some creditors turn to '
              'attorneys but very few lawyers are in the business of judgment recovery the '
              'court does not enforce collection.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Learn from our step-by-step do-it-yourself course some creditors turn to '
             'attorneys but very few lawyers are in the business of judgment recovery the '
             'court does not enforce collection.',
      'title': 'Judgment Recovery Business (Cross the River, Find the Treasure)',
      'url': 'https://www.youtube.com/watch?v=TiGcICs90xE&t=36s',
      'video_id': 'TiGcICs90xE'},
     {'author': 'Nizam Hashmi - Hashmi Law Group',
      'channel': 'Nizam Hashmi - Hashmi Law Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=AT4U_1yLtaE&t=49s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is where an examination in aid of execution becomes important. The debtor '
              'may be required to answer under oath about employment, income, property, bank '
              'accounts, debts, expenses, and other financial information.',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'That is where an examination in aid of execution becomes important. The debtor '
             'may be required to answer under oath about employment, income, property, bank '
             'accounts, debts, expenses, and other financial information.',
      'title': 'Enforcing a Judgment in Ontario: How Do You Actually Get Paid? Hashmi Law '
               'Group (Nizam Hashmi - Hashmi Law Group)',
      'url': 'https://www.youtube.com/watch?v=AT4U_1yLtaE&t=49s',
      'video_id': 'AT4U_1yLtaE'},
     {'author': 'Consumer Warrior',
      'channel': 'Consumer Warrior',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:06](https://www.youtube.com/watch?v=fWHpyqQu_5M&t=246s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Debt collectors and their attorneys are counting on that—they know the system, '
              'and you don’t. So, the first step is simple: show up, be on time, be a few '
              'minutes early, whether on Zoom or in person.',
      'timestamp': 246,
      'timestamp_label': '[00:04:06]',
      'timestamp_seconds': 246,
      'tip': 'Debt collectors and their attorneys are counting on that—they know the system, '
             'and you don’t. So, the first step is simple: show up, be on time, be a few '
             'minutes early, whether on Zoom or in person.',
      'title': 'Sued by a Debt Collector—How to Win Without Paying (Consumer Warrior)',
      'url': 'https://www.youtube.com/watch?v=fWHpyqQu_5M&t=246s',
      'video_id': 'fWHpyqQu_5M'},
     {'author': 'Thompson Coburn LLP',
      'channel': 'Thompson Coburn LLP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:12](https://www.youtube.com/watch?v=LBVpN-q6M-A&t=792s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mismanaging assets by bringing the deor into the jurisdiction of the bankruptcy '
              "court the debtor's Affairs then become subject to the disclosure process "
              "that's.",
      'timestamp': 792,
      'timestamp_label': '[00:13:12]',
      'timestamp_seconds': 792,
      'tip': 'Mismanaging assets by bringing the deor into the jurisdiction of the bankruptcy '
             "court the debtor's Affairs then become subject to the disclosure process that's.",
      'title': 'Bankruptcy 101: Bankruptcy Basics (Thompson Coburn LLP)',
      'url': 'https://www.youtube.com/watch?v=LBVpN-q6M-A&t=792s',
      'video_id': 'LBVpN-q6M-A'},
     {'author': 'Los Angeles County Consumer and Business Affairs',
      'channel': 'Los Angeles County Consumer and Business Affairs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:20](https://www.youtube.com/watch?v=f4vDDF_EojM&t=260s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reports that partial payment has been received from the debtor thanks for '
              'watching if you would like additional information about the small claims '
              'process visit our website.',
      'timestamp': 260,
      'timestamp_label': '[00:04:20]',
      'timestamp_seconds': 260,
      'tip': 'Reports that partial payment has been received from the debtor thanks for '
             'watching if you would like additional information about the small claims process '
             'visit our website.',
      'title': 'Small Claims Court - Acknowledgment of Satisfaction of Judgment (Los Angeles '
               'County Consumer and Business Affairs)',
      'url': 'https://www.youtube.com/watch?v=f4vDDF_EojM&t=260s',
      'video_id': 'f4vDDF_EojM'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:50](https://www.youtube.com/watch?v=i6PAssklgJg&t=290s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Methods such as filing a lawsuit to collect on the debt through the supervision '
              'of the judicial system debtors are protected from harassment.',
      'timestamp': 290,
      'timestamp_label': '[00:04:50]',
      'timestamp_seconds': 290,
      'tip': 'Methods such as filing a lawsuit to collect on the debt through the supervision '
             'of the judicial system debtors are protected from harassment.',
      'title': 'Fair Debt Collection Practices Act (LawShelf)',
      'url': 'https://www.youtube.com/watch?v=i6PAssklgJg&t=290s',
      'video_id': 'i6PAssklgJg'},
     {'author': 'Judgment Recovery Training Online',
      'channel': 'Judgment Recovery Training Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=U_rmTsuyYV8&t=178s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That need to be completed and submitted to the court as the forms and process '
              "to submit judging paperwork to the local sheriff's department to seize click "
              'the link below for more information on how to start your own judgment recovery '
              'business.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': 'That need to be completed and submitted to the court as the forms and process to '
             "submit judging paperwork to the local sheriff's department to seize click the "
             'link below for more information on how to start your own judgment recovery '
             'business.',
      'title': 'Judgment Recovery Business Opportunity | Judgment Recovery Networking '
               '(Judgment Recovery Training Online)',
      'url': 'https://www.youtube.com/watch?v=U_rmTsuyYV8&t=178s',
      'video_id': 'U_rmTsuyYV8'},
     {'author': 'People Locator Skip Tracing',
      'channel': 'People Locator Skip Tracing',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=leX2BIpiyNQ&t=36s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Despite the different names, the core process is similar everywhere. To '
              'initiate a debtor examination, the judgment creditor files a motion or '
              'application with the court the judgment, requesting an order requiring the '
              'debtor to appear.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': 'Despite the different names, the core process is similar everywhere. To initiate '
             'a debtor examination, the judgment creditor files a motion or application with '
             'the court the judgment, requesting an order requiring the debtor to appear.',
      'title': 'Debtor Examination Guide (People Locator Skip Tracing)',
      'url': 'https://www.youtube.com/watch?v=leX2BIpiyNQ&t=36s',
      'video_id': 'leX2BIpiyNQ'},
     {'author': 'NYU School of Law',
      'channel': 'NYU School of Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:41](https://www.youtube.com/watch?v=M__Ft9jrAVI&t=1841s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The court dismisses the named plaintiffs but retained the claims of the named '
              'New Jersey plaintiff and then the rest of the class members.',
      'timestamp': 1841,
      'timestamp_label': '[00:30:41]',
      'timestamp_seconds': 1841,
      'tip': 'The court dismisses the named plaintiffs but retained the claims of the named '
             'New Jersey plaintiff and then the rest of the class members.',
      'title': 'Jurisdiction and Choice of Law (NYU School of Law)',
      'url': 'https://www.youtube.com/watch?v=M__Ft9jrAVI&t=1841s',
      'video_id': 'M__Ft9jrAVI'},
     {'author': 'Studicata',
      'channel': 'Studicata',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=r3PQ_FYkNRM&t=159s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would be the supreme court and federal courts right so taking a step back '
              'though for a second right if we think about issue spotting in the big picture.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': 'Would be the supreme court and federal courts right so taking a step back though '
             'for a second right if we think about issue spotting in the big picture.',
      'title': 'Justiciability and the "Case or Controversy Requirement" [LEAP Preview: '
               'Constitutional Law] (Studicata)',
      'url': 'https://www.youtube.com/watch?v=r3PQ_FYkNRM&t=159s',
      'video_id': 'r3PQ_FYkNRM'},
     {'author': 'Vann Attorneys, PLLC',
      'channel': 'Vann Attorneys, PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=YhtCR_GKvQ4&t=127s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '30 days to respond to it and after that, the court will then issue the judgment '
              "in North Carolina. At that point, we're off to the races just like we always "
              'are in trying to find the assets to satisfy that judgment. Again, this is not '
              'really a very difficult process.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': '30 days to respond to it and after that, the court will then issue the judgment '
             "in North Carolina. At that point, we're off to the races just like we always are "
             'in trying to find the assets to satisfy that judgment. Again, this is not really '
             'a very difficult process.',
      'title': 'Enforcement of Foreign Judgments by James Vann (Vann Attorneys, PLLC)',
      'url': 'https://www.youtube.com/watch?v=YhtCR_GKvQ4&t=127s',
      'video_id': 'YhtCR_GKvQ4'},
     {'author': 'Bobby Benjy',
      'channel': 'Bobby Benjy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:59](https://www.youtube.com/watch?v=a13Ojjc6ruw&t=419s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is a very brief generalized summary for how the process works but it's "
              'pretty concise and to the point and reasonably accurate if you have any '
              'questions please feel free to call us our website is www.pevs.com.',
      'timestamp': 419,
      'timestamp_label': '[00:06:59]',
      'timestamp_seconds': 419,
      'tip': "This is a very brief generalized summary for how the process works but it's "
             'pretty concise and to the point and reasonably accurate if you have any '
             'questions please feel free to call us our website is www.pevs.com.',
      'title': 'California Money Judgment Enforcement Series - Part 5: Bank Levies (Bobby '
               'Benjy)',
      'url': 'https://www.youtube.com/watch?v=a13Ojjc6ruw&t=419s',
      'video_id': 'a13Ojjc6ruw'},
     {'author': 'Brandon Joe Williams - Law Made Fun and Simple!',
      'channel': 'Brandon Joe Williams - Law Made Fun and Simple!',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:57](https://www.youtube.com/watch?v=LmiTRGMtKr0&t=2637s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Thing if they sneeze you're going to file in an opposition so that's important "
              'to clarify when they file a motion to dismiss the onus is on you to to make a '
              "counter if they file anything yeah if they breathe into the docket you're in "
              'opposition.',
      'timestamp': 2637,
      'timestamp_label': '[00:43:57]',
      'timestamp_seconds': 2637,
      'tip': "Thing if they sneeze you're going to file in an opposition so that's important "
             'to clarify when they file a motion to dismiss the onus is on you to to make a '
             "counter if they file anything yeah if they breathe into the docket you're in "
             'opposition.',
      'title': '(VIEW VIDEO DESCRIPTION) Litigation Course - Video 2 of 5 - Navigating PACER, '
               'looking at a docket (Brandon Joe Williams - Law Made Fun and Simple!)',
      'url': 'https://www.youtube.com/watch?v=LmiTRGMtKr0&t=2637s',
      'video_id': 'LmiTRGMtKr0'},
     {'author': 'ExamPrepAI CPA Review',
      'channel': 'ExamPrepAI CPA Review',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:06](https://www.youtube.com/watch?v=uGQHaP-BNy0&t=486s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Studying I know seems impossible right especially to enjoy the material we'll "
              'do it together tap into the power of cpa.psu.edu.',
      'timestamp': 486,
      'timestamp_label': '[00:08:06]',
      'timestamp_seconds': 486,
      'tip': "Studying I know seems impossible right especially to enjoy the material we'll do "
             'it together tap into the power of cpa.psu.edu.',
      'title': 'The Fair Debt Collection Practices Act (FDCPA) [CPA Prep] (ExamPrepAI CPA '
               'Review)',
      'url': 'https://www.youtube.com/watch?v=uGQHaP-BNy0&t=486s',
      'video_id': 'uGQHaP-BNy0'},
     {'author': 'Florida Trust, Real Estate, Probate, & Foreclosure',
      'channel': 'Florida Trust, Real Estate, Probate, & Foreclosure',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=9x7_I2ygY9E&t=36s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Mary do you know Miss Miss Worthington is here what's that that wasn't her just "
              'I was a lady just went out a minute ago was that her for chance want me go look '
              'checking Mr McDonald.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "Mary do you know Miss Miss Worthington is here what's that that wasn't her just "
             'I was a lady just went out a minute ago was that her for chance want me go look '
             'checking Mr McDonald.',
      'title': 'Can a Foreign Judgment Be BLOCKED by the Statute of Limitations? | FL '
               'Appellate Oral Argument (Florida Trust, Real Estate, Probate, & Foreclosure)',
      'url': 'https://www.youtube.com/watch?v=9x7_I2ygY9E&t=36s',
      'video_id': '9x7_I2ygY9E'}],
 8: [{'author': 'Receivables Info | Debt Collection News',
      'channel': 'Receivables Info | Debt Collection News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:19](https://www.youtube.com/watch?v=1M9DIxuxJGA&t=259s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I so I think it's a combination of the two, right? So we know that whether it's "
              'consumer data consumer data or commercial data, business data, data degrades at '
              'a pretty fast clip.',
      'timestamp': 259,
      'timestamp_label': '[00:04:19]',
      'timestamp_seconds': 259,
      'tip': "I so I think it's a combination of the two, right? So we know that whether it's "
             'consumer data consumer data or commercial data, business data, data degrades at '
             'a pretty fast clip.',
      'title': 'Debt Collection Data Waterfalls: Testing, KPIs, and Continuous Improvement | '
               'Ep. 264 (Receivables Info | Debt Collection News)',
      'url': 'https://www.youtube.com/watch?v=1M9DIxuxJGA&t=259s',
      'video_id': '1M9DIxuxJGA'},
     {'author': 'Hidden Power Files',
      'channel': 'Hidden Power Files',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:24](https://www.youtube.com/watch?v=-HFzhDO6v-A&t=324s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ask whether your county maintains a separate judgment lien index or judgment '
              "docket. If yes, search it under the same names. Check whether your county's "
              'court records are searchable online through a separate portal.',
      'timestamp': 324,
      'timestamp_label': '[00:05:24]',
      'timestamp_seconds': 324,
      'tip': 'Ask whether your county maintains a separate judgment lien index or judgment '
             "docket. If yes, search it under the same names. Check whether your county's "
             'court records are searchable online through a separate portal.',
      'title': 'How Judgment Liens Show Up in Courthouse Records — And How to Find Them | '
               'Hidden Power Files (Hidden Power Files)',
      'url': 'https://www.youtube.com/watch?v=-HFzhDO6v-A&t=324s',
      'video_id': '-HFzhDO6v-A'},
     {'author': 'Alabama Consumer Protection Lawyers',
      'channel': 'Alabama Consumer Protection Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:46](https://www.youtube.com/watch?v=fPw38bPWFtw&t=466s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purpose was not the collection debt but rather its acquisition so again kind of '
              "a clever argument they say no we're not in the business of collecting debts.",
      'timestamp': 466,
      'timestamp_label': '[00:07:46]',
      'timestamp_seconds': 466,
      'tip': 'Purpose was not the collection debt but rather its acquisition so again kind of '
             "a clever argument they say no we're not in the business of collecting debts.",
      'title': 'Case Decision FDCPA Definition of Debt Collector of Debt Buyer --  Barbato v '
               'Crown Asset (Alabama Consumer Protection Lawyers)',
      'url': 'https://www.youtube.com/watch?v=fPw38bPWFtw&t=466s',
      'video_id': 'fPw38bPWFtw'},
     {'author': 'Tommy from DocketDrafter',
      'channel': 'Tommy from DocketDrafter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=ARBpLFKK8iA&t=57s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's also very useful for legal research, but if you actually want docket "
              'entries, you need to go into RECAP. So go over here and click on search PACER '
              "data, and that's going to bring you to this scary screen called advanced RECAP "
              'search.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "That's also very useful for legal research, but if you actually want docket "
             'entries, you need to go into RECAP. So go over here and click on search PACER '
             "data, and that's going to bring you to this scary screen called advanced RECAP "
             'search.',
      'title': 'How to Search Federal Court Dockets for Free with CourtListener (Tommy from '
               'DocketDrafter)',
      'url': 'https://www.youtube.com/watch?v=ARBpLFKK8iA&t=57s',
      'video_id': 'ARBpLFKK8iA'},
     {'author': 'Wilhelmina Randtke',
      'channel': 'Wilhelmina Randtke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=nxcVuXjUaaA&t=205s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is the Medina County Clerk of Court's website and we'll run a simple "
              "search in the docket here to just see what docket for case looks like. We'll "
              'look for all cases with John Smith. You can see lots of John Smiths in Medina '
              'County. Lot of suits in Medina County.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': "This is the Medina County Clerk of Court's website and we'll run a simple search "
             "in the docket here to just see what docket for case looks like. We'll look for "
             'all cases with John Smith. You can see lots of John Smiths in Medina County. Lot '
             'of suits in Medina County.',
      'title': 'Online Legal Research: Part 4 of 9: Court Dockets (Wilhelmina Randtke)',
      'url': 'https://www.youtube.com/watch?v=nxcVuXjUaaA&t=205s',
      'video_id': 'nxcVuXjUaaA'},
     {'author': 'Tim Santoni',
      'channel': 'Tim Santoni',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=rDAzEvzlcbo&t=94s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're looking for information about investigation and background tips and "
              'tricks equipment and other tools and database solutions we appreciate you '
              'following us connect with us in the comments we look forward to seeing you in a '
              'future show thanks.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "If you're looking for information about investigation and background tips and "
             'tricks equipment and other tools and database solutions we appreciate you '
             'following us connect with us in the comments we look forward to seeing you in a '
             'future show thanks.',
      'title': '3 Investigation Strategies for Judgment Enforcement - Debt Collection- Finding '
               'Assets (Tim Santoni)',
      'url': 'https://www.youtube.com/watch?v=rDAzEvzlcbo&t=94s',
      'video_id': 'rDAzEvzlcbo'},
     {'author': 'G2 Risk Solutions',
      'channel': 'G2 Risk Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:29](https://www.youtube.com/watch?v=1PpzRRYapuA&t=1289s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reviewing specific rules to see which jurisdictions require certificates of '
              'service or other nuanced rules make the decision to use a tool where you can '
              'file all of your claims within one single user interface that manages all of '
              'the unique quote.',
      'timestamp': 1289,
      'timestamp_label': '[00:21:29]',
      'timestamp_seconds': 1289,
      'tip': 'Reviewing specific rules to see which jurisdictions require certificates of '
             'service or other nuanced rules make the decision to use a tool where you can '
             'file all of your claims within one single user interface that manages all of the '
             'unique quote.',
      'title': 'How to Optimize Bankruptcy Claims to Maximize Recoveries (G2 Risk Solutions)',
      'url': 'https://www.youtube.com/watch?v=1PpzRRYapuA&t=1289s',
      'video_id': '1PpzRRYapuA'},
     {'author': 'SurplusFundsRiches',
      'channel': 'SurplusFundsRiches',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:08](https://www.youtube.com/watch?v=cKgzsxKOOxs&t=68s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're not concerned about the bad credit. They're not concerned about any of "
              "that. They're not in the middle of buying another house, so they don't have to "
              "get rid of the judgment. They're not in the middle of anything that requires "
              'them to handle this debt.',
      'timestamp': 68,
      'timestamp_label': '[00:01:08]',
      'timestamp_seconds': 68,
      'tip': "They're not concerned about the bad credit. They're not concerned about any of "
             "that. They're not in the middle of buying another house, so they don't have to "
             "get rid of the judgment. They're not in the middle of anything that requires "
             'them to handle this debt.',
      'title': 'Judgment recovery? Nope - waaay better $ maker! (SurplusFundsRiches)',
      'url': 'https://www.youtube.com/watch?v=cKgzsxKOOxs&t=68s',
      'video_id': 'cKgzsxKOOxs'},
     {'author': 'Pankauski Lazarus P.L.L.C.',
      'channel': 'Pankauski Lazarus P.L.L.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=Qdxx6piwSow&t=168s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The equitable or injunctive relief claims in the fourth District Court of '
              'Appeal as of April of 2016 the answer is yes my name is Jonathan calcium and '
              'estate probate litigator with Penn kowski Hauser in West Palm Beach.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'The equitable or injunctive relief claims in the fourth District Court of Appeal '
             'as of April of 2016 the answer is yes my name is Jonathan calcium and estate '
             'probate litigator with Penn kowski Hauser in West Palm Beach.',
      'title': 'Florida Litigation, Proposals for Settlement and Offers of Judgment (Pankauski '
               'Lazarus P.L.L.C.)',
      'url': 'https://www.youtube.com/watch?v=Qdxx6piwSow&t=168s',
      'video_id': 'Qdxx6piwSow'},
     {'author': 'David Holt',
      'channel': 'David Holt',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=mu_dxy3i9Rc&t=57s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The US District Court for the District of Oregon once I've selected a court "
              "you'll notice that other options appear in the bottom half of the screen among "
              'those include a cause of action so you can restrict your results to trademark '
              'infringement click on search.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "The US District Court for the District of Oregon once I've selected a court "
             "you'll notice that other options appear in the bottom half of the screen among "
             'those include a cause of action so you can restrict your results to trademark '
             'infringement click on search.',
      'title': 'Searching Dockets on Bloomberg via PACER (David Holt)',
      'url': 'https://www.youtube.com/watch?v=mu_dxy3i9Rc&t=57s',
      'video_id': 'mu_dxy3i9Rc'},
     {'author': 'Circuit Court Clerk of Nashville, Davidson County',
      'channel': 'Circuit Court Clerk of Nashville, Davidson County',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=FSUH2GyMLJ8&t=90s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Here you can enter in the dollar amount you can select default agreement of '
              'parties or trial in court whichever applies and here you can select your post '
              'judgment interest rate.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Here you can enter in the dollar amount you can select default agreement of '
             'parties or trial in court whichever applies and here you can select your post '
             'judgment interest rate.',
      'title': 'How To E-File A Civil Judgment (Circuit Court Clerk of Nashville, Davidson '
               'County)',
      'url': 'https://www.youtube.com/watch?v=FSUH2GyMLJ8&t=90s',
      'video_id': 'FSUH2GyMLJ8'},
     {'author': 'Badwolf Unincorporated',
      'channel': 'Badwolf Unincorporated',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=2bsfGcj8H0Y&t=122s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Access to more than one one billion records um all filed at the federal courts '
              'okay and it has a search a name for a nationwide index okay of of cases.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'Access to more than one one billion records um all filed at the federal courts '
             'okay and it has a search a name for a nationwide index okay of of cases.',
      'title': 'PACER: Public Access to Court Electronic Records - Learn about cases to win in '
               'court! (Badwolf Unincorporated)',
      'url': 'https://www.youtube.com/watch?v=2bsfGcj8H0Y&t=122s',
      'video_id': '2bsfGcj8H0Y'},
     {'author': 'AFX Videos',
      'channel': 'AFX Videos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=a5bLikprQ4E&t=117s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ordering a title search that you specify the judgment liens are something that '
              'you want to be aware of if you do have questions about running a title search '
              'or researching land records you can reach us at our website at titlesearch.com.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Ordering a title search that you specify the judgment liens are something that '
             'you want to be aware of if you do have questions about running a title search or '
             'researching land records you can reach us at our website at titlesearch.com.',
      'title': 'What is a judgment lien? (AFX Videos)',
      'url': 'https://www.youtube.com/watch?v=a5bLikprQ4E&t=117s',
      'video_id': 'a5bLikprQ4E'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=OaGDs2nX-tw&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'بقضية هو نصف المعركة، وتحصيل مبلغ الحكم قد يكون مجهداً بقدر التقاضي الفعلي.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'بقضية هو نصف المعركة، وتحصيل مبلغ الحكم قد يكون مجهداً بقدر التقاضي الفعلي.',
      'title': "Getting the Money You've Won in Court: Enforcement of Civil Judgement "
               '(LawShelf)',
      'url': 'https://www.youtube.com/watch?v=OaGDs2nX-tw&t=15s',
      'video_id': 'OaGDs2nX-tw'},
     {'author': 'The Credit Repair Shop',
      'channel': 'The Credit Repair Shop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=4Mctc4AuqWA&t=268s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '20 Dela 10 District of Colombia District of Colombia 12 years we got Iowa 20 '
              'straight up 20 10 years 10 years we got 10 years.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': '20 Dela 10 District of Colombia District of Colombia 12 years we got Iowa 20 '
             'straight up 20 10 years 10 years we got 10 years.',
      'title': 'Statute of Limitation on a Judgment (The Credit Repair Shop)',
      'url': 'https://www.youtube.com/watch?v=4Mctc4AuqWA&t=268s',
      'video_id': '4Mctc4AuqWA'}],
 9: [{'author': 'Simple Explain',
      'channel': 'Simple Explain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:37](https://www.youtube.com/watch?v=njrU1ZwxRCY&t=217s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Debtor three if a debt collector violates the fdcpa the debtor can sue them in '
              'state or federal court for damages and legal fees within one year of the '
              'violation hope this would help thanks for watching.',
      'timestamp': 217,
      'timestamp_label': '[00:03:37]',
      'timestamp_seconds': 217,
      'tip': 'Debtor three if a debt collector violates the fdcpa the debtor can sue them in '
             'state or federal court for damages and legal fees within one year of the '
             'violation hope this would help thanks for watching.',
      'title': 'Fair Debt Collection Practices Act (FDCPA): Definition and Rules (Simple '
               'Explain)',
      'url': 'https://www.youtube.com/watch?v=njrU1ZwxRCY&t=217s',
      'video_id': 'njrU1ZwxRCY'},
     {'author': 'LawShelf',
      'channel': 'LawShelf',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:28](https://www.youtube.com/watch?v=IXYtvqeecYI&t=268s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'American debtor-creditor law, but the two are separate legal fields. '
              'Debtor-creditor law, for example, includes regulations on debt collection, '
              'credit reporting, and wage garnishment.',
      'timestamp': 268,
      'timestamp_label': '[00:04:28]',
      'timestamp_seconds': 268,
      'tip': 'American debtor-creditor law, but the two are separate legal fields. '
             'Debtor-creditor law, for example, includes regulations on debt collection, '
             'credit reporting, and wage garnishment.',
      'title': 'Overview of Bankruptcy: Module 1 of 5 (LawShelf)',
      'url': 'https://www.youtube.com/watch?v=IXYtvqeecYI&t=268s',
      'video_id': 'IXYtvqeecYI'},
     {'author': 'The Business Guy | Asset Protection Planners',
      'channel': 'The Business Guy | Asset Protection Planners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=5mmy9Xz_Oko&t=60s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Needs to act under state law to seize the debtors assets failure to pay a '
              'judgment is not subject to contempt of court or imprisonment in other words.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'Needs to act under state law to seize the debtors assets failure to pay a '
             'judgment is not subject to contempt of court or imprisonment in other words.',
      'title': 'How to Avoid Paying a Civil Judgment [Asset Protection Strategies] (The '
               'Business Guy | Asset Protection Planners)',
      'url': 'https://www.youtube.com/watch?v=5mmy9Xz_Oko&t=60s',
      'video_id': '5mmy9Xz_Oko'},
     {'author': 'R.E.A.D.Y. Nation',
      'channel': 'R.E.A.D.Y. Nation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:10](https://www.youtube.com/watch?v=CPZ9XWAJAIY&t=130s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is the world of the of the uniform commercial code. This is the world of '
              'the Federal Reserve Note, the debt instruments. This is the all the world of '
              'the all caps individual, which is the legal fiction. And so, the legal '
              "fiction's role in the UCC is the debtor.",
      'timestamp': 130,
      'timestamp_label': '[00:02:10]',
      'timestamp_seconds': 130,
      'tip': 'This is the world of the of the uniform commercial code. This is the world of '
             'the Federal Reserve Note, the debt instruments. This is the all the world of the '
             "all caps individual, which is the legal fiction. And so, the legal fiction's "
             'role in the UCC is the debtor.',
      'title': 'UCC-1 Explained: Debtor vs. Secured Party & the Two Planes of Law (R.E.A.D.Y. '
               'Nation)',
      'url': 'https://www.youtube.com/watch?v=CPZ9XWAJAIY&t=130s',
      'video_id': 'CPZ9XWAJAIY'},
     {'author': 'JD Simplified',
      'channel': 'JD Simplified',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:17](https://www.youtube.com/watch?v=FUPJlxOU2nI&t=797s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Substantive law defines the legal rights and duties that govern people in their '
              'day-to-day lives outside court. So, for example, the elements required to '
              'establish a breach of contract, or the standard of liability for negligence.',
      'timestamp': 797,
      'timestamp_label': '[00:13:17]',
      'timestamp_seconds': 797,
      'tip': 'Substantive law defines the legal rights and duties that govern people in their '
             'day-to-day lives outside court. So, for example, the elements required to '
             'establish a breach of contract, or the standard of liability for negligence.',
      'title': 'NEW 2026 How to do the analysis for Transfer & Forum Non Conveniens | '
               '§1404(a), §1406(a), §1631 (JD Simplified)',
      'url': 'https://www.youtube.com/watch?v=FUPJlxOU2nI&t=797s',
      'video_id': 'FUPJlxOU2nI'},
     {'author': 'AmeriLawyer',
      'channel': 'AmeriLawyer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=KH6HJIebxnk&t=15s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Including local state and federal laws listeners names and questions may be '
              'simulated the show is not intended to offer business tax or legal advice and.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Including local state and federal laws listeners names and questions may be '
             'simulated the show is not intended to offer business tax or legal advice and.',
      'title': 'Buying Assets From A Distressed Company Before They File Bankruptcy '
               '(AmeriLawyer)',
      'url': 'https://www.youtube.com/watch?v=KH6HJIebxnk&t=15s',
      'video_id': 'KH6HJIebxnk'},
     {'author': 'The Business Guy | Asset Protection Planners',
      'channel': 'The Business Guy | Asset Protection Planners',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:55](https://www.youtube.com/watch?v=nbtlIEi4we0&t=415s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Federal law it seeks a declaratory judgment from the court to determine his '
              'legal obligations under the law number six a consent judgment in a civil.',
      'timestamp': 415,
      'timestamp_label': '[00:06:55]',
      'timestamp_seconds': 415,
      'tip': 'Federal law it seeks a declaratory judgment from the court to determine his '
             'legal obligations under the law number six a consent judgment in a civil.',
      'title': 'How Long Does a Judgment Last? (The Business Guy | Asset Protection Planners)',
      'url': 'https://www.youtube.com/watch?v=nbtlIEi4we0&t=415s',
      'video_id': 'nbtlIEi4we0'},
     {'author': 'North Texas Paralegal Institute',
      'channel': 'North Texas Paralegal Institute',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=9nntBUk_Poo&t=31s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s business decisions, like accepting a case or setting a fee. You organize, "
              'draft from instructions, calendar, gather, track, and flag. The attorney owns '
              'legal judgment, strategy, advice, what to plead or settle, and anything that '
              "needs a lawyer's signature or license.",
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': "'s business decisions, like accepting a case or setting a fee. You organize, "
             'draft from instructions, calendar, gather, track, and flag. The attorney owns '
             'legal judgment, strategy, advice, what to plead or settle, and anything that '
             "needs a lawyer's signature or license.",
      'title': 'What Should I Do? Unauthorized Practice of Law in Texas Family Law | Free NTPI '
               'Lesson (North Texas Paralegal Institute)',
      'url': 'https://www.youtube.com/watch?v=9nntBUk_Poo&t=31s',
      'video_id': '9nntBUk_Poo'},
     {'author': 'Alabama Consumer Protection Lawyers',
      'channel': 'Alabama Consumer Protection Lawyers',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:01:34](https://www.youtube.com/watch?v=qTSer3pu6io&t=3694s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Collecting under state law again it's not really a defense to the state law "
              "claim it's just you have a very nice case against that debt collector for doing "
              "that let's see here.",
      'timestamp': 3694,
      'timestamp_label': '[01:01:34]',
      'timestamp_seconds': 3694,
      'tip': "Collecting under state law again it's not really a defense to the state law "
             "claim it's just you have a very nice case against that debt collector for doing "
             "that let's see here.",
      'title': 'New FDCPA Rules (Regulation F) -- Part One (Alabama Consumer Protection '
               'Lawyers)',
      'url': 'https://www.youtube.com/watch?v=qTSer3pu6io&t=3694s',
      'video_id': 'qTSer3pu6io'},
     {'author': 'Whalen Law Office',
      'channel': 'Whalen Law Office',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=pvEePhOPGhE&t=194s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "When somebody's out there practicing law without a license is the client okay "
              "they're uh receiving legal advice that is generally speaking.",
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': "When somebody's out there practicing law without a license is the client okay "
             "they're uh receiving legal advice that is generally speaking.",
      'title': 'UPL - The Unlicensed Practice of Law (Whalen Law Office)',
      'url': 'https://www.youtube.com/watch?v=pvEePhOPGhE&t=194s',
      'video_id': 'pvEePhOPGhE'},
     {'author': 'Certified ADA Advocacy',
      'channel': 'Certified ADA Advocacy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=6sPkEnDXerg&t=160s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Gave her legal advice and counsel and interestingly enough they didn't equate "
              'that with me practicing the law.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "Gave her legal advice and counsel and interestingly enough they didn't equate "
             'that with me practicing the law.',
      'title': 'Unauthorized Practice of Law OUTCOME (Certified ADA Advocacy)',
      'url': 'https://www.youtube.com/watch?v=6sPkEnDXerg&t=160s',
      'video_id': '6sPkEnDXerg'},
     {'author': 'Five Minute Legal Master Series',
      'channel': 'Five Minute Legal Master Series',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=V5NrY_biljg&t=349s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Against personal property thanks for listening this has been another '
              'installment of the five-minute legal master series where expert attorneys help '
              'you master important legal topics for more information on this and other topics '
              'please visit.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'Against personal property thanks for listening this has been another installment '
             'of the five-minute legal master series where expert attorneys help you master '
             'important legal topics for more information on this and other topics please '
             'visit.',
      'title': 'The Five Minute Legal Master Series: Judgment and Judgment Liens (Five Minute '
               'Legal Master Series)',
      'url': 'https://www.youtube.com/watch?v=V5NrY_biljg&t=349s',
      'video_id': 'V5NrY_biljg'},
     {'author': 'Jedidiah “Jed” McKeehan',
      'channel': 'Jedidiah “Jed” McKeehan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=0Kq_0NfOnMo&t=168s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Issue and other legal issues by going to my website attorney Knoxville comm you '
              'can listen to my podcast in session with Jed McKeon in the itunes store you can '
              'find me on Facebook and Twitter you can also view my other YouTube videos.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Issue and other legal issues by going to my website attorney Knoxville comm you '
             'can listen to my podcast in session with Jed McKeon in the itunes store you can '
             'find me on Facebook and Twitter you can also view my other YouTube videos.',
      'title': 'Collecting Money After A Judgment - Wage Garnishment And Bank Levy (Jedidiah '
               '“Jed” McKeehan)',
      'url': 'https://www.youtube.com/watch?v=0Kq_0NfOnMo&t=168s',
      'video_id': '0Kq_0NfOnMo'},
     {'author': 'Downs Law',
      'channel': 'Downs Law',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:55](https://www.youtube.com/watch?v=K1KakWduA04&t=115s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So those are really the the really kind of essential kind of main ways to '
              'collect on a judgment in georgia there are obviously a variety of other factors '
              "that can be evolved so if you have any questions about that don't hesitate to "
              'reach out to us at downes law.',
      'timestamp': 115,
      'timestamp_label': '[00:01:55]',
      'timestamp_seconds': 115,
      'tip': 'So those are really the the really kind of essential kind of main ways to '
             'collect on a judgment in georgia there are obviously a variety of other factors '
             "that can be evolved so if you have any questions about that don't hesitate to "
             'reach out to us at downes law.',
      'title': 'How to Collect on a Judgment (Downs Law)',
      'url': 'https://www.youtube.com/watch?v=K1KakWduA04&t=115s',
      'video_id': 'K1KakWduA04'},
     {'author': 'The Proper Person',
      'channel': 'The Proper Person',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:01](https://www.youtube.com/watch?v=DfQbJSuzkUQ&t=601s)',
      'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                   'docket screening, lawful assignment/attorney enforcement, and lien '
                   'priority (Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Sorry that I can't give you predictions and very specific detailed answers on "
              "what exactly you have to do so with that I'll go ahead and end this video and "
              "with that I'll see you guys next time.",
      'timestamp': 601,
      'timestamp_label': '[00:10:01]',
      'timestamp_seconds': 601,
      'tip': "Sorry that I can't give you predictions and very specific detailed answers on "
             "what exactly you have to do so with that I'll go ahead and end this video and "
             "with that I'll see you guys next time.",
      'title': 'Legal Nuts And Bolts: Unauthorized Practice Of Law (The Proper Person)',
      'url': 'https://www.youtube.com/watch?v=DfQbJSuzkUQ&t=601s',
      'video_id': 'DfQbJSuzkUQ'}],
 10: [{'author': 'Steiner Law Group, LLC',
       'channel': 'Steiner Law Group, LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:03](https://www.youtube.com/watch?v=RAT4YjdyfEo&t=183s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The bank accounts upon the filing of a bankruptcy to learn more about the many '
               'benefits that bankruptcy offers and to receive help with your debt please give '
               'us a call or visit our website and sign up for our newsletter fresh chapter '
               "don't take chances with your second.",
       'timestamp': 183,
       'timestamp_label': '[00:03:03]',
       'timestamp_seconds': 183,
       'tip': 'The bank accounts upon the filing of a bankruptcy to learn more about the many '
              'benefits that bankruptcy offers and to receive help with your debt please give '
              'us a call or visit our website and sign up for our newsletter fresh chapter '
              "don't take chances with your second.",
       'title': 'Bank Account Garnishments (Steiner Law Group, LLC)',
       'url': 'https://www.youtube.com/watch?v=RAT4YjdyfEo&t=183s',
       'video_id': 'RAT4YjdyfEo'},
      {'author': 'Cross the River, Find the Treasure',
       'channel': 'Cross the River, Find the Treasure',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:31](https://www.youtube.com/watch?v=qHxMlQjoBsU&t=271s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The Judgment amount to cover your charges and extra expenses any enforcement '
               'expenses will eventually be paid by the debtor the Judgment debt is paid in '
               'full when all expenses are met a notification of satisfaction of judgment is '
               'submitted and filed with the court.',
       'timestamp': 271,
       'timestamp_label': '[00:04:31]',
       'timestamp_seconds': 271,
       'tip': 'The Judgment amount to cover your charges and extra expenses any enforcement '
              'expenses will eventually be paid by the debtor the Judgment debt is paid in '
              'full when all expenses are met a notification of satisfaction of judgment is '
              'submitted and filed with the court.',
       'title': 'Judgment Recovery Business Training Course: Small Claims & More Collection '
                'Opportunity (Cross the River, Find the Treasure)',
       'url': 'https://www.youtube.com/watch?v=qHxMlQjoBsU&t=271s',
       'video_id': 'qHxMlQjoBsU'},
      {'author': 'Mr. Grey Judgment Enforcement',
       'channel': 'Mr. Grey Judgment Enforcement',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:23](https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=23s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'What section of the california code of civil procedure says that I cannot levy '
               'on more than one bank at a time great things great babies very good well mr '
               "esidra we don't know anything about this judgment your agent for service the "
               'process ct corp was served great kids.',
       'timestamp': 23,
       'timestamp_label': '[00:00:23]',
       'timestamp_seconds': 23,
       'tip': 'What section of the california code of civil procedure says that I cannot levy '
              'on more than one bank at a time great things great babies very good well mr '
              "esidra we don't know anything about this judgment your agent for service the "
              'process ct corp was served great kids.',
       'title': "Mr  Grey's bank levy strategy - How to collect a judgment from a business "
                '(Mr. Grey Judgment Enforcement)',
       'url': 'https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=23s',
       'video_id': 'CLxNTh8V1qQ'},
      {'author': 'The DeVries Law Firm',
       'channel': 'The DeVries Law Firm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=lfTu39ygsSI&t=47s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I'll also explain how bankruptcy can offer relief and why it may be the "
               'fastest way to regain control if garnishment has already begun. Wage '
               'garnishment happens when a court or government agency orders your employer to '
               'take money directly from your paycheck to pay a debt.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': "I'll also explain how bankruptcy can offer relief and why it may be the fastest "
              'way to regain control if garnishment has already begun. Wage garnishment '
              'happens when a court or government agency orders your employer to take money '
              'directly from your paycheck to pay a debt.',
       'title': 'How To Stop Wage Garnishment Immediately (The DeVries Law Firm)',
       'url': 'https://www.youtube.com/watch?v=lfTu39ygsSI&t=47s',
       'video_id': 'lfTu39ygsSI'},
      {'author': 'Gustan Cho Associates',
       'channel': 'Gustan Cho Associates',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:27](https://www.youtube.com/watch?v=SvBZyaCOSrc&t=27s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's 7 years on your credit report negatively. But, what these banks are doing "
               "is they're selling their debt or these debtors are doing, they're selling "
               'their debt and selling it to new collection and they get another 7 years.',
       'timestamp': 27,
       'timestamp_label': '[00:00:27]',
       'timestamp_seconds': 27,
       'tip': "It's 7 years on your credit report negatively. But, what these banks are doing "
              "is they're selling their debt or these debtors are doing, they're selling their "
              'debt and selling it to new collection and they get another 7 years.',
       'title': 'What Is The Statute Of Limitations On Debt And Judgments (Gustan Cho '
                'Associates)',
       'url': 'https://www.youtube.com/watch?v=SvBZyaCOSrc&t=27s',
       'video_id': 'SvBZyaCOSrc'},
      {'author': 'Hendershot Cowart P.C.',
       'channel': 'Hendershot Cowart P.C.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=-kyDpaMUqFY&t=59s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And so the debtor would have to show that this was, you know, whatever amount '
               'was in the bank account is the exact amount of their current wages. Um, and '
               'then going on, you can get a turnover order, which orders the debtor to turn '
               'over any non-exempt assets.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': 'And so the debtor would have to show that this was, you know, whatever amount '
              'was in the bank account is the exact amount of their current wages. Um, and '
              'then going on, you can get a turnover order, which orders the debtor to turn '
              'over any non-exempt assets.',
       'title': 'Texas Judgment Collection: Tools to Get Paid After You Win (Hendershot Cowart '
                'P.C.)',
       'url': 'https://www.youtube.com/watch?v=-kyDpaMUqFY&t=59s',
       'video_id': '-kyDpaMUqFY'},
      {'author': 'Shergroup TV',
       'channel': 'Shergroup TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:07](https://www.youtube.com/watch?v=aPUKKsyL_NM&t=127s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Our job and we collect your debt we'll charge you 15% better than that if we "
               'look at your terms of business we may be able to help.',
       'timestamp': 127,
       'timestamp_label': '[00:02:07]',
       'timestamp_seconds': 127,
       'tip': "Our job and we collect your debt we'll charge you 15% better than that if we "
              'look at your terms of business we may be able to help.',
       'title': 'CASHFLOW SOLUTIONS | TURN YOUR UNPAID INVOICES AND JUDGMENTS INTO CASH IN THE '
                'BANK (Shergroup TV)',
       'url': 'https://www.youtube.com/watch?v=aPUKKsyL_NM&t=127s',
       'video_id': 'aPUKKsyL_NM'},
      {'author': 'HELPS Law Group',
       'channel': 'HELPS Law Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:37](https://www.youtube.com/watch?v=m3ELQTLjg20&t=157s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um now in most jurisdictions if a person serve with a debtor's exam and they "
               "don't appear at the debtor's exam, the creditor, the attorney representing the "
               'person that has the judgment could file a motion to have that person cited in '
               'contempt of court.',
       'timestamp': 157,
       'timestamp_label': '[00:02:37]',
       'timestamp_seconds': 157,
       'tip': "Um now in most jurisdictions if a person serve with a debtor's exam and they "
              "don't appear at the debtor's exam, the creditor, the attorney representing the "
              'person that has the judgment could file a motion to have that person cited in '
              'contempt of court.',
       'title': "What is a Debtor's Exam? (HELPS Law Group)",
       'url': 'https://www.youtube.com/watch?v=m3ELQTLjg20&t=157s',
       'video_id': 'm3ELQTLjg20'},
      {'author': 'Haber Law',
       'channel': 'Haber Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:20](https://www.youtube.com/watch?v=ZdVZvPMh4qM&t=1040s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Sometimes you can you can hit it big with that too and that allows you to levy '
               'bank accounts you can serve ritz of garnishment.',
       'timestamp': 1040,
       'timestamp_label': '[00:17:20]',
       'timestamp_seconds': 1040,
       'tip': 'Sometimes you can you can hit it big with that too and that allows you to levy '
              'bank accounts you can serve ritz of garnishment.',
       'title': 'Domesticating an Out of State Judgment in The State of Florida (Haber Law)',
       'url': 'https://www.youtube.com/watch?v=ZdVZvPMh4qM&t=1040s',
       'video_id': 'ZdVZvPMh4qM'},
      {'author': 'Alabama Consumer Protection Lawyers',
       'channel': 'Alabama Consumer Protection Lawyers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:59](https://www.youtube.com/watch?v=Ce0D7z4zJFo&t=539s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Something a nice overview of what happens when we sue an abusive debt '
               'collector under the fair debt collection practices I okay guys thanks for '
               "watching this I'll catch you in the next one bye-bye.",
       'timestamp': 539,
       'timestamp_label': '[00:08:59]',
       'timestamp_seconds': 539,
       'tip': 'Something a nice overview of what happens when we sue an abusive debt collector '
              'under the fair debt collection practices I okay guys thanks for watching this '
              "I'll catch you in the next one bye-bye.",
       'title': 'Overview of a typical FDCPA lawsuit against an abusive debt collector '
                '(Alabama Consumer Protection Lawyers)',
       'url': 'https://www.youtube.com/watch?v=Ce0D7z4zJFo&t=539s',
       'video_id': 'Ce0D7z4zJFo'},
      {'author': 'Kitchen Court Cases',
       'channel': 'Kitchen Court Cases',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:31:28](https://www.youtube.com/watch?v=nRWberpO6tg&t=5488s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Picture it didn't happen for which one and okay here we go we are back onto "
               "one speed and he's calling me yelling he starts texting and calling all hours "
               'of the night so we took it to email in January and February.',
       'timestamp': 5488,
       'timestamp_label': '[01:31:28]',
       'timestamp_seconds': 5488,
       'tip': "Picture it didn't happen for which one and okay here we go we are back onto one "
              "speed and he's calling me yelling he starts texting and calling all hours of "
              'the night so we took it to email in January and February.',
       'title': 'Contempt of Court - Civil Court Hearing - Kitchen Court Cases (Kitchen Court '
                'Cases)',
       'url': 'https://www.youtube.com/watch?v=nRWberpO6tg&t=5488s',
       'video_id': 'nRWberpO6tg'},
      {'author': 'Former IRS Agent Representation   4.2M Views',
       'channel': 'Former IRS Agent Representation   4.2M Views',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=go3rRhIEajA&t=38s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So the general statute of limitations on collection cases are 10 years from '
               'the date of the.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': 'So the general statute of limitations on collection cases are 10 years from the '
              'date of the.',
       'title': 'Former IRS Agent Explains The 10 year Statute of Limitations + BEWARE (Former '
                'IRS Agent Representation   4.2M Views)',
       'url': 'https://www.youtube.com/watch?v=go3rRhIEajA&t=38s',
       'video_id': 'go3rRhIEajA'},
      {'author': 'Weston Legal',
       'channel': 'Weston Legal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:57](https://www.youtube.com/watch?v=HD3idZhyATA&t=57s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "How long does a judgment last? Let's say they win the lawsuit. Judgment can "
               'last 20 years in many states. Much longer than the statute of limitations for '
               "a lawsuit. Judgments last a very long time. So, that's the statute of "
               "limitations. Don't just say that's an old debt.",
       'timestamp': 57,
       'timestamp_label': '[00:00:57]',
       'timestamp_seconds': 57,
       'tip': "How long does a judgment last? Let's say they win the lawsuit. Judgment can "
              'last 20 years in many states. Much longer than the statute of limitations for a '
              "lawsuit. Judgments last a very long time. So, that's the statute of "
              "limitations. Don't just say that's an old debt.",
       'title': 'What is the Statute of Limitations? (Weston Legal)',
       'url': 'https://www.youtube.com/watch?v=HD3idZhyATA&t=57s',
       'video_id': 'HD3idZhyATA'},
      {'author': 'Fitzgerald & Campbell, APLC',
       'channel': 'Fitzgerald & Campbell, APLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:56](https://www.youtube.com/watch?v=rSqWVX1naKw&t=116s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Opposing Council and tell them that they have you in custody so you then can '
               'answer the questions so take a judgment de or examination very seriously if '
               "you have one pending against you very wise to talk to a lawyer who's been to "
               'them many times.',
       'timestamp': 116,
       'timestamp_label': '[00:01:56]',
       'timestamp_seconds': 116,
       'tip': 'Opposing Council and tell them that they have you in custody so you then can '
              'answer the questions so take a judgment de or examination very seriously if you '
              "have one pending against you very wise to talk to a lawyer who's been to them "
              'many times.',
       'title': 'What is a Judgment Debtor Examination? (Fitzgerald & Campbell, APLC)',
       'url': 'https://www.youtube.com/watch?v=rSqWVX1naKw&t=116s',
       'video_id': 'rSqWVX1naKw'},
      {'author': 'TheJRInstitute',
       'channel': 'TheJRInstitute',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:53](https://www.youtube.com/watch?v=3p5TZGrk1og&t=593s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Happy hour if you would like more information on how to enroll in the j.r '
               'institute and start your venture in judgment recovery go to our website '
               'wwlp.com we look forward to seeing you next time.',
       'timestamp': 593,
       'timestamp_label': '[00:09:53]',
       'timestamp_seconds': 593,
       'tip': 'Happy hour if you would like more information on how to enroll in the j.r '
              'institute and start your venture in judgment recovery go to our website '
              'wwlp.com we look forward to seeing you next time.',
       'title': 'Judgment Recovery Happy Hour - Freebies (TheJRInstitute)',
       'url': 'https://www.youtube.com/watch?v=3p5TZGrk1og&t=593s',
       'video_id': '3p5TZGrk1og'}],
 11: [{'author': 'Law Office of Richard Kistnen',
       'channel': 'Law Office of Richard Kistnen',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:59](https://www.youtube.com/watch?v=bkM9l8fajkc&t=479s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'A judgment in New York can follow you for up to 20 years, freeze your bank '
               'account, garnish wages, and create serious problems if it becomes a lean on '
               'your home. Bankruptcy can stop collection and discharge the underlying debt, '
               'but timing matters.',
       'timestamp': 479,
       'timestamp_label': '[00:07:59]',
       'timestamp_seconds': 479,
       'tip': 'A judgment in New York can follow you for up to 20 years, freeze your bank '
              'account, garnish wages, and create serious problems if it becomes a lean on '
              'your home. Bankruptcy can stop collection and discharge the underlying debt, '
              'but timing matters.',
       'title': 'Bankruptcy and Judgments in New York: What Happens in 2026? (Law Office of '
                'Richard Kistnen)',
       'url': 'https://www.youtube.com/watch?v=bkM9l8fajkc&t=479s',
       'video_id': 'bkM9l8fajkc'},
      {'author': 'Khan Academy',
       'channel': 'Khan Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:06](https://www.youtube.com/watch?v=mxVWyzzMOXM&t=366s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This debtor will hire one bank. Maybe the management will hire another bank. '
               "And everyone's going to come up with bankruptcy plans. But bankruptcy plans "
               "are usually of one or more varieties. It's essentially just saying, well, we "
               'need to value these assets, right?',
       'timestamp': 366,
       'timestamp_label': '[00:06:06]',
       'timestamp_seconds': 366,
       'tip': 'This debtor will hire one bank. Maybe the management will hire another bank. '
              "And everyone's going to come up with bankruptcy plans. But bankruptcy plans are "
              "usually of one or more varieties. It's essentially just saying, well, we need "
              'to value these assets, right?',
       'title': 'Chapter 11: Bankruptcy restructuring | Stocks and bonds | Finance & Capital '
                'Markets | Khan Academy (Khan Academy)',
       'url': 'https://www.youtube.com/watch?v=mxVWyzzMOXM&t=366s',
       'video_id': 'mxVWyzzMOXM'},
      {'author': 'The Tribe',
       'channel': 'The Tribe',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:28](https://www.youtube.com/watch?v=r1sk4alg3RM&t=388s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The obligation may be here we go a typical commercial or consumer debt. A '
               'plaintiff who has recovered a judgment. Collateral is a plaintiff who has '
               'recovered a judgment. A contractual obligation of another kind.',
       'timestamp': 388,
       'timestamp_label': '[00:06:28]',
       'timestamp_seconds': 388,
       'tip': 'The obligation may be here we go a typical commercial or consumer debt. A '
              'plaintiff who has recovered a judgment. Collateral is a plaintiff who has '
              'recovered a judgment. A contractual obligation of another kind.',
       'title': 'Secured Transactions - Collection of Debts, Liens, and Why Collateral Matters '
                '(The Tribe)',
       'url': 'https://www.youtube.com/watch?v=r1sk4alg3RM&t=388s',
       'video_id': 'r1sk4alg3RM'},
      {'author': 'SeniorLiving.Org',
       'channel': 'SeniorLiving.Org',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:48](https://www.youtube.com/watch?v=9RtU4rpS3pw&t=408s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'For someone who has a lot of medical bills in the clinic or a hospital to have '
               'multiple accounts with a debt collection agency so if you have five.',
       'timestamp': 408,
       'timestamp_label': '[00:06:48]',
       'timestamp_seconds': 408,
       'tip': 'For someone who has a lot of medical bills in the clinic or a hospital to have '
              'multiple accounts with a debt collection agency so if you have five.',
       'title': "Regulation F: New Debt Collection Laws You Need to Know Even if You're not in "
                'Debt (SeniorLiving.Org)',
       'url': 'https://www.youtube.com/watch?v=9RtU4rpS3pw&t=408s',
       'video_id': '9RtU4rpS3pw'},
      {'author': 'People Locator Skip Tracing',
       'channel': 'People Locator Skip Tracing',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:04](https://www.youtube.com/watch?v=nwM1K55PtXM&t=64s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Financial disclosures, deposition testimony, and court filings from prior '
               'cases, divorce proceedings, bankruptcy filings, prior collections matters, '
               "often contain the debtor's own sworn statements about assets and income.",
       'timestamp': 64,
       'timestamp_label': '[00:01:04]',
       'timestamp_seconds': 64,
       'tip': 'Financial disclosures, deposition testimony, and court filings from prior '
              'cases, divorce proceedings, bankruptcy filings, prior collections matters, '
              "often contain the debtor's own sworn statements about assets and income.",
       'title': 'How to Prepare Debtor Examination (People Locator Skip Tracing)',
       'url': 'https://www.youtube.com/watch?v=nwM1K55PtXM&t=64s',
       'video_id': 'nwM1K55PtXM'},
      {'author': 'The National Law Review',
       'channel': 'The National Law Review',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:18](https://www.youtube.com/watch?v=aQwpKSW3PEA&t=198s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And then there's the Enron view, which drew a distinction between a sale of a "
               "claim and an assignment of a claim. I think that's a very fine, nuanced "
               'distinction, but the court was of the view that a a a sale severed the '
               'infirmity from the the claim and the buyer.',
       'timestamp': 198,
       'timestamp_label': '[00:03:18]',
       'timestamp_seconds': 198,
       'tip': "And then there's the Enron view, which drew a distinction between a sale of a "
              "claim and an assignment of a claim. I think that's a very fine, nuanced "
              'distinction, but the court was of the view that a a a sale severed the '
              'infirmity from the the claim and the buyer.',
       'title': 'Bankruptcy Claims Trading Risks (The National Law Review)',
       'url': 'https://www.youtube.com/watch?v=aQwpKSW3PEA&t=198s',
       'video_id': 'aQwpKSW3PEA'},
      {'author': 'Hard Hat Economics',
       'channel': 'Hard Hat Economics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:37](https://www.youtube.com/watch?v=-FdK6kbQiio&t=457s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Button to join the channel for updates and let's continue the discussion in "
               'the comments section below let me know what you think about the collection '
               "agency business opportunity and we'll see you next time.",
       'timestamp': 457,
       'timestamp_label': '[00:07:37]',
       'timestamp_seconds': 457,
       'tip': "Button to join the channel for updates and let's continue the discussion in the "
              'comments section below let me know what you think about the collection agency '
              "business opportunity and we'll see you next time.",
       'title': 'How This Guy Started an $80k / Month Debt Collection Service (Hard Hat '
                'Economics)',
       'url': 'https://www.youtube.com/watch?v=-FdK6kbQiio&t=457s',
       'video_id': '-FdK6kbQiio'},
      {'author': 'Snellings Law LLC',
       'channel': 'Snellings Law LLC',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:07](https://www.youtube.com/watch?v=W1XbSRwt1D8&t=67s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Creditor filing the judgment in the home state and then the judgment will be '
               'treated as if a court in that state made the judgment after the filing the '
               'judgment will then be served on the debtor and the home state court can '
               'enforce the judgment.',
       'timestamp': 67,
       'timestamp_label': '[00:01:07]',
       'timestamp_seconds': 67,
       'tip': 'Creditor filing the judgment in the home state and then the judgment will be '
              'treated as if a court in that state made the judgment after the filing the '
              'judgment will then be served on the debtor and the home state court can enforce '
              'the judgment.',
       'title': 'How to Enforce a Foreign Judgment (Snellings Law LLC)',
       'url': 'https://www.youtube.com/watch?v=W1XbSRwt1D8&t=67s',
       'video_id': 'W1XbSRwt1D8'},
      {'author': 'Law Office of Jeffrey B. Kelly',
       'channel': 'Law Office of Jeffrey B. Kelly',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:48](https://www.youtube.com/watch?v=cHsptp1ujiI&t=48s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "That's why we we have a pretty high bankruptcy filing rate because it's "
               'honestly the fastest way to stop them from doing it. They can also clean out '
               'your checking account or clean out your savings account up to the amount of '
               'the debt owed.',
       'timestamp': 48,
       'timestamp_label': '[00:00:48]',
       'timestamp_seconds': 48,
       'tip': "That's why we we have a pretty high bankruptcy filing rate because it's "
              'honestly the fastest way to stop them from doing it. They can also clean out '
              'your checking account or clean out your savings account up to the amount of the '
              'debt owed.',
       'title': 'Wage Garnishment in Georgia - How Much Can They Take and How Do You Stop It? '
                '(Law Office of Jeffrey B. Kelly)',
       'url': 'https://www.youtube.com/watch?v=cHsptp1ujiI&t=48s',
       'video_id': 'cHsptp1ujiI'},
      {'author': 'Alabama Consumer Protection Lawyers',
       'channel': 'Alabama Consumer Protection Lawyers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=z04uhB8lcJU&t=15s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Fair debt collection practices i specifically covering debt collectors which '
               'would include eviction lawyers who are involved in evicting people due.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Fair debt collection practices i specifically covering debt collectors which '
              'would include eviction lawyers who are involved in evicting people due.',
       'title': 'Breaking news! FDCPA liability in evictions (CDC Order) (Alabama Consumer '
                'Protection Lawyers)',
       'url': 'https://www.youtube.com/watch?v=z04uhB8lcJU&t=15s',
       'video_id': 'z04uhB8lcJU'},
      {'author': 'Juris Wire',
       'channel': 'Juris Wire',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:44](https://www.youtube.com/watch?v=xCHuZoPk7vA&t=284s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I would also ask that an order enter regarding discovery if all of these items '
               "that he's holding on to are intended to be used as exhibits at the trial. Uh I "
               'would like to have copies of those so that we can be prepared.',
       'timestamp': 284,
       'timestamp_label': '[00:04:44]',
       'timestamp_seconds': 284,
       'tip': 'I would also ask that an order enter regarding discovery if all of these items '
              "that he's holding on to are intended to be used as exhibits at the trial. Uh I "
              'would like to have copies of those so that we can be prepared.',
       'title': 'Sovereign Citizen Refuses to Follow Court Rules — Judge Sends Him Straight to '
                'Jail! (Juris Wire)',
       'url': 'https://www.youtube.com/watch?v=xCHuZoPk7vA&t=284s',
       'video_id': 'xCHuZoPk7vA'},
      {'author': 'Brandon Weaver',
       'channel': 'Brandon Weaver',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:25](https://www.youtube.com/watch?v=iHnRz6R1jS8&t=85s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Because a lot of these debt collectors these debt scavengers don't have this "
               "information and they're trying to get quick default judgment and garnish your.",
       'timestamp': 85,
       'timestamp_label': '[00:01:25]',
       'timestamp_seconds': 85,
       'tip': "Because a lot of these debt collectors these debt scavengers don't have this "
              "information and they're trying to get quick default judgment and garnish your.",
       'title': 'Stop Wage Garnishment? Appeal Judgments? || Live Debt Free || Good Credit '
                'Good Life (Brandon Weaver)',
       'url': 'https://www.youtube.com/watch?v=iHnRz6R1jS8&t=85s',
       'video_id': 'iHnRz6R1jS8'},
      {'author': 'Former IRS Agent Representation   4.2M Views',
       'channel': 'Former IRS Agent Representation   4.2M Views',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:41](https://www.youtube.com/watch?v=0jHEJqFcgLA&t=101s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Time it was an offer status if you file a bankruptcy it will extend the time '
               'it was in bankruptcy if you applied for a taxpayer.',
       'timestamp': 101,
       'timestamp_label': '[00:01:41]',
       'timestamp_seconds': 101,
       'tip': 'Time it was an offer status if you file a bankruptcy it will extend the time it '
              'was in bankruptcy if you applied for a taxpayer.',
       'title': 'Can IRS Extend My 10 Year Statue Of Limitation, What Events Toll The IRS '
                'Statute Former IRS Explains (Former IRS Agent Representation   4.2M Views)',
       'url': 'https://www.youtube.com/watch?v=0jHEJqFcgLA&t=101s',
       'video_id': '0jHEJqFcgLA'},
      {'author': 'ShadowAnyone',
       'channel': 'ShadowAnyone',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:38](https://www.youtube.com/watch?v=esyMX8o3OR0&t=338s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Over if you have any questions let me know I'll answer all that I can in the "
               'meantime this is Larry K with shadowanyone.com remember do the right thing '
               "even if it's the hard thing.",
       'timestamp': 338,
       'timestamp_label': '[00:05:38]',
       'timestamp_seconds': 338,
       'tip': "Over if you have any questions let me know I'll answer all that I can in the "
              'meantime this is Larry K with shadowanyone.com remember do the right thing even '
              "if it's the hard thing.",
       'title': 'How to open a free PACER account to find federal criminal and bankruptcy '
                'public records. OSINT gold! (ShadowAnyone)',
       'url': 'https://www.youtube.com/watch?v=esyMX8o3OR0&t=338s',
       'video_id': 'esyMX8o3OR0'},
      {'author': 'Thomas Higgins Limited',
       'channel': 'Thomas Higgins Limited',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:37](https://www.youtube.com/watch?v=MxMjZqkhltA&t=37s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So what's the difference between commercial and consumer debt? In simple "
               'terms, commercial debt occurs between two businesses. Whereas consumer debt '
               'involves an individual owing money to a business.',
       'timestamp': 37,
       'timestamp_label': '[00:00:37]',
       'timestamp_seconds': 37,
       'tip': "So what's the difference between commercial and consumer debt? In simple terms, "
              'commercial debt occurs between two businesses. Whereas consumer debt involves '
              'an individual owing money to a business.',
       'title': 'Thomas Higgins Limited - What Is the Process of Commercial Debt Collection? '
                '(Thomas Higgins Limited)',
       'url': 'https://www.youtube.com/watch?v=MxMjZqkhltA&t=37s',
       'video_id': 'MxMjZqkhltA'}],
 12: [{'author': 'WealthCurve',
       'channel': 'WealthCurve',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:53](https://www.youtube.com/watch?v=cKYmFnf_o2Q&t=173s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Your 30-day window is the most powerful 30 days in consumer law, and it starts '
               'when you receive the validation notice. If you send a written dispute within '
               'that window, the collector must stop all collection activity.',
       'timestamp': 173,
       'timestamp_label': '[00:02:53]',
       'timestamp_seconds': 173,
       'tip': 'Your 30-day window is the most powerful 30 days in consumer law, and it starts '
              'when you receive the validation notice. If you send a written dispute within '
              'that window, the collector must stop all collection activity.',
       'title': 'Debt Collectors: Know Your Rights Before You Pay a Dollar 🛡️ (WealthCurve)',
       'url': 'https://www.youtube.com/watch?v=cKYmFnf_o2Q&t=173s',
       'video_id': 'cKYmFnf_o2Q'},
      {'author': 'Night Ferry',
       'channel': 'Night Ferry',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:24](https://www.youtube.com/watch?v=7HVra7o-cZg&t=204s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Under Regulation F, the federal debt collection rule, more than 7 calls about '
               'a debt within 7 days is presumed to break the law. Rings and voicemails count. '
               "Thursday's ringing call makes 6; a busy signal that day doesn't count.",
       'timestamp': 204,
       'timestamp_label': '[00:03:24]',
       'timestamp_seconds': 204,
       'tip': 'Under Regulation F, the federal debt collection rule, more than 7 calls about a '
              'debt within 7 days is presumed to break the law. Rings and voicemails count. '
              "Thursday's ringing call makes 6; a busy signal that day doesn't count.",
       'title': "Debt Collector Rights: What They Can and Can't Do (Night Ferry)",
       'url': 'https://www.youtube.com/watch?v=7HVra7o-cZg&t=204s',
       'video_id': '7HVra7o-cZg'},
      {'author': 'Cross the River, Find the Treasure',
       'channel': 'Cross the River, Find the Treasure',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:25](https://www.youtube.com/watch?v=Ss8eyzh_cQ8&t=25s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Recover one's rightful money with a civil small claims lawsuit or start a "
               'lucrative work from home business unlike internet marketing schemes where very '
               'few succeed here Anyone who puts in the work will prosper.',
       'timestamp': 25,
       'timestamp_label': '[00:00:25]',
       'timestamp_seconds': 25,
       'tip': "Recover one's rightful money with a civil small claims lawsuit or start a "
              'lucrative work from home business unlike internet marketing schemes where very '
              'few succeed here Anyone who puts in the work will prosper.',
       'title': 'Judgment Recover Business Training Course (Cross the River, Find the '
                'Treasure)',
       'url': 'https://www.youtube.com/watch?v=Ss8eyzh_cQ8&t=25s',
       'video_id': 'Ss8eyzh_cQ8'},
      {'author': 'Solo – Resolve Your Debt',
       'channel': 'Solo – Resolve Your Debt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:53:09](https://www.youtube.com/watch?v=n3SZjPQDSHc&t=3189s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I mean they're going to hit your account, your bank account on the 2nd of the "
               "month, a day after you got paid. That's when they're going to go take your "
               "money. And you you've got rent and your other bills to pay, so that that could "
               'be a very stressful.',
       'timestamp': 3189,
       'timestamp_label': '[00:53:09]',
       'timestamp_seconds': 3189,
       'tip': "I mean they're going to hit your account, your bank account on the 2nd of the "
              "month, a day after you got paid. That's when they're going to go take your "
              "money. And you you've got rent and your other bills to pay, so that that could "
              'be a very stressful.',
       'title': 'The Fair Debt Collection Practices Act Explained by an Attorney (Solo – '
                'Resolve Your Debt)',
       'url': 'https://www.youtube.com/watch?v=n3SZjPQDSHc&t=3189s',
       'video_id': 'n3SZjPQDSHc'},
      {'author': 'Receivables Info | Debt Collection News',
       'channel': 'Receivables Info | Debt Collection News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:07](https://www.youtube.com/watch?v=9VNthZZ6JNk&t=547s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And let's just say that that consumer has had enough and they don't want to "
               "talk to us anymore and they say no, okay? Because they've had enough. They "
               'they they want the next seven days to be free. However, what they forgot about '
               "is that there's a court hearing tomorrow.",
       'timestamp': 547,
       'timestamp_label': '[00:09:07]',
       'timestamp_seconds': 547,
       'tip': "And let's just say that that consumer has had enough and they don't want to "
              "talk to us anymore and they say no, okay? Because they've had enough. They they "
              'they want the next seven days to be free. However, what they forgot about is '
              "that there's a court hearing tomorrow.",
       'title': 'What a New Bill in Congress Means for Collection Attorney Litigation | Ep. '
                '271 (Receivables Info | Debt Collection News)',
       'url': 'https://www.youtube.com/watch?v=9VNthZZ6JNk&t=547s',
       'video_id': '9VNthZZ6JNk'},
      {'author': 'Calhoun School of Law',
       'channel': 'Calhoun School of Law',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=ObrPaCTQ6ZQ&t=78s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can even start the enforcement processes the day after that appellate time '
               'frame is exhausted The way you go about enforcing a judgment is pretty well up '
               'to you. The court is fairly well hands-off whenever it comes to collecting '
               'judgments.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': 'You can even start the enforcement processes the day after that appellate time '
              'frame is exhausted The way you go about enforcing a judgment is pretty well up '
              'to you. The court is fairly well hands-off whenever it comes to collecting '
              'judgments.',
       'title': 'How to Collect Judgment. #Law #history #facts (Calhoun School of Law)',
       'url': 'https://www.youtube.com/watch?v=ObrPaCTQ6ZQ&t=78s',
       'video_id': 'ObrPaCTQ6ZQ'},
      {'author': 'Steve Vondran',
       'channel': 'Steve Vondran',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:14](https://www.youtube.com/watch?v=qlw161ht_Kw&t=374s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Parties get together you have this joint report you get together and you you '
               "set times and days for your discovery i'll give.",
       'timestamp': 374,
       'timestamp_label': '[00:06:14]',
       'timestamp_seconds': 374,
       'tip': 'Parties get together you have this joint report you get together and you you '
              "set times and days for your discovery i'll give.",
       'title': 'How to review a Federal Court Docket by Attorney Steve (Steve Vondran)',
       'url': 'https://www.youtube.com/watch?v=qlw161ht_Kw&t=374s',
       'video_id': 'qlw161ht_Kw'},
      {'author': 'surplusfundswealth1',
       'channel': 'surplusfundswealth1',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:43](https://www.youtube.com/watch?v=ML9MBLDQFHY&t=223s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Estate where we can go after estate money as well here in the next week or two '
               "appreciate your time taking a look at the video guys it's a lot of money and "
               "we are halfway to our goal of being completely National we'd love for you to "
               'be on the team have a great day.',
       'timestamp': 223,
       'timestamp_label': '[00:03:43]',
       'timestamp_seconds': 223,
       'tip': 'Estate where we can go after estate money as well here in the next week or two '
              "appreciate your time taking a look at the video guys it's a lot of money and we "
              "are halfway to our goal of being completely National we'd love for you to be on "
              'the team have a great day.',
       'title': 'Why This is Better than Judgment Recovery Business Training Courses **Free '
                'Download (surplusfundswealth1)',
       'url': 'https://www.youtube.com/watch?v=ML9MBLDQFHY&t=223s',
       'video_id': 'ML9MBLDQFHY'},
      {'author': 'Bob Jablonsky',
       'channel': 'Bob Jablonsky',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:27](https://www.youtube.com/watch?v=KU5hNE5Z2MU&t=207s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Is on that day the purpose here is that it just it wouldn't be fair if the "
               'taxpayer could I just keep filing bankruptcy or keep making offers that.',
       'timestamp': 207,
       'timestamp_label': '[00:03:27]',
       'timestamp_seconds': 207,
       'tip': "Is on that day the purpose here is that it just it wouldn't be fair if the "
              'taxpayer could I just keep filing bankruptcy or keep making offers that.',
       'title': 'Why the IRS 10 Year Statute of Limitations is Critical if you have Tax Debt! '
                '(Bob Jablonsky)',
       'url': 'https://www.youtube.com/watch?v=KU5hNE5Z2MU&t=207s',
       'video_id': 'KU5hNE5Z2MU'},
      {'author': 'Plain Finance',
       'channel': 'Plain Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:53](https://www.youtube.com/watch?v=i54UmAtM9Y0&t=413s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '160,000, wired within the week, good until Friday at 5. You take the number to '
               'a diner counter and do the arithmetic on the back of the receipt. 2 million in '
               'ordinary claims, roughly 39% of the pool.',
       'timestamp': 413,
       'timestamp_label': '[00:06:53]',
       'timestamp_seconds': 413,
       'tip': '160,000, wired within the week, good until Friday at 5. You take the number to '
              'a diner counter and do the arithmetic on the back of the receipt. 2 million in '
              'ordinary claims, roughly 39% of the pool.',
       'title': 'You Bought a Worthless Bankruptcy Claim for $2,400. Three Years Later, It '
                'Paid $1.4 Million. (Plain Finance)',
       'url': 'https://www.youtube.com/watch?v=i54UmAtM9Y0&t=413s',
       'video_id': 'i54UmAtM9Y0'},
      {'author': 'Law Frog RN, Esq.',
       'channel': 'Law Frog RN, Esq.',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:42](https://www.youtube.com/watch?v=NL1hJNjxmU4&t=282s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Every plaintiff must be a citizen of a different state from every defendant '
               'across opposing sides of the lawsuit. Diversity of citizenship and amount in '
               'controversy are measured strictly at the exact moment the complaint is filed '
               'in federal court.',
       'timestamp': 282,
       'timestamp_label': '[00:04:42]',
       'timestamp_seconds': 282,
       'tip': 'Every plaintiff must be a citizen of a different state from every defendant '
              'across opposing sides of the lawsuit. Diversity of citizenship and amount in '
              'controversy are measured strictly at the exact moment the complaint is filed in '
              'federal court.',
       'title': 'Civil Procedure Statutes, Rules & Definitions | 91 Flashcards for 1L | Law '
                'Frog RN, Esq. (Law Frog RN, Esq.)',
       'url': 'https://www.youtube.com/watch?v=NL1hJNjxmU4&t=282s',
       'video_id': 'NL1hJNjxmU4'},
      {'author': 'Law Accent',
       'channel': 'Law Accent',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:07](https://www.youtube.com/watch?v=vhXnhEvki3E&t=427s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Leave a comment don't forget to share don't forget to ask questions if you "
               "have any and don't forget to join us on another episode on accent litigation "
               'my name is isaac and I will see you next week.',
       'timestamp': 427,
       'timestamp_label': '[00:07:07]',
       'timestamp_seconds': 427,
       'tip': "Leave a comment don't forget to share don't forget to ask questions if you have "
              "any and don't forget to join us on another episode on accent litigation my name "
              'is isaac and I will see you next week.',
       'title': 'HOW TO ENFORCE JUDGEMENT: JUDGEMENT SUMMONS (Law Accent)',
       'url': 'https://www.youtube.com/watch?v=vhXnhEvki3E&t=427s',
       'video_id': 'vhXnhEvki3E'},
      {'author': 'Hanna Hasl-Kelchner',
       'channel': 'Hanna Hasl-Kelchner',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:44](https://www.youtube.com/watch?v=ha0J206Xt6k&t=704s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You can hold over their head to encourage them to settle well that definitely '
               "sounds like a plan I've also heard of people saying show me your key ring and "
               'then explain what every key opens I guess that could be another another '
               'shortcut.',
       'timestamp': 704,
       'timestamp_label': '[00:11:44]',
       'timestamp_seconds': 704,
       'tip': 'You can hold over their head to encourage them to settle well that definitely '
              "sounds like a plan I've also heard of people saying show me your key ring and "
              'then explain what every key opens I guess that could be another another '
              'shortcut.',
       'title': 'How to Improve Your Judgment Recovery Success Rate with Joe Dickerson (Hanna '
                'Hasl-Kelchner)',
       'url': 'https://www.youtube.com/watch?v=ha0J206Xt6k&t=704s',
       'video_id': 'ha0J206Xt6k'},
      {'author': 'Sacramento County Public Law Library',
       'channel': 'Sacramento County Public Law Library',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:53](https://www.youtube.com/watch?v=bX8Hhszjuxs&t=293s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So was always kind of a good way that if I didn't know where they were anymore "
               'at least I used to know who lived next to store to them and it was a good '
               'place to start you know and just a nice polite inquiry may not get you '
               'anywhere but you never.',
       'timestamp': 293,
       'timestamp_label': '[00:04:53]',
       'timestamp_seconds': 293,
       'tip': "So was always kind of a good way that if I didn't know where they were anymore "
              'at least I used to know who lived next to store to them and it was a good place '
              'to start you know and just a nice polite inquiry may not get you anywhere but '
              'you never.',
       'title': 'Enforcement of Judgments: Part 1: Introduction (Sacramento County Public Law '
                'Library)',
       'url': 'https://www.youtube.com/watch?v=bX8Hhszjuxs&t=293s',
       'video_id': 'bX8Hhszjuxs'},
      {'author': 'Santiago Cueto | Miami Business Litigation Lawyer',
       'channel': 'Santiago Cueto | Miami Business Litigation Lawyer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:34](https://www.youtube.com/watch?v=W9UHSaFUIn8&t=454s)',
       'relevance': 'Attributed practitioner commentary on commercial post-judgment recovery, '
                    'docket screening, lawful assignment/attorney enforcement, and lien '
                    'priority (Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But it is absolutely possible. I have recovered money from accounts in '
               'Switzerland, the Cayman Islands, and beyond. Now let me talk about something '
               'that no one discusses. The psychology of debt collection. Most debtors are not '
               'criminal masterminds.',
       'timestamp': 454,
       'timestamp_label': '[00:07:34]',
       'timestamp_seconds': 454,
       'tip': 'But it is absolutely possible. I have recovered money from accounts in '
              'Switzerland, the Cayman Islands, and beyond. Now let me talk about something '
              'that no one discusses. The psychology of debt collection. Most debtors are not '
              'criminal masterminds.',
       'title': "Judgment-Proof Debtor THINKS They're Safe | Here's Why They're Wrong "
                '(Santiago Cueto | Miami Business Litigation Lawyer)',
       'url': 'https://www.youtube.com/watch?v=W9UHSaFUIn8&t=454s',
       'video_id': 'W9UHSaFUIn8'}]}
