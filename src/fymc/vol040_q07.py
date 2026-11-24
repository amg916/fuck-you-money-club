from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'reference-based-pricing-and-direct-contracting',
 'question_prompt': 'How does reference-based pricing and direct contracting replace PPO network '
                    'discounts, and how are balance bills and provider pushback handled?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Reference-Based Pricing and Direct Contracting',
 'subtitle': 'RBP vs. PPO and commercial claims pricing, Medicare-plus pricing, chargemasters, negotiation '
             'best practices, surprise-billing interaction, member advocacy, RBP costs, and direct '
             'employer–provider contracts',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree reference-based pricing is just a different way to pay a claim '
                      'inside a self-funded or level-funded plan: build up from Medicare instead of '
                      'discounting down from a hospital chargemaster. Quoted savings run 20 to 40 percent, '
                      'and ClaimDOC reports a 300-employee agricultural group cutting plan spend 41.4 '
                      'percent, from $819 to $480 per employee per month, with zero known balance bills. '
                      'The street mechanics: pay facilities the greater of Medicare plus 25 or cost plus '
                      '20, clinically audit every inpatient bill, pre-sign physicians through outreach '
                      'that wins 95 percent acceptance, and cut single-case agreements on the rest. '
                      "Operators split on posture, from Montana's arm-twisting that cut hospital pay to "
                      '200-220 percent of Medicare, to pay-and-defend versus negotiate-and-settle, while '
                      'one producer reverted a client to PPO within months over balance-bill complaints.',
 'key_metrics': [{'label': 'Year-One Plan Spend Reduction (300-Employee Agricultural Group)',
                  'metric': 'Year-One Plan Spend Reduction (300-Employee Agricultural Group)',
                  'value': '41.4% ($819 to $480 per covered employee per month; $1.6M saved)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Broker-matured year-one claims on a blue-collar California agricultural '
                             'client: stop-loss renewal at minus 10.1%, zero known balance bills across '
                             '2,000-plus claims, three access issues.',
                  'source': 'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:45:10])'},
                 {'label': 'Physician Acceptance After Proactive Outreach',
                  'metric': 'Physician Acceptance After Proactive Outreach',
                  'value': '95%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Acceptance rate ClaimDOC reports when it calls member-nominated doctors '
                             'before the effective date and explains payment terms, payer ID, and ID card.',
                  'source': 'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:12:17])'},
                 {'label': 'Montana State Plan Hospital Reimbursement Reset',
                  'metric': 'Montana State Plan Hospital Reimbursement Reset',
                  'value': '191-611% of Medicare cut to 200-220%; $15M hospital + $5M Rx = $20M saved',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Marilyn Bartlett's RBP negotiation for Montana state employees, combining "
                             'cost-coverage analysis with arm-twisting tactics.',
                  'source': 'AHealthcareZ - Healthcare Finance Explained ([gpm3vtKEf5U @ 00:01:05])'},
                 {'label': 'ClaimDOC Facility Payment Formula',
                  'metric': 'ClaimDOC Facility Payment Formula',
                  'value': 'Greater of Medicare + 25% or hospital self-reported cost + 20%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Standard facility pricing, run line by line, using the cost-of-services '
                             'report every Medicare-participating hospital files with CMS.',
                  'source': 'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:24:54])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner who prices claims for a living lands on the same core '
                              'mechanic: reference-based pricing is not a plan, it is a different way to '
                              'pay a claim. Lester Morales frames the PPO as top-down, starting from a '
                              "hospital's billed charge and shaving a discount, while RBP is bottom-up, "
                              'starting from Medicare and paying a percentage above it, with both routes '
                              'answering the same question of what the plan reimburses for a knee surgery '
                              'or an MRI [xVuFXA-gN8g @ 00:05:18]. Omar Arif of ClaimDOC goes further, '
                              'calling the product network replacement rather than RBP, and pointing out '
                              'that every big carrier already reference-prices out-of-network claims and '
                              'already pays physicians Medicare plus a markup, so RBP is baked into every '
                              'group plan in the country [A__ZFq9k8Ds @ 00:22:42]. Tom Stein of American '
                              'Trust Administrators strips the chargemaster down to a restaurant menu that '
                              'only the uninitiated believe is real, and says RBP discounts that menu '
                              'entirely and keys off what the hospital accepts from its biggest payer, the '
                              'government [D3AuT-Ki3nw @ 00:02:52]. Mike Kupa of Remodel Benefits calls '
                              "the savings 'literally just math': egregious providers sitting inside "
                              'carrier contracts simply get paid less, and that gap is where the '
                              "employer's money comes back [vCzjI43ZWVI @ 00:03:26].",
                              'The savings bands cluster tightly across operators who run the numbers '
                              'independently. Kupa tells employers to expect 20 to 30 percent on medical '
                              'spend, sometimes more, after years of implementing and maintaining RBP '
                              'plans [vCzjI43ZWVI @ 00:00:49]. Arif says ClaimDOC has historically '
                              'promised 25 to 35 percent of overall spend depending on geography and plan '
                              'structure, and that its 2022 book was tracking into the high 30s or low 40s '
                              'against Kaiser Family Foundation figures, measured on true cost per '
                              'employee and per family rather than on discount percentages [A__ZFq9k8Ds @ '
                              '00:37:45]. The funding prerequisite is just as uniform. Howard Deihl of The '
                              'General Agency states RBP contracts are only written self-funded or '
                              'level-funded, never in the fully insured market, are medically '
                              'underwritten, and in the level-funded version unused claim funds get '
                              'refunded to the employer, so low utilization stacks extra savings on top of '
                              'the rate cut [FPcS3pupwwA @ 00:05:33]. Ryan of Holloway Benefit Concepts '
                              'confirms underwriting and risk analysis still apply, pitches the model '
                              'squarely at small and mid-sized businesses, and reports two clients on RBP '
                              'whose claim costs and overall premiums dropped two years in a row '
                              '[2dsXkvZasDU @ 00:01:14]. Deihl adds that RBP coinsurance can run anywhere '
                              'from 50 to 90 percent, but the single out-of-pocket maximum is the number '
                              'operators sell on.',
                              'The third consensus point is that RBP fails without member education and '
                              'advocacy wrapped around it. Rhett Robbins says employees can visit '
                              'virtually any provider but need to confirm in advance that the provider '
                              'accepts RBP pricing, with a third-party advocate stepping in to negotiate '
                              'any billing dispute, and folds direct contracting with preferred providers '
                              'into the same toolkit [8begy-typh4 @ 00:01:24]. Benefits Studio names the '
                              'two catches every buyer has to price in: without a contract a hospital can '
                              'balance bill the employee for the rest of its charge, and some hospitals '
                              'refuse to take part at all, which leaves real gaps in access [noY8cLblMi4 @ '
                              '00:01:31]. Arif is blunt that nobody saves a health plan 20 to 40, '
                              'sometimes 50 percent without disruption, and that the fix is telling '
                              'clients up front what will break and how it gets fixed, then repeating it '
                              'in a constant drip of communication all year [mPaz9R2yMrs @ 00:08:48]. '
                              'Marty Makary, in a clip run by both Imagine360 and ELAP, supplies the macro '
                              'case operators lean on when the noise starts: hospital prices have no '
                              'orbit, they need to be anchored to something, and reference-based pricing '
                              'is that anchor, with the added promise of reining in surprise billing and '
                              'ensuring claims are paid at a fair amount [U6ZwMY7UtFU @ 00:02:01].'],
               'table': {'caption': 'Where RBP and Direct-Contracting Practitioners Agree',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reports',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['RBP is a payment method, not a separate plan',
                                   'PPO discounts top-down off billed charge; RBP builds bottom-up from '
                                   'Medicare plus a percentage',
                                   'Treat it as a repricing swap inside a self-funded plan, not a new '
                                   'product',
                                   'Dysrupt Healthcare Podcast ([xVuFXA-gN8g @ 00:05:18])'],
                                  ['Savings come from paying egregious providers less money',
                                   'Illustrative carrier contract lands near 250% of Medicare versus a '
                                   '150% RBP target',
                                   'Model savings on actual provider payment, never on headline discount '
                                   'percentages',
                                   'Remodel Benefits ([vCzjI43ZWVI @ 00:02:07])'],
                                  ['Target multiples sit comfortably above the Medicare floor',
                                   'Quoted ranges run 150-200% of Medicare, typically higher than what '
                                   'Medicare pays',
                                   'Set the multiple high enough that hospitals keep a healthy margin '
                                   'without gouging',
                                   'Holloway Benefit Concepts ([2dsXkvZasDU @ 00:00:24])'],
                                  ['Funding structure is the hard prerequisite for every deal',
                                   'RBP products are only written self-funded or level-funded, and they '
                                   'are medically underwritten',
                                   'Move the group off fully insured paper before pitching any repricing '
                                   'program',
                                   'The General Agency ([FPcS3pupwwA @ 00:01:17])'],
                                  ['Commercial hospital prices are untethered from any benchmark',
                                   'RAND found employers paid hospitals 254% of Medicare in 2022, topping '
                                   '300% in eight states',
                                   'Lead the CFO conversation with the commercial-to-Medicare gap as the '
                                   'savings story',
                                   'Benefits Studio ([noY8cLblMi4 @ 00:01:31])'],
                                  ['Member education and advocacy are mandatory, not optional extras',
                                   'Members must confirm provider acceptance in advance; advocates '
                                   'negotiate every billing dispute',
                                   'Fund advocacy and communications before the effective date or expect '
                                   'balance-bill noise',
                                   'Rhett Robbins ([8begy-typh4 @ 00:01:24])'],
                                  ['Price anchoring is the cure for non-competitive hospital markets',
                                   'Makary says prices with no orbit need an anchor, and reference-based '
                                   'pricing supplies it',
                                   'Frame RBP to leadership as anchoring runaway prices rather than '
                                   'shifting cost to staff',
                                   'ELAP Services ([UcjjCTQMOV4 @ 00:02:03])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The rate engine is where operators make or lose the deal. ClaimDOC prices '
                              'every facility claim two ways, Medicare plus a 25 percent markup and the '
                              "hospital's own self-reported cost plus a 20 percent markup, then pays "
                              'whichever is higher; the cost figure comes from the cost-of-services report '
                              'every Medicare hospital must file with CMS, which Arif argues is fully '
                              'loaded because hospitals use it to set their own government reimbursement '
                              '[mPaz9R2yMrs @ 00:24:54]. The math runs line by line, so the plan can '
                              'defend every payment as fair and reasonable, and Arif, self-described as '
                              'aggressive, says a flat-Medicare program a broker touted on LinkedIn would '
                              "scare even Arif [A__ZFq9k8Ds @ 00:48:56]. Kupa's worked example shows where "
                              'the spread lives: a $10,000 billed procedure with a 62.5 percent carrier '
                              'discount pays $3,750, roughly 250 percent of Medicare; Medicare itself pays '
                              '$1,500; an RBP plan at 150 percent pays $2,250, an effective 77.5 percent '
                              'discount [vCzjI43ZWVI @ 00:01:46]. Deihl gives the carrier comparison '
                              'operators quote against, with insurers averaging about 140 percent of '
                              'Medicare for hospital services and 120 to 125 percent for physician '
                              'services, higher or lower depending on the carrier [FPcS3pupwwA @ '
                              '00:00:41].',
                              "Access is engineered before the first claim drops. ClaimDOC's Pave the Way "
                              "program pulls the consultant's top utilization report, lets members "
                              'nominate their own doctors during open enrollment and all year, then calls '
                              'each office with a fixed script: here is how we pay, how fast we pay, the '
                              'payer ID, what the card looks like, and will you keep charging the $25 '
                              'copay; that outreach lands about a 95 percent physician acceptance rate '
                              '[mPaz9R2yMrs @ 00:12:17]. Facility care is left to flow through normal '
                              'pre-certification: Arif estimates roughly 85 percent of outpatient '
                              'procedures clear with no friction, eight or nine of every ten flagged cases '
                              'settle through a ten-person provider relations team run by a former '
                              'hospital executive, leaving one or two percent that need a delay or a '
                              'redirect to another facility [mPaz9R2yMrs @ 00:21:38]. In markets locked by '
                              'one dominant system, the plan B is contracting freestanding ambulatory '
                              'surgery centers, while ERs stay covered because the Consolidated '
                              'Appropriations Act bars them from balance billing the member [A__ZFq9k8Ds @ '
                              "00:38:40]. Eric Bricker's direct-contracting stack mirrors this: bundled or "
                              'discounted fee-for-service rates, an independent TPA loading a '
                              'client-specific network, zero out-of-pocket benefit design, and a '
                              'navigation service [xcu6bvj22fc @ 00:02:50].',
                              "The back end is a claims-defense machine. Arif relays the ClaimDOC CEO's "
                              'estimate that the clinical team of nurses and coding experts scrapes 25 to '
                              '30 percent of the dollars off any inpatient stay before repricing even '
                              'starts [A__ZFq9k8Ds @ 00:33:00]. The marquee catch is ICU unbundling: Arif '
                              'cites Stanford billing up to $80,000 a day for what should be an all-in per '
                              'diem, and COVID-era claims where oxygen, ventilator, ECMO and even nursing '
                              'were split out until bills hit $23 million and tripped PPO outlier clauses, '
                              'turning a presumed 50 percent discount into 15 percent [mPaz9R2yMrs @ '
                              '00:35:26]. Every audited facility claim goes to the hospital by certified '
                              "mail with appeal instructions and the hospital's own self-reported "
                              'financials; if the provider later bills the member, a notice goes to that '
                              'same address stating the check was cashed and the plan paid per the plan '
                              'document. ClaimDOC itself is paid a percentage of billed charge, capped per '
                              'claim, and Arif says experienced stop-loss carriers grant ClaimDOC '
                              'decrements that more than offset the fee against a fixed-PEPM vendor '
                              "[A__ZFq9k8Ds @ 00:34:41]. Deihl's carriers go one step further on "
                              'collections, mailing providers a letter telling them not to report the '
                              'member while a claims negotiation runs [FPcS3pupwwA @ 00:07:38].'],
               'table': {'caption': 'RBP and Direct-Contracting Levers, Numbers and Execution',
                         'headers': ['Lever',
                                     'Exact Mechanic or Number',
                                     'How Operators Run It',
                                     'Expert Source'],
                         'rows': [['Facility rate formula used on every hospital claim',
                                   'Greater of Medicare plus 25% or CMS-reported hospital cost plus 20%, '
                                   'line by line',
                                   'Pull hospital cost reports and price each line against both benchmarks',
                                   'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:24:54])'],
                                  ['Physician rate pitched to independent doctors',
                                   'Medicare plus 25% versus a Dallas blended commercial average near 103% '
                                   'of Medicare',
                                   'Sell physicians on higher, faster, simpler payment than their network '
                                   'contracts',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:45:45])'],
                                  ['Clinical pre-audit before any repricing happens',
                                   'Nurses and coding experts scrape 25-30% of inpatient stay dollars '
                                   'first',
                                   'Audit every facility bill clinically before applying the Medicare '
                                   'multiple',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:33:00])'],
                                  ['Montana hardball hospital negotiation playbook',
                                   'Hospital rates moved from 191-611% down to 200-220% of Medicare; $20M '
                                   'saved overall',
                                   'Pair cost-coverage analysis with threats to publish rates and '
                                   'executive contact details',
                                   'AHealthcareZ - Healthcare Finance Explained ([gpm3vtKEf5U @ '
                                   '00:01:24])'],
                                  ['Side-by-side PPO versus RBP rate quote',
                                   '29-life older group: $678 employee-only on PPO versus $334 on RBP; '
                                   'spouse $1,545 versus $757',
                                   'Quote both plans together and highlight the single $5,000 '
                                   'out-of-pocket cap',
                                   'The General Agency ([FPcS3pupwwA @ 00:04:33])'],
                                  ['Vendor fee structure and stop-loss offset',
                                   'Percentage of billed charge, capped per claim, offset by stop-loss '
                                   'decrements',
                                   'Compare total cost against a $30 PEPM vendor carrying higher stop-loss '
                                   'rates',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:34:41])'],
                                  ['Direct contract administration through a TPA',
                                   'Independent TPA builds a client-specific network with custom allowed '
                                   'amounts per code',
                                   'Pair it with zero out-of-pocket benefit design and a dedicated '
                                   'navigation service',
                                   'AHealthcareZ - Healthcare Finance Explained ([xcu6bvj22fc @ '
                                   '00:02:50])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Leverage Plays the Operators Actually Use',
                           'body': 'These are the specific pressure points practitioners pulled to get '
                                   'hospitals, physicians, and members to accept a Medicare-anchored '
                                   'price.',
                           'items': ['Rational analysis alone did not close Montana; the deal closed after '
                                     'threats to publish commercial payment rates and the personal emails '
                                     'and cell numbers of hospital board members, CEOs and CFOs, plus '
                                     'union pressure and an offer to ship members out of state with free '
                                     'transportation [AHealthcareZ - Healthcare Finance Explained — '
                                     'gpm3vtKEf5U @ 00:03:19].',
                                     'Target reimbursement sandwiched between government and commercial '
                                     'payers so a nonprofit system cannot credibly call the payment unfair '
                                     'when it beats their biggest payer [Dysrupt Healthcare Podcast — '
                                     'mPaz9R2yMrs @ 00:27:32].',
                                     "Run a dual option on the UMR and United network: ClaimDOC's first "
                                     'case offered a $2,000 deductible at $130 a month versus $200 a month '
                                     'for United, and 350 enrolled with ClaimDOC while six picked United '
                                     '[Self-Funded — A__ZFq9k8Ds @ 00:55:41].',
                                     'In direct contracting, the bargaining chips are concentrated '
                                     'headcount for steerage and faster payment, since major carriers can '
                                     'take 30, 60, even 90 days to pay the provider [AHealthcareZ - '
                                     'Healthcare Finance Explained — xcu6bvj22fc @ 00:02:17].']},
               'sop_steps': [{'step': 1,
                              'title': 'Lock the Funding and the Plan Document',
                              'action': 'Confirm self-funded status, hire the TPA and RBP vendor, and '
                                        'write Medicare-based rates into the plan document.',
                              'detail': 'Self-fund first, then hire a TPA or RBP vendor, write the '
                                        'Medicare-based rates into the plan document, and train HR before '
                                        'open enrollment [Benefits Studio — noY8cLblMi4 @ 00:00:33].'},
                             {'step': 2,
                              'title': 'Pave the Way Before Go-Live',
                              'action': 'Start implementation two to three months out and call every '
                                        'high-use and member-nominated provider.',
                              'detail': 'The implementation team engages two to three months before the '
                                        'effective date, works the top utilization report, and collects '
                                        'member-nominated doctors for proactive outreach [Self-Funded — '
                                        'A__ZFq9k8Ds @ 00:41:13].'},
                             {'step': 3,
                              'title': 'Staff a Single-Case Agreement Desk',
                              'action': 'Keep provider relations on standby to negotiate facility '
                                        'agreements the moment intake flags the plan.',
                              'detail': 'A ten-person provider relations team led by a former hospital '
                                        'executive opens negotiation immediately and cuts single-case or '
                                        'single-patient agreements to avoid delays or redirects [Dysrupt '
                                        'Healthcare Podcast — mPaz9R2yMrs @ 00:20:33].'},
                             {'step': 4,
                              'title': 'Audit, Mail, and Defend Every Facility Claim',
                              'action': 'Audit and reprice each facility claim, send the certified packet, '
                                        'and answer any balance bill in writing.',
                              'detail': 'Send the audit by certified mail with appeal instructions and the '
                                        "hospital's own financials, then answer any member balance bill "
                                        'with a notice to the same address [Dysrupt Healthcare Podcast — '
                                        'mPaz9R2yMrs @ 00:40:11].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fault line is the multiple itself. Ryan at Holloway Benefit '
                              'Concepts sells plans where every claim is paid at a higher percentage of '
                              'Medicare, typically 150% to 200%, and pitches it as an exit from back-door, '
                              'no-transparency carrier-hospital negotiations [2dsXkvZasDU @ 00:00:24]. '
                              'Omar Arif at ClaimDOC runs a tighter, line-by-line formula: facilities get '
                              "Medicare plus 25% or the hospital's own self-reported cost plus 20%, "
                              'whichever is higher, and that floor is what lets ClaimDOC defend every '
                              'payment as fair and reasonable. Arif says a broker moving a client to flat '
                              'Medicare would scare even an operator as aggressive as Arif [A__ZFq9k8Ds @ '
                              '00:48:56]. Howard Deihl at The General Agency puts the incumbent baseline '
                              'on the table: carriers are reimbursing about 140% of Medicare for hospital '
                              'services and 120% to 125% for physician services, with some higher and some '
                              'lower depending on the carrier [FPcS3pupwwA @ 00:00:41]. Tom Stein at '
                              'American Trust Administrators attacks from the opposite flank, arguing that '
                              'paying 50% more than the state pays means small business is getting '
                              'fleeced, while hospitals counter that government underpayment forces '
                              'private plans to subsidize them [D3AuT-Ki3nw @ 00:03:28]. Same chassis, '
                              'different price anchors, and each one moves acceptance, savings, and '
                              'defensibility in a different direction.',
                              'Negotiation posture splits practitioners even harder. Arif lays out the two '
                              'primary ways to run RBP: pay and defend, where the plan pays what it judges '
                              'fair and defends the claim, or negotiate and settle, which can be better '
                              'for a member in certain scenarios but sets a bad precedent and dilutes plan '
                              'assets. ClaimDOC keeps both weapons plus single case agreements and direct '
                              'contracts under one roof, with legal, provider relations, and member '
                              'services in-house [A__ZFq9k8Ds @ 00:29:51]. Dr. Eric Bricker at '
                              'AHealthcareZ argues rational analysis alone did not seal the deal in '
                              "Montana: Marilyn Bartlett's analysis found Medicare covered 92% of hospital "
                              'costs, yet the agreement only closed after arm twisting, including threats '
                              'to publish commercial payment rates and the personal cell phone numbers of '
                              "hospital board members, CEOs, and CFOs [gpm3vtKEf5U @ 00:03:19]. Bricker's "
                              'direct-contracting playbook runs on volume instead of threats: a '
                              'concentrated workforce gives the employer steerage as leverage at the table '
                              'with independent physician practices and ambulatory surgery centers '
                              '[xcu6bvj22fc @ 00:01:02]. Carrie Nixon at Healthcare Solutions Connection '
                              'reports Boeing going straight to two local accountable care organizations '
                              'in Puget Sound, where 30% of employees chose the preferred partnership '
                              'option in year one with an 8.5 out of 10 satisfaction rating [ypiI6d2Bnkk @ '
                              '00:01:53].',
                              'The fee model and the rollout architecture are the third split. Arif '
                              'defends ClaimDOC taking a percentage of billed charge, capped per claim, '
                              'over a flat fee: on a 200-life case where nobody hits the hospital for six '
                              'months, the employer pays $30 PEPM to a fixed-fee vendor or nothing to '
                              'ClaimDOC, and stop-loss carriers that know the model hand out decrements '
                              '[A__ZFq9k8Ds @ 00:34:13]. Benefits Studio counters that there is no public '
                              'price list, every TPA and RBP vendor fee is quoted, and Willis Towers '
                              'Watson warns repricing fees can eat into the saving [noY8cLblMi4 @ '
                              '00:01:12]. On architecture, Arif rejects RBP ever becoming the norm and '
                              'expects a hybrid with PPOs; ClaimDOC already runs dual-option enrollments, '
                              'and on the first one six employees picked the United Healthcare plan while '
                              '350 picked ClaimDOC at a lower monthly premium [A__ZFq9k8Ds @ 00:55:41]. '
                              'Adam Rousseau of the Fiat Group, speaking on Partners MGU, reads surprise '
                              'billing rules as a huge opportunity rather than the end of RBP and sees RBP '
                              'eventually becoming an RBP network built on direct contracting, while host '
                              'Vince Lewis reports a producer forced back to a conventional PPO within '
                              'months [YEFRBSmT3IE @ 00:03:08]. One camp bets on pure network replacement; '
                              'the other wants a network to fall back on.'],
               'table': {'caption': 'Side-by-Side Playbooks: Where RBP and Direct Contracting Operators '
                                    'Split',
                         'headers': ['Decision Point',
                                     'Camp A Position',
                                     'Camp B Position',
                                     'Expert Source'],
                         'rows': [['Payment multiple set for facility and hospital claims',
                                   'Holloway prices every single claim at 150% to 200% of Medicare',
                                   'ClaimDOC pays Medicare plus 25% or cost plus 20%, whichever is higher',
                                   'Holloway Benefit Concepts ([2dsXkvZasDU @ 00:00:24]); Self-Funded '
                                   '([A__ZFq9k8Ds @ 00:48:56])'],
                                  ['Claim dispute posture taken with hospital billing departments',
                                   'Pay and defend the claim as fair and reasonable under the plan',
                                   'Negotiate and settle, which sets a bad precedent and dilutes plan '
                                   'assets',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:29:51])'],
                                  ['Leverage used to win a hospital agreement on reimbursement',
                                   'Rational analysis showing Medicare covered 92% of Montana hospital '
                                   'costs',
                                   'Arm twisting: threaten to publish commercial rates and executive cell '
                                   'numbers',
                                   'AHealthcareZ - Healthcare Finance Explained ([gpm3vtKEf5U @ '
                                   '00:03:19])'],
                                  ['Network replacement versus a direct contract with providers',
                                   'Open Access plan with proactive physician outreach landing roughly 95% '
                                   'acceptance',
                                   'Direct contract built on steerage from a concentrated employee base',
                                   'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:12:17]); AHealthcareZ - '
                                   'Healthcare Finance Explained ([xcu6bvj22fc @ 00:01:02])'],
                                  ['Vendor fee structure charged against the plan savings',
                                   'Percentage of billed charge with a per-claim cap and stop-loss '
                                   'decrements',
                                   'Quoted TPA and repricing fees that Willis Towers Watson warns can eat '
                                   'savings',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:34:13]); Benefits Studio ([noY8cLblMi4 '
                                   '@ 00:01:12])'],
                                  ['Full replacement versus a hybrid enrollment choice for employees',
                                   'Dual-option enrollment where 350 chose ClaimDOC and six chose United '
                                   'Healthcare',
                                   'Boeing ran an ACO option beside its standard self-funded plan, drawing '
                                   '30% enrollment',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:55:41]); Healthcare Solutions '
                                   'Connection ([ypiI6d2Bnkk @ 00:01:53])'],
                                  ['How to read surprise billing rules for an RBP plan',
                                   'Huge opportunity that pushes RBP toward a direct-contracted RBP '
                                   'network',
                                   'Arbitration ignores Medicare pricing and keys off average network '
                                   'rates instead',
                                   'Partners MGU ([YEFRBSmT3IE @ 00:03:08]); Partners MGU ([YEFRBSmT3IE @ '
                                   '00:04:33])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The fastest reversal on record is a full unwind. Vince Lewis at Partners '
                              'MGU took a call from a producer whose January RBP client had to convert '
                              'back to a conventional PPO just a few months in, because employees kept '
                              'complaining about balance bills from the local provider and requests for '
                              'cash upfront before treatment; Lewis calls it a morale issue at best and a '
                              'public relations nightmare in the media [YEFRBSmT3IE @ 00:00:29]. Arif '
                              'traces the stigma to early vendors that ended up in litigious fights with '
                              'hospitals or acted as repricers that slammed a plan in to make a sale with '
                              'no advocacy or education, and admits deals have gone sideways on ClaimDOC '
                              'groups too when the team could not get access to HR and rank-and-file '
                              'employees [mPaz9R2yMrs @ 00:08:26]. Micro-Dyn spells out the mechanism: '
                              'when providers reject the benchmark rate, the patient can receive a balance '
                              'bill for the difference [Hz5wBrKavxY @ 00:01:14]. Deihl adds the '
                              'collections trap, where billing companies historically dinged credit right '
                              'away and sent accounts straight to collections, so the carriers The General '
                              'Agency works with mail hold letters to providers while a claim is under '
                              'negotiation [FPcS3pupwwA @ 00:07:38].',
                              'Access friction is the second bottleneck, and it is measurable. Arif '
                              'estimates about 85% of outpatient facility claims flow through with no '
                              'problems before care, leaving roughly 15% with friction; eight or nine of '
                              'every ten of those get worked out, which leaves one to two percent of '
                              'procedures where the surgery slips a week or the doctor has to move it to '
                              'another facility. The nightmare version is a provider calling at 7 p.m. '
                              'Central to secure a contract for an 8 a.m. surgery the next day '
                              '[mPaz9R2yMrs @ 00:22:14]. In markets controlled by one dominant system, '
                              'often rural, ClaimDOC contracts with as many freestanding ambulatory '
                              'surgery centers as possible and leans on the Consolidated Appropriations '
                              'Act for emergency rooms, which cannot balance bill the member or turn care '
                              'away, a fallback the provider relations team calls plan B [A__ZFq9k8Ds @ '
                              '00:38:56]. Benefits Studio flags the same catch: some hospitals refuse to '
                              'take part, which can leave gaps in access [noY8cLblMi4 @ 00:01:49]. Bricker '
                              'warns that direct contracts stall without navigation, because employees end '
                              'up getting lost, and notes that getting a major ASO to administer one has '
                              'been super hard, so independent TPAs build client specific networks instead '
                              '[xcu6bvj22fc @ 00:04:03].',
                              'The economics checks start with the bill itself. Arif describes hospitals '
                              'unbundling ICU charges that are supposed to be an all-in per diem, billing '
                              'oxygen, ventilator, ECMO, and even nursing separately on COVID stays, so '
                              'claims that should have been billed at a fraction of that came in at $23 '
                              'million and tripped an outlier clause that turned a supposed 50% PPO '
                              'discount into 15% [mPaz9R2yMrs @ 00:35:10]. Micro-Dyn warns that under RBP '
                              'coding errors can multiply into bigger financial losses than under contract '
                              'pricing [Hz5wBrKavxY @ 00:01:34]. Deihl keeps quotes honest: a '
                              'demographically older 29-employee group priced at $334 per employee on RBP '
                              'against $678 on the PPO, booked as 202% savings, but most of the time the '
                              'agency sees anywhere from 15% to 70%, and these plans are medically '
                              'underwritten [FPcS3pupwwA @ 00:04:56]. Stein calls the EOB headline a trap '
                              'of its own, where a hospital bills $96,000, the administrator touts a '
                              '$40,000 discount, and the chargemaster number was never what anyone '
                              'expected to collect, an opacity that benefits every party except '
                              'self-funded plans [D3AuT-Ki3nw @ 00:06:10]. Measure cost per employee per '
                              'month and real dollars paid, not discount percentages.'],
               'table': {'caption': 'Firsthand Failure Modes and the Numbers Behind Them',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Balance-bill revolt forcing a full PPO unwind',
                                   'Employer converted a January RBP client back to a PPO months in',
                                   'Morale damage and media exposure from cash-upfront demands and balance '
                                   'bills',
                                   'Partners MGU ([YEFRBSmT3IE @ 00:00:29])'],
                                  ['Slam-in implementation with no member education at all',
                                   'Early repricers sold plans without advocacy and deals went sideways',
                                   'Savings of 20% to 40% always arrive with some disruption to manage',
                                   'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:08:26]); Dysrupt '
                                   'Healthcare Podcast ([mPaz9R2yMrs @ 00:09:08])'],
                                  ['Facility friction surfacing right before a scheduled surgery',
                                   'About 15% of outpatient facility claims hit friction before care',
                                   'Only one to two percent of procedures need a delay or redirection',
                                   'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:22:14])'],
                                  ['Dominant health system blocking access in a whole market',
                                   'Single-system and rural markets refuse anything not hospital '
                                   'contracted',
                                   'Contract freestanding surgery centers and rely on ER protections as '
                                   'plan B',
                                   'Self-Funded ([A__ZFq9k8Ds @ 00:38:56])'],
                                  ['Unbundled ICU billing tripping PPO outlier clauses on big claims',
                                   'Oxygen, ventilator, ECMO, and nursing unbundled on COVID ICU stays',
                                   'Claims ballooned to $23 million and a 50% discount became 15%',
                                   'Dysrupt Healthcare Podcast ([mPaz9R2yMrs @ 00:35:10])'],
                                  ['Collections and credit damage while a bill is disputed',
                                   'Billing companies dinged member credit and sent accounts straight to '
                                   'collections',
                                   'Carrier hold letters to providers during claim negotiation stop credit '
                                   'reporting',
                                   'The General Agency ([FPcS3pupwwA @ 00:07:38])'],
                                  ['Overstated savings promises built on one outlier group quote',
                                   'Older 29-employee group showed 202% savings on RBP versus the PPO',
                                   'Typical savings run anywhere from 15% to 70% depending on demographics',
                                   'The General Agency ([FPcS3pupwwA @ 00:04:56])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill-Switch Checks Before Pulling the Network Off the ID Card',
                           'body': 'Every one of these gates maps to a failure an operator lived through: '
                                   'a PPO unwind, a slam-in rollout that went sideways, a dominant system '
                                   'shutting the door, or fees quietly eating the spread. Clear all four '
                                   'before the effective date.',
                           'items': ['Lock in access to HR and rank-and-file employees for education '
                                     'before go-live, because deals without that access went sideways '
                                     '[Dysrupt Healthcare Podcast — mPaz9R2yMrs @ 00:08:26].',
                                     'Map dominant-system and rural markets and contract freestanding '
                                     'ambulatory surgery centers as plan B before members need surgery '
                                     '[Self-Funded — A__ZFq9k8Ds @ 00:38:56].',
                                     'Stand up balance-bill advocates before employees face cash-upfront '
                                     'demands, the complaints that forced one client back to a '
                                     'conventional PPO within months [Partners MGU — YEFRBSmT3IE @ '
                                     '00:00:29].',
                                     'Get TPA and repricing fees quoted and net them against projected '
                                     'savings, since repricing fees can eat into the saving [Benefits '
                                     'Studio — noY8cLblMi4 @ 00:01:12].']}}],
 'pull_quote': '"You\'re not going to save a health plan 20 to 40, sometimes 50%... without having some '
               'sort of disruption." — Omar Arif, Dysrupt Healthcare Podcast (mPaz9R2yMrs @ 00:09:08).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Confirm the plan is self-funded, hire a TPA or RBP vendor, and write the '
                      'Medicare-based rates into the plan document [Benefits Studio — noY8cLblMi4 @ '
                      '00:00:33].',
                      'Pull a top-utilization report and let members nominate their doctors during open '
                      'enrollment so the vendor can call each provider before the first claim [Self-Funded '
                      '— A__ZFq9k8Ds @ 00:27:31].',
                      'Put the implementation team in place two to three months before the effective date '
                      'to run open enrollment communication, and keep the drip running all plan year '
                      '[Self-Funded — A__ZFq9k8Ds @ 00:41:13].',
                      'Keep a provider relations team on standby to cut single case agreements when a '
                      "facility balks at pre-cert, and reroute through the surgeon's other admitting "
                      'facility if needed [Self-Funded — A__ZFq9k8Ds @ 00:44:13].',
                      'Audit every facility claim, reprice it, and send the audit with appeal instructions '
                      "and the hospital's own financials to the billing department by certified mail "
                      '[Dysrupt Healthcare Podcast — mPaz9R2yMrs @ 00:40:11].',
                      'For direct contracts, change the benefit design so the contracted provider carries '
                      'zero out-of-pocket cost, then add a navigation service so employees do not get lost '
                      '[AHealthcareZ - Healthcare Finance Explained — xcu6bvj22fc @ 00:03:18].'],
 'statutory_citations': [{'title': 'Dysrupt Healthcare Podcast — Unlocking Healthcare Savings with '
                                   'Reference-Based Pricing: Insights from Omar Arif [00:24:54]',
                          'url': 'https://www.youtube.com/watch?v=mPaz9R2yMrs&t=1494s',
                          'relevance': "Primary practitioner testimony on ClaimDOC's Medicare plus 25% or "
                                       'cost plus 20% facility payment formula.'},
                         {'title': 'Self-Funded — Unlocking Cost Savings with Reference Based Pricing '
                                   '(RBP) - ClaimDOC - Omar Arif [00:29:51]',
                          'url': 'https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1791s',
                          'relevance': 'Primary practitioner testimony on pay-and-defend versus '
                                       'negotiate-and-settle RBP models.'},
                         {'title': 'AHealthcareZ - Healthcare Finance Explained — 7 Best Practices in '
                                   'Reference-Based Pricing Negotiation [00:03:19]',
                          'url': 'https://www.youtube.com/watch?v=gpm3vtKEf5U&t=199s',
                          'relevance': 'Primary practitioner testimony on the arm-twisting tactics that '
                                       "closed Montana's RBP hospital deal."},
                         {'title': 'Partners MGU — How Surprise Billing Impacts Reference-Based Pricing '
                                   '[00:00:29]',
                          'url': 'https://www.youtube.com/watch?v=YEFRBSmT3IE&t=29s',
                          'relevance': 'Primary practitioner testimony on an RBP client converting back to '
                                       'a PPO over balance billing.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'xVuFXA-gN8g',
                       'title': 'Is Reference-Based Pricing (RBP) Really That Controversial?',
                       'channel': 'Dysrupt Healthcare Podcast',
                       'author': 'Dysrupt Healthcare Podcast',
                       'text': 'Typically models of what I would call the 1.0 models kind of did a bait '
                               'and switch about how much they were going to pay and it was very '
                               'litigious, but there are ways to do this correctly.',
                       'tip': 'Typically models of what I would call the 1.0 models kind of did a bait and '
                              'switch about how much they were going to pay and it was very litigious, but '
                              'there are ways to do this correctly.',
                       'timestamp': 433,
                       'timestamp_seconds': 433,
                       'timestamp_label': '[00:07:13]',
                       'url': 'https://www.youtube.com/watch?v=xVuFXA-gN8g&t=433s',
                       'markdown': '[00:07:13](https://www.youtube.com/watch?v=xVuFXA-gN8g&t=433s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2dsXkvZasDU',
                       'title': 'What is Reference Based Pricing? | Employee Benefits 101 | Holloway '
                                'Benefit Concepts (2020)',
                       'channel': 'Holloway Benefit Concepts',
                       'author': 'Holloway Benefit Concepts',
                       'text': "It's always a higher percentage, typically 150% to 200% of Medicare.",
                       'tip': "It's always a higher percentage, typically 150% to 200% of Medicare.",
                       'timestamp': 24,
                       'timestamp_seconds': 24,
                       'timestamp_label': '[00:00:24]',
                       'url': 'https://www.youtube.com/watch?v=2dsXkvZasDU&t=24s',
                       'markdown': '[00:00:24](https://www.youtube.com/watch?v=2dsXkvZasDU&t=24s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vCzjI43ZWVI',
                       'title': 'Reference Based Pricing - Lesson 1',
                       'channel': 'Remodel Benefits',
                       'author': 'Remodel Benefits',
                       'text': 'When you implement a reference-based pricing environment for a health '
                               'insurance plan you can expect 20 to 30% savings on your medical plans, '
                               'sometimes even more than that.',
                       'tip': 'When you implement a reference-based pricing environment for a health '
                              'insurance plan you can expect 20 to 30% savings on your medical plans, '
                              'sometimes even more than that.',
                       'timestamp': 49,
                       'timestamp_seconds': 49,
                       'timestamp_label': '[00:00:49]',
                       'url': 'https://www.youtube.com/watch?v=vCzjI43ZWVI&t=49s',
                       'markdown': '[00:00:49](https://www.youtube.com/watch?v=vCzjI43ZWVI&t=49s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Hz5wBrKavxY',
                       'title': 'Reference-Based Pricing vs. Commercial Claims Pricing: What You NEED to '
                                'Know',
                       'channel': 'Micro-Dyn',
                       'author': 'Micro-Dyn',
                       'text': 'In both systems, accuracy is critical, but in RBP, coding errors can '
                               'multiply, leading to bigger financial losses.',
                       'tip': 'In both systems, accuracy is critical, but in RBP, coding errors can '
                              'multiply, leading to bigger financial losses.',
                       'timestamp': 94,
                       'timestamp_seconds': 94,
                       'timestamp_label': '[00:01:34]',
                       'url': 'https://www.youtube.com/watch?v=Hz5wBrKavxY&t=94s',
                       'markdown': '[00:01:34](https://www.youtube.com/watch?v=Hz5wBrKavxY&t=94s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'U6ZwMY7UtFU',
                       'title': 'Marty Makary, MD Explains How Reference-Based Pricing Is Transforming '
                                'Employer-Sponsored Healthcare',
                       'channel': 'Imagine360',
                       'author': 'Imagine360',
                       'text': 'You guys are really setting a standard for prices that otherwise have no '
                               "orbit in outer space and they need to be anchored to something, and that's "
                               'exactly what reference-based pricing does in the market.',
                       'tip': 'You guys are really setting a standard for prices that otherwise have no '
                              "orbit in outer space and they need to be anchored to something, and that's "
                              'exactly what reference-based pricing does in the market.',
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=U6ZwMY7UtFU&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=U6ZwMY7UtFU&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mPaz9R2yMrs',
                       'title': 'Unlocking Healthcare Savings with Reference-Based Pricing: Insights from '
                                'Omar Arif',
                       'channel': 'Dysrupt Healthcare Podcast',
                       'author': 'Dysrupt Healthcare Podcast',
                       'text': "We look at Medicare plus a 25% markup, we look at the hospital's own "
                               'self-reported cost and a 20% markup, and whichever of those two methods is '
                               "higher, that's how we pay the facility.",
                       'tip': "We look at Medicare plus a 25% markup, we look at the hospital's own "
                              'self-reported cost and a 20% markup, and whichever of those two methods is '
                              "higher, that's how we pay the facility.",
                       'timestamp': 1494,
                       'timestamp_seconds': 1494,
                       'timestamp_label': '[00:24:54]',
                       'url': 'https://www.youtube.com/watch?v=mPaz9R2yMrs&t=1494s',
                       'markdown': '[00:24:54](https://www.youtube.com/watch?v=mPaz9R2yMrs&t=1494s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mPaz9R2yMrs',
                       'title': 'Unlocking Healthcare Savings with Reference-Based Pricing: Insights from '
                                'Omar Arif',
                       'channel': 'Dysrupt Healthcare Podcast',
                       'author': 'Dysrupt Healthcare Podcast',
                       'text': "Their cost per covered employee went from $819 to $480 PEPM, so that's a "
                               '41.4% overall reduction in plan spend.',
                       'tip': "Their cost per covered employee went from $819 to $480 PEPM, so that's a "
                              '41.4% overall reduction in plan spend.',
                       'timestamp': 2710,
                       'timestamp_seconds': 2710,
                       'timestamp_label': '[00:45:10]',
                       'url': 'https://www.youtube.com/watch?v=mPaz9R2yMrs&t=2710s',
                       'markdown': '[00:45:10](https://www.youtube.com/watch?v=mPaz9R2yMrs&t=2710s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8begy-typh4',
                       'title': 'Reference-Based Pricing: How it works',
                       'channel': 'Rhett Robbins',
                       'author': 'Rhett Robbins',
                       'text': 'Team members can visit virtually any provider but they need to confirm in '
                               "advance if the provider accepts RBP pricing, and if there's a billing "
                               'dispute a third party advocate steps in to negotiate.',
                       'tip': 'Team members can visit virtually any provider but they need to confirm in '
                              "advance if the provider accepts RBP pricing, and if there's a billing "
                              'dispute a third party advocate steps in to negotiate.',
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=8begy-typh4&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=8begy-typh4&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gpm3vtKEf5U',
                       'title': '7 Best Practices in Reference-Based Pricing Negotiation',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': 'This is the most important part of the video: Marilyn Bartlett threatened '
                               'to publish the payment rates by commercial insurance to the hospitals.',
                       'tip': 'This is the most important part of the video: Marilyn Bartlett threatened '
                              'to publish the payment rates by commercial insurance to the hospitals.',
                       'timestamp': 199,
                       'timestamp_seconds': 199,
                       'timestamp_label': '[00:03:19]',
                       'url': 'https://www.youtube.com/watch?v=gpm3vtKEf5U&t=199s',
                       'markdown': '[00:03:19](https://www.youtube.com/watch?v=gpm3vtKEf5U&t=199s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A__ZFq9k8Ds',
                       'title': 'Unlocking Cost Savings with Reference Based Pricing (RBP) - ClaimDOC - '
                                'Omar Arif',
                       'channel': 'Self-Funded',
                       'author': 'Self-Funded',
                       'text': "There's two primary ways to do RBP: one is pay and defend, you pay the "
                               'claim you think is fair and reasonable and then you defend that claim, and '
                               'the other way is to negotiate and settle.',
                       'tip': "There's two primary ways to do RBP: one is pay and defend, you pay the "
                              'claim you think is fair and reasonable and then you defend that claim, and '
                              'the other way is to negotiate and settle.',
                       'timestamp': 1791,
                       'timestamp_seconds': 1791,
                       'timestamp_label': '[00:29:51]',
                       'url': 'https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1791s',
                       'markdown': '[00:29:51](https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1791s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'A__ZFq9k8Ds',
                       'title': 'Unlocking Cost Savings with Reference Based Pricing (RBP) - ClaimDOC - '
                                'Omar Arif',
                       'channel': 'Self-Funded',
                       'author': 'Self-Funded',
                       'text': "We're going to scrape off 25 to 30 percent of the dollars of any inpatient "
                               'stay before we reprice the claim.',
                       'tip': "We're going to scrape off 25 to 30 percent of the dollars of any inpatient "
                              'stay before we reprice the claim.',
                       'timestamp': 1980,
                       'timestamp_seconds': 1980,
                       'timestamp_label': '[00:33:00]',
                       'url': 'https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1980s',
                       'markdown': '[00:33:00](https://www.youtube.com/watch?v=A__ZFq9k8Ds&t=1980s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xcu6bvj22fc',
                       'title': 'Healthcare Direct Contracting Explained',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': 'When the employer goes to the negotiating table to sit down with the '
                               'provider, one of their main points of leverage is steerage.',
                       'tip': 'When the employer goes to the negotiating table to sit down with the '
                              'provider, one of their main points of leverage is steerage.',
                       'timestamp': 62,
                       'timestamp_seconds': 62,
                       'timestamp_label': '[00:01:02]',
                       'url': 'https://www.youtube.com/watch?v=xcu6bvj22fc&t=62s',
                       'markdown': '[00:01:02](https://www.youtube.com/watch?v=xcu6bvj22fc&t=62s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ypiI6d2Bnkk',
                       'title': "Direct Contracting between Employers and Healthcare Providers: HSC's "
                                'Two-Minute Warning',
                       'channel': 'Healthcare Solutions Connection',
                       'author': 'Healthcare Solutions Connection',
                       'text': 'In the first year 30% of employees chose the preferred partnership ACO '
                               'option with a satisfaction rating of 8.5 out of 10.',
                       'tip': 'In the first year 30% of employees chose the preferred partnership ACO '
                              'option with a satisfaction rating of 8.5 out of 10.',
                       'timestamp': 92,
                       'timestamp_seconds': 92,
                       'timestamp_label': '[00:01:32]',
                       'url': 'https://www.youtube.com/watch?v=ypiI6d2Bnkk&t=92s',
                       'markdown': '[00:01:32](https://www.youtube.com/watch?v=ypiI6d2Bnkk&t=92s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UcjjCTQMOV4',
                       'title': 'Reference-based pricing, Marty Makary, MD, & Healthcare Cost Transparency',
                       'channel': 'ELAP Services',
                       'author': 'ELAP Services',
                       'text': 'Reference based pricing is becoming far more dominant in the marketplace; '
                               'it has the promise of reining in surprise billing and it also ensures that '
                               'claims are paid out at a fair amount.',
                       'tip': 'Reference based pricing is becoming far more dominant in the marketplace; '
                              'it has the promise of reining in surprise billing and it also ensures that '
                              'claims are paid out at a fair amount.',
                       'timestamp': 23,
                       'timestamp_seconds': 23,
                       'timestamp_label': '[00:00:23]',
                       'url': 'https://www.youtube.com/watch?v=UcjjCTQMOV4&t=23s',
                       'markdown': '[00:00:23](https://www.youtube.com/watch?v=UcjjCTQMOV4&t=23s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FPcS3pupwwA',
                       'title': 'PPO vs RBP (reference-based pricing)',
                       'channel': 'The General Agency',
                       'author': 'The General Agency',
                       'text': 'The plans are medically underwritten, so there are medical questions asked '
                               'of the employees, and the patients can be subject to balance billing.',
                       'tip': 'The plans are medically underwritten, so there are medical questions asked '
                              'of the employees, and the patients can be subject to balance billing.',
                       'timestamp': 368,
                       'timestamp_seconds': 368,
                       'timestamp_label': '[00:06:08]',
                       'url': 'https://www.youtube.com/watch?v=FPcS3pupwwA&t=368s',
                       'markdown': '[00:06:08](https://www.youtube.com/watch?v=FPcS3pupwwA&t=368s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'D3AuT-Ki3nw',
                       'title': 'Reference Based Pricing vs PPO: The TRUTH About Fair Pricing, Charge '
                                'Masters, and Level-Funded Plans',
                       'channel': 'American Trust Administrators | Level Funding',
                       'author': 'American Trust Administrators | Level Funding',
                       'text': "We're actually overpaying if we're paying more than what the biggest guys "
                               'are paying, so why are we penalizing the little man.',
                       'tip': "We're actually overpaying if we're paying more than what the biggest guys "
                              'are paying, so why are we penalizing the little man.',
                       'timestamp': 208,
                       'timestamp_seconds': 208,
                       'timestamp_label': '[00:03:28]',
                       'url': 'https://www.youtube.com/watch?v=D3AuT-Ki3nw&t=208s',
                       'markdown': '[00:03:28](https://www.youtube.com/watch?v=D3AuT-Ki3nw&t=208s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YEFRBSmT3IE',
                       'title': 'How Surprise Billing Impacts Reference-Based Pricing',
                       'channel': 'Partners MGU',
                       'author': 'Partners MGU',
                       'text': 'The reference-based pricing program the producer had just put in place for '
                               'a client this past January had to convert back to a conventional PPO '
                               'program just a few months in.',
                       'tip': 'The reference-based pricing program the producer had just put in place for '
                              'a client this past January had to convert back to a conventional PPO '
                              'program just a few months in.',
                       'timestamp': 29,
                       'timestamp_seconds': 29,
                       'timestamp_label': '[00:00:29]',
                       'url': 'https://www.youtube.com/watch?v=YEFRBSmT3IE&t=29s',
                       'markdown': '[00:00:29](https://www.youtube.com/watch?v=YEFRBSmT3IE&t=29s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'noY8cLblMi4',
                       'title': 'What Is Reference-Based Pricing? How It Works and What It Costs Employers',
                       'channel': 'Benefits Studio',
                       'author': 'Benefits Studio',
                       'text': 'A self-funded plan pays a third-party administrator to run claims and an '
                               'RBP vendor to reprice them and handle disputes, each quoted, and Willis '
                               'Towers Watson warns repricing fees can eat into the saving.',
                       'tip': 'A self-funded plan pays a third-party administrator to run claims and an '
                              'RBP vendor to reprice them and handle disputes, each quoted, and Willis '
                              'Towers Watson warns repricing fees can eat into the saving.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=noY8cLblMi4&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=noY8cLblMi4&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
