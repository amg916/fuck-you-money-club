from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'q10-compliance-loan-servicing-back-office',
 'question_prompt': 'What regulatory and servicing infrastructure sits behind a note, from MLO rules to '
                    'loan servicers and payment histories?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'Compliance and Loan Servicing: The Back Office of Every Note',
 'subtitle': 'Dodd-Frank origination and MLO compensation rules, RESPA/TILA/ECOA, SAFE Act exam concepts, '
             'non-QM qualification, choosing full-service vs. client-managed servicers, servicing '
             'timelines, reading payment histories and servicer portals, and why poorly documented '
             'seller-finance notes are worthless',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Note operators and servicers converge on one rule: board every note with a licensed '
                      'servicer, because the servicer is the compliance shield, the fraud preventer, and '
                      'the payment record that makes paper sellable. Sohail Badruddin sees at least a '
                      'couple of noncompliant notes a week and rejects or forces reclosing on the blatant '
                      'ones, while the servicing desk Scott Horne and Sohail walk through runs a fixed '
                      'waterfall: four-day check hold, underlying lien first, escrow into trust, fee, then '
                      'remainder to the investor. Street pricing runs $15 to $35 per loan per month for '
                      'performing paper, roughly $90 plus contingency for full-service collections, and '
                      '$350 to $700 for attorney-reviewed closing packages. The split comes on control: '
                      'FIXnotes and Rick of Paperstac keep loss mitigation in-house, while full-service '
                      'shops can bill a point on UPB when a loan reperforms.',
 'key_metrics': [{'label': 'Full-Service Collections Servicing Cost',
                  'metric': 'Full-Service Collections Servicing Cost',
                  'value': 'About $90 per loan per month plus a contingency fee on collected deals',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'FIXnotes calls this the most an investor pays for servicing and reports '
                             'never finding a full-service shop at that price with satisfying results.',
                  'source': 'FIXnotes | Non-Performing Note Investing ([5H6jVWw2QK0 @ 00:00:00])'},
                 {'label': 'Standard Client-Managed Servicing Fee',
                  'metric': 'Standard Client-Managed Servicing Fee',
                  'value': '$30 per loan per month standard; as low as $15 with bare-bones servicers',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Benchmarked against the BSI itemized fee menu for servicers doing more than '
                             'sending statements.',
                  'source': 'FIXnotes | Non-Performing Note Investing ([5H6jVWw2QK0 @ 00:04:06])'},
                 {'label': 'Attorney-Reviewed Closing Document Package',
                  'metric': 'Attorney-Reviewed Closing Document Package',
                  'value': '$350 to $400 for a standard note and deed of trust package; $600 to $700 for a '
                           'wrapped note',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Sohail Badruddin's pricing for doc prep with attorney review, usually "
                             'charged to the borrower.',
                  'source': 'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ 00:12:47])'},
                 {'label': 'Borrower Check Clearing Hold',
                  'metric': 'Borrower Check Clearing Hold',
                  'value': '4 days before funds are disbursed',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Servicer waits for a borrower check to clear before paying the underlying '
                             'lien, escrow, fee, and investor remainder.',
                  'source': "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:09:42])"}],
 'sections': [{'number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every operator in this back office starts from the same point: the servicer '
                              'is not optional overhead, it is the core of the note business. Chris of 7e '
                              'Investments calls the servicer the heart of the operation, the company that '
                              'collects payments, keeps the investor inside state and federal rules, and '
                              'through which everything flows [SZhJFIusBp4 @ 00:00:43]. JKP Holdings host '
                              'Dave Putz tells every note creator to board with a servicer, because the '
                              'servicer can and will reject flawed paper, not to be rude but to protect '
                              'itself from audits [uKK5_EVlvus @ 00:06:44]. On the Owner Finance Network '
                              'walkthrough, Sohail Badruddin and Scott Horne keep the job narrow: the '
                              'servicer does not modify loans and is not a hardcore collection agency; it '
                              'collects payments, distributes them properly, and acts as the fraud '
                              'preventer that keeps money from being pocketed in a distressed stretch '
                              'instead of paying the mortgage [adTW0EyLeRk @ 00:10:34]. The Loan Note '
                              "Exchange breakdown calls collecting and servicing the long part of a note's "
                              'life, ten to twenty years of tracking interest, principal, taxes, '
                              'insurance, and late follow-ups, and rates a clean payment record among the '
                              'most valuable things a holder owns, because it drives what the note is '
                              'worth today [epnA26NInuc @ 00:03:37].',
                              'The second point of agreement is that the paperwork and the escrow money '
                              'have to be clean before a servicer will touch them. Sohail reports that '
                              'Provident Loan Servicing sees at least a couple of noncompliant notes every '
                              'week; blatant ones get rejected or sent back to be reclosed on the '
                              "servicer's suggestions, and lenders who refuse cannot be onboarded because "
                              'a foreclosed borrower will sue everybody involved [uKK5_EVlvus @ 00:07:44]. '
                              "Nathan Turner's North Carolina land contract shows the pattern: a "
                              'promissory note under one page when Sohail puts normal at three to four '
                              'pages, a blank notary block, an unrecorded contract, and a seller '
                              'collecting taxes and insurance inside the payment instead of escrowing '
                              "them, which Nathan calls the borrower's money, not the lender's "
                              '[uKK5_EVlvus @ 00:20:37]. Horne and Sohail run escrow the same way in daily '
                              'operations: where no underlying lender escrows, the servicer holds taxes '
                              'and insurance in a dedicated trust account that nobody else touches, and '
                              'only principal and interest move on to the investor [adTW0EyLeRk @ '
                              '00:11:59]. Chris of 7e lists escrow collection as a function every investor '
                              'must consciously assign, to the servicer, an internal team, or another '
                              'hire, alongside workouts on non-performing paper [SZhJFIusBp4 @ 00:01:36].',
                              'Licensing trainers and servicers describe the same federal overlay, built '
                              'after the 2008 crisis, sitting on top of owner-occupied paper. Ameritrain '
                              'boils Dodd-Frank down to three things for an MLO: it created the CFPB, '
                              'delivered the ability-to-repay rule, and strengthened protections for '
                              'homeowners after closing [35EmXeZQAsY @ 00:05:13]. Shari Olefson lays out '
                              'the qualified mortgage lines: no riskier adjustable or balloon structures, '
                              'a term no longer than 30 years, fees capped at 3%, and monthly expenses no '
                              'higher than 43% of monthly income, with QM lenders getting protection '
                              'against lawsuits [g-UjM12V8m0 @ 00:02:32]. Sohail maps that directly onto '
                              'seller paper: a 30-year, fully amortized, regular-payment note typically '
                              'lands as QM, while balloons and prepayment penalties push it into non-QM, '
                              'so the recommendation is to err toward QM because a bank buyer pays more '
                              'for it, even though most note buyers ignore the distinction [uKK5_EVlvus @ '
                              "01:02:09]. SAFE Act trainer Pat O'Connor defines an MLO as someone who "
                              'takes a residential application and offers or negotiates terms for '
                              'compensation or gain, and flags the NMLS identifier required on the '
                              'application, the note, and the mortgage or deed of trust, on top of a '
                              '20-hour prelicensing minimum and eight hours of annual continuing education '
                              '[xZohXlsFnks @ 00:22:30].'],
               'table': {'caption': 'Where the servicers, note buyers, and licensing trainers line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['The servicer is the core of the business',
                                   'Collects payments, keeps the investor compliant with state and federal '
                                   'rules, and everything flows through it',
                                   'Pick the servicer before buying volume because it protects every '
                                   'downstream exit',
                                   '7e Investments ([SZhJFIusBp4 @ 00:00:43])'],
                                  ['Boarding a note is a free collateral audit',
                                   'Servicers can and will reject flawed notes to protect themselves from '
                                   'state audits',
                                   'Treat a boarding rejection as a collateral defect to fix, not an '
                                   'insult',
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '00:06:44])'],
                                  ['Escrow belongs to the borrower, not the lender',
                                   'Taxes and insurance sit in a dedicated trust account that nobody else '
                                   'touches',
                                   'Never sweep escrow dollars into principal and interest revenue on your '
                                   'books',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:11:59])"],
                                  ['Servicing notes matter as much as payment history',
                                   'Contact logs are as important as the ledger for reading the real story '
                                   'of a loan',
                                   'Demand both documents during due diligence before committing to any '
                                   'purchase price',
                                   'Paperstac ([VkGqESM8fdY @ 00:01:54])'],
                                  ['Every servicer portal reads differently and cryptically',
                                   'No two servicers display data the same way, and cryptic column labels '
                                   'are routine',
                                   "Learn each portal's vocabulary or call the servicer for a guided "
                                   'walkthrough',
                                   'Fusion Notes ([Wt2pat2PE2w @ 00:00:59])'],
                                  ['QM structure makes seller paper easier to sell',
                                   'Thirty-year fully amortized notes land as QM while balloons and '
                                   'prepayment penalties push non-QM',
                                   'Default to QM terms whenever a bank could become the eventual note '
                                   'buyer',
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '01:02:09])'],
                                  ['Originator pay cannot track the loan terms',
                                   'Compensation may vary only with the principal amount, never with other '
                                   'terms of the loan',
                                   'Tie any originator payout to principal size, never to rate or term',
                                   'My Mortgage Trainer, Inc. ([nPRf3YuUI2o @ 00:00:35])']]}},
              {'number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The Horne and Sohail timeline starts before closing. The note holder '
                              "downloads the servicer's package, fills out the investor side early, and "
                              'the borrower signs their portion at the table; after closing the servicer '
                              'needs the note, the deed of trust, the closing disclosure, and cancelled '
                              'checks for ACH [adTW0EyLeRk @ 00:01:08]. The first-payment math trips '
                              'people up: close January 15 and the first payment is March 1, but interest '
                              'from January 16 to month end and escrow for the stub period plus February '
                              "still have to be handled, because March pays February's interest backward "
                              "and March's escrow forward. Their fix is collecting the 15 days of interest "
                              'and forward escrow at the closing table, or forwarding the escrow piece to '
                              "the servicer's trust account so nobody chases it when taxes come due "
                              '[adTW0EyLeRk @ 00:02:18]. Within days of boarding, borrowers get a welcome '
                              'letter and statement by email and mail, with check, Cash App, and ACH '
                              "options. FIXnotes adds that onboarding is where the servicer's real work "
                              'sits, uploading the CSV and Excel files, after which mailing houses handle '
                              "statements [5H6jVWw2QK0 @ 00:04:57]. Loan Note Exchange's worked example "
                              'shows what gets boarded: $142,000 financed at 7% over 20 years for roughly '
                              '$1,100 a month [epnA26NInuc @ 00:01:37].',
                              'Once money lands, the servicing desk runs a fixed sequence. Checks sit four '
                              'days to clear; then the servicer pays any underlying lien, pulls escrow '
                              'into trust, deducts its fee, and forwards the remainder to the investor '
                              '[adTW0EyLeRk @ 00:09:56]. Sohail confirms the same three-to-four business '
                              'day clearing window on the JKP show, which is why note language ordering a '
                              'servicer to pay the first lien immediately cannot bind it [uKK5_EVlvus @ '
                              '00:42:45]. The calendar is simple: due on the 1st, late on the 2nd, a '
                              '10-day grace period, and a late charge starting day 11. A late notice plus '
                              'email, text, and call go out after the grace period; by the 20th the '
                              'investor is told and urged to call the borrower, and in Texas the '
                              'recommended law firm sends the initial foreclosure notice on the 20th so '
                              'months of nonpayment do not pile up [adTW0EyLeRk @ 00:19:19]. Escrow '
                              "shortfalls against an underlying lender come out of the investor's "
                              'principal and interest, overages are held until the annual analysis, and '
                              'borrowers cure shortages in a lump sum or over 12 months. On the collection '
                              'side, FIXnotes pairs one RESPA hello letter with one attorney letter that '
                              'routes callers to a web form or straight to a cell phone [5H6jVWw2QK0 @ '
                              '00:01:11].',
                              'Pricing is where operators get nickel-and-dimed. FIXnotes puts full-service '
                              'collections at about $90 per loan per month plus a contingency fee and says '
                              'no servicer at that price produced satisfying results; client-managed '
                              'servicing at $30 is standard, with bare-bones shops as low as $15, and the '
                              'BSI itemized fee menu is the benchmark for comparing boarding, deboarding, '
                              'bankruptcy, and loss mitigation charges [5H6jVWw2QK0 @ 00:04:06]. Rick of '
                              'Paperstac sees performing servicing from $10 to $35, warns that $35 on a '
                              '$200 payment eats nearly 25% of revenue, and flags full-service shops '
                              'charging one point on UPB when a loan reperforms [kXMfkHu1Tu0 @ 00:03:17]. '
                              'Chris of 7e says the $20 to $25 monthly fee balloons to $40 to $45 through '
                              'add-ons, so the fee schedule must be read side by side with the servicing '
                              'agreement [SZhJFIusBp4 @ 00:03:22]. Dan Deppen of Fusion Notes runs Allied '
                              'at $18.50 a month because it is dirt cheap, but keeps a separate '
                              "spreadsheet to find loans in Allied's unordered account list and decodes "
                              'notes like S/W BORR for spoke with borrower; FCI costs more but has the '
                              'cleanest portal, including a payment day variance column that showed a '
                              '217-day gap [Wt2pat2PE2w @ 00:18:17].'],
               'table': {'caption': 'Servicing calendar, cash rules, and borrower payment controls',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Borrower check clearing hold before disbursement',
                                   'Four days of waiting before any funds move onward to anyone',
                                   'Prevents paying the lien or investor on a bounced borrower check',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:09:42])"],
                                  ['Monthly payment and late charge calendar',
                                   'Due on the 1st, late on the 2nd, 10-day grace, charge starts day 11',
                                   'Borrowers learn that receipt date, not mailing date, controls lateness',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:08:47])"],
                                  ['Texas early foreclosure notice trigger',
                                   'Recommended law firm sends the initial foreclosure notice on the 20th',
                                   'Trains borrowers to pay on time and stops months of silent drift',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:19:19])"],
                                  ['Year-end interest reporting to borrowers',
                                   'Servicer sends the 1098 for interest paid by January 31',
                                   'Investor offloads year-end tax paperwork to the servicer every single '
                                   'year',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:15:52])"],
                                  ['Correct base for the late charge',
                                   '5% late charge applies to principal and interest, never to escrows',
                                   'Charging late fees on escrow puts the lender out of compliance and '
                                   'into court',
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '00:54:28])'],
                                  ['Direct deposit bounce rule at the servicer',
                                   'Two bounced payments ends online and direct deposit payment privileges',
                                   "Borrower is moved to cashier's checks or Zelle only from then on",
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '00:25:57])'],
                                  ['Payoff statement source at refinance or sale',
                                   "Payoff comes only from the lender or that lender's servicer directly",
                                   'Closing agents avoid third-party payoff fraud that happens every day',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:16:51])"]]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Servicer-Side Edges the Pros Actually Use',
                           'body': 'These are the moves operators run on top of the standard servicing '
                                   'stack to find hidden exits, speed up workouts, and keep paper '
                                   'boardable.',
                           'items': ['Read the servicing notes, not just the ledger: one Paperstac '
                                     'operator paid about $30,000 for a four-years-delinquent contract for '
                                     'deed with a $40,000 payoff because the notes said the borrower would '
                                     'sign a deed in lieu, and the borrower signed once a new owner '
                                     'replaced the rude attorney [Paperstac — VkGqESM8fdY @ 00:03:17].',
                                     'Hold delegated authority and negotiate yourself: FIXnotes preps the '
                                     'modification the day of the borrower call, sends it with the '
                                     "servicer's ACH authorization form, and sees the loan modified within "
                                     'about 30 days [FIXnotes | Non-Performing Note Investing — '
                                     '5H6jVWw2QK0 @ 00:02:02].',
                                     'Patch missing material terms with a borrower-signed addendum instead '
                                     'of a full redo; only an incorrect interest rate or P&I amount forces '
                                     'redoing the documents [Note Investing & Seller Financing - JKP '
                                     'Holdings — uKK5_EVlvus @ 00:09:09].',
                                     'Favor servicers whose call logs store borrower and lender emails, as '
                                     "Madison's do, so any staffer covering a vacation can follow your "
                                     'written instructions [Fusion Notes — Wt2pat2PE2w @ 00:15:46].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pre-board the investor before closing',
                              'action': 'Download the servicer package, complete the investor side, and '
                                        'send it in ahead of the closing date.',
                              'detail': 'After closing, deliver the note, deed of trust, closing '
                                        'disclosure, and cancelled checks for ACH so the servicer can '
                                        "board immediately [Scott Horne's Owner Finance Network — "
                                        'adTW0EyLeRk @ 00:00:50].'},
                             {'step': 2,
                              'title': 'Settle stub interest and escrow at the table',
                              'action': 'Collect the partial-month interest and forward escrow at closing, '
                                        "or forward the escrow piece to the servicer's trust account.",
                              'detail': 'Sohail recommends bringing in the 15 days of interest plus '
                                        'forward escrows at closing so nobody chases the money at tax time '
                                        "[Scott Horne's Owner Finance Network — adTW0EyLeRk @ 00:03:14]."},
                             {'step': 3,
                              'title': 'Interview servicers on license, fees, and portal',
                              'action': 'Confirm state licensing, read the fee schedule against the '
                                        'servicing agreement, and test the online portal.',
                              'detail': 'Ask which states the servicer is licensed in first, since New '
                                        'York shrinks the field to one or two servicers [7e Investments — '
                                        'SZhJFIusBp4 @ 00:02:44]; reject any servicer without portal '
                                        'access to pay history and servicing notes [Paperstac — '
                                        'kXMfkHu1Tu0 @ 00:04:29].'},
                             {'step': 4,
                              'title': 'Run pay history and servicing notes diligence',
                              'action': 'Pull 12 to 24 months of pay history plus the servicing notes from '
                                        'the seller before closing any purchase.',
                              'detail': 'Price rolling-30 payers down and treat rolling-60 as heavy risk '
                                        '[Paperstac — VkGqESM8fdY @ 00:05:20]; always request the '
                                        'servicing notes from the seller during due diligence [Fusion '
                                        'Notes — Wt2pat2PE2w @ 00:03:11].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over who drives the borrower once a loan is boarded. '
                              'FIXnotes prices full-service collections at roughly 90 bucks a month per '
                              'loan plus a contingency fee on anything collected, says no full-service '
                              'shop has delivered results worth that, and calls client-managed servicing '
                              'the sweet spot, where the licensed servicer handles statements and year-end '
                              'tax accounting while the investor or a hired attorney runs skip tracing, '
                              'letters and modification calls [5H6jVWw2QK0 @ 00:00:00]. Rick at Paperstac '
                              'refuses to crown one model and matches the shop to the operator instead: '
                              'FCI lets a hands-on investor set up and drive their own loss mitigation '
                              'flows, while SN likes to take control for investors who would rather sit in '
                              "the back seat [kXMfkHu1Tu0 @ 00:02:10]. Scott Horne's servicing desk draws "
                              'the hardest line, stating the servicer does not make decisions to modify a '
                              'loan and is not really the collection agent, only collecting payments, '
                              'distributing them properly and acting as the fraud preventer [adTW0EyLeRk @ '
                              '00:10:34]. Yet that same Texas operation has its recommended law firm send '
                              'the initial foreclosure notice on the 20th of the month if the payment has '
                              'not landed, specifically so investors do not sit idle while a borrower '
                              'slides one, two, then three months behind [adTW0EyLeRk @ 00:19:19].',
                              'Price is where the numbers split, and every practitioner quotes a different '
                              'floor and ceiling. FIXnotes calls 30 bucks per loan per month pretty '
                              'standard for a servicer doing more than mailing statements, and has seen '
                              'bare-bones shops go as low as $15 [5H6jVWw2QK0 @ 00:04:06]. Rick at '
                              'Paperstac has seen performing servicing anywhere from 10 or 15 dollars up '
                              'to 35, and warns that 35 bucks against a 200-dollar payment knocks out '
                              'nearly 25 percent of revenue and starts eating yield [kXMfkHu1Tu0 @ '
                              '00:02:41]. Chris at 7e Investments argues the headline rate is the wrong '
                              'number to shop at all: servicers tack on monthly add-ons, so a loan you '
                              'think costs 20 or 25 bucks turns into 40 or 45 very quickly, which is why '
                              'the fee schedule has to be read side by side with the servicing agreement '
                              'before signing [SZhJFIusBp4 @ 00:03:22]. Dan Deppen at Fusion Notes shows '
                              'the trade-off from inside live portals, calling Allied definitely not easy '
                              'to work with yet keeping loans there for one reason, because they are dirt '
                              'cheap at 18.50 a month [Wt2pat2PE2w @ 00:18:17]. The cheap-shop camp is '
                              'buying margin and paying for it in decoding time; the other camps are '
                              'buying visibility and fewer surprises on the invoice.',
                              'Practitioners also split on what belongs in the paper itself. Loan Note '
                              'Exchange walks a seller-financed example where payments run on a 20-year '
                              'schedule but a balloon brings about $112,000 due all at once after seven '
                              'years, presenting it as an ordinary term choice [epnA26NInuc @ 00:01:59]. '
                              'Sohail Badruddin of Provident Loan Servicing takes the opposite line on '
                              "owner-occupied paper: balloons, don't do it; interest-only, don't do it; "
                              'and anything under a five-year balloon Provident will not even board '
                              '[uKK5_EVlvus @ 01:01:17]. Even inside that same episode the room splits on '
                              'prepayment penalties, with one host stating they are against the law on '
                              'owner-occupied notes and Sohail correcting that you can do it, it is just '
                              'not how you would want to, the same way balloons are frowned upon rather '
                              'than illegal [uKK5_EVlvus @ 00:59:48]. Dani Rudd of Legacy Mutual Mortgage '
                              'pushes from the other direction on non-qualified product, noting a non-QM '
                              'loan with as little as 10 percent down carries no PMI and that its rates '
                              'have lately been pricing better than qualified mortgages [5VZzJLRM1kI @ '
                              '00:04:07]. The operator read: the balloon and non-QM structures one camp '
                              'treats as routine, the servicing camp may refuse to board at all.'],
               'table': {'caption': 'Competing servicing and paper-design playbooks, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Who runs borrower outreach after boarding',
                                   'Client-managed: servicer handles statements and tax accounting, '
                                   'investor or attorney negotiates',
                                   'Full-service collections at about 90 bucks per loan plus a contingency '
                                   'fee',
                                   'FIXnotes | Non-Performing Note Investing ([5H6jVWw2QK0 @ 00:00:00])'],
                                  ['Who controls loss mitigation strategy on non-performers',
                                   'FCI lets hands-on investors set up and run their own loss mitigation '
                                   'flows',
                                   'SN likes to take control and handle workouts for back-seat investors',
                                   'Paperstac ([kXMfkHu1Tu0 @ 00:02:10])'],
                                  ['How far the servicer goes on late payers',
                                   'Servicer collects and distributes only, never modifies loans or acts '
                                   'as collector',
                                   'Same desk has a recommended Texas law firm send foreclosure notice on '
                                   'the 20th',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:10:34]); Scott "
                                   "Horne's Owner Finance Network ([adTW0EyLeRk @ 00:19:19])"],
                                  ['Cheap servicer versus clean reporting portal',
                                   'Allied at 18.50 a month, dirt cheap but definitely not easy to '
                                   'navigate',
                                   'FCI is the least cryptic portal but more expensive, never any free '
                                   'lunch',
                                   'Fusion Notes ([Wt2pat2PE2w @ 00:18:17]); Fusion Notes ([Wt2pat2PE2w @ '
                                   '00:19:37])'],
                                  ['Balloons on seller-financed owner-occupied paper',
                                   'Seven-year balloon leaving about $112,000 due at once, presented as a '
                                   'term choice',
                                   "Balloons and interest-only: don't do it; anything under five years "
                                   'gets rejected',
                                   'Loan Note Exchange ([epnA26NInuc @ 00:01:59]); Note Investing & Seller '
                                   'Financing - JKP Holdings ([uKK5_EVlvus @ 01:01:17])'],
                                  ['Qualified mortgage versus non-QM positioning',
                                   'Qualified mortgages get lawsuit protection, are easier to get and cost '
                                   'less money',
                                   'Non-QM with 10 percent down carries no PMI and often prices better '
                                   'lately',
                                   'Shari Olefson ([g-UjM12V8m0 @ 00:01:41]); Dani Rudd ([5VZzJLRM1kI @ '
                                   '00:04:07])'],
                                  ['Funding the escrow gap created at closing',
                                   'Bring 15 days of interest plus the forward escrows to the closing '
                                   'table',
                                   'If tight, collect from the seller at closing or go back at tax time',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:03:14]); Scott "
                                   "Horne's Owner Finance Network ([adTW0EyLeRk @ 00:05:37])"]]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Nathan Turner's North Carolina file is the cleanest anatomy of worthless "
                              'paper. On the surface the numbers looked great: roughly $200,000 of '
                              'property value, a $145,000 sale price, $30,000 down, 10 percent interest on '
                              'a 30-year amortization. Then the promissory note turned out to be less than '
                              'a page, and Nathan knew without reading a word that this was not going to '
                              'be good [uKK5_EVlvus @ 00:15:41]. The signatures were there but the notary '
                              'block was blank, which the hosts treat as unenforceable on its face '
                              '[uKK5_EVlvus @ 00:20:04]. The servicing history showed the seller '
                              'collecting principal, interest, taxes and insurance as one payment and '
                              'keeping the escrow, which Nathan calls a big no-no because that is the '
                              "borrower's money held for them [uKK5_EVlvus @ 00:20:37]. The contract for "
                              'deed was never recorded, which Nathan says means it does not exist in the '
                              'judicial system, so there is nothing to enforce when payments stop, and the '
                              'last three months of payments had already been missed, making it a '
                              'non-performing note on top of everything else. Nathan told the seller to '
                              'tune it up first; the seller never fixed it, and the deal died [uKK5_EVlvus '
                              '@ 00:22:27].',
                              'When paper like that reaches a servicer, the reversal comes fast. Sohail '
                              'sees at least a couple of non-compliant notes a week; the blatantly '
                              'out-of-compliance ones get rejected or sent back for the lender to reclose '
                              "with Provident's corrections, and lenders who refuse simply cannot board, "
                              'because the servicer will not absorb the reputational risk of a borrower '
                              'who sues everybody involved [uKK5_EVlvus @ 00:07:44]. In court the downside '
                              'is worse: best case the documents get corrected, worst case a judge '
                              'nullifies the contract with a rescission, the lender refunds everything the '
                              'borrower paid over, say, five years, and then waits for the property to be '
                              'vacated; on a wrap, most of those proceeds already went to the underlying '
                              'note [uKK5_EVlvus @ 00:13:40]. The panel also kills the pre-signed deed in '
                              'lieu and the clause making a note null and void at 30 days in arrears, '
                              'because a borrower cannot be bound in advance to hand the property back '
                              'without court involvement [uKK5_EVlvus @ 00:48:47]. The flip side shows up '
                              'at Paperstac: a four-years-delinquent contract for deed sat dead because '
                              'the borrower stopped answering a rude attorney, and the Paperstac host read '
                              'the servicing notes, called, and got the deed in lieu [VkGqESM8fdY @ '
                              '00:04:07].',
                              "The quieter losses are operational. Scott Horne's servicing desk explains "
                              'that when the escrow being collected runs short of what the underlying lien '
                              'holder charges, the shortfall cannot be short-paid and comes straight out '
                              "of the lender's principal and interest payment [adTW0EyLeRk @ 00:13:11]. "
                              'Dan Deppen has owned loans where the borrower kept paying while the '
                              'servicer allocated every dollar to interest, late fees and lender advances, '
                              "with none of it reaching principal, which is why each payment's breakdown "
                              'has to be checked before it goes into the books [Wt2pat2PE2w @ 00:07:11]. '
                              "Rick at Paperstac warns that a servicer's loss mitigation pricing can hide "
                              'a point on the UPB when a loan reperforms, a fee that may be worth paying '
                              'if the servicer did the work, but not if the investor did the outreach and '
                              'the servicer collects at each hurdle [kXMfkHu1Tu0 @ 00:03:17]. Sohail flags '
                              'a late charge written as 5 percent of the total payment due: charging on '
                              'escrows just for being late puts the lender out of compliance and can land '
                              'them in court, so the charge has to run on principal and interest only '
                              '[uKK5_EVlvus @ 00:54:28]. Each leak looks small on one statement and only '
                              'surfaces when the investor actually reconciles.'],
               'table': {'caption': 'Firsthand traps reported by servicers and note investors, with the '
                                    'economics behind each',
                         'headers': ['Trap', 'Firsthand Detail', 'Economics Check', 'Expert Source'],
                         'rows': [['Reusing an attorney-drafted note as a closing template',
                                   'Many states are attorney review states, so every note and deed of '
                                   'trust needs fresh review',
                                   'Full closing package with attorney review runs about $350 to $400, '
                                   'usually charged to borrower',
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '00:12:13]); Note Investing & Seller Financing - JKP Holdings '
                                   '([uKK5_EVlvus @ 00:12:47])'],
                                  ['Default interest rate written into an owner-occupied note',
                                   'Servicer alerts the lender it cannot be enforced and leaves it out of '
                                   'boarding',
                                   'Business-to-business paper is the Wild West short of usury; homeowners '
                                   'win in court',
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '00:09:30]); Note Investing & Seller Financing - JKP Holdings '
                                   '([uKK5_EVlvus @ 00:10:08])'],
                                  ['Mandatory direct deposit clause in the financing terms',
                                   'Borrowers bouncing payments twice get pulled off online payments, '
                                   "forced to cashier's checks or Zelle",
                                   "Once the servicer removes direct deposit, the contract's own terms no "
                                   'longer match reality',
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   '00:25:35])'],
                                  ['Note ordering the servicer to pay the first lien immediately',
                                   'Payments need three to four business days to clear before anything '
                                   'gets disbursed downstream',
                                   'Provident rejected that note, and a check-paying borrower means a '
                                   "four-day wait at Scott Horne's desk",
                                   'Note Investing & Seller Financing - JKP Holdings ([uKK5_EVlvus @ '
                                   "00:42:45]); Scott Horne's Owner Finance Network ([adTW0EyLeRk @ "
                                   '00:09:42])'],
                                  ['Borrower mailing the check near the end of grace period',
                                   'Mailed on the 8th, received on the 11th, and the late charge has '
                                   'already hit',
                                   'Due on the first, late on the second, late charge starts on day 11',
                                   "Scott Horne's Owner Finance Network ([adTW0EyLeRk @ 00:08:29])"],
                                  ['Boarding at a servicer with cryptic notes and shaky footing',
                                   'Allied notes read S/W BORR with no content, and Allied got kicked out '
                                   'of Michigan and Pennsylvania',
                                   'Dan maintains a separate spreadsheet just to map Allied loan numbers '
                                   'back to borrowers',
                                   'Fusion Notes ([Wt2pat2PE2w @ 00:17:37]); Fusion Notes ([Wt2pat2PE2w @ '
                                   '00:18:34]); Fusion Notes ([Wt2pat2PE2w @ 00:16:58])'],
                                  ['Signing a servicing agreement without matching the fee schedule',
                                   'Most complaints Chris hears come from investors not understanding the '
                                   'terms of their agreement',
                                   'Few servicers work New York, shrinking choices from five to ten down '
                                   'to one or two',
                                   '7e Investments ([SZhJFIusBp4 @ 00:04:14]); 7e Investments '
                                   '([SZhJFIusBp4 @ 00:02:44])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill Or Reprice The Note Before It Boards',
                           'body': 'Every item below comes from a file a practitioner either walked away '
                                   'from, got rejected on, or had to clean up after. Run all four before '
                                   'money moves.',
                           'items': ['Pull the promissory note, notary block and recording proof first; a '
                                     'sub-one-page note, a blank notary block or an unrecorded contract '
                                     'for deed means walk or force a reclose [Note Investing & Seller '
                                     'Financing - JKP Holdings — uKK5_EVlvus @ 00:20:04].',
                                     'Read 12 to 24 months of pay history alongside the servicing notes; '
                                     'knock the price down for rolling 30s and price in heavy risk for '
                                     'rolling 60s [Paperstac — VkGqESM8fdY @ 00:06:38].',
                                     "Take payoff figures only from the lender directly or that lender's "
                                     'servicer directly, never from a third party, because payoff fraud '
                                     "happens out there every day [Scott Horne's Owner Finance Network — "
                                     'adTW0EyLeRk @ 00:16:51].',
                                     "Lay the servicer's fee schedule over the servicing agreement line by "
                                     'line so a 20 to 25 dollar quote does not quietly become 40 to 45 [7e '
                                     'Investments — SZhJFIusBp4 @ 00:03:22].']}}],
 'pull_quote': 'A servicer is kind of like the placeholder in football where they hold it for the kicker; '
               "they did their job as expected, but if they screw up then it's magnified to the extreme. "
               'Attributed to 7e Investments (SZhJFIusBp4 @ 00:02:11).',
 'diagram_id': 'diag-02',
 'action_checklist': ["Download and complete the investor side of the servicer's boarding package before "
                      'closing, then deliver the note, deed of trust, closing disclosure and ACH paperwork '
                      "right after signing [Scott Horne's Owner Finance Network — adTW0EyLeRk @ 00:01:08].",
                      'Have a doc-prep attorney review every note and deed of trust instead of reusing a '
                      'template, budgeting about $350 to $400 for a standard package and $600 to $700 for '
                      'a wrap, usually charged to the borrower [Note Investing & Seller Financing - JKP '
                      'Holdings — uKK5_EVlvus @ 00:12:47].',
                      'Interview servicers on which states they are licensed in before buying notes there, '
                      'since markets like New York leave only one or two servicers to choose from [7e '
                      'Investments — SZhJFIusBp4 @ 00:02:29].',
                      "Pull a servicer's published itemized fee menu covering boarding, deboarding, "
                      'bankruptcy, escrow, foreclosure and loss mit so every servicer interview is priced '
                      'against it [FIXnotes | Non-Performing Note Investing — 5H6jVWw2QK0 @ 00:02:56].',
                      "Pair the servicer's hello letter with one attorney letter that routes the borrower "
                      'to a web form or a call to your cell, then send the modification and ACH form the '
                      'same day so the loan is modified within about 30 days [FIXnotes | Non-Performing '
                      'Note Investing — 5H6jVWw2QK0 @ 00:01:11].',
                      'Put every borrower workout or loan modification in writing and send it to the '
                      'servicer so they can adjust terms and stop reporting the borrower late or pursuing '
                      "foreclosure [Scott Horne's Owner Finance Network — adTW0EyLeRk @ 00:20:31]."],
 'statutory_citations': [{'title': 'Note Investing & Seller Financing - JKP Holdings — Most Seller Finance '
                                   'Notes Are Legally Worthless | Sohail Badruddin [00:07:03]',
                          'url': 'https://www.youtube.com/watch?v=uKK5_EVlvus&t=423s',
                          'relevance': 'Primary practitioner testimony on servicers rejecting '
                                       'non-compliant seller-finance notes at boarding and the court-side '
                                       'fallout of bad paper.'},
                         {'title': "Scott Horne's Owner Finance Network — What is the Timeline and Process "
                                   'for Loan Servicing [00:09:56]',
                          'url': 'https://www.youtube.com/watch?v=adTW0EyLeRk&t=596s',
                          'relevance': 'Primary practitioner testimony on check clearing, the payment '
                                       'waterfall, escrow trust handling and default timelines.'},
                         {'title': 'Fusion Notes — How To Navigate Servicer Reports From Different Lender '
                                   'Portals [00:05:57]',
                          'url': 'https://www.youtube.com/watch?v=Wt2pat2PE2w&t=357s',
                          'relevance': 'Primary practitioner testimony on reading date paid versus date '
                                       'due, payment allocation and comparing servicer portals.'},
                         {'title': 'Paperstac — Mortgage Note Servicers - How to Pick Yours (Snackable) '
                                   '[00:00:47]',
                          'url': 'https://www.youtube.com/watch?v=kXMfkHu1Tu0&t=47s',
                          'relevance': 'Primary practitioner testimony on choosing a servicer by price, '
                                       'services offered and technology interface.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'nPRf3YuUI2o',
                       'title': 'Dodd Frank MLO Compensation Rule (Module 3) | NMLS SAFE MLO Exam Study '
                                'Series and Test Prep',
                       'channel': 'My Mortgage Trainer, Inc.',
                       'author': 'My Mortgage Trainer, Inc.',
                       'text': 'For any residential mortgage loan, no mortgage originator shall receive '
                               'from any person and no person shall pay to a mortgage originator, directly '
                               'or indirectly, compensation that varies based on the term of the loan '
                               'other than the amount of the principal.',
                       'tip': 'No mortgage originator shall receive compensation that varies based on the '
                              'term of the loan other than the amount of the principal.',
                       'timestamp': 35,
                       'timestamp_seconds': 35,
                       'timestamp_label': '[00:00:35]',
                       'url': 'https://www.youtube.com/watch?v=nPRf3YuUI2o&t=35s',
                       'markdown': '[00:00:35](https://www.youtube.com/watch?v=nPRf3YuUI2o&t=35s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '35EmXeZQAsY',
                       'title': 'Federal Mortgage Laws Explained: RESPA, TILA, ECOA & the SAFE Act',
                       'channel': 'Ameritrain Mortgage Institute',
                       'author': 'Ameritrain Mortgage Institute',
                       'text': "You can just call this the no surprises at the closing table act; it's all "
                               'about making sure borrowers see every settlement cost upfront, but just as '
                               'importantly, it completely outlaws kickbacks.',
                       'tip': 'RESPA completely outlaws kickbacks, meaning no more shady deals where '
                              'someone gets a secret fee just for sending business their way.',
                       'timestamp': 108,
                       'timestamp_seconds': 108,
                       'timestamp_label': '[00:01:48]',
                       'url': 'https://www.youtube.com/watch?v=35EmXeZQAsY&t=108s',
                       'markdown': '[00:01:48](https://www.youtube.com/watch?v=35EmXeZQAsY&t=108s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C1it2AZx0B4',
                       'title': 'Introduction to Dodd-Frank (Module 3) | NMLS SAFE MLO Exam Study Series '
                                'and Test Prep',
                       'channel': 'My Mortgage Trainer, Inc.',
                       'author': 'My Mortgage Trainer, Inc.',
                       'text': 'The bureau may take any action including prescribing rules to prevent a '
                               'covered person or a service provider from committing or engaging in an '
                               'unfair, deceptive or abusive act or practice.',
                       'tip': 'The CFPB can prescribe rules to stop a covered person or a service provider '
                              'from engaging in an unfair, deceptive or abusive act or practice.',
                       'timestamp': 189,
                       'timestamp_seconds': 189,
                       'timestamp_label': '[00:03:09]',
                       'url': 'https://www.youtube.com/watch?v=C1it2AZx0B4&t=189s',
                       'markdown': '[00:03:09](https://www.youtube.com/watch?v=C1it2AZx0B4&t=189s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rmcxN_JOvoY',
                       'title': 'Dodd Frank Loan Originator Compensation (Module 3) | NMLS SAFE MLO Exam '
                                'Study Series and Test Prep',
                       'channel': 'My Mortgage Trainer, Inc.',
                       'author': 'My Mortgage Trainer, Inc.',
                       'text': 'A safe harbor is provided to facilitate compliance with the anti-steering '
                               'prohibition; loan originators are deemed to comply if they present loan '
                               'options that offer the lowest interest rate and no risky features.',
                       'tip': 'Additionally, the rule provides a safe harbor for compliance with the '
                              'anti-steering prohibition.',
                       'timestamp': 174,
                       'timestamp_seconds': 174,
                       'timestamp_label': '[00:02:54]',
                       'url': 'https://www.youtube.com/watch?v=rmcxN_JOvoY&t=174s',
                       'markdown': '[00:02:54](https://www.youtube.com/watch?v=rmcxN_JOvoY&t=174s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'g-UjM12V8m0',
                       'title': "New Dodd Frank Mortgage Laws & What's In Store For Banks & Borrowers?",
                       'channel': 'Shari Olefson',
                       'author': 'Shari Olefson',
                       'text': 'Under Dodd-Frank, banks that make safe loans, which are called qualified '
                               'mortgages, will get protection against lawsuits, so banks are going to '
                               'want to make those safe loans.',
                       'tip': "Loans that don't meet the qualified mortgage criteria will be harder for "
                              'you to find and may cost you more money.',
                       'timestamp': 101,
                       'timestamp_seconds': 101,
                       'timestamp_label': '[00:01:41]',
                       'url': 'https://www.youtube.com/watch?v=g-UjM12V8m0&t=101s',
                       'markdown': '[00:01:41](https://www.youtube.com/watch?v=g-UjM12V8m0&t=101s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5H6jVWw2QK0',
                       'title': "The Beginner's Guide To Loan Servicing",
                       'channel': 'FIXnotes | Non-Performing Note Investing',
                       'author': 'FIXnotes | Non-Performing Note Investing',
                       'text': "30 bucks per month per loan, that's pretty standard; I've seen that as low "
                               "as $15 per loan per month when you're working with a real barebones "
                               'servicer.',
                       'tip': "If they're doing a lot more than just sending the statements, 30 bucks a "
                              'month is pretty reasonable.',
                       'timestamp': 246,
                       'timestamp_seconds': 246,
                       'timestamp_label': '[00:04:06]',
                       'url': 'https://www.youtube.com/watch?v=5H6jVWw2QK0&t=246s',
                       'markdown': '[00:04:06](https://www.youtube.com/watch?v=5H6jVWw2QK0&t=246s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SZhJFIusBp4',
                       'title': 'Selecting a Loan Servicer For Your Note Investing Business',
                       'channel': '7e Investments',
                       'author': '7e Investments',
                       'text': "Some of them tack on additional fees monthly, so what you think you're "
                               'paying, 20, 25 bucks, turns up to 40, 45 very, very quickly.',
                       'tip': 'Take that servicing agreement and read through it with their fee schedule.',
                       'timestamp': 202,
                       'timestamp_seconds': 202,
                       'timestamp_label': '[00:03:22]',
                       'url': 'https://www.youtube.com/watch?v=SZhJFIusBp4&t=202s',
                       'markdown': '[00:03:22](https://www.youtube.com/watch?v=SZhJFIusBp4&t=202s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'adTW0EyLeRk',
                       'title': 'What is the Timeline and Process for Loan Servicing',
                       'channel': "Scott Horne's Owner Finance Network",
                       'author': "Scott Horne's Owner Finance Network",
                       'text': 'Once the check has cleared, we will pay the underlying lien holder if '
                               "there's one, remove the escrow funds and hold them in a trust account, "
                               "then whatever's left we deduct our fee and forward the remainder to the "
                               'investor.',
                       'tip': "We wait four days; you want to make sure it's clear.",
                       'timestamp': 596,
                       'timestamp_seconds': 596,
                       'timestamp_label': '[00:09:56]',
                       'url': 'https://www.youtube.com/watch?v=adTW0EyLeRk&t=596s',
                       'markdown': '[00:09:56](https://www.youtube.com/watch?v=adTW0EyLeRk&t=596s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VkGqESM8fdY',
                       'title': 'How to Read Payment History on a Mortgage Note (Decode the Servicing '
                                'Notes)',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'I got the servicing notes, I started looking at the servicing notes, and '
                               'in the servicing notes it said, borrower willing to sign deed in lieu.',
                       'tip': 'Several references, borrower has paperwork for deed in lieu, and then '
                              'borrower went dark.',
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=VkGqESM8fdY&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=VkGqESM8fdY&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kXMfkHu1Tu0',
                       'title': 'Mortgage Note Servicers - How to Pick Yours (Snackable)',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': "Don't just look at what's my monthly; look at the details page, because if "
                               "they get a loan reperforming, sometimes it's one point, you're going to "
                               'pay a point on the UPB.',
                       'tip': "You're going to pay a point on the UPB.",
                       'timestamp': 197,
                       'timestamp_seconds': 197,
                       'timestamp_label': '[00:03:17]',
                       'url': 'https://www.youtube.com/watch?v=kXMfkHu1Tu0&t=197s',
                       'markdown': '[00:03:17](https://www.youtube.com/watch?v=kXMfkHu1Tu0&t=197s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uKK5_EVlvus',
                       'title': 'Most Seller Finance Notes Are Legally Worthless | Sohail Badruddin',
                       'channel': 'Note Investing & Seller Financing - JKP Holdings',
                       'author': 'Note Investing & Seller Financing - JKP Holdings',
                       'text': 'Those are the ones we will reject or ask the lender to reclose the loan '
                               "taking our suggestions; the ones who won't, we can't onboard because it "
                               'throws us out of compliance.',
                       'tip': 'It could potentially become a reputational risk for us, because if the '
                              "borrower ends up in foreclosure they'll just sue everybody involved.",
                       'timestamp': 464,
                       'timestamp_seconds': 464,
                       'timestamp_label': '[00:07:44]',
                       'url': 'https://www.youtube.com/watch?v=uKK5_EVlvus&t=464s',
                       'markdown': '[00:07:44](https://www.youtube.com/watch?v=uKK5_EVlvus&t=464s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uKK5_EVlvus',
                       'title': 'Most Seller Finance Notes Are Legally Worthless | Sohail Badruddin',
                       'channel': 'Note Investing & Seller Financing - JKP Holdings',
                       'author': 'Note Investing & Seller Financing - JKP Holdings',
                       'text': 'It could be as bad as nullifying the contract along with a rescission '
                               "where you're paying back everything the borrower had paid to you, for five "
                               'years for example.',
                       'tip': 'Best case scenario, it could be just as simple as getting it corrected and '
                              'then going back to court.',
                       'timestamp': 820,
                       'timestamp_seconds': 820,
                       'timestamp_label': '[00:13:40]',
                       'url': 'https://www.youtube.com/watch?v=uKK5_EVlvus&t=820s',
                       'markdown': '[00:13:40](https://www.youtube.com/watch?v=uKK5_EVlvus&t=820s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'epnA26NInuc',
                       'title': 'What Is a Seller-Financed Note? The 5 Steps Explained',
                       'channel': 'Loan Note Exchange',
                       'author': 'Loan Note Exchange',
                       'text': 'Some note holders do this themselves, others hire a loan servicing company '
                               'to handle it; either way, a clean payment record is one of the most '
                               'valuable things a note holder can have.',
                       'tip': 'A clean payment record is one of the most valuable things a note holder can '
                              'have.',
                       'timestamp': 217,
                       'timestamp_seconds': 217,
                       'timestamp_label': '[00:03:37]',
                       'url': 'https://www.youtube.com/watch?v=epnA26NInuc&t=217s',
                       'markdown': '[00:03:37](https://www.youtube.com/watch?v=epnA26NInuc&t=217s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5IxbTVhJdr8',
                       'title': 'Passing the NMLS Exam - THE SAFE ACT REGULATION  - POP QUIZ',
                       'channel': 'Affinity Real Estate & Mortgage Training',
                       'author': 'Affinity Real Estate & Mortgage Training',
                       'text': "The rule is you cannot have a felony unless it's been pardoned within the "
                               'last seven years.',
                       'tip': 'A felony assault from 10 years ago would not automatically disqualify an '
                              'applicant for a mortgage loan originator license.',
                       'timestamp': 203,
                       'timestamp_seconds': 203,
                       'timestamp_label': '[00:03:23]',
                       'url': 'https://www.youtube.com/watch?v=5IxbTVhJdr8&t=203s',
                       'markdown': '[00:03:23](https://www.youtube.com/watch?v=5IxbTVhJdr8&t=203s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xZohXlsFnks',
                       'title': 'SAFE Act - Part 2 (Free Tutorial)',
                       'channel': 'National Mortgage Exam',
                       'author': 'National Mortgage Exam',
                       'text': 'You and your company need your NMLS ID on the loan application, on the '
                               'note and on the mortgage or deed of trust.',
                       'tip': 'NMLS identifier requirements: your NMLS ID goes on the loan application, '
                              'the note and the mortgage or deed of trust.',
                       'timestamp': 1350,
                       'timestamp_seconds': 1350,
                       'timestamp_label': '[00:22:30]',
                       'url': 'https://www.youtube.com/watch?v=xZohXlsFnks&t=1350s',
                       'markdown': '[00:22:30](https://www.youtube.com/watch?v=xZohXlsFnks&t=1350s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5VZzJLRM1kI',
                       'title': 'Non QM Mortgage Loan Explained | 3 Ways Self Employed Borrowers Can '
                                'Qualify',
                       'channel': 'Dani Rudd',
                       'author': 'Dani Rudd',
                       'text': "There's no mortgage insurance, so even if you're on a program that's "
                               'putting as little as 10% down on a non-QM product, there is no PMI.',
                       'tip': 'Their interest rates are very competitive and in most cases recently '
                              "they're often pricing better than qualified mortgages.",
                       'timestamp': 247,
                       'timestamp_seconds': 247,
                       'timestamp_label': '[00:04:07]',
                       'url': 'https://www.youtube.com/watch?v=5VZzJLRM1kI&t=247s',
                       'markdown': '[00:04:07](https://www.youtube.com/watch?v=5VZzJLRM1kI&t=247s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Wt2pat2PE2w',
                       'title': 'How To Navigate Servicer Reports From Different Lender Portals',
                       'channel': 'Fusion Notes',
                       'author': 'Fusion Notes',
                       'text': "I've had loans where the borrower was making payments, but the loan "
                               'servicer was allocating all of those funds to interest, late fees, maybe '
                               'lender advances, and actually none of it was going to principal.',
                       'tip': 'Look at the breakdown for each payment that comes in and how the pieces of '
                              'that payment were allocated.',
                       'timestamp': 431,
                       'timestamp_seconds': 431,
                       'timestamp_label': '[00:07:11]',
                       'url': 'https://www.youtube.com/watch?v=Wt2pat2PE2w&t=431s',
                       'markdown': '[00:07:11](https://www.youtube.com/watch?v=Wt2pat2PE2w&t=431s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
