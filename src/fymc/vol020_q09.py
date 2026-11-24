from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'limitations-on-subcontracting-affiliation-enforcement',
 'question_prompt': 'How much work must I perform myself, and what compliance and fraud risks come with '
                    'passing work through?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Limitations on Subcontracting, Affiliation and Enforcement',
 'subtitle': "13 CFR 125.6 and the 50% rule, SBA's updated rules, similarly situated entities, ostensible "
             'contractor and affiliation risk, FAR Part 44 and flow-down compliance for subs, and DOJ '
             'fraud prosecutions such as Operation Ghostbusters',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Federal set-aside primes agree on one hard rule: the small business that wins the '
                      'award must keep a fixed share of the dollars, measured as amount paid to '
                      'non-similarly-situated subs. Services and supplies cap subcontracted pay at 50%, '
                      'general construction at 85%, and specialty trades at 75%, with materials excluded. '
                      "Similarly situated entities, first-tier subs holding the prime's status and small "
                      "under the subcontract NAICS, count as the prime's own work, and PilieroMazza says a "
                      'WOSB can push 100% to a WOSB SSE. Compliance is measured per base or option period '
                      'or task order, tracked monthly, and enforced through negative CPARS, debarment and '
                      'rising DOJ probes. Practitioners split on whether construction self-performance is '
                      "15% or 25%, which NAICS governs SSE size, and whether leasing a sub's employees is "
                      'a legitimate workaround.',
 'key_metrics': [{'label': 'Services subcontracting cap to non-similarly-situated subs',
                  'metric': 'Services subcontracting cap to non-similarly-situated subs',
                  'value': '50% of amount paid',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'PilieroMazza lists services at 50%, alongside manufacturer 50%, general '
                             'construction 85% and specialty trade 75%, excluding materials where '
                             'applicable.',
                  'source': 'PilieroMazza PLLC ([i9prjadeAyM @ 00:12:37])'},
                 {'label': 'Recommended subcontracting buffer under the services cap',
                  'metric': 'Recommended subcontracting buffer under the services cap',
                  'value': 'Subcontract around 47-49%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'PilieroMazza advises primes to subcontract around 47 to 49% rather than a '
                             'full 50% to keep wiggle room.',
                  'source': 'PilieroMazza PLLC ([i9prjadeAyM @ 00:14:43])'},
                 {'label': 'Self-performance requirement in worked monthly example',
                  'metric': 'Self-performance requirement in worked monthly example',
                  'value': '$450K on $1M/month with $100K materials',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Worked example: a $1M-per-month contract with $100K in materials produces a '
                             '$450K self-performance requirement.',
                  'source': 'PilieroMazza PLLC ([i9prjadeAyM @ 00:32:49])'},
                 {'label': 'Economic dependence affiliation trigger',
                  'metric': 'Economic dependence affiliation trigger',
                  'value': '70% or more of revenue from one company in the prior year',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Watson cites 70%+ revenue from a single company as the economic-dependence '
                             'basis for affiliation under 13 CFR 121.103.',
                  'source': 'Theodore Watson ([k1ZkyITmwWM @ 00:02:49])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same premise: the limitation on '
                              'subcontracting is a performance rule that binds the small business that won '
                              'a set-aside, not the subs and not full-and-open winners. GovPrep tells '
                              'primes to pull up SF 1449 and read Block 10 before assuming the clause is '
                              'live, walking through a 2013 set-aside under NAICS 311422 as the example '
                              '[bg9NY9VUfsE @ 00:00:41]. PilieroMazza widens the net: the limit attaches '
                              'to all set-asides, and the only carve-out is a small business set-aside '
                              'below the simplified acquisition threshold [i9prjadeAyM @ 00:10:51]. The '
                              'measuring stick has also changed. PilieroMazza traces the 2016 overhaul '
                              'that moved the calculation from personnel cost to amount paid [qxE-37z0qfw '
                              '@ 00:06:28], and the SDVOSB prime behind Vet GovCon Blueprint compresses '
                              'the point into two words, dollars paid, rejecting hours or headcount as the '
                              'yardstick [go1eoNNgFRM @ 00:01:34]. Under that standard, the number that '
                              'matters is what gets paid to each non-similarly-situated sub against the '
                              'total paid on the contract. The baseline sequence the speakers share is to '
                              'confirm set-aside status in the award document, identify the governing '
                              'clause, which GovPrep pins to 52.219-14, and build the subcontract budget '
                              'around dollars before any teaming agreement gets signed.',
                              'The percentage ladder is where the speakers line up most tightly. Mark Ryan '
                              'lays it out cleanly: services at 50%, construction at 85%, specialty trades '
                              'such as plumbing and electrical at 75%, and manufacturers at 50%, with '
                              'resellers required to buy from a small domestic manufacturer [ne7XpEiLNKE @ '
                              '00:01:06]. PilieroMazza gives the identical ladder for services, '
                              'manufacturing, general construction and specialty trade, adding that '
                              'materials come out of the math where applicable [i9prjadeAyM @ 00:14:21]. '
                              'The Vet GovCon Blueprint operator frames the same numbers as caps on pay to '
                              'subs that are not similarly situated, excluding materials on supplies, '
                              'general construction and special trades, and measures mixed contracts '
                              'portion by portion [go1eoNNgFRM @ 00:01:59]. Theodore Watson adds the '
                              'warning that not every NAICS runs on a 51/49 split, flagging the 236 and '
                              '237 construction series at 15% prime and 85% subs, a figure he prefaces '
                              "with 'I believe' [28K_7987r8w @ 00:01:19]. Watson also confirms that under "
                              "a 51/49 split the prime's 51% can be a blend of its own work and similarly "
                              'situated sub work. For an operator, the takeaway is simple: identify the '
                              'contract type first, because the allowable subcontract share swings from '
                              'half the dollars to 85% depending on whether the work is services, supply, '
                              'general construction or a specialty trade.',
                              'The similarly situated entity is the consensus pressure valve. PilieroMazza '
                              'defines it in three parts: a first-tier sub, holding the same status that '
                              'qualified the prime, and small under the NAICS code assigned to the '
                              'subcontract [i9prjadeAyM @ 00:07:08]. Theodore Watson hammers the last '
                              'prong, saying most people miss that the size test runs on the subcontract '
                              "NAICS the prime assigns, not the prime's own code [28K_7987r8w @ 00:04:26]. "
                              'Status must match pairwise, as Watson lists it: small business to small '
                              "business, 8(a) to 8(a), HUBZone, SDVOSB and WOSB. When it does, the SSE's "
                              "dollars count as the prime's own performance, which Watson says actually "
                              'helps the prime. The consensus limit on that valve is that it does not '
                              'survive a second hop. The Vet GovCon Blueprint operator warns that work an '
                              'SSE passes downstream counts against the prime [go1eoNNgFRM @ 00:03:54], '
                              "echoing Watson's rule that anyone other than prime employees or first-tier "
                              'SSE employees counts against the prime. Enforcement has teeth on the agency '
                              'side as well. Mark Ryan reports that contracting officers are now required '
                              'to issue a negative CPARS when a prime misses the requirement [ne7XpEiLNKE '
                              '@ 00:04:54]. PilieroMazza stacks suspension, debarment and fines on top, '
                              'and flags DOJ investigations as a rising trend.'],
               'table': {'caption': 'Where the speakers agree on scope, math and similarly situated '
                                    'entities',
                         'headers': ['Consensus Point',
                                     'What Practitioners Agree On',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Scope of the limitation and who it actually binds',
                                   'Small business primes on set-aside awards, not subs or full-and-open '
                                   'award winners',
                                   'Check SF 1449 Block 10 before modeling any prime-to-sub dollar split',
                                   'GovPrep ([bg9NY9VUfsE @ 00:00:01])'],
                                  ['Measurement basis used for every compliance calculation',
                                   'Dollars paid to subs, not labor hours, headcount or personnel cost',
                                   'Track every check written to each non-similarly-situated sub against '
                                   'total paid',
                                   'Vet GovCon Blueprint ([go1eoNNgFRM @ 00:01:34])'],
                                  ['Services and supply subcontracting cap on set-aside work',
                                   'No more than 50% of amount paid may go to non-SSE subs',
                                   'Subcontract around 47 to 49% to preserve deliberate wiggle room',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:12:37])'],
                                  ['Construction and specialty trade caps on subcontracted dollars',
                                   'General construction up to 85% subbed, specialty trades such as '
                                   'plumbing 75%',
                                   'Confirm whether the NAICS is general building or a specialty trade '
                                   'first',
                                   'Mark Ryan ([ne7XpEiLNKE @ 00:01:06])'],
                                  ['Similarly situated entity qualification test for first-tier subs',
                                   'First-tier sub, same qualifying status, and small under the '
                                   'subcontract NAICS',
                                   'Size-check the sub against the NAICS you assign, not your own code',
                                   'Theodore Watson ([28K_7987r8w @ 00:04:26])'],
                                  ['Second-tier pass-through clawback against the prime contractor',
                                   'Work a similarly situated sub subcontracts out again gets clawed back',
                                   'Flow the limitation into SSE subcontracts and audit their downstream '
                                   'spend',
                                   'Mark Ryan ([ne7XpEiLNKE @ 00:03:07])'],
                                  ['Independent contractor treatment under the limitation on '
                                   'subcontracting',
                                   '1099 independent contractors are treated as subcontractors, not prime '
                                   'employees',
                                   'Keep self-performance labor on employee payroll rather than 1099 '
                                   'agreements',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:11:35])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The arithmetic is where operators either stay clean or quietly drift out of '
                              "compliance. PilieroMazza's worked example runs a $1M-per-month services "
                              'contract carrying $100K in materials: strip the materials, take half of the '
                              'remaining $900K, and the prime owes $450K of self-performance every month '
                              "[i9prjadeAyM @ 00:32:49]. The same firm's earlier session clarifies what "
                              'can be stripped on services work: G&A and overhead stay in the base, while '
                              'materials that are separately line-itemed can be deducted, illustrated with '
                              'a janitorial contract [qxE-37z0qfw @ 00:54:18]. Mark Ryan shows the SSE '
                              'lever in dollars: on a $100K 8(a) IT contract, $20K subbed to another 8(a) '
                              "still counts toward the prime's $50K [ne7XpEiLNKE @ 00:02:25]. The Vet "
                              'GovCon Blueprint operator runs the failure case on the same $100K services '
                              'contract, where at most $50K can flow to subs that are not similarly '
                              'situated, so a $70K check to one such sub breaks the rule outright '
                              '[go1eoNNgFRM @ 00:02:38]. GovPrep adds that the services figure is '
                              'calculated fully burdened with fee. The operating move is a monthly '
                              'tracking sheet that subtracts eligible materials first, applies the cap to '
                              'what remains, and then credits only first-tier SSE dollars back to the '
                              "prime's side of the ledger.",
                              'Timing is the second mechanic, and the speakers agree the old back-loaded '
                              'self-performance play is dead. Mark Ryan says he has watched firms sub 70% '
                              'in year one, 40% in year two and 10% in year three, then self-perform in '
                              'year four and get away with it; the updated rule measures compliance per '
                              'contract year, and on IDIQs per task order, specifically to make audits '
                              'easier [ne7XpEiLNKE @ 00:03:26]. PilieroMazza calls the belief that a firm '
                              'can fall short early and make it up over the remaining option years the '
                              'most common misconception about the rule, because compliance is measured '
                              'per base or option period [i9prjadeAyM @ 00:38:18]. That pushes tracking '
                              'cadence to the front of the playbook. PilieroMazza wants the numbers pulled '
                              'monthly and no less than quarterly [i9prjadeAyM @ 00:43:56], and the Vet '
                              'GovCon Blueprint operator names silent drift over time as one of three '
                              'traps, prescribing the same fix of tracking dollars to each sub every month '
                              "[go1eoNNgFRM @ 00:04:20]. PilieroMazza's earlier session adds that on "
                              'full-and-open vehicles, the measurement runs per order rather than over the '
                              'whole vehicle. For a broker structuring a multi-year deal, the build is a '
                              'running monthly ledger per period and per order, so the prime sees a breach '
                              'coming before the period closes rather than after.',
                              "Paper is the third mechanic. PilieroMazza says a prime may rely on a sub's "
                              'SAM representations or written representations as of the date of the '
                              'subcontract offer, with the caveats that HUBZone status must be confirmed '
                              'against SBA certification and WOSB remains self-certified for subcontracts '
                              '[i9prjadeAyM @ 00:22:14]. The same firm wants a clause forcing prompt '
                              'notice of any status change plus indemnification, and its earlier session '
                              'lists the teaming agreement terms to lock down: NAICS assignment for the '
                              'sub, size and status representations, and a limitations on subcontracting '
                              'awareness clause [qxE-37z0qfw @ 00:30:19]. Theodore Watson goes further on '
                              'the back end, suggesting primes make subs certify compliance with each '
                              'invoice; he concedes no case law backs it, but says it may help against '
                              'False Claims and pass-through scrutiny [28K_7987r8w @ 00:08:07]. On the '
                              "front end, Watson's affiliation session advises spelling out in the "
                              'proposal itself what percentage of the statement of work the prime will '
                              'perform versus the sub or teaming partner [k1ZkyITmwWM @ 00:12:00]. '
                              'PilieroMazza also points to other direct cost exclusions recognized through '
                              'VA, GSA and DOE class deviations, including airline travel, environmental '
                              'remediation, cloud computing and mass media, though the Vet GovCon '
                              'Blueprint operator stresses such exclusions only apply as the solicitation '
                              'allows.'],
               'table': {'caption': 'Street-level numbers and structures practitioners use to stay inside '
                                    'the cap',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Apply It',
                                     'Expert Source'],
                         'rows': [['Self-performance math on a services contract with materials',
                                   '$1M per month minus $100K materials leaves a $450K requirement',
                                   'Strip separately line-itemed materials before applying the 50% '
                                   'services cap',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:32:49])'],
                                  ['Subcontracting buffer kept below the services cap',
                                   'Subcontract roughly 47 to 49% instead of a full 50%',
                                   'Hold a deliberate cushion under the cap for wiggle room',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:14:43])'],
                                  ['Lower-tier leakage through a similarly situated sub',
                                   'Prime 40% plus SSE 20%, SSE subs out 15%, prime lands at 45%',
                                   'Audit what your SSE subcontracts out to its own downstream vendors',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:19:17])'],
                                  ['Joint venture self-performance share for the qualifying partner',
                                   "Qualifying party must perform 40% of the JV partners' share",
                                   'Model the JV work split before signing the joint venture agreement',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:47:18])'],
                                  ['HUBZone pooling example used to clear the prime share',
                                   '35% prime work plus 15 to 16% from a HUBZone sub',
                                   'Pair with a same-status sub to reach the required prime share',
                                   'GovPrep ([bg9NY9VUfsE @ 00:06:31])'],
                                  ['Seven allowed justifications for missing the required percentage',
                                   'Labor shortage, scope mod, emergency, site change, sub '
                                   'misrepresentation, status loss, force majeure',
                                   'Document that the cause was beyond control and not mitigable without '
                                   'undue cost',
                                   'Mark Ryan ([ne7XpEiLNKE @ 00:05:54])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Field Moves for Holding the Prime Share',
                           'body': 'Four moves the speakers teach for keeping the self-performance share '
                                   'defensible and the subcontract paper clean.',
                           'items': ['Verify you actually have the staff and infrastructure before '
                                     'bidding, or be prepared to withdraw the bid [PilieroMazza PLLC — '
                                     'i9prjadeAyM @ 00:04:28].',
                                     'Bring the December 2018 class deviation 0003 to the table on SSE '
                                     "pooling, because in Eric Coffie's experience contracting officers "
                                     'have asked him to explain the rule [Eric Coffie — 8-4Lml2bZj4 @ '
                                     '00:01:25].',
                                     'After selecting a sub, Natalie Rosario asks it to lease one to two '
                                     'of its employees for the duration, providing only what the contract '
                                     'requires with no handbooks or perks; she says hungry subs usually '
                                     'agree [Natalie Rosario | GovCon Coach — G44VRBscagY @ 00:02:31].',
                                     "Avoid hiring an incumbent's workforce en masse, especially its "
                                     'managers, and never rely on a large sub to manage the contract '
                                     '[Theodore Watson — k1ZkyITmwWM @ 00:10:42].']},
               'sop_steps': [{'step': 1,
                              'title': 'Confirm the clause is live',
                              'action': 'Pull the award form, confirm set-aside status, and identify the '
                                        'governing clause.',
                              'detail': 'GovPrep reads SF 1449 Block 10 to confirm a set-aside and points '
                                        'to 52.219-14; PilieroMazza adds the limit hits all set-asides '
                                        'except small business set-asides below the simplified acquisition '
                                        'threshold [GovPrep — bg9NY9VUfsE @ 00:00:41].'},
                             {'step': 2,
                              'title': 'Build the dollar base and cap',
                              'action': 'Subtract eligible materials, apply the contract-type cap, and set '
                                        'a 47-49% subcontract target.',
                              'detail': 'On $1M per month with $100K in materials, the prime owes $450K of '
                                        'self-performance, and PilieroMazza advises subcontracting around '
                                        '47 to 49% for wiggle room [PilieroMazza PLLC — i9prjadeAyM @ '
                                        '00:32:49].'},
                             {'step': 3,
                              'title': 'Qualify and paper every SSE',
                              'action': 'Check matching status and size under the subcontract NAICS, then '
                                        'lock reps, notice and indemnification terms.',
                              'detail': 'Watson says most people miss that SSE size runs on the NAICS the '
                                        'prime assigns to the subcontract, and PilieroMazza lets primes '
                                        'rely on SAM or written reps as of the subcontract offer date '
                                        '[Theodore Watson — 28K_7987r8w @ 00:04:26].'},
                             {'step': 4,
                              'title': 'Track dollars monthly per period and order',
                              'action': 'Run a monthly ledger of dollars paid to each sub, measured per '
                                        'base, option period or task order.',
                              'detail': 'The Vet GovCon Blueprint operator names silent drift as a core '
                                        'trap and prescribes tracking dollars to each sub monthly, since '
                                        'shortfalls cannot be made up in later years [Vet GovCon Blueprint '
                                        '— go1eoNNgFRM @ 00:04:20].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over which NAICS code decides whether a sub counts as '
                              'similarly situated. Natalie Rosario of GovCon Coach tells primes to prove '
                              "the sub's matching status in SAM and says that registration sits 'under the "
                              "NAICS code of the contract that was awarded' [G44VRBscagY @ 00:01:00]. "
                              'Theodore Watson contradicts that directly: the sub must be small under the '
                              "NAICS the prime assigns to the subcontract, not the prime's own code, and "
                              "Watson warns that 'most people miss this' [28K_7987r8w @ 00:04:26]. "
                              'PilieroMazza sides with Watson and adds that the subcontract NAICS may '
                              "carry a higher size standard than the prime's [i9prjadeAyM @ 00:08:35]. The "
                              'construction numbers fracture the same way. Watson puts general '
                              "construction at 15% prime and 85% subs, hedged with 'I believe,' and "
                              'PilieroMazza states 85% for general construction and 75% for specialty '
                              "trades. Eric Coffie instead describes a '25% requirement' on construction, "
                              'so that 75% can be subbed [8-4Lml2bZj4 @ 00:03:58], while GovPrep '
                              "separately states specialty trade as '25.' An operator pricing a "
                              'construction bid off the wrong speaker builds the self-performance budget '
                              "on a misstatement, and GovPrep's own answer is to pull the clause, "
                              '52.219-14, and check Block 10 of the SF 1449 to confirm the set-aside '
                              'before committing a number.',
                              'How a prime manufactures its self-performance share is the second fault '
                              "line. Rosario's street play is to select the sub, then ask to 'lease one to "
                              "two of your employees for the duration'; Rosario reports that hungry subs "
                              'usually agree and gives those leased workers only what the contract '
                              'requires, with no handbooks or perks [G44VRBscagY @ 00:02:31]. The '
                              "counter-pressure comes from how other speakers define the prime's own "
                              "labor. GovPrep insists the work be done with 'your w-2 employees,' not "
                              '1099s and not subcontractors, and PilieroMazza likewise treats independent '
                              'contractors as subcontractors rather than employees [i9prjadeAyM @ '
                              "00:11:35]. Watson attacks the adjacent move of absorbing someone else's "
                              "people: on affiliation, Watson tells primes to avoid hiring an incumbent's "
                              'workforce en masse, especially its managers, and not to rely on a large sub '
                              'to manage the contract [k1ZkyITmwWM @ 00:10:42]. Rosario and Watson do '
                              'converge on management. Rosario says management and admin do not count '
                              "toward the prime's 51% of labor, and Watson warns that mere supervision may "
                              'itself violate the ostensible subcontractor rule because the prime must '
                              'perform the primary and vital parts [28K_7987r8w @ 00:09:51]. Rosario pairs '
                              'the leasing play with a hard warning: primes submit yearly prime-versus-sub '
                              'labor hours and must keep them accurate.',
                              'The third split is whether the similarly situated structure is a loophole '
                              'to exploit or a trap. PilieroMazza walks through a WOSB prime subbing 100% '
                              "to a WOSB similarly situated entity and concedes 'it's not in violation of "
                              "the statute or the regulation so sba recognizes the loophole and we'll see' "
                              '[qxE-37z0qfw @ 00:15:05]; the firm adds that only the CO, the prime or SBA '
                              "can protest a sub's size. Eric Coffie frames the same rule as help for "
                              "small firms, describing December 2018 class deviation '0003' letting firms "
                              'pool similarly situated entities across matching statuses such as HUBZone '
                              'with HUBZone [8-4Lml2bZj4 @ 00:02:32]. Vet GovCon Blueprint, speaking as an '
                              "SDVOSB prime, takes the opposite view of pass-through arrangements: 'That's "
                              "not a loophole — that's the exact scheme this rule was written to stop' "
                              '[go1eoNNgFRM @ 00:04:42]. Watson lands on the enforcement side, warning '
                              'that pass-throughs can bring criminal violations [28K_7987r8w @ 00:10:32]. '
                              'The timing playbook has also flipped. Mark Ryan says firms used to sub 70%, '
                              "40% and 10% across years and then self-perform in year four 'and get away "
                              "with that,' which Ryan says no longer works because compliance now runs per "
                              'contract year and, on IDIQs, per task order. Where FAR and SBA texts '
                              "conflict, NSBGCA's DCAA speaker Amanda Reed answers simply: follow the "
                              'contract.'],
               'table': {'caption': 'Side-by-side practitioner playbooks on Limitations on Subcontracting',
                         'headers': ['Contested Issue', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which NAICS code decides similarly situated sub status',
                                   "Rosario: prove the sub's status in SAM under the awarded contract's "
                                   'NAICS code',
                                   'Watson and PilieroMazza: sub must be small under the NAICS assigned to '
                                   'the subcontract',
                                   'Natalie Rosario | GovCon Coach ([G44VRBscagY @ 00:01:00]); Theodore '
                                   'Watson ([28K_7987r8w @ 00:04:26])'],
                                  ['How much general construction work the prime must self-perform',
                                   'GovPrep: prime does 15%, typically of labor, with up to 85% subbed',
                                   "Coffie: a '25% requirement' on construction, leaving 75% that can be "
                                   'subbed',
                                   'GovPrep ([bg9NY9VUfsE @ 00:07:37]); Eric Coffie ([8-4Lml2bZj4 @ '
                                   '00:03:58])'],
                                  ['How the prime fills its own self-performance labor share',
                                   "Rosario: lease one to two of the sub's employees for the duration",
                                   'PilieroMazza and GovPrep: 1099 independent contractors count as '
                                   'subcontractors, not prime employees',
                                   'Natalie Rosario | GovCon Coach ([G44VRBscagY @ 00:02:31]); '
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:11:35])'],
                                  ['Whether a 100% pass-through to a similarly situated sub is acceptable',
                                   "PilieroMazza: a WOSB can sub 100% to a WOSB SSE and SBA 'recognizes "
                                   "the loophole'",
                                   'Vet GovCon Blueprint: pass-throughs are the exact scheme the rule was '
                                   'written to stop',
                                   'PilieroMazza PLLC ([qxE-37z0qfw @ 00:15:05]); Vet GovCon Blueprint '
                                   '([go1eoNNgFRM @ 00:04:42])'],
                                  ['Back-loading self-performance into the final contract years',
                                   'Old practice per Ryan: sub 70%, 40%, 10%, then self-perform in year '
                                   'four',
                                   'Now measured per contract year or option period, so shortfalls cannot '
                                   'be made up later',
                                   'Mark Ryan ([ne7XpEiLNKE @ 00:03:26]); PilieroMazza PLLC ([i9prjadeAyM '
                                   '@ 00:38:18])'],
                                  ['When the sub must be small for similarly situated credit',
                                   'Watson assumes proposal or certification time, admitting there is no '
                                   'case law',
                                   'PilieroMazza: primes may rely on SAM or written reps as of the '
                                   'subcontract offer date',
                                   'Theodore Watson ([28K_7987r8w @ 00:06:20]); PilieroMazza PLLC '
                                   '([i9prjadeAyM @ 00:22:14])'],
                                  ['What unit actually measures compliance with the percentage cap',
                                   'PilieroMazza and Vet GovCon: amount paid, dollars, not hours or '
                                   'headcount',
                                   'Rosario: yearly prime-versus-sub labor hours submitted and kept '
                                   'accurate',
                                   'PilieroMazza PLLC ([qxE-37z0qfw @ 00:06:28]); Natalie Rosario | GovCon '
                                   'Coach ([G44VRBscagY @ 00:03:32])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most common failure is leakage below the first tier. PilieroMazza's "
                              'worked example has a prime performing 40% and a similarly situated sub '
                              'performing 20%, but that sub farms out 15%, leaving the prime credited with '
                              'only 45% and non-compliant [i9prjadeAyM @ 00:19:17]. Mark Ryan describes '
                              'the same mechanic from the other direction: on a $100K 8(a) IT contract, '
                              '$20K subbed to another 8(a) still counts toward the $50K, but any further '
                              "subbing is clawed back [ne7XpEiLNKE @ 00:03:07]. Watson's rule of thumb is "
                              "blunt: work by anyone other than the prime's employees or first-tier "
                              'similarly situated employees counts against the prime [28K_7987r8w @ '
                              '00:09:10]. Vet GovCon Blueprint names three traps from running an SDVOSB '
                              "prime: pass-through arrangements, mixed status where the sub's status does "
                              'not match the set-aside, and silent drift over time, summed up as '
                              "'Certifications lapse' [go1eoNNgFRM @ 00:04:20]. Their fix is mechanical, "
                              'tracking dollars to each sub monthly, and PilieroMazza sets the floor at '
                              'monthly tracking and no less than quarterly. Back-loading is dead as a '
                              "recovery plan: PilieroMazza calls 'we'll make it up' over the remaining "
                              'years the most common misconception, because compliance is measured per '
                              'base or option period and shortfalls cannot be recovered later.',
                              'The economics check starts with the math, and the math is easy to get '
                              "wrong. PilieroMazza's worked example of $1M per month with $100K in "
                              'materials produces a $450K self-performance requirement [i9prjadeAyM @ '
                              '00:32:49], and Vet GovCon Blueprint shows that on a $100K services '
                              'contract, paying $70K to one non-similarly-situated sub breaks the rule. '
                              "GovPrep's own example illustrates the danger of trusting a speaker's "
                              "arithmetic: the GovPrep speaker says a '$100,000 contract' requires "
                              "'$500,000,' which does not reconcile with the stated 50% services rule "
                              '[bg9NY9VUfsE @ 00:04:23]. Getting it wrong is expensive. Mark Ryan reports '
                              'that COs are now required to give a negative CPARS for missing the '
                              'requirement [ne7XpEiLNKE @ 00:05:33], PilieroMazza lists suspension, '
                              'debarment and fines and reports DOJ investigations rising, and Amanda Reed '
                              'of DCAA, speaking at NSBGCA, adds withheld payments, treble damages under '
                              'the False Claims Act, termination for default, and suspension or debarment '
                              "[ka1Q_JhjM8w @ 00:19:40]. Watson's hedge against False Claims and "
                              'pass-through scrutiny is to have subs certify compliance with each invoice, '
                              'though Watson concedes no case law supports it. Federal-funds enforcement '
                              "reach shows in Court Files' report of 47 ghost-student cases across 27 of "
                              "the FBI's 55 field offices, though Scamverge stresses these are charges, "
                              'not convictions.',
                              'Status and paperwork traps sink primes who trust the wrong document. '
                              "PilieroMazza says primes may rely on a sub's SAM or written representations "
                              'as of the subcontract offer date, but HUBZone status requires confirming '
                              'SBA certification and SDVOSB self-certification ended in January 2023 '
                              "[i9prjadeAyM @ 00:24:39]; the firm's defensive clause requires prompt "
                              'notice of status changes plus indemnification. On affiliation, Watson flags '
                              '70% or more of revenue from one company in the prior year as economic '
                              'dependence and treats an incumbent sub as a red flag under the ostensible '
                              "subcontractor rule, while stressing 'there is no bright line rule every "
                              "case is fact specific' and that 'affiliation is a rebuttable presumption' "
                              "[k1ZkyITmwWM @ 00:04:50]; Watson's firm won Argus & Black after OHA held "
                              'that mechanically applying economic dependence to a startup was wrong. '
                              "Flow-downs are the third trap. Devine Hewitt warns 'Most primes flow "
                              "everything down,' including clauses that do not apply to the sub, and tells "
                              'subs to reject blanket comply-with-everything language [yp5LO51vPi8 @ '
                              '00:18:25]. Chase K. of Capital Edge adds that naming a sub during '
                              'negotiations does not satisfy 52.244-2, and that consent must be written '
                              'consent from the CO because verbal consent does not count [36eRQkU2X_I @ '
                              '00:13:16].'],
               'table': {'caption': 'Firsthand failure modes and the cost of each',
                         'headers': ['Failure Mode',
                                     'What Happened or Was Warned',
                                     'Economics or Consequence',
                                     'Expert Source'],
                         'rows': [['Lower-tier leakage through a similarly situated sub',
                                   'Prime does 40%, SSE does 20%, then the SSE subs out 15%',
                                   'Prime is left at 45% and is non-compliant for the period',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:19:17])'],
                                  ['Back-loading self-performance into later contract years',
                                   'Firms subbed 70%, 40%, 10%, then self-performed in year four',
                                   'Now measured per contract year and per IDIQ task order, with negative '
                                   'CPARS',
                                   'Mark Ryan ([ne7XpEiLNKE @ 00:03:26])'],
                                  ['Mixed status and silent certification drift on subs',
                                   'Sub status does not match the set-aside, and certifications lapse',
                                   'Those dollars count against the cap, so track each sub monthly',
                                   'Vet GovCon Blueprint ([go1eoNNgFRM @ 00:04:20])'],
                                  ['Bidding without staff or infrastructure already in place',
                                   'Prime cannot self-perform the required share after submitting the bid',
                                   'Prime may need to withdraw the bid entirely before award',
                                   'PilieroMazza PLLC ([i9prjadeAyM @ 00:04:28])'],
                                  ['Prime only supervises while the sub performs the work',
                                   'Mere supervision may violate the ostensible subcontractor rule on '
                                   'primary and vital work',
                                   'Pass-through arrangements can bring criminal violations for the prime',
                                   'Theodore Watson ([28K_7987r8w @ 00:09:51])'],
                                  ['Large-business past performance demands on small set-asides',
                                   'VA T4NG small set-aside required past performance basically the same '
                                   'as a large company',
                                   '13 of 15 small set-aside awards went to joint ventures with large '
                                   'partners',
                                   'Eric Coffie ([TpwUzqMIZKw @ 00:00:43])'],
                                  ['Vehicle-wide cost accounting system requirement excluding small firms',
                                   "Approved cost accounting system required even where the small firm's "
                                   'work did not need CAS',
                                   'Only about 5 of roughly 100 task orders actually required CAS',
                                   'Eric Coffie ([TpwUzqMIZKw @ 00:02:58])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before the subcontract dollars move',
                           'body': 'Each check maps to a failure a practitioner watched happen or warned '
                                   'about directly; clear all four before signing a sub or submitting an '
                                   'invoice.',
                           'items': ['Confirm the staff and infrastructure to self-perform exist before '
                                     'bidding, or be ready to withdraw the bid [PilieroMazza PLLC — '
                                     'i9prjadeAyM @ 00:04:28].',
                                     'Verify every similarly situated sub is first tier, holds the same '
                                     'program status, and is small under the NAICS assigned to the '
                                     "subcontract, not the prime's NAICS [Theodore Watson — 28K_7987r8w @ "
                                     '00:04:26].',
                                     'Track dollars paid to each sub monthly so silent drift and lapsed '
                                     'certifications are caught inside the measurement period [Vet GovCon '
                                     'Blueprint — go1eoNNgFRM @ 00:05:58].',
                                     'On IDIQs, test compliance per task order, not across the whole '
                                     'vehicle, because that is now how it is audited [Mark Ryan — '
                                     'ne7XpEiLNKE @ 00:04:20].']}}],
 'pull_quote': '"That\'s not a loophole — that\'s the exact scheme this rule was written to stop." — Vet '
               'GovCon Blueprint (go1eoNNgFRM @ 00:04:42).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Check Block 10 of the SF 1449 to confirm the award is a set-aside before applying '
                      'the limitation, since it does not apply to full-and-open awards [GovPrep — '
                      'bg9NY9VUfsE @ 00:00:41].',
                      'Budget subcontracted work at around 47 to 49% on services so there is wiggle room '
                      'under the 50% cap [PilieroMazza PLLC — i9prjadeAyM @ 00:14:43].',
                      'Spell out in the proposal what percentages of the statement of work the prime will '
                      'provide versus the subcontractor or teaming partner [Theodore Watson — k1ZkyITmwWM '
                      '@ 00:12:00].',
                      'Write NAICS assignment, size and status representations, and a '
                      'limitations-on-subcontracting awareness clause into every teaming agreement '
                      '[PilieroMazza PLLC — qxE-37z0qfw @ 00:30:19].',
                      'Get subs or classes of subs listed at 52.244-2(j) so consent is already handled, '
                      'and never rely on verbal consent [How To Sell To & Win Federal Government Contracts '
                      '— 36eRQkU2X_I @ 00:08:54].',
                      'As a sub, reject blanket comply-with-everything language, ask for the prime '
                      "contract, accept flow-downs 'as applicable,' and strike clauses that do not apply "
                      '[How To Sell To & Win Federal Government Contracts — yp5LO51vPi8 @ 00:24:51].'],
 'statutory_citations': [{'title': 'PilieroMazza PLLC — Limitations on Subcontracting: Key Updates and '
                                   'Tips for Compliance [00:19:17]',
                          'url': 'https://www.youtube.com/watch?v=i9prjadeAyM&t=1157s',
                          'relevance': 'Primary practitioner testimony on lower-tier leakage, percentage '
                                       'caps, measurement periods, and penalties.'},
                         {'title': 'Theodore Watson — FAR Limitations on Subcontracting Lawyers & 13 CFR '
                                   '125.6 [00:04:26]',
                          'url': 'https://www.youtube.com/watch?v=28K_7987r8w&t=266s',
                          'relevance': 'Primary practitioner testimony on the two-part similarly situated '
                                       'entity test and pass-through exposure.'},
                         {'title': 'Mark Ryan — Limitations on Subcontracting Rule 13 C.F.R. § 125.6 '
                                   'Overview and Updates to the Regulations [00:03:26]',
                          'url': 'https://www.youtube.com/watch?v=ne7XpEiLNKE&t=206s',
                          'relevance': 'Primary practitioner testimony on per-contract-year and '
                                       'per-task-order compliance and mandatory negative CPARS.'},
                         {'title': 'Vet GovCon Blueprint — The 50% Rule: Who Actually Has to Do the Work? '
                                   '[00:04:20]',
                          'url': 'https://www.youtube.com/watch?v=go1eoNNgFRM&t=260s',
                          'relevance': 'Primary practitioner testimony on pass-through, mixed-status, and '
                                       'silent-drift traps from an SDVOSB prime.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '28K_7987r8w',
                       'title': 'FAR Limitations on Subcontracting Lawyers & 13 CFR 125.6',
                       'channel': 'Theodore Watson',
                       'author': 'Theodore Watson',
                       'text': 'The subs cannot pass all the work to large businesses.',
                       'tip': 'The subs cannot pass all the work to large businesses.',
                       'timestamp': 487,
                       'timestamp_seconds': 487,
                       'timestamp_label': '[00:08:07]',
                       'url': 'https://www.youtube.com/watch?v=28K_7987r8w&t=487s',
                       'markdown': '[00:08:07](https://www.youtube.com/watch?v=28K_7987r8w&t=487s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i9prjadeAyM',
                       'title': 'Limitations on Subcontracting: Key Updates and Tips for Compliance',
                       'channel': 'PilieroMazza PLLC',
                       'author': 'PilieroMazza PLLC',
                       'text': 'The most common misconception with the limitations on subcontracting is we '
                               "really weren't complying over the first year or two but it's fine we have "
                               "three years left we'll make it up, that's not correct.",
                       'tip': 'The most common misconception with the limitations on subcontracting is we '
                              "really weren't complying over the first year or two but it's fine we have "
                              "three years left we'll make it up, that's not correct.",
                       'timestamp': 2336,
                       'timestamp_seconds': 2336,
                       'timestamp_label': '[00:38:56]',
                       'url': 'https://www.youtube.com/watch?v=i9prjadeAyM&t=2336s',
                       'markdown': '[00:38:56](https://www.youtube.com/watch?v=i9prjadeAyM&t=2336s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ne7XpEiLNKE',
                       'title': 'Limitations on Subcontracting Rule 13 C.F.R. § 125.6 Overview and Updates '
                                'to the Regulations',
                       'channel': 'Mark Ryan',
                       'author': 'Mark Ryan',
                       'text': "They're required to give you a negative CPARS if you did not meet the "
                               'subcontractor requirements.',
                       'tip': "They're required to give you a negative CPARS if you did not meet the "
                              'subcontractor requirements.',
                       'timestamp': 333,
                       'timestamp_seconds': 333,
                       'timestamp_label': '[00:05:33]',
                       'url': 'https://www.youtube.com/watch?v=ne7XpEiLNKE&t=333s',
                       'markdown': '[00:05:33](https://www.youtube.com/watch?v=ne7XpEiLNKE&t=333s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qxE-37z0qfw',
                       'title': 'Limitations on Subcontracting New Rules',
                       'channel': 'PilieroMazza PLLC',
                       'author': 'PilieroMazza PLLC',
                       'text': "It's not in violation of the statute or the regulation so SBA recognizes "
                               "the loophole and we'll see.",
                       'tip': "It's not in violation of the statute or the regulation so SBA recognizes "
                              "the loophole and we'll see.",
                       'timestamp': 905,
                       'timestamp_seconds': 905,
                       'timestamp_label': '[00:15:05]',
                       'url': 'https://www.youtube.com/watch?v=qxE-37z0qfw&t=905s',
                       'markdown': '[00:15:05](https://www.youtube.com/watch?v=qxE-37z0qfw&t=905s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'G44VRBscagY',
                       'title': 'UNDERSTANDING LIMTATIONS TO SUBCONTRACTING -The FPF Academyx',
                       'channel': 'Natalie Rosario | GovCon Coach',
                       'author': 'Natalie Rosario | GovCon Coach',
                       'text': 'Limitations on subcontracting is pretty much the government telling you '
                               'the prime contractor has to complete at least 51% of the labor.',
                       'tip': 'Limitations on subcontracting is pretty much the government telling you the '
                              'prime contractor has to complete at least 51% of the labor.',
                       'timestamp': 22,
                       'timestamp_seconds': 22,
                       'timestamp_label': '[00:00:22]',
                       'url': 'https://www.youtube.com/watch?v=G44VRBscagY&t=22s',
                       'markdown': '[00:00:22](https://www.youtube.com/watch?v=G44VRBscagY&t=22s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bg9NY9VUfsE',
                       'title': 'Limits on Subcontracting',
                       'channel': 'GovPrep',
                       'author': 'GovPrep',
                       'text': 'Work for your company, not 1099s, not subcontractors, so you need to do '
                               'with your employees, your W-2 employees, at least 50 percent of the work.',
                       'tip': 'Work for your company, not 1099s, not subcontractors, so you need to do '
                              'with your employees, your W-2 employees, at least 50 percent of the work.',
                       'timestamp': 326,
                       'timestamp_seconds': 326,
                       'timestamp_label': '[00:05:26]',
                       'url': 'https://www.youtube.com/watch?v=bg9NY9VUfsE&t=326s',
                       'markdown': '[00:05:26](https://www.youtube.com/watch?v=bg9NY9VUfsE&t=326s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8-4Lml2bZj4',
                       'title': 'Similarly Situated Entity helps Limitations on SUBCONTRACTING for small '
                                'firms - Eric Coffie',
                       'channel': 'Eric Coffie',
                       'author': 'Eric Coffie',
                       'text': 'Contracting officers may not know this rule, and contracting officers have '
                               'asked about it.',
                       'tip': 'Contracting officers may not know this rule, and contracting officers have '
                              'asked about it.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=8-4Lml2bZj4&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=8-4Lml2bZj4&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '36eRQkU2X_I',
                       'title': 'Government Contacting - FAR Part 44 - Subcontracting Policies and '
                                'Procedures - Win Federal Contracts',
                       'channel': 'How To Sell To & Win Federal Government Contracts',
                       'author': 'How To Sell To & Win Federal Government Contracts',
                       'text': 'FAR 44 tells us that the advanced notice and consent requirements are '
                               'waived.',
                       'tip': 'FAR 44 tells us that the advanced notice and consent requirements are '
                              'waived.',
                       'timestamp': 354,
                       'timestamp_seconds': 354,
                       'timestamp_label': '[00:05:54]',
                       'url': 'https://www.youtube.com/watch?v=36eRQkU2X_I&t=354s',
                       'markdown': '[00:05:54](https://www.youtube.com/watch?v=36eRQkU2X_I&t=354s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yp5LO51vPi8',
                       'title': 'Government Contracting - FAR Compliance - What Every Sub Needs To Know - '
                                'Win Federal Contracts',
                       'channel': 'How To Sell To & Win Federal Government Contracts',
                       'author': 'How To Sell To & Win Federal Government Contracts',
                       'text': "What subs also don't realize is that discretionary clauses can be "
                               'negotiated.',
                       'tip': "What subs also don't realize is that discretionary clauses can be "
                              'negotiated.',
                       'timestamp': 906,
                       'timestamp_seconds': 906,
                       'timestamp_label': '[00:15:06]',
                       'url': 'https://www.youtube.com/watch?v=yp5LO51vPi8&t=906s',
                       'markdown': '[00:15:06](https://www.youtube.com/watch?v=yp5LO51vPi8&t=906s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ka1Q_JhjM8w',
                       'title': 'Understanding FAR Compliance',
                       'channel': 'NSBGCA',
                       'author': 'NSBGCA',
                       'text': 'Your compliance is only as strong as your weakest link.',
                       'tip': 'Your compliance is only as strong as your weakest link.',
                       'timestamp': 1279,
                       'timestamp_seconds': 1279,
                       'timestamp_label': '[00:21:19]',
                       'url': 'https://www.youtube.com/watch?v=ka1Q_JhjM8w&t=1279s',
                       'markdown': '[00:21:19](https://www.youtube.com/watch?v=ka1Q_JhjM8w&t=1279s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k1ZkyITmwWM',
                       'title': 'SBA Affiliation Rules 13 CFR 121.103 Ostensible Contractor Rule Lawyers. '
                                'SBA OHA Appeal Lawyers',
                       'channel': 'Theodore Watson',
                       'author': 'Theodore Watson',
                       'text': 'As the prime contractor you cannot have your sub or team and partner '
                               'perform the primary and vital parts of the contract.',
                       'tip': 'As the prime contractor you cannot have your sub or team and partner '
                              'perform the primary and vital parts of the contract.',
                       'timestamp': 290,
                       'timestamp_seconds': 290,
                       'timestamp_label': '[00:04:50]',
                       'url': 'https://www.youtube.com/watch?v=k1ZkyITmwWM&t=290s',
                       'markdown': '[00:04:50](https://www.youtube.com/watch?v=k1ZkyITmwWM&t=290s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k1ZkyITmwWM',
                       'title': 'SBA Affiliation Rules 13 CFR 121.103 Ostensible Contractor Rule Lawyers. '
                                'SBA OHA Appeal Lawyers',
                       'channel': 'Theodore Watson',
                       'author': 'Theodore Watson',
                       'text': 'You may want to spell out in your actual proposal what percentages of the '
                               'statement of work you as the prime are going to be providing versus what '
                               'your subcontractor or teaming partner is going to provide.',
                       'tip': 'You may want to spell out in your actual proposal what percentages of the '
                              'statement of work you as the prime are going to be providing versus what '
                              'your subcontractor or teaming partner is going to provide.',
                       'timestamp': 720,
                       'timestamp_seconds': 720,
                       'timestamp_label': '[00:12:00]',
                       'url': 'https://www.youtube.com/watch?v=k1ZkyITmwWM&t=720s',
                       'markdown': '[00:12:00](https://www.youtube.com/watch?v=k1ZkyITmwWM&t=720s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rcSJIi02YnA',
                       'title': 'BREAKING NEWS: DOJ Busts Ghost Student Fraud Ring — October 29th, 2026',
                       'channel': 'Politics_Shmolitics',
                       'author': 'Politics_Shmolitics',
                       'text': 'At a press conference, McDonald called it organized fraud at scale.',
                       'tip': 'At a press conference, McDonald called it organized fraud at scale.',
                       'timestamp': 93,
                       'timestamp_seconds': 93,
                       'timestamp_label': '[00:01:33]',
                       'url': 'https://www.youtube.com/watch?v=rcSJIi02YnA&t=93s',
                       'markdown': '[00:01:33](https://www.youtube.com/watch?v=rcSJIi02YnA&t=93s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7GhlupAi3Jg',
                       'title': 'OPERATION GHOSTBUSTERS — The $200 Million Ghost Student Fraud',
                       'channel': 'Scamverge',
                       'author': 'Scamverge',
                       'text': 'These are charges, not convictions.',
                       'tip': 'These are charges, not convictions.',
                       'timestamp': 34,
                       'timestamp_seconds': 34,
                       'timestamp_label': '[00:00:34]',
                       'url': 'https://www.youtube.com/watch?v=7GhlupAi3Jg&t=34s',
                       'markdown': '[00:00:34](https://www.youtube.com/watch?v=7GhlupAi3Jg&t=34s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-RjbcsAnouU',
                       'title': "Operation Ghostbusters: 5 Charged in the 'Ghost Student' Financial Aid "
                                'Fraud',
                       'channel': 'Court Files',
                       'author': 'Court Files',
                       'text': 'So the fraudsters use artificial intelligence to keep the ghost alive.',
                       'tip': 'So the fraudsters use artificial intelligence to keep the ghost alive.',
                       'timestamp': 185,
                       'timestamp_seconds': 185,
                       'timestamp_label': '[00:03:05]',
                       'url': 'https://www.youtube.com/watch?v=-RjbcsAnouU&t=185s',
                       'markdown': '[00:03:05](https://www.youtube.com/watch?v=-RjbcsAnouU&t=185s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'go1eoNNgFRM',
                       'title': 'The 50% Rule: Who Actually Has to Do the Work?',
                       'channel': 'Vet GovCon Blueprint',
                       'author': 'Vet GovCon Blueprint',
                       'text': "That's not a loophole — that's the exact scheme this rule was written to "
                               'stop.',
                       'tip': "That's not a loophole — that's the exact scheme this rule was written to "
                              'stop.',
                       'timestamp': 282,
                       'timestamp_seconds': 282,
                       'timestamp_label': '[00:04:42]',
                       'url': 'https://www.youtube.com/watch?v=go1eoNNgFRM&t=282s',
                       'markdown': '[00:04:42](https://www.youtube.com/watch?v=go1eoNNgFRM&t=282s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'go1eoNNgFRM',
                       'title': 'The 50% Rule: Who Actually Has to Do the Work?',
                       'channel': 'Vet GovCon Blueprint',
                       'author': 'Vet GovCon Blueprint',
                       'text': 'Track it monthly.',
                       'tip': 'Track it monthly.',
                       'timestamp': 358,
                       'timestamp_seconds': 358,
                       'timestamp_label': '[00:05:58]',
                       'url': 'https://www.youtube.com/watch?v=go1eoNNgFRM&t=358s',
                       'markdown': '[00:05:58](https://www.youtube.com/watch?v=go1eoNNgFRM&t=358s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TpwUzqMIZKw',
                       'title': 'Subcontracting Secrets EXPOSED! What Nobody Tells You About Federal '
                                'Contracts',
                       'channel': 'Eric Coffie',
                       'author': 'Eric Coffie',
                       'text': "And anything that we think they can't do 100% can subcontract up to 49% of "
                               'it to somebody else.',
                       'tip': "And anything that we think they can't do 100% can subcontract up to 49% of "
                              'it to somebody else.',
                       'timestamp': 314,
                       'timestamp_seconds': 314,
                       'timestamp_label': '[00:05:14]',
                       'url': 'https://www.youtube.com/watch?v=TpwUzqMIZKw&t=314s',
                       'markdown': '[00:05:14](https://www.youtube.com/watch?v=TpwUzqMIZKw&t=314s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
