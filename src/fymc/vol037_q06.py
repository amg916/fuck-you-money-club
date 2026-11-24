from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'ucaas-ccaas-resale-zoom-ringcentral-partner-channel',
 'question_prompt': 'Which UCaaS and CCaaS platforms are partners selling, and how do partner programs, '
                    'pricing, integrations, and compliance shape those deals?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'UCaaS and CCaaS Resale: Zoom, RingCentral, and the Partner Channel Opportunity',
 'subtitle': 'RingCentral IGNITE and Zoom channel programs, agentic AI in contact centers, the Gartner '
             'UCaaS Magic Quadrant, Zoom Phone demos, pricing, onboarding, and compliance, CRM '
             'integrations for resellers, AI copilots across Microsoft, Zoom, and Webex, and Zoom Phone vs '
             'RingCentral comparisons',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners selling UCaaS and CCaaS through the partner channel converge on one '
                      'play: the broker or advisor owns the deal, the vendor pays the fee, and the '
                      "customer pays nothing for representation. AeroCom's Mike Smith prices Zoom Phone "
                      'Unlimited below $10 against a $15 list and Metered near $5 against $10, while '
                      "Telarus partners chase a 15x SPIFF on RingCX and RingCentral's Channel Harmony "
                      'limits conflict. Zoom executives size the channel TAM above $200B and push '
                      'dedicated practices, AI voicebots, and bundled security. Contact center features '
                      'are sliding into the base UCaaS license, opening $20-$25 add-on upsells. '
                      "Disagreements are sharp: Brian Nichols attacks RingCentral's Trustpilot and BBB "
                      'record, analysts call Zoom Contact Center a 1.0 product, and full contact center '
                      'pricing is quoted anywhere from $69 to $149 per agent.',
 'key_metrics': [{'label': 'Zoom Phone Unlimited street price',
                  'metric': 'Zoom Phone Unlimited street price',
                  'value': 'Below $10/user/month (sometimes $8-$9) against a $15 list price',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Mike Smith of AeroCom reports what brokered clients pay for the most popular '
                             'Zoom Phone tier versus list.',
                  'source': 'AeroCom Inc ([viRtp8k9GAo @ 00:03:12])'},
                 {'label': 'RingCX partner SPIFF',
                  'metric': 'RingCX partner SPIFF',
                  'value': '15x SPIFF plus increased residuals through year-end',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Brandon Thomas of RingCentral describes the RingCX partner incentive as a '
                             '"crazy amount of money" on the Telarus channel.',
                  'source': 'Telarus ([8ge4I4KL5kQ @ 00:10:59])'},
                 {'label': 'Zoom channel total addressable market',
                  'metric': 'Zoom channel total addressable market',
                  'value': '$200B+ by end of decade',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Zoom Head of Global Channel Mark Jenkins sizes the partner opportunity and '
                             'urges partners to build a dedicated Zoom practice.',
                  'source': 'UC Today News ([dqTXnYdAKdQ @ 00:10:09])'},
                 {'label': 'Customer Engagement Pack vs full contact center',
                  'metric': 'Customer Engagement Pack vs full contact center',
                  'value': '$20/supervisor/month vs $100+/agent/month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'AeroCom demo positions the queue-analytics add-on as a cheap alternative to '
                             'full contact center licensing.',
                  'source': 'AeroCom Inc ([auYElw4sYi8 @ 00:13:34])'}],
 'sections': [{'title': 'The Practitioner Consensus',
               'paragraphs': ['The channel consensus starts with who pays the broker. AeroCom president '
                              'Mike Smith tells buyers flatly, "Don\'t call Zoom directly," and explains '
                              'that the vendor pays the fee, so representation costs the customer nothing '
                              '[viRtp8k9GAo @ 00:00:38]. The AeroCom Zoom Phone review repeats the pitch: '
                              'better-than-direct pricing for organizations of 100 or more users, with the '
                              'provider covering the broker fee and the customer paying $0 [auYElw4sYi8 @ '
                              '00:31:55]. RingCentral runs the same logic through the Telarus channel. '
                              'Brandon Thomas, RingCentral AVP of Partner Success, told Telarus CCO '
                              'Richard Murray that customers with a partner attached stay with RingCentral '
                              'longer [8ge4I4KL5kQ @ 00:04:58], and named limiting channel conflict '
                              "through Channel Harmony as the vendor's number one priority [8ge4I4KL5kQ @ "
                              "00:05:28]. Zoom's channel chief Mark Jenkins pushes the same direction at "
                              'larger scale, sizing the total addressable market at more than $200 billion '
                              'by the end of the decade and urging partners to build a dedicated Zoom '
                              'practice instead of treating Zoom as a side line [dqTXnYdAKdQ @ 00:10:23]. '
                              'Jenkins also counts five to seven or more partners touching a single '
                              'customer, from consultants and solution providers to integrators and MSPs '
                              '[dqTXnYdAKdQ @ 00:10:58]. Across vendors the operator takeaway is '
                              'identical: the partner owns the relationship, the vendor funds the '
                              'commission, and customer stickiness is the asset being sold.',
                              'The second point of agreement is that UCaaS and CCaaS are collapsing into '
                              "one sale. UC Today's David Dungay observed that buying the two together is "
                              'spreading down to mid-market and SMB accounts [dqTXnYdAKdQ @ 00:04:27], and '
                              'Zoom CX chief Chris Moresy told Telarus that CCaaS, CRM, ticketing, '
                              'hyperscalers, UC and CC are converging [-0tioUlVICE @ 00:10:16]. Moresy '
                              "added that Zoom's contact center has passed 1,500 customers, including "
                              'first-time Zoom buyers who purchase contact center only [-0tioUlVICE @ '
                              "00:09:47]. AeroCom's Mike Smith shows the mechanism on the product side: "
                              'queue login and logout, mandatory logout reason codes, and callback in '
                              'queue have moved into the base Zoom Phone license [H1SvYMYWK1o @ 00:03:33], '
                              'while a full contact center seat still runs $70 to $80 or more per user '
                              '[H1SvYMYWK1o @ 00:03:10]. On RingCentral, Brandon Thomas describes RingCX '
                              'as out-of-the-box and easier to implement, with WFM integrations, analytics '
                              'and conversational AI, and a sweet spot of mid-market and below '
                              '[8ge4I4KL5kQ @ 00:11:33]. Thomas also reports partners already closing '
                              'RingCX deals in the last month by pivoting UC sales that carried complex '
                              'analytics requirements [8ge4I4KL5kQ @ 00:12:58]. For a reseller, the phone '
                              'deal is now also a light contact center deal, and every UC conversation is '
                              'a doorway into a CCaaS seat.',
                              'The baseline prerequisites are just as consistent. VoxFlo opens with a '
                              'blunt observation: CRM integration comes up early in every UCaaS and CCaaS '
                              'sale, and without it deals stall, go to a competitor, or require a bespoke '
                              'build costing thousands [Zbk_QOoXQ_M @ 00:00:01]. VoxFlo adds that 79% of '
                              'opportunity data never reaches the CRM and 45% of CRM data is not AI-ready '
                              "[Zbk_QOoXQ_M @ 00:00:25]. Zoom's Mark Jenkins lists the skills a partner "
                              'practice needs: technical depth, consultative selling, support and project '
                              'management, with named gaps in cloud integration, security and compliance, '
                              "and data analytics [dqTXnYdAKdQ @ 00:14:27]. Jenkins points to Zoom's "
                              'self-paced training, UCaaS and CCaaS advisors, boot camps, and '
                              'accreditations up more than 300% year over year to close those gaps '
                              '[dqTXnYdAKdQ @ 00:16:05]. Compliance is the hidden deal-killer in regulated '
                              "accounts. Theta Lake's Anthony Robinson told Zoom architect Patrick Kelly "
                              'that regulated customers switch off team chat, meeting chat and recordings, '
                              'pushing users into other tools and wasting licenses they already pay for '
                              '[CHFSW3MiXcU @ 00:03:53]. Partners who lack depth can borrow it: Richard '
                              'Murray notes Telarus engineers and solution architects can overlay on deals '
                              '[8ge4I4KL5kQ @ 00:09:08]. The prerequisite stack is CRM sync, compliance '
                              'capture, and engineering backup before the first quote goes out.'],
               'table': {'caption': 'Where UCaaS and CCaaS channel practitioners agree',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Vendor-paid broker fee model for Zoom Phone buyers',
                                   'Mike Smith says vendors pay the fee and buyers should never call Zoom '
                                   'directly',
                                   'Lead every pitch with zero-cost representation and better-than-direct '
                                   'pricing for buyers',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:00:38])'],
                                  ['Partner-attached RingCentral customers stay longer than unattached '
                                   'ones',
                                   'Brandon Thomas says RingCentral customers with a partner attached stay '
                                   'longer',
                                   'Sell retention value to the vendor and lean on Channel Harmony '
                                   'protection',
                                   'Telarus ([8ge4I4KL5kQ @ 00:04:58])'],
                                  ['Dedicated vendor practice beats treating Zoom as a side line',
                                   'Mark Jenkins sizes the Zoom channel TAM above $200B by end of decade',
                                   'Build a focused Zoom practice with technical, sales, support, and '
                                   'project skills',
                                   'UC Today News ([dqTXnYdAKdQ @ 00:10:23])'],
                                  ['UCaaS and CCaaS increasingly bought together in smaller accounts',
                                   'David Dungay sees combined buying spreading into mid-market and SMB '
                                   'accounts',
                                   'Quote phone and contact center together instead of as separate '
                                   'projects',
                                   'UC Today News ([dqTXnYdAKdQ @ 00:04:27])'],
                                  ['Contact center features are entering the base UCaaS license',
                                   'Queue login, logout reason codes, and queue callback now ship in base '
                                   'Zoom Phone',
                                   'Use base-license queue features to win light contact center buyers '
                                   'cheaply',
                                   'AeroCom Inc ([H1SvYMYWK1o @ 00:03:33])'],
                                  ['CRM integration decides UCaaS and CCaaS deals very early',
                                   'VoxFlo says missing CRM integration stalls deals or forces builds '
                                   'costing thousands',
                                   'Confirm CRM sync before quoting and revisit deals previously lost on '
                                   'integration',
                                   'WeAreVoxFlo ([Zbk_QOoXQ_M @ 00:00:01])'],
                                  ['Compliance capture unlocks regulated accounts that disable Zoom '
                                   'features',
                                   'Regulated customers disable chat and recordings, wasting licenses they '
                                   'already pay for',
                                   'Pair Zoom with Theta Lake capture so regulated buyers can switch '
                                   'features back on',
                                   'Tattooed Nerd ([CHFSW3MiXcU @ 00:03:53])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["AeroCom's Mike Smith gives the most granular Zoom Phone price sheet. Phone "
                              'Unlimited, the most popular tier, lists at $15 per user per month, and '
                              "Smith's clients land below $10, sometimes at $8 to $9 [viRtp8k9GAo @ "
                              '00:03:12]. Pro Plus lists at $18.32 with clients paying around $14, and '
                              'Business Plus lists at $22.49 with clients near $16 [viRtp8k9GAo @ '
                              '00:02:37]. Metered lists at $10 per user or device, comes in around $5, and '
                              'bills every outbound minute because it includes no usage [viRtp8k9GAo @ '
                              "00:04:29]. Smith's 2026 update notes the base price climbed from $15 to "
                              '$16, though they claim clients pay far less [H1SvYMYWK1o @ 00:01:52]. The '
                              'fee structure is the second weapon. Zoom charges no admin or 911 fee, while '
                              'competitors charge roughly $4 plus $1, or $5 per user per month '
                              '[viRtp8k9GAo @ 00:05:04]. The AeroCom demo states it directly: "Zoom is $5 '
                              'less per month per user than a lot of their competition" [auYElw4sYi8 @ '
                              '00:22:49]. Idle DIDs list at $5 a month and are often negotiated to about '
                              '$1 [viRtp8k9GAo @ 00:08:22], toll-free numbers run $5 per month plus 3.7 '
                              'cents per inbound minute with high-volume users reaching 1.5 to 2 cents, '
                              'and international is billed per country at roughly $20 a month typical '
                              'spend [viRtp8k9GAo @ 00:09:17].',
                              'The upsell ladder sits between the phone seat and a full contact center. '
                              'Smith lists Zoom Contact Center at $69, $99 or $149 per agent per month, '
                              'with discounts of about 25% common [viRtp8k9GAo @ 00:06:12]. Below that '
                              'tier, the Power Pack at $25 per number per month delivers queue analytics '
                              'without contact center licenses and enables SMS on the main number '
                              '[viRtp8k9GAo @ 00:07:07]. In the AeroCom demo the add-on, since renamed the '
                              'Customer Engagement Pack [H1SvYMYWK1o @ 00:12:24], is pitched at $20 per '
                              'supervisor per month against $100 or more per agent for a full contact '
                              'center: "it\'s only $20 per month as an add-on, and it gives you all that '
                              'insight, real-time analytics" [auYElw4sYi8 @ 00:13:34]. Revenue Accelerator '
                              'is the AI upsell Smith calls "the biggest thing," with talk-to-listen '
                              'ratio, talk speed, longest spiel and filler-word tracking against custom '
                              'thresholds such as 50/50 or 85/15 [H1SvYMYWK1o @ 00:05:24]. On RingCentral, '
                              'the money sits in IGNITE and RingCX. Thomas says partners wanted to own the '
                              'sale and asked for speed first, so RingCentral strengthened quoting tools '
                              'and matched compensation to the work [8ge4I4KL5kQ @ 00:07:33]. RingCX '
                              'carries a 15x SPIFF plus increased residuals through year-end, which Thomas '
                              'called a "crazy amount of money" [8ge4I4KL5kQ @ 00:10:59].',
                              'Execution comes down to a few repeatable plays. The AeroCom demo describes '
                              'contract buyouts in which Zoom gives 12 to 15 months of free service, '
                              '"within reason," to pull customers off existing agreements [auYElw4sYi8 @ '
                              '00:23:27]. For Microsoft shops, Thomas says RingCentral has shifted from '
                              'replacing Teams to an additive sale through an embedded dialer or direct '
                              'routing [8ge4I4KL5kQ @ 00:15:08], with no double licensing required '
                              "[8ge4I4KL5kQ @ 00:16:51]. Murray contrasts RingCentral's five 9s with Teams "
                              'at "three9," and Thomas affirms it [8ge4I4KL5kQ @ 00:17:07]. CRM '
                              'integration is outsourced rather than built. VoxFlo supports more than 300 '
                              'CRMs "with no bespoke build and no upfront cost," runs live with '
                              'RingCentral and Zoom Phone, and is white-label [Zbk_QOoXQ_M @ 00:00:47]. '
                              'Its go-to-market script targets recruitment, real estate, legal and '
                              'financial services, reopens deals lost on integration, and closes with: '
                              '"Offer a free 14-day trial for five users" [Zbk_QOoXQ_M @ 00:02:08]. '
                              'Sales-team deployments follow the Zoom Phone and Outreach pattern Brian '
                              'Bolander demonstrated: the admin adds the app from the Marketplace, selects '
                              'it under Settings > Voice, and accepts that the voice setting is '
                              'all-or-none across the whole organization [cHY6UbMTjDA @ 00:02:33]. Reps '
                              'then work sequences with preset dispositions through a Chrome extension '
                              'CTI, and outbound calls are recorded and transcribed [cHY6UbMTjDA @ '
                              '00:09:53].'],
               'table': {'caption': 'Street pricing and partner incentives quoted by channel practitioners',
                         'headers': ['Line Item',
                                     'List or Base Price',
                                     'Street or Negotiated Price',
                                     'Expert Source'],
                         'rows': [['Zoom Phone Unlimited, the most popular single-license tier',
                                   '$15 per user per month at Zoom list price',
                                   'Below $10 per user, sometimes $8 to $9 negotiated',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:03:12])'],
                                  ['Zoom Pro Plus bundle quoted for mid-to-large companies',
                                   '$18.32 per user per month list price quoted',
                                   'Around $14 per user depending on total user count',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:02:19])'],
                                  ['Zoom Metered license with zero included usage minutes',
                                   '$10 per user or device per month list',
                                   'Around $5, with every outbound minute billed separately',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:04:29])'],
                                  ['Zoom Contact Center agent licenses across three tiers',
                                   '$69, $99, or $149 per agent per month',
                                   'Discounts of about 25% off list are common',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:06:12])'],
                                  ['Customer Engagement Pack supervisor analytics add-on for queues',
                                   '$20 per supervisor per month as an add-on',
                                   'Versus $100 or more per agent for full contact center',
                                   'AeroCom Inc ([auYElw4sYi8 @ 00:13:34])'],
                                  ['Idle DIDs and toll-free numbers on Zoom Phone accounts',
                                   '$5 per idle DID; toll-free $5 plus 3.7 cents per minute',
                                   'Idle DIDs near $1; high-volume toll-free at 1.5 to 2 cents',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:08:22])'],
                                  ['RingCX contact center deals sold through the RingCentral partner '
                                   'channel',
                                   '15x SPIFF plus increased residuals through year-end',
                                   "Called a crazy amount of money by RingCentral's Brandon Thomas",
                                   'Telarus ([8ge4I4KL5kQ @ 00:10:59])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the Channel Margin Actually Hides',
                           'body': 'The practitioners make their money on the gap between list and street '
                                   'pricing, on fee stripping, and on stacking vendor incentives on top of '
                                   'add-on upsells.',
                           'items': ['Never let a 100-plus-user buyer go direct; the broker route promises '
                                     'better-than-direct pricing and the provider pays the fee [AeroCom '
                                     'Inc — auYElw4sYi8 @ 00:02:36].',
                                     'Negotiate idle DIDs from the $5 list toward $1 and push high-volume '
                                     'toll-free from 3.7 cents down to 1.5 to 2 cents per inbound minute '
                                     '[AeroCom Inc — viRtp8k9GAo @ 00:08:22].',
                                     'Pivot UC deals stuck on complex analytics requirements into RingCX '
                                     'to capture the 15x SPIFF and increased residuals before year-end '
                                     '[Telarus — 8ge4I4KL5kQ @ 00:12:58].',
                                     "Reopen deals previously lost on CRM integration with VoxFlo's free "
                                     '14-day trial for five users [WeAreVoxFlo — Zbk_QOoXQ_M @ '
                                     '00:02:08].']},
               'sop_steps': [{'step': 1,
                              'title': 'Qualify Seat Count and Fit',
                              'action': 'Target companies from 50 to a few thousand employees and screen '
                                        'out seasonal headcount swings.',
                              'detail': 'Mike Smith targets 50 to a few thousand employees [AeroCom Inc — '
                                        'H1SvYMYWK1o @ 00:00:25], and the AeroCom review flags seasonal '
                                        'user swings as a poor fit because Zoom is not month-to-month '
                                        '[AeroCom Inc — auYElw4sYi8 @ 00:28:43].'},
                             {'step': 2,
                              'title': 'Quote Below List and Strip Fees',
                              'action': 'Price Phone Unlimited under $10 and sell the absence of admin and '
                                        '911 fees.',
                              'detail': "Smith's clients pay below $10 against a $15 list, and Zoom "
                                        'carries no admin or 911 fee versus roughly $5 per user at '
                                        'competitors [AeroCom Inc — viRtp8k9GAo @ 00:05:04].'},
                             {'step': 3,
                              'title': 'Stack the Upsell',
                              'action': 'Attach the $20 Customer Engagement Pack or move complex deals '
                                        'into RingCX for the SPIFF.',
                              'detail': 'The AeroCom demo prices the add-on at $20 per supervisor versus '
                                        '$100+ per agent [AeroCom Inc — auYElw4sYi8 @ 00:13:34], while '
                                        'RingCX pays a 15x SPIFF plus increased residuals [Telarus — '
                                        '8ge4I4KL5kQ @ 00:10:59].'},
                             {'step': 4,
                              'title': 'Lock In CRM and Sales-Tool Integrations',
                              'action': 'Connect the CRM through VoxFlo and configure Outreach under '
                                        'Settings > Voice before go-live.',
                              'detail': 'VoxFlo covers 300+ CRMs with no bespoke build [WeAreVoxFlo — '
                                        'Zbk_QOoXQ_M @ 00:00:47], and the Outreach voice setting applies '
                                        'all-or-none across the organization [Tattooed Nerd — cHY6UbMTjDA '
                                        '@ 00:03:17].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split among brokers is whether to sell a full contact center '
                              "seat at all. AeroCom's demo broker pegs a full contact center at $100 or "
                              'more per agent and steers queue-heavy buyers into the Customer Engagement '
                              'Pack, pitching it as "only $20 per month as an add-on" that exposes '
                              'real-time queue analytics, call length, and declined or unanswered calls '
                              "[auYElw4sYi8 @ 00:13:34]. Mike Smith, AeroCom's president, quotes that same "
                              'full seat at $70 to $80-plus per user and says the gap keeps shrinking '
                              'because queue login and logout, mandatory logout reason codes, and callback '
                              'in queue now ride inside the base UCaaS license [H1SvYMYWK1o @ 00:03:10]. '
                              'In a 2025 pricing walk-through, Smith lists Zoom Contact Center at $69, '
                              '$99, or $149 per agent per month with roughly 25% discounts common, and '
                              'prices the Power Pack at $25 per number per month for queue analytics plus '
                              'SMS on the main number [viRtp8k9GAo @ 00:06:12]. Three price anchors '
                              'circulate from one brokerage, so a reseller quoting a mid-market buyer has '
                              'to decide up front whether the deal is a cheap add-on upsell or a full '
                              'per-agent seat sale before the first proposal goes out.',
                              "Zoom's contact center maturity splits the room. Tutorials By David says "
                              'Zoom Phone "lacks some of the deep contact center features" larger '
                              'businesses need and hands enterprises to RingCentral, which integrates with '
                              'Salesforce and HubSpot but costs more for small teams [iZPzQgYhbHA @ '
                              '00:00:14]. Zeus Kerravala, on the UC Today News panel, calls Zoom Contact '
                              'Center a "pretty good 1.0" that still lacked Salesforce and Zendesk '
                              'integrations when the panel reviewed it [Wcqc4eUu_5o @ 00:22:11]. On the '
                              'other side, Patrick Kelly of Tattooed Nerd presents the contact center as a '
                              'strength, bundling the Video Engagement Center and Solvvy AI on a single '
                              "dashboard [pW6NJcmH21E @ 00:08:35]. Zoom's own CX chief, Chris Moresy, "
                              'counters the immaturity charge with four years in contact center, roughly '
                              '$100M in business at high double-digit growth, and 1,500-plus customers, '
                              'some of them first-time Zoom buyers purchasing contact center only '
                              '[-0tioUlVICE @ 00:09:47]. The playbook fork is clear: resellers chasing '
                              'large enterprise logos with deep CRM workflows lean RingCentral, while '
                              "resellers working existing Zoom accounts and mid-market buyers pitch Zoom's "
                              'contact center as a single-platform add, accepting that analysts and some '
                              'reviewers still grade it below the specialists.',
                              "Microsoft Teams forces another fork. RingCentral's Brandon Thomas, speaking "
                              'on Telarus, says the play has shifted from replacing Teams to an additive '
                              'sale through an embedded dialer or direct routing, with no double licensing '
                              'required [8ge4I4KL5kQ @ 00:15:08]. Thomas also affirms Telarus host Richard '
                              "Murray's framing of RingCentral's five 9s against Teams at three 9s. "
                              "AeroCom's broker takes the opposite line for light phone users already on "
                              'Teams E5 or E7, sending them to Teams Phone via Operator Connect rather '
                              'than forcing a Zoom deal [auYElw4sYi8 @ 00:30:05]. Brian Nichols of CX '
                              'without the BS notes Gartner cut its forecast for calling through office '
                              'suites by 2028 from 90% to 70%, a 20-point retreat [DKzL7oMyWis @ '
                              "00:04:07]. On AI pricing, CallTower's Kade Herbert says Zoom and Webex AI "
                              'are "very free," helping ROI, while Copilot carries a premium, and Madison '
                              'D makes budget a deciding factor because Microsoft means extra licensing '
                              '[YnbZO1fa7BQ @ 00:06:04]. The contrast sets two openings: a '
                              'Teams-coexistence overlay where RingCentral sells beside Microsoft, and a '
                              "cost-displacement pitch where Zoom's bundled AI undercuts Copilot add-on "
                              'spend for buyers who are not locked into Microsoft 365 workflows.'],
               'table': {'caption': 'Contested playbooks for UCaaS and CCaaS resale, side by side',
                         'headers': ['Contested Question',
                                     'Playbook A (Who Argues It)',
                                     'Playbook B (Who Argues It)',
                                     'Expert Source'],
                         'rows': [['Full contact center seat versus add-on analytics pack',
                                   'Sell the $20 per supervisor Customer Engagement Pack instead of '
                                   '$100-plus agent seats',
                                   'Price full Zoom Contact Center at $69, $99, or $149 per agent with '
                                   'roughly 25% discounts',
                                   'AeroCom Inc ([auYElw4sYi8 @ 00:13:34]); AeroCom Inc ([viRtp8k9GAo @ '
                                   '00:06:12])'],
                                  ['Is Zoom Contact Center mature enough for enterprise buyers?',
                                   'Zoom lacks some deep contact center features, and RingCentral suits '
                                   'larger enterprises better',
                                   'Zoom bundles the Video Engagement Center and Solvvy AI on one single '
                                   'dashboard',
                                   'Tutorials By David ([iZPzQgYhbHA @ 00:00:14]); Tattooed Nerd '
                                   '([pW6NJcmH21E @ 00:08:35])'],
                                  ['Replace Microsoft Teams or sell alongside it as an overlay',
                                   'RingCentral now sells additively through embedded dialer or direct '
                                   'routing without double licensing',
                                   'Light phone users on Teams E5 or E7 should take Teams Phone through '
                                   'Operator Connect',
                                   'Telarus ([8ge4I4KL5kQ @ 00:15:08]); AeroCom Inc ([auYElw4sYi8 @ '
                                   '00:30:05])'],
                                  ['Is Zoom AI a selling point or a renewal risk?',
                                   'Gartner flags inconsistent Zoom AI and bundling that raises customer '
                                   'renewal costs over time',
                                   'Revenue Accelerator is "the biggest thing" with talk ratios, Ask AI, '
                                   'and manager dashboards',
                                   'CX without the BS ([DKzL7oMyWis @ 00:03:44]); AeroCom Inc '
                                   '([H1SvYMYWK1o @ 00:04:47])'],
                                  ['Fully autonomous voicebots versus keeping human agents in the loop',
                                   'Klarna fired agents for a 75% expense cut, then partly backtracked on '
                                   'the move',
                                   'Zoom rejects "agents don\'t have a place" and pushes Agent Assist over '
                                   '16 knowledge bases',
                                   'Telarus ([-0tioUlVICE @ 00:05:35]); Telarus ([-0tioUlVICE @ '
                                   '00:06:08])'],
                                  ['Is Zoom pricing simple or a complicated fee ecosystem?',
                                   'No admin fee and no 911 fee saves about $5 per user every month',
                                   'Complex pricing and steep multi-site setups make Zoom hard for '
                                   'first-time admins to run',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:05:04]); LONDON FILM ([ZHjObNVm5_Y @ '
                                   '00:03:42])'],
                                  ['Who owns the customer relationship in the channel model?',
                                   'RingCentral IGNITE lets partners own the sale with SE support and '
                                   'stronger quoting tools',
                                   'ALE partners now own and invoice customers directly, an approach Avaya '
                                   'also took earlier',
                                   'Telarus ([8ge4I4KL5kQ @ 00:07:03]); UC Today News ([Wcqc4eUu_5o @ '
                                   '00:04:09])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Brian Nichols of CX without the BS, who discloses a bias as a Level365 '
                              'seller, opens with the warning that Leader status is no free pass, then '
                              "lays out RingCentral's review gap: 4.2 out of 5 on G2 and Capterra against "
                              '1.8 on Trustpilot across about 2,000 reviews, and roughly 1.06 on BBB with '
                              '596 complaints in three years [DKzL7oMyWis @ 00:01:55]. The complaints '
                              'Nichols cites are exit traps: 16 calls and a 2.5-hour call to cancel, four '
                              'months to close an account, overbilling that took 90 days plus an FCC '
                              'complaint to unwind, and auto-renewal without clear notice [DKzL7oMyWis @ '
                              '00:02:16]. Nichols pitches the inverse at Level365: 100% US-based support, '
                              'month-to-month terms, and no early termination fees [DKzL7oMyWis @ '
                              "00:08:28]. Zoom carries its own lock-in: AeroCom's broker warns that as a "
                              'publicly traded company Zoom rarely releases customers early, is not '
                              'month-to-month, and so misfits companies with seasonal user swings, and it '
                              'is a poor fit for customers who need hand-holding [auYElw4sYi8 @ 00:24:32]. '
                              'For a reseller, the check is the exit clause and the cancellation path, '
                              "because both vendors' terms decide how painful and how slow a customer "
                              'departure becomes.',
                              'Line-item fees surface after signature. Mike Smith of AeroCom warns that '
                              '"every single provider is going to charge you for idle IDs," with Zoom\'s '
                              'base at about $5 per DID per month, often negotiated down to about $1 '
                              "[viRtp8k9GAo @ 00:08:22]. Smith's Metered license at $10 list includes no "
                              'usage, so every outbound minute is billed, and toll-free runs $5 per number '
                              'plus 3.7 cents per inbound minute unless volume earns 1.5 to 2 cents. '
                              "LONDON FILM's review flags that live chat support requires a subscription "
                              'over $10 a month and live phone support requires over $200 a month, and its '
                              'documentation is text-heavy, with fewer screenshots than Nextiva '
                              '[ZHjObNVm5_Y @ 00:02:11]. The same review calls call routing, reports, and '
                              'AI settings "overwhelming" for teams moving off landlines and points them '
                              'toward Ooma or Nextiva when IT support is thin [GA4lZkmVP-w @ 00:09:23]. '
                              'Add-on creep compounds it: polling needs a licensed host on an eligible '
                              'paid plan, Zoom Mate requires extra licensing, and custom Clips branding '
                              "needs Clips Plus. Gartner's flag, relayed by Brian Nichols, is that Zoom's "
                              'bundling raises renewal costs [DKzL7oMyWis @ 00:03:44].',
                              'Integration gaps kill UCaaS and CCaaS deals before pricing even matters. '
                              'WeAreVoxFlo says CRM integration comes up early in every sale and, without '
                              'it, deals stall, go to a competitor, or need a bespoke build "costing '
                              'thousands," while 79% of opportunity data never reaches the CRM and 45% of '
                              'CRM data is not AI-ready [Zbk_QOoXQ_M @ 00:00:25]. Configuration traps '
                              'follow: on Tattooed Nerd, the Zoom Phone and Outreach voice setting is '
                              'all-or-none for the whole organization, and the CTI still requires the Zoom '
                              'client running [cHY6UbMTjDA @ 00:03:17]. In regulated accounts, Theta '
                              "Lake's Anthony Robinson reports customers disabling team chat, meeting "
                              'chat, and recordings, which pushes users to other tools and wastes licenses '
                              "they already pay for [CHFSW3MiXcU @ 00:03:53]. On automation, Zoom's Chris "
                              'Moresy and the Telarus host recount Klarna firing agents, cutting expenses '
                              "75%, then partly unwinding the move, the cautionary tale behind Zoom's "
                              'stance that human agents still have a place [-0tioUlVICE @ 00:05:35]. The '
                              'operator check is to qualify the CRM, compliance archive, and staffing plan '
                              'before quoting a single seat, because each of these failures strands '
                              'licenses the customer is already paying for.'],
               'table': {'caption': 'Firsthand failure modes and the economics check each one demands',
                         'headers': ['Failure Mode',
                                     'What Practitioners Report',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['RingCentral cancellation maze',
                                   '16 calls, 2.5-hour calls to cancel, and four months to close an '
                                   'account',
                                   'Overbilling took 90 days plus an FCC complaint to recover',
                                   'CX without the BS ([DKzL7oMyWis @ 00:02:16])'],
                                  ['Cisco Webex outage remedy cap',
                                   'Webex calling outage remedies are capped at 5% of the monthly fee',
                                   '"5% is not a remedy" for enterprises that live and die by uptime',
                                   'CX without the BS ([DKzL7oMyWis @ 00:03:24])'],
                                  ['NICE plus RingCentral ticket ownership gap',
                                   'Unresolved question of whose queue owns a 9 PM Friday ticket',
                                   'The partner is left holding the ticket when ownership is unclear',
                                   'CX without the BS ([DKzL7oMyWis @ 00:06:07])'],
                                  ['Zoom contract lock-in',
                                   'Publicly traded Zoom rarely releases customers early and is not '
                                   'month-to-month',
                                   'Seasonal headcount swings do not fit a fixed-seat Zoom contract',
                                   'AeroCom Inc ([auYElw4sYi8 @ 00:24:32])'],
                                  ['Idle DIDs and metered minutes',
                                   'Idle DIDs list at $5 per month each, and Metered includes no usage',
                                   'Negotiate idle DIDs toward about $1 and price outbound minutes into '
                                   'Metered quotes',
                                   'AeroCom Inc ([viRtp8k9GAo @ 00:08:22])'],
                                  ['Live support paywall',
                                   'Live chat requires over $10 per month and live phone over $200 per '
                                   'month',
                                   'Small accounts on low tiers fall back to text-heavy documentation',
                                   'LONDON FILM ([GA4lZkmVP-w @ 00:14:48])'],
                                  ['Compliance-driven feature shutdown',
                                   'Regulated customers disable team chat, meeting chat, and recordings '
                                   'entirely',
                                   'Users drift to other tools while paid licenses sit wasted',
                                   'Tattooed Nerd ([CHFSW3MiXcU @ 00:03:53])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before a UCaaS or CCaaS quote goes out',
                           'body': 'Each gate below comes straight from a pitfall a practitioner reported '
                                   'losing deals, money, or customers to.',
                           'items': ['Confirm the CRM integration path before pricing, and run the free '
                                     '14-day trial for five users on deals previously lost to integration '
                                     'gaps [WeAreVoxFlo — Zbk_QOoXQ_M @ 00:02:08].',
                                     'Check exit terms and headcount volatility, since Zoom rarely '
                                     'releases customers early and is not month-to-month [AeroCom Inc — '
                                     'auYElw4sYi8 @ 00:24:32].',
                                     'Verify the support tier the customer will actually get, because chat '
                                     'needs over $10 a month and phone support over $200 a month [LONDON '
                                     'FILM — ZHjObNVm5_Y @ 00:02:11].',
                                     'On integrated NICE plus RingCentral deals, demand proof of '
                                     'integrated workflows, consistent administration, data sharing, and '
                                     'implementation ownership [CX without the BS — DKzL7oMyWis @ '
                                     '00:06:51].']}}],
 'pull_quote': '"For large enterprises that lives and dies by uptime, 5% is not a remedy." — CX without '
               'the BS (DKzL7oMyWis @ 00:03:24).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Route mid-to-large Zoom deals through a broker instead of calling Zoom directly, '
                      'with the broker fee paid by the vendor [AeroCom Inc — viRtp8k9GAo @ 00:00:38].',
                      'Negotiate Zoom Phone Unlimited from the $15 list to below $10 per user, sometimes '
                      '$8 to $9 [AeroCom Inc — viRtp8k9GAo @ 00:03:12].',
                      'Use contract buyouts to pull customers off incumbent providers, with free service '
                      'for 12 to 15 months within reason [AeroCom Inc — auYElw4sYi8 @ 00:23:27].',
                      'Pivot complex-analytics UC sales into RingCX for mid-market and below to capture '
                      'the 15x SPIFF plus increased residuals through year-end [Telarus — 8ge4I4KL5kQ @ '
                      '00:10:59].',
                      'Revisit deals lost on CRM integration with a white-label connector covering '
                      '300-plus CRMs and a free 14-day trial for five users [WeAreVoxFlo — Zbk_QOoXQ_M @ '
                      '00:02:08].',
                      "Bundle security with UCaaS and CCaaS for SMB using Zoom's Palo Alto Networks, "
                      'Zscaler, and Theta Lake integrations [UC Today News — dqTXnYdAKdQ @ 00:09:03].'],
 'statutory_citations': [{'title': 'AeroCom Inc — Zoom Phone Pricing for Mid-Large-Size Companies in 2025 '
                                   '[00:08:22]',
                          'url': 'https://www.youtube.com/watch?v=viRtp8k9GAo&t=502s',
                          'relevance': 'Primary practitioner testimony on Zoom list versus negotiated '
                                       'pricing, idle DID fees, and broker-paid fees.'},
                         {'title': 'CX without the BS — Gartner UCaaS Magic Quadrant 2026 EXPLAINED '
                                   '(Cisco, Microsoft, RingCentral, Zoom) [00:02:16]',
                          'url': 'https://www.youtube.com/watch?v=DKzL7oMyWis&t=136s',
                          'relevance': 'Primary practitioner testimony on RingCentral cancellation '
                                       'complaints, Cisco outage remedies, and Zoom renewal-cost risk.'},
                         {'title': 'Telarus — How RingCentral is Currently Innovating in the Contact '
                                   'Center Space and their IGNITE! Program [00:10:59]',
                          'url': 'https://www.youtube.com/watch?v=8ge4I4KL5kQ&t=659s',
                          'relevance': 'Primary practitioner testimony on RingCX SPIFFs, IGNITE partner '
                                       'ownership, and the Teams additive sale.'},
                         {'title': 'AeroCom Inc — Zoom Phone System (UCaaS) Review & Demo | Hard to Beat '
                                   '[00:24:32]',
                          'url': 'https://www.youtube.com/watch?v=auYElw4sYi8&t=1472s',
                          'relevance': 'Primary practitioner testimony on Zoom contract lock-in, add-on '
                                       'packs, and customer fit.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '8ge4I4KL5kQ',
                       'title': 'How RingCentral is Currently Innovating in the Contact Center Space and '
                                'their IGNITE! Program',
                       'channel': 'Telarus',
                       'author': 'Telarus',
                       'text': 'RingCentral is paying a 15x SPIFF plus increased residuals on RingCX '
                               'through year-end, which is a crazy amount of money.',
                       'tip': 'RingCentral is paying a 15x SPIFF plus increased residuals on RingCX '
                              'through year-end, which is a crazy amount of money.',
                       'timestamp': 659,
                       'timestamp_seconds': 659,
                       'timestamp_label': '[00:10:59]',
                       'url': 'https://www.youtube.com/watch?v=8ge4I4KL5kQ&t=659s',
                       'markdown': '[00:10:59](https://www.youtube.com/watch?v=8ge4I4KL5kQ&t=659s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-0tioUlVICE',
                       'title': 'Understanding Agentic AI in CX- An Executive Interview with Zoom',
                       'channel': 'Telarus',
                       'author': 'Telarus',
                       'text': 'It can take actions on its own.',
                       'tip': 'It can take actions on its own.',
                       'timestamp': 80,
                       'timestamp_seconds': 80,
                       'timestamp_label': '[00:01:20]',
                       'url': 'https://www.youtube.com/watch?v=-0tioUlVICE&t=80s',
                       'markdown': '[00:01:20](https://www.youtube.com/watch?v=-0tioUlVICE&t=80s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DKzL7oMyWis',
                       'title': 'Gartner UCaaS Magic Quadrant 2026 EXPLAINED (Cisco, Microsoft, '
                                'RingCentral, Zoom)',
                       'channel': 'CX without the BS',
                       'author': 'CX without the BS',
                       'text': 'For large enterprises that lives and dies by uptime, 5% is not a remedy.',
                       'tip': 'For large enterprises that lives and dies by uptime, 5% is not a remedy.',
                       'timestamp': 204,
                       'timestamp_seconds': 204,
                       'timestamp_label': '[00:03:24]',
                       'url': 'https://www.youtube.com/watch?v=DKzL7oMyWis&t=204s',
                       'markdown': '[00:03:24](https://www.youtube.com/watch?v=DKzL7oMyWis&t=204s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DKzL7oMyWis',
                       'title': 'Gartner UCaaS Magic Quadrant 2026 EXPLAINED (Cisco, Microsoft, '
                                'RingCentral, Zoom)',
                       'channel': 'CX without the BS',
                       'author': 'CX without the BS',
                       'text': 'See, real support answers the phone and owns the problem.',
                       'tip': 'See, real support answers the phone and owns the problem.',
                       'timestamp': 272,
                       'timestamp_seconds': 272,
                       'timestamp_label': '[00:04:32]',
                       'url': 'https://www.youtube.com/watch?v=DKzL7oMyWis&t=272s',
                       'markdown': '[00:04:32](https://www.youtube.com/watch?v=DKzL7oMyWis&t=272s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Zbk_QOoXQ_M',
                       'title': 'VoxFlo | CRM Integration for UCaaS & CCaaS Resellers #wearevoxflo',
                       'channel': 'WeAreVoxFlo',
                       'author': 'WeAreVoxFlo',
                       'text': 'It supports over 300 CRM with no bespoke build and no upfront cost.',
                       'tip': 'It supports over 300 CRM with no bespoke build and no upfront cost.',
                       'timestamp': 47,
                       'timestamp_seconds': 47,
                       'timestamp_label': '[00:00:47]',
                       'url': 'https://www.youtube.com/watch?v=Zbk_QOoXQ_M&t=47s',
                       'markdown': '[00:00:47](https://www.youtube.com/watch?v=Zbk_QOoXQ_M&t=47s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dqTXnYdAKdQ',
                       'title': 'Zoom Multicast: The Next UC Channel Opportunity',
                       'channel': 'UC Today News',
                       'author': 'UC Today News',
                       'text': 'The channel TAM is $200 billion plus by the end of the decade, and '
                               'partners should build a dedicated Zoom practice.',
                       'tip': 'The channel TAM is $200 billion plus by the end of the decade, and partners '
                              'should build a dedicated Zoom practice.',
                       'timestamp': 609,
                       'timestamp_seconds': 609,
                       'timestamp_label': '[00:10:09]',
                       'url': 'https://www.youtube.com/watch?v=dqTXnYdAKdQ&t=609s',
                       'markdown': '[00:10:09](https://www.youtube.com/watch?v=dqTXnYdAKdQ&t=609s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'auYElw4sYi8',
                       'title': 'Zoom Phone System (UCaaS) Review & Demo | Hard to Beat',
                       'channel': 'AeroCom Inc',
                       'author': 'AeroCom Inc',
                       'text': "So, it's only $20 per month as an add-on, and it gives you all that "
                               'insight, real-time analytics, like you know, how long your calls are, you '
                               'know, in queue, and all kinds of good stuff.',
                       'tip': "So, it's only $20 per month as an add-on, and it gives you all that "
                              'insight, real-time analytics, like you know, how long your calls are, you '
                              'know, in queue, and all kinds of good stuff.',
                       'timestamp': 814,
                       'timestamp_seconds': 814,
                       'timestamp_label': '[00:13:34]',
                       'url': 'https://www.youtube.com/watch?v=auYElw4sYi8&t=814s',
                       'markdown': '[00:13:34](https://www.youtube.com/watch?v=auYElw4sYi8&t=814s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'auYElw4sYi8',
                       'title': 'Zoom Phone System (UCaaS) Review & Demo | Hard to Beat',
                       'channel': 'AeroCom Inc',
                       'author': 'AeroCom Inc',
                       'text': 'So, right away, Zoom is $5 less per month per user than a lot of their '
                               'competition.',
                       'tip': 'So, right away, Zoom is $5 less per month per user than a lot of their '
                              'competition.',
                       'timestamp': 1369,
                       'timestamp_seconds': 1369,
                       'timestamp_label': '[00:22:49]',
                       'url': 'https://www.youtube.com/watch?v=auYElw4sYi8&t=1369s',
                       'markdown': '[00:22:49](https://www.youtube.com/watch?v=auYElw4sYi8&t=1369s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cHY6UbMTjDA',
                       'title': 'Zoom Phone & Outreach Integration - DEMO!',
                       'channel': 'Tattooed Nerd',
                       'author': 'Tattooed Nerd',
                       'text': 'The voice setting is all or none for the whole organization.',
                       'tip': 'The voice setting is all or none for the whole organization.',
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=cHY6UbMTjDA&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=cHY6UbMTjDA&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'H1SvYMYWK1o',
                       'title': "Zoom Phone - What's New in 2026",
                       'channel': 'AeroCom Inc',
                       'author': 'AeroCom Inc',
                       'text': 'The Zoom Phone base price went up from $15 to $16 per user per month.',
                       'tip': 'The Zoom Phone base price went up from $15 to $16 per user per month.',
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=H1SvYMYWK1o&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=H1SvYMYWK1o&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GA4lZkmVP-w',
                       'title': 'ZOOM PHONE EXPERT REVIEW FOR BUSINESSES B2B -COMPLETE PROFESSIONAL '
                                'ANALYSIS',
                       'channel': 'LONDON FILM',
                       'author': 'LONDON FILM',
                       'text': 'Live support access depends on your subscription level.',
                       'tip': 'Live support access depends on your subscription level.',
                       'timestamp': 870,
                       'timestamp_seconds': 870,
                       'timestamp_label': '[00:14:30]',
                       'url': 'https://www.youtube.com/watch?v=GA4lZkmVP-w&t=870s',
                       'markdown': '[00:14:30](https://www.youtube.com/watch?v=GA4lZkmVP-w&t=870s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YnbZO1fa7BQ',
                       'title': 'AI Disruption in UC: Copilot, Zoom & Webex Face Off',
                       'channel': 'UC Today News',
                       'author': 'UC Today News',
                       'text': 'The sky is no longer falling.',
                       'tip': 'The sky is no longer falling.',
                       'timestamp': 128,
                       'timestamp_seconds': 128,
                       'timestamp_label': '[00:02:08]',
                       'url': 'https://www.youtube.com/watch?v=YnbZO1fa7BQ&t=128s',
                       'markdown': '[00:02:08](https://www.youtube.com/watch?v=YnbZO1fa7BQ&t=128s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Wcqc4eUu_5o',
                       'title': 'The Latest Big News on ALE Doubling Down on UCaaS, Enterprise ChatGPT & '
                                "Zoom's AI Companion",
                       'channel': 'UC Today News',
                       'author': 'UC Today News',
                       'text': 'Zoom Contact Center is a pretty good 1.0, but it lacks Salesforce and '
                               'Zendesk integrations.',
                       'tip': 'Zoom Contact Center is a pretty good 1.0, but it lacks Salesforce and '
                              'Zendesk integrations.',
                       'timestamp': 1331,
                       'timestamp_seconds': 1331,
                       'timestamp_label': '[00:22:11]',
                       'url': 'https://www.youtube.com/watch?v=Wcqc4eUu_5o&t=1331s',
                       'markdown': '[00:22:11](https://www.youtube.com/watch?v=Wcqc4eUu_5o&t=1331s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CHFSW3MiXcU',
                       'title': 'Is your Zoom compliance actually secure?',
                       'channel': 'Tattooed Nerd',
                       'author': 'Tattooed Nerd',
                       'text': "We don't hold your data hostage.",
                       'tip': "We don't hold your data hostage.",
                       'timestamp': 1505,
                       'timestamp_seconds': 1505,
                       'timestamp_label': '[00:25:05]',
                       'url': 'https://www.youtube.com/watch?v=CHFSW3MiXcU&t=1505s',
                       'markdown': '[00:25:05](https://www.youtube.com/watch?v=CHFSW3MiXcU&t=1505s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'viRtp8k9GAo',
                       'title': 'Zoom Phone Pricing for Mid-Large-Size Companies in 2025',
                       'channel': 'AeroCom Inc',
                       'author': 'AeroCom Inc',
                       'text': 'My customers will probably pay more around the $14 range, but again, it '
                               'depends on the amount of users you have.',
                       'tip': 'My customers will probably pay more around the $14 range, but again, it '
                              'depends on the amount of users you have.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=viRtp8k9GAo&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=viRtp8k9GAo&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'viRtp8k9GAo',
                       'title': 'Zoom Phone Pricing for Mid-Large-Size Companies in 2025',
                       'channel': 'AeroCom Inc',
                       'author': 'AeroCom Inc',
                       'text': "Every single provider is going to charge you for idle IDs, and that's "
                               "Zoom's base price is about $5 per month per did for idle did.",
                       'tip': "Every single provider is going to charge you for idle IDs, and that's "
                              "Zoom's base price is about $5 per month per did for idle did.",
                       'timestamp': 502,
                       'timestamp_seconds': 502,
                       'timestamp_label': '[00:08:22]',
                       'url': 'https://www.youtube.com/watch?v=viRtp8k9GAo&t=502s',
                       'markdown': '[00:08:22](https://www.youtube.com/watch?v=viRtp8k9GAo&t=502s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pW6NJcmH21E',
                       'title': 'Is Zoom the best UCaaS Platform?',
                       'channel': 'Tattooed Nerd',
                       'author': 'Tattooed Nerd',
                       'text': 'People know Zoom only for meetings.',
                       'tip': 'People know Zoom only for meetings.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=pW6NJcmH21E&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=pW6NJcmH21E&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZHjObNVm5_Y',
                       'title': 'ZOOM PHONE REVIEW - IMPLEMENTATION/ ONBOARDING - CUSTOMER SUPPORT B2B '
                                'BUSINESS EXPERT  ANALYSIS',
                       'channel': 'LONDON FILM',
                       'author': 'LONDON FILM',
                       'text': "Zoom's biggest onboarding advantage is familiarity.",
                       'tip': "Zoom's biggest onboarding advantage is familiarity.",
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=ZHjObNVm5_Y&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=ZHjObNVm5_Y&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iZPzQgYhbHA',
                       'title': "Zoom Phone VS RingCentral in 2026 (What's Better?)",
                       'channel': 'Tutorials By David',
                       'author': 'Tutorials By David',
                       'text': 'Zoom Phone lacks some of the deep contact center features that larger '
                               'businesses need.',
                       'tip': 'Zoom Phone lacks some of the deep contact center features that larger '
                              'businesses need.',
                       'timestamp': 14,
                       'timestamp_seconds': 14,
                       'timestamp_label': '[00:00:14]',
                       'url': 'https://www.youtube.com/watch?v=iZPzQgYhbHA&t=14s',
                       'markdown': '[00:00:14](https://www.youtube.com/watch?v=iZPzQgYhbHA&t=14s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
