from __future__ import annotations

CHAPTER_2 = {'id': 'Q2',
 'chapter_id': 'Q2',
 'chapter_number': 2,
 'question_number': 2,
 'slug': 'building-and-funding-a-reseller-channel-program',
 'question_prompt': 'How does a software vendor build, recruit for, and fund a reseller channel program '
                    'that partners will actually use?',
 'kicker': 'Q2 / THE BIG MONEY PLAYBOOKS',
 'title': 'Building and Funding a Reseller Channel Program',
 'subtitle': 'Step-by-step SaaS channel design, reseller vs. referral setups in partner portals, PRM deal '
             "registration and lead distribution with Salesforce, VMware's recruitment case study, ISV "
             'channel mistakes, recurring-commission programs, and why partners leave Market Development '
             'Funds unused',
 'layout_template': 'executive_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Operators who build reseller channels agree on two things: sequence and '
                      'selectivity. Fix direct sales first. Recruit a narrow set of partners rather than '
                      "200 or 300 idle logos. Make the partner's money obvious with free training, no "
                      "joining fees and tiered margins. Ted Finch's template runs authorized, gold and "
                      'platinum tiers at 10/20/30% margins, with a $250K platinum quota and bonuses for '
                      "deal registration. Payouts range from TAP's $2,500 a month for 12 months per sale "
                      "to Ooma's majority-upfront model. Willingness to Pay prices partner payouts against "
                      'a $21,500 direct CAC. MDF is chronically wasted: ZINFI cites up to 60% unused each '
                      'quarter, and The Crancer Group recovered $5-7K and, in other cases, $20-50K of '
                      'missed Microsoft co-op. The sharpest split is margin size. Luasai says resellers '
                      "take 5-10%, while Viktor's guest says 20-30% usually is not going to be enough.",
 'key_metrics': [{'label': 'Unused Market Development Funds Per Quarter',
                  'metric': 'Unused Market Development Funds Per Quarter',
                  'value': 'As much as 60%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "ZINFI's worldwide channel survey data shows as much as 60% of market "
                             'development funds are not used on a quarterly basis.',
                  'source': 'ZINFI Technologies, Inc. ([lET3Wc2a74o @ 00:00:35])'},
                 {'label': 'TAP Reseller Commission Per Sale',
                  'metric': 'TAP Reseller Commission Per Sale',
                  'value': '$2,500 per month for 12 months',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'TAP Innovations pays this ongoing commission for each SaaS platform sale. '
                             'Its sweet spot is organizations of 100-1,000 people.',
                  'source': 'TAP Innovations ([6_xruMdmmjM @ 00:02:23])'},
                 {'label': 'Direct Customer Acquisition Cost Benchmark',
                  'metric': 'Direct Customer Acquisition Cost Benchmark',
                  'value': '$21,500 CAC',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Funnel example: 100 leads ($10k), 20 qualified ($2k), 4 demos ($4k), 2 '
                             'evaluations ($3k) and 1 close ($2.5k). Partners are paid according to the '
                             'stages they cover.',
                  'source': 'Willingness to Pay ([_pp2kmBgn7s @ 00:13:06])'},
                 {'label': 'Combined Distributor Plus VAR Take',
                  'metric': 'Combined Distributor Plus VAR Take',
                  'value': '5%, maximum 10%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Luasai calls the '40%' reseller-margin objection false. In enterprise "
                             'software, distributor and VAR combined take 5-10%.',
                  'source': 'Luasai ([9ijiF4Aas8o @ 00:14:38])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The loudest agreement among operators is about sequencing: fix the direct '
                              "motion before you bolt on a channel. Luasai's founders say most ISVs hire "
                              'direct reps first and end up about six months behind. They then retrofit a '
                              "channel and have to 'double pay the channel and the reps' [9ijiF4Aas8o @ "
                              '00:03:22]. The Willingness to Pay consultant draws on 30+ client projects '
                              'and often ends up killing the channel for clients. He warns that a partner '
                              "is 'never going to be better at selling' your product than you are, so "
                              'direct sales get fixed first [_pp2kmBgn7s @ 00:47:03]. Viktor from Sales '
                              'reaches the same conclusion in his takeaways: figure out direct sales, get '
                              "a seat at the table, do things that don't scale, and skip the PRM early "
                              '[6Z4v3jibmMw @ 00:41:37]. The second shared rule is fewer, sharper '
                              "partners. Luasai warns against recruiting 200 partners only to watch '195' "
                              "sit idle. Viktor's guest says signing '300 Partners' in a month spreads the "
                              'team too thin. He pushes a narrow ideal partner profile and fast '
                              'disqualification instead [6Z4v3jibmMw @ 00:04:25]. Founders who expect '
                              'gratitude get corrected too. Partners are often bigger businesses, and '
                              "recruiting one is like hiring a rep on 'commission only,' so the vendor has "
                              'to earn every hour of attention.',
                              'The second consensus point is that a reseller program lives or dies on one '
                              'question partners ask: can I make money? Ted Finch of channel.com has '
                              'worked in the channel since 1989 and built 270+ programs. He says resellers '
                              'first probe whether the product is competitive, then margins, regional '
                              'competition, training, channel conflict and sales tools. He discourages '
                              'charging for training because it becomes a barrier to entry [hdz5UsJS-qY @ '
                              '00:05:29]. Vendors running live programs echo this low-friction entry. Iron '
                              "Software's Nick pitches 'no joining fee and no upfront commitment,' plus "
                              "tiered discounts where 'the more you sell, the deeper your discounts' "
                              '[lCobx44k0Tw @ 00:00:47]. TAP Innovations bundles materials, resources and '
                              "training 'at no extra cost.' That covers lead generation, selling to "
                              'existing and past customers, opportunity meetings and account management '
                              '[6_xruMdmmjM @ 00:02:40]. Ooma provides training modules, a partner support '
                              'line, and a marketing and branding library. VARs also get a Dedicated '
                              'Account Manager, priority technical support and the option to order direct '
                              '[a299ToKLxRs @ 00:00:45]. The pattern holds across all four: enablement is '
                              'free, economics are tiered to reward volume, and partners can reach support '
                              'while a deal is still live. Finch adds that a reseller support hotline '
                              'should answer in 30 seconds, not 20 minutes.',
                              'On market development funds, operators agree on two things: the money is '
                              'real, and most partners leave it on the table. Pete Matheson calls MDF '
                              "'free money, sat there, waiting for you to use it.' It typically covers up "
                              'to 50% of an activity and is usually paid after the event. He says mostly '
                              "bigger MSPs tap it, while smaller ones don't know about it, don't "
                              "understand it, or don't use it [lcMWkAWGxSU @ 00:00:32]. ZINFI puts a "
                              "number on the leak: its worldwide channel survey data shows 'as much as "
                              "60%' of market development funds go unused each quarter [lET3Wc2a74o @ "
                              '00:00:35]. ZINFI gives several reasons. The vendor is an add-on rather than '
                              "the partner's core business. Partners under $5-10M plan quarterly. "
                              'Resellers lack digital skills and dedicated marketers. The Crancer Group '
                              "calls Microsoft co-op the 'biggest missed incentive,' measured on CSP seats "
                              'and MRR, Azure consumption, and designations or specializations '
                              '[dM62o5Vq5U4 @ 00:03:10]. Marketing Business Network lays out the chain '
                              'everyone works within: proposal, approval, activity, a claim with evidence, '
                              "then payment. It stresses that 'an approved budget is not automatically a "
                              "payment' [gPoVTzxEwPw @ 00:00:44]. ZINFI's fix is to focus on partners who "
                              'already use funds and to automate localized, co-branded campaigns partners '
                              'can launch themselves.'],
               'table': {'caption': 'Where the operators line up on how a reseller channel gets built and '
                                    'funded',
                         'headers': ['Consensus Principle',
                                     'What The Practitioner Reports',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Direct sales before any channel buildout',
                                   'ISVs that hire direct reps first fall about six months behind, then '
                                   'double pay channel and reps',
                                   'Prove a repeatable direct motion before recruiting resellers to carry '
                                   'it',
                                   'Luasai ([9ijiF4Aas8o @ 00:03:22])'],
                                  ['Partners will not outsell the vendor',
                                   'A partner is never going to be better at selling your product than you '
                                   'are',
                                   'Fix direct sales first and treat the channel as a multiplier, not a '
                                   'rescue',
                                   'Willingness to Pay ([_pp2kmBgn7s @ 00:47:03])'],
                                  ['Narrow ideal partner profile over volume signups',
                                   'Signing 300 partners in a month spreads the partnership team far too '
                                   'thin',
                                   'Write a narrow ideal partner profile and disqualify poor fits quickly',
                                   'Viktor from Sales ([6Z4v3jibmMw @ 00:05:07])'],
                                  ['Partner profitability is the first question asked',
                                   'Resellers ask whether the product is competitive and whether they can '
                                   'make money',
                                   'Lead recruiting pitches with margins, regional competition, training '
                                   'and conflict rules',
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:05:29])'],
                                  ['Low-friction entry with performance-based tiers',
                                   'No joining fee, no upfront commitment, no hard quotas, and deeper '
                                   'discounts with volume',
                                   'Remove signup friction and let incentives scale with actual partner '
                                   'sales',
                                   'Iron Software ([lCobx44k0Tw @ 00:00:47])'],
                                  ['Market development funds are chronically left unused',
                                   'Survey data shows as much as 60% of MDF goes unused every single '
                                   'quarter',
                                   'Target partners who already spend funds and automate co-branded '
                                   'campaigns for the rest',
                                   'ZINFI Technologies, Inc. ([lET3Wc2a74o @ 00:00:35])'],
                                  ['MDF works as after-the-fact reimbursement',
                                   'Vendors usually cover up to 50% of an activity and pay after the event',
                                   'Ask vendors which activities worked for other partners before '
                                   'committing any spend',
                                   'Pete Matheson - Not a Business Coach ([lcMWkAWGxSU @ 00:00:32])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Ted Finch's tier template is the most complete build sheet any of these "
                              "operators offer. Use plain names, 'authorized, gold, platinum,' with "
                              'example margins of 10/20/30%. Authorized carries no quota and gets no '
                              "leads. Gold adds a quota and first-level certification. Platinum's example "
                              'quota is $250K a year plus a second certification covering first- and '
                              'second-line support [hdz5UsJS-qY @ 00:08:53]. Leads route by region, then '
                              'by level, and quotas keep a shared salesforce loyal. For the ramp, he '
                              'grandfathers new partners into gold for 90 days. He runs a new program for '
                              'about six months, then sets levels from real data, for example platinum at '
                              '$100K-150K with a $10K minimum. Partners get three months to transition '
                              'between levels [hdz5UsJS-qY @ 00:13:19]. His deal-registration split plugs '
                              'into the tiers: gold gets 10% base plus 10% for registering, and platinum '
                              'gets 20% base plus 10%. If registration compliance is low, he raises the '
                              'registered portion. Digital Watchdog runs four tiers, with better buying '
                              'discounts at higher tiers. Partners must save up to five distribution '
                              'account numbers under the My Company tab before they can earn rewards '
                              '[NrZYppqY_R4 @ 00:00:16]. Iron Software keeps tiered discounts without hard '
                              "quotas, 'so your incentive grows with your performance' [lCobx44k0Tw @ "
                              '00:01:25].',
                              'Payout design is where the numbers get specific. TAP Innovations pays '
                              "'$2,500 per month for 12 months for each sale,' and its sweet spot is "
                              'organizations of 100-1,000 people [6_xruMdmmjM @ 00:02:23]. Ooma pays a '
                              'multiple of monthly service plus a percentage of ongoing service. Unlike '
                              "programs that dole payment out slowly over a long period, Ooma 'pays the "
                              "majority upfront' [a299ToKLxRs @ 00:00:28]. Finch shows why timing matters. "
                              'A $10K desktop sale pays $1,000 now, versus $100 a month on a $12K SaaS '
                              'deal. SaaS can pay roughly 3x over five years. Companies at $1-5M pay 28% '
                              'upfront, and larger ones pay 50%. A 70% cancellation rate makes the deal a '
                              "'bum deal' for the partner [hdz5UsJS-qY @ 00:53:21]. The Willingness to Pay "
                              'consultant prices partner payouts against the CAC funnel he would otherwise '
                              'fund: 100 leads at $10k, 20 qualified at $2k, 4 demos at $4k, 2 evaluations '
                              'at $3k and 1 close at $2.5k. That totals $21,500 CAC, and he pays partners '
                              'for the funnel stages they actually cover [_pp2kmBgn7s @ 00:13:06]. He also '
                              "checks fit: your product should be 5-15% of the partner's deal. He drops "
                              "the '20% of ARR' norm and front-loads payment, for example 50% in year one.",
                              "The plumbing is concrete. Channeltivity's Zach pushes partner-registered "
                              'deals into Salesforce as leads. Partner data stays in separate fields '
                              "'since there's an inherent danger' in letting partners update your CRM, and "
                              'the link survives conversion from lead to opportunity. Setup takes four '
                              'steps: enter credentials with API access, choose deal registration only or '
                              'add lead distribution, map fields in each direction, done [5iuG2nYpJ0U @ '
                              "00:00:55]. PartnerPortal io frames the reseller switch as 'who collects the "
                              "customer's money.' Set the Partner Model card to Reseller and let the "
                              'partner collect. Match revenue by tagging Stripe, QuickBooks or Xero '
                              "invoices with the lead's website domain. For revenue with no named "
                              "customer, create a catch-all Won lead on the reseller's own domain "
                              '[KpcTpbw5dho @ 00:01:09]. Finch uses a generic portal until about 50 '
                              'partners. His record setup time is under four hours, and he warns against '
                              'replicating the main website inside the portal [hdz5UsJS-qY @ 00:15:19]. '
                              'For Microsoft, The Crancer Group picks the Cloud Solutions Provider fund '
                              'category, not hosting co-op. A $0 balance means either no designation or '
                              'not yet past the $10K threshold. He checks every location plus hosting '
                              'co-op and Surface rebates. That turned up an extra $5-7K and, in other '
                              'cases, $20-50K [dM62o5Vq5U4 @ 00:06:19].'],
               'table': {'caption': 'Exact payout, margin and funding numbers operators quote for reseller '
                                    'programs',
                         'headers': ['Lever',
                                     'Exact Number Taught',
                                     'How The Operator Uses It',
                                     'Expert Source'],
                         'rows': [['Recurring SaaS reseller commission',
                                   '$2,500 per month for 12 months for each sale closed',
                                   'Targets organizations of 100-1,000 people as the commission sweet spot',
                                   'TAP Innovations ([6_xruMdmmjM @ 00:02:23])'],
                                  ['Deal registration bonus layered on tiers',
                                   'Gold 10% base plus 10% registered; platinum 20% base plus 10%',
                                   'Raises the registered portion when partners fail to register their '
                                   'deals',
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:27:48])'],
                                  ['Enterprise distributor plus VAR combined take',
                                   '5%, maximum 10%, versus the claimed 40% reseller margin objection',
                                   'Offloads procurement admin, returns about 30% of rep time, adds 10%+ '
                                   'revenue',
                                   'Luasai ([9ijiF4Aas8o @ 00:14:38])'],
                                  ['Direct customer acquisition cost benchmark',
                                   '$21,500 CAC across leads, qualification, demos, evaluation and close',
                                   'Pays partners according to which funnel stages they actually cover',
                                   'Willingness to Pay ([_pp2kmBgn7s @ 00:13:06])'],
                                  ['Partner deal-size fit window',
                                   "Product at 5-15% of the partner's deal, roughly $25k-75k",
                                   'Rejects $200k products inside $500k projects and $5k add-ons as '
                                   'misfits',
                                   'Willingness to Pay ([_pp2kmBgn7s @ 00:25:19])'],
                                  ['MDF matching reimbursement math',
                                   'Vendor covers 50% up to $1,000; $1,600 spent returns $800',
                                   'Treats the cap as a ceiling and files claims with evidence on deadline',
                                   'Marketing Business Network ([gPoVTzxEwPw @ 00:01:00])'],
                                  ['Recovered Microsoft co-op dollars',
                                   'Extra $5-7K found, and $20-50K in other partner cases',
                                   'Checks every location, hosting co-op and Surface rebates in the '
                                   'earnings dashboard',
                                   'The Crancer Group ([dM62o5Vq5U4 @ 00:06:19])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Street-Level Moves Operators Actually Run',
                           'body': 'Unconventional tactics operators use to filter competitors, drive real '
                                   'product usage, mine hidden partners and unlock incentive tiers.',
                           'items': ["Add a fake 'authorized distributor' requirement to the reseller "
                                     'application to stop competitors from applying. Pair it with detailed '
                                     'partner profiling; one company paid $38,000 to re-profile later '
                                     '[chanimalvideos — hdz5UsJS-qY @ 00:40:02].',
                                     'Charge $5-10 for not-for-resale copies instead of giving them away. '
                                     "Ashton-Tate's free 15-per-location copies mostly went uninstalled, "
                                     'while a small charge pushed usage above 70%. Alternative: a '
                                     '10-question quiz [chanimalvideos — hdz5UsJS-qY @ 00:37:23].',
                                     'Run Clearbit enrichment on your existing user base to find partners '
                                     "already inside it. Viktor's guest surfaced about 700 agencies "
                                     'already using the product [Viktor from Sales — 6Z4v3jibmMw @ '
                                     '00:07:14].',
                                     "Count nonprofits toward new customer adds in Microsoft's program. "
                                     'They can carry a partner to the Modern Work designation, which '
                                     'Copilot accelerators require [The Crancer Group — dM62o5Vq5U4 @ '
                                     '00:01:58].']},
               'sop_steps': [{'step': 1,
                              'title': "Recruit From Competitors' Reseller Benches First",
                              'action': "Build the recruiting list in order: competitors' resellers, then "
                                        'alliance partners, then purchased lists. Open with email.',
                              'detail': "Finch starts with competitors' resellers, moves to alliance "
                                        "partners such as Citrix's roughly 2,200, then lists such as CMP "
                                        'and VAR City. He runs a 3-part email campaign. A CRN newsletter '
                                        'placement cost about $800 and brought in 35 resellers '
                                        '[chanimalvideos — hdz5UsJS-qY @ 01:03:43].'},
                             {'step': 2,
                              'title': 'Launch Tiers With A Grandfathered Ramp',
                              'action': 'Grandfather new partners into gold for 90 days, run about six '
                                        'months, then set tier thresholds from actual sales data.',
                              'detail': 'Example thresholds after the ramp: platinum at $100K-150K with a '
                                        '$10K minimum. Give three months to transition between levels. '
                                        'Require one promotion per month for the first three months '
                                        '[chanimalvideos — hdz5UsJS-qY @ 00:13:19].'},
                             {'step': 3,
                              'title': 'Wire Deal Registration Into The CRM',
                              'action': 'Push registered deals into Salesforce as leads with partner data '
                                        'walled off in separate fields, and map fields both directions.',
                              'detail': 'Enter credentials with API access, pick deal registration only or '
                                        'add lead distribution, and map fields for each direction. The '
                                        'link survives conversion from lead to opportunity [Channeltivity '
                                        '- Channel Partner Portal — 5iuG2nYpJ0U @ 00:00:55].'},
                             {'step': 4,
                              'title': 'Run MDF Through The Full Claim Chain',
                              'action': 'Get the proposal approved before spending. Execute the activity, '
                                        'file the claim with evidence on deadline, then track outcomes '
                                        'separately.',
                              'detail': 'An approved budget is not automatically a payment. Miss a '
                                        'deadline or run unapproved spend and the partner may pay the '
                                        'bill. Partners may also have to front the costs [Marketing '
                                        'Business Network — gPoVTzxEwPw @ 00:00:44].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over how much margin a reseller actually needs. '
                              'Luasai [9ijiF4Aas8o @ 00:14:38] calls the 40% objection false outright. In '
                              'their enterprise deals, the distributor and the VAR combined take 5%, '
                              'maximum 10%, because the ISV rep keeps control and plays quarterback on SKU '
                              'and terms while the partner offloads procurement admin. Viktor from Sales '
                              '[6Z4v3jibmMw @ 00:30:05] lands somewhere else. A 20 to 30% margin usually '
                              "is not going to be enough on its own, because the partner's real money is "
                              'in services. At 10% of a $100k deal the partner gets only $10k, so '
                              'certifications, marketing and priority support have to round out the offer. '
                              'chanimalvideos [hdz5UsJS-qY @ 00:47:51] brings survey data showing how '
                              'fragmented the market is. Sixty percent of SaaS vendors pay 10 to 15%, '
                              'which Ted Finch labels affiliate rates. Some pay 16 to 30%, and 21% pay 40% '
                              'or more. Meanwhile a desktop 50% discount erodes to roughly 30% once the '
                              'reseller discounts to win. Willingness to Pay [_pp2kmBgn7s @ 00:27:14] '
                              'documents the high end in practice. In a hospital-robot deal the vendor ran '
                              'the entire top of the funnel and the distributor only closed, yet the '
                              'distributor still took 30%.',
                              'Payout timing splits operators into front-loaders and drip-payers. '
                              'Willingness to Pay [_pp2kmBgn7s @ 00:35:26] tells clients to drop the '
                              '20%-of-ARR norm and front-load, for example 50% in year one, then pay '
                              'cost-plus for any service work. The VC math backs this up. At ARR 100 and a '
                              '20x multiple, the front-loaded model funds roughly 200 per year of capital, '
                              'versus about 160 under a recurring 20% cut. Ooma [a299ToKLxRs @ 00:00:28] '
                              'pitches the same idea to recruits. Unlike most programs where payment is '
                              'slowly doled out over a long period of time, Ooma pays a multiple of '
                              'monthly service plus a percentage of ongoing service, with the majority '
                              'upfront. TAP Innovations [6_xruMdmmjM @ 00:02:23] runs the opposite '
                              'structure, paying $2,500 per month for 12 months for each sale. Its sweet '
                              'spot is organizations of 100 to 1,000 people. chanimalvideos [hdz5UsJS-qY @ '
                              '00:53:21] frames the tension in cash terms. A $10K desktop sale pays the '
                              'reseller $1,000 now, while a $12K SaaS deal pays $100 a month, even though '
                              'SaaS can pay about three times as much over five years. Vendors at $1 to 5M '
                              'pay 28% upfront and larger ones pay 50%. A 70% cancellation rate turns '
                              'recurring commission into a bum deal.',
                              'Quotas and recruiting breadth are the third fault line. chanimalvideos '
                              '[hdz5UsJS-qY @ 00:08:53] builds authorized, gold and platinum tiers at '
                              'example margins of 10, 20 and 30%. Authorized carries no quota. Gold adds a '
                              'quota and first-level certification. Platinum requires a $250K yearly quota '
                              'plus a second certification. The argument is that quotas keep a shared '
                              'salesforce loyal. Leads route by region and then by level, and authorized '
                              'partners get none. Iron Software [lCobx44k0Tw @ 00:01:25] goes the other '
                              'way: no joining fee, no upfront commitment, no hard quotas, and discounts '
                              'that simply deepen the more a partner sells. On volume, chanimalvideos '
                              "[hdz5UsJS-qY @ 01:03:43] recruits wide. The order is competitors' resellers "
                              "first, then alliance partners such as Citrix's roughly 2,200, then "
                              'purchased lists. One CRN newsletter placement cost about $800 and brought '
                              'in 35 resellers. The same session cites SalesLogix pilfering over 800 '
                              'resellers from GoldMine. It also recommends a fake authorized-distributor '
                              'requirement to stop competitors from applying. Viktor from Sales '
                              '[6Z4v3jibmMw @ 00:05:07] runs the opposite playbook. That means a narrow '
                              'ideal partner profile and fast disqualification, plus a blunt warning that '
                              'signing 300 partners in a month spreads the partner team too thin.'],
               'table': {'caption': 'Side-by-side playbooks where channel practitioners split',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Reseller margin needed to win enterprise software deals',
                                   'Distributor plus VAR combined take 5%, maximum 10%, while the ISV rep '
                                   'quarterbacks terms',
                                   'A 20 to 30% margin usually is not enough without partner services '
                                   'revenue',
                                   'Luasai ([9ijiF4Aas8o @ 00:14:38]) versus Viktor from Sales '
                                   '([6Z4v3jibmMw @ 00:30:05])'],
                                  ['Commission timing structure for recurring SaaS partner revenue',
                                   'Front-load payouts, for example 50% in year one, and drop the '
                                   '20%-of-ARR norm',
                                   'Pay $2,500 per month for 12 months for each closed sale',
                                   'Willingness to Pay ([_pp2kmBgn7s @ 00:35:26]) versus TAP Innovations '
                                   '([6_xruMdmmjM @ 00:02:23])'],
                                  ['Quotas as the loyalty lever across partner tiers',
                                   'Authorized, gold, platinum at 10, 20, 30% margins with a $250K '
                                   'platinum quota',
                                   'No joining fee, no hard quotas, and discounts deepen as partner volume '
                                   'grows',
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:08:53]) versus Iron Software '
                                   '([lCobx44k0Tw @ 00:01:25])'],
                                  ['How wide to cast the partner recruiting net',
                                   "Raid competitors' resellers first; one CRN placement at about $800 "
                                   'brought in 35 resellers',
                                   'Narrow ideal partner profile and fast disqualification; 300 partners '
                                   'in a month spreads too thin',
                                   'chanimalvideos ([hdz5UsJS-qY @ 01:03:43]) versus Viktor from Sales '
                                   '([6Z4v3jibmMw @ 00:05:07])'],
                                  ['When to stand up a partner portal or PRM',
                                   'Run a generic portal until about 50 partners; record setup took under '
                                   'four hours',
                                   "No PRM early; get a seat at the table and do things that don't scale",
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:15:19]) versus Viktor from Sales '
                                   '([6Z4v3jibmMw @ 00:44:09])'],
                                  ['Who directs partner marketing money and campaign execution',
                                   'Co-op accrues and the partner chooses the spend, while with MDF the '
                                   'vendor directs it',
                                   'Automate localized co-branded campaigns partners launch themselves, '
                                   'plus free bite-size concierge help',
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:02:20]) versus ZINFI Technologies, '
                                   'Inc. ([lET3Wc2a74o @ 00:04:17])'],
                                  ['Referral partner versus true reseller billing and payout model',
                                   'Reseller bills the customer and keeps margin, you bill wholesale, so '
                                   "there's no commission to pay",
                                   'Referral-only is an affiliate marketing program; partners also need '
                                   'marketing, certifications, priority support',
                                   'PartnerPortal io ([KpcTpbw5dho @ 00:00:20]) versus Viktor from Sales '
                                   '([6Z4v3jibmMw @ 00:32:39])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure is opening a channel too early or bolting it on '
                              'too late. Luasai [9ijiF4Aas8o @ 00:03:22] watches ISVs hire direct reps '
                              'first and land about six months behind. They then retrofit a channel and '
                              'end up having to double pay the channel and the reps. Of the 10 to 20 ISVs '
                              'they cite, very few get the mix right. Willingness to Pay [_pp2kmBgn7s @ '
                              '00:01:17] reports more channels failing than succeeding across 30-plus '
                              'client projects and often ends up killing the channel outright. The same '
                              'speaker warns [_pp2kmBgn7s @ 00:47:03] that a partner is never going to be '
                              'better at selling your product than you are, so direct sales get fixed '
                              'first. Viktor from Sales [6Z4v3jibmMw @ 00:01:40] adds the founder trap. '
                              'Teams turn to partners only when they hit a growth ceiling, then discover '
                              'several problems at once. Partners take longer to nurture than direct '
                              'deals, they expect leads from the vendor too, and they often sign up for '
                              'the logo and then never sell, or undercut on price. Luasai names the '
                              'mindset error underneath all of it. Founders expect partners to be '
                              'grateful, but partners are often bigger businesses, and recruiting one is '
                              'like hiring a rep on commission only.',
                              'Partner sprawl and deal-size misfit kill programs that look healthy on '
                              'paper. Luasai [9ijiF4Aas8o @ 00:25:51] warns against recruiting 200 '
                              'partners with 195 sitting idle, and against importing Palo Alto playbooks '
                              'into a Series A company. Viktor from Sales [6Z4v3jibmMw @ 00:36:27] '
                              'recounts the big-logo version at Accenture, where roughly 100 users out of '
                              '200,000 people in India alone was not enough. Small agencies of 10 to 100 '
                              'people moved faster. Willingness to Pay [_pp2kmBgn7s @ 00:21:01] puts a '
                              'number on the misfit: about three of four partner agreements fail on ACV. A '
                              '$200k product inside a $500k system-integrator project is too big at 40% of '
                              'the deal. A $5k product adds only about 0.2% and is too small. The sweet '
                              "spot is 5 to 15% of the partner's deal, roughly $25k to $75k. The same "
                              'speaker tracks a partner funnel where 100 surveyed partners yield 2 closed, '
                              'then watches for silent-partnership churn after signing. Recruiting itself '
                              'grinds. chanimalvideos [hdz5UsJS-qY @ 00:44:53] reports a record of seven '
                              'calls just to reach one channel manager, and finds that 60 to 70% of vendor '
                              'sites miss sign-up basics.',
                              'Funding traps sit inside MDF and co-op mechanics. Marketing Business '
                              'Network [gPoVTzxEwPw @ 00:01:41] lays out the chain: proposal, approval, '
                              'activity, claim with evidence, then payment. The speaker stresses that an '
                              'approved budget is not automatically a payment. With a 50% match capped at '
                              '$1,000, a $1,600 event returns $800. A missed deadline or unapproved spend '
                              'can leave the partner paying the whole bill. Pete Matheson [lcMWkAWGxSU @ '
                              '00:01:43] warns that some vendors demand proof of ROI, leads, conversion '
                              'rates and sales. Mostly bigger MSPs claim the funds, while smaller ones '
                              "don't know about them, don't understand them, or don't use them. ZINFI "
                              'Technologies [lET3Wc2a74o @ 00:00:59] explains why as much as 60% of MDF '
                              'goes unused each quarter. The vendor is an add-on, partners under $5 to 10M '
                              'plan quarterly, and they lack dedicated marketers. Corruption sometimes '
                              'reaches into channel management itself. The Crancer Group [dM62o5Vq5U4 @ '
                              '00:06:19] shows the Microsoft version of the leak. A $0 balance means no '
                              'designation, or not yet past the $10K threshold. Checking every location, '
                              'plus hosting co-op and Surface rebates, surfaced an extra $5 to 7K, and in '
                              'other cases $20 to 50K.'],
               'table': {'caption': 'Firsthand channel failures with the economics behind each one',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Retrofitting a channel after hiring direct reps first',
                                   'ISVs hire direct reps first, fall about six months behind, then bolt '
                                   'on partners',
                                   'The retrofit forces the vendor to double pay the channel and the reps',
                                   'Luasai ([9ijiF4Aas8o @ 00:05:43])'],
                                  ['Free not-for-resale copies that nobody ever installs',
                                   'Ashton-Tate handed out 15 free copies per location and few were ever '
                                   'installed',
                                   'Charging $5 to $10 pushed usage above 70%; the alternative is a '
                                   '10-question quiz',
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:37:23])'],
                                  ['Slow, first-year-only SaaS commission payouts to partners',
                                   'Salesforce pays 10%, first year only, 45 days after quarter end, about '
                                   '4.5 months',
                                   'Most affiliate programs pay every 30 days; Finch calls Salesforce one '
                                   'of the worst examples',
                                   'chanimalvideos ([hdz5UsJS-qY @ 00:58:50])'],
                                  ["Product ACV misfit inside the partner's larger deal",
                                   'About three of four partner agreements fail because the product ACV '
                                   'does not fit',
                                   "Target 5 to 15% of the partner's deal, roughly $25k to $75k per deal",
                                   'Willingness to Pay ([_pp2kmBgn7s @ 00:21:01])'],
                                  ['Unapproved or late MDF spend left unreimbursed by the vendor',
                                   'Missed deadlines or unapproved spend can leave the partner paying the '
                                   'full bill',
                                   'At 50% up to $1,000, a $1,600 event returns only $800 to the partner',
                                   'Marketing Business Network ([YKXY9b__zcA @ 00:01:42])'],
                                  ['Partner leader laid off before the channel program matures',
                                   'Partner leaders have short tenure and often get laid off at 6 to 12 '
                                   'months',
                                   'Lock C-level alignment for 1 to 2 years, since partners may take that '
                                   'long',
                                   'Viktor from Sales ([6Z4v3jibmMw @ 00:20:56])'],
                                  ['Channel neglect from thin partner management coverage across the base',
                                   'One person covering 1,000 resellers is what Finch calls channel '
                                   'neglect outright',
                                   "Finch's 4-person team raised sales 620% in under six weeks by managing "
                                   'like sales',
                                   'chanimalvideos ([hdz5UsJS-qY @ 01:07:03])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill-Switch Checks Before You Sign or Fund a Partner',
                           'body': 'Run each check before you sign a partner or commit channel budget. '
                                   'Every check comes from a loss, reversal or bottleneck the '
                                   'practitioners hit themselves.',
                           'items': ['Do not open the channel until direct sales converts, because a '
                                     'partner is never going to be better at selling your product than you '
                                     'are [Willingness to Pay — _pp2kmBgn7s @ 00:47:03].',
                                     'Recruit only partners you can activate, since 200 signed partners '
                                     'with 195 sitting idle is the pattern that sinks programs [Luasai — '
                                     '9ijiF4Aas8o @ 00:25:51].',
                                     'Keep partner-submitted deal data in separate CRM fields, since '
                                     "there's an inherent danger in letting partners update your CRM "
                                     'directly [Channeltivity - Channel Partner Portal — 5iuG2nYpJ0U @ '
                                     '00:00:55].',
                                     'Get every MDF activity approved first and file the claim with '
                                     'evidence before the deadline, because an approved budget is not '
                                     'automatically a payment [Marketing Business Network — gPoVTzxEwPw @ '
                                     '00:00:44].']}}],
 'pull_quote': 'The most successful companies in the world are indirect companies. — Luasai (9ijiF4Aas8o @ '
               '00:18:12).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Run Clearbit enrichment on your existing user base to surface agencies already '
                      'using the product; one run found about 700 [Viktor from Sales — 6Z4v3jibmMw @ '
                      '00:07:14].',
                      'Map your CAC funnel from leads to close (a $21,500 example) and pay each partner '
                      'only for the funnel stages it covers [Willingness to Pay — _pp2kmBgn7s @ 00:16:12].',
                      'Split deal registration payouts, e.g. gold at 10% base plus 10% for registering, '
                      'and raise the registered portion if registration is low [chanimalvideos — '
                      'hdz5UsJS-qY @ 00:27:48].',
                      'Open the Microsoft earnings dashboard and select the Cloud Solutions Provider fund '
                      'category. Then check every location, plus hosting co-op and Surface rebates, for '
                      'unclaimed money [The Crancer Group — dM62o5Vq5U4 @ 00:06:19].',
                      'Set the Partner Model card to Reseller and tag each Stripe, QuickBooks or Xero '
                      "invoice with the lead's website domain so reseller revenue matches the right lead "
                      '[PartnerPortal io — KpcTpbw5dho @ 00:01:09].',
                      "Require partners to enter up to five distribution account numbers in the portal's "
                      'My Company tab before they can earn rewards and sell [Digital Watchdog — '
                      'NrZYppqY_R4 @ 00:01:04].'],
 'statutory_citations': [{'title': 'Luasai — Why Most ISVs Get Channel Wrong | Building an Enterprise '
                                   'Software Ecosystem [00:14:38]',
                          'url': 'https://www.youtube.com/watch?v=9ijiF4Aas8o&t=878s',
                          'relevance': 'Primary practitioner testimony on the 5 to 10% reseller margin, '
                                       'ISV rep control, and the double-pay retrofit failure.'},
                         {'title': 'Willingness to Pay — SaaS Partners & Resellers [Lessons From 30+ '
                                   'Client Projects] [00:21:01]',
                          'url': 'https://www.youtube.com/watch?v=_pp2kmBgn7s&t=1261s',
                          'relevance': 'Primary practitioner testimony on ACV misfit, front-loaded partner '
                                       'payouts, and funnel-stage partner compensation.'},
                         {'title': 'chanimalvideos — How to Create a Reseller Program  - SaaS & Enterprise '
                                   'Software & Hardware [00:27:48]',
                          'url': 'https://www.youtube.com/watch?v=hdz5UsJS-qY&t=1668s',
                          'relevance': 'Primary practitioner testimony on tier design, deal registration '
                                       'splits, recruiting tactics, and commission timing.'},
                         {'title': 'Marketing Business Network — What are Market Development Funds? '
                                   '[00:00:44]',
                          'url': 'https://www.youtube.com/watch?v=gPoVTzxEwPw&t=44s',
                          'relevance': 'Primary practitioner testimony on the MDF proposal-to-payment '
                                       'chain and reimbursement traps.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '6_xruMdmmjM',
                       'title': 'TAP Reseller/Channel Partner Video',
                       'channel': 'TAP Innovations',
                       'author': 'TAP Innovations',
                       'text': 'Partners earn $2,500 per month for 12 months for each sale.',
                       'tip': 'Partners earn $2,500 per month for 12 months for each sale.',
                       'timestamp': 143,
                       'timestamp_seconds': 143,
                       'timestamp_label': '[00:02:23]',
                       'url': 'https://www.youtube.com/watch?v=6_xruMdmmjM&t=143s',
                       'markdown': '[00:02:23](https://www.youtube.com/watch?v=6_xruMdmmjM&t=143s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lCobx44k0Tw',
                       'title': 'Join the Iron Software Reseller Partner Program',
                       'channel': 'Iron Software',
                       'author': 'Iron Software',
                       'text': "There's no joining fee and no upfront commitment.",
                       'tip': "There's no joining fee and no upfront commitment.",
                       'timestamp': 47,
                       'timestamp_seconds': 47,
                       'timestamp_label': '[00:00:47]',
                       'url': 'https://www.youtube.com/watch?v=lCobx44k0Tw&t=47s',
                       'markdown': '[00:00:47](https://www.youtube.com/watch?v=lCobx44k0Tw&t=47s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lCobx44k0Tw',
                       'title': 'Join the Iron Software Reseller Partner Program',
                       'channel': 'Iron Software',
                       'author': 'Iron Software',
                       'text': "We don't set hard quotas, so your incentive grows with your performance.",
                       'tip': "We don't set hard quotas, so your incentive grows with your performance.",
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=lCobx44k0Tw&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=lCobx44k0Tw&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hdz5UsJS-qY',
                       'title': 'How to Create a Reseller Program  - SaaS & Enterprise Software & Hardware',
                       'channel': 'chanimalvideos',
                       'author': 'chanimalvideos',
                       'text': 'The vendor will not call on a registered deal, and if it makes a mistake '
                               'it still pays the reseller the full commission.',
                       'tip': 'The vendor will not call on a registered deal, and if it makes a mistake it '
                              'still pays the reseller the full commission.',
                       'timestamp': 1668,
                       'timestamp_seconds': 1668,
                       'timestamp_label': '[00:27:48]',
                       'url': 'https://www.youtube.com/watch?v=hdz5UsJS-qY&t=1668s',
                       'markdown': '[00:27:48](https://www.youtube.com/watch?v=hdz5UsJS-qY&t=1668s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hdz5UsJS-qY',
                       'title': 'How to Create a Reseller Program  - SaaS & Enterprise Software & Hardware',
                       'channel': 'chanimalvideos',
                       'author': 'chanimalvideos',
                       'text': 'When free copies were handed out few were installed, but charging $5 to '
                               '$10 pushed usage above 70%.',
                       'tip': 'When free copies were handed out few were installed, but charging $5 to $10 '
                              'pushed usage above 70%.',
                       'timestamp': 2243,
                       'timestamp_seconds': 2243,
                       'timestamp_label': '[00:37:23]',
                       'url': 'https://www.youtube.com/watch?v=hdz5UsJS-qY&t=2243s',
                       'markdown': '[00:37:23](https://www.youtube.com/watch?v=hdz5UsJS-qY&t=2243s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5iuG2nYpJ0U',
                       'title': "Integrate Salesforce w/ Channeltivity's PRM Software - Deal Registration "
                                'and Lead Distribution',
                       'channel': 'Channeltivity - Channel Partner Portal',
                       'author': 'Channeltivity - Channel Partner Portal',
                       'text': "Partner data lives in its own fields, since there's an inherent danger in "
                               'letting partners update your CRM.',
                       'tip': "Partner data lives in its own fields, since there's an inherent danger in "
                              'letting partners update your CRM.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=5iuG2nYpJ0U&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=5iuG2nYpJ0U&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lcMWkAWGxSU',
                       'title': 'What is Market Development Funds (MDF)',
                       'channel': 'Pete Matheson - Not a Business Coach',
                       'author': 'Pete Matheson - Not a Business Coach',
                       'text': 'MDF stands for Market Development Funds and ensure it is free money, sat '
                               'there, waiting for you to use it.',
                       'tip': 'MDF stands for Market Development Funds and ensure it is free money, sat '
                              'there, waiting for you to use it.',
                       'timestamp': 16,
                       'timestamp_seconds': 16,
                       'timestamp_label': '[00:00:16]',
                       'url': 'https://www.youtube.com/watch?v=lcMWkAWGxSU&t=16s',
                       'markdown': '[00:00:16](https://www.youtube.com/watch?v=lcMWkAWGxSU&t=16s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dM62o5Vq5U4',
                       'title': 'VOMP Highlights: Stop Missing Out on Microsoft Market Development Funds',
                       'channel': 'The Crancer Group',
                       'author': 'The Crancer Group',
                       'text': "If you're investing in your business, Microsoft is willing to invest with "
                               'you.',
                       'tip': "If you're investing in your business, Microsoft is willing to invest with "
                              'you.',
                       'timestamp': 763,
                       'timestamp_seconds': 763,
                       'timestamp_label': '[00:12:43]',
                       'url': 'https://www.youtube.com/watch?v=dM62o5Vq5U4&t=763s',
                       'markdown': '[00:12:43](https://www.youtube.com/watch?v=dM62o5Vq5U4&t=763s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lET3Wc2a74o',
                       'title': 'Why Channel Partners Don’t Use Market Development Funds (MDF)',
                       'channel': 'ZINFI Technologies, Inc.',
                       'author': 'ZINFI Technologies, Inc.',
                       'text': 'In fact, our worldwide channel survey data shows as much as 60% of market '
                               'development funds are not used on a quarterly basis.',
                       'tip': 'In fact, our worldwide channel survey data shows as much as 60% of market '
                              'development funds are not used on a quarterly basis.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=lET3Wc2a74o&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=lET3Wc2a74o&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gPoVTzxEwPw',
                       'title': 'What are Market Development Funds?',
                       'channel': 'Marketing Business Network',
                       'author': 'Marketing Business Network',
                       'text': 'An approved budget is not automatically a payment.',
                       'tip': 'An approved budget is not automatically a payment.',
                       'timestamp': 44,
                       'timestamp_seconds': 44,
                       'timestamp_label': '[00:00:44]',
                       'url': 'https://www.youtube.com/watch?v=gPoVTzxEwPw&t=44s',
                       'markdown': '[00:00:44](https://www.youtube.com/watch?v=gPoVTzxEwPw&t=44s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YKXY9b__zcA',
                       'title': 'What are Market Development Funds?',
                       'channel': 'Marketing Business Network',
                       'author': 'Marketing Business Network',
                       'text': 'The vendor covers 50% up to $1,000, the costs come to $1,600, so the '
                               'vendor reimburses $800.',
                       'tip': 'The vendor covers 50% up to $1,000, the costs come to $1,600, so the vendor '
                              'reimburses $800.',
                       'timestamp': 61,
                       'timestamp_seconds': 61,
                       'timestamp_label': '[00:01:01]',
                       'url': 'https://www.youtube.com/watch?v=YKXY9b__zcA&t=61s',
                       'markdown': '[00:01:01](https://www.youtube.com/watch?v=YKXY9b__zcA&t=61s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7tcEnD85CE4',
                       'title': 'Channel Partner Recruitment Case Study - Channel Institute',
                       'channel': 'Channel Institute',
                       'author': 'Channel Institute',
                       'text': 'VMware recruits services-oriented partners and no longer requires them to '
                               'sell products outside their core.',
                       'tip': 'VMware recruits services-oriented partners and no longer requires them to '
                              'sell products outside their core.',
                       'timestamp': 149,
                       'timestamp_seconds': 149,
                       'timestamp_label': '[00:02:29]',
                       'url': 'https://www.youtube.com/watch?v=7tcEnD85CE4&t=149s',
                       'markdown': '[00:02:29](https://www.youtube.com/watch?v=7tcEnD85CE4&t=149s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9ijiF4Aas8o',
                       'title': 'Why Most ISVs Get Channel Wrong | Building an Enterprise Software '
                                'Ecosystem',
                       'channel': 'Luasai',
                       'author': 'Luasai',
                       'text': 'Control ultimately still sits with the ISV and the ISV rep.',
                       'tip': 'Control ultimately still sits with the ISV and the ISV rep.',
                       'timestamp': 910,
                       'timestamp_seconds': 910,
                       'timestamp_label': '[00:15:10]',
                       'url': 'https://www.youtube.com/watch?v=9ijiF4Aas8o&t=910s',
                       'markdown': '[00:15:10](https://www.youtube.com/watch?v=9ijiF4Aas8o&t=910s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9ijiF4Aas8o',
                       'title': 'Why Most ISVs Get Channel Wrong | Building an Enterprise Software '
                                'Ecosystem',
                       'channel': 'Luasai',
                       'author': 'Luasai',
                       'text': "You're going from a nine month onboarding process to a three week sales "
                               'cycle if you leverage an existing supplier into an enterprise.',
                       'tip': "You're going from a nine month onboarding process to a three week sales "
                              'cycle if you leverage an existing supplier into an enterprise.',
                       'timestamp': 1385,
                       'timestamp_seconds': 1385,
                       'timestamp_label': '[00:23:05]',
                       'url': 'https://www.youtube.com/watch?v=9ijiF4Aas8o&t=1385s',
                       'markdown': '[00:23:05](https://www.youtube.com/watch?v=9ijiF4Aas8o&t=1385s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_pp2kmBgn7s',
                       'title': 'SaaS Partners & Resellers [Lessons From 30+ Client Projects]',
                       'channel': 'Willingness to Pay',
                       'author': 'Willingness to Pay',
                       'text': 'Fix direct sales first, because a partner is never going to be better at '
                               'selling your product than you are.',
                       'tip': 'Fix direct sales first, because a partner is never going to be better at '
                              'selling your product than you are.',
                       'timestamp': 2823,
                       'timestamp_seconds': 2823,
                       'timestamp_label': '[00:47:03]',
                       'url': 'https://www.youtube.com/watch?v=_pp2kmBgn7s&t=2823s',
                       'markdown': '[00:47:03](https://www.youtube.com/watch?v=_pp2kmBgn7s&t=2823s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KpcTpbw5dho',
                       'title': 'How to Set Up Reseller Partners | PartnerPortal Tutorial',
                       'channel': 'PartnerPortal io',
                       'author': 'PartnerPortal io',
                       'text': "The biggest difference is who collects the customer's money.",
                       'tip': "The biggest difference is who collects the customer's money.",
                       'timestamp': 1,
                       'timestamp_seconds': 1,
                       'timestamp_label': '[00:00:01]',
                       'url': 'https://www.youtube.com/watch?v=KpcTpbw5dho&t=1s',
                       'markdown': '[00:00:01](https://www.youtube.com/watch?v=KpcTpbw5dho&t=1s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6Z4v3jibmMw',
                       'title': '5 Things Every Channel Partner Program Needs',
                       'channel': 'Viktor from Sales',
                       'author': 'Viktor from Sales',
                       'text': 'A 20 to 30% margin usually is not going to be enough.',
                       'tip': 'A 20 to 30% margin usually is not going to be enough.',
                       'timestamp': 1805,
                       'timestamp_seconds': 1805,
                       'timestamp_label': '[00:30:05]',
                       'url': 'https://www.youtube.com/watch?v=6Z4v3jibmMw&t=1805s',
                       'markdown': '[00:30:05](https://www.youtube.com/watch?v=6Z4v3jibmMw&t=1805s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NrZYppqY_R4',
                       'title': 'DW Channel Partner Program Overview',
                       'channel': 'Digital Watchdog',
                       'author': 'Digital Watchdog',
                       'text': 'Enter your distributor information with up to five distribution account '
                               'numbers, then hit Save at the bottom of the My Company tab.',
                       'tip': 'Enter your distributor information with up to five distribution account '
                              'numbers, then hit Save at the bottom of the My Company tab.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=NrZYppqY_R4&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=NrZYppqY_R4&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a299ToKLxRs',
                       'title': "Ooma's Reseller Partner Program",
                       'channel': 'Ooma',
                       'author': 'Ooma',
                       'text': 'Unlike most other programs where payment is slowly doled out over a long '
                               'period of time, Ooma pays the majority upfront.',
                       'tip': 'Unlike most other programs where payment is slowly doled out over a long '
                              'period of time, Ooma pays the majority upfront.',
                       'timestamp': 28,
                       'timestamp_seconds': 28,
                       'timestamp_label': '[00:00:28]',
                       'url': 'https://www.youtube.com/watch?v=a299ToKLxRs&t=28s',
                       'markdown': '[00:00:28](https://www.youtube.com/watch?v=a299ToKLxRs&t=28s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'}]}
