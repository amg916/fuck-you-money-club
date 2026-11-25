from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'nsa-idr-operations-final-rule-tma-litigation-congressional-fixes',
 'question_prompt': 'How are the IDR Operations Final Rule, court rulings, and pending legislation '
                    'changing access, batching, fees, and timing for disputing parties?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'The Shifting Rulebook: IDR Operations Final Rule, TMA Litigation, and Congressional Fixes',
 'subtitle': 'New federal IDR portal, batching limits, administrative and entity fees, November 1, 2026 '
             'deadline changes for radiology, TMA III ruling impacts, Pallone and Cassidy proposals, payer '
             'and TPA reality checks, and competing reform agendas from Georgetown CHIR, Paragon, and '
             'hospital coalitions',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': "Payer, provider, and policy practitioners agree that the No Surprises Act's patient "
                      'protections work. IDR is where the system broke: 17,000 expected disputes became '
                      'more than 2.6 million, a handful of repeat filers including HaloMD drive most of '
                      'the volume, and providers win roughly 85 to 88 percent of determinations. The May '
                      '28, 2026 operations final rule changes the plumbing, not the substance. The CMS '
                      'administrative fee drops from $115 to $15 per party. Batches are capped at 50 line '
                      'items for open negotiations starting on or after November 1, 2026. Non-initiating '
                      'parties must respond by business day 15. A 30-business-day cooling-off period now '
                      'feeds a four-business-day filing window with no grace period, and unregistered '
                      'plans default at the offer stage. Practitioners split on whether the batch cap rose '
                      'from 25 or from unlimited, and on whether the rule fixes anything that matters.',
 'key_metrics': [{'label': 'Provider Win Rate in IDR Determinations (Jan-Jun 2025)',
                  'metric': 'Provider Win Rate in IDR Determinations (Jan-Jun 2025)',
                  'value': 'About 88% providers vs. 12% plans',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Brady Bazar's read of CMS data for January to June 2025. The prevailing "
                             'offer also exceeded the QPA in about 88% of determinations.',
                  'source': 'The Phia Group, LLC ([ksxW878eWWk @ 00:07:44])'},
                 {'label': 'CMS Non-Refundable Administrative Fee Per Party',
                  'metric': 'CMS Non-Refundable Administrative Fee Per Party',
                  'value': '$115 cut to $15 per party ($30 total), effective June 11, 2026',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "HaloMD's breakdown of the IDR operations final rule. HaloMD says it "
                             'initiates about 22% of IDR disputes.',
                  'source': 'HaloMD ([of6CD7esHY0 @ 00:02:33])'},
                 {'label': 'Batch Cap for Open Negotiations Starting On or After Nov 1, 2026',
                  'metric': 'Batch Cap for Open Negotiations Starting On or After Nov 1, 2026',
                  'value': 'Exactly 50 line items per batched dispute',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Xpert Billing Talk's radiology batching briefing. Older single, bundled, and "
                             'batch disputes keep the prior rules.',
                  'source': 'Xpert Billing Talk ([g3C-DoM_9CI @ 00:00:45])'},
                 {'label': 'Disputes Initiated Through the IDR Portal (Jan-Jun 2025)',
                  'metric': 'Disputes Initiated Through the IDR Portal (Jan-Jun 2025)',
                  'value': '1,186,812 disputes, 39% above H2 2024, 81% initiated by providers or their '
                           'representatives',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Brady Bazar's walkthrough of CMS IDR volume data for TPAs.",
                  'source': 'The Phia Group, LLC ([ksxW878eWWk @ 00:02:28])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus: Protections Work, IDR Broke, and the '
                        'Rulebook Keeps Moving',
               'paragraphs': ['Across payer, provider, and policy camps, the starting point is the same: '
                              'the patient-protection half of the No Surprises Act works, and the '
                              "arbitration half is where the money leaks. Brian O'Hara of The Phia Group "
                              "says the law 'really did accomplish its goal of preventing surprise balance "
                              "bills' and argues that reform should not weaken those protections "
                              '[8QIP4F1EGTA @ 00:01:47]. The volume numbers explain why IDR became the '
                              'battlefield for every stakeholder. Kenna Watts at the Center on Health '
                              'Insurance Reforms puts 2025 IDR costs above $16 billion, roughly 3.5 times '
                              'the prior year. The expectation was 17,000 disputes; the actual count was '
                              'more than 2.6 million, or upward of 7,000 a day [wJkWOgxZj6k @ 00:10:12]. '
                              "Paragon's panel lands in the same zone with different counting: a "
                              '22,000-per-year estimate versus 258,000 merit line items in 2023 and 4.2 '
                              'million in 2025, about 5.7 million counting every dispute [PpfXacIXrAc @ '
                              "00:11:31]. O'Hara adds the business-model read: a few provider groups have "
                              'turned IDR into routine revenue-cycle management rather than an exception '
                              'process [8QIP4F1EGTA @ 00:05:07]. The numbers disagree on scale, but nobody '
                              'on either side argues that the original forecast survived contact with the '
                              'market. That volume is the baseline every workflow change now has to '
                              'absorb.',
                              'The second point of consensus is that a small set of repeat filers drives '
                              'the machine and wins most of the time. Watts reports that five provider '
                              'groups file roughly three-quarters of all disputes: four private-equity '
                              'staffing groups plus HaloMD. The staffing groups win 90 to 96 percent, '
                              'awards run 6 to 10 times the median in-network rate, and up to $1.4 billion '
                              'has gone to contingency fees [wJkWOgxZj6k @ 00:12:03]. HaloMD does not '
                              'dodge its footprint. Its own leadership says the firm initiates about 22 '
                              'percent of IDR disputes and operates in all 50 states [of6CD7esHY0 @ '
                              '00:00:32]. Brady Bazar of The Phia Group, working from CMS data for January '
                              'to June 2025, puts provider wins at about 88 percent of determinations and '
                              'plan wins at 12 percent. The prevailing offer landed above the QPA in about '
                              '88 percent of cases [ksxW878eWWk @ 00:07:44]. Paragon tracks the trend '
                              'line: provider win rates of 82.1 percent in 2023 and 85.2 percent in 2025. '
                              'In Major League Baseball arbitration, the format members believed would '
                              'force reasonable offers, players win 45 percent and owners 55 percent '
                              '[PpfXacIXrAc @ 00:12:43]. Whichever dataset an operator trusts, the payer '
                              'side loses the large majority of determinations, and the filers on the '
                              'other side are concentrated and still growing every year.',
                              'The third point of consensus is that the rulebook keeps shifting and the '
                              'newest federal rule changes the plumbing, not the substance. KLGates '
                              'describes the final rule issued May 28, 2026 by HHS, Labor, Treasury, and '
                              'OPM as operational rather than substantive. It was driven by the hundreds '
                              'of thousands of claims filed since 2022, far more than the agencies '
                              'anticipated [NwapzBNojY0 @ 00:00:39]. Katie Johnson of the American '
                              "Benefits Council calls the rules an 'initial step' that took years to "
                              'finalize. Johnson says substantial further improvement and oversight are '
                              "needed and that the rules miss 'the most egregious areas of abuse' "
                              '[30BDiubQ0cg @ 00:00:59]. Underneath the rule, the courts keep rewriting '
                              "the math. The Zelis speaker puts it bluntly: 'litigation continues to kind "
                              "of steer the policy.' TMA3 on QPA calculation is unresolved, and CMS "
                              'typically follows major rulings with guidance 6 to 12 months later '
                              '[D63N2KsthY8 @ 00:05:52]. Ron Howrigan of Fulcrum Strategies reports that '
                              'Judge Kernodle sided with TMA on every QPA calculation point and vacated '
                              'the guidance. TMA lost on disclosure because the statute is not '
                              'prescriptive there, which leaves CMS deference, and Howrigan scores the '
                              "outcome a 'triple' [f9Q5ImwNeS0 @ 00:09:18]. Any team running eligibility, "
                              'QPA, or payment workflows is working against a target that moves with each '
                              'ruling and each guidance cycle.'],
               'table': {'caption': 'Where payer, provider, and policy practitioners land on the same side '
                                    'of the IDR fight',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Patient protections succeeded while the IDR arbitration machinery '
                                   'broke down',
                                   "O'Hara says the law accomplished its goal of preventing surprise "
                                   'balance bills to patients',
                                   'The reform fight targets arbitration mechanics, not the '
                                   'balance-billing ban members rely on',
                                   'The Phia Group, LLC ([8QIP4F1EGTA @ 00:01:47])'],
                                  ['Dispute volume ran orders beyond the original federal forecast',
                                   'Expected 17,000 disputes became more than 2.6 million, over 7,000 '
                                   'filed per day',
                                   'Budget fees, staffing, and deadline tracking for multi-million annual '
                                   'dispute volume',
                                   'Center on Health Insurance Reforms ([wJkWOgxZj6k @ 00:10:12])'],
                                  ['A few repeat filers drive a large share of all IDR volume',
                                   'HaloMD, Team Health, and SCP Health accounted for 44 percent of '
                                   'disputes in H1 2025',
                                   'Payer teams build dashboards that flag repeat initiators and their '
                                   'filing patterns',
                                   'The Phia Group, LLC ([ksxW878eWWk @ 00:02:53])'],
                                  ['Providers win the large majority of merit determinations every year',
                                   'Provider win rates measured at 82.1 percent in 2023 and 85.2 percent '
                                   'in 2025',
                                   'Payers enter most disputes expecting to lose, so award size drives '
                                   'real exposure',
                                   'Paragon Health Institute ([PpfXacIXrAc @ 00:12:43])'],
                                  ['Awards land far above in-network benchmarks for plans and participants',
                                   'Median determinations exceed 450 percent of the median in-network '
                                   'rate, per Johnson',
                                   'Employers see the gap flow straight into plan costs and participant '
                                   'contributions',
                                   'American Benefits Council ([d6dlKYRPJTA @ 00:00:55])'],
                                  ['The 2026 final rule is operational housekeeping, not a substantive '
                                   'rewrite',
                                   'Issued May 28, 2026 by HHS, Labor, Treasury, and OPM after claim '
                                   'volume overwhelmed agencies',
                                   'Expect workflow, fee, and deadline changes rather than any shift in '
                                   'award math',
                                   'KLGatesLaw ([NwapzBNojY0 @ 00:00:39])'],
                                  ['Litigation, not rulemaking, steers how the QPA and IDR actually '
                                   'operate',
                                   'TMA3 on QPA calculation remains unresolved; CMS issues guidance 6 to '
                                   '12 months after rulings',
                                   'Plan every QPA and eligibility workflow around the next court ruling '
                                   'and guidance lag',
                                   'Zelis Healthcare ([D63N2KsthY8 @ 00:05:52])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers: Fees, Batches, Clocks, and '
                        'the Registry',
               'paragraphs': ['The headline mechanic is the cost of entry, and every camp quotes the same '
                              "number. HaloMD's team states that the CMS non-refundable administrative fee "
                              "'is going from $115 to $15' per party, $30 total for both sides, effective "
                              'June 11, 2026 [of6CD7esHY0 @ 00:02:33]. Anders Gilberg of MGMA, whose group '
                              "advocated for the cut, calls it 'a significant reduction' and says that "
                              "'for smaller practices that is a huge improvement' [K4eVTdf3xa0 @ "
                              '00:04:28]. Xpert Billing Talk supplies the street math behind that '
                              'statement: a $150 anesthesia claim was not worth fighting at $115, because '
                              "'you'd basically lose money trying to get your money' [CwSXrQBZiOg @ "
                              '00:02:01]. Batching is the second lever, and its trigger is a date rather '
                              "than a dollar figure. According to Xpert's radiology briefing, open "
                              "negotiations starting on or after November 1, 2026 are 'strictly capped at "
                              "exactly 50 line items, period.' Those batched disputes then sit through a "
                              'new 30-business-day cooling-off period meant to force negotiation and clear '
                              'the backlog, while single, bundled, and older batch disputes keep the '
                              '90-calendar-day rules [g3C-DoM_9CI @ 00:00:45]. The operating consequence '
                              'Xpert spells out is two parallel tracking systems running at once: one for '
                              'legacy disputes and one keyed to the open-negotiation start date of every '
                              'new batched dispute in the queue.',
                              'The clocks are where cases now die. KLGates reports that the final rule '
                              "requires the non-initiating party, 'which is often the payer, to issue a "
                              "response by the 15th business day of the open negotiation period,' inside "
                              'the 30-business-day window [NwapzBNojY0 @ 00:04:19]. HaloMD adds the fine '
                              'print: that response requires no counteroffer, and the non-initiating party '
                              'must answer an IDR initiation within 3 business days [of6CD7esHY0 @ '
                              '00:10:39]. The batch side is less forgiving. Once the cooling-off period '
                              'ends, Xpert describes a four-business-day filing window that the portal '
                              "enforces with no grace period. Late claims 'just get dumped right into your "
                              "denial management queues as permanent losses,' and Xpert says spreadsheets "
                              'are inadequate for tracking the window [g3C-DoM_9CI @ 00:02:21]. On the '
                              "back end, The Phia Group reminds plans that 'the IDR awards have to be paid "
                              "within 30 calendar days of the date that a determination is rendered' and "
                              'tells them to build a dedicated award-payment tracker [ksxW878eWWk @ '
                              '00:14:13]. Each of these deadlines is counted differently: business days on '
                              'the negotiation and filing side, calendar days on the payment side. That is '
                              'why Xpert pushes a calendar-based tool and Phia pushes a standalone tracker '
                              'for every determination that lands against a plan.',
                              'The third mechanic is identity and coding, and it is the one most likely to '
                              'produce outright defaults. HaloMD reports that plans must register in the '
                              'new IDR registry within 90 days, a window the same speakers later restate '
                              'as 90 business days [of6CD7esHY0 @ 00:15:34]. The penalty for skipping '
                              'registration is severe. An unregistered plan cannot respond and defaults at '
                              'the offer stage, and a plan that registers late is covered only for steps '
                              'going forward [of6CD7esHY0 @ 00:19:47]. KLGates adds that payers must use '
                              'CARCs and RARCs to flag IDR eligibility and must include contact '
                              'information with denials. That requirement is effective August 3, 2026 but '
                              'still awaits further guidance from the agencies [NwapzBNojY0 @ 00:02:32]. '
                              'The intake channel is changing at the same time. Xpert says the 30-day '
                              'open-negotiation clock now runs from portal date stamps and that fax and '
                              "email proof is 'completely dead.' Missing a stamp means permanently losing "
                              'the dispute window, so the portal has to be monitored every day '
                              '[CwSXrQBZiOg @ 00:03:36]. For payers, the registry is the sharpest edge in '
                              'the rule, because missing registration converts a defensible dispute into a '
                              'default at the offer stage. For providers, the remittance codes become the '
                              'eligibility flag KLGates describes, telling billing teams which claims '
                              'belong in the federal process.'],
               'table': {'caption': 'Operations final rule mechanics, clocks, and cutover dates as '
                                    'practitioners lay them out',
                         'headers': ['Mechanic', 'Rule or Number', 'Execution Detail', 'Expert Source'],
                         'rows': [['Certified IDR entity eligibility clock after selection',
                                   'Eligibility determinations required within five business days of IDRE '
                                   'selection',
                                   'KLGates flags this as a new hard deadline on the arbitration entities '
                                   'themselves',
                                   'KLGatesLaw ([NwapzBNojY0 @ 00:05:09])'],
                                  ['Batch line-item ceiling and its starting baseline',
                                   'Lines per batch go from unlimited to 50, with 25 as the proposed '
                                   'figure',
                                   'Xpert frames the same change as a doubling from 25 to 50 line items',
                                   'HaloMD ([of6CD7esHY0 @ 00:28:16])'],
                                  ['Batch cooling-off and resubmission timing after a determination',
                                   'Cooling drops to 30 business days; the resubmission window shrinks to '
                                   'four business days',
                                   'HaloMD warns that missing this change means you will expire cases '
                                   'outright',
                                   'HaloMD ([of6CD7esHY0 @ 00:29:23])'],
                                  ['Rebatching sunset tied to the new plan registry launch',
                                   'Rebatching ends 120 days after the IDR registry launches for plans',
                                   'Clear any rebatching backlog before the registry clock runs out on the '
                                   'queue',
                                   'HaloMD ([of6CD7esHY0 @ 00:30:25])'],
                                  ['Remittance code specificity problem for eligibility flagging',
                                   'N830 is described as non-specific, and 20 states are bifurcated '
                                   'between regimes',
                                   'Codes alone will not settle eligibility in bifurcated states without '
                                   'further guidance',
                                   'HaloMD ([of6CD7esHY0 @ 00:23:06])'],
                                  ['IDR gateway cutover replacing the old federal web forms',
                                   'Old web forms shut down January 15, 2027 and the IDR gateway takes '
                                   'over',
                                   'Every user must be verified and US-based before filing through the new '
                                   'gateway',
                                   'Xpert Billing Talk ([g3C-DoM_9CI @ 00:04:07])'],
                                  ['Technical assistance reopenings and the payment obligation',
                                   'Payment is still due within 30 days even while a reopening request is '
                                   'pending',
                                   'Do not hold award payments while a technical assistance reopening sits '
                                   'open',
                                   'HaloMD ([of6CD7esHY0 @ 00:46:49])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the operators are actually running the new rulebook',
                           'body': 'Billing shops, TPAs, and provider-side filers are converging on the '
                                   'same habits: separate the legacy and new-rule caseloads, document '
                                   'everything in writing, and police eligibility code by code before the '
                                   'portal or the arbitrator does it for you.',
                           'items': ['Split the caseload into pre- and post-November 1 tracking systems '
                                     'keyed on the open-negotiation start date, and run deadlines on a '
                                     'calendar-based tool rather than spreadsheets [Xpert Billing Talk — '
                                     'g3C-DoM_9CI @ 00:01:47]',
                                     'Radiology batching runs on Category I CPT codes. Coders must '
                                     'cross-reference manually, because mixing eligible and ineligible '
                                     'codes in one batch triggers automatic rejection [Xpert Billing Talk '
                                     '— g3C-DoM_9CI @ 00:03:22]',
                                     'Billing agencies initiate on everything and ignore negotiation '
                                     'requests, so log every good-faith outreach and submit the log in '
                                     'IDR, where it is considered, unlike settlement talks in litigation '
                                     '[The Phia Group, LLC — ksxW878eWWk @ 00:03:31]',
                                     'Anesthesia is usually elective, so it is IDR-eligible only if the '
                                     'facility was in-network. Check network status, admission type, and '
                                     "timelines on every claim and 'be the goalie' [The Phia Group, LLC — "
                                     'ksxW878eWWk @ 00:06:46]']},
               'sop_steps': [{'step': 1,
                              'title': 'Re-map remittance and eligibility workflows',
                              'action': 'Audit current IDR workflows, build in the new CARC/RARC codes, '
                                        'and re-screen low-dollar claims that were previously written off.',
                              'detail': 'KLGates tells clients to audit workflows now, build in the new '
                                        'codes, revisit low-dollar claims now that the fee is lower, and '
                                        'monitor agency guidance [KLGatesLaw — NwapzBNojY0 @ 00:06:25]'},
                             {'step': 2,
                              'title': 'Register every plan in the IDR registry on time',
                              'action': 'Register each plan inside the registry window, because late '
                                        'registration covers only steps going forward.',
                              'detail': 'An unregistered plan cannot respond and defaults at the offer '
                                        'stage, and a plan that registers late is covered only for steps '
                                        'going forward [HaloMD — of6CD7esHY0 @ 00:19:47]'},
                             {'step': 3,
                              'title': 'Run open negotiation on portal date stamps',
                              'action': 'Treat the portal date stamp as the only clock, monitor the portal '
                                        'daily, and answer by business day 15 when you are the '
                                        'non-initiating party.',
                              'detail': "Fax and email proof is 'completely dead,' and 'missing a deadline "
                                        "now has zero margin for error,' so the portal must be monitored "
                                        'daily [Xpert Billing Talk — CwSXrQBZiOg @ 00:03:54]'},
                             {'step': 4,
                              'title': 'Track awards and flag repeat initiators',
                              'action': 'Pay awards inside 30 calendar days through a dedicated tracker, '
                                        'and run a dispute dashboard that flags repeat initiators.',
                              'detail': 'IDR awards must be paid within 30 calendar days of the '
                                        'determination, so build an award-payment tracker alongside a '
                                        'dashboard that flags repeat initiators [The Phia Group, LLC — '
                                        'ksxW878eWWk @ 00:14:13]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest fight is over what Congress should bolt onto IDR. Tom '
                              'Leefrieded of the AFL-CIO calls ranking member Pallone\'s bill "really the '
                              'gold standard" because it trends 2019 rates forward, forces payment at 30 '
                              'days, strips out ghost rates, mandates CMS audits of QPAs, and eliminates '
                              'arbitration outright [9SCzxZp8uAE @ 00:34:14]. James Greenspan reads the '
                              'same bill as a nonstarter. Pallone floated the identical idea in 2019, was '
                              'overruled, and then signed the version that kept arbitration. The new bill '
                              'has no co-sponsors and "not a lot of appetite on the Hill," so Greenspan '
                              'treats it as an anchoring tactic ahead of next-Congress negotiations '
                              "[HTDpgKwIfRg @ 00:00:33]. Brian O'Hara of The Phia Group sees a payer-side "
                              'danger in a benchmark as well, warning that payers could end up setting '
                              "rates unilaterally. O'Hara also points to New Jersey bills running $100K to "
                              '$500K and assistant-surgeon claims topping $1M on a usual-and-customary '
                              'basis that the NSA does not permit [8QIP4F1EGTA @ 00:17:27]. Greenspan '
                              'flags a third lane that sidesteps the rate fight entirely: a possible '
                              'Cassidy legacy bill. It would not narrow which cases qualify. Instead it '
                              'would move the eligibility determination earlier in the process and make it '
                              'binding, ending the repeated eligibility challenges that both sides now '
                              'fight over on case after case [HTDpgKwIfRg @ 00:01:36].',
                              'Practitioners split just as hard on whether the system is broken or merely '
                              'being abused. At the Coalition for Affordable Hospitals panel, Maya Holmes '
                              'of the Culinary Health Fund rated the NSA net negative. Tom Leefrieded of '
                              'the AFL-CIO rated it net positive, on the grounds that the patient '
                              'protections are still needed [9SCzxZp8uAE @ 00:38:26]. Provider-side '
                              'operators reject the runaway-cost story. Pilgrim of SCP Health says the '
                              'group is now in network more often and at lower rates, and adds: "We are '
                              'actually making less dollars after the No Surprises Act has been '
                              'implemented than we did before" [PpfXacIXrAc @ 00:53:49]. Anders Gilberg of '
                              'MGMA concedes that abuses exist but calls them "not the majority." Gilberg '
                              'argues that payers are "hiding behind" egregious cases, such as a Florida '
                              "physician's six-figure claim, when they should be offering amounts nearer "
                              'to in-network rates [K4eVTdf3xa0 @ 00:08:37]. The payer camp answers with '
                              'concentration data. Kenna Watts reports that five provider groups, four '
                              'private-equity staffing groups plus HaloMD, file roughly three-quarters of '
                              'all disputes. Watts adds that up to $1.4B has gone to contingency fees, and '
                              'that staffing groups win 90% to 96% of the time with awards running 6 to 10 '
                              'times median in-network rates [wJkWOgxZj6k @ 00:12:03].',
                              'The operations final rule itself gets graded on a curve. Gilberg, whose '
                              'MGMA pushed for the cut in the initiation fee from $115 to $15, sums up the '
                              'provider reaction: "we\'ll take it as a win and move on from there" '
                              '[K4eVTdf3xa0 @ 00:16:02]. Katie Johnson of the American Benefits Council '
                              'calls the same rules only an "initial step." They were proposed years ago, '
                              'took a long time to finalize, and in the Council\'s view miss "the most '
                              'egregious areas of abuse." The Council is pressing Congress and the Trump '
                              'administration for more rigorous oversight [30BDiubQ0cg @ 00:00:59]. The '
                              'litigation track divides operators too. Judge Kernodle sided with TMA on '
                              'every QPA calculation point. Ron Howrigan of Fulcrum Strategies predicts '
                              'that CMS still will not audit QPAs, so the next move is a "TMA-5" suit '
                              'against CMS or a class action against carriers. Howrigan expects the class '
                              'action to land harder [f9Q5ImwNeS0 @ 00:11:50]. Brady Bazar of The Phia '
                              'Group runs the defensive play for TPAs. Plans should use a good-faith '
                              'interpretation of the 2023 methodology until the Fifth Circuit rules en '
                              'banc, document that approach without writing a "40page memo," and keep QPA '
                              'disclosures carrying certification language [ksxW878eWWk @ 00:08:47].'],
               'table': {'caption': 'Contested Playbooks: Congress, Recourse, Award Math, Fees, and Timing',
                         'headers': ['Contested Question', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Should Congress replace arbitration with a national benchmark rate?',
                                   'Pallone bill trends 2019 rates forward, pays at 30 days, and '
                                   'eliminates arbitration entirely',
                                   'Greenspan says the same idea already lost in 2019, has no co-sponsors, '
                                   'and is likely anchoring',
                                   'Coalition for Affordable Hospitals ([9SCzxZp8uAE @ 00:34:14]); '
                                   'Gottlieb and Greenspan, LLC ([HTDpgKwIfRg @ 00:00:33])'],
                                  ['Does enforcing IDR awards fix the broken process or worsen it?',
                                   'Murphy approach keeps IDR intact and adds enforcement of awards, which '
                                   'favors providers',
                                   "O'Hara warns that this assumes IDR works, so enforcement would "
                                   'snowball the existing problem',
                                   'The Phia Group, LLC ([8QIP4F1EGTA @ 00:12:10]); The Phia Group, LLC '
                                   '([8QIP4F1EGTA @ 00:13:21])'],
                                  ['Do self-funded employers have any real recourse against abusive '
                                   'filers?',
                                   'Gelfand says employers have no recourse and IDREs lose money when they '
                                   'reject ineligible claims',
                                   'Pilgrim counters that a pattern-of-practice review now gives employers '
                                   'recourse against repeat filers',
                                   'Paragon Health Institute ([PpfXacIXrAc @ 01:05:43]); Paragon Health '
                                   'Institute ([PpfXacIXrAc @ 01:06:28])'],
                                  ['What drives payer cost more: provider win rate or award size?',
                                   'Hammond says Cigna offered about 3.6 times QPA and still lost about '
                                   'three-quarters of disputes',
                                   'Ippolito says award size matters more, because insurers could win '
                                   'every case offering $5M',
                                   'Center on Health Insurance Reforms ([wJkWOgxZj6k @ 00:29:21]); Paragon '
                                   'Health Institute ([PpfXacIXrAc @ 00:19:45])'],
                                  ['Was the pre-NSA market a workable equilibrium worth restoring?',
                                   'Paragon panelists frame pre-NSA pricing as an equilibrium that '
                                   'arbitration has since distorted',
                                   'Tripoli says market negotiations are failing and wants a statutory '
                                   'anchor, citing California and Ohio',
                                   'Center on Health Insurance Reforms ([wJkWOgxZj6k @ 00:59:11]); Center '
                                   'on Health Insurance Reforms ([wJkWOgxZj6k @ 01:00:17])'],
                                  ['Will the $15 administrative fee help small practices or flood the '
                                   'system?',
                                   'HaloMD expects volume to rise among small groups; KLGates says revisit '
                                   'low-dollar claims now',
                                   'Xpert Billing Talk asks whether the $15 fee triggers a spike that '
                                   'creates a new backlog',
                                   'HaloMD ([of6CD7esHY0 @ 00:08:16]); KLGatesLaw ([NwapzBNojY0 @ '
                                   '00:06:25]); Xpert Billing Talk ([CwSXrQBZiOg @ 00:05:10])'],
                                  ['When could a congressional IDR fix realistically pass into law?',
                                   'Hammond says a lame-duck fix is unlikely, but a 2027 vehicle is viable',
                                   'Ippolito rates reform odds modest at best; Adler expects reform to '
                                   'ride as a budget offset',
                                   'Center on Health Insurance Reforms ([wJkWOgxZj6k @ 00:54:51]); Paragon '
                                   'Health Institute ([PpfXacIXrAc @ 00:44:29])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The costliest firsthand trap is the clock. Xpert Billing Talk warns that '
                              'batched disputes now sit through a new 30-business-day cooling-off period '
                              'and then get a four-business-day filing window. The portal blocks late '
                              'filings with no grace period, and those claims "just get dumped right into '
                              'your denial management queues as permanent losses" [g3C-DoM_9CI @ '
                              '00:02:36]. The HaloMD team hammers the same point on the batch resubmission '
                              'window, which has been cut to 4 business days: "Do not miss this particular '
                              'change because you will expire cases" [of6CD7esHY0 @ 00:30:03]. The proof '
                              'standard is tightening at the same time. The second Xpert Billing Talk '
                              'breakdown says the 30-day open-negotiation clock now runs off portal date '
                              'stamps and that fax and email proof is "completely dead." In that '
                              'breakdown\'s words, "Missing a deadline now has zero margin for error," so '
                              'the portal has to be monitored daily [CwSXrQBZiOg @ 00:03:54]. Xpert '
                              'Billing Talk also says spreadsheets are not up to the job and teams need a '
                              'calendar-based tracking tool. Radiology coders face an extra trap: they '
                              'must manually cross-reference Category I CPT codes, because mixing eligible '
                              'and ineligible codes in a batch triggers automatic rejection [g3C-DoM_9CI @ '
                              '00:03:53].',
                              "Plans and TPAs report their own bleeding points. Brian O'Hara describes one "
                              'claim split into 15 disputes, one per CPT code, spread across seven or '
                              'eight IDREs with mixed outcomes: "Some IDREs have dismissed disputes, some '
                              'are letting them go through, some we haven\'t heard back from" [8QIP4F1EGTA '
                              "@ 00:07:06]. O'Hara also reports plans learning of determinations months "
                              'after the fact. IDREs refuse to correct errors the provider caused, such as '
                              'filing with the wrong email address, and eligibility problems surface in '
                              'roughly half of all cases. O\'Hara\'s verdict: "This is all the time" '
                              '[8QIP4F1EGTA @ 00:16:00]. HaloMD flags a new default trap in the plan '
                              'registry. A plan that has not registered cannot respond and defaults at the '
                              'offer stage. Registering late helps only with steps going forward, because '
                              '"It is forward-looking only" [of6CD7esHY0 @ 00:20:52]. Brady Bazar puts '
                              'numbers on the eligibility war: eligibility was challenged in 40% of '
                              'disputes, about 476,000 in the first half of 2025, making it the main '
                              'bottleneck in the entire process. For TPAs, that turns eligibility proof '
                              'into the core daily workload. The provider side faces the mirror image of '
                              'that grind, since every one of those challenged filings is a claim stuck '
                              'outside the payment pipeline [ksxW878eWWk @ 00:05:31].',
                              'Winning is not the same as collecting. Anders Gilberg says providers win '
                              'more than 80% of the time but often go unpaid, which is why MGMA wants '
                              'accountability for timely payment and why enforcement legislation is '
                              'pending [K4eVTdf3xa0 @ 00:07:01]. Brady Bazar explains the hole. In '
                              'Guardian Flight, the Fifth Circuit held there is no private right of action '
                              'to enforce IDR awards, and the Supreme Court declined review, so '
                              'enforcement runs through HHS civil penalties. Awards are still due within '
                              '30 calendar days, and nonpayment carries reputational and regulatory risk. '
                              'TPAs are told to build an award-payment tracker [ksxW878eWWk @ 00:12:11]. '
                              'On the payer ledger, Bartlett of ERIC describes one employer whose IDR '
                              'costs went from $3.5M in 2025 to a $12M pace, about $4,000 in excess per '
                              'claim, with settlements stretching from one month to three. Another '
                              'employer is absorbing awards at 4.5 times billed charges [wJkWOgxZj6k @ '
                              '00:33:59]. The network fallout cuts both ways. Ron Howrigan cites an ASA '
                              'survey in which more than 40% of respondents reported a UnitedHealthcare '
                              'termination or threat of one, alongside Blue Cross NC threat letters. Both '
                              'carriers stopped once the lawsuits began [f9Q5ImwNeS0 @ 00:19:50].'],
               'table': {'caption': 'Firsthand Failure Modes and the Economics Behind Them',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw Firsthand',
                                     'Economics Check or Counter-Move',
                                     'Expert Source'],
                         'rows': [['Paying the wrong fee at dispute initiation or offer stage',
                                   'Bazar says entity fees were updated and paying the wrong fee gets your '
                                   'offer denied',
                                   'HaloMD reports the admin fee dropping from $115 to $15, so confirm '
                                   'current fees first',
                                   'The Phia Group, LLC ([ksxW878eWWk @ 00:17:28]); HaloMD ([of6CD7esHY0 @ '
                                   '00:02:33])'],
                                  ['Mixing eligible and ineligible radiology codes inside one batch',
                                   'Batching runs on Category I CPT codes and mixed batches trigger '
                                   'automatic rejection',
                                   'Coders must manually cross-reference every code before the batch hits '
                                   'the portal',
                                   'Xpert Billing Talk ([g3C-DoM_9CI @ 00:03:22])'],
                                  ['Assuming a technical assistance reopening pauses the payment clock',
                                   'HaloMD says payment is still due within 30 days while a reopening is '
                                   'pending',
                                   'Fund the award on time and pursue the reopening on a separate track',
                                   'HaloMD ([of6CD7esHY0 @ 00:46:49])'],
                                  ['Trying to apply cooling-off periods across a whole TPA book',
                                   'HaloMD states that cooling cannot be applied at the TPA level at all',
                                   'Track cooling periods by plan, since each ERISA plan gets its own '
                                   'registry ID',
                                   'HaloMD ([of6CD7esHY0 @ 00:37:06]); HaloMD ([of6CD7esHY0 @ 00:21:12])'],
                                  ['In-network surgeon billing out of network through a separate TIN',
                                   'Awards hit $85,448.66 against $1,969.44, and the surgeon terminated '
                                   'the contract when challenged',
                                   'Challenging the billing pattern cost the fund that in-network '
                                   'relationship outright',
                                   'Coalition for Affordable Hospitals ([9SCzxZp8uAE @ 00:09:07]); '
                                   'Coalition for Affordable Hospitals ([9SCzxZp8uAE @ 00:33:01])'],
                                  ['Shared-savings vendors sitting between plans and providers',
                                   'Gelfand says these vendors keep about 30% of the difference and should '
                                   'be banned',
                                   'Pilgrim says shared savings arrangements block in-network deals from '
                                   'getting done',
                                   'Paragon Health Institute ([PpfXacIXrAc @ 01:15:43]); Paragon Health '
                                   'Institute ([PpfXacIXrAc @ 01:17:11])'],
                                  ['Counting on CMS to follow a court win against its guidance',
                                   'After TMA-1, CMS reissued the same guidance, which forced the TMA-2 '
                                   'lawsuit',
                                   'Howrigan expects more litigation, including a possible class action '
                                   'against carriers',
                                   'Fulcrum Strategies ([f9Q5ImwNeS0 @ 00:07:16]); Fulcrum Strategies '
                                   '([f9Q5ImwNeS0 @ 00:11:50])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Ways Disputes Die Before Anyone Argues the Merits',
                           'body': 'Every item below is a loss practitioners watched happen on procedure '
                                   'alone, before an arbitrator ever weighed an offer.',
                           'items': ['Hard-calendar the four-business-day filing window after the '
                                     '30-business-day cooling-off period, because the portal blocks late '
                                     'filings with no grace period and dumps them into denial queues as '
                                     'permanent losses [Xpert Billing Talk — g3C-DoM_9CI @ 00:02:36].',
                                     'Register every plan in the IDR registry before the deadline, because '
                                     'an unregistered plan cannot respond, defaults at the offer stage, '
                                     'and late registration only covers steps going forward [HaloMD — '
                                     'of6CD7esHY0 @ 00:19:47].',
                                     'Verify the current administrative and entity fees before every '
                                     'payment, because paying the wrong fee means your offer is denied '
                                     '[The Phia Group, LLC — ksxW878eWWk @ 00:17:28].',
                                     'Run an award-payment tracker against the 30-calendar-day deadline, '
                                     'because unpaid awards carry reputational and regulatory risk even '
                                     'without a private right of action [The Phia Group, LLC — ksxW878eWWk '
                                     '@ 00:14:13].']}}],
 'pull_quote': '"Do not miss this particular change because you will expire cases." attributed to HaloMD '
               '(of6CD7esHY0 @ 00:30:03).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Split the dispute caseload into pre- and post-November 1, 2026 tracking systems '
                      'keyed on the open-negotiation start date [Xpert Billing Talk — g3C-DoM_9CI @ '
                      '00:01:47].',
                      'Log every good-faith negotiation outreach and submit the log in IDR, because it is '
                      'considered there, unlike settlement talks in litigation [The Phia Group, LLC — '
                      'ksxW878eWWk @ 00:03:31].',
                      'Audit workflows now, build in the new CARC/RARC codes, and revisit low-dollar '
                      'claims under the lower administrative fee [KLGatesLaw — NwapzBNojY0 @ 00:06:25].',
                      'As the non-initiating party, issue a response by the 15th business day of the '
                      '30-business-day open negotiation period [KLGatesLaw — NwapzBNojY0 @ 00:04:19].',
                      'Build a dispute dashboard that flags repeat initiators, and back eligibility '
                      'challenges with EOBs and internal network records kept clear and concise [The Phia '
                      'Group, LLC — ksxW878eWWk @ 00:15:55].',
                      'Stay current on rulings and agency moves through specialty societies such as ASA, '
                      'EDPMA, and ACR [Fulcrum Strategies — f9Q5ImwNeS0 @ 00:21:28].'],
 'statutory_citations': [{'title': 'HaloMD — Decoding The Federal IDR Operations Final Rule: Access, '
                                   'Process and Timing [00:30:03]',
                          'url': 'https://www.youtube.com/watch?v=of6CD7esHY0&t=1803s',
                          'relevance': 'Primary practitioner testimony on batch resubmission windows, plan '
                                       'registry defaults, and expired-case risk under the operations '
                                       'final rule.'},
                         {'title': 'The Phia Group, LLC — Empowering Plans: P254 – Fixing the No Surprises '
                                   'Act: Will Congress Repair IDR? [00:21:33]',
                          'url': 'https://www.youtube.com/watch?v=8QIP4F1EGTA&t=1293s',
                          'relevance': 'Primary practitioner testimony on the Pallone and Murphy proposals '
                                       'and the proposed CMS eligibility gate before arbitration.'},
                         {'title': 'Paragon Health Institute — Fixing the No Surprises Act: Scaling Back '
                                   'and Reforming the Federal Arbitration System [00:26:13]',
                          'url': 'https://www.youtube.com/watch?v=PpfXacIXrAc&t=1573s',
                          'relevance': 'Primary practitioner testimony on IDRE volume incentives, award '
                                       'multiples, and competing employer and provider reform positions.'},
                         {'title': 'Xpert Billing Talk — Federal IDR Changes Nov. 1, 2026: Radiology '
                                   'Batching & Deadlines [00:02:36]',
                          'url': 'https://www.youtube.com/watch?v=g3C-DoM_9CI&t=156s',
                          'relevance': 'Primary practitioner testimony on the 50-line batching cap, '
                                       'cooling-off period, and the four-business-day filing window.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'D63N2KsthY8',
                       'title': 'No Surprises Act & IDR Updates | What Healthcare Payers & Providers Need '
                                'to Know',
                       'channel': 'Zelis Healthcare',
                       'author': 'Zelis Healthcare',
                       'text': 'So, litigation continues to kind of steer the policy.',
                       'tip': 'So, litigation continues to kind of steer the policy.',
                       'timestamp': 352,
                       'timestamp_seconds': 352,
                       'timestamp_label': '[00:05:52]',
                       'url': 'https://www.youtube.com/watch?v=D63N2KsthY8&t=352s',
                       'markdown': '[00:05:52](https://www.youtube.com/watch?v=D63N2KsthY8&t=352s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NwapzBNojY0',
                       'title': 'No Surprises Act Check-In: The Latest Changes to the IDR Process',
                       'channel': 'KLGatesLaw',
                       'author': 'KLGatesLaw',
                       'text': 'In light of that, the final rule actually requires the non-initiating '
                               'party, which is often the payer, to issue a response by the 15th business '
                               'day of the open negotiation period.',
                       'tip': 'In light of that, the final rule actually requires the non-initiating '
                              'party, which is often the payer, to issue a response by the 15th business '
                              'day of the open negotiation period.',
                       'timestamp': 259,
                       'timestamp_seconds': 259,
                       'timestamp_label': '[00:04:19]',
                       'url': 'https://www.youtube.com/watch?v=NwapzBNojY0&t=259s',
                       'markdown': '[00:04:19](https://www.youtube.com/watch?v=NwapzBNojY0&t=259s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9SCzxZp8uAE',
                       'title': 'Panel - Fixing the No Surprises Act’s Independent Dispute Resolution '
                                '(IDR) Process',
                       'channel': 'Coalition for Affordable Hospitals',
                       'author': 'Coalition for Affordable Hospitals',
                       'text': "There's literally no transparency as to why arbitrators are selecting one "
                               'offer over another.',
                       'tip': "There's literally no transparency as to why arbitrators are selecting one "
                              'offer over another.',
                       'timestamp': 857,
                       'timestamp_seconds': 857,
                       'timestamp_label': '[00:14:17]',
                       'url': 'https://www.youtube.com/watch?v=9SCzxZp8uAE&t=857s',
                       'markdown': '[00:14:17](https://www.youtube.com/watch?v=9SCzxZp8uAE&t=857s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XZ1MNlkWu4Y',
                       'title': 'New Final Rule on No Surprises Act - Explained',
                       'channel': 'HealthWatch Wisconsin',
                       'author': 'HealthWatch Wisconsin',
                       'text': "They don't dictate which offer needs to be accepted but instead help spell "
                               'out the process.',
                       'tip': "They don't dictate which offer needs to be accepted but instead help spell "
                              'out the process.',
                       'timestamp': 69,
                       'timestamp_seconds': 69,
                       'timestamp_label': '[00:01:09]',
                       'url': 'https://www.youtube.com/watch?v=XZ1MNlkWu4Y&t=69s',
                       'markdown': '[00:01:09](https://www.youtube.com/watch?v=XZ1MNlkWu4Y&t=69s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wJkWOgxZj6k',
                       'title': 'Runaway Costs: Getting the No Surprises Act Back on Track',
                       'channel': 'Center on Health Insurance Reforms',
                       'author': 'Center on Health Insurance Reforms',
                       'text': 'This makes providers functionally customers of the IDRs or IDREs.',
                       'tip': 'This makes providers functionally customers of the IDRs or IDREs.',
                       'timestamp': 1669,
                       'timestamp_seconds': 1669,
                       'timestamp_label': '[00:27:49]',
                       'url': 'https://www.youtube.com/watch?v=wJkWOgxZj6k&t=1669s',
                       'markdown': '[00:27:49](https://www.youtube.com/watch?v=wJkWOgxZj6k&t=1669s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'of6CD7esHY0',
                       'title': 'Decoding The Federal IDR Operations Final Rule: Access, Process and '
                                'Timing',
                       'channel': 'HaloMD',
                       'author': 'HaloMD',
                       'text': 'Do not miss this particular change because you will expire cases.',
                       'tip': 'Do not miss this particular change because you will expire cases.',
                       'timestamp': 1803,
                       'timestamp_seconds': 1803,
                       'timestamp_label': '[00:30:03]',
                       'url': 'https://www.youtube.com/watch?v=of6CD7esHY0&t=1803s',
                       'markdown': '[00:30:03](https://www.youtube.com/watch?v=of6CD7esHY0&t=1803s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HTDpgKwIfRg',
                       'title': 'No Surprises Act Update - October 2026: Pallone, Cassidy, CMS Meeting',
                       'channel': 'Gottlieb and Greenspan, LLC',
                       'author': 'Gottlieb and Greenspan, LLC',
                       'text': "From what I'm hearing, there's not a lot of appetite on the Hill to "
                               'support this bill.',
                       'tip': "From what I'm hearing, there's not a lot of appetite on the Hill to support "
                              'this bill.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=HTDpgKwIfRg&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=HTDpgKwIfRg&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'f9Q5ImwNeS0',
                       'title': 'Ep. 61 - Breaking down the impacts of the TMA 3 ruling',
                       'channel': 'Fulcrum Strategies',
                       'author': 'Fulcrum Strategies',
                       'text': 'Right now almost 60 percent of all practicing anesthesiologists are over '
                               'the age of 55.',
                       'tip': 'Right now almost 60 percent of all practicing anesthesiologists are over '
                              'the age of 55.',
                       'timestamp': 1087,
                       'timestamp_seconds': 1087,
                       'timestamp_label': '[00:18:07]',
                       'url': 'https://www.youtube.com/watch?v=f9Q5ImwNeS0&t=1087s',
                       'markdown': '[00:18:07](https://www.youtube.com/watch?v=f9Q5ImwNeS0&t=1087s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PpfXacIXrAc',
                       'title': 'Fixing the No Surprises Act: Scaling Back and Reforming the Federal '
                                'Arbitration System',
                       'channel': 'Paragon Health Institute',
                       'author': 'Paragon Health Institute',
                       'text': "That's how arbitrators make money is by the volume of disputes.",
                       'tip': "That's how arbitrators make money is by the volume of disputes.",
                       'timestamp': 1573,
                       'timestamp_seconds': 1573,
                       'timestamp_label': '[00:26:13]',
                       'url': 'https://www.youtube.com/watch?v=PpfXacIXrAc&t=1573s',
                       'markdown': '[00:26:13](https://www.youtube.com/watch?v=PpfXacIXrAc&t=1573s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PpfXacIXrAc',
                       'title': 'Fixing the No Surprises Act: Scaling Back and Reforming the Federal '
                                'Arbitration System',
                       'channel': 'Paragon Health Institute',
                       'author': 'Paragon Health Institute',
                       'text': 'We are actually making less dollars after the No Surprises Act has been '
                               'implemented than we did before.',
                       'tip': 'We are actually making less dollars after the No Surprises Act has been '
                              'implemented than we did before.',
                       'timestamp': 3229,
                       'timestamp_seconds': 3229,
                       'timestamp_label': '[00:53:49]',
                       'url': 'https://www.youtube.com/watch?v=PpfXacIXrAc&t=3229s',
                       'markdown': '[00:53:49](https://www.youtube.com/watch?v=PpfXacIXrAc&t=3229s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8QIP4F1EGTA',
                       'title': 'Empowering Plans: P254 – Fixing the No Surprises Act: Will Congress '
                                'Repair IDR?',
                       'channel': 'The Phia Group, LLC',
                       'author': 'The Phia Group, LLC',
                       'text': 'Some IDREs have dismissed disputes, some are letting them go through, some '
                               "we haven't heard back from.",
                       'tip': 'Some IDREs have dismissed disputes, some are letting them go through, some '
                              "we haven't heard back from.",
                       'timestamp': 426,
                       'timestamp_seconds': 426,
                       'timestamp_label': '[00:07:06]',
                       'url': 'https://www.youtube.com/watch?v=8QIP4F1EGTA&t=426s',
                       'markdown': '[00:07:06](https://www.youtube.com/watch?v=8QIP4F1EGTA&t=426s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'g3C-DoM_9CI',
                       'title': 'Federal IDR Changes Nov. 1, 2026: Radiology Batching & Deadlines',
                       'channel': 'Xpert Billing Talk',
                       'author': 'Xpert Billing Talk',
                       'text': 'So, they just get dumped right into your denial management queues as '
                               'permanent losses.',
                       'tip': 'So, they just get dumped right into your denial management queues as '
                              'permanent losses.',
                       'timestamp': 156,
                       'timestamp_seconds': 156,
                       'timestamp_label': '[00:02:36]',
                       'url': 'https://www.youtube.com/watch?v=g3C-DoM_9CI&t=156s',
                       'markdown': '[00:02:36](https://www.youtube.com/watch?v=g3C-DoM_9CI&t=156s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CwSXrQBZiOg',
                       'title': 'Federal IDR Gateway Rules 2026: New Portal, Fees & Batching Changes',
                       'channel': 'Xpert Billing Talk',
                       'author': 'Xpert Billing Talk',
                       'text': 'Missing a deadline now has zero margin for error.',
                       'tip': 'Missing a deadline now has zero margin for error.',
                       'timestamp': 234,
                       'timestamp_seconds': 234,
                       'timestamp_label': '[00:03:54]',
                       'url': 'https://www.youtube.com/watch?v=CwSXrQBZiOg&t=234s',
                       'markdown': '[00:03:54](https://www.youtube.com/watch?v=CwSXrQBZiOg&t=234s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'K4eVTdf3xa0',
                       'title': "S1 Ep161: The No Surprises Act's new payment dispute rule, with Anders "
                                'Gilberg of MGMA',
                       'channel': 'Medical Economics TV',
                       'author': 'Medical Economics TV',
                       'text': 'And that is a significant reduction and for smaller practices that is a '
                               'huge improvement and something that we advocated for as part of this rule.',
                       'tip': 'And that is a significant reduction and for smaller practices that is a '
                              'huge improvement and something that we advocated for as part of this rule.',
                       'timestamp': 268,
                       'timestamp_seconds': 268,
                       'timestamp_label': '[00:04:28]',
                       'url': 'https://www.youtube.com/watch?v=K4eVTdf3xa0&t=268s',
                       'markdown': '[00:04:28](https://www.youtube.com/watch?v=K4eVTdf3xa0&t=268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ksxW878eWWk',
                       'title': 'Empowering Plans: P235 – The Latest No Surprises Act Developments: A 2026 '
                                'Reality Check for TPAs',
                       'channel': 'The Phia Group, LLC',
                       'author': 'The Phia Group, LLC',
                       'text': 'The IDR awards have to be paid within 30 calendar days of the date that a '
                               'determination is rendered.',
                       'tip': 'The IDR awards have to be paid within 30 calendar days of the date that a '
                              'determination is rendered.',
                       'timestamp': 853,
                       'timestamp_seconds': 853,
                       'timestamp_label': '[00:14:13]',
                       'url': 'https://www.youtube.com/watch?v=ksxW878eWWk&t=853s',
                       'markdown': '[00:14:13](https://www.youtube.com/watch?v=ksxW878eWWk&t=853s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'd6dlKYRPJTA',
                       'title': 'Just a Minute! on The Unsurprising Flaw in the No Surprises Act',
                       'channel': 'American Benefits Council',
                       'author': 'American Benefits Council',
                       'text': 'Also, we are seeing much higher volumes of claims being sent to '
                               'arbitration than expected, many of which have been found ineligible for '
                               'arbitration.',
                       'tip': 'Also, we are seeing much higher volumes of claims being sent to arbitration '
                              'than expected, many of which have been found ineligible for arbitration.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=d6dlKYRPJTA&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=d6dlKYRPJTA&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '30BDiubQ0cg',
                       'title': 'Just a Minute! on New No Surprises Act Arbitration Rules',
                       'channel': 'American Benefits Council',
                       'author': 'American Benefits Council',
                       'text': 'Last week, federal regulators attempted to respond to some of the IDR '
                               "system's problems by issuing final rules governing the IDR process.",
                       'tip': 'Last week, federal regulators attempted to respond to some of the IDR '
                              "system's problems by issuing final rules governing the IDR process.",
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=30BDiubQ0cg&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=30BDiubQ0cg&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'of6CD7esHY0',
                       'title': 'Decoding The Federal IDR Operations Final Rule: Access, Process and '
                                'Timing',
                       'channel': 'HaloMD',
                       'author': 'HaloMD',
                       'text': 'It is forward-looking only.',
                       'tip': 'It is forward-looking only.',
                       'timestamp': 1252,
                       'timestamp_seconds': 1252,
                       'timestamp_label': '[00:20:52]',
                       'url': 'https://www.youtube.com/watch?v=of6CD7esHY0&t=1252s',
                       'markdown': '[00:20:52](https://www.youtube.com/watch?v=of6CD7esHY0&t=1252s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
