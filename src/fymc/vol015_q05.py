from __future__ import annotations

CHAPTER_5 = {'id': 'Q5',
 'chapter_id': 'Q5',
 'chapter_number': 5,
 'question_number': 5,
 'slug': 'wage-garnishments-bank-levies-writs-of-execution',
 'question_prompt': 'How do wage garnishments, bank levies, and writs of execution actually pull money '
                    'from a debtor, and how do debtors try to stop them?',
 'kicker': 'Q5 / THE BIG MONEY PLAYBOOKS',
 'title': 'Wage Garnishments, Bank Levies, and Writs of Execution',
 'subtitle': 'Bank levy vs. wage garnishment mechanics, California bank levies, multi-bank levy strategy '
             'against businesses, Georgia garnishment limits, small-claims wage garnishment, what follows '
             'a writ of execution, and debtor countermeasures including exemptions, appeals, bankruptcy, '
             'and IRS levy relief',
 'layout_template': 'case_study',
 'reading_time_minutes': 15,
 'executive_summary': 'Judgment-recovery practitioners agree the judgment is only a license to hunt. The '
                      "creditor has to locate a job or a bank account and fire the state's collection "
                      'machinery personally. Wage garnishment is the ongoing workhorse, running check '
                      'after check under an order of continuing lien. A bank levy is a one-shot freeze '
                      'that needs a fresh writ to repeat. The numbers swing by state: 25% of wages in '
                      'Knoxville and Georgia practice, 10% of net in Arizona, and a federal ceiling tied '
                      'to 30 times minimum wage. Operators widen the net. Mr. Grey levies four major banks '
                      'at once, Maryland creditors request writs for every bank in a region, and creditors '
                      'pressure debtors through subpoenas and asset disclosure. The friction points are '
                      "that exemptions are reactive and debtor-claimed, Arizona's 10% cap can lose to 30% "
                      'interest, and a bankruptcy filing freezes everything instantly.',
 'key_metrics': [{'label': 'Wage garnishment take per paycheck',
                  'metric': 'Wage garnishment take per paycheck',
                  'value': 'Up to 25 percent of wages',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Jed McKeehan says the court's garnishment tells the employer to start taking "
                             'up to 25 percent of wages and send it through the court for as long as the '
                             'debtor keeps the job.',
                  'source': 'Jedidiah “Jed” McKeehan ([0Kq_0NfOnMo @ 00:01:13])'},
                 {'label': 'Arizona wage garnishment cap',
                  'metric': 'Arizona wage garnishment cap',
                  'value': '10% of net wages (down from 25% a few years ago)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'John Skiba reports Arizona creditors can now take only 10% of net wages, '
                             'leaving 90% protected. Judgments accruing at a contract rate of roughly 28 '
                             'to 30% can outrun that payment.',
                  'source': 'Consumer Warrior ([YmCEqLCbD3s @ 00:02:53])'},
                 {'label': 'Simultaneous bank levies',
                  'metric': 'Simultaneous bank levies',
                  'value': '4 major banks at once',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Mr. Grey runs a four-bank levy strategy. Overage goes back to the debtor '
                             'when the banks take too much, and an American Airlines levy ended with the '
                             "call 'your money's coming.'",
                  'source': 'Mr. Grey Judgment Enforcement ([CLxNTh8V1qQ @ 00:00:01])'},
                 {'label': 'Garnishee bank response window (California)',
                  'metric': 'Garnishee bank response window (California)',
                  'value': '10 statutory days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Bobby Benjy says the levied bank gets ten statutory days to determine how '
                             "much it held in the debtor's name as of the levy date before freezing funds "
                             'up to the writ amount.',
                  'source': 'Bobby Benjy ([a13Ojjc6ruw @ 00:03:26])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same hard truth: the judgment is a '
                              'hunting license, not a check. Knoxville attorney Jed McKeehan screens every '
                              'would-be plaintiff with one question: does this person have any money they '
                              'can actually pay, or will you win a judgment and never collect a dime? A '
                              "defendant with no cash but a steady job is 'something I can work with' "
                              '[0Kq_0NfOnMo @ 00:00:22]. There is no $10,000 waiting in the back of the '
                              "courtroom. It is the creditor's responsibility to go get the money when the "
                              'defendant does not pay voluntarily, which happens often [0Kq_0NfOnMo @ '
                              '00:00:56]. John Skiba of Consumer Warrior puts the gate in numbers. In '
                              'roughly 99% of circumstances, a private creditor needs a court judgment '
                              'before it can obtain a writ of garnishment. The carve-outs belong to '
                              'government collectors on taxes and certain student loans, who run '
                              'administrative wage garnishment without suing first [YmCEqLCbD3s @ '
                              '00:01:19]. The Verdict breakdown explains why the judgment is worth '
                              'chasing. Once entered, it fixes the amount owed, starts interest running, '
                              "and can become a lien on real estate. It also hands the winner the state's "
                              'collection machinery, which the winner can use mostly without asking a '
                              "judge's permission each time [aWnv0AR52jY @ 00:02:47].",
                              'The second point of agreement is that wage garnishment and the bank levy '
                              'are the two workhorse tools, and they behave very differently. McKeehan '
                              'calls them the two simplest ways to collect, especially on judgments under '
                              "a few thousand dollars. If the debtor keeps the job, the court's "
                              'garnishment tells the employer to take up to 25 percent of wages and route '
                              'it through the court, automatically, check after check. The bank levy, by '
                              'contrast, is a one-time hit. The bank sends whatever sits in the account up '
                              'to the amount owed, and if the balance is thin, part of the judgment stays '
                              'uncovered [0Kq_0NfOnMo @ 00:02:06]. Skiba confirms the same split under '
                              "Arizona practice. After the debtor's 10-day objection window closes, the "
                              'court issues an order of continuing lien, and the employer keeps '
                              'withholding every paycheck without renewal until the judgment is paid in '
                              'full [YmCEqLCbD3s @ 00:04:17]. A bank writ gives the creditor one shot, and '
                              'trying again requires a fresh writ [YmCEqLCbD3s @ 00:08:23]. County Portal '
                              "Law describes the same division from the sheriff's side. The bank must "
                              'freeze immediately up to the debt, and the employer must deduct a portion '
                              'each pay period [Nl9nVJJo6Xs @ 00:00:34].',
                              'Third, every practitioner agrees that exemptions do not stop the first '
                              'strike. They only claw money back if the debtor moves fast. Mike Ziegler of '
                              'Debt Fighters calls Florida protections like Social Security and '
                              "head-of-household status 'reactive.' The creditor garnishes first and the "
                              'wages or account get frozen. Only then does the burden shift to the debtor '
                              'to file a claim of exemption and go through a hearing [_XHjLiGTAYw @ '
                              '00:04:15]. The Verdict breakdown adds that an unclaimed exemption can be '
                              'lost outright, since in many cases the claim must be made in writing on a '
                              'deadline after the levy [aWnv0AR52jY @ 00:18:45]. County Portal Law warns '
                              'that a debtor who does not file on time may lose even basic exempt property '
                              '[Nl9nVJJo6Xs @ 00:01:43]. The one weapon that beats the whole machine is '
                              'bankruptcy. Eric Steiner of Steiner Law Group says a bank garnishment stops '
                              'when a bankruptcy case is filed, and the creditor and bank must then '
                              'unfreeze the account [RAT4YjdyfEo @ 00:02:52]. For a creditor, that '
                              'consensus sets the operating rhythm. Strike before the debtor organizes, '
                              "and treat exemption claims as the debtor's burden to raise. Price in the "
                              'risk that a cornered debtor files and freezes everything at once.'],
               'table': {'caption': 'Where the enforcement practitioners line up',
                         'headers': ['Consensus Point', 'What Practitioners Report', 'Expert Source'],
                         'rows': [['Judgment comes before any garnishment',
                                   'Private creditors need a court judgment in roughly 99% of '
                                   'circumstances before a writ of garnishment can issue against wages',
                                   'Consumer Warrior ([YmCEqLCbD3s @ 00:01:19])'],
                                  ['Government collectors skip the courthouse entirely',
                                   'Government agencies and the IRS can use administrative garnishment on '
                                   'wages without first obtaining a court order',
                                   'Thomson Reuters ([hAq3ZiEtqk0 @ 00:04:52])'],
                                  ['Collectability screen comes before suing',
                                   'Ask whether the defendant has money or a job before filing, or the '
                                   'judgment may never collect a dime',
                                   'Jedidiah “Jed” McKeehan ([0Kq_0NfOnMo @ 00:00:22])'],
                                  ['Wage garnishment is an ongoing collection stream',
                                   'The employer keeps withholding each paycheck and sending it through '
                                   'the court for as long as the debtor holds that job',
                                   'Jedidiah “Jed” McKeehan ([0Kq_0NfOnMo @ 00:01:30])'],
                                  ['Bank levy is a one-shot strike',
                                   'A bank writ gives the creditor one attempt; collecting again requires '
                                   'going back to court for another writ of garnishment',
                                   'Consumer Warrior ([YmCEqLCbD3s @ 00:08:23])'],
                                  ['Exemptions are reactive, not automatic shields',
                                   'The creditor garnishes first; the debtor then carries the burden to '
                                   'file a claim of exemption and attend a hearing',
                                   'Ziegler Diamond Law: Debt Fighters ([_XHjLiGTAYw @ 00:04:15])'],
                                  ['Bankruptcy filing stops the entire machine',
                                   'The automatic stay halts bank garnishments, and the creditor and '
                                   'financial institution must unfreeze frozen accounts upon filing',
                                   'Steiner Law Group, LLC ([RAT4YjdyfEo @ 00:02:52])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Los Angeles collections attorney Bobby Benjy lays out the bank-levy '
                              'pipeline step by step. After judgment, the creditor applies for a writ of '
                              'execution. It is a one- or two-page document bearing the court seal and the '
                              "deputy clerk's signature. It certifies the judgment, states the amount due "
                              'as of a date certain, names the debtor, and is directed to a county sheriff '
                              "[a13Ojjc6ruw @ 00:01:34]. The creditor's attorney sends the original writ "
                              'to the sheriff with written instructions, and the sheriff opens a file. '
                              'Notices of levy plus a memorandum of garnishee then go to the bank, such as '
                              'Wells Fargo. The bank gets ten statutory days to determine what it held in '
                              "the debtor's name on the levy date. Benjy says three kinds of accounts can "
                              "all be levied if the creditor crosses the T's and dots the i's: accounts "
                              "held solely by the debtor, accounts in the name of the debtor's spouse, and "
                              'accounts held jointly with a non-debtor third party [a13Ojjc6ruw @ '
                              '00:04:01]. Safe deposit boxes get shut down, drilled, and auctioned at a '
                              "sheriff's execution sale [a13Ojjc6ruw @ 00:06:00]. County Portal Law adds "
                              'that the sheriff keeps a small fee. When no assets turn up, the writ comes '
                              'back unsatisfied and the creditor must try again later [Nl9nVJJo6Xs @ '
                              '00:01:59].',
                              'Finding the money is the real skill. Skiba says creditors pull employment '
                              "data from the personal section of the debtor's credit report, even when it "
                              'is stale. They locate banks by checking how the debtor paid past creditors, '
                              'whether by check or automatic debit [YmCEqLCbD3s @ 00:06:03]. Eric Steiner '
                              'reports that Maryland creditors often request writs of garnishment other '
                              'than wages for every bank in a geographic area, to cast the widest possible '
                              'net. Many banks freeze accounts on mere notice that such a writ has been '
                              'requested [RAT4YjdyfEo @ 00:02:32]. Mr. Grey Judgment Enforcement runs a '
                              'four-bank levy strategy, hitting four major banks at once. Overage gets '
                              'sent back to the debtor when the banks take too much. The American Airlines '
                              'legal department in Texas called to complain about one of these levies. Mr. '
                              'Grey asked which section of the California Code of Civil Procedure barred '
                              'levying more than one bank at a time. Mr. Grey also pointed out that CT '
                              "Corp, the company's agent for service of process, had been served on a "
                              'seven-year-old judgment, so the company had sat on its rights. Mr. Grey '
                              'then threatened to sue if local counsel dragged the matter into court. The '
                              "next call was 'your money's coming' [CLxNTh8V1qQ @ 00:00:01].",
                              'On wages, the numbers vary sharply by state. Jeffrey Kelly says Georgia '
                              'creditors can take up to 25% of net wages, which is $250 out of a $1,000 '
                              'week. An employer who botches the withholding by even a small amount can '
                              'become liable for the entire debt. An associate who used to work for a '
                              'collection company told Kelly it happened all the time [cHsptp1ujiI @ '
                              '00:02:35]. Skiba warns of a different trap in Arizona, where the cap is 10% '
                              'of net wages. Defaulted credit-card judgments accrue at a contract rate of '
                              'roughly 28 to 30%. The 10% often fails to cover that interest, producing an '
                              'indefinite garnishment while the balance grows [YmCEqLCbD3s @ 00:04:40]. '
                              'Discovery is the pressure lever. Mike Ziegler says Florida judgment debtors '
                              'must complete the Form 1.977 financial disclosure and may face a deposition '
                              'in aid of execution. Refusing can, in extreme cases, bring a writ of bodily '
                              'attachment, which is effectively an arrest warrant [_XHjLiGTAYw @ '
                              "00:02:41]. Mr. Grey spotted a debtor's new management job in Facebook "
                              'wedding photos. Mr. Grey then filed wage garnishments, subpoenaed the '
                              'debtor, and floated subpoenaing the newly employed spouse. The debtor '
                              'begged off, agreed not to bother with a motion to vacate, and said there '
                              'was extra money to pay [DYAsqrLyB-c @ 00:00:49].'],
               'table': {'caption': 'Enforcement mechanics and hard numbers by practitioner',
                         'headers': ['Mechanic / Number', 'Street Detail', 'Expert Source'],
                         'rows': [['Writ of execution format and routing',
                                   'One or two pages with court seal and deputy clerk signature, amount '
                                   'due as of a date certain, directed to county sheriff',
                                   'Bobby Benjy ([a13Ojjc6ruw @ 00:01:34])'],
                                  ['Bank answer window in California levies',
                                   'The garnishee bank gets ten statutory days to determine funds held in '
                                   "the debtor's name on the levy date",
                                   'Bobby Benjy ([a13Ojjc6ruw @ 00:03:26])'],
                                  ['Bank answer window in Maryland garnishments',
                                   'The financial institution has 30 days to answer the writ; the debtor '
                                   'has only 30 days to claim an exemption',
                                   'Steiner Law Group, LLC ([RAT4YjdyfEo @ 00:01:52])'],
                                  ['Federal consumer-debt wage cap formula',
                                   'Lesser of 25% of weekly disposable income or the excess over 30 times '
                                   'federal minimum wage; full 25% at $290 weekly',
                                   'Thomson Reuters ([hAq3ZiEtqk0 @ 00:02:09])'],
                                  ['Georgia wage take and employer exposure',
                                   'Up to 25% of net wages, meaning $250 from a $1,000 weekly paycheck in '
                                   'a typical Georgia case',
                                   'Law Office of Jeffrey B. Kelly ([cHsptp1ujiI @ 00:00:01])'],
                                  ['Arizona bank account exemption for 2026',
                                   'Roughly $5,600 protected in one checking or savings account, adjusted '
                                   'annually, and doubled for married couples',
                                   'Consumer Warrior ([YmCEqLCbD3s @ 00:07:23])'],
                                  ['Automatic federal benefits bank shield',
                                   'Banks must automatically protect two months of directly deposited '
                                   'Social Security, SSI, and veterans benefits without any filing',
                                   'Verdict ([aWnv0AR52jY @ 00:17:03])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the Money Actually Gets Found',
                           'body': 'Working collectors win by widening the target list and hitting '
                                   "accounts the debtor does not expect, then letting the garnishee's own "
                                   'liability do the pressure work [Mr. Grey Judgment Enforcement — '
                                   'CLxNTh8V1qQ @ 00:00:01].',
                           'items': ['Levy several banks at once instead of gambling on one account. Mr. '
                                     'Grey runs a four-bank levy and lets any overage flow back to the '
                                     'debtor [Mr. Grey Judgment Enforcement — CLxNTh8V1qQ @ 00:00:01]',
                                     'Mine the credit report and the old payment trail. Employment data '
                                     'sits in the personal section of the credit report, and past payments '
                                     'by check or auto-debit reveal the bank [Consumer Warrior — '
                                     'YmCEqLCbD3s @ 00:06:03]',
                                     'Levy the spouse-name and joint accounts too. Accounts in the '
                                     "spouse's name or held jointly with a non-debtor third party can be "
                                     'levied if the paperwork is clean [Bobby Benjy — a13Ojjc6ruw @ '
                                     '00:04:01]',
                                     'Count on garnishee liability to keep employers careful. In Georgia, '
                                     'an employer that withholds the wrong amount can become liable for '
                                     'the entire debt [Law Office of Jeffrey B. Kelly — cHsptp1ujiI @ '
                                     '00:02:35]']},
               'sop_steps': [{'step': 1,
                              'title': 'Screen collectability before suing',
                              'action': 'Confirm the defendant has reachable money or a job before '
                                        'investing in a judgment.',
                              'detail': 'Ask whether the person has money to pay you or a job you can '
                                        'garnish. Without either, the judgment may never collect a dime '
                                        '[Jedidiah “Jed” McKeehan — 0Kq_0NfOnMo @ 00:00:22]'},
                             {'step': 2,
                              'title': 'Pull the writ and route it to the sheriff',
                              'action': 'Apply for a writ of execution and deliver the original to the '
                                        'county sheriff with written levy instructions.',
                              'detail': "The creditor's attorney sends the writ to the sheriff with "
                                        'instructions. The sheriff opens a file and follows them within '
                                        'statutory limits [Bobby Benjy — a13Ojjc6ruw @ 00:02:07]'},
                             {'step': 3,
                              'title': 'Serve every garnishee in reach',
                              'action': 'Serve the employer and request writs against every bank in the '
                                        "debtor's area at once.",
                              'detail': 'Creditors often request writs of garnishment other than wages for '
                                        'all bank accounts in a geographic area to make sure they find at '
                                        'least one account [Steiner Law Group, LLC — RAT4YjdyfEo @ '
                                        '00:02:11]'},
                             {'step': 4,
                              'title': 'Apply funds and file the satisfaction',
                              'action': 'Credit turned-over funds against the judgment and file a partial '
                                        'or full satisfaction.',
                              'detail': 'The bank turns funds over to the sheriff, who passes them to the '
                                        'creditor. The creditor applies the money to the judgment and '
                                        'issues a partial or full satisfaction [Bobby Benjy — a13Ojjc6ruw '
                                        '@ 00:05:11]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fight is over how deep the paycheck cut goes, and the '
                              'practitioners quote different ceilings depending on where they stand. Jed '
                              'McKeehan frames the wage garnishment as an order telling the employer to '
                              'start taking up to 25 percent of wages and send it through the court for as '
                              'long as the debtor keeps that job [0Kq_0NfOnMo @ 00:01:13]. Jeffrey B. '
                              'Kelly says Georgia is rough: up to 25 percent of net wages, so a $1,000 '
                              'weekly earner loses $250, and creditors do not care about the rent '
                              '[cHsptp1ujiI @ 00:00:01]. John Skiba of Consumer Warrior reports Arizona '
                              'dropped from 25 percent to 10 percent of net wages, leaving 90 percent '
                              'protected, and names Texas and Florida as states with no wage garnishment '
                              'at all [YmCEqLCbD3s @ 00:03:09]. Verdict draws the map differently: the '
                              'federal cap is the lesser of 25 percent of disposable earnings or the '
                              'excess over 30 times the federal minimum wage, California caps at 20 '
                              'percent, Illinois at 15 percent of gross, New York at 10 percent of gross, '
                              'and the effective consumer-debt bans are Texas, Pennsylvania, North '
                              'Carolina, and South Carolina, while Florida shields a head of household '
                              '[aWnv0AR52jY @ 00:15:39]. Pull the local cap before pricing any garnishment '
                              'file.',
                              'On bank levies, the split is between targeted hits and the wide net. Skiba '
                              'says creditors find the bank through the credit report or by checking how '
                              'past bills were paid, by check or automatic debit, then serve that one '
                              'institution [YmCEqLCbD3s @ 00:06:03]. Eric Steiner of Steiner Law Group '
                              'describes the Maryland alternative: creditors request writs of garnishment '
                              'other than wages for all bank accounts in a geographical area to cast as '
                              'wide a net as possible and make sure they find at least one account '
                              '[RAT4YjdyfEo @ 00:02:11]. Mr. Grey runs a business-collection version, a '
                              'four-bank levy strategy against four major banks at once, and reports that '
                              'every time, money is sent back to the judgment debtor because the levy took '
                              'too much. When the American Airlines legal department in Texas called to '
                              'say it could not be done, Mr. Grey demanded the section of the California '
                              'Code of Civil Procedure that bars levying more than one bank at a time '
                              '[CLxNTh8V1qQ @ 00:00:01]. The multi-bank play compensates for a hard limit: '
                              'Jed McKeehan calls the levy a one-time thing where you do not know the '
                              'balance ahead of time [0Kq_0NfOnMo @ 00:02:06], and Skiba adds that a '
                              'second shot requires a fresh writ.',
                              'Once collection lands, the playbooks fork. Kelly calls bankruptcy the '
                              'fastest fix because the automatic stay lets the firm serve the employer and '
                              'the garnishing creditor immediately, and warns that a counter lawsuit costs '
                              'a lot of money with low odds if the debt is actually owed [cHsptp1ujiI @ '
                              '00:06:43]. Brandon Weaver pushes the opposite: show up, fight, demand '
                              'proof, contracts, data storage, and a state collection license, hire a '
                              'lawyer even at roughly $1,000, and attack a default within 6 months where '
                              'the defendant was not personally served [iHnRz6R1jS8 @ 00:03:34]. Mike '
                              'Ziegler of Ziegler Diamond Law lays out four exits, set aside, pay in full, '
                              'settle, or bankruptcy, and argues judgment holders discount because time is '
                              'money and a bird in hand is worth two in the bush [_XHjLiGTAYw @ 00:06:04]. '
                              'On the IRS track, Mike Sullivan, a former IRS agent, says a single phone '
                              'call interrupts the automated CP14, CP501, CP503, CP504, and 1058 notice '
                              'cycle, after which the agency takes a 433F or 433A and lands the case in '
                              'currently non-collectible status or a payment agreement [wSIheT1KrFw @ '
                              '00:01:32]. The collector reading: debtors who call, fight, or file each '
                              'break a different link.'],
               'table': {'caption': 'Side-by-side playbooks where practitioners split on garnishment and '
                                    'levy execution',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How much of each paycheck the garnishment takes',
                                   'Georgia allows up to 25 percent of net wages, so $250 comes out of a '
                                   '$1,000 week',
                                   'Arizona now caps the take at 10 percent of net wages, down from 25 '
                                   'percent a few years ago',
                                   'Law Office of Jeffrey B. Kelly ([cHsptp1ujiI @ 00:00:01]); Consumer '
                                   'Warrior ([YmCEqLCbD3s @ 00:03:09])'],
                                  ['How the creditor picks which bank to hit',
                                   "Locate one bank through the credit report or the debtor's past payment "
                                   'method, then serve it',
                                   'Request writs for all banks in a geographical area, or levy four major '
                                   'banks at the same time',
                                   'Consumer Warrior ([YmCEqLCbD3s @ 00:06:03]); Steiner Law Group, LLC '
                                   '([RAT4YjdyfEo @ 00:02:11]); Mr. Grey Judgment Enforcement '
                                   '([CLxNTh8V1qQ @ 00:00:01])'],
                                  ['Who screens exempt money before it gets frozen',
                                   'The bank should check for Social Security deposits and answer that the '
                                   'account is exempt',
                                   'Protections are reactive: the creditor freezes first and the debtor '
                                   'carries the burden to claim exemption',
                                   'Consumer Warrior ([YmCEqLCbD3s @ 00:06:43]); Ziegler Diamond Law: Debt '
                                   'Fighters ([_XHjLiGTAYw @ 00:04:15])'],
                                  ['How a debtor stops an active wage garnishment',
                                   'File Chapter 7 or Chapter 13 and serve the automatic stay on the '
                                   'employer right away',
                                   'Show up, demand proof and verification, and attack defaults within 6 '
                                   'months for lack of personal service',
                                   'Law Office of Jeffrey B. Kelly ([cHsptp1ujiI @ 00:06:11]); Brandon '
                                   'Weaver ([iHnRz6R1jS8 @ 00:03:34])'],
                                  ['How the judgment gets resolved without a bankruptcy filing',
                                   'Settle at a discount because judgment holders know time is money and '
                                   'certainty beats waiting',
                                   'Negotiate a payment plan, lump sum, or hardship relief before the '
                                   'garnishment ever begins',
                                   'Ziegler Diamond Law: Debt Fighters ([_XHjLiGTAYw @ 00:06:04]); The '
                                   'DeVries Law Firm ([lfTu39ygsSI @ 00:07:13])'],
                                  ['How an IRS levy or garnishment gets interrupted',
                                   'Call the IRS to break the automated notice cycle and submit a 433F or '
                                   '433A statement',
                                   'Respond within 30 days of the certified Notice of Intent to Levy with '
                                   'Fresh Start or an Offer in Compromise',
                                   'Former IRS Agent Representation   4.2M Views ([wSIheT1KrFw @ '
                                   '00:01:32]); Revermann Law ([74MBbfTO3Po @ 00:00:16])'],
                                  ['How long the creditor can keep the judgment alive',
                                   'Georgia fi fa renewals cost a very small amount and can in theory '
                                   'continue forever',
                                   'California enforces for 10 years, renewable, with accrued interest '
                                   'folded into the new principal',
                                   'Law Office of Jeffrey B. Kelly ([cHsptp1ujiI @ 00:05:37]); Verdict '
                                   '([aWnv0AR52jY @ 00:21:10])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The ugliest economics check is interest outrunning the garnishment. Skiba '
                              'reports that judgments on defaulted credit cards often carry contract '
                              'interest around 28 to 30 percent, so a 10 percent net-wage garnishment can '
                              'fail to cover the monthly interest, creating an indefinite garnishment '
                              'where the balance grows each month; Skiba has watched people pay that way '
                              'for years before realizing they need a lump-sum settlement or a bankruptcy '
                              "[YmCEqLCbD3s @ 00:04:40]. Verdict runs the same math at California's 10 "
                              'percent simple rate, where an unpaid judgment doubles in 10 years without '
                              'the creditor doing anything, and flags that renewal folds accrued interest '
                              'into the new principal [aWnv0AR52jY @ 00:07:40]. The O.J. Simpson file is '
                              'the cautionary ceiling: a $33.5 million 1997 judgment, an estate claim over '
                              '$117 million after 27 years, a claim accepted at just under $58 million, '
                              'and estate assets of roughly half a million to a million dollars, because '
                              'pension and Florida homestead protections kept the bulk out of reach '
                              '[aWnv0AR52jY @ 00:23:08]. Kelly adds that Georgia judgments can be renewed '
                              'with a fi fa for a very small amount of money, in theory forever '
                              '[cHsptp1ujiI @ 00:05:54]. Size of the number means nothing next to the '
                              'exemption map.',
                              'Process friction kills timelines on both sides. The Westgate Law attorney, '
                              'who reports more than 3,000 bankruptcy cases, says the sheriff is usually '
                              "the problem: after the lender's attorney forwards the bankruptcy notice, "
                              'getting the sheriff to notify the employer or bank can take weeks or even '
                              'months, so the debtor has to keep calling and sometimes go down to the '
                              'Sheriff Department, and money taken from a levy before filing may never '
                              'come back [Nb1quOaLNWk @ 00:01:37]. Kelly flags a Georgia trap that cuts '
                              'against employers: if an employer messes up the garnishment by any small '
                              'amount, it can become liable for the entire debt, and an associate who used '
                              'to work for a collection company says small employers goofed it up all the '
                              'time [cHsptp1ujiI @ 00:02:54]. Thomson Reuters confirms liability for '
                              "failing to comply with a garnishment order falls on the employer's "
                              'shoulders [hAq3ZiEtqk0 @ 00:05:09]. On notice, Steiner says mailing the '
                              'writ to a last known address satisfies Maryland law even when the creditor '
                              'has no current address, which is why debtors first learn of the freeze when '
                              "the debit card fails [RAT4YjdyfEo @ 00:01:32]. Kelly's roommate scenario "
                              'completes the sneak attack: service on any adult in the home.',
                              'The last group of traps rewards the operator who moves first. Verdict cites '
                              'Pew research that more than 70 percent of debt collection lawsuits end in '
                              'default judgments, reaching 82 percent in some state data, and warns that '
                              'appealing does not stop collection: without a bond, typically covering the '
                              'full judgment plus interest and costs, the winner may garnish and levy '
                              'while the appeal is pending [aWnv0AR52jY @ 00:14:00]. Ziegler says a debtor '
                              'who fails to complete the Florida 1.977 form can, in extreme circumstances, '
                              'face a writ of bodily attachment, which is in fact an arrest warrant '
                              '[_XHjLiGTAYw @ 00:02:41]. Mr. Grey turned that discovery pressure into '
                              "payment: after spotting the debtor's new job and new spouse through wedding "
                              'pictures on Facebook, Mr. Grey issued a subpoena and wage garnishments and '
                              'floated subpoenaing the spouse, and the debtor begged, dropped any motion '
                              'to vacate, and said they had extra money to pay [DYAsqrLyB-c @ 00:00:25]. '
                              'Bobby Benjy supplies the auction warning: a safe deposit box holding '
                              "$50,000 to $100,000 in diamonds can sell at a sheriff's execution sale for "
                              'whatever the highest bidder offers, even $1,000 against a $10,000 judgment '
                              '[a13Ojjc6ruw @ 00:06:17]. County Portal Law adds that a writ can come back '
                              'unsatisfied when the sheriff finds no assets, forcing the creditor to try '
                              'again later.'],
               'table': {'caption': 'Firsthand failure modes, bottlenecks, and the economics behind each '
                                    'one',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Interest outruns a 10 percent wage garnishment',
                                   'Contract interest of 28 to 30 percent keeps the balance growing while '
                                   'the debtor pays for years',
                                   'Read the judgment copy and check whether the 10 percent actually pays '
                                   'the judgment down',
                                   'Consumer Warrior ([YmCEqLCbD3s @ 00:05:09])'],
                                  ['Bank levy lands on a thin account',
                                   'The creditor does not know the balance ahead of time, so the levy may '
                                   'not cover the judgment',
                                   'A levy is one shot; trying again means going back to get another writ '
                                   'issued',
                                   'Jedidiah “Jed” McKeehan ([0Kq_0NfOnMo @ 00:02:06]); Consumer Warrior '
                                   '([YmCEqLCbD3s @ 00:08:37])'],
                                  ['Safe deposit contents sell at a fire-sale price',
                                   'Diamonds worth $50,000 to $100,000 can go to the highest bidder at a '
                                   "sheriff's execution sale",
                                   'If the top bid is $1,000, only $1,000 gets credited against a $10,000 '
                                   'judgment',
                                   'Bobby Benjy ([a13Ojjc6ruw @ 00:06:17])'],
                                  ['Sheriff lag after a bankruptcy filing',
                                   'Getting the sheriff to notify the employer or bank can take weeks or '
                                   'even months',
                                   'Money taken after filing comes back but slowly; pre-filing levy money '
                                   'may not return at all',
                                   'Westgate Law ([Nb1quOaLNWk @ 00:01:52])'],
                                  ['Employer botches the garnishment withholding amount',
                                   'Small Georgia employers goof the amount and become liable for the '
                                   'entire debt owed',
                                   'Compliance liability sits on the employer, giving the creditor a '
                                   'second party to collect from',
                                   'Law Office of Jeffrey B. Kelly ([cHsptp1ujiI @ 00:02:54]); Thomson '
                                   'Reuters ([hAq3ZiEtqk0 @ 00:05:09])'],
                                  ['Corporate legal department pushes back on a multi-bank levy',
                                   'American Airlines legal said it could not be done; the seven-year-old '
                                   'judgment had been served on CT Corp',
                                   'Mr. Grey held firm, said they sat on their rights, threatened suit, '
                                   'and got the call that the money was coming',
                                   'Mr. Grey Judgment Enforcement ([CLxNTh8V1qQ @ 00:01:01])'],
                                  ['Debtor overcommits to an IRS payment agreement',
                                   'A caller got stuck with a $2,000 a month IRS payment agreement with '
                                   'nowhere to find the money',
                                   'IRS National Standards for food, housing, and car costs decide '
                                   "affordability, not the taxpayer's own estimate",
                                   'Former IRS Agent Representation   4.2M Views ([wSIheT1KrFw @ '
                                   '00:02:52])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Levy Operator Gate',
                           'body': 'Run these four checks before committing filing fees and sheriff time '
                                   'to a garnishment or levy, because each one is a place the '
                                   'practitioners watched collections stall or reverse.',
                           'items': ['Run the interest math before relying on a 10 percent garnishment; at '
                                     '28 to 30 percent contract interest the balance can grow every month '
                                     'and the garnishment never ends [Consumer Warrior — YmCEqLCbD3s @ '
                                     '00:04:40].',
                                     'Confirm the employer computes the withholding correctly; in Georgia '
                                     'a botched amount by any small sum can make the employer liable for '
                                     'the entire debt [Law Office of Jeffrey B. Kelly — cHsptp1ujiI @ '
                                     '00:02:54].',
                                     'Expect exemption fights right after the freeze: all-Social Security '
                                     'accounts, the Arizona roughly $5,600 single-account exemption that '
                                     'doubles for married couples, and joint accounts holding an adult '
                                     "child's money [Consumer Warrior — YmCEqLCbD3s @ 00:07:38].",
                                     'Once a bankruptcy notice lands, enforcement must stop and any money '
                                     'taken from the account after filing goes back to the debtor, so '
                                     'track the sheriff and the bank [Westgate Law — Nb1quOaLNWk @ '
                                     '00:02:19].']}}],
 'pull_quote': '"To be precise, nobody can jail you for owing the money. People get jailed for ignoring '
               'the court\'s orders." — Verdict (aWnv0AR52jY @ 00:18:27).',
 'diagram_id': 'diag-05',
 'action_checklist': ["Confirm the judgment is entered, then pull the debtor's employer from the personal "
                      'section of the credit report before applying for the writ of garnishment [Consumer '
                      'Warrior — YmCEqLCbD3s @ 00:02:00].',
                      'Apply for the writ of execution, then deliver the original to the sheriff with '
                      'written instructions so a levy file gets opened [Bobby Benjy — a13Ojjc6ruw @ '
                      '00:02:07].',
                      'Levy several banks at once, four major banks or every bank in the geographical '
                      'area, so at least one account gets caught [Mr. Grey Judgment Enforcement — '
                      'CLxNTh8V1qQ @ 00:00:01].',
                      'Force financial disclosure through the Florida 1.977 form and a deposition in aid '
                      'of execution to map assets, income, and where they sit [Ziegler Diamond Law: Debt '
                      'Fighters — _XHjLiGTAYw @ 00:01:40].',
                      'Check social media for a new job or spouse, then pair a debtor subpoena with wage '
                      'garnishments to bring the debtor to the table [Mr. Grey Judgment Enforcement — '
                      'DYAsqrLyB-c @ 00:00:25].',
                      'Apply every recovery to the balance and file a partial or full satisfaction of '
                      'judgment with the court after each payout [Bobby Benjy — a13Ojjc6ruw @ 00:05:11].'],
 'statutory_citations': [{'title': "Mr. Grey Judgment Enforcement — Mr  Grey's bank levy strategy - How to "
                                   'collect a judgment from a business [00:00:01]',
                          'url': 'https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=1s',
                          'relevance': 'Primary practitioner testimony on the four-bank simultaneous levy '
                                       'and handling corporate legal pushback.'},
                         {'title': "Consumer Warrior — Bank Levy vs. Wage Garnishment... What's the "
                                   'Difference? [00:04:40]',
                          'url': 'https://www.youtube.com/watch?v=YmCEqLCbD3s&t=280s',
                          'relevance': 'Primary practitioner testimony on the 10 percent Arizona cap, '
                                       'contract interest, and indefinite garnishment.'},
                         {'title': 'Bobby Benjy — California Money Judgment Enforcement Series - Part 5: '
                                   'Bank Levies [00:01:17]',
                          'url': 'https://www.youtube.com/watch?v=a13Ojjc6ruw&t=77s',
                          'relevance': 'Primary practitioner testimony on the writ of execution, sheriff '
                                       'levy workflow, and safe deposit box sales.'},
                         {'title': 'Verdict — # What Happens If You Lose a Civil Lawsuit? Judgment & '
                                   'Garnishment Explained [00:15:39]',
                          'url': 'https://www.youtube.com/watch?v=aWnv0AR52jY&t=939s',
                          'relevance': 'Primary practitioner testimony on state-by-state garnishment caps '
                                       'and the four collection machines.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '0Kq_0NfOnMo',
                       'title': 'Collecting Money After A Judgment - Wage Garnishment And Bank Levy',
                       'channel': 'Jedidiah “Jed” McKeehan',
                       'author': 'Jedidiah “Jed” McKeehan',
                       'text': "Bank levy is a one-time thing; it's not an ongoing collection effort like "
                               'a wage garnishment is.',
                       'tip': "Bank levy is a one-time thing; it's not an ongoing collection effort like a "
                              'wage garnishment is.',
                       'timestamp': 126,
                       'timestamp_seconds': 126,
                       'timestamp_label': '[00:02:06]',
                       'url': 'https://www.youtube.com/watch?v=0Kq_0NfOnMo&t=126s',
                       'markdown': '[00:02:06](https://www.youtube.com/watch?v=0Kq_0NfOnMo&t=126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YmCEqLCbD3s',
                       'title': "Bank Levy vs. Wage Garnishment... What's the Difference?",
                       'channel': 'Consumer Warrior',
                       'author': 'Consumer Warrior',
                       'text': 'Many of these judgments have interest at the contract rate of interest, '
                               "and with a defaulted credit card, that's usually right around 28 to 30%.",
                       'tip': 'Many of these judgments have interest at the contract rate of interest, and '
                              "with a defaulted credit card, that's usually right around 28 to 30%.",
                       'timestamp': 280,
                       'timestamp_seconds': 280,
                       'timestamp_label': '[00:04:40]',
                       'url': 'https://www.youtube.com/watch?v=YmCEqLCbD3s&t=280s',
                       'markdown': '[00:04:40](https://www.youtube.com/watch?v=YmCEqLCbD3s&t=280s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YmCEqLCbD3s',
                       'title': "Bank Levy vs. Wage Garnishment... What's the Difference?",
                       'channel': 'Consumer Warrior',
                       'author': 'Consumer Warrior',
                       'text': 'In Arizona, at least in the year 2026, there is a bank account exemption '
                               'that protects roughly $5,600 in your checking account or savings account.',
                       'tip': 'In Arizona, at least in the year 2026, there is a bank account exemption '
                              'that protects roughly $5,600 in your checking account or savings account.',
                       'timestamp': 443,
                       'timestamp_seconds': 443,
                       'timestamp_label': '[00:07:23]',
                       'url': 'https://www.youtube.com/watch?v=YmCEqLCbD3s&t=443s',
                       'markdown': '[00:07:23](https://www.youtube.com/watch?v=YmCEqLCbD3s&t=443s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'aWnv0AR52jY',
                       'title': '# What Happens If You Lose a Civil Lawsuit? Judgment & Garnishment '
                                'Explained',
                       'channel': 'Verdict',
                       'author': 'Verdict',
                       'text': 'Under a federal regulation, when a bank receives a garnishment order, it '
                               'must protect two months worth of directly deposited federal benefits '
                               'without you filing anything.',
                       'tip': 'Under a federal regulation, when a bank receives a garnishment order, it '
                              'must protect two months worth of directly deposited federal benefits '
                              'without you filing anything.',
                       'timestamp': 1023,
                       'timestamp_seconds': 1023,
                       'timestamp_label': '[00:17:03]',
                       'url': 'https://www.youtube.com/watch?v=aWnv0AR52jY&t=1023s',
                       'markdown': '[00:17:03](https://www.youtube.com/watch?v=aWnv0AR52jY&t=1023s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a13Ojjc6ruw',
                       'title': 'California Money Judgment Enforcement Series - Part 5: Bank Levies',
                       'channel': 'Bobby Benjy',
                       'author': 'Bobby Benjy',
                       'text': "It could be an account in the name of the judgment debtor's spouse, or in "
                               'the name of the judgment debtor plus some third party, and any one of '
                               'those can successfully be levied upon.',
                       'tip': "It could be an account in the name of the judgment debtor's spouse, or in "
                              'the name of the judgment debtor plus some third party, and any one of those '
                              'can successfully be levied upon.',
                       'timestamp': 241,
                       'timestamp_seconds': 241,
                       'timestamp_label': '[00:04:01]',
                       'url': 'https://www.youtube.com/watch?v=a13Ojjc6ruw&t=241s',
                       'markdown': '[00:04:01](https://www.youtube.com/watch?v=a13Ojjc6ruw&t=241s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cHsptp1ujiI',
                       'title': 'Wage Garnishment in Georgia - How Much Can They Take and How Do You Stop '
                                'It?',
                       'channel': 'Law Office of Jeffrey B. Kelly',
                       'author': 'Law Office of Jeffrey B. Kelly',
                       'text': 'If your employer messes up this garnishment at all by any small amount of '
                               'money, they can become liable for the entire amount of the debt owed.',
                       'tip': 'If your employer messes up this garnishment at all by any small amount of '
                              'money, they can become liable for the entire amount of the debt owed.',
                       'timestamp': 155,
                       'timestamp_seconds': 155,
                       'timestamp_label': '[00:02:35]',
                       'url': 'https://www.youtube.com/watch?v=cHsptp1ujiI&t=155s',
                       'markdown': '[00:02:35](https://www.youtube.com/watch?v=cHsptp1ujiI&t=155s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CLxNTh8V1qQ',
                       'title': "Mr  Grey's bank levy strategy - How to collect a judgment from a business",
                       'channel': 'Mr. Grey Judgment Enforcement',
                       'author': 'Mr. Grey Judgment Enforcement',
                       'text': 'I have a four bank levy strategy, this is four major banks, and every time '
                               'we do that money is sent back to the judgment debtor because we took too '
                               'much.',
                       'tip': 'I have a four bank levy strategy, this is four major banks, and every time '
                              'we do that money is sent back to the judgment debtor because we took too '
                              'much.',
                       'timestamp': 1,
                       'timestamp_seconds': 1,
                       'timestamp_label': '[00:00:01]',
                       'url': 'https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=1s',
                       'markdown': '[00:00:01](https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=1s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'CLxNTh8V1qQ',
                       'title': "Mr  Grey's bank levy strategy - How to collect a judgment from a business",
                       'channel': 'Mr. Grey Judgment Enforcement',
                       'author': 'Mr. Grey Judgment Enforcement',
                       'text': "Here's what happened: I get a call yesterday, your money's coming.",
                       'tip': "Here's what happened: I get a call yesterday, your money's coming.",
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=CLxNTh8V1qQ&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iHnRz6R1jS8',
                       'title': 'Stop Wage Garnishment? Appeal Judgments? || Live Debt Free || Good Credit '
                                'Good Life',
                       'channel': 'Brandon Weaver',
                       'author': 'Brandon Weaver',
                       'text': 'You have 6 months to appeal default judgments where the defendant was not '
                               'personally served.',
                       'tip': 'You have 6 months to appeal default judgments where the defendant was not '
                              'personally served.',
                       'timestamp': 214,
                       'timestamp_seconds': 214,
                       'timestamp_label': '[00:03:34]',
                       'url': 'https://www.youtube.com/watch?v=iHnRz6R1jS8&t=214s',
                       'markdown': '[00:03:34](https://www.youtube.com/watch?v=iHnRz6R1jS8&t=214s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lfTu39ygsSI',
                       'title': 'How To Stop Wage Garnishment Immediately',
                       'channel': 'The DeVries Law Firm',
                       'author': 'The DeVries Law Firm',
                       'text': 'If you default on a federal student loan, the Department of Education can '
                               'garnish up to 15% of your disposable income without going to court.',
                       'tip': 'If you default on a federal student loan, the Department of Education can '
                              'garnish up to 15% of your disposable income without going to court.',
                       'timestamp': 269,
                       'timestamp_seconds': 269,
                       'timestamp_label': '[00:04:29]',
                       'url': 'https://www.youtube.com/watch?v=lfTu39ygsSI&t=269s',
                       'markdown': '[00:04:29](https://www.youtube.com/watch?v=lfTu39ygsSI&t=269s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RAT4YjdyfEo',
                       'title': 'Bank Account Garnishments',
                       'channel': 'Steiner Law Group, LLC',
                       'author': 'Steiner Law Group, LLC',
                       'text': 'Creditors often will request writs of garnishment other than wages for all '
                               'bank accounts in a geographical area to cast as wide a net as possible.',
                       'tip': 'Creditors often will request writs of garnishment other than wages for all '
                              'bank accounts in a geographical area to cast as wide a net as possible.',
                       'timestamp': 131,
                       'timestamp_seconds': 131,
                       'timestamp_label': '[00:02:11]',
                       'url': 'https://www.youtube.com/watch?v=RAT4YjdyfEo&t=131s',
                       'markdown': '[00:02:11](https://www.youtube.com/watch?v=RAT4YjdyfEo&t=131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Nb1quOaLNWk',
                       'title': 'How To Stop Wage Garnishments and Bank Levies | Bankruptcy Law',
                       'channel': 'Westgate Law',
                       'author': 'Westgate Law',
                       'text': 'Getting the sheriff to notify your employer or notify the bank can '
                               'sometimes take weeks or even months.',
                       'tip': 'Getting the sheriff to notify your employer or notify the bank can '
                              'sometimes take weeks or even months.',
                       'timestamp': 97,
                       'timestamp_seconds': 97,
                       'timestamp_label': '[00:01:37]',
                       'url': 'https://www.youtube.com/watch?v=Nb1quOaLNWk&t=97s',
                       'markdown': '[00:01:37](https://www.youtube.com/watch?v=Nb1quOaLNWk&t=97s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wSIheT1KrFw',
                       'title': 'Preventing IRS Bank Levy and Wage Garnishment: Tips to Halt Enforcement '
                                'Actions Immediately',
                       'channel': 'Former IRS Agent Representation   4.2M Views',
                       'author': 'Former IRS Agent Representation   4.2M Views',
                       'text': "When you call, what you think you're paying and what IRS is going to allow "
                               'you to pay are going to be two different things.',
                       'tip': "When you call, what you think you're paying and what IRS is going to allow "
                              'you to pay are going to be two different things.',
                       'timestamp': 172,
                       'timestamp_seconds': 172,
                       'timestamp_label': '[00:02:52]',
                       'url': 'https://www.youtube.com/watch?v=wSIheT1KrFw&t=172s',
                       'markdown': '[00:02:52](https://www.youtube.com/watch?v=wSIheT1KrFw&t=172s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Nl9nVJJo6Xs',
                       'title': 'What Happens After A Writ Of Execution?',
                       'channel': 'County Portal Law',
                       'author': 'County Portal Law',
                       'text': 'Sometimes, the sheriff cannot find any assets and the writ is returned '
                               'unsatisfied; if this happens, the creditor must try again later.',
                       'tip': 'Sometimes, the sheriff cannot find any assets and the writ is returned '
                              'unsatisfied; if this happens, the creditor must try again later.',
                       'timestamp': 119,
                       'timestamp_seconds': 119,
                       'timestamp_label': '[00:01:59]',
                       'url': 'https://www.youtube.com/watch?v=Nl9nVJJo6Xs&t=119s',
                       'markdown': '[00:01:59](https://www.youtube.com/watch?v=Nl9nVJJo6Xs&t=119s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hAq3ZiEtqk0',
                       'title': 'Financial Literacy: Understanding and Managing Debt–Segment 7: '
                                'Garnishments, Liens, & Judgements',
                       'channel': 'Thomson Reuters',
                       'author': 'Thomson Reuters',
                       'text': 'Liability for failure to comply with a garnishment order falls on the '
                               "employer's shoulders.",
                       'tip': 'Liability for failure to comply with a garnishment order falls on the '
                              "employer's shoulders.",
                       'timestamp': 309,
                       'timestamp_seconds': 309,
                       'timestamp_label': '[00:05:09]',
                       'url': 'https://www.youtube.com/watch?v=hAq3ZiEtqk0&t=309s',
                       'markdown': '[00:05:09](https://www.youtube.com/watch?v=hAq3ZiEtqk0&t=309s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_XHjLiGTAYw',
                       'title': 'What happens After a Judgement is Entered?',
                       'channel': 'Ziegler Diamond Law: Debt Fighters',
                       'author': 'Ziegler Diamond Law: Debt Fighters',
                       'text': 'The company that has the judgment usually will first execute on the '
                               'garnishment, and after those assets have been frozen the burden is on the '
                               'judgment debtor to file a claim of exemption.',
                       'tip': 'The company that has the judgment usually will first execute on the '
                              'garnishment, and after those assets have been frozen the burden is on the '
                              'judgment debtor to file a claim of exemption.',
                       'timestamp': 255,
                       'timestamp_seconds': 255,
                       'timestamp_label': '[00:04:15]',
                       'url': 'https://www.youtube.com/watch?v=_XHjLiGTAYw&t=255s',
                       'markdown': '[00:04:15](https://www.youtube.com/watch?v=_XHjLiGTAYw&t=255s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '74MBbfTO3Po',
                       'title': 'How to stop a bank levy or wage garnishment?',
                       'channel': 'Revermann Law',
                       'author': 'Revermann Law',
                       'text': "They send what's called a Notice of Intent to Levy by certified mail, and "
                               'once 30 days goes by, they have the right to go to your bank or to your '
                               'employer.',
                       'tip': "They send what's called a Notice of Intent to Levy by certified mail, and "
                              'once 30 days goes by, they have the right to go to your bank or to your '
                              'employer.',
                       'timestamp': 16,
                       'timestamp_seconds': 16,
                       'timestamp_label': '[00:00:16]',
                       'url': 'https://www.youtube.com/watch?v=74MBbfTO3Po&t=16s',
                       'markdown': '[00:00:16](https://www.youtube.com/watch?v=74MBbfTO3Po&t=16s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DYAsqrLyB-c',
                       'title': 'Judgment enforcement with wage garnishments | how do you collect on a '
                                'small claims judgement order!',
                       'channel': 'Mr. Grey Judgment Enforcement',
                       'author': 'Mr. Grey Judgment Enforcement',
                       'text': 'I subpoenaed [the debtor] to come and answer questions and I also did '
                               "what's called wage garnishments.",
                       'tip': 'I subpoenaed [the debtor] to come and answer questions and I also did '
                              "what's called wage garnishments.",
                       'timestamp': 25,
                       'timestamp_seconds': 25,
                       'timestamp_label': '[00:00:25]',
                       'url': 'https://www.youtube.com/watch?v=DYAsqrLyB-c&t=25s',
                       'markdown': '[00:00:25](https://www.youtube.com/watch?v=DYAsqrLyB-c&t=25s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q5.'}]}
