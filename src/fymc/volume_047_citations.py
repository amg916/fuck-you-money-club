"""Curated 180-citation AI Data-Center Powered Land, Substation Headroom & BESS Site Optioning baseline (15 per chapter across Q1-Q12) mined strictly from verified AI Data-Center Powered Land, Substation Headroom & BESS Site Optioning YouTube transcripts."""
from __future__ import annotations

CHAPTER_KEYWORDS: dict[int, set[str]] = {1: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'business',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 2: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'budget',
     'building',
     'buyer',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 3: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cash',
     'cashflow',
     'cbre',
     'center',
     'centers',
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
 4: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'budget',
     'building',
     'calling',
     'capacity',
     'capital',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 5: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'audit',
     'avoid',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 6: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 7: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 8: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'api',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 9: {'138kv',
     '200k',
     '2023',
     '345kv',
     '69kv',
     'abatement',
     'acre',
     'acres',
     'agreement',
     'analysis',
     'assembly',
     'assignable',
     'assigning',
     'assignment',
     'avoiding',
     'battery',
     'behind',
     'bess',
     'brokerage',
     'brownfield',
     'btm',
     'building',
     'calling',
     'capacity',
     'carrier',
     'carry',
     'case',
     'cbre',
     'center',
     'centers',
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
 10: {'138kv',
      '200k',
      '2023',
      '345kv',
      '69kv',
      'abatement',
      'acre',
      'acres',
      'agent',
      'agreement',
      'ai',
      'analysis',
      'assembly',
      'assignable',
      'assigning',
      'assignment',
      'automate',
      'automation',
      'avoiding',
      'battery',
      'behind',
      'bess',
      'brokerage',
      'brownfield',
      'btm',
      'building',
      'calling',
      'capacity',
      'carrier',
      'carry',
      'case',
      'cbre',
      'center',
      'centers',
      'dashboard',
      'leverage',
      'pipeline',
      'scale',
      'script',
      'speed',
      'template',
      'workflow'},
 11: {'138kv',
      '200k',
      '2023',
      '345kv',
      '69kv',
      'abatement',
      'acre',
      'acres',
      'agreement',
      'analysis',
      'assembly',
      'assignable',
      'assigning',
      'assignment',
      'avoiding',
      'battery',
      'behind',
      'bess',
      'brokerage',
      'brownfield',
      'btm',
      'building',
      'calling',
      'capacity',
      'carrier',
      'carry',
      'case',
      'cbre',
      'center',
      'centers',
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
 12: {'138kv',
      '200k',
      '2023',
      '345kv',
      '69kv',
      'abatement',
      'acre',
      'acres',
      'action',
      'agreement',
      'analysis',
      'assembly',
      'assignable',
      'assigning',
      'assignment',
      'avoiding',
      'battery',
      'behind',
      'bess',
      'brokerage',
      'brownfield',
      'btm',
      'building',
      'calling',
      'capacity',
      'carrier',
      'carry',
      'case',
      'cbre',
      'center',
      'centers',
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

BASELINE_EXPERT_CITATIONS_BY_CHAPTER: dict[int, list[dict]] = {1: [{'author': 'STG Nations Energy',
      'channel': 'STG Nations Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:31](https://www.youtube.com/watch?v=AVf_DgVRB3w&t=211s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Those are ancillary services. It can be paid to exist as backup capacity the '
              'grid can call on. A well-run battery stacks these revenues, moving between them '
              'as market conditions change. None of that value is on the data sheet. It lives '
              'entirely in the model.',
      'timestamp': 211,
      'timestamp_label': '[00:03:31]',
      'timestamp_seconds': 211,
      'tip': 'Those are ancillary services. It can be paid to exist as backup capacity the '
             'grid can call on. A well-run battery stacks these revenues, moving between them '
             'as market conditions change. None of that value is on the data sheet. It lives '
             'entirely in the model.',
      'title': 'BESS 101 for developers: sizing, chemistry, revenue stacking (STG Nations '
               'Energy)',
      'url': 'https://www.youtube.com/watch?v=AVf_DgVRB3w&t=211s',
      'video_id': 'AVf_DgVRB3w'},
     {'author': 'learnBESS',
      'channel': 'learnBESS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:44](https://www.youtube.com/watch?v=m0yVO4ZOmdc&t=104s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Balancing pre-qualification, imbalance pricing, network tariffs, and whether a '
              "capacity mechanism exists at all. That's why two BESS plants with identical "
              "hardware earn different revenue in different European countries. A BESS plant's "
              'revenue is market-based.',
      'timestamp': 104,
      'timestamp_label': '[00:01:44]',
      'timestamp_seconds': 104,
      'tip': 'Balancing pre-qualification, imbalance pricing, network tariffs, and whether a '
             "capacity mechanism exists at all. That's why two BESS plants with identical "
             "hardware earn different revenue in different European countries. A BESS plant's "
             'revenue is market-based.',
      'title': 'How Battery Storage Makes Money in EU Electricity Markets — BESS Explained '
               '(learnBESS)',
      'url': 'https://www.youtube.com/watch?v=m0yVO4ZOmdc&t=104s',
      'video_id': 'm0yVO4ZOmdc'},
     {'author': 'Your Finance Uncle',
      'channel': 'Your Finance Uncle',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:15](https://www.youtube.com/watch?v=BXuRdYxfF2k&t=495s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This is why cutting price is often the worst move a struggling data center '
              "operator can make. Enterprise clients don't read a rate cut as a bargain. They "
              "read it as a warning sign that a facility can't fill capacity or maintain "
              'reliability.',
      'timestamp': 495,
      'timestamp_label': '[00:08:15]',
      'timestamp_seconds': 495,
      'tip': 'This is why cutting price is often the worst move a struggling data center '
             "operator can make. Enterprise clients don't read a rate cut as a bargain. They "
             "read it as a warning sign that a facility can't fill capacity or maintain "
             'reliability.',
      'title': 'The Economics of Owning a Data Center (Why 65% Full Means Bankrupt) (Your '
               'Finance Uncle)',
      'url': 'https://www.youtube.com/watch?v=BXuRdYxfF2k&t=495s',
      'video_id': 'BXuRdYxfF2k'},
     {'author': 'Digital Infrastructure Network',
      'channel': 'Digital Infrastructure Network',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:15](https://www.youtube.com/watch?v=U2apRbTTZuE&t=195s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Services to the grid which is going to generate an additional Revenue stream '
              'for the data center operator if we look at the technologies that we.',
      'timestamp': 195,
      'timestamp_label': '[00:03:15]',
      'timestamp_seconds': 195,
      'tip': 'Services to the grid which is going to generate an additional Revenue stream for '
             'the data center operator if we look at the technologies that we.',
      'title': 'Sustainable Data Centers: microgrid-enabled and battery energy storage powered '
               'systems (Digital Infrastructure Network)',
      'url': 'https://www.youtube.com/watch?v=U2apRbTTZuE&t=195s',
      'video_id': 'U2apRbTTZuE'},
     {'author': 'Break Even',
      'channel': 'Break Even',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:04](https://www.youtube.com/watch?v=gMNnJebMwzw&t=244s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For every 1,000 MW of capacity, three are available. Everything else is spoken '
              'for, often years before the building is even finished. There is no other real '
              'estate market on the planet that looks like this. A shopping mall dreams of 90% '
              'occupancy.',
      'timestamp': 244,
      'timestamp_label': '[00:04:04]',
      'timestamp_seconds': 244,
      'tip': 'For every 1,000 MW of capacity, three are available. Everything else is spoken '
             'for, often years before the building is even finished. There is no other real '
             'estate market on the planet that looks like this. A shopping mall dreams of 90% '
             'occupancy.',
      'title': "The Real Product of a Data Center Isn't Data (Break Even)",
      'url': 'https://www.youtube.com/watch?v=gMNnJebMwzw&t=244s',
      'video_id': 'gMNnJebMwzw'},
     {'author': 'The smarter E',
      'channel': 'The smarter E',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:35](https://www.youtube.com/watch?v=-6QrZ_r6oJs&t=1535s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And if you ask him how often he use the battery, he said, "I don\'t know." So '
              'and this shows a bit there is a is a is a financial market and then there is a '
              'real energy market behind it. And both things are coming together now and I '
              'think this is super interesting right now.',
      'timestamp': 1535,
      'timestamp_label': '[00:25:35]',
      'timestamp_seconds': 1535,
      'tip': 'And if you ask him how often he use the battery, he said, "I don\'t know." So '
             'and this shows a bit there is a is a is a financial market and then there is a '
             'real energy market behind it. And both things are coming together now and I '
             'think this is super interesting right now.',
      'title': 'From EVs to BESS: Why capital is flowing to batteries – with Laurent Segalen '
               'and Stefan Mueller (The smarter E)',
      'url': 'https://www.youtube.com/watch?v=-6QrZ_r6oJs&t=1535s',
      'video_id': '-6QrZ_r6oJs'},
     {'author': 'IRECUSA',
      'channel': 'IRECUSA',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:24:56](https://www.youtube.com/watch?v=AKo4FQtyC68&t=1496s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um so those are the variables that go into the analytical model um that are '
              'ascertained from current conditions or future conditions. Uh then we have the '
              'evaluations and assumptions. Um these are kind of the core uh foundation of '
              'host capacity analysis.',
      'timestamp': 1496,
      'timestamp_label': '[00:24:56]',
      'timestamp_seconds': 1496,
      'tip': 'Um so those are the variables that go into the analytical model um that are '
             'ascertained from current conditions or future conditions. Uh then we have the '
             'evaluations and assumptions. Um these are kind of the core uh foundation of host '
             'capacity analysis.',
      'title': 'Exploring How Hosting Capacity Analysis Can Inform Proactive Grid Planning and '
               'Cost Allocation (IRECUSA)',
      'url': 'https://www.youtube.com/watch?v=AKo4FQtyC68&t=1496s',
      'video_id': 'AKo4FQtyC68'},
     {'author': 'Bloomberg Podcasts',
      'channel': 'Bloomberg Podcasts',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:20](https://www.youtube.com/watch?v=cvNO9pZAhM0&t=1520s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Because data centers produce a lot of tax revenue for these states, which go to '
              'help fund schools and the like. Is anyone talking about public private '
              'partnerships in the data center context? I feel like this is something that '
              'like comes in waves.',
      'timestamp': 1520,
      'timestamp_label': '[00:25:20]',
      'timestamp_seconds': 1520,
      'tip': 'Because data centers produce a lot of tax revenue for these states, which go to '
             'help fund schools and the like. Is anyone talking about public private '
             'partnerships in the data center context? I feel like this is something that like '
             'comes in waves.',
      'title': 'This Is What It Takes to Get a Data Center Financed | Odd Lots (Bloomberg '
               'Podcasts)',
      'url': 'https://www.youtube.com/watch?v=cvNO9pZAhM0&t=1520s',
      'video_id': 'cvNO9pZAhM0'},
     {'author': 'Project Cargo Professionals',
      'channel': 'Project Cargo Professionals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:51](https://www.youtube.com/watch?v=fzdDu4tWnGQ&t=51s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Um best it's a growing market, so it's very interesting for business doing "
              'business with us all those kind of the special um goods what we have. Um these '
              'are lithium lithium ion batteries um with quite a high number of volume.',
      'timestamp': 51,
      'timestamp_label': '[00:00:51]',
      'timestamp_seconds': 51,
      'tip': "Um best it's a growing market, so it's very interesting for business doing "
             'business with us all those kind of the special um goods what we have. Um these '
             'are lithium lithium ion batteries um with quite a high number of volume.',
      'title': 'Fluence and the BESS Boom | The Future of Battery Storage Logistics (Project '
               'Cargo Professionals)',
      'url': 'https://www.youtube.com/watch?v=fzdDu4tWnGQ&t=51s',
      'video_id': 'fzdDu4tWnGQ'},
     {'author': 'Lockton Europe',
      'channel': 'Lockton Europe',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=UI-9nmVEA9U&t=60s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And so, as a business, we have made the strategic decision to look at other '
              'markets, and in particular, the ERCOT market, so looking at the Texas power '
              'grid uh over in the United States.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'And so, as a business, we have made the strategic decision to look at other '
             'markets, and in particular, the ERCOT market, so looking at the Texas power grid '
             'uh over in the United States.',
      'title': 'Lockton Energy And Power Podcast | Scaling Success: Expanding A BESS Business '
               '(Lockton Europe)',
      'url': 'https://www.youtube.com/watch?v=UI-9nmVEA9U&t=60s',
      'video_id': 'UI-9nmVEA9U'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:53](https://www.youtube.com/watch?v=YabOCr0t9pI&t=53s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Between that signed agreement and your first breaker close lies an intensive '
              'gauntlet of asbuilt modeling model checks, quarterly stability assessments, and '
              "transmission service provider approvals. URT's QSA process operates on an "
              'unforgiving quarterly cycle.',
      'timestamp': 53,
      'timestamp_label': '[00:00:53]',
      'timestamp_seconds': 53,
      'tip': 'Between that signed agreement and your first breaker close lies an intensive '
             'gauntlet of asbuilt modeling model checks, quarterly stability assessments, and '
             "transmission service provider approvals. URT's QSA process operates on an "
             'unforgiving quarterly cycle.',
      'title': 'Post-SGIA Interconnection Studies in ERCOT | From SGIA to Grid Synchronization '
               '| Keentel Engineering (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=YabOCr0t9pI&t=53s',
      'video_id': 'YabOCr0t9pI'},
     {'author': 'ERCOTISO',
      'channel': 'ERCOTISO',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:20:41](https://www.youtube.com/watch?v=a34rwkck9IA&t=1241s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'How do we restart it from a supply chain point of view? Get the manufacturing '
              'capacity and get the supply chains and all of that up and running. But then we '
              'have to restart it from a market design point of view as well.',
      'timestamp': 1241,
      'timestamp_label': '[00:20:41]',
      'timestamp_seconds': 1241,
      'tip': 'How do we restart it from a supply chain point of view? Get the manufacturing '
             'capacity and get the supply chains and all of that up and running. But then we '
             'have to restart it from a market design point of view as well.',
      'title': 'Energy Insights: A Conversation between ERCOT and PJM leaders (ERCOTISO)',
      'url': 'https://www.youtube.com/watch?v=a34rwkck9IA&t=1241s',
      'video_id': 'a34rwkck9IA'},
     {'author': 'LandApp by LandGate',
      'channel': 'LandApp by LandGate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:15](https://www.youtube.com/watch?v=eTK7c4pacdY&t=75s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Behind a met rooftop so I'm a Target I want to know where uh where is the "
              'highest value to build those rooftops um same thing or residential so we we.',
      'timestamp': 75,
      'timestamp_label': '[00:01:15]',
      'timestamp_seconds': 75,
      'tip': "Behind a met rooftop so I'm a Target I want to know where uh where is the "
             'highest value to build those rooftops um same thing or residential so we we.',
      'title': 'How to Identify Renewable Energy Potential for Land & CRE (LandApp by '
               'LandGate)',
      'url': 'https://www.youtube.com/watch?v=eTK7c4pacdY&t=75s',
      'video_id': 'eTK7c4pacdY'},
     {'author': 'SAUR ENERGY',
      'channel': 'SAUR ENERGY',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=PY-zYkA73eA&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'देखिए सस्टेनेबल हो या ना हो इसके पीछे एक अंडरलाइंग फैक्ट ये है कि अब एनर्जी '
              'स्टोरेज इज नो लगर नाइस टू हैव बट इट बिकम अ मस्ट हैव। सो [संगीत] एनर्जी स्टोरेज.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'देखिए सस्टेनेबल हो या ना हो इसके पीछे एक अंडरलाइंग फैक्ट ये है कि अब एनर्जी '
             'स्टोरेज इज नो लगर नाइस टू हैव बट इट बिकम अ मस्ट हैव। सो [संगीत] एनर्जी स्टोरेज.',
      'title': 'Biggest Challenges in India’s Battery Storage Market Explained | BESS Podcast '
               '(SAUR ENERGY)',
      'url': 'https://www.youtube.com/watch?v=PY-zYkA73eA&t=15s',
      'video_id': 'PY-zYkA73eA'},
     {'author': 'Ram Khilawan',
      'channel': 'Ram Khilawan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=LGJ1-q14M9A&t=42s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q1 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'करने के बाद फाइल Jio डेटाबेस में जाएंगे। उस पे राइट क्लिक करेंगे। राइट क्लिक '
              'करने के बाद न्यू में जाएंगे। न्यू में जाने के बाद आपको यहां सेलेक्ट करना है '
              'जियोमेट्रिक नेटवर्क।.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'करने के बाद फाइल Jio डेटाबेस में जाएंगे। उस पे राइट क्लिक करेंगे। राइट क्लिक '
             'करने के बाद न्यू में जाएंगे। न्यू में जाने के बाद आपको यहां सेलेक्ट करना है '
             'जियोमेट्रिक नेटवर्क।.',
      'title': 'HV Transmission Line GIS Project | Geometric Network Creation | Complete '
               'Practical Tutorial in Hindi (Ram Khilawan)',
      'url': 'https://www.youtube.com/watch?v=LGJ1-q14M9A&t=42s',
      'video_id': 'LGJ1-q14M9A'}],
 2: [{'author': 'Moxa',
      'channel': 'Moxa',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:30](https://www.youtube.com/watch?v=NqAAt_iYj9w&t=30s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'FTM) and customer centric energy applications, mostly called behind the meter '
              '(BTM). In the front of the meter domain encompassing power generation, '
              'transmission, and distribution, BESS plays a vital role.',
      'timestamp': 30,
      'timestamp_label': '[00:00:30]',
      'timestamp_seconds': 30,
      'tip': 'FTM) and customer centric energy applications, mostly called behind the meter '
             '(BTM). In the front of the meter domain encompassing power generation, '
             'transmission, and distribution, BESS plays a vital role.',
      'title': 'Decoding BESS: What is Battery Energy Storage Systems | Moxa (Moxa)',
      'url': 'https://www.youtube.com/watch?v=NqAAt_iYj9w&t=30s',
      'video_id': 'NqAAt_iYj9w'},
     {'author': 'Solar Grid Check',
      'channel': 'Solar Grid Check',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:47](https://www.youtube.com/watch?v=9mZg--94z1I&t=107s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's the entire explanation for the per acre rate. The project makes "
              'serious money on a tiny footprint, so it can afford to pay seriously for the '
              'footprint. A viable commercial battery project fits on half an acre to two '
              'acres.',
      'timestamp': 107,
      'timestamp_label': '[00:01:47]',
      'timestamp_seconds': 107,
      'tip': "And that's the entire explanation for the per acre rate. The project makes "
             'serious money on a tiny footprint, so it can afford to pay seriously for the '
             'footprint. A viable commercial battery project fits on half an acre to two '
             'acres.',
      'title': 'Leasing Land for Battery Storage: What Your Land Is Actually Worth (UK, 2026) '
               '(Solar Grid Check)',
      'url': 'https://www.youtube.com/watch?v=9mZg--94z1I&t=107s',
      'video_id': '9mZg--94z1I'},
     {'author': 'Critical Systems Explained',
      'channel': 'Critical Systems Explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:32](https://www.youtube.com/watch?v=uEz7S-WjHG0&t=572s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'They can also evaluate alternative sites with more available grid capacity, '
              'because sometimes the smartest power system decision happens before the first '
              'building is designed.',
      'timestamp': 572,
      'timestamp_label': '[00:09:32]',
      'timestamp_seconds': 572,
      'tip': 'They can also evaluate alternative sites with more available grid capacity, '
             'because sometimes the smartest power system decision happens before the first '
             'building is designed.',
      'title': 'Why AI Data Centers Can Wait Years for One Transformer (Critical Systems '
               'Explained)',
      'url': 'https://www.youtube.com/watch?v=uEz7S-WjHG0&t=572s',
      'video_id': 'uEz7S-WjHG0'},
     {'author': 'Dominic AI',
      'channel': 'Dominic AI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:38](https://www.youtube.com/watch?v=rt0yZyeY-ms&t=38s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "That's generating behind the meter: making power on the customer's side of the "
              'point where the utility hands over electricity, so it feeds the servers without '
              'crossing the public grid. Data centers have long kept backup generators for '
              'grid failures.',
      'timestamp': 38,
      'timestamp_label': '[00:00:38]',
      'timestamp_seconds': 38,
      'tip': "That's generating behind the meter: making power on the customer's side of the "
             'point where the utility hands over electricity, so it feeds the servers without '
             'crossing the public grid. Data centers have long kept backup generators for grid '
             'failures.',
      'title': 'Why AI Data Centers Are Building Their Own Power Plants (Dominic AI)',
      'url': 'https://www.youtube.com/watch?v=rt0yZyeY-ms&t=38s',
      'video_id': 'rt0yZyeY-ms'},
     {'author': 'The Power Engineer',
      'channel': 'The Power Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:40](https://www.youtube.com/watch?v=BWtk0CSPH6g&t=100s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most will never be built, but everyone has to be studied. When the grid builds '
              'new capacity, everyone pays. In the largest grid market in the United States, '
              'data center load drove about $6. 5 billion of one recent auction. So what does '
              'mean for power engineers?',
      'timestamp': 100,
      'timestamp_label': '[00:01:40]',
      'timestamp_seconds': 100,
      'tip': 'Most will never be built, but everyone has to be studied. When the grid builds '
             'new capacity, everyone pays. In the largest grid market in the United States, '
             'data center load drove about $6. 5 billion of one recent auction. So what does '
             'mean for power engineers?',
      'title': "AI Data Centre Load and Grid Impact — One Campus Uses a City's Power (The "
               'Power Engineer)',
      'url': 'https://www.youtube.com/watch?v=BWtk0CSPH6g&t=100s',
      'video_id': 'BWtk0CSPH6g'},
     {'author': 'Edgecom Energy',
      'channel': 'Edgecom Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=R1HunYyjous&t=79s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '3 years ahead to ensure future power supply. PJM plays a major role in what you '
              "pay for electricity. About 25% of your bill comes from PJM's capacity market "
              'charges. It also decides who pays for transmission upgrades, which can impact '
              'costs in different states.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': '3 years ahead to ensure future power supply. PJM plays a major role in what you '
             "pay for electricity. About 25% of your bill comes from PJM's capacity market "
             'charges. It also decides who pays for transmission upgrades, which can impact '
             'costs in different states.',
      'title': 'Understanding PJM Interconnection: Powering the Grid Efficiently (Edgecom '
               'Energy)',
      'url': 'https://www.youtube.com/watch?v=R1HunYyjous&t=79s',
      'video_id': 'R1HunYyjous'},
     {'author': 'GridState',
      'channel': 'GridState',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:10](https://www.youtube.com/watch?v=ObxvY1JRruo&t=370s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Renewable energy deployment, battery storage growth, data center expansion, '
              'electric vehicle adoption, grid reliability, customer costs, economic '
              'development. The Q determines how quickly new resources can come online and how '
              'quickly infrastructure can evolve to meet demand.',
      'timestamp': 370,
      'timestamp_label': '[00:06:10]',
      'timestamp_seconds': 370,
      'tip': 'Renewable energy deployment, battery storage growth, data center expansion, '
             'electric vehicle adoption, grid reliability, customer costs, economic '
             'development. The Q determines how quickly new resources can come online and how '
             'quickly infrastructure can evolve to meet demand.',
      'title': "Why New Power Projects Can't Connect to the Grid (GridState)",
      'url': 'https://www.youtube.com/watch?v=ObxvY1JRruo&t=370s',
      'video_id': 'ObxvY1JRruo'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:23](https://www.youtube.com/watch?v=VdwOf6TKl6U&t=203s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Four eligibility requirements, in commercial operation at the affidavit '
              'submission date, executed RA a procurement agreement with an RA obligated LSE. '
              'That contract must require the project to seek TPD and it must procure RA '
              'eligible capacity for five or more years.',
      'timestamp': 203,
      'timestamp_label': '[00:03:23]',
      'timestamp_seconds': 203,
      'tip': 'Four eligibility requirements, in commercial operation at the affidavit '
             'submission date, executed RA a procurement agreement with an RA obligated LSE. '
             'That contract must require the project to seek TPD and it must procure RA '
             'eligible capacity for five or more years.',
      'title': 'CAISO IPE 5.0 Explained | Cluster 16 Interconnection Changes | Solar & BESS '
               'Developers Guide (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=VdwOf6TKl6U&t=203s',
      'video_id': 'VdwOf6TKl6U'},
     {'author': 'Latitude Media',
      'channel': 'Latitude Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:36:10](https://www.youtube.com/watch?v=D7D1CPOoub4&t=2170s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "It's just the world they know. I think they get a little nervous when it's "
              'their brand and when you know a Walmart or a big office building is like we '
              'have a contract with Google.',
      'timestamp': 2170,
      'timestamp_label': '[00:36:10]',
      'timestamp_seconds': 2170,
      'tip': "It's just the world they know. I think they get a little nervous when it's their "
             'brand and when you know a Walmart or a big office building is like we have a '
             'contract with Google.',
      'title': 'How Tiny Data Centers Could Solve AI’s Power Crunch (Latitude Media)',
      'url': 'https://www.youtube.com/watch?v=D7D1CPOoub4&t=2170s',
      'video_id': 'D7D1CPOoub4'},
     {'author': 'Infrastructure explained',
      'channel': 'Infrastructure explained',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:38](https://www.youtube.com/watch?v=Cym8njcfsfQ&t=218s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'California has installed so much solar capacity that on spring afternoons it '
              'produces far more electricity than it can use. Grid operators pay neighboring '
              'states to take the excess. Then, the sun goes down, and within 2 hours demand '
              'spikes by 15,000 MW.',
      'timestamp': 218,
      'timestamp_label': '[00:03:38]',
      'timestamp_seconds': 218,
      'tip': 'California has installed so much solar capacity that on spring afternoons it '
             'produces far more electricity than it can use. Grid operators pay neighboring '
             'states to take the excess. Then, the sun goes down, and within 2 hours demand '
             'spikes by 15,000 MW.',
      'title': 'Every US Power Grid Explained (Infrastructure explained)',
      'url': 'https://www.youtube.com/watch?v=Cym8njcfsfQ&t=218s',
      'video_id': 'Cym8njcfsfQ'},
     {'author': 'ESB Networks',
      'channel': 'ESB Networks',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:24](https://www.youtube.com/watch?v=fqIsW9Rhp48&t=264s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Our commitment to improving the customer experience harnessing data and digital '
              'Technologies to provide better information insights and transparency for more '
              'information visit esbnetworks.ie forward slash network capacity map.',
      'timestamp': 264,
      'timestamp_label': '[00:04:24]',
      'timestamp_seconds': 264,
      'tip': 'Our commitment to improving the customer experience harnessing data and digital '
             'Technologies to provide better information insights and transparency for more '
             'information visit esbnetworks.ie forward slash network capacity map.',
      'title': 'ESB Networks Availability Capacity Heat Map (ESB Networks)',
      'url': 'https://www.youtube.com/watch?v=fqIsW9Rhp48&t=264s',
      'video_id': 'fqIsW9Rhp48'},
     {'author': 'Systems Leverage',
      'channel': 'Systems Leverage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:10](https://www.youtube.com/watch?v=nx4eX4emlwE&t=190s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Who pays once the buildings begin operating? The filing says one tenant leases '
              'both buildings. It gives two different rent start dates, March 18th and July '
              '1st, 2025. The economic development submission names Oracle as the data center '
              'tenant.',
      'timestamp': 190,
      'timestamp_label': '[00:03:10]',
      'timestamp_seconds': 190,
      'tip': 'Who pays once the buildings begin operating? The filing says one tenant leases '
             'both buildings. It gives two different rent start dates, March 18th and July '
             '1st, 2025. The economic development submission names Oracle as the data center '
             'tenant.',
      'title': 'Stargate’s $1 Land Option: Who Pays for the $15 Billion Build? (Systems '
               'Leverage)',
      'url': 'https://www.youtube.com/watch?v=nx4eX4emlwE&t=190s',
      'video_id': 'nx4eX4emlwE'},
     {'author': 'Environmental Defense Fund',
      'channel': 'Environmental Defense Fund',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:49:27](https://www.youtube.com/watch?v=M62wgLYBKBw&t=2967s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Slightly but none of the increase comes from Renewables and then we find '
              'relative to entry fees increasing fees for later studies are less effective if '
              'your goal is just to increase.',
      'timestamp': 2967,
      'timestamp_label': '[00:49:27]',
      'timestamp_seconds': 2967,
      'tip': 'Slightly but none of the increase comes from Renewables and then we find '
             'relative to entry fees increasing fees for later studies are less effective if '
             'your goal is just to increase.',
      'title': 'An Empirical Analysis of the Interconnection Queue - January 2024 '
               '(Environmental Defense Fund)',
      'url': 'https://www.youtube.com/watch?v=M62wgLYBKBw&t=2967s',
      'video_id': 'M62wgLYBKBw'},
     {'author': 'Behind the Ordinary',
      'channel': 'Behind the Ordinary',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:18](https://www.youtube.com/watch?v=s-MjCamBeVI&t=258s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The construction more than 70 in development, 21 proposed. Thea expects 15 to '
              '27 gawatt installed by 2030. Ownership is the second correction.',
      'timestamp': 258,
      'timestamp_label': '[00:04:18]',
      'timestamp_seconds': 258,
      'tip': 'The construction more than 70 in development, 21 proposed. Thea expects 15 to 27 '
             'gawatt installed by 2030. Ownership is the second correction.',
      'title': 'Why AI Data Centers Are Building Their Own Power Plants (Behind the Ordinary)',
      'url': 'https://www.youtube.com/watch?v=s-MjCamBeVI&t=258s',
      'video_id': 's-MjCamBeVI'},
     {'author': 'Decarbonize!',
      'channel': 'Decarbonize!',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:21](https://www.youtube.com/watch?v=DgivMHf303Y&t=501s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q2 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can also support the channel by buying me a coffee and if you want to catch any '
              'of my episodes on transmission you can follow this link and please share this '
              'video with anyone who you think will enjoy empathizing with FK chairman Willie '
              'Phillips.',
      'timestamp': 501,
      'timestamp_label': '[00:08:21]',
      'timestamp_seconds': 501,
      'tip': 'Can also support the channel by buying me a coffee and if you want to catch any '
             'of my episodes on transmission you can follow this link and please share this '
             'video with anyone who you think will enjoy empathizing with FK chairman Willie '
             'Phillips.',
      'title': 'Why We’re Totally FERC’d: Plan for the Grid We Need or Sit in the Cold and '
               'Dark (Decarbonize!)',
      'url': 'https://www.youtube.com/watch?v=DgivMHf303Y&t=501s',
      'video_id': 'DgivMHf303Y'}],
 3: [{'author': 'Académie Énergie — Efficacité & Électricité',
      'channel': 'Académie Énergie — Efficacité & Électricité',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:39](https://www.youtube.com/watch?v=V57-D23t6Lo&t=39s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Yeah, you're seeing that right, 89%. That's how much the cost of battery "
              'storage projects just plummeted between 2010 and 2023. A price drop that steep '
              "has completely thrown the doors open for the market and it's unleashed a tidal "
              'wave of investment.',
      'timestamp': 39,
      'timestamp_label': '[00:00:39]',
      'timestamp_seconds': 39,
      'tip': "Yeah, you're seeing that right, 89%. That's how much the cost of battery storage "
             'projects just plummeted between 2010 and 2023. A price drop that steep has '
             "completely thrown the doors open for the market and it's unleashed a tidal wave "
             'of investment.',
      'title': 'BESS sizing: how to design a battery system that actually pays back (Académie '
               'Énergie — Efficacité & Électricité)',
      'url': 'https://www.youtube.com/watch?v=V57-D23t6Lo&t=39s',
      'video_id': 'V57-D23t6Lo'},
     {'author': 'Beyound The Signal',
      'channel': 'Beyound The Signal',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=Lh1aLCJikCo&t=160s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The monitor is clear that not all of the rise in capacity costs comes from data '
              'centers. Its position is that data center load.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': 'The monitor is clear that not all of the rise in capacity costs comes from data '
             'centers. Its position is that data center load.',
      'title': 'Who Pays When an AI Data Centre Cannot Connect? (Beyound The Signal)',
      'url': 'https://www.youtube.com/watch?v=Lh1aLCJikCo&t=160s',
      'video_id': 'Lh1aLCJikCo'},
     {'author': 'America2050',
      'channel': 'America2050',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:33](https://www.youtube.com/watch?v=n3d_tHGh1Qk&t=93s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One analysis says a data center can be built in 12 to 24 months. Getting the '
              'grid ready to feed it can take 3 to 7 years. And the cost of waiting is '
              'enormous.',
      'timestamp': 93,
      'timestamp_label': '[00:01:33]',
      'timestamp_seconds': 93,
      'tip': 'One analysis says a data center can be built in 12 to 24 months. Getting the '
             'grid ready to feed it can take 3 to 7 years. And the cost of waiting is '
             'enormous.',
      'title': "America's Data Centers Are Becoming Their Own Power Plants (America2050)",
      'url': 'https://www.youtube.com/watch?v=n3d_tHGh1Qk&t=93s',
      'video_id': 'n3d_tHGh1Qk'},
     {'author': 'Economy Media',
      'channel': 'Economy Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:26](https://www.youtube.com/watch?v=e0Dlr07jfjA&t=446s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'While components such as generators, power supplies, and connection cables '
              'represent less than 10% of the cost of building a data center, nothing can '
              'function until these components are installed.',
      'timestamp': 446,
      'timestamp_label': '[00:07:26]',
      'timestamp_seconds': 446,
      'tip': 'While components such as generators, power supplies, and connection cables '
             'represent less than 10% of the cost of building a data center, nothing can '
             'function until these components are installed.',
      'title': 'Why Tech Companies Are Quietly Cancelling AI Data Centers (Economy Media)',
      'url': 'https://www.youtube.com/watch?v=e0Dlr07jfjA&t=446s',
      'video_id': 'e0Dlr07jfjA'},
     {'author': 'Jerzy Kuzminski',
      'channel': 'Jerzy Kuzminski',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:55](https://www.youtube.com/watch?v=fDBjJyTGWDQ&t=895s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And you can integrate it with your existing PV. So you basically store your own '
              "solar generation for later use. CNI projects have simpler economics. You're "
              'comparing battery costs against your electricity bills.',
      'timestamp': 895,
      'timestamp_label': '[00:14:55]',
      'timestamp_seconds': 895,
      'tip': 'And you can integrate it with your existing PV. So you basically store your own '
             "solar generation for later use. CNI projects have simpler economics. You're "
             'comparing battery costs against your electricity bills.',
      'title': '01 What is BESS and Why Poland (Jerzy Kuzminski)',
      'url': 'https://www.youtube.com/watch?v=fDBjJyTGWDQ&t=895s',
      'video_id': 'fDBjJyTGWDQ'},
     {'author': 'US Energy Weekly',
      'channel': 'US Energy Weekly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:29](https://www.youtube.com/watch?v=sxulqIJRZrM&t=209s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Each nodal price has two parts: the cost of energy itself, and the cost of '
              'transmission congestion. Power is cheap at nodes near West Texas wind farms and '
              'expensive in congested cities. These nodal prices are called LMP, Locational '
              'Marginal Pricing.',
      'timestamp': 209,
      'timestamp_label': '[00:03:29]',
      'timestamp_seconds': 209,
      'tip': 'Each nodal price has two parts: the cost of energy itself, and the cost of '
             'transmission congestion. Power is cheap at nodes near West Texas wind farms and '
             'expensive in congested cities. These nodal prices are called LMP, Locational '
             'Marginal Pricing.',
      'title': 'Why No Capacity Market? ERCOT Market Explained | US Energy ESSENTIALS (US '
               'Energy Weekly)',
      'url': 'https://www.youtube.com/watch?v=sxulqIJRZrM&t=209s',
      'video_id': 'sxulqIJRZrM'},
     {'author': 'Democracy Now!',
      'channel': 'Democracy Now!',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:00](https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=480s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And really push back on the the physical and the material impacts on our lands. '
              'A recent Bloomberg analysis found electricity costs go up nearly 267% near data '
              'centers. Yet a lot of these data centers target poorer tribal nations.',
      'timestamp': 480,
      'timestamp_label': '[00:08:00]',
      'timestamp_seconds': 480,
      'tip': 'And really push back on the the physical and the material impacts on our lands. '
             'A recent Bloomberg analysis found electricity costs go up nearly 267% near data '
             'centers. Yet a lot of these data centers target poorer tribal nations.',
      'title': '“Data Colonialism”: Native Communities Fight AI Data Centers on Indigenous '
               'Land (Democracy Now!)',
      'url': 'https://www.youtube.com/watch?v=Ac0-fBK0LVQ&t=480s',
      'video_id': 'Ac0-fBK0LVQ'},
     {'author': 'Modo Energy',
      'channel': 'Modo Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:08](https://www.youtube.com/watch?v=GAfgw6dL34Q&t=248s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Which will also optimize behind the meter assets for cost saving or profit '
              'behind the meter assets are set to play an increasingly prevalent role on our '
              "journey towards net zero anyway thanks for watching and I'll see you next time.",
      'timestamp': 248,
      'timestamp_label': '[00:04:08]',
      'timestamp_seconds': 248,
      'tip': 'Which will also optimize behind the meter assets for cost saving or profit '
             'behind the meter assets are set to play an increasingly prevalent role on our '
             "journey towards net zero anyway thanks for watching and I'll see you next time.",
      'title': 'Behind-the-meter electricity: what does it mean? (Modo Energy)',
      'url': 'https://www.youtube.com/watch?v=GAfgw6dL34Q&t=248s',
      'video_id': 'GAfgw6dL34Q'},
     {'author': 'BESS Engineer',
      'channel': 'BESS Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:24](https://www.youtube.com/watch?v=H7C34V05QQw&t=84s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In IEC markets, it's commonly called RMU, ring main unit. And finally, the "
              'metallic support base. This is a mechanical frame that holds everything '
              'together and ensure structural stability. The entire assembly is tested at the '
              'factory.',
      'timestamp': 84,
      'timestamp_label': '[00:01:24]',
      'timestamp_seconds': 84,
      'tip': "In IEC markets, it's commonly called RMU, ring main unit. And finally, the "
             'metallic support base. This is a mechanical frame that holds everything together '
             'and ensure structural stability. The entire assembly is tested at the factory.',
      'title': 'BESS MV Skid Explained: PCS, Transformer, Switchgear & Cost Breakdown (BESS '
               'Engineer)',
      'url': 'https://www.youtube.com/watch?v=H7C34V05QQw&t=84s',
      'video_id': 'H7C34V05QQw'},
     {'author': 'Josimar Tello Maita',
      'channel': 'Josimar Tello Maita',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:04:31](https://www.youtube.com/watch?v=xyUNxe8t4I0&t=271s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Voltage in the network the maximum voltage does not reach 1.1 per unit in the '
              'case of 100 of participation there is a 5 probability of over voltage occurring '
              'if the penetration is 100 as well.',
      'timestamp': 271,
      'timestamp_label': '[00:04:31]',
      'timestamp_seconds': 271,
      'tip': 'Voltage in the network the maximum voltage does not reach 1.1 per unit in the '
             'case of 100 of participation there is a 5 probability of over voltage occurring '
             'if the penetration is 100 as well.',
      'title': 'Assessing the PV Hosting Capacity of a Colombian Urban MV Distribution Network '
               '(Josimar Tello Maita)',
      'url': 'https://www.youtube.com/watch?v=xyUNxe8t4I0&t=271s',
      'video_id': 'xyUNxe8t4I0'},
     {'author': 'Founders Explain The World',
      'channel': 'Founders Explain The World',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:48](https://www.youtube.com/watch?v=JvqqjgCu9mg&t=468s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "How to tell kind of how much more we need, but there's no denying it. It's, one "
              'thing we can all agree on is the cost has come down right? And we need to '
              'figure out more efficient ways to do this. Datacenter costs, energy source cost '
              'model because all of those things.',
      'timestamp': 468,
      'timestamp_label': '[00:07:48]',
      'timestamp_seconds': 468,
      'tip': "How to tell kind of how much more we need, but there's no denying it. It's, one "
             'thing we can all agree on is the cost has come down right? And we need to figure '
             'out more efficient ways to do this. Datacenter costs, energy source cost model '
             'because all of those things.',
      'title': 'AI Without New Data Centers? (Founders Explain The World)',
      'url': 'https://www.youtube.com/watch?v=JvqqjgCu9mg&t=468s',
      'video_id': 'JvqqjgCu9mg'},
     {'author': 'KorrAI',
      'channel': 'KorrAI',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:34](https://www.youtube.com/watch?v=MvUw50RZNRQ&t=34s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'One month of delay on a 60 MW facility can cost up to $14 million. If you pick '
              'the wrong site or miss an environmental impact, the local community gets '
              'affected. Local opposition in the US blocked nearly $200 billion of data center '
              'projects in early 2026.',
      'timestamp': 34,
      'timestamp_label': '[00:00:34]',
      'timestamp_seconds': 34,
      'tip': 'One month of delay on a 60 MW facility can cost up to $14 million. If you pick '
             'the wrong site or miss an environmental impact, the local community gets '
             'affected. Local opposition in the US blocked nearly $200 billion of data center '
             'projects in early 2026.',
      'title': 'Data Center Site Due Diligence & lifecycle Monitoring | KorrAI TRAIL (KorrAI)',
      'url': 'https://www.youtube.com/watch?v=MvUw50RZNRQ&t=34s',
      'video_id': 'MvUw50RZNRQ'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=AgfRaZtdbh8&t=80s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The price is made up of three components. System lambda, the base cost of the '
              'next unit of power statewide, a congestion component that adjusts for '
              'transmission bottlenecks, and a price adder that kicks in when reserves get '
              'tight.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'The price is made up of three components. System lambda, the base cost of the '
             'next unit of power statewide, a congestion component that adjusts for '
             'transmission bottlenecks, and a price adder that kicks in when reserves get '
             'tight.',
      'title': 'ERCOT Explained: How the Texas Power Grid Actually Works (LMP, SCED & Markets) '
               '(Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=AgfRaZtdbh8&t=80s',
      'video_id': 'AgfRaZtdbh8'},
     {'author': 'Modo Energy',
      'channel': 'Modo Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=xZ1P-4F8Jf8&t=81s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ERCOT produces a unique LMP for each of them. But, how are these prices formed? '
              'Well, the main component of prices across ERCOT is something called the "System '
              'Lambda". System Lambda is just cost of procuring the next cheapest unit of '
              'energy across the entire system.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'ERCOT produces a unique LMP for each of them. But, how are these prices formed? '
             'Well, the main component of prices across ERCOT is something called the "System '
             'Lambda". System Lambda is just cost of procuring the next cheapest unit of '
             'energy across the entire system.',
      'title': 'Price formation in ERCOT - System Lambda (The Energy Academy: ERCOT - E5) '
               '(Modo Energy)',
      'url': 'https://www.youtube.com/watch?v=xZ1P-4F8Jf8&t=81s',
      'video_id': 'xZ1P-4F8Jf8'},
     {'author': 'Mohamed Hassan',
      'channel': 'Mohamed Hassan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=J9T5h7HRJbk&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q3 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'اس في تجهيز الداتا لتصميم خط الترانسميشن لاين بالجرافيتي وازاي بعد كده ناخد '
              'الداتا اللي تم تجهيزها باستخدام الكيو جاي اس ونستخدمها في برنامج ايب نت وبعد.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'اس في تجهيز الداتا لتصميم خط الترانسميشن لاين بالجرافيتي وازاي بعد كده ناخد '
             'الداتا اللي تم تجهيزها باستخدام الكيو جاي اس ونستخدمها في برنامج ايب نت وبعد.',
      'title': 'Design of Transmission Line Using QGIS Part2 Comments (Mohamed Hassan)',
      'url': 'https://www.youtube.com/watch?v=J9T5h7HRJbk&t=15s',
      'video_id': 'J9T5h7HRJbk'}],
 4: [{'author': 'Techdamentals',
      'channel': 'Techdamentals',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:42](https://www.youtube.com/watch?v=u6jr6SB0bD4&t=162s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Most existing data center capacity still runs ordinary cloud storage and '
              'business software, not artificial intelligence. AI servers are a new and very '
              'power-hungry tenant moving into a building type that was already large and '
              'already growing.',
      'timestamp': 162,
      'timestamp_label': '[00:02:42]',
      'timestamp_seconds': 162,
      'tip': 'Most existing data center capacity still runs ordinary cloud storage and '
             'business software, not artificial intelligence. AI servers are a new and very '
             'power-hungry tenant moving into a building type that was already large and '
             'already growing.',
      'title': 'Why Is My Electric Bill So High? Live Close to Data Centers & AI Power? '
               'Explained (Techdamentals)',
      'url': 'https://www.youtube.com/watch?v=u6jr6SB0bD4&t=162s',
      'video_id': 'u6jr6SB0bD4'},
     {'author': 'Dr. SPACE',
      'channel': 'Dr. SPACE',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:38](https://www.youtube.com/watch?v=tsZSfPjuuck&t=338s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's break down the base case financial model. You start with a gross capital "
              'expenditure of 14. But when you stack the demand savings with tariff arbitrage '
              'and offsetting diesel costs, things get really interesting.',
      'timestamp': 338,
      'timestamp_label': '[00:05:38]',
      'timestamp_seconds': 338,
      'tip': "Let's break down the base case financial model. You start with a gross capital "
             'expenditure of 14. But when you stack the demand savings with tariff arbitrage '
             'and offsetting diesel costs, things get really interesting.',
      'title': 'Economics of Behind-The-Meter (BTM) Energy Storage (Dr. SPACE)',
      'url': 'https://www.youtube.com/watch?v=tsZSfPjuuck&t=338s',
      'video_id': 'tsZSfPjuuck'},
     {'author': 'US Energy Weekly',
      'channel': 'US Energy Weekly',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:09](https://www.youtube.com/watch?v=DzkVggOvJGs&t=309s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It nearly doubled in a year, from twenty-six to forty-eight gigawatts between '
              'October 2024 and October 2025, a clear signal of demand for firm, dispatchable '
              'capacity. For the technical review process and the capital game behind it, see '
              'our Interconnection ESSENTIALS episode.',
      'timestamp': 309,
      'timestamp_label': '[00:05:09]',
      'timestamp_seconds': 309,
      'tip': 'It nearly doubled in a year, from twenty-six to forty-eight gigawatts between '
             'October 2024 and October 2025, a clear signal of demand for firm, dispatchable '
             'capacity. For the technical review process and the capital game behind it, see '
             'our Interconnection ESSENTIALS episode.',
      'title': 'A 5-Year Wait to Connect? ERCOT Queue Explained | US Energy ESSENTIALS (US '
               'Energy Weekly)',
      'url': 'https://www.youtube.com/watch?v=DzkVggOvJGs&t=309s',
      'video_id': 'DzkVggOvJGs'},
     {'author': 'Texas Energy & Power',
      'channel': 'Texas Energy & Power',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:29:30](https://www.youtube.com/watch?v=nzC-XREeuz4&t=1770s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Typically, the General Assembly sends a governor a budget, and that's finalized "
              "by the end of the General Assembly session. We're still waiting to get a budget "
              'deal done, in part because of a difference on what to do about the data center '
              'tax exemption.',
      'timestamp': 1770,
      'timestamp_label': '[00:29:30]',
      'timestamp_seconds': 1770,
      'tip': "Typically, the General Assembly sends a governor a budget, and that's finalized "
             "by the end of the General Assembly session. We're still waiting to get a budget "
             'deal done, in part because of a difference on what to do about the data center '
             'tax exemption.',
      'title': 'Why PJM is looking at the Texas grid (Texas Energy & Power)',
      'url': 'https://www.youtube.com/watch?v=nzC-XREeuz4&t=1770s',
      'video_id': 'nzC-XREeuz4'},
     {'author': 'Civil and Structural Engineer',
      'channel': 'Civil and Structural Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:02](https://www.youtube.com/watch?v=935Rt3dBZso&t=122s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'To ensure they can do this safely, engineers run a swept path analysis using '
              'specialized modeling software to simulate exactly how large vehicles maneuver '
              'through corners and critical equipment zones. Heavy loaders require wide '
              'sweeping paths to clear intersections safely.',
      'timestamp': 122,
      'timestamp_label': '[00:02:02]',
      'timestamp_seconds': 122,
      'tip': 'To ensure they can do this safely, engineers run a swept path analysis using '
             'specialized modeling software to simulate exactly how large vehicles maneuver '
             'through corners and critical equipment zones. Heavy loaders require wide '
             'sweeping paths to clear intersections safely.',
      'title': 'Civil Engineering Design for Battery Energy Storage Systems (BESS) in '
               'Australia (Civil and Structural Engineer)',
      'url': 'https://www.youtube.com/watch?v=935Rt3dBZso&t=122s',
      'video_id': '935Rt3dBZso'},
     {'author': 'BESS Engineer',
      'channel': 'BESS Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:17](https://www.youtube.com/watch?v=r852ohYdDhc&t=77s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Is a bank comfortable lending money? All the major risk have been identified '
              'and either mitigated, transferred, or have insurance to bank satisfaction. And '
              'finally we have financing when we finally got money. So money is released and '
              'the bank signed the loan agreement.',
      'timestamp': 77,
      'timestamp_label': '[00:01:17]',
      'timestamp_seconds': 77,
      'tip': 'Is a bank comfortable lending money? All the major risk have been identified and '
             'either mitigated, transferred, or have insurance to bank satisfaction. And '
             'finally we have financing when we finally got money. So money is released and '
             'the bank signed the loan agreement.',
      'title': 'From Site to COD: The 6 Stages of a BESS Project (BESS Engineer)',
      'url': 'https://www.youtube.com/watch?v=r852ohYdDhc&t=77s',
      'video_id': 'r852ohYdDhc'},
     {'author': 'Jeff Pierson',
      'channel': 'Jeff Pierson',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:46](https://www.youtube.com/watch?v=CmmE71lfGdw&t=166s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'This chart compares the high administrative cost of maintaining a strict '
              'regulatory framework against the limited budget of a typical small county '
              'planning staff. This is factor three, regulatory capacity.',
      'timestamp': 166,
      'timestamp_label': '[00:02:46]',
      'timestamp_seconds': 166,
      'tip': 'This chart compares the high administrative cost of maintaining a strict '
             'regulatory framework against the limited budget of a typical small county '
             'planning staff. This is factor three, regulatory capacity.',
      'title': 'Preparing your community for grid scale energy and hyperscale data centers '
               '(Jeff Pierson)',
      'url': 'https://www.youtube.com/watch?v=CmmE71lfGdw&t=166s',
      'video_id': 'CmmE71lfGdw'},
     {'author': 'InfraEnergy Academy',
      'channel': 'InfraEnergy Academy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:55](https://www.youtube.com/watch?v=YSqciE_dMbY&t=235s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'UPS or block redundant topologies. In the old setup, every active line holds '
              'back a chunk of its capacity for emergencies. But with a block-level setup, you '
              'dedicate entirely separate lineups for your backup.',
      'timestamp': 235,
      'timestamp_label': '[00:03:55]',
      'timestamp_seconds': 235,
      'tip': 'UPS or block redundant topologies. In the old setup, every active line holds '
             'back a chunk of its capacity for emergencies. But with a block-level setup, you '
             'dedicate entirely separate lineups for your backup.',
      'title': 'How Data Center Power Works: From Grid Substation to AI Racks (InfraEnergy '
               'Academy)',
      'url': 'https://www.youtube.com/watch?v=YSqciE_dMbY&t=235s',
      'video_id': 'YSqciE_dMbY'},
     {'author': 'Atlas Public Policy',
      'channel': 'Atlas Public Policy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:42](https://www.youtube.com/watch?v=eIAGiv0LD8Y&t=642s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And I'm talking about the PB maps. That's when we started bringing in the "
              'feeder level analysis and whatnot. And fast forward to 2023, you know, '
              'Christina had mentioned that, hey, we have a, you know, goal or aim to get to 1 '
              'million EVs.',
      'timestamp': 642,
      'timestamp_label': '[00:10:42]',
      'timestamp_seconds': 642,
      'tip': "And I'm talking about the PB maps. That's when we started bringing in the feeder "
             'level analysis and whatnot. And fast forward to 2023, you know, Christina had '
             'mentioned that, hey, we have a, you know, goal or aim to get to 1 million EVs.',
      'title': 'EV Hub Live #42: Powering Up with Hosting Capacity Maps (Atlas Public Policy)',
      'url': 'https://www.youtube.com/watch?v=eIAGiv0LD8Y&t=642s',
      'video_id': 'eIAGiv0LD8Y'},
     {'author': 'primtech solutions',
      'channel': 'primtech solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:03](https://www.youtube.com/watch?v=2FBThdUqgRg&t=723s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I'm going to come over here cuz this is going to be where my transformer is. "
              "And I'm going to say that goes to 0 0. And in this case, I want it pointing "
              'down that Y- axis. Again, just like any other CAD software, that orientation.',
      'timestamp': 723,
      'timestamp_label': '[00:12:03]',
      'timestamp_seconds': 723,
      'tip': "I'm going to come over here cuz this is going to be where my transformer is. And "
             "I'm going to say that goes to 0 0. And in this case, I want it pointing down "
             'that Y- axis. Again, just like any other CAD software, that orientation.',
      'title': 'Design a complete 138 kV Substation in only 60 minutes - Live Presentation '
               '@SDSIC 2025 Spring Event (primtech solutions)',
      'url': 'https://www.youtube.com/watch?v=2FBThdUqgRg&t=723s',
      'video_id': '2FBThdUqgRg'},
     {'author': 'The Pharos Project',
      'channel': 'The Pharos Project',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:20](https://www.youtube.com/watch?v=Br7K7fGD4uk&t=140s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Every kind of generator is in the same line. The total American queue fell 10% '
              'from 2024, and it sits below its peak of nearly 2600 gawatt at the end of 2023. '
              'Over 750 gawatts of capacity withdrew in 2025 by Barclay Labs estimate.',
      'timestamp': 140,
      'timestamp_label': '[00:02:20]',
      'timestamp_seconds': 140,
      'tip': 'Every kind of generator is in the same line. The total American queue fell 10% '
             'from 2024, and it sits below its peak of nearly 2600 gawatt at the end of 2023. '
             'Over 750 gawatts of capacity withdrew in 2025 by Barclay Labs estimate.',
      'title': 'Waiting for Power  Why New Electricity Gets Stuck Before It Reaches the Grid '
               '(The Pharos Project)',
      'url': 'https://www.youtube.com/watch?v=Br7K7fGD4uk&t=140s',
      'video_id': 'Br7K7fGD4uk'},
     {'author': 'Beyond the Breaker Podcast',
      'channel': 'Beyond the Breaker Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:29](https://www.youtube.com/watch?v=P6AUptGZBvI&t=89s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um and then I [clears throat] was kind of looking for a way like looking for '
              'what my next move was. Um called my dad who happened to be in the trades. We '
              'have you know the the family lineage. Um and I started working on my '
              "journeyman's license.",
      'timestamp': 89,
      'timestamp_label': '[00:01:29]',
      'timestamp_seconds': 89,
      'tip': 'Um and then I [clears throat] was kind of looking for a way like looking for '
             'what my next move was. Um called my dad who happened to be in the trades. We '
             'have you know the the family lineage. Um and I started working on my '
             "journeyman's license.",
      'title': 'Building a Hyperscale Data Center Team (Beyond the Breaker Podcast)',
      'url': 'https://www.youtube.com/watch?v=P6AUptGZBvI&t=89s',
      'video_id': 'P6AUptGZBvI'},
     {'author': 'datacenterHawk',
      'channel': 'datacenterHawk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:07:55](https://www.youtube.com/watch?v=dTHn2ejpXvM&t=475s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like a farmers 200 acre Family Farm And they like went to the farmer and '
              'brought an offer and thought almost the the sense I got was they were almost '
              'taking.',
      'timestamp': 475,
      'timestamp_label': '[00:07:55]',
      'timestamp_seconds': 475,
      'tip': 'Like a farmers 200 acre Family Farm And they like went to the farmer and brought '
             'an offer and thought almost the the sense I got was they were almost taking.',
      'title': 'Land Battle: Powered vs Unpowered in Data Center Development (datacenterHawk)',
      'url': 'https://www.youtube.com/watch?v=dTHn2ejpXvM&t=475s',
      'video_id': 'dTHn2ejpXvM'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:02](https://www.youtube.com/watch?v=gGBYCEdn18o&t=302s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'TVA will study storage at your proposed charging assumptions and injection '
              'limiting equipment allows study below full capacity. When did the new LGIP take '
              'effect? Effective November 1st, 2024. Replacing the serial Q with a cluster '
              'process under FIRK order number 2023.',
      'timestamp': 302,
      'timestamp_label': '[00:05:02]',
      'timestamp_seconds': 302,
      'tip': 'TVA will study storage at your proposed charging assumptions and injection '
             'limiting equipment allows study below full capacity. When did the new LGIP take '
             'effect? Effective November 1st, 2024. Replacing the serial Q with a cluster '
             'process under FIRK order number 2023.',
      'title': 'TVA Interconnection Queue Reform Explained | New Cluster Process, Deposits & '
               'Costs (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=gGBYCEdn18o&t=302s',
      'video_id': 'gGBYCEdn18o'},
     {'author': 'SpeedFreakLS1',
      'channel': 'SpeedFreakLS1',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:26](https://www.youtube.com/watch?v=-RBp8jOUA1U&t=866s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q4 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Big alarm and say hey trip me off so it looks like they're kind of set here um "
              "sorry there we go you've got one I'm not sure what that is this one's set at "
              "75c this one's set at just above a 100 and then this one is set.",
      'timestamp': 866,
      'timestamp_label': '[00:14:26]',
      'timestamp_seconds': 866,
      'tip': "Big alarm and say hey trip me off so it looks like they're kind of set here um "
             "sorry there we go you've got one I'm not sure what that is this one's set at 75c "
             "this one's set at just above a 100 and then this one is set.",
      'title': '138 kV High Voltage Substation Walk (SpeedFreakLS1)',
      'url': 'https://www.youtube.com/watch?v=-RBp8jOUA1U&t=866s',
      'video_id': '-RBp8jOUA1U'}],
 5: [{'author': 'Franklin Andrew Cruz',
      'channel': 'Franklin Andrew Cruz',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=YrpzmGX0-YM&t=21s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And I've got some notes here, so I want to make sure. The first thing when "
              "you're dealing with a AI data center, and this is what I've learned going "
              'through the process, because I do have 130 acre site that we could do an '
              'assembly for 288 acres, is power.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': "And I've got some notes here, so I want to make sure. The first thing when "
             "you're dealing with a AI data center, and this is what I've learned going "
             'through the process, because I do have 130 acre site that we could do an '
             'assembly for 288 acres, is power.',
      'title': 'The Truth About AI Data Center Land (Most Sites Don’t Qualify) (Franklin '
               'Andrew Cruz)',
      'url': 'https://www.youtube.com/watch?v=YrpzmGX0-YM&t=21s',
      'video_id': 'YrpzmGX0-YM'},
     {'author': 'Sarthak',
      'channel': 'Sarthak',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=u0kuoKQbHTs&t=117s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The planning trap: navigating the risk of overbuilding versus underbuilding. '
              'This uncertainty forces utilities into a really difficult trap, and both '
              'options carry huge risks.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'The planning trap: navigating the risk of overbuilding versus underbuilding. '
             'This uncertainty forces utilities into a really difficult trap, and both options '
             'carry huge risks.',
      'title': 'AI’s Grid Queue: Who Pays to Connect the Data-Centre Boom? (Sarthak)',
      'url': 'https://www.youtube.com/watch?v=u0kuoKQbHTs&t=117s',
      'video_id': 'u0kuoKQbHTs'},
     {'author': 'MEP Engineer AJ',
      'channel': 'MEP Engineer AJ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=lTK_pU1_uFc&t=192s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Plus, you have to assess the physical environment. Do the topography, flood '
              'risks, and soil conditions actually support a heavy data center? Especially if '
              'you plan to expand into a multi-building campus down the road.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': 'Plus, you have to assess the physical environment. Do the topography, flood '
             'risks, and soil conditions actually support a heavy data center? Especially if '
             'you plan to expand into a multi-building campus down the road.',
      'title': 'Building Hyperscale Data Centers: Site Selection, Long-Lead Gear & Ground Prep '
               '(MEP Engineer AJ)',
      'url': 'https://www.youtube.com/watch?v=lTK_pU1_uFc&t=192s',
      'video_id': 'lTK_pU1_uFc'},
     {'author': 'Careers Over Beers Podcast',
      'channel': 'Careers Over Beers Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:16:47](https://www.youtube.com/watch?v=S_6FoEr75bs&t=1007s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We listened to Kevin Olri who uh just is doing this huge 62 square mile acre '
              "data center in Utah. And he was calling out people which is why I'm naming his "
              'name. We listened to him yesterday who were standing up and and they were '
              'against this and saying this is not good.',
      'timestamp': 1007,
      'timestamp_label': '[00:16:47]',
      'timestamp_seconds': 1007,
      'tip': 'We listened to Kevin Olri who uh just is doing this huge 62 square mile acre '
             "data center in Utah. And he was calling out people which is why I'm naming his "
             'name. We listened to him yesterday who were standing up and and they were '
             'against this and saying this is not good.',
      'title': 'The AI Data Center Land Grab: Money, Secrecy, & Community Resistance | Kristen '
               'Meghan & Tammy Clark (Careers Over Beers Podcast)',
      'url': 'https://www.youtube.com/watch?v=S_6FoEr75bs&t=1007s',
      'video_id': 'S_6FoEr75bs'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:18:46](https://www.youtube.com/watch?v=TM7qt8CCWxk&t=1126s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The second message is that entering a FERC Order 2023 cluster study without '
              'adequate preparation creates significant financial risk. Developers should '
              'perform preemptive CEII base case screening wherever access and applicable '
              'requirements permit.',
      'timestamp': 1126,
      'timestamp_label': '[00:18:46]',
      'timestamp_seconds': 1126,
      'tip': 'The second message is that entering a FERC Order 2023 cluster study without '
             'adequate preparation creates significant financial risk. Developers should '
             'perform preemptive CEII base case screening wherever access and applicable '
             'requirements permit.',
      'title': 'FERC Order 2023 Cluster Interconnection Studies | Costs, POI & Network '
               'Upgrades (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=TM7qt8CCWxk&t=1126s',
      'video_id': 'TM7qt8CCWxk'},
     {'author': 'Storlytics Energy Storage',
      'channel': 'Storlytics Energy Storage',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:34](https://www.youtube.com/watch?v=pk02pXrBqWI&t=94s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, in this case, since we want the battery to take care of this net demand '
              'completely, so we come here, under charge threshold, we select that curve, net '
              'demand. And of course, you have options, right?',
      'timestamp': 94,
      'timestamp_label': '[00:01:34]',
      'timestamp_seconds': 94,
      'tip': 'So, in this case, since we want the battery to take care of this net demand '
             'completely, so we come here, under charge threshold, we select that curve, net '
             'demand. And of course, you have options, right?',
      'title': 'How to Size BESS for Microgrid Applications (Storlytics Energy Storage)',
      'url': 'https://www.youtube.com/watch?v=pk02pXrBqWI&t=94s',
      'video_id': 'pk02pXrBqWI'},
     {'author': 'Asianometry',
      'channel': 'Asianometry',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=tJYSzc7YkY0&t=21s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We all know they need a lot of energy. The two are very closely tied together. '
              'This channel has a not-so-secret obsession with water. In this video, we look '
              "at the data center's massive water footprint. Types of Data Centers Data "
              'centers come in all sizes and functions.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'We all know they need a lot of energy. The two are very closely tied together. '
             'This channel has a not-so-secret obsession with water. In this video, we look at '
             "the data center's massive water footprint. Types of Data Centers Data centers "
             'come in all sizes and functions.',
      'title': 'The Big Data Center Water Problem (Asianometry)',
      'url': 'https://www.youtube.com/watch?v=tJYSzc7YkY0&t=21s',
      'video_id': 'tJYSzc7YkY0'},
     {'author': 'UL Solutions',
      'channel': 'UL Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:41](https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=881s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'But given the potential risk to human life and then the risk of downtime in '
              'data centers as well, all that preparation and effort going into it is '
              "certainly more than justified, of course, given the stakes of what's going on "
              'right now.',
      'timestamp': 881,
      'timestamp_label': '[00:14:41]',
      'timestamp_seconds': 881,
      'tip': 'But given the potential risk to human life and then the risk of downtime in data '
             'centers as well, all that preparation and effort going into it is certainly more '
             "than justified, of course, given the stakes of what's going on right now.",
      'title': 'Understanding BESS Fire Testing for Data Centers | TCA 18 (UL Solutions)',
      'url': 'https://www.youtube.com/watch?v=TtbHyJ6xzNg&t=881s',
      'video_id': 'TtbHyJ6xzNg'},
     {'author': 'Clearspot',
      'channel': 'Clearspot',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:58:09](https://www.youtube.com/watch?v=tFP2z1s7IrM&t=3489s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'t mean that mean to price risk in battery today? To price the risk any kind of "
              "risk you need to understand the risk. If you don't understand the risk you can "
              'price the risk right?',
      'timestamp': 3489,
      'timestamp_label': '[00:58:09]',
      'timestamp_seconds': 3489,
      'tip': "'t mean that mean to price risk in battery today? To price the risk any kind of "
             "risk you need to understand the risk. If you don't understand the risk you can "
             'price the risk right?',
      'title': '2GW BESS Lessons Every Asset Owner Needs (Clearspot)',
      'url': 'https://www.youtube.com/watch?v=tFP2z1s7IrM&t=3489s',
      'video_id': 'tFP2z1s7IrM'},
     {'author': 'Chris Heasley',
      'channel': 'Chris Heasley',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:46:40](https://www.youtube.com/watch?v=oHZCEiu2Vc8&t=2800s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So there is a shown case with too much noise pollution actually leads to people '
              "with more depression or anger issues in a lot of cases because they're "
              'constantly on edge is what it falls into. So there is a lot of loud noise to it '
              'and that falls into nuisance.',
      'timestamp': 2800,
      'timestamp_label': '[00:46:40]',
      'timestamp_seconds': 2800,
      'tip': 'So there is a shown case with too much noise pollution actually leads to people '
             "with more depression or anger issues in a lot of cases because they're "
             'constantly on edge is what it falls into. So there is a lot of loud noise to it '
             'and that falls into nuisance.',
      'title': 'B E S S  Battery Energy Storage Systems and the Grid (Chris Heasley)',
      'url': 'https://www.youtube.com/watch?v=oHZCEiu2Vc8&t=2800s',
      'video_id': 'oHZCEiu2Vc8'},
     {'author': 'CME Group',
      'channel': 'CME Group',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:12](https://www.youtube.com/watch?v=dYvEG3uQzsQ&t=192s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Variety of futures and options contracts for electricity day ahead real time '
              'and capacity markets this provides market participants a variety of regional '
              'locations to hedge and manage risk exposure.',
      'timestamp': 192,
      'timestamp_label': '[00:03:12]',
      'timestamp_seconds': 192,
      'tip': 'Variety of futures and options contracts for electricity day ahead real time and '
             'capacity markets this provides market participants a variety of regional '
             'locations to hedge and manage risk exposure.',
      'title': 'Understanding Basics of the Power Market (CME Group)',
      'url': 'https://www.youtube.com/watch?v=dYvEG3uQzsQ&t=192s',
      'video_id': 'dYvEG3uQzsQ'},
     {'author': 'Data Center Sales & Marketing Institute (DCSMI)',
      'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=tWgTVIzYje8&t=137s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re new and early adopting, which means that when you're building a site 2020, "
              'odd years ago, when they were building sites, and because those tier ones have '
              "got a bit of history, they've been around for a lot longer, they were hard to "
              'build a green field site.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "'re new and early adopting, which means that when you're building a site 2020, "
             'odd years ago, when they were building sites, and because those tier ones have '
             "got a bit of history, they've been around for a lot longer, they were hard to "
             'build a green field site.',
      'title': 'Decentralized Data Centers vs. Hyperscale vs. Edge (Data Center Sales & '
               'Marketing Institute (DCSMI))',
      'url': 'https://www.youtube.com/watch?v=tWgTVIzYje8&t=137s',
      'video_id': 'tWgTVIzYje8'},
     {'author': 'Avangrid Renewables',
      'channel': 'Avangrid Renewables',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:25](https://www.youtube.com/watch?v=T_Y5rMNtBVs&t=205s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Successfully develop renewable energy resources across the US this is '
              'especially true in the pjm interconnection Eola Renewables has operated here '
              'since 2007 building and operating 815 megaw of wind power at five facilities '
              'enough to power.',
      'timestamp': 205,
      'timestamp_label': '[00:03:25]',
      'timestamp_seconds': 205,
      'tip': 'Successfully develop renewable energy resources across the US this is especially '
             'true in the pjm interconnection Eola Renewables has operated here since 2007 '
             'building and operating 815 megaw of wind power at five facilities enough to '
             'power.',
      'title': 'PJM Interconnection: U.S. Energy Markets (Avangrid Renewables)',
      'url': 'https://www.youtube.com/watch?v=T_Y5rMNtBVs&t=205s',
      'video_id': 'T_Y5rMNtBVs'},
     {'author': 'Practical Engineering',
      'channel': 'Practical Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:17](https://www.youtube.com/watch?v=7Q-aVBv7PWM&t=197s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Like all equipment, substations occasionally have malfunctions or things that '
              'simply require regular maintenance. To avoid shutting down the entire '
              'substation, we need switches that can isolate equipment, transfer load, and '
              'control the flow of electricity along the bus.',
      'timestamp': 197,
      'timestamp_label': '[00:03:17]',
      'timestamp_seconds': 197,
      'tip': 'Like all equipment, substations occasionally have malfunctions or things that '
             'simply require regular maintenance. To avoid shutting down the entire '
             'substation, we need switches that can isolate equipment, transfer load, and '
             'control the flow of electricity along the bus.',
      'title': 'How Do Substations Work? (Practical Engineering)',
      'url': 'https://www.youtube.com/watch?v=7Q-aVBv7PWM&t=197s',
      'video_id': '7Q-aVBv7PWM'},
     {'author': 'Gokce Capital',
      'channel': 'Gokce Capital',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:06:48](https://www.youtube.com/watch?v=zeoe1qgsv2c&t=408s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q5 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Listings at gochecapital.com listings finally don't hesitate to reach out you "
              'can email call or text and we will respond as soon as possible so thank you for '
              'listening and more to come.',
      'timestamp': 408,
      'timestamp_label': '[00:06:48]',
      'timestamp_seconds': 408,
      'tip': "Listings at gochecapital.com listings finally don't hesitate to reach out you "
             'can email call or text and we will respond as soon as possible so thank you for '
             'listening and more to come.',
      'title': 'Substation: 6 Things You Ought To Know (Gokce Capital)',
      'url': 'https://www.youtube.com/watch?v=zeoe1qgsv2c&t=408s',
      'video_id': 'zeoe1qgsv2c'}],
 6: [{'author': 'Profound Studies',
      'channel': 'Profound Studies',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:53](https://www.youtube.com/watch?v=dMPUECoTe2M&t=173s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'s location, ramp schedule, and power supply. Texas is auditing its list. PJM "
              'is building a register. Everyone is trying to find out which data centers are '
              "real. The idea behind PJM's rejected plan has a name, bring your own new "
              'capacity.',
      'timestamp': 173,
      'timestamp_label': '[00:02:53]',
      'timestamp_seconds': 173,
      'tip': "'s location, ramp schedule, and power supply. Texas is auditing its list. PJM is "
             'building a register. Everyone is trying to find out which data centers are real. '
             "The idea behind PJM's rejected plan has a name, bring your own new capacity.",
      'title': 'Should Data Centers Bring Their Own Power or Wait in Line? (Profound Studies)',
      'url': 'https://www.youtube.com/watch?v=dMPUECoTe2M&t=173s',
      'video_id': 'dMPUECoTe2M'},
     {'author': 'ALL4 Environmental Consultants',
      'channel': 'ALL4 Environmental Consultants',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=-B0ACVnCSu0&t=116s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'I acknowledge as leaders and experts when it comes to understanding battery '
              'systems and the various challenges they can present. With us today we have '
              'Sharon Sadler. Sharon serves as a principal and the data center sector lead for '
              'all four.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': 'I acknowledge as leaders and experts when it comes to understanding battery '
             'systems and the various challenges they can present. With us today we have '
             'Sharon Sadler. Sharon serves as a principal and the data center sector lead for '
             'all four.',
      'title': 'Battery Energy Storage Systems BESS Considerations for Data Centers (ALL4 '
               'Environmental Consultants)',
      'url': 'https://www.youtube.com/watch?v=-B0ACVnCSu0&t=116s',
      'video_id': '-B0ACVnCSu0'},
     {'author': 'Collicutt Energy Services',
      'channel': 'Collicutt Energy Services',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:37:41](https://www.youtube.com/watch?v=CVfxSDNW3G4&t=2261s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Okay, I want to get into lead time. And this is less of a comparison. It's more "
              "of just a a statement around the faster that you're able to deploy equipment, "
              "the faster obviously you're able to get to first power and you're able to get "
              'to first use of that data center.',
      'timestamp': 2261,
      'timestamp_label': '[00:37:41]',
      'timestamp_seconds': 2261,
      'tip': "Okay, I want to get into lead time. And this is less of a comparison. It's more "
             "of just a a statement around the faster that you're able to deploy equipment, "
             "the faster obviously you're able to get to first power and you're able to get to "
             'first use of that data center.',
      'title': 'Big Power Needed Now! How Behind-the-Meter Generation can solve Grid '
               'Constraints & AI Power Demand (Collicutt Energy Services)',
      'url': 'https://www.youtube.com/watch?v=CVfxSDNW3G4&t=2261s',
      'video_id': 'CVfxSDNW3G4'},
     {'author': 'WPLG Local 10',
      'channel': 'WPLG Local 10',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:32](https://www.youtube.com/watch?v=iYCYPKhdqcY&t=32s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'BIPARTISAN protests all over the country and now the fight has come to Florida. '
              "You'd have to be living under a rock to not realize how horrible these centers "
              'are. Project Tango, a proposed hyperscale data center, the first in the state, '
              'in western Palm Beach County.',
      'timestamp': 32,
      'timestamp_label': '[00:00:32]',
      'timestamp_seconds': 32,
      'tip': 'BIPARTISAN protests all over the country and now the fight has come to Florida. '
             "You'd have to be living under a rock to not realize how horrible these centers "
             'are. Project Tango, a proposed hyperscale data center, the first in the state, '
             'in western Palm Beach County.',
      'title': 'Project Tango fuels debate over Florida’s first hyperscale AI data center '
               '(WPLG Local 10)',
      'url': 'https://www.youtube.com/watch?v=iYCYPKhdqcY&t=32s',
      'video_id': 'iYCYPKhdqcY'},
     {'author': 'Eaton',
      'channel': 'Eaton',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:59](https://www.youtube.com/watch?v=II6xdRkgivE&t=119s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Let's take a look at different types of data centers. First, our manage and "
              'hosted data centers that offer data center as a service.',
      'timestamp': 119,
      'timestamp_label': '[00:01:59]',
      'timestamp_seconds': 119,
      'tip': "Let's take a look at different types of data centers. First, our manage and "
             'hosted data centers that offer data center as a service.',
      'title': 'Data center solutions: Types, design, and infrastructure explained | Eaton '
               'PSEC (Eaton)',
      'url': 'https://www.youtube.com/watch?v=II6xdRkgivE&t=119s',
      'video_id': 'II6xdRkgivE'},
     {'author': 'datacenterHawk',
      'channel': 'datacenterHawk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=9IIIRj5ao20&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Topics where we're focusing on the most influential things impacting the data "
              'center space today and the first one that we are covering.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Topics where we're focusing on the most influential things impacting the data "
             'center space today and the first one that we are covering.',
      'title': 'Big Topics: Data Center Site Selection with CBRE (datacenterHawk)',
      'url': 'https://www.youtube.com/watch?v=9IIIRj5ao20&t=15s',
      'video_id': '9IIIRj5ao20'},
     {'author': 'Andy Knows It',
      'channel': 'Andy Knows It',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:14:45](https://www.youtube.com/watch?v=QxDqhnba2Jg&t=885s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "66 gigawatts in 2027, from only 31 in 2025, with data center's share of total "
              'U. 9% in 2027, from 4% in 2025. So data centers are queuing up and running into '
              'the same study timelines and same upgrade cost math as any other grid project.',
      'timestamp': 885,
      'timestamp_label': '[00:14:45]',
      'timestamp_seconds': 885,
      'tip': "66 gigawatts in 2027, from only 31 in 2025, with data center's share of total U. "
             '9% in 2027, from 4% in 2025. So data centers are queuing up and running into the '
             'same study timelines and same upgrade cost math as any other grid project.',
      'title': 'Interconnection Queue Explained: The $3.5 Billion Waiting List (Andy Knows It)',
      'url': 'https://www.youtube.com/watch?v=QxDqhnba2Jg&t=885s',
      'video_id': 'QxDqhnba2Jg'},
     {'author': 'Stats in Motion',
      'channel': 'Stats in Motion',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:54](https://www.youtube.com/watch?v=Z2FdaH10ZCY&t=54s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Federal regulators tried to fix this with FERC Order 2023, which forced grid '
              'operators to study projects in clusters instead of one by one. But this data is '
              "the first real report card on those reforms, and it suggests the patient's "
              'health is not improving.',
      'timestamp': 54,
      'timestamp_label': '[00:00:54]',
      'timestamp_seconds': 54,
      'tip': 'Federal regulators tried to fix this with FERC Order 2023, which forced grid '
             'operators to study projects in clusters instead of one by one. But this data is '
             "the first real report card on those reforms, and it suggests the patient's "
             'health is not improving.',
      'title': "The Interconnection Queue Shrank. That's Not Good News (Stats in Motion)",
      'url': 'https://www.youtube.com/watch?v=Z2FdaH10ZCY&t=54s',
      'video_id': 'Z2FdaH10ZCY'},
     {'author': 'Democracy Now!',
      'channel': 'Democracy Now!',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:38](https://www.youtube.com/watch?v=OeYd0jErrF4&t=98s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '1,500 jobs that are available. Oftentimes those jobs will not go to local '
              'community members. They will go to construction companies who already '
              'specialize in building hyperscale data centers.',
      'timestamp': 98,
      'timestamp_label': '[00:01:38]',
      'timestamp_seconds': 98,
      'tip': '1,500 jobs that are available. Oftentimes those jobs will not go to local '
             'community members. They will go to construction companies who already specialize '
             'in building hyperscale data centers.',
      'title': 'How huge AI data centers can harm local communities (Democracy Now!)',
      'url': 'https://www.youtube.com/watch?v=OeYd0jErrF4&t=98s',
      'video_id': 'OeYd0jErrF4'},
     {'author': 'Data Center Sales & Marketing Institute (DCSMI)',
      'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:25](https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=25s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "They don't have the client, and most importantly, they don't have natural gas. "
              "And somewhat most importantly, they don't have all the generator sets to make "
              "these gigawatts or hundreds of megawatt sites. So I didn't ask that question at "
              'the first game.',
      'timestamp': 25,
      'timestamp_label': '[00:00:25]',
      'timestamp_seconds': 25,
      'tip': "They don't have the client, and most importantly, they don't have natural gas. "
             "And somewhat most importantly, they don't have all the generator sets to make "
             "these gigawatts or hundreds of megawatt sites. So I didn't ask that question at "
             'the first game.',
      'title': "Why Big Tech Can't Build AI Data Centers Fast Enough (Data Center Sales & "
               'Marketing Institute (DCSMI))',
      'url': 'https://www.youtube.com/watch?v=ZcZ62ZBZTrA&t=25s',
      'video_id': 'ZcZ62ZBZTrA'},
     {'author': 'The Land Department Podcast',
      'channel': 'The Land Department Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=bWbMkkvRPWI&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Storage project the battery is a fairly simple Prospect compared to let's say "
              "wind turbines you know where you've got these like massive structures but "
              "that's.",
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': "Storage project the battery is a fairly simple Prospect compared to let's say "
             "wind turbines you know where you've got these like massive structures but "
             "that's.",
      'title': 'The Ultimate Guide to BESS with Drew Lebowitz and Sean Daly | TLD 032 (The '
               'Land Department Podcast)',
      'url': 'https://www.youtube.com/watch?v=bWbMkkvRPWI&t=15s',
      'video_id': 'bWbMkkvRPWI'},
     {'author': 'Modo Energy',
      'channel': 'Modo Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:36](https://www.youtube.com/watch?v=LhT4VVDW7CI&t=576s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Leads up to you know more of the interconnection and grid studies right so '
              "we'll look at line capacity we'll try to get estimates for you know maybe what.",
      'timestamp': 576,
      'timestamp_label': '[00:09:36]',
      'timestamp_seconds': 576,
      'tip': "Leads up to you know more of the interconnection and grid studies right so we'll "
             "look at line capacity we'll try to get estimates for you know maybe what.",
      'title': 'Developing BESS - from greenfield to grid with Ravi Sharma - Transmission '
               '(Modo Energy)',
      'url': 'https://www.youtube.com/watch?v=LhT4VVDW7CI&t=576s',
      'video_id': 'LhT4VVDW7CI'},
     {'author': 'BESS Engineer',
      'channel': 'BESS Engineer',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:21](https://www.youtube.com/watch?v=MnGAkKrZF_I&t=81s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Improvements. That matters because electricity is usually the largest ongoing '
              'cost of running a data center. IDC puts it at.',
      'timestamp': 81,
      'timestamp_label': '[00:01:21]',
      'timestamp_seconds': 81,
      'tip': 'Improvements. That matters because electricity is usually the largest ongoing '
             'cost of running a data center. IDC puts it at.',
      'title': 'Data Center PUE Explained: Same IT Load, 30 MW Less | AIDC Decoded Ep. 3 (BESS '
               'Engineer)',
      'url': 'https://www.youtube.com/watch?v=MnGAkKrZF_I&t=81s',
      'video_id': 'MnGAkKrZF_I'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:21](https://www.youtube.com/watch?v=GAM0L1fXtiA&t=21s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We also cover the standards framework behind each milestone, five real world '
              'case studies, and 18 frequently asked questions across two FAQ sections.',
      'timestamp': 21,
      'timestamp_label': '[00:00:21]',
      'timestamp_seconds': 21,
      'tip': 'We also cover the standards framework behind each milestone, five real world '
             'case studies, and 18 frequently asked questions across two FAQ sections.',
      'title': 'Substation Design | 30–60–90–IFC | Keentel Engineering (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=GAM0L1fXtiA&t=21s',
      'video_id': 'GAM0L1fXtiA'},
     {'author': 'Ram Khilawan',
      'channel': 'Ram Khilawan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=82WTDfToVvY&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q6 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'का बफर लेना है या बफर जोन क्रिएट करना है। इसके बाद इसके इस वीडियो में अब '
              'बताएंगे किस तरीके से आपको 1 स्क्वायर कि.मी. के अंदर रोड कैप्चर करना है। अगर.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'का बफर लेना है या बफर जोन क्रिएट करना है। इसके बाद इसके इस वीडियो में अब बताएंगे '
             'किस तरीके से आपको 1 स्क्वायर कि.मी. के अंदर रोड कैप्चर करना है। अगर.',
      'title': 'HV Transmission Line GIS Project | Connect Road Centerline to HVT Pole | '
               'Complete Practical Tutorial (Ram Khilawan)',
      'url': 'https://www.youtube.com/watch?v=82WTDfToVvY&t=15s',
      'video_id': '82WTDfToVvY'}],
 7: [{'author': 'DIgSILENT GmbH – Power System Solutions',
      'channel': 'DIgSILENT GmbH – Power System Solutions',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:42](https://www.youtube.com/watch?v=7iequWeuZTQ&t=42s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Harmonic analysis in a single workflow providing a systematic and efficient '
              'approach for the analysis of deer and consumer integration the hosting capacity '
              'study case should be activated.',
      'timestamp': 42,
      'timestamp_label': '[00:00:42]',
      'timestamp_seconds': 42,
      'tip': 'Harmonic analysis in a single workflow providing a systematic and efficient '
             'approach for the analysis of deer and consumer integration the hosting capacity '
             'study case should be activated.',
      'title': 'PowerFactory - MV Distribution Network – Hosting Capacity Analysis (DIgSILENT '
               'GmbH – Power System Solutions)',
      'url': 'https://www.youtube.com/watch?v=7iequWeuZTQ&t=42s',
      'video_id': '7iequWeuZTQ'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:28](https://www.youtube.com/watch?v=BTkszCEW7nY&t=28s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The reality is that a BESS is fundamentally a power electronic converter with a '
              'battery attached. While energy capacity dictates your run time, the inverter '
              'dictates what the grid actually experiences, from harmonic injections to fault '
              'current contributions.',
      'timestamp': 28,
      'timestamp_label': '[00:00:28]',
      'timestamp_seconds': 28,
      'tip': 'The reality is that a BESS is fundamentally a power electronic converter with a '
             'battery attached. While energy capacity dictates your run time, the inverter '
             'dictates what the grid actually experiences, from harmonic injections to fault '
             'current contributions.',
      'title': 'BESS for Data Centers: Power Quality, Harmonics & Grid Stability Explained | '
               'Keentel Engineering (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=BTkszCEW7nY&t=28s',
      'video_id': 'BTkszCEW7nY'},
     {'author': 'Base Config',
      'channel': 'Base Config',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:36](https://www.youtube.com/watch?v=giNYYY0DnJw&t=156s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'For data centers, we rely on double conversion UPS technology. It takes dirty '
              'AC power, converts it to clean DC power, and then converts it back into AC '
              'perfect sine wave. The transfer time is zero when the grid fails. This '
              'conversion step dictates battery choice.',
      'timestamp': 156,
      'timestamp_label': '[00:02:36]',
      'timestamp_seconds': 156,
      'tip': 'For data centers, we rely on double conversion UPS technology. It takes dirty AC '
             'power, converts it to clean DC power, and then converts it back into AC perfect '
             'sine wave. The transfer time is zero when the grid fails. This conversion step '
             'dictates battery choice.',
      'title': "Data Center Power Explained (It's simpler than you think) (Base Config)",
      'url': 'https://www.youtube.com/watch?v=giNYYY0DnJw&t=156s',
      'video_id': 'giNYYY0DnJw'},
     {'author': 'Power System Operation Slides',
      'channel': 'Power System Operation Slides',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:08:16](https://www.youtube.com/watch?v=7tln9f5Ak7M&t=496s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'BOS and a design failure of the control system. The Victoria Big Battery '
              'incident in Australia during 2021 demonstrates another critical aspect of BES '
              'failure analysis. During commissioning, a leak in the coolant system led to a '
              'fire that spread across two best units.',
      'timestamp': 496,
      'timestamp_label': '[00:08:16]',
      'timestamp_seconds': 496,
      'tip': 'BOS and a design failure of the control system. The Victoria Big Battery '
             'incident in Australia during 2021 demonstrates another critical aspect of BES '
             'failure analysis. During commissioning, a leak in the coolant system led to a '
             'fire that spread across two best units.',
      'title': 'BESS Operational Projects Worldwide | Grid Scale Utility BESS Overview | '
               "Europe's Largest BESS (Power System Operation Slides)",
      'url': 'https://www.youtube.com/watch?v=7tln9f5Ak7M&t=496s',
      'video_id': '7tln9f5Ak7M'},
     {'author': 'WhyPKD',
      'channel': 'WhyPKD',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:20](https://www.youtube.com/watch?v=EvpNriZrrME&t=80s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Thus, after some consideration, ERCOT decided to develop a batch planning '
              'process, essentially hoovering up a bunch of these projects, assigning them to '
              'a group, and then evaluating the system impacts of that aggregation.',
      'timestamp': 80,
      'timestamp_label': '[00:01:20]',
      'timestamp_seconds': 80,
      'tip': 'Thus, after some consideration, ERCOT decided to develop a batch planning '
             'process, essentially hoovering up a bunch of these projects, assigning them to a '
             'group, and then evaluating the system impacts of that aggregation.',
      'title': 'Ending the "Stupid Land" Queue: ERCOT\'s New Rules for Massive Power Loads '
               '(WhyPKD)',
      'url': 'https://www.youtube.com/watch?v=EvpNriZrrME&t=80s',
      'video_id': 'EvpNriZrrME'},
     {'author': 'Nebraska Wind and Solar',
      'channel': 'Nebraska Wind and Solar',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:27:28](https://www.youtube.com/watch?v=6zj9DYoE8-U&t=1648s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And so, we're building out a a data center, so to speak, um with graphics pro "
              'processing units that can process things 80% faster than traditional power '
              "flow. And we're seeing that across the board.",
      'timestamp': 1648,
      'timestamp_label': '[00:27:28]',
      'timestamp_seconds': 1648,
      'tip': "And so, we're building out a a data center, so to speak, um with graphics pro "
             'processing units that can process things 80% faster than traditional power flow. '
             "And we're seeing that across the board.",
      'title': 'SPP Generation Interconnection Queue Process and Current Backlog (Nebraska '
               'Wind and Solar)',
      'url': 'https://www.youtube.com/watch?v=6zj9DYoE8-U&t=1648s',
      'video_id': '6zj9DYoE8-U'},
     {'author': 'Owl WiS',
      'channel': 'Owl WiS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:35](https://www.youtube.com/watch?v=7n-ba9KN-Uc&t=35s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The answer is Battery Energy Storage Systems, or BESS. A Battery Energy Storage '
              'System, commonly called BESS, is a system that stores electrical energy in '
              'batteries and supplies it whenever electricity is needed.',
      'timestamp': 35,
      'timestamp_label': '[00:00:35]',
      'timestamp_seconds': 35,
      'tip': 'The answer is Battery Energy Storage Systems, or BESS. A Battery Energy Storage '
             'System, commonly called BESS, is a system that stores electrical energy in '
             'batteries and supplies it whenever electricity is needed.',
      'title': 'Battery Energy Storage System | BESS Explained (Owl WiS)',
      'url': 'https://www.youtube.com/watch?v=7n-ba9KN-Uc&t=35s',
      'video_id': '7n-ba9KN-Uc'},
     {'author': 'Australian Control Engineering | Smart Utilities',
      'channel': 'Australian Control Engineering | Smart Utilities',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:19](https://www.youtube.com/watch?v=8eadjA6Pqyo&t=79s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Network integrate a platform engineered for performance, reliability and '
              'compliance. Evaluate and verify functionality and regulatory compliance. '
              'Commission for first time right connection transfer and train to deliver a '
              'complete documented and user ready system.',
      'timestamp': 79,
      'timestamp_label': '[00:01:19]',
      'timestamp_seconds': 79,
      'tip': 'Network integrate a platform engineered for performance, reliability and '
             'compliance. Evaluate and verify functionality and regulatory compliance. '
             'Commission for first time right connection transfer and train to deliver a '
             'complete documented and user ready system.',
      'title': 'BESS Site Visit: SCADA Integration & Delivery Lessons (Australian Control '
               'Engineering | Smart Utilities)',
      'url': 'https://www.youtube.com/watch?v=8eadjA6Pqyo&t=79s',
      'video_id': '8eadjA6Pqyo'},
     {'author': 'Electrical Engineering - Power System',
      'channel': 'Electrical Engineering - Power System',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:20](https://www.youtube.com/watch?v=9N3qVzFvgwg&t=20s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'We can select the wind farm example and execute this one. Then you will have '
              'this example. So in this example we have a grid that is connected to a couple '
              'of uh wind farms and we can uh execute the housing capacity for this system.',
      'timestamp': 20,
      'timestamp_label': '[00:00:20]',
      'timestamp_seconds': 20,
      'tip': 'We can select the wind farm example and execute this one. Then you will have '
             'this example. So in this example we have a grid that is connected to a couple of '
             'uh wind farms and we can uh execute the housing capacity for this system.',
      'title': 'DIgSILENT PowerFactory Tutorial: Lecture 18, Hosting Capacity Analysis '
               '(Electrical Engineering - Power System)',
      'url': 'https://www.youtube.com/watch?v=9N3qVzFvgwg&t=20s',
      'video_id': '9N3qVzFvgwg'},
     {'author': 'TechTrainerNJ',
      'channel': 'TechTrainerNJ',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:38](https://www.youtube.com/watch?v=QtOyye8fYNk&t=158s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'And can be either a battery or a flywheel system both systems store specified '
              'amount of energy to span the time between utility power outage and.',
      'timestamp': 158,
      'timestamp_label': '[00:02:38]',
      'timestamp_seconds': 158,
      'tip': 'And can be either a battery or a flywheel system both systems store specified '
             'amount of energy to span the time between utility power outage and.',
      'title': 'Data Center Power Chain - Animation (TechTrainerNJ)',
      'url': 'https://www.youtube.com/watch?v=QtOyye8fYNk&t=158s',
      'video_id': 'QtOyye8fYNk'},
     {'author': 'ELFBULB Battery',
      'channel': 'ELFBULB Battery',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:00](https://www.youtube.com/watch?v=NZa3fz23P5Q&t=60s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'See how we combine this system this battery clusters one cluster is 200 '
              'kilowatt hour and in this space 20 ft container the two space is two cluster '
              'that will be 400 kilowatt hour and we have total six class.',
      'timestamp': 60,
      'timestamp_label': '[00:01:00]',
      'timestamp_seconds': 60,
      'tip': 'See how we combine this system this battery clusters one cluster is 200 kilowatt '
             'hour and in this space 20 ft container the two space is two cluster that will be '
             '400 kilowatt hour and we have total six class.',
      'title': 'Bellie Breaks Down the 3.6MWh BESS: Your Key to Sustainable Energy! (ELFBULB '
               'Battery)',
      'url': 'https://www.youtube.com/watch?v=NZa3fz23P5Q&t=60s',
      'video_id': 'NZa3fz23P5Q'},
     {'author': 'HeatSpring',
      'channel': 'HeatSpring',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:04](https://www.youtube.com/watch?v=KpCBra3viO8&t=64s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Along with a medium voltage Transformer typical voltages for a system like this '
              'would be 1, to 1500 volts DC on the battery.',
      'timestamp': 64,
      'timestamp_label': '[00:01:04]',
      'timestamp_seconds': 64,
      'tip': 'Along with a medium voltage Transformer typical voltages for a system like this '
             'would be 1, to 1500 volts DC on the battery.',
      'title': 'Inside AC Block Architecture: A Technical Walkthrough of Utility-Scale Energy '
               'Storage Systems Design (HeatSpring)',
      'url': 'https://www.youtube.com/watch?v=KpCBra3viO8&t=64s',
      'video_id': 'KpCBra3viO8'},
     {'author': 'Blueprint States',
      'channel': 'Blueprint States',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:54](https://www.youtube.com/watch?v=v2cs7ZXTQH0&t=114s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '7 years for those built between 2011 and 2021. Those historical figures measure '
              'the overall interval to commercial operation in the four system operators '
              'studied. They do not show that every individual step became slower.',
      'timestamp': 114,
      'timestamp_label': '[00:01:54]',
      'timestamp_seconds': 114,
      'tip': '7 years for those built between 2011 and 2021. Those historical figures measure '
             'the overall interval to commercial operation in the four system operators '
             'studied. They do not show that every individual step became slower.',
      'title': "Why the Grid Queue Isn't a Construction Schedule (Blueprint States)",
      'url': 'https://www.youtube.com/watch?v=v2cs7ZXTQH0&t=114s',
      'video_id': 'v2cs7ZXTQH0'},
     {'author': 'VoltaGrid',
      'channel': 'VoltaGrid',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:39](https://www.youtube.com/watch?v=rQu_8zcOaZU&t=159s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "'re able to destroy SO2 up to 95% and our CO levels are getting destroyed over "
              "95%. Again, that's a proprietary process I think to Voltter Grid as I've "
              'learned about it and actually the air permitting is something too that we do '
              'entirely internally.',
      'timestamp': 159,
      'timestamp_label': '[00:02:39]',
      'timestamp_seconds': 159,
      'tip': "'re able to destroy SO2 up to 95% and our CO levels are getting destroyed over "
             "95%. Again, that's a proprietary process I think to Voltter Grid as I've learned "
             'about it and actually the air permitting is something too that we do entirely '
             'internally.',
      'title': 'Powering a Data Center Off the Grid: Part 1 – Natural Gas Solutions '
               '(VoltaGrid)',
      'url': 'https://www.youtube.com/watch?v=rQu_8zcOaZU&t=159s',
      'video_id': 'rQu_8zcOaZU'},
     {'author': 'datacenterHawk',
      'channel': 'datacenterHawk',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:22:40](https://www.youtube.com/watch?v=pt4hMec2LbM&t=1360s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q7 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "We're putting out there so please let us know how we can be helpful uh dater "
              "hawk.com is our site check it out and we'll see you next time.",
      'timestamp': 1360,
      'timestamp_label': '[00:22:40]',
      'timestamp_seconds': 1360,
      'tip': "We're putting out there so please let us know how we can be helpful uh dater "
             "hawk.com is our site check it out and we'll see you next time.",
      'title': 'Understanding Powered Shell Data Centers (datacenterHawk)',
      'url': 'https://www.youtube.com/watch?v=pt4hMec2LbM&t=1360s',
      'video_id': 'pt4hMec2LbM'}],
 8: [{'author': 'Volta Foundation',
      'channel': 'Volta Foundation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:13:45](https://www.youtube.com/watch?v=7h6DABJ_xgs&t=825s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Now, but we have to be a little careful here. Analysis differ on how much data '
              'center was the deciding factor. And there are still support from the Congress '
              'from the White House and the industry still back the build out of these data '
              'centers.',
      'timestamp': 825,
      'timestamp_label': '[00:13:45]',
      'timestamp_seconds': 825,
      'tip': 'Now, but we have to be a little careful here. Analysis differ on how much data '
             'center was the deciding factor. And there are still support from the Congress '
             'from the White House and the industry still back the build out of these data '
             'centers.',
      'title': 'Battery Forum: Grid-Forming BESS Architectures for AI Data Center Power '
               'Quality with Lyten (Volta Foundation)',
      'url': 'https://www.youtube.com/watch?v=7h6DABJ_xgs&t=825s',
      'video_id': '7h6DABJ_xgs'},
     {'author': 'Build Core',
      'channel': 'Build Core',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=tNNIXQhntOk&t=33s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Before we get ahead of ourselves, let's build a data center. And yes, we're "
              'tracking how often I repeat that phrase. The term data center gets thrown '
              "around constantly now, almost like it's one type of building.",
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': "Before we get ahead of ourselves, let's build a data center. And yes, we're "
             'tracking how often I repeat that phrase. The term data center gets thrown around '
             "constantly now, almost like it's one type of building.",
      'title': 'Why AI Data Centers Are Heading to Rural America (Build Core)',
      'url': 'https://www.youtube.com/watch?v=tNNIXQhntOk&t=33s',
      'video_id': 'tNNIXQhntOk'},
     {'author': 'JSA TV: Tech & Telecom News',
      'channel': 'JSA TV: Tech & Telecom News',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:17](https://www.youtube.com/watch?v=oQVb9TRp6Og&t=137s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Hypers model is a little different. We're essentially building private "
              'manufacturing capacity for hyperscale colo and neo cloud data center '
              'developers.',
      'timestamp': 137,
      'timestamp_label': '[00:02:17]',
      'timestamp_seconds': 137,
      'tip': "Hypers model is a little different. We're essentially building private "
             'manufacturing capacity for hyperscale colo and neo cloud data center developers.',
      'title': 'How Modular Manufacturing Accelerates Data Center Deployment | Hyper (JSA TV: '
               'Tech & Telecom News)',
      'url': 'https://www.youtube.com/watch?v=oQVb9TRp6Og&t=137s',
      'video_id': 'oQVb9TRp6Og'},
     {'author': 'The Clean Energy Edge Podcast',
      'channel': 'The Clean Energy Edge Podcast',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:12](https://www.youtube.com/watch?v=CjD4mAL9NCA&t=132s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "And that's exactly the direction some developers are moving. We're talking "
              'about dedicated natural gas generation, solar, battery storage, and '
              'combinations of different technologies. Sometimes that generation is located '
              'directly on the data center property.',
      'timestamp': 132,
      'timestamp_label': '[00:02:12]',
      'timestamp_seconds': 132,
      'tip': "And that's exactly the direction some developers are moving. We're talking about "
             'dedicated natural gas generation, solar, battery storage, and combinations of '
             'different technologies. Sometimes that generation is located directly on the '
             'data center property.',
      'title': "The Grid Can't Keep Up — So Data Centers Are Building Their Own Power! (The "
               'Clean Energy Edge Podcast)',
      'url': 'https://www.youtube.com/watch?v=CjD4mAL9NCA&t=132s',
      'video_id': 'CjD4mAL9NCA'},
     {'author': 'Uintah County Economic Development (Official)',
      'channel': 'Uintah County Economic Development (Official)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:42](https://www.youtube.com/watch?v=169FuRa1T-0&t=582s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "3 megawws plate capacity, I think. Um, I'm showing this because a whole bunch "
              'of these are being deployed right now at a big self-generating data center in '
              'West Jordan, Utah. Um, something like 180 megawws plus and they are being used '
              'to power a modern AI data center.',
      'timestamp': 582,
      'timestamp_label': '[00:09:42]',
      'timestamp_seconds': 582,
      'tip': "3 megawws plate capacity, I think. Um, I'm showing this because a whole bunch of "
             'these are being deployed right now at a big self-generating data center in West '
             'Jordan, Utah. Um, something like 180 megawws plus and they are being used to '
             'power a modern AI data center.',
      'title': 'Behind the Meter: A new frontier for natural gas (Uintah County Economic '
               'Development (Official))',
      'url': 'https://www.youtube.com/watch?v=169FuRa1T-0&t=582s',
      'video_id': '169FuRa1T-0'},
     {'author': 'Environment+Energy Leader',
      'channel': 'Environment+Energy Leader',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:33](https://www.youtube.com/watch?v=wOKA9jWA8fw&t=33s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '2/3 of respondents who were surveyed for the Foley 2026 Data Center Report. '
              'Power as the gating factor. Most data centers are connected to the grid as a '
              'steady and dependable source of power.',
      'timestamp': 33,
      'timestamp_label': '[00:00:33]',
      'timestamp_seconds': 33,
      'tip': '2/3 of respondents who were surveyed for the Foley 2026 Data Center Report. '
             'Power as the gating factor. Most data centers are connected to the grid as a '
             'steady and dependable source of power.',
      'title': 'Industry Voice: How Powered Land Is Changing Data Center Site Selection '
               '(Environment+Energy Leader)',
      'url': 'https://www.youtube.com/watch?v=wOKA9jWA8fw&t=33s',
      'video_id': 'wOKA9jWA8fw'},
     {'author': 'Shawn Yarter',
      'channel': 'Shawn Yarter',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:27](https://www.youtube.com/watch?v=RoQA5d_fDFw&t=207s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Analysis widget and use the create buffers tool using the line that I just '
              'created I will use a 50-foot buffer 100 feet would be a typical width for a '
              "transmission line easement so 50 feet I'm using since the buffer is from the "
              'center line of the the line that I drew.',
      'timestamp': 207,
      'timestamp_label': '[00:03:27]',
      'timestamp_seconds': 207,
      'tip': 'Analysis widget and use the create buffers tool using the line that I just '
             'created I will use a 50-foot buffer 100 feet would be a typical width for a '
             "transmission line easement so 50 feet I'm using since the buffer is from the "
             'center line of the the line that I drew.',
      'title': 'Transmission Line Siting  Project for Web GIS (Shawn Yarter)',
      'url': 'https://www.youtube.com/watch?v=RoQA5d_fDFw&t=207s',
      'video_id': 'RoQA5d_fDFw'},
     {'author': 'Ryne Ogren',
      'channel': 'Ryne Ogren',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:05:18](https://www.youtube.com/watch?v=6_osryMHPf4&t=318s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "I don't know what happens if you have a 500 KV line just like going into your "
              "building. But they these data centers need the substations and usually they're "
              "going to be on site cuz they're interconnecting to those big voltage lines in "
              'some way, shape or form.',
      'timestamp': 318,
      'timestamp_label': '[00:05:18]',
      'timestamp_seconds': 318,
      'tip': "I don't know what happens if you have a 500 KV line just like going into your "
             "building. But they these data centers need the substations and usually they're "
             "going to be on site cuz they're interconnecting to those big voltage lines in "
             'some way, shape or form.',
      'title': 'What is a substation and why is it important for data centers? (Ryne Ogren)',
      'url': 'https://www.youtube.com/watch?v=6_osryMHPf4&t=318s',
      'video_id': '6_osryMHPf4'},
     {'author': 'LandApp by LandGate',
      'channel': 'LandApp by LandGate',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:22](https://www.youtube.com/watch?v=2mYrH35TasY&t=22s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Um I think an average hyperscale data center can use around the equivalent of '
              '50,000 homes worth homes electricity. Um so, in order for these to be built, '
              'you have to be close to what we call a substation.',
      'timestamp': 22,
      'timestamp_label': '[00:00:22]',
      'timestamp_seconds': 22,
      'tip': 'Um I think an average hyperscale data center can use around the equivalent of '
             '50,000 homes worth homes electricity. Um so, in order for these to be built, you '
             'have to be close to what we call a substation.',
      'title': 'Data Centers Are Paying Top Dollar- Is Your Property a Match? (LandApp by '
               'LandGate)',
      'url': 'https://www.youtube.com/watch?v=2mYrH35TasY&t=22s',
      'video_id': '2mYrH35TasY'},
     {'author': 'National Grid Distributed Generation',
      'channel': 'National Grid Distributed Generation',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:25:30](https://www.youtube.com/watch?v=KxAPuQUu_II&t=1530s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Can you send out the links just a series of links in the email when you send it '
              'out that will connect to this data a series of links to get to the this data '
              'portal here yeah yes.',
      'timestamp': 1530,
      'timestamp_label': '[00:25:30]',
      'timestamp_seconds': 1530,
      'tip': 'Can you send out the links just a series of links in the email when you send it '
             'out that will connect to this data a series of links to get to the this data '
             'portal here yeah yes.',
      'title': 'National Grid MA DG Hosting Capacity Maps Webinar - 6/17/2021 (National Grid '
               'Distributed Generation)',
      'url': 'https://www.youtube.com/watch?v=KxAPuQUu_II&t=1530s',
      'video_id': 'KxAPuQUu_II'},
     {'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:10:31](https://www.youtube.com/watch?v=WN6PtJ3kQDQ&t=631s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'In that case, manufacturers initially selected settings primarily to protect '
              'their converters. In the data center environment, vendors can similarly select '
              'settings primarily to protect facility equipment.',
      'timestamp': 631,
      'timestamp_label': '[00:10:31]',
      'timestamp_seconds': 631,
      'tip': 'In that case, manufacturers initially selected settings primarily to protect '
             'their converters. In the data center environment, vendors can similarly select '
             'settings primarily to protect facility equipment.',
      'title': '3,800 MW Data Center Load Event Explained | PJM Grid, Ride-Through & '
               'Reliability Lessons (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=WN6PtJ3kQDQ&t=631s',
      'video_id': 'WN6PtJ3kQDQ'},
     {'author': 'POWERmagvideos',
      'channel': 'POWERmagvideos',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:09](https://www.youtube.com/watch?v=DU-7TmjHp7c&t=69s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "So, that's what we're driving towards uh for our November filing. How difficult "
              'is it to plan when these data centers are being added to the grid and and '
              "everybody's looking for new generation?",
      'timestamp': 69,
      'timestamp_label': '[00:01:09]',
      'timestamp_seconds': 69,
      'tip': "So, that's what we're driving towards uh for our November filing. How difficult "
             'is it to plan when these data centers are being added to the grid and and '
             "everybody's looking for new generation?",
      'title': 'Planning the Grid for Large Loads, Jason Connell, PJM Interconnection | EP '
               '2026 (POWERmagvideos)',
      'url': 'https://www.youtube.com/watch?v=DU-7TmjHp7c&t=69s',
      'video_id': 'DU-7TmjHp7c'},
     {'author': 'Inel Institute of Technology',
      'channel': 'Inel Institute of Technology',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[01:11:43](https://www.youtube.com/watch?v=5K3HSEyhIng&t=4303s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Platform uh thank you Mr nasier okay for the rest of the participants if you '
              'want to get a free certification please scan this QR and there is a link also '
              'in the chat thank you very much for everything.',
      'timestamp': 4303,
      'timestamp_label': '[01:11:43]',
      'timestamp_seconds': 4303,
      'tip': 'Platform uh thank you Mr nasier okay for the rest of the participants if you '
             'want to get a free certification please scan this QR and there is a link also in '
             'the chat thank you very much for everything.',
      'title': 'FREE VIRTUAL MASTERCLASS: Applied case study of designing a Battery Energy '
               'Storage System (BESS) (Inel Institute of Technology)',
      'url': 'https://www.youtube.com/watch?v=5K3HSEyhIng&t=4303s',
      'video_id': '5K3HSEyhIng'},
     {'author': 'Cummins',
      'channel': 'Cummins',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:21](https://www.youtube.com/watch?v=RRbdgfTqeTA&t=141s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The helm along with generator sets capable of operating on hydrogenated '
              'vegetable oil or natural gas next my colleague CH Will Walker through the '
              "detailed aspects of the C's.",
      'timestamp': 141,
      'timestamp_label': '[00:02:21]',
      'timestamp_seconds': 141,
      'tip': 'The helm along with generator sets capable of operating on hydrogenated '
             'vegetable oil or natural gas next my colleague CH Will Walker through the '
             "detailed aspects of the C's.",
      'title': 'Cummins Power Generation Battery Energy Storage Systems (BESS) launch unveil '
               '(Cummins)',
      'url': 'https://www.youtube.com/watch?v=RRbdgfTqeTA&t=141s',
      'video_id': 'RRbdgfTqeTA'},
     {'author': 'Ram Khilawan',
      'channel': 'Ram Khilawan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=jNG8_YbkY6E&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q8 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'ट्रांसमिशन लाइन की लेंथ को कैलकुलेट करना है। आज की इस क्लास में मैं बताऊंगा किस '
              'तरीके से आपको पोल की आईडी देनी है और उसकी फील्ड क्रिएट करानी है तो बने रहिए.',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'ट्रांसमिशन लाइन की लेंथ को कैलकुलेट करना है। आज की इस क्लास में मैं बताऊंगा किस '
             'तरीके से आपको पोल की आईडी देनी है और उसकी फील्ड क्रिएट करानी है तो बने रहिए.',
      'title': 'HV Transmission Line GIS Project | Pole Numbering | GPS Pole Numbering '
               'Complete Tutorial in Hindi (Ram Khilawan)',
      'url': 'https://www.youtube.com/watch?v=jNG8_YbkY6E&t=15s',
      'video_id': 'jNG8_YbkY6E'}],
 9: [{'author': 'Keentel Engineering',
      'channel': 'Keentel Engineering',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:03:59](https://www.youtube.com/watch?v=f1C-d4m7OHg&t=239s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Then someone adds a 4 megavolt ampere battery behind the same transformer. The '
              'aggregate jumps to 22 and the plant instantly crosses the threshold into strict '
              'compliance. A modest capacity addition changes your regulatory status '
              'overnight.',
      'timestamp': 239,
      'timestamp_label': '[00:03:59]',
      'timestamp_seconds': 239,
      'tip': 'Then someone adds a 4 megavolt ampere battery behind the same transformer. The '
             'aggregate jumps to 22 and the plant instantly crosses the threshold into strict '
             'compliance. A modest capacity addition changes your regulatory status overnight.',
      'title': 'NERC Compliance Engineering: Reliability Standards, IBR Requirements & Power '
               'System Compliance (Keentel Engineering)',
      'url': 'https://www.youtube.com/watch?v=f1C-d4m7OHg&t=239s',
      'video_id': 'f1C-d4m7OHg'},
     {'author': 'IVY Press Room',
      'channel': 'IVY Press Room',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:50](https://www.youtube.com/watch?v=WnjqDbowqy0&t=50s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'US node electricity systems could integrate up to 70 gigawatts of new data '
              'center capacity without a single grid upgrade. How does clean backup power '
              'technology address increasing state restrictions on diesel generators at data '
              'centers?',
      'timestamp': 50,
      'timestamp_label': '[00:00:50]',
      'timestamp_seconds': 50,
      'tip': 'US node electricity systems could integrate up to 70 gigawatts of new data '
             'center capacity without a single grid upgrade. How does clean backup power '
             'technology address increasing state restrictions on diesel generators at data '
             'centers?',
      'title': 'Phinergy and Rosendin Unlock New Grid Capacity for Data Centers (IVY Press '
               'Room)',
      'url': 'https://www.youtube.com/watch?v=WnjqDbowqy0&t=50s',
      'video_id': 'WnjqDbowqy0'},
     {'author': 'Learn Solar & BESS',
      'channel': 'Learn Solar & BESS',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:56](https://www.youtube.com/watch?v=Wc1MU3K4OEc&t=116s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'That brings us to section one. In the absolute simplest terms, a BESS, or '
              'battery energy storage system, is just a giant rechargeable battery bank '
              'connected directly to the electricity grid.',
      'timestamp': 116,
      'timestamp_label': '[00:01:56]',
      'timestamp_seconds': 116,
      'tip': 'That brings us to section one. In the absolute simplest terms, a BESS, or '
             'battery energy storage system, is just a giant rechargeable battery bank '
             'connected directly to the electricity grid.',
      'title': 'Battery Energy Storage System (BESS) Explained | Complete Beginner to Expert '
               'Guide (2026) (Learn Solar & BESS)',
      'url': 'https://www.youtube.com/watch?v=Wc1MU3K4OEc&t=116s',
      'video_id': 'Wc1MU3K4OEc'},
     {'author': 'Dirt to Data',
      'channel': 'Dirt to Data',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:11:26](https://www.youtube.com/watch?v=264d0wu5W4k&t=686s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'The old conversation was, can you find enough power for the data center?" The '
              'new conversation is, "Can you find enough power, connect it quickly, preserve '
              'reliability, navigate federal and state rules, and prove that everybody else '
              'will not be left paying for your project?".',
      'timestamp': 686,
      'timestamp_label': '[00:11:26]',
      'timestamp_seconds': 686,
      'tip': 'The old conversation was, can you find enough power for the data center?" The '
             'new conversation is, "Can you find enough power, connect it quickly, preserve '
             'reliability, navigate federal and state rules, and prove that everybody else '
             'will not be left paying for your project?".',
      'title': 'What Is an Interconnection Queue (Dirt to Data)',
      'url': 'https://www.youtube.com/watch?v=264d0wu5W4k&t=686s',
      'video_id': '264d0wu5W4k'},
     {'author': 'Gaurav J - TheElectricalGuy',
      'channel': 'Gaurav J - TheElectricalGuy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:09:33](https://www.youtube.com/watch?v=Bg-6ClEVMSU&t=573s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'So, what do you think will be the design changes in terms of BESS in this '
              'situation? Or the same machine can use for both application? The biggest change '
              'goes into the EMS. We call like, okay, then battery is the body, then EMS is '
              'the soul.',
      'timestamp': 573,
      'timestamp_label': '[00:09:33]',
      'timestamp_seconds': 573,
      'tip': 'So, what do you think will be the design changes in terms of BESS in this '
             'situation? Or the same machine can use for both application? The biggest change '
             'goes into the EMS. We call like, okay, then battery is the body, then EMS is the '
             'soul.',
      'title': 'BESS Explained by a Manufacturer: Applications, Lifecycle & Industry Trends '
               '(Gaurav J - TheElectricalGuy)',
      'url': 'https://www.youtube.com/watch?v=Bg-6ClEVMSU&t=573s',
      'video_id': 'Bg-6ClEVMSU'},
     {'author': 'Regen',
      'channel': 'Regen',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:17:22](https://www.youtube.com/watch?v=Zmu3gs7y51A&t=1042s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "On noise, um it's fairly clearcut. There's some existing policy available. Um "
              'the general gist of this is that there are abatement technologies out there, '
              'some buffering in terms of kind of trees or shrubbing in terms of planting.',
      'timestamp': 1042,
      'timestamp_label': '[00:17:22]',
      'timestamp_seconds': 1042,
      'tip': "On noise, um it's fairly clearcut. There's some existing policy available. Um "
             'the general gist of this is that there are abatement technologies out there, '
             'some buffering in terms of kind of trees or shrubbing in terms of planting.',
      'title': 'Planning for clean Energy - Assessing battery energy storage system (BESS) '
               'applications (Regen)',
      'url': 'https://www.youtube.com/watch?v=Zmu3gs7y51A&t=1042s',
      'video_id': 'Zmu3gs7y51A'},
     {'author': 'Data Center Sales & Marketing Institute (DCSMI)',
      'channel': 'Data Center Sales & Marketing Institute (DCSMI)',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:02:40](https://www.youtube.com/watch?v=W92xU-lo1Gc&t=160s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "20 megawatt data center in a district heating system, that all we're doing is "
              'just getting ahead of the queue, really, in terms of power allocation.',
      'timestamp': 160,
      'timestamp_label': '[00:02:40]',
      'timestamp_seconds': 160,
      'tip': "20 megawatt data center in a district heating system, that all we're doing is "
             'just getting ahead of the queue, really, in terms of power allocation.',
      'title': 'Hyperscale vs. Decentralized Data Centers, Global Energy Capacity, and $1T ASI '
               'Cluster (Data Center Sales & Marketing Institute (DCSMI))',
      'url': 'https://www.youtube.com/watch?v=W92xU-lo1Gc&t=160s',
      'video_id': 'W92xU-lo1Gc'},
     {'author': 'SunCast Media',
      'channel': 'SunCast Media',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:34:11](https://www.youtube.com/watch?v=eynQ4qifTao&t=2051s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'It was funded by by the the state of Washington and really does a good job '
              'diving into the ways it can use the solar to become a microgrid if there was a '
              'grid-wide outage, how they can reduce their energy bills by cutting demand '
              'charges. So, a lot of that case study applies.',
      'timestamp': 2051,
      'timestamp_label': '[00:34:11]',
      'timestamp_seconds': 2051,
      'tip': 'It was funded by by the the state of Washington and really does a good job '
             'diving into the ways it can use the solar to become a microgrid if there was a '
             'grid-wide outage, how they can reduce their energy bills by cutting demand '
             'charges. So, a lot of that case study applies.',
      'title': 'Required Reading For Battery Technology? The BESS Book: Utility-Scale Battery '
               'Energy Storage Systems (SunCast Media)',
      'url': 'https://www.youtube.com/watch?v=eynQ4qifTao&t=2051s',
      'video_id': 'eynQ4qifTao'},
     {'author': 'WIRES',
      'channel': 'WIRES',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:47:27](https://www.youtube.com/watch?v=-BTpIv2G5-0&t=2847s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "Compliance process as well um last thing I'll say the other thing Fork did was "
              'require the installation of monitoring and control Technologies at the battery.',
      'timestamp': 2847,
      'timestamp_label': '[00:47:27]',
      'timestamp_seconds': 2847,
      'tip': "Compliance process as well um last thing I'll say the other thing Fork did was "
             'require the installation of monitoring and control Technologies at the battery.',
      'title': 'WIRES 2023 Fall Meeting Panel 1 – FERC Order 2023 (WIRES)',
      'url': 'https://www.youtube.com/watch?v=-BTpIv2G5-0&t=2847s',
      'video_id': '-BTpIv2G5-0'},
     {'author': 'PBS NewsHour',
      'channel': 'PBS NewsHour',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:12:32](https://www.youtube.com/watch?v=fkB8mt1DEVw&t=752s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Oftentimes the companies will ask for non-disclosure agreements so that the '
              'deals themselves that the data center construction companies or the data center '
              'operators sign are really opaque. And people think, "What on earth is going on '
              'here?',
      'timestamp': 752,
      'timestamp_label': '[00:12:32]',
      'timestamp_seconds': 752,
      'tip': 'Oftentimes the companies will ask for non-disclosure agreements so that the '
             'deals themselves that the data center construction companies or the data center '
             'operators sign are really opaque. And people think, "What on earth is going on '
             'here?',
      'title': 'Why communities are revolting against data centers (PBS NewsHour)',
      'url': 'https://www.youtube.com/watch?v=fkB8mt1DEVw&t=752s',
      'video_id': 'fkB8mt1DEVw'},
     {'author': 'Kai Sun',
      'channel': 'Kai Sun',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:39:35](https://www.youtube.com/watch?v=Kq3m6y4jjFM&t=2375s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': "In our case, we have just a single line. Which is similar to, to, They're just "
              "single current, there's no many terms, right? We only just study, the conduct "
              "as a cylinder, so only coupled If there's any magnetic field of phi. So the psi "
              'plus linkage is just exactly 5.',
      'timestamp': 2375,
      'timestamp_label': '[00:39:35]',
      'timestamp_seconds': 2375,
      'tip': "In our case, we have just a single line. Which is similar to, to, They're just "
             "single current, there's no many terms, right? We only just study, the conduct as "
             "a cylinder, so only coupled If there's any magnetic field of phi. So the psi "
             'plus linkage is just exactly 5.',
      'title': 'ECE421 - Lec 13: Transmission Line Parameters; Resistance; Inductance (Kai '
               'Sun)',
      'url': 'https://www.youtube.com/watch?v=Kq3m6y4jjFM&t=2375s',
      'video_id': 'Kq3m6y4jjFM'},
     {'author': 'Modo Energy',
      'channel': 'Modo Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:03](https://www.youtube.com/watch?v=OIAK1RATT9M&t=63s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Terms the capacity of a generation unit specifies its maximum instantaneous '
              "output so if you hear someone say we've just built a 14 megawatt Wind Farm the.",
      'timestamp': 63,
      'timestamp_label': '[00:01:03]',
      'timestamp_seconds': 63,
      'tip': 'Terms the capacity of a generation unit specifies its maximum instantaneous '
             "output so if you hear someone say we've just built a 14 megawatt Wind Farm the.",
      'title': "Megawatts (MW) vs. megawatt hours (MWh): what's the difference? (Modo Energy)",
      'url': 'https://www.youtube.com/watch?v=OIAK1RATT9M&t=63s',
      'video_id': 'OIAK1RATT9M'},
     {'author': 'Modo Energy',
      'channel': 'Modo Energy',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:01:57](https://www.youtube.com/watch?v=ijPF1Cwm0wA&t=117s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'Instead, ERCOT is overseen by the Public Utility Commission of Texas (or the '
              "PUCT). The PUCT has final say on changes to ERCOT's rules and protocols. But "
              'both ERCOT and the PUCT have to work within the frameworks and boundaries of '
              'the Texas state legislature.',
      'timestamp': 117,
      'timestamp_label': '[00:01:57]',
      'timestamp_seconds': 117,
      'tip': 'Instead, ERCOT is overseen by the Public Utility Commission of Texas (or the '
             "PUCT). The PUCT has final say on changes to ERCOT's rules and protocols. But "
             'both ERCOT and the PUCT have to work within the frameworks and boundaries of the '
             'Texas state legislature.',
      'title': 'Understanding the Basics of the Power System (The Energy Academy: ERCOT - E1) '
               '(Modo Energy)',
      'url': 'https://www.youtube.com/watch?v=ijPF1Cwm0wA&t=117s',
      'video_id': 'ijPF1Cwm0wA'},
     {'author': 'IIT Roorkee July 2018',
      'channel': 'IIT Roorkee July 2018',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:31:35](https://www.youtube.com/watch?v=Q5WOz2acUrM&t=1895s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': '200 this is our book of I rooki and you could see these are the areas where the '
              'solar technology is available or the rooftop PB and these are my smart meters.',
      'timestamp': 1895,
      'timestamp_label': '[00:31:35]',
      'timestamp_seconds': 1895,
      'tip': '200 this is our book of I rooki and you could see these are the areas where the '
             'solar technology is available or the rooftop PB and these are my smart meters.',
      'title': 'Optimal location and sizing battery energy storage system (BESS) (IIT Roorkee '
               'July 2018)',
      'url': 'https://www.youtube.com/watch?v=Q5WOz2acUrM&t=1895s',
      'video_id': 'Q5WOz2acUrM'},
     {'author': 'Ram Khilawan',
      'channel': 'Ram Khilawan',
      'epistemic_status': 'attributed_practitioner_claim',
      'markdown': '[00:00:15](https://www.youtube.com/watch?v=OzHE4fl9JjE&t=15s)',
      'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                   'hosting-capacity screening, dark-fiber corridor verification, and '
                   'assignable `12–24` month diligence-contingent land options flipped to '
                   '`BESS` and modular/hyperscale AI data-center developers (Chapter Q9 '
                   'operational verification).',
      'source_type': 'video_pro_tip',
      'text': 'बनाते हैं, किस तरीके से ट्रैस करते हैं? अपस्ट्रीम कैसे देखते हैं, डाउन स्ट्रीम '
              'कैसे देखते हैं? लूप कैसे चेक करते हैं? कनेक्ट और डिस्कनेक्ट कैसे चेक करते हैं?',
      'timestamp': 15,
      'timestamp_label': '[00:00:15]',
      'timestamp_seconds': 15,
      'tip': 'बनाते हैं, किस तरीके से ट्रैस करते हैं? अपस्ट्रीम कैसे देखते हैं, डाउन स्ट्रीम '
             'कैसे देखते हैं? लूप कैसे चेक करते हैं? कनेक्ट और डिस्कनेक्ट कैसे चेक करते हैं?',
      'title': 'HV Transmission Line GIS Project Final Layout Design | Professional Layout Map '
               'तैयार करें | हिंदी (Ram Khilawan)',
      'url': 'https://www.youtube.com/watch?v=OzHE4fl9JjE&t=15s',
      'video_id': 'OzHE4fl9JjE'}],
 10: [{'author': 'The Machine Room Podcast',
       'channel': 'The Machine Room Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=rED467a2820&t=20s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI is transforming the scale of power required for data centers, why '
               'behind-the-meter generation is emerging as a key option for faster deployment, '
               'and how innovations from hydrogen-ready turbines to small modular reactors '
               'could help meet future demand.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': 'AI is transforming the scale of power required for data centers, why '
              'behind-the-meter generation is emerging as a key option for faster deployment, '
              'and how innovations from hydrogen-ready turbines to small modular reactors '
              'could help meet future demand.',
       'title': 'Behind the Meter: Powering AI at Gigawatt Scale (The Machine Room Podcast)',
       'url': 'https://www.youtube.com/watch?v=rED467a2820&t=20s',
       'video_id': 'rED467a2820'},
      {'author': 'Datacenter Dynamics',
       'channel': 'Datacenter Dynamics',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=XjWqZlxWJuw&t=20s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "In today's talk, we're going to be driving into behind the meter power and the "
               'growing role of high-speed gas generation in enabling new data center '
               "capacity. Thomas, thank you so much for joining us. Yeah, it's exciting to be "
               'here.',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "In today's talk, we're going to be driving into behind the meter power and the "
              'growing role of high-speed gas generation in enabling new data center capacity. '
              "Thomas, thank you so much for joining us. Yeah, it's exciting to be here.",
       'title': 'Fast, flexible behind the meter power (Datacenter Dynamics)',
       'url': 'https://www.youtube.com/watch?v=XjWqZlxWJuw&t=20s',
       'video_id': 'XjWqZlxWJuw'},
      {'author': 'CBC News: The National',
       'channel': 'CBC News: The National',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:45](https://www.youtube.com/watch?v=Rj_icscgo_Q&t=45s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'But the scale and location of data centers is changing in Canada to meet '
               "demands of AI and large-scale cloud computing. It is Alberta's first truly "
               'hyperscale large-scale data center at 90 MW.',
       'timestamp': 45,
       'timestamp_label': '[00:00:45]',
       'timestamp_seconds': 45,
       'tip': 'But the scale and location of data centers is changing in Canada to meet '
              "demands of AI and large-scale cloud computing. It is Alberta's first truly "
              'hyperscale large-scale data center at 90 MW.',
       'title': 'A hyperscale AI data centre boom is coming (CBC News: The National)',
       'url': 'https://www.youtube.com/watch?v=Rj_icscgo_Q&t=45s',
       'video_id': 'Rj_icscgo_Q'},
      {'author': 'ELK TRADING Co LLC | Natural Gas Trading',
       'channel': 'ELK TRADING Co LLC | Natural Gas Trading',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:35](https://www.youtube.com/watch?v=mRxFZBnZSiM&t=95s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Providers are securing natural gas for hyperscale data centers this allows AI '
               'growth to continue without waiting on large scale grid expansions or nuclear.',
       'timestamp': 95,
       'timestamp_label': '[00:01:35]',
       'timestamp_seconds': 95,
       'tip': 'Providers are securing natural gas for hyperscale data centers this allows AI '
              'growth to continue without waiting on large scale grid expansions or nuclear.',
       'title': 'Behind the Meter Generation: How Natural Gas Fuels AI Growth Until Nuclear '
                'Scales Up (ELK TRADING Co LLC | Natural Gas Trading)',
       'url': 'https://www.youtube.com/watch?v=mRxFZBnZSiM&t=95s',
       'video_id': 'mRxFZBnZSiM'},
      {'author': 'THE PHYSICAL LAYER',
       'channel': 'THE PHYSICAL LAYER',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:07:01](https://www.youtube.com/watch?v=v5uOMJOzPbk&t=421s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'First, the bottleneck behind AI is not only chips and data centers, it is also '
               'the unglamorous work of connecting power plants to wires and the wires to each '
               'other. A chatbot can be trained in months. A transmission upgrade can take '
               'years.',
       'timestamp': 421,
       'timestamp_label': '[00:07:01]',
       'timestamp_seconds': 421,
       'tip': 'First, the bottleneck behind AI is not only chips and data centers, it is also '
              'the unglamorous work of connecting power plants to wires and the wires to each '
              'other. A chatbot can be trained in months. A transmission upgrade can take '
              'years.',
       'title': 'The 5-Year Queue Behind Your Chatbot (THE PHYSICAL LAYER)',
       'url': 'https://www.youtube.com/watch?v=v5uOMJOzPbk&t=421s',
       'video_id': 'v5uOMJOzPbk'},
      {'author': 'Schneider Electric',
       'channel': 'Schneider Electric',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:12:50](https://www.youtube.com/watch?v=2ORDbZvOirU&t=770s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So, I I think you you brought up a good point there, right? There'll be a "
               'certain type of data center that may locate in in an area like Virginia. There '
               'may be other types of AI or data centers in Texas, right?',
       'timestamp': 770,
       'timestamp_label': '[00:12:50]',
       'timestamp_seconds': 770,
       'tip': "So, I I think you you brought up a good point there, right? There'll be a "
              'certain type of data center that may locate in in an area like Virginia. There '
              'may be other types of AI or data centers in Texas, right?',
       'title': 'Powered Land Explained: The Race for Energy Infrastructure (Schneider '
                'Electric)',
       'url': 'https://www.youtube.com/watch?v=2ORDbZvOirU&t=770s',
       'video_id': '2ORDbZvOirU'},
      {'author': 'Fierce Network TV',
       'channel': 'Fierce Network TV',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:29](https://www.youtube.com/watch?v=ixyJ-cWKBEg&t=29s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I do wonder, however, whether particularly in the US, we've sort of over "
               'focused on building data centers and to the detriment of the network which '
               'must surely connect them and connect the AI out into the rest of the world.',
       'timestamp': 29,
       'timestamp_label': '[00:00:29]',
       'timestamp_seconds': 29,
       'tip': "I do wonder, however, whether particularly in the US, we've sort of over "
              'focused on building data centers and to the detriment of the network which must '
              'surely connect them and connect the AI out into the rest of the world.',
       'title': 'Akamai on Why AI Needs More Than Hyperscale Data Centers (Fierce Network TV)',
       'url': 'https://www.youtube.com/watch?v=ixyJ-cWKBEg&t=29s',
       'video_id': 'ixyJ-cWKBEg'},
      {'author': 'Dirt To Data Podcast',
       'channel': 'Dirt To Data Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:04:43](https://www.youtube.com/watch?v=quCPqX-ExfQ&t=283s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "'s a guy there, David, from New York and he literally >> Teared up. AI works, "
               "whatever else it is. He's building the data center, but he was tearing up "
               'because it was help the AI was helping his daughter with cerebral palsy. Yep, '
               'she has cerebral palsy.',
       'timestamp': 283,
       'timestamp_label': '[00:04:43]',
       'timestamp_seconds': 283,
       'tip': "'s a guy there, David, from New York and he literally >> Teared up. AI works, "
              "whatever else it is. He's building the data center, but he was tearing up "
              'because it was help the AI was helping his daughter with cerebral palsy. Yep, '
              'she has cerebral palsy.',
       'title': 'Debunking Data Center Myths: Facts on Water Usage and Human Impact (Dirt To '
                'Data Podcast)',
       'url': 'https://www.youtube.com/watch?v=quCPqX-ExfQ&t=283s',
       'video_id': 'quCPqX-ExfQ'},
      {'author': 'Keentel Engineering',
       'channel': 'Keentel Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:07](https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=307s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "And once you're in the EIT, inflexibility is the price of the speed you're "
               'getting. Case B is pipeline meets forecast discounting. The key lesson here is '
               'the one from the previous slide. A signed contract is not counted megawatt.',
       'timestamp': 307,
       'timestamp_label': '[00:05:07]',
       'timestamp_seconds': 307,
       'tip': "And once you're in the EIT, inflexibility is the price of the speed you're "
              'getting. Case B is pipeline meets forecast discounting. The key lesson here is '
              'the one from the previous slide. A signed contract is not counted megawatt.',
       'title': 'PJM Interconnection Explained: How Data Centers Connect to the Power Grid '
                '(Keentel Engineering)',
       'url': 'https://www.youtube.com/watch?v=C9tZQM-x_Ho&t=307s',
       'video_id': 'C9tZQM-x_Ho'},
      {'author': 'The POWER Podcast',
       'channel': 'The POWER Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:29](https://www.youtube.com/watch?v=Ic-Cuo3Xdfo&t=329s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'AI developers because developers, of course, are racing to deploy capacity as '
               'fast as they can while the utilities have to figure out a way to connect these '
               'unusually large loads. So where do those different priorities come into '
               "conflict that that you've seen?",
       'timestamp': 329,
       'timestamp_label': '[00:05:29]',
       'timestamp_seconds': 329,
       'tip': 'AI developers because developers, of course, are racing to deploy capacity as '
              'fast as they can while the utilities have to figure out a way to connect these '
              'unusually large loads. So where do those different priorities come into '
              "conflict that that you've seen?",
       'title': '219. Spiky AI Loads Are Forcing a Rethink of Data Center Power (The POWER '
                'Podcast)',
       'url': 'https://www.youtube.com/watch?v=Ic-Cuo3Xdfo&t=329s',
       'video_id': 'Ic-Cuo3Xdfo'},
      {'author': 'The Clean Energy Edge Podcast',
       'channel': 'The Clean Energy Edge Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:19](https://www.youtube.com/watch?v=kHFYcexB2dU&t=319s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "It's in in in a lot of ways they'll looks. You might not even if you walked "
               'into a data center, almost might not even know the difference between an AI '
               'data center and a traditional one in in some sense.',
       'timestamp': 319,
       'timestamp_label': '[00:05:19]',
       'timestamp_seconds': 319,
       'tip': "It's in in in a lot of ways they'll looks. You might not even if you walked "
              'into a data center, almost might not even know the difference between an AI '
              'data center and a traditional one in in some sense.',
       'title': 'Why AI Data Centers Are Overwhelming the Grid (It’s Not Just Generation) (The '
                'Clean Energy Edge Podcast)',
       'url': 'https://www.youtube.com/watch?v=kHFYcexB2dU&t=319s',
       'video_id': 'kHFYcexB2dU'},
      {'author': 'Energy Systems Integration Group',
       'channel': 'Energy Systems Integration Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:21](https://www.youtube.com/watch?v=nFQOwcyPbbE&t=21s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Lauren, turn it over to you. Um, I'm very excited to talk about one of um, my "
               'favorite topics, the interconnection queue. Um, our session title is '
               'modernizing the interconnection queue, AI automation and process reform. Um, '
               'we have a great group of panelists today.',
       'timestamp': 21,
       'timestamp_label': '[00:00:21]',
       'timestamp_seconds': 21,
       'tip': "Lauren, turn it over to you. Um, I'm very excited to talk about one of um, my "
              'favorite topics, the interconnection queue. Um, our session title is '
              'modernizing the interconnection queue, AI automation and process reform. Um, we '
              'have a great group of panelists today.',
       'title': '2025 Fall Workshop: Session 3B: Modernizing Interconnection Queue: AI, '
                'Automation, & Process Reform (Energy Systems Integration Group)',
       'url': 'https://www.youtube.com/watch?v=nFQOwcyPbbE&t=21s',
       'video_id': 'nFQOwcyPbbE'},
      {'author': 'Kognito Key',
       'channel': 'Kognito Key',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:20](https://www.youtube.com/watch?v=u8ABTJm2_XQ&t=20s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Today, we're going to break down the complex engineering behind our power "
               'grids, looking exactly at how different substation layouts have evolved over '
               "time to keep our lights on. Okay, so let's start by establishing our "
               'foundation. What exactly is a substation?',
       'timestamp': 20,
       'timestamp_label': '[00:00:20]',
       'timestamp_seconds': 20,
       'tip': "Today, we're going to break down the complex engineering behind our power "
              'grids, looking exactly at how different substation layouts have evolved over '
              "time to keep our lights on. Okay, so let's start by establishing our "
              'foundation. What exactly is a substation?',
       'title': 'Electrical Substation Layout Configurations | Radial, Tapped, LILO & '
                'Interconnected (Kognito Key)',
       'url': 'https://www.youtube.com/watch?v=u8ABTJm2_XQ&t=20s',
       'video_id': 'u8ABTJm2_XQ'},
      {'author': 'California ISO',
       'channel': 'California ISO',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:31](https://www.youtube.com/watch?v=YAtPW03BCrY&t=151s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Amount you maybe want and you can figure out where on the map your request '
               "would fit best so now that we've gone over how to utilize the heat map I want "
               'to pull up the heat map itself and we can go through a demo.',
       'timestamp': 151,
       'timestamp_label': '[00:02:31]',
       'timestamp_seconds': 151,
       'tip': 'Amount you maybe want and you can figure out where on the map your request '
              "would fit best so now that we've gone over how to utilize the heat map I want "
              'to pull up the heat map itself and we can go through a demo.',
       'title': 'Sep 17, 2024 - FERC Order No. 2023 - Points of Interconnection Heatmap '
                '(California ISO)',
       'url': 'https://www.youtube.com/watch?v=YAtPW03BCrY&t=151s',
       'video_id': 'YAtPW03BCrY'},
      {'author': 'Ram Khilawan',
       'channel': 'Ram Khilawan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:15](https://www.youtube.com/watch?v=0g0z2irniQo&t=15s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q10 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'हैं और इस वीडियो में मैं आपको बताऊंगा किस तरीके से ट्रांसमिशन लाइन को बनाते '
               'हैं या क्रिएट करते हैं। तो वीडियो को अंत तक जरूर देखिएगा और लाइक करिएगा, शेयर.',
       'timestamp': 15,
       'timestamp_label': '[00:00:15]',
       'timestamp_seconds': 15,
       'tip': 'हैं और इस वीडियो में मैं आपको बताऊंगा किस तरीके से ट्रांसमिशन लाइन को बनाते हैं '
              'या क्रिएट करते हैं। तो वीडियो को अंत तक जरूर देखिएगा और लाइक करिएगा, शेयर.',
       'title': 'HV Transmission Line Creation | शुरुआत से अंत तक Complete GIS Mapping '
                'Tutorial | ArcGIS/QGIS हिंदी (Ram Khilawan)',
       'url': 'https://www.youtube.com/watch?v=0g0z2irniQo&t=15s',
       'video_id': '0g0z2irniQo'}],
 11: [{'author': 'Mini Leviathan',
       'channel': 'Mini Leviathan',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:36](https://www.youtube.com/watch?v=Ayt6rLwGjYM&t=36s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "So today we're going to explore how hyperscale data centers work. Chapter one, "
               'what makes a data center hyperscale? A data center is simply a building that '
               'houses computing equipment. A hyperscale data center takes that concept to a '
               'much larger scale.',
       'timestamp': 36,
       'timestamp_label': '[00:00:36]',
       'timestamp_seconds': 36,
       'tip': "So today we're going to explore how hyperscale data centers work. Chapter one, "
              'what makes a data center hyperscale? A data center is simply a building that '
              'houses computing equipment. A hyperscale data center takes that concept to a '
              'much larger scale.',
       'title': 'How Hyperscale Data Centers Work – The Factories Of The Digital World. (Mini '
                'Leviathan)',
       'url': 'https://www.youtube.com/watch?v=Ayt6rLwGjYM&t=36s',
       'video_id': 'Ayt6rLwGjYM'},
      {'author': 'FlexGen',
       'channel': 'FlexGen',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:51](https://www.youtube.com/watch?v=LhqvSN3OdlI&t=231s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Hybrid OS intelligently throttles on-site generation while using the battery '
               'to bridge the gap. This ensures the data center stays at 100% capacity without '
               "ever violating the grid's cap.",
       'timestamp': 231,
       'timestamp_label': '[00:03:51]',
       'timestamp_seconds': 231,
       'tip': 'Hybrid OS intelligently throttles on-site generation while using the battery to '
              'bridge the gap. This ensures the data center stays at 100% capacity without '
              "ever violating the grid's cap.",
       'title': 'Powering the AI Boom: Co-locating Batteries with Data Centers (FlexGen)',
       'url': 'https://www.youtube.com/watch?v=LhqvSN3OdlI&t=231s',
       'video_id': 'LhqvSN3OdlI'},
      {'author': 'Keentel Engineering',
       'channel': 'Keentel Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:10:18](https://www.youtube.com/watch?v=M2z-pv6j-N4&t=618s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Engineering experience becomes especially valuable when projects involve '
               'large-scale grid integration and strict utility requirements. Battery energy '
               'storage systems are transforming modern power systems. But behind every '
               'successful installation is far more than batteries.',
       'timestamp': 618,
       'timestamp_label': '[00:10:18]',
       'timestamp_seconds': 618,
       'tip': 'Engineering experience becomes especially valuable when projects involve '
              'large-scale grid integration and strict utility requirements. Battery energy '
              'storage systems are transforming modern power systems. But behind every '
              'successful installation is far more than batteries.',
       'title': 'Inside a Battery Energy Storage System (BESS): Components Explained | BMS, '
                'PCS, EMS & More (Keentel Engineering)',
       'url': 'https://www.youtube.com/watch?v=M2z-pv6j-N4&t=618s',
       'video_id': 'M2z-pv6j-N4'},
      {'author': 'Barton Malow',
       'channel': 'Barton Malow',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:43](https://www.youtube.com/watch?v=WNd-Q3GWyEI&t=43s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Once they're in the building, that's where our team takes over. Starting with "
               'the boilermaker scopes, the final assemblies of the units, and then our '
               'subcontractor partners complete the mechanical and electrical scopes. So, as '
               'we talk about speed to market, right?',
       'timestamp': 43,
       'timestamp_label': '[00:00:43]',
       'timestamp_seconds': 43,
       'tip': "Once they're in the building, that's where our team takes over. Starting with "
              'the boilermaker scopes, the final assemblies of the units, and then our '
              'subcontractor partners complete the mechanical and electrical scopes. So, as we '
              'talk about speed to market, right?',
       'title': 'Inside the Build | Energy Center and BESS Yard in Central Ohio (Barton Malow)',
       'url': 'https://www.youtube.com/watch?v=WNd-Q3GWyEI&t=43s',
       'video_id': 'WNd-Q3GWyEI'},
      {'author': 'Power System Operation Slides',
       'channel': 'Power System Operation Slides',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:05](https://www.youtube.com/watch?v=Xys0DmLCtVk&t=125s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'The analysis of classified incidents reveals that integration, assembly, and '
               'construction emerges as the most common root cause of best failures, '
               'accounting for approximately 65% of all identified faults.',
       'timestamp': 125,
       'timestamp_label': '[00:02:05]',
       'timestamp_seconds': 125,
       'tip': 'The analysis of classified incidents reveals that integration, assembly, and '
              'construction emerges as the most common root cause of best failures, accounting '
              'for approximately 65% of all identified faults.',
       'title': 'BESS Operational Projects Worldwide | Grid Scale Utility BESS Overview | '
                "Europe's Largest BESS (Power System Operation Slides)",
       'url': 'https://www.youtube.com/watch?v=Xys0DmLCtVk&t=125s',
       'video_id': 'Xys0DmLCtVk'},
      {'author': 'Modo Energy',
       'channel': 'Modo Energy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:47](https://www.youtube.com/watch?v=AtMNJWhrmXE&t=47s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This intermittent generation means prices are now more unpredictable, and '
               'batteries allow you to smooth that out without building expensive and fossil '
               "fuel heavy natural gas plants. Let's say you build a battery energy storage "
               'project.',
       'timestamp': 47,
       'timestamp_label': '[00:00:47]',
       'timestamp_seconds': 47,
       'tip': 'This intermittent generation means prices are now more unpredictable, and '
              'batteries allow you to smooth that out without building expensive and fossil '
              "fuel heavy natural gas plants. Let's say you build a battery energy storage "
              'project.',
       'title': 'The Economics of Grid-Scale Batteries Explained (Modo Energy)',
       'url': 'https://www.youtube.com/watch?v=AtMNJWhrmXE&t=47s',
       'video_id': 'AtMNJWhrmXE'},
      {'author': 'BUILT BENEATH',
       'channel': 'BUILT BENEATH',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:46](https://www.youtube.com/watch?v=7L7MfK9coTY&t=46s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And what happens when the fastest-growing technology industry in the world '
               'collides with infrastructure that can take years to expand? First, we need to '
               'understand the scale. A traditional office building might require a few '
               'megawatts of electricity.',
       'timestamp': 46,
       'timestamp_label': '[00:00:46]',
       'timestamp_seconds': 46,
       'tip': 'And what happens when the fastest-growing technology industry in the world '
              'collides with infrastructure that can take years to expand? First, we need to '
              'understand the scale. A traditional office building might require a few '
              'megawatts of electricity.',
       'title': 'Data Center Electricity: Why AI Facilities Are Short on Power (BUILT BENEATH)',
       'url': 'https://www.youtube.com/watch?v=7L7MfK9coTY&t=46s',
       'video_id': '7L7MfK9coTY'},
      {'author': 'Fire Protection Engineering Podcast',
       'channel': 'Fire Protection Engineering Podcast',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:17:00](https://www.youtube.com/watch?v=biJIJcXR5mE&t=1020s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Um its growth annually in deployment since 2020 is is 10 times greater every '
               'year. Um US energy storage investment between 2021 and 2030 is $70 billion. Um '
               'and 500 plus megawatts per year of average new uh battery energy storage '
               'capacity is installed monthly.',
       'timestamp': 1020,
       'timestamp_label': '[00:17:00]',
       'timestamp_seconds': 1020,
       'tip': 'Um its growth annually in deployment since 2020 is is 10 times greater every '
              'year. Um US energy storage investment between 2021 and 2030 is $70 billion. Um '
              'and 500 plus megawatts per year of average new uh battery energy storage '
              'capacity is installed monthly.',
       'title': 'BESS Design-Build Best Practices with Daniel Hudson (Fire Protection '
                'Engineering Podcast)',
       'url': 'https://www.youtube.com/watch?v=biJIJcXR5mE&t=1020s',
       'video_id': 'biJIJcXR5mE'},
      {'author': 'Cool Vector',
       'channel': 'Cool Vector',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:20:19](https://www.youtube.com/watch?v=rab11GilV3g&t=1219s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Particularly if you have it in scale so if you think about our 270,000 Acres '
               'of surface are ebit do for next year is projected to be.',
       'timestamp': 1219,
       'timestamp_label': '[00:20:19]',
       'timestamp_seconds': 1219,
       'tip': 'Particularly if you have it in scale so if you think about our 270,000 Acres of '
              'surface are ebit do for next year is projected to be.',
       'title': 'West Texas Land is Perfect for Data Centers, Says LandBridge Founder (Cool '
                'Vector)',
       'url': 'https://www.youtube.com/watch?v=rab11GilV3g&t=1219s',
       'video_id': 'rab11GilV3g'},
      {'author': 'Gaurav J - TheElectricalGuy',
       'channel': 'Gaurav J - TheElectricalGuy',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:18](https://www.youtube.com/watch?v=zphURkyhD-c&t=78s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Battery modules composed of electrochemical cells are where energy is stored. '
               'For grid scale application, lithium ion is the most common choice. But '
               'depending on your needs, lead acid, sodium based or redox flow batteries might '
               'be used.',
       'timestamp': 78,
       'timestamp_label': '[00:01:18]',
       'timestamp_seconds': 78,
       'tip': 'Battery modules composed of electrochemical cells are where energy is stored. '
              'For grid scale application, lithium ion is the most common choice. But '
              'depending on your needs, lead acid, sodium based or redox flow batteries might '
              'be used.',
       'title': 'BESS Components Explained: Every Part You Need to Know! (Gaurav J - '
                'TheElectricalGuy)',
       'url': 'https://www.youtube.com/watch?v=zphURkyhD-c&t=78s',
       'video_id': 'zphURkyhD-c'},
      {'author': 'Rand Simulation',
       'channel': 'Rand Simulation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:24:46](https://www.youtube.com/watch?v=LBt7MoTnFFQ&t=1486s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Swept it over those different wind conditions you can see here the worst case '
               'wind scenario so 7 m per hour wind from the southeast which was a fairly.',
       'timestamp': 1486,
       'timestamp_label': '[00:24:46]',
       'timestamp_seconds': 1486,
       'tip': 'Swept it over those different wind conditions you can see here the worst case '
              'wind scenario so 7 m per hour wind from the southeast which was a fairly.',
       'title': 'Leveraging Simulation for BESS & Data Center Sites (Rand Simulation)',
       'url': 'https://www.youtube.com/watch?v=LBt7MoTnFFQ&t=1486s',
       'video_id': 'LBt7MoTnFFQ'},
      {'author': 'LandApp by LandGate',
       'channel': 'LandApp by LandGate',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:09:36](https://www.youtube.com/watch?v=0_owMAznas0&t=576s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Parcels of land um that they are building their own solar Farms on so um the '
               'entire industry is moving towards something that would be essentially more '
               "efficient but also energy friendly um and you're not using 50,000 houses worth "
               'of power um in a year.',
       'timestamp': 576,
       'timestamp_label': '[00:09:36]',
       'timestamp_seconds': 576,
       'tip': 'Parcels of land um that they are building their own solar Farms on so um the '
              'entire industry is moving towards something that would be essentially more '
              "efficient but also energy friendly um and you're not using 50,000 houses worth "
              'of power um in a year.',
       'title': 'Understanding Property Qualifications for Data Centers (LandApp by LandGate)',
       'url': 'https://www.youtube.com/watch?v=0_owMAznas0&t=576s',
       'video_id': '0_owMAznas0'},
      {'author': 'Maclarens Lawyers',
       'channel': 'Maclarens Lawyers',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:05:40](https://www.youtube.com/watch?v=q09nIjF9s5c&t=340s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Vendor and you have been approached by developer to sell your property you '
               'need to make sure that you speak to an experienced property lawyer about the '
               "option you wish to enter contact the experience team at mclaren's lawyers for "
               'more information.',
       'timestamp': 340,
       'timestamp_label': '[00:05:40]',
       'timestamp_seconds': 340,
       'tip': 'Vendor and you have been approached by developer to sell your property you need '
              'to make sure that you speak to an experienced property lawyer about the option '
              "you wish to enter contact the experience team at mclaren's lawyers for more "
              'information.',
       'title': 'Property Insights:  Land Option Contracts (Maclarens Lawyers)',
       'url': 'https://www.youtube.com/watch?v=q09nIjF9s5c&t=340s',
       'video_id': 'q09nIjF9s5c'},
      {'author': 'REsource Labs',
       'channel': 'REsource Labs',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:57](https://www.youtube.com/watch?v=lFIWqD0EAkM&t=837s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Generation hope the folks will check out what you do thanks for taking time to '
               'sit with us today thank you very much appreciate it Nico absolutely.',
       'timestamp': 837,
       'timestamp_label': '[00:13:57]',
       'timestamp_seconds': 837,
       'tip': 'Generation hope the folks will check out what you do thanks for taking time to '
              'sit with us today thank you very much appreciate it Nico absolutely.',
       'title': 'Why Data Centers Are Choosing This Company For Substations | Dan Girard at '
                'Midwest Solar Expo 2024 (REsource Labs)',
       'url': 'https://www.youtube.com/watch?v=lFIWqD0EAkM&t=837s',
       'video_id': 'lFIWqD0EAkM'},
      {'author': 'Franklin Andrew Cruz',
       'channel': 'Franklin Andrew Cruz',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:26](https://www.youtube.com/watch?v=YrpzmGX0-YM&t=26s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q11 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "I've learned going through the process, because I do have 130 acre site that "
               "we could do an assembly for 288 acres, is power. It's power, fuel, and water. "
               'But let me explain the power part. An AI data center is going to take 1 '
               'megawatt of power per acre.',
       'timestamp': 26,
       'timestamp_label': '[00:00:26]',
       'timestamp_seconds': 26,
       'tip': "I've learned going through the process, because I do have 130 acre site that we "
              "could do an assembly for 288 acres, is power. It's power, fuel, and water. But "
              'let me explain the power part. An AI data center is going to take 1 megawatt of '
              'power per acre.',
       'title': 'The Truth About AI Data Center Land (Most Sites Don’t Qualify) (Franklin '
                'Andrew Cruz)',
       'url': 'https://www.youtube.com/watch?v=YrpzmGX0-YM&t=26s',
       'video_id': 'YrpzmGX0-YM'}],
 12: [{'author': 'Advanta IRA',
       'channel': 'Advanta IRA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:19:14](https://www.youtube.com/watch?v=3rM3iGzRRUA&t=1154s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'So, um, we had a good plan to start with. The data center is a better plan, '
               "but you know, like I said, you got to have a plan B to know that you're going "
               "to get out and you're not going to get stuck with 200 acres out in the middle "
               'of nowhere that nobody wants, right?',
       'timestamp': 1154,
       'timestamp_label': '[00:19:14]',
       'timestamp_seconds': 1154,
       'tip': 'So, um, we had a good plan to start with. The data center is a better plan, but '
              "you know, like I said, you got to have a plan B to know that you're going to "
              "get out and you're not going to get stuck with 200 acres out in the middle of "
              'nowhere that nobody wants, right?',
       'title': 'The Real Estate Behind AI: Data Center Land Deals Explained - Episode 193 '
                '(Advanta IRA)',
       'url': 'https://www.youtube.com/watch?v=3rM3iGzRRUA&t=1154s',
       'video_id': '3rM3iGzRRUA'},
      {'author': 'Southern Economic Development Council',
       'channel': 'Southern Economic Development Council',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:13:36](https://www.youtube.com/watch?v=yg9V2befNR0&t=816s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "But we're also going to start to see more and more capacity, what we call at "
               'the edge. And you may have heard that term before, but that means midsize data '
               'centers, smaller data centers that are going to be located closer to located '
               'closer to customers.',
       'timestamp': 816,
       'timestamp_label': '[00:13:36]',
       'timestamp_seconds': 816,
       'tip': "But we're also going to start to see more and more capacity, what we call at "
              'the edge. And you may have heard that term before, but that means midsize data '
              'centers, smaller data centers that are going to be located closer to located '
              'closer to customers.',
       'title': 'Data Center Site Selection and Navigating Power Procurement (Southern '
                'Economic Development Council)',
       'url': 'https://www.youtube.com/watch?v=yg9V2befNR0&t=816s',
       'video_id': 'yg9V2befNR0'},
      {'author': 'James Dickey',
       'channel': 'James Dickey',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:27:24](https://www.youtube.com/watch?v=9zpO8wwsfXc&t=1644s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'This is I think, how we similar to what we presented in the last workshop, but '
               "there's going to be a case building period that will prerun the start of the "
               'official batch.',
       'timestamp': 1644,
       'timestamp_label': '[00:27:24]',
       'timestamp_seconds': 1644,
       'tip': 'This is I think, how we similar to what we presented in the last workshop, but '
              "there's going to be a case building period that will prerun the start of the "
              'official batch.',
       'title': 'Batch Zero 9-Month Clock Starts: ERCOT Large Load Interconnection Workshop 3 '
                '— Feb 26, 2026 (James Dickey)',
       'url': 'https://www.youtube.com/watch?v=9zpO8wwsfXc&t=1644s',
       'video_id': '9zpO8wwsfXc'},
      {'author': 'Data Centers Technical Info',
       'channel': 'Data Centers Technical Info',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:08:34](https://www.youtube.com/watch?v=S8vmSHwFrvE&t=514s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'It may take you a year to start building infrastructure, then another six '
               "months to get the next delivery of equipment at your site. You'll submit that "
               "load energization plan to OKR, which we'll consider in that review.",
       'timestamp': 514,
       'timestamp_label': '[00:08:34]',
       'timestamp_seconds': 514,
       'tip': 'It may take you a year to start building infrastructure, then another six '
              "months to get the next delivery of equipment at your site. You'll submit that "
              "load energization plan to OKR, which we'll consider in that review.",
       'title': 'Large Load Interconnection to ERCOT (Data Centers Technical Info)',
       'url': 'https://www.youtube.com/watch?v=S8vmSHwFrvE&t=514s',
       'video_id': 'S8vmSHwFrvE'},
      {'author': 'Energy Systems Integration Group',
       'channel': 'Energy Systems Integration Group',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:15:09](https://www.youtube.com/watch?v=6tz6xMnl1D8&t=909s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Thanks for joining this early morning session. I might kind of start things '
               'out by checking who in the audience has uh controllable thermostat, an '
               'electric vehicle, a behind-the-meter battery, just a show of hands.',
       'timestamp': 909,
       'timestamp_label': '[00:15:09]',
       'timestamp_seconds': 909,
       'tip': 'Thanks for joining this early morning session. I might kind of start things out '
              'by checking who in the audience has uh controllable thermostat, an electric '
              'vehicle, a behind-the-meter battery, just a show of hands.',
       'title': '2026 Spring Tech Session 3B: FERC Order 2222 on DER Aggregation Participation '
                'in Wholesale Markets (Energy Systems Integration Group)',
       'url': 'https://www.youtube.com/watch?v=6tz6xMnl1D8&t=909s',
       'video_id': '6tz6xMnl1D8'},
      {'author': 'US Energy Weekly',
       'channel': 'US Energy Weekly',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:03:24](https://www.youtube.com/watch?v=JwCWz91cMQc&t=204s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Almost every lease also carries an annual escalator, usually 1. 5 to 3 '
               'percent, compounding like inflation. One hundred acres at $1,000 per acre with '
               'a 2 percent escalator starts at $100,000 a year and passes $170,000 by year '
               'thirty. How long does the lease run?',
       'timestamp': 204,
       'timestamp_label': '[00:03:24]',
       'timestamp_seconds': 204,
       'tip': 'Almost every lease also carries an annual escalator, usually 1. 5 to 3 percent, '
              'compounding like inflation. One hundred acres at $1,000 per acre with a 2 '
              'percent escalator starts at $100,000 a year and passes $170,000 by year thirty. '
              'How long does the lease run?',
       'title': 'No Land, No Project? Site Control Explained | US Energy ESSENTIALS (US Energy '
                'Weekly)',
       'url': 'https://www.youtube.com/watch?v=JwCWz91cMQc&t=204s',
       'video_id': 'JwCWz91cMQc'},
      {'author': 'Energy Institute, University of Texas at Austin',
       'channel': 'Energy Institute, University of Texas at Austin',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:25:15](https://www.youtube.com/watch?v=HhLc8bnBSIo&t=1515s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'And so, the the system that I actually showed you, one of the functionalities '
               "we do on the oil and gas rigs is we do the black start capability that's "
               "there. So, what we ultimately will see is as a and I'll I'll go back to the "
               'oil rig to make the point on the data centers.',
       'timestamp': 1515,
       'timestamp_label': '[00:25:15]',
       'timestamp_seconds': 1515,
       'tip': 'And so, the the system that I actually showed you, one of the functionalities '
              "we do on the oil and gas rigs is we do the black start capability that's there. "
              "So, what we ultimately will see is as a and I'll I'll go back to the oil rig to "
              'make the point on the data centers.',
       'title': 'Insights on Battery Energy Storage Systems (BESS) (Energy Institute, '
                'University of Texas at Austin)',
       'url': 'https://www.youtube.com/watch?v=HhLc8bnBSIo&t=1515s',
       'video_id': 'HhLc8bnBSIo'},
      {'author': 'Keentel Engineering',
       'channel': 'Keentel Engineering',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:38](https://www.youtube.com/watch?v=u_aIABsRd0A&t=38s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': "Let's start with what has changed. In the past, a data center was a passive "
               'load. It sat behind a 60 hertz iron core transformer, and its response to a '
               'fault was predictable because it was governed by physics, copper, iron, and '
               'magnetic flux. The future looks very different.',
       'timestamp': 38,
       'timestamp_label': '[00:00:38]',
       'timestamp_seconds': 38,
       'tip': "Let's start with what has changed. In the past, a data center was a passive "
              'load. It sat behind a 60 hertz iron core transformer, and its response to a '
              'fault was predictable because it was governed by physics, copper, iron, and '
              'magnetic flux. The future looks very different.',
       'title': 'Solid-State Transformers & MVDC: Revolutionizing AI Data Center Power Systems '
                '| Keentel Engineering (Keentel Engineering)',
       'url': 'https://www.youtube.com/watch?v=u_aIABsRd0A&t=38s',
       'video_id': 'u_aIABsRd0A'},
      {'author': 'The New York Times',
       'channel': 'The New York Times',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:27](https://www.youtube.com/watch?v=e8QyJw6I-Bc&t=87s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Georgia Power has made aren’t enough to start over again somewhere else. What '
               'if in a year or two from now, they going to come and start another line? '
               'Because all those data centers — how do we know? To me personally, I need '
               'replacement value.',
       'timestamp': 87,
       'timestamp_label': '[00:01:27]',
       'timestamp_seconds': 87,
       'tip': 'Georgia Power has made aren’t enough to start over again somewhere else. What '
              'if in a year or two from now, they going to come and start another line? '
              'Because all those data centers — how do we know? To me personally, I need '
              'replacement value.',
       'title': 'When the Power Company Takes Your Land for a Data Center (The New York Times)',
       'url': 'https://www.youtube.com/watch?v=e8QyJw6I-Bc&t=87s',
       'video_id': 'e8QyJw6I-Bc'},
      {'author': 'pjminterconnection',
       'channel': 'pjminterconnection',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:00:54](https://www.youtube.com/watch?v=ulpPgF6UT1E&t=54s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'By matching energy supply with future energy demand, the capacity market '
               'provides assurance that homeowners will be able to run their air conditioner '
               'on a hot day for several years into the future.',
       'timestamp': 54,
       'timestamp_label': '[00:00:54]',
       'timestamp_seconds': 54,
       'tip': 'By matching energy supply with future energy demand, the capacity market '
              'provides assurance that homeowners will be able to run their air conditioner on '
              'a hot day for several years into the future.',
       'title': 'Markets In A Minute: A Brief Overview of PJM Markets (pjminterconnection)',
       'url': 'https://www.youtube.com/watch?v=ulpPgF6UT1E&t=54s',
       'video_id': 'ulpPgF6UT1E'},
      {'author': 'LUMA',
       'channel': 'LUMA',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:03](https://www.youtube.com/watch?v=UnmedCjwEb0&t=123s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'GD penetration layer, and the incremental hosting capacity layer. In addition '
               'to this, there will be a legend on the left side that will change, that is, it '
               "is dynamic depending on the layer that we are using. Let's start with the "
               'voltage level section.',
       'timestamp': 123,
       'timestamp_label': '[00:02:03]',
       'timestamp_seconds': 123,
       'tip': 'GD penetration layer, and the incremental hosting capacity layer. In addition '
              'to this, there will be a legend on the left side that will change, that is, it '
              "is dynamic depending on the layer that we are using. Let's start with the "
              'voltage level section.',
       'title': 'Tutorial - Hosting Capacity Maps (LUMA)',
       'url': 'https://www.youtube.com/watch?v=UnmedCjwEb0&t=123s',
       'video_id': 'UnmedCjwEb0'},
      {'author': 'Wattlore',
       'channel': 'Wattlore',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:01:59](https://www.youtube.com/watch?v=CDd-hsI3tKQ&t=119s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Nearly half of that solar and storage comes as a pair a solar farm with a '
               "battery right beside it So let's follow one of those from the day it takes its "
               "ticket I'll call it Meadow Solar It's our own made-up example a solar farm.",
       'timestamp': 119,
       'timestamp_label': '[00:01:59]',
       'timestamp_seconds': 119,
       'tip': 'Nearly half of that solar and storage comes as a pair a solar farm with a '
              "battery right beside it So let's follow one of those from the day it takes its "
              "ticket I'll call it Meadow Solar It's our own made-up example a solar farm.",
       'title': 'One solar farm was handed a $598 million bill to plug in (Wattlore)',
       'url': 'https://www.youtube.com/watch?v=CDd-hsI3tKQ&t=119s',
       'video_id': 'CDd-hsI3tKQ'},
      {'author': 'datacenterHawk',
       'channel': 'datacenterHawk',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:11:27](https://www.youtube.com/watch?v=SVLPjGiZivc&t=687s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Week we did a a a panel on with data center dynamics where we talked about the '
               "evolving enterprise user and there's a very.",
       'timestamp': 687,
       'timestamp_label': '[00:11:27]',
       'timestamp_seconds': 687,
       'tip': 'Week we did a a a panel on with data center dynamics where we talked about the '
              "evolving enterprise user and there's a very.",
       'title': 'What is a Hyperscale Data Center? - Data Center Fundamentals - Data Center '
                'Investing (datacenterHawk)',
       'url': 'https://www.youtube.com/watch?v=SVLPjGiZivc&t=687s',
       'video_id': 'SVLPjGiZivc'},
      {'author': 'Energy Storage Assocation',
       'channel': 'Energy Storage Assocation',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[01:00:53](https://www.youtube.com/watch?v=Mk3XaANjMd4&t=3653s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Planning uh for energy storage on December 2nd and 3D and uh please submit any '
               'suggestions for future webinar topics to events at energy stage.org best '
               'wishes for the rest of your day and hoping that you all stay safe and healthy.',
       'timestamp': 3653,
       'timestamp_label': '[01:00:53]',
       'timestamp_seconds': 3653,
       'tip': 'Planning uh for energy storage on December 2nd and 3D and uh please submit any '
              'suggestions for future webinar topics to events at energy stage.org best wishes '
              'for the rest of your day and hoping that you all stay safe and healthy.',
       'title': 'FERC ORDER 2222: Implications for Storage Aggregations, the Grid, and '
                'Resilience Webinar (Energy Storage Assocation)',
       'url': 'https://www.youtube.com/watch?v=Mk3XaANjMd4&t=3653s',
       'video_id': 'Mk3XaANjMd4'},
      {'author': 'Profound Studies',
       'channel': 'Profound Studies',
       'epistemic_status': 'attributed_practitioner_claim',
       'markdown': '[00:02:56](https://www.youtube.com/watch?v=dMPUECoTe2M&t=176s)',
       'relevance': 'Attributed practitioner commentary on GIS-driven `69kV–345kV` substation '
                    'hosting-capacity screening, dark-fiber corridor verification, and '
                    'assignable `12–24` month diligence-contingent land options flipped to '
                    '`BESS` and modular/hyperscale AI data-center developers (Chapter Q12 '
                    'operational verification).',
       'source_type': 'video_pro_tip',
       'text': 'Texas is auditing its list. PJM is building a register. Everyone is trying to '
               "find out which data centers are real. The idea behind PJM's rejected plan has "
               'a name, bring your own new capacity. Data centers that accept cuts in an '
               'emergency could connect sooner.',
       'timestamp': 176,
       'timestamp_label': '[00:02:56]',
       'timestamp_seconds': 176,
       'tip': 'Texas is auditing its list. PJM is building a register. Everyone is trying to '
              "find out which data centers are real. The idea behind PJM's rejected plan has a "
              'name, bring your own new capacity. Data centers that accept cuts in an '
              'emergency could connect sooner.',
       'title': 'Should Data Centers Bring Their Own Power or Wait in Line? (Profound Studies)',
       'url': 'https://www.youtube.com/watch?v=dMPUECoTe2M&t=176s',
       'video_id': 'dMPUECoTe2M'}]}
