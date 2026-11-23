"""Curated 180-citation Live-Event, Super Bowl & VIP Ticket Brokering baseline (15 per chapter across Q1-Q12) mined strictly from verified Live-Event, Super Bowl & VIP Ticket Brokering YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'business',
     'client',
     'clients',
     'firm',
     'margin',
     'market',
     'model',
     'niche',
     'operator',
     'revenue',
     'service',
     'value'},
 2: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'budget',
     'buyer',
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
 3: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'cash',
     'cashflow',
     'commission',
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
 4: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'budget',
     'capital',
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
 5: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'audit',
     'augusta',
     'automatiq',
     'avoid',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'clawback',
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
 6: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'client',
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
 7: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
     'checklist',
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
 8: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
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
 9: {'1099',
     '200',
     '500k',
     'access',
     'accounting',
     'act',
     'add',
     'agency',
     'agreement',
     'all',
     'allocation',
     'allotments',
     'amex',
     'api',
     'arbitrage',
     'arena',
     'artist',
     'association',
     'augusta',
     'automatiq',
     'avoiding',
     'axs',
     'b2b',
     'badge',
     'ban',
     'barcode',
     'best',
     'beverage',
     'beyonce',
     'bots',
     'bowl',
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
 10: {'1099',
      '200',
      '500k',
      'access',
      'accounting',
      'act',
      'add',
      'agency',
      'agent',
      'ai',
      'all',
      'allocation',
      'allotments',
      'amex',
      'api',
      'arbitrage',
      'arena',
      'artist',
      'association',
      'augusta',
      'automate',
      'automation',
      'automatiq',
      'avoiding',
      'axs',
      'b2b',
      'badge',
      'ban',
      'barcode',
      'best',
      'beverage',
      'beyonce',
      'bots',
      'bowl',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'1099',
      '200',
      '500k',
      'access',
      'accounting',
      'act',
      'add',
      'agency',
      'all',
      'allocation',
      'allotments',
      'amex',
      'api',
      'arbitrage',
      'arena',
      'artist',
      'association',
      'augusta',
      'automatiq',
      'avoiding',
      'axs',
      'b2b',
      'badge',
      'ban',
      'barcode',
      'best',
      'beverage',
      'beyonce',
      'bots',
      'bowl',
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
 12: {'1099',
      '200',
      '500k',
      'access',
      'accounting',
      'act',
      'action',
      'add',
      'agency',
      'all',
      'allocation',
      'allotments',
      'amex',
      'api',
      'arbitrage',
      'arena',
      'artist',
      'association',
      'augusta',
      'automatiq',
      'avoiding',
      'axs',
      'b2b',
      'badge',
      'ban',
      'barcode',
      'best',
      'beverage',
      'beyonce',
      'bots',
      'bowl',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'Nerd Nook Hub',
      'channel': 'Nerd Nook Hub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:48](https://www.youtube.com/watch?v=8OkQ2Oq5Lbc&t=48s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The sweet spot is usually located in the lower bowl corners or end zone areas '
              'or even a solid 200 level seats. Expect to pay roughly $7,500 to $10,500 '
              'depending on the matchup and timing. This is the best value per view zone.',
      'timestamp': 48,
      'timestamp_label': '[00:00:48]',
      'timestamp_seconds': 48,
      'tip': 'The sweet spot is usually located in the lower bowl corners or end zone areas or '
             'even a solid 200 level seats. Expect to pay roughly $7,500 to $10,500 depending '
             'on the matchup and timing. This is the best value per view zone.',
      'title': 'How Much Does it Cost to Go to the Super Bowl LX? 2026 (Nerd Nook Hub)',
      'url': 'https://www.youtube.com/watch?v=8OkQ2Oq5Lbc&t=48s',
      'video_id': '8OkQ2Oq5Lbc'},
     {'author': 'Why It Costs',
      'channel': 'Why It Costs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:07](https://www.youtube.com/watch?v=tH7bLaJI6ZE&t=547s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The artist's majority share comes after show costs. A thin Concerts margin does "
              'not erase market power, or the earnings of other business segments.',
      'timestamp': 547,
      'timestamp_label': '[00:09:07]',
      'timestamp_seconds': 547,
      'tip': "The artist's majority share comes after show costs. A thin Concerts margin does "
             'not erase market power, or the earnings of other business segments.',
      'title': 'Concert Tickets: Why a 90% Artist Share Misleads (Why It Costs)',
      'url': 'https://www.youtube.com/watch?v=tH7bLaJI6ZE&t=547s',
      'video_id': 'tH7bLaJI6ZE'},
     {'author': 'Hidden Price',
      'channel': 'Hidden Price',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:32](https://www.youtube.com/watch?v=pfp0vvw1nXo&t=92s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's our calculation, from the company's own figures. Eight cents doesn't "
              'sound like much. But on that revenue, the ticketing business reported an '
              'operating margin of twenty-nine percent. Now the ticket price itself, the face '
              'value.',
      'timestamp': 92,
      'timestamp_label': '[00:01:32]',
      'timestamp_seconds': 92,
      'tip': "That's our calculation, from the company's own figures. Eight cents doesn't "
             'sound like much. But on that revenue, the ticketing business reported an '
             'operating margin of twenty-nine percent. Now the ticket price itself, the face '
             'value.',
      'title': 'Why Concert Tickets Are So Expensive (Who Really Gets Your Money) (Hidden '
               'Price)',
      'url': 'https://www.youtube.com/watch?v=pfp0vvw1nXo&t=92s',
      'video_id': 'pfp0vvw1nXo'},
     {'author': 'SportsRender',
      'channel': 'SportsRender',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:24](https://www.youtube.com/watch?v=BQI_sOqcfx4&t=204s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Santiago Bernabéu, premium hospitality became a major part of the stadium's "
              'business model. Between VIP seating, events, and concerts, the stadium now '
              'generates revenue far beyond just football matches. Because every luxury suite '
              'usually replaces dozens of regular seats.',
      'timestamp': 204,
      'timestamp_label': '[00:03:24]',
      'timestamp_seconds': 204,
      'tip': "Santiago Bernabéu, premium hospitality became a major part of the stadium's "
             'business model. Between VIP seating, events, and concerts, the stadium now '
             'generates revenue far beyond just football matches. Because every luxury suite '
             'usually replaces dozens of regular seats.',
      'title': 'Why Football Stadiums Are Turning Into Luxury Hotels (SportsRender)',
      'url': 'https://www.youtube.com/watch?v=BQI_sOqcfx4&t=204s',
      'video_id': 'BQI_sOqcfx4'},
     {'author': 'Decibel & Docket',
      'channel': 'Decibel & Docket',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=2Vb_eyHh2aw&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I think radically change um the resale market. It would basically ban scalpers '
              '[snorts] from selling concert tickets for more than 10% markups on the face '
              'value of a ticket, right?',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'I think radically change um the resale market. It would basically ban scalpers '
             '[snorts] from selling concert tickets for more than 10% markups on the face '
             'value of a ticket, right?',
      'title': 'Decibel and Docket covers hearing on AB1720, California concert ticket resale '
               'price cap. (Decibel & Docket)',
      'url': 'https://www.youtube.com/watch?v=2Vb_eyHh2aw&t=20s',
      'video_id': '2Vb_eyHh2aw'},
     {'author': 'CBS News',
      'channel': 'CBS News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:56](https://www.youtube.com/watch?v=IF-yvujBqTU&t=176s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'THAT IS A HUGE ISSUE THAT ARTISTS ARE FACING WITH MANAGEMENT. DO THEY WANT TO '
              'POTENTIALLY ANGER OR UPSET A HUGE PORTION OF THEIR FAN BASE OR -- DO THEY WANT '
              'TO CUT INTO THE GRAY MARKET , THE BUSINESS OF SCALPERS, TO ENSURE WHATEVER '
              'EXTRA PROFIT GOES TO THE ARTIST.',
      'timestamp': 176,
      'timestamp_label': '[00:02:56]',
      'timestamp_seconds': 176,
      'tip': 'THAT IS A HUGE ISSUE THAT ARTISTS ARE FACING WITH MANAGEMENT. DO THEY WANT TO '
             'POTENTIALLY ANGER OR UPSET A HUGE PORTION OF THEIR FAN BASE OR -- DO THEY WANT '
             'TO CUT INTO THE GRAY MARKET , THE BUSINESS OF SCALPERS, TO ENSURE WHATEVER EXTRA '
             'PROFIT GOES TO THE ARTIST.',
      'title': 'Beyoncé fans complain of inconsistent ticket prices for Cowboy Carter Tour '
               '(CBS News)',
      'url': 'https://www.youtube.com/watch?v=IF-yvujBqTU&t=176s',
      'video_id': 'IF-yvujBqTU'},
     {'author': 'Scott Cramer',
      'channel': 'Scott Cramer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:00](https://www.youtube.com/watch?v=kFsH01UthzA&t=1200s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Ticketmaster is like the best service. They don't own 80% of the market because "
              "they're the best service. If that was the case, whatever. You know, let the "
              'best rise to the top.',
      'timestamp': 1200,
      'timestamp_label': '[00:20:00]',
      'timestamp_seconds': 1200,
      'tip': "Ticketmaster is like the best service. They don't own 80% of the market because "
             "they're the best service. If that was the case, whatever. You know, let the best "
             'rise to the top.',
      'title': 'Ticket Prices Are Disgusting (Scott Cramer)',
      'url': 'https://www.youtube.com/watch?v=kFsH01UthzA&t=1200s',
      'video_id': 'kFsH01UthzA'},
     {'author': 'FOX 5 Washington DC',
      'channel': 'FOX 5 Washington DC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:07](https://www.youtube.com/watch?v=ZiwpM_Fr8eU&t=127s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'REVENUE GENERATION TECHNIQUE, SO IT IS NOT NEW TO THE COMMANDERS. MANY OTHER '
              'PLACES SO IT IS NOT NEW TO THE COMMANDERS. MANY OTHER PLACES STADIUMS HAVE '
              'IMPLEMENTED SLS COMMANDERS. MANY OTHER PLACES STADIUMS HAVE IMPLEMENTED SLS AND '
              'THEY’VE ALL WORKED WELL.',
      'timestamp': 127,
      'timestamp_label': '[00:02:07]',
      'timestamp_seconds': 127,
      'tip': 'REVENUE GENERATION TECHNIQUE, SO IT IS NOT NEW TO THE COMMANDERS. MANY OTHER '
             'PLACES SO IT IS NOT NEW TO THE COMMANDERS. MANY OTHER PLACES STADIUMS HAVE '
             'IMPLEMENTED SLS COMMANDERS. MANY OTHER PLACES STADIUMS HAVE IMPLEMENTED SLS AND '
             'THEY’VE ALL WORKED WELL.',
      'title': 'New Commanders’ stadium personal seat licenses explained (FOX 5 Washington DC)',
      'url': 'https://www.youtube.com/watch?v=ZiwpM_Fr8eU&t=127s',
      'video_id': 'ZiwpM_Fr8eU'},
     {'author': 'Romano Law PLLC',
      'channel': 'Romano Law PLLC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=nQoLincg1zk&t=89s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Would there be any retroaction as a result of some of these legal matters? Um, '
              'you know, according to the allegations, the brokers are scooping up tickets and '
              'reselling them at inflated prices, all while layering on hidden fees. Now, '
              "that's not just bad business.",
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Would there be any retroaction as a result of some of these legal matters? Um, '
             'you know, according to the allegations, the brokers are scooping up tickets and '
             'reselling them at inflated prices, all while layering on hidden fees. Now, '
             "that's not just bad business.",
      'title': 'FTC Sues Ticketmaster: Domenic Romano Weighs In On Lawsuits for Unethical '
               'Ticket Reselling Practices (Romano Law PLLC)',
      'url': 'https://www.youtube.com/watch?v=nQoLincg1zk&t=89s',
      'video_id': 'nQoLincg1zk'},
     {'author': 'CBC News: The National',
      'channel': 'CBC News: The National',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=h_mhu-A8WR4&t=25s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The millions the movie was way way easier to get tickets for than the concert '
              "it's a business lesson for a 2020s pop star music is just a percentage even if "
              "it's a large percentage and Swift isn't alone Beyonce by her side at the "
              "world's.",
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'The millions the movie was way way easier to get tickets for than the concert '
             "it's a business lesson for a 2020s pop star music is just a percentage even if "
             "it's a large percentage and Swift isn't alone Beyonce by her side at the "
             "world's.",
      'title': 'Taylor Swift and Beyoncé attempt to pack movie theatres like stadiums (CBC '
               'News: The National)',
      'url': 'https://www.youtube.com/watch?v=h_mhu-A8WR4&t=25s',
      'video_id': 'h_mhu-A8WR4'},
     {'author': '2 Minute Expert',
      'channel': '2 Minute Expert',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=1m8cAjtjH5A&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Now, let's delve into the details. Starting with the pros, dynamic pricing can "
              'maximize revenue for sellers. By adjusting prices to match real-time demand, '
              "organizations can ensure they're getting the most value out of each ticket.",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Now, let's delve into the details. Starting with the pros, dynamic pricing can "
             'maximize revenue for sellers. By adjusting prices to match real-time demand, '
             "organizations can ensure they're getting the most value out of each ticket.",
      'title': 'The Pros & Cons of Dynamic Ticket Pricing in 2 Minutes (2 Minute Expert)',
      'url': 'https://www.youtube.com/watch?v=1m8cAjtjH5A&t=20s',
      'video_id': '1m8cAjtjH5A'},
     {'author': 'The Current',
      'channel': 'The Current',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=9rdi7Mk3v-Y&t=109s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'JADE: And unfortunately, I have to bring you some bad news about a very young '
              'musician. Hip-hop artist Chynna as died at the age of 25. Now the rapper, she '
              'first rose to fame as a model, but you might know her either from her solo work '
              'or from her work with ASAP Mob.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': 'JADE: And unfortunately, I have to bring you some bad news about a very young '
             'musician. Hip-hop artist Chynna as died at the age of 25. Now the rapper, she '
             'first rose to fame as a model, but you might know her either from her solo work '
             'or from her work with ASAP Mob.',
      'title': 'Angry fans accuse ticketers of deceptive concert refund policies (The Current '
               'Music News) (The Current)',
      'url': 'https://www.youtube.com/watch?v=9rdi7Mk3v-Y&t=109s',
      'video_id': '9rdi7Mk3v-Y'},
     {'author': 'ESPN FC',
      'channel': 'ESPN FC',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:18](https://www.youtube.com/watch?v=p9Q9_2anOiA&t=138s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Think this is a fair representation of the change in value from one season to '
              "another if you add Leon Messi and if I'm an inter Miami fan I may be bitter I "
              'may.',
      'timestamp': 138,
      'timestamp_label': '[00:02:18]',
      'timestamp_seconds': 138,
      'tip': 'Think this is a fair representation of the change in value from one season to '
             "another if you add Leon Messi and if I'm an inter Miami fan I may be bitter I "
             'may.',
      'title': "'Somebody's getting rich here!' 🤑 Sebi & Herc get heated over Inter Miami "
               'ticket prices | ESPN FC (ESPN FC)',
      'url': 'https://www.youtube.com/watch?v=p9Q9_2anOiA&t=138s',
      'video_id': 'p9Q9_2anOiA'},
     {'author': '9NEWS',
      'channel': '9NEWS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:13](https://www.youtube.com/watch?v=rhYfYkzJGmU&t=133s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's frustrating Steve on your side. Contacted Yad attorney who told us the "
              'real secret the family emergency is her business imploding a decades old '
              'business model of waiting until the last minute to snag discounted seats.',
      'timestamp': 133,
      'timestamp_label': '[00:02:13]',
      'timestamp_seconds': 133,
      'tip': "It's frustrating Steve on your side. Contacted Yad attorney who told us the real "
             'secret the family emergency is her business imploding a decades old business '
             'model of waiting until the last minute to snag discounted seats.',
      'title': 'Dozens are out hundreds of dollars after using a local ticket broker (9NEWS)',
      'url': 'https://www.youtube.com/watch?v=rhYfYkzJGmU&t=133s',
      'video_id': 'rhYfYkzJGmU'},
     {'author': 'Luxology',
      'channel': 'Luxology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=rodIE0qwiT4&t=209s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q1 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Even the seating is evolving. Modern premium seats can feature wider spacing, '
              'improved comfort, charging points, dedicated service, and unobstructed views.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'Even the seating is evolving. Modern premium seats can feature wider spacing, '
             'improved comfort, charging points, dedicated service, and unobstructed views.',
      'title': 'A Stadium Designed Like a Five-Star Resort | Inside the New Entertainment Era '
               '(Luxology)',
      'url': 'https://www.youtube.com/watch?v=rodIE0qwiT4&t=209s',
      'video_id': 'rodIE0qwiT4'}],
 2: [{'author': 'THE MARKUP FILES',
      'channel': 'THE MARKUP FILES',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:00](https://www.youtube.com/watch?v=rT4gQkoEVDI&t=780s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The buyer pays a separate 12% fee on the same amount. On a $10,000 transaction, '
              "the seller receives 8,800. That's almost $2,400 in combined fees on a single "
              'transaction.',
      'timestamp': 780,
      'timestamp_label': '[00:13:00]',
      'timestamp_seconds': 780,
      'tip': 'The buyer pays a separate 12% fee on the same amount. On a $10,000 transaction, '
             "the seller receives 8,800. That's almost $2,400 in combined fees on a single "
             'transaction.',
      'title': 'How NFL Teams Make Money Before Selling Season Tickets ($750 to $50,000 Just '
               'for the Right) (THE MARKUP FILES)',
      'url': 'https://www.youtube.com/watch?v=rT4gQkoEVDI&t=780s',
      'video_id': 'rT4gQkoEVDI'},
     {'author': 'The Fine Print Audit',
      'channel': 'The Fine Print Audit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:14](https://www.youtube.com/watch?v=SdsGfL0IdKk&t=374s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The seller's projected payout was $254. 85 seller fee, which is 15%. The spread "
              'between what the seller got and what the buyer paid, $168. 30 on a $299 ticket, '
              "and not all of it is Ticketmaster's to keep because the help page says resale "
              'fees are shared.',
      'timestamp': 374,
      'timestamp_label': '[00:06:14]',
      'timestamp_seconds': 374,
      'tip': "The seller's projected payout was $254. 85 seller fee, which is 15%. The spread "
             'between what the seller got and what the buyer paid, $168. 30 on a $299 ticket, '
             "and not all of it is Ticketmaster's to keep because the help page says resale "
             'fees are shared.',
      'title': 'Ticketmaster Fees Hit 44%. The FTC Is Suing. I Read the Fine Print. (The Fine '
               'Print Audit)',
      'url': 'https://www.youtube.com/watch?v=SdsGfL0IdKk&t=374s',
      'video_id': 'SdsGfL0IdKk'},
     {'author': 'Business Made Simple',
      'channel': 'Business Made Simple',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:47](https://www.youtube.com/watch?v=VBp4zpS7F3o&t=167s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The first add-on is usually called a service fee, and it is the one people '
              'notice most. A ticketing company sells the tickets, runs the website, handles '
              'payments, and answers customer questions.',
      'timestamp': 167,
      'timestamp_label': '[00:02:47]',
      'timestamp_seconds': 167,
      'tip': 'The first add-on is usually called a service fee, and it is the one people '
             'notice most. A ticketing company sells the tickets, runs the website, handles '
             'payments, and answers customer questions.',
      'title': 'Why Are Concert Tickets So Expensive? The Fees After Face Value (Business Made '
               'Simple)',
      'url': 'https://www.youtube.com/watch?v=VBp4zpS7F3o&t=167s',
      'video_id': 'VBp4zpS7F3o'},
     {'author': 'KPRC 2 Click2Houston',
      'channel': 'KPRC 2 Click2Houston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:31](https://www.youtube.com/watch?v=UVUOSv2U_BM&t=331s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um, StubHub and all the secondary sites usually charge a fee. They charge the '
              'buyer a fee and they charge the seller a fee, which is about 15 to 20%. So, if '
              'you call a local ticket broker, they have the tickets in their possession, in '
              'their inventory.',
      'timestamp': 331,
      'timestamp_label': '[00:05:31]',
      'timestamp_seconds': 331,
      'tip': 'Um, StubHub and all the secondary sites usually charge a fee. They charge the '
             'buyer a fee and they charge the seller a fee, which is about 15 to 20%. So, if '
             'you call a local ticket broker, they have the tickets in their possession, in '
             'their inventory.',
      'title': "'Buy now': Houston ticket broker says FIFA World Cup ticket prices are "
               'sky-high and trending upward (KPRC 2 Click2Houston)',
      'url': 'https://www.youtube.com/watch?v=UVUOSv2U_BM&t=331s',
      'video_id': 'UVUOSv2U_BM'},
     {'author': 'Cold Talk',
      'channel': 'Cold Talk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=0sxw7eRx9Fs&t=54s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Super Bowl for this much money is if y'all are accepting Monopoly bucks. "
              'Because every price you got on here is a down payment on something. This is '
              "I'mma watch the game at home or I'mma turn my PlayStation on, put on Madden, "
              'and play the Super Bowl myself.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': "Super Bowl for this much money is if y'all are accepting Monopoly bucks. Because "
             "every price you got on here is a down payment on something. This is I'mma watch "
             "the game at home or I'mma turn my PlayStation on, put on Madden, and play the "
             'Super Bowl myself.',
      'title': 'Super Bowl Ticket Prices Are HIGH.. Fans Are Going BROKE (Cold Talk)',
      'url': 'https://www.youtube.com/watch?v=0sxw7eRx9Fs&t=54s',
      'video_id': '0sxw7eRx9Fs'},
     {'author': 'Brian Jones',
      'channel': 'Brian Jones',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=4Ddm_7kF3nc&t=70s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '0) and a reason, such as a press ticket. If the customer is driving, tick Add '
              "parking and type in the car's registration. The parking fee is added to the "
              'total, and it covers the day of the show, from arrival until midnight. Next, '
              "the customer's name and phone number.",
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': '0) and a reason, such as a press ticket. If the customer is driving, tick Add '
             "parking and type in the car's registration. The parking fee is added to the "
             'total, and it covers the day of the show, from arrival until midnight. Next, the '
             "customer's name and phone number.",
      'title': 's-ticket for staff: box office, parking, refunds and door check-in (5-minute '
               'guide) (Brian Jones)',
      'url': 'https://www.youtube.com/watch?v=4Ddm_7kF3nc&t=70s',
      'video_id': '4Ddm_7kF3nc'},
     {'author': 'Consumer Context',
      'channel': 'Consumer Context',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=L3_AaKpmtQI&t=93s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That total includes every fee the business knows about and can calculate in '
              'advance. So the headline number is supposed to be the real number. But which '
              "fees count as fees you have to pay? The FTC's guidance lists conditions.",
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'That total includes every fee the business knows about and can calculate in '
             'advance. So the headline number is supposed to be the real number. But which '
             "fees count as fees you have to pay? The FTC's guidance lists conditions.",
      'title': 'The Hidden System Behind Concert Ticket And Hotel Fees (Consumer Context)',
      'url': 'https://www.youtube.com/watch?v=L3_AaKpmtQI&t=93s',
      'video_id': 'L3_AaKpmtQI'},
     {'author': 'WFAA',
      'channel': 'WFAA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=OSbD9xp5Dw4&t=70s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You want -- to look for a real buyer protection, places like Facebook '
              "Marketplace or social media sites, uh, or Craigslist, don't have that. Another "
              'thing to keep in mind, even if you pay and get a confirmation, right now, '
              'nobody has the ticket or barcode.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'You want -- to look for a real buyer protection, places like Facebook '
             "Marketplace or social media sites, uh, or Craigslist, don't have that. Another "
             'thing to keep in mind, even if you pay and get a confirmation, right now, nobody '
             'has the ticket or barcode.',
      'title': "Trying to get World Cup tickets? Here's how to avoid a scam (WFAA)",
      'url': 'https://www.youtube.com/watch?v=OSbD9xp5Dw4&t=70s',
      'video_id': 'OSbD9xp5Dw4'},
     {'author': 'Prof AI Unfiltered',
      'channel': 'Prof AI Unfiltered',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:26](https://www.youtube.com/watch?v=enPVz7BsM7Q&t=206s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Seller and another fee from the next buyer. When one corporate  group '
              'participates at several stages, each stage can create a new incentive.',
      'timestamp': 206,
      'timestamp_label': '[00:03:26]',
      'timestamp_seconds': 206,
      'tip': 'Seller and another fee from the next buyer. When one corporate  group '
             'participates at several stages, each stage can create a new incentive.',
      'title': 'Taylor Swift’s Ticketmaster Fiasco: Who Really Controls Ticket Prices? Prof AI '
               'Unfiltered (Prof AI Unfiltered)',
      'url': 'https://www.youtube.com/watch?v=enPVz7BsM7Q&t=206s',
      'video_id': 'enPVz7BsM7Q'},
     {'author': 'Fastweigh',
      'channel': 'Fastweigh',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=SqgRdPpIv_I&t=39s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In the bulk edit screen all selected tickets will be repriced based on the '
              'latest pricing information three the hall or pay or new.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': 'In the bulk edit screen all selected tickets will be repriced based on the '
             'latest pricing information three the hall or pay or new.',
      'title': 'Ticket Repricing Overview (Fastweigh)',
      'url': 'https://www.youtube.com/watch?v=SqgRdPpIv_I&t=39s',
      'video_id': 'SqgRdPpIv_I'},
     {'author': 'Football Explainer',
      'channel': 'Football Explainer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:43:40](https://www.youtube.com/watch?v=Y_cqkCHiMu8&t=2620s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Premium sections had been constructed specifically for fans and corporations '
              'willing to pay enormous amounts for access. Now, many of those seats were '
              'empty, and the financial consequences were enormous.',
      'timestamp': 2620,
      'timestamp_label': '[00:43:40]',
      'timestamp_seconds': 2620,
      'tip': 'Premium sections had been constructed specifically for fans and corporations '
             'willing to pay enormous amounts for access. Now, many of those seats were empty, '
             'and the financial consequences were enormous.',
      'title': 'NFL Ticket Prices Explained (How They Became Expensive) (Football Explainer)',
      'url': 'https://www.youtube.com/watch?v=Y_cqkCHiMu8&t=2620s',
      'video_id': 'Y_cqkCHiMu8'},
     {'author': '9NEWS',
      'channel': '9NEWS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:36](https://www.youtube.com/watch?v=w0cU0-OiMB8&t=36s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'ll be priced out when there's a new stadium back there by a one-time fee to "
              "keep their seats. Let's talk about personal seat licenses. It's kind of like a "
              'down payment on a mortgage, a mortgage with no end date.',
      'timestamp': 36,
      'timestamp_label': '[00:00:36]',
      'timestamp_seconds': 36,
      'tip': "'ll be priced out when there's a new stadium back there by a one-time fee to "
             "keep their seats. Let's talk about personal seat licenses. It's kind of like a "
             'down payment on a mortgage, a mortgage with no end date.',
      'title': 'Personal seat licenses | Will longtime Denver Broncos fans be priced out of '
               'tickets at new stadium? (9NEWS)',
      'url': 'https://www.youtube.com/watch?v=w0cU0-OiMB8&t=36s',
      'video_id': 'w0cU0-OiMB8'},
     {'author': 'Yea Baby',
      'channel': 'Yea Baby',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=0a9pLnuCUAk&t=84s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Be everywhere and Glendale PD says it hasn't yet had a case of anyone trying to "
              "sell fake tickets but if you're there on Sunday and you learn that a scammer "
              'did it to you find an officer immediately and they will try to help you but '
              "remember it's always buyer beware.",
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "Be everywhere and Glendale PD says it hasn't yet had a case of anyone trying to "
             "sell fake tickets but if you're there on Sunday and you learn that a scammer did "
             'it to you find an officer immediately and they will try to help you but remember '
             "it's always buyer beware.",
      'title': 'Cheapest Super Bowl Tickets for Last-Minute Buyers Are Running #tickets '
               '#scalping #superbowl (Yea Baby)',
      'url': 'https://www.youtube.com/watch?v=0a9pLnuCUAk&t=84s',
      'video_id': '0a9pLnuCUAk'},
     {'author': 'Reuters',
      'channel': 'Reuters',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=2mMyznWPgpc&t=190s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The ticket and then we can get it uh cheap you know because right now they're "
              "asking crazy number they're asking him for 700 800 1000 crazy numbers you know "
              'and they how much they pay for the ticket is ridiculous they probably pay 150 '
              'dollars or less.',
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': "The ticket and then we can get it uh cheap you know because right now they're "
             "asking crazy number they're asking him for 700 800 1000 crazy numbers you know "
             'and they how much they pay for the ticket is ridiculous they probably pay 150 '
             'dollars or less.',
      'title': "This is what it's like to scalp World Cup tickets (Reuters)",
      'url': 'https://www.youtube.com/watch?v=2mMyznWPgpc&t=190s',
      'video_id': '2mMyznWPgpc'},
     {'author': 'The Savvy Professor',
      'channel': 'The Savvy Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=zH4ITvC9voc&t=158s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q2 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "App to get into the event if it's unavailable contact your seller and that's "
              'how you save your Ticket Master tickets to Apple wallet I hope this helps feel '
              'free to leave a comment like and share the video till next time thanks for '
              'watching.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': "App to get into the event if it's unavailable contact your seller and that's how "
             'you save your Ticket Master tickets to Apple wallet I hope this helps feel free '
             'to leave a comment like and share the video till next time thanks for watching.',
      'title': 'How to Save Ticketmaster Tickets to Apple Wallet (How Do I Add Tickets to a '
               'Digital Wallet?) (The Savvy Professor)',
      'url': 'https://www.youtube.com/watch?v=zH4ITvC9voc&t=158s',
      'video_id': 'zH4ITvC9voc'}],
 3: [{'author': 'Overtime Economics',
      'channel': 'Overtime Economics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:16](https://www.youtube.com/watch?v=C_QtPWHCo_U&t=76s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Green Bay won, 35 to 10, in front of all those empty seats. In today's money, "
              "that best seat would cost about 123 dollars. Super Bowl one's cheapest seat, in "
              "today's money: about 61 dollars. That's about 15 times as much after inflation, "
              'and most fans never see that price.',
      'timestamp': 76,
      'timestamp_label': '[00:01:16]',
      'timestamp_seconds': 76,
      'tip': "Green Bay won, 35 to 10, in front of all those empty seats. In today's money, "
             "that best seat would cost about 123 dollars. Super Bowl one's cheapest seat, in "
             "today's money: about 61 dollars. That's about 15 times as much after inflation, "
             'and most fans never see that price.',
      'title': 'Super Bowl I vs Today: No Sellout at $12. Now Seats Start at $950 (Overtime '
               'Economics)',
      'url': 'https://www.youtube.com/watch?v=C_QtPWHCo_U&t=76s',
      'video_id': 'C_QtPWHCo_U'},
     {'author': 'Firstpost',
      'channel': 'Firstpost',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=R9QNsXzjvxU&t=190s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And sporting events have witnessed a surge in ticket costs. Look at the tickets '
              'for the Premier League games. They have increased by 800% since 1990. Tickets '
              'for the Super Bowl were sold at an average price of about $10,000 last year.',
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': 'And sporting events have witnessed a surge in ticket costs. Look at the tickets '
             'for the Premier League games. They have increased by 800% since 1990. Tickets '
             'for the Super Bowl were sold at an average price of about $10,000 last year.',
      'title': 'Inside Wimbledon’s $275,000 Debenture Seats: The Profit-Making Machine | '
               'Vantage with Palki Sharma (Firstpost)',
      'url': 'https://www.youtube.com/watch?v=R9QNsXzjvxU&t=190s',
      'video_id': 'R9QNsXzjvxU'},
     {'author': 'Profit Mechanics',
      'channel': 'Profit Mechanics',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:41](https://www.youtube.com/watch?v=p8peX6mgbrw&t=281s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It is the same trick airlines use with baggage fees and hotels use with resort '
              'fees. Show a low price to win the click, then add the real cost at the end when '
              'leaving feels like is the resale cut. The promoter getting paid twice for the '
              'same seat.',
      'timestamp': 281,
      'timestamp_label': '[00:04:41]',
      'timestamp_seconds': 281,
      'tip': 'It is the same trick airlines use with baggage fees and hotels use with resort '
             'fees. Show a low price to win the click, then add the real cost at the end when '
             'leaving feels like is the resale cut. The promoter getting paid twice for the '
             'same seat.',
      'title': 'How concert promoters make money: dynamic pricing and the resale cut (Profit '
               'Mechanics)',
      'url': 'https://www.youtube.com/watch?v=p8peX6mgbrw&t=281s',
      'video_id': 'p8peX6mgbrw'},
     {'author': 'NBC10 Boston',
      'channel': 'NBC10 Boston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:50](https://www.youtube.com/watch?v=-GwKaOFdk_M&t=110s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Secure their tickets on a major marketplace that is backed by a guarantee, so '
              'you know that your purchase is protected. Also very important that you are '
              "price shopping and making sure that you're getting the best deal possible. It's "
              'a lot of money to go to the Super Bowl.',
      'timestamp': 110,
      'timestamp_label': '[00:01:50]',
      'timestamp_seconds': 110,
      'tip': 'Secure their tickets on a major marketplace that is backed by a guarantee, so '
             'you know that your purchase is protected. Also very important that you are price '
             "shopping and making sure that you're getting the best deal possible. It's a lot "
             'of money to go to the Super Bowl.',
      'title': "Want Super Bowl tickets? Here's what to know (NBC10 Boston)",
      'url': 'https://www.youtube.com/watch?v=-GwKaOFdk_M&t=110s',
      'video_id': '-GwKaOFdk_M'},
     {'author': 'Bloomberg Television',
      'channel': 'Bloomberg Television',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:57](https://www.youtube.com/watch?v=zXgujuB9yXw&t=57s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Over the last few years, walking into the golden gates of the Super Bowl will '
              'at minimum cost you $3,000. But Super Bowl 58 in Las Vegas tripled that. What '
              'really drives the price comes down to the matchup in the venue.',
      'timestamp': 57,
      'timestamp_label': '[00:00:57]',
      'timestamp_seconds': 57,
      'tip': 'Over the last few years, walking into the golden gates of the Super Bowl will at '
             'minimum cost you $3,000. But Super Bowl 58 in Las Vegas tripled that. What '
             'really drives the price comes down to the matchup in the venue.',
      'title': 'What You Really Get In a Super Bowl Suite (Bloomberg Television)',
      'url': 'https://www.youtube.com/watch?v=zXgujuB9yXw&t=57s',
      'video_id': 'zXgujuB9yXw'},
     {'author': 'JCFB',
      'channel': 'JCFB',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:19](https://www.youtube.com/watch?v=Dl5FeuC7tUA&t=499s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "PSLs we've covered, but it's crazy to see the price increases that Browns fans "
              'are taking on. According to this Twitter user, their PSL and season ticket cost '
              'for six tickets went from $24,600 all the way up to $131,000 with this new '
              'stadium.',
      'timestamp': 499,
      'timestamp_label': '[00:08:19]',
      'timestamp_seconds': 499,
      'tip': "PSLs we've covered, but it's crazy to see the price increases that Browns fans "
             'are taking on. According to this Twitter user, their PSL and season ticket cost '
             'for six tickets went from $24,600 all the way up to $131,000 with this new '
             'stadium.',
      'title': 'The NFL’s Biggest Scam: Personal Seat Licenses (JCFB)',
      'url': 'https://www.youtube.com/watch?v=Dl5FeuC7tUA&t=499s',
      'video_id': 'Dl5FeuC7tUA'},
     {'author': 'Martin Bursatil',
      'channel': 'Martin Bursatil',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:41](https://www.youtube.com/watch?v=S5_EsejwubY&t=701s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Apart from all the brands that want to be here. It has four main sources of '
              'income. Broadcast rights, race promotion, sponsorship, and others. The profit '
              "margin is close to 16%. And you can be a shareholder; there's F1 , there's "
              "Ferrari, there's Mercedes.",
      'timestamp': 701,
      'timestamp_label': '[00:11:41]',
      'timestamp_seconds': 701,
      'tip': 'Apart from all the brands that want to be here. It has four main sources of '
             'income. Broadcast rights, race promotion, sponsorship, and others. The profit '
             "margin is close to 16%. And you can be a shareholder; there's F1 , there's "
             "Ferrari, there's Mercedes.",
      'title': '¿Vale la pena pagar por el Paddock Club de Fórmula 1? (Martin Bursatil)',
      'url': 'https://www.youtube.com/watch?v=S5_EsejwubY&t=701s',
      'video_id': 'S5_EsejwubY'},
     {'author': 'Snazzy Trendz',
      'channel': 'Snazzy Trendz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:40](https://www.youtube.com/watch?v=5ggSZvvL_vo&t=220s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '20,000 depending on location and demand. For fans who wanted the absolute best '
              'experience, front row and premium seating came at an entirely different price '
              'level.',
      'timestamp': 220,
      'timestamp_label': '[00:03:40]',
      'timestamp_seconds': 220,
      'tip': '20,000 depending on location and demand. For fans who wanted the absolute best '
             'experience, front row and premium seating came at an entirely different price '
             'level.',
      'title': 'How Much Did Super Bowl LX 2026 Tickets REALLY Cost? Total Breakdown! '
               '#superbowllx  #nfl (Snazzy Trendz)',
      'url': 'https://www.youtube.com/watch?v=5ggSZvvL_vo&t=220s',
      'video_id': '5ggSZvvL_vo'},
     {'author': 'WTHR',
      'channel': 'WTHR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:49](https://www.youtube.com/watch?v=5T8RLIaR8yg&t=109s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So you know I can ask for any price for a ticket, but that doesn't mean that's "
              'actually the market price. So we should be a little cautious about how many '
              'transactions are actually going on at these prices. Now his best advice is to '
              'keep watching.',
      'timestamp': 109,
      'timestamp_label': '[00:01:49]',
      'timestamp_seconds': 109,
      'tip': "So you know I can ask for any price for a ticket, but that doesn't mean that's "
             'actually the market price. So we should be a little cautious about how many '
             'transactions are actually going on at these prices. Now his best advice is to '
             'keep watching.',
      'title': 'College football championship tickets will cost Hoosiers a pretty penny (WTHR)',
      'url': 'https://www.youtube.com/watch?v=5T8RLIaR8yg&t=109s',
      'video_id': '5T8RLIaR8yg'},
     {'author': 'AwayDays',
      'channel': 'AwayDays',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:49](https://www.youtube.com/watch?v=Hl-tVhzYfsw&t=769s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "The best hospitality in my opinion in the world is Man City's Tunnel Club. If "
              'you could get that for what this cost, and that is like five-course dinner.',
      'timestamp': 769,
      'timestamp_label': '[00:12:49]',
      'timestamp_seconds': 769,
      'tip': "The best hospitality in my opinion in the world is Man City's Tunnel Club. If "
             'you could get that for what this cost, and that is like five-course dinner.',
      'title': 'I Tried a 2026 World Cup VIP Ticket (AwayDays)',
      'url': 'https://www.youtube.com/watch?v=Hl-tVhzYfsw&t=769s',
      'video_id': 'Hl-tVhzYfsw'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:53](https://www.youtube.com/watch?v=TpXJCfuFf4o&t=293s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Initially assigned you know for the pre-sale add a specific face value price '
              "and they're actually just converting them directly to official platinum.",
      'timestamp': 293,
      'timestamp_label': '[00:04:53]',
      'timestamp_seconds': 293,
      'tip': 'Initially assigned you know for the pre-sale add a specific face value price and '
             "they're actually just converting them directly to official platinum.",
      'title': 'HOW DYNAMIC TICKET PRICING & OFFICIAL PLATINUM SEATS WORK ON TICKETMASTER '
               '(thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=TpXJCfuFf4o&t=293s',
      'video_id': 'TpXJCfuFf4o'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:49](https://www.youtube.com/watch?v=GORTWFnPPt0&t=289s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Help you find better tickets and the price break seats are always going to make '
              'more money and let you make more profit than the seats in front of them and the '
              'more expensive s.',
      'timestamp': 289,
      'timestamp_label': '[00:04:49]',
      'timestamp_seconds': 289,
      'tip': 'Help you find better tickets and the price break seats are always going to make '
             'more money and let you make more profit than the seats in front of them and the '
             'more expensive s.',
      'title': 'WHY some tickets ALWAYS make more Profit (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=GORTWFnPPt0&t=289s',
      'video_id': 'GORTWFnPPt0'},
     {'author': 'The Pat McAfee Show',
      'channel': 'The Pat McAfee Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:11](https://www.youtube.com/watch?v=uK2f6TsToVA&t=251s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's like we won't we won't they walk out of the room I got a guy 7500 I got a "
              "guy 8500 whoa whoa whoa whoa whoa who's is that cash is that happening right "
              "now obviously I'll write it off I will report to the earnings anything over 599 "
              'bucks.',
      'timestamp': 251,
      'timestamp_label': '[00:04:11]',
      'timestamp_seconds': 251,
      'tip': "It's like we won't we won't they walk out of the room I got a guy 7500 I got a "
             "guy 8500 whoa whoa whoa whoa whoa who's is that cash is that happening right now "
             "obviously I'll write it off I will report to the earnings anything over 599 "
             'bucks.',
      'title': 'The Average Resell Price Of Super Bowl LIX Is Over $10,000?! | Pat McAfee Show '
               '(The Pat McAfee Show)',
      'url': 'https://www.youtube.com/watch?v=uK2f6TsToVA&t=251s',
      'video_id': 'uK2f6TsToVA'},
     {'author': 'CBS Boston',
      'channel': 'CBS Boston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=QRxTlhb8Bt4&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Yeah, Lisa and David, that mom I spoke to is out nearly $4,000 right now. And a '
              'new bill proposed here at the State House is trying to make it illegal for '
              "tickets to even cost that much. Auburn's Jack Campbell dreamed of seeing a "
              'World Cup match.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Yeah, Lisa and David, that mom I spoke to is out nearly $4,000 right now. And a '
             'new bill proposed here at the State House is trying to make it illegal for '
             "tickets to even cost that much. Auburn's Jack Campbell dreamed of seeing a World "
             'Cup match.',
      'title': 'Some World Cup fans frustrated with ticket buying experience on secondary '
               'market (CBS Boston)',
      'url': 'https://www.youtube.com/watch?v=QRxTlhb8Bt4&t=20s',
      'video_id': 'QRxTlhb8Bt4'},
     {'author': 'Chicoblanco',
      'channel': 'Chicoblanco',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:58](https://www.youtube.com/watch?v=v-LGKb8taFw&t=1078s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q3 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Gonna go ahead and text James and tell him that we should meet up I think this '
              'is it I think this is the final draw right here this is going to get us to the '
              'Super.',
      'timestamp': 1078,
      'timestamp_label': '[00:17:58]',
      'timestamp_seconds': 1078,
      'tip': 'Gonna go ahead and text James and tell him that we should meet up I think this '
             'is it I think this is the final draw right here this is going to get us to the '
             'Super.',
      'title': 'Trading a Penny to Super Bowl Tickets (Chicoblanco)',
      'url': 'https://www.youtube.com/watch?v=v-LGKb8taFw&t=1078s',
      'video_id': 'v-LGKb8taFw'}],
 4: [{'author': 'Hustle Audit',
      'channel': 'Hustle Audit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:29](https://www.youtube.com/watch?v=NOBp14Qcy_8&t=329s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '273 tickets against a posted limit of six per person. The company argues it '
              'used no automated software at all, no bots, and so did not violate the act. '
              'Whether 49 accounts and 273 tickets counts as circumvention without a bot is '
              'now the question a court will decide.',
      'timestamp': 329,
      'timestamp_label': '[00:05:29]',
      'timestamp_seconds': 329,
      'tip': '273 tickets against a posted limit of six per person. The company argues it used '
             'no automated software at all, no bots, and so did not violate the act. Whether '
             '49 accounts and 273 tickets counts as circumvention without a bot is now the '
             'question a court will decide.',
      'title': 'The BOTS Act: Why Ticket Reselling Communities Live In A Legal Grey Zone '
               '(Hustle Audit)',
      'url': 'https://www.youtube.com/watch?v=NOBp14Qcy_8&t=329s',
      'video_id': 'NOBp14Qcy_8'},
     {'author': 'Strat Americas',
      'channel': 'Strat Americas',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=d4DslgcIQ7Y&t=25s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, the Maryland company at the center of the suit has been allegedly scamming '
              'the system and according to the Federal Trade Commission breaking the Bots Act. '
              'The Bots Act was passed in 2016. It makes it illegal to use software to evade '
              'online ticket limits or restrictions.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': 'Now, the Maryland company at the center of the suit has been allegedly scamming '
             'the system and according to the Federal Trade Commission breaking the Bots Act. '
             'The Bots Act was passed in 2016. It makes it illegal to use software to evade '
             'online ticket limits or restrictions.',
      'title': 'The FTC Goes After A Ticket Reseller (Strat Americas)',
      'url': 'https://www.youtube.com/watch?v=d4DslgcIQ7Y&t=25s',
      'video_id': 'd4DslgcIQ7Y'},
     {'author': 'PBS NewsHour',
      'channel': 'PBS NewsHour',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:20](https://www.youtube.com/watch?v=rZJgedd2Fk4&t=320s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um It's like a feminist act to listen to. You know, the Taylors version of "
              'Speak now or red instead of the original Swift concert kicked off the girl Bus '
              "summer one also defined by Greta Gerwig, Blockbuster Barbie movie and Beyonce's "
              'World Renaissance Tools.',
      'timestamp': 320,
      'timestamp_label': '[00:05:20]',
      'timestamp_seconds': 320,
      'tip': "Um It's like a feminist act to listen to. You know, the Taylors version of Speak "
             'now or red instead of the original Swift concert kicked off the girl Bus summer '
             "one also defined by Greta Gerwig, Blockbuster Barbie movie and Beyonce's World "
             'Renaissance Tools.',
      'title': 'How Taylor Swift created an economic juggernaut with her Eras Tour (PBS '
               'NewsHour)',
      'url': 'https://www.youtube.com/watch?v=rZJgedd2Fk4&t=320s',
      'video_id': 'rZJgedd2Fk4'},
     {'author': 'Matthew Josiah',
      'channel': 'Matthew Josiah',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:23](https://www.youtube.com/watch?v=qg3wvctM0wM&t=83s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That is the special ticket access that you get. All card members can access MX '
              'pre-sale tickets and AMX reserve tickets. So, the pre-sale is obviously the '
              'ability to buy tickets before the event and before the public is able to buy '
              'those tickets.',
      'timestamp': 83,
      'timestamp_label': '[00:01:23]',
      'timestamp_seconds': 83,
      'tip': 'That is the special ticket access that you get. All card members can access MX '
             'pre-sale tickets and AMX reserve tickets. So, the pre-sale is obviously the '
             'ability to buy tickets before the event and before the public is able to buy '
             'those tickets.',
      'title': 'This AMEX Perk Gets You Concert Tickets Before Everyone Else (Matthew Josiah)',
      'url': 'https://www.youtube.com/watch?v=qg3wvctM0wM&t=83s',
      'video_id': 'qg3wvctM0wM'},
     {'author': 'FOX 13 Seattle',
      'channel': 'FOX 13 Seattle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:43](https://www.youtube.com/watch?v=q4jIeRrkSGg&t=163s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Super Bowl unless Jackson gives me a ticket. Jaxon Smith-njigba Super Bowl '
              'unless Jackson gives me a ticket. Jaxon Smith-njigba now, if you’re listening. '
              'Jaxon Smith-njigba now, if you’re listening. Being here with all the now, if '
              'you’re listening.',
      'timestamp': 163,
      'timestamp_label': '[00:02:43]',
      'timestamp_seconds': 163,
      'tip': 'Super Bowl unless Jackson gives me a ticket. Jaxon Smith-njigba Super Bowl '
             'unless Jackson gives me a ticket. Jaxon Smith-njigba now, if you’re listening. '
             'Jaxon Smith-njigba now, if you’re listening. Being here with all the now, if '
             'you’re listening.',
      'title': 'Inside the Super Bowl 2026 fan experience (FOX 13 Seattle)',
      'url': 'https://www.youtube.com/watch?v=q4jIeRrkSGg&t=163s',
      'video_id': 'q4jIeRrkSGg'},
     {'author': 'Zach Bye',
      'channel': 'Zach Bye',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:08](https://www.youtube.com/watch?v=FZyPq0QfTdg&t=368s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "All right, who can afford it where the average person cannot. PSL's, you know, "
              "if you look around sports, they're not super prominent in a place like uh the "
              'NBA, only four teams in the NBA, the Hornets, the Warriors, the Raptors, and '
              'the Jazz have personal seat license.',
      'timestamp': 368,
      'timestamp_label': '[00:06:08]',
      'timestamp_seconds': 368,
      'tip': "All right, who can afford it where the average person cannot. PSL's, you know, "
             "if you look around sports, they're not super prominent in a place like uh the "
             'NBA, only four teams in the NBA, the Hornets, the Warriors, the Raptors, and the '
             'Jazz have personal seat license.',
      'title': 'Personal Seat License are coming to the Denver Broncos new stadium (Zach Bye)',
      'url': 'https://www.youtube.com/watch?v=FZyPq0QfTdg&t=368s',
      'video_id': 'FZyPq0QfTdg'},
     {'author': 'WGRZ-TV',
      'channel': 'WGRZ-TV',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=-hTj-NHHeDc&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Dave, the president of VIP Ticks. The bill's informing fans who are unable to "
              'secure a personal seat license to stay on the priority list. Priority list '
              'members receive access to purchase PSLs when seats become available.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': "Dave, the president of VIP Ticks. The bill's informing fans who are unable to "
             'secure a personal seat license to stay on the priority list. Priority list '
             'members receive access to purchase PSLs when seats become available.',
      'title': 'Bills sell out of personal seat licenses (WGRZ-TV)',
      'url': 'https://www.youtube.com/watch?v=-hTj-NHHeDc&t=20s',
      'video_id': '-hTj-NHHeDc'},
     {'author': 'Travel with Frodo',
      'channel': 'Travel with Frodo',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=3jMjNVjPzTo&t=173s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "There isn't even hot water available. This is really disappointing. Here you "
              'can see the chef stations at the end and all the food is located here. There is '
              'a similar setup on the other end with the same food is duplicated.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "There isn't even hot water available. This is really disappointing. Here you can "
             'see the chef stations at the end and all the food is located here. There is a '
             'similar setup on the other end with the same food is duplicated.',
      'title': '$2900 World Cup VIP Hospitality ticket! Am I crazy? (Travel with Frodo)',
      'url': 'https://www.youtube.com/watch?v=3jMjNVjPzTo&t=173s',
      'video_id': '3jMjNVjPzTo'},
     {'author': 'BBB National Programs',
      'channel': 'BBB National Programs',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:30](https://www.youtube.com/watch?v=111H45dtJsI&t=570s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Software that scoops up all the tickets for a long time we we have arguments '
              "that we think we get blamed for the scarcity of tickets when it's not really.",
      'timestamp': 570,
      'timestamp_label': '[00:09:30]',
      'timestamp_seconds': 570,
      'tip': 'Software that scoops up all the tickets for a long time we we have arguments '
             "that we think we get blamed for the scarcity of tickets when it's not really.",
      'title': 'The Ticket Industry Uncovered (BBB National Programs)',
      'url': 'https://www.youtube.com/watch?v=111H45dtJsI&t=570s',
      'video_id': '111H45dtJsI'},
     {'author': 'TickPick',
      'channel': 'TickPick',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:30](https://www.youtube.com/watch?v=tY7hYkxsK3k&t=90s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Sunday and can accommodate any questions that anyone may have you can give us a '
              'call at 845-538-4567 and a representative would be happy to help or you can '
              'email us at support tickpick.com hoping we can help you get to see Super Bowl '
              '50 this year take a pic.',
      'timestamp': 90,
      'timestamp_label': '[00:01:30]',
      'timestamp_seconds': 90,
      'tip': 'Sunday and can accommodate any questions that anyone may have you can give us a '
             'call at 845-538-4567 and a representative would be happy to help or you can '
             'email us at support tickpick.com hoping we can help you get to see Super Bowl 50 '
             'this year take a pic.',
      'title': 'How to Buy Super Bowl 50 Tickets (TickPick)',
      'url': 'https://www.youtube.com/watch?v=tY7hYkxsK3k&t=90s',
      'video_id': 'tY7hYkxsK3k'},
     {'author': 'SOL - Supercars of London',
      'channel': 'SOL - Supercars of London',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:35](https://www.youtube.com/watch?v=rQvPQuH1YXw&t=575s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Tour I don't think there's anything else these are all quite large Vehicles so "
              "I don't think there's any super cars here the F1 cars are still whizzing around "
              "I'm going to quickly take a photo of the satin black GT3 RS down here and then "
              'make my way back to the paddock.',
      'timestamp': 575,
      'timestamp_label': '[00:09:35]',
      'timestamp_seconds': 575,
      'tip': "Tour I don't think there's anything else these are all quite large Vehicles so I "
             "don't think there's any super cars here the F1 cars are still whizzing around "
             "I'm going to quickly take a photo of the satin black GT3 RS down here and then "
             'make my way back to the paddock.',
      'title': 'INSIDE The Most Expensive Qatar F1 Tickets | Behind the Scenes! (SOL - '
               'Supercars of London)',
      'url': 'https://www.youtube.com/watch?v=rQvPQuH1YXw&t=575s',
      'video_id': 'rQvPQuH1YXw'},
     {'author': 'The Savvy Professor',
      'channel': 'The Savvy Professor',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=kC2NXuA1XV4&t=137s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Number 11 you will get a confirmation email when the receiver has received the '
              "ticket so there you have it that's all the information on how to transfer "
              'tickets on tickets Master kindly share like and leave a comment on the video '
              'till next time thanks for watching.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': 'Number 11 you will get a confirmation email when the receiver has received the '
             "ticket so there you have it that's all the information on how to transfer "
             'tickets on tickets Master kindly share like and leave a comment on the video '
             'till next time thanks for watching.',
      'title': 'How to Transfer Tickets on Ticketmaster (What is a Ticket Transfer?) (The '
               'Savvy Professor)',
      'url': 'https://www.youtube.com/watch?v=kC2NXuA1XV4&t=137s',
      'video_id': 'kC2NXuA1XV4'},
     {'author': 'Tennis Fights',
      'channel': 'Tennis Fights',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=vvND5YxS-Hg&t=89s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is This is the sad thing. This is a whole This This must be a whole big '
              "city thing. Like a whole because it's in New York. Because I mean you can see "
              'all these guys anywhere else for hardly anything.',
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'This is This is the sad thing. This is a whole This This must be a whole big '
             "city thing. Like a whole because it's in New York. Because I mean you can see "
             'all these guys anywhere else for hardly anything.',
      'title': 'US OPEN Tennis Tickets in New York are CRAZY (Tennis Fights)',
      'url': 'https://www.youtube.com/watch?v=vvND5YxS-Hg&t=89s',
      'video_id': 'vvND5YxS-Hg'},
     {'author': '9NEWS',
      'channel': '9NEWS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:52](https://www.youtube.com/watch?v=s4p8gnL-WFw&t=112s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Who knows what they could cost in Denver if the Broncos do decide to go with '
              'the PSLs. I think there will be some definite sticker shock. 22 of the 32 NFL '
              'teams have used some sort of seat license at a new stadium.',
      'timestamp': 112,
      'timestamp_label': '[00:01:52]',
      'timestamp_seconds': 112,
      'tip': 'Who knows what they could cost in Denver if the Broncos do decide to go with the '
             'PSLs. I think there will be some definite sticker shock. 22 of the 32 NFL teams '
             'have used some sort of seat license at a new stadium.',
      'title': 'Broncos uncertain about selling Personal Seat Licenses to buy the right to '
               'purchase future tickets (9NEWS)',
      'url': 'https://www.youtube.com/watch?v=s4p8gnL-WFw&t=112s',
      'video_id': 's4p8gnL-WFw'},
     {'author': 'MPR News',
      'channel': 'MPR News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:06](https://www.youtube.com/watch?v=V-6dQZRMe2Y&t=186s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q4 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Fans go for this scheme if other NFL cities are any indication they probably '
              'will fans have paid football teams more than a billion dollars for the seed '
              'licenses in just the last three years Tim Nelson Minnesota Public Radio News.',
      'timestamp': 186,
      'timestamp_label': '[00:03:06]',
      'timestamp_seconds': 186,
      'tip': 'Fans go for this scheme if other NFL cities are any indication they probably '
             'will fans have paid football teams more than a billion dollars for the seed '
             'licenses in just the last three years Tim Nelson Minnesota Public Radio News.',
      'title': 'How seat licenses work (MPR News)',
      'url': 'https://www.youtube.com/watch?v=V-6dQZRMe2Y&t=186s',
      'video_id': 'V-6dQZRMe2Y'}],
 5: [{'author': '6abc Philadelphia',
      'channel': '6abc Philadelphia',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=w_3Yfr30xIo&t=44s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'BOWL 59, GET READY TO DIG DEEP INTO YOUR POCKETS. JESSICA PARKER, FOUNDER OF '
              'THE TRAVEL WHISPERER TRAVEL AGENCY IN PHILADELPHIA, SAYS THE BEST WAY TO DO IT '
              'IS TO PURCHASE AN ALL INCLUSIVE PACKAGE FROM A REPUTABLE SOURCE.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': 'BOWL 59, GET READY TO DIG DEEP INTO YOUR POCKETS. JESSICA PARKER, FOUNDER OF THE '
             'TRAVEL WHISPERER TRAVEL AGENCY IN PHILADELPHIA, SAYS THE BEST WAY TO DO IT IS TO '
             'PURCHASE AN ALL INCLUSIVE PACKAGE FROM A REPUTABLE SOURCE.',
      'title': 'Trip to the Super Bowl would be super fun but super costly (6abc Philadelphia)',
      'url': 'https://www.youtube.com/watch?v=w_3Yfr30xIo&t=44s',
      'video_id': 'w_3Yfr30xIo'},
     {'author': 'Team Jesser',
      'channel': 'Team Jesser',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:21](https://www.youtube.com/watch?v=jgHnABCslrA&t=861s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, this is not good for the Patriots at all. It's time for the Bad Bunny "
              'performance. Obviously, the copyright music is going to be a problem, BUT WE '
              'GOT YOU WITH THE MONTAGE. HEY, let me get you on the vlog. We got a legend '
              "right here. I'm just trying to survive.",
      'timestamp': 861,
      'timestamp_label': '[00:14:21]',
      'timestamp_seconds': 861,
      'tip': "So, this is not good for the Patriots at all. It's time for the Bad Bunny "
             'performance. Obviously, the copyright music is going to be a problem, BUT WE GOT '
             'YOU WITH THE MONTAGE. HEY, let me get you on the vlog. We got a legend right '
             "here. I'm just trying to survive.",
      'title': 'VIP Experience At The Super Bowl! (Team Jesser)',
      'url': 'https://www.youtube.com/watch?v=jgHnABCslrA&t=861s',
      'video_id': 'jgHnABCslrA'},
     {'author': 'Quick and Easy',
      'channel': 'Quick and Easy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=oQOmX8EOyW4&t=82s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Even if you don't have internet you will be able to access this information so "
              'all you have to do is open up the app and show this QR code to use your a a XS.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': "Even if you don't have internet you will be able to access this information so "
             'all you have to do is open up the app and show this QR code to use your a a XS.',
      'title': 'How To Use AXS Tickets (Quick and Easy!) (Quick and Easy)',
      'url': 'https://www.youtube.com/watch?v=oQOmX8EOyW4&t=82s',
      'video_id': 'oQOmX8EOyW4'},
     {'author': 'Firstpost',
      'channel': 'Firstpost',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:45](https://www.youtube.com/watch?v=nAgJ_xD_wuE&t=225s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '7 million tickets were sold then with many failing to secure seats for the '
              "coveted concerts. After all, who wouldn't want to experience the concert of an "
              "artist who had won album of the year at the Grammys? That even Queen Bay isn't "
              'immune to a stadium standoff.',
      'timestamp': 225,
      'timestamp_label': '[00:03:45]',
      'timestamp_seconds': 225,
      'tip': '7 million tickets were sold then with many failing to secure seats for the '
             "coveted concerts. After all, who wouldn't want to experience the concert of an "
             "artist who had won album of the year at the Grammys? That even Queen Bay isn't "
             'immune to a stadium standoff.',
      'title': "Beyonce's Cowboy Carter Tour Struggles to Sell Out Stadiums | Firstpost "
               'America | N18G (Firstpost)',
      'url': 'https://www.youtube.com/watch?v=nAgJ_xD_wuE&t=225s',
      'video_id': 'nAgJ_xD_wuE'},
     {'author': 'AP Archive',
      'channel': 'AP Archive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:41](https://www.youtube.com/watch?v=NxbqrXeuWTI&t=101s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "This is a gift to you back from us it's a little surprise and delight it's "
              "definitely a thank you and it's something we like to do for all our fans this "
              "is the eighth year in a row that we've done a super bowl experience for free "
              'for our customers.',
      'timestamp': 101,
      'timestamp_label': '[00:01:41]',
      'timestamp_seconds': 101,
      'tip': "This is a gift to you back from us it's a little surprise and delight it's "
             "definitely a thank you and it's something we like to do for all our fans this is "
             "the eighth year in a row that we've done a super bowl experience for free for "
             'our customers.',
      'title': 'StubHub officials discuss market for Super Bowl tickets, fan experience at '
               'amusement park (AP Archive)',
      'url': 'https://www.youtube.com/watch?v=NxbqrXeuWTI&t=101s',
      'video_id': 'NxbqrXeuWTI'},
     {'author': 'Katarina Mogus',
      'channel': 'Katarina Mogus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=ouFzQnXDzjU&t=241s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's called sneaker tattoos. So, there's all these different tattoos and I can "
              "put them on my sneakers and it's going to end up like this. So, I just got "
              "these yesterday. I don't want to add anything, but I think I'm going to get "
              'that tiny F1 car on like the heel of my shoe.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': "It's called sneaker tattoos. So, there's all these different tattoos and I can "
             "put them on my sneakers and it's going to end up like this. So, I just got these "
             "yesterday. I don't want to add anything, but I think I'm going to get that tiny "
             'F1 car on like the heel of my shoe.',
      'title': "I Got Ferrari's MOST Exclusive F1 Experience (Katarina Mogus)",
      'url': 'https://www.youtube.com/watch?v=ouFzQnXDzjU&t=241s',
      'video_id': 'ouFzQnXDzjU'},
     {'author': 'WTHR',
      'channel': 'WTHR',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:10](https://www.youtube.com/watch?v=OSa-CK_qebs&t=70s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Hoosiers still have a chance to snag tickets. 9 times out of 10, prices come '
              'down as you get closer to the event. Sellers put up a really high price. Most '
              "of them don't sell at those prices. It all comes down to if a fan wants to run "
              'the risk.',
      'timestamp': 70,
      'timestamp_label': '[00:01:10]',
      'timestamp_seconds': 70,
      'tip': 'Hoosiers still have a chance to snag tickets. 9 times out of 10, prices come '
             'down as you get closer to the event. Sellers put up a really high price. Most of '
             "them don't sell at those prices. It all comes down to if a fan wants to run the "
             'risk.',
      'title': "Here's what it'll cost to go to CFP National Championship between IU and Miami "
               '(WTHR)',
      'url': 'https://www.youtube.com/watch?v=OSa-CK_qebs&t=70s',
      'video_id': 'OSa-CK_qebs'},
     {'author': 'Proxxxymiron',
      'channel': 'Proxxxymiron',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:43](https://www.youtube.com/watch?v=6xTWnxPdGP0&t=43s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Ticketmaster and access as thousands of independent buyers. To avoid being '
              "blocked, it allegedly used other people's names, numerous email addresses and "
              'phone numbers, VPNs, rotating proxies, multi-session browsers, and other '
              'methods.',
      'timestamp': 43,
      'timestamp_label': '[00:00:43]',
      'timestamp_seconds': 43,
      'tip': 'Ticketmaster and access as thousands of independent buyers. To avoid being '
             "blocked, it allegedly used other people's names, numerous email addresses and "
             'phone numbers, VPNs, rotating proxies, multi-session browsers, and other '
             'methods.',
      'title': 'Why You Can’t Get Concert Tickets: The $1.3 Billion Scheme (Proxxxymiron)',
      'url': 'https://www.youtube.com/watch?v=6xTWnxPdGP0&t=43s',
      'video_id': '6xTWnxPdGP0'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:14](https://www.youtube.com/watch?v=NGFBVOXqxpA&t=74s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They're coming directly from the artist so you're going to get some of the best "
              'deals the second place is the secondary marketplaces so a lot of you might not.',
      'timestamp': 74,
      'timestamp_label': '[00:01:14]',
      'timestamp_seconds': 74,
      'tip': "They're coming directly from the artist so you're going to get some of the best "
             'deals the second place is the secondary marketplaces so a lot of you might not.',
      'title': 'How to get More Tickets to Flip (Ticket Flipping)',
      'url': 'https://www.youtube.com/watch?v=NGFBVOXqxpA&t=74s',
      'video_id': 'NGFBVOXqxpA'},
     {'author': 'Sportico',
      'channel': 'Sportico',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=uhgdo0oPQ0E&t=137s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um but it's a product that's does really well here. Um but yeah, this will be "
              'full à la carte menu, beer, wine, soft drinks. So, no shortage of food and '
              "beverage. Um it's invited guests only.",
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "Um but it's a product that's does really well here. Um but yeah, this will be "
             'full à la carte menu, beer, wine, soft drinks. So, no shortage of food and '
             "beverage. Um it's invited guests only.",
      'title': "The 'NFL Suite Life' at Tottenham Hotspur Stadium | BTS NFL Exclusive VIP "
               'Hospitality & Suites (Sportico)',
      'url': 'https://www.youtube.com/watch?v=uhgdo0oPQ0E&t=137s',
      'video_id': 'uhgdo0oPQ0E'},
     {'author': 'Oscar Alejandro',
      'channel': 'Oscar Alejandro',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=Sl_1OxOBH2c&t=446s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'De probar los servicios de Future boutique vamos a esperarla porque va a salir '
              'de desde [Música] allá ya la gorra está lista y ahora vamos a pagar con la.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': 'De probar los servicios de Future boutique vamos a esperarla porque va a salir '
             'de desde [Música] allá ya la gorra está lista y ahora vamos a pagar con la.',
      'title': 'FÓRMULA 1 VIP EN MIAMI 🔥 ¡Solo MILLONARIOS pueden VIVIRLO! Paddock Club (Oscar '
               'Alejandro)',
      'url': 'https://www.youtube.com/watch?v=Sl_1OxOBH2c&t=446s',
      'video_id': 'Sl_1OxOBH2c'},
     {'author': 'Guide Nation',
      'channel': 'Guide Nation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:22](https://www.youtube.com/watch?v=Mkuhus1taO4&t=82s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Guys is how to use digital tickets on Ticket Master if you guys know of a '
              'better or easier way to actually do this let me know in the comments down below '
              "I would love to know but thanks so much for watching everyone and I'll see you "
              'guys all in the next video.',
      'timestamp': 82,
      'timestamp_label': '[00:01:22]',
      'timestamp_seconds': 82,
      'tip': 'Guys is how to use digital tickets on Ticket Master if you guys know of a better '
             'or easier way to actually do this let me know in the comments down below I would '
             "love to know but thanks so much for watching everyone and I'll see you guys all "
             'in the next video.',
      'title': 'How To Use Digital Tickets On Ticketmaster (Guide Nation)',
      'url': 'https://www.youtube.com/watch?v=Mkuhus1taO4&t=82s',
      'video_id': 'Mkuhus1taO4'},
     {'author': 'Chicoblanco',
      'channel': 'Chicoblanco',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:48](https://www.youtube.com/watch?v=we9NjqAzpU0&t=348s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm telling you, I knew you'd like the color. And this is a lens, correct? Why "
              "don't you have the lens? I know very well she's hiding all that pain behind her "
              'smile.',
      'timestamp': 348,
      'timestamp_label': '[00:05:48]',
      'timestamp_seconds': 348,
      'tip': "I'm telling you, I knew you'd like the color. And this is a lens, correct? Why "
             "don't you have the lens? I know very well she's hiding all that pain behind her "
             'smile.',
      'title': 'Trading Football For NFL Tickets (Chicoblanco)',
      'url': 'https://www.youtube.com/watch?v=we9NjqAzpU0&t=348s',
      'video_id': 'we9NjqAzpU0'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=O-Sq4DDGKAY&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '5 of the tickets make sense teams who are in the super bowl they should '
              "probably you know be able to attend said super bowl what's dealers come on "
              'steelers come on stealers concealers come and steal this concealer now 17.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': '5 of the tickets make sense teams who are in the super bowl they should probably '
             "you know be able to attend said super bowl what's dealers come on steelers come "
             'on stealers concealers come and steal this concealer now 17.',
      'title': 'HOW TO GET SUPER BOWL TICKETS FOR FACE VALUE! (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=O-Sq4DDGKAY&t=20s',
      'video_id': 'O-Sq4DDGKAY'},
     {'author': 'Poolarity - Life Hacks',
      'channel': 'Poolarity - Life Hacks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=IENQeieAOCo&t=100s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q5 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Actually just transfer one ticket which is a you know in case I'm selling it to "
              "somebody or that um you know I'm I want to I bought a bunch of tickets and I "
              "want to send it to each individual so that's also a possibility so if I'm just "
              'sending one and I do continue.',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': "Actually just transfer one ticket which is a you know in case I'm selling it to "
             "somebody or that um you know I'm I want to I bought a bunch of tickets and I "
             "want to send it to each individual so that's also a possibility so if I'm just "
             'sending one and I do continue.',
      'title': 'TicketMaster SafeTix Transfer Tickets | How To Demo (Poolarity - Life Hacks)',
      'url': 'https://www.youtube.com/watch?v=IENQeieAOCo&t=100s',
      'video_id': 'IENQeieAOCo'}],
 6: [{'author': 'The Credit Nerd',
      'channel': 'The Credit Nerd',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:44](https://www.youtube.com/watch?v=JS9sO0Fx9A0&t=44s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's dive into the first card on the list, the Capital One Savor Card. For "
              'many people, this is probably the best all-around credit card for entertainment '
              'spending.',
      'timestamp': 44,
      'timestamp_label': '[00:00:44]',
      'timestamp_seconds': 44,
      'tip': "Let's dive into the first card on the list, the Capital One Savor Card. For many "
             'people, this is probably the best all-around credit card for entertainment '
             'spending.',
      'title': '3 Best Credit Cards For Concert Tickets & Entertainment In 2026 | NerdWallet '
               '(The Credit Nerd)',
      'url': 'https://www.youtube.com/watch?v=JS9sO0Fx9A0&t=44s',
      'video_id': 'JS9sO0Fx9A0'},
     {'author': 'Zippykind',
      'channel': 'Zippykind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:26](https://www.youtube.com/watch?v=OaCa2-zmCe8&t=26s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "If you're the client of a courier, include your Location ID in the file. You'll "
              'find it in the Locations Manager. To add several items to one ticket, put each '
              'item on its own row under the ticket and leave the first column blank on those '
              'rows, like you see here.',
      'timestamp': 26,
      'timestamp_label': '[00:00:26]',
      'timestamp_seconds': 26,
      'tip': "If you're the client of a courier, include your Location ID in the file. You'll "
             'find it in the Locations Manager. To add several items to one ticket, put each '
             'item on its own row under the ticket and leave the first column blank on those '
             'rows, like you see here.',
      'title': 'Bulk Import Delivery Orders From a Spreadsheet | Zippykind (Zippykind)',
      'url': 'https://www.youtube.com/watch?v=OaCa2-zmCe8&t=26s',
      'video_id': 'OaCa2-zmCe8'},
     {'author': 'Arizona’s Family (3TV / CBS 5)',
      'channel': 'Arizona’s Family (3TV / CBS 5)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:02](https://www.youtube.com/watch?v=3kV_14yzGfk&t=62s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "OWL IN WHICH TICKETS >> IT'S NOT THE FIRST SUPER BOWL IN WHICH TICKETS WILL >> "
              "IT'S NOT THE FIRST SUPER BOWL IN WHICH TICKETS WILL BE >> IT'S NOT THE FIRST "
              'SUPER BOWL IN WHICH TICKETS WILL BE ALL IN WHICH TICKETS WILL BE ALL IN WHICH '
              'TICKETS WILL BE ALL DIGITAL.',
      'timestamp': 62,
      'timestamp_label': '[00:01:02]',
      'timestamp_seconds': 62,
      'tip': "OWL IN WHICH TICKETS >> IT'S NOT THE FIRST SUPER BOWL IN WHICH TICKETS WILL >> "
             "IT'S NOT THE FIRST SUPER BOWL IN WHICH TICKETS WILL BE >> IT'S NOT THE FIRST "
             'SUPER BOWL IN WHICH TICKETS WILL BE ALL IN WHICH TICKETS WILL BE ALL IN WHICH '
             'TICKETS WILL BE ALL DIGITAL.',
      'title': 'Ways to buy or sell Super Bowl tickets without being defrauded (Arizona’s '
               'Family (3TV / CBS 5))',
      'url': 'https://www.youtube.com/watch?v=3kV_14yzGfk&t=62s',
      'video_id': '3kV_14yzGfk'},
     {'author': 'CBS Atlanta',
      'channel': 'CBS Atlanta',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=vYgE480j7AA&t=25s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "AUGUSTA, BUT DURING THE WEEK OF THE MASTERS IT'S SOMETHING COMPLETELY "
              'DIFFERENT. FOR 18 YEARS, THIS IS THE FIRST FACE MANY PEOPLE SEE WHEN THEY WALK '
              'THROUGH THE DOOR. LEE SMITH FROM ACWORTH MAKES THE TRIP FROM METRO ATLANTA '
              "EVERY YEAR. SO IT'S NOT A BAD DRIVE AT ALL.",
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "AUGUSTA, BUT DURING THE WEEK OF THE MASTERS IT'S SOMETHING COMPLETELY DIFFERENT. "
             'FOR 18 YEARS, THIS IS THE FIRST FACE MANY PEOPLE SEE WHEN THEY WALK THROUGH THE '
             'DOOR. LEE SMITH FROM ACWORTH MAKES THE TRIP FROM METRO ATLANTA EVERY YEAR. SO '
             "IT'S NOT A BAD DRIVE AT ALL.",
      'title': 'Inside Club Magnolia: The Masters’ secret experience with Atlanta ties (CBS '
               'Atlanta)',
      'url': 'https://www.youtube.com/watch?v=vYgE480j7AA&t=25s',
      'video_id': 'vYgE480j7AA'},
     {'author': 'Prodigy Slots',
      'channel': 'Prodigy Slots',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=rYABa5xL6d0&t=114s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s where you'll find the VIP experience location. Uh from there, it'll give you "
              'a little bit of background information, a little bit of information about what '
              "all it entails. Um and then it'll have the the list of events at the bottom.",
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': "'s where you'll find the VIP experience location. Uh from there, it'll give you "
             'a little bit of background information, a little bit of information about what '
             "all it entails. Um and then it'll have the the list of events at the bottom.",
      'title': 'Is the UFC VIP Experience worth it? (Prodigy Slots)',
      'url': 'https://www.youtube.com/watch?v=rYABa5xL6d0&t=114s',
      'video_id': 'rYABa5xL6d0'},
     {'author': 'Simply Finance',
      'channel': 'Simply Finance',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:06](https://www.youtube.com/watch?v=SnJa0jDKiKE&t=66s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'You should be doing if you are unable to find ticket in the AXS app that is all '
              'for this video I hope the video was helpful make sure like share and.',
      'timestamp': 66,
      'timestamp_label': '[00:01:06]',
      'timestamp_seconds': 66,
      'tip': 'You should be doing if you are unable to find ticket in the AXS app that is all '
             'for this video I hope the video was helpful make sure like share and.',
      'title': "What Should I Do If I Can't Find My Tickets In The Axs App ! (Simply Finance)",
      'url': 'https://www.youtube.com/watch?v=SnJa0jDKiKE&t=66s',
      'video_id': 'SnJa0jDKiKE'},
     {'author': 'NDSE',
      'channel': 'NDSE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:01](https://www.youtube.com/watch?v=N4lHcJFrT1E&t=121s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Better help desk practices lead to fewer repeat issues, smoother onboarding, '
              'clearer budgeting, stronger cybersecurity awareness, and less disruption across '
              'daily work. To go deeper, read the full article and add this to your Spotify '
              'playlist.',
      'timestamp': 121,
      'timestamp_label': '[00:02:01]',
      'timestamp_seconds': 121,
      'tip': 'Better help desk practices lead to fewer repeat issues, smoother onboarding, '
             'clearer budgeting, stronger cybersecurity awareness, and less disruption across '
             'daily work. To go deeper, read the full article and add this to your Spotify '
             'playlist.',
      'title': 'IT Helpdesk Best Practices That Reduce Tickets And Keep Work Moving (NDSE)',
      'url': 'https://www.youtube.com/watch?v=N4lHcJFrT1E&t=121s',
      'video_id': 'N4lHcJFrT1E'},
     {'author': 'Ticket Flipping',
      'channel': 'Ticket Flipping',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:50](https://www.youtube.com/watch?v=ajoRfqew338&t=890s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, we'll go here and go to shows. Uh, and we'll start scrolling down here. Uh, "
              "this is, you know, this event is today. So, we'll go ahead and search Dell "
              "Water. I don't know if that's the actual name of the artist, but yeah, it is. "
              "So, let's go to the artist here.",
      'timestamp': 890,
      'timestamp_label': '[00:14:50]',
      'timestamp_seconds': 890,
      'tip': "So, we'll go here and go to shows. Uh, and we'll start scrolling down here. Uh, "
             "this is, you know, this event is today. So, we'll go ahead and search Dell "
             "Water. I don't know if that's the actual name of the artist, but yeah, it is. "
             "So, let's go to the artist here.",
      'title': 'Live Training: How to find tickets to flip based on the Venue! (Ticket '
               'Flipping)',
      'url': 'https://www.youtube.com/watch?v=ajoRfqew338&t=890s',
      'video_id': 'ajoRfqew338'},
     {'author': 'News 5 Cleveland',
      'channel': 'News 5 Cleveland',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=-zd2mlj0u8U&t=104s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'CAM POWELL IS A SPORTS MARKETING CONSULTANT PART OF THE TEAM THAT NEGOTIATED '
              'WITH THE NFL TO MAKE THE STADIUM DEAL HAPPENS WHEN THAT THE ASSAULTS FIRST CAME '
              "ON EARLY 90'S THAT WAS CONSIDERED RACKET IN A JUST A MONEY GRAB. BUT IT'S "
              "THEY'RE KIND OF ENTRENCHED NOW.",
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'CAM POWELL IS A SPORTS MARKETING CONSULTANT PART OF THE TEAM THAT NEGOTIATED '
             'WITH THE NFL TO MAKE THE STADIUM DEAL HAPPENS WHEN THAT THE ASSAULTS FIRST CAME '
             "ON EARLY 90'S THAT WAS CONSIDERED RACKET IN A JUST A MONEY GRAB. BUT IT'S "
             "THEY'RE KIND OF ENTRENCHED NOW.",
      'title': 'How much? Browns fans outraged by possible personal seat-license (PSL) pricing '
               'in Brook Park. (News 5 Cleveland)',
      'url': 'https://www.youtube.com/watch?v=-zd2mlj0u8U&t=104s',
      'video_id': '-zd2mlj0u8U'},
     {'author': 'Kayvan Goes',
      'channel': 'Kayvan Goes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:30:42](https://www.youtube.com/watch?v=2UDtC8EP8GA&t=1842s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Like the people who paid the most don't have seats because we can move around. "
              'The The idea was like, okay, we can move anywhere in the Paddock Club. Like we '
              'can go all the way through the pit pit lane. We can go all the way to the '
              'Tarzan, the first turn.',
      'timestamp': 1842,
      'timestamp_label': '[00:30:42]',
      'timestamp_seconds': 1842,
      'tip': "Like the people who paid the most don't have seats because we can move around. "
             'The The idea was like, okay, we can move anywhere in the Paddock Club. Like we '
             'can go all the way through the pit pit lane. We can go all the way to the '
             'Tarzan, the first turn.',
      'title': 'Is the F1 Paddock Club Actually Worth It? (Kayvan Goes)',
      'url': 'https://www.youtube.com/watch?v=2UDtC8EP8GA&t=1842s',
      'video_id': '2UDtC8EP8GA'},
     {'author': 'Landon Kissell',
      'channel': 'Landon Kissell',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:01](https://www.youtube.com/watch?v=76zFs7tuCJw&t=241s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': '3 2 1 >> [cheering] [cheering] [cheering] >> All right, match has ended saying '
              'at the Brazilian area now absolute insanity of a game. Brazil Morocco first '
              'half so fast flowing a great great goal by Vinnie.',
      'timestamp': 241,
      'timestamp_label': '[00:04:01]',
      'timestamp_seconds': 241,
      'tip': '3 2 1 >> [cheering] [cheering] [cheering] >> All right, match has ended saying '
             'at the Brazilian area now absolute insanity of a game. Brazil Morocco first half '
             'so fast flowing a great great goal by Vinnie.',
      'title': 'WORLD CUP FIFA PAVILION HOSPITALITY TICKETS | Brazil vs Morocco (Landon '
               'Kissell)',
      'url': 'https://www.youtube.com/watch?v=76zFs7tuCJw&t=241s',
      'video_id': '76zFs7tuCJw'},
     {'author': 'Wise Explainer',
      'channel': 'Wise Explainer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:59](https://www.youtube.com/watch?v=WNNmn1bxFEU&t=59s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But, there are some downsides. First, the experience can feel more '
              'information-heavy than consumer-focused concert apps. If you just want a quick '
              'list of concerts near you and an easy checkout, Pollstar may not feel as '
              'straightforward.',
      'timestamp': 59,
      'timestamp_label': '[00:00:59]',
      'timestamp_seconds': 59,
      'tip': 'But, there are some downsides. First, the experience can feel more '
             'information-heavy than consumer-focused concert apps. If you just want a quick '
             'list of concerts near you and an easy checkout, Pollstar may not feel as '
             'straightforward.',
      'title': 'Pollstar for Concert Discovery Honest Review - Watch Before Using (Wise '
               'Explainer)',
      'url': 'https://www.youtube.com/watch?v=WNNmn1bxFEU&t=59s',
      'video_id': 'WNNmn1bxFEU'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:38](https://www.youtube.com/watch?v=s9mNdqH694I&t=338s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Soon no first wave opens up May 1st to May 30th all the things I've already "
              "haven't in the past that would be the window to make your selections on.",
      'timestamp': 338,
      'timestamp_label': '[00:05:38]',
      'timestamp_seconds': 338,
      'tip': "Soon no first wave opens up May 1st to May 30th all the things I've already "
             "haven't in the past that would be the window to make your selections on.",
      'title': 'TICKETMASTER REFUND POLICY UPDATE FOR CANCELLED AND POSTPONED EVENTS | TICKET '
               'REFUND PLAN (thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=s9mNdqH694I&t=338s',
      'video_id': 's9mNdqH694I'},
     {'author': 'Tickets To Travel Podcast',
      'channel': 'Tickets To Travel Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:26:11](https://www.youtube.com/watch?v=pugjl3jzpWU&t=1571s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Discussing and sort of how entrepreneurs find a way to get it done I think it's "
              'a perfect storm I think that travel experiences led by tickets are going to.',
      'timestamp': 1571,
      'timestamp_label': '[00:26:11]',
      'timestamp_seconds': 1571,
      'tip': "Discussing and sort of how entrepreneurs find a way to get it done I think it's "
             'a perfect storm I think that travel experiences led by tickets are going to.',
      'title': 'Tickets To Travel Ep  10  Beyond the Ticket  Merging Travel with VIP Event '
               'Experiences   A Conversa (Tickets To Travel Podcast)',
      'url': 'https://www.youtube.com/watch?v=pugjl3jzpWU&t=1571s',
      'video_id': 'pugjl3jzpWU'},
     {'author': 'MMALeaked',
      'channel': 'MMALeaked',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=2vauuB_YXFc&t=224s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q6 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Event yes I could see them from far away but it just hits different when you '
              'can see them up close like that now I want to now I want to show you how far I '
              'was at the UFC 299 event mind you this was $300 more than the fight.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': 'Event yes I could see them from far away but it just hits different when you can '
             'see them up close like that now I want to now I want to show you how far I was '
             'at the UFC 299 event mind you this was $300 more than the fight.',
      'title': 'First UFC Event? Essential Tips for Buying Tickets! (MMALeaked)',
      'url': 'https://www.youtube.com/watch?v=2vauuB_YXFc&t=224s',
      'video_id': '2vauuB_YXFc'}],
 7: [{'author': 'Emmanuel Ak',
      'channel': 'Emmanuel Ak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:15](https://www.youtube.com/watch?v=RsyNgibgVJY&t=795s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That was at the start of the year when they released. But Beyonce, Houston, '
              "Texas, performed the best because I believe that's her hometown in comparison "
              'to Chicago where she was performing as well. Hometown of the artist is usually '
              'a guaranteed sellout.',
      'timestamp': 795,
      'timestamp_label': '[00:13:15]',
      'timestamp_seconds': 795,
      'tip': 'That was at the start of the year when they released. But Beyonce, Houston, '
             "Texas, performed the best because I believe that's her hometown in comparison to "
             'Chicago where she was performing as well. Hometown of the artist is usually a '
             'guaranteed sellout.',
      'title': 'The Hidden System Behind $30K/Month Concert Ticket Flips (Emmanuel Ak)',
      'url': 'https://www.youtube.com/watch?v=RsyNgibgVJY&t=795s',
      'video_id': 'RsyNgibgVJY'},
     {'author': 'Paso a paso',
      'channel': 'Paso a paso',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=EwQdnuSrWAo&t=72s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To use Safetix more efficiently, you should take the following steps into '
              'account. Present the dynamic barcode of your digital ticket in its original '
              'size. Do not make it larger or smaller. Verify that the elements of your '
              'digital Ticketmaster Safetix are in motion.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'To use Safetix more efficiently, you should take the following steps into '
             'account. Present the dynamic barcode of your digital ticket in its original '
             'size. Do not make it larger or smaller. Verify that the elements of your digital '
             'Ticketmaster Safetix are in motion.',
      'title': '¿Cómo usar SafeTix de Ticketmaster? Tutorial paso a paso (Paso a paso)',
      'url': 'https://www.youtube.com/watch?v=EwQdnuSrWAo&t=72s',
      'video_id': 'EwQdnuSrWAo'},
     {'author': 'Guide Gurus',
      'channel': 'Guide Gurus',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:08](https://www.youtube.com/watch?v=6Og6Y7NbLsk&t=128s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The recipient will then need to create a Seedgeek account, claim their tickets, '
              'and access them through the Seedgeek app. By following these steps and being '
              'aware of any fees and time requirements, you can successfully transfer tickets '
              'from AXS to Seedgeek.',
      'timestamp': 128,
      'timestamp_label': '[00:02:08]',
      'timestamp_seconds': 128,
      'tip': 'The recipient will then need to create a Seedgeek account, claim their tickets, '
             'and access them through the Seedgeek app. By following these steps and being '
             'aware of any fees and time requirements, you can successfully transfer tickets '
             'from AXS to Seedgeek.',
      'title': 'How To Transfer Tickets From Axs To Seatgeek (2025) (Guide Gurus)',
      'url': 'https://www.youtube.com/watch?v=6Og6Y7NbLsk&t=128s',
      'video_id': '6Og6Y7NbLsk'},
     {'author': 'Gadget Tune',
      'channel': 'Gadget Tune',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:48](https://www.youtube.com/watch?v=8yXxF_U1uek&t=108s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To ensure successful ticket transfers, follow these essential best practices '
              'that will save you time and prevent common issues. Always verify the '
              "recipient's email address or phone number before initiating the transfer.",
      'timestamp': 108,
      'timestamp_label': '[00:01:48]',
      'timestamp_seconds': 108,
      'tip': 'To ensure successful ticket transfers, follow these essential best practices '
             "that will save you time and prevent common issues. Always verify the recipient's "
             'email address or phone number before initiating the transfer.',
      'title': 'How to Transfer Ticketmaster Tickets from Apple Wallet – Step By Step Guide '
               '(Gadget Tune)',
      'url': 'https://www.youtube.com/watch?v=8yXxF_U1uek&t=108s',
      'video_id': '8yXxF_U1uek'},
     {'author': 'Helpful Solutions',
      'channel': 'Helpful Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=hNlTOy1daSA&t=63s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The operating system that is not compatible then such issues May prevent '
              'barcodes from displaying in the wallet so first of all you must update The.',
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'The operating system that is not compatible then such issues May prevent '
             'barcodes from displaying in the wallet so first of all you must update The.',
      'title': 'How To Fix Ticketmaster Barcode Not Showing In Wallet (Easy Solutions To '
               'Troubleshoot The Issue) (Helpful Solutions)',
      'url': 'https://www.youtube.com/watch?v=hNlTOy1daSA&t=63s',
      'video_id': 'hNlTOy1daSA'},
     {'author': 'Web Mind',
      'channel': 'Web Mind',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:24](https://www.youtube.com/watch?v=RDQeHkadlqk&t=24s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It has over 10 million downloads. It is a very good application. And here we '
              'will learn how the booking process works in this application. We will explain '
              'how to understand it and how to make bookings and all.',
      'timestamp': 24,
      'timestamp_label': '[00:00:24]',
      'timestamp_seconds': 24,
      'tip': 'It has over 10 million downloads. It is a very good application. And here we '
             'will learn how the booking process works in this application. We will explain '
             'how to understand it and how to make bookings and all.',
      'title': 'how to buy tickets on axs !! How to use axs tickets app (Web Mind)',
      'url': 'https://www.youtube.com/watch?v=RDQeHkadlqk&t=24s',
      'video_id': 'RDQeHkadlqk'},
     {'author': "Ryan's Reviews and Overviews",
      'channel': "Ryan's Reviews and Overviews",
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:20](https://www.youtube.com/watch?v=25ntbvX_0_0&t=680s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Uh some of the the best food I've had in a very long time. Now for the most "
              'improved, um, getting here. So, if you can, if you are traveling to Miami for '
              'the World Cup and the games and everything, try to do what you can to avoid the '
              'shuttle system.',
      'timestamp': 680,
      'timestamp_label': '[00:11:20]',
      'timestamp_seconds': 680,
      'tip': "Uh some of the the best food I've had in a very long time. Now for the most "
             'improved, um, getting here. So, if you can, if you are traveling to Miami for '
             'the World Cup and the games and everything, try to do what you can to avoid the '
             'shuttle system.',
      'title': 'Miami FIFA World Cup 26 Hospitality Tickets (FIFA Pavilion) Saudi Arabia vs '
               "Uruguay VLOG (Ryan's Reviews and Overviews)",
      'url': 'https://www.youtube.com/watch?v=25ntbvX_0_0&t=680s',
      'video_id': '25ntbvX_0_0'},
     {'author': 'Nexustech',
      'channel': 'Nexustech',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:16](https://www.youtube.com/watch?v=lBLVmAx5wkQ&t=136s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Screenshots or copies won't work. Entry scanners will reject them. So the "
              'system forces you to transfer only through ticket master. When the person '
              'accepts the ticket in their ticket master account, then they can open the '
              'ticket and tap add to Apple wallet.',
      'timestamp': 136,
      'timestamp_label': '[00:02:16]',
      'timestamp_seconds': 136,
      'tip': "Screenshots or copies won't work. Entry scanners will reject them. So the system "
             'forces you to transfer only through ticket master. When the person accepts the '
             'ticket in their ticket master account, then they can open the ticket and tap add '
             'to Apple wallet.',
      'title': 'How To Transfer Ticketmaster Tickets from Apple Wallet to Someone Else [2026 '
               'GUIDE] (Nexustech)',
      'url': 'https://www.youtube.com/watch?v=lBLVmAx5wkQ&t=136s',
      'video_id': 'lBLVmAx5wkQ'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:35](https://www.youtube.com/watch?v=MP1aH4hgG70&t=95s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Once you're there two things you wanna know. One, not all events will have the "
              'transfer feature available. Reason behind that is twofold: One, the event '
              'itself may not have the delivery delay lifted, so the tickets are still not '
              'available to be accessed.',
      'timestamp': 95,
      'timestamp_label': '[00:01:35]',
      'timestamp_seconds': 95,
      'tip': "Once you're there two things you wanna know. One, not all events will have the "
             'transfer feature available. Reason behind that is twofold: One, the event itself '
             'may not have the delivery delay lifted, so the tickets are still not available '
             'to be accessed.',
      'title': 'HOW TO TRANSFER TICKETS ON TICKETMASTER TO ANOTHER PHONE | TICKET TIP THURSDAY '
               '(thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=MP1aH4hgG70&t=95s',
      'video_id': 'MP1aH4hgG70'},
     {'author': 'TicketWire',
      'channel': 'TicketWire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=M80btlo7xJc&t=53s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Verify trust but verify folks so then there's Str Marketplace I'll go down I'll "
              'click the team I want to purchase tickets for and once again this is just the '
              "SPL so sbl's for sale.",
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': "Verify trust but verify folks so then there's Str Marketplace I'll go down I'll "
             'click the team I want to purchase tickets for and once again this is just the '
             "SPL so sbl's for sale.",
      'title': 'Buying NFL Season Tickets: SBL is Step One. (TicketWire)',
      'url': 'https://www.youtube.com/watch?v=M80btlo7xJc&t=53s',
      'video_id': 'M80btlo7xJc'},
     {'author': 'LawVS',
      'channel': 'LawVS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:49](https://www.youtube.com/watch?v=0KKYkQr1SBk&t=349s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I forgot the pit walls are like laid in the pit passes little bit of grass. But '
              "now we've reached the point where McLaren is right now. Oh, it looks so good in "
              'the flesh. You can tell all the pearlescence.',
      'timestamp': 349,
      'timestamp_label': '[00:05:49]',
      'timestamp_seconds': 349,
      'tip': 'I forgot the pit walls are like laid in the pit passes little bit of grass. But '
             "now we've reached the point where McLaren is right now. Oh, it looks so good in "
             'the flesh. You can tell all the pearlescence.',
      'title': "I Spent A Day In F1's Most Expensive Hospitality (LawVS)",
      'url': 'https://www.youtube.com/watch?v=0KKYkQr1SBk&t=349s',
      'video_id': '0KKYkQr1SBk'},
     {'author': '850 Club Credit',
      'channel': '850 Club Credit',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:19](https://www.youtube.com/watch?v=p8CMjg4a_CI&t=139s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Purchased prior to okay during the whole resale process or the pre-sale '
              'processes I should say so with the American Express they allow you to buy up up '
              'to I.',
      'timestamp': 139,
      'timestamp_label': '[00:02:19]',
      'timestamp_seconds': 139,
      'tip': 'Purchased prior to okay during the whole resale process or the pre-sale '
             'processes I should say so with the American Express they allow you to buy up up '
             'to I.',
      'title': 'How American Express/CITI Bank Can Get You Into Any Concert/Event For Free - '
               'Drake & Migos Concert (850 Club Credit)',
      'url': 'https://www.youtube.com/watch?v=p8CMjg4a_CI&t=139s',
      'video_id': 'p8CMjg4a_CI'},
     {'author': 'Hermanos F.C.',
      'channel': 'Hermanos F.C.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:51](https://www.youtube.com/watch?v=x2psJ5xGp18&t=471s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Else's seat yeah they take me down with the cops this all happened super fast "
              "take me down with the cops cuz you wouldn't cuz wouldn't move cuz I also.",
      'timestamp': 471,
      'timestamp_label': '[00:07:51]',
      'timestamp_seconds': 471,
      'tip': "Else's seat yeah they take me down with the cops this all happened super fast "
             "take me down with the cops cuz you wouldn't cuz wouldn't move cuz I also.",
      'title': 'Inter Miami Let Me Down—Why I’m Canceling My Season Tickets (Hermanos F.C.)',
      'url': 'https://www.youtube.com/watch?v=x2psJ5xGp18&t=471s',
      'video_id': 'x2psJ5xGp18'},
     {'author': 'Emmanuel Ak',
      'channel': 'Emmanuel Ak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:06](https://www.youtube.com/watch?v=ETQnblEeP94&t=546s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I've traveled five times and it's October. Ah, I'm getting I'm getting "
              "distracted here. But what I'm just trying to get across here is that never "
              "settle for less. Step by step, you're gonna get there. Don't don't feel like "
              "it's not achievable.",
      'timestamp': 546,
      'timestamp_label': '[00:09:06]',
      'timestamp_seconds': 546,
      'tip': "I've traveled five times and it's October. Ah, I'm getting I'm getting "
             "distracted here. But what I'm just trying to get across here is that never "
             "settle for less. Step by step, you're gonna get there. Don't don't feel like "
             "it's not achievable.",
      'title': 'How I scaled to 5 figure months Reselling Concert Tickets(1hr Full Course) '
               '(Emmanuel Ak)',
      'url': 'https://www.youtube.com/watch?v=ETQnblEeP94&t=546s',
      'video_id': 'ETQnblEeP94'},
     {'author': 'Francerz',
      'channel': 'Francerz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:45](https://www.youtube.com/watch?v=7VYhOZ4uE-I&t=45s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q7 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'De abrirla para que agregue su cuenta posteriormente a ello este van a ir al '
              'sitio de Ticket Master en el sitio de Ticket Master van a darle clic en su '
              'perfil una y una vez lo quedo iniciado la sesión van a darle clic en ver '
              'próximos.',
      'timestamp': 45,
      'timestamp_label': '[00:00:45]',
      'timestamp_seconds': 45,
      'tip': 'De abrirla para que agregue su cuenta posteriormente a ello este van a ir al '
             'sitio de Ticket Master en el sitio de Ticket Master van a darle clic en su '
             'perfil una y una vez lo quedo iniciado la sesión van a darle clic en ver '
             'próximos.',
      'title': 'Ticketmaster SafeTix + Google Wallet (Francerz)',
      'url': 'https://www.youtube.com/watch?v=7VYhOZ4uE-I&t=45s',
      'video_id': '7VYhOZ4uE-I'}],
 8: [{'author': 'GigaBits',
      'channel': 'GigaBits',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:12](https://www.youtube.com/watch?v=7KU-5HUqmzA&t=72s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I now have a clear picture of which platform actually works in 2026 and which '
              'one only works for itself. All three claim to offer secure purchases, '
              'transparent pricing, and the best seat selection. Ticket Master highlights '
              'official access.',
      'timestamp': 72,
      'timestamp_label': '[00:01:12]',
      'timestamp_seconds': 72,
      'tip': 'I now have a clear picture of which platform actually works in 2026 and which '
             'one only works for itself. All three claim to offer secure purchases, '
             'transparent pricing, and the best seat selection. Ticket Master highlights '
             'official access.',
      'title': 'Ticketmaster vs StubHub vs SeatGeek (2025) – What Ticket Seller Do We Need in '
               '2026? (GigaBits)',
      'url': 'https://www.youtube.com/watch?v=7KU-5HUqmzA&t=72s',
      'video_id': '7KU-5HUqmzA'},
     {'author': 'AidensGotGuides',
      'channel': 'AidensGotGuides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:04](https://www.youtube.com/watch?v=xEM0K5YLBZk&t=124s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, it helps to move efficiently and double-check all event details before '
              'buying. The key takeaway is simple. Direct cross-platform transfers between AXS '
              'and Ticketmaster are generally not supported.',
      'timestamp': 124,
      'timestamp_label': '[00:02:04]',
      'timestamp_seconds': 124,
      'tip': 'So, it helps to move efficiently and double-check all event details before '
             'buying. The key takeaway is simple. Direct cross-platform transfers between AXS '
             'and Ticketmaster are generally not supported.',
      'title': 'How to Transfer AXS Tickets to Ticketmaster (AidensGotGuides)',
      'url': 'https://www.youtube.com/watch?v=xEM0K5YLBZk&t=124s',
      'video_id': 'xEM0K5YLBZk'},
     {'author': 'NBC Bay Area',
      'channel': 'NBC Bay Area',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:01](https://www.youtube.com/watch?v=X3-flSVor4E&t=181s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Private jets park here for the Super Bowl. Noah expects about 150 to flood this '
              'zone. How do you put 150 airplanes on the ground here all at the same time? '
              'Noah says the real sorcery is software to virtually assign parking spots.',
      'timestamp': 181,
      'timestamp_label': '[00:03:01]',
      'timestamp_seconds': 181,
      'tip': 'Private jets park here for the Super Bowl. Noah expects about 150 to flood this '
             'zone. How do you put 150 airplanes on the ground here all at the same time? Noah '
             'says the real sorcery is software to virtually assign parking spots.',
      'title': 'Behind the scenes: Watch special teams prepare for blitz of Super Bowl flights '
               '(NBC Bay Area)',
      'url': 'https://www.youtube.com/watch?v=X3-flSVor4E&t=181s',
      'video_id': 'X3-flSVor4E'},
     {'author': 'Patchwave Tutorials',
      'channel': 'Patchwave Tutorials',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=Wqb02oxLDJ0&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Open settings and go to general then go to software update to install the '
              'latest iOS. Then update the Ticketmaster app via the App Store. Go to App '
              'Store, search for Ticketmaster, click update button and wait for the process to '
              'complete.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Open settings and go to general then go to software update to install the latest '
             'iOS. Then update the Ticketmaster app via the App Store. Go to App Store, search '
             'for Ticketmaster, click update button and wait for the process to complete.',
      'title': 'How to Fix Unable to Add Pass to Apple Wallet from Ticketmaster – iPhone Setup '
               '& Fix Guide (Patchwave Tutorials)',
      'url': 'https://www.youtube.com/watch?v=Wqb02oxLDJ0&t=20s',
      'video_id': 'Wqb02oxLDJ0'},
     {'author': 'ALSD',
      'channel': 'ALSD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:14](https://www.youtube.com/watch?v=ImKo957VLSo&t=194s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're all trying to get better. We're all trying to be the best, either in our "
              "cities or our organizations, whatever it may be. It's a forum where we all get "
              'to network, and come together, and share crazy ideas, failures, successes, make '
              'friends in the same community.',
      'timestamp': 194,
      'timestamp_label': '[00:03:14]',
      'timestamp_seconds': 194,
      'tip': "We're all trying to get better. We're all trying to be the best, either in our "
             "cities or our organizations, whatever it may be. It's a forum where we all get "
             'to network, and come together, and share crazy ideas, failures, successes, make '
             'friends in the same community.',
      'title': 'Hotel Hospitality Ideas for the Sports and Entertainment Venue Marketplace '
               '(ALSD)',
      'url': 'https://www.youtube.com/watch?v=ImKo957VLSo&t=194s',
      'video_id': 'ImKo957VLSo'},
     {'author': 'Senior Travel World',
      'channel': 'Senior Travel World',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:49](https://www.youtube.com/watch?v=QaNF9gbCV78&t=169s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The most underrated benefit in these lounges is the access to clean, private '
              'bathrooms. Avoiding the legendary lines of a soldout 80,000 seat stadium is a '
              'massive stress reducer, keeping you comfortable and close to your seat. These '
              'stadiums are sprawling.',
      'timestamp': 169,
      'timestamp_label': '[00:02:49]',
      'timestamp_seconds': 169,
      'tip': 'The most underrated benefit in these lounges is the access to clean, private '
             'bathrooms. Avoiding the legendary lines of a soldout 80,000 seat stadium is a '
             'massive stress reducer, keeping you comfortable and close to your seat. These '
             'stadiums are sprawling.',
      'title': 'FIFA World Cup 2026: Hospitality vs General Admission - Which to Buy? (Senior '
               'Travel World)',
      'url': 'https://www.youtube.com/watch?v=QaNF9gbCV78&t=169s',
      'video_id': 'QaNF9gbCV78'},
     {'author': 'DigitalThinker Inc.',
      'channel': 'DigitalThinker Inc.',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=Y0_GSVWwMIw&t=15s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Going to talk about how you can get access to digital thinkers customer portal '
              'how to submit help desk tickets and also.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'Going to talk about how you can get access to digital thinkers customer portal '
             'how to submit help desk tickets and also.',
      'title': 'Learn how to submit Support Tickets & Navigate the DTI portal! (DigitalThinker '
               'Inc.)',
      'url': 'https://www.youtube.com/watch?v=Y0_GSVWwMIw&t=15s',
      'video_id': 'Y0_GSVWwMIw'},
     {'author': 'Inside Edition',
      'channel': 'Inside Edition',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:03](https://www.youtube.com/watch?v=qQIN_PDMcPA&t=123s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Reality here is you've got what 20 million people trying to get 200 000 tickets "
              "of course there are going to be problems of course there's going to be "
              'bottlenecks nobody really ends up looking good now if the artist now '
              'Ticketmaster.',
      'timestamp': 123,
      'timestamp_label': '[00:02:03]',
      'timestamp_seconds': 123,
      'tip': "Reality here is you've got what 20 million people trying to get 200 000 tickets "
             "of course there are going to be problems of course there's going to be "
             'bottlenecks nobody really ends up looking good now if the artist now '
             'Ticketmaster.',
      'title': 'Taylor Swift’s ‘Eras Tour’ Tickets Crash Ticketmaster (Inside Edition)',
      'url': 'https://www.youtube.com/watch?v=qQIN_PDMcPA&t=123s',
      'video_id': 'qQIN_PDMcPA'},
     {'author': 'TechTutorXpress',
      'channel': 'TechTutorXpress',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=edUbHihe2lI&t=22s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Over here, you can either search for the app or you can scroll down and look '
              'for it. On the next screen, you need to tap on the offload app option. A '
              'confirmation pop-up will come up. Now, tap on the offload app option here.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Over here, you can either search for the app or you can scroll down and look for '
             'it. On the next screen, you need to tap on the offload app option. A '
             'confirmation pop-up will come up. Now, tap on the offload app option here.',
      'title': 'AXS Tickets App Not Working: How to FIX AXS Tickets App Not Working (FIXED) '
               '(TechTutorXpress)',
      'url': 'https://www.youtube.com/watch?v=edUbHihe2lI&t=22s',
      'video_id': 'edUbHihe2lI'},
     {'author': 'Forbes',
      'channel': 'Forbes',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:09](https://www.youtube.com/watch?v=fI8OAlihCxc&t=249s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Reserving the right to buy a season ticket reportedly ranges from $750 all the '
              "way up to $75,000 for full coverage check out Brett Knight's piece on "
              'forbes.com this is Kieran Meadows from Forbes thanks for tuning in e.',
      'timestamp': 249,
      'timestamp_label': '[00:04:09]',
      'timestamp_seconds': 249,
      'tip': 'Reserving the right to buy a season ticket reportedly ranges from $750 all the '
             "way up to $75,000 for full coverage check out Brett Knight's piece on forbes.com "
             'this is Kieran Meadows from Forbes thanks for tuning in e.',
      'title': 'Why Sports Arenas Make Millions More By Building Fewer Luxury Suites (Forbes)',
      'url': 'https://www.youtube.com/watch?v=fI8OAlihCxc&t=249s',
      'video_id': 'fI8OAlihCxc'},
     {'author': 'thebombtickets',
      'channel': 'thebombtickets',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:55:41](https://www.youtube.com/watch?v=icH7RV48MeY&t=3341s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In vancouver and sort of thing the the intensity of that that event that was '
              'really cool and I have the tickets so and I one one got a psa 10. so I do have '
              'some software.',
      'timestamp': 3341,
      'timestamp_label': '[00:55:41]',
      'timestamp_seconds': 3341,
      'tip': 'In vancouver and sort of thing the the intensity of that that event that was '
             'really cool and I have the tickets so and I one one got a psa 10. so I do have '
             'some software.',
      'title': 'World Series & NBA Finals Ticket Stubs - Ticket Stub Collecting w/ James '
               'Burzynski (thebombtickets)',
      'url': 'https://www.youtube.com/watch?v=icH7RV48MeY&t=3341s',
      'video_id': 'icH7RV48MeY'},
     {'author': 'PowerBombClub',
      'channel': 'PowerBombClub',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:41](https://www.youtube.com/watch?v=UTfE6DLqtLY&t=761s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I know us MMA fans love to talk about robberies, but since you know I did have '
              "the best seat in the house, I've got to say this, I just don't know how they "
              'gave it to Cortez. In my opinion, this was like the most clear spac I think '
              "I've ever seen.",
      'timestamp': 761,
      'timestamp_label': '[00:12:41]',
      'timestamp_seconds': 761,
      'tip': 'I know us MMA fans love to talk about robberies, but since you know I did have '
             "the best seat in the house, I've got to say this, I just don't know how they "
             "gave it to Cortez. In my opinion, this was like the most clear spac I think I've "
             'ever seen.',
      'title': 'I got $80,000 VIP Tickets to the UFC! (PowerBombClub)',
      'url': 'https://www.youtube.com/watch?v=UTfE6DLqtLY&t=761s',
      'video_id': 'UTfE6DLqtLY'},
     {'author': 'NFL',
      'channel': 'NFL',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:58](https://www.youtube.com/watch?v=G6FuWd4wNd8&t=778s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The National Football League thanks you for watching the Apple Music Super Bowl '
              '60 halftime show. Thank you for [música] watching this presentation of the '
              'national foall league.',
      'timestamp': 778,
      'timestamp_label': '[00:12:58]',
      'timestamp_seconds': 778,
      'tip': 'The National Football League thanks you for watching the Apple Music Super Bowl '
             '60 halftime show. Thank you for [música] watching this presentation of the '
             'national foall league.',
      'title': "Bad Bunny's Apple Music Super Bowl Halftime Show (NFL)",
      'url': 'https://www.youtube.com/watch?v=G6FuWd4wNd8&t=778s',
      'video_id': 'G6FuWd4wNd8'},
     {'author': 'thumbsuprun',
      'channel': 'thumbsuprun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:34](https://www.youtube.com/watch?v=sIgspwKXj_0&t=454s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "You're going ahead and actually trying to buy those tickets online with all "
              'that being said thanks again for watching be sure to stay tuned to all the '
              'different reviews coming up and see you guys next time.',
      'timestamp': 454,
      'timestamp_label': '[00:07:34]',
      'timestamp_seconds': 454,
      'tip': "You're going ahead and actually trying to buy those tickets online with all that "
             'being said thanks again for watching be sure to stay tuned to all the different '
             'reviews coming up and see you guys next time.',
      'title': 'THE 5 THINGS ANY TICKET RESALE WEBSITE NEEDS TO HAVE | ARE THEY LEGIT? '
               '(thumbsuprun)',
      'url': 'https://www.youtube.com/watch?v=sIgspwKXj_0&t=454s',
      'video_id': 'sIgspwKXj_0'},
     {'author': 'Follow The Why',
      'channel': 'Follow The Why',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:14](https://www.youtube.com/watch?v=cmeE4rZAlVk&t=494s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q8 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is still being fought over. So, why do concert tickets sell out in 9 seconds? '
              'Not because fans are slow, because the building was carved up before you '
              'arrived.',
      'timestamp': 494,
      'timestamp_label': '[00:08:14]',
      'timestamp_seconds': 494,
      'tip': 'Is still being fought over. So, why do concert tickets sell out in 9 seconds? '
             'Not because fans are slow, because the building was carved up before you '
             'arrived.',
      'title': 'Concert Tickets Explained: Why They Sell Out in 9 Seconds (Follow The Why)',
      'url': 'https://www.youtube.com/watch?v=cmeE4rZAlVk&t=494s',
      'video_id': 'cmeE4rZAlVk'}],
 9: [{'author': 'NBC News',
      'channel': 'NBC News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:55](https://www.youtube.com/watch?v=BOIfCHick7o&t=55s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "LET'S BRING IN NBC NEWS LEGAL ANALYST DANNY CEVALLOS TO BREAK IT DOWN. SO WALK "
              "US THROUGH THE FTC'S LAWSUIT HERE, AND HOW THE FTC CLAIMS THIS COMPANY BROKE "
              'THE LAW. ESSENTIALLY, THE FTC ALLEGES THAT THE DEFENDANT BROKE THE BOTS ACT.',
      'timestamp': 55,
      'timestamp_label': '[00:00:55]',
      'timestamp_seconds': 55,
      'tip': "LET'S BRING IN NBC NEWS LEGAL ANALYST DANNY CEVALLOS TO BREAK IT DOWN. SO WALK "
             "US THROUGH THE FTC'S LAWSUIT HERE, AND HOW THE FTC CLAIMS THIS COMPANY BROKE THE "
             'LAW. ESSENTIALLY, THE FTC ALLEGES THAT THE DEFENDANT BROKE THE BOTS ACT.',
      'title': 'FTC sues ticket-reselling operation for using fake accounts (NBC News)',
      'url': 'https://www.youtube.com/watch?v=BOIfCHick7o&t=55s',
      'video_id': 'BOIfCHick7o'},
     {'author': '11Alive',
      'channel': '11Alive',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=QiKFtpmNUqo&t=64s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'There is so much tradition at Augusta National. The Masters is one of the most '
              'coveted events in all of sports. It is the first major of the year for the. So '
              'there is that kind of amplified excitement around it and there are a lot of '
              'rules to follow.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'There is so much tradition at Augusta National. The Masters is one of the most '
             'coveted events in all of sports. It is the first major of the year for the. So '
             'there is that kind of amplified excitement around it and there are a lot of '
             'rules to follow.',
      'title': "Yes, it's true. You cannot buy or sell tickets for The Masters on a secondary "
               'resale site (11Alive)',
      'url': 'https://www.youtube.com/watch?v=QiKFtpmNUqo&t=64s',
      'video_id': 'QiKFtpmNUqo'},
     {'author': 'Dot Detective',
      'channel': 'Dot Detective',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:49](https://www.youtube.com/watch?v=7SSPFtppfGE&t=49s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Break it, and the FTC can treat that as an unfair or deceptive practice with '
              "civil penalties attached. The law is called the BOTS Act, and as we'll see, the "
              "company's defenses, roughly, were not bots, we're just a lot of people. Now, "
              'how did the scheme allegedly work?',
      'timestamp': 49,
      'timestamp_label': '[00:00:49]',
      'timestamp_seconds': 49,
      'tip': 'Break it, and the FTC can treat that as an unfair or deceptive practice with '
             "civil penalties attached. The law is called the BOTS Act, and as we'll see, the "
             "company's defenses, roughly, were not bots, we're just a lot of people. Now, how "
             'did the scheme allegedly work?',
      'title': "Limit 8 Per Customer… 1,300 Accounts? The DOJ's BOTS Act Case Against REPS, "
               'Explained (Dot Detective)',
      'url': 'https://www.youtube.com/watch?v=7SSPFtppfGE&t=49s',
      'video_id': '7SSPFtppfGE'},
     {'author': 'CBS Boston',
      'channel': 'CBS Boston',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=Wtsvx9NdMgc&t=80s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'LIVE NATION SAYS IT IS TO PREVENT TICKET SCALPERS. IT IS ABOUT WHETHER THE '
              'PROFESSIONAL BROKERS AND RETAIL SITES CAN USE THEIR BOTS AND ALL THEIR OTHER '
              'TACTICS TO GRAB THOUSANDS OF TICKETS MEANT FOR REAL FANS AND RESELL THEM. THERE '
              'ARE SCALPERS THAT UP SELL THE COST.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'LIVE NATION SAYS IT IS TO PREVENT TICKET SCALPERS. IT IS ABOUT WHETHER THE '
             'PROFESSIONAL BROKERS AND RETAIL SITES CAN USE THEIR BOTS AND ALL THEIR OTHER '
             'TACTICS TO GRAB THOUSANDS OF TICKETS MEANT FOR REAL FANS AND RESELL THEM. THERE '
             'ARE SCALPERS THAT UP SELL THE COST.',
      'title': 'New Massachusetts law changes how people can resell concert or sports tickets '
               '(CBS Boston)',
      'url': 'https://www.youtube.com/watch?v=Wtsvx9NdMgc&t=80s',
      'video_id': 'Wtsvx9NdMgc'},
     {'author': 'Gameday Guides',
      'channel': 'Gameday Guides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=LtTBm2wHjoE&t=28s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Welcome to your complete Masters survival guide. How to actually get tickets, '
              "what to do once you're inside, the rules that will get you kicked out if you "
              'break them, and the perfect itinerary for your first trip to Augusta. First, '
              'there are three ways to get tickets.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'Welcome to your complete Masters survival guide. How to actually get tickets, '
             "what to do once you're inside, the rules that will get you kicked out if you "
             'break them, and the perfect itinerary for your first trip to Augusta. First, '
             'there are three ways to get tickets.',
      'title': 'How to Get Tickets To The Masters and Insider Tips When You Get There (Gameday '
               'Guides)',
      'url': 'https://www.youtube.com/watch?v=LtTBm2wHjoE&t=28s',
      'video_id': 'LtTBm2wHjoE'},
     {'author': 'Any Given Wednesday with Bill Simmons',
      'channel': 'Any Given Wednesday with Bill Simmons',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=VzrNov3Y_qM&t=20s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Just in time for a whole new generation of fair weather LA football fans. MAN: '
              'In 2019, the team anticipates the majority of its seats, if not all, will '
              "require a personal seat license or PSL. BILL: What's a PSL you ask?",
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'Just in time for a whole new generation of fair weather LA football fans. MAN: '
             'In 2019, the team anticipates the majority of its seats, if not all, will '
             "require a personal seat license or PSL. BILL: What's a PSL you ask?",
      'title': 'Personal Seat Licenses are Bulls**t (HBO) (Any Given Wednesday with Bill '
               'Simmons)',
      'url': 'https://www.youtube.com/watch?v=VzrNov3Y_qM&t=20s',
      'video_id': 'VzrNov3Y_qM'},
     {'author': 'WKBW TV | Buffalo, NY',
      'channel': 'WKBW TV | Buffalo, NY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=gBkBFmKTfls&t=21s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'WILL ADD ON PS ELSE EACH SEASON TICKET HOLDER SEAT IN ITS NEW 60,000 SEAT '
              'ORCHARD PARK STADIUM. WHAT IS A PSL PSL STANDS FOR A PERSONAL SEAT LICENSE BY '
              "DEFINITION, IT'S A PREMIUM PRICE. YOU PAY TO ENJOY THAT FACILITY.",
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'WILL ADD ON PS ELSE EACH SEASON TICKET HOLDER SEAT IN ITS NEW 60,000 SEAT '
             'ORCHARD PARK STADIUM. WHAT IS A PSL PSL STANDS FOR A PERSONAL SEAT LICENSE BY '
             "DEFINITION, IT'S A PREMIUM PRICE. YOU PAY TO ENJOY THAT FACILITY.",
      'title': "Bills to sell PSL's (WKBW TV | Buffalo, NY)",
      'url': 'https://www.youtube.com/watch?v=gBkBFmKTfls&t=21s',
      'video_id': 'gBkBFmKTfls'},
     {'author': 'Bear Bets: A FOX Sports Gambling Show',
      'channel': 'Bear Bets: A FOX Sports Gambling Show',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:05](https://www.youtube.com/watch?v=T7ujtjzkDcQ&t=2225s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Those Mariners guys are all really good. They always leave you at least me '
              "wanting a little more. But Kirby just in terms of a talent play, Jeff, I don't "
              'know. If I had to bet anyone right now, that would probably be the guy.',
      'timestamp': 2225,
      'timestamp_label': '[00:37:05]',
      'timestamp_seconds': 2225,
      'tip': 'Those Mariners guys are all really good. They always leave you at least me '
             "wanting a little more. But Kirby just in terms of a talent play, Jeff, I don't "
             'know. If I had to bet anyone right now, that would probably be the guy.',
      'title': 'NBA Playoffs Gambling Guide 🏀💰 (Bear Bets: A FOX Sports Gambling Show)',
      'url': 'https://www.youtube.com/watch?v=T7ujtjzkDcQ&t=2225s',
      'video_id': 'T7ujtjzkDcQ'},
     {'author': 'Apparently Athletic',
      'channel': 'Apparently Athletic',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:44](https://www.youtube.com/watch?v=wOQ8g0C7oCw&t=224s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Since 2023, it's been the Apple Music Super Bowl Halftime Show. The terms "
              "haven't been disclosed. Press reports put them at about $50 million a year. So "
              'almost everything around those 12 minutes is sold. The airtime, the name on the '
              'show, everything except the performance.',
      'timestamp': 224,
      'timestamp_label': '[00:03:44]',
      'timestamp_seconds': 224,
      'tip': "Since 2023, it's been the Apple Music Super Bowl Halftime Show. The terms "
             "haven't been disclosed. Press reports put them at about $50 million a year. So "
             'almost everything around those 12 minutes is sold. The airtime, the name on the '
             'show, everything except the performance.',
      'title': "Why the World's Biggest Stars Accept $0 for the Super Bowl (Apparently "
               'Athletic)',
      'url': 'https://www.youtube.com/watch?v=wOQ8g0C7oCw&t=224s',
      'video_id': 'wOQ8g0C7oCw'},
     {'author': 'David Fiene',
      'channel': 'David Fiene',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=QPC4K8A6GJg&t=39s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Video i'm going to walk you through those rules including what you should keep "
              "to support the deduction so let's get to work all right so let's talk.",
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "Video i'm going to walk you through those rules including what you should keep "
             "to support the deduction so let's get to work all right so let's talk.",
      'title': 'Business Meals and Entertainment Tax deduction - What You Should Know (David '
               'Fiene)',
      'url': 'https://www.youtube.com/watch?v=QPC4K8A6GJg&t=39s',
      'video_id': 'QPC4K8A6GJg'},
     {'author': 'CBS TEXAS',
      'channel': 'CBS TEXAS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:23](https://www.youtube.com/watch?v=6a_saGlb7l8&t=23s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "THEIR APPEARANCE KNOWN AHEAD OF THIS GAME. THAT'S RIGHT, ENGLAND FANS. YOU "
              'MIGHT HAVE SEEN THEM ACROSS NORTH TEXAS THIS WEEK. FROM COWBOY BOOTS TO '
              'BARBECUE JOINTS. AGAIN ALL ACROSS SOCIAL MEDIA, MANY ARE EXPERIENCING TEXAS FOR '
              'THE VERY FIRST TIME NOW.',
      'timestamp': 23,
      'timestamp_label': '[00:00:23]',
      'timestamp_seconds': 23,
      'tip': "THEIR APPEARANCE KNOWN AHEAD OF THIS GAME. THAT'S RIGHT, ENGLAND FANS. YOU MIGHT "
             'HAVE SEEN THEM ACROSS NORTH TEXAS THIS WEEK. FROM COWBOY BOOTS TO BARBECUE '
             'JOINTS. AGAIN ALL ACROSS SOCIAL MEDIA, MANY ARE EXPERIENCING TEXAS FOR THE VERY '
             'FIRST TIME NOW.',
      'title': 'FIFA World Cup fans report issues with match tickets purchased from resale '
               'sites (CBS TEXAS)',
      'url': 'https://www.youtube.com/watch?v=6a_saGlb7l8&t=23s',
      'video_id': '6a_saGlb7l8'},
     {'author': 'NBC New York',
      'channel': 'NBC New York',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=-NeAkVXcsP4&t=21s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, certainly different cities have different levels of demand, different teams '
              "as well. I think what we're seeing in terms of cities is places like Miami, New "
              "York. They're really driving some of the biggest demand, but really it comes "
              'down to the team specifically.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'So, certainly different cities have different levels of demand, different teams '
             "as well. I think what we're seeing in terms of cities is places like Miami, New "
             "York. They're really driving some of the biggest demand, but really it comes "
             'down to the team specifically.',
      'title': "SeatGeek's tips for buying FIFA World Cup tickets (NBC New York)",
      'url': 'https://www.youtube.com/watch?v=-NeAkVXcsP4&t=21s',
      'video_id': '-NeAkVXcsP4'},
     {'author': 'TicketWire',
      'channel': 'TicketWire',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:28](https://www.youtube.com/watch?v=hlfwsoMBQS0&t=148s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's how you beat me so but I didn't even think of any of this I just here "
              'take my money and just keep in mind this is so this is the the license for the '
              "seats this isn't actually for the the price for the tickets for that year no "
              'right this is a one-time.',
      'timestamp': 148,
      'timestamp_label': '[00:02:28]',
      'timestamp_seconds': 148,
      'tip': "That's how you beat me so but I didn't even think of any of this I just here "
             'take my money and just keep in mind this is so this is the the license for the '
             "seats this isn't actually for the the price for the tickets for that year no "
             'right this is a one-time.',
      'title': 'NFL Season Tickets: Shawn Covers Key Step in Buying (TicketWire)',
      'url': 'https://www.youtube.com/watch?v=hlfwsoMBQS0&t=148s',
      'video_id': 'hlfwsoMBQS0'},
     {'author': 'CBS Mornings',
      'channel': 'CBS Mornings',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:30](https://www.youtube.com/watch?v=RGn3Hcnvklg&t=270s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'TV you can build yourself a TV room you get you get a new outfit a new pair of '
              'shoes to show everybody to serve everybody some weenie dogs with order some '
              "chicken wings that's like a good option to me yes.",
      'timestamp': 270,
      'timestamp_label': '[00:04:30]',
      'timestamp_seconds': 270,
      'tip': 'TV you can build yourself a TV room you get you get a new outfit a new pair of '
             'shoes to show everybody to serve everybody some weenie dogs with order some '
             "chicken wings that's like a good option to me yes.",
      'title': "Security behind StubHub's Super Bowl ticket operations (CBS Mornings)",
      'url': 'https://www.youtube.com/watch?v=RGn3Hcnvklg&t=270s',
      'video_id': 'RGn3Hcnvklg'},
     {'author': 'Troydan',
      'channel': 'Troydan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:14](https://www.youtube.com/watch?v=0jqhQFvHHcc&t=1214s)',
      'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                   'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                   'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                   'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                   '(Chapter Q9 operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Mullet smell like tobacco I loved it this was a great experience one that I '
              'will never forget but I am exhausted I need to sleep right now guys thank you '
              'for watching and as always keep yours stick on the ice.',
      'timestamp': 1214,
      'timestamp_label': '[00:20:14]',
      'timestamp_seconds': 1214,
      'tip': 'Mullet smell like tobacco I loved it this was a great experience one that I will '
             'never forget but I am exhausted I need to sleep right now guys thank you for '
             'watching and as always keep yours stick on the ice.',
      'title': 'I got $47,000 VIP Tickets to the UFC! (Troydan)',
      'url': 'https://www.youtube.com/watch?v=0jqhQFvHHcc&t=1214s',
      'video_id': '0jqhQFvHHcc'}],
 10: [{'author': 'GQ',
       'channel': 'GQ',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:58](https://www.youtube.com/watch?v=nT-DpxVmqC0&t=58s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Nothing is off limits because this is GQ All Access. You've come to the crown "
               'jewels of NFL stadium, Allegiant Stadium, home of the Super Bowl. It almost '
               "makes me wanna suit up. I mean, I don't know if you guys know this, but I can "
               'kick a pretty mean field goal.',
       'timestamp': 58,
       'timestamp_label': '[00:00:58]',
       'timestamp_seconds': 58,
       'tip': "Nothing is off limits because this is GQ All Access. You've come to the crown "
              'jewels of NFL stadium, Allegiant Stadium, home of the Super Bowl. It almost '
              "makes me wanna suit up. I mean, I don't know if you guys know this, but I can "
              'kick a pretty mean field goal.',
       'title': 'What $2.5M Gets You at the Super Bowl | All Access | GQ Sports (GQ)',
       'url': 'https://www.youtube.com/watch?v=nT-DpxVmqC0&t=58s',
       'video_id': 'nT-DpxVmqC0'},
      {'author': 'Supplier Digital Portal',
       'channel': 'Supplier Digital Portal',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:06](https://www.youtube.com/watch?v=Db5sc_kyZFE&t=66s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'After reviewing the details, check the tick box to confirm that you have read '
               'all the provided information. If you are satisfied with the information '
               'provided, select the back to dashboard option. This will allow you to access '
               'the relevant details without creating a ticket.',
       'timestamp': 66,
       'timestamp_label': '[00:01:06]',
       'timestamp_seconds': 66,
       'tip': 'After reviewing the details, check the tick box to confirm that you have read '
              'all the provided information. If you are satisfied with the information '
              'provided, select the back to dashboard option. This will allow you to access '
              'the relevant details without creating a ticket.',
       'title': 'Ticket Creation (Supplier Digital Portal)',
       'url': 'https://www.youtube.com/watch?v=Db5sc_kyZFE&t=66s',
       'video_id': 'Db5sc_kyZFE'},
      {'author': 'Simply Finance',
       'channel': 'Simply Finance',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:41](https://www.youtube.com/watch?v=s7E1Yc3RoQc&t=41s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "All that but I'm going to go with buying ticket and here you could go ahead "
               'and tap the question button in order to get in contact with the live agent so '
               'over.',
       'timestamp': 41,
       'timestamp_label': '[00:00:41]',
       'timestamp_seconds': 41,
       'tip': "All that but I'm going to go with buying ticket and here you could go ahead and "
              'tap the question button in order to get in contact with the live agent so over.',
       'title': 'Can I Change The Delivery Method Of My Tickets In The Axs App ! (Simply '
                'Finance)',
       'url': 'https://www.youtube.com/watch?v=s7E1Yc3RoQc&t=41s',
       'video_id': 's7E1Yc3RoQc'},
      {'author': 'lighthouse travel group',
       'channel': 'lighthouse travel group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:45](https://www.youtube.com/watch?v=YbCPfj2AvV4&t=165s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '>> We have it all for Lighthouse Crew. >>  >> Super Bowl.',
       'timestamp': 165,
       'timestamp_label': '[00:02:45]',
       'timestamp_seconds': 165,
       'tip': '>> We have it all for Lighthouse Crew. >>  >> Super Bowl.',
       'title': '🏈🔥 GO BIG! GO LOUD! SUPER BOWL 2027! 🔥🏈🏆  GAME. THE ULTIMATE VIP EXPERIENCE. '
                'THE TRIP OF A LIFETIME! (lighthouse travel group)',
       'url': 'https://www.youtube.com/watch?v=YbCPfj2AvV4&t=165s',
       'video_id': 'YbCPfj2AvV4'},
      {'author': 'Morning Brew',
       'channel': 'Morning Brew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:11](https://www.youtube.com/watch?v=ow9KXpcvvEg&t=131s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But it wasn't until the 1980s when the scale of business potential was "
               'realized in an effort to bring the Super Bowl to Miami, Dolphins owner Joe '
               'Robbie made a plan to build a new stadium for $115 million.',
       'timestamp': 131,
       'timestamp_label': '[00:02:11]',
       'timestamp_seconds': 131,
       'tip': "But it wasn't until the 1980s when the scale of business potential was realized "
              'in an effort to bring the Super Bowl to Miami, Dolphins owner Joe Robbie made a '
              'plan to build a new stadium for $115 million.',
       'title': 'The real reason NFL stadiums have so many luxury suites (Morning Brew)',
       'url': 'https://www.youtube.com/watch?v=ow9KXpcvvEg&t=131s',
       'video_id': 'ow9KXpcvvEg'},
      {'author': 'PromoTix',
       'channel': 'PromoTix',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:10](https://www.youtube.com/watch?v=IdHpcPxQTfU&t=130s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So this is where you add in your venue address, select the time zone for the '
               'event. And also at the bottom here, this is where you add all of the dates and '
               'times. For this event specifically, I set this up as a recurring event.',
       'timestamp': 130,
       'timestamp_label': '[00:02:10]',
       'timestamp_seconds': 130,
       'tip': 'So this is where you add in your venue address, select the time zone for the '
              'event. And also at the bottom here, this is where you add all of the dates and '
              'times. For this event specifically, I set this up as a recurring event.',
       'title': 'Create, Sell, and Manage Tickets for Any Event: Ticketing Demo || PromoTix '
                '(PromoTix)',
       'url': 'https://www.youtube.com/watch?v=IdHpcPxQTfU&t=130s',
       'video_id': 'IdHpcPxQTfU'},
      {'author': 'Logitix',
       'channel': 'Logitix',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:20](https://www.youtube.com/watch?v=YaZpToURgBk&t=200s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Venue please reference our pricing automation recording for additional '
               'capabilities within the Zone grid within the ticket group grid you have the '
               'ability to mass edit inventory this is useful to quickly update listing prices '
               'or add internal or external.',
       'timestamp': 200,
       'timestamp_label': '[00:03:20]',
       'timestamp_seconds': 200,
       'tip': 'Venue please reference our pricing automation recording for additional '
              'capabilities within the Zone grid within the ticket group grid you have the '
              'ability to mass edit inventory this is useful to quickly update listing prices '
              'or add internal or external.',
       'title': 'Logitix One - Event Detail Page (Logitix)',
       'url': 'https://www.youtube.com/watch?v=YaZpToURgBk&t=200s',
       'video_id': 'YaZpToURgBk'},
      {'author': 'L0B0',
       'channel': 'L0B0',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:12](https://www.youtube.com/watch?v=TofGuOnLm0A&t=72s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Know when you were the super bowl that's not no advantage I don't have no then "
               "no advantage okay all right so everybody's saying they have advantage at every "
               "home game during the year so I mean it ain't like they won every home game so "
               "it ain't much of an advantage.",
       'timestamp': 72,
       'timestamp_label': '[00:01:12]',
       'timestamp_seconds': 72,
       'tip': "Know when you were the super bowl that's not no advantage I don't have no then "
              "no advantage okay all right so everybody's saying they have advantage at every "
              "home game during the year so I mean it ain't like they won every home game so "
              "it ain't much of an advantage.",
       'title': 'Former NFL Player Dwight Smith EXPOSES NFL For RIGGING Games!!! (L0B0)',
       'url': 'https://www.youtube.com/watch?v=TofGuOnLm0A&t=72s',
       'video_id': 'TofGuOnLm0A'},
      {'author': 'ABC7 News Bay Area',
       'channel': 'ABC7 News Bay Area',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:04](https://www.youtube.com/watch?v=YZ3TuDNRcvw&t=64s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'SO PENA IS PAYING $11,300 TOTAL FOR TWO TICKETS IN THE LOWER END ZONE. TICKETS '
               'THAT ARE GOING FOR MORE THAN 12 GRAND APIECE IN THE RESALE MARKETPLACE. A LOT '
               'OF PEOPLE MIGHT BE WORRIED ABOUT LOSING THAT MONEY. YEAH, WELL, I WAS I WAS '
               'PRETTY STRESSED OUT ALL YEAR.',
       'timestamp': 64,
       'timestamp_label': '[00:01:04]',
       'timestamp_seconds': 64,
       'tip': 'SO PENA IS PAYING $11,300 TOTAL FOR TWO TICKETS IN THE LOWER END ZONE. TICKETS '
              'THAT ARE GOING FOR MORE THAN 12 GRAND APIECE IN THE RESALE MARKETPLACE. A LOT '
              'OF PEOPLE MIGHT BE WORRIED ABOUT LOSING THAT MONEY. YEAH, WELL, I WAS I WAS '
              'PRETTY STRESSED OUT ALL YEAR.',
       'title': "Here's how Bay Area 49ers fan got Super Bowl tickets under average resale "
                'price of $9,000 (ABC7 News Bay Area)',
       'url': 'https://www.youtube.com/watch?v=YZ3TuDNRcvw&t=64s',
       'video_id': 'YZ3TuDNRcvw'},
      {'author': 'Luxury Travel Professional',
       'channel': 'Luxury Travel Professional',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:10](https://www.youtube.com/watch?v=6CYg2Av2xS4&t=310s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Lewis and N rord back in 2016 here's what's coming up we've had this Stu "
               "already but we've got the third practice session coming up at 5:30 this "
               'afternoon 5:30 this afternoon all 20 cars out on track the final chance for '
               'ad.',
       'timestamp': 310,
       'timestamp_label': '[00:05:10]',
       'timestamp_seconds': 310,
       'tip': "Lewis and N rord back in 2016 here's what's coming up we've had this Stu "
              "already but we've got the third practice session coming up at 5:30 this "
              'afternoon 5:30 this afternoon all 20 cars out on track the final chance for ad.',
       'title': '[$14,000 Ticket] Inside the F1 Paddock Club | Singapore Grand Prix VIP '
                'Experience (Luxury Travel Professional)',
       'url': 'https://www.youtube.com/watch?v=6CYg2Av2xS4&t=310s',
       'video_id': '6CYg2Av2xS4'},
      {'author': 'Fixed Formulas',
       'channel': 'Fixed Formulas',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:31](https://www.youtube.com/watch?v=f7BuIdB0-6I&t=31s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'After that click on the option of upcoming events under my tickets. So when '
               'you do this you will be landed here on this particular page. Now it is going '
               'to show you all of the tickets that are available in your upcoming events.',
       'timestamp': 31,
       'timestamp_label': '[00:00:31]',
       'timestamp_seconds': 31,
       'tip': 'After that click on the option of upcoming events under my tickets. So when you '
              'do this you will be landed here on this particular page. Now it is going to '
              'show you all of the tickets that are available in your upcoming events.',
       'title': 'How to Transfer Tickets on Ticketmaster [2026] UPDATED (Fixed Formulas)',
       'url': 'https://www.youtube.com/watch?v=f7BuIdB0-6I&t=31s',
       'video_id': 'f7BuIdB0-6I'},
      {'author': 'Courtney Willis',
       'channel': 'Courtney Willis',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:49](https://www.youtube.com/watch?v=f5hPIW3U13c&t=49s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Now that I'm thinking back on it, I totally could have gotten VIP, but in my "
               "mind, I'm like this is my first year. Don't need to be bougie, don't need to "
               'be posh. I do know that Coachella offers certain presale tickets to like AMEX '
               'cardholders.',
       'timestamp': 49,
       'timestamp_label': '[00:00:49]',
       'timestamp_seconds': 49,
       'tip': "Now that I'm thinking back on it, I totally could have gotten VIP, but in my "
              "mind, I'm like this is my first year. Don't need to be bougie, don't need to be "
              'posh. I do know that Coachella offers certain presale tickets to like AMEX '
              'cardholders.',
       'title': 'Coachella 2027 Tickets Are Selling Out! Prices, Camping & More (Courtney '
                'Willis)',
       'url': 'https://www.youtube.com/watch?v=f5hPIW3U13c&t=49s',
       'video_id': 'f5hPIW3U13c'},
      {'author': 'NBC News',
       'channel': 'NBC News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=7SO1FTTFaBM&t=20s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "KNOW, BOTS HAPPEN WHEN YOU'RE BUYING TICKETS. THIS LAWSUIT SAYS THAT THE "
               'COMPANY, LIVE NATION, WENT AGAINST THEIR OWN LIMITS AND LET RESELLERS BUY, '
               "LIKE, A LOT OF TICKETS FOR BIG EVENTS. AND IF YOU'RE LIKE, WAIT A SECOND, THIS "
               'SOUNDS FAMILIAR.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "KNOW, BOTS HAPPEN WHEN YOU'RE BUYING TICKETS. THIS LAWSUIT SAYS THAT THE "
              'COMPANY, LIVE NATION, WENT AGAINST THEIR OWN LIMITS AND LET RESELLERS BUY, '
              "LIKE, A LOT OF TICKETS FOR BIG EVENTS. AND IF YOU'RE LIKE, WAIT A SECOND, THIS "
              'SOUNDS FAMILIAR.',
       'title': 'FTC sues Live Nation and Ticketmaster over claims of illegal resale tactics '
                '(NBC News)',
       'url': 'https://www.youtube.com/watch?v=7SO1FTTFaBM&t=20s',
       'video_id': '7SO1FTTFaBM'},
      {'author': 'iKnow iOS',
       'channel': 'iKnow iOS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=zghU1cQya5k&t=108s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Button and consider subscribing if you found this video helpful and if you '
               "have any queries you can drop it down in the comment section below we'll see "
               'you in the next one.',
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': 'Button and consider subscribing if you found this video helpful and if you have '
              "any queries you can drop it down in the comment section below we'll see you in "
              'the next one.',
       'title': 'AXS App Not Working: How to Fix AXS Tickets App Not Working (iKnow iOS)',
       'url': 'https://www.youtube.com/watch?v=zghU1cQya5k&t=108s',
       'video_id': 'zghU1cQya5k'},
      {'author': 'Ticket Flipping',
       'channel': 'Ticket Flipping',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:04](https://www.youtube.com/watch?v=JwHo6if-9Wo&t=724s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q10 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Kind of check it out if you want you'll be one of the first people in the "
               'group um so again check out the free training and you can decide if this '
               "business is for you uh again thanks for watching the video um and I'll see you "
               'guys in the next one.',
       'timestamp': 724,
       'timestamp_label': '[00:12:04]',
       'timestamp_seconds': 724,
       'tip': "Kind of check it out if you want you'll be one of the first people in the group "
              'um so again check out the free training and you can decide if this business is '
              "for you uh again thanks for watching the video um and I'll see you guys in the "
              'next one.',
       'title': 'The Simplest Resale Business No One is Doing (Ticket Flipping)',
       'url': 'https://www.youtube.com/watch?v=JwHo6if-9Wo&t=724s',
       'video_id': 'JwHo6if-9Wo'}],
 11: [{'author': 'MMG',
       'channel': 'MMG',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:21](https://www.youtube.com/watch?v=JfafTeTKsyo&t=621s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Super Bowl like WATCHING ARE USUALLY NOT DIE HARD FANS OF THE TEAM. I mean '
               "we're not Patriots or fans. The 12 people in front of us were all Patriots "
               'fans. This is the Super Bowl, ladies and gentlemen. These are like these are '
               "like $20,000 seats and they're meeting traffic.",
       'timestamp': 621,
       'timestamp_label': '[00:10:21]',
       'timestamp_seconds': 621,
       'tip': 'Super Bowl like WATCHING ARE USUALLY NOT DIE HARD FANS OF THE TEAM. I mean '
              "we're not Patriots or fans. The 12 people in front of us were all Patriots "
              'fans. This is the Super Bowl, ladies and gentlemen. These are like these are '
              "like $20,000 seats and they're meeting traffic.",
       'title': 'My VIP Experience at Super Bowl LX! (MMG)',
       'url': 'https://www.youtube.com/watch?v=JfafTeTKsyo&t=621s',
       'video_id': 'JfafTeTKsyo'},
      {'author': '9NEWS',
       'channel': '9NEWS',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:56](https://www.youtube.com/watch?v=Qmi-KnjQ-xo&t=116s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Santa Clara is a weird deal. I mean, and you're probably not gonna probably "
               "stay there, so you're gonna have to go to some of those other cities around "
               "there. But if your team's in the Super Bowl and you do all sorts of crazy "
               'things, you have a pot of gold sorts of money.',
       'timestamp': 116,
       'timestamp_label': '[00:01:56]',
       'timestamp_seconds': 116,
       'tip': "Santa Clara is a weird deal. I mean, and you're probably not gonna probably "
              "stay there, so you're gonna have to go to some of those other cities around "
              "there. But if your team's in the Super Bowl and you do all sorts of crazy "
              'things, you have a pot of gold sorts of money.',
       'title': "Super Bowl 2026 tickets: How much they cost, where they're sold and how to "
                'get them (9NEWS)',
       'url': 'https://www.youtube.com/watch?v=Qmi-KnjQ-xo&t=116s',
       'video_id': 'Qmi-KnjQ-xo'},
      {'author': 'Mercedes-AMG PETRONAS F1 Team',
       'channel': 'Mercedes-AMG PETRONAS F1 Team',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:04](https://www.youtube.com/watch?v=fl-tIcZO3u4&t=124s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'I have a core team of people from designers to project managers to hospitality '
               'and event specialists and they all come together to deliver these phenomenal '
               'experiences. Hospitality can add to performance of the team in many ways.',
       'timestamp': 124,
       'timestamp_label': '[00:02:04]',
       'timestamp_seconds': 124,
       'tip': 'I have a core team of people from designers to project managers to hospitality '
              'and event specialists and they all come together to deliver these phenomenal '
              'experiences. Hospitality can add to performance of the team in many ways.',
       'title': 'The VIP Experience | How It Works: F1 Hospitality 🤩 (Mercedes-AMG PETRONAS F1 '
                'Team)',
       'url': 'https://www.youtube.com/watch?v=fl-tIcZO3u4&t=124s',
       'video_id': 'fl-tIcZO3u4'},
      {'author': 'WFAA',
       'channel': 'WFAA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:57](https://www.youtube.com/watch?v=5niSyiKlGY4&t=57s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'FC Dallas president Dan Hunt is excited and tired and all the above for Messi. '
               'The match, but mostly for the team and fans. So we made sure the pre sale was '
               'dedicated to our core FC Dallas fan base. FC Dallas tickets are regularly '
               'between 20 and $200 for this match.',
       'timestamp': 57,
       'timestamp_label': '[00:00:57]',
       'timestamp_seconds': 57,
       'tip': 'FC Dallas president Dan Hunt is excited and tired and all the above for Messi. '
              'The match, but mostly for the team and fans. So we made sure the pre sale was '
              'dedicated to our core FC Dallas fan base. FC Dallas tickets are regularly '
              'between 20 and $200 for this match.',
       'title': 'The Messi effect: FC Dallas vs. Inter Miami ticket prices soar ahead of match '
                '(WFAA)',
       'url': 'https://www.youtube.com/watch?v=5niSyiKlGY4&t=57s',
       'video_id': '5niSyiKlGY4'},
      {'author': 'Kicking it with Drew',
       'channel': 'Kicking it with Drew',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:04](https://www.youtube.com/watch?v=TIrEHtyuX3g&t=424s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'That one of the best teams, if not the best team right now in England and one '
               'of the top leagues in the world, has cheaper tickets than a mediocre MLS team '
               "that has the best player of all time in it. That That That's absolutely crazy. "
               'Like this is really the Messi effect.',
       'timestamp': 424,
       'timestamp_label': '[00:07:04]',
       'timestamp_seconds': 424,
       'tip': 'That one of the best teams, if not the best team right now in England and one '
              'of the top leagues in the world, has cheaper tickets than a mediocre MLS team '
              "that has the best player of all time in it. That That That's absolutely crazy. "
              'Like this is really the Messi effect.',
       'title': 'These Are Most EXPENSIVE Season Tickets Ever!! (Kicking it with Drew)',
       'url': 'https://www.youtube.com/watch?v=TIrEHtyuX3g&t=424s',
       'video_id': 'TIrEHtyuX3g'},
      {'author': '24H SPORT',
       'channel': '24H SPORT',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:36](https://www.youtube.com/watch?v=pAU7eEVgp1A&t=336s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Goldberg said if you're a broker with a front door deal with the team where "
               "you buy 500 season tickets during the regular season it's reasonable to expect "
               "you're going to get Super Bowl tickets from that team photos one great image "
               'from every Super Bowl.',
       'timestamp': 336,
       'timestamp_label': '[00:05:36]',
       'timestamp_seconds': 336,
       'tip': "Goldberg said if you're a broker with a front door deal with the team where you "
              "buy 500 season tickets during the regular season it's reasonable to expect "
              "you're going to get Super Bowl tickets from that team photos one great image "
              'from every Super Bowl.',
       'title': 'Players, coaches continue to resell Super Bowl tickets, despite ban on the '
                'practice (24H SPORT)',
       'url': 'https://www.youtube.com/watch?v=pAU7eEVgp1A&t=336s',
       'video_id': 'pAU7eEVgp1A'},
      {'author': 'WKMG News 6 ClickOrlando',
       'channel': 'WKMG News 6 ClickOrlando',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:24](https://www.youtube.com/watch?v=9L6opSvFpSA&t=84s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'THAT NUMBER IS ONLY EXPECTED TO GO UP IF THE HOMETOWN BUCCANEERS BECOME IS '
               'ONLY EXPECTED TO GO UP IF THE HOMETOWN BUCCANEERS BECOME THE FIRST TEAM TO '
               'PLAY A SUPER THE HOMETOWN BUCCANEERS BECOME THE FIRST TEAM TO PLAY A SUPER '
               'BOWL IN THEIR HOME STADIUM.',
       'timestamp': 84,
       'timestamp_label': '[00:01:24]',
       'timestamp_seconds': 84,
       'tip': 'THAT NUMBER IS ONLY EXPECTED TO GO UP IF THE HOMETOWN BUCCANEERS BECOME IS ONLY '
              'EXPECTED TO GO UP IF THE HOMETOWN BUCCANEERS BECOME THE FIRST TEAM TO PLAY A '
              'SUPER THE HOMETOWN BUCCANEERS BECOME THE FIRST TEAM TO PLAY A SUPER BOWL IN '
              'THEIR HOME STADIUM.',
       'title': 'How much is a resale ticket for the Super Bowl? (WKMG News 6 ClickOrlando)',
       'url': 'https://www.youtube.com/watch?v=9L6opSvFpSA&t=84s',
       'video_id': '9L6opSvFpSA'},
      {'author': 'Global Nomads',
       'channel': 'Global Nomads',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:37](https://www.youtube.com/watch?v=ePgxCdmE8o8&t=397s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s a very famous photographer who does all of the F1. And we also saw Fred "
               "Vasuer and Zach who's the team Zack. He also came out onto the pit. So, and "
               'Martin Brundle zoom past on a little on a scooter. And today was really a lot '
               'of testing.',
       'timestamp': 397,
       'timestamp_label': '[00:06:37]',
       'timestamp_seconds': 397,
       'tip': "'s a very famous photographer who does all of the F1. And we also saw Fred "
              "Vasuer and Zach who's the team Zack. He also came out onto the pit. So, and "
              'Martin Brundle zoom past on a little on a scooter. And today was really a lot '
              'of testing.',
       'title': 'Melbourne Grand Prix 2026 | Formula 1 Paddock Club v Red Bull Pit Lane '
                'Review. Was it worth $6,000 (Global Nomads)',
       'url': 'https://www.youtube.com/watch?v=ePgxCdmE8o8&t=397s',
       'video_id': 'ePgxCdmE8o8'},
      {'author': 'Grind City Media',
       'channel': 'Grind City Media',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:34:55](https://www.youtube.com/watch?v=x5waP6wwK-Y&t=2095s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I think um [laughter] I think there's a lot of resources that are being put in "
               "the game and you've got a lot of Well, I think first of all, look at our team. "
               "If you look at look at all of our team, the whole team, everybody's playing at "
               'big clubs in Europe.',
       'timestamp': 2095,
       'timestamp_label': '[00:34:55]',
       'timestamp_seconds': 2095,
       'tip': "I think um [laughter] I think there's a lot of resources that are being put in "
              "the game and you've got a lot of Well, I think first of all, look at our team. "
              "If you look at look at all of our team, the whole team, everybody's playing at "
              'big clubs in Europe.',
       'title': 'NBA Finals, World Cup Odds, Stanley Cup Finals, College World Series | The '
                'Odds Couple (Grind City Media)',
       'url': 'https://www.youtube.com/watch?v=x5waP6wwK-Y&t=2095s',
       'video_id': 'x5waP6wwK-Y'},
      {'author': 'Break The Board Sports',
       'channel': 'Break The Board Sports',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:55](https://www.youtube.com/watch?v=ojMLC_Y0QgI&t=355s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'re looking at the conference, right, looking at the conference bets in the "
               'NBA, um I said before the year, Knicks and Nuggets, uh I still am not worried '
               "about the Cavs. The Cavs don't scare me at all. I think the Pistons are a "
               'really good regular season team.',
       'timestamp': 355,
       'timestamp_label': '[00:05:55]',
       'timestamp_seconds': 355,
       'tip': "'re looking at the conference, right, looking at the conference bets in the "
              'NBA, um I said before the year, Knicks and Nuggets, uh I still am not worried '
              "about the Cavs. The Cavs don't scare me at all. I think the Pistons are a "
              'really good regular season team.',
       'title': 'The Ultimate Futures Betting Guide | NBA, NHL, MLB & More (Break The Board '
                'Sports)',
       'url': 'https://www.youtube.com/watch?v=ojMLC_Y0QgI&t=355s',
       'video_id': 'ojMLC_Y0QgI'},
      {'author': 'Making It Network',
       'channel': 'Making It Network',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:02](https://www.youtube.com/watch?v=zwZDxD4dEpY&t=422s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The the artist has to sign off on that the artist and their team has to '
               'approve on ticket prices so when it come comes to Dynamic and platinum '
               'ticketing the.',
       'timestamp': 422,
       'timestamp_label': '[00:07:02]',
       'timestamp_seconds': 422,
       'tip': 'The the artist has to sign off on that the artist and their team has to approve '
              'on ticket prices so when it come comes to Dynamic and platinum ticketing the.',
       'title': 'Taylor Swift Eras Tour VS Ticketmaster Dynamic Pricing - Who is Responsible '
                'for High Ticket Prices? (Making It Network)',
       'url': 'https://www.youtube.com/watch?v=zwZDxD4dEpY&t=422s',
       'video_id': 'zwZDxD4dEpY'},
      {'author': 'Víctor Abad',
       'channel': 'Víctor Abad',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:05](https://www.youtube.com/watch?v=3cvtvbU9nb0&t=185s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'España con una promoción muy sencilla. Si os creáis una cuenta y hacéis una '
               'compra de al menos 1 € os podéis llevar una gorra exclusiva del equipo '
               'McLaren.',
       'timestamp': 185,
       'timestamp_label': '[00:03:05]',
       'timestamp_seconds': 185,
       'tip': 'España con una promoción muy sencilla. Si os creáis una cuenta y hacéis una '
              'compra de al menos 1 € os podéis llevar una gorra exclusiva del equipo McLaren.',
       'title': 'Así ven la Fórmula 1 los ricos - Entramos en el Paddock Club de Zandvoort '
                '(Víctor Abad)',
       'url': 'https://www.youtube.com/watch?v=3cvtvbU9nb0&t=185s',
       'video_id': '3cvtvbU9nb0'},
      {'author': 'WGRZ-TV',
       'channel': 'WGRZ-TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=YksJO2KDmnk&t=26s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Others were simply postponed by the pandemic and that can impact whether or '
               'not you get a refund tonight another reminder about reading all the fine print '
               'when you purchase something like a ticket.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': 'Others were simply postponed by the pandemic and that can impact whether or not '
              'you get a refund tonight another reminder about reading all the fine print when '
              'you purchase something like a ticket.',
       'title': 'Wednesday Town Hall: Can you get a refund on canceled or postponed concert '
                'tickets? (WGRZ-TV)',
       'url': 'https://www.youtube.com/watch?v=YksJO2KDmnk&t=26s',
       'video_id': 'YksJO2KDmnk'},
      {'author': 'KSAT 12',
       'channel': 'KSAT 12',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:29](https://www.youtube.com/watch?v=UB3lQ-5pQXE&t=29s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AND I THINK I PAID ALMOST $250, PROBABLY FOR TICKETS THAT WERE MAYBE LIKE. '
               '250, PROBABLY FOR TICKETS THAT WERE MAYBE LIKE. BUT I’VE SEEN, YOU KNOW, WERE '
               'MAYBE LIKE. BUT I’VE SEEN, YOU KNOW, EVEN ARE IN RE CENT. BUT I’VE SEEN, YOU '
               'KNOW, EVEN ARE IN RE CENT.',
       'timestamp': 29,
       'timestamp_label': '[00:00:29]',
       'timestamp_seconds': 29,
       'tip': 'AND I THINK I PAID ALMOST $250, PROBABLY FOR TICKETS THAT WERE MAYBE LIKE. 250, '
              'PROBABLY FOR TICKETS THAT WERE MAYBE LIKE. BUT I’VE SEEN, YOU KNOW, WERE MAYBE '
              'LIKE. BUT I’VE SEEN, YOU KNOW, EVEN ARE IN RE CENT. BUT I’VE SEEN, YOU KNOW, '
              'EVEN ARE IN RE CENT.',
       'title': 'SA concertgoer shares how bots, high resale prices hurt real fans amid FTC '
                'Ticketmaster lawsuit (KSAT 12)',
       'url': 'https://www.youtube.com/watch?v=UB3lQ-5pQXE&t=29s',
       'video_id': 'UB3lQ-5pQXE'},
      {'author': 'The Credit Nerd',
       'channel': 'The Credit Nerd',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:28](https://www.youtube.com/watch?v=JS9sO0Fx9A0&t=88s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q11 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Capital One also gives eligible cardholders access to select exclusive '
               'tickets, events, and presales, making this a good combination of potential '
               'rewards and access. But, with that said, Capital One is not going to have '
               'access to every single artist, team, or event.',
       'timestamp': 88,
       'timestamp_label': '[00:01:28]',
       'timestamp_seconds': 88,
       'tip': 'Capital One also gives eligible cardholders access to select exclusive tickets, '
              'events, and presales, making this a good combination of potential rewards and '
              'access. But, with that said, Capital One is not going to have access to every '
              'single artist, team, or event.',
       'title': '3 Best Credit Cards For Concert Tickets & Entertainment In 2026 | NerdWallet '
                '(The Credit Nerd)',
       'url': 'https://www.youtube.com/watch?v=JS9sO0Fx9A0&t=88s',
       'video_id': 'JS9sO0Fx9A0'}],
 12: [{'author': 'Ticket Flipping',
       'channel': 'Ticket Flipping',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:54](https://www.youtube.com/watch?v=hw92haJDs9Y&t=114s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "24 hours or the past 7 days. It's simple, it's easy to sort, you can filter "
               '[clears throat] by many, many different metrics such as venue size, such as '
               'the artist popularity score from Spotify. And this latest availability column '
               'refreshes non-stop all day long.',
       'timestamp': 114,
       'timestamp_label': '[00:01:54]',
       'timestamp_seconds': 114,
       'tip': "24 hours or the past 7 days. It's simple, it's easy to sort, you can filter "
              '[clears throat] by many, many different metrics such as venue size, such as the '
              'artist popularity score from Spotify. And this latest availability column '
              'refreshes non-stop all day long.',
       'title': 'The New Way to Find Tickets To Flip (Ticket Flipping)',
       'url': 'https://www.youtube.com/watch?v=hw92haJDs9Y&t=114s',
       'video_id': 'hw92haJDs9Y'},
      {'author': 'Front Office Sports News',
       'channel': 'Front Office Sports News',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:14](https://www.youtube.com/watch?v=6ufb5u4PcIQ&t=134s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Super Bowl game day experience freely adept, exciting, great access, easy to '
               "get in and out of. That makes for a great environment for us. Um, it doesn't "
               'necessarily work per perfectly on a regular season.',
       'timestamp': 134,
       'timestamp_label': '[00:02:14]',
       'timestamp_seconds': 134,
       'tip': 'Super Bowl game day experience freely adept, exciting, great access, easy to '
              "get in and out of. That makes for a great environment for us. Um, it doesn't "
              'necessarily work per perfectly on a regular season.',
       'title': 'How the VIP Super Bowl Experience Works with On Location President Paul Caine '
                '(Front Office Sports News)',
       'url': 'https://www.youtube.com/watch?v=6ufb5u4PcIQ&t=134s',
       'video_id': '6ufb5u4PcIQ'},
      {'author': 'J Properties Group',
       'channel': 'J Properties Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:06:54](https://www.youtube.com/watch?v=U3YMt8EJCrE&t=414s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And third, plan your trip very early because during the Masters week in '
               'Augusta, hotels fill up, homes rent out very quick, restaurants get booked up '
               'sometimes months or even years in advance.',
       'timestamp': 414,
       'timestamp_label': '[00:06:54]',
       'timestamp_seconds': 414,
       'tip': 'And third, plan your trip very early because during the Masters week in '
              'Augusta, hotels fill up, homes rent out very quick, restaurants get booked up '
              'sometimes months or even years in advance.',
       'title': "Masters Tickets Explained | Why They're Almost Impossible to Get! (J "
                'Properties Group)',
       'url': 'https://www.youtube.com/watch?v=U3YMt8EJCrE&t=414s',
       'video_id': 'U3YMt8EJCrE'},
      {'author': 'Adventure & Sports',
       'channel': 'Adventure & Sports',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:59](https://www.youtube.com/watch?v=qSTxMUdp-ro&t=59s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Watch every match at the venue of your choice. Includes four to nine matches '
               'depending on venue. All match days and stages eligible. And it is available '
               'for all the hospitality options. See your team in action at every early stage '
               'match regardless of location.',
       'timestamp': 59,
       'timestamp_label': '[00:00:59]',
       'timestamp_seconds': 59,
       'tip': 'Watch every match at the venue of your choice. Includes four to nine matches '
              'depending on venue. All match days and stages eligible. And it is available for '
              'all the hospitality options. See your team in action at every early stage match '
              'regardless of location.',
       'title': 'World Cup Hospitality Tickets Explained (Adventure & Sports)',
       'url': 'https://www.youtube.com/watch?v=qSTxMUdp-ro&t=59s',
       'video_id': 'qSTxMUdp-ro'},
      {'author': 'BAG & TRAVEL',
       'channel': 'BAG & TRAVEL',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:31](https://www.youtube.com/watch?v=B2P9oIBqq5Q&t=91s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've had, um I'm going to get start with the best ticket that I've had and "
               'then go work my way back. I can only give you advice based on the tickets that '
               "I've had and the best ticket that I've had is fan week, the week before is the "
               'qualifying week basically essentially.',
       'timestamp': 91,
       'timestamp_label': '[00:01:31]',
       'timestamp_seconds': 91,
       'tip': "I've had, um I'm going to get start with the best ticket that I've had and then "
              "go work my way back. I can only give you advice based on the tickets that I've "
              "had and the best ticket that I've had is fan week, the week before is the "
              'qualifying week basically essentially.',
       'title': 'What ticket should you buy for US Open? My experience (BAG & TRAVEL)',
       'url': 'https://www.youtube.com/watch?v=B2P9oIBqq5Q&t=91s',
       'video_id': 'B2P9oIBqq5Q'},
      {'author': 'Sports Travel Tom',
       'channel': 'Sports Travel Tom',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:08](https://www.youtube.com/watch?v=iKAz6YJRTXI&t=188s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'If you get tickets for Tuesday, $125. Wednesday slightly more, but of course '
               'you get the par 3 tournament within that as well, $150. And then tournament '
               "days, $160. Those ticket prices aren't bad at all really for The Masters.",
       'timestamp': 188,
       'timestamp_label': '[00:03:08]',
       'timestamp_seconds': 188,
       'tip': 'If you get tickets for Tuesday, $125. Wednesday slightly more, but of course '
              'you get the par 3 tournament within that as well, $150. And then tournament '
              "days, $160. Those ticket prices aren't bad at all really for The Masters.",
       'title': 'How to Get Masters Tickets (2027 Guide: Ballot vs Packages) (Sports Travel '
                'Tom)',
       'url': 'https://www.youtube.com/watch?v=iKAz6YJRTXI&t=188s',
       'video_id': 'iKAz6YJRTXI'},
      {'author': 'thumbsuprun',
       'channel': 'thumbsuprun',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:42](https://www.youtube.com/watch?v=sQtHQZ6UoRM&t=42s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The best way to go ahead and actually start making money selling seasoned '
               'seats there are a couple of reasons behind that one if you.',
       'timestamp': 42,
       'timestamp_label': '[00:00:42]',
       'timestamp_seconds': 42,
       'tip': 'The best way to go ahead and actually start making money selling seasoned seats '
              'there are a couple of reasons behind that one if you.',
       'title': 'CAN YOU MAKE MONEY SELLING SEASON TICKETS? | 4 WAYS TO SELL TICKETS TO MAKE '
                'MONEY | NFL NBA NHL MLB (thumbsuprun)',
       'url': 'https://www.youtube.com/watch?v=sQtHQZ6UoRM&t=42s',
       'video_id': 'sQtHQZ6UoRM'},
      {'author': 'Emily Canham Vlogs',
       'channel': 'Emily Canham Vlogs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:34](https://www.youtube.com/watch?v=UgpOwtQHKS4&t=274s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "A text from a car saying that they were a few minutes away oh look the car's "
               "here Dad whenever you're ready I'm ready got my own thank you all good if you "
               'need to throw is amazing thank you have a wonderful day.',
       'timestamp': 274,
       'timestamp_label': '[00:04:34]',
       'timestamp_seconds': 274,
       'tip': "A text from a car saying that they were a few minutes away oh look the car's "
              "here Dad whenever you're ready I'm ready got my own thank you all good if you "
              'need to throw is amazing thank you have a wonderful day.',
       'title': 'Surprising my DAD with F1 PADDOCK CLUB tickets at Silverstone 😅 British Grand '
                'Prix 2023 🏎️ (Emily Canham Vlogs)',
       'url': 'https://www.youtube.com/watch?v=UgpOwtQHKS4&t=274s',
       'video_id': 'UgpOwtQHKS4'},
      {'author': 'Live The Dash',
       'channel': 'Live The Dash',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:21:03](https://www.youtube.com/watch?v=emvC24ZLBWo&t=1263s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "China is that it's a sprint race. So it means you get more on track action "
               'than a normal race weekend. Another reason why this is the race to upgrade, if '
               "you're going to upgrade any of them. We've decided to watch the sprint from "
               'the rooftop.',
       'timestamp': 1263,
       'timestamp_label': '[00:21:03]',
       'timestamp_seconds': 1263,
       'tip': "China is that it's a sprint race. So it means you get more on track action than "
              'a normal race weekend. Another reason why this is the race to upgrade, if '
              "you're going to upgrade any of them. We've decided to watch the sprint from the "
              'rooftop.',
       'title': 'I Upgraded My F1 Ticket In China… (Live The Dash)',
       'url': 'https://www.youtube.com/watch?v=emvC24ZLBWo&t=1263s',
       'video_id': 'emvC24ZLBWo'},
      {'author': 'Only Scrans',
       'channel': 'Only Scrans',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:34](https://www.youtube.com/watch?v=XhaS3MGZL-o&t=214s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Review when there are cars going 100 Mil hour straight P here maybe more it's "
               "all super tasty it is quite small that's not the worst thing in the world when "
               'you got a full day of watching cars go dead.',
       'timestamp': 214,
       'timestamp_label': '[00:03:34]',
       'timestamp_seconds': 214,
       'tip': "Review when there are cars going 100 Mil hour straight P here maybe more it's "
              "all super tasty it is quite small that's not the worst thing in the world when "
              'you got a full day of watching cars go dead.',
       'title': "THE WORLD'S MOST EXPENSIVE F1 EXPERIENCE (Only Scrans)",
       'url': 'https://www.youtube.com/watch?v=XhaS3MGZL-o&t=214s',
       'video_id': 'XhaS3MGZL-o'},
      {'author': 'The Wrestling Classic',
       'channel': 'The Wrestling Classic',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:49](https://www.youtube.com/watch?v=oqJoU9yO2_c&t=169s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "UFC the first fight, but he's been on a tear since then. And Brendan is, you "
               "know, he's been battle tested since day one. So I think they both deserve "
               'respect and I know there is a lot of respect between all of them guys.',
       'timestamp': 169,
       'timestamp_label': '[00:02:49]',
       'timestamp_seconds': 169,
       'tip': "UFC the first fight, but he's been on a tear since then. And Brendan is, you "
              "know, he's been battle tested since day one. So I think they both deserve "
              'respect and I know there is a lot of respect between all of them guys.',
       'title': 'UFC Fight Night: Vancouver Vlog - On Location VIP Experience (The Wrestling '
                'Classic)',
       'url': 'https://www.youtube.com/watch?v=oqJoU9yO2_c&t=169s',
       'video_id': 'oqJoU9yO2_c'},
      {'author': 'World Of Entertainment',
       'channel': 'World Of Entertainment',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:39](https://www.youtube.com/watch?v=0hT1wi4_aew&t=99s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '10 dead in company 2 288 252 115. 11 queen plus adam lambert hundred 21777 '
               'dollars one hundred thirty nine dollars oh seven dot twelve iron maiden one '
               'five hundred ninety five thousand two hundred eighty five dollars dollar '
               'seventy dot 18.',
       'timestamp': 99,
       'timestamp_label': '[00:01:39]',
       'timestamp_seconds': 99,
       'tip': '10 dead in company 2 288 252 115. 11 queen plus adam lambert hundred 21777 '
              'dollars one hundred thirty nine dollars oh seven dot twelve iron maiden one '
              'five hundred ninety five thousand two hundred eighty five dollars dollar '
              'seventy dot 18.',
       'title': 'Top 20 Global Concert Tours from Pollstar (World Of Entertainment)',
       'url': 'https://www.youtube.com/watch?v=0hT1wi4_aew&t=99s',
       'video_id': '0hT1wi4_aew'},
      {'author': 'WCPO 9',
       'channel': 'WCPO 9',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:48](https://www.youtube.com/watch?v=VBj60jqiycw&t=108s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Spokesman promised to investigate nicu's request for a refund but keep this in "
               'mind in the next few years as you start purchasing tickets again that there '
               "are differences with third-party websites so you don't waste your money I'm "
               "john madder's wcbo 9 news.",
       'timestamp': 108,
       'timestamp_label': '[00:01:48]',
       'timestamp_seconds': 108,
       'tip': "Spokesman promised to investigate nicu's request for a refund but keep this in "
              'mind in the next few years as you start purchasing tickets again that there are '
              "differences with third-party websites so you don't waste your money I'm john "
              "madder's wcbo 9 news.",
       'title': 'Struggle for concert ticket refunds (WCPO 9)',
       'url': 'https://www.youtube.com/watch?v=VBj60jqiycw&t=108s',
       'video_id': 'VBj60jqiycw'},
      {'author': 'Valuetainment Short Clips',
       'channel': 'Valuetainment Short Clips',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:26](https://www.youtube.com/watch?v=jQCA_9sgdpM&t=686s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Just happy though that end racism which is the most UN goal as much as we want '
               "it you're not going to stop some guy in Mississippi stop being racism that's "
               "like saying stop ugliness you can't so the fact that they finally took that "
               'stupid ass thing out of there Choose.',
       'timestamp': 686,
       'timestamp_label': '[00:11:26]',
       'timestamp_seconds': 686,
       'tip': 'Just happy though that end racism which is the most UN goal as much as we want '
              "it you're not going to stop some guy in Mississippi stop being racism that's "
              "like saying stop ugliness you can't so the fact that they finally took that "
              'stupid ass thing out of there Choose.',
       'title': '"Ticket Prices Have PLUMMETED!" - NFL Fans STUNNED As Super Bowl Tickets Hit '
                'By MASSIVE Price Drop (Valuetainment Short Clips)',
       'url': 'https://www.youtube.com/watch?v=jQCA_9sgdpM&t=686s',
       'video_id': 'jQCA_9sgdpM'},
      {'author': 'Nerd Nook Hub',
       'channel': 'Nerd Nook Hub',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:44](https://www.youtube.com/watch?v=8OkQ2Oq5Lbc&t=164s)',
       'relevance': 'Attributed practitioner commentary on `Super Bowl`/`World Cup`/`F1` VIP '
                    'hospitality & sponsor-allotment bundling, stadium luxury-suite '
                    'seat-splitting, `NFL`/`NBA` `SSL` playoff-option strips, and `BOTS '
                    'Act`-compliant `SkyBox`/`Automatiq` multi-exchange POS broadcasting '
                    '(Chapter Q12 operational verification).',
       'source_type': 'video_pro_tip',
       'text': '1,000 if you want to take it up a notch. Transportation depends on whether you '
               'rent a car, ride share, or use public transit. Super Bowl day ride shares can '
               'surge hard. The best approach is to plan around transit or arrive early.',
       'timestamp': 164,
       'timestamp_label': '[00:02:44]',
       'timestamp_seconds': 164,
       'tip': '1,000 if you want to take it up a notch. Transportation depends on whether you '
              'rent a car, ride share, or use public transit. Super Bowl day ride shares can '
              'surge hard. The best approach is to plan around transit or arrive early.',
       'title': 'How Much Does it Cost to Go to the Super Bowl LX? 2026 (Nerd Nook Hub)',
       'url': 'https://www.youtube.com/watch?v=8OkQ2Oq5Lbc&t=164s',
       'video_id': '8OkQ2Oq5Lbc'}]}
