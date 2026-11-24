from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'q9-working-with-and-around-medicaid-brokers',
 'question_prompt': 'How do Medicaid NEMT brokers work, how do I get in network, and how do I protect '
                    'myself from broker tactics?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Working With (and Around) Medicaid Brokers',
 'subtitle': 'Finding and inquiring with brokers, the four broker payment models (fee-for-service, '
             "capitation, MCO, hybrid), broker lists, Modivcare's NC takeover, Georgia's 2.1M-ride award, "
             'the $200K loss and $75K MTM fines case, contract and service agreement terms, renewal '
             'retaliation, VA third-party contract traps, and operating out of network',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Medicaid brokers sit between state Medicaid money and the van owner. They collect '
                      'the full reimbursement and subpay providers a lower number. Nemiton puts that '
                      'spread at 15-35%, and WholeRoute says 60-80% gets taken out. MJ Business Academy, '
                      'WholeRoute, Nemiton and Joel Davis of UMTPG agree that broker trips are easy to '
                      'get, cheap, and dangerous to depend on. The street mechanics include inquiry forms '
                      'resubmitted weekly, calls to the broker before applying, credentialing windows of '
                      '21-45 days, and mileage-bucket rates from a $7.23 base up to a $55-70 wheelchair '
                      'base. Davis negotiates hard, in writing only, and pushes email-only correspondence, '
                      'cherry-picked trips and out-of-network leverage. Christopher Buell and Six Figure '
                      "Transportation's Eric skip brokers almost entirely. Nemiton models a 70/30 "
                      'broker/private hybrid that adds about $6,000 a month.',
 'key_metrics': [{'label': 'Broker Spread Over Provider Pay',
                  'metric': 'Broker Spread Over Provider Pay',
                  'value': '15-35%, equal to $15,000-18,750 per year on a 3-vehicle fleet',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "The broker receives the state's full Medicaid reimbursement rate and subpays "
                             'the provider at a lower number.',
                  'source': 'Nemiton ([LjAb-IUYxbM @ 00:01:11])'},
                 {'label': 'Hybrid Mix Revenue Uplift',
                  'metric': 'Hybrid Mix Revenue Uplift',
                  'value': '$14,200-18,900 per month at a 70/30 broker/private mix vs $8,700-11,300 at '
                           '100% broker',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Private pay at $35-85 per trip carries a 63-285% premium over broker rates; '
                             'expect a 60-90 day ramp.',
                  'source': 'Nemiton ([LjAb-IUYxbM @ 00:08:35])'},
                 {'label': 'First-Year Failure Rate of Contract Holders',
                  'metric': 'First-Year Failure Rate of Contract Holders',
                  'value': 'Only half of applicants get a contract; 70% of those are out of business in '
                           'year one',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Applies to the broker application pipeline, where 80-85% of applicants are '
                             'first-time business owners.',
                  'source': 'WholeRoute ([rLXiXIWHxIA @ 00:02:01])'},
                 {'label': 'Re-Credentialing Failure After Broker Switch',
                  'metric': 'Re-Credentialing Failure After Broker Switch',
                  'value': 'About 30% of providers fail to re-credential in time',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Reported around the Georgia handover, where Verida takes all 5 regions on '
                             'April 1, 2026 and ModivCare exits.',
                  'source': 'Nemt University ([zXw7440bths @ 00:06:26])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus: Brokers Are Volume at a Discount, Never the '
                          'Foundation',
               'paragraphs': ["A Medicaid broker is the middleman between the state's Medicaid money and "
                              'the provider who actually runs the van, and every practitioner here '
                              'describes the same economics [0nJ9GYcr744 @ 00:01:21]. Nemiton lays it out '
                              "plainly: the broker receives the state's full Medicaid reimbursement rate "
                              'and subpays the provider at a lower number. That spread runs 15-35%, which '
                              'works out to $15,000-18,750 a year on a 3-vehicle fleet [LjAb-IUYxbM @ '
                              '00:01:11]. Jay at WholeRoute puts the cut even higher. Statistically, he '
                              'says, 60 to 80% gets taken out before the provider sees a dollar '
                              '[rLXiXIWHxIA @ 00:03:12]. Joel Davis of UMTPG adds the piece most newcomers '
                              'miss: the broker still gets paid for trips that are not performed, and the '
                              'provider does not. Cancellations and no-shows therefore become free money '
                              "on the broker's side of the ledger [Bvcsc1hEgT0 @ 00:12:00]. In the same "
                              'breakdown Davis describes the payment chain. The true guaranteed payer is '
                              'the government, and the government guarantees it will pay the broker. The '
                              'broker never guarantees it will pay you. He tells providers to negotiate '
                              'no-show pay whenever they have the leverage. The shared conclusion is that '
                              'broker work is real, steady volume, but it is priced at a structural '
                              'discount. A broker is a pipe for trips, not a partner, and operators who '
                              'treat it as anything more get squeezed.',
                              'The second point of agreement is that brokers should be a slice of the '
                              'business, never the foundation. Jasmine and Monica of MJ Business Academy '
                              'tell new owners to keep brokers to a small share of revenue, because '
                              'brokers themselves can lose their health-plan contracts and take your '
                              'volume with them [KSSO5Igfn2Y @ 00:09:55]. Jay at WholeRoute sizes the '
                              'broker at "maybe 15 maybe 20%" of potential revenue and uses website and '
                              'community-rider math to fill the rest [rLXiXIWHxIA @ 00:20:22]. Nemiton '
                              'calls broker concentration the number one hidden risk in NEMT [LjAb-IUYxbM '
                              '@ 00:13:47]. Joel Davis supplies the casualties. One client lost about '
                              '$185K after buying the wrong vehicles on bad advice and is still waiting on '
                              'about $45K from ModivCare. A second client faces an MTM audit claiming $75K '
                              'on disputed trips worth roughly $20K, plus a demand for flat rates. Both '
                              'were 100% broker-dependent [A2vs7pLblSk @ 00:12:13]. Davis calls these '
                              'agreements "sharecropping" and says Medicaid-heavy companies carry the '
                              'lowest resale value in NEMT. His fix is to keep using the existing Medicaid '
                              'cash flow while signing direct-pay contracts with hospitals, SNFs and '
                              'schools. Everyone who addresses the question lands in the same place: take '
                              'the broker money, but plan your exit away from it from day one.',
                              'The baseline prerequisites are the same on every channel. Nemt University '
                              'lists an NPI from cms.gov, an EIN, and an LLC or corporation as the entry '
                              'ticket before any broker conversation [0nJ9GYcr744 @ 00:04:31]. Nemt '
                              'University also splits the landscape into four models [iihLkCuH8NY @ '
                              '00:01:12]:\n'
                              '- In-house state management on fee-for-service, which the speaker calls '
                              '"the best one." Examples: Michigan, Pennsylvania and Minnesota.\n'
                              '- MCO managed care, where trips need prior approval that owners dislike.\n'
                              '- Statewide or regional brokers that centralize call centers, eligibility '
                              'and authorization. Examples: Ohio, North Carolina, South Carolina, '
                              'Louisiana and Texas.\n'
                              '- Mixed county-by-county models such as Philadelphia County.\n'
                              'Nemiton opens its own breakdown with a warning: if you signed a broker '
                              'contract without knowing which of the four models you operate under, you do '
                              "not know your business [LjAb-IUYxbM @ 00:00:00]. Georgia's transition to "
                              'Verida shows what full broker requirements look like in practice. They '
                              'include GAMMIS enrollment, a Type 2 NPI, and $1M auto plus $1M general '
                              'liability per occurrence with Verida and DCH named as additional insureds. '
                              'Vehicles must be 2016 or newer, lift-equipped and GPS-tracked. Drivers must '
                              'clear a 3-year MVR, FBI fingerprints, and HIPAA, ADA, CPR and first aid '
                              'training [zXw7440bths @ 00:07:31]. Nemt University also sees consolidation '
                              'coming, with brokers shrinking toward 3 national players.'],
               'table': {'caption': 'Where the practitioners agree on Medicaid broker economics and '
                                    'dependence',
                         'headers': ['Consensus Point',
                                     'What the Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Broker keeps a large spread on every trip',
                                   'Broker receives full state Medicaid rate and subpays providers 15-35% '
                                   'lower',
                                   'Price your fleet knowing you never see the full Medicaid rate',
                                   'Nemiton ([LjAb-IUYxbM @ 00:01:11])'],
                                  ['Total haircut can be far larger than expected',
                                   'Statistically 60 to 80% of what Medicaid pays gets taken out',
                                   'Treat broker revenue as a thin-margin filler for empty time slots',
                                   'WholeRoute ([rLXiXIWHxIA @ 00:03:12])'],
                                  ['Brokers should be a small revenue share',
                                   'Brokers can lose their health-plan contracts, so keep exposure small',
                                   'Build facility and private-pay accounts before broker volume grows '
                                   'large',
                                   'MJ Business Academy ([KSSO5Igfn2Y @ 00:09:55])'],
                                  ['Broker dependence destroys owners who go all in',
                                   'Two clients at 100% broker faced $45K unpaid and a $75K audit',
                                   'Never let one broker control your cash flow or your survival',
                                   'United Medical Transportation Providers Group ([A2vs7pLblSk @ '
                                   '00:12:13])'],
                                  ['Single-payer concentration must be capped as fleets grow',
                                   'At 11+ vehicles run full hybrid with no payer above 60%',
                                   'Track payer mix monthly and diversify as each vehicle is added',
                                   'Nemiton ([LjAb-IUYxbM @ 00:12:41])'],
                                  ['Entry paperwork is the same everywhere',
                                   'NPI from cms.gov, EIN, and an LLC or corporation before applying',
                                   'Complete the entity and NPI setup before contacting any broker at all',
                                   'Nemt University ([0nJ9GYcr744 @ 00:04:31])'],
                                  ['Broker market is consolidating fast',
                                   'Brokers are consolidating toward 3 national players as states switch '
                                   'contracts',
                                   'Expect re-credentialing whenever a state hands regions to a new broker',
                                   'Nemt University ([zXw7440bths @ 00:15:25])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers: Getting In, Pricing, and Operating on '
                          'Your Terms',
               'paragraphs': ['Getting onto a broker panel is a paperwork grind with a sales layer on top. '
                              "MJ Business Academy's workflow is simple. Go to each broker's website, "
                              'click the inquiry tab, and fill out the questionnaire. Pre-launch owners '
                              'can describe themselves as a current provider ("you have two vehicles") '
                              '[KSSO5Igfn2Y @ 00:01:33]. Expect a reply in 5-7 business days listing the '
                              'required documents. If nothing comes back, resubmit every week, because '
                              'inquiries get lost [KSSO5Igfn2Y @ 00:03:35]. Jay at WholeRoute insists you '
                              'call the broker before you apply and ask three questions [rLXiXIWHxIA @ '
                              '00:12:49]:\n'
                              '1. Are you accepting providers, and what is the trip volume?\n'
                              '2. What vehicle types do you need?\n'
                              '3. What are the insurance requirements?\n'
                              'On the application, list a routing or dispatch software and present your '
                              'driving experience competitively, though Jay says not to lie. Have a '
                              'website ready, because half of brokers require one. Plan for a long '
                              'timeline. Jay budgets about 3 months to get in. In one Florida case, a '
                              'provider with 2 ambulatory vehicles was asked for 4 wheelchair vehicles '
                              'after waiting 4 months. Only half of applicants get a contract at all '
                              '[rLXiXIWHxIA @ 00:11:48]. Brokers mostly add providers when enrollment '
                              'rises. A provider exit creating a vacuum is a "1%" case, and 80-85% of '
                              'applicants are first-time owners competing against established taxi fleets.',
                              'Rates are where, in MJ Business Academy\'s words, "the battle starts." '
                              'Never accept the first offer, and keep pushing until the broker says "final '
                              'final offer" [KSSO5Igfn2Y @ 00:05:52]. Broker pay comes in mileage buckets. '
                              'Trips of 0-3 miles start around $12, rates climb to $26-27 on longer '
                              'buckets, and an ambulatory 5-mile round trip lands around "30 something '
                              '40." Wheelchair pays more than ambulatory. The low end is brutal. The '
                              'Southeast Trans sheet Joel Davis reviewed set ambulatory at a $7.23 base '
                              'with 6 miles included and $1.32 a mile after, and wheelchair at a $17 base '
                              'with 6 miles included and $1.48 a mile after [v-IpSBjauKY @ 00:03:12]. A '
                              'ModivCare holdout in the same video was paid a 14 base and $1.65 a mile '
                              'ambulatory, and an 18 base and $1.85 a mile wheelchair, with no increase '
                              'since 2019. Georgia under Verida pays more. Ambulatory runs $28-35 base '
                              'plus $1.35-1.85 a mile, and wheelchair $55-70 base plus $2.75 a mile. '
                              'Private facility rates there are $65 ambulatory and $95 wheelchair. Verida '
                              'pays net 21 to net 30 and audits heavily in the first 90 days [zXw7440bths '
                              "@ 00:11:35]. For rate reviews, Nemiton's leverage list is an on-time rate "
                              'above 95%, a low no-show rate, a review request at 6 months, and a push for '
                              'multi-year terms [LjAb-IUYxbM @ 00:14:39].',
                              'How you behave inside a broker relationship matters as much as the rate. '
                              'Davis and his UMTPG team insist that all correspondence with ModivCare go '
                              'by email. Brokers push for phone calls because it is part of their '
                              'training, and calls leave no paper trail [0Z6CsGngipI @ 00:02:44]. Davis '
                              'plays deliberately hard to get over email. He calls the broker a "pet '
                              'alligator": you can be friendly with it, but it is not your friend. He '
                              'advises staying out of network unless the margin is good. One '
                              'out-of-network operator shows the payoff. Brokers offered to raise that '
                              "operator's rates, Access2Care offered to remove the mileage cap on "
                              'stretcher rates, and MTM put a credit card on file for a dialysis client '
                              '[xx3dHh731rY @ 00:05:46]. That operator runs about 10 vehicles at '
                              "seven-figure revenue and roughly 50% margin, against Davis's target of "
                              'about 25%. Inside the network, Davis says to cherry-pick and skip the '
                              'losing trips [Bvcsc1hEgT0 @ 00:14:51]. Brokers police providers in return. '
                              "MTM Michigan's rules [Bvcsc1hEgT0 @ 00:04:14]:\n"
                              '- No quoting on trips; only Schedule A rates apply.\n'
                              '- Every vendor no-show gets a follow-up call.\n'
                              '- More than 5 complaints a month triggers a call.\n'
                              '- Turn-backs are reviewed daily, and capacity is cut.\n'
                              '- High numbers for over 2 months lead to a corrective action plan, then '
                              'termination.\n'
                              'Davis also warns never to depend on broker software, because brokers '
                              'eventually lose their contracts.'],
               'table': {'caption': 'Broker onboarding steps, rate sheets and negotiation levers with '
                                    'exact figures',
                         'headers': ['Mechanic / Rate Item',
                                     'Exact Number or Step',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Broker inquiry form response window',
                                   'Reply listing required documents arrives in 5-7 business days',
                                   'Resubmit the inquiry every single week until a reply arrives',
                                   'MJ Business Academy ([KSSO5Igfn2Y @ 00:03:35])'],
                                  ['Pre-application broker phone call',
                                   'Ask about provider intake, trip volume, vehicle types, and insurance '
                                   'requirements',
                                   'Call before applying so the fleet matches what the broker needs',
                                   'WholeRoute ([rLXiXIWHxIA @ 00:12:49])'],
                                  ['Mileage-bucket broker pay ladder',
                                   '0-3 miles starts near $12 and climbs up to $26-27',
                                   'Never accept the first offer; push for the final final offer',
                                   'MJ Business Academy ([KSSO5Igfn2Y @ 00:06:49])'],
                                  ['Southeast Trans low-ball rate sheet',
                                   'Ambulatory $7.23 base, 6 miles included, then $1.32 per mile',
                                   'Decline and stop replying when the volume-for-rates question comes '
                                   'back',
                                   'United Medical Transportation Providers Group ([v-IpSBjauKY @ '
                                   '00:03:12])'],
                                  ['Verida Georgia broker rates and terms',
                                   'Wheelchair $55-70 base plus $2.75 per mile, paid net 21-30',
                                   'Start in Central or Southwest regions because Atlanta is oversaturated',
                                   'Nemt University ([zXw7440bths @ 00:11:35])'],
                                  ['Credentialing timeline after applying to Verida',
                                   'Credentialing takes 21 to 45 days with heavy 90-day audits',
                                   'Hold enough cash reserves to cover the credentialing gap and audit '
                                   'period',
                                   'Nemt University ([zXw7440bths @ 00:13:33])'],
                                  ['Rate review negotiation levers',
                                   'On-time rate above 95%, low no-shows, request review at 6 months',
                                   'Expect volume guarantees instead of raises; push for multi-year '
                                   'contracts',
                                   'Nemiton ([LjAb-IUYxbM @ 00:14:39])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the Veterans Work the Broker Without Getting Eaten',
                           'body': 'These moves come straight from operators who have negotiated, '
                                   'declined, or worked outside broker contracts. Each one protects '
                                   'margin, leverage, or the paper trail.',
                           'items': ['Keep every broker exchange in writing. Brokers push for phone calls '
                                     'because it is part of their training, so stay off the phones and '
                                     'correspond by email [United Medical Transportation Providers Group — '
                                     '0Z6CsGngipI @ 00:04:36].',
                                     'If the broker reaches out first, you are "in the driver\'s seat." '
                                     'Play hard to get over email and work out of network unless the '
                                     'margin is good [United Medical Transportation Providers Group — '
                                     '0Z6CsGngipI @ 00:06:21].',
                                     'Pick software that integrates with brokers instead of running on '
                                     'theirs. RouteGenie integrates with MTM, ModivCare and Access2Care '
                                     '[Nemiton — LjAb-IUYxbM @ 00:16:01].',
                                     'Use social services as a side door. Vance County Social Services '
                                     'needs providers and pays more than ModivCare, and working directly '
                                     'with social services usually means better rates [Motivational '
                                     'Charles — BCwbkTt30cY @ 00:03:57].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the entity and identifiers',
                              'action': 'Form the LLC or corporation, pull the EIN, and register the NPI '
                                        'before any broker contact.',
                              'detail': 'Nemt University lists an NPI from cms.gov, an EIN, and an LLC or '
                                        'corporation as the prerequisites for partnering with brokers '
                                        '[Nemt University — 0nJ9GYcr744 @ 00:04:31].'},
                             {'step': 2,
                              'title': 'Call first, then submit the inquiry',
                              'action': 'Ask each broker about provider intake, trip volume, vehicle types '
                                        'and insurance, then file the inquiry form.',
                              'detail': 'Jay says to call the broker before you apply and ask the three '
                                        'qualifying questions. MJ Business Academy then has you fill out '
                                        'the inquiry tab and resubmit weekly if there is no reply '
                                        '[WholeRoute — rLXiXIWHxIA @ 00:12:49].'},
                             {'step': 3,
                              'title': 'Negotiate the rate sheet in writing',
                              'action': 'Reject the first offer, push to the final final offer, and keep '
                                        'every exchange on email.',
                              'detail': 'Rate negotiation is "when the battle starts." Never accept the '
                                        'first offer, and keep the correspondence on email to preserve the '
                                        'paper trail [MJ Business Academy — KSSO5Igfn2Y @ 00:05:52].'},
                             {'step': 4,
                              'title': 'Run performance numbers and request a review',
                              'action': 'Hold on-time above 95% and no-shows low, then request a rate '
                                        'review at 6 months.',
                              'detail': 'Nemiton names on-time performance and a low no-show rate as the '
                                        'levers, with a rate review at 6 months and a push for multi-year '
                                        'contracts [Nemiton — LjAb-IUYxbM @ 00:14:39].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether a broker belongs in the business at all. '
                              'Christopher Buell grew one company to about 10 vans in roughly four years '
                              'and a second to about 8 vans in roughly two and a half years, predominantly '
                              'without brokers, and calls the DHS-to-broker bidding setup in that state '
                              'totally not worth it; the preferred move is collecting payment on the spot '
                              'and handing the client a receipt to submit to their insurance [HxtN-7tsjNA '
                              '@ 00:05:27]. Eric at Six Figure Transportation does not work with brokers '
                              'at all, steering into skilled nursing facilities where 5 to 10 percent of '
                              'residents are temporary rehab patients who become private-pay riders on '
                              'automatic after discharge [zyo_6OZNupU @ 00:02:15]. The middle camp keeps '
                              'the broker but shrinks it. Jasmine and Monica tell owners to keep brokers a '
                              'small share of revenue because brokers can lose their health-plan contracts '
                              '[KSSO5Igfn2Y @ 00:09:55], while Joel Davis tells fully broker-dependent '
                              'clients to leverage existing Medicaid cash flow as the bankroll for '
                              'direct-pay hospital, SNF, and school contracts instead of walking away cold '
                              '[A2vs7pLblSk @ 00:33:56]. The real choice is how much runway the private '
                              'book has before broker money dries up, not which camp sounds tougher.',
                              'Practitioners also split on how loud to negotiate. Jasmine and Monica treat '
                              'rate talks as the moment when the battle starts: never accept the first '
                              'offer, keep pushing until the broker says final final offer, and expect '
                              'mileage buckets that open near $12 for 0 to 3 miles and climb to $26 or $27 '
                              '[KSSO5Igfn2Y @ 00:05:52]. Joel Davis plays it colder. The Davis rule is he '
                              'who speaks first loses, and when a welcome packet forces you to show retail '
                              'prices first, you come in strong [gJ4V8yGqCFY @ 00:00:43]. With brokers '
                              'specifically, Davis runs a deliberate hard-to-get email strategy and keeps '
                              'every exchange in writing, because brokers are trained to pull providers '
                              'onto the phone where no paper trail exists [0Z6CsGngipI @ 00:04:36]. '
                              'Nemiton offers a data-driven third path: walk in with an on-time rate above '
                              '95 percent and a low no-show rate, request a rate review after six months, '
                              'push for multi-year terms, and expect some brokers to counter with volume '
                              'guarantees instead of higher per-trip pay [LjAb-IUYxbM @ 00:14:39]. The '
                              'tradeoff is visible: the push-hard camp chases rate bumps on the call, '
                              'while the paper-trail camp protects the provider when a later audit or '
                              'penalty dispute lands.',
                              'Where to plug in is the third fault line. Nemt University ranks the '
                              'in-house model, where the State Medicaid agency administers NEMT '
                              'fee-for-service, as the best one, naming Michigan, Pennsylvania, and '
                              'Minnesota, and notes owners do not like the prior approvals that come with '
                              'MCO work [iihLkCuH8NY @ 00:01:12]. Nemiton instead maps payers to fleet '
                              'size: one to three vehicles run FFS in tier-1 states or MCO in tier-3 '
                              'states, four to ten vehicles stack MCO with private pay, and eleven-plus go '
                              'full hybrid with no single payer above 60 percent [LjAb-IUYxbM @ 00:12:41]. '
                              'Joel Davis pushes the out-of-network route unless broker margin is good, '
                              'pointing to clients who operate out of network yet still hold a broker '
                              'credit card on file, while conceding the play fails in markets saturated '
                              'with independents [0Z6CsGngipI @ 00:06:21]. Motivational Charles, boxed out '
                              'because North Carolina Social Services enrollment is closed and ModivCare '
                              'holds all the PHP plans, is emailing Vance County Social Services because '
                              'it needs providers and pays more than ModivCare [BCwbkTt30cY @ 00:03:57]. '
                              'Same goal, four different doors: state FFS, model-matched contracts, '
                              'out-of-network leverage, or county-direct billing, and each depends on what '
                              'the local market actually allows.'],
               'table': {'caption': 'Competing broker playbooks side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Should a broker be in the revenue mix at all',
                                   'Skip brokers entirely and build private pay from SNF rehab discharges '
                                   'on automatic',
                                   'Keep brokers as a small slice, maybe 15 to 20 percent of potential '
                                   'revenue',
                                   'Six Figure Transportation ([zyo_6OZNupU @ 00:02:15]); WholeRoute '
                                   '([rLXiXIWHxIA @ 00:20:22])'],
                                  ['How hard to push on the first rate offer',
                                   'Never accept the first offer and keep pushing until you hear final '
                                   'final offer',
                                   'He who speaks first loses, so stay quiet and come in strong when '
                                   'forced',
                                   'MJ Business Academy ([KSSO5Igfn2Y @ 00:05:52]); United Medical '
                                   'Transportation Providers Group ([gJ4V8yGqCFY @ 00:00:43])'],
                                  ['Phone calls versus written broker correspondence',
                                   'Brokers push for phone calls to win providers over without leaving any '
                                   'record',
                                   'Stay off the phones and correspond through email so a paper trail '
                                   'exists',
                                   'United Medical Transportation Providers Group ([0Z6CsGngipI @ '
                                   '00:02:44])'],
                                  ['Which payer model to target first',
                                   'State in-house fee-for-service management ranked as the best one '
                                   'available to providers',
                                   'Match the model to fleet size, with no single payer above 60 percent',
                                   'Nemt University ([iihLkCuH8NY @ 00:01:12]); Nemiton ([LjAb-IUYxbM @ '
                                   '00:12:41])'],
                                  ['In-network versus out-of-network operation',
                                   'Operate out of network unless the broker margin is genuinely good '
                                   'enough',
                                   'Out-of-network play is not possible in markets saturated with '
                                   'independent providers',
                                   'United Medical Transportation Providers Group ([0Z6CsGngipI @ '
                                   '00:06:21]); United Medical Transportation Providers Group '
                                   '([0Z6CsGngipI @ 00:08:10])'],
                                  ['Third-party contract managers on VA hospital work',
                                   'Bid directly on SAM.gov to cut out management firms paying pennies on '
                                   'the dollar',
                                   'Not against fair third parties, but do your research before signing '
                                   'anything',
                                   'The Travae Willis Transportation Channel ([YFWOnVDBziM @ 00:04:05]); '
                                   'The Travae Willis Transportation Channel ([YFWOnVDBziM @ 00:04:40])'],
                                  ['Whether ambulatory broker trips are worth running',
                                   'Ambulatory is a waste of time and the least profitable of three modes',
                                   'Georgia ambulatory pays $28 to $35 base plus $1.35 to $1.85 per mile',
                                   'United Medical Transportation Providers Group ([xx3dHh731rY @ '
                                   '00:15:05]); Nemt University ([zXw7440bths @ 00:11:35])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure is total broker dependence. Joel Davis walked '
                              'through a client who lost about $185K after buying the wrong vehicles on '
                              'bad advice and is still waiting on roughly $45K from ModivCare, alongside a '
                              'second client whose MTM audit claims $75K owed on disputed trips worth '
                              'about $20K while demanding flat rates; Davis calls broker agreements '
                              'sharecropping and notes both clients were 100 percent broker-dependent '
                              '[A2vs7pLblSk @ 00:09:40]. A taxi company turned NEMT provider running 25 to '
                              '40 legs a day across 50 counties with LogistiCare got the same verdict: the '
                              'house is completely built on sand [xx3dHh731rY @ 00:20:18]. Davis also '
                              'warns against leaning on broker software, because brokers eventually lose '
                              'their contracts and a provider wired into their systems collapses with them '
                              '[Bvcsc1hEgT0 @ 00:06:22]. Nemt University puts a number on that churn: '
                              'Verida takes all five Georgia regions on April 1, 2026 as ModivCare exits, '
                              'and about 30 percent of providers fail to re-credential in time after a '
                              'broker switch, with credentialing alone taking 21 to 45 days [zXw7440bths @ '
                              '00:06:26]. The check is blunt: if one broker transition or one audit letter '
                              'can choke cash flow, broker share is too high.',
                              'The second trap is signing or renewing at rates that cannot carry the '
                              'truck. Davis showed a Southeast Trans offer a provider was pushed to sign '
                              'on January 12: ambulatory at a $7.23 base with six miles included and $1.32 '
                              'per mile after, wheelchair at $17 base with the same six miles and $1.48 '
                              'per mile [v-IpSBjauKY @ 00:03:12]. A ModivCare holdout on 14 base at $1.65 '
                              'per mile had seen no increase since 2019 despite gas and labor costs, had '
                              'done no hospital or nursing-home outreach in that stretch, and now faced a '
                              'late-renewal penalty of up to $2,500 a month [v-IpSBjauKY @ 00:20:18]. '
                              'Travae Willis reports North Carolina insurance rising about 40 percent and '
                              'companies going out of business because of it, so the advice is stay small '
                              'and price trips to cover insurance [YFWOnVDBziM @ 00:08:10]. Under all of '
                              'it sits the leakage brokers keep: they get paid for trips that are not '
                              'performed while the provider does not, which is why Davis says to negotiate '
                              'no-show pay whenever you hold leverage [Bvcsc1hEgT0 @ 00:12:00]. Run the '
                              'per-trip math against insurance, fuel, and driver cost before the '
                              'signature, not after the first quarter.',
                              'The third cluster is launch and operating mistakes that kill new entrants. '
                              "WholeRoute's Jay says only half of applicants land a broker contract and 70 "
                              'percent of those are out of business within the first year, with 80 to 85 '
                              'percent of new applicants being first-time business owners competing '
                              'against established taxi fleets [rLXiXIWHxIA @ 00:02:01]. Davis warns off '
                              'both ends of the vehicle market, new vans at $80K to $100K-plus and $5K '
                              "clunkers, after a client's $185K loss tied to the wrong vehicles "
                              '[A2vs7pLblSk @ 00:13:31]. On the VA side, Travae Willis says the callers '
                              'asking about your van count and rates are usually management firms with no '
                              'vans that win the SAM.gov bid and pay pennies on the dollar, and that even '
                              'a seasoned operator with about 18 vans could not handle a roughly '
                              '20,000-trip-a-year contract [YFWOnVDBziM @ 00:06:44]. Once inside a broker '
                              'network, enforcement bites: the MTM Michigan letter bans trip quoting, '
                              'triggers calls at more than five complaints a month, reviews turn-backs '
                              'daily, and moves high numbers lasting over two months to a corrective '
                              'action plan and then termination [Bvcsc1hEgT0 @ 00:12:50]. Capacity, '
                              'vehicles, and metrics have to be squared before chasing volume.'],
               'table': {'caption': 'Firsthand broker failure modes and the check that catches each one',
                         'headers': ['Failure Mode',
                                     'Reported Damage or Number',
                                     'Operator Check',
                                     'Expert Source'],
                         'rows': [['Total dependence on one or two Medicaid brokers',
                                   'About $185K lost, $45K owed by ModivCare, $75K MTM audit claim',
                                   'Use existing Medicaid cash flow to build direct-pay facility contracts '
                                   'now',
                                   'United Medical Transportation Providers Group ([A2vs7pLblSk @ '
                                   '00:09:40]); United Medical Transportation Providers Group '
                                   '([A2vs7pLblSk @ 00:33:56])'],
                                  ['Broker contract loss and statewide transition',
                                   'About 30 percent of providers fail to re-credential after a broker '
                                   'switch',
                                   'Start credentialing immediately because it takes 21 to 45 days to '
                                   'clear',
                                   'Nemt University ([zXw7440bths @ 00:06:26]); Nemt University '
                                   '([zXw7440bths @ 00:13:33])'],
                                  ['Below-cost Southeast Trans rate sheet pushed for signature',
                                   '$7.23 ambulatory base with six included miles and $1.32 per mile after',
                                   'Decline the sheet and do not answer volume-for-rate fishing questions '
                                   'in writing',
                                   'United Medical Transportation Providers Group ([v-IpSBjauKY @ '
                                   '00:03:12]); United Medical Transportation Providers Group '
                                   '([v-IpSBjauKY @ 00:16:04])'],
                                  ['Stale ModivCare rates and a missed renewal deadline',
                                   'No rate increase since 2019 and a late penalty up to $2,500 monthly',
                                   'Run hospital and nursing-home outreach instead of waiting on broker '
                                   'renewals',
                                   'United Medical Transportation Providers Group ([v-IpSBjauKY @ '
                                   '00:20:18])'],
                                  ['Insurance cost spike crushing per-trip margin',
                                   'North Carolina insurance up about 40 percent with companies closing '
                                   'over it',
                                   'Stay small and price every single trip to cover the insurance load',
                                   'The Travae Willis Transportation Channel ([YFWOnVDBziM @ 00:08:10])'],
                                  ['Newcomers undercutting negotiated broker rates',
                                   'Hundreds of new entrants accept $12 to $15 trips and scraps',
                                   'Hold negotiated rates and refuse scraps rather than chasing raw trip '
                                   'volume',
                                   'MJ Business Academy ([KSSO5Igfn2Y @ 00:11:02]); The Travae Willis '
                                   'Transportation Channel ([YFWOnVDBziM @ 00:09:31])'],
                                  ['MTM performance enforcement escalating to termination',
                                   'Over five complaints monthly triggers calls, then corrective action, '
                                   'then termination',
                                   'Track complaints, turn-backs, and vendor no-shows daily against broker '
                                   'thresholds',
                                   'United Medical Transportation Providers Group ([Bvcsc1hEgT0 @ '
                                   '00:12:50])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Before You Sign or Renew With a Broker',
                           'body': 'Every item below comes from a provider who already paid for skipping '
                                   'it. Clear all four before the signature goes on a broker agreement or '
                                   'renewal.',
                           'items': ['Broker share check: if one broker is 100 percent of revenue, you are '
                                     'in the same seat as the clients who lost about $185K and faced a '
                                     '$75K MTM audit claim [United Medical Transportation Providers Group '
                                     '— A2vs7pLblSk @ 00:12:13].',
                                     'Paper trail check: every broker exchange on rates, renewals, and '
                                     'disputes goes by email, never phone, so you have a paper trail '
                                     '[United Medical Transportation Providers Group — 0Z6CsGngipI @ '
                                     '00:22:59].',
                                     'Re-credential check: the moment a broker switch is announced, start '
                                     'credentialing, because about 30 percent of providers miss the window '
                                     '[Nemt University — zXw7440bths @ 00:06:26].',
                                     'Vehicle cash check: put vehicles and capital equipment in a separate '
                                     'entity that leases them to the NEMT business, and buy future '
                                     'vehicles in cash after P&L and cash-flow review [United Medical '
                                     'Transportation Providers Group — v-IpSBjauKY @ 00:34:28].']}}],
 'pull_quote': "The true guaranteed payer is the government, and the government guarantees they're gonna "
               "pay the broker, but the broker doesn't guarantee that they're always gonna pay you. — "
               'United Medical Transportation Providers Group (Bvcsc1hEgT0 @ 00:11:13).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Call the broker before applying and ask whether they are accepting providers, the '
                      'trip volume, the vehicle types needed, and the insurance requirements [WholeRoute — '
                      'rLXiXIWHxIA @ 00:12:49].',
                      'Fill out the broker inquiry questionnaire, expect a document list in 5 to 7 '
                      'business days, and resubmit every week if no reply arrives [MJ Business Academy — '
                      'KSSO5Igfn2Y @ 00:03:35].',
                      'Move all broker correspondence to email and refuse phone-based negotiation so every '
                      'rate and dispute has a paper trail [United Medical Transportation Providers Group — '
                      '0Z6CsGngipI @ 00:04:36].',
                      'Back every rate request with an on-time rate above 95 percent and a low no-show '
                      'rate, and request a rate review after six months [Nemiton — LjAb-IUYxbM @ '
                      '00:14:39].',
                      'Cherry-pick trips, refuse loser trips, and negotiate paid no-shows whenever you '
                      'hold leverage [United Medical Transportation Providers Group — Bvcsc1hEgT0 @ '
                      '00:14:51].',
                      'Get out from behind the desk and visit facilities in person to land direct service '
                      'agreements outside the broker [United Medical Transportation Providers Group — '
                      '0Z6CsGngipI @ 00:20:37].'],
 'statutory_citations': [{'title': 'United Medical Transportation Providers Group — Lost Almost $200k '
                                   'Starting NEMT, Waiting on $45k from Modivcare, being "fined" $75k by '
                                   'MTM - Hijinks [00:12:13]',
                          'url': 'https://www.youtube.com/watch?v=A2vs7pLblSk&t=733s',
                          'relevance': 'Primary practitioner testimony on the losses, unpaid balances, and '
                                       'audit claims hitting 100 percent broker-dependent providers.'},
                         {'title': 'Nemiton — NEMT Broker Payment Models Explained: Fee-for-Service, '
                                   'Capitation, MCO & Hybrid [00:13:47]',
                          'url': 'https://www.youtube.com/watch?v=LjAb-IUYxbM&t=827s',
                          'relevance': 'Primary practitioner testimony on broker concentration risk, '
                                       'payment models, and fleet-size payer mix.'},
                         {'title': 'United Medical Transportation Providers Group — NEMT Provider?  '
                                   'Dealing with Brokers?  This is a MUST See! [00:11:13]',
                          'url': 'https://www.youtube.com/watch?v=Bvcsc1hEgT0&t=673s',
                          'relevance': 'Primary practitioner testimony on MTM enforcement rules, unpaid '
                                       'no-shows, and broker payment risk.'},
                         {'title': 'United Medical Transportation Providers Group — How Modivcare Treats '
                                   "Providers Who Don't Renew their Contracts - More Laughable Broker "
                                   'Tactics! [00:20:18]',
                          'url': 'https://www.youtube.com/watch?v=v-IpSBjauKY&t=1218s',
                          'relevance': 'Primary practitioner testimony on renewal penalties, stale rates, '
                                       'and below-cost broker rate sheets.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'KSSO5Igfn2Y',
                       'title': 'Step-by-Step Guide to Finding NEMT Brokers',
                       'channel': 'MJ Business Academy',
                       'author': 'MJ Business Academy',
                       'text': 'Rate negotiation is when the battle starts, so never accept the first '
                               'offer and keep pushing until you hear final final offer.',
                       'tip': 'Rate negotiation is when the battle starts, so never accept the first offer '
                              'and keep pushing until you hear final final offer.',
                       'timestamp': 352,
                       'timestamp_seconds': 352,
                       'timestamp_label': '[00:05:52]',
                       'url': 'https://www.youtube.com/watch?v=KSSO5Igfn2Y&t=352s',
                       'markdown': '[00:05:52](https://www.youtube.com/watch?v=KSSO5Igfn2Y&t=352s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iihLkCuH8NY',
                       'title': 'WHAT ARE THE 4 DIFFERENT TYPES OF NEMT BROKER MODELS (🤐Explained)',
                       'channel': 'Nemt University',
                       'author': 'Nemt University',
                       'text': 'In-house management, where the State Medicaid agency administers NEMT on a '
                               'fee-for-service basis, is the best one.',
                       'tip': 'In-house management, where the State Medicaid agency administers NEMT on a '
                              'fee-for-service basis, is the best one.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=iihLkCuH8NY&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=iihLkCuH8NY&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HxtN-7tsjNA',
                       'title': 'How to sell NEMT Brokers',
                       'channel': 'NEMT Sales is now NEMT-Alliance.',
                       'author': 'NEMT Sales is now NEMT-Alliance.',
                       'text': 'Medicaid money goes to DHS, which bids it out to brokers, and that is '
                               'totally not worth it.',
                       'tip': 'Medicaid money goes to DHS, which bids it out to brokers, and that is '
                              'totally not worth it.',
                       'timestamp': 327,
                       'timestamp_seconds': 327,
                       'timestamp_label': '[00:05:27]',
                       'url': 'https://www.youtube.com/watch?v=HxtN-7tsjNA&t=327s',
                       'markdown': '[00:05:27](https://www.youtube.com/watch?v=HxtN-7tsjNA&t=327s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LjAb-IUYxbM',
                       'title': 'NEMT Broker Payment Models Explained: Fee-for-Service, Capitation, MCO & '
                                'Hybrid',
                       'channel': 'Nemiton',
                       'author': 'Nemiton',
                       'text': 'Broker concentration is the number one hidden risk in NEMT.',
                       'tip': 'Broker concentration is the number one hidden risk in NEMT.',
                       'timestamp': 827,
                       'timestamp_seconds': 827,
                       'timestamp_label': '[00:13:47]',
                       'url': 'https://www.youtube.com/watch?v=LjAb-IUYxbM&t=827s',
                       'markdown': '[00:13:47](https://www.youtube.com/watch?v=LjAb-IUYxbM&t=827s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LjAb-IUYxbM',
                       'title': 'NEMT Broker Payment Models Explained: Fee-for-Service, Capitation, MCO & '
                                'Hybrid',
                       'channel': 'Nemiton',
                       'author': 'Nemiton',
                       'text': "They receive the state's full Medicaid reimbursement rate, and they subpay "
                               'you at a lower number.',
                       'tip': "They receive the state's full Medicaid reimbursement rate, and they subpay "
                              'you at a lower number.',
                       'timestamp': 54,
                       'timestamp_seconds': 54,
                       'timestamp_label': '[00:00:54]',
                       'url': 'https://www.youtube.com/watch?v=LjAb-IUYxbM&t=54s',
                       'markdown': '[00:00:54](https://www.youtube.com/watch?v=LjAb-IUYxbM&t=54s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zyo_6OZNupU',
                       'title': '4 ways to get paid with NEMT!!!',
                       'channel': 'Six Figure Transportation',
                       'author': 'Six Figure Transportation',
                       'text': 'I do not work with brokers at all.',
                       'tip': 'I do not work with brokers at all.',
                       'timestamp': 135,
                       'timestamp_seconds': 135,
                       'timestamp_label': '[00:02:15]',
                       'url': 'https://www.youtube.com/watch?v=zyo_6OZNupU&t=135s',
                       'markdown': '[00:02:15](https://www.youtube.com/watch?v=zyo_6OZNupU&t=135s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gJ4V8yGqCFY',
                       'title': "Let's Talk About Your Non-Emergency Medical Transportation Contracts and "
                                'Service Agreements',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'He who speaks first loses.',
                       'tip': 'He who speaks first loses.',
                       'timestamp': 43,
                       'timestamp_seconds': 43,
                       'timestamp_label': '[00:00:43]',
                       'url': 'https://www.youtube.com/watch?v=gJ4V8yGqCFY&t=43s',
                       'markdown': '[00:00:43](https://www.youtube.com/watch?v=gJ4V8yGqCFY&t=43s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0nJ9GYcr744',
                       'title': '(WATCH LIST👀) NEMT LIST OF BROKERS TO PARTNER WITH💡',
                       'channel': 'Nemt University',
                       'author': 'Nemt University',
                       'text': 'Before partnering with a broker you need an NPI, an EIN, and an LLC or '
                               'corporation.',
                       'tip': 'Before partnering with a broker you need an NPI, an EIN, and an LLC or '
                              'corporation.',
                       'timestamp': 271,
                       'timestamp_seconds': 271,
                       'timestamp_label': '[00:04:31]',
                       'url': 'https://www.youtube.com/watch?v=0nJ9GYcr744&t=271s',
                       'markdown': '[00:04:31](https://www.youtube.com/watch?v=0nJ9GYcr744&t=271s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'BCwbkTt30cY',
                       'title': 'Modivcare To Soon Take Over Most Of Medicaid NEMT in NC #NEMT '
                                '#transportation',
                       'channel': 'Motivational Charles',
                       'author': 'Motivational Charles',
                       'text': 'Vance County Social Services needs providers and pays more than ModivCare, '
                               'so I am emailing them.',
                       'tip': 'Vance County Social Services needs providers and pays more than ModivCare, '
                              'so I am emailing them.',
                       'timestamp': 237,
                       'timestamp_seconds': 237,
                       'timestamp_label': '[00:03:57]',
                       'url': 'https://www.youtube.com/watch?v=BCwbkTt30cY&t=237s',
                       'markdown': '[00:03:57](https://www.youtube.com/watch?v=BCwbkTt30cY&t=237s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zXw7440bths',
                       'title': '🚨GEORGIA HANDS ONE COMPANY 2.1 MILLION MEDICAID RIDES🚗',
                       'channel': 'Nemt University',
                       'author': 'Nemt University',
                       'text': 'About 30 percent of providers fail to re-credential in time after a broker '
                               'switch.',
                       'tip': 'About 30 percent of providers fail to re-credential in time after a broker '
                              'switch.',
                       'timestamp': 386,
                       'timestamp_seconds': 386,
                       'timestamp_label': '[00:06:26]',
                       'url': 'https://www.youtube.com/watch?v=zXw7440bths&t=386s',
                       'markdown': '[00:06:26](https://www.youtube.com/watch?v=zXw7440bths&t=386s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A2vs7pLblSk',
                       'title': 'Lost Almost $200k Starting NEMT, Waiting on $45k from Modivcare, being '
                                '"fined" $75k by MTM - Hijinks',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'The MTM audit claims $75K owed on disputed trips worth about $20K, and '
                               'broker agreements are sharecropping.',
                       'tip': 'The MTM audit claims $75K owed on disputed trips worth about $20K, and '
                              'broker agreements are sharecropping.',
                       'timestamp': 580,
                       'timestamp_seconds': 580,
                       'timestamp_label': '[00:09:40]',
                       'url': 'https://www.youtube.com/watch?v=A2vs7pLblSk&t=580s',
                       'markdown': '[00:09:40](https://www.youtube.com/watch?v=A2vs7pLblSk&t=580s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A2vs7pLblSk',
                       'title': 'Lost Almost $200k Starting NEMT, Waiting on $45k from Modivcare, being '
                                '"fined" $75k by MTM - Hijinks',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'Both of these clients were 100 percent broker-dependent.',
                       'tip': 'Both of these clients were 100 percent broker-dependent.',
                       'timestamp': 733,
                       'timestamp_seconds': 733,
                       'timestamp_label': '[00:12:13]',
                       'url': 'https://www.youtube.com/watch?v=A2vs7pLblSk&t=733s',
                       'markdown': '[00:12:13](https://www.youtube.com/watch?v=A2vs7pLblSk&t=733s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0Z6CsGngipI',
                       'title': "Let's Talk Movidcare and Associated Broker Tactics, Facility Contracts, "
                                'Agreements, and More!',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'Stay off the phones with the brokers, the brokers want you on the phone, '
                               "it's part of their training, this is literally what they're trained.",
                       'tip': 'Stay off the phones with the brokers, the brokers want you on the phone, '
                              "it's part of their training, this is literally what they're trained.",
                       'timestamp': 276,
                       'timestamp_seconds': 276,
                       'timestamp_label': '[00:04:36]',
                       'url': 'https://www.youtube.com/watch?v=0Z6CsGngipI&t=276s',
                       'markdown': '[00:04:36](https://www.youtube.com/watch?v=0Z6CsGngipI&t=276s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xx3dHh731rY',
                       'title': 'Medicaid Brokers - the Benefits and Possibilities of Working Out of '
                                'Network and Not Being Dependent!',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'Ambulatory is a waste of time, we want multiples, we want increased '
                               'capacity.',
                       'tip': 'Ambulatory is a waste of time, we want multiples, we want increased '
                              'capacity.',
                       'timestamp': 905,
                       'timestamp_seconds': 905,
                       'timestamp_label': '[00:15:05]',
                       'url': 'https://www.youtube.com/watch?v=xx3dHh731rY&t=905s',
                       'markdown': '[00:15:05](https://www.youtube.com/watch?v=xx3dHh731rY&t=905s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YFWOnVDBziM',
                       'title': 'VA hospital Contracts',
                       'channel': 'The Travae Willis Transportation Channel',
                       'author': 'The Travae Willis Transportation Channel',
                       'text': 'You carry the insurance, the breakdowns, the fuel and the drivers.',
                       'tip': 'You carry the insurance, the breakdowns, the fuel and the drivers.',
                       'timestamp': 434,
                       'timestamp_seconds': 434,
                       'timestamp_label': '[00:07:14]',
                       'url': 'https://www.youtube.com/watch?v=YFWOnVDBziM&t=434s',
                       'markdown': '[00:07:14](https://www.youtube.com/watch?v=YFWOnVDBziM&t=434s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Bvcsc1hEgT0',
                       'title': 'NEMT Provider?  Dealing with Brokers?  This is a MUST See!',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'The true guaranteed payer is the government, and the government guarantees '
                               "they're gonna pay the broker, but the broker doesn't guarantee that "
                               "they're always gonna pay you.",
                       'tip': 'The true guaranteed payer is the government, and the government guarantees '
                              "they're gonna pay the broker, but the broker doesn't guarantee that they're "
                              'always gonna pay you.',
                       'timestamp': 673,
                       'timestamp_seconds': 673,
                       'timestamp_label': '[00:11:13]',
                       'url': 'https://www.youtube.com/watch?v=Bvcsc1hEgT0&t=673s',
                       'markdown': '[00:11:13](https://www.youtube.com/watch?v=Bvcsc1hEgT0&t=673s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rLXiXIWHxIA',
                       'title': 'Medicaid NEMT - everything you need to know about brokers before you get '
                                'started',
                       'channel': 'WholeRoute',
                       'author': 'WholeRoute',
                       'text': 'And then 70% of them that get the contract are out of business in the '
                               'first year.',
                       'tip': 'And then 70% of them that get the contract are out of business in the first '
                              'year.',
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=rLXiXIWHxIA&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=rLXiXIWHxIA&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v-IpSBjauKY',
                       'title': "How Modivcare Treats Providers Who Don't Renew their Contracts - More "
                                'Laughable Broker Tactics!',
                       'channel': 'United Medical Transportation Providers Group',
                       'author': 'United Medical Transportation Providers Group',
                       'text': 'The penalty phase for being late is up to $2,500 per month.',
                       'tip': 'The penalty phase for being late is up to $2,500 per month.',
                       'timestamp': 1218,
                       'timestamp_seconds': 1218,
                       'timestamp_label': '[00:20:18]',
                       'url': 'https://www.youtube.com/watch?v=v-IpSBjauKY&t=1218s',
                       'markdown': '[00:20:18](https://www.youtube.com/watch?v=v-IpSBjauKY&t=1218s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
