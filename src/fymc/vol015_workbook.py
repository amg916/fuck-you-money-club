from __future__ import annotations

def build_volume_015_workbook() -> dict:
    return {'workbook_id': 'wb-015-judgment-recovery',
 'volume_id': 'vol-015-judgment-recovery',
 'title': 'Judgment Recovery — Practitioner Testimony Operator Workbook',
 'subtitle': "A working operator's planner for screening unpaid judgments, securing clean assignments, "
             'staying inside legal-practice boundaries, building the enforcement stack, running debtor '
             'examinations, firing garnishments and bank levies, and recording liens that hold their place '
             'in line',
 'worksheets': [{'worksheet_id': 'ws-01',
                 'number': 1,
                 'title': 'Opportunity Screen and Assignment Paperwork',
                 'purpose': 'Turn the judgment recovery opportunity into a disciplined intake system. Set '
                            'your contingency or purchase terms, size your runway, screen out dead and '
                            'uncollectible files before signing anyone, and lock down the notarized '
                            'assignment, legal-practice limits, and satisfaction filings that protect '
                            'every deal.',
                 'chapter_ref': 'Q1-Q2',
                 'instructions': ['Complete every field in order, because the screening fields decide '
                                  'whether the paperwork fields ever get used on a given file.',
                                  'Anchor each answer to a specific practitioner figure, such as a split '
                                  'percentage, garnishment cost, or collectible share, rather than a '
                                  'general impression.',
                                  'Write your numbers as ranges where practitioners disagree, and note '
                                  "which practitioner's figure you are adopting as your working "
                                  'assumption.',
                                  'Treat the dead-file screen and collectibility rating as hard gates; a '
                                  'file that fails either one never reaches the assignment stage.',
                                  'Revisit this worksheet after your first ten files and replace any '
                                  'benchmark that your own results have contradicted.'],
                 'fields': [{'name': 'market_thesis',
                             'type': 'textarea',
                             'prompt': 'State in your own words why unpaid judgments create an opening for '
                                       'a recovery operator. Name the unpaid share you are relying on, the '
                                       'source of that figure, and the one practitioner warning that '
                                       'tempers your expectations before you commit capital.',
                             'example': 'Courts award money but never enforce it, and roughly 80 to 90 '
                                        'percent of civil judgments are never recovered [Cross the River, '
                                        'Find the Treasure — Ss8eyzh_cQ8 @ 00:01:25]. My tempering warning '
                                        'comes from Cynthia Schmidt, who rates only about 70 percent of '
                                        'old unpaid judgments collectible, so I plan as if three in ten '
                                        'files will be declined at intake.'},
                            {'name': 'revenue_model',
                             'type': 'text',
                             'prompt': 'Write the contingency split you will offer judgment creditors, the '
                                       'expenses and interest you will add on top, and the batch math you '
                                       'expect from one round of solicitation letters, using a '
                                       'practitioner figure as your starting benchmark.',
                             'example': 'I charge fifty percent of the amount collected on every '
                                        'assignment, plus accrued interest and all expenses [Cross the '
                                        'River, Find the Treasure — TiGcICs90xE @ 00:01:18]. My benchmark '
                                        'batch is 100 letters producing seven to nine winning files '
                                        'averaging $2,000 each, or $16,000 split evenly, leaving about '
                                        '$8,000 to me before interest and enforcement cost recovery.'},
                            {'name': 'settlement_stream',
                             'type': 'textarea',
                             'prompt': 'Describe how you will turn bank garnishments into a recurring '
                                       'monthly payment stream. Include the garnishment cost, the down '
                                       'payment and monthly amount you will accept for dismissing the '
                                       'writ, and how many new files per month you need.',
                             'example': "Following Rich Meyer, I locate the debtor's bank account before "
                                        'anything else, garnish for $188, then offer to dismiss the writ '
                                        'in exchange for $500 down plus $100 to $200 a month. Repeating '
                                        'that on ten files a month should build toward roughly $3,000 per '
                                        'month by the third month [Default Investor Association — '
                                        'fjA8sRRh0ZI @ 00:22:13].'},
                            {'name': 'time_and_runway',
                             'type': 'text',
                             'prompt': 'Estimate the hours you will spend on each judgment, the typical '
                                       'collection timeline, and how long you can operate before first '
                                       'revenue arrives. Note which enforcement routes stretch the '
                                       'timeline and how you will fund the gap.',
                             'example': 'Evan Ross puts direct work at one to two hours per judgment '
                                        'across an average eight-week collection, with longer timelines '
                                        'when forcing property sales or liens [Franchise Brokers '
                                        'Association — YqjXCyNkUZ8 @ 00:05:38]. He also reports six months '
                                        'to first revenue, so I am reserving six months of living expenses '
                                        'and filing fees before signing my first creditor.'},
                            {'name': 'dead_file_screen',
                             'type': 'textarea',
                             'prompt': 'List the checks you run before preparing any assignment so you '
                                       'never start work on a dead file. Cover bankruptcy, death records, '
                                       'attachable assets, and exemptions, and state the single condition '
                                       'that makes you decline a file outright.',
                             'example': 'Step one is bankruptcy filings and death records, checked before '
                                        'the assignment is drafted [TheJRInstitute — 3p5TZGrk1og @ '
                                        '00:05:09]. Step two confirms an attachable asset exists, because '
                                        'head-of-household exemptions can make wage and bank garnishment '
                                        'difficult. Active-duty military status does not end the screen, '
                                        'since wages can still be garnished. No identifiable asset means I '
                                        'decline the file.'},
                            {'name': 'collectibility_rating',
                             'type': 'textarea',
                             'prompt': 'Build your collectibility rating for each judgment. Name the '
                                       'factors you score, how you weigh where the debtor moved, the live '
                                       'amount, and competing judgments, and the cutoff below which you '
                                       'refuse the assignment or decline to buy.',
                             'example': 'I rate every file on three factors Cynthia Schmidt names: where '
                                        'the debtor moved, how much of the judgment is still live, and '
                                        'whether other judgments already sit against the debtor [cynthia '
                                        'schmidt — t_Wf5tSZn4s @ 00:01:02]. Files scoring in the bottom '
                                        'tier join the roughly 30 percent she calls uncollectible, and I '
                                        'pass on them without exception.'},
                            {'name': 'assignment_paperwork',
                             'type': 'textarea',
                             'prompt': 'Map the exact paperwork sequence that gives you legal authority to '
                                       'collect. Identify which documents require a notary, where each is '
                                       'filed, and the moment you are allowed to begin collection activity '
                                       'on a newly signed judgment.',
                             'example': "Lance converts a client's $10,000 judgment into a notarized "
                                        'assignment plus an agreement to purchase judgment, then files it '
                                        'with the court. The assignment must be signed in front of a '
                                        'notary, filed, and returned by the court before any collection '
                                        'begins [Judgment Recovery Training Online — L2dopNFjS6s @ '
                                        "00:04:17]. My first post-return step is the driver's license "
                                        'suspension paperwork.'},
                            {'name': 'buy_or_contingency',
                             'type': 'textarea',
                             'prompt': 'Decide whether you will take judgments on contingency, buy them '
                                       'outright for cash, or buy them on future pay. State the price or '
                                       'share you will pay the original creditor and the settlement figure '
                                       'you will target with debtors.',
                             'example': "For no-money-down deals I use Schmidt's future-pay structure, "
                                        'paying 15 to 20 percent of collections back to the original '
                                        'creditor until the judgment is satisfied [cynthia schmidt — '
                                        't_Wf5tSZn4s @ 00:01:25]. For cash buys, I pay about $500 for a '
                                        '$5,000 judgment and send the debtor a one-time settlement '
                                        'agreement near $1,500 before starting post-judgment proceedings.'},
                            {'name': 'upl_boundaries',
                             'type': 'textarea',
                             'prompt': 'Write the legal-practice boundaries you and any staff will follow. '
                                       'Identify the titles you will never use, the drafting you will '
                                       'refuse without a supervising lawyer, and the collection conduct '
                                       'rules you train on before the first call.',
                             'example': 'No one on my team uses a lawyer title, a blank title, or '
                                        'new-lawyer marketing, and we decline side drafting with no '
                                        'supervising lawyer [North Texas Paralegal Institute — nFhwr1E6-NE '
                                        '@ 00:02:51]. Texas makes unauthorized practice a class A '
                                        'misdemeanor. Before calls start, staff learn: no abusive or '
                                        'deceptive practices, no middle-of-the-night calls, and no more '
                                        'than seven calls weekly.'},
                            {'name': 'satisfaction_and_contact',
                             'type': 'textarea',
                             'prompt': 'Describe how you will handle debtor contact security and closing '
                                       'out paid files. Explain the order of first contact, how later '
                                       'emails are protected, which satisfaction forms you file on full '
                                       'payment, and how quickly you respond to written demands.',
                             'example': 'First contact is always a mailed hard-copy letter containing a '
                                        'PIN, and every later email is encrypted with that PIN '
                                        '[TheJRInstitute — 3p5TZGrk1og @ 00:01:38]. On full payment I file '
                                        "SC-130, SC-290, or EJ-100 right away, never letting a debtor's "
                                        'written demand sit 14 days, and I use a notarized EJ-100 whenever '
                                        'a lien was recorded.'}],
                 'completion_gate': 'Do not sign a single creditor until your dead-file screen, '
                                    'collectibility rating, and legal-practice boundaries are written '
                                    'down, and until you can name the notary, filing, and court-return '
                                    'steps that must be finished before any collection activity begins.'},
                {'worksheet_id': 'ws-02',
                 'number': 2,
                 'title': 'Enforcement Toolkit and Debtor Examination Plan',
                 'purpose': 'Build the post-judgment machine that turns a court award into money. Confirm '
                            'a reachable asset, record the lien fast, sequence discovery, garnishment, and '
                            'levy with real cost figures, decide what to delegate, and run a debtor '
                            'examination that is investigated, served, scripted, and followed by immediate '
                            'action.',
                 'chapter_ref': 'Q3-Q4',
                 'instructions': ['Write the enforcement stack for the specific jurisdiction where your '
                                  'debtor lives or banks, since deposits, freezes, and reach differ by '
                                  'state and county.',
                                  'Record every cost and deadline as a number so you can compare total '
                                  'enforcement spend against the realistic recovery on each file.',
                                  'Finish the skip trace and asset investigation fields before drafting '
                                  'any examination questions, because the questions come from what the '
                                  'records show.',
                                  'Keep all third-party contact limited to location questions and never '
                                  "describe the debtor's debt to friends, family, or neighbors.",
                                  'Prepare the post-examination levies before the examination date so they '
                                  'can be served the same day the debtor is tipped off.'],
                 'fields': [{'name': 'pre_suit_asset_check',
                             'type': 'textarea',
                             'prompt': 'Before you sue or accept a file, record the insurance or reachable '
                                       'asset that makes the judgment worth enforcing. Explain what you '
                                       'will do if no asset appears and how you avoid post-judgment fees '
                                       'that exceed the recovery.',
                             'example': 'I confirm insurance or a known, reachable asset before suing, '
                                        'because a judgment against a dry hole only adds fees [Attorney '
                                        'Michael Ehline — jPO9_I_LBSw @ 00:00:00]. The governing rule is '
                                        "simple: you don't spend a million dollars to collect half a "
                                        'million. If no asset appears, the file goes into a six-month '
                                        'recheck queue instead of active enforcement.'},
                            {'name': 'lien_recording',
                             'type': 'text',
                             'prompt': 'State when and where you record the judgment after entry, and why '
                                       'speed matters against competing creditors and a possible '
                                       "bankruptcy. Note the lien's limits, including what it cannot force "
                                       'and how long it may sit without paying.',
                             'example': 'I record the judgment immediately so a bankruptcy filing does not '
                                        'leave me unsecured behind faster creditors [The National Law '
                                        'Review — R3nWxu374QE @ 00:47:09]. I also accept the limits: a '
                                        'judgment lien blocks a sale but cannot force a foreclosure, and '
                                        'it may yield nothing for 20 years while needing renewal as '
                                        'interest steadily accrues.'},
                            {'name': 'toolkit_stack',
                             'type': 'textarea',
                             'prompt': 'Lay out your enforcement stack in the order you will use it, from '
                                       'lien to discovery to garnishment or sheriff levy. Include the '
                                       'cost, deposit, or timing number you associate with each tool in '
                                       'the jurisdiction you work.',
                             'example': 'My stack runs lien, sworn post-judgment discovery, then wage '
                                        'garnishment or sheriff levy. In California the writ of execution '
                                        'lives 180 days, issues in three copies, and levy deposits run '
                                        'from $30 to $1,500 or more [Lawyer Tips by The Sterling Firm '
                                        '#lawyer #law — UV-WyQ1-NC4 @ 00:02:17]. In Georgia, garnished '
                                        'bank funds freeze three days before deposit into court.'},
                            {'name': 'wage_cap_math',
                             'type': 'text',
                             'prompt': "Calculate the most you can take from a debtor's paycheck under the "
                                       'federal ceiling and note which debt types sit outside that cap. '
                                       'Show the formula you will use so an employer withholding error is '
                                       'easy to spot.',
                             'example': 'The federal ceiling is the lesser of 25 percent of disposable '
                                        'earnings or earnings above 30 times the federal minimum wage '
                                        '[LawShelf — fQZc8moX-c4 @ 00:01:13]. I compute both figures every '
                                        'pay period and expect the smaller one. Support orders, federal '
                                        'tax debt, and Department of Education loans may fall outside this '
                                        'cap, so I flag those files separately.'},
                            {'name': 'bank_intelligence',
                             'type': 'textarea',
                             'prompt': "List every source you will mine to identify the debtor's bank "
                                       'before serving garnishment. Include what your own client already '
                                       'holds, how you treat uncertain banks, and what you may and may not '
                                       "say when contacting the debtor's friends.",
                             'example': "I start with my client's records: check copies, wire remittances, "
                                        'and bank references on the original credit application [The '
                                        'National Law Review — R3nWxu374QE @ 00:05:05]. I serve likely '
                                        'banks even when unsure an account exists. With mutual friends, '
                                        'especially ones who dislike the debtor, I ask only about '
                                        'location, such as a forwarding address, never calling the debtor '
                                        'a deadbeat.'},
                            {'name': 'delegation_cost',
                             'type': 'textarea',
                             'prompt': 'Decide which enforcement work you keep in-house and which you hand '
                                       'to a receiver, collection agency, or investigator. Record each '
                                       "option's cut or fee and explain why passive phone collection "
                                       'differs from active recovery for your files.',
                             'example': 'A Texas receiver typically takes 25 percent of whatever is '
                                        'collected, so I treat receivership as a last resort [Hendershot '
                                        'Cowart P.C. — -kyDpaMUqFY @ 00:01:44]. Collection agencies are '
                                        'contingency phone-callers, and giving away a third may be '
                                        'permanent. I keep active recovery in-house, and when wages move '
                                        "too slowly I pursue the debtor's business websites, email, and "
                                        'phone numbers.'},
                            {'name': 'pre_exam_skip_trace',
                             'type': 'textarea',
                             'prompt': 'Outline the skip trace and asset investigation you complete before '
                                       'calendaring a debtor examination. Name the record categories you '
                                       'search, how the results support service of the order, and how they '
                                       'arm your cross-examination questions.',
                             'example': 'Before any exam I run a skip trace and asset investigation '
                                        'covering real estate, vehicles, entities in all 50 states, UCC '
                                        'liens, licenses, and court records [People Locator Skip Tracing — '
                                        'nwM1K55PtXM @ 00:00:16]. The address work makes service land, and '
                                        'each hit becomes a question. Trash pulls by a paid investigator '
                                        'have produced more useful information than most techniques.'},
                            {'name': 'exam_filing_service',
                             'type': 'textarea',
                             'prompt': 'Record the filing cost, reach, repeat-exam rules, and service '
                                       'method for the examination or citation in your court. Note any '
                                       'required attachments and whether you will issue a writ of '
                                       'execution at the same time as the order.',
                             'example': 'In Sacramento the examination order costs $60, a writ of '
                                        'execution issues at the same time for free, and the court backlog '
                                        'can run a month or more [Sacramento County Public Law Library — '
                                        'HrhPbWDRBVU @ 00:06:37]. Reach is 150 miles from the courthouse. '
                                        'In Cook County I personally serve the full packet with '
                                        'standing-order Attachments A and E.'},
                            {'name': 'exam_question_script',
                             'type': 'textarea',
                             'prompt': 'Draft the core questions for your examination script. Cover the '
                                       'asset categories and lookback windows you will use, the indirect '
                                       'questions that reveal a bank, and which third parties you will '
                                       'subpoena to apply pressure on the debtor.',
                             'example': 'My script uses two-year lookbacks for accounts, four years for '
                                        'real estate transfers, and 90 days for pre-bankruptcy payments '
                                        '[People Locator Skip Tracing — 6mK0uU9RBO8 @ 00:01:36]. Instead '
                                        'of asking where the debtor banks, I ask what card or account paid '
                                        'the last utility bill. I subpoena the landlord and anyone holding '
                                        '$250 or more for the debtor.'},
                            {'name': 'post_exam_action',
                             'type': 'textarea',
                             'prompt': 'Plan what happens in the hours after the examination and if the '
                                       'debtor fails to appear. Describe the levies you will have ready, '
                                       'the contempt path for a no-show, and how you screen out debtors '
                                       'whose income is protected.',
                             'example': 'The exam tips the debtor off and funds may move to a different '
                                        'bank, so my levies are prepared to fire immediately afterward '
                                        '[Sacramento County Public Law Library — HrhPbWDRBVU @ 00:05:46]. '
                                        'A no-show leads to a contempt warrant, typically with bail set at '
                                        'the debt amount. Debtors proving Social Security or pension '
                                        'income are screened out before calendaring.'}],
                 'completion_gate': 'Do not calendar a debtor examination until the judgment is recorded, '
                                    'the skip trace and asset investigation are complete, the service '
                                    'method and required attachments are confirmed, and the follow-up '
                                    'levies are drafted and ready to serve the same day.'},
                {'worksheet_id': 'ws-03',
                 'number': 3,
                 'title': 'Garnishment, Bank Levy, and Real Property Lien Execution',
                 'purpose': 'Convert located jobs, accounts, and land into collected dollars. Choose '
                            'between ongoing wage garnishment and one-shot bank levies, run the interest '
                            'math against state caps, widen the levy net, anticipate exemption and '
                            'bankruptcy fights, and record abstracts that keep their priority and survive '
                            'revival deadlines.',
                 'chapter_ref': 'Q5-Q6',
                 'instructions': ['Fill in the state-specific numbers for every jurisdiction on your '
                                  'active list, since garnishment caps, response windows, and exemptions '
                                  'vary widely.',
                                  'Run the interest comparison before relying on any garnishment, and mark '
                                  'files where interest outpaces the monthly take for a different '
                                  'strategy.',
                                  'List every bank and account type you intend to levy, including '
                                  'spouse-name and joint accounts, with the supporting paperwork for each.',
                                  'Build a written response for each expected exemption claim and a '
                                  'stop-enforcement checklist for the day a bankruptcy notice arrives.',
                                  'Enter every revival and renewal deadline into a calendar the day the '
                                  'lien is recorded, not when the deadline approaches.'],
                 'fields': [{'name': 'tool_choice',
                             'type': 'textarea',
                             'prompt': 'Explain when you will use wage garnishment versus a bank levy on '
                                       'each file. Describe how each tool runs over time, what you must do '
                                       'to repeat a levy, and which tool you treat as the ongoing '
                                       'workhorse.',
                             'example': 'A bank levy is a one-time thing, not an ongoing collection effort '
                                        'like a wage garnishment [Jedidiah “Jed” McKeehan — 0Kq_0NfOnMo @ '
                                        '00:02:06]. When I know the employer, garnishment is my workhorse, '
                                        'with the employer taking up to 25 percent of wages for as long as '
                                        'the debtor stays employed. Repeating a bank levy requires a fresh '
                                        'writ.'},
                            {'name': 'state_cap_interest',
                             'type': 'textarea',
                             'prompt': 'Record the wage garnishment cap in each state where your debtors '
                                       "work and compare it with the judgment's interest rate. Show "
                                       'whether the monthly garnishment actually reduces the balance or '
                                       'whether interest outruns it and the file never closes.',
                             'example': 'Arizona now allows only 10 percent of net wages, down from 25 '
                                        'percent, while defaulted credit card judgments often carry '
                                        'contract interest around 28 to 30 percent [Consumer Warrior — '
                                        'YmCEqLCbD3s @ 00:04:40]. Before relying on an Arizona garnishment '
                                        'I run the interest math monthly; if the balance grows, I pivot '
                                        'that file toward a bank levy or settlement.'},
                            {'name': 'multi_bank_levy',
                             'type': 'textarea',
                             'prompt': 'Design your multi-bank levy plan. State how many banks you will '
                                       'levy at once, how you choose them, how overage is returned to the '
                                       'debtor, and how many statutory days the garnishee bank has to '
                                       'report held funds.',
                             'example': "I copy Mr. Grey's four-bank levy strategy, hitting four major "
                                        'banks at once instead of gambling on one account, and any overage '
                                        'goes back to the debtor [Mr. Grey Judgment Enforcement — '
                                        'CLxNTh8V1qQ @ 00:00:01]. In California the levied bank gets ten '
                                        'statutory days to determine what it held on the levy date before '
                                        'freezing funds up to the writ amount.'},
                            {'name': 'employer_data',
                             'type': 'text',
                             'prompt': "Identify where you will find the debtor's employer and bank from "
                                       'existing records rather than guesswork. Note which credit report '
                                       'section holds employment data and how old payment trails can point '
                                       'you to the account worth levying.',
                             'example': 'Employment data sits in the personal section of the credit '
                                        'report, so I pull that first for garnishment targeting [Consumer '
                                        'Warrior — YmCEqLCbD3s @ 00:06:03]. For the bank, I review past '
                                        'payments the debtor made by check or auto-debit, since each one '
                                        'names the institution. Those two sources set my garnishment and '
                                        'levy targets before any writ issues.'},
                            {'name': 'joint_spouse_accounts',
                             'type': 'textarea',
                             'prompt': "List the account types beyond the debtor's sole-name accounts that "
                                       'you will include in a levy. Explain the paperwork standard you '
                                       'must meet for spouse-name and joint accounts and the exemption '
                                       'claims you expect those accounts to trigger.',
                             'example': "Accounts in the spouse's name, or held jointly by the debtor and "
                                        'a third party, can be levied when my paperwork is clean [Bobby '
                                        'Benjy — a13Ojjc6ruw @ 00:04:01]. I expect pushback, especially '
                                        "joint accounts holding an adult child's money, so I document "
                                        'ownership facts before levying and prepare a response for each '
                                        'exemption claim that follows the freeze.'},
                            {'name': 'exemption_forecast',
                             'type': 'textarea',
                             'prompt': 'Forecast the exemption fights likely after each freeze. Note '
                                       'protected federal benefits, state bank-account exemptions and how '
                                       'they change for married couples, and how you will decide whether '
                                       'to contest a claim or release the funds.',
                             'example': 'Banks must protect two months of directly deposited federal '
                                        'benefits without the debtor filing anything [Verdict — '
                                        'aWnv0AR52jY @ 00:17:03]. All-Social Security accounts will be '
                                        'released. In Arizona I expect a roughly $5,600 single-account '
                                        'exemption that doubles for married couples, so I only contest '
                                        'when the frozen balance clearly exceeds the protected amount and '
                                        'no benefit deposits appear.'},
                            {'name': 'employer_bankruptcy_watch',
                             'type': 'textarea',
                             'prompt': "Describe how you will monitor the employer's withholding accuracy "
                                       'and respond the moment a bankruptcy notice arrives. Include who '
                                       'you will contact to stop enforcement and how you will track money '
                                       'taken after the filing date.',
                             'example': 'In Georgia an employer that withholds the wrong amount by any '
                                        'small sum can become liable for the entire debt, so I check each '
                                        'remittance [Law Office of Jeffrey B. Kelly — cHsptp1ujiI @ '
                                        '00:02:54]. When a bankruptcy notice lands, I stop enforcement, '
                                        'notify the sheriff and the bank, and return any money taken after '
                                        'the filing date.'},
                            {'name': 'abstract_recording',
                             'type': 'textarea',
                             'prompt': 'Choose the counties where you will record an abstract of judgment '
                                       'and explain why. Note how many certified originals you will order, '
                                       'who records them, and how a recorded abstract treats property the '
                                       'debtor buys later.',
                             'example': 'Following Bob Benjy, I skip the record-everywhere approach and '
                                        'record in major counties such as LA, Orange, and San Francisco '
                                        'plus every county where research shows the debtor owns land '
                                        '[Bobby Benjy — hJmfkC9gu4c @ 00:05:35]. I order one sealed '
                                        'original per county through an attorney service. A recorded '
                                        'abstract waits and attaches when the debtor buys later.'},
                            {'name': 'title_search_equity',
                             'type': 'textarea',
                             'prompt': 'Set the standard for your title search and equity check before '
                                       'counting on a real property lien. State which index entries and '
                                       'owner names you read, and how you confirm the property is worth '
                                       'more than what is owed.',
                             'example': 'My search reads every instrument type under the current owner and '
                                        'every prior owner name, plus any separate judgment index or '
                                        'docket [Hidden Power Files — -HFzhDO6v-A @ 00:04:56]. A deed-only '
                                        'search scans right past a judgment lien. I then confirm equity; '
                                        'with no equity the lien attaches to nothing, and the play becomes '
                                        'waiting for a refinance.'},
                            {'name': 'priority_and_revival',
                             'type': 'textarea',
                             'prompt': 'Build your lien priority and revival calendar. Record the revival '
                                       'deadline measured from entry of judgment, the interest rate '
                                       'accruing, which liens can jump ahead of yours, and the bankruptcy '
                                       'lookback that could get your lien avoided.',
                             'example': 'For Pennsylvania files I calendar revival within five years of '
                                        'entry; a late revival survives but goes to the end of the line '
                                        'behind intervening liens [Five Minute Legal Master Series — '
                                        'V5NrY_biljg @ 00:02:56]. New York judgments accrue nine percent '
                                        'yearly. Tax liens jump above judgment liens, and a lien filed '
                                        'within 90 days before bankruptcy can be avoided.'}],
                 'completion_gate': 'Do not fire any garnishment or levy until the interest math, target '
                                    'banks and accounts, exemption responses, and bankruptcy stop '
                                    'checklist are written, and do not count a real property lien as '
                                    'security until the full-index title search, equity check, and revival '
                                    'deadline are recorded.'},
                {'worksheet_id': 'ws-04',
                 'number': 4,
                 'title': 'Asset Map and Cross-Border Enforcement Planner',
                 'purpose': 'Build a complete asset map from records before the debtor knows enforcement '
                            'is coming, protect the file from pretexting exposure, rank skip data on '
                            'measurable results, and confirm that a judgment from another state or country '
                            'is still live and worth domesticating where the assets actually sit.',
                 'chapter_ref': 'Q7-Q8',
                 'instructions': ['Complete the baseline asset and background investigation before any '
                                  'contact with the debtor, then work through each field in order so later '
                                  'decisions rest on records rather than guesses.',
                                  'Subpoena 24 to 36 months of bank history before any levy, and log every '
                                  'zero or near-zero balance as a possible nightly sweep signal.',
                                  'Obtain written confirmation that nobody on the team, on the vendor '
                                  'list, or on the client side uses bank pretexting of any kind.',
                                  "Pull the originating state's limitation period and renewal history "
                                  'before registering the judgment in any new forum, and flag any lapse.',
                                  'Size the judgment against the full collection cost and record a '
                                  'proceed, sue-direct, or shelve decision before spending money on '
                                  'writs.'],
                 'fields': [{'name': 'debtor_asset_baseline',
                             'type': 'textarea',
                             'prompt': 'List every baseline record pulled on the debtor before any '
                                       'contact: real estate by county, vehicles, entities across all 50 '
                                       'states, UCC liens, licenses, and court records. Note which '
                                       'searches came back empty and which still need a field visit or '
                                       'trash pull.',
                             'example': 'Tim Santoni starts with the basic asset and background '
                                        'investigation to find where the debtor owns property [Tim Santoni '
                                        '— rDAzEvzlcbo @ 00:00:20]. Sample entry: two parcels found in the '
                                        'grantor index, one titled truck, one active LLC, a UCC filing '
                                        'naming a regional lender; trash pull and 4-7 days of surveillance '
                                        'scheduled for the residence.'},
                            {'name': 'bank_subpoena_history',
                             'type': 'textarea',
                             'prompt': 'Record the bank subpoena plan for each suspected account, '
                                       'including the institution, the 24 to 36 month window of credits '
                                       'and debits requested, wire transfer detail, and the date records '
                                       'arrived. Confirm no levy fires until that history is reviewed.',
                             'example': 'Joe Dickerson never garnishes an account until at least 24 to 36 '
                                        'months of credits and debits, including wire transfers, are '
                                        'subpoenaed, because the intelligence outweighs the balance [Hanna '
                                        'Hasl-Kelchner — ha0J206Xt6k @ 00:13:28]. Sample entry: subpoena '
                                        "served on the debtor's checking bank for 36 months; wires to a "
                                        'second institution revealed; levy held pending review.'},
                            {'name': 'sweep_and_zero_balance_check',
                             'type': 'textarea',
                             'prompt': 'Log every levy or garnishment that returned a zero or near-zero '
                                       'balance, with dates. If zeros appear more than once, describe the '
                                       'suspected nightly sweep pattern and name the holding company whose '
                                       'any and all banks will be garnished next.',
                             'example': 'Repeated zero balances revealed a nightly offshore sweep, which '
                                        "was solved by garnishing the holding company's any and all banks "
                                        '[OffshoreAlert — j34w1ZyVNSc @ 00:26:19]. Sample entry: operating '
                                        'account levied twice in three weeks, both returns at zero; '
                                        'incoming deposits seen in subpoenaed statements vanish overnight; '
                                        "writ now directed at the parent holding company's banks."},
                            {'name': 'pretexting_compliance_signoff',
                             'type': 'text',
                             'prompt': 'Name every team member, vendor, client contact, and attorney '
                                       'touching bank information on this file, and record that each '
                                       'confirmed no pretexting. State the exposure level briefed to them '
                                       'and the date of the written acknowledgment each signed before work '
                                       'began.',
                             'example': 'GLBA exposure for bank pretexting runs up to $10K or 10 years and '
                                        'reaches the investigator, vendor, client, and attorney '
                                        '[OffshoreAlert — j34w1ZyVNSc @ 00:23:29]. Sample entry: skip '
                                        'tracer, field investigator, client controller, and enforcement '
                                        'counsel briefed on the $10K and 10-year exposure; signed '
                                        'acknowledgments collected; bank data limited to subpoena returns '
                                        'and client remittance records.'},
                            {'name': 'skip_data_vendor_waterfall',
                             'type': 'textarea',
                             'prompt': 'Rank each skip-trace and trigger-data vendor in waterfall order, '
                                       'with the cost per hit and the portfolio-level contact and '
                                       'collection rates tracked for each. Describe the follow-up process '
                                       'that works every alert before any new data purchase is approved.',
                             'example': 'Chris Ball warns that skip tracing is typically the second '
                                        'largest expense in a collection agency after personnel, and that '
                                        'data dumped into systems often goes unused [Arbeit U — '
                                        'd5DXPK2ggSk @ 00:04:30]. Sample entry: vendor A first, vendor B '
                                        'second for misses; car-loan and mortgage triggers routed to a '
                                        'same-day call queue; vendors cut if contact rates stall.'},
                            {'name': 'federal_docket_research',
                             'type': 'textarea',
                             'prompt': 'Summarize every federal and bankruptcy docket pulled for the '
                                       'debtor through PACER, CourtListener, or Bloomberg: case numbers, '
                                       'open and close dates, creditor lists, and page costs. Note what '
                                       'the case duration says about whether this debtor litigates.',
                             'example': 'Steve Vondran reads open and close dates first: a four-month case '
                                        'is short, while a case that runs over a year shows the party '
                                        'litigates [Steve Vondran — qlw161ht_Kw @ 00:00:49]. Sample entry: '
                                        'one prior bankruptcy petition pulled on PACER at about 10 cents a '
                                        'page, quarterly total under $30; RECAP copy checked first on '
                                        'CourtListener; a 14-month commercial suit flags a fighter.'},
                            {'name': 'trust_and_offshore_structures',
                             'type': 'textarea',
                             'prompt': 'Describe any trust, offshore entity, or asset-protection structure '
                                       'the debtor has raised or that the records reveal. Identify settlor '
                                       'and trustee, whether the trust is revocable, and which bank voice '
                                       'recordings of wire instructions should be subpoenaed.',
                             'example': 'Dickerson treats revocable trusts as having no asset protection '
                                        'because the settlor and trustee are usually the same party '
                                        '[OffshoreAlert — 2ApchMyxmWg @ 00:03:58]. Bank voice recordings '
                                        'of wire instructions are kept 7 years and can win repatriation '
                                        'and contempt orders [OffshoreAlert — j34w1ZyVNSc @ 00:34:21]. '
                                        'Sample entry: revocable family trust, debtor is settlor and '
                                        'trustee; recordings requested.'},
                            {'name': 'originating_judgment_limitation',
                             'type': 'text',
                             'prompt': "Enter the originating state, judgment entry date, that state's "
                                       'limitation period, every renewal filed, and the date registration '
                                       'is planned in the new forum. Flag any gap where the original '
                                       'judgment lapsed before execution was sought.',
                             'example': 'A judgment entered in Arizona in 2003 was registered in Florida '
                                        "in 2006, Arizona's five-year limit lapsed in 2008 without "
                                        'renewal, and execution was sought in 2012 [Florida Trust, Real '
                                        'Estate, Probate, & Foreclosure — 9x7_I2ygY9E @ 00:25:40]. Sample '
                                        'entry: originating state limit five years; renewal filed in year '
                                        'four; registration scheduled before the renewed term expires.'},
                            {'name': 'domestication_and_service_plan',
                             'type': 'textarea',
                             'prompt': 'Map the domestication path: the forum where the debtor or assets '
                                       'sit, certified copy status, filing date, service method, and the '
                                       '30-day response deadline. For overseas defendants, answer the '
                                       'Hague membership, objections and declarations, and language '
                                       'questions first.',
                             'example': 'A sister-state money judgment gets full faith and credit, so the '
                                        'creditor domesticates it by filing in the home state and then '
                                        'serves the debtor [Snellings Law LLC — W1XbSRwt1D8 @ 00:00:30]. '
                                        'Skipping the Hague route gets service quashed and defaults '
                                        'vacated [The Global Process Server — SUlnLzzcvIk @ 00:00:47]. '
                                        "Sample entry: certified copy ordered; filing in debtor's county; "
                                        'response deadline calendared.'},
                            {'name': 'cross_border_economics',
                             'type': 'textarea',
                             'prompt': 'Size the judgment against total collection cost in the enforcing '
                                       'forum: writ service fees, number of banks targeted, local counsel, '
                                       'and expected timeline. State whether the file proceeds, sues '
                                       'directly where assets sit, or is shelved as uneconomic.',
                             'example': 'Haber Law fires writs of garnishment at about 10 banks at once, '
                                        'each costing roughly $50 to $100 to serve [Haber Law — '
                                        'ZdVZvPMh4qM @ 00:19:17], yet warns that $15,000 to $20,000 '
                                        'judgments may not be worth pursuing [Haber Law — ZdVZvPMh4qM @ '
                                        '00:20:36]. Sample entry: $90,000 judgment, ten writs budgeted '
                                        'near $1,000, asset map attached; proceed.'}],
                 'completion_gate': 'Do not register, domesticate, or levy until the asset map is '
                                    'complete, 24 to 36 months of bank history has been reviewed, every '
                                    'zero balance has been checked for a sweep, pretexting acknowledgments '
                                    'are signed, the originating limitation and renewal history is '
                                    'confirmed live, and the economics show the judgment is worth the '
                                    'collection cost.'},
                {'worksheet_id': 'ws-05',
                 'number': 5,
                 'title': 'Bankruptcy Claims and Commercial Collection Control Sheet',
                 'purpose': 'Protect recoveries when a debtor files bankruptcy by meeting every bar date '
                            'and filing only claims worth filing, diligence any claim bought or sold, and '
                            'run commercial collections on a disciplined escalation ladder with clear '
                            'fees, secured-interest checks, and fresh contact data.',
                 'chapter_ref': 'Q9-Q10',
                 'instructions': ['Calendar the proof of claim bar date and every objection response date '
                                  'the day a bankruptcy notice arrives, because late claims are rejected '
                                  'even when the debt is valid.',
                                  'Match every claim to the correct obligor and guarantee, and finish '
                                  'preference, conduct, and anti-assignment diligence before any funds are '
                                  'wired.',
                                  "Size the bankruptcy case and compare the bid with the leading fund's "
                                  'pricing before committing to a claim purchase.',
                                  'Work each commercial account up the escalation ladder in order, putting '
                                  'the litigation threat on the table through mediation or a letter before '
                                  'action before filing suit.',
                                  'Confirm secured status before touching any debtor property, and refresh '
                                  'contact data on at least a quarterly retest cycle.'],
                 'fields': [{'name': 'bar_date_calendar',
                             'type': 'text',
                             'prompt': 'Enter the bankruptcy case number, chapter, petition date, and the '
                                       'proof of claim bar date for this creditor, noting whether the '
                                       'government deadline applies. Add every objection response date so '
                                       'no claim is lost by default.',
                             'example': 'The proof of claim bar date runs about 70 days for non-government '
                                        'creditors and up to 180 days for government, and late claims are '
                                        'rejected even when the debt is valid [Fairmax Law , a Debt Relief '
                                        'Law Firm — 2eXm6HnwE1g @ 00:00:49]. Sample entry: Chapter 11 '
                                        'petition filed; bar date set 70 days out; two objection windows '
                                        'calendared.'},
                            {'name': 'claim_filing_filter',
                             'type': 'textarea',
                             'prompt': 'List every eligible claim against the bankrupt debtor with its '
                                       'face amount and expected recovery. Mark which claims fall below '
                                       'expected recovery and will not be filed, and confirm the remaining '
                                       'proofs of claim were generated and filed.',
                             'example': 'One creditor filed only 3% of its eligible bankruptcy claims and '
                                        'missed more than $2M, which was redistributed to other creditors '
                                        '[G2 Risk Solutions — 1PpzRRYapuA @ 00:14:58]. G2 filters out '
                                        'claims below expected recovery and auto-generates the rest, '
                                        'saving about 80% of the time [G2 Risk Solutions — 1PpzRRYapuA @ '
                                        '00:20:01]. Sample entry: 40 eligible, 6 filtered, 34 filed.'},
                            {'name': 'obligor_and_guarantee_match',
                             'type': 'text',
                             'prompt': 'Identify the exact obligor on the claim being bought or sold, '
                                       'whether a guarantee backs it, and the document proving each point. '
                                       'Confirm the match is verified against the underlying contract '
                                       'before any funds are wired.',
                             'example': 'A client bought the wrong claim, one with a guarantee versus one '
                                        'with none, because the claim was not matched to the right obligor '
                                        'before wiring funds [The National Law Review — lSw0SJbVp-A @ '
                                        '00:40:05]. Read the guarantee carefully and know how it works '
                                        '[The National Law Review — R3nWxu374QE @ 00:31:20]. Sample entry: '
                                        'parent entity guarantee confirmed in contract section reviewed.'},
                            {'name': 'holder_conduct_diligence',
                             'type': 'textarea',
                             'prompt': 'Document diligence on the selling holder: any pre-petition '
                                       'payments that could be clawed back as a section 547 preference, '
                                       'any conduct supporting equitable subordination, and any '
                                       'anti-assignment clause in the contract. State the contractual '
                                       'remedy negotiated for each risk.',
                             'example': 'Equitable subordination drops a claim to the bottom of the chain '
                                        'for bad conduct, and whoever holds the claim is subject to that '
                                        'infirmity [The National Law Review — aQwpKSW3PEA @ 00:03:10]. The '
                                        'Woodbridge ruling held an anti-assignment clause can void the '
                                        'claim [The National Law Review — dGbPfDmUGhk @ 00:33:07]. Sample '
                                        'entry: 85-day pre-petition payment found; refund remedy added.'},
                            {'name': 'claim_pricing_spread',
                             'type': 'textarea',
                             'prompt': "Record the claim's face value, the bid price in cents on the "
                                       'dollar, the expected distribution, and the leading buyers active '
                                       'in the case. Explain the spread target and how the bid compares '
                                       'with the price the leading fund is paying.',
                             'example': 'A classic trade claim is bought at 50 hoping for a 70 recovery '
                                        '[The National Law Review — aQwpKSW3PEA @ 00:01:51]. Joe Sarachek '
                                        'copies Silver Point and beats them by a point, using '
                                        'participation agreements or SPVs to stay anonymous [The National '
                                        'Law Review — dGbPfDmUGhk @ 00:14:34]. Sample entry: $120,000 '
                                        'vendor claim, bid at 51, projected distribution near 70.'},
                            {'name': 'case_solvency_sizing',
                             'type': 'textarea',
                             'prompt': 'Size the bankruptcy case before bidding: number of vendors, '
                                       'secured and administrative layers ahead of unsecured creditors, '
                                       'and any sign of administrative insolvency. Note which 3001E '
                                       'transfer notices show who is selling and at what volume.',
                             'example': 'Watch the 3001E transfer-notice services to see who is selling, '
                                        'then size the case; in Saks, with more than 2,500 vendors, the '
                                        'unsecured claims were worthless [The National Law Review — '
                                        'dGbPfDmUGhk @ 00:36:12]. Sears was administratively insolvent '
                                        '[The National Law Review — dGbPfDmUGhk @ 00:43:42]. Sample entry: '
                                        '1,800 vendors, heavy secured debt, administrative claims growing; '
                                        'pass on bid.'},
                            {'name': 'escalation_ladder',
                             'type': 'textarea',
                             'prompt': 'Chart the commercial escalation ladder for this account: soft '
                                       'collection dates, the letter before action, mediation offer, court '
                                       'claim, and enforcement agent instruction. Record the stall tactics '
                                       'the debtor used at each rung and the response given.',
                             'example': 'Taurus sees a much higher rate of people voluntarily complying '
                                        'with a mediated settlement than with a court order forced on them '
                                        '[Taurus Collections (UK) Ltd — PQz21Mf4OZc @ 00:07:16]. Thomas '
                                        'Higgins instructs the county court bailiff under £600 and the '
                                        'high court enforcement officer above [Thomas Higgins Limited — '
                                        'MxMjZqkhltA @ 00:02:58]. Sample entry: resend request answered '
                                        'same day; mediation offered.'},
                            {'name': 'placement_fee_and_timing',
                             'type': 'text',
                             'prompt': 'State the agency or firm chosen, the contingency rate, any take-on '
                                       'fee, the age of the receivable at placement, and the recovery '
                                       "range expected in the first few months. Confirm the client's terms "
                                       'make collection cost recoverable.',
                             'example': 'US agencies charge 20 to 25 percent on debts over $2,000, with '
                                        'success often above 50 percent [The Business Disputes Register — '
                                        'bgQht-y6jWY @ 00:00:38]. Mike Martinez says a $1 million file '
                                        'yields $170,000 to $350,000 in the first few months [Danny Klein '
                                        '— 3AJVt6F_pYQ @ 00:10:08]. Sample entry: 22 percent contingency, '
                                        'no take-on fee, placed at month five.'},
                            {'name': 'secured_interest_and_levy_path',
                             'type': 'textarea',
                             'prompt': 'Confirm whether the creditor holds a perfected security interest, '
                                       'citing the UCC filing and collateral description. If unsecured, '
                                       'describe the levy and sheriff sale path instead, and note asset '
                                       'leads such as tuition payments uncovered through deposition.',
                             'example': 'An unsecured creditor who takes debtor property commits '
                                        'conversion and must go through levy and sheriff sale [The Tribe — '
                                        "r1sk4alg3RM @ 00:09:38]. Knowing where a debtor's kids attend "
                                        'private school and tracing how that tuition is paid can lead to '
                                        'collection [Evanns Collection Law Firm — XOwPGudMeaY @ 00:01:32]. '
                                        'Sample entry: no UCC filing; tuition paid from business account.'},
                            {'name': 'contact_data_retest_log',
                             'type': 'textarea',
                             'prompt': 'Log the date contact data was last refreshed, the source of each '
                                       'phone and address, and the result of the most recent quarterly '
                                       'retest. Describe any waterfall order change tested retroactively '
                                       'on accounts with known outcomes before production.',
                             'example': 'Will Turner puts consumer contact data at 60 to 70 percent '
                                        'incorrect after two years, so creditor-provided data is never '
                                        'trusted alone [Receivables Info | Debt Collection News — '
                                        '1M9DIxuxJGA @ 00:24:47]. New waterfall orders are tested '
                                        'retroactively first [Receivables Info | Debt Collection News — '
                                        '1M9DIxuxJGA @ 00:21:30]. Sample entry: creditor phone dead; '
                                        'second vendor hit confirmed.'}],
                 'completion_gate': 'Do not wire funds for any claim, file suit on any commercial account, '
                                    'or lay hands on debtor property until the bar date and objection '
                                    'dates are calendared, the obligor and guarantee are matched, holder '
                                    'diligence is complete, the escalation ladder shows mediation or a '
                                    'letter before action, secured status is confirmed, and contact data '
                                    'has passed its quarterly retest.'},
                {'worksheet_id': 'ws-06',
                 'number': 6,
                 'title': 'Compliance Shield and Judgment Lifespan Tracker',
                 'purpose': 'Keep every consumer contact inside the call, text, validation, and dispute '
                            'rules, build an evidence file strong enough to defeat a technical violation '
                            "claim, and track each judgment's lifespan, renewal, and revival deadlines "
                            "while planning for the debtor's likely resistance posture.",
                 'chapter_ref': 'Q11-Q12',
                 'instructions': ['Classify the file before the first contact, and apply the full consumer '
                                  'collection rules whenever the debtor is a natural person and the '
                                  'operation acts as a third-party collector or debt buyer.',
                                  'Count every call attempt against the seven-in-seven ceiling, stay '
                                  'inside the 8:00 a.m. to 9:00 p.m. window, and stop texting the moment a '
                                  'stop reply arrives.',
                                  'Process every dispute and representation letter the day it arrives, and '
                                  'keep a copy of every letter with its certified tracking number.',
                                  "Calendar the judgment's renewal and revival deadlines with lead time, "
                                  'and check any purchased judgment against the state revival window '
                                  'before filing.',
                                  "Record the debtor's resistance posture and a realistic counter-plan, "
                                  'remembering that failure to pay a judgment does not lead to '
                                  'imprisonment.'],
                 'fields': [{'name': 'debt_collector_status',
                             'type': 'text',
                             'prompt': 'State whether this operation acts as a third-party collector or '
                                       'debt buyer on consumer debt, and whether the debtor is a natural '
                                       'person. Record who reviewed that classification and the date the '
                                       'compliance rules were applied to the file.',
                             'example': 'A consumer is a natural person obligated or allegedly obligated '
                                        'to pay any debt [Alabama Consumer Protection Lawyers — '
                                        'qTSer3pu6io @ 00:22:13]. Eviction lawyers count as debt '
                                        'collectors and must give clear and conspicuous written notice of '
                                        'CDC moratorium eligibility [Alabama Consumer Protection Lawyers — '
                                        'z04uhB8lcJU @ 00:04:45]. Sample entry: assigned consumer '
                                        'judgment, debtor is an individual; full compliance rules apply.'},
                            {'name': 'call_attempt_log',
                             'type': 'textarea',
                             'prompt': 'Log every call attempt on this account by date and time, '
                                       'confirming each fell between 8:00 a.m. and 9:00 p.m. Tally '
                                       'attempts in each rolling seven-day period, and note any connection '
                                       'that limits further contact that week.',
                             'example': 'Kaiser Jansen describes the 7-in-7 rule: seven call attempts per '
                                        'seven days per account, with only one contact per seven-day '
                                        'period after a connection [SeniorLiving.Org — 9RtU4rpS3pw @ '
                                        "00:05:51]. A debtor's 'okay' to a callback offer counts as "
                                        'consent to further contact [SeniorLiving.Org — 9RtU4rpS3pw @ '
                                        '00:06:29]. Sample entry: five attempts, one connection Tuesday; '
                                        'dialing paused.'},
                            {'name': 'text_email_optout_log',
                             'type': 'textarea',
                             'prompt': 'Record every text and email sent to the debtor, the opt-out '
                                       'language included in each, and any stop reply received. Confirm '
                                       'contact ended after each stop reply and that screenshots of the '
                                       'full thread are preserved in the file.',
                             'example': "Texts and emails aren't counted toward call limits, but can't "
                                        'harass either, and each must offer a simple opt-out [Night Ferry '
                                        '— 7HVra7o-cZg @ 00:04:04]. Contact continuing after a stop reply '
                                        'is actionable [SeniorLiving.Org — 9RtU4rpS3pw @ 00:08:21]. Sample '
                                        'entry: two texts with opt-out line, stop reply received Friday, '
                                        'texting disabled, thread screenshots saved.'},
                            {'name': 'validation_and_dispute_tracking',
                             'type': 'textarea',
                             'prompt': 'Enter the date the validation notice was sent, confirming it went '
                                       'out within five days of first contact, and the date any written '
                                       'dispute arrived. Describe how all collection activity paused until '
                                       'the dispute was answered in writing.',
                             'example': 'If a written dispute arrives within the window, the collector '
                                        'must stop all collection activity [WealthCurve — cKYmFnf_o2Q @ '
                                        '00:03:01]. Representation letters must be processed the day they '
                                        'arrive; a two-week delay plus one unwanted letter was enough for '
                                        'standing in Sixty v. IQ Data [Saul Ewing LLP — MM_dCPRf9LE @ '
                                        '00:32:32]. Sample entry: notice day three, dispute day 18, calls '
                                        'halted.'},
                            {'name': 'voicemail_and_paid_debt_audit',
                             'type': 'textarea',
                             'prompt': 'Audit every voicemail script and the account history before '
                                       'contact: confirm limited-content messages avoid barred phrases, '
                                       'and confirm the balance was not already paid before a bulk resale. '
                                       'List the itemization and contract-fee checks completed on this '
                                       'file.',
                             'example': "Watts says phrases like 'pre-litigation department' are barred "
                                        'from limited-content voicemails [Alabama Consumer Protection '
                                        'Lawyers — qTSer3pu6io @ 00:39:31]. Loman says collecting paid '
                                        'debt resold in bulk spreadsheet sales is the most common '
                                        'violation seen now [Solo – Resolve Your Debt — n3SZjPQDSHc @ '
                                        '00:13:41]. Sample entry: voicemail script cleaned; payment '
                                        'history requested from original creditor; fees match contract.'},
                            {'name': 'damages_exposure_estimate',
                             'type': 'textarea',
                             'prompt': "Estimate the file's worst-case exposure if a violation were "
                                       'proven: actual damages, statutory damages, attorney fees, and any '
                                       'class exposure. Identify the specific technical violations most '
                                       'likely on this account and the evidence file that would rebut '
                                       'them.',
                             'example': 'Remedies include actual damages plus up to $1,000 additional, '
                                        'with class actions capped at the lesser of $500,000 or 1% of net '
                                        'worth, plus costs and fees [LawShelf — i6PAssklgJg @ 00:05:05]. '
                                        'Two technical violations wiped about $4,000 of debt and generated '
                                        'about $4,500 in fees [Consumer Law 101 by Attorney Aaron Swift — '
                                        'owpVxkqEbEk @ 00:05:22]. Sample entry: texting risk flagged.'},
                            {'name': 'evidence_file_build',
                             'type': 'textarea',
                             'prompt': 'Inventory the evidence file for this account: a copy of every '
                                       'letter sent, each certified mail tracking number, return receipts, '
                                       'call logs, and preserved texts. Note any gap that would weaken a '
                                       'bona fide error defense if a claim were filed.',
                             'example': 'Keep a copy of every letter and its 16-digit certified tracking '
                                        'number, since PRA beat a reporting claim on bona fide error [Meet '
                                        'Jermaine (Clear &Strategic) — XSfDS_s1URg @ 00:06:09]. Never mail '
                                        'a dispute on day 29 of the 30-day window [WealthCurve — '
                                        'cKYmFnf_o2Q @ 00:03:01]. Sample entry: four letters scanned with '
                                        'tracking numbers, two return receipts pending, call log exported '
                                        'weekly.'},
                            {'name': 'judgment_lifespan_renewal',
                             'type': 'text',
                             'prompt': "Enter the judgment entry date, the issuing state's lifespan rule, "
                                       'the renewal or revival deadline, and every renewal already filed. '
                                       'Confirm the next deadline is calendared with enough lead time to '
                                       'file before the window closes.',
                             'example': 'In California a judgment lasts 10 years and can be renewed for '
                                        'another 10, while in Oklahoma a judgment expires in five years '
                                        'and can be renewed every five years indefinitely [The Business '
                                        'Guy | Asset Protection Planners — nbtlIEi4we0 @ 00:02:28]. Sample '
                                        'entry: California judgment entered year one; renewal calendared '
                                        'for year nine; reminder set 90 days earlier.'},
                            {'name': 'revival_window_check',
                             'type': 'textarea',
                             'prompt': 'For any dormant or purchased judgment, compare the original '
                                       'judgment date with the state revival window and record the result '
                                       'before any revival filing or hearing. Note whether the debtor is '
                                       'represented and how notice of the revival was served.',
                             'example': 'One Ohio collector filed a revival two years past a 10-year '
                                        'window [The Credit Repair Shop — --FOsBTlu2E @ 00:04:17]. Some '
                                        'judgments cannot be renewed at all, and a no-show debtor leaves '
                                        'the renewal unchallenged [The Credit Repair Shop — 4Mctc4AuqWA @ '
                                        '00:10:05]. Sample entry: purchased judgment eight years old; '
                                        'inside the revival window; debtor unrepresented; notice '
                                        'personally served.'},
                            {'name': 'debtor_resistance_posture',
                             'type': 'textarea',
                             'prompt': "Describe the debtor's resistance posture: default, answer, "
                                       'arbitration demand, asset shielding, IRS tolling issues, or '
                                       'bankruptcy threat. Record the counter-plan for this file, '
                                       'including arbitration fee economics, trigger-report monitoring, '
                                       'and the realistic limits on compelling payment without assets.',
                             'example': 'A compelled AAA arbitration costs the consumer about $200 versus '
                                        '$2,500 to $5,000 upfront for the creditor, so small suits usually '
                                        'end in dismissal [Consumer Warrior — fWHpyqQu_5M @ 00:07:45]. '
                                        'Failure to pay a judgment is not subject to contempt or '
                                        'imprisonment [The Business Guy | Asset Protection Planners — '
                                        '5mmy9Xz_Oko @ 00:00:58]. Sample entry: arbitration demanded on '
                                        '$3,500 balance; walk-away weighed.'}],
                 'completion_gate': 'Do not place another call, send another message, or file any renewal '
                                    'or revival until the collector classification is recorded, the '
                                    'seven-day call tally and opt-out log are current, every dispute has '
                                    'been answered in writing, the evidence file has no gaps, and the '
                                    "judgment's renewal or revival deadline is confirmed inside its state "
                                    'window.'}]}
