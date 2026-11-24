from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'contingency-cost-reduction-telecom-expense-audits',
 'question_prompt': 'How do contingency-based cost-reduction consultants and telecom expense management '
                    'firms find savings, and how do spend visibility and GPO programs feed into that?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Contingency Cost Reduction and Telecom Expense Management Audits',
 'subtitle': 'Contingency-fee expense consulting, consulting cost-cutting frameworks, telecom bill audits '
             'with credits, refunds, and forward savings, the role of a TEM specialist, mobile fleet TEM, '
             'UCaaS expense management for Zoom, Sage expense automation, and OMNIA spend visibility and '
             'private-equity group purchasing',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Contingency cost-reduction shops and telecom expense management (TEM) auditors '
                      'converge on one pitch: nobody pays until savings land, vendors usually stay in '
                      'place, and the money hides in auto-paid invoices nobody reads. Auditel pulled an '
                      '$8,100 back-billing refund off a single $1,200-a-month account and a $165,000 '
                      'credit on a go-behind audit; brightfin recouped roughly $56,000 from a switch left '
                      'live in a closed office. Street mechanics run on a 12-month general ledger, rate '
                      'benchmarking that cut some contract rates by more than 50%, disconnecting '
                      'zero-usage lines, and policing carrier orders until they bill correctly. Calero '
                      'MDSL extends the playbook to Zoom and Teams license reclamation. Practitioners '
                      'split on outsourcing versus internal audits (15-40% versus 3-5% reductions), on fee '
                      'models from contingency share to retainer and hourly, and on whether to swap '
                      'suppliers or squeeze incumbents.',
 'key_metrics': [{'label': 'Single-Account Forward Savings',
                  'metric': 'Single-Account Forward Savings',
                  'value': '$68,000/month bill cut to just under $36,000/month (a little under '
                           '$33,000/month saved)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Auditel disconnected months-dead lines, benchmarked renewal rates, and '
                             'cancelled services at closed satellite offices on one multi-circuit account.',
                  'source': 'Auditel, Inc. Telecom Expense Management ([F00NVfaC6Tk @ 00:02:21])'},
                 {'label': 'Outsourced vs Internal Audit Reduction',
                  'metric': 'Outsourced vs Internal Audit Reduction',
                  'value': '15% to 40% outsourced versus 3% to 5% internal',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Singlesource Telecom compared typical cost reductions from internally run '
                             'telecom audits against outsourced auditing.',
                  'source': 'singlesourcetelecom ([GcLqzAGpP2s @ 00:02:19])'},
                 {'label': 'Go-Behind Audit Credit',
                  'metric': 'Go-Behind Audit Credit',
                  'value': '$165,000 credit on a single account',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Auditel re-audited a client that had already been audited twice by other '
                             'firms and found multiple data-account billing errors.',
                  'source': 'Auditel, Inc. Telecom Expense Management ([YAHf-FXxBCM @ 00:01:35])'},
                 {'label': 'Contingency Client Average Savings',
                  'metric': 'Contingency Client Average Savings',
                  'value': 'In excess of 20% per year, savings found for 100% of clients',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Expense Consulting's shared-savings model with no upfront cost; most clients "
                             'start saving within weeks.',
                  'source': 'Expense Consulting ([o2wyRpIYL0w @ 00:01:34])'}],
 'sections': [{'section': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every operator here starts from the same diagnosis: the money leaks through '
                              "invoices nobody reads. ExpenseSavvy's host watched loan applicants obsess "
                              'over revenue while their vendors sat on auto pay, with zero transparency '
                              'into what the business down the street pays the same vendor for the same '
                              'account [2RDXap2GiBE @ 00:01:28]. brightfin hit the textbook version when '
                              "pulling a new client's telecom invoices: the company had moved out of an "
                              'office, emailed the carrier to shut the switch off, the switch never got '
                              'shut off, and finance kept paying because nobody told finance the office '
                              'had closed; brightfin recouped roughly $56,000 of that erroneous billing '
                              '[lxObl7Zpr2A @ 00:03:06]. Auditel reports the same pattern on '
                              'forward-savings work, where customers closed smaller satellite offices and '
                              'neglected to cancel services, which the Auditel presenter says happens more '
                              'than you might think [F00NVfaC6Tk @ 00:02:06]. RadiusPoint goes further and '
                              'says flatly that every client it was hired by faced waste and overspending '
                              'in telecom, most were overpaying carriers, and none could trace their '
                              'device inventory to a number, a location, and an end user ID [mFoRTIncoOI @ '
                              '00:03:17]. The consensus prerequisite is therefore inventory and visibility '
                              'before negotiation: you cannot cut what you cannot map back to a live user '
                              'or site.',
                              'The commercial consensus is just as tight: the client pays nothing up front '
                              'and the shop eats only from savings it actually lands. Expense Consulting '
                              'says it costs nothing to get started, the firm simply shares the savings it '
                              'finds, claims it has found savings for 100% of its clients, and says those '
                              'clients now average savings in excess of 20% per year, with most saving '
                              'within weeks [o2wyRpIYL0w @ 00:01:34]. Kirk Canol of DCI Solutions pitches '
                              'the identical no-risk structure, getting paid only after the client gets '
                              'savings, and backs it with hit rates: money recovered every time, savings '
                              '80% of the time in freight, telecom, and utilities, 70% of the time in '
                              'insurance, and half the time in office and warehouse supplies or refundable '
                              'sales tax and unclaimed tax credits [meAxKn8Td5k @ 00:00:16]. Auditel '
                              'frames telecom audits as contingency-based, meaning the client pays nothing '
                              'if nothing is found, a no-risk, no-lose alternative to continuing to '
                              'overpay [YAHf-FXxBCM @ 00:01:52]. ExpenseSavvy runs the free analysis, '
                              'charges nothing for the work, and takes a portion of savings only once the '
                              'client starts saving [2RDXap2GiBE @ 00:03:51]. The second shared rule is '
                              'vendor neutrality: keep the incumbent, cut the price, a line DCI and '
                              'Expense Consulting both repeat to clients.',
                              'The levers themselves line up across the generalist and specialist camps. '
                              'Startup Akademia lays out four directions for any cost base: reduce usage, '
                              'automate, optimize the process and cost level, and renegotiate contracts, '
                              'with usage cuts running from fully eliminating an expense to changing the '
                              'specification, using less of something or swapping in a cheaper substitute '
                              '[T9lHBjJeZVI @ 00:00:14]. The TEM shops execute exactly those levers on '
                              'telecom: killing dead lines, downgrading plans, and renegotiating rates. '
                              'Mark from Calero MDSL, after 20 years in expense management, sequences it '
                              'as visibility first, cost ownership second, and says real cost reductions '
                              'show up once you foster that spirit of cost ownership down to department '
                              'heads and individual employees who can reclaim and return their own '
                              "licenses [bQwapQbcKSk @ 00:18:23]. OMNIA Partners' enterprise team adds the "
                              'unglamorous prerequisite: the data has to be cleaned before it can be '
                              'categorized, because the same supplier name can appear 20 times in one data '
                              'file, and without GL coding nobody even knows what some suppliers do for '
                              'the organization [qPpAutcFjBw @ 00:01:28]. Scope is broad by design; '
                              'ExpenseSavvy says there are savings across the board in waste, telecom, and '
                              'insurance, with hundreds of line items in play [2RDXap2GiBE @ 00:04:49].'],
               'table': {'caption': 'Where the contingency and TEM practitioners agree',
                         'headers': ['Consensus Point',
                                     'What The Practitioner Reports',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Auto-paid invoices hide the leaks',
                                   'Owners chase revenue, put vendors on auto pay, and never see what '
                                   'peers pay',
                                   'Pull every recurring vendor charge before pitching any savings number '
                                   'to the client',
                                   'ExpenseSavvy ([2RDXap2GiBE @ 00:01:28])'],
                                  ['Closed sites keep billing for months',
                                   'Switch left live after an office move cost a client roughly $56,000 '
                                   'before recovery',
                                   'Cross-check every carrier account against the current list of open '
                                   'locations',
                                   'brightfin ([lxObl7Zpr2A @ 00:03:06])'],
                                  ['Contingency fee removes all buying friction',
                                   'Nothing paid if nothing found; pitched as a no-risk, no-lose '
                                   'alternative to overpaying',
                                   'Lead with zero upfront cost so the audit sells itself on found money',
                                   'Auditel, Inc. Telecom Expense Management ([YAHf-FXxBCM @ 00:01:52])'],
                                  ['Keep incumbent vendors, lower the price',
                                   'Savings require no vendor changes; if you like your vendors, keep your '
                                   'vendors',
                                   'Negotiate with incumbents first to avoid client resistance to '
                                   'switching suppliers',
                                   'kconole2011 ([meAxKn8Td5k @ 00:01:52])'],
                                  ['Asset inventory is the missing foundation',
                                   'No client could tie devices to a number, a location, and an end user '
                                   'ID',
                                   'Build the asset-to-user inventory before disputing or renegotiating a '
                                   'single line',
                                   'RadiusPoint ([mFoRTIncoOI @ 00:03:17])'],
                                  ['Visibility comes before cost ownership',
                                   'Twenty years in expense management: visibility first, then cost '
                                   'ownership drives reductions',
                                   'Give department heads employee-level views so they surrender unused '
                                   'licenses themselves',
                                   'UC Today News ([bQwapQbcKSk @ 00:18:23])'],
                                  ['Stay engaged after the first win',
                                   'Firm keeps working after patching leaks, continually auditing invoices '
                                   'from then on',
                                   'Structure the engagement for recurring invoice audits rather than a '
                                   'one-time sweep',
                                   'Expense Consulting ([o2wyRpIYL0w @ 00:01:52])']]}},
              {'section': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Intake is deliberately light, opening with a 10-minute call. ExpenseSavvy '
                              'needs exactly one document, a 12-month general ledger exported from the '
                              "client's accounting software; its partner's technology runs that ledger "
                              'against millions of data points sorted by industry, employee count, and '
                              "location, then returns a report along the lines of 'we think we can save "
                              "you X dollars annually on these 10 line items,' pitching potential savings "
                              'of up to 25% of operational expenses [2RDXap2GiBE @ 00:02:29]. The ideal '
                              'target, per ExpenseSavvy, is any business doing 500,000 to 200 million in '
                              'revenue, and the firm does not attack all 100 vendors at once; it starts '
                              'with three to five and negotiates new agreements with the existing vendors '
                              "[2RDXap2GiBE @ 00:03:32]. Auditel's benchmarking lever is the sharpest in "
                              'the set: on a customer that simply was not paying attention when renewing '
                              'its contract, rate benchmarking cut rates by a considerable margin, '
                              'sometimes more than 50% [F00NVfaC6Tk @ 00:01:49]. For portfolio-scale '
                              'buyers, OMNIA Partners says it gathers data, cross-maps where its group '
                              'purchasing programs fit, and typically starts identifying categories and '
                              "implementing within two to three weeks, including one PE-level 'cube of "
                              "cube' rolling up 30-plus portfolio companies [QYe90AHibvQ @ 00:03:11].",
                              'The audit itself splits into two revenue streams. The first is look-back '
                              'money: Auditel found a $139-a-month overcharge on a $1,200-a-month account, '
                              'corrected it going forward, then dug through historical billing and pulled '
                              'an $8,100 refund on that one account alone [YAHf-FXxBCM @ 00:01:02]. On a '
                              'client already audited twice by other firms, Auditel ran what it calls a '
                              'go-behind audit, found multiple billing errors in data accounts, and '
                              'obtained a $165,000 credit on a single account, with more credits beyond '
                              'that across the engagement [YAHf-FXxBCM @ 00:01:19]. The second stream is '
                              'forward savings: on a bill running $68,000 a month, Auditel killed '
                              'months-dead lines, benchmarked rates, and cancelled services at closed '
                              'satellite offices, landing the bill just under $36,000, a saving of a '
                              'little under $33,000 a month on one account; two smaller accounts dropped '
                              'from about $5,600 and $6,200 a month to a little over $900 each '
                              '[F00NVfaC6Tk @ 00:02:21]. Singlesource Telecom flags what the auditor '
                              'actually needs to make those disputes stick: access to past and present '
                              'tariffs, contracts, and rates, plus the staff hours to contact carriers and '
                              'negotiate refunds, which can be the majority of total project time on an '
                              'internal run [GcLqzAGpP2s @ 00:01:02].',
                              'Platform-driven TEM adds in-cycle optimization that a one-time audit cannot '
                              'touch. brightfin staff manually review usage and, when someone has barely '
                              'used a $100 plan, drop it before the invoice cycle closes so the bill lands '
                              'at $10; when five phones out of a 30,000-device fleet eat all the data '
                              'streaming Disney Plus, brightfin blocks Disney Plus on work phones '
                              '[lxObl7Zpr2A @ 00:08:22]. The same shop flags the closet problem: 50 '
                              'recouped phones at $100 a month is $5,000 buried in a $400,000 invoice, '
                              "easy to miss month after month [lxObl7Zpr2A @ 00:07:47]. Calero MDSL's Zoom "
                              "marketplace app pulls license and usage data straight from Zoom's APIs, "
                              'automates moves, adds, and changes, downgrades Pro users who only join '
                              'calls to Basic, and reclaims idle licenses for redeployment; it also '
                              'catches stacking, where one heavy Zoom user holds licenses for one, two, or '
                              'even three other similar products, and feeding HR data in lets it flag '
                              'departed employees still holding active licenses and reclaim them '
                              'automatically [bQwapQbcKSk @ 00:14:25]. RadiusPoint runs nine processes, '
                              'closing the loop by disputing billing errors, recovering credits and '
                              'refunds, and tracking vendor invoices that are not arriving on time so late '
                              'fees and service interruptions are avoided [mFoRTIncoOI @ 00:02:27].'],
               'table': {'caption': 'Street mechanics and the numbers practitioners attached to them',
                         'headers': ['Mechanic',
                                     'Exact Numbers Reported',
                                     'How It Is Executed',
                                     'Expert Source'],
                         'rows': [['General ledger intake and peer benchmarking',
                                   '12-month general ledger in; savings up to 25% of operational expenses '
                                   'pitched',
                                   'Partner technology benchmarks line items by industry, employee count, '
                                   'and location',
                                   'ExpenseSavvy ([2RDXap2GiBE @ 00:02:29])'],
                                  ['Historical back-billing refund on one account',
                                   '$139 monthly overcharge on a $1,200 bill produced an $8,100 refund',
                                   'Correct the rate going forward, then recover years of historical '
                                   'overbilling',
                                   'Auditel, Inc. Telecom Expense Management ([YAHf-FXxBCM @ 00:01:02])'],
                                  ['Forward savings on a large circuit account',
                                   '$68,000 monthly bill cut to just under $36,000 per month',
                                   'Disconnect zero-usage lines, benchmark renewal rates, cancel '
                                   'closed-office services',
                                   'Auditel, Inc. Telecom Expense Management ([F00NVfaC6Tk @ 00:02:21])'],
                                  ['In-cycle mobile plan downgrade before billing',
                                   '$100 plan reduced to $10 before the invoice cycle closes',
                                   "Review usage manually and change the carrier plan on the client's "
                                   'behalf',
                                   'brightfin ([lxObl7Zpr2A @ 00:08:22])'],
                                  ['Outsourced versus internal audit yield',
                                   'Internal audits reduce 3 to 5 percent; outsourced audits 15 to 40 '
                                   'percent',
                                   'Hand bill scouring, carrier disputes, and refund negotiation to '
                                   'outside auditors',
                                   'singlesourcetelecom ([GcLqzAGpP2s @ 00:02:19])'],
                                  ['Workflow automation for new-hire onboarding',
                                   'IT onboarding time per new nurse cut from 23 hours to one hour',
                                   'Automated workflows built on ServiceNow replace manual provisioning '
                                   'steps at Vitas Healthcare',
                                   'brightfin ([lxObl7Zpr2A @ 00:09:17])'],
                                  ['Bank charge and payroll fee audits',
                                   '$200,000 bank charges saved over three years; $51,000 yearly on '
                                   'payroll processing',
                                   'Cut fees in place without changing banks or payroll vendors',
                                   'kconole2011 ([meAxKn8Td5k @ 00:01:30])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the hidden money sits',
                           'body': 'Four plays practitioners use to find savings that earlier audits and '
                                   'internal staff walk past.',
                           'items': ['Run a go-behind audit on accounts other firms already combed: '
                                     'Auditel found multiple data-account billing errors on a client '
                                     'audited twice before and pulled a $165,000 credit on one account '
                                     '[Auditel, Inc. Telecom Expense Management — YAHf-FXxBCM @ 00:01:19].',
                                     'Hunt sales tax that vendors over-collect; DCI says it happens more '
                                     'than you think and it not only finds it but gets the money refunded '
                                     'back to the client [kconole2011 — meAxKn8Td5k @ 00:01:52].',
                                     'Hunt license stacking: heavy Zoom users often hold licenses for one, '
                                     'two, or even three similar products, but bake deliberate redundancy '
                                     'into policy for sales staff who need a backup tool for customer '
                                     'demos [UC Today News — bQwapQbcKSk @ 00:12:20].',
                                     'Prioritize by wave: start with low-hanging-fruit commodity '
                                     'categories at the top of the savings list and push categories the '
                                     'client is not ready for into wave two or wave three [OMNIA Partners '
                                     '— qPpAutcFjBw @ 00:03:22].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pull the ledger and book the findings meeting',
                              'action': 'Collect a 12-month general ledger and run the free savings '
                                        'analysis.',
                              'detail': 'ExpenseSavvy needs only a 12-month general ledger from the '
                                        "client's accounting software, runs the analysis, then meets again "
                                        'to walk through findings before signing the client [ExpenseSavvy '
                                        '— 2RDXap2GiBE @ 00:04:32].'},
                             {'step': 2,
                              'title': 'Inventory every asset to a user',
                              'action': 'Map lines, services, data circuits, and mobile devices to end '
                                        'users and locations.',
                              'detail': "RadiusPoint's first processes are inventorying and auditing "
                                        'telecom assets and services, then assigning those assets to end '
                                        'users and tracking usage to detect abuse and device loss '
                                        '[RadiusPoint — mFoRTIncoOI @ 00:01:46].'},
                             {'step': 3,
                              'title': 'Audit against contract and dispute the gap',
                              'action': 'Check every charge against contract terms and raise disputes on '
                                        'anything extra.',
                              'detail': 'TEM teams audit each invoice to confirm charges match the '
                                        'contract and raise a dispute on any additional charge, because '
                                        'even a small amount recovered is savings for the client [Ancy '
                                        'Alphonse — RV9K4EXWxJs @ 00:02:42].'},
                             {'step': 4,
                              'title': 'Place the orders and police them until they bill right',
                              'action': 'Present recommendations, place approved orders, and monitor them '
                                        'through correct billing.',
                              'detail': 'Auditel places the orders with the provider, follows up, and '
                                        'confirms correct billing, because providers sometimes place '
                                        'orders incorrectly or not at all while the accounts keep billing '
                                        '[Auditel, Inc. Telecom Expense Management — F00NVfaC6Tk @ '
                                        '00:01:18].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The cleanest split on the street is how the auditor gets paid. Expense '
                              'Consulting pitches pure share-of-savings: it costs nothing to get started, '
                              'the firm simply shares the savings it finds, says it has found savings for '
                              '100% of its clients, and claims an average savings in excess of 20 percent '
                              'per year, with most clients saving within weeks [o2wyRpIYL0w @ 00:01:34]. '
                              'Auditel runs the same no-find, no-fee contingency on telecom audits, '
                              'calling it a no risk, no lose alternative to continuing to overpay for '
                              'telecom expense [YAHf-FXxBCM @ 00:01:52]. ExpenseSavvy layers a '
                              'channel-partner model on top, paid only on actual savings and taking a '
                              'portion once the client starts saving [2RDXap2GiBE @ 00:03:51]. Single '
                              'Source Telecom breaks ranks with the contingency purists: some auditing '
                              'firms take a percentage of recovered revenues, while others charge a '
                              'one-time fee, a retainer, or an hourly rate, and its own fees are set by '
                              'the solution the client selects, from a simple audit all the way up to a '
                              'comprehensive ongoing outsourced network and billing management system '
                              '[GcLqzAGpP2s @ 00:03:18]. The operator takeaway: contingency wins the first '
                              'meeting because the buyer never has to find room in the budget, but ongoing '
                              'managed scope gets priced as a service rather than as a cut of recoveries.',
                              'Whether to keep the incumbent vendor is the second fault line. Kirk Conole '
                              'of DCI Solutions sells the no-switch angle hard: savings require no changes '
                              'to your vendors, so if you like your vendors keep them but lower the price, '
                              'and one client saved $200,000 over three years on bank charges without '
                              'changing banks [meAxKn8Td5k @ 00:01:52]. ExpenseSavvy runs the same play, '
                              'negotiating new agreements with the existing vendor instead of replacing '
                              'anyone, so the owner never has to change who they buy from [2RDXap2GiBE @ '
                              "00:03:13]. Startup Akademia's consulting framework goes the other way: "
                              'change the supplier through an auction among potential suppliers and pick '
                              'the best offer, or change the form of use, moving from paying for something '
                              'to renting it, so the producer is forced to optimize its own cost and '
                              'therefore yours [T9lHBjJeZVI @ 00:02:29]. On who should run the work, '
                              'Single Source Telecom quotes the sharpest split in the field: internally '
                              'run audits typically land a 3 to 5% cost reduction, while outsourced '
                              'auditing normally lands 15 to 40%, and most of the time outsourcing the '
                              'auditing and expense management pays for itself at a fraction of the cost '
                              'of an internal audit [GcLqzAGpP2s @ 00:02:19].',
                              'How the data gets in, and how wide the first sweep goes, splits the field '
                              'further. ExpenseSavvy needs nothing but a 12-month general ledger from the '
                              'accounting software, runs it against millions of data points keyed to '
                              'industry, employee count and location, and deliberately starts with three '
                              'to five vendors rather than all 100 [2RDXap2GiBE @ 00:02:29]. Calero MDSL '
                              "plugs straight into Zoom's APIs through its marketplace app, seeding "
                              'licenses and spend for a turnkey implementation and onboarding UCaaS data '
                              'in minutes instead of weeks or months [bQwapQbcKSk @ 00:09:53]. Brightfin '
                              'argues the system of record matters most, storing mobile, fixed and cloud '
                              'invoice data inside ServiceNow so spend lines up against tickets, '
                              'departments and projects, while other TEMs keep invoices in a separate '
                              'system that is extremely difficult to make talk to IT service data '
                              '[lxObl7Zpr2A @ 00:11:04]. OMNIA Partners warns that before categorizing '
                              'anything you must harmonize supplier names, since the same supplier can '
                              'show up 20 times in one data file, then sequence the work in waves, '
                              'starting with low-hanging commodity categories and pushing the rest to wave '
                              'two or wave three [qPpAutcFjBw @ 00:01:28]. The quick-ledger route wins '
                              'speed to a savings pitch; the API and ServiceNow routes win ongoing control '
                              'over recurring spend.'],
               'table': {'caption': 'Competing playbooks for contingency cost reduction and TEM audits',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How the auditor gets paid for the work',
                                   'Pure contingency: no find, no fee, client never budgets for the audit',
                                   'Menu pricing: percentage of recoveries, one-time fee, retainer or '
                                   'hourly rate',
                                   'Auditel, Inc. Telecom Expense Management ([YAHf-FXxBCM @ 00:01:52]); '
                                   'singlesourcetelecom ([GcLqzAGpP2s @ 00:03:18])'],
                                  ['Handling the incumbent vendor during negotiation',
                                   'Keep the vendor and cut price, bank charges reduced without switching '
                                   'banks',
                                   'Run a supplier auction or shift from buying to renting to force '
                                   'optimization',
                                   'kconole2011 ([meAxKn8Td5k @ 00:01:52]); Startup Akademia ([T9lHBjJeZVI '
                                   '@ 00:02:29])'],
                                  ['Who actually runs the bill audit',
                                   'Internal staff audits typically yield only a 3 to 5% cost reduction',
                                   'Outsourced auditing normally yields 15 to 40% and usually pays for '
                                   'itself',
                                   'singlesourcetelecom ([GcLqzAGpP2s @ 00:02:19])'],
                                  ['Make or buy a recurring service',
                                   'Buy from a specialist supplier who may deliver the service more '
                                   'cheaply',
                                   'Re-check after optimizing; on many occasions doing it internally '
                                   'proves cheaper',
                                   'Startup Akademia ([8ORoloHxouk @ 00:02:04])'],
                                  ['How spend data gets into the analysis',
                                   'Twelve-month general ledger benchmarked against millions of peer data '
                                   'points',
                                   'Direct API connection via the Zoom marketplace app, onboarding in '
                                   'minutes',
                                   'ExpenseSavvy ([2RDXap2GiBE @ 00:02:29]); UC Today News ([bQwapQbcKSk @ '
                                   '00:09:53])'],
                                  ['Where the expense platform lives day to day',
                                   'Own hosted SaaS, sold self-service or wrapped in a holistic managed '
                                   'service',
                                   'Invoice data stored natively inside ServiceNow beside IT service '
                                   'tickets and projects',
                                   'UC Today News ([bQwapQbcKSk @ 00:19:16]); brightfin ([lxObl7Zpr2A @ '
                                   '00:10:47])'],
                                  ['Policy on duplicate or idle collaboration licenses',
                                   'Reclaim unused and redundant licenses automatically and redeploy them '
                                   'elsewhere',
                                   'Bake deliberate redundancy into policy, such as a backup UCaaS tool '
                                   'for salespeople',
                                   'UC Today News ([bQwapQbcKSk @ 00:12:58])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure the TEM operators report is the disconnect that '
                              'never happened. Brightfin onboarded a client that had moved out of an '
                              'office long ago and emailed the carrier to shut the switch off; it never '
                              'got shut off, finance kept paying the invoices because it did not know the '
                              'office had closed, and Brightfin recouped roughly $56,000 in erroneous '
                              'billing [lxObl7Zpr2A @ 00:03:06]. Auditel hit the same pattern in its '
                              'forward-savings work: lines with no use for months still billing, plus '
                              'closed satellite offices whose services were never canceled, which it says '
                              'happens more than you might think [F00NVfaC6Tk @ 00:02:06]. Auditel adds '
                              'that the order cycle itself is a trap, because providers sometimes place '
                              'disconnect orders incorrectly or do not place them at all, and the accounts '
                              'keep billing the entire time, so orders must be monitored rigorously until '
                              'the bill confirms the change [F00NVfaC6Tk @ 00:01:18]. Ancy Alphonse '
                              'describes the closed-site variant from the analyst chair: devices moved or '
                              'ported to a different vendor, the building empty, yet charges persist on '
                              'the invoice until someone works the vendor and discovers a modem still '
                              'activated at the site [RV9K4EXWxJs @ 00:04:19].',
                              'Auto-pay is where leakage hides. ExpenseSavvy says owners put vendors on '
                              'auto pay and forget what they are paying, with no transparency into what '
                              'the business down the street pays the same vendor for the same account '
                              '[2RDXap2GiBE @ 00:01:28]. Brightfin sizes the blind spot: 50 phones sitting '
                              'in a closet at about $100 a month each is roughly $5,000 buried inside a '
                              '$400,000 total charge, very easy to miss even a year after the employee '
                              'left [lxObl7Zpr2A @ 00:07:47]. Prior audits are no proof of a clean bill '
                              'either. Auditel ran a go-behind audit on a client that had been audited '
                              'twice in the not-too-distant past, found multiple billing errors in data '
                              'accounts overbilled for a very long time, and obtained a $165,000 credit on '
                              'a single account [YAHf-FXxBCM @ 00:01:19]. The renewal desk is another '
                              'leak: Auditel found a client that was not overcharged per se but was paying '
                              'far more than it should after renewing without attention, and rate '
                              'benchmarking cut rates, sometimes by more than 50% [F00NVfaC6Tk @ '
                              '00:01:49]. The fixed-line results show the scale: one account fell from '
                              '$68,000 to just under $36,000 a month, and two others dropped from about '
                              '$5,600 and $6,200 to a little over $900 each.',
                              'In-house teams fail on bandwidth and memory. Single Source Telecom warns '
                              'that staff must scour every bill, then contact carriers and negotiate '
                              'refunds, which can be the majority of project time, and they still need '
                              'access to past and present tariffs, contracts and rates, plus a procedure '
                              'that survives turnover and retraining [GcLqzAGpP2s @ 00:01:02]. Calero MDSL '
                              'sees the SaaS version of the leak: everyone got a license when work went '
                              'remote during COVID, utilization is now low or zero, the same heavy Zoom '
                              'user may carry one, two or three other similar products, and departed '
                              'employees keep active licenses until off-boarding flags reclaim them '
                              '[bQwapQbcKSk @ 00:12:00]. RadiusPoint reports that before engagement none '
                              'of its clients could tie device inventory to a number, a location and an '
                              'end-user ID, a number faced loss, theft and usage abuse, and invoices that '
                              'do not arrive on time set up late fees and service interruptions '
                              '[mFoRTIncoOI @ 00:03:17]. On labor economics, Brightfin cut Vitas '
                              "Healthcare's IT setup work from 23 hours per new hire to one hour through "
                              'automated workflows [lxObl7Zpr2A @ 00:09:41]. Every one of these leaks '
                              'compounds month after month until someone with the tooling and the time '
                              'goes looking.'],
               'table': {'caption': 'Firsthand leakage cases and their measured impact',
                         'headers': ['Failure Mode',
                                     'What Happened',
                                     'Dollar or Time Impact',
                                     'Expert Source'],
                         'rows': [['Carrier disconnect requested by email but never executed',
                                   'Client emailed carrier to kill switch at vacated office; billing '
                                   'continued and finance kept paying',
                                   'About $56,000 recouped as erroneous billing for that one company',
                                   'brightfin ([lxObl7Zpr2A @ 00:03:24])'],
                                  ['Closed satellite offices and idle lines left billing',
                                   'Offices closed without canceling services, plus lines with no usage '
                                   'for months',
                                   'One account cut from $68,000 a month to just under $36,000',
                                   'Auditel, Inc. Telecom Expense Management ([F00NVfaC6Tk @ 00:02:21])'],
                                  ['Trusting two earlier audits as a clean bill',
                                   'Client audited twice before was still overbilled on data accounts for '
                                   'a long time',
                                   '$165,000 credit obtained on a single account through a go-behind audit',
                                   'Auditel, Inc. Telecom Expense Management ([YAHf-FXxBCM @ 00:01:35])'],
                                  ['Small recurring overcharge ignored for years',
                                   'A $139 monthly overcharge sat on a $1,200-a-month bill for years',
                                   'Bill reduced going forward plus a refund of the historical overbilling',
                                   'Auditel, Inc. Telecom Expense Management ([YAHf-FXxBCM @ 00:01:02])'],
                                  ["Departed employees' phones stored in a closet",
                                   'Devices recouped from leavers but the carrier plans were never turned '
                                   'off',
                                   'Roughly $5,000 a month hidden inside a $400,000 total charge',
                                   'brightfin ([lxObl7Zpr2A @ 00:07:28])'],
                                  ['Vendors over-collecting sales tax without anyone noticing',
                                   'Vendors over-collect sales tax more than buyers think, and staff '
                                   'cannot see everything',
                                   'Over-collected tax found and refunded back to the client',
                                   'kconole2011 ([meAxKn8Td5k @ 00:02:11])'],
                                  ['Finance teams chasing receipts and reconciling by hand',
                                   'Card transactions reconciled manually with constant follow-up on '
                                   'missing receipts',
                                   'Average of 30-plus hours a month lost by accountants and finance teams',
                                   'Sage Expense Management ([HJSf4yb3-CM @ 00:00:00])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do Not Book a Saving Until the Invoice Proves It',
                           'body': 'Every reported loss traces back to a change that was requested but '
                                   'never verified on the bill, an audit treated as final, or a license '
                                   'nobody owned. Clear these four checks before reporting savings to a '
                                   'client.',
                           'items': ['Track every disconnect and rate-change order until the next invoice '
                                     'confirms it, because providers place orders incorrectly or not at '
                                     'all while the account keeps billing [Auditel, Inc. Telecom Expense '
                                     'Management — F00NVfaC6Tk @ 00:01:33].',
                                     'On any closed site, work the vendor line by line for leftover '
                                     'equipment such as a still-activated modem generating charges after '
                                     'devices were moved or ported [Ancy Alphonse — RV9K4EXWxJs @ '
                                     '00:04:19].',
                                     'Never accept a prior audit as the last word; run a go-behind audit '
                                     'on data accounts, where a twice-audited client still yielded a '
                                     '$165,000 credit [Auditel, Inc. Telecom Expense Management — '
                                     'YAHf-FXxBCM @ 00:01:19].',
                                     "Tie every license to HR master data so departed employees' active "
                                     'licenses are flagged and reclaimed at off-boarding [UC Today News — '
                                     'bQwapQbcKSk @ 00:14:25].']}}],
 'pull_quote': '"You can\'t save money you don\'t see, and expecting your staff to see everything, well '
               'that\'s just unrealistic." — kconole2011 (meAxKn8Td5k @ 00:02:11).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Pull a 12-month general ledger from the accounting software and attack three to '
                      'five vendors first instead of all 100 [ExpenseSavvy — 2RDXap2GiBE @ 00:03:32].',
                      'Inventory and audit every line, service, data circuit and mobile device, then '
                      'assign each asset to an end user and track usage [RadiusPoint — mFoRTIncoOI @ '
                      '00:01:46].',
                      'Correct each overcharge going forward, then go back through historical billing to '
                      'claim the refund on years of overpayment [Auditel, Inc. Telecom Expense Management '
                      '— YAHf-FXxBCM @ 00:01:02].',
                      "Benchmark rates before and at contract renewal; rate benchmarking cut one client's "
                      'rates sometimes by more than 50% [Auditel, Inc. Telecom Expense Management — '
                      'F00NVfaC6Tk @ 00:01:49].',
                      'Drop underused mobile plans before the invoice cycle closes and block data-heavy '
                      'apps like Disney Plus on work phones [brightfin — lxObl7Zpr2A @ 00:08:22].',
                      'Harmonize supplier names, categorize spend, and sequence categories into waves '
                      'starting with low-hanging commodity categories [OMNIA Partners — qPpAutcFjBw @ '
                      '00:03:22].'],
 'statutory_citations': [{'title': 'Auditel, Inc. Telecom Expense Management — Technology expense '
                                   'management - Why Do a telecom audit? [00:01:19]',
                          'url': 'https://www.youtube.com/watch?v=YAHf-FXxBCM&t=79s',
                          'relevance': 'Primary practitioner testimony on contingency go-behind audits '
                                       'recovering a $165,000 credit on a single account.'},
                         {'title': 'brightfin — What is Telecom Expense Management (TEM)? [00:03:06]',
                          'url': 'https://www.youtube.com/watch?v=lxObl7Zpr2A&t=186s',
                          'relevance': 'Primary practitioner testimony on a never-executed carrier '
                                       'disconnect and the $56,000 recovery.'},
                         {'title': 'singlesourcetelecom — Bill Auditing and Telecom Expense Management '
                                   'Tips [00:02:19]',
                          'url': 'https://www.youtube.com/watch?v=GcLqzAGpP2s&t=139s',
                          'relevance': 'Primary practitioner testimony on internal 3 to 5% versus '
                                       'outsourced 15 to 40% audit results and fee structures.'},
                         {'title': 'Auditel, Inc. Telecom Expense Management — Telecom Expense Management: '
                                   'Why have a telecom audit? Part 3 Forward Savings [00:02:21]',
                          'url': 'https://www.youtube.com/watch?v=F00NVfaC6Tk&t=141s',
                          'relevance': 'Primary practitioner testimony on forward savings cutting a '
                                       '$68,000 monthly bill to just under $36,000.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'bQwapQbcKSk',
                       'title': 'Next Level UCaaS Expense Management for Zoom - UC Today News',
                       'channel': 'UC Today News',
                       'author': 'UC Today News',
                       'text': "We're able to right-size that and reclaim those licenses automatically so "
                               'they can be redeployed to other areas of business that maybe do want to '
                               'use them.',
                       'tip': "We're able to right-size that and reclaim those licenses automatically so "
                              'they can be redeployed to other areas of business that maybe do want to use '
                              'them.',
                       'timestamp': 687,
                       'timestamp_seconds': 687,
                       'timestamp_label': '[00:11:27]',
                       'url': 'https://www.youtube.com/watch?v=bQwapQbcKSk&t=687s',
                       'markdown': '[00:11:27](https://www.youtube.com/watch?v=bQwapQbcKSk&t=687s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o2wyRpIYL0w',
                       'title': 'Cost Reduction Consultants - Contingency Based - Expense Consulting',
                       'channel': 'Expense Consulting',
                       'author': 'Expense Consulting',
                       'text': 'It costs nothing for us to get started, we simply share the savings we '
                               "find, which means you don't have to find room in the budget.",
                       'tip': 'It costs nothing for us to get started, we simply share the savings we '
                              "find, which means you don't have to find room in the budget.",
                       'timestamp': 94,
                       'timestamp_seconds': 94,
                       'timestamp_label': '[00:01:34]',
                       'url': 'https://www.youtube.com/watch?v=o2wyRpIYL0w&t=94s',
                       'markdown': '[00:01:34](https://www.youtube.com/watch?v=o2wyRpIYL0w&t=94s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'meAxKn8Td5k',
                       'title': 'Business Cost Reduction Consultants FREE Consultation, San Deigo, Irvine '
                                'CA',
                       'channel': 'kconole2011',
                       'author': 'kconole2011',
                       'text': 'Our savings require no changes to your vendors, so if you like your '
                               "vendors keep your vendors but let's lower the price.",
                       'tip': 'Our savings require no changes to your vendors, so if you like your vendors '
                              "keep your vendors but let's lower the price.",
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=meAxKn8Td5k&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=meAxKn8Td5k&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T9lHBjJeZVI',
                       'title': 'How to cut costs – Cost Reduction Framework from Management Consulting '
                                'Projects',
                       'channel': 'Startup Akademia',
                       'author': 'Startup Akademia',
                       'text': 'Sometimes it is cheaper to do it internally than externally.',
                       'tip': 'Sometimes it is cheaper to do it internally than externally.',
                       'timestamp': 134,
                       'timestamp_seconds': 134,
                       'timestamp_label': '[00:02:14]',
                       'url': 'https://www.youtube.com/watch?v=T9lHBjJeZVI&t=134s',
                       'markdown': '[00:02:14](https://www.youtube.com/watch?v=T9lHBjJeZVI&t=134s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8ORoloHxouk',
                       'title': 'Management Consulting Case Interview – a framework for cost cutting',
                       'channel': 'Startup Akademia',
                       'author': 'Startup Akademia',
                       'text': 'You can renegotiate the contracts with current suppliers, so get better '
                               'conditions, maybe lower prices, extended payment terms.',
                       'tip': 'You can renegotiate the contracts with current suppliers, so get better '
                              'conditions, maybe lower prices, extended payment terms.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=8ORoloHxouk&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=8ORoloHxouk&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '2RDXap2GiBE',
                       'title': 'Cost Reduction Strategies for Business Owners',
                       'channel': 'ExpenseSavvy',
                       'author': 'ExpenseSavvy',
                       'text': "We don't start and go after all 100 of your vendors, we strategically do "
                               'it, we usually start with three to five of those vendors.',
                       'tip': "We don't start and go after all 100 of your vendors, we strategically do "
                              'it, we usually start with three to five of those vendors.',
                       'timestamp': 212,
                       'timestamp_seconds': 212,
                       'timestamp_label': '[00:03:32]',
                       'url': 'https://www.youtube.com/watch?v=2RDXap2GiBE&t=212s',
                       'markdown': '[00:03:32](https://www.youtube.com/watch?v=2RDXap2GiBE&t=212s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lxObl7Zpr2A',
                       'title': 'What is Telecom Expense Management (TEM)?',
                       'channel': 'brightfin',
                       'author': 'brightfin',
                       'text': 'They had moved out of an office a long time ago, emailed the carrier to '
                               'shut that switch off and it never got shut off.',
                       'tip': 'They had moved out of an office a long time ago, emailed the carrier to '
                              'shut that switch off and it never got shut off.',
                       'timestamp': 186,
                       'timestamp_seconds': 186,
                       'timestamp_label': '[00:03:06]',
                       'url': 'https://www.youtube.com/watch?v=lxObl7Zpr2A&t=186s',
                       'markdown': '[00:03:06](https://www.youtube.com/watch?v=lxObl7Zpr2A&t=186s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YAHf-FXxBCM',
                       'title': 'Technology expense management - Why Do a telecom audit?',
                       'channel': 'Auditel, Inc. Telecom Expense Management',
                       'author': 'Auditel, Inc. Telecom Expense Management',
                       'text': 'They engaged us to do what we call a go behind audit for them and we found '
                               'multiple billing errors in their data accounts.',
                       'tip': 'They engaged us to do what we call a go behind audit for them and we found '
                              'multiple billing errors in their data accounts.',
                       'timestamp': 79,
                       'timestamp_seconds': 79,
                       'timestamp_label': '[00:01:19]',
                       'url': 'https://www.youtube.com/watch?v=YAHf-FXxBCM&t=79s',
                       'markdown': '[00:01:19](https://www.youtube.com/watch?v=YAHf-FXxBCM&t=79s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GcLqzAGpP2s',
                       'title': 'Bill Auditing and Telecom Expense Management Tips',
                       'channel': 'singlesourcetelecom',
                       'author': 'singlesourcetelecom',
                       'text': 'Most internally run audits result in a 3 to 5% reduction in cost, whereas '
                               'with outsourced auditing the reduction is normally in the range of 15 to '
                               '40%.',
                       'tip': 'Most internally run audits result in a 3 to 5% reduction in cost, whereas '
                              'with outsourced auditing the reduction is normally in the range of 15 to '
                              '40%.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=GcLqzAGpP2s&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=GcLqzAGpP2s&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mFoRTIncoOI',
                       'title': 'What does a Telecom Expense Management Specialist Do? How does TEM Help '
                                'Cutting Costs?',
                       'channel': 'RadiusPoint',
                       'author': 'RadiusPoint',
                       'text': 'None of them could track their device inventory to a number, a location '
                               'and an end user ID.',
                       'tip': 'None of them could track their device inventory to a number, a location and '
                              'an end user ID.',
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=mFoRTIncoOI&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=mFoRTIncoOI&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'F00NVfaC6Tk',
                       'title': 'Telecom Expense Management: Why have a telecom audit? Part 3 Forward '
                                'Savings',
                       'channel': 'Auditel, Inc. Telecom Expense Management',
                       'author': 'Auditel, Inc. Telecom Expense Management',
                       'text': "It's really important that orders be monitored rigorously to ensure things "
                               'go as planned, as there are times where the provider places them '
                               "incorrectly or doesn't place them at all.",
                       'tip': "It's really important that orders be monitored rigorously to ensure things "
                              'go as planned, as there are times where the provider places them '
                              "incorrectly or doesn't place them at all.",
                       'timestamp': 78,
                       'timestamp_seconds': 78,
                       'timestamp_label': '[00:01:18]',
                       'url': 'https://www.youtube.com/watch?v=F00NVfaC6Tk&t=78s',
                       'markdown': '[00:01:18](https://www.youtube.com/watch?v=F00NVfaC6Tk&t=78s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'F00NVfaC6Tk',
                       'title': 'Telecom Expense Management: Why have a telecom audit? Part 3 Forward '
                                'Savings',
                       'channel': 'Auditel, Inc. Telecom Expense Management',
                       'author': 'Auditel, Inc. Telecom Expense Management',
                       'text': 'If you had 50 accounts that we were able to save an average of two hundred '
                               "dollars a month on, that's a hundred and twenty thousand dollars a year, "
                               'year after year.',
                       'tip': 'If you had 50 accounts that we were able to save an average of two hundred '
                              "dollars a month on, that's a hundred and twenty thousand dollars a year, "
                              'year after year.',
                       'timestamp': 206,
                       'timestamp_seconds': 206,
                       'timestamp_label': '[00:03:26]',
                       'url': 'https://www.youtube.com/watch?v=F00NVfaC6Tk&t=206s',
                       'markdown': '[00:03:26](https://www.youtube.com/watch?v=F00NVfaC6Tk&t=206s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HJSf4yb3-CM',
                       'title': 'Introducing Sage Expense Management',
                       'channel': 'Sage Expense Management',
                       'author': 'Sage Expense Management',
                       'text': 'Accountants and finance teams spend an average of 30 plus hours a month '
                               'chasing receipts and reconciling transactions.',
                       'tip': 'Accountants and finance teams spend an average of 30 plus hours a month '
                              'chasing receipts and reconciling transactions.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=HJSf4yb3-CM&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=HJSf4yb3-CM&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RV9K4EXWxJs',
                       'title': 'Telecom Expense Management',
                       'channel': 'Ancy Alphonse',
                       'author': 'Ancy Alphonse',
                       'text': 'They work with the vendor, they find out what exactly the charges are, and '
                               "then we come to okay, there is a modem activated there, so that's why "
                               'there is a charge.',
                       'tip': 'They work with the vendor, they find out what exactly the charges are, and '
                              "then we come to okay, there is a modem activated there, so that's why there "
                              'is a charge.',
                       'timestamp': 259,
                       'timestamp_seconds': 259,
                       'timestamp_label': '[00:04:19]',
                       'url': 'https://www.youtube.com/watch?v=RV9K4EXWxJs&t=259s',
                       'markdown': '[00:04:19](https://www.youtube.com/watch?v=RV9K4EXWxJs&t=259s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aIRwF9gyA-w',
                       'title': 'Telecom Expense Management',
                       'channel': 'Deutsche Telekom - B2B Europe',
                       'author': 'Deutsche Telekom - B2B Europe',
                       'text': 'Virtually every employee has a mobile connection and sometimes multiple '
                               'ones, and this can result in ineffective cost tracking and over usage.',
                       'tip': 'Virtually every employee has a mobile connection and sometimes multiple '
                              'ones, and this can result in ineffective cost tracking and over usage.',
                       'timestamp': 5,
                       'timestamp_seconds': 5,
                       'timestamp_label': '[00:00:05]',
                       'url': 'https://www.youtube.com/watch?v=aIRwF9gyA-w&t=5s',
                       'markdown': '[00:00:05](https://www.youtube.com/watch?v=aIRwF9gyA-w&t=5s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QYe90AHibvQ',
                       'title': 'Unlocking Private Equity Value with OMNIA Partners’ Spend Path and The '
                                'Power of Group Purchasing',
                       'channel': 'OMNIA Partners',
                       'author': 'OMNIA Partners',
                       'text': 'As integration increases, you have more disparate systems and more '
                               'opportunities for error.',
                       'tip': 'As integration increases, you have more disparate systems and more '
                              'opportunities for error.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=QYe90AHibvQ&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=QYe90AHibvQ&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qPpAutcFjBw',
                       'title': 'Spend Visibility: Your Tool for Greater Efficiencies and Cost Savings',
                       'channel': 'OMNIA Partners',
                       'author': 'OMNIA Partners',
                       'text': 'A lot of times you see the same supplier name 20 times in the data file, '
                               'so you got to clean that up before you start categorizing it.',
                       'tip': 'A lot of times you see the same supplier name 20 times in the data file, so '
                              'you got to clean that up before you start categorizing it.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=qPpAutcFjBw&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=qPpAutcFjBw&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
