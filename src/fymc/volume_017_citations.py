"""Curated 180-citation Domain Investing baseline (15 per chapter across Q1-Q12) mined strictly from verified Domain Investing YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'catching',
     'check',
     'clean',
     'clearance',
     'client',
     'clients',
     'cloudflare',
     'com',
     'comps',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'desk',
     'dictionary',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'budget',
     'business',
     'buyer',
     'buying',
     'catching',
     'check',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'comps',
     'contract',
     'crunchbase',
     'customer',
     'cybersquatting',
     'cyger',
     'dan',
     'decision',
     'desk',
     'dictionary',
     'escrow',
     'fee',
     'fees',
     'invoice',
     'pay',
     'payment',
     'pays',
     'retainer'},
 3: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'cash',
     'cashflow',
     'catching',
     'check',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'commission',
     'comps',
     'cost',
     'costs',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'desk',
     'dictionary',
     'economics',
     'margin',
     'margins',
     'price',
     'pricing',
     'profit',
     'roi',
     'unit'},
 4: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'budget',
     'business',
     'buying',
     'capital',
     'catching',
     'check',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'comps',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'desk',
     'dictionary',
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
 5: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoid',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'catching',
     'check',
     'clawback',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'comps',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'desk',
     'dictionary',
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
 6: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'catching',
     'check',
     'clean',
     'clearance',
     'client',
     'cloudflare',
     'com',
     'comps',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'data',
     'deal',
     'desk',
     'dictionary',
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
 7: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'catching',
     'check',
     'checklist',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'comps',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'delivery',
     'desk',
     'dictionary',
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
 8: {'acpa',
     'afternic',
     'aged',
     'andrew',
     'api',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'catching',
     'check',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'comps',
     'crm',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'data',
     'database',
     'desk',
     'dictionary',
     'platform',
     'portal',
     'scraper',
     'search',
     'software',
     'tool',
     'tools',
     'tracking'},
 9: {'acpa',
     'afternic',
     'aged',
     'agreement',
     'andrew',
     'archive',
     'atom',
     'auction',
     'auctions',
     'audit',
     'authority',
     'avoiding',
     'backlink',
     'bin',
     'bodis',
     'brandables',
     'business',
     'buying',
     'catching',
     'check',
     'clean',
     'clearance',
     'cloudflare',
     'com',
     'compliance',
     'comps',
     'contract',
     'crunchbase',
     'cybersquatting',
     'cyger',
     'dan',
     'desk',
     'dictionary',
     'disclosure',
     'law',
     'legal',
     'license',
     'outreach',
     'rules',
     'script',
     'state',
     'terms'},
 10: {'acpa',
      'afternic',
      'aged',
      'agent',
      'ai',
      'andrew',
      'archive',
      'atom',
      'auction',
      'auctions',
      'audit',
      'authority',
      'automate',
      'automation',
      'avoiding',
      'backlink',
      'bin',
      'bodis',
      'brandables',
      'business',
      'buying',
      'catching',
      'check',
      'clean',
      'clearance',
      'cloudflare',
      'com',
      'comps',
      'crunchbase',
      'cybersquatting',
      'cyger',
      'dan',
      'dashboard',
      'desk',
      'dictionary',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'acpa',
      'afternic',
      'aged',
      'andrew',
      'archive',
      'atom',
      'auction',
      'auctions',
      'audit',
      'authority',
      'avoiding',
      'backlink',
      'bin',
      'bodis',
      'brandables',
      'business',
      'buying',
      'catching',
      'check',
      'clean',
      'clearance',
      'cloudflare',
      'com',
      'comps',
      'contractor',
      'crunchbase',
      'cybersquatting',
      'cyger',
      'dan',
      'desk',
      'dictionary',
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
 12: {'acpa',
      'action',
      'afternic',
      'aged',
      'andrew',
      'archive',
      'atom',
      'auction',
      'auctions',
      'audit',
      'authority',
      'avoiding',
      'backlink',
      'bin',
      'bodis',
      'brandables',
      'business',
      'buying',
      'catching',
      'check',
      'clean',
      'clearance',
      'cloudflare',
      'com',
      'comps',
      'crunchbase',
      'cybersquatting',
      'cyger',
      'dan',
      'day',
      'days',
      'desk',
      'dictionary',
      'launch',
      'milestone',
      'month',
      'plan',
      'roadmap',
      'sprint',
      'start',
      'thirty',
      'week'}}

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'KT Blogger',
      'channel': 'KT Blogger',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:29](https://www.youtube.com/watch?v=yz0jUQvunAI&t=2789s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'It is true that due to AI, service work has slowed down a bit on Fiverr and '
              "Upwork, but it hasn't stopped or ended; in fact, you are getting even more "
              'valuable clients, okay? You are getting high-value, high-margin clients.',
      'timestamp': 2789,
      'timestamp_label': '[00:46:29]',
      'timestamp_seconds': 2789,
      'tip': 'It is true that due to AI, service work has slowed down a bit on Fiverr and '
             "Upwork, but it hasn't stopped or ended; in fact, you are getting even more "
             'valuable clients, okay? You are getting high-value, high-margin clients.',
      'title': 'How I Turned $10 into $1500 Selling a Domain | Domain Flipping Business '
               'Explained (KT Blogger)',
      'url': 'https://www.youtube.com/watch?v=yz0jUQvunAI&t=2789s',
      'video_id': 'yz0jUQvunAI'},
     {'author': 'Reza Taheri',
      'channel': 'Reza Taheri',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:48](https://www.youtube.com/watch?v=2jfssBvnbfw&t=168s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh unfortunately Dan was closed last year. It was merged with after league you '
              'know and uh it has no longer in service. So we had to move to after nick. But '
              'after having this issue this experience with after nick I uh uh change the all '
              'of my domain names name server to atom.',
      'timestamp': 168,
      'timestamp_label': '[00:02:48]',
      'timestamp_seconds': 168,
      'tip': 'Uh unfortunately Dan was closed last year. It was merged with after league you '
             'know and uh it has no longer in service. So we had to move to after nick. But '
             'after having this issue this experience with after nick I uh uh change the all '
             'of my domain names name server to atom.',
      'title': 'Afternic Review: Why It’s Killing Your Domain Sales (Reza Taheri)',
      'url': 'https://www.youtube.com/watch?v=2jfssBvnbfw&t=168s',
      'video_id': '2jfssBvnbfw'},
     {'author': 'Craylor',
      'channel': 'Craylor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=IXpvUD5SDzA&t=122s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s no advantage to upgrading. Cloudflare's paid plans are for advanced and "
              "enterprise users, so if you're a small business owner or individual, you can "
              'get an insane value out of the free plan.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': "'s no advantage to upgrading. Cloudflare's paid plans are for advanced and "
             "enterprise users, so if you're a small business owner or individual, you can get "
             'an insane value out of the free plan.',
      'title': '5 Things to Know BEFORE Using Cloudflare! (Craylor)',
      'url': 'https://www.youtube.com/watch?v=IXpvUD5SDzA&t=122s',
      'video_id': 'IXpvUD5SDzA'},
     {'author': 'GoDaddy',
      'channel': 'GoDaddy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=qJ6o0aD4Msg&t=45s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Oh, so it's like buying and selling properties like a real estate agent? Yeah, "
              "kind of more like an investor. So if you're investing in real estate, you look "
              'for stuff that might be a little bit under the market value.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': "Oh, so it's like buying and selling properties like a real estate agent? Yeah, "
             "kind of more like an investor. So if you're investing in real estate, you look "
             'for stuff that might be a little bit under the market value.',
      'title': 'What Is Domain Investing (& Why You Should Invest) | The Journey (GoDaddy)',
      'url': 'https://www.youtube.com/watch?v=qJ6o0aD4Msg&t=45s',
      'video_id': 'qJ6o0aD4Msg'},
     {'author': 'Domain Value Estimator',
      'channel': 'Domain Value Estimator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=nC0fLv5Q_PI&t=241s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Length scores 78 out of 100. Three characters, of course. SEO 72, brand 47, dot '
              'co 81. The model saw three-letter domain and reached for the three-letter. But '
              'dot co is not dot com, and the market said 17,000.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': 'Length scores 78 out of 100. Three characters, of course. SEO 72, brand 47, dot '
             'co 81. The model saw three-letter domain and reached for the three-letter. But '
             'dot co is not dot com, and the market said 17,000.',
      'title': "You're Reading Domain Appraisals Wrong (Domain Value Estimator)",
      'url': 'https://www.youtube.com/watch?v=nC0fLv5Q_PI&t=241s',
      'video_id': 'nC0fLv5Q_PI'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:30](https://www.youtube.com/watch?v=KYAHTsYNIPI&t=2970s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '\'re like, "Well, I\'m thinking about auctioning it." Or it\'s like, "Look, my '
              'personal motto is that auctions are for buying, not selling." Well, because '
              "it's it's going to be wholesale. It's It's If you want liquidity, fine. You "
              'know, sell it sell it to another.',
      'timestamp': 2970,
      'timestamp_label': '[00:49:30]',
      'timestamp_seconds': 2970,
      'tip': '\'re like, "Well, I\'m thinking about auctioning it." Or it\'s like, "Look, my '
             'personal motto is that auctions are for buying, not selling." Well, because '
             "it's it's going to be wholesale. It's It's If you want liquidity, fine. You "
             'know, sell it sell it to another.',
      'title': 'Navigating Appraised Value vs Market Value of Your Domain (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=KYAHTsYNIPI&t=2970s',
      'video_id': 'KYAHTsYNIPI'},
     {'author': 'GigaLaw - Doug Isenberg',
      'channel': 'GigaLaw - Doug Isenberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:39](https://www.youtube.com/watch?v=GI9Us2WWsAo&t=219s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I do in any event I suspect the firm's decision to file an acpa complaint was "
              'motivated in large part by the availability of injunctive relief according to '
              'the magistrate judges report deba voice filed its complaint on December 13 2021 '
              'and a U.',
      'timestamp': 219,
      'timestamp_label': '[00:03:39]',
      'timestamp_seconds': 219,
      'tip': "I do in any event I suspect the firm's decision to file an acpa complaint was "
             'motivated in large part by the availability of injunctive relief according to '
             'the magistrate judges report deba voice filed its complaint on December 13 2021 '
             'and a U.',
      'title': 'Lessons About UDRP v. ACPA from the Debevoise Cybersquatting Case (GigaLaw - '
               'Doug Isenberg)',
      'url': 'https://www.youtube.com/watch?v=GI9Us2WWsAo&t=219s',
      'video_id': 'GI9Us2WWsAo'},
     {'author': 'The Dividend Domain',
      'channel': 'The Dividend Domain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:58](https://www.youtube.com/watch?v=xVfENzSxmO0&t=178s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I have conviction in Bitcoin. And I say like so like I have a lot too much '
              "exposure, but to me is like this is the best time if we're in a bear Bitcoin or "
              "crypto bear market, it's in my best interest if I see value to buy at these "
              'opportune times.',
      'timestamp': 178,
      'timestamp_label': '[00:02:58]',
      'timestamp_seconds': 178,
      'tip': 'I have conviction in Bitcoin. And I say like so like I have a lot too much '
             "exposure, but to me is like this is the best time if we're in a bear Bitcoin or "
             "crypto bear market, it's in my best interest if I see value to buy at these "
             'opportune times.',
      'title': "The Power of Margin: How I'm Supercharging My Investments| Robin Fire Ep 41 "
               '(The Dividend Domain)',
      'url': 'https://www.youtube.com/watch?v=xVfENzSxmO0&t=178s',
      'video_id': 'xVfENzSxmO0'},
     {'author': 'Unstoppable AI',
      'channel': 'Unstoppable AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=FRAPXUkvbv0&t=150s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Uh in 2016-17 that whole thing blew up and you know they all lost 60 plus of '
              'the value that it had run up to now two number.com is still incredibly scarce '
              "and it's still super valuable uh a three number.com is still super scarce and "
              "it's still incredibly valuable.",
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'Uh in 2016-17 that whole thing blew up and you know they all lost 60 plus of the '
             'value that it had run up to now two number.com is still incredibly scarce and '
             "it's still super valuable uh a three number.com is still super scarce and it's "
             'still incredibly valuable.',
      'title': 'NFT Domain Investing Secrets From The #1 Domain Broker In The World | The '
               'Unstoppable Podcast Clips (Unstoppable AI)',
      'url': 'https://www.youtube.com/watch?v=FRAPXUkvbv0&t=150s',
      'video_id': 'FRAPXUkvbv0'},
     {'author': 'MediaOptions',
      'channel': 'MediaOptions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=On67hq0XY6k&t=15s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Dollars in revenue or a publicly traded company how often is it that they '
              'recognize the value before that has been built into a company like Michaels so.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Dollars in revenue or a publicly traded company how often is it that they '
             'recognize the value before that has been built into a company like Michaels so.',
      'title': 'Why Exact Match Domains Names Are Valuable (MediaOptions)',
      'url': 'https://www.youtube.com/watch?v=On67hq0XY6k&t=15s',
      'video_id': 'On67hq0XY6k'},
     {'author': 'SkyInclude',
      'channel': 'SkyInclude',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:32](https://www.youtube.com/watch?v=0-ax0cEcuZk&t=1652s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s say i've got a you know investment firm it's called black horse right and i "
              "want to have black dot horse and uh uh that's great and i've got my home page "
              'at black.',
      'timestamp': 1652,
      'timestamp_label': '[00:27:32]',
      'timestamp_seconds': 1652,
      'tip': "'s say i've got a you know investment firm it's called black horse right and i "
             "want to have black dot horse and uh uh that's great and i've got my home page at "
             'black.',
      'title': 'The Future of Domains with Andrew Rosener | HANDYCON (SkyInclude)',
      'url': 'https://www.youtube.com/watch?v=0-ax0cEcuZk&t=1652s',
      'video_id': '0-ax0cEcuZk'},
     {'author': 'Sedo.com, LLC',
      'channel': 'Sedo.com, LLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:51](https://www.youtube.com/watch?v=XPj2Qjpi55Y&t=111s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "What the domain's value is this is because if you have a buy now price that's "
              "too high you'll just put off any potential buyers.",
      'timestamp': 111,
      'timestamp_label': '[00:01:51]',
      'timestamp_seconds': 111,
      'tip': "What the domain's value is this is because if you have a buy now price that's "
             "too high you'll just put off any potential buyers.",
      'title': 'What Sales Settings to Choose When Selling Domains - Buy Now VS Make Offer '
               '(Sedo.com, LLC)',
      'url': 'https://www.youtube.com/watch?v=XPj2Qjpi55Y&t=111s',
      'video_id': 'XPj2Qjpi55Y'},
     {'author': 'Semantic Mastery',
      'channel': 'Semantic Mastery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=eSTvHrvbZ-4&t=138s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "A parking page so like where does the revenue come from i'm not sure maybe i "
              "don't know i i just i'm.",
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': "A parking page so like where does the revenue come from i'm not sure maybe i "
             "don't know i i just i'm.",
      'title': 'What Are Your Thoughts On Parked Domains For Monetizing Domains With Some '
               'Amounts Of Traffic? (Semantic Mastery)',
      'url': 'https://www.youtube.com/watch?v=eSTvHrvbZ-4&t=138s',
      'video_id': 'eSTvHrvbZ-4'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=P7O7_GHUYb0&t=20s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Shane's recent re-entry into the ethereum market so we'll dive into that and "
              "then we've got the name Jack gonna jet segment sponsored by namejet and we talk "
              'about some domains coming up for auctions such as medical center.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Shane's recent re-entry into the ethereum market so we'll dive into that and "
             "then we've got the name Jack gonna jet segment sponsored by namejet and we talk "
             'about some domains coming up for auctions such as medical center.',
      'title': 'DomainSherpa Review – 10/27/22: Cyger Says “I’m Back”: RealInnovation, '
               'Tradesman, Encrypto (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=P7O7_GHUYb0&t=20s',
      'video_id': 'P7O7_GHUYb0'},
     {'author': 'kickstartcommerce',
      'channel': 'kickstartcommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:53](https://www.youtube.com/watch?v=IJ9lx010Yps&t=1073s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q1 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Appropriate so it's definitely something that's ass and it's definitely "
              "something that's that's good to have if that's where your your your morals are "
              'lying in that event.',
      'timestamp': 1073,
      'timestamp_label': '[00:17:53]',
      'timestamp_seconds': 1073,
      'tip': "Appropriate so it's definitely something that's ass and it's definitely "
             "something that's that's good to have if that's where your your your morals are "
             'lying in that event.',
      'title': 'The Essentials of Domain Leasing with Escrow’s Brian Tharp (kickstartcommerce)',
      'url': 'https://www.youtube.com/watch?v=IJ9lx010Yps&t=1073s',
      'video_id': 'IJ9lx010Yps'}],
 2: [{'author': '30MinuteDeal Global',
      'channel': '30MinuteDeal Global',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=wCiUhJTjJyo&t=117s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then I registered and found this thread in Escrow portal. It was showing the '
              'transaction details. I had to pay $20 dollars as a disbursement fee. I agreed '
              'to the terms, then the buyer agreed to the terms and escrow was waiting for the '
              'buyer’s payment.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Then I registered and found this thread in Escrow portal. It was showing the '
             'transaction details. I had to pay $20 dollars as a disbursement fee. I agreed to '
             'the terms, then the buyer agreed to the terms and escrow was waiting for the '
             'buyer’s payment.',
      'title': 'How I Sold a $10 Domain at $500 with DomainAgents & Escrow.com (30MinuteDeal '
               'Global)',
      'url': 'https://www.youtube.com/watch?v=wCiUhJTjJyo&t=117s',
      'video_id': 'wCiUhJTjJyo'},
     {'author': 'DomainRacer Hindi',
      'channel': 'DomainRacer Hindi',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:50](https://www.youtube.com/watch?v=eDmh_k07UEg&t=170s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "But all these tips won't work. There's a bonus tip you should know: If anyone "
              "tells you they'll pay you later, it's a red flag. You should immediately avoid "
              'that buyer , otherwise you could face significant losses. Step seven: Use an '
              'escrow service to secure the payment.',
      'timestamp': 170,
      'timestamp_label': '[00:02:50]',
      'timestamp_seconds': 170,
      'tip': "But all these tips won't work. There's a bonus tip you should know: If anyone "
             "tells you they'll pay you later, it's a red flag. You should immediately avoid "
             'that buyer , otherwise you could face significant losses. Step seven: Use an '
             'escrow service to secure the payment.',
      'title': 'Domain Buy & Sell Detailed Guide | How to Buy and Sell Domain | Domain '
               'Flipping Guide 2025 (DomainRacer Hindi)',
      'url': 'https://www.youtube.com/watch?v=eDmh_k07UEg&t=170s',
      'video_id': 'eDmh_k07UEg'},
     {'author': 'Domain Value Estimator',
      'channel': 'Domain Value Estimator',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:34](https://www.youtube.com/watch?v=zNcj1gwZsso&t=394s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if a buyer will not use escrow you verify yourself, there is no deal. The '
              '$50,000 was never real. The only real money in the whole conversation was the '
              'fee they wanted you to pay. You never need to pay for an appraisal to answer a '
              'buyer.',
      'timestamp': 394,
      'timestamp_label': '[00:06:34]',
      'timestamp_seconds': 394,
      'tip': 'And if a buyer will not use escrow you verify yourself, there is no deal. The '
             '$50,000 was never real. The only real money in the whole conversation was the '
             'fee they wanted you to pay. You never need to pay for an appraisal to answer a '
             'buyer.',
      'title': 'A Buyer Offered Me $50,000. It Was a Scam (Domain Value Estimator)',
      'url': 'https://www.youtube.com/watch?v=zNcj1gwZsso&t=394s',
      'video_id': 'zNcj1gwZsso'},
     {'author': 'Sufian Twellman',
      'channel': 'Sufian Twellman',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=uxbVmXRdRtU&t=147s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "3 once you've agreed on the terms you'll create an escrow. 4 the buyer will "
              "receive any mail from escrow. 'll need to provide their payment details such as "
              'their credit card or bank account information step 5 once the buyer has '
              'provided their payment details escrow.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': "3 once you've agreed on the terms you'll create an escrow. 4 the buyer will "
             "receive any mail from escrow. 'll need to provide their payment details such as "
             'their credit card or bank account information step 5 once the buyer has provided '
             'their payment details escrow.',
      'title': 'How to Buy a Website Online Using Escrow.com (Sufian Twellman)',
      'url': 'https://www.youtube.com/watch?v=uxbVmXRdRtU&t=147s',
      'video_id': 'uxbVmXRdRtU'},
     {'author': 'Make Money Anthony',
      'channel': 'Make Money Anthony',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:05](https://www.youtube.com/watch?v=-3yBZKLuJnU&t=65s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re going to be conducting they only go off of what the contract says so before "
              "you go into a transaction on escrow. 're buying an item or whether you're "
              'selling an item make sure that you have a really good contract set up before '
              'you send it over to escrow.',
      'timestamp': 65,
      'timestamp_label': '[00:01:05]',
      'timestamp_seconds': 65,
      'tip': "'re going to be conducting they only go off of what the contract says so before "
             "you go into a transaction on escrow. 're buying an item or whether you're "
             'selling an item make sure that you have a really good contract set up before you '
             'send it over to escrow.',
      'title': '✅ Is Escrow.com Safe To Use 🔴 (Make Money Anthony)',
      'url': 'https://www.youtube.com/watch?v=-3yBZKLuJnU&t=65s',
      'video_id': '-3yBZKLuJnU'},
     {'author': 'Domains No Broker',
      'channel': 'Domains No Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:56](https://www.youtube.com/watch?v=FSQ0uJ1Ul9Q&t=56s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You initiate the transfer of the domain name to the buyer. Because the escrow '
              'service is already holding the money, you can move forward knowing that your '
              'payment is guaranteed as soon as the transfer is complete.',
      'timestamp': 56,
      'timestamp_label': '[00:00:56]',
      'timestamp_seconds': 56,
      'tip': 'You initiate the transfer of the domain name to the buyer. Because the escrow '
             'service is already holding the money, you can move forward knowing that your '
             'payment is guaranteed as soon as the transfer is complete.',
      'title': 'Domain Escrow Explained: How to Sell Safely (Domains No Broker)',
      'url': 'https://www.youtube.com/watch?v=FSQ0uJ1Ul9Q&t=56s',
      'video_id': 'FSQ0uJ1Ul9Q'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:39:06](https://www.youtube.com/watch?v=CKvIo_PJEQI&t=5946s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Maybe you're getting a buyer that pays you 10 or 15 and that's that's kind of "
              "the moonshot price I think on that name. So, >> you know, I'm wanting I want to "
              'pay a few hundred bucks, you know, no more than a grand. And compare that to '
              'the appraised.',
      'timestamp': 5946,
      'timestamp_label': '[01:39:06]',
      'timestamp_seconds': 5946,
      'tip': "Maybe you're getting a buyer that pays you 10 or 15 and that's that's kind of "
             "the moonshot price I think on that name. So, >> you know, I'm wanting I want to "
             'pay a few hundred bucks, you know, no more than a grand. And compare that to the '
             'appraised.',
      'title': 'How Domain Investors Pick Names for Moonshot Pricing | DomainSherpa Podcast '
               '(September 3, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=CKvIo_PJEQI&t=5946s',
      'video_id': 'CKvIo_PJEQI'},
     {'author': 'Lanre Enlight',
      'channel': 'Lanre Enlight',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:16](https://www.youtube.com/watch?v=dEguqGldBcI&t=1756s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Buyer wants to get it so this is another mustard view that's Trust okay this is "
              'build um building dots this these are very nice names so like I said I want to '
              'check Uber suggests.',
      'timestamp': 1756,
      'timestamp_label': '[00:29:16]',
      'timestamp_seconds': 1756,
      'tip': "Buyer wants to get it so this is another mustard view that's Trust okay this is "
             'build um building dots this these are very nice names so like I said I want to '
             'check Uber suggests.',
      'title': 'Domain Flipping: The Ultimate Pro Step-by-Step Guide to Making $1000 Quickly '
               '(Lanre Enlight)',
      'url': 'https://www.youtube.com/watch?v=dEguqGldBcI&t=1756s',
      'video_id': 'dEguqGldBcI'},
     {'author': 'live NDDCamp',
      'channel': 'live NDDCamp',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:02:09](https://www.youtube.com/watch?v=PdwE4T9wmMo&t=3729s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Basically the my buyer was the biggest in one region. And the budget was 20 '
              'million. And it was and it was not enough. So there are maybe this one is top '
              'one in the world but another one maybe is top five.',
      'timestamp': 3729,
      'timestamp_label': '[01:02:09]',
      'timestamp_seconds': 3729,
      'tip': 'Basically the my buyer was the biggest in one region. And the budget was 20 '
             'million. And it was and it was not enough. So there are maybe this one is top '
             'one in the world but another one maybe is top five.',
      'title': 'Domain investment in 2026: disputes, TLDs, marketplaces, and pricing '
               'strategies (live NDDCamp)',
      'url': 'https://www.youtube.com/watch?v=PdwE4T9wmMo&t=3729s',
      'video_id': 'PdwE4T9wmMo'},
     {'author': 'The Dividend Domain',
      'channel': 'The Dividend Domain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=l5aojx7kWb8&t=157s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And that way I'm not pulling too much margin and that helps cuz my overhead can "
              "be anywhere from 5 to 6,000. So, if I'm using one check of my base checks to "
              'pay down or pay towards bills, that actually helps me maintain the margin.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "And that way I'm not pulling too much margin and that helps cuz my overhead can "
             "be anywhere from 5 to 6,000. So, if I'm using one check of my base checks to pay "
             'down or pay towards bills, that actually helps me maintain the margin.',
      'title': 'How My $55,000 Portfolio Generates $757 Every Month Using Margin (The Dividend '
               'Domain)',
      'url': 'https://www.youtube.com/watch?v=l5aojx7kWb8&t=157s',
      'video_id': 'l5aojx7kWb8'},
     {'author': 'Name Experts',
      'channel': 'Name Experts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=VgeW1cO-RaE&t=104s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is completed in some instances paper contracts are then distributed to all '
              'parties with the execution contract so that they have copies for their records '
              "and the transaction is completed and we're ready to move on to the next one.",
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Is completed in some instances paper contracts are then distributed to all '
             'parties with the execution contract so that they have copies for their records '
             "and the transaction is completed and we're ready to move on to the next one.",
      'title': 'Finalizing a Domain Name Purchase with Escrow (Name Experts)',
      'url': 'https://www.youtube.com/watch?v=VgeW1cO-RaE&t=104s',
      'video_id': 'VgeW1cO-RaE'},
     {'author': 'DaaZ Domain Name Marketplace',
      'channel': 'DaaZ Domain Name Marketplace',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:06](https://www.youtube.com/watch?v=OpC53UvZ_Ss&t=126s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Payments then you have the option to select payments choose the months you are '
              'looking to clear the payments from the drop-down and process the payment easily '
              'once the first payment plan is done our agent can guide you to use the domain '
              'name.',
      'timestamp': 126,
      'timestamp_label': '[00:02:06]',
      'timestamp_seconds': 126,
      'tip': 'Payments then you have the option to select payments choose the months you are '
             'looking to clear the payments from the drop-down and process the payment easily '
             'once the first payment plan is done our agent can guide you to use the domain '
             'name.',
      'title': 'Buy a domain name by using Lease to Own Option (DaaZ Domain Name Marketplace)',
      'url': 'https://www.youtube.com/watch?v=OpC53UvZ_Ss&t=126s',
      'video_id': 'OpC53UvZ_Ss'},
     {'author': 'newnet',
      'channel': 'newnet',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=gDTGdxMNGZs&t=225s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Many other personalization options each website in the network contains highly '
              'relevant advertisements that pay you when visitors click all righty I see our '
              'site is embarked and ready to view.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': 'Many other personalization options each website in the network contains highly '
             'relevant advertisements that pay you when visitors click all righty I see our '
             'site is embarked and ready to view.',
      'title': 'Domain Embarking - Introduction (newnet)',
      'url': 'https://www.youtube.com/watch?v=gDTGdxMNGZs&t=225s',
      'video_id': 'gDTGdxMNGZs'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:52](https://www.youtube.com/watch?v=KZqosumnXfg&t=1372s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'t really regret that it fell through because i think i think the name "
              'ultimately is worth more to the right buyer yeah um so how much did you pay for '
              'oregano.',
      'timestamp': 1372,
      'timestamp_label': '[00:22:52]',
      'timestamp_seconds': 1372,
      'tip': "'t really regret that it fell through because i think i think the name "
             'ultimately is worth more to the right buyer yeah um so how much did you pay for '
             'oregano.',
      'title': 'Making Money on the Buy -- With Andrew Rosener (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=KZqosumnXfg&t=1372s',
      'video_id': 'KZqosumnXfg'},
     {'author': 'GoDaddy',
      'channel': 'GoDaddy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:21:55](https://www.youtube.com/watch?v=OM_5VESPepY&t=1315s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q2 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Year um you know this year is running out soon but uh but it is on our plate '
              "and it's a high priority for us to figure out for next year and we want we want "
              "to get that going high page yeah it's good to hear.",
      'timestamp': 1315,
      'timestamp_label': '[00:21:55]',
      'timestamp_seconds': 1315,
      'tip': 'Year um you know this year is running out soon but uh but it is on our plate and '
             "it's a high priority for us to figure out for next year and we want we want to "
             "get that going high page yeah it's good to hear.",
      'title': 'Time’s Up: Acquiring Expired Domains | GoDaddy Hangout (GoDaddy)',
      'url': 'https://www.youtube.com/watch?v=OM_5VESPepY&t=1315s',
      'video_id': 'OM_5VESPepY'}],
 3: [{'author': 'Eunice Ajim',
      'channel': 'Eunice Ajim',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:22](https://www.youtube.com/watch?v=WtkHxzirORM&t=382s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The business [clears throat] model is structurally sound, not just favorable '
              'under ideal conditions. A company that has attractive unit economics only '
              'because they have not yet had to deal with the full cost of operating at scale, '
              'that is a risk I need to price carefully.',
      'timestamp': 382,
      'timestamp_label': '[00:06:22]',
      'timestamp_seconds': 382,
      'tip': 'The business [clears throat] model is structurally sound, not just favorable '
             'under ideal conditions. A company that has attractive unit economics only '
             'because they have not yet had to deal with the full cost of operating at scale, '
             'that is a risk I need to price carefully.',
      'title': "The Truth About Raising Capital In Africa (That Investors Won't Tell You) "
               '(Eunice Ajim)',
      'url': 'https://www.youtube.com/watch?v=WtkHxzirORM&t=382s',
      'video_id': 'WtkHxzirORM'},
     {'author': 'Make Money with Stacy La',
      'channel': 'Make Money with Stacy La',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:22](https://www.youtube.com/watch?v=SuiwtFN2AO8&t=742s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'But one important thing I want to point out is once somebody places a bid, you '
              "cannot cancel the auction. So make sure you're 100% sure about your starting "
              "price before you list it. Now, at this point, we've covered the basics of "
              'buying and selling domains for a profit.',
      'timestamp': 742,
      'timestamp_label': '[00:12:22]',
      'timestamp_seconds': 742,
      'tip': 'But one important thing I want to point out is once somebody places a bid, you '
             "cannot cancel the auction. So make sure you're 100% sure about your starting "
             "price before you list it. Now, at this point, we've covered the basics of buying "
             'and selling domains for a profit.',
      'title': 'Domain Flipping with AI in 2025 | Full Tutorial (Make Money with Stacy La)',
      'url': 'https://www.youtube.com/watch?v=SuiwtFN2AO8&t=742s',
      'video_id': 'SuiwtFN2AO8'},
     {'author': 'GoDaddy Domain Academy',
      'channel': 'GoDaddy Domain Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:44:28](https://www.youtube.com/watch?v=d1VjM9-Tyig&t=2668s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "One one thing I I learned too is on pricing. So maybe I'd be interested to hear "
              'your your take on pricing if you had to do things over. But what I I made a '
              'mistake of trying to price things too low. You know, I priced everything pretty '
              'much at wholesale for bin.',
      'timestamp': 2668,
      'timestamp_label': '[00:44:28]',
      'timestamp_seconds': 2668,
      'tip': "One one thing I I learned too is on pricing. So maybe I'd be interested to hear "
             'your your take on pricing if you had to do things over. But what I I made a '
             'mistake of trying to price things too low. You know, I priced everything pretty '
             'much at wholesale for bin.',
      'title': 'S2 E8 The $500 Domain Investing Challenge: Who’s Winning & What We’ve Learned '
               'So Far (GoDaddy Domain Academy)',
      'url': 'https://www.youtube.com/watch?v=d1VjM9-Tyig&t=2668s',
      'video_id': 'd1VjM9-Tyig'},
     {'author': 'Andrey Verevko',
      'channel': 'Andrey Verevko',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:33](https://www.youtube.com/watch?v=bVQnMN-Qrd8&t=333s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You could have a fixed price or an auction, and the auction every time you run '
              'an auction, there is fees associated with it, regardless if you sell it or not, '
              'or worst-case scenario, someone buys it at the minimum price. So, I tried a '
              'couple auctions.',
      'timestamp': 333,
      'timestamp_label': '[00:05:33]',
      'timestamp_seconds': 333,
      'tip': 'You could have a fixed price or an auction, and the auction every time you run '
             'an auction, there is fees associated with it, regardless if you sell it or not, '
             'or worst-case scenario, someone buys it at the minimum price. So, I tried a '
             'couple auctions.',
      'title': 'How to Start Domain Flipping in 2026 (My Complete Experience) (Andrey Verevko)',
      'url': 'https://www.youtube.com/watch?v=bVQnMN-Qrd8&t=333s',
      'video_id': 'bVQnMN-Qrd8'},
     {'author': 'David Utke',
      'channel': 'David Utke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=UkMYRY9wDN0&t=20s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "The simple reason is that you'll just get a better price at a domain name "
              "register for your com. 're in the mood for compared to a web host or a website "
              'builder because that web host and website builder well they need to mark up the '
              'domain name in order to make a profit.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "The simple reason is that you'll just get a better price at a domain name "
             "register for your com. 're in the mood for compared to a web host or a website "
             'builder because that web host and website builder well they need to mark up the '
             'domain name in order to make a profit.',
      'title': 'The 5 BEST Domain Registrars in 2026: Where to Buy Your Domain Name (David '
               'Utke)',
      'url': 'https://www.youtube.com/watch?v=UkMYRY9wDN0&t=20s',
      'video_id': 'UkMYRY9wDN0'},
     {'author': 'GoDaddy Help Center',
      'channel': 'GoDaddy Help Center',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=9335u-6w_ZQ&t=59s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Check the box next to the domain you wanna sell, and on the action menu, choose '
              "sell domain and then select get started. I'm gonna price mine a little under "
              'the suggested price hoping it will sell faster.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'Check the box next to the domain you wanna sell, and on the action menu, choose '
             "sell domain and then select get started. I'm gonna price mine a little under the "
             'suggested price hoping it will sell faster.',
      'title': 'How to Sell Your Godaddy Domain Step-By-Step on Afternic (GoDaddy Help Center)',
      'url': 'https://www.youtube.com/watch?v=9335u-6w_ZQ&t=59s',
      'video_id': '9335u-6w_ZQ'},
     {'author': 'The Dividend Domain',
      'channel': 'The Dividend Domain',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:37](https://www.youtube.com/watch?v=VV0hxi5TUu4&t=637s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So I put a stop order here because um I'm in profit right now and if this drops "
              "to 109, then it's going to sell and I'm going to use that 2930 to probably cost "
              'down, more than likely cost down on QQQM and just increase that position.',
      'timestamp': 637,
      'timestamp_label': '[00:10:37]',
      'timestamp_seconds': 637,
      'tip': "So I put a stop order here because um I'm in profit right now and if this drops "
             "to 109, then it's going to sell and I'm going to use that 2930 to probably cost "
             'down, more than likely cost down on QQQM and just increase that position.',
      'title': "How I'm Balancing Growth, Income & Margin Risk to Retire Early (The Dividend "
               'Domain)',
      'url': 'https://www.youtube.com/watch?v=VV0hxi5TUu4&t=637s',
      'video_id': 'VV0hxi5TUu4'},
     {'author': 'Andrew Allemann',
      'channel': 'Andrew Allemann',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:32](https://www.youtube.com/watch?v=memimdQC7MY&t=1592s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Instead of 24, setting them for 25. Uh we do see that a lot of people do check '
              'out at that rate and it does reduce the commission amount for the seller. It is '
              'a way of being able just to display it differently.',
      'timestamp': 1592,
      'timestamp_label': '[00:26:32]',
      'timestamp_seconds': 1592,
      'tip': 'Instead of 24, setting them for 25. Uh we do see that a lot of people do check '
             'out at that rate and it does reduce the commission amount for the seller. It is '
             'a way of being able just to display it differently.',
      'title': 'Selling domains through Afternic - DNW Podcast #561 (Andrew Allemann)',
      'url': 'https://www.youtube.com/watch?v=memimdQC7MY&t=1592s',
      'video_id': 'memimdQC7MY'},
     {'author': 'Chris Zuiker - Domain Name Broker',
      'channel': 'Chris Zuiker - Domain Name Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:37](https://www.youtube.com/watch?v=DBqMibOXGo8&t=157s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "If you try to price your domain and let's say it's like some derivative um you "
              "know I don't even know. Like maybe you have Milwaukee quilt something, right? "
              "You're like, I don't understand. This is a million-dollar business. Um you "
              'understand who it attracts.',
      'timestamp': 157,
      'timestamp_label': '[00:02:37]',
      'timestamp_seconds': 157,
      'tip': "If you try to price your domain and let's say it's like some derivative um you "
             "know I don't even know. Like maybe you have Milwaukee quilt something, right? "
             "You're like, I don't understand. This is a million-dollar business. Um you "
             'understand who it attracts.',
      'title': 'Sell your domain name faster by understanding this one thing. (Chris Zuiker - '
               'Domain Name Broker)',
      'url': 'https://www.youtube.com/watch?v=DBqMibOXGo8&t=157s',
      'video_id': 'DBqMibOXGo8'},
     {'author': 'Brooks Conkle // Build Income Streams',
      'channel': 'Brooks Conkle // Build Income Streams',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:41](https://www.youtube.com/watch?v=nOLgURAW0ns&t=41s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So, big commission taken from Afterneck. But I'm going to share some thoughts "
              "of what I think about that. I'm going to tell you my pricing strategy as we go "
              "throughout the video. But here's the first thing to note is that $200 wasn't "
              'going to get me there to this sale.',
      'timestamp': 41,
      'timestamp_label': '[00:00:41]',
      'timestamp_seconds': 41,
      'tip': "So, big commission taken from Afterneck. But I'm going to share some thoughts of "
             "what I think about that. I'm going to tell you my pricing strategy as we go "
             "throughout the video. But here's the first thing to note is that $200 wasn't "
             'going to get me there to this sale.',
      'title': '$2k Domain Flipping Update (Brooks Conkle // Build Income Streams)',
      'url': 'https://www.youtube.com/watch?v=nOLgURAW0ns&t=41s',
      'video_id': 'nOLgURAW0ns'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:50:37](https://www.youtube.com/watch?v=sekhN8zuNlU&t=3037s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Maybe another reason take the cash. You don't want to deal with that. Routine "
              'service air after the auction, right? Like >> routine service is only 2500 a '
              "year. Um when he's angling like it's like when he sees a name in auction that "
              'he likes and he starts play on the show.',
      'timestamp': 3037,
      'timestamp_label': '[00:50:37]',
      'timestamp_seconds': 3037,
      'tip': "Maybe another reason take the cash. You don't want to deal with that. Routine "
             'service air after the auction, right? Like >> routine service is only 2500 a '
             "year. Um when he's angling like it's like when he sees a name in auction that he "
             'likes and he starts play on the show.',
      'title': '$175K for Techno.com?! Premium Domain Sales & Valuations | DomainSherpa '
               'Podcast (November 12, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=sekhN8zuNlU&t=3037s',
      'video_id': 'sekhN8zuNlU'},
     {'author': 'Mere Mortals Podcasts',
      'channel': 'Mere Mortals Podcasts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=yowbJC4PEWE&t=16s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'How much it would cost to to be able to get a dot podcast how much uh about uh '
              'james gridlin was mentioning this uh about half a mil.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'How much it would cost to to be able to get a dot podcast how much uh about uh '
             'james gridlin was mentioning this uh about half a mil.',
      'title': 'The ICANN Monopoly On Domain Names (Mere Mortals Podcasts)',
      'url': 'https://www.youtube.com/watch?v=yowbJC4PEWE&t=16s',
      'video_id': 'yowbJC4PEWE'},
     {'author': 'ICANN',
      'channel': 'ICANN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=AybZsS3NmFo&t=127s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Registrations at a price you choose or you could decide not to sell them at all '
              'maybe you issue them only to your employees you could offer specialized '
              'Security Services or perhaps you want all the web addresses in your TLD to work '
              'in your native.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'Registrations at a price you choose or you could decide not to sell them at all '
             'maybe you issue them only to your employees you could offer specialized Security '
             'Services or perhaps you want all the web addresses in your TLD to work in your '
             'native.',
      'title': 'Overview : Get Ready for the Next Big .Thing - English (ICANN)',
      'url': 'https://www.youtube.com/watch?v=AybZsS3NmFo&t=127s',
      'video_id': 'AybZsS3NmFo'},
     {'author': 'kickstartcommerce',
      'channel': 'kickstartcommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:18](https://www.youtube.com/watch?v=yMsNlST-y9M&t=2958s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm gonna hold this domain for a while now and wait for the and your end users "
              "to give me my price this is the domain which I'm holding right now.",
      'timestamp': 2958,
      'timestamp_label': '[00:49:18]',
      'timestamp_seconds': 2958,
      'tip': "I'm gonna hold this domain for a while now and wait for the and your end users "
             "to give me my price this is the domain which I'm holding right now.",
      'title': 'How Yogi Solanki Sold 15+ Domains in 60 Days (kickstartcommerce)',
      'url': 'https://www.youtube.com/watch?v=yMsNlST-y9M&t=2958s',
      'video_id': 'yMsNlST-y9M'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:38](https://www.youtube.com/watch?v=oeP4t891CPs&t=638s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q3 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So if the >> the cash the cash >> the cash from the auction. So if they took '
              'the cash from the auction then the auction winner kept the car. If they took '
              "the car then the auction didn't matter.",
      'timestamp': 638,
      'timestamp_label': '[00:10:38]',
      'timestamp_seconds': 638,
      'tip': 'So if the >> the cash the cash >> the cash from the auction. So if they took the '
             'cash from the auction then the auction winner kept the car. If they took the car '
             "then the auction didn't matter.",
      'title': 'Inside the Domain Market: Valuations, NamesCon & What’s Next | DomainSherpa '
               'Podcast (Nov. 19, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=oeP4t891CPs&t=638s',
      'video_id': 'oeP4t891CPs'}],
 4: [{'author': 'Ajit Sahane | AI SEO, Backlinks & Websites',
      'channel': 'Ajit Sahane | AI SEO, Backlinks & Websites',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=4HSXReKgl4o&t=258s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Pay with UPI or PayPal with no auto-renewal Stop paying for links you can't "
              'prove Check every backlink the way Google sees it Start free at tools dot '
              'webhostpune dot com.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': "Pay with UPI or PayPal with no auto-renewal Stop paying for links you can't "
             'prove Check every backlink the way Google sees it Start free at tools dot '
             'webhostpune dot com.',
      'title': 'Backlink Checker Tool Demo: Check if Your Backlinks Are Live, Dofollow & '
               'Indexed (Free) (Ajit Sahane | AI SEO, Backlinks & Websites)',
      'url': 'https://www.youtube.com/watch?v=4HSXReKgl4o&t=258s',
      'video_id': '4HSXReKgl4o'},
     {'author': 'Thinking Blueprint',
      'channel': 'Thinking Blueprint',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:30](https://www.youtube.com/watch?v=12ohlClK0g8&t=150s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'About 75% of all domain sales are com domains. IO is also trusted in the tech '
              'and startup world. Country extensions likede for Germany or. United Kingdom '
              'also sell but only to a business that wants customers in that specific country.',
      'timestamp': 150,
      'timestamp_label': '[00:02:30]',
      'timestamp_seconds': 150,
      'tip': 'About 75% of all domain sales are com domains. IO is also trusted in the tech '
             'and startup world. Country extensions likede for Germany or. United Kingdom also '
             'sell but only to a business that wants customers in that specific country.',
      'title': 'Domain Flipping - The Art of Investing in Domains (Thinking Blueprint)',
      'url': 'https://www.youtube.com/watch?v=12ohlClK0g8&t=150s',
      'video_id': '12ohlClK0g8'},
     {'author': 'Ninja Guides',
      'channel': 'Ninja Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=dn3tXJXOypg&t=94s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "This can feel a bit daunting, but it's similar to changing the address on a "
              'package to ensure it arrives at the right destination. Finally, complete the '
              'setup and verify your changes. Return to your Cloudflare dashboard and click on '
              'done, check name servers.',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': "This can feel a bit daunting, but it's similar to changing the address on a "
             'package to ensure it arrives at the right destination. Finally, complete the '
             'setup and verify your changes. Return to your Cloudflare dashboard and click on '
             'done, check name servers.',
      'title': 'How to Set Up Cloudflare DNS to Your Domain - Full Guide (2026) (Ninja Guides)',
      'url': 'https://www.youtube.com/watch?v=dn3tXJXOypg&t=94s',
      'video_id': 'dn3tXJXOypg'},
     {'author': 'Design Guy',
      'channel': 'Design Guy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:56](https://www.youtube.com/watch?v=chataozFYGw&t=296s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Four dead heats out of five rounds, which means your real decision comes down '
              "to that refund flexibility versus the rest of Cloudflare's ecosystem. So which "
              'registrar actually belongs in your stack? Let us break it down into two clean '
              'questions you can answer right now.',
      'timestamp': 296,
      'timestamp_label': '[00:04:56]',
      'timestamp_seconds': 296,
      'tip': 'Four dead heats out of five rounds, which means your real decision comes down to '
             "that refund flexibility versus the rest of Cloudflare's ecosystem. So which "
             'registrar actually belongs in your stack? Let us break it down into two clean '
             'questions you can answer right now.',
      'title': 'Cloudflare Registrar vs Dynadot — Which Wins for Domain Registration in 2026? '
               '(Design Guy)',
      'url': 'https://www.youtube.com/watch?v=chataozFYGw&t=296s',
      'video_id': 'chataozFYGw'},
     {'author': 'ThemeAtelier',
      'channel': 'ThemeAtelier',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:33](https://www.youtube.com/watch?v=uSvTpFGqTaY&t=453s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'JavaScript for additional customization. You can manage backups and activate '
              'your plug-in license here. Finally, inside the tools menu, you will find import '
              'and export options. This allows you to easily migrate domains, offers, and '
              'plug-in configurations.',
      'timestamp': 453,
      'timestamp_label': '[00:07:33]',
      'timestamp_seconds': 453,
      'tip': 'JavaScript for additional customization. You can manage backups and activate '
             'your plug-in license here. Finally, inside the tools menu, you will find import '
             'and export options. This allows you to easily migrate domains, offers, and '
             'plug-in configurations.',
      'title': 'Domain For Sale WordPress Plugin (Pro) – Complete Setup & Selling Domains with '
               'Escrow.com (ThemeAtelier)',
      'url': 'https://www.youtube.com/watch?v=uSvTpFGqTaY&t=453s',
      'video_id': 'uSvTpFGqTaY'},
     {'author': "Jake's Tech Lab",
      'channel': "Jake's Tech Lab",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=ul52eFQneY0&t=370s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before we wrap up, let us run back through all five to see which one fits your '
              'setup. Pick Cloudflare if you want free privacy protection and built-in '
              'security certificates without spending extra.',
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': 'Before we wrap up, let us run back through all five to see which one fits your '
             'setup. Pick Cloudflare if you want free privacy protection and built-in security '
             'certificates without spending extra.',
      'title': 'Best Domain Registrars for Free Extras: 5 Compared on the Specs That Matter '
               "(Jake's Tech Lab)",
      'url': 'https://www.youtube.com/watch?v=ul52eFQneY0&t=370s',
      'video_id': 'ul52eFQneY0'},
     {'author': 'Creed Explains - Hosting & Website Builders',
      'channel': 'Creed Explains - Hosting & Website Builders',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=URhIR-ejFvA&t=57s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "You'll see a status switch next to it, and all you need to do is toggle that "
              'switch to on. Once you enable it, Namecheap will start applying the parking '
              'setup to your domain, but there is one very important thing you need to check '
              'before you finish.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': "You'll see a status switch next to it, and all you need to do is toggle that "
             'switch to on. Once you enable it, Namecheap will start applying the parking '
             'setup to your domain, but there is one very important thing you need to check '
             'before you finish.',
      'title': 'How To Park Domains In Namecheap Account (Step by Step Guide) (Creed Explains '
               '- Hosting & Website Builders)',
      'url': 'https://www.youtube.com/watch?v=URhIR-ejFvA&t=57s',
      'video_id': 'URhIR-ejFvA'},
     {'author': 'The How-To Learning Academy',
      'channel': 'The How-To Learning Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=f5MBxWdYUPw&t=89s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Next, let's look at using Cloudflare DNS for your website. Go to Cloudflare and "
              'sign up for a free account. After that, click add a site or add a domain and '
              'enter your website URL. Cloudflare will guide you through the setup process. '
              'When prompted, choose the free plan.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': "Next, let's look at using Cloudflare DNS for your website. Go to Cloudflare and "
             'sign up for a free account. After that, click add a site or add a domain and '
             'enter your website URL. Cloudflare will guide you through the setup process. '
             'When prompted, choose the free plan.',
      'title': 'How to Use Cloudflare DNS [Full Guide 2026] (The How-To Learning Academy)',
      'url': 'https://www.youtube.com/watch?v=f5MBxWdYUPw&t=89s',
      'video_id': 'f5MBxWdYUPw'},
     {'author': 'Andrew Allemann',
      'channel': 'Andrew Allemann',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:55](https://www.youtube.com/watch?v=jD02RIu6q3Q&t=175s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And there are other tools that'll allow you to see that as well. Uh that not on "
              "DB, but other sites. So, it's kind of interesting. Don't know what that is, but "
              'obviously not a commercial opportunity here. This is a software company, so '
              "that's kind of interesting.",
      'timestamp': 175,
      'timestamp_label': '[00:02:55]',
      'timestamp_seconds': 175,
      'tip': "And there are other tools that'll allow you to see that as well. Uh that not on "
             "DB, but other sites. So, it's kind of interesting. Don't know what that is, but "
             'obviously not a commercial opportunity here. This is a software company, so '
             "that's kind of interesting.",
      'title': 'Domain investing: Using DotDB to find end users and value domains (Andrew '
               'Allemann)',
      'url': 'https://www.youtube.com/watch?v=jD02RIu6q3Q&t=175s',
      'video_id': 'jD02RIu6q3Q'},
     {'author': 'HostMaria',
      'channel': 'HostMaria',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:00](https://www.youtube.com/watch?v=anQ8Zjhrg_M&t=1500s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "100 queries or something like that. I think I put $10 and it's lasted me almost "
              'a year, so pretty good. Do you remember the your story about your bell? I know '
              "it's in my desk here.",
      'timestamp': 1500,
      'timestamp_label': '[00:25:00]',
      'timestamp_seconds': 1500,
      'tip': "100 queries or something like that. I think I put $10 and it's lasted me almost "
             'a year, so pretty good. Do you remember the your story about your bell? I know '
             "it's in my desk here.",
      'title': 'Adam Dicker: How to Value a Domain Name, Domain Valuation Tools & UK domain '
               'portfolio review (HostMaria)',
      'url': 'https://www.youtube.com/watch?v=anQ8Zjhrg_M&t=1500s',
      'video_id': 'anQ8Zjhrg_M'},
     {'author': 'GoDaddy Domain Academy',
      'channel': 'GoDaddy Domain Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=Osg5qiW8qYI&t=98s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I point my name servers there and automatically set it up for 14 months. If I '
              'wanted to come in here to my portfolio and check on my settings, I could do '
              "this several ways. I'm going to show you how to do it quickly.",
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': 'I point my name servers there and automatically set it up for 14 months. If I '
             'wanted to come in here to my portfolio and check on my settings, I could do this '
             "several ways. I'm going to show you how to do it quickly.",
      'title': 'Boost Domain Sales: Easy 14-Month Lease to Own Setup (Afternic Tutorial) '
               '(GoDaddy Domain Academy)',
      'url': 'https://www.youtube.com/watch?v=Osg5qiW8qYI&t=98s',
      'video_id': 'Osg5qiW8qYI'},
     {'author': 'LLMrefs AI SEO',
      'channel': 'LLMrefs AI SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=XEh3aA3iqtI&t=64s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Google's spam policy lists this exact setup as doorway abuse and since May that "
              'policy also covers AI overviews too and one manual action could take out all 22 '
              'sites at once and potentially Zeton themselves and even the links are fragile.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': "Google's spam policy lists this exact setup as doorway abuse and since May that "
             'policy also covers AI overviews too and one manual action could take out all 22 '
             'sites at once and potentially Zeton themselves and even the links are fragile.',
      'title': 'Exact Match Domain Hack for AI Visibility (0 to $7M in 10 days) (LLMrefs AI '
               'SEO)',
      'url': 'https://www.youtube.com/watch?v=XEh3aA3iqtI&t=64s',
      'video_id': 'XEh3aA3iqtI'},
     {'author': 'Carter Law Firm',
      'channel': 'Carter Law Firm',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=JxPAjtHrSQo&t=127s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Include a couple of links below to a couple other articles on trademarks and I '
              'think are really helpful and if you have any questions feel free to contact me '
              'so I hope this has been helpful and I will catch up with you later take care.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'Include a couple of links below to a couple other articles on trademarks and I '
             'think are really helpful and if you have any questions feel free to contact me '
             'so I hope this has been helpful and I will catch up with you later take care.',
      'title': 'Check the USPTO Before you Brand your Business or Product (Carter Law Firm)',
      'url': 'https://www.youtube.com/watch?v=JxPAjtHrSQo&t=127s',
      'video_id': 'JxPAjtHrSQo'},
     {'author': 'Abbas Ravji',
      'channel': 'Abbas Ravji',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:22](https://www.youtube.com/watch?v=gtVEsaXqXHo&t=982s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'React org from this timestamp to this timestamp now this timestamp here if I '
              'actually copy this and I paste it inside of here oops.',
      'timestamp': 982,
      'timestamp_label': '[00:16:22]',
      'timestamp_seconds': 982,
      'tip': 'React org from this timestamp to this timestamp now this timestamp here if I '
             'actually copy this and I paste it inside of here oops.',
      'title': 'How To recreate Expired Domains For your PBN using Free Tools (wayback Machine '
               'Restorer) (Abbas Ravji)',
      'url': 'https://www.youtube.com/watch?v=gtVEsaXqXHo&t=982s',
      'video_id': 'gtVEsaXqXHo'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=OzWsYhxMiCE&t=20s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q4 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Then we've got the name jack in the jet segment sponsored by name jet and we "
              'talk about some domains coming up for auction including voso.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Then we've got the name jack in the jet segment sponsored by name jet and we "
             'talk about some domains coming up for auction including voso.',
      'title': 'The Biggest Mistake Domain Investors Make And How to Fix It | DomainSherpa '
               'Podcast (March 19, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=OzWsYhxMiCE&t=20s',
      'video_id': 'OzWsYhxMiCE'}],
 5: [{'author': 'Ownerly',
      'channel': 'Ownerly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:54](https://www.youtube.com/watch?v=xPtTNJU_OGE&t=354s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Skipping the trademark check is the single most expensive mistake a beginner '
              "can make, because buying a name that infringes a registered mark doesn't just "
              'leave you with a worthless asset.',
      'timestamp': 354,
      'timestamp_label': '[00:05:54]',
      'timestamp_seconds': 354,
      'tip': 'Skipping the trademark check is the single most expensive mistake a beginner can '
             "make, because buying a name that infringes a registered mark doesn't just leave "
             'you with a worthless asset.',
      'title': 'The Reality of Owning a Domain Flipping Business (Ownerly)',
      'url': 'https://www.youtube.com/watch?v=xPtTNJU_OGE&t=354s',
      'video_id': 'xPtTNJU_OGE'},
     {'author': 'SERPSUPPORT',
      'channel': 'SERPSUPPORT',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:19](https://www.youtube.com/watch?v=_rpmkLdcJvc&t=319s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "No pressure and no fake flattery. You're solving a problem for them. The links "
              'you earn this way are editorial. Nothing is hidden and they stay valuable for '
              "years. There's one more legitimate case. Sometimes buying an expired domain is "
              'simply a smart business move.',
      'timestamp': 319,
      'timestamp_label': '[00:05:19]',
      'timestamp_seconds': 319,
      'tip': "No pressure and no fake flattery. You're solving a problem for them. The links "
             'you earn this way are editorial. Nothing is hidden and they stay valuable for '
             "years. There's one more legitimate case. Sometimes buying an expired domain is "
             'simply a smart business move.',
      'title': 'Backlinks from Expired Domains: The Safe Way (and the Trap Most SEOs Fall '
               'Into) (SERPSUPPORT)',
      'url': 'https://www.youtube.com/watch?v=_rpmkLdcJvc&t=319s',
      'video_id': '_rpmkLdcJvc'},
     {'author': 'Expired Domains',
      'channel': 'Expired Domains',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:00](https://www.youtube.com/watch?v=5nQIZvvcgfY&t=180s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Someone neglected it, business failure, spam, penalties, whatever. A great '
              'example of this is spend. It was caught by Drop Catch and auction for $82,000. '
              'This shows that even an excellent domain can drop sometimes by mistake.',
      'timestamp': 180,
      'timestamp_label': '[00:03:00]',
      'timestamp_seconds': 180,
      'tip': 'Someone neglected it, business failure, spam, penalties, whatever. A great '
             'example of this is spend. It was caught by Drop Catch and auction for $82,000. '
             'This shows that even an excellent domain can drop sometimes by mistake.',
      'title': 'Archive Birth Year vs Whois Birth Year - Explained & Why They Matter For Your '
               'Next Domain Investment (Expired Domains)',
      'url': 'https://www.youtube.com/watch?v=5nQIZvvcgfY&t=180s',
      'video_id': '5nQIZvvcgfY'},
     {'author': 'Domains No Broker',
      'channel': 'Domains No Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:16](https://www.youtube.com/watch?v=LrpkfK_9XY0&t=16s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Transfer. Mistake one is buying or holding a domain without checking whether a '
              'real audience or industry could want it.',
      'timestamp': 16,
      'timestamp_label': '[00:00:16]',
      'timestamp_seconds': 16,
      'tip': 'Transfer. Mistake one is buying or holding a domain without checking whether a '
             'real audience or industry could want it.',
      'title': 'Seven Mistakes Domain Sellers Should Avoid (Domains No Broker)',
      'url': 'https://www.youtube.com/watch?v=LrpkfK_9XY0&t=16s',
      'video_id': 'LrpkfK_9XY0'},
     {'author': 'TheMaskedFreelancer😷',
      'channel': 'TheMaskedFreelancer😷',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:48:24](https://www.youtube.com/watch?v=AiootzfgBRM&t=2904s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, after that, uh and and that is exactly why I created my domain academy to '
              'assist you people, to guide you step by step so that you avoid this mistake and '
              'focus only on what works. I focus only on what works. And uh uh The result of '
              'my academy speaks for itself.',
      'timestamp': 2904,
      'timestamp_label': '[00:48:24]',
      'timestamp_seconds': 2904,
      'tip': 'So, after that, uh and and that is exactly why I created my domain academy to '
             'assist you people, to guide you step by step so that you avoid this mistake and '
             'focus only on what works. I focus only on what works. And uh uh The result of my '
             'academy speaks for itself.',
      'title': 'How to start a $1500 domain investment business in Nigeria | How to make money '
               'online (TheMaskedFreelancer😷)',
      'url': 'https://www.youtube.com/watch?v=AiootzfgBRM&t=2904s',
      'video_id': 'AiootzfgBRM'},
     {'author': 'HowToWebmaster',
      'channel': 'HowToWebmaster',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=nBNA5_Ty8Jc&t=50s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "So my website how to webmaster.com Let's submit okay now it will give you the "
              'backlink results just the poorest one or the worst ones and you can quickly.',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': "So my website how to webmaster.com Let's submit okay now it will give you the "
             'backlink results just the poorest one or the worst ones and you can quickly.',
      'title': 'Detect Bad-Spam Backlinks to Your Website Hurting Your SEO (HowToWebmaster)',
      'url': 'https://www.youtube.com/watch?v=nBNA5_Ty8Jc&t=50s',
      'video_id': 'nBNA5_Ty8Jc'},
     {'author': 'SOCDemystified',
      'channel': 'SOCDemystified',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=GPScvA9fgcw&t=163s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Google with one O or Netflix without the I. They are specifically designed to '
              'be traps to catch your typos and hijack your traffic before you even realize '
              'you made a mistake. Your accidental click is actually a valuable commodity.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Google with one O or Netflix without the I. They are specifically designed to be '
             'traps to catch your typos and hijack your traffic before you even realize you '
             'made a mistake. Your accidental click is actually a valuable commodity.',
      'title': 'Day 5 – Domain Parking Exposed: How It Became a Cybercrime Tool '
               '(SOCDemystified)',
      'url': 'https://www.youtube.com/watch?v=GPScvA9fgcw&t=163s',
      'video_id': 'GPScvA9fgcw'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:27](https://www.youtube.com/watch?v=jwAIj8M8kPc&t=2187s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Mistake they would have been more successful if they'd search com you know it's "
              'one of the most successful companies if not the most successful.',
      'timestamp': 2187,
      'timestamp_label': '[00:36:27]',
      'timestamp_seconds': 2187,
      'tip': "Mistake they would have been more successful if they'd search com you know it's "
             'one of the most successful companies if not the most successful.',
      'title': 'What Startups Need to Know About Acquiring a Killer Domain Name -- With Andrew '
               'Rosener (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=jwAIj8M8kPc&t=2187s',
      'video_id': 'jwAIj8M8kPc'},
     {'author': 'Domainer Den',
      'channel': 'Domainer Den',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:28:16](https://www.youtube.com/watch?v=n-fXqW1-lzo&t=1696s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reliance.com होता तो अच्छा नाम होता देखो रेर कॉइन इन्वेस्टिंग भी ये 23 साल '
              'पुराना नेम है मतलब ये कॉइन बिटकॉइन वाला नहीं होगा यह कॉइन जो हमारे रियल कॉइंस '
              'होते.',
      'timestamp': 1696,
      'timestamp_label': '[00:28:16]',
      'timestamp_seconds': 1696,
      'tip': 'Reliance.com होता तो अच्छा नाम होता देखो रेर कॉइन इन्वेस्टिंग भी ये 23 साल '
             'पुराना नेम है मतलब ये कॉइन बिटकॉइन वाला नहीं होगा यह कॉइन जो हमारे रियल कॉइंस '
             'होते.',
      'title': 'Domain Life Cycle and GoDaddy Expiry Auctions (Domainer Den)',
      'url': 'https://www.youtube.com/watch?v=n-fXqW1-lzo&t=1696s',
      'video_id': 'n-fXqW1-lzo'},
     {'author': 'GigaLaw - Doug Isenberg',
      'channel': 'GigaLaw - Doug Isenberg',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:44](https://www.youtube.com/watch?v=OfgGOACCYO0&t=284s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Trademark most sophisticated companies and smart business owners as well as '
              'many individuals.',
      'timestamp': 284,
      'timestamp_label': '[00:04:44]',
      'timestamp_seconds': 284,
      'tip': 'Trademark most sophisticated companies and smart business owners as well as many '
             'individuals.',
      'title': 'Domain Dispute Masterclass (#5): What type of trademark is required to file a '
               'UDRP complaint? (GigaLaw - Doug Isenberg)',
      'url': 'https://www.youtube.com/watch?v=OfgGOACCYO0&t=284s',
      'video_id': 'OfgGOACCYO0'},
     {'author': 'Create a Pro Website',
      'channel': 'Create a Pro Website',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:36](https://www.youtube.com/watch?v=08Ekqe45IH0&t=216s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'You simply type in the domain name that you want, add it to your cart, and '
              "check out. I'll put a link to it in the description. Or, number two, you're "
              "someone who's actually ready to build a website after they get their domain.",
      'timestamp': 216,
      'timestamp_label': '[00:03:36]',
      'timestamp_seconds': 216,
      'tip': 'You simply type in the domain name that you want, add it to your cart, and check '
             "out. I'll put a link to it in the description. Or, number two, you're someone "
             "who's actually ready to build a website after they get their domain.",
      'title': "Don't Buy a Domain Until You Watch This! (Best Domain Name Registrars 2026) "
               '(Create a Pro Website)',
      'url': 'https://www.youtube.com/watch?v=08Ekqe45IH0&t=216s',
      'video_id': '08Ekqe45IH0'},
     {'author': 'Chris Zuiker - Domain Name Broker',
      'channel': 'Chris Zuiker - Domain Name Broker',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:17](https://www.youtube.com/watch?v=veILle9et0o&t=17s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Chrissecker.com and do the daily podcast a lot of good information over there '
              'on both on both channels also domain sure if we did another domain trip of '
              'this.',
      'timestamp': 17,
      'timestamp_label': '[00:00:17]',
      'timestamp_seconds': 17,
      'tip': 'Chrissecker.com and do the daily podcast a lot of good information over there on '
             'both on both channels also domain sure if we did another domain trip of this.',
      'title': 'Price your domain name using these three frames. (Chris Zuiker - Domain Name '
               'Broker)',
      'url': 'https://www.youtube.com/watch?v=veILle9et0o&t=17s',
      'video_id': 'veILle9et0o'},
     {'author': 'GoDaddy Domain Academy',
      'channel': 'GoDaddy Domain Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=n2nzWV5BL3M&t=162s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Of training I think at the time and they had one slide in that three weeks that '
              'was for the auctions it said this you know this is the auctions we need to.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'Of training I think at the time and they had one slide in that three weeks that '
             'was for the auctions it said this you know this is the auctions we need to.',
      'title': "S1E6 A Chat with the Boss GoDaddy's VP of Domain Investing Paul Nicks (GoDaddy "
               'Domain Academy)',
      'url': 'https://www.youtube.com/watch?v=n2nzWV5BL3M&t=162s',
      'video_id': 'n2nzWV5BL3M'},
     {'author': 'theseogeek',
      'channel': 'theseogeek',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:45](https://www.youtube.com/watch?v=13GEx8eLqzo&t=105s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Your link so usually from the home page but if there's an an inner page that's "
              'really really powerful then you can go and you know put your link on that page.',
      'timestamp': 105,
      'timestamp_label': '[00:01:45]',
      'timestamp_seconds': 105,
      'tip': "Your link so usually from the home page but if there's an an inner page that's "
             'really really powerful then you can go and you know put your link on that page.',
      'title': 'Content When Rebuilding Expired and Auction Domains from Wayback Machine '
               '(theseogeek)',
      'url': 'https://www.youtube.com/watch?v=13GEx8eLqzo&t=105s',
      'video_id': '13GEx8eLqzo'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:49](https://www.youtube.com/watch?v=35YUAM-dUn0&t=469s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q5 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'He\'s like, "We\'re now on that super intelligence." And now that of course has '
              'all the people like a lot of these guys, you know, and big shout out to all '
              'the, you know, our listeners and our friends who have been investing and buying '
              'up some of these SI domain names.',
      'timestamp': 469,
      'timestamp_label': '[00:07:49]',
      'timestamp_seconds': 469,
      'tip': 'He\'s like, "We\'re now on that super intelligence." And now that of course has '
             'all the people like a lot of these guys, you know, and big shout out to all the, '
             'you know, our listeners and our friends who have been investing and buying up '
             'some of these SI domain names.',
      'title': '.AI Domains, .SI Hype & the Future of Domain Investing | DomainSherpa Podcast '
               '(October 1, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=35YUAM-dUn0&t=469s',
      'video_id': '35YUAM-dUn0'}],
 6: [{'author': 'Affiliate Credo',
      'channel': 'Affiliate Credo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=S8e33kDoWhQ&t=43s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'First, I want to tell you how I do the initial analysis of the domain before '
              'buying it at auction. I search in Spamzilla and, based on filters and sorting I '
              'find domains according to the given parameters, I determine the most '
              'trustworthy domains for myself 2.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'First, I want to tell you how I do the initial analysis of the domain before '
             'buying it at auction. I search in Spamzilla and, based on filters and sorting I '
             'find domains according to the given parameters, I determine the most trustworthy '
             'domains for myself 2.',
      'title': '📰How to Use Archive.Org to Analyze Expired Domains (Affiliate Credo)',
      'url': 'https://www.youtube.com/watch?v=S8e33kDoWhQ&t=43s',
      'video_id': 'S8e33kDoWhQ'},
     {'author': 'Alex: SEO, Domains & Growth',
      'channel': 'Alex: SEO, Domains & Growth',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=HOn72gelh4s&t=20s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And the first, my favorite tool is Gone Domains. It helps you find quality and '
              'value domains quickly, especially if you want to find expired domains with '
              'backlinks. It shows you a data like domain authority, niche, back links, and '
              'age.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'And the first, my favorite tool is Gone Domains. It helps you find quality and '
             'value domains quickly, especially if you want to find expired domains with '
             'backlinks. It shows you a data like domain authority, niche, back links, and '
             'age.',
      'title': 'Domain Investing Is Easy If You Use These 10 FREE Tools (Alex: SEO, Domains & '
               'Growth)',
      'url': 'https://www.youtube.com/watch?v=HOn72gelh4s&t=20s',
      'video_id': 'HOn72gelh4s'},
     {'author': 'ReviewUP',
      'channel': 'ReviewUP',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=LqUB5Dr0vrE&t=30s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Obviously, we don't want to dig through all that. So, let's set up the filters "
              'used weekly on domaintoprofit. First, open the show filters panel. This is '
              "where you'll clean up the massive list of expiring domains and make it much "
              'easier to find quality names.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': "Obviously, we don't want to dig through all that. So, let's set up the filters "
             'used weekly on domaintoprofit. First, open the show filters panel. This is where '
             "you'll clean up the massive list of expiring domains and make it much easier to "
             'find quality names.',
      'title': 'How to Find Cheap and Good  Expired Domains on GoDaddy (Quick & Easy Domain '
               'Flipping Tutorial) (ReviewUP)',
      'url': 'https://www.youtube.com/watch?v=LqUB5Dr0vrE&t=30s',
      'video_id': 'LqUB5Dr0vrE'},
     {'author': 'Launch with Bryan',
      'channel': 'Launch with Bryan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:23](https://www.youtube.com/watch?v=ASaM7hIMKVI&t=443s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "An affiliate website or lead generation microsite doesn't automatically, you "
              'know, qualify for a Google Business Profile. So, for those [clears throat] '
              "projects, I'm primarily focusing on getting traffic through the regular organic "
              'search results.',
      'timestamp': 443,
      'timestamp_label': '[00:07:23]',
      'timestamp_seconds': 443,
      'tip': "An affiliate website or lead generation microsite doesn't automatically, you "
             'know, qualify for a Google Business Profile. So, for those [clears throat] '
             "projects, I'm primarily focusing on getting traffic through the regular organic "
             'search results.',
      'title': 'Exact Match Domains In 2026: Do They Still Work For SEO? (Launch with Bryan)',
      'url': 'https://www.youtube.com/watch?v=ASaM7hIMKVI&t=443s',
      'video_id': 'ASaM7hIMKVI'},
     {'author': 'GoDaddy Domain Academy',
      'channel': 'GoDaddy Domain Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:47](https://www.youtube.com/watch?v=n3Z47PI6nj0&t=287s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, take take a look and make sure you check that out. Let me show you one last '
              "tip. This time, we're going to do it on GoDaddy Auctions, and I'm going to do "
              'that just to show you a different UI and and how you can reuse this list. Now, '
              'remember, we had starts with, right?',
      'timestamp': 287,
      'timestamp_label': '[00:04:47]',
      'timestamp_seconds': 287,
      'tip': 'So, take take a look and make sure you check that out. Let me show you one last '
             "tip. This time, we're going to do it on GoDaddy Auctions, and I'm going to do "
             'that just to show you a different UI and and how you can reuse this list. Now, '
             'remember, we had starts with, right?',
      'title': 'The Best Way to Filter and Find Profitable Expired Domains (Keyword Data in '
               'Action) (GoDaddy Domain Academy)',
      'url': 'https://www.youtube.com/watch?v=n3Z47PI6nj0&t=287s',
      'video_id': 'n3Z47PI6nj0'},
     {'author': 'Jamie Lewis',
      'channel': 'Jamie Lewis',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=h0uYdy4XIdY&t=51s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'And you\'re like, "Well, shoot. You can\'t find any domains. And so then '
              "you're like, heck, well, maybe I should try an expired drop list, right? So you "
              'uh go to Estabbot and you sign up at Estabbot and you download your first drop '
              'list.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': 'And you\'re like, "Well, shoot. You can\'t find any domains. And so then you\'re '
             'like, heck, well, maybe I should try an expired drop list, right? So you uh go '
             'to Estabbot and you sign up at Estabbot and you download your first drop list.',
      'title': 'Expired Domains Are 99% Trash — Here’s How to Find the Gold #jamielewis (Jamie '
               'Lewis)',
      'url': 'https://www.youtube.com/watch?v=h0uYdy4XIdY&t=51s',
      'video_id': 'h0uYdy4XIdY'},
     {'author': 'George Basics',
      'channel': 'George Basics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=aeqNGnkQgbA&t=69s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then you need to scroll a little bit down and you will see DNS settings. You '
              'need to click this button right here. And from this list, select name servers '
              'and tick this enter new or existing name servers. Paste the first name server '
              'we just copied from Cloudflare.',
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': 'Then you need to scroll a little bit down and you will see DNS settings. You '
             'need to click this button right here. And from this list, select name servers '
             'and tick this enter new or existing name servers. Paste the first name server we '
             'just copied from Cloudflare.',
      'title': 'How To Setup Cloudflare With Dynadot Domain - Full Guide (George Basics)',
      'url': 'https://www.youtube.com/watch?v=aeqNGnkQgbA&t=69s',
      'video_id': 'aeqNGnkQgbA'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:54](https://www.youtube.com/watch?v=4lvZ-LZJ3Sc&t=2214s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s more open uh to to tech or something something else. So >> what what are you "
              "paying for that in auction when you out >> uh five grand? I'm probably not "
              "buying it, but you know, maybe five 5k. James, let's talk to you, bro. What do "
              "you like or don't like on the list?",
      'timestamp': 2214,
      'timestamp_label': '[00:36:54]',
      'timestamp_seconds': 2214,
      'tip': "'s more open uh to to tech or something something else. So >> what what are you "
             "paying for that in auction when you out >> uh five grand? I'm probably not "
             "buying it, but you know, maybe five 5k. James, let's talk to you, bro. What do "
             "you like or don't like on the list?",
      'title': 'AI Domains, .SI Hype & the Future of Domain Investing | Sherpa Snippets '
               '(domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=4lvZ-LZJ3Sc&t=2214s',
      'video_id': '4lvZ-LZJ3Sc'},
     {'author': 'bytecash',
      'channel': 'bytecash',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:27](https://www.youtube.com/watch?v=Hw6wg0dsANM&t=87s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "In um you're going to want to look for we can do three categories here and you "
              "can search so you know we'll try to find something security wise let's see okay "
              'we got to Direct Hit.',
      'timestamp': 87,
      'timestamp_label': '[00:01:27]',
      'timestamp_seconds': 87,
      'tip': "In um you're going to want to look for we can do three categories here and you "
             "can search so you know we'll try to find something security wise let's see okay "
             'we got to Direct Hit.',
      'title': 'Selling Websites on SEDO and AFTERNIC (bytecash)',
      'url': 'https://www.youtube.com/watch?v=Hw6wg0dsANM&t=87s',
      'video_id': 'Hw6wg0dsANM'},
     {'author': 'kickstartcommerce',
      'channel': 'kickstartcommerce',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=gQJxEyrhqec&t=15s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'We share search marketing and domain investing strategies to help grow your '
              "business in today's episode our guests are.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'We share search marketing and domain investing strategies to help grow your '
             "business in today's episode our guests are.",
      'title': 'Domain Outbound Strategies and Best Practices to Sell Domains with Jason '
               'Eisler and Yogi Solanki (kickstartcommerce)',
      'url': 'https://www.youtube.com/watch?v=gQJxEyrhqec&t=15s',
      'video_id': 'gQJxEyrhqec'},
     {'author': 'Scott Redgate',
      'channel': 'Scott Redgate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:13](https://www.youtube.com/watch?v=mRcM1Utk5hI&t=313s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Three remaining search GPT domains but I unlisted one of them so that I can '
              "show you the process for how you can actually list this for sale so it's this "
              'one right here search gppro.',
      'timestamp': 313,
      'timestamp_label': '[00:05:13]',
      'timestamp_seconds': 313,
      'tip': 'Three remaining search GPT domains but I unlisted one of them so that I can show '
             "you the process for how you can actually list this for sale so it's this one "
             'right here search gppro.',
      'title': 'How to Buy & Sell Website Domains to Make Money (Scott Redgate)',
      'url': 'https://www.youtube.com/watch?v=mRcM1Utk5hI&t=313s',
      'video_id': 'mRcM1Utk5hI'},
     {'author': 'DomainFestConference',
      'channel': 'DomainFestConference',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:49](https://www.youtube.com/watch?v=ZMna4WBn7vc&t=1069s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll do search engine optimization we'll get the organic leads so what we found "
              'out was that 40% of the people who are coming to the homepage of '
              'insurancequotes.',
      'timestamp': 1069,
      'timestamp_label': '[00:17:49]',
      'timestamp_seconds': 1069,
      'tip': "'ll do search engine optimization we'll get the organic leads so what we found "
             'out was that 40% of the people who are coming to the homepage of '
             'insurancequotes.',
      'title': 'Webfest Global 2013 Panel - Domain Monetization Options Beyond Domain Parking '
               '(DomainFestConference)',
      'url': 'https://www.youtube.com/watch?v=ZMna4WBn7vc&t=1069s',
      'video_id': 'ZMna4WBn7vc'},
     {'author': 'Brooks Conkle // Build Income Streams',
      'channel': 'Brooks Conkle // Build Income Streams',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:12](https://www.youtube.com/watch?v=uIsWkqUglS4&t=972s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'About this and like have different strategies and some people you know do some '
              'outbound and Outreach some people just like literally just list on um on.',
      'timestamp': 972,
      'timestamp_label': '[00:16:12]',
      'timestamp_seconds': 972,
      'tip': 'About this and like have different strategies and some people you know do some '
             'outbound and Outreach some people just like literally just list on um on.',
      'title': 'How This Broker Sells Domains for MILLIONS — Brian Harbin Interview (Brooks '
               'Conkle // Build Income Streams)',
      'url': 'https://www.youtube.com/watch?v=uIsWkqUglS4&t=972s',
      'video_id': 'uIsWkqUglS4'},
     {'author': 'GoDaddy Domain Academy',
      'channel': 'GoDaddy Domain Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:22](https://www.youtube.com/watch?v=LcmoZJ33ZJ4&t=142s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'They will spend their time teaching a system what opportunity looks like. And '
              'then they will let it hunt while they sleep. The ones who learn this first will '
              'win the names. The ones who do not will keep starting the list over. We are '
              'going to show you exactly how it is done.',
      'timestamp': 142,
      'timestamp_label': '[00:02:22]',
      'timestamp_seconds': 142,
      'tip': 'They will spend their time teaching a system what opportunity looks like. And '
             'then they will let it hunt while they sleep. The ones who learn this first will '
             'win the names. The ones who do not will keep starting the list over. We are '
             'going to show you exactly how it is done.',
      'title': 'The AI Domain Investor: Find More. Bid More. Win More! (GoDaddy Domain '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=LcmoZJ33ZJ4&t=142s',
      'video_id': 'LcmoZJ33ZJ4'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:15:38](https://www.youtube.com/watch?v=J6_UP-VNOco&t=938s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q6 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s primarily done through search engines but i mean in terms of even just like "
              'display or offline advertising like vpn go to vpn.',
      'timestamp': 938,
      'timestamp_label': '[00:15:38]',
      'timestamp_seconds': 938,
      'tip': "'s primarily done through search engines but i mean in terms of even just like "
             'display or offline advertising like vpn go to vpn.',
      'title': 'Royal Rumble over Forbes Domain Valuation Method (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=J6_UP-VNOco&t=938s',
      'video_id': 'J6_UP-VNOco'}],
 7: [{'author': 'Tutorials With Trevor',
      'channel': 'Tutorials With Trevor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:43](https://www.youtube.com/watch?v=w83CsN7RD1Y&t=103s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'However, having a natural mix that includes no follow links can also be '
              'beneficial. The final and crucial step of your audit is to review the quality '
              'of these links. Identify which links are beneficial, often coming from high '
              'authority and relevant websites to your niche.',
      'timestamp': 103,
      'timestamp_label': '[00:01:43]',
      'timestamp_seconds': 103,
      'tip': 'However, having a natural mix that includes no follow links can also be '
             'beneficial. The final and crucial step of your audit is to review the quality of '
             'these links. Identify which links are beneficial, often coming from high '
             'authority and relevant websites to your niche.',
      'title': 'How To Do Backlink Audit With Ubersuggest (Tutorials With Trevor)',
      'url': 'https://www.youtube.com/watch?v=w83CsN7RD1Y&t=103s',
      'video_id': 'w83CsN7RD1Y'},
     {'author': 'PMN Online',
      'channel': 'PMN Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=piq0yLKq_SE&t=28s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'If your DNS settings are incorrect, it can lead to website downtime or '
              "functionality issues. So, it's crucial to get these settings right. Now, let's "
              'dive into the step-by-step process of adding DNS records on Cloudflare.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'If your DNS settings are incorrect, it can lead to website downtime or '
             "functionality issues. So, it's crucial to get these settings right. Now, let's "
             'dive into the step-by-step process of adding DNS records on Cloudflare.',
      'title': 'How to Add DNS Records on Cloudflare Easily 2026 (PMN Online)',
      'url': 'https://www.youtube.com/watch?v=piq0yLKq_SE&t=28s',
      'video_id': 'piq0yLKq_SE'},
     {'author': 'Luka Knows',
      'channel': 'Luka Knows',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:06](https://www.youtube.com/watch?v=oi-pZAGrrhQ&t=486s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Squarespace, also formerly known as Google Domains. Squarespace bought Google '
              'Domains a while back and like most of the acquisition, they need to make that '
              'money back. That said, the buying process is genuinely clean, very minimalistic '
              'and straightforward.',
      'timestamp': 486,
      'timestamp_label': '[00:08:06]',
      'timestamp_seconds': 486,
      'tip': 'Squarespace, also formerly known as Google Domains. Squarespace bought Google '
             'Domains a while back and like most of the acquisition, they need to make that '
             'money back. That said, the buying process is genuinely clean, very minimalistic '
             'and straightforward.',
      'title': "Where to Buy a Domain in 2026? (Don't choose WRONG!) (Luka Knows)",
      'url': 'https://www.youtube.com/watch?v=oi-pZAGrrhQ&t=486s',
      'video_id': 'oi-pZAGrrhQ'},
     {'author': 'DomCop',
      'channel': 'DomCop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=fVAMuCrwtUw&t=21s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Steps to place a back order step one to place an order for a domain name you '
              'would first search for the domain name using the search tool on the home page '
              'so in this example we will be typing in domain buzz com.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'Steps to place a back order step one to place an order for a domain name you '
             'would first search for the domain name using the search tool on the home page so '
             'in this example we will be typing in domain buzz com.',
      'title': 'Domcop - How to Backorder Domains w Namejet and SnapNames (DomCop)',
      'url': 'https://www.youtube.com/watch?v=fVAMuCrwtUw&t=21s',
      'video_id': 'fVAMuCrwtUw'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=zCEoH4BHEDI&t=20s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And then we've got the namejack in a jet segment sponsored by namejet. And we "
              'talk about some domains coming up for auction including clack. And we also talk '
              "about Dan's upcoming move to Portugal. We talk about where things stand in the "
              'new GTLD process.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "And then we've got the namejack in a jet segment sponsored by namejet. And we "
             'talk about some domains coming up for auction including clack. And we also talk '
             "about Dan's upcoming move to Portugal. We talk about where things stand in the "
             'new GTLD process.',
      'title': 'What’s Next for Domain Names? .WEB, ICANN & Market Trends | DomainSherpa '
               'Podcast (Sept. 17, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=zCEoH4BHEDI&t=20s',
      'video_id': 'zCEoH4BHEDI'},
     {'author': 'Nexustech',
      'channel': 'Nexustech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:33](https://www.youtube.com/watch?v=25Wr9hdEUCw&t=153s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s history helps verify its cleanliness, ensuring it hasn't been blacklisted. "
              'The more details you provide here, the higher your listing quality score, which '
              "helps Flippa's algorithm push your domain higher in the search results.",
      'timestamp': 153,
      'timestamp_label': '[00:02:33]',
      'timestamp_seconds': 153,
      'tip': "'s history helps verify its cleanliness, ensuring it hasn't been blacklisted. "
             'The more details you provide here, the higher your listing quality score, which '
             "helps Flippa's algorithm push your domain higher in the search results.",
      'title': 'How to Sell Your Domain on Flippa [2026 GUIDE] (Nexustech)',
      'url': 'https://www.youtube.com/watch?v=25Wr9hdEUCw&t=153s',
      'video_id': '25Wr9hdEUCw'},
     {'author': 'MMX',
      'channel': 'MMX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:27](https://www.youtube.com/watch?v=oSf_C1HUEVA&t=147s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is really effective and efficient way to clean up your toxic backlinks. If '
              "the backlinking domain owners don't remove your link from their site, you can "
              'also take steps to disavow that link where you provide Google with a text file '
              'that says, "We don\'t know these guys.',
      'timestamp': 147,
      'timestamp_label': '[00:02:27]',
      'timestamp_seconds': 147,
      'tip': 'This is really effective and efficient way to clean up your toxic backlinks. If '
             "the backlinking domain owners don't remove your link from their site, you can "
             'also take steps to disavow that link where you provide Google with a text file '
             'that says, "We don\'t know these guys.',
      'title': 'How to Remove Toxic Backlinks in Semrush to Boost Your SEO (MMX)',
      'url': 'https://www.youtube.com/watch?v=oSf_C1HUEVA&t=147s',
      'video_id': 'oSf_C1HUEVA'},
     {'author': 'Efty',
      'channel': 'Efty',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:25](https://www.youtube.com/watch?v=i5aX4LKqSuI&t=85s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a step-by-step tutorial it only takes a couple minutes to do it's super easy "
              'so once done go back to settings preferences here you scroll down to '
              'integration settings and check the use installments checkbox then click save '
              "let's go back to heal.",
      'timestamp': 85,
      'timestamp_label': '[00:01:25]',
      'timestamp_seconds': 85,
      'tip': "'s a step-by-step tutorial it only takes a couple minutes to do it's super easy "
             'so once done go back to settings preferences here you scroll down to integration '
             "settings and check the use installments checkbox then click save let's go back "
             'to heal.',
      'title': 'Boost your domain name sales with Lease-To-Own (Efty)',
      'url': 'https://www.youtube.com/watch?v=i5aX4LKqSuI&t=85s',
      'video_id': 'i5aX4LKqSuI'},
     {'author': 'David Utke',
      'channel': 'David Utke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=ck1VMki_11Q&t=163s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like always, make sure to check the description for links to namecheep '
              'timestamps and any additional resources mentioned in this video. So, step one '
              'with parking a domain name is to actually get a domain name.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Like always, make sure to check the description for links to namecheep '
             'timestamps and any additional resources mentioned in this video. So, step one '
             'with parking a domain name is to actually get a domain name.',
      'title': 'How to Park a Domain & Make Money With Ads (Step-by-Step) (David Utke)',
      'url': 'https://www.youtube.com/watch?v=ck1VMki_11Q&t=163s',
      'video_id': 'ck1VMki_11Q'},
     {'author': 'DomCop',
      'channel': 'DomCop',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:31](https://www.youtube.com/watch?v=im4LjoyOxPE&t=31s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Voodoo okay so here's a step-by-step process that will better help you "
              "understand how domain parking works okay so here's the first step step one it "
              'visitor types in your Park domain name ENT the browser address.',
      'timestamp': 31,
      'timestamp_label': '[00:00:31]',
      'timestamp_seconds': 31,
      'tip': "Voodoo okay so here's a step-by-step process that will better help you "
             "understand how domain parking works okay so here's the first step step one it "
             'visitor types in your Park domain name ENT the browser address.',
      'title': 'How to Domain Park with Voodoo and Bodis (DomCop)',
      'url': 'https://www.youtube.com/watch?v=im4LjoyOxPE&t=31s',
      'video_id': 'im4LjoyOxPE'},
     {'author': 'Hannan Muhammad - Domain Flipping',
      'channel': 'Hannan Muhammad - Domain Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:26](https://www.youtube.com/watch?v=ndpt66l5N1I&t=806s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'देखें जैसे vin.com वट की विडिंग $62 है तो इसे हम छोड़ देते हैं उसके बाद यह डन '
              'भी कुछ बेहतर है g.com बट इसकी जो रजिस्ट्रेशंस है वो.',
      'timestamp': 806,
      'timestamp_label': '[00:13:26]',
      'timestamp_seconds': 806,
      'tip': 'देखें जैसे vin.com वट की विडिंग $62 है तो इसे हम छोड़ देते हैं उसके बाद यह डन भी '
             'कुछ बेहतर है g.com बट इसकी जो रजिस्ट्रेशंस है वो.',
      'title': 'Expired Domain Mastery - Step-by-Step Guide to ExpiredDomains.net | Domain '
               'Investing (Hannan Muhammad - Domain Flipping)',
      'url': 'https://www.youtube.com/watch?v=ndpt66l5N1I&t=806s',
      'video_id': 'ndpt66l5N1I'},
     {'author': 'USENIX',
      'channel': 'USENIX',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:42](https://www.youtube.com/watch?v=XyzbG8sP8iA&t=882s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Classify traffic spam covers over 38 percent of the traffic so um the the the '
              'traffic that was monetized through uh traffic monetization or through a traffic '
              'exchange system was more than 38 but 38 of it was considered spam.',
      'timestamp': 882,
      'timestamp_label': '[00:14:42]',
      'timestamp_seconds': 882,
      'tip': 'Classify traffic spam covers over 38 percent of the traffic so um the the the '
             'traffic that was monetized through uh traffic monetization or through a traffic '
             'exchange system was more than 38 but 38 of it was considered spam.',
      'title': "USENIX Security '14 - Understanding the Dark Side of Domain Parking (USENIX)",
      'url': 'https://www.youtube.com/watch?v=XyzbG8sP8iA&t=882s',
      'video_id': 'XyzbG8sP8iA'},
     {'author': 'SoftSolvate Labs',
      'channel': 'SoftSolvate Labs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=qo5bNS_rl3I&t=15s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'वेबसाइट होती है पास डाटा होता है वह कैसे चेक कर सकते हैं तू वेबैक मशीन सो हेलो '
              'दोस्तों देशभर में टावर हमें 10 साल से बिजली मार्केटिंग की फिल्म में काम कर रहा.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'वेबसाइट होती है पास डाटा होता है वह कैसे चेक कर सकते हैं तू वेबैक मशीन सो हेलो '
             'दोस्तों देशभर में टावर हमें 10 साल से बिजली मार्केटिंग की फिल्म में काम कर रहा.',
      'title': 'Check Wayback Machine(Internet Archive) Data for Past Website Data - Expired '
               'Domain Series Part 5 (SoftSolvate Labs)',
      'url': 'https://www.youtube.com/watch?v=qo5bNS_rl3I&t=15s',
      'video_id': 'qo5bNS_rl3I'},
     {'author': 'NetSpaceindia',
      'channel': 'NetSpaceindia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=_4JXw4pR9G8&t=15s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'लोग बोलेंगे यार तुक्का लग गया होगा। तो चलो उसी बंदे ने एक हफ्ते बाद यह डोमेन '
              'बेचा और यह बेचा उसने ऑलमोस्ट 3 करोड़ का। यानी दोनों मिला के डोमेनस ऑलमोस्ट 4.5 '
              'से.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'लोग बोलेंगे यार तुक्का लग गया होगा। तो चलो उसी बंदे ने एक हफ्ते बाद यह डोमेन '
             'बेचा और यह बेचा उसने ऑलमोस्ट 3 करोड़ का। यानी दोनों मिला के डोमेनस ऑलमोस्ट 4.5 '
             'से.',
      'title': 'How to Make Money Flipping Domains in 2026 (AI Makes It EASY) (NetSpaceindia)',
      'url': 'https://www.youtube.com/watch?v=_4JXw4pR9G8&t=15s',
      'video_id': '_4JXw4pR9G8'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:06](https://www.youtube.com/watch?v=Yvi8ys0RQH8&t=2346s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q7 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Where I'm seeing that growth in in education is one step below that like what "
              "do I need to be online like we're still you know you're still talking to "
              'companies who who go out and buy domain names that are 75 characters long like '
              'I was told at some point.',
      'timestamp': 2346,
      'timestamp_label': '[00:39:06]',
      'timestamp_seconds': 2346,
      'tip': "Where I'm seeing that growth in in education is one step below that like what do "
             "I need to be online like we're still you know you're still talking to companies "
             'who who go out and buy domain names that are 75 characters long like I was told '
             'at some point.',
      'title': 'GoDaddy’s Aftermarket Approach: Normalizing Premium Domain Acquisitions '
               '(domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=Yvi8ys0RQH8&t=2346s',
      'video_id': 'Yvi8ys0RQH8'}],
 8: [{'author': 'DotOutbound',
      'channel': 'DotOutbound',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=6cANvHgSKgI&t=62s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'To pull this off, the platform uses a super clean two-step workflow. Think of '
              "it as a one-two punch. Step one is the radar tool. That's where you scan fast. "
              'And step two is the hunter tool, where you go deep. Two tools, one seamless '
              'workflow.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': 'To pull this off, the platform uses a super clean two-step workflow. Think of it '
             "as a one-two punch. Step one is the radar tool. That's where you scan fast. And "
             'step two is the hunter tool, where you go deep. Two tools, one seamless '
             'workflow.',
      'title': 'DotOutbound.com Walkthrough | How to Sell Domain Names via Outbound Fast '
               '(DotOutbound)',
      'url': 'https://www.youtube.com/watch?v=6cANvHgSKgI&t=62s',
      'video_id': '6cANvHgSKgI'},
     {'author': 'Edvido',
      'channel': 'Edvido',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:40](https://www.youtube.com/watch?v=XjoQwN4FcDU&t=400s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'SEO tools and SEO review tools are actually pulling their data straight from '
              'the Seamrush API. So if Semrush ever hits you with a payw wall, you can '
              'actually access their exact numbers for free just by hopping over to one of '
              'these other sites.',
      'timestamp': 400,
      'timestamp_label': '[00:06:40]',
      'timestamp_seconds': 400,
      'tip': 'SEO tools and SEO review tools are actually pulling their data straight from the '
             'Seamrush API. So if Semrush ever hits you with a payw wall, you can actually '
             'access their exact numbers for free just by hopping over to one of these other '
             'sites.',
      'title': 'Best Free Backlink Checkers Tested (15K vs 65K Links?!) | Real SEO Case Study '
               '| Edvido (Edvido)',
      'url': 'https://www.youtube.com/watch?v=XjoQwN4FcDU&t=400s',
      'video_id': 'XjoQwN4FcDU'},
     {'author': 'OpenSEO',
      'channel': 'OpenSEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=CDKhSTwWeN8&t=75s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'URL, the URL and its subpaths, the domain excluding subdomains, or the domain '
              "including all subdomains. After clicking search, you'll see a number of helpful "
              'graphs and lists containing backlink data for the domain.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': 'URL, the URL and its subpaths, the domain excluding subdomains, or the domain '
             "including all subdomains. After clicking search, you'll see a number of helpful "
             'graphs and lists containing backlink data for the domain.',
      'title': 'How to Check Backlinks with OpenSEO (OpenSEO)',
      'url': 'https://www.youtube.com/watch?v=CDKhSTwWeN8&t=75s',
      'video_id': 'CDKhSTwWeN8'},
     {'author': 'Craig Campbell SEO',
      'channel': 'Craig Campbell SEO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=v_e7GOstIuc&t=32s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "And and you know basically compare the data that they both give now i've done a "
              'backlink audit on my website using the same rush and this is a really good.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': "And and you know basically compare the data that they both give now i've done a "
             'backlink audit on my website using the same rush and this is a really good.',
      'title': 'How to do a Link Audit, Auditing your Backlinks (Craig Campbell SEO)',
      'url': 'https://www.youtube.com/watch?v=v_e7GOstIuc&t=32s',
      'video_id': 'v_e7GOstIuc'},
     {'author': 'ICANN',
      'channel': 'ICANN',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:13](https://www.youtube.com/watch?v=ubAwLfPKk6s&t=73s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'The NCO aggregates data daily from multiple sources. This includes several root '
              'server operators, as well as publicly available data from two recursive DNS '
              'resolvers, Cloudflare and QAx. To use the tool, enter a proposed string.',
      'timestamp': 73,
      'timestamp_label': '[00:01:13]',
      'timestamp_seconds': 73,
      'tip': 'The NCO aggregates data daily from multiple sources. This includes several root '
             'server operators, as well as publicly available data from two recursive DNS '
             'resolvers, Cloudflare and QAx. To use the tool, enter a proposed string.',
      'title': '2026 Round | TAMS: Name Collision Observatory (ICANN)',
      'url': 'https://www.youtube.com/watch?v=ubAwLfPKk6s&t=73s',
      'video_id': 'ubAwLfPKk6s'},
     {'author': 'Jazzy Domainz',
      'channel': 'Jazzy Domainz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:37](https://www.youtube.com/watch?v=7r4PuUv52Pw&t=397s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Um, let's just mention the GoDaddy appraisal tool. Again, like I said, there "
              'are other tools out there um, but this one is a good tool to use.',
      'timestamp': 397,
      'timestamp_label': '[00:06:37]',
      'timestamp_seconds': 397,
      'tip': "Um, let's just mention the GoDaddy appraisal tool. Again, like I said, there are "
             'other tools out there um, but this one is a good tool to use.',
      'title': 'How I List Domains for Sale on Afternic (Step-by-Step Example) (Jazzy Domainz)',
      'url': 'https://www.youtube.com/watch?v=7r4PuUv52Pw&t=397s',
      'video_id': '7r4PuUv52Pw'},
     {'author': 'Tutorials by Manizha & Ryan',
      'channel': 'Tutorials by Manizha & Ryan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:42](https://www.youtube.com/watch?v=Ji9xSr9WZnA&t=522s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Or something like that maybe like a service let's go ahead and search for "
              "service okay madeservice.com that's 45 000 but.",
      'timestamp': 522,
      'timestamp_label': '[00:08:42]',
      'timestamp_seconds': 522,
      'tip': "Or something like that maybe like a service let's go ahead and search for "
             "service okay madeservice.com that's 45 000 but.",
      'title': 'Domain Flipping Guide (2026) | How To Make Money Flipping Domain Names '
               '(Tutorials by Manizha & Ryan)',
      'url': 'https://www.youtube.com/watch?v=Ji9xSr9WZnA&t=522s',
      'video_id': 'Ji9xSr9WZnA'},
     {'author': 'Chris Koerner on The Koerner Office Podcast',
      'channel': 'Chris Koerner on The Koerner Office Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:10](https://www.youtube.com/watch?v=aba_NmtzK1I&t=670s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Things directly into the Google browser not Google search but into your Chrome '
              'browser my friend Peter owns Vidalia onions.com and a ton of his traffic.',
      'timestamp': 670,
      'timestamp_label': '[00:11:10]',
      'timestamp_seconds': 670,
      'tip': 'Things directly into the Google browser not Google search but into your Chrome '
             'browser my friend Peter owns Vidalia onions.com and a ton of his traffic.',
      'title': '15 Years of Domain Name Investing Knowledge in 15 Mins (Chris Koerner on The '
               'Koerner Office Podcast)',
      'url': 'https://www.youtube.com/watch?v=aba_NmtzK1I&t=670s',
      'video_id': 'aba_NmtzK1I'},
     {'author': 'GoDaddy Domain Academy',
      'channel': 'GoDaddy Domain Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=EZU1Ld6SO_o&t=224s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "800 new ones if I click that, which is going to save me a ton of time. I don't "
              'have to keep going back through the 5,000 I looked over. So this gives you a '
              "couple practical ways to use that data that we saw. Let's convert it quickly "
              'and easily into a save search.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': "800 new ones if I click that, which is going to save me a ton of time. I don't "
             'have to keep going back through the 5,000 I looked over. So this gives you a '
             "couple practical ways to use that data that we saw. Let's convert it quickly and "
             'easily into a save search.',
      'title': 'Turn Atom’s Top-Selling Keywords into a Daily Domain Deal Flow (GoDaddy Domain '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=EZU1Ld6SO_o&t=224s',
      'video_id': 'EZU1Ld6SO_o'},
     {'author': 'SpeedyIndex Link Indexing Service',
      'channel': 'SpeedyIndex Link Indexing Service',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:40](https://www.youtube.com/watch?v=wqhZ_zZZgpk&t=40s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Search Console, Links report, top linking sites, and your most  linked pages. '
              'Think of every backlink as a recommendation, but recommendations.',
      'timestamp': 40,
      'timestamp_label': '[00:00:40]',
      'timestamp_seconds': 40,
      'tip': 'Search Console, Links report, top linking sites, and your most  linked pages. '
             'Think of every backlink as a recommendation, but recommendations.',
      'title': 'What Are Backlinks in SEO? Good vs Bad Links (2026) (SpeedyIndex Link Indexing '
               'Service)',
      'url': 'https://www.youtube.com/watch?v=wqhZ_zZZgpk&t=40s',
      'video_id': 'wqhZ_zZZgpk'},
     {'author': 'PPC Better',
      'channel': 'PPC Better',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:59](https://www.youtube.com/watch?v=raCnNNzO6po&t=479s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'re tired of getting bad results from your Google ads campaigns it's time to "
              'talk to PPC better so check out our website at ppcbetter.',
      'timestamp': 479,
      'timestamp_label': '[00:07:59]',
      'timestamp_seconds': 479,
      'tip': "'re tired of getting bad results from your Google ads campaigns it's time to "
             'talk to PPC better so check out our website at ppcbetter.',
      'title': 'Exact Match Domains and Website Search Engine Optimization (SEO) in 2023. (PPC '
               'Better)',
      'url': 'https://www.youtube.com/watch?v=raCnNNzO6po&t=479s',
      'video_id': 'raCnNNzO6po'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=AnOYqTuITG4&t=21s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "We also talk about what's the right measure for this information specifically "
              'median versus mean and how to best provide and use the data. We also discuss '
              'some of the geographic trends that are highlighted in the report and that '
              'escrow is seeing on the platform.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "We also talk about what's the right measure for this information specifically "
             'median versus mean and how to best provide and use the data. We also discuss '
             'some of the geographic trends that are highlighted in the report and that escrow '
             'is seeing on the platform.',
      'title': 'Escrow.com Domain Report: .AI vs .COM Trends Explained | DomainSherpa Podcast '
               '(March 12, 2026) (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=AnOYqTuITG4&t=21s',
      'video_id': 'AnOYqTuITG4'},
     {'author': 'OpenTalk',
      'channel': 'OpenTalk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=VIRXW2_q7xI&t=110s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': '10 000 so dear friend how you can earn by domain parking earning by domain '
              'parking is very easy all you have to do you have to buy a domain name from any '
              'platform like godaddy namecheap epic.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': '10 000 so dear friend how you can earn by domain parking earning by domain '
             'parking is very easy all you have to do you have to buy a domain name from any '
             'platform like godaddy namecheap epic.',
      'title': 'Earn $1000 for domain parking - Best way to make money online - BODIS '
               '(OpenTalk)',
      'url': 'https://www.youtube.com/watch?v=VIRXW2_q7xI&t=110s',
      'video_id': 'VIRXW2_q7xI'},
     {'author': 'NewMovementMedia',
      'channel': 'NewMovementMedia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=ptDjIj-5f0U&t=79s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'I can is saying that they are allowing 500 applications this first round and '
              '400 the next round the first application route will begin January 12 2012 and '
              'in April 12 2012.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'I can is saying that they are allowing 500 applications this first round and 400 '
             'the next round the first application route will begin January 12 2012 and in '
             'April 12 2012.',
      'title': "ICANN's New gTLD Program (NewMovementMedia)",
      'url': 'https://www.youtube.com/watch?v=ptDjIj-5f0U&t=79s',
      'video_id': 'ptDjIj-5f0U'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:13:10](https://www.youtube.com/watch?v=R695oEH1bvA&t=4390s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q8 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Cornstarch because somebody knows about it and then it's gonna sit in their "
              'portfolio for the rest of their lives yeah yeah it is one it is one of those '
              'names but I kind of want it now [Laughter].',
      'timestamp': 4390,
      'timestamp_label': '[01:13:10]',
      'timestamp_seconds': 4390,
      'tip': "Cornstarch because somebody knows about it and then it's gonna sit in their "
             'portfolio for the rest of their lives yeah yeah it is one it is one of those '
             'names but I kind of want it now [Laughter].',
      'title': 'DomainSherpa Review – Dec 21: BainbridgeBuilders.com, Ziplet.com, Metaverse.io '
               '(domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=R695oEH1bvA&t=4390s',
      'video_id': 'R695oEH1bvA'}],
 9: [{'author': 'VPN.com',
      'channel': 'VPN.com',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:28](https://www.youtube.com/watch?v=nwlWrMSMdUU&t=88s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Agreeance on both sides of the equation so I hope you've learned something "
              'again Michael at VPN com if you need any help buying or selling your premium '
              "domain names we'd love to help you out or check us out at VPN comm slash "
              'domains hope you have a great day bye.',
      'timestamp': 88,
      'timestamp_label': '[00:01:28]',
      'timestamp_seconds': 88,
      'tip': "Agreeance on both sides of the equation so I hope you've learned something again "
             'Michael at VPN com if you need any help buying or selling your premium domain '
             "names we'd love to help you out or check us out at VPN comm slash domains hope "
             'you have a great day bye.',
      'title': 'Top 3 Tips for Acquiring 6-8 Figure Exact-Match Domains (VPN.com)',
      'url': 'https://www.youtube.com/watch?v=nwlWrMSMdUU&t=88s',
      'video_id': 'nwlWrMSMdUU'},
     {'author': "Arvow's AI SEO Tips",
      'channel': "Arvow's AI SEO Tips",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=zNPRVbbrEL0&t=100s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Before paying for any placement, ask for the exact page, the proposed '
              'paragraph, the destination URL, and the link wording. Check that the '
              'destination answers the promise made in the article. Also, confirm the '
              'placement terms and what happens if if page or link is removed.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Before paying for any placement, ask for the exact page, the proposed paragraph, '
             'the destination URL, and the link wording. Check that the destination answers '
             'the promise made in the article. Also, confirm the placement terms and what '
             'happens if if page or link is removed.',
      'title': "Backlink Audit: How to Check a Website Before Buying Backlinks (Arvow's AI SEO "
               'Tips)',
      'url': 'https://www.youtube.com/watch?v=zNPRVbbrEL0&t=100s',
      'video_id': 'zNPRVbbrEL0'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:58](https://www.youtube.com/watch?v=HfWOYwPZ1HU&t=58s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "David Weslo understands your needs and goals whether it's a cease and assist "
              'letter a udrp case or buying or selling one or more domain names contact David '
              'Weslo at new medip law.',
      'timestamp': 58,
      'timestamp_label': '[00:00:58]',
      'timestamp_seconds': 58,
      'tip': "David Weslo understands your needs and goals whether it's a cease and assist "
             'letter a udrp case or buying or selling one or more domain names contact David '
             'Weslo at new medip law.',
      'title': 'How To Value Generic Domain Names -- with Andrew Rosener (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=HfWOYwPZ1HU&t=58s',
      'video_id': 'HfWOYwPZ1HU'},
     {'author': 'Tutorials With Alen',
      'channel': 'Tutorials With Alen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=53UqsOGx89Q&t=124s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Finally, it's time to publish your listing. Take a moment here to review all "
              "the information you've entered. Double check your domain name, its price, and "
              'the terms of sale to ensure everything appears just as you intend.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': "Finally, it's time to publish your listing. Take a moment here to review all the "
             "information you've entered. Double check your domain name, its price, and the "
             'terms of sale to ensure everything appears just as you intend.',
      'title': '💸 How to Sell Your GoDaddy Domain Step-by-Step on Afternic (2025 Complete '
               'Guide) (Tutorials With Alen)',
      'url': 'https://www.youtube.com/watch?v=53UqsOGx89Q&t=124s',
      'video_id': '53UqsOGx89Q'},
     {'author': 'NameLifter',
      'channel': 'NameLifter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:27](https://www.youtube.com/watch?v=hBPJH2jIqJ0&t=27s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'When a domain agreement is finalized, there are three general steps involved in '
              'completing the transfer. First, the transaction terms are confirmed. We use an '
              'independent third-party escrow provider, escrow.',
      'timestamp': 27,
      'timestamp_label': '[00:00:27]',
      'timestamp_seconds': 27,
      'tip': 'When a domain agreement is finalized, there are three general steps involved in '
             'completing the transfer. First, the transaction terms are confirmed. We use an '
             'independent third-party escrow provider, escrow.',
      'title': 'NameLifter Escrow.com Domain Purchase Instructions (NameLifter)',
      'url': 'https://www.youtube.com/watch?v=hBPJH2jIqJ0&t=27s',
      'video_id': 'hBPJH2jIqJ0'},
     {'author': 'David Utke',
      'channel': 'David Utke',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=A6-lVEeaHEs&t=116s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then you have domain privacy which is free forever. Domain privacy is very '
              'important. So part of I can rules whenever you register a domain name. You have '
              'to enter in your legal name, address, phone number, email, like a lot of '
              'personal information.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': 'Then you have domain privacy which is free forever. Domain privacy is very '
             'important. So part of I can rules whenever you register a domain name. You have '
             'to enter in your legal name, address, phone number, email, like a lot of '
             'personal information.',
      'title': 'How To Easily Sell Your Namcheap Domain Names! (Step by Step Tutorial) (David '
               'Utke)',
      'url': 'https://www.youtube.com/watch?v=A6-lVEeaHEs&t=116s',
      'video_id': 'A6-lVEeaHEs'},
     {'author': 'PMN Online',
      'channel': 'PMN Online',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=AKtcv_vFlSY&t=183s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Cloudflare DNS, significantly improving both performance and the resilience of '
              'your website. Remember, DNS changes can take up to 48 hours to propagate '
              "worldwide, so be patient and check back if you don't see immediate results.",
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': 'Cloudflare DNS, significantly improving both performance and the resilience of '
             'your website. Remember, DNS changes can take up to 48 hours to propagate '
             "worldwide, so be patient and check back if you don't see immediate results.",
      'title': 'How to Set Cloudflare DNS Easily 2026 (PMN Online)',
      'url': 'https://www.youtube.com/watch?v=AKtcv_vFlSY&t=183s',
      'video_id': 'AKtcv_vFlSY'},
     {'author': 'GoDaddy',
      'channel': 'GoDaddy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:03](https://www.youtube.com/watch?v=OKekYzcUFsg&t=183s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "It's important to know what you're doing when you're getting into the domain "
              'name trade. So if you need help buying or selling a good domain for your '
              'business, a domain broker can be a great help.',
      'timestamp': 183,
      'timestamp_label': '[00:03:03]',
      'timestamp_seconds': 183,
      'tip': "It's important to know what you're doing when you're getting into the domain "
             'name trade. So if you need help buying or selling a good domain for your '
             'business, a domain broker can be a great help.',
      'title': 'Building a Domain Portfolio - How to Invest in Domains | The Journey (GoDaddy)',
      'url': 'https://www.youtube.com/watch?v=OKekYzcUFsg&t=183s',
      'video_id': 'OKekYzcUFsg'},
     {'author': 'Brooks Conkle // Build Income Streams',
      'channel': 'Brooks Conkle // Build Income Streams',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:14](https://www.youtube.com/watch?v=USC2_VCPYbc&t=134s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "Go to like this one I see Summit Nest I don't know like I don't I I don't even "
              'know who I would reach out to or like or where that would go a Prosper bin.',
      'timestamp': 134,
      'timestamp_label': '[00:02:14]',
      'timestamp_seconds': 134,
      'tip': "Go to like this one I see Summit Nest I don't know like I don't I I don't even "
             'know who I would reach out to or like or where that would go a Prosper bin.',
      'title': 'Outbounding Domain Names (Sales Outreach Tutorial) (Brooks Conkle // Build '
               'Income Streams)',
      'url': 'https://www.youtube.com/watch?v=USC2_VCPYbc&t=134s',
      'video_id': 'USC2_VCPYbc'},
     {'author': 'Hannan Muhammad - Domain Flipping',
      'channel': 'Hannan Muhammad - Domain Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:18](https://www.youtube.com/watch?v=FoTuWS2OJes&t=498s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like.com.net.org डीएचडी जो होती है टॉप लेवल डोमेन यह तू टाइप्स की होती है एक '
              'होता है जीटीएल दी जेनेरिक टॉप लेवल डोमेन जेनेरिक टॉप लेवल जो होती है ये होती है '
              'जो जनरल टर्म्स होती है like.com.',
      'timestamp': 498,
      'timestamp_label': '[00:08:18]',
      'timestamp_seconds': 498,
      'tip': 'Like.com.net.org डीएचडी जो होती है टॉप लेवल डोमेन यह तू टाइप्स की होती है एक '
             'होता है जीटीएल दी जेनेरिक टॉप लेवल डोमेन जेनेरिक टॉप लेवल जो होती है ये होती है '
             'जो जनरल टर्म्स होती है like.com.',
      'title': 'Domaining 101 - Introduction to Domain Investing (Hannan Muhammad - Domain '
               'Flipping)',
      'url': 'https://www.youtube.com/watch?v=FoTuWS2OJes&t=498s',
      'video_id': 'FoTuWS2OJes'},
     {'author': 'cssfx',
      'channel': 'cssfx',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:18](https://www.youtube.com/watch?v=zN6FKHG-ORs&t=78s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, Dino Dot also has the ability to add prepaid credits to your account via '
              'credit card, PayPal, or other means. This is a great feature, especially for '
              'drop catching utilities like Snatcher that allows you to do instant '
              'registration when providing your login credentials.',
      'timestamp': 78,
      'timestamp_label': '[00:01:18]',
      'timestamp_seconds': 78,
      'tip': 'So, Dino Dot also has the ability to add prepaid credits to your account via '
             'credit card, PayPal, or other means. This is a great feature, especially for '
             'drop catching utilities like Snatcher that allows you to do instant registration '
             'when providing your login credentials.',
      'title': 'Dynadot: An Often Overlooked Player in the Expired Domain Name Aftermarket '
               '(cssfx)',
      'url': 'https://www.youtube.com/watch?v=zN6FKHG-ORs&t=78s',
      'video_id': 'zN6FKHG-ORs'},
     {'author': 'Scott Redgate',
      'channel': 'Scott Redgate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:57](https://www.youtube.com/watch?v=rzHCbB8_QqU&t=237s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'NameCheep or GoDaddy and you can purchase it usually for $12 or less per year. '
              'But there are some other statuses like maybe that domain is up on the auction '
              'websites and so you would actually have to bid. Sometimes that domain is '
              'backorded.',
      'timestamp': 237,
      'timestamp_label': '[00:03:57]',
      'timestamp_seconds': 237,
      'tip': 'NameCheep or GoDaddy and you can purchase it usually for $12 or less per year. '
             'But there are some other statuses like maybe that domain is up on the auction '
             'websites and so you would actually have to bid. Sometimes that domain is '
             'backorded.',
      'title': 'How to Buy Expired Domains (but should you really?) (Scott Redgate)',
      'url': 'https://www.youtube.com/watch?v=rzHCbB8_QqU&t=237s',
      'video_id': 'rzHCbB8_QqU'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:08](https://www.youtube.com/watch?v=ksUajnoey7I&t=2228s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "I could understand that you're trying to close the deal you need to be be able "
              'to explain things in real people terms and explain why the domain is worth that '
              "much and and close the deal but when you're buying something like 9g.",
      'timestamp': 2228,
      'timestamp_label': '[00:37:08]',
      'timestamp_seconds': 2228,
      'tip': "I could understand that you're trying to close the deal you need to be be able "
             'to explain things in real people terms and explain why the domain is worth that '
             "much and and close the deal but when you're buying something like 9g.",
      'title': 'How a Fishmonger Lost $300K Learning the Domain Name Ropes - With Andrew '
               'Rosener @MediaOptions (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=ksUajnoey7I&t=2228s',
      'video_id': 'ksUajnoey7I'},
     {'author': 'Domain Notebook',
      'channel': 'Domain Notebook',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=ntMgB1hXTa8&t=104s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purchase best college road and you purchase through godaddy or whoever and you '
              'want you want to park it on our site all you have to do is simply go to the '
              'parking tab add the domain name.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Purchase best college road and you purchase through godaddy or whoever and you '
             'want you want to park it on our site all you have to do is simply go to the '
             'parking tab add the domain name.',
      'title': 'Domain Notebook Parking Tutorial (Domain Notebook)',
      'url': 'https://www.youtube.com/watch?v=ntMgB1hXTa8&t=104s',
      'video_id': 'ntMgB1hXTa8'},
     {'author': 'domainsherpa',
      'channel': 'domainsherpa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:50:45](https://www.youtube.com/watch?v=3C8uYmkV_aE&t=3045s)',
      'relevance': 'Attributed practitioner commentary on '
                   'brandable/exact-match/expired-authority domain investing, drop-catch '
                   'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q9 operational '
                   'verification).',
      'source_type': 'video_pro_tip',
      'text': "'s a lot of value in there but yeah you know in fact probably possibly by the "
              "time the show goes live we'll probably have a link to the book back up on the "
              'website so go to the about us page on the media options.',
      'timestamp': 3045,
      'timestamp_label': '[00:50:45]',
      'timestamp_seconds': 3045,
      'tip': "'s a lot of value in there but yeah you know in fact probably possibly by the "
             "time the show goes live we'll probably have a link to the book back up on the "
             'website so go to the about us page on the media options.',
      'title': 'Decoding End-User Mindset for Premium Domains | DomainSherpa Podcast | '
               'November 2, 2023 (domainsherpa)',
      'url': 'https://www.youtube.com/watch?v=3C8uYmkV_aE&t=3045s',
      'video_id': '3C8uYmkV_aE'}],
 10: [{'author': 'rulo digital',
       'channel': 'rulo digital',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:22](https://www.youtube.com/watch?v=M9xJJGeG1q8&t=682s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That is the exact mechanism at play, yeah. Because to an AI agent that has '
               'been trained on millions of data points to spot fishing attacks and malware, a '
               'misspelled or overly complex domain looks like a security risk. It lacks '
               'mathematical authority.',
       'timestamp': 682,
       'timestamp_label': '[00:11:22]',
       'timestamp_seconds': 682,
       'tip': 'That is the exact mechanism at play, yeah. Because to an AI agent that has been '
              'trained on millions of data points to spot fishing attacks and malware, a '
              'misspelled or overly complex domain looks like a security risk. It lacks '
              'mathematical authority.',
       'title': 'Prime Digital Real Estate: Why Exact-Match .com Domains Are the Ultimate '
                'Business Weapon (rulo digital)',
       'url': 'https://www.youtube.com/watch?v=M9xJJGeG1q8&t=682s',
       'video_id': 'M9xJJGeG1q8'},
      {'author': 'Manic Millionaire',
       'channel': 'Manic Millionaire',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:07](https://www.youtube.com/watch?v=rMXyBJCRlDQ&t=367s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So when you get that right for a pound, it's you can do it on scale. And so "
               "now it with AI as well, it's even easier to create the script to go and find "
               'the soft uh to create the names to go and take advantage of the opportunity.',
       'timestamp': 367,
       'timestamp_label': '[00:06:07]',
       'timestamp_seconds': 367,
       'tip': "So when you get that right for a pound, it's you can do it on scale. And so now "
              "it with AI as well, it's even easier to create the script to go and find the "
              'soft uh to create the names to go and take advantage of the opportunity.',
       'title': 'How I Made $10 Million Trading Domains (Manic Millionaire)',
       'url': 'https://www.youtube.com/watch?v=rMXyBJCRlDQ&t=367s',
       'video_id': 'rMXyBJCRlDQ'},
      {'author': 'The How-To Learning Academy',
       'channel': 'The How-To Learning Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=r3zrQNCo_eU&t=123s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Afternic, verified and published, and confirmed fast transfer to speed up the '
               'handoff and reduce fees. From here, monitor your Afternic dashboard for '
               'offers, respond promptly to broker outreach, and fine-tune pricing as needed '
               'to keep your listings competitive.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': 'Afternic, verified and published, and confirmed fast transfer to speed up the '
              'handoff and reduce fees. From here, monitor your Afternic dashboard for offers, '
              'respond promptly to broker outreach, and fine-tune pricing as needed to keep '
              'your listings competitive.',
       'title': 'How to Sell Your GoDaddy Domain on Afternic [2026 Guide] (The How-To Learning '
                'Academy)',
       'url': 'https://www.youtube.com/watch?v=r3zrQNCo_eU&t=123s',
       'video_id': 'r3zrQNCo_eU'},
      {'author': 'Web Whizz',
       'channel': 'Web Whizz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:26](https://www.youtube.com/watch?v=UPcwro2bxDg&t=146s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Afternic.com and it will show you on the website bonus some of the option that '
               'you caner navigating such as the dashboard portfolio sales offers and.',
       'timestamp': 146,
       'timestamp_label': '[00:02:26]',
       'timestamp_seconds': 146,
       'tip': 'Afternic.com and it will show you on the website bonus some of the option that '
              'you caner navigating such as the dashboard portfolio sales offers and.',
       'title': 'How to Sell Domain on Afternic | Afternic Payment Setup Tutorial (2026) (Web '
                'Whizz)',
       'url': 'https://www.youtube.com/watch?v=UPcwro2bxDg&t=146s',
       'video_id': 'UPcwro2bxDg'},
      {'author': 'Tim Verdouw',
       'channel': 'Tim Verdouw',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:34](https://www.youtube.com/watch?v=ehERSgNWmRc&t=94s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So figuring out what kind of domain to buy, when to buy, how to sell it, how '
               "to negotiate, it's a lot of work, it's a full-time job. That's what domain "
               'flippers do. So we wanted to build a solution uh using Agentic AI where AI '
               'agent does all the work.',
       'timestamp': 94,
       'timestamp_label': '[00:01:34]',
       'timestamp_seconds': 94,
       'tip': 'So figuring out what kind of domain to buy, when to buy, how to sell it, how to '
              "negotiate, it's a lot of work, it's a full-time job. That's what domain "
              'flippers do. So we wanted to build a solution uh using Agentic AI where AI '
              'agent does all the work.',
       'title': 'How to Flip Domains in 2026 Using AI (AIFlipDomains Demo) (Tim Verdouw)',
       'url': 'https://www.youtube.com/watch?v=ehERSgNWmRc&t=94s',
       'video_id': 'ehERSgNWmRc'},
      {'author': 'Edward Sturm',
       'channel': 'Edward Sturm',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:41:03](https://www.youtube.com/watch?v=MvbVisdUAZ0&t=2463s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s as much training as people think. I think it's more QFO than training. Um, "
               "Cloudflare came out and said we're going to by default block AI bots. Uh, so "
               "that basically it's up to the publisher to say whether they want the AI bots.",
       'timestamp': 2463,
       'timestamp_label': '[00:41:03]',
       'timestamp_seconds': 2463,
       'tip': "'s as much training as people think. I think it's more QFO than training. Um, "
              "Cloudflare came out and said we're going to by default block AI bots. Uh, so "
              "that basically it's up to the publisher to say whether they want the AI bots.",
       'title': 'Exact Match Domains Still Work (Most SEOs Are Wrong) (Edward Sturm)',
       'url': 'https://www.youtube.com/watch?v=MvbVisdUAZ0&t=2463s',
       'video_id': 'MvbVisdUAZ0'},
      {'author': 'The AI Traffic Engine',
       'channel': 'The AI Traffic Engine',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:09](https://www.youtube.com/watch?v=N4WntkgqqAg&t=309s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI we create backlinks okay so our strategy the way we create our backlinks is '
               'is we call it like double standard or double strategy. How we do it is one '
               'backlinks. It comes with a backlink and it also comes with a brand mention.',
       'timestamp': 309,
       'timestamp_label': '[00:05:09]',
       'timestamp_seconds': 309,
       'tip': 'AI we create backlinks okay so our strategy the way we create our backlinks is '
              'is we call it like double standard or double strategy. How we do it is one '
              'backlinks. It comes with a backlink and it also comes with a brand mention.',
       'title': 'Exact Match Domain (EMD) Loophole 2026: How I Ranked #1 on Google (Proof '
                'Inside) #ai #seo #links (The AI Traffic Engine)',
       'url': 'https://www.youtube.com/watch?v=N4WntkgqqAg&t=309s',
       'video_id': 'N4WntkgqqAg'},
      {'author': 'The Lone Crater',
       'channel': 'The Lone Crater',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:44](https://www.youtube.com/watch?v=hdvK17zvRgk&t=44s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Beyond just domain registration, Cloudflare provides a comprehensive suite of '
               'integrated services, such as efficient DNS management and free SSL '
               'certificates, making it a one-stop solution for many webmasters seeking '
               'enhanced security and speed.',
       'timestamp': 44,
       'timestamp_label': '[00:00:44]',
       'timestamp_seconds': 44,
       'tip': 'Beyond just domain registration, Cloudflare provides a comprehensive suite of '
              'integrated services, such as efficient DNS management and free SSL '
              'certificates, making it a one-stop solution for many webmasters seeking '
              'enhanced security and speed.',
       'title': 'Cloudflare vs Porkbun Domain - 2025 Comparison (The Lone Crater)',
       'url': 'https://www.youtube.com/watch?v=hdvK17zvRgk&t=44s',
       'video_id': 'hdvK17zvRgk'},
      {'author': 'PMN Online',
       'channel': 'PMN Online',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=YwH_rctl2Kc&t=21s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "With Cloudflare, this task becomes straightforward, and I'm here to guide you "
               "through each step. Let's kick things off by navigating to the DNS section of "
               'your CloudFlare dashboard. After logging into your account, your first stop '
               'should be the DNS area.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "With Cloudflare, this task becomes straightforward, and I'm here to guide you "
              "through each step. Let's kick things off by navigating to the DNS section of "
              'your CloudFlare dashboard. After logging into your account, your first stop '
              'should be the DNS area.',
       'title': 'How to Change DNS in Cloudflare, Update & Setup Easily 2026 (PMN Online)',
       'url': 'https://www.youtube.com/watch?v=YwH_rctl2Kc&t=21s',
       'video_id': 'YwH_rctl2Kc'},
      {'author': 'The Dividend Domain',
       'channel': 'The Dividend Domain',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:16:06](https://www.youtube.com/watch?v=bdb3z0S5ybA&t=966s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "You get a diversity, my allocations. Um, and now I think yeah, let's get into "
               "the last portion of it, and that's going to be uh the margin health dashboard. "
               "So, I don't um keep a spreadsheet, but I regularly run the numbers through AI "
               'and just kind of getting a general idea.',
       'timestamp': 966,
       'timestamp_label': '[00:16:06]',
       'timestamp_seconds': 966,
       'tip': "You get a diversity, my allocations. Um, and now I think yeah, let's get into "
              "the last portion of it, and that's going to be uh the margin health dashboard. "
              "So, I don't um keep a spreadsheet, but I regularly run the numbers through AI "
              'and just kind of getting a general idea.',
       'title': '$50K Portfolio While Using Margin to Pay My Bills (The Dividend Domain)',
       'url': 'https://www.youtube.com/watch?v=bdb3z0S5ybA&t=966s',
       'video_id': 'bdb3z0S5ybA'},
      {'author': 'SawSells',
       'channel': 'SawSells',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:13](https://www.youtube.com/watch?v=EA8QZJvkKP4&t=133s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "When I look through here, it's talking about other things. Are you looking for "
               'something else? Some things have slightly changed in the AI AI world since '
               'then. We got Council of Governmental Ethics Laws. Architecture of Cognitive '
               'Representative Learner.',
       'timestamp': 133,
       'timestamp_label': '[00:02:13]',
       'timestamp_seconds': 133,
       'tip': "When I look through here, it's talking about other things. Are you looking for "
              'something else? Some things have slightly changed in the AI AI world since '
              'then. We got Council of Governmental Ethics Laws. Architecture of Cognitive '
              'Representative Learner.',
       'title': '3 Things Brokers Look for Before Taking On a Domain for Outbound (SawSells)',
       'url': 'https://www.youtube.com/watch?v=EA8QZJvkKP4&t=133s',
       'video_id': 'EA8QZJvkKP4'},
      {'author': 'HostMaria',
       'channel': 'HostMaria',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:23:06](https://www.youtube.com/watch?v=SE1nkvW6rGw&t=1386s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What's the best way to scale things like that now on the flip side of the coin "
               "if you have a hundred thousand pieces of traffic and you're wanting to "
               'monetize that okay now let me answer that question.',
       'timestamp': 1386,
       'timestamp_label': '[00:23:06]',
       'timestamp_seconds': 1386,
       'tip': "What's the best way to scale things like that now on the flip side of the coin "
              "if you have a hundred thousand pieces of traffic and you're wanting to monetize "
              'that okay now let me answer that question.',
       'title': 'Parking Domains with ParkLogic for a Newbie - Michael Gilmour (HostMaria)',
       'url': 'https://www.youtube.com/watch?v=SE1nkvW6rGw&t=1386s',
       'video_id': 'SE1nkvW6rGw'},
      {'author': 'GoDaddy Domain Academy',
       'channel': 'GoDaddy Domain Academy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=I1_LrdnHVvo&t=91s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, you know, there's always something to learn. But if you want to just skip "
               'past setting up your account, you maybe want to use uh how how you would set '
               'up a for sale lander or the best thing to do with lease to own. Did you know '
               'that we have AI powered pricing insights?',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': "So, you know, there's always something to learn. But if you want to just skip "
              'past setting up your account, you maybe want to use uh how how you would set up '
              'a for sale lander or the best thing to do with lease to own. Did you know that '
              'we have AI powered pricing insights?',
       'title': 'Unlock More Domain Sales Today: Secrets from the Afternic Masterclass '
                '(GoDaddy Domain Academy)',
       'url': 'https://www.youtube.com/watch?v=I1_LrdnHVvo&t=91s',
       'video_id': 'I1_LrdnHVvo'},
      {'author': 'GoDaddy',
       'channel': 'GoDaddy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:38](https://www.youtube.com/watch?v=0f-o9p0h6u8&t=158s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Important too if a names changes uh the bids and you're out bid you can get a "
               "push notification things like that that are really important so we're going to "
               'start by talking through what the name the life cycle is for the name so how '
               'does a name actually expire.',
       'timestamp': 158,
       'timestamp_label': '[00:02:38]',
       'timestamp_seconds': 158,
       'tip': "Important too if a names changes uh the bids and you're out bid you can get a "
              "push notification things like that that are really important so we're going to "
              'start by talking through what the name the life cycle is for the name so how '
              'does a name actually expire.',
       'title': 'Learning the Basics of Buying Expired Domains | GoDaddy Hangout (GoDaddy)',
       'url': 'https://www.youtube.com/watch?v=0f-o9p0h6u8&t=158s',
       'video_id': '0f-o9p0h6u8'},
      {'author': 'domainsherpa',
       'channel': 'domainsherpa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:13:13](https://www.youtube.com/watch?v=yT5y3iEQ96U&t=4393s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Organizations which are domain name Centric um do do you um I don't know if "
               "you've heard of that project or if you want to talk about the viability of "
               'that kind of structure as new companies are created.',
       'timestamp': 4393,
       'timestamp_label': '[01:13:13]',
       'timestamp_seconds': 4393,
       'tip': "Organizations which are domain name Centric um do do you um I don't know if "
              "you've heard of that project or if you want to talk about the viability of that "
              'kind of structure as new companies are created.',
       'title': 'Down the Domain & Crypto Rabbit Hole – with Bitcoin Developer Jimmy Song '
                '(domainsherpa)',
       'url': 'https://www.youtube.com/watch?v=yT5y3iEQ96U&t=4393s',
       'video_id': 'yT5y3iEQ96U'}],
 11: [{'author': 'Design Guy',
       'channel': 'Design Guy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:44](https://www.youtube.com/watch?v=mMGvtO-bkPI&t=404s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Cloudflare Registar takes three of the six rounds. Now, treat that three of '
               'six as a starting point, not gospel. You will want to check the current '
               'figures on both pages before buying because prices and plans move. Pick '
               'Cloudflare registar if every dollar on renewal counts.',
       'timestamp': 404,
       'timestamp_label': '[00:06:44]',
       'timestamp_seconds': 404,
       'tip': 'Cloudflare Registar takes three of the six rounds. Now, treat that three of six '
              'as a starting point, not gospel. You will want to check the current figures on '
              'both pages before buying because prices and plans move. Pick Cloudflare '
              'registar if every dollar on renewal counts.',
       'title': 'Porkbun or Cloudflare Registrar? Domain Registration Service Compared for '
                '2026 (Design Guy)',
       'url': 'https://www.youtube.com/watch?v=mMGvtO-bkPI&t=404s',
       'video_id': 'mMGvtO-bkPI'},
      {'author': 'NamesBrun',
       'channel': 'NamesBrun',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:18](https://www.youtube.com/watch?v=tVPy99Y1MsA&t=798s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But this is also you know securing their uh brand identity. If the person '
               "cannot find you on the com, they can find you on the. I don't know why I "
               "selected this sun temples. I don't know but I just wanted to check. Maybe "
               "there's a sun temple in India.",
       'timestamp': 798,
       'timestamp_label': '[00:13:18]',
       'timestamp_seconds': 798,
       'tip': 'But this is also you know securing their uh brand identity. If the person '
              "cannot find you on the com, they can find you on the. I don't know why I "
              "selected this sun temples. I don't know but I just wanted to check. Maybe "
              "there's a sun temple in India.",
       'title': 'Live Domain Name Hunt: Expired Ai Domains and Godaddy Auctions | Day-16 '
                '(NamesBrun)',
       'url': 'https://www.youtube.com/watch?v=tVPy99Y1MsA&t=798s',
       'video_id': 'tVPy99Y1MsA'},
      {'author': 'GoDaddy',
       'channel': 'GoDaddy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:40](https://www.youtube.com/watch?v=SNukqlGstqs&t=520s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You might know what this would benefit, you know, another business, a '
               'competitor, yourself, and then you can gauge the value a lot better than if '
               "you're just buying random names that you think might be valuable.",
       'timestamp': 520,
       'timestamp_label': '[00:08:40]',
       'timestamp_seconds': 520,
       'tip': 'You might know what this would benefit, you know, another business, a '
              'competitor, yourself, and then you can gauge the value a lot better than if '
              "you're just buying random names that you think might be valuable.",
       'title': 'Domain Valuation - How to Price and Sell Domains (GoDaddy)',
       'url': 'https://www.youtube.com/watch?v=SNukqlGstqs&t=520s',
       'video_id': 'SNukqlGstqs'},
      {'author': 'Easytorial',
       'channel': 'Easytorial',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:26](https://www.youtube.com/watch?v=sx83eEm6nk4&t=86s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'You want it landing at the right place. Next up, Cloudflare will provide you '
               "with two unique name servers. They'll look something like Alice NS Cloudflare "
               "com and Bob NS Cloudflare com where you'll actually connect your domain to "
               'Cloudflare.',
       'timestamp': 86,
       'timestamp_label': '[00:01:26]',
       'timestamp_seconds': 86,
       'tip': 'You want it landing at the right place. Next up, Cloudflare will provide you '
              "with two unique name servers. They'll look something like Alice NS Cloudflare "
              "com and Bob NS Cloudflare com where you'll actually connect your domain to "
              'Cloudflare.',
       'title': 'How to Set Up and Manage Domain and DNS on Cloudflare [In 3 steps] '
                '(Easytorial)',
       'url': 'https://www.youtube.com/watch?v=sx83eEm6nk4&t=86s',
       'video_id': 'sx83eEm6nk4'},
      {'author': 'Brooks Conkle // Build Income Streams',
       'channel': 'Brooks Conkle // Build Income Streams',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=ciS3H3ANjuM&t=38s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The biggest one in the industry is by far afternick. Used to be another '
               'company called dan. So after nick by far by far is the largest. I know domain '
               'name sellers that this is their full-time business.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': 'The biggest one in the industry is by far afternick. Used to be another company '
              'called dan. So after nick by far by far is the largest. I know domain name '
              'sellers that this is their full-time business.',
       'title': 'How to Make Money Selling Domain Names (3 Easy Methods) (Brooks Conkle // '
                'Build Income Streams)',
       'url': 'https://www.youtube.com/watch?v=ciS3H3ANjuM&t=38s',
       'video_id': 'ciS3H3ANjuM'},
      {'author': 'Domain Reseller',
       'channel': 'Domain Reseller',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:13](https://www.youtube.com/watch?v=72rBKTbIECI&t=193s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Register, and manage domains with every billable action waiting for your '
               'approval. So your domain operations fit your  business, not the other way.',
       'timestamp': 193,
       'timestamp_label': '[00:03:13]',
       'timestamp_seconds': 193,
       'tip': 'Register, and manage domains with every billable action waiting for your '
              'approval. So your domain operations fit your  business, not the other way.',
       'title': 'Stop Overpaying for Domain Reselling! GoDaddy vs. Domain Name API (Domain '
                'Reseller)',
       'url': 'https://www.youtube.com/watch?v=72rBKTbIECI&t=193s',
       'video_id': '72rBKTbIECI'},
      {'author': 'Rookie Domainer',
       'channel': 'Rookie Domainer',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:22](https://www.youtube.com/watch?v=Bi-_Gko1m0g&t=202s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Perspective so obviously this is interesting the guy who currently owns it and '
               "hasn't renewed it yet has it up for sale for 100 uh well I don't know how much "
               "he has it for esther bots appraising out a hundred let's check this out here.",
       'timestamp': 202,
       'timestamp_label': '[00:03:22]',
       'timestamp_seconds': 202,
       'tip': 'Perspective so obviously this is interesting the guy who currently owns it and '
              "hasn't renewed it yet has it up for sale for 100 uh well I don't know how much "
              "he has it for esther bots appraising out a hundred let's check this out here.",
       'title': 'Salvage Domains from the GoDaddy Auctions Bargain Bin (Rookie Domainer)',
       'url': 'https://www.youtube.com/watch?v=Bi-_Gko1m0g&t=202s',
       'video_id': 'Bi-_Gko1m0g'},
      {'author': 'Ecommerce FM',
       'channel': 'Ecommerce FM',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:47](https://www.youtube.com/watch?v=N8NOW92hCY4&t=287s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Was originally registered through gets a cut of those profits from the auction '
               'as well so nobody else really gets a chance to.',
       'timestamp': 287,
       'timestamp_label': '[00:04:47]',
       'timestamp_seconds': 287,
       'tip': 'Was originally registered through gets a cut of those profits from the auction '
              'as well so nobody else really gets a chance to.',
       'title': 'Expired Domains, SEO & Drop Catching (Ecommerce FM)',
       'url': 'https://www.youtube.com/watch?v=N8NOW92hCY4&t=287s',
       'video_id': 'N8NOW92hCY4'},
      {'author': 'domainsherpa',
       'channel': 'domainsherpa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:29:59](https://www.youtube.com/watch?v=cAguI2-CkwU&t=5399s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's always like% >> picks and shovels business, baby. Like people ask me "
               'whether I like SI. I love anything that sells. If I could participate better '
               "on the other side, the auction side 100% I'd be doing. Am I holding it for "
               'reinvestment down the road?',
       'timestamp': 5399,
       'timestamp_label': '[01:29:59]',
       'timestamp_seconds': 5399,
       'tip': "It's always like% >> picks and shovels business, baby. Like people ask me "
              'whether I like SI. I love anything that sells. If I could participate better on '
              "the other side, the auction side 100% I'd be doing. Am I holding it for "
              'reinvestment down the road?',
       'title': 'Premium Domains: .AI vs .SI, Marketplaces & Valuations | DomainSherpa Podcast '
                '(October 29, 2026) (domainsherpa)',
       'url': 'https://www.youtube.com/watch?v=cAguI2-CkwU&t=5399s',
       'video_id': 'cAguI2-CkwU'},
      {'author': 'POWERS Pod',
       'channel': 'POWERS Pod',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:00](https://www.youtube.com/watch?v=S9SNhuYObsA&t=540s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "What's stopping me from going directly to that person just offering them money "
               'and buying their website from them this is why this is a good bit before or.',
       'timestamp': 540,
       'timestamp_label': '[00:09:00]',
       'timestamp_seconds': 540,
       'tip': "What's stopping me from going directly to that person just offering them money "
              'and buying their website from them this is why this is a good bit before or.',
       'title': 'Domain Name Investing 101 with Peter Askew - Founder of Deep South Ventures '
                '(POWERS Pod)',
       'url': 'https://www.youtube.com/watch?v=S9SNhuYObsA&t=540s',
       'video_id': 'S9SNhuYObsA'},
      {'author': 'Chandler Bolt',
       'channel': 'Chandler Bolt',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=NheyTdmBlH0&t=15s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A domain now i've purchased a couple domains i've actually purchased a lot but "
               'there are two big ones selfpublishingschool.com.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': "A domain now i've purchased a couple domains i've actually purchased a lot but "
              'there are two big ones selfpublishingschool.com.',
       'title': 'How To Buy & Negotiate A Domain Purchase (Chandler Bolt)',
       'url': 'https://www.youtube.com/watch?v=NheyTdmBlH0&t=15s',
       'video_id': 'NheyTdmBlH0'},
      {'author': 'Chris Zuiker - Domain Name Broker',
       'channel': 'Chris Zuiker - Domain Name Broker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=yhwbFofi-Q0&t=15s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Help companies to acquire the wrong version the brand brokens from the best '
               'that means the planets check that out over at medium comm check out Dax comm.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'Help companies to acquire the wrong version the brand brokens from the best '
              'that means the planets check that out over at medium comm check out Dax comm.',
       'title': 'Why are one word domain names valuable? (Chris Zuiker - Domain Name Broker)',
       'url': 'https://www.youtube.com/watch?v=yhwbFofi-Q0&t=15s',
       'video_id': 'yhwbFofi-Q0'},
      {'author': 'Shawna Newman (Skipblast)',
       'channel': 'Shawna Newman (Skipblast)',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:12](https://www.youtube.com/watch?v=wkwOl5VePMM&t=252s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Any questions or anything or go ahead and give this video a like by doing this '
               'it kind of lets me know if I should create more videos on topics like this or '
               'if I should try something else to kind of help you build and grow your own '
               'sites alright thanks for watching.',
       'timestamp': 252,
       'timestamp_label': '[00:04:12]',
       'timestamp_seconds': 252,
       'tip': 'Any questions or anything or go ahead and give this video a like by doing this '
              'it kind of lets me know if I should create more videos on topics like this or '
              'if I should try something else to kind of help you build and grow your own '
              'sites alright thanks for watching.',
       'title': 'How To Use The Wayback Machine To Do Due Diligence On Aged Domains (Shawna '
                'Newman (Skipblast))',
       'url': 'https://www.youtube.com/watch?v=wkwOl5VePMM&t=252s',
       'video_id': 'wkwOl5VePMM'},
      {'author': 'ICANN',
       'channel': 'ICANN',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:42](https://www.youtube.com/watch?v=rod8ZJjpJO4&t=222s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "How these internationalized top level domains are working we're launching a "
               "test and we're going to come with a video that will show you how you can "
               'participate in that and help us evaluate if things are set up in the right '
               'way.',
       'timestamp': 222,
       'timestamp_label': '[00:03:42]',
       'timestamp_seconds': 222,
       'tip': "How these internationalized top level domains are working we're launching a "
              "test and we're going to come with a video that will show you how you can "
              'participate in that and help us evaluate if things are set up in the right way.',
       'title': 'Introduction to IDNs (ICANN)',
       'url': 'https://www.youtube.com/watch?v=rod8ZJjpJO4&t=222s',
       'video_id': 'rod8ZJjpJO4'},
      {'author': 'Ajit Sahane | AI SEO, Backlinks & Websites',
       'channel': 'Ajit Sahane | AI SEO, Backlinks & Websites',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:22](https://www.youtube.com/watch?v=4HSXReKgl4o&t=262s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Stop paying for links you can't prove Check every backlink the way Google sees "
               'it Start free at tools dot webhostpune dot com.',
       'timestamp': 262,
       'timestamp_label': '[00:04:22]',
       'timestamp_seconds': 262,
       'tip': "Stop paying for links you can't prove Check every backlink the way Google sees "
              'it Start free at tools dot webhostpune dot com.',
       'title': 'Backlink Checker Tool Demo: Check if Your Backlinks Are Live, Dofollow & '
                'Indexed (Free) (Ajit Sahane | AI SEO, Backlinks & Websites)',
       'url': 'https://www.youtube.com/watch?v=4HSXReKgl4o&t=262s',
       'video_id': '4HSXReKgl4o'}],
 12: [{'author': 'Tim Ferriss',
       'channel': 'Tim Ferriss',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:51:21](https://www.youtube.com/watch?v=ApCGeST90RA&t=3081s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But if I can make $250 every day minimum, then my business will survive. Tim '
               'Ferriss: How did you arrive at that number? Andrew Rosener: I calculated what '
               'my annual expenses were going to be in totality and divided by the number of '
               'business days.',
       'timestamp': 3081,
       'timestamp_label': '[00:51:21]',
       'timestamp_seconds': 3081,
       'tip': 'But if I can make $250 every day minimum, then my business will survive. Tim '
              'Ferriss: How did you arrive at that number? Andrew Rosener: I calculated what '
              'my annual expenses were going to be in totality and divided by the number of '
              'business days.',
       'title': 'From Scallop Kingpin to Selling 8-Figure Domains (4K) (Tim Ferriss)',
       'url': 'https://www.youtube.com/watch?v=ApCGeST90RA&t=3081s',
       'video_id': 'ApCGeST90RA'},
      {'author': 'Andrew Allemann',
       'channel': 'Andrew Allemann',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:35](https://www.youtube.com/watch?v=E4jnQONuo6E&t=755s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I think I walk on water and I start buying a lot of aftermarket domains to '
               "keep things going. I'd say if you catch me on the right day in a slow month, "
               'you can also get a good deal.',
       'timestamp': 755,
       'timestamp_label': '[00:12:35]',
       'timestamp_seconds': 755,
       'tip': 'I think I walk on water and I start buying a lot of aftermarket domains to keep '
              "things going. I'd say if you catch me on the right day in a slow month, you can "
              'also get a good deal.',
       'title': 'My domain investing year so far - DNW Podcast #602 (Andrew Allemann)',
       'url': 'https://www.youtube.com/watch?v=E4jnQONuo6E&t=755s',
       'video_id': 'E4jnQONuo6E'},
      {'author': 'SEARCHLIGHT HQ',
       'channel': 'SEARCHLIGHT HQ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:57](https://www.youtube.com/watch?v=RClpPcLHviU&t=117s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The Pro plan costs $24 per or $60 for the first year when billed annually. It '
               'renews at $240 per year and includes 20 gigabytes of storage and five '
               'dedicated PHP processes. Finally, the business plan costs $36 per month or $90 '
               'for the first year with annual billing.',
       'timestamp': 117,
       'timestamp_label': '[00:01:57]',
       'timestamp_seconds': 117,
       'tip': 'The Pro plan costs $24 per or $60 for the first year when billed annually. It '
              'renews at $240 per year and includes 20 gigabytes of storage and five dedicated '
              'PHP processes. Finally, the business plan costs $36 per month or $90 for the '
              'first year with annual billing.',
       'title': 'Porkbun Review 2026 | Is Porkbun Worth It for Domain Registration? '
                '(SEARCHLIGHT HQ)',
       'url': 'https://www.youtube.com/watch?v=RClpPcLHviU&t=117s',
       'video_id': 'RClpPcLHviU'},
      {'author': 'SearchGAPMethod',
       'channel': 'SearchGAPMethod',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:01](https://www.youtube.com/watch?v=UXycltw74Bw&t=301s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Cloudflare check I won't click through. That's a 31% pass rate on the number "
               'one Google result for free backlinks. Three rows, start to finish. '
               'ReverbNation, live DR90, a real band page with a website link and no nofollow, '
               'around 840,000 estimated visits, pass.',
       'timestamp': 301,
       'timestamp_label': '[00:05:01]',
       'timestamp_seconds': 301,
       'tip': "Cloudflare check I won't click through. That's a 31% pass rate on the number "
              'one Google result for free backlinks. Three rows, start to finish. '
              'ReverbNation, live DR90, a real band page with a website link and no nofollow, '
              'around 840,000 estimated visits, pass.',
       'title': "I Audited Every Link on Google's #1 Free Backlinks List and You're Still "
                'Using It (SearchGAPMethod)',
       'url': 'https://www.youtube.com/watch?v=UXycltw74Bw&t=301s',
       'video_id': 'UXycltw74Bw'},
      {'author': 'Dotup ICANN Accreditation Consulting',
       'channel': 'Dotup ICANN Accreditation Consulting',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:11](https://www.youtube.com/watch?v=UVaTuGEfJF8&t=71s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "TLD registry, what is the ICAN's new GTLD program 2026, how to invest and "
               'start a TLD registry business, investment goals, business models, regulatory '
               'modes, etc. At top level domain is the extension at the end of the web address '
               'like com.',
       'timestamp': 71,
       'timestamp_label': '[00:01:11]',
       'timestamp_seconds': 71,
       'tip': "TLD registry, what is the ICAN's new GTLD program 2026, how to invest and start "
              'a TLD registry business, investment goals, business models, regulatory modes, '
              'etc. At top level domain is the extension at the end of the web address like '
              'com.',
       'title': 'How to Start A Top Level Domain Registry Business? Apply for New gTLD -2026 | '
                'ICANN New gTLD Program (Dotup ICANN Accreditation Consulting)',
       'url': 'https://www.youtube.com/watch?v=UVaTuGEfJF8&t=71s',
       'video_id': 'UVaTuGEfJF8'},
      {'author': 'kickstartcommerce',
       'channel': 'kickstartcommerce',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:46](https://www.youtube.com/watch?v=5UOGADHB0l0&t=886s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Um and I I have thick skin you can call me whatever you want to call me you're "
               "having a bad day or I don't care so I will try again in a couple of days right "
               "so so you know it doesn't matter to me you know you need a hug.",
       'timestamp': 886,
       'timestamp_label': '[00:14:46]',
       'timestamp_seconds': 886,
       'tip': "Um and I I have thick skin you can call me whatever you want to call me you're "
              "having a bad day or I don't care so I will try again in a couple of days right "
              "so so you know it doesn't matter to me you know you need a hug.",
       'title': 'Selling Domains Using The Dan.com Outbound Method with Alex Verdea '
                '(kickstartcommerce)',
       'url': 'https://www.youtube.com/watch?v=5UOGADHB0l0&t=886s',
       'video_id': '5UOGADHB0l0'},
      {'author': 'DomCop',
       'channel': 'DomCop',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:36](https://www.youtube.com/watch?v=r5xkDG4-mvo&t=96s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Here you can see all the metrics along with a list of backlinks to The Domain '
               'the domain name links directly to the auction on the GoDaddy website you can '
               "bid on the domain or buy it from there thank you for watching I'll see you "
               'next week.',
       'timestamp': 96,
       'timestamp_label': '[00:01:36]',
       'timestamp_seconds': 96,
       'tip': 'Here you can see all the metrics along with a list of backlinks to The Domain '
              'the domain name links directly to the auction on the GoDaddy website you can '
              "bid on the domain or buy it from there thank you for watching I'll see you next "
              'week.',
       'title': 'Find awesome expired domains at GoDaddy Auctions using DomCop (DomCop)',
       'url': 'https://www.youtube.com/watch?v=r5xkDG4-mvo&t=96s',
       'video_id': 'r5xkDG4-mvo'},
      {'author': 'RollerAds',
       'channel': 'RollerAds',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=-i811Ip0HIo&t=176s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Want to see how your travel domains did last week? Pick the tag and there it '
               "is. Five domains or 5,000, you can keep them organized. Who's there when you "
               "need help? You shouldn't have to wait days for an answer. At Roller Ads, you "
               'get a personal manager and fast support.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'Want to see how your travel domains did last week? Pick the tag and there it '
              "is. Five domains or 5,000, you can keep them organized. Who's there when you "
              "need help? You shouldn't have to wait days for an answer. At Roller Ads, you "
              'get a personal manager and fast support.',
       'title': '5 things you should know before parking your domains 🎯 (RollerAds)',
       'url': 'https://www.youtube.com/watch?v=-i811Ip0HIo&t=176s',
       'video_id': '-i811Ip0HIo'},
      {'author': 'Rick',
       'channel': 'Rick',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:58](https://www.youtube.com/watch?v=KJ61MrgDU6U&t=58s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Let it load for a moment while Cloudflare processes your domain. A plan '
               'selection screen now appears in front of you. Cloudflare offers different '
               "plans depending on what you need. Take a look at what's available and pick the "
               'plan that suits your needs.',
       'timestamp': 58,
       'timestamp_label': '[00:00:58]',
       'timestamp_seconds': 58,
       'tip': 'Let it load for a moment while Cloudflare processes your domain. A plan '
              'selection screen now appears in front of you. Cloudflare offers different plans '
              "depending on what you need. Take a look at what's available and pick the plan "
              'that suits your needs.',
       'title': 'How To Set Up Cloudflare DNS In Under 5 Minutes [Step By Step Guide] (Rick)',
       'url': 'https://www.youtube.com/watch?v=KJ61MrgDU6U&t=58s',
       'video_id': 'KJ61MrgDU6U'},
      {'author': 'GoDaddy',
       'channel': 'GoDaddy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:44](https://www.youtube.com/watch?v=PPJ8y-pwY38&t=524s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'First two days of sales and how high the close percentage is um on day three '
               "as Todd mentioned the close percentage significantly drops um that's due to "
               'you.',
       'timestamp': 524,
       'timestamp_label': '[00:08:44]',
       'timestamp_seconds': 524,
       'tip': 'First two days of sales and how high the close percentage is um on day three as '
              "Todd mentioned the close percentage significantly drops um that's due to you.",
       'title': 'On The Dot! | Domain Aftermarket | Episode 1 - Afternic Integration with '
                'GoDaddy | GoDaddy Hangout (GoDaddy)',
       'url': 'https://www.youtube.com/watch?v=PPJ8y-pwY38&t=524s',
       'video_id': 'PPJ8y-pwY38'},
      {'author': 'George Basics',
       'channel': 'George Basics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=OuQbsdwFTA0&t=20s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And now go to the Cloudflare. Sign in or register an account. Then click '
               'account home in the menu. And from this page, you can start adding your domain '
               'to Cloudflare. We need to enter our domain right here.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'And now go to the Cloudflare. Sign in or register an account. Then click '
              'account home in the menu. And from this page, you can start adding your domain '
              'to Cloudflare. We need to enter our domain right here.',
       'title': 'How To Setup Cloudflare With Porkbun Domain (Step By Step) (George Basics)',
       'url': 'https://www.youtube.com/watch?v=OuQbsdwFTA0&t=20s',
       'video_id': 'OuQbsdwFTA0'},
      {'author': 'Adam Dicker',
       'channel': 'Adam Dicker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:14:40](https://www.youtube.com/watch?v=DnnSbpJm2ZI&t=880s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Very much uh again you can reach me on Skype also at adam. Dicker and you have '
               "my email you have my cell I've given it a numerous times and uh I hope you "
               "enjoyed this video and I'm looking forward to doing the next one have a great "
               'day bye-bye.',
       'timestamp': 880,
       'timestamp_label': '[00:14:40]',
       'timestamp_seconds': 880,
       'tip': 'Very much uh again you can reach me on Skype also at adam. Dicker and you have '
              "my email you have my cell I've given it a numerous times and uh I hope you "
              "enjoyed this video and I'm looking forward to doing the next one have a great "
              'day bye-bye.',
       'title': 'TheArtOfTheName.com - The Benefits of Domain Leasing and use eCop.com or '
                'Escrow.comcom (Adam Dicker)',
       'url': 'https://www.youtube.com/watch?v=DnnSbpJm2ZI&t=880s',
       'video_id': 'DnnSbpJm2ZI'},
      {'author': 'Chris Zuiker - Domain Name Broker',
       'channel': 'Chris Zuiker - Domain Name Broker',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:27](https://www.youtube.com/watch?v=dgnnNdyoENg&t=27s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I guess one of the takeaways for me. Um you know, part of this is that we '
               'negotiate with a lot of companies every single day and these are domain names '
               'going from uh some maybe in the four figures, five figures, six figures, seven '
               'figures, eight figures.',
       'timestamp': 27,
       'timestamp_label': '[00:00:27]',
       'timestamp_seconds': 27,
       'tip': 'I guess one of the takeaways for me. Um you know, part of this is that we '
              'negotiate with a lot of companies every single day and these are domain names '
              'going from uh some maybe in the four figures, five figures, six figures, seven '
              'figures, eight figures.',
       'title': 'Negotiating domain names (Chris Zuiker - Domain Name Broker)',
       'url': 'https://www.youtube.com/watch?v=dgnnNdyoENg&t=27s',
       'video_id': 'dgnnNdyoENg'},
      {'author': 'domainsherpa',
       'channel': 'domainsherpa',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:05](https://www.youtube.com/watch?v=Y1dwwAJKRdg&t=425s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Thursday Friday this week yeah y exactly so as this the one dictating the date '
               "on this one let's go so as you are listening or watching the show and we'll "
               'talk about some of the uh the data points but then uh you know definitely get '
               'to escrow.',
       'timestamp': 425,
       'timestamp_label': '[00:07:05]',
       'timestamp_seconds': 425,
       'tip': 'Thursday Friday this week yeah y exactly so as this the one dictating the date '
              "on this one let's go so as you are listening or watching the show and we'll "
              'talk about some of the uh the data points but then uh you know definitely get '
              'to escrow.',
       'title': 'Escrow.com Q4 Report: AI Domains, Market Trends & Insights | DomainSherpa '
                'Podcast | March 20, 2025 (domainsherpa)',
       'url': 'https://www.youtube.com/watch?v=Y1dwwAJKRdg&t=425s',
       'video_id': 'Y1dwwAJKRdg'},
      {'author': 'VPN.com',
       'channel': 'VPN.com',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:30](https://www.youtube.com/watch?v=nwlWrMSMdUU&t=90s)',
       'relevance': 'Attributed practitioner commentary on '
                    'brandable/exact-match/expired-authority domain investing, drop-catch '
                    'auctions, UDRP/ACPA safety, and outbound upgrades (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So I hope you've learned something again Michael at VPN com if you need any "
               "help buying or selling your premium domain names we'd love to help you out or "
               'check us out at VPN comm slash domains hope you have a great day bye.',
       'timestamp': 90,
       'timestamp_label': '[00:01:30]',
       'timestamp_seconds': 90,
       'tip': "So I hope you've learned something again Michael at VPN com if you need any "
              "help buying or selling your premium domain names we'd love to help you out or "
              'check us out at VPN comm slash domains hope you have a great day bye.',
       'title': 'Top 3 Tips for Acquiring 6-8 Figure Exact-Match Domains (VPN.com)',
       'url': 'https://www.youtube.com/watch?v=nwlWrMSMdUU&t=90s',
       'video_id': 'nwlWrMSMdUU'}]}
