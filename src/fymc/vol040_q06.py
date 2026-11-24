from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'pbm-contract-forensics-spread-rebates-mac-audits',
 'question_prompt': 'How do self-funded employers spot PBM spread, rebate, and MAC games in their '
                    'contracts, and how do pharmacies survive PBM audits?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'PBM Contract Forensics: Spread, Rebates, MAC Pricing, and Audits',
 'subtitle': 'Generic spread pricing, rebate pass-through definitions, maximum allowable cost indexes, '
             'transparent and pass-through contract language, generic compliance ratios, continuous '
             'pricing improvement, specialty carve-outs, and PBM audit and network compliance',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one diagnosis: the PBM profits in the gap between what '
                      'the plan is billed and what the pharmacy is paid, and percentage discounts off AWP '
                      "hide that gap. Dr. Eric Bricker's amlodipine math shows a plan paying 48 cents for "
                      'a drug acquired at 1.9 cents, roughly 25 times cost, while Jim Lodge cites an '
                      'almost 500% markup in the Johnson & Johnson case. Rebate pass-through pledges leak '
                      'through PBM-owned GPOs and rebate aggregators, and rebates fell from 48% to 13% of '
                      'PBM profit. Operators fight back with absolute-price benchmarks, quarterly discount '
                      'audits that recover 10 to 40%, five core contract clauses, and specialty '
                      'carve-outs. Practitioners split on whether pass-through contracts fix the problem '
                      'or simply move it: SmithRx and Cora Opsahl argue that fixed guarantees still trap '
                      'sponsors inside pass-through deals.',
 'key_metrics': [{'label': 'Generic Spread Multiplier',
                  'metric': 'Generic Spread Multiplier',
                  'value': '~25x (48 cents billed vs 1.9 cents acquisition)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Amlodipine (generic Norvasc) walk-through: AWP $2.38 at 20% of AWP is 48 '
                             'cents billed to the plan, the pharmacy acquires the drug for 1.9 cents, and '
                             'the plan pays almost exactly 25 times more.',
                  'source': 'AHealthcareZ - Healthcare Finance Explained ([0XFk1m3yGuY @ 00:03:09])'},
                 {'label': 'High-Cost Drug Markup in J&J Fiduciary Case',
                  'metric': 'High-Cost Drug Markup in J&J Fiduciary Case',
                  'value': 'Almost 500% average markup',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'High-cost drugs were marked up an average of almost 500% to Johnson & '
                             'Johnson compared with pharmacy reimbursement, and the PBM kept the spread as '
                             'pure profit on top of admin fees.',
                  'source': 'PBM Insider ([o57C9bK5ouI @ 00:01:20])'},
                 {'label': 'Rebates as Share of PBM Profit',
                  'metric': 'Rebates as Share of PBM Profit',
                  'value': '48% (2012) to 13% (2023)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Nephron profit mix: admin fees rose from 5% to 22% and mail/specialty/spread '
                             'rose from 47% to 65%, so 100% rebate pass-through touches only 13% of profit '
                             'and leaves 87% outside it.',
                  'source': 'AHealthcareZ - Healthcare Finance Explained ([yFJFnewKqw4 @ 00:08:25])'},
                 {'label': 'PBM Audit Overcharge Findings',
                  'metric': 'PBM Audit Overcharge Findings',
                  'value': '30-40% overcharges',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A jumbo plan sponsor reports that audits find 30 to 40% overcharges and that '
                             'every audit the sponsor has run yielded money back; The Partners Group puts '
                             'typical audit findings at 10 to 30%.',
                  'source': 'Relentless Health Value ([xHAyQelFkf8 @ 00:16:37])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Spread pricing is not complex, whatever the PBM pitch about puts and takes. '
                              'Jim Lodge of PBM Insider breaks it into two contracts. The first is the '
                              'PBM-to-plan-sponsor contract, which carries the formulary, the prices and '
                              'the estimated rebates. The second is a separate PBM-to-pharmacy contract '
                              'that pays a drug reimbursement plus a professional dispensing fee. Spread '
                              'pricing is simply the difference between the two [o57C9bK5ouI @ 00:00:59]. '
                              'Dr. Eric Bricker of AHealthcareZ reduces it to two formulas. PBM profit '
                              'equals the net AWP billed to the plan minus MAC plus dispensing fee. '
                              'Pharmacy profit equals MAC plus fee minus acquisition cost from the '
                              'wholesaler [0XFk1m3yGuY @ 00:01:34]. Gary Alton of The Partners Group sees '
                              'the same gap at the carrier level, where a carrier negotiates a 75% '
                              'discount, passes along 65% and keeps a 10-point spread [Cxvmh46o824 @ '
                              '00:43:34]. Lodge anchors the stakes in the Johnson & Johnson fiduciary '
                              'case, where high-cost drugs were marked up almost 500% over pharmacy '
                              'reimbursement and the PBM kept the difference as pure profit on top of its '
                              'admin fees [o57C9bK5ouI @ 00:01:20]. The remedy Lodge prescribes is blunt: '
                              'the sponsor pays the identical ingredient cost and dispensing fee the PBM '
                              "reimburses the pharmacy, and the admin fee is the PBM's only revenue.",
                              'The second point of agreement: a discount off AWP is not a price. On '
                              'Relentless Health Value, the Gleevec example from Benjamin Jolley runs the '
                              'numbers. Branded Gleevec cost $27,000 a month. Generic imatinib through a '
                              'PBM cost $9,000 a month and was framed as an $18,000 savings. The Cost Plus '
                              "cash price was $25 a month. AWP means Ain't What's Paid, so sponsors should "
                              'insist on absolute prices rather than discounts [xHAyQelFkf8 @ 00:08:26]. '
                              'Justine of TheCoyPharmer explains why the guarantee works as a floor. If '
                              'the sponsor was promised AWP minus 89% and the book runs at minus 88%, the '
                              'PBM pays the shortfall, but overperformance is not reciprocal, because PBM '
                              'guarantees to plan sponsors are typically a minimum level [H3p5Yw0Y-ek @ '
                              '00:07:20]. Alan Pannier of SmithRx extends the critique to pass-through '
                              'deals. Under both spread and pass-through models, the PBM is incentivized '
                              'to manage pricing toward the fixed rates set at selection, so better '
                              'pharmacy and manufacturer pricing won mid-term never reaches the sponsor '
                              '[ZuvAxUS0mII @ 00:00:30]. Cora Opsahl adds that guarantees are reconciled '
                              'by therapeutic category at year end, with figures like AWP minus 49 '
                              'reverse-engineered after the fact [xHAyQelFkf8 @ 00:14:09].',
                              'Practitioners also agree that a 100% rebate pass-through pledge settles '
                              'very little. Dr. Bricker lists the pledges: Optum in January 2025, CVS in '
                              '2018, and Cigna/Express Scripts in October 2025, effective 2027. Then '
                              "Bricker points to the PBM-owned GPOs (Optum's MSR, CVS's Zinc, Cigna's "
                              'Ascent), which collect admin fees that are a total black box [yFJFnewKqw4 @ '
                              '00:03:01]. Using Nephron figures, Bricker shows the profit mix shifting '
                              'between 2012 and 2023. Rebates fell from 48% to 13% of PBM profit. Admin '
                              'fees rose from 5% to 22%, and mail, specialty and spread rose from 47% to '
                              '65%. A pass-through promise therefore touches only 13% of profit and leaves '
                              '87% outside it [yFJFnewKqw4 @ 00:08:25]. Frier Levitt describes '
                              'litigation-exposed rebate aggregators that demand, for example, 25 cents on '
                              'the dollar for formulary access. The aggregator keeps about 30% and passes '
                              '60 to 70 cents to the PBM, which then tells the plan it is turning it all '
                              'over [8mubYuuHvMI @ 00:01:20]. Benefits Blake supplies the scoreboard: only '
                              '59% of employers receive full traditional rebates, and only 57% receive '
                              'full specialty rebates [wUzyX8bEvt0 @ 00:11:06].'],
               'table': {'caption': 'Where practitioners agree on how PBMs extract margin and what '
                                    'sponsors must demand',
                         'headers': ['Consensus Point',
                                     'Mechanic Reported',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Spread pricing is the gap between two separate contracts',
                                   'PBM bills the plan one price and reimburses the pharmacy a lower '
                                   'ingredient cost plus fee',
                                   'Demand identical ingredient cost and fee billed and paid, with admin '
                                   'fee as sole PBM revenue',
                                   'PBM Insider ([o57C9bK5ouI @ 00:00:59])'],
                                  ['AWP discounts disguise inflated generic prices',
                                   'Imatinib sold as an $18,000 monthly savings at $9,000 versus $25 cash '
                                   'at Cost Plus',
                                   'Negotiate and benchmark on absolute prices, never on percentage '
                                   'discounts off AWP',
                                   'Relentless Health Value ([xHAyQelFkf8 @ 00:08:26])'],
                                  ['Discount guarantees are floors, not shared upside',
                                   'PBM pays any shortfall below guarantee, but overperformance is not '
                                   'returned to the sponsor',
                                   'Push for NADAC or pass-through models so overperformance flows back to '
                                   'the sponsor',
                                   'TheCoyPharmer ([H3p5Yw0Y-ek @ 00:07:20])'],
                                  ['Fixed pricing locks sponsors out of mid-contract gains',
                                   'PBM keeps negotiating better pharmacy and manufacturer pricing '
                                   'throughout the contract term',
                                   'Seek pricing that updates continuously across the book instead of '
                                   'fixed discount guarantees',
                                   'SmithRx ([ZuvAxUS0mII @ 00:00:30])'],
                                  ['Rebate pass-through covers a shrinking slice of PBM profit',
                                   'Rebates fell from 48% to 13% of profit while admin fees rose to 22%',
                                   'Write GPO admin fees explicitly into the pass-through definitions, not '
                                   'just manufacturer rebates',
                                   'AHealthcareZ - Healthcare Finance Explained ([yFJFnewKqw4 @ '
                                   '00:08:25])'],
                                  ['Rebate aggregators skim before the plan sees any money',
                                   'PBM-owned aggregator keeps roughly 30% and passes 60 to 70 cents '
                                   'onward',
                                   'Negotiate down to the definitions section using counsel not paid by '
                                   'the PBM',
                                   'Frier Levitt ([8mubYuuHvMI @ 00:01:20])'],
                                  ['Audits of incumbent PBM contracts reliably recover money',
                                   'Typical audits find 10 to 30% while incumbent generic discounts lagged '
                                   '55% versus 76%',
                                   'Audit discounts quarterly and renegotiate annually rather than signing '
                                   'multi-year stale deals',
                                   'The Partners Group ([Cxvmh46o824 @ 00:56:10])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Bricker's amlodipine walk-through is the template for repricing a generic "
                              'claim. AWP for generic Norvasc is $2.38, and at an 80% discount the plan '
                              'pays the PBM 20%, or 48 cents [0XFk1m3yGuY @ 00:02:14]. MAC is unknown, not '
                              'published and proprietary, so Bricker plugs in a hypothetical 25 cents for '
                              'MAC plus dispensing fee. On those numbers the PBM keeps 23 cents. The '
                              'pharmacy buys the drug for 1.9 cents and also clears about 23 cents. The '
                              'plan pays almost exactly 25 times more than the drug costs [0XFk1m3yGuY @ '
                              '00:03:09]. Scaled up, Ohio Medicaid lost $208 million on generic spend '
                              'alone, and Kentucky Medicaid had the same problem. That raises the question '
                              'of what is happening inside municipalities, school systems and private '
                              "employers [0XFk1m3yGuY @ 00:03:27]. Alton's case study of an employer with "
                              'roughly 400 lives answers it for the private side. The effective generic '
                              'discount was 55% under the incumbent versus 76% under the C2 coalition '
                              'contract, and rebate shares across the market ranged from 0% to 75 to 80% '
                              '[Cxvmh46o824 @ 00:51:42]. The switch was projected to save 30%, or $163K, '
                              'and came in at about 32%.',
                              'MAC is where the generic spread is manufactured. Justine, a pharmacist with '
                              '20 years in the field, explains that brand claims reimburse at a stable AWP '
                              'minus 18 to 21%. Generics instead run on MAC prices that the PBM sets '
                              'unilaterally and changes by member, by network or over time. A claim with a '
                              '$45 usual and customary price is paid at MAC whenever MAC is lower '
                              '[H3p5Yw0Y-ek @ 00:04:54]. Behind the scenes there are separate MAC lists '
                              'for each pharmacy guarantee. Sponsors are grouped into 5 to 8 cohorts, the '
                              'lists are adjusted daily or weekly, and overperforming sponsors may be '
                              'migrated to a new MAC list [H3p5Yw0Y-ek @ 00:13:52]. PA Pharmacists '
                              "document the pharmacy side. One drug's cost jumped from $25 to $155 while "
                              'MAC reimbursement sat at $55, a $100 loss on the fill. The pharmacy lost at '
                              'least $1,500 in two weeks, because PBMs cut MAC quickly but lag on '
                              'increases [l81CzyzPR6M @ 00:01:11]. Cora Opsahl reports the pass-through '
                              'version of the squeeze. Plans are charged on an AWP discount while '
                              'pharmacies are reimbursed on acquisition cost plus. GLP-1 claims come in '
                              'roughly $130 underwater, so pharmacies refuse those scripts [xHAyQelFkf8 @ '
                              '00:13:20].',
                              "The contracting and audit cadence practitioners run is concrete. Alton's C2 "
                              'coalition is 7 firms with $3.3B of premium under management. It sent an RFP '
                              'to 13 PBMs, received 8 responses to more than 350 questions, and selected '
                              'Express Scripts and CVS Caremark. It renegotiates contracts annually and '
                              'audits discounts quarterly [Cxvmh46o824 @ 00:09:35]. On fees, Alton sees '
                              'integration charges from $0.45 to $6 PEPM and pegs a reasonable fee at $2 '
                              'to $3. A mandatory mail-order program would add about 5% more savings '
                              '[Cxvmh46o824 @ 00:46:05]. Benefits Blake reduces the contract to five '
                              "clauses: rebate pass-through, a spread ban, audit rights (30 days' notice "
                              'is tolerable), data ownership and fee disclosure. Blake adds a warning not '
                              'to evaluate a PBM on its pitch deck [wUzyX8bEvt0 @ 00:09:10]. Cora Opsahl '
                              'names the fine print that blunts audits: pre-approved auditors, 250-claim '
                              'samples, no extrapolation and a limited look-back. There is also the '
                              'contractual bar that stops a sponsor from auditing its own claims. Even so, '
                              'every audit Cora has run yielded money back, with overcharges of 30 to 40% '
                              '[xHAyQelFkf8 @ 00:17:14].'],
               'table': {'caption': 'Street-level levers, exact numbers, and how operators deploy them',
                         'headers': ['Lever',
                                     'Exact Number Reported',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Generic claim repricing',
                                   'AWP $2.38 times 0.2 equals 48 cents billed versus 1.9 cents '
                                   'acquisition',
                                   'Rebuild PBM profit as net AWP minus MAC plus dispensing fee',
                                   'AHealthcareZ - Healthcare Finance Explained ([0XFk1m3yGuY @ '
                                   '00:02:14])'],
                                  ['Effective generic discount benchmark',
                                   '55% under the incumbent contract versus 76% under C2 coalition pricing',
                                   'Compare realized generic discount against coalition rates before any '
                                   'renewal negotiation',
                                   'The Partners Group ([Cxvmh46o824 @ 00:51:42])'],
                                  ['Integration fee ceiling',
                                   '$0.45 to $6 PEPM range, with $2 to $3 PEPM called reasonable',
                                   'Challenge any integration fee that lands above the $2 to $3 PEPM band',
                                   'The Partners Group ([Cxvmh46o824 @ 00:46:05])'],
                                  ['MAC list cohorting surveillance',
                                   'Sponsors grouped into 5 to 8 cohorts, lists adjusted daily or weekly',
                                   'Demand monthly or weekly reporting to catch quiet migration to new MAC '
                                   'lists',
                                   'TheCoyPharmer ([H3p5Yw0Y-ek @ 00:13:01])'],
                                  ['Specialty carve-out with biosimilar switch',
                                   'Remicade to Inflectra switch delivered roughly 32% year-over-year '
                                   'savings',
                                   'Start with one biosimilar switch, then add carved-out drugs every '
                                   'quarter',
                                   "Employers' Forum of Indiana ([zoRFywXBoLM @ 00:17:56])"],
                                  ['Transparent cost-plus price check',
                                   'Imatinib about $25 at Cost Plus versus roughly $200 from the primary '
                                   'wholesaler',
                                   'Use cost-plus cash prices as the absolute benchmark against PBM '
                                   'generic charges',
                                   'Relentless Health Value ([xHAyQelFkf8 @ 00:06:53])'],
                                  ['Member-level savings alerts',
                                   'Rx Savings Solutions delivered a 2% pharmacy spend decrease in 2020',
                                   'Push email or text alerts on generics, splits and dose optimization to '
                                   'members',
                                   "Employers' Forum of Indiana ([zoRFywXBoLM @ 00:22:11])"]]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Leverage plays practitioners use against PBM contract terms',
                           'body': 'These are the moves practitioners say shift negotiating power back to '
                                   'the plan sponsor, from RFP design to specialty carve-outs [Relentless '
                                   'Health Value — xHAyQelFkf8 @ 00:18:34].',
                           'items': ['Make the RFP require Cost Plus Drugs in the network. Cuban says the '
                                     'big PBMs will immediately offer bigger rebates and better terms to '
                                     'try to keep Cost Plus out [Relentless Health Value — xHAyQelFkf8 @ '
                                     '00:18:34].',
                                     'Negotiate all the way down to the definitions section with competent '
                                     'counsel, and do not use consultants paid by the PBM, which Frier '
                                     'Levitt calls a real conflict of interest [Frier Levitt — 8mubYuuHvMI '
                                     '@ 00:03:34].',
                                     'Ask for monthly or weekly reporting, and push toward NADAC or '
                                     'pass-through pricing so that overperformance on MAC flows to the '
                                     'sponsor rather than the PBM [TheCoyPharmer — H3p5Yw0Y-ek @ '
                                     '00:15:25].',
                                     'Carve out specialty starting with one biosimilar switch. Purdue '
                                     'moved Remicade to Inflectra for about 32% year-over-year savings, '
                                     'met with nearly every affected member, and now adds drugs quarterly '
                                     "[Employers' Forum of Indiana — zoRFywXBoLM @ 00:17:56]."]},
               'sop_steps': [{'step': 1,
                              'title': 'Map both contracts and reprice generic claims',
                              'action': 'Lay the sponsor contract next to the pharmacy reimbursement terms '
                                        'and compute the PBM margin on each claim.',
                              'detail': 'Treat spread as the difference between the PBM-to-sponsor and '
                                        'PBM-to-pharmacy contracts, then apply the formula PBM profit = '
                                        'net AWP minus (MAC plus dispensing fee). Run it on generics such '
                                        'as amlodipine, where 48 cents is billed for a drug bought at 1.9 '
                                        'cents [PBM Insider — o57C9bK5ouI @ 00:00:21] [AHealthcareZ - '
                                        'Healthcare Finance Explained — 0XFk1m3yGuY @ 00:01:34].'},
                             {'step': 2,
                              'title': 'Benchmark generic performance against absolute numbers',
                              'action': 'Check the generic dispense rate and the effective generic '
                                        'discount against coalition-level rates.',
                              'detail': 'A generic dispense rate in the mid-70s is a red flag. An '
                                        'effective generic discount of 55% against a 76% coalition rate '
                                        'shows how much money is on the table before renewal [The Partners '
                                        'Group — Cxvmh46o824 @ 00:15:36] [The Partners Group — Cxvmh46o824 '
                                        '@ 00:51:42].'},
                             {'step': 3,
                              'title': 'Rewrite the contract around five clauses and tight definitions',
                              'action': 'Insert rebate pass-through, a spread ban, audit rights, data '
                                        'ownership and fee disclosure, and define GPO admin fees inside '
                                        'pass-through.',
                              'detail': "Benefits Blake's five clauses form the spine of the contract, "
                                        "with 30 days' audit notice as tolerable. Pass-through language "
                                        'must reach the GPO admin fees that Bricker calls a total black '
                                        'box [Benefits Blake — wUzyX8bEvt0 @ 00:09:10] [AHealthcareZ - '
                                        'Healthcare Finance Explained — yFJFnewKqw4 @ 00:03:01].'},
                             {'step': 4,
                              'title': 'Audit quarterly and re-bid annually',
                              'action': 'Run quarterly discount audits and strike audit limits such as '
                                        'fixed claim samples and no-extrapolation clauses.',
                              'detail': 'C2 audits discounts quarterly and renegotiates annually. Typical '
                                        'audits find 10 to 30%, and Cora Opsahl reports 30 to 40% '
                                        'overcharges and money back on every audit run [The Partners Group '
                                        '— Cxvmh46o824 @ 00:56:10] [Relentless Health Value — xHAyQelFkf8 '
                                        '@ 00:16:37].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["Jim Lodge's fix for spread is blunt: the plan sponsor should pay the PBM "
                              'the exact ingredient cost and dispensing fee the PBM pays the pharmacy, '
                              "leaving the admin fee as the PBM's only revenue, which Lodge calls “just "
                              'the correct and transparent way to do things” [o57C9bK5ouI @ 00:01:59]. Dr. '
                              'Eric Bricker argues that headline pass-through pledges miss where the money '
                              'moved. Using Nephron data, Bricker shows rebates fell from 48% of PBM '
                              'profit in 2012 to 13% in 2023, while admin fees rose to 22% and mail, '
                              'specialty and spread climbed to 65%, so a 100% rebate pass-through covers '
                              'only 13% of the profit pool and leaves 87% outside it [yFJFnewKqw4 @ '
                              '00:08:25]. Alan Pannier at SmithRx goes further, warning that under both '
                              'spread and pass-through models the PBM is incentivized to manage pricing '
                              'toward the fixed discount rates the sponsor locked in at selection '
                              '[ZuvAxUS0mII @ 00:00:30]. Cora Opsahl, running a jumbo plan, describes the '
                              'same mismatch from inside a so-called pass-through deal: the plan gets '
                              'charged on an AWP discount while pharmacies get reimbursed on acquisition '
                              'cost plus, and the guarantees are reconciled by therapeutic category at '
                              'year end [xHAyQelFkf8 @ 00:12:47]. The operator takeaway: the label on the '
                              'contract settles nothing until the pricing formula on both sides matches.',
                              'The Partners Group plays the incumbent game and keeps score in discounts. '
                              "Gary Alton's C2 coalition, seven firms with $3.3B in premium, ran a "
                              '350-question RFP across 13 PBMs and landed on Express Scripts and CVS '
                              "Caremark; in the roughly 400-life case study, the client's effective "
                              'generic discount was 55% against 76% under C2, with rebate shares across '
                              'the market ranging from 0% up to 75-80% [Cxvmh46o824 @ 00:51:42]. The '
                              'Relentless Health Value panel attacks that whole scoreboard. Citing '
                              'Benjamin Jolley, they walk through imatinib: branded Gleevec at $27,000 a '
                              'month, PBM generic at $9,000 framed as an “$18,000 savings,” and a Cost '
                              "Plus cash price of $25 a month, concluding that AWP means “Ain't What's "
                              'Paid” and buyers should insist on absolute prices instead of discounts '
                              "[xHAyQelFkf8 @ 00:08:26]. Cuban's alternative lever is to stop playing on "
                              "the big PBMs' turf: write the RFP so Cost Plus Drugs must be in the "
                              'network, and the incumbents “will immediately give you a better deal to try '
                              'to exclude us” [xHAyQelFkf8 @ 00:18:34]. Benefits Blake points to the same '
                              'exit ramp, listing Cost Plus at a 15% markup and transparent shops like '
                              'Capital Rx, SmithRx, Navitus, Rightway and FairosRx as live replacements '
                              'for the Big Three [wUzyX8bEvt0 @ 00:05:48].',
                              'On specialty, the split is carve it out versus fix the pricing engine in '
                              'place. Candace Schaefer at Purdue carved specialty to Archimedes after '
                              'seeing specialty eat 46% of Rx dollars on 1-2% of volume; the first move, '
                              'Remicade to the biosimilar Inflectra, was projected to save about $180K and '
                              'actually landed near 32% year over year, and Purdue now adds drugs '
                              'quarterly [zoRFywXBoLM @ 00:17:56]. Robert Lewis of Rx Benefits backs the '
                              'carve-out direction with trend data: carved-in pharmacy running 10-12% '
                              'against 3-4% carved out, with 85% of the Fortune 500 already carved out '
                              'versus about 1 in 5 mid-market employers [Cxvmh46o824 @ 00:34:06]. Justine '
                              'at TheCoyPharmer keeps the fight inside the pricing index instead, arguing '
                              'that NADAC or pass-through models are what let generic overperformance flow '
                              "back to the sponsor rather than stay with the PBM's MAC spread [H3p5Yw0Y-ek "
                              '@ 00:14:30]. Alan Pannier pitches a third route: platform pricing where new '
                              'pharmacy network and manufacturer contracts are applied immediately and '
                              'visible in real time across the whole book, instead of renegotiating fixed '
                              'rates [ZuvAxUS0mII @ 00:01:17]. Each path attacks the same leak, but '
                              'carve-outs demand heavy member contact, while index or platform fixes '
                              'depend on reporting visibility.'],
               'table': {'caption': 'Side-by-side playbooks practitioners run against PBM contract leakage',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How to kill the spread inside the contract',
                                   'Mirror pharmacy ingredient cost and dispensing fee so the PBM earns '
                                   'admin fee only',
                                   'Assume pass-through still leaks through GPO admin fees, mail, '
                                   'specialty and spread',
                                   'PBM Insider ([o57C9bK5ouI @ 00:01:59]); AHealthcareZ - Healthcare '
                                   'Finance Explained ([yFJFnewKqw4 @ 00:08:25])'],
                                  ['How to score a PBM deal during the RFP',
                                   'Benchmark effective generic discount, such as 55% versus 76% under the '
                                   'C2 coalition',
                                   'Ignore AWP discounts and insist on absolute prices because AWP is '
                                   "Ain't What's Paid",
                                   'The Partners Group ([Cxvmh46o824 @ 00:51:42]); Relentless Health Value '
                                   '([xHAyQelFkf8 @ 00:08:26])'],
                                  ['Whether to stay with the big PBMs at all',
                                   'Coalition RFP to 13 PBMs, select Express Scripts and CVS Caremark, '
                                   'renegotiate annually',
                                   'Require Cost Plus Drugs in the RFP network or move to a transparent '
                                   'PBM',
                                   'The Partners Group ([Cxvmh46o824 @ 00:07:07]); Relentless Health Value '
                                   '([xHAyQelFkf8 @ 00:18:34])'],
                                  ['Which lever to pull first on drug spend',
                                   'Carve specialty out to Archimedes and add drugs quarterly after '
                                   'Remicade to Inflectra',
                                   'Steer members with Rx Savings Solutions alerts to generics, splits and '
                                   'dose optimization',
                                   "Employers' Forum of Indiana ([zoRFywXBoLM @ 00:19:36]); Employers' "
                                   'Forum of Indiana ([zoRFywXBoLM @ 00:22:11])'],
                                  ['How to escape fixed discount guarantees over the term',
                                   'Move to NADAC or pass-through models and demand weekly or monthly '
                                   'reporting',
                                   'Use platform pricing that applies new network and manufacturer '
                                   'contracts immediately',
                                   'TheCoyPharmer ([H3p5Yw0Y-ek @ 00:14:30]); SmithRx ([ZuvAxUS0mII @ '
                                   '00:01:17])'],
                                  ['Who should actually run the PBM audit',
                                   'Hire an independent firm with in-sourced code that controls its own '
                                   'data',
                                   'Panel complains sponsors must hire outside auditors because '
                                   'self-auditing violates the contract',
                                   'Ethica Pharmacy Advisors ([z2vuJMYnjZE @ 00:01:53]); Relentless Health '
                                   'Value ([xHAyQelFkf8 @ 00:18:19])'],
                                  ['How to get rebate terms the plan can trust',
                                   'Hire competent counsel, negotiate down to definitions, and reject '
                                   'PBM-paid consultants',
                                   'Demand five clauses: pass-through, spread ban, audit rights, data '
                                   'ownership, fee disclosure',
                                   'Frier Levitt ([8mubYuuHvMI @ 00:03:34]); Benefits Blake ([wUzyX8bEvt0 '
                                   '@ 00:09:10])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first sponsor-side trap is the stale contract. Gary Alton watched a '
                              'multi-year deal freeze a client into “stale discounts,” with one exit '
                              'penalty topping $500K, and in the same case study a carrier negotiated 75% '
                              'but passed along 65%, quietly keeping a 10% spread [Cxvmh46o824 @ '
                              '00:44:25]. Alton puts typical audit findings at 10-30%, the size of leak a '
                              'frozen contract can hide. Alan Pannier explains why the lock hurts even '
                              'without fraud: over the term the PBM keeps winning better retail pharmacy '
                              'and manufacturer pricing, but the sponsor gets none of those gains because '
                              'its pricing is fixed [ZuvAxUS0mII @ 00:01:02]. Justine at TheCoyPharmer '
                              'flags the trap inside the guarantee itself: PBM guarantees to plan sponsors '
                              'are “typically a minimum level,” so a sponsor promised AWP minus 89% that '
                              'runs at minus 88% gets the shortfall paid [H3p5Yw0Y-ek @ 00:07:20]. The '
                              'catch is that the PBM runs separate MAC lists per guarantee, groups '
                              'sponsors into 5-8 cohorts, adjusts the lists daily or weekly, and may '
                              'migrate an overperforming sponsor onto a new MAC list [H3p5Yw0Y-ek @ '
                              '00:13:52]. The economics check is simple: without the monthly or weekly '
                              'reporting Justine tells resellers to demand, a sponsor cannot tell whether '
                              'its contractual floor quietly became its ceiling.',
                              'On rebates, the trap is believing the pass-through promise without seeing '
                              'the plumbing. Frier Levitt describes litigation that exposed PBM-owned '
                              'rebate aggregators demanding, say, 25 cents on the dollar for formulary '
                              'access, keeping about 30% and sending 60-70 cents to the PBM, which then '
                              "tells the plan “we're going to turn it all over to you” [8mubYuuHvMI @ "
                              '00:01:20]. Frier Levitt adds that Medicare Part D and Medicare Advantage '
                              'carry reporting duties while ERISA private plans have no such obligation, '
                              'so the private employer sees only what the contract forces [8mubYuuHvMI @ '
                              '00:02:16]. Benefits Blake puts a number on the damage: only 59% of '
                              'employers receive full traditional rebates and 57% full specialty rebates '
                              '[wUzyX8bEvt0 @ 00:11:06]. The second trap is the referee. Frier Levitt '
                              'calls consultants paid by the PBM a “real conflict of interest,” and Cora '
                              "Opsahl's panel describes big PBMs paying consultants per RFP while renewals "
                              'get pitched as “only up 4% or 6%” [xHAyQelFkf8 @ 00:16:01]. Even the audit '
                              'right gets hollowed out with pre-approved auditors, 250-claim samples, no '
                              'extrapolation and limited look-back, and the panel notes a sponsor must '
                              'hire an outside auditor because doing it in-house would violate the '
                              'contract, even though audits in that world find 30-40% overcharges.',
                              'On the pharmacy side, the failure modes are cash-flow bleeds and audit '
                              'compounding. A PA Pharmacists speaker filled a drug whose cost jumped from '
                              '$25 to $155 against a $55 MAC, a $100 loss on one fill, and lost at least '
                              '$1,500 in two weeks because PBMs cut MAC prices fast but lag on increases '
                              "[l81CzyzPR6M @ 00:01:11]. Frier Levitt's team says the top audit "
                              'discrepancy is inventory shortage, and some PBMs reconcile at the NDC '
                              'level, so buying a 50-count package against a 100-count billed NDC reads as '
                              'a shortage and can trigger full recovery [67He43cmPRc @ 00:17:51]. Frier '
                              "Levitt's New Jersey panel warns that shrugging off a $5,000 finding burns "
                              'pharmacies later: findings compound, as in $5,000 in 2021 and $25,000 in '
                              '2023 feeding a 2025 network review, so every finding gets appealed '
                              'regardless of size [hKqVi489zow @ 00:14:40]. Late fixes backfire too. '
                              'Collecting house-account copays only after an audit notice lands is a “red '
                              'flag” [67He43cmPRc @ 00:28:44], and copay evidence produced after the audit '
                              'starts gets rejected. The economics check: a $10,000 audit you ignore is '
                              'the down payment on a termination, and a MAC price you never appeal keeps '
                              'bleeding margin until the list finally moves.'],
               'table': {'caption': 'Firsthand failure modes, the damage reported, and the countermove '
                                    'practitioners teach',
                         'headers': ['Failure Mode',
                                     'What Practitioners Reported',
                                     'Countermove Taught',
                                     'Expert Source'],
                         'rows': [['Stale multi-year discounts backed by exit penalties',
                                   'One client faced an exit penalty above $500K while locked into stale '
                                   'discounts',
                                   'Renegotiate contracts annually and audit discounts quarterly as the C2 '
                                   'coalition does',
                                   'The Partners Group ([Cxvmh46o824 @ 00:44:25]); The Partners Group '
                                   '([Cxvmh46o824 @ 00:09:35])'],
                                  ['Rebate aggregator skims before the pass-through',
                                   'Aggregator keeps about 30% and passes 60-70 cents while PBM claims '
                                   'full turnover',
                                   'Negotiate down to the definitions section with competent counsel, not '
                                   'PBM-paid consultants',
                                   'Frier Levitt ([8mubYuuHvMI @ 00:01:20]); Frier Levitt ([8mubYuuHvMI @ '
                                   '00:03:34])'],
                                  ['MAC reimbursement goes underwater on generic fills',
                                   'Cost rose from $25 to $155 against a $55 MAC; $1,500 lost in two weeks',
                                   'Appeal MAC prices; the Pennsylvania bill requires MAC updates every 7 '
                                   'business days',
                                   'PA Pharmacists ([l81CzyzPR6M @ 00:00:40]); TheCoyPharmer ([H3p5Yw0Y-ek '
                                   '@ 00:05:34])'],
                                  ['Inventory shortage created by purchase timing gaps',
                                   '200 units bought in 2024 plus 200 in late 2023 against 300 dispensed',
                                   'Send all wholesaler, marketplace and pharmacy-to-pharmacy purchases '
                                   'and file bulk-purchase notifications',
                                   'Frier Levitt ([hKqVi489zow @ 00:24:29]); Frier Levitt ([hKqVi489zow @ '
                                   '00:06:59])'],
                                  ['Ignoring small audit findings to save staff time',
                                   'Pharmacies skip $5,000 to $10,000 audits, then findings compound into '
                                   'termination or complaints',
                                   'Contest every finding regardless of dollar amount and exhaust internal '
                                   'dispute steps first',
                                   'Frier Levitt ([67He43cmPRc @ 00:45:23]); Frier Levitt ([hKqVi489zow @ '
                                   '00:13:06])'],
                                  ['On-site audit failures on basic store operations',
                                   "Being closed on Presidents' Day led to a one-year wait to reapply",
                                   'Prepare refrigerator logs, PHI destruction, inventory separation and '
                                   'holiday staffing before visits',
                                   'Frier Levitt ([JTumBwWl7Mw @ 00:05:02]); Frier Levitt ([JTumBwWl7Mw @ '
                                   '00:06:10])'],
                                  ['Underpaid GLP-1 scripts inside a pass-through deal',
                                   'GLP-1 underpayment of about $130 per script makes pharmacies refuse to '
                                   'fill them',
                                   'Check both sides of the formula: plan charge basis versus pharmacy '
                                   'reimbursement basis',
                                   'Relentless Health Value ([xHAyQelFkf8 @ 00:13:20]); Relentless Health '
                                   'Value ([xHAyQelFkf8 @ 00:12:47])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Hard Stops Before You Sign, Renew, or Settle',
                           'body': 'Four stops drawn straight from the money practitioners watched '
                                   'sponsors and pharmacies lose.',
                           'items': ["Do not accept a pass-through label until the plan's charge basis "
                                     'matches pharmacy reimbursement; Cora Opsahl reports AWP-discount '
                                     'billing against acquisition-cost-plus reimbursement [Relentless '
                                     'Health Value — xHAyQelFkf8 @ 00:12:47].',
                                     'Do not sign a multi-year deal without annual repricing; stale '
                                     'discounts and an exit penalty above $500K trapped one client [The '
                                     'Partners Group — Cxvmh46o824 @ 00:44:25].',
                                     'Do not let a 100% rebate pass-through pledge end diligence; '
                                     'PBM-owned GPO admin fees remain a total black box [AHealthcareZ - '
                                     'Healthcare Finance Explained — yFJFnewKqw4 @ 00:03:01].',
                                     'Do not send purchase records for the listed claims only or skip a '
                                     'small audit; submit every purchase source for the full period [Frier '
                                     'Levitt — hKqVi489zow @ 00:06:59].']}}],
 'pull_quote': '“If you want to get bigger rebates, the easiest way to get bigger rebates and better '
               'terms, just make part of the RFP require that Cost Plus Drugs as part of the network and '
               'they will immediately give you a better deal to try to exclude us from the network.” — '
               'Mark Cuban, Relentless Health Value (xHAyQelFkf8 @ 00:18:34).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Rewrite the contract so the PBM charges the same ingredient cost and dispensing fee '
                      'it pays the pharmacy, with the admin fee as its only revenue [PBM Insider — '
                      'o57C9bK5ouI @ 00:01:59].',
                      'Price drugs in absolute dollars instead of AWP discounts, checking PBM generics '
                      'against the $25 Cost Plus imatinib benchmark [Relentless Health Value — xHAyQelFkf8 '
                      '@ 00:08:26].',
                      'Write Cost Plus Drugs into the RFP network requirement to force incumbents into a '
                      'better deal [Relentless Health Value — xHAyQelFkf8 @ 00:18:34].',
                      'Lock in the five clauses: rebate pass-through, spread ban, audit rights with '
                      'tolerable 30-day notice, data ownership, and fee disclosure [Benefits Blake — '
                      'wUzyX8bEvt0 @ 00:09:10].',
                      'Renegotiate annually, audit discounts quarterly, and expect typical audit findings '
                      'of 10-30% [The Partners Group — Cxvmh46o824 @ 00:56:10].',
                      'On the pharmacy side, self-audit regularly and keep independent purchase records '
                      'from every wholesaler before any audit notice arrives [Frier Levitt — 67He43cmPRc @ '
                      '00:53:08].'],
 'statutory_citations': [{'title': 'Relentless Health Value — Mark Cuban and Cora Opsahl: The Truth About '
                                   'Pass-Through PBM Contracts and Generic Compliance Ratios [00:12:47]',
                          'url': 'https://www.youtube.com/watch?v=xHAyQelFkf8&t=767s',
                          'relevance': 'Primary practitioner testimony on pass-through formula mismatch, '
                                       'audit limits, and the Cost Plus RFP tactic.'},
                         {'title': 'AHealthcareZ - Healthcare Finance Explained — PBM Deception on Rebate '
                                   'Pass-Through [00:08:25]',
                          'url': 'https://www.youtube.com/watch?v=yFJFnewKqw4&t=505s',
                          'relevance': 'Primary practitioner testimony on rebate pass-through covering '
                                       'only 13% of PBM profit and GPO admin fees.'},
                         {'title': 'TheCoyPharmer — Drug Pricing Indexes: Maximum Allowable Cost (MAC) '
                                   '[00:07:20]',
                          'url': 'https://www.youtube.com/watch?v=H3p5Yw0Y-ek&t=440s',
                          'relevance': 'Primary practitioner testimony on MAC guarantee reconciliation '
                                       'asymmetry and MAC-list migration.'},
                         {'title': 'Frier Levitt — PBM Audits & Network Compliance 2026: Critical '
                                   'Strategies for New Jersey Pharmacies [00:11:14]',
                          'url': 'https://www.youtube.com/watch?v=hKqVi489zow&t=674s',
                          'relevance': 'Primary practitioner testimony on appealing every audit finding '
                                       'and compounding findings leading to termination.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'o57C9bK5ouI',
                       'title': 'The PBM Insider - What is Spread Pricing?',
                       'channel': 'PBM Insider',
                       'author': 'PBM Insider',
                       'text': 'Spread pricing is the difference between the pricing in these two '
                               'contracts.',
                       'tip': 'Spread pricing is the difference between the pricing in these two '
                              'contracts.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=o57C9bK5ouI&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=o57C9bK5ouI&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0XFk1m3yGuY',
                       'title': 'PBM Spread Pricing for Generic Prescriptions Explained',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': 'The PBM and the pharmacy each profit about 23 cents, and the plan paid '
                               'almost exactly 25 times more.',
                       'tip': 'The PBM and the pharmacy each profit about 23 cents, and the plan paid '
                              'almost exactly 25 times more.',
                       'timestamp': 189,
                       'timestamp_seconds': 189,
                       'timestamp_label': '[00:03:09]',
                       'url': 'https://www.youtube.com/watch?v=0XFk1m3yGuY&t=189s',
                       'markdown': '[00:03:09](https://www.youtube.com/watch?v=0XFk1m3yGuY&t=189s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zoRFywXBoLM',
                       'title': 'February 25 2021 All Stakeholder Meeting - Specialty Pharmacy Carve-Out',
                       'channel': "Employers' Forum of Indiana",
                       'author': "Employers' Forum of Indiana",
                       'text': 'So you can see that trend, we saw a negative trend, our trend go down in '
                               '2017.',
                       'tip': 'So you can see that trend, we saw a negative trend, our trend go down in '
                              '2017.',
                       'timestamp': 318,
                       'timestamp_seconds': 318,
                       'timestamp_label': '[00:05:18]',
                       'url': 'https://www.youtube.com/watch?v=zoRFywXBoLM&t=318s',
                       'markdown': '[00:05:18](https://www.youtube.com/watch?v=zoRFywXBoLM&t=318s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cxvmh46o824',
                       'title': 'Healthcare Savings Via Pharmacy Benefit Management Programs for '
                                'Self-Funded Employers',
                       'channel': 'The Partners Group',
                       'author': 'The Partners Group',
                       'text': 'We had 86 new products launched last year and another 50 are expected in '
                               '2015.',
                       'tip': 'We had 86 new products launched last year and another 50 are expected in '
                              '2015.',
                       'timestamp': 781,
                       'timestamp_seconds': 781,
                       'timestamp_label': '[00:13:01]',
                       'url': 'https://www.youtube.com/watch?v=Cxvmh46o824&t=781s',
                       'markdown': '[00:13:01](https://www.youtube.com/watch?v=Cxvmh46o824&t=781s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'H3p5Yw0Y-ek',
                       'title': 'Drug Pricing Indexes: Maximum Allowable Cost (MAC)',
                       'channel': 'TheCoyPharmer',
                       'author': 'TheCoyPharmer',
                       'text': 'The MAC price is the price that the PBMs are reimbursing the pharmacies '
                               'for generic products.',
                       'tip': 'The MAC price is the price that the PBMs are reimbursing the pharmacies for '
                              'generic products.',
                       'timestamp': 74,
                       'timestamp_seconds': 74,
                       'timestamp_label': '[00:01:14]',
                       'url': 'https://www.youtube.com/watch?v=H3p5Yw0Y-ek&t=74s',
                       'markdown': '[00:01:14](https://www.youtube.com/watch?v=H3p5Yw0Y-ek&t=74s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '67He43cmPRc',
                       'title': 'PBM Audits & Network Compliance in 2026 What Pharmacies Need to Know Now',
                       'channel': 'Frier Levitt',
                       'author': 'Frier Levitt',
                       'text': "I've had instances of where pharmacy say it's $5,000, it's $10,000, I'm "
                               'too busy to otherwise challenge these results.',
                       'tip': "I've had instances of where pharmacy say it's $5,000, it's $10,000, I'm too "
                              'busy to otherwise challenge these results.',
                       'timestamp': 2723,
                       'timestamp_seconds': 2723,
                       'timestamp_label': '[00:45:23]',
                       'url': 'https://www.youtube.com/watch?v=67He43cmPRc&t=2723s',
                       'markdown': '[00:45:23](https://www.youtube.com/watch?v=67He43cmPRc&t=2723s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yFJFnewKqw4',
                       'title': 'PBM Deception on Rebate Pass-Through',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': 'They decreased their rebate profit from 48% to 13%.',
                       'tip': 'They decreased their rebate profit from 48% to 13%.',
                       'timestamp': 505,
                       'timestamp_seconds': 505,
                       'timestamp_label': '[00:08:25]',
                       'url': 'https://www.youtube.com/watch?v=yFJFnewKqw4&t=505s',
                       'markdown': '[00:08:25](https://www.youtube.com/watch?v=yFJFnewKqw4&t=505s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8mubYuuHvMI',
                       'title': 'Let’s Talk: Rebates and PBMs',
                       'channel': 'Frier Levitt',
                       'author': 'Frier Levitt',
                       'text': 'The aggregator keeps about 30 percent, passes 60 to 70 cents to the PBM, '
                               "and the PBM tells the plan we're going to turn it all over to you.",
                       'tip': 'The aggregator keeps about 30 percent, passes 60 to 70 cents to the PBM, '
                              "and the PBM tells the plan we're going to turn it all over to you.",
                       'timestamp': 80,
                       'timestamp_seconds': 80,
                       'timestamp_label': '[00:01:20]',
                       'url': 'https://www.youtube.com/watch?v=8mubYuuHvMI&t=80s',
                       'markdown': '[00:01:20](https://www.youtube.com/watch?v=8mubYuuHvMI&t=80s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z2vuJMYnjZE',
                       'title': 'PBM Audits: Why Independence Matters',
                       'channel': 'Ethica Pharmacy Advisors',
                       'author': 'Ethica Pharmacy Advisors',
                       'text': 'This is a complex space, and our goal is to really educate.',
                       'tip': 'This is a complex space, and our goal is to really educate.',
                       'timestamp': 95,
                       'timestamp_seconds': 95,
                       'timestamp_label': '[00:01:35]',
                       'url': 'https://www.youtube.com/watch?v=z2vuJMYnjZE&t=95s',
                       'markdown': '[00:01:35](https://www.youtube.com/watch?v=z2vuJMYnjZE&t=95s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JTumBwWl7Mw',
                       'title': 'Navigating PBM Audits: Ensuring Pharmacy Compliance and Mitigating Risks',
                       'channel': 'Frier Levitt',
                       'author': 'Frier Levitt',
                       'text': 'Signature logs and doorstep deliveries lead to patient denials, and audits '
                               'serve as a source of revenue for PBMs.',
                       'tip': 'Signature logs and doorstep deliveries lead to patient denials, and audits '
                              'serve as a source of revenue for PBMs.',
                       'timestamp': 1645,
                       'timestamp_seconds': 1645,
                       'timestamp_label': '[00:27:25]',
                       'url': 'https://www.youtube.com/watch?v=JTumBwWl7Mw&t=1645s',
                       'markdown': '[00:27:25](https://www.youtube.com/watch?v=JTumBwWl7Mw&t=1645s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wUzyX8bEvt0',
                       'title': 'Best-in-Class Transparent PBMs: What the Contract Has to Say',
                       'channel': 'Benefits Blake',
                       'author': 'Benefits Blake',
                       'text': "Don't evaluate your PBM on their pitch deck.",
                       'tip': "Don't evaluate your PBM on their pitch deck.",
                       'timestamp': 801,
                       'timestamp_seconds': 801,
                       'timestamp_label': '[00:13:21]',
                       'url': 'https://www.youtube.com/watch?v=wUzyX8bEvt0&t=801s',
                       'markdown': '[00:13:21](https://www.youtube.com/watch?v=wUzyX8bEvt0&t=801s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l81CzyzPR6M',
                       'title': 'Maximum Allowable Cost pricing or MAC pricing on pharmacies',
                       'channel': 'PA Pharmacists',
                       'author': 'PA Pharmacists',
                       'text': 'We lost at least $1,500 in two weeks, and PBMs lower MAC prices quickly '
                               'but lag when costs go up.',
                       'tip': 'We lost at least $1,500 in two weeks, and PBMs lower MAC prices quickly but '
                              'lag when costs go up.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=l81CzyzPR6M&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=l81CzyzPR6M&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5rIKr0wfdwo',
                       'title': 'PBM Drug Rebates',
                       'channel': 'Mattingly House',
                       'author': 'Mattingly House',
                       'text': 'When the outcomes are equal, the drug with the much better rebate is the '
                               'one that gets covered.',
                       'tip': 'When the outcomes are equal, the drug with the much better rebate is the '
                              'one that gets covered.',
                       'timestamp': 391,
                       'timestamp_seconds': 391,
                       'timestamp_label': '[00:06:31]',
                       'url': 'https://www.youtube.com/watch?v=5rIKr0wfdwo&t=391s',
                       'markdown': '[00:06:31](https://www.youtube.com/watch?v=5rIKr0wfdwo&t=391s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hKqVi489zow',
                       'title': 'PBM Audits & Network Compliance 2026: Critical Strategies for New Jersey '
                                'Pharmacies',
                       'channel': 'Frier Levitt',
                       'author': 'Frier Levitt',
                       'text': 'Unresolved discrepancies usually means increased risk of termination.',
                       'tip': 'Unresolved discrepancies usually means increased risk of termination.',
                       'timestamp': 709,
                       'timestamp_seconds': 709,
                       'timestamp_label': '[00:11:49]',
                       'url': 'https://www.youtube.com/watch?v=hKqVi489zow&t=709s',
                       'markdown': '[00:11:49](https://www.youtube.com/watch?v=hKqVi489zow&t=709s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xHAyQelFkf8',
                       'title': 'Mark Cuban and Cora Opsahl: The Truth About Pass-Through PBM Contracts '
                                'and Generic Compliance Ratios',
                       'channel': 'Relentless Health Value',
                       'author': 'Relentless Health Value',
                       'text': "You don't have to work with the big PBMs.",
                       'tip': "You don't have to work with the big PBMs.",
                       'timestamp': 1179,
                       'timestamp_seconds': 1179,
                       'timestamp_label': '[00:19:39]',
                       'url': 'https://www.youtube.com/watch?v=xHAyQelFkf8&t=1179s',
                       'markdown': '[00:19:39](https://www.youtube.com/watch?v=xHAyQelFkf8&t=1179s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZuvAxUS0mII',
                       'title': 'Modern PBM 101 with Alan Pannier, PharmD, MBA: Continuous Pricing '
                                'Improvement',
                       'channel': 'SmithRx',
                       'author': 'SmithRx',
                       'text': 'What this looks like in reality is consistent improvements and a reduction '
                               "in your per member per month spend over the course that you're with "
                               'SmithRx.',
                       'tip': 'What this looks like in reality is consistent improvements and a reduction '
                              "in your per member per month spend over the course that you're with "
                              'SmithRx.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=ZuvAxUS0mII&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=ZuvAxUS0mII&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xHAyQelFkf8',
                       'title': 'Mark Cuban and Cora Opsahl: The Truth About Pass-Through PBM Contracts '
                                'and Generic Compliance Ratios',
                       'channel': 'Relentless Health Value',
                       'author': 'Relentless Health Value',
                       'text': 'And if you want to get bigger rebates, the easiest way to get bigger '
                               'rebates and better terms, just make part of the RFP require that Cost Plus '
                               'Drugs as part of the network and they will immediately give you a better '
                               'deal to try to exclude us from the network.',
                       'tip': 'And if you want to get bigger rebates, the easiest way to get bigger '
                              'rebates and better terms, just make part of the RFP require that Cost Plus '
                              'Drugs as part of the network and they will immediately give you a better '
                              'deal to try to exclude us from the network.',
                       'timestamp': 1114,
                       'timestamp_seconds': 1114,
                       'timestamp_label': '[00:18:34]',
                       'url': 'https://www.youtube.com/watch?v=xHAyQelFkf8&t=1114s',
                       'markdown': '[00:18:34](https://www.youtube.com/watch?v=xHAyQelFkf8&t=1114s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hKqVi489zow',
                       'title': 'PBM Audits & Network Compliance 2026: Critical Strategies for New Jersey '
                                'Pharmacies',
                       'channel': 'Frier Levitt',
                       'author': 'Frier Levitt',
                       'text': 'Certain PBMs, however, only give you a month.',
                       'tip': 'Certain PBMs, however, only give you a month.',
                       'timestamp': 1576,
                       'timestamp_seconds': 1576,
                       'timestamp_label': '[00:26:16]',
                       'url': 'https://www.youtube.com/watch?v=hKqVi489zow&t=1576s',
                       'markdown': '[00:26:16](https://www.youtube.com/watch?v=hKqVi489zow&t=1576s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
