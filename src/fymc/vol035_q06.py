from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'due-on-sale-clause-law-exceptions-practitioner-workarounds',
 'question_prompt': 'What does the due-on-sale clause actually allow lenders to do, what exceptions exist, '
                    'and how do operators structure around it?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'The Due-on-Sale Clause: Law, Exceptions, and Practitioner Workarounds',
 'subtitle': 'Loan acceleration mechanics, Garn-St. Germain exceptions, land trusts and LLC transfers, '
             'deed-back and lease-option fallbacks, myth-busting live sessions, and what happens when a '
             'lender invokes the clause',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners agree the due-on-sale clause is a lender right that is rarely '
                      'exercised. Pace Morby puts calls at roughly one in 500 houses, the Investor Army '
                      'Podcast guest reports fewer than ten across fifteen thousand owner-financed '
                      'mortgages, and William Tingle reports 24 plus years without one. The real triggers '
                      'are operational, not the recorded deed: botched insurance, missed payments, bad '
                      'paperwork, a deed moved too fast after a foreclosure reinstatement, small local '
                      'banks, and angry sellers or ex-spouses. Street mechanics include a 10 to 15 day '
                      'post-reinstatement wait, Westar servicing at $27 a month, due-on-sale insurance '
                      'near 1% of price, and a deed-back-plus-agreement-for-sale cure inside a 30 to 35 '
                      'day letter window. The sharpest split is land trusts: Clint Coons builds subject-to '
                      'deals around them, while Morby says a land trust does not stop the clause.',
 'key_metrics': [{'label': 'Due-on-sale call frequency',
                  'metric': 'Due-on-sale call frequency',
                  'value': 'About 1 out of 500 houses',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Morby's estimate of how often the clause gets called on subject-to deals, "
                             'including deals using land trusts and other strategies.',
                  'source': 'Pace Morby ([cOTyo3LTDPk @ 00:00:12])'},
                 {'label': 'Due-on-sale insurance cost',
                  'metric': 'Due-on-sale insurance cost',
                  'value': 'About 1% of purchase price ($4,000 on a $400,000 home)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Coverage whose provider will fix a called clause or refinance the house out '
                             'with its own money; many operators skip it because of cost.',
                  'source': 'Pace Morby ([cOTyo3LTDPk @ 00:01:54])'},
                 {'label': 'Post-reinstatement cooling-off wait',
                  'metric': 'Post-reinstatement cooling-off wait',
                  'value': '10 to 15 days after the loan is reinstated',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Wait after catching up a foreclosure before closing escrow; transferring the '
                             "deed 3 days into reinstatement is Morby's most common cause of a call.",
                  'source': 'Pace Morby ([cOTyo3LTDPk @ 00:03:27])'},
                 {'label': 'Acceleration notice cure window',
                  'metric': 'Acceleration notice cure window',
                  'value': '30 days to pay the full balance',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Window found in every clause reviewed across private, Fannie Mae, Freddie '
                             'Mac, FHA, and VA loans; lenders usually also offer a 30-day title-back '
                             'option.',
                  'source': 'In Rem Podcast ([d9fjKwIC-VE @ 00:00:41])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus: Rare Calls, Known Triggers, Clean Cures',
               'paragraphs': ['Every operator here agrees on the baseline: the due-on-sale clause is real, '
                              'it lives in the note or deed of trust, and it gives the lender a right, not '
                              'an obligation, to accelerate the loan when ownership moves. Pace Morby '
                              'states flatly that he has had it called on him multiple times and that '
                              'anyone claiming it never happens has not been doing subject-to long enough, '
                              'yet he pegs the rate at roughly one out of every 500 houses [cOTyo3LTDPk @ '
                              '00:00:12]. Ken McElroy frames it as a right but not the obligation and '
                              'traces its origin to the 1980s, when rates near 18% sat against 4% loans '
                              'and wraps were everywhere [ulx_sqYnYVA @ 00:00:00]. The Investor Army '
                              'Podcast guest says subject-to triggers the clause rather than violates it, '
                              'notes it sits in about 98 percent of deeds of trust, and reports fewer than '
                              'ten calls across fifteen thousand owner-financed mortgages and 75 million '
                              'originated [WFGzQCgPP54 @ 00:02:26]. William Tingle adds 24 plus years '
                              'without a single loan called, conditioned on on-time payments and proper '
                              'insurance [ccfeK6C6SeI @ 00:01:15]. The consensus is not that the risk is '
                              'zero; it is that the risk is small, predictable, and driven by operator '
                              'sloppiness.',
                              'The second point of agreement is what actually wakes a lender up, and it is '
                              'almost never the recorded deed itself. Morby says that most of the time the '
                              'bank never notices, that even when it notices it does not care, and that '
                              'the real triggers are transferring insurance incorrectly or stopping '
                              'payments [cOTyo3LTDPk @ 00:01:35]. Clint Coons lands in the same place from '
                              'the asset-protection side: unpaid taxes, missed payments, or no insurance '
                              "are what draw the lender's eye, and red flags like an out-of-state address "
                              'or an uninsured property should be avoided [nS_9Os_42MQ @ 00:06:30]. In his '
                              'longer breakdown, Morby ranks the top five ways banks find out: a small '
                              'local bank plus redeeming a foreclosure at the wrong time, improper '
                              'insurance, a missed payment, incorrect paperwork, and an angry seller or '
                              'ex-spouse [KXUHeABJyeY @ 00:42:38]. The Investor Army guest names wrong '
                              'insurance as the main cause behind their handful of calls and flags small '
                              'banks such as Colonial Savings, which called five houses, as riskier than '
                              'Wells Fargo or Bank of America [WFGzQCgPP54 @ 00:10:11]. Morby also '
                              'stresses that banks are not notified when the county recorder records a '
                              'deed, because they bundle and sell loans rather than watch titles.',
                              'The third consensus is that a called clause is a paperwork problem with a '
                              'long fuse, not a seizure. Coons says there is no credit damage and no jail, '
                              "and that the lender's ask is either refinance, pay off, or put title back "
                              "into the borrower's name [nS_9Os_42MQ @ 00:07:02]. The In Rem Podcast "
                              'reviewer says every clause they have read, across private, Fannie Mae, '
                              'Freddie Mac, FHA, and VA paper, carries a notice of acceleration with 30 '
                              'days to pay the full balance, and that lenders usually also offer the '
                              "option to put title back in the seller's name within 30 days [d9fjKwIC-VE @ "
                              "00:01:43]. Morby's demand letter gives 35 days, carries no fine, and when "
                              'the buyer calls the bank the issue is resolved 90%+ of the time, with the '
                              'servicing simply synced [W60Ytz4Wb5U @ 00:16:54]. Even when a lender pushes '
                              'past the letter, Morby says acceleration runs through foreclosure, which '
                              'takes three to 12 months depending on the state, and a judicial foreclosure '
                              'costs a bank $30,000 to $50,000 and dents its ratings and warehouse lines '
                              '[dMDfltvY39k @ 00:36:23]. Karla Kyte adds the statutory floor: in death and '
                              'divorce, lenders have to honor the transfer.'],
               'table': {'caption': 'Where the operators line up on due-on-sale risk',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Call frequency is low but nonzero across a large deal count',
                                   'Roughly one out of 500 houses get called, land trusts included',
                                   'Budget for at least one call across any long-held subject-to portfolio',
                                   'Pace Morby ([cOTyo3LTDPk @ 00:00:12])'],
                                  ['Insurance errors are the single most cited lender trigger',
                                   'Fewer than ten calls across fifteen thousand owner-financed mortgages, '
                                   'mainly wrong insurance',
                                   'Set named insured, additional insured, and mortgagee positions '
                                   'correctly at closing',
                                   'Investor Army Podcast ([WFGzQCgPP54 @ 00:02:26])'],
                                  ['Missed payments and unpaid taxes draw attention faster than any deed',
                                   'Unpaid taxes, missed payments, or no insurance are the real triggers',
                                   'Automate payments and taxes so the loan never shows any distress',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([nS_9Os_42MQ @ '
                                   '00:06:30])'],
                                  ['The clause is a lender right, never a lender obligation',
                                   'Right but not the obligation, born from the 1980s 18% versus 4% rate '
                                   'gap',
                                   'Expect enforcement pressure mainly when legacy loan rates sit far '
                                   'below market',
                                   'Ken McElroy ([ulx_sqYnYVA @ 00:00:00])'],
                                  ['A called loan arrives as a letter with a cure window',
                                   'Every clause reviewed gives 30 days to pay the full balance',
                                   'Line up refinance, sale, or restructure moves before the 30 days lapse',
                                   'In Rem Podcast ([d9fjKwIC-VE @ 00:00:41])'],
                                  ['Banks are not watching county recorder filings for deed transfers',
                                   'Recorder offices do not notify banks; the Wells Fargo scraping rumor '
                                   'was a hoax',
                                   'Treat course pitches built on recorder-scraping fear as sales '
                                   'boogeymen',
                                   'Pace Morby ([KXUHeABJyeY @ 00:18:44])'],
                                  ['Clean operators report long careers without a single loan called',
                                   '24 plus years with no loan called, given on-time payments and proper '
                                   'insurance',
                                   'Discipline on payments and insurance matters more than clever title '
                                   'structures',
                                   'William Tingle ([ccfeK6C6SeI @ 00:01:15])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The first mechanic every Morby student learns is timing around a '
                              'foreclosure reinstatement, because that is where most of his own calls came '
                              'from. The typical case: the seller is in foreclosure, he catches up the '
                              'payments, the deed transfers three days later during reinstatement, and the '
                              'bank calls the clause; the fix is to wait 10 to 15 days after the loan is '
                              'reinstated before closing escrow [cOTyo3LTDPk @ 00:03:27]. On the Lost '
                              'Dutchman deal, where the deed moved a day after redemption with a small '
                              'local bank, he tightened that into a cooling-off period of at least five to '
                              'ten days while holding the physical warranty deed for about 30 days before '
                              'recording [KXUHeABJyeY @ 00:43:27]. Insurance is the second build. Morby '
                              'gets a second policy a week before close with the seller as loss payee, and '
                              'a broker notifies the bank about 30 days after close [dMDfltvY39k @ '
                              '00:33:30]. The Investor Army guest gives the exact stack: on a rental, the '
                              'investor is named insured, the seller additional insured, and the lender '
                              'mortgagee; on a wrap, the end buyer is named insured, the seller additional '
                              'insured, the lender primary mortgagee, and the investor secondary mortgagee '
                              '[WFGzQCgPP54 @ 00:04:00].',
                              'Payments and paperwork are the third and fourth triggers, and Morby '
                              'automates both. He routes payments through Westar servicing at $27 a month, '
                              'which makes five payments covering principal, interest, taxes, insurance, '
                              'and seller equity [dMDfltvY39k @ 00:31:29]. His sub2 purchase agreement '
                              'carries about 19 disclosures, including continued liability and a '
                              'due-on-sale plan, followed by a TC plus escrow or a closing attorney; the '
                              'deed is one page and costs $17, and skipping title insurance is called lazy '
                              'and irresponsible [W60Ytz4Wb5U @ 00:11:42]. For a backstop, due-on-sale '
                              'insurance runs about 1% of purchase price, roughly $4,000 on a $400,000 '
                              'home, and the provider will fix it or refinance the house out with its own '
                              'money [cOTyo3LTDPk @ 00:01:54]. Many operators skip the coverage because of '
                              'cost. Morby is also part-owner of Equity Assurance, which negotiates with '
                              'the bank and, if that fails, refinances with the exact same terms and earns '
                              'the interest [4krb0pqCMC8 @ 00:00:57]. The seller contract also includes a '
                              '$50,000 fine if the seller goes to the bank, aimed at the angry-seller '
                              "trigger, and Morby's team says it spent $40,000 to $50,000 over six to "
                              'seven years drafting documents it revises every three to six months.',
                              'When the letter lands, the execution sequence is consistent. Step one is '
                              'the phone: per Morby, the buyer calls the bank and more than 90% of the '
                              'time it is perfectly fine; otherwise the fallback is an executory contract '
                              'and/or a lease option or land lease [W60Ytz4Wb5U @ 00:17:25]. At Johnston '
                              "Johnson Bank he reached the president, the founder's son, who suggested "
                              'deeding the property back to the owner and buying on an agreement for sale; '
                              'Morby then wrote an Arizona agreement for sale, recorded it at the county '
                              'recorder, and says all five times the paperwork was simply rearranged '
                              '[cOTyo3LTDPk @ 00:04:24]. The In Rem Podcast lays out the same restructure: '
                              'a warranty deed from buyer back to seller, then either an agreement for '
                              'sale where payments mirror the existing loan and the buyer holds equitable '
                              'interest and possession, or a long-term lease with option to purchase, with '
                              'Garn-St. Germain allowing leases up to three years [d9fjKwIC-VE @ '
                              '00:05:12]. Option two is selling to a third party within 30 days; option '
                              'three is a refinance, caveated by current rates. Morby holds the '
                              'executory-contract deed unrecorded in a safety deposit box that needs both '
                              'parties to sign off, with a three-day notice on breach [dMDfltvY39k @ '
                              '00:40:40].'],
               'table': {'caption': 'Street mechanics, tools, and unit economics on due-on-sale exposure',
                         'headers': ['Mechanic', 'Exact Number or Tool', 'How It Is Run', 'Expert Source'],
                         'rows': [['Reinstatement cooling-off before transferring the deed',
                                   'Wait 10 to 15 days after the loan is reinstated',
                                   'Catch up the payments, let the loan reinstate, then close escrow',
                                   'Pace Morby ([cOTyo3LTDPk @ 00:03:27])'],
                                  ['Third-party payment servicing to kill missed payments',
                                   'Westar servicing at $27 per month making five payments',
                                   'Servicer pays principal, interest, taxes, insurance, and seller equity '
                                   'every month',
                                   'Pace Morby ([dMDfltvY39k @ 00:31:29])'],
                                  ['Due-on-sale insurance as a paid backstop',
                                   'About 1% of price, roughly $4,000 on a $400,000 home',
                                   'Provider fixes the call or refinances the house out with its own money',
                                   'Pace Morby ([cOTyo3LTDPk @ 00:01:54])'],
                                  ['Land trust title layout with seller as initial trustee',
                                   "Trustee's deed held unrecorded plus recorded notice of interest",
                                   'Seller resigns as trustee, buyer steps in as successor, power of '
                                   'attorney covers utilities',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([0hSERgZotJM @ '
                                   '00:06:36])'],
                                  ['Land trust lease-option deal with four separate paydays',
                                   '$1,800 rent less $1,400 mortgage nets $400 monthly',
                                   'Add a $5,000 option fee and $75,000 exercise spread for about $90,000 '
                                   'total',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([0hSERgZotJM @ '
                                   '00:11:50])'],
                                  ['Sandwich lease option layered on a controlled property',
                                   'Pay $2,000 rent with $2,500 fee, sublease $2,400 with $7,500 fee',
                                   'Nets $400 per month plus $5,000 upfront on the spread',
                                   'Pace Morby ([dMDfltvY39k @ 01:32:25])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the operators do that most subject-to buyers miss',
                           'body': 'Four moves that keep the lender asleep or turn a called clause into a '
                                   'routine paperwork swap.',
                           'items': ['Never notify the bank: there is no due-on-sale department, phone '
                                     'support is mostly overseas virtual assistants, and on the Whitman '
                                     'deal Morby spent a 4-hour round trip calling the bank trying to get '
                                     'the clause called and could not [Pace Morby — dMDfltvY39k @ '
                                     '01:56:03]',
                                     'On LLC transfers, match LLC ownership and percentages to the deed; '
                                     'Fannie Mae exempts transfers to a borrower-controlled LLC on loans '
                                     'from June 1st, 2016 onward, and Freddie Mac requires the original '
                                     'borrower to be managing member [Ken McElroy — ulx_sqYnYVA @ '
                                     '00:04:01]',
                                     'When the lender mails a letter asking you to verify ownership, '
                                     'answer it with the LLC operating agreement or the land trust '
                                     'agreement rather than ignoring it [Clint Coons Esq. | Real Estate '
                                     'Asset Protection — nS_9Os_42MQ @ 00:04:29]',
                                     'In a divorce, the spouse awarded the home should send the lender the '
                                     'separation agreement and lock in full account access; the lender '
                                     'cannot call the loan or force a refinance because in death and '
                                     'divorce they have to honor it [My Divorce Mortgage Planning with '
                                     'Karla Kyte, CDLP — DANV_9GW0PU @ 00:05:49]']},
               'sop_steps': [{'step': 1,
                              'title': 'Script the seller and disclose up front',
                              'action': 'Raise the due-on-sale clause proactively and paper it in the '
                                        'purchase agreement.',
                              'detail': "Morby's seller script uses a groceries analogy and brings up the "
                                        'clause before the seller does, and his sub2 purchase agreement '
                                        'carries about 19 disclosures including continued liability and a '
                                        'due-on-sale plan [Pace Morby — RZpKVqqUZPQ @ 00:00:20]'},
                             {'step': 2,
                              'title': 'Time the deed and stack the insurance',
                              'action': 'Hold the deed transfer until the reinstated loan cools off and '
                                        'set insurance before close.',
                              'detail': 'Wait 10 to 15 days after reinstatement before closing, and get a '
                                        'second policy a week before close with the seller as loss payee '
                                        'so a broker can notify the bank about 30 days after close [Pace '
                                        'Morby — dMDfltvY39k @ 00:26:41]'},
                             {'step': 3,
                              'title': 'Automate payments and close clean',
                              'action': 'Route the loan through a servicer and buy title insurance on '
                                        'every deal.',
                              'detail': 'Use Westar servicing at $27 a month for the five payments, record '
                                        'the one-page $17 deed, and always buy title insurance, since '
                                        'skipping it is lazy and irresponsible [Pace Morby — W60Ytz4Wb5U @ '
                                        '00:11:42]'},
                             {'step': 4,
                              'title': 'Run the cure sequence on a demand letter',
                              'action': 'Call the bank first, then restructure, sell, or refinance inside '
                                        'the 30-day window.',
                              'detail': 'Deed back to the seller and re-buy on an agreement for sale or a '
                                        'long-term lease with option, or sell to a third party within 30 '
                                        'days and pay off, or refinance if rates allow [In Rem Podcast — '
                                        'd9fjKwIC-VE @ 00:02:42]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on the street is whether a land trust shields a '
                              'subject-to deal. Clint Coons now structures acquisitions through a land '
                              "trust with the investor's LLC as beneficiary, puts the seller on title as "
                              "initial trustee so the record reads 'Tom as trustee,' then has Tom resign "
                              'so the buyer steps in as undisclosed successor trustee, arguing that nobody '
                              'sees the trustee because the trust is not a public document [0hSERgZotJM @ '
                              '00:05:06]. Pace Morby calls that theory a myth: a land trust hides who the '
                              'new owner is but does not change the fact that the deed moved to a new '
                              'entity, beneficiaries stay visible in Arizona, and half of the called loans '
                              'Morby hears about were bought in land trusts [KXUHeABJyeY @ 00:29:41]. The '
                              'Garn-St Germain camp narrows the argument further: Brooke and Dan read the '
                              '1982 act as protecting a transfer into a revocable inter vivos trust only '
                              'when the property is under five units and the borrower stays beneficiary '
                              '[l81_UM-dG9Y @ 00:02:38], while Joe Seagull says that exception is gone '
                              "once the property is out of the borrower's name and the borrower has moved "
                              'out, and flatly refuses to extend it to second homes or investment property '
                              '[yd3L18YPXDU @ 00:02:04].',
                              'Practitioners also split on how often the clause actually fires and how '
                              "hard it bites. Pace Morby's own numbers drift across appearances, from "
                              'roughly one in 500 deals to four out of about 700 to ten calls with one '
                              'active, and the takeaway Morby pushes is that the clause is a boogeyman '
                              'that is easy to solve [dMDfltvY39k @ 00:15:02]. William Tingle goes '
                              'further, reporting 24-plus years with no loan called as long as payments '
                              'land on time and insurance is set up properly [ccfeK6C6SeI @ 00:01:15]. Joe '
                              'Seagull runs the opposite read: legacy loans at 2 to 3 percent sitting '
                              'against 6 to 7 percent money give lenders a reason to call notes and '
                              'relend, and while judges may stall out of sympathy, the lender ultimately '
                              'gets its non-monetary foreclosure [yd3L18YPXDU @ 00:02:24]. UpCounsel '
                              'frames the consequence as immediate full repayment or foreclosure, whereas '
                              'Morby counters that acceleration runs through a foreclosure process that '
                              'takes three to 12 months depending on the state, which is the cure window '
                              "operators actually work inside [KXUHeABJyeY @ 00:16:41]. Morby's own answer "
                              'to whether an operator should worry is a flat yes, with the worry dial '
                              'pinned at level 10 only for the uninformed.',
                              'The LLC question and the fallback-clause question draw a third line. Ken '
                              'McElroy tells investors not to fear moving property into an LLC, citing '
                              "Fannie Mae's exemption for transfers to a borrower-controlled LLC on loans "
                              "from June 1st, 2016, Freddie Mac's requirement that the original borrower "
                              'be managing member, and the tactic of matching LLC ownership and '
                              'percentages to the deed [ulx_sqYnYVA @ 00:04:01]. Clint Coons has moved the '
                              'other way on subject-to deals, no longer deeding to an LLC because it reads '
                              'as a red flag if the lender pulls title, a reversal Coons ties directly to '
                              'higher interest rates [0hSERgZotJM @ 00:01:46]. Pace Morby goes the '
                              'opposite direction from silence on paperwork, loading a sub2 purchase '
                              'agreement with about 19 disclosures that spell out continued liability and '
                              'a due-on-sale plan, and Morby insists the clause is something to bring up '
                              'with the seller even when the seller does not care [W60Ytz4Wb5U @ '
                              '00:08:09]. William Tingle refuses to write a deed-back or lease-option '
                              'fallback clause into the contract at all, because it unsettles sellers who '
                              'want certainty [ccfeK6C6SeI @ 00:00:04]. The In Rem Podcast lands closer to '
                              'Morby, laying out restructure, sale, or refinance as the three paths once a '
                              '30-day acceleration notice arrives.'],
               'table': {'caption': 'Contested playbooks on the due-on-sale clause, side by side',
                         'headers': ['Contested Question',
                                     'Practitioner Position A',
                                     'Practitioner Position B',
                                     'Expert Source'],
                         'rows': [['Does a land trust shield a subject-to transfer from the lender?',
                                   'Coons titles the deal in a land trust, seller as initial trustee, then '
                                   'the seller resigns to an undisclosed successor trustee.',
                                   'Morby says a land trust only hides the owner, and half of the called '
                                   'loans Morby hears about used one.',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([0hSERgZotJM @ '
                                   '00:05:06]); Pace Morby ([KXUHeABJyeY @ 00:31:46])'],
                                  ['How far does the Garn-St Germain trust exception actually reach?',
                                   'Brooke and Dan: revocable inter vivos trust, under five units, with '
                                   'the borrower remaining the beneficiary.',
                                   'Seagull: no cover for second homes or investment property, and once '
                                   'the borrower moves out the exception is gone.',
                                   'High Yield Real Estate Investing ([l81_UM-dG9Y @ 00:02:38]); '
                                   'TrustThisTV ([yd3L18YPXDU @ 00:01:39])'],
                                  ['Is deeding the property into an LLC safe from acceleration?',
                                   'McElroy cites the Fannie Mae borrower-controlled LLC exemption for '
                                   'loans from June 1st, 2016 onward.',
                                   'Coons no longer deeds subject-to deals to an LLC because it is a red '
                                   'flag on a title pull.',
                                   'Ken McElroy ([ulx_sqYnYVA @ 00:04:01]); Clint Coons Esq. | Real Estate '
                                   'Asset Protection ([0hSERgZotJM @ 00:01:46])'],
                                  ['How often do lenders actually call the loan due?',
                                   'Morby reports four out of about 700 deals; Tingle reports 24-plus '
                                   'years with no loan called.',
                                   'Seagull says more lenders are calling loans because 2 to 3 percent '
                                   'notes sit against 6 to 7 percent money.',
                                   'Pace Morby ([RZpKVqqUZPQ @ 00:01:04]); William Tingle ([ccfeK6C6SeI @ '
                                   '00:01:15]); TrustThisTV ([yd3L18YPXDU @ 00:02:24])'],
                                  ['How fast does the consequence land once the clause is called?',
                                   'UpCounsel frames the outcome as immediate full repayment or a '
                                   'foreclosure on the property.',
                                   'Morby says acceleration runs through foreclosure taking three to 12 '
                                   'months depending on the state.',
                                   'UpCounsel ([o5_cemzYC-w @ 00:01:31]); Pace Morby ([KXUHeABJyeY @ '
                                   '00:16:41])'],
                                  ['Should a deed-back fallback clause go into the seller contract?',
                                   'Tingle refuses the deed-back or lease-option clause because it '
                                   'unsettles sellers who want certainty.',
                                   'Morby loads about 19 disclosures into the sub2 agreement, including '
                                   'continued liability and a due-on-sale plan.',
                                   'William Tingle ([ccfeK6C6SeI @ 00:00:04]); Pace Morby ([W60Ytz4Wb5U @ '
                                   '00:08:09])'],
                                  ['What is the first move after the acceleration letter arrives?',
                                   'Morby has the buyer call the bank, which is perfectly fine 90-plus '
                                   'percent of the time once servicing syncs.',
                                   'In Rem goes straight to restructure via deed back plus agreement for '
                                   'sale or long lease, sale, or refinance.',
                                   'Pace Morby ([W60Ytz4Wb5U @ 00:16:54]); In Rem Podcast ([d9fjKwIC-VE @ '
                                   '00:02:42])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most repeated firsthand failure is closing too fast after curing a '
                              "foreclosure. Pace Morby's typical call came when a seller was in "
                              'foreclosure, the payments were caught up, and the deed transferred three '
                              'days later during reinstatement, which tripped the clause; the fix Morby '
                              'now runs is to wait 10 to 15 days after the loan is reinstated before '
                              'closing escrow [cOTyo3LTDPk @ 00:03:13]. On the Lost Dutchman deal the deed '
                              'moved a day after redemption at a small local bank, and the corrected '
                              'sequence is to redeem, sit through a cooling-off period of at least five to '
                              'ten days, and hold the physical warranty deed for about 30 days before '
                              "recording [KXUHeABJyeY @ 00:42:38]. Bank size is the second trap. Morby's "
                              'line that banks are way too big to care breaks down at the small end, where '
                              'very small banks may notice transfers on their own, and the Investor Army '
                              'guest names Colonial Savings with five houses called while rating Wells '
                              'Fargo and Bank of America fine [WFGzQCgPP54 @ 00:10:11]. When Morby reached '
                              "the president of a small bank, the founder's son, the cure was to deed the "
                              'property back and re-buy on a recorded Arizona agreement for sale '
                              '[cOTyo3LTDPk @ 00:04:24].',
                              'Insurance is the trigger every camp names. The Investor Army guest, with '
                              'fifteen thousand owner-financed mortgages and fewer than ten called, pins '
                              'the main cause on wrong insurance and spells out the fix: on a rental the '
                              'investor is named insured, the seller additional insured, and the lender '
                              'mortgagee, while on a wrap the end buyer becomes named insured and the '
                              'investor slides to secondary mortgagee [WFGzQCgPP54 @ 00:04:00]. Pace '
                              "Morby's version is a second policy bound a week before close with the "
                              'seller as loss payee, then a broker notifies the bank about 30 days after '
                              'closing [dMDfltvY39k @ 00:33:30]. Missed payments are the next landmine, '
                              'and Morby pays Westar $27 a month to push five separate payments covering '
                              'principal, interest, taxes, insurance, and seller equity so nothing slips. '
                              'Clint Coons lists unpaid taxes, missed payments, and no insurance as the '
                              'real triggers, and recounts a borrower who moved 14 rentals into 14 LLCs, '
                              "got caught by the insurer's spot check, and was told to retitle with an "
                              'ability to cure [nS_9Os_42MQ @ 00:07:47]. Morby adds incorrect paperwork to '
                              "the list, including roughly 10 setup steps such as redirecting the lender's "
                              'mail [KXUHeABJyeY @ 00:55:00].',
                              "The last class of failures comes from people, not paperwork. Pace Morby's "
                              'fifth trigger is an angry seller or ex-spouse: on a Chandler deal of '
                              'roughly $350,000, the ex-wife was still on the mortgage while the husband '
                              'held the deed alone, her attorney threatened, and attorney Sean Sinclair '
                              "had to resolve it, and Morby's seller contract now carries a $50,000 fine "
                              'if the seller goes to the bank [KXUHeABJyeY @ 00:51:27]. Karla Kyte sees '
                              'the divorce trap from the other side, with a client paying the mortgage '
                              'without account access because the ex-husband never granted it, and pushes '
                              'access terms into the separation agreement [DANV_9GW0PU @ 00:03:54]. The '
                              'affidavit trap is sharper. Clint Coons has an active client being asked to '
                              'attest the seller still resides in a property titled in an LLC, and Joe '
                              'Seagull warns that a false affidavit is wire fraud if emailed and bank '
                              'fraud because it goes to a federally regulated lender [yd3L18YPXDU @ '
                              '00:03:48]. Run the economics before signing anything: due-on-sale insurance '
                              'runs about 1 percent of price, roughly $4,000 on a $400,000 home, and the '
                              "refinance exit carries today's rates, which is the caveat the In Rem "
                              'Podcast attaches to its third option [d9fjKwIC-VE @ 00:07:27].'],
               'table': {'caption': 'Firsthand due-on-sale failure modes and the fixes practitioners now '
                                    'run',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Fix or Economics Check',
                                     'Expert Source'],
                         'rows': [['Deed recorded too soon after a foreclosure reinstatement',
                                   'Payments caught up, deed transferred three days later during '
                                   'reinstatement, and the bank called the loan.',
                                   'Wait 10 to 15 days after the loan is reinstated before closing escrow '
                                   'on the deal.',
                                   'Pace Morby ([cOTyo3LTDPk @ 00:03:27])'],
                                  ['Small local bank watching its own book closely',
                                   'Lost Dutchman deed moved one day after redemption at a small local '
                                   'bank and drew the call.',
                                   'Redeem, sit a five to ten day cooling-off period, and hold the '
                                   'warranty deed about 30 days.',
                                   'Pace Morby ([KXUHeABJyeY @ 00:42:38]); Investor Army Podcast '
                                   '([WFGzQCgPP54 @ 00:10:11])'],
                                  ['Insurance transferred or structured the wrong way',
                                   'Wrong insurance is the main cause behind fewer than ten calls across '
                                   'fifteen thousand mortgages.',
                                   'Investor named insured, seller additional insured, lender mortgagee; '
                                   'on wraps the end buyer is named insured.',
                                   'Investor Army Podcast ([WFGzQCgPP54 @ 00:04:00]); Pace Morby '
                                   '([dMDfltvY39k @ 00:33:30])'],
                                  ['Missed payments, unpaid taxes, or entity retitling spotted',
                                   "A borrower moved 14 rentals into 14 LLCs and the insurer's spot check "
                                   'forced a retitle.',
                                   'Use Westar servicing at $27 a month to push five payments, and keep '
                                   'taxes and insurance current.',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([nS_9Os_42MQ @ '
                                   '00:07:47]); Pace Morby ([dMDfltvY39k @ 00:31:29])'],
                                  ['Angry seller or ex-spouse goes to the bank',
                                   'Chandler deal near $350,000: ex-wife still on the mortgage, her '
                                   'attorney threatened, attorney stepped in.',
                                   'Seller contract carries a $50,000 fine if the seller contacts the bank '
                                   'about the deal.',
                                   'Pace Morby ([KXUHeABJyeY @ 00:51:27]); Pace Morby ([KXUHeABJyeY @ '
                                   '00:47:48])'],
                                  ['Signing a false residency affidavit for the lender',
                                   'An active Coons client is being asked to attest the seller still lives '
                                   'in an LLC-titled house.',
                                   'Seagull warns a false affidavit is wire fraud if emailed and bank '
                                   'fraud to a federal lender.',
                                   'Clint Coons Esq. | Real Estate Asset Protection ([nS_9Os_42MQ @ '
                                   '00:04:57]); TrustThisTV ([yd3L18YPXDU @ 00:03:48])'],
                                  ['Counting on a land trust as the only protection',
                                   'Morby reports a dozen students were still called while holding '
                                   'properties in land trusts.',
                                   'Morby uses a land trust only in Texas as a last resort where executory '
                                   'contracts are hard.',
                                   'Pace Morby ([W60Ytz4Wb5U @ 00:17:48]); Pace Morby ([W60Ytz4Wb5U @ '
                                   '00:18:21])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Close Kill Switch',
                           'body': 'Every item below is a trigger that practitioners watched fire on live '
                                   'deals. Clear all four before the deed moves.',
                           'items': ['Reinstatement timing cleared: no deed transfer until 10 to 15 days '
                                     'after the loan is reinstated, with the physical warranty deed held '
                                     'about 30 days on small-bank loans [Pace Morby — cOTyo3LTDPk @ '
                                     '00:03:27].',
                                     'Insurance structure verified: investor named insured, seller '
                                     'additional insured, lender mortgagee, and on wraps the end buyer '
                                     'named insured with the investor as secondary mortgagee [Investor '
                                     'Army Podcast — WFGzQCgPP54 @ 00:04:00].',
                                     'No false paperwork to the lender: a false affidavit emailed to a '
                                     'federally regulated lender is wire fraud and bank fraud [TrustThisTV '
                                     '— yd3L18YPXDU @ 00:03:48].',
                                     'Seller and ex-spouse risk mapped: confirm who is on the mortgage '
                                     'versus the deed, because an angry ex-spouse on the loan is a '
                                     'top-five trigger [Pace Morby — KXUHeABJyeY @ 00:51:27].']}}],
 'pull_quote': '"So essentially what you have is you have 3 to 12 months to solve the do on sale clause, '
               'which is the easiest thing on planet Earth to solve." — attributed to Pace Morby '
               '(dMDfltvY39k @ 01:38:00).',
 'diagram_id': 'diag-02',
 'action_checklist': ["Catch up the seller's payments, then wait 10 to 15 days after the loan is "
                      'reinstated before closing escrow [Pace Morby — cOTyo3LTDPk @ 00:03:27].',
                      'Set insurance with the investor as named insured, the seller as additional insured, '
                      'and the lender as mortgagee before close [Investor Army Podcast — WFGzQCgPP54 @ '
                      '00:04:00].',
                      'Route payments through Westar servicing at $27 a month so principal, interest, '
                      'taxes, insurance, and seller equity never slip [Pace Morby — dMDfltvY39k @ '
                      '00:31:29].',
                      'When the demand letter lands, have the buyer call the bank first, which is '
                      'perfectly fine 90-plus percent of the time once servicing syncs [Pace Morby — '
                      'W60Ytz4Wb5U @ 00:16:54].',
                      'If the bank will not sync, deed back to the seller and re-buy on a recorded '
                      'agreement for sale or a long-term lease with option [In Rem Podcast — d9fjKwIC-VE @ '
                      '00:03:00].',
                      'On a divorce award, notify the lender with the agreement and lock account access '
                      'into the separation agreement [My Divorce Mortgage Planning with Karla Kyte, CDLP — '
                      'DANV_9GW0PU @ 00:03:19].'],
 'statutory_citations': [{'title': 'Pace Morby — Busting the Biggest Myth in Creative Finance (Due on Sale '
                                   'Clause) [00:15:02]',
                          'url': 'https://www.youtube.com/watch?v=dMDfltvY39k&t=902s',
                          'relevance': 'Primary practitioner testimony on due-on-sale frequency, triggers, '
                                       'the 35-day letter, and the bank call-back cure.'},
                         {'title': 'In Rem Podcast — What if your lender invokes the due on sale clause '
                                   'following a Subject To Transaction? [00:02:42]',
                          'url': 'https://www.youtube.com/watch?v=d9fjKwIC-VE&t=162s',
                          'relevance': 'Primary practitioner testimony on the restructure, sell, and '
                                       'refinance options after a 30-day acceleration notice.'},
                         {'title': 'TrustThisTV — Exceptions to the Due on Sale Clause & the Garn-St. '
                                   'Germain Act [00:03:48]',
                          'url': 'https://www.youtube.com/watch?v=yd3L18YPXDU&t=228s',
                          'relevance': 'Primary practitioner testimony on Garn-St Germain scope, rising '
                                       'lender calls, and the false-affidavit fraud trap.'},
                         {'title': 'Clint Coons Esq. | Real Estate Asset Protection — How To Overcome The '
                                   'Due On Sale Clause On A Subject To Deal [00:05:06]',
                          'url': 'https://www.youtube.com/watch?v=0hSERgZotJM&t=306s',
                          'relevance': 'Primary practitioner testimony on the land trust successor-trustee '
                                       'structure and the LLC red-flag reversal.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'cOTyo3LTDPk',
                       'title': 'Overcoming The Due On Sale Clause In Subject To',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': 'So, what we typically do is we catch up the payments, and then we wait '
                               'about 10 to 15 days after the loan is reinstated to then close escrow, and '
                               "then you don't have that problem.",
                       'tip': 'So, what we typically do is we catch up the payments, and then we wait '
                              'about 10 to 15 days after the loan is reinstated to then close escrow, and '
                              "then you don't have that problem.",
                       'timestamp': 207,
                       'timestamp_seconds': 207,
                       'timestamp_label': '[00:03:27]',
                       'url': 'https://www.youtube.com/watch?v=cOTyo3LTDPk&t=207s',
                       'markdown': '[00:03:27](https://www.youtube.com/watch?v=cOTyo3LTDPk&t=207s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nS_9Os_42MQ',
                       'title': 'Due On Sale Clause and How To AVOID It (Real Estate Investments!)',
                       'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'author': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'text': "What's going to happen is you're going to be asked to either refi or pay "
                               'off the loan if they discover it.',
                       'tip': "What's going to happen is you're going to be asked to either refi or pay "
                              'off the loan if they discover it.',
                       'timestamp': 422,
                       'timestamp_seconds': 422,
                       'timestamp_label': '[00:07:02]',
                       'url': 'https://www.youtube.com/watch?v=nS_9Os_42MQ&t=422s',
                       'markdown': '[00:07:02](https://www.youtube.com/watch?v=nS_9Os_42MQ&t=422s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o5_cemzYC-w',
                       'title': 'Due on Sale Clauses  What Property Owners Need to Know',
                       'channel': 'UpCounsel',
                       'author': 'UpCounsel',
                       'text': 'This protects lenders from being stuck with below market interest rates '
                               'when property ownership changes.',
                       'tip': 'This protects lenders from being stuck with below market interest rates '
                              'when property ownership changes.',
                       'timestamp': 16,
                       'timestamp_seconds': 16,
                       'timestamp_label': '[00:00:16]',
                       'url': 'https://www.youtube.com/watch?v=o5_cemzYC-w&t=16s',
                       'markdown': '[00:00:16](https://www.youtube.com/watch?v=o5_cemzYC-w&t=16s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yd3L18YPXDU',
                       'title': 'Exceptions to the Due on Sale Clause & the Garn-St. Germain Act',
                       'channel': 'TrustThisTV',
                       'author': 'TrustThisTV',
                       'text': 'A false affidavit is wire fraud if it is emailed, and it is bank fraud '
                               'because it goes to a federally regulated lender.',
                       'tip': 'A false affidavit is wire fraud if it is emailed, and it is bank fraud '
                              'because it goes to a federally regulated lender.',
                       'timestamp': 228,
                       'timestamp_seconds': 228,
                       'timestamp_label': '[00:03:48]',
                       'url': 'https://www.youtube.com/watch?v=yd3L18YPXDU&t=228s',
                       'markdown': '[00:03:48](https://www.youtube.com/watch?v=yd3L18YPXDU&t=228s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'W60Ytz4Wb5U',
                       'title': 'Should You Be Worried About the Due on Sale Clause?',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': 'The buyer calls the bank, and more than 90 percent of the time it is '
                               'perfectly fine and the servicing gets synced.',
                       'tip': 'The buyer calls the bank, and more than 90 percent of the time it is '
                              'perfectly fine and the servicing gets synced.',
                       'timestamp': 1014,
                       'timestamp_seconds': 1014,
                       'timestamp_label': '[00:16:54]',
                       'url': 'https://www.youtube.com/watch?v=W60Ytz4Wb5U&t=1014s',
                       'markdown': '[00:16:54](https://www.youtube.com/watch?v=W60Ytz4Wb5U&t=1014s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DANV_9GW0PU',
                       'title': 'Protect Your Rights | Garn-St Germain Act',
                       'channel': 'My Divorce Mortgage Planning with Karla Kyte, CDLP',
                       'author': 'My Divorce Mortgage Planning with Karla Kyte, CDLP',
                       'text': "Don't keep it a secret, because the lender can't call the note due because "
                               'of the divorce.',
                       'tip': "Don't keep it a secret, because the lender can't call the note due because "
                              'of the divorce.',
                       'timestamp': 199,
                       'timestamp_seconds': 199,
                       'timestamp_label': '[00:03:19]',
                       'url': 'https://www.youtube.com/watch?v=DANV_9GW0PU&t=199s',
                       'markdown': '[00:03:19](https://www.youtube.com/watch?v=DANV_9GW0PU&t=199s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dMDfltvY39k',
                       'title': 'Busting the Biggest Myth in Creative Finance (Due on Sale Clause)',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': "The do on sale clause is such a boogeyman, it's unfreaking believable.",
                       'tip': "The do on sale clause is such a boogeyman, it's unfreaking believable.",
                       'timestamp': 902,
                       'timestamp_seconds': 902,
                       'timestamp_label': '[00:15:02]',
                       'url': 'https://www.youtube.com/watch?v=dMDfltvY39k&t=902s',
                       'markdown': '[00:15:02](https://www.youtube.com/watch?v=dMDfltvY39k&t=902s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dMDfltvY39k',
                       'title': 'Busting the Biggest Myth in Creative Finance (Due on Sale Clause)',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': 'A land trust does not stop the do on sale clause.',
                       'tip': 'A land trust does not stop the do on sale clause.',
                       'timestamp': 6634,
                       'timestamp_seconds': 6634,
                       'timestamp_label': '[01:50:34]',
                       'url': 'https://www.youtube.com/watch?v=dMDfltvY39k&t=6634s',
                       'markdown': '[01:50:34](https://www.youtube.com/watch?v=dMDfltvY39k&t=6634s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'd9fjKwIC-VE',
                       'title': 'What if your lender invokes the due on sale clause following a Subject To '
                                'Transaction?',
                       'channel': 'In Rem Podcast',
                       'author': 'In Rem Podcast',
                       'text': 'The first option is to restructure, with the buyer deeding the property '
                               'back to the seller by warranty deed and then buying on an agreement for '
                               'sale or a long-term lease with an option to purchase.',
                       'tip': 'The first option is to restructure, with the buyer deeding the property '
                              'back to the seller by warranty deed and then buying on an agreement for '
                              'sale or a long-term lease with an option to purchase.',
                       'timestamp': 162,
                       'timestamp_seconds': 162,
                       'timestamp_label': '[00:02:42]',
                       'url': 'https://www.youtube.com/watch?v=d9fjKwIC-VE&t=162s',
                       'markdown': '[00:02:42](https://www.youtube.com/watch?v=d9fjKwIC-VE&t=162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0hSERgZotJM',
                       'title': 'How To Overcome The Due On Sale Clause On A Subject To Deal',
                       'channel': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'author': 'Clint Coons Esq. | Real Estate Asset Protection',
                       'text': "No one sees the fact that I'm actually the trustee of this of this trust, "
                               'because that trust is not a public document.',
                       'tip': "No one sees the fact that I'm actually the trustee of this of this trust, "
                              'because that trust is not a public document.',
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=0hSERgZotJM&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=0hSERgZotJM&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ulx_sqYnYVA',
                       'title': "Transferring Property to an LLC: Don't Fear the Due On Sale Clause",
                       'channel': 'Ken McElroy',
                       'author': 'Ken McElroy',
                       'text': 'So simply transferring it into an LLC that I own that has the same '
                               'ownership as this property is less of a concern to the lender.',
                       'tip': 'So simply transferring it into an LLC that I own that has the same '
                              'ownership as this property is less of a concern to the lender.',
                       'timestamp': 213,
                       'timestamp_seconds': 213,
                       'timestamp_label': '[00:03:33]',
                       'url': 'https://www.youtube.com/watch?v=ulx_sqYnYVA&t=213s',
                       'markdown': '[00:03:33](https://www.youtube.com/watch?v=ulx_sqYnYVA&t=213s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RZpKVqqUZPQ',
                       'title': 'What is a Due on Sale Clause | What you Need to Know',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': 'The due on sale clause has been called four times out of probably 700 '
                               'deals.',
                       'tip': 'The due on sale clause has been called four times out of probably 700 '
                              'deals.',
                       'timestamp': 64,
                       'timestamp_seconds': 64,
                       'timestamp_label': '[00:01:04]',
                       'url': 'https://www.youtube.com/watch?v=RZpKVqqUZPQ&t=64s',
                       'markdown': '[00:01:04](https://www.youtube.com/watch?v=RZpKVqqUZPQ&t=64s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WFGzQCgPP54',
                       'title': 'Subject To Investing and How To Avoid the Due on Sale Clause',
                       'channel': 'Investor Army Podcast',
                       'author': 'Investor Army Podcast',
                       'text': 'Out of fifteen thousand owner-financed mortgages, fewer than ten have been '
                               'called, and the main cause is wrong insurance.',
                       'tip': 'Out of fifteen thousand owner-financed mortgages, fewer than ten have been '
                              'called, and the main cause is wrong insurance.',
                       'timestamp': 146,
                       'timestamp_seconds': 146,
                       'timestamp_label': '[00:02:26]',
                       'url': 'https://www.youtube.com/watch?v=WFGzQCgPP54&t=146s',
                       'markdown': '[00:02:26](https://www.youtube.com/watch?v=WFGzQCgPP54&t=146s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ccfeK6C6SeI',
                       'title': "Why the Due on Sale Clause Doesn't Keep Me Up at Night!",
                       'channel': 'William Tingle',
                       'author': 'William Tingle',
                       'text': 'In 24 plus years no loan has been called, as long as the payments are made '
                               'on time and the insurance is set up properly.',
                       'tip': 'In 24 plus years no loan has been called, as long as the payments are made '
                              'on time and the insurance is set up properly.',
                       'timestamp': 75,
                       'timestamp_seconds': 75,
                       'timestamp_label': '[00:01:15]',
                       'url': 'https://www.youtube.com/watch?v=ccfeK6C6SeI&t=75s',
                       'markdown': '[00:01:15](https://www.youtube.com/watch?v=ccfeK6C6SeI&t=75s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4krb0pqCMC8',
                       'title': 'How To Handle A Due On Sale Clause',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': 'Equity Assurance negotiates with the bank, and if that fails it refinances '
                               'the loan with the exact same terms and earns the interest.',
                       'tip': 'Equity Assurance negotiates with the bank, and if that fails it refinances '
                              'the loan with the exact same terms and earns the interest.',
                       'timestamp': 57,
                       'timestamp_seconds': 57,
                       'timestamp_label': '[00:00:57]',
                       'url': 'https://www.youtube.com/watch?v=4krb0pqCMC8&t=57s',
                       'markdown': '[00:00:57](https://www.youtube.com/watch?v=4krb0pqCMC8&t=57s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KXUHeABJyeY',
                       'title': '07-18-21 | Due On Sale Clause In Subject To',
                       'channel': 'Pace Morby',
                       'author': 'Pace Morby',
                       'text': "A land trust hides who the new owner is but it doesn't mean that the deed "
                               'did not transfer to a new entity.',
                       'tip': "A land trust hides who the new owner is but it doesn't mean that the deed "
                              'did not transfer to a new entity.',
                       'timestamp': 1781,
                       'timestamp_seconds': 1781,
                       'timestamp_label': '[00:29:41]',
                       'url': 'https://www.youtube.com/watch?v=KXUHeABJyeY&t=1781s',
                       'markdown': '[00:29:41](https://www.youtube.com/watch?v=KXUHeABJyeY&t=1781s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l81_UM-dG9Y',
                       'title': 'Garn St.Germain Act',
                       'channel': 'High Yield Real Estate Investing',
                       'author': 'High Yield Real Estate Investing',
                       'text': 'The Saint-Germain Act allowed property owners to transfer title of their '
                               'property into an inter vivos trust without triggering the due on sale '
                               'clause of their mortgage.',
                       'tip': 'The Saint-Germain Act allowed property owners to transfer title of their '
                              'property into an inter vivos trust without triggering the due on sale '
                              'clause of their mortgage.',
                       'timestamp': 143,
                       'timestamp_seconds': 143,
                       'timestamp_label': '[00:02:23]',
                       'url': 'https://www.youtube.com/watch?v=l81_UM-dG9Y&t=143s',
                       'markdown': '[00:02:23](https://www.youtube.com/watch?v=l81_UM-dG9Y&t=143s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
