from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'post-judgment-enforcement-fundamentals',
 'question_prompt': 'Once a money judgment is entered, what is the overall post-judgment enforcement '
                    'toolkit and court process a creditor works within?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'Post-Judgment Enforcement Fundamentals',
 'subtitle': "How a judgment is entered and e-filed, judgment duration and renewal, the creditor's "
             'collection toolkit (Texas, California, England and Wales), execution-case asset tracing, '
             'self-help center guidance, and the civil-procedure and case-law research foundations behind '
             'enforcement',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the judgment is only the halfway mark: the court goes '
                      'hands-off, debtors abscond and dissipate assets, and creditors race each other to '
                      'collect first. The working stack is consistent across Georgia, Texas, California '
                      'and Mississippi: record a lien, run post-judgment discovery under oath, then '
                      'garnish wages and bank accounts or send the sheriff to levy. Street numbers include '
                      'a 3-day bank freeze in Georgia, a $30 California wage-levy deposit with employers '
                      'remitting 25% of net wages, a $300-per-8-hours keeper, and the federal cap at the '
                      'lesser of 25% of disposable earnings or earnings above 30 times minimum wage. '
                      'Disagreement centers on cost and delegation: receivers take 25%, collection '
                      'agencies can take a third permanently, and post-judgment fees can exceed what the '
                      'win itself cost.',
 'key_metrics': [{'label': 'Texas Receiver Cut',
                  'metric': 'Texas Receiver Cut',
                  'value': '25% of whatever is collected',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Hendershot Cowart calls a receiver the last resort because receivers '
                             'typically take 25%, while the firm works without that cut.',
                  'source': 'Hendershot Cowart P.C. ([-kyDpaMUqFY @ 00:01:44])'},
                 {'label': 'Federal Wage Garnishment Cap',
                  'metric': 'Federal Wage Garnishment Cap',
                  'value': 'Lesser of 25% of disposable earnings or earnings above 30x the federal minimum '
                           'wage',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'CCPA Title III ceiling; may not apply to support orders, federal tax debt, '
                             'or Department of Education loans.',
                  'source': 'LawShelf ([fQZc8moX-c4 @ 00:01:13])'},
                 {'label': 'Georgia Bank Garnishment Freeze',
                  'metric': 'Georgia Bank Garnishment Freeze',
                  'value': '3 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Garnished bank funds are frozen for 3 days, then deposited into court for '
                             'the creditor to collect.',
                  'source': 'Downs Law ([K1KakWduA04 @ 00:01:17])'},
                 {'label': 'California Writ of Execution Life',
                  'metric': 'California Writ of Execution Life',
                  'value': '180 days; issued in 3 copies; deposits from $30 to $1,500 or more',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Writ issued under CCP 681-688; levy deposits scale from bank and wage levies '
                             'up to business and sale notices.',
                  'source': 'Lawyer Tips by The Sterling Firm #lawyer #law ([UV-WyQ1-NC4 @ 00:02:17])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['Every practitioner who addressed the question frames the judgment as a '
                              "starting line, not a finish. Calhoun School of Law puts winning at 'about "
                              "halfway' and notes the court goes 'hands-off' once the ruling issues "
                              '[ObrPaCTQ6ZQ @ 00:00:00]. Eric Nano of the Sacramento County Public Law '
                              "Library tells creditors that getting the judgment was 'possibly the easy "
                              "part,' using the Better Off Dead paperboy who is owed $2 and never collects "
                              'as the warning [bX8Hhszjuxs @ 00:00:45]. The consensus fix is to think '
                              'about collection before filing. Timothy Anenberger on The National Law '
                              'Review panel says to ask whether the defendant is judgment-proof, map '
                              'assets, and use provisional remedies such as attachment up front, because '
                              "debtors abscond, transfer, and dissipate assets 'all the time' [R3nWxu374QE "
                              '@ 00:02:25]. Attorney Michael Ehline is blunter: do not sue without '
                              'insurance or a known asset, and remember a settlement is not a judgment '
                              '[jPO9_I_LBSw @ 00:00:00]. Jeffrey Leon closes the same loop from the panel, '
                              "pulling Dun & Bradstreet reports so the client avoids suing a 'dry hole.' "
                              'The operator baseline is therefore an asset thesis before a complaint, with '
                              'insurance, bank relationships, and real property identified before the '
                              'debtor has a chance to move them.',
                              'The core toolkit repeats almost word for word across jurisdictions. Will of '
                              'Downs Law lists three primary Georgia methods: record a fifa with the '
                              'superior court as a lien on real or personal property, garnish wages or '
                              'bank funds, and run post-judgment discovery for documents and a sworn asset '
                              'statement [K1KakWduA04 @ 00:00:23]. Calhoun School of Law names the same '
                              'three instruments, liens, writs of execution and writs of garnishment, and '
                              'adds that writs must be localized where the property sits, Chicago versus '
                              'Dallas [ObrPaCTQ6ZQ @ 00:02:02]. Hendershot Cowart puts post-judgment '
                              'discovery first in Texas to locate non-exempt assets, then layers writs of '
                              'execution, garnishment, turnover orders and, last, a receiver [-kyDpaMUqFY '
                              '@ 00:00:03]. The Sterling Firm opens with a written demand, then picks '
                              'among a debtor appearance order, a writ of execution, and an abstract of '
                              'judgment that creates a lien [UV-WyQ1-NC4 @ 00:01:01]. Across all four, the '
                              'lien is the passive anchor and garnishment is the active cash tool. Will is '
                              "explicit that a lien 'doesn't necessarily get you paid right then,' but "
                              'forces payoff when the debtor sells or refinances, which is why operators '
                              'record it immediately and run garnishment and discovery in parallel rather '
                              'than waiting on a sale.',
                              'Speed is the third point of agreement, bounded by the appeal clock. The '
                              'Private Investigator Videos operator says to wait out the 30 to 60 day '
                              'appeal window before seizing anything, but to start the asset search '
                              'immediately [q-khGCaOPck @ 00:00:56]. Calhoun School of Law gives the same '
                              'sequence: let the appellate timeframe run out, then start the next day '
                              '[ObrPaCTQ6ZQ @ 00:01:16]. Scott Bernstein explains why the next day '
                              'matters: debtors stretch payables across two or three vendors suing at '
                              "once, and 'it's a race once you have the judgment to see who can collect "
                              "first,' so nobody should sit on the paper [R3nWxu374QE @ 00:07:07]. Timothy "
                              'Anenberger adds the bankruptcy penalty for slowness: an unrecorded judgment '
                              'leaves the creditor unsecured when the debtor files [R3nWxu374QE @ '
                              '00:45:03]. The window is long but not unlimited. The Sterling Firm treats a '
                              'judgment as valid for 10 years and renewable, Calhoun says at least 10 '
                              'years extendable by 10 more with interest accruing, the investigator cites '
                              'limitation periods of 5, 10 or 20 years, and SQE1window gives 6 years. The '
                              'shared rule is to record fast, search during the appeal window, and '
                              'calendar renewal before the clock expires.'],
               'table': {'caption': 'Where the practitioners line up on enforcement fundamentals',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['The judgment marks only the halfway point',
                                   'Winning is about halfway and the court goes hands-off after ruling',
                                   'Budget a separate enforcement campaign before celebrating the verdict',
                                   'Calhoun School of Law ([ObrPaCTQ6ZQ @ 00:00:00])'],
                                  ['Plan collection before the complaint is filed',
                                   'Ask whether the defendant is judgment-proof, map assets, and use '
                                   'attachment early',
                                   'Build the asset map during pleadings instead of after the verdict',
                                   'The National Law Review ([R3nWxu374QE @ 00:02:25])'],
                                  ['No reachable asset means no lawsuit worth filing',
                                   'Do not sue without insurance or a known asset; settlement is not '
                                   'judgment',
                                   'Confirm a policy or reachable asset before spending any fees',
                                   'Attorney Michael Ehline ([jPO9_I_LBSw @ 00:00:00])'],
                                  ['Three primary collection methods run side by side',
                                   'Record a fifa lien, garnish wages or bank funds, run post-judgment '
                                   'discovery',
                                   'Open lien, garnishment and discovery tracks together from day one',
                                   'Downs Law ([K1KakWduA04 @ 00:00:23])'],
                                  ['Post-judgment discovery comes before the writs',
                                   'Discovery locates non-exempt assets before execution, garnishment or '
                                   'turnover issue',
                                   'Aim writs only after discovery shows where non-exempt assets sit',
                                   'Hendershot Cowart P.C. ([-kyDpaMUqFY @ 00:00:03])'],
                                  ['Enforcement starts the day after appeals expire',
                                   'Wait out the appellate timeframe, then begin enforcement the very next '
                                   'day',
                                   'Calendar the appeal deadline and queue writs for the following morning',
                                   'Calhoun School of Law ([ObrPaCTQ6ZQ @ 00:01:16])'],
                                  ['Judgments lapse unless the creditor renews them',
                                   'A judgment stays valid for 10 years and can be renewed',
                                   'Diary renewal well ahead of the ten-year expiry date',
                                   'Lawyer Tips by The Sterling Firm #lawyer #law ([UV-WyQ1-NC4 @ '
                                   '00:00:01])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Enforcement starts with finding the debtor and then the money. Eric Nano '
                              'works outward from what the case already produced: where the debtor lived '
                              'during the suit, the service address on a default, and contact details from '
                              'trial or settlement. Under the FDCPA, the creditor can ask friends and '
                              'family only for location, such as a forwarding address, and must leave them '
                              'alone once the debtor is found; mutual friends who no longer like the '
                              'debtor are flagged as prime sources, alongside Google, White Pages and '
                              'public social media, with professionals holding subscription databases too '
                              'expensive for individuals [bX8Hhszjuxs @ 00:04:02]. The Private '
                              'Investigator Videos operator then locks the debtor into a financial '
                              'disclosure or examination under penalty of perjury and runs an independent '
                              'asset search to compare the two [q-khGCaOPck @ 00:02:10]. Steven Rinold '
                              'hands operators a ready-made question list: the federal bankruptcy '
                              'schedules of assets and liabilities, used as a post-judgment discovery '
                              'checklist [R3nWxu374QE @ 00:11:32]. Will of Downs Law specifies the '
                              'document haul: tax returns, bank account information and other assets '
                              '[K1KakWduA04 @ 00:01:34]. Any gap between the sworn statement and the '
                              'search becomes the leverage point, since no-shows and liars can be ordered '
                              'to pay fees and produce tax returns.',
                              'The cash tools carry hard numbers. The Sterling Firm prices a California '
                              'wage levy at a $30 deposit, with the employer remitting 25% of net wages '
                              'starting 10 days after service for up to 10 years; a bank levy is another '
                              '$30 deposit with the bank remitting within 10 days, and collected funds are '
                              'held 21 days [UV-WyQ1-NC4 @ 00:04:15]. Hendershot Cowart separates the '
                              'Texas writ of garnishment, which targets a known bank and exempts only '
                              'current wages the debtor can prove the balance equals, from the broader '
                              'turnover order, which can be served on any bank that then searches for the '
                              "debtor's accounts itself [-kyDpaMUqFY @ 00:01:03]. Timothy Anenberger's "
                              'Mississippi practice treats a bank garnishment as a lien from service plus '
                              '30 days and serves banks even when nobody is sure an account exists '
                              '[R3nWxu374QE @ 00:14:54]. LawShelf supplies the federal ceiling: CCPA Title '
                              'III caps wage garnishment at the lesser of 25% of disposable earnings or '
                              'earnings above 30 times the federal minimum wage, with support orders, '
                              'federal tax debt and Department of Education loans potentially outside the '
                              'cap [fQZc8moX-c4 @ 00:01:13]. Business targets cost more under the Sterling '
                              'schedule: an $85 till tap, a $300 keeper per 8 hours, and roughly $1,000 '
                              'for a real estate levy.',
                              'When the obvious accounts run dry, practitioners turn to pressure. Jeffrey '
                              "Leon's playbook is to become a nuisance: depositions, subpoenas, account "
                              'freezes that leave only a living-expense allowance, and credit-report hits, '
                              'noting that recorded liens can trip mortgage defaults [R3nWxu374QE @ '
                              '00:19:30]. Scott Bernstein lays out the escalation ladder against a '
                              'stonewalling debtor: an order to compel, then contempt with daily fines, '
                              'then a civil arrest warrant [R3nWxu374QE @ 00:34:17]. The Private '
                              'Investigator Videos operator calls wages slow and goes after leverage '
                              'instead, seizing business websites, email and phone numbers, and points to '
                              'storage units, ATVs and boats as overlooked targets [q-khGCaOPck @ '
                              '00:07:25]. On the panel, Anenberger skips defunct LLCs entirely and pursues '
                              'personal guarantors, using a judgment debtor exam to bring them to the '
                              "table, while charging orders reach a debtor's financial interest in an LLC "
                              'or LP but not management rights. Hendershot Cowart keeps the receiver as '
                              'the last resort because receivers typically take 25% of whatever is '
                              'collected [-kyDpaMUqFY @ 00:01:30]. The stated end state, from Bernstein, '
                              'is a forbearance agreement with a payment schedule, reached through '
                              'persistence rather than a single knockout writ.'],
               'table': {'caption': 'Collection tools with the exact numbers practitioners quote',
                         'headers': ['Tool or Move', 'Exact Mechanic', 'Numbers and Cost', 'Expert Source'],
                         'rows': [['Georgia bank garnishment on a known bank',
                                   'Garnish bank funds where the bank is known; funds go into court',
                                   'Funds frozen for 3 days, then deposited into court for collection',
                                   'Downs Law ([K1KakWduA04 @ 00:01:17])'],
                                  ['California wage levy served on the employer',
                                   'Employer withholds and remits a share of net wages after service',
                                   '$30 deposit; 25% of net wages; starts 10 days after service; up to 10 '
                                   'years',
                                   'Lawyer Tips by The Sterling Firm #lawyer #law ([UV-WyQ1-NC4 @ '
                                   '00:04:15])'],
                                  ['California writ of execution under CCP 681-688',
                                   'Writ issued in three copies to support levies by the levying officer',
                                   'Valid 180 days; deposits run from $30 to $1,500 or more',
                                   'Lawyer Tips by The Sterling Firm #lawyer #law ([UV-WyQ1-NC4 @ '
                                   '00:02:17])'],
                                  ['Business till tap and keeper levy',
                                   'Levying officer taps the register or installs a keeper at the business',
                                   'Till tap $85; keeper $300 per 8 hours; sale notice $1,500, 10 days '
                                   'ahead',
                                   'Lawyer Tips by The Sterling Firm #lawyer #law ([UV-WyQ1-NC4 @ '
                                   '00:06:05])'],
                                  ['Texas turnover order served on any bank',
                                   "Order served on any bank, which then searches for the debtor's "
                                   'accounts',
                                   'Broader than garnishment, which requires the creditor to know the bank',
                                   'Hendershot Cowart P.C. ([-kyDpaMUqFY @ 00:01:03])'],
                                  ['Federal wage garnishment ceiling under CCPA Title III',
                                   'Caps how much of a paycheck any wage garnishment can reach',
                                   'Lesser of 25% of disposable earnings or earnings above 30 times '
                                   'minimum wage',
                                   'LawShelf ([fQZc8moX-c4 @ 00:01:13])'],
                                  ['New York individual bank account exemption',
                                   "First slice of an individual debtor's bank balance is protected from "
                                   'levy',
                                   'First $3,000 in the account is protected; notice of exemptions before '
                                   'levy',
                                   'The National Law Review ([R3nWxu374QE @ 00:18:10])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Leverage Moves the Practitioners Actually Use',
                           'body': 'Small moves from the panel, the investigator, and the self-help '
                                   'attorney that widen the net before and after judgment.',
                           'items': ["Mine your own client for the debtor's bank: check copies, wire "
                                     'remittances, and the bank references on the original credit '
                                     'application [The National Law Review — R3nWxu374QE @ 00:05:05].',
                                     'Serve banks with garnishment even when you are not sure an account '
                                     'exists there [The National Law Review — R3nWxu374QE @ 00:15:27].',
                                     "Work mutual friends, especially ones that don't like the debtor "
                                     'anymore, but ask only for location under the FDCPA [Sacramento '
                                     'County Public Law Library — bX8Hhszjuxs @ 00:04:28].',
                                     "When wages move too slowly, seize the debtor's business websites, "
                                     'email, and phone numbers as leverage [Private Investigator Videos — '
                                     'q-khGCaOPck @ 00:07:25].']},
               'sop_steps': [{'step': 1,
                              'title': 'Map Assets Before Filing',
                              'action': "Pull a Dun & Bradstreet report and mine the client's records for "
                                        "the debtor's bank details.",
                              'detail': "Jeffrey Leon uses Dun & Bradstreet to avoid suing a 'dry hole' "
                                        '[The National Law Review — R3nWxu374QE @ 01:00:03]; Scott '
                                        'Bernstein pulls check copies, wire remittances and '
                                        'credit-application bank references from the client [The National '
                                        'Law Review — R3nWxu374QE @ 00:05:05].'},
                             {'step': 2,
                              'title': 'Enter and Record the Judgment',
                              'action': 'File the judgment with amount, basis and post-judgment interest '
                                        'rate, then record the lien immediately.',
                              'detail': "Nashville's e-file form captures amount, basis (default, "
                                        'agreement or trial) and post-judgment interest rate [Circuit '
                                        'Court Clerk of Nashville, Davidson County — FSUH2GyMLJ8 @ '
                                        '00:01:03]; record a fifa with the superior court as a lien [Downs '
                                        'Law — K1KakWduA04 @ 00:00:23] or an abstract of judgment [Lawyer '
                                        'Tips by The Sterling Firm #lawyer #law — UV-WyQ1-NC4 @ '
                                        '00:08:34].'},
                             {'step': 3,
                              'title': 'Put the Debtor Under Oath',
                              'action': 'Obtain a financial disclosure or debtor examination under perjury '
                                        'and compare it to an independent asset search.',
                              'detail': 'Lock the sworn disclosure, then run the asset search to compare '
                                        '[Private Investigator Videos — q-khGCaOPck @ 00:02:10]; no-shows '
                                        'or liars can be ordered to pay fees and produce tax returns '
                                        '[Private Investigator Videos — q-khGCaOPck @ 00:06:26].'},
                             {'step': 4,
                              'title': 'Hit Income and Accounts, Then Escalate',
                              'action': 'Levy wages and banks, widen with a turnover order, and climb to '
                                        'contempt if the debtor stonewalls.',
                              'detail': 'Bank levy costs a $30 deposit with remittance within 10 days '
                                        '[Lawyer Tips by The Sterling Firm #lawyer #law — UV-WyQ1-NC4 @ '
                                        '00:05:09]; a turnover order reaches any bank [Hendershot Cowart '
                                        'P.C. — -kyDpaMUqFY @ 00:01:03]; escalate through order to compel, '
                                        'contempt with daily fines, and a civil arrest warrant [The '
                                        'National Law Review — R3nWxu374QE @ 00:34:17].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The lien camp splits on whether a recorded judgment is a weapon or a '
                              'waiting room. Will at Downs Law treats the Georgia fifa recorded with the '
                              'superior court as one of three core methods, but concedes up front that it '
                              "'doesn't necessarily get you paid right then'. The payoff only lands when "
                              'the debtor tries to sell or refinance the house, lot, or investment '
                              'property [K1KakWduA04 @ 00:00:43]. LawShelf pushes that warning further: a '
                              'judgment lien blocks a sale yet cannot force a foreclosure, it may sit for '
                              '20 years without producing a dollar, it has to be renewed, and interest '
                              'keeps accruing the whole time [fQZc8moX-c4 @ 00:03:01]. The National Law '
                              'Review panel runs the lien as an active pressure lever instead of a parking '
                              'spot. Jeff Leon stacks liens with depositions, subpoenas, freezes, and '
                              'credit-report hits to become a nuisance, noting that a lien can trip a '
                              "default on the debtor's mortgage [R3nWxu374QE @ 00:19:30]. Tim Anenberger "
                              'adds a priority angle the passive camp never touches: when property is held '
                              'as tenancy by the entirety, record in chancery court immediately, because '
                              "it is 'first in time, first in right' [R3nWxu374QE @ 00:16:35]. The "
                              'operator read: record fast for priority, but never count the lien as cash.',
                              'Wage garnishment draws the sharpest split between the first-strike camp and '
                              'the skeptics. Tim Anenberger calls it the first tool in Mississippi. It '
                              'creates a lien on the income stream, and when the debtor changes jobs you '
                              'simply re-issue it, though North Carolina bars it outright except for child '
                              'support and taxes [R3nWxu374QE @ 00:12:48]. The Sterling Firm lays out its '
                              'version as a low-cost grind: a $30 deposit, after which the employer remits '
                              '25% of net wages starting 10 days after service, for up to 10 years '
                              '[UV-WyQ1-NC4 @ 00:04:15]. LawShelf undercuts the strategy for a big slice '
                              'of debtors. The CCPA Title III cap limits the take to the lesser of 25% of '
                              'disposable earnings or earnings above 30 times the federal minimum wage, '
                              'and garnishment simply fails on low income or unemployment [fQZc8moX-c4 @ '
                              '00:02:41]. Private Investigator Videos goes further and calls wages slow, '
                              "pushing operators toward leverage plays instead: seize the debtor's "
                              'business websites, email, and phone numbers so the business itself feels '
                              'the squeeze [q-khGCaOPck @ 00:07:25]. The playbook choice comes down to the '
                              'debtor profile. Steady salaried earners get the wage order. Self-employed '
                              'operators with digital storefronts get hit where the revenue actually '
                              'flows.',
                              'The practitioners also disagree on who should do the collecting and how '
                              "hard to chase. Hendershot Cowart P.C. ranks a Texas receiver as the 'last "
                              "resort' because receivers 'typically take 25% of whatever is collected,' "
                              'and the firm pitches its own work as running without that cut [-kyDpaMUqFY '
                              '@ 00:01:44]. Attorney Michael Ehline lists collection agencies as a normal '
                              'California step alongside wage garnishment, liens, and renewing the '
                              'judgment, treating the agency as just another tool in the kit [jPO9_I_LBSw '
                              '@ 00:00:28]. Private Investigator Videos rejects that framing hard. '
                              "Agencies are contingency phone-callers, giving away 'a third' may be "
                              "permanent, and passive 'collection' is a different business from active "
                              "'recovery' [q-khGCaOPck @ 00:11:17]. On how far to push, Jeff Leon argues "
                              'for compromise priced on the time value of money and risk, warning that '
                              "clients who chase a judgment 'to the end of the earth' end up running 'two "
                              "litigations in one' [R3nWxu374QE @ 00:23:38]. The split is about the cost "
                              'of handing off the file. Outsource and surrender a quarter or a third of '
                              'every recovered dollar, or keep the work in-house, apply relentless '
                              'pressure, and settle the moment the math turns against you.'],
               'table': {'caption': 'Competing enforcement playbooks reported by the practitioners',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['When to launch the first enforcement strike',
                                   'Wait until the appellate timeframe is exhausted, then start the very '
                                   'next day',
                                   'Treat it as a race because debtors stretch payables across two or '
                                   'three suing vendors',
                                   'Calhoun School of Law ([ObrPaCTQ6ZQ @ 00:01:16]); The National Law '
                                   'Review ([R3nWxu374QE @ 00:07:07])'],
                                  ["How to hit the debtor's bank money",
                                   'Garnish a known bank; funds freeze three days, then get deposited into '
                                   'court',
                                   'Texas turnover order served on any bank, which then searches for the '
                                   "debtor's accounts",
                                   'Downs Law ([K1KakWduA04 @ 00:01:17]); Hendershot Cowart P.C. '
                                   '([-kyDpaMUqFY @ 00:01:03])'],
                                  ['Banks where an account is only suspected',
                                   'Banks pay only on a writ of garnishment aimed at the debtor',
                                   'Serve banks even when unsure an account exists; lien runs service plus '
                                   '30 days',
                                   'Private Investigator Videos ([q-khGCaOPck @ 00:03:50]); The National '
                                   'Law Review ([R3nWxu374QE @ 00:14:54])'],
                                  ['Value of a recorded judgment lien',
                                   'Passive: blocks sale, cannot force foreclosure, may yield nothing for '
                                   '20 years',
                                   'Active: liens trigger mortgage defaults and stack with subpoenas and '
                                   'credit-report hits',
                                   'LawShelf ([fQZc8moX-c4 @ 00:03:01]); The National Law Review '
                                   '([R3nWxu374QE @ 00:19:30])'],
                                  ['Using jail and contempt as leverage',
                                   'Contempt and jail apply only to defying orders like debtor exams, '
                                   'never the debt itself',
                                   'Escalate from an order to compel, to contempt with daily fines, to a '
                                   'civil arrest warrant',
                                   'LawShelf ([fQZc8moX-c4 @ 00:05:16]); The National Law Review '
                                   '([R3nWxu374QE @ 00:34:17])'],
                                  ['Where to enforce a federal judgment',
                                   'Transfer to state court and use county sheriff civil units over '
                                   'slower, costlier US Marshals',
                                   'Register the final federal judgment in another district by filing a '
                                   'form',
                                   'The National Law Review ([R3nWxu374QE @ 00:31:39]); The National Law '
                                   'Review ([R3nWxu374QE @ 00:44:14])'],
                                  ['Pursuing entity debtors versus their individual backers',
                                   'Charging orders reach LLC or LP financial interests, not the '
                                   'management rights',
                                   'Skip the defunct LLC and drag the personal guarantors into a judgment '
                                   'debtor exam',
                                   'The National Law Review ([R3nWxu374QE @ 00:14:18]); The National Law '
                                   'Review ([R3nWxu374QE @ 00:28:39])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failure starts before the complaint is filed. Attorney '
                              "Michael Ehline's opening rule is blunt: don't sue without insurance or a "
                              'known asset, and remember that a settlement is not a judgment [jPO9_I_LBSw '
                              '@ 00:00:00]. Eric Nano of the Sacramento County Public Law Library warns '
                              'that debtors living off the grid are hard to find, and the ones who truly '
                              'live that way likely have nothing worth collecting anyway [bX8Hhszjuxs @ '
                              '00:06:17]. Jeff Leon frames the cost side just as bluntly: weigh the cost '
                              'of collection, especially on a contingency file, because post-judgment fees '
                              'can exceed what was spent winning the judgment in the first place '
                              '[R3nWxu374QE @ 00:08:27]. The panel boils the whole calculation down to a '
                              "single line: 'you don't spend a million dollars to collect half a million "
                              "dollars' [R3nWxu374QE @ 00:22:53]. That means every enforcement step needs "
                              'a projected return attached before it is filed, not after the invoices '
                              'land. The economics check is simple and unforgiving. Before spending a '
                              'dollar on enforcement, know exactly what asset you are chasing, what it '
                              'will cost to reach it, how long it will take to convert into cash, and at '
                              'what point the file stops being worth another hour of billable work.',
                              'The second trap is assuming the debtor will sit still. Tim Anenberger says '
                              "debtors abscond, transfer, and dissipate assets 'all the time,' which is "
                              'why execution planning, asset mapping, and provisional remedies like '
                              'attachment belong at the start of the case, before the complaint is even '
                              'filed, not after the verdict [R3nWxu374QE @ 00:02:25]. Once the judgment '
                              'lands, Tim reports debtors stonewalling and dodging the sheriff for months, '
                              'and warns that if the debtor files bankruptcy while your judgment sits '
                              'unrecorded, you are just another unsecured creditor [R3nWxu374QE @ '
                              '00:45:03]. Private Investigator Videos flags the classic dump: a $100K car '
                              'sold for $5K is a below-value transfer that counts as fraudulent '
                              'conveyance, and storage units, ATVs, and boats are the targets worth '
                              'hunting [q-khGCaOPck @ 00:04:52]. Attorney Michael Ehline points to debtors '
                              "who 'escape' to Florida, citing the OJ and Goldman wrongful death case "
                              '[jPO9_I_LBSw @ 00:00:44]. Each of these moves forces the creditor to spend '
                              'more just to get back to where they started. The operator lesson is speed '
                              'and paper. Record immediately, freeze what you can, and document every '
                              'suspicious transfer before the trail goes cold.',
                              'The third failure mode is the creditor becoming the defendant. Eric Nano '
                              'warns that under the FDCPA you cannot tell friends or family the debtor is '
                              'a deadbeat. You may only ask about location, such as whether a forwarding '
                              'address was left, and once the debtor is found you leave everyone else '
                              'alone [bX8Hhszjuxs @ 00:04:02]. Steven Rinold adds that wrongly liening '
                              "someone's property can be 'slander of title,' turning an aggressive lien "
                              'into a liability [R3nWxu374QE @ 00:55:04]. The Sterling Firm flags the '
                              'back-end trap that catches creditors who finally get paid: file the '
                              'satisfaction of judgment within 15 days or face liability yourself '
                              '[UV-WyQ1-NC4 @ 00:01:24]. On the flip side, Private Investigator Videos '
                              'tells creditors to watch the docket for unauthorized satisfaction filings '
                              'against their own judgment [q-khGCaOPck @ 00:10:34]. Aggression only pays '
                              'when the paperwork is clean. Every levy, lien, garnishment, and third-party '
                              "contact needs to survive a challenge from the debtor's side, because one "
                              'sloppy step flips the leverage and turns the collection file into a defense '
                              'file. Track deadlines on both ends of the case: the clock that starts when '
                              'you collect, and the filings someone else might slip in while you are not '
                              'looking.'],
               'table': {'caption': 'Firsthand traps and the counter-moves practitioners report',
                         'headers': ['Trap', 'What Goes Wrong', 'Counter-Move', 'Expert Source'],
                         'rows': [['Suing a dry-hole defendant with no reachable assets',
                                   'Fees pile up against a judgment-proof debtor with nothing to seize',
                                   'Pull Dun & Bradstreet reports before filing to avoid suing a dry hole',
                                   'The National Law Review ([R3nWxu374QE @ 01:00:03])'],
                                  ['Handing the file to a Texas receiver too early',
                                   'The receiver typically takes 25% of whatever is collected from the '
                                   'debtor',
                                   'Run discovery, execution, garnishment, and turnover orders before '
                                   'appointing a receiver',
                                   'Hendershot Cowart P.C. ([-kyDpaMUqFY @ 00:01:30])'],
                                  ['Signing a contingency deal with a collection agency',
                                   'Agencies mostly make phone calls while keeping a third, possibly '
                                   'permanently',
                                   'Run active recovery with asset searches, sworn disclosures, and '
                                   'targeted seizures',
                                   'Private Investigator Videos ([q-khGCaOPck @ 00:11:17])'],
                                  ['Letting the judgment lapse past its enforcement window',
                                   'Limitation periods run 5, 10, or 20 years depending on the '
                                   'jurisdiction',
                                   'Calendar renewal dates early because judgments can be renewed before '
                                   'they expire',
                                   'Private Investigator Videos ([q-khGCaOPck @ 00:08:23]); Lawyer Tips by '
                                   'The Sterling Firm #lawyer #law ([UV-WyQ1-NC4 @ 00:00:01])'],
                                  ['Leaving the judgment unrecorded when bankruptcy hits',
                                   'An unrecorded judgment leaves the creditor sitting unsecured in the '
                                   'bankruptcy',
                                   'Record immediately, appear, use the 341 meeting, file proofs of claim, '
                                   'seek stay relief',
                                   'The National Law Review ([R3nWxu374QE @ 00:47:09]; [R3nWxu374QE @ '
                                   '00:49:17])'],
                                  ['Chasing out-of-state assets with the home-state lawyer',
                                   'An Illinois judgment against Florida assets requires hiring a Florida '
                                   'lawyer',
                                   'Budget local counsel and check homestead protection, since the uniform '
                                   'act is not uniform',
                                   'The National Law Review ([R3nWxu374QE @ 00:21:52]; [R3nWxu374QE @ '
                                   '00:36:58])'],
                                  ["Levying without honoring the debtor's exemptions",
                                   'Improper execution exposes the creditor to lawsuits and court '
                                   'sanctions',
                                   'Give individuals exemption notice; New York protects the first $3,000 '
                                   'in accounts',
                                   'The National Law Review ([R3nWxu374QE @ 00:53:02]; [R3nWxu374QE @ '
                                   '00:18:10])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Gates Before Spending on Enforcement',
                           'body': 'Every gate below comes from a trap a practitioner reported. Clear them '
                                   'before the first levy, lien, or garnishment goes out, and again before '
                                   'any payment is booked as closed.',
                           'items': ['Confirm insurance or a known, reachable asset exists before suing, '
                                     'because a judgment against a dry hole only adds fees [Attorney '
                                     'Michael Ehline — jPO9_I_LBSw @ 00:00:00].',
                                     'Record the judgment immediately so a bankruptcy filing does not '
                                     'leave you unsecured behind faster creditors [The National Law Review '
                                     '— R3nWxu374QE @ 00:47:09].',
                                     'Serve the required notice before enforcement: debtors must receive '
                                     'at least seven clear days notice unless the court permits otherwise '
                                     '[SQE1window — Khe45F-Cnr4 @ 00:07:15].',
                                     'Once paid, file the satisfaction of judgment within 15 days or face '
                                     'liability as the creditor [Lawyer Tips by The Sterling Firm #lawyer '
                                     '#law — UV-WyQ1-NC4 @ 00:01:24].']}}],
 'pull_quote': "“You don't spend a million dollars to collect half a million dollars.” — The National Law "
               'Review (R3nWxu374QE @ 00:22:53).',
 'diagram_id': 'diag-03',
 'action_checklist': ["Mine your own client file for the debtor's bank details, check copies, wire "
                      'remittances, and credit-application bank references [The National Law Review — '
                      'R3nWxu374QE @ 00:05:05].',
                      "Lock the debtor's financial disclosure or examination on record under penalty of "
                      'perjury, then run an asset search to compare the two [Private Investigator Videos — '
                      'q-khGCaOPck @ 00:02:10].',
                      'Use the federal bankruptcy schedules of assets and liabilities as your '
                      'post-judgment discovery checklist [The National Law Review — R3nWxu374QE @ '
                      '00:11:32].',
                      "Serve a turnover order on any bank so the bank itself searches for the debtor's "
                      'accounts [Hendershot Cowart P.C. — -kyDpaMUqFY @ 00:01:03].',
                      "Record a fifa with the superior court so it operates as a lien on the debtor's real "
                      'or personal property [Downs Law — K1KakWduA04 @ 00:00:23].',
                      'Skip the defunct LLC, read the guarantee carefully, and bring the personal '
                      'guarantors to the table with a judgment debtor exam [The National Law Review — '
                      'R3nWxu374QE @ 00:28:39].'],
 'statutory_citations': [{'title': 'The National Law Review — Enforcement Post Judgment Proceedings and '
                                   'Collections [00:02:25]',
                          'url': 'https://www.youtube.com/watch?v=R3nWxu374QE&t=145s',
                          'relevance': 'Primary practitioner testimony on pre-suit asset mapping, '
                                       'provisional remedies, and debtors who abscond and dissipate '
                                       'assets.'},
                         {'title': 'Hendershot Cowart P.C. — Texas Judgment Collection: Tools to Get Paid '
                                   'After You Win [00:01:03]',
                          'url': 'https://www.youtube.com/watch?v=-kyDpaMUqFY&t=63s',
                          'relevance': 'Primary practitioner testimony on turnover orders served on any '
                                       'bank and the 25% receiver cut.'},
                         {'title': 'Lawyer Tips by The Sterling Firm #lawyer #law — POST-JUDGMENT: HOW TO '
                                   'COLLECT YOUR MONEY? POST JUDGMENT COLLECTION METHOD | #LAWYER #LAWFIRM '
                                   '[00:04:15]',
                          'url': 'https://www.youtube.com/watch?v=UV-WyQ1-NC4&t=255s',
                          'relevance': 'Primary practitioner testimony on wage levy deposits, the 25% net '
                                       'wage remittance, and levy fee schedules.'},
                         {'title': 'SQE1window — Enforcement of Judgments - CH 20 - Dispute Resolution '
                                   '[00:07:55]',
                          'url': 'https://www.youtube.com/watch?v=Khe45F-Cnr4&t=475s',
                          'relevance': 'Primary practitioner testimony on attachment of earnings '
                                       'thresholds, forms, and the interest stop.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'K1KakWduA04',
                       'title': 'How to Collect on a Judgment',
                       'channel': 'Downs Law',
                       'author': 'Downs Law',
                       'text': 'Garnish means seize, and bank funds are frozen for three days and then '
                               'deposited into the court for you to collect.',
                       'tip': 'Garnish means seize, and bank funds are frozen for three days and then '
                              'deposited into the court for you to collect.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=K1KakWduA04&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=K1KakWduA04&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bX8Hhszjuxs',
                       'title': 'Enforcement of Judgments: Part 1: Introduction',
                       'channel': 'Sacramento County Public Law Library',
                       'author': 'Sacramento County Public Law Library',
                       'text': 'You cannot tell friends or family that the debtor is a deadbeat; you may '
                               'only ask about location, such as whether a forwarding address was left.',
                       'tip': 'You cannot tell friends or family that the debtor is a deadbeat; you may '
                              'only ask about location, such as whether a forwarding address was left.',
                       'timestamp': 242,
                       'timestamp_seconds': 242,
                       'timestamp_label': '[00:04:02]',
                       'url': 'https://www.youtube.com/watch?v=bX8Hhszjuxs&t=242s',
                       'markdown': '[00:04:02](https://www.youtube.com/watch?v=bX8Hhszjuxs&t=242s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R3nWxu374QE',
                       'title': 'Enforcement Post Judgment Proceedings and Collections',
                       'channel': 'The National Law Review',
                       'author': 'The National Law Review',
                       'text': "You don't spend a million dollars to collect half a million dollars.",
                       'tip': "You don't spend a million dollars to collect half a million dollars.",
                       'timestamp': 1373,
                       'timestamp_seconds': 1373,
                       'timestamp_label': '[00:22:53]',
                       'url': 'https://www.youtube.com/watch?v=R3nWxu374QE&t=1373s',
                       'markdown': '[00:22:53](https://www.youtube.com/watch?v=R3nWxu374QE&t=1373s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R3nWxu374QE',
                       'title': 'Enforcement Post Judgment Proceedings and Collections',
                       'channel': 'The National Law Review',
                       'author': 'The National Law Review',
                       'text': 'So, read guarantee carefully and know how it works.',
                       'tip': 'So, read guarantee carefully and know how it works.',
                       'timestamp': 1880,
                       'timestamp_seconds': 1880,
                       'timestamp_label': '[00:31:20]',
                       'url': 'https://www.youtube.com/watch?v=R3nWxu374QE&t=1880s',
                       'markdown': '[00:31:20](https://www.youtube.com/watch?v=R3nWxu374QE&t=1880s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'R3nWxu374QE',
                       'title': 'Enforcement Post Judgment Proceedings and Collections',
                       'channel': 'The National Law Review',
                       'author': 'The National Law Review',
                       'text': 'The escalation path runs from an order to compel, to contempt with daily '
                               'fines, to a civil arrest warrant.',
                       'tip': 'The escalation path runs from an order to compel, to contempt with daily '
                              'fines, to a civil arrest warrant.',
                       'timestamp': 2057,
                       'timestamp_seconds': 2057,
                       'timestamp_label': '[00:34:17]',
                       'url': 'https://www.youtube.com/watch?v=R3nWxu374QE&t=2057s',
                       'markdown': '[00:34:17](https://www.youtube.com/watch?v=R3nWxu374QE&t=2057s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-kyDpaMUqFY',
                       'title': 'Texas Judgment Collection: Tools to Get Paid After You Win',
                       'channel': 'Hendershot Cowart P.C.',
                       'author': 'Hendershot Cowart P.C.',
                       'text': "I say that's sort of a last resort because they typically take 25% of "
                               'whatever is collected.',
                       'tip': "I say that's sort of a last resort because they typically take 25% of "
                              'whatever is collected.',
                       'timestamp': 104,
                       'timestamp_seconds': 104,
                       'timestamp_label': '[00:01:44]',
                       'url': 'https://www.youtube.com/watch?v=-kyDpaMUqFY&t=104s',
                       'markdown': '[00:01:44](https://www.youtube.com/watch?v=-kyDpaMUqFY&t=104s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fQZc8moX-c4',
                       'title': 'Post Judgment Collection Methods',
                       'channel': 'LawShelf',
                       'author': 'LawShelf',
                       'text': 'A judgment lien blocks a sale but cannot force a foreclosure, and it may '
                               'yield nothing for 20 years while it needs renewal and interest accrues.',
                       'tip': 'A judgment lien blocks a sale but cannot force a foreclosure, and it may '
                              'yield nothing for 20 years while it needs renewal and interest accrues.',
                       'timestamp': 181,
                       'timestamp_seconds': 181,
                       'timestamp_label': '[00:03:01]',
                       'url': 'https://www.youtube.com/watch?v=fQZc8moX-c4&t=181s',
                       'markdown': '[00:03:01](https://www.youtube.com/watch?v=fQZc8moX-c4&t=181s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q-khGCaOPck',
                       'title': 'Steps To Collect Court Judgment Debt Assets',
                       'channel': 'Private Investigator Videos',
                       'author': 'Private Investigator Videos',
                       'text': 'Collection agencies are contingency phone-callers, giving away a third may '
                               'be permanent, and collection is passive while recovery is active.',
                       'tip': 'Collection agencies are contingency phone-callers, giving away a third may '
                              'be permanent, and collection is passive while recovery is active.',
                       'timestamp': 677,
                       'timestamp_seconds': 677,
                       'timestamp_label': '[00:11:17]',
                       'url': 'https://www.youtube.com/watch?v=q-khGCaOPck&t=677s',
                       'markdown': '[00:11:17](https://www.youtube.com/watch?v=q-khGCaOPck&t=677s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FSUH2GyMLJ8',
                       'title': 'How To E-File A Civil Judgment',
                       'channel': 'Circuit Court Clerk of Nashville, Davidson County',
                       'author': 'Circuit Court Clerk of Nashville, Davidson County',
                       'text': 'Use the generated form to enter the amount, the basis of default, '
                               'agreement, or trial, and the post-judgment interest rate.',
                       'tip': 'Use the generated form to enter the amount, the basis of default, '
                              'agreement, or trial, and the post-judgment interest rate.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=FSUH2GyMLJ8&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=FSUH2GyMLJ8&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NL1hJNjxmU4',
                       'title': 'Civil Procedure Statutes, Rules & Definitions | 91 Flashcards for 1L | '
                                'Law Frog RN, Esq.',
                       'channel': 'Law Frog RN, Esq.',
                       'author': 'Law Frog RN, Esq.',
                       'text': 'Removal must be filed within 30 days, with a one-year cap.',
                       'tip': 'Removal must be filed within 30 days, with a one-year cap.',
                       'timestamp': 629,
                       'timestamp_seconds': 629,
                       'timestamp_label': '[00:10:29]',
                       'url': 'https://www.youtube.com/watch?v=NL1hJNjxmU4&t=629s',
                       'markdown': '[00:10:29](https://www.youtube.com/watch?v=NL1hJNjxmU4&t=629s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b-12dpeHnyA',
                       'title': 'Week 14: Closing Address & Judgment EXPLAINED | Nigerian Law School Civil '
                                'Litigation',
                       'channel': 'Nigerian Law School Lectures',
                       'author': 'Nigerian Law School Lectures',
                       'text': 'Failure to sign a judgement renders it invalid.',
                       'tip': 'Failure to sign a judgement renders it invalid.',
                       'timestamp': 1883,
                       'timestamp_seconds': 1883,
                       'timestamp_label': '[00:31:23]',
                       'url': 'https://www.youtube.com/watch?v=b-12dpeHnyA&t=1883s',
                       'markdown': '[00:31:23](https://www.youtube.com/watch?v=b-12dpeHnyA&t=1883s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7vopi99AK4A',
                       'title': 'QUT Law Week 6 Class: Introduction to case law - Part 2 and tips for '
                                'Assignment Two',
                       'channel': 'Law Librarianship: Legal Research',
                       'author': 'Law Librarianship: Legal Research',
                       'text': 'The core question is whether a case is still good law.',
                       'tip': 'The core question is whether a case is still good law.',
                       'timestamp': 94,
                       'timestamp_seconds': 94,
                       'timestamp_label': '[00:01:34]',
                       'url': 'https://www.youtube.com/watch?v=7vopi99AK4A&t=94s',
                       'markdown': '[00:01:34](https://www.youtube.com/watch?v=7vopi99AK4A&t=94s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'r3PQ_FYkNRM',
                       'title': 'Justiciability and the "Case or Controversy Requirement" [LEAP Preview: '
                                'Constitutional Law]',
                       'channel': 'Studicata',
                       'author': 'Studicata',
                       'text': 'Jailing the father does not redress an economic loss, while damages would.',
                       'tip': 'Jailing the father does not redress an economic loss, while damages would.',
                       'timestamp': 1743,
                       'timestamp_seconds': 1743,
                       'timestamp_label': '[00:29:03]',
                       'url': 'https://www.youtube.com/watch?v=r3PQ_FYkNRM&t=1743s',
                       'markdown': '[00:29:03](https://www.youtube.com/watch?v=r3PQ_FYkNRM&t=1743s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UV-WyQ1-NC4',
                       'title': 'POST-JUDGMENT: HOW TO COLLECT YOUR MONEY? POST JUDGMENT COLLECTION METHOD '
                                '| #LAWYER #LAWFIRM',
                       'channel': 'Lawyer Tips by The Sterling Firm #lawyer #law',
                       'author': 'Lawyer Tips by The Sterling Firm #lawyer #law',
                       'text': 'File the satisfaction of judgment within 15 days or face liability.',
                       'tip': 'File the satisfaction of judgment within 15 days or face liability.',
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=UV-WyQ1-NC4&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=UV-WyQ1-NC4&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5rA-sJpvgAY',
                       'title': 'CASENGINE Execution Module: Enforce Judgments & Recover Debts',
                       'channel': 'Casengine App',
                       'author': 'Casengine App',
                       'text': 'Keeping the two apart is what stops the same money being counted twice.',
                       'tip': 'Keeping the two apart is what stops the same money being counted twice.',
                       'timestamp': 486,
                       'timestamp_seconds': 486,
                       'timestamp_label': '[00:08:06]',
                       'url': 'https://www.youtube.com/watch?v=5rA-sJpvgAY&t=486s',
                       'markdown': '[00:08:06](https://www.youtube.com/watch?v=5rA-sJpvgAY&t=486s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ObrPaCTQ6ZQ',
                       'title': 'How to Collect Judgment. #Law #history #facts',
                       'channel': 'Calhoun School of Law',
                       'author': 'Calhoun School of Law',
                       'text': 'Wait until the appellate timeframe is exhausted, then start enforcement '
                               'the next day.',
                       'tip': 'Wait until the appellate timeframe is exhausted, then start enforcement the '
                              'next day.',
                       'timestamp': 76,
                       'timestamp_seconds': 76,
                       'timestamp_label': '[00:01:16]',
                       'url': 'https://www.youtube.com/watch?v=ObrPaCTQ6ZQ&t=76s',
                       'markdown': '[00:01:16](https://www.youtube.com/watch?v=ObrPaCTQ6ZQ&t=76s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Khe45F-Cnr4',
                       'title': 'Enforcement of Judgments - CH 20 - Dispute Resolution',
                       'channel': 'SQE1window',
                       'author': 'SQE1window',
                       'text': 'Debtors must receive at least seven clear days notice before enforcement '
                               'unless the court permits otherwise.',
                       'tip': 'Debtors must receive at least seven clear days notice before enforcement '
                              'unless the court permits otherwise.',
                       'timestamp': 435,
                       'timestamp_seconds': 435,
                       'timestamp_label': '[00:07:15]',
                       'url': 'https://www.youtube.com/watch?v=Khe45F-Cnr4&t=435s',
                       'markdown': '[00:07:15](https://www.youtube.com/watch?v=Khe45F-Cnr4&t=435s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'jPO9_I_LBSw',
                       'title': 'How To Collect a Civil Judgment in California',
                       'channel': 'Attorney Michael Ehline',
                       'author': 'Attorney Michael Ehline',
                       'text': "Don't sue without insurance or a known asset.",
                       'tip': "Don't sue without insurance or a known asset.",
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=jPO9_I_LBSw&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=jPO9_I_LBSw&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
