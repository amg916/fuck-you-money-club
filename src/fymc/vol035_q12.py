from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'note-exits-liquidity-partials-sales-funding-marketplaces',
 'question_prompt': 'How do I sell, partial out, fund, and trade notes, including notes I create from my '
                    'own seller-financed or wrapped deals?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Note Exits and Liquidity: Partials, Sales, Funding, and Marketplaces',
 'subtitle': 'Selling partials, selling a note after one payment, pricing a note for sale, buying notes '
             'with no money, five creative funding sources, hypothecation with local banks, turning a '
             'rental into a note, Paperstac listings and trading, note arbitrage, and first-deal mistakes',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Note holders exit through three doors: a full sale, a partial sale of the next '
                      'block of payments, or borrowing against the paper. Fred and Tracy Rewey, Cal Ewing, '
                      'and the Paperstac operators agree the partial is the sharpest lever. It lets a '
                      'holder raise cash at 10-13% investor yields while keeping the tail, and the '
                      'buy-full, sell-front-partial play can recover nearly all capital. Seasoning drives '
                      'price: Moxxie buys after one payment, but 6-12 months moves offers and 24+ is '
                      'stronger. Bank-like paper fetches 95-98% of principal versus 90%-70% for '
                      'seller-finance notes. Marketplaces bundle listing, escrow, collateral audit, timed '
                      'auctions, and an AI price predictor. Disagreements center on leverage: Justin '
                      'Roberts hypothecates notes with local banks at about 80%, the JKP host doubts a 10x '
                      'leverage claim, and Paperstac calls partials on wraps potentially sticky.',
 'key_metrics': [{'label': 'Rewey partial buyer yield',
                  'metric': 'Rewey partial buyer yield',
                  'value': '13.3% on the next 96 of 176 payments bought for $47,615',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Partial carved from an $86,900 note at 9.5%; the seller is owed $47,249 when '
                             'the note reassigns.',
                  'source': 'Paperstac ([UwiEQOh84Y4 @ 00:17:14])'},
                 {'label': 'Cal Ewing partial investor IRR',
                  'metric': 'Cal Ewing partial investor IRR',
                  'value': '10.48%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'An IRA investor paid 55,000 for the next 120 payments on a Laredo-area '
                             'mobile-home note while Cal kept the tail, valued at 95,402 at full term.',
                  'source': 'Cal Ewing ([LCY-eZOK6gw @ 00:09:51])'},
                 {'label': 'Seller-finance note sale price vs bank-like paper',
                  'metric': 'Seller-finance note sale price vs bank-like paper',
                  'value': '90%-70% of principal vs 95-98% for bank-like loans',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Pricing spread between owner-financed notes and loans that resemble a '
                             'traditional bank mortgage.',
                  'source': 'Texas Capital Finance ([w4PRGbUrreA @ 00:08:46])'},
                 {'label': 'Paperstac price predictor accuracy',
                  'metric': 'Paperstac price predictor accuracy',
                  'value': 'Within about 2% on sales of $30K or more',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Model retrained monthly on about 40 data points and used internally for '
                             '2.5-3 years before launch.',
                  'source': 'Paperstac ([zhg1k-uMJM0 @ 00:15:26])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Across the Paperstac, Rewey, and Cal Ewing camps, the partial is the '
                              'default liquidity lever for a performing note. Instead of dumping the whole '
                              'asset, the holder sells a defined block of upcoming payments and keeps the '
                              'tail. Paperstac frames it as buying, say, 100 of 360 payments. The seller '
                              'steps back in if the borrower defaults, and only certain servicers are set '
                              'up to handle the split [XRyBErGyKgQ @ 00:06:24]. Fred and Tracy Rewey run '
                              'the classic version on an $86,900 note at 9.5%. An investor buys the next '
                              '96 of 176 payments for $47,615 at a 13.3% yield, and the seller is owed '
                              '$47,249 when the note reassigns. Partial size is dictated by how much cash '
                              'the seller actually needs [UwiEQOh84Y4 @ 00:17:14]. Cal Ewing used the same '
                              'move on a Laredo-area mobile-home note when a private lender needed repair '
                              'cash. Cal sold the next 120 payments to an IRA investor for 55,000 while '
                              'keeping a 130-plus payment tail valued at 95,402 at full term [LCY-eZOK6gw '
                              '@ 00:09:12]. Texas Capital Finance lists full and partial sales as the two '
                              'exit types and says partials often command a higher price. That gives '
                              'holders a reason to price both before letting go of the whole income stream '
                              '[w4PRGbUrreA @ 00:02:30].',
                              'The exit price is set long before the sale, at origination and through '
                              "seasoning. Moxxie's senior note analyst Dawn says a note can technically "
                              'sell the day after it is created, and Moxxie will buy once the first '
                              "payment lands. Even so, six to 12 months of consistent payments 'can make a "
                              "real difference' and 24 months or more is stronger. With zero history, "
                              'pricing has to lean on borrower credit, down payment and structure alone '
                              "[usXnfzN3Wmc @ 00:01:02]. Cherif Medawar's buy-side checklist mirrors that: "
                              '6 months to a year of on-time payments, a real cash down payment, credit '
                              "actually run, and collateral comps. Medawar's reason is that borrowers with "
                              'no skin in the game walk away [bhfdMe7Dpwk @ 00:06:55]. Texas Capital '
                              'Finance puts the spread in numbers. Bank-like loans sell for 95-98% of '
                              'principal while seller-finance notes sell between 90% and 70%, and the '
                              'closer the paper resembles a traditional bank mortgage, the higher the '
                              'price [w4PRGbUrreA @ 00:08:46]. Sierra Davis adds the hard floor on '
                              "paperwork: 'If the paperwork is not good, you can't forclose on it.' A "
                              'broken chain of assignment or a missing promissory note kills value no '
                              'matter how clean the pay history looks [XsNZ5SQXdCI @ 00:16:34].',
                              'On the full-sale side, the consensus venue is the online marketplace that '
                              'bundles listing with closing. Rick Allen and Brett Berkkey of Paperstac, on '
                              "Patrick Franz's show, describe the platform as 'MLS plus the title "
                              "company.' Some deals sold 'in the first hour' and a pool of Colorado land "
                              'notes went the same day, while listings that sit 30 days without an update '
                              'expire [y6ljJ3T0eNg @ 00:33:07]. The Paperstac listing walkthrough tells '
                              'sellers to pre-load files, a recent BPO and pay history, because buyers '
                              'will ask for them anyway. Sellers then pick flexible, firm or make-an-offer '
                              'pricing and write a description that tells the story [chL0454K1Zs @ '
                              "00:01:09]. The relaunch team warns that mispriced assets 'go to die,' and "
                              'the platform now runs a price predictor retrained monthly on about 40 data '
                              "points [zhg1k-uMJM0 @ 00:16:15]. Paperstac's first-deal mistakes episode "
                              "drives home the back-office rule that protects every future exit: 'Record "
                              "your assignments and record your deeds.' Unrecorded paper knocks buyers out "
                              'of the chain of title. In their examples, one buyer surfaced three years '
                              'later and tax notices arrived 18 months after a sale [MkofIE1Xq0o @ '
                              '00:14:43].'],
               'table': {'caption': 'Where the note-exit practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Partials are the go-to liquidity lever for performing notes',
                                   'Investor buys the next 96 of 176 payments for $47,615 at 13.3% yield',
                                   'Seller raises cash and still holds the reassigned back-end payments',
                                   'Paperstac ([UwiEQOh84Y4 @ 00:17:14])'],
                                  ["Partial size is driven by the seller's actual cash need",
                                   'The Reweys set the number of payments sold by what the seller needs',
                                   'Size the payment block to the lump sum the holder actually needs',
                                   'Paperstac ([UwiEQOh84Y4 @ 00:18:02])'],
                                  ['Experienced sellers act as a motivated default backstop for buyers',
                                   'Partial buyers get an already-performing loan and a seller who steps '
                                   'in on default',
                                   'Partials suit buyers with limited capital who want an active backstop',
                                   'Paperstac ([XRyBErGyKgQ @ 00:07:37])'],
                                  ['Seasoning materially lifts the offer price on a note sale',
                                   'Moxxie buys after the first payment; 6-12 months helps and 24+ months '
                                   'is stronger',
                                   "Clean on-time history lowers perceived risk and raises the buyer's "
                                   'offer',
                                   'Moxxie Education - Seller Financing & Notes ([usXnfzN3Wmc @ '
                                   '00:01:02])'],
                                  ['Bank-like paper commands the highest exit price in the market',
                                   'Bank-like loans sell at 95-98% of principal, seller-finance notes at '
                                   '90%-70%',
                                   'The closer the note resembles a bank mortgage, the higher the price '
                                   'paid',
                                   'Texas Capital Finance ([w4PRGbUrreA @ 00:08:46])'],
                                  ['Paperwork must support a foreclosure or the note loses value',
                                   'Promissory note present, unbroken chain of assignment, and a '
                                   'business-use affidavit are required',
                                   'Broken paperwork means no foreclosure remedy, and buyers price that in',
                                   'Agent2Investor Podcast ([XsNZ5SQXdCI @ 00:16:53])'],
                                  ['Record every assignment and deed before you try to resell',
                                   'Unrecorded paper drops buyers out of the chain of title years after '
                                   'closing',
                                   'Recording protects the next exit and avoids chasing wound-down fund '
                                   'sellers',
                                   'Paperstac ([MkofIE1Xq0o @ 00:14:54])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The most-repeated street play is to buy the whole note, sell a front '
                              'partial that recovers the cost, and keep the tail for close to nothing. The '
                              "Reweys' Dallas deal is the template. They bought a $54,000 note at 11.5% "
                              'for $47,500, then sold the next 279 payments for $51,000 to an investor '
                              'earning 11.7%. They netted $3,500 at closing and kept 79 payments, which '
                              'paid out when the loan cleared after 18 years [UwiEQOh84Y4 @ 00:28:05]. On '
                              'their base deal, selling 144 of 176 payments for the full $68,430 purchase '
                              "price left 32 payments of about $800 with an 'infinite' return. Paperstac's "
                              'funding episode runs the non-performing version: buy at $35,000 on a '
                              '$55,000-60,000 UPB, reperform it, and sell a partial for $34,000. The buyer '
                              "then sits on a $1,000 basis plus the tail. In Eddie Speed's '$100 model,' "
                              "$100 stays in as the IRS 'substantial investment' [_BvWeumu2WI @ 00:02:01]. "
                              "Inside a self-directed IRA the same move was described as 'bought it for "
                              "30... sold it for 30 100,' keeping $15,000-16,000 tax-free. Josh Andrews "
                              'pre-sells partials before buying [XRyBErGyKgQ @ 00:13:59].',
                              'The paperwork has to spell out what happens when the stream breaks early. '
                              "The Reweys' rule is that on payoff each party receives the present value of "
                              'its share. That can be calculated either on yield, which they favor when '
                              'selling, or as present value at the note rate, and servicing stays where it '
                              'already is [UwiEQOh84Y4 @ 00:20:16]. Cal Ewing modeled three 36-month '
                              'outcomes on the Laredo partial. On payoff, the investor has collected '
                              '26,217 and takes 41,900 more, for 68,000 total and a 13,017 profit, while '
                              'Cal gets about 20,600 [LCY-eZOK6gw @ 00:12:50]. At a Texas non-judicial '
                              'auction, a 105,000 bid less a 5,000 attorney fee against 62,500 owed '
                              'produces the same 41,900 and 20,600 split, with the surplus going to the '
                              "borrower. In an REO, the investor's interest converts to a present-value "
                              'claim. ARV of 130,000 less 20,000 in costs nets 110,000. The investor takes '
                              '41,900 plus 10,215, described as 15% of the net, for 52,115, and Cal keeps '
                              '57,885 [LCY-eZOK6gw @ 00:19:21]. Paperstac notes that FCI is among the '
                              'servicers that handle partials, and who pays servicing on default depends '
                              'on the agreement [XRyBErGyKgQ @ 00:11:22].',
                              'When the holder wants cash without giving up ownership at all, Justin '
                              'Roberts borrows against the paper instead. Roberts got about $80,000 '
                              'against a roughly $100,000 note, plus a portfolio loan on 24 notes for '
                              "about $2 million priced 'a little bit under prime.' Roberts also warns not "
                              "to bank on 80% from day one [b-4NVMQ1GZ8 @ 00:20:09]. Paperstac's wrap play "
                              'turns a rental into sellable paper. A property bought in 2015, owing '
                              '$80,000 and worth $230,000-240,000, sells at $240,000 with $30,000 down on '
                              'a $210,000 note at 8.5-9% over 30 years. After six months of seasoning the '
                              'note sells for $180,000-190,000, and Paperstac pays off the $80,000 '
                              'underlying lien before releasing funds [5bOm5hdSRXc @ 00:08:58]. On the '
                              'closing side, 88-90% of Paperstac buyers use escrow plus collateral audit '
                              'and sign a disbursement agreement only after reviewing the audit. The '
                              'platform pays for FedEx two-day shipping so files land in 3-5 days, instead '
                              'of a buyer wiring $50,000 and waiting 30 days [y6ljJ3T0eNg @ 00:43:47]. The '
                              'relaunched site adds timed auctions of 1 to 30 days. Winning means being '
                              "'awarded' the asset, followed by a 14-day due diligence window [zhg1k-uMJM0 "
                              '@ 00:04:54].'],
               'table': {'caption': 'Exit mechanics with the exact numbers practitioners stated',
                         'headers': ['Mechanic',
                                     'Exact Numbers Stated',
                                     'Execution Detail',
                                     'Expert Source'],
                         'rows': [['Buy the full note, then sell a front partial (Dallas deal)',
                                   '$54,000 note at 11.5% bought for $47,500; next 279 payments sold for '
                                   '$51,000',
                                   'Investor earns 11.7%; the Reweys net $3,500 and keep 79 tail payments',
                                   'Paperstac ([UwiEQOh84Y4 @ 00:28:05])'],
                                  ['Reperform a non-performer, then sell a partial',
                                   'Bought at $35,000 on $55,000-60,000 UPB; partial sold for $34,000',
                                   'Keep a $1,000 basis plus the tail; the $100 model leaves $100 in',
                                   'Paperstac ([_BvWeumu2WI @ 00:02:01])'],
                                  ['Partial sold to take out a private lender',
                                   '120 payments sold for 55,000; investor IRR of 10.48% with 32,291 '
                                   'profit',
                                   'Tail worth 95,402 at full term stays with Cal Ewing as owner',
                                   'Cal Ewing ([LCY-eZOK6gw @ 00:09:51])'],
                                  ['Hypothecating notes with small local banks',
                                   'About $80,000 on a $100,000 note; 24 notes collateralized for about '
                                   '$2M',
                                   'Portfolio loan priced a little bit under prime, backed by personal '
                                   'guarantees',
                                   'Note Investing & Seller Financing - JKP Holdings ([b-4NVMQ1GZ8 @ '
                                   '00:20:09])'],
                                  ['Converting a mortgaged rental into a wrap note',
                                   '$210,000 note at 8.5-9%, seasoned 6 months, sold for $180,000-190,000',
                                   'Paperstac pays off the $80,000 underlying lien, then releases the '
                                   "seller's funds",
                                   'Paperstac ([5bOm5hdSRXc @ 00:08:58])'],
                                  ['Marketplace escrow plus collateral audit at closing',
                                   '88-90% of buyers use escrow and audit; files arrive in 3-5 days',
                                   'Buyer signs the disbursement agreement only after reviewing the audit '
                                   'results',
                                   'Patrick Franz ([y6ljJ3T0eNg @ 00:43:47])'],
                                  ['Timed auctions and the AI price predictor',
                                   'Auctions run 1 to 30 days; predictor within about 2% on $30K+ sales',
                                   'Auction winner is awarded the asset, then gets a 14-day due diligence '
                                   'period',
                                   'Paperstac ([zhg1k-uMJM0 @ 00:15:26])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Partial Structuring Edges From the Desk',
                           'body': 'Small structuring moves the practitioners use to squeeze yield, '
                                   'protect the tail, and time the market.',
                           'items': ['Re-amortize a restarted loan at 360 months so payments are '
                                     'front-loaded with interest, and track three balances: the partial '
                                     "buyer's balance, the reassignment/entitlement balance, and current "
                                     'UPB [Paperstac — XRyBErGyKgQ @ 00:17:35].',
                                     'Size the partial to your cash and yield target: on a $400 payment, '
                                     '12 months equals $4,800, so paying $4,000 earns about 20% while '
                                     'paying $5,000 loses money [Paperstac — XRyBErGyKgQ @ 00:09:50].',
                                     'Split-payment partials only work on notes paying more than '
                                     '$1,000/mo, and the Reweys route them through an attorney so the '
                                     "structure doesn't create a security [Paperstac — UwiEQOh84Y4 @ "
                                     '00:32:03].',
                                     'Hunt auction inventory late in the year: the relaunch team says the '
                                     "best deals come from 'Thanksgiving on' [Paperstac — zhg1k-uMJM0 @ "
                                     '00:04:26].']},
               'sop_steps': [{'step': 1,
                              'title': 'Assemble the sale package',
                              'action': 'Gather the full document stack before requesting quotes.',
                              'detail': 'Pull the promissory note, deed of trust, settlement statement, '
                                        'insurance and tax records, and the borrower credit report, then '
                                        'add payment history and collateral details. A borrower score of '
                                        '650+ gets the highest price [Texas Capital Finance — w4PRGbUrreA '
                                        '@ 00:04:25].'},
                             {'step': 2,
                              'title': 'Get vetted and list on the marketplace',
                              'action': 'Register as a seller, pass ownership vetting, and load the asset.',
                              'detail': "Click 'become a seller,' pass the vetting that confirms you hold "
                                        'the note, then list by data tape, servicer email feed, or manual '
                                        'entry with public/private files and pay history [Patrick Franz — '
                                        'y6ljJ3T0eNg @ 00:32:11]. Choose flexible, firm, or make-an-offer '
                                        'pricing [Paperstac — chL0454K1Zs @ 00:01:45].'},
                             {'step': 3,
                              'title': 'Structure the partial if you are keeping the tail',
                              'action': 'Set the payment block by cash need and price it on yield.',
                              'detail': "Let the seller's cash need set how many payments to sell, price "
                                        'on yield when selling, and fix the reassignment balance plus '
                                        'payoff treatment, where each party gets the present value of its '
                                        'share. Leave servicing where it is [Paperstac — UwiEQOh84Y4 @ '
                                        '00:18:02].'},
                             {'step': 4,
                              'title': 'Close through escrow and audit, then record',
                              'action': 'Fund escrow, clear the collateral audit, and record the '
                                        'assignment.',
                              'detail': 'Have the buyer sign the disbursement agreement after reviewing '
                                        'the collateral audit [Patrick Franz — y6ljJ3T0eNg @ 00:44:17], '
                                        'then record assignments and deeds so neither side falls out of '
                                        'the chain of title [Paperstac — MkofIE1Xq0o @ 00:14:43].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Partials split the room on who should sit on which side of the trade. Fred '
                              'and Tracy Rewey treat buy-full, sell-partial as the cleanest exit. They '
                              'sell 144 of 176 payments for the same $68,430 paid for the whole note, and '
                              "the remaining 32 payments of roughly $800 carry an 'infinite' return. Their "
                              'Dallas deal, bought at $47,500, sold the next 279 payments for $51,000, '
                              'netting $3,500 while keeping 79 payments [UwiEQOh84Y4 @ 00:23:31]. Cal '
                              'Ewing came at partials from the opposite direction, as a reluctant '
                              "first-timer. Texas is Cal's favorite state and Cal did not want to sell, "
                              'but the private lender on the deal needed repair cash. So an IRA investor '
                              'paid 55,000 for the next 120 payments at a 10.48% IRR, while Cal kept a '
                              'tail of 130-plus payments worth 95,402 at full term [LCY-eZOK6gw @ '
                              '00:09:12]. Buy-side yield expectations diverge hard. The Reweys priced '
                              "their partial at 13.3%. Paperstac's hosts pitch whole-loan yields of 12 or "
                              "13 percent becoming '30 35' through partial structuring, and call the 10 to "
                              '20 percent buyers target expensive money for the seller [XRyBErGyKgQ @ '
                              "00:09:02]. The Paperstac guests on Patrick Franz's show quote partial "
                              "purchases at '30 40%' yields [y6ljJ3T0eNg @ 00:13:08]. A seller reading "
                              'those numbers is looking at what buyers think the lump sum is worth to '
                              'them.',
                              'Pricing method is the second fault line. The Reweys run partials two ways: '
                              'on yield, which they favor when selling, or at present value using the note '
                              'rate. On any payoff, each party collects the present value of its share '
                              '[UwiEQOh84Y4 @ 00:21:17]. Sierra Davis prices off yield and LTV together: '
                              '12% is the target, 13% is good, and nothing goes under a 10% floor. A 70% '
                              'LTV cap turns roughly $85,000 to $86,000 owed on a $120,000 sale into a '
                              '$75,000 offer at 11% [XsNZ5SQXdCI @ 00:41:16]. The JKP Holdings hosts push '
                              'back on that mindset. They warn against pricing performing paper on yield '
                              'alone and against assuming it keeps performing, and they dismiss '
                              "percent-of-UPB pricing as 'an old wise sale' [b-4NVMQ1GZ8 @ 00:05:05]. "
                              "Texas Capital Finance frames price from the seller's chair instead: the "
                              'closer a note resembles a traditional bank mortgage, the higher the price. '
                              'Bank-like paper fetches 95 to 98% of principal, while typical '
                              'seller-finance notes land between 90% and 70% [w4PRGbUrreA @ 00:08:46]. '
                              'These camps write very different checks on identical paper. Whoever sells a '
                              'partial or a whole note has to know which lens the buyer uses: yield, LTV, '
                              'or how closely the file looks like bank paper.',
                              "Leverage is where the playbooks split widest. JKP's hosts draw the line "
                              'cleanly: a partial buyer owns the note for a period, while hypothecation '
                              'lets the creator keep the note and borrow against it [b-4NVMQ1GZ8 @ '
                              '00:08:47]. Justin Roberts went the bank route after five or six notes '
                              'drained their cash. They pulled about $80,000 against a roughly $100,000 '
                              'note, plus a 24-note portfolio loan near $2 million priced a little under '
                              'prime. Yet the host openly doubted 10x leverage claims and pegged fund '
                              'financing at 75 to 80% advances at 4 to 5% [b-4NVMQ1GZ8 @ 00:41:50]. Justin '
                              'also refuses private money at 8 to 12%, even while lending at 12% '
                              "themselves. Paperstac's funding playbook runs another way. It sells a "
                              'partial off a reperformed non-performer, brings in patient rather than '
                              'active JV capital, or raises a Reg D fund from accredited investors. Their '
                              'Reg A+ raise left them doubting they would do another, because collecting '
                              '$1,000 at a time is brutal next to $100,000 to $500,000 checks [_BvWeumu2WI '
                              '@ 00:06:12]. Dave Van Horn takes yet another lane: borrowing 80% of about '
                              '$2 million in home equity at 4% to lend $1.6 million at 14%. Van Horn stays '
                              "mixed on HELOCs, though, because undisciplined borrowers 'go to vegas' "
                              '[jFBvJbcMbFA @ 00:20:36].'],
               'table': {'caption': 'Contrasting exit, pricing, and liquidity playbooks reported by note '
                                    'practitioners',
                         'headers': ['Decision Point',
                                     'Playbook A',
                                     'Contrasting Playbook',
                                     'Expert Source'],
                         'rows': [['Full sale versus partial sale as the exit route',
                                   'Texas Capital Finance says partial sales often command a higher price '
                                   'than full sales',
                                   'The Reweys buy the full note, sell 144 of 176 payments, and keep an '
                                   'infinite-return tail',
                                   'Texas Capital Finance ([w4PRGbUrreA @ 00:02:30]); Paperstac '
                                   '([UwiEQOh84Y4 @ 00:23:31])'],
                                  ['How long to season a fresh note before selling',
                                   'Moxxie buys once the first payment lands, and no law or rule requires '
                                   'holding',
                                   'Cherif Medawar wants six months to a year of on-time payments before '
                                   'buying',
                                   'Moxxie Education - Seller Financing & Notes ([usXnfzN3Wmc @ '
                                   '00:00:19]); Cherif Medawar ([bhfdMe7Dpwk @ 00:06:55])'],
                                  ['Which math sets the price of a partial',
                                   'The Reweys calculate on yield, which they treat as best when selling a '
                                   'partial',
                                   'The alternative is present value at the note rate, and on payoff each '
                                   'side takes its present value',
                                   'Paperstac ([UwiEQOh84Y4 @ 00:21:17]); Paperstac ([UwiEQOh84Y4 @ '
                                   '00:20:16])'],
                                  ['Yield-driven bids versus skepticism about yield-only pricing',
                                   'Sierra Davis targets 12% yield with a 10% floor and a 70% LTV cap',
                                   'JKP hosts warn against pricing performing paper on yield alone or '
                                   'assuming it keeps performing',
                                   'Agent2Investor Podcast ([XsNZ5SQXdCI @ 00:43:31]); Note Investing & '
                                   'Seller Financing - JKP Holdings ([b-4NVMQ1GZ8 @ 00:05:05])'],
                                  ['Unlocking cash from notes already held',
                                   'Sell a partial, so the buyer owns the payment stream for a set period',
                                   'Hypothecate with local banks: about $80,000 against a $100,000 note, '
                                   'though Justin warns not to bank on 80% on day one',
                                   'Note Investing & Seller Financing - JKP Holdings ([b-4NVMQ1GZ8 @ '
                                   '00:08:47]); Note Investing & Seller Financing - JKP Holdings '
                                   '([b-4NVMQ1GZ8 @ 00:19:30])'],
                                  ['Raising outside capital for note purchases',
                                   'A Reg D fund with accredited investors, an attorney, and a track '
                                   'record can reach millions',
                                   'Reg A+ allows non-accredited money but is expensive and capped, and '
                                   'Paperstac doubts it would repeat one',
                                   'Paperstac ([_BvWeumu2WI @ 00:05:35]); Paperstac ([_BvWeumu2WI @ '
                                   '00:06:12])'],
                                  ['Selling partials on wraparound notes',
                                   'Paperstac calls partials on wraps potentially sticky, so sellers use '
                                   'the proceeds to pay off the underlying lien',
                                   'Justin Roberts gets local banks to sign off on due-on-sale and wrap '
                                   'through bank-approved structures',
                                   'Paperstac ([5bOm5hdSRXc @ 00:07:29]); Note Investing & Seller '
                                   'Financing - JKP Holdings ([b-4NVMQ1GZ8 @ 00:12:35])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Most note deals that blow up do it at the closing table, not in the payment '
                              'stream. Paperstac watches hundreds of closings a quarter and keeps seeing '
                              'the same buyer errors. Buyers bid without an indicative bid. They show up '
                              'without funds ready, so sellers suspect the loan is being shopped and block '
                              'them. Their self-directed IRA custodians take weeks while the assignment '
                              'sits in draft, and one deal has run three months [MkofIE1Xq0o @ 00:07:23]. '
                              'Vesting mistakes on FBO wording, address, or signer are worse. Changing the '
                              'PSA after the collateral is with the auditor and money is in escrow '
                              'unravels the whole closing, so screenshot the vesting before anything moves '
                              '[MkofIE1Xq0o @ 00:12:07]. Lowballing every listing by $20,000 gets an '
                              'account frozen, and going dark mid-deal invites the seller to resell. The '
                              'quietest trap hits after funding. Unrecorded assignments and deeds have '
                              'knocked buyers out of the chain of title, surfacing three years later or as '
                              'tax notices 18 months after a sale. Fund wind-downs then make the original '
                              'seller nearly impossible to track down [MkofIE1Xq0o @ 00:14:54]. '
                              "Off-platform, the Paperstac guests on Patrick Franz's show describe buyers "
                              'wiring $50,000 and waiting 30 days for a collateral file. On-platform, '
                              'FedEx two-day shipping lands files in three to five days [y6ljJ3T0eNg @ '
                              '00:45:12].',
                              "Collateral and paper quality kill exits further downstream. Sierra Davis's "
                              'first note, bought from a mentor after seven months of study, collapsed '
                              'fast. The borrower paid three times, then the roughly $75,000 house turned '
                              'up empty mid-renovation. Sierra cancelled the contract and resold the '
                              'property as-is on seller financing [XsNZ5SQXdCI @ 00:32:08]. Their rule '
                              'since then: if the paperwork is not good, you cannot foreclose. Justin '
                              'Roberts found that sloppy origination also blocks leverage. Their first '
                              'dozen notes carried no RMLO and a flat $20,000 down regardless of credit, '
                              'and banks rejected them as below standard [b-4NVMQ1GZ8 @ 00:16:07]. Growth '
                              "then slammed into one bank's legal lending limit, forcing a pivot and a "
                              'revolving door of bank contacts. Cherif Medawar flags the borrower with no '
                              'skin in the game, pointing to VA loans up to $2 million with no money down '
                              'where borrowers simply walk. Cherif demands a real cash down payment plus '
                              'six months to a year of on-time seasoning [bhfdMe7Dpwk @ 00:06:08]. '
                              "Paperstac's wrap segment adds the structural warnings. Originate through an "
                              'attorney or title company, watch the due-on-sale exposure because banks are '
                              'wise to subject-to deals, and never turn a great portfolio of real estate '
                              'into a crappy portfolio of notes [5bOm5hdSRXc @ 00:15:37].',
                              'Run the downside math before signing any partial or note sale. Cal Ewing '
                              'modeled three outcomes at month 36 on the 55,000 partial. A payoff gives '
                              'the investor 68,000 total and a 13,017 profit, with roughly 20,600 to Cal. '
                              'A Texas non-judicial auction at a 105,000 bid, less a 5,000 attorney fee, '
                              'still pays the investor 41,900 and Cal 20,600, with the surplus going to '
                              'the borrower. An REO sale at 130,000 ARV, less 20,000 in costs, pays the '
                              'investor 52,115 and leaves Cal 57,885 [LCY-eZOK6gw @ 00:19:21]. Texas '
                              "Capital Finance warns sellers that total future interest is not the note's "
                              'value, because borrowers can prepay [w4PRGbUrreA @ 00:08:31]. Justin '
                              'Roberts lived that: their first owner-financed flip paid off after two '
                              'payments. Justin also reports that buyers with $20,000 to $30,000 down have '
                              'dried up and four flips sit unsold. Desperate sellers are now cutting 4 to '
                              "5% 30-year notes, the kind of low-rate paper Justin says won't win 80% bank "
                              "advances [b-4NVMQ1GZ8 @ 00:47:49]. Paperstac's pricing team adds the "
                              'marketplace verdict: mispriced assets go to die. Their monthly-retrained '
                              'price predictor runs within about 2% on sales of $30,000 or more, so an '
                              'inflated ask gets exposed fast [zhg1k-uMJM0 @ 00:16:15].'],
               'table': {'caption': 'Firsthand failure modes and the economics checks practitioners now '
                                    'run',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check Or Fix',
                                     'Expert Source'],
                         'rows': [['Bidding without funds actually ready to close',
                                   'Sellers suspect the buyer is shopping the loan and block that buyer',
                                   'Have cash or a fully approved retirement account in place before '
                                   'placing any bid',
                                   'Paperstac ([MkofIE1Xq0o @ 00:05:56])'],
                                  ['Self-directed IRA custodian delays stalling the assignment',
                                   'Custodians take weeks, the assignment stays in draft, and one deal ran '
                                   'three months',
                                   'Get a complete stamp of approval from the account manager before going '
                                   'under contract',
                                   'Paperstac ([MkofIE1Xq0o @ 00:10:25])'],
                                  ['Unrecorded assignments and deeds after closing',
                                   'Buyers fell out of the chain of title, discovered three years later or '
                                   'via tax notices',
                                   "Record assignments and deeds immediately, using Paperstac's recording "
                                   'option when available',
                                   'Paperstac ([MkofIE1Xq0o @ 00:14:54])'],
                                  ['Weak origination blocking bank hypothecation',
                                   'First dozen notes with no RMLO and flat $20,000 down were rejected by '
                                   'banks',
                                   'Originate to bank standards and keep polished financials, QuickBooks, '
                                   'and DSCR ready',
                                   'Note Investing & Seller Financing - JKP Holdings ([b-4NVMQ1GZ8 @ '
                                   '00:16:07])'],
                                  ['Borrower abandoning the property soon after purchase',
                                   'Borrower paid three times and the house was found empty mid-renovation',
                                   'Underwrite property, paperwork, and payer, then lean on mentors for '
                                   'red flags',
                                   'Agent2Investor Podcast ([XsNZ5SQXdCI @ 00:32:08])'],
                                  ['Split-payment partials drifting into a securities problem',
                                   'The Reweys only use split-payment partials on notes paying more than '
                                   '$1,000 monthly',
                                   'Bring in an attorney so the split structure does not create a security',
                                   'Paperstac ([UwiEQOh84Y4 @ 00:32:03])'],
                                  ['Wiring money before the collateral file arrives',
                                   'Off-platform buyers wire $50,000 and wait 30 days for the collateral '
                                   'file',
                                   'Use escrow plus collateral audit and sign disbursement only after '
                                   'reviewing the audit',
                                   'Patrick Franz ([y6ljJ3T0eNg @ 00:45:12])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Gates Before Any Note Exit or Partial',
                           'body': 'Every gate below comes from a deal that stalled, unraveled, or lost '
                                   'money for a named practitioner. Clear all four before signing a '
                                   'purchase, a partial sale, or a full note sale.',
                           'items': ['Lock an indicative bid off verified rate, UPB, origination date, and '
                                     'last pay date, and never lowball every listing by $20,000 [Paperstac '
                                     '— MkofIE1Xq0o @ 00:04:12].',
                                     'Confirm FBO wording, address, and signer on the vesting and '
                                     'screenshot it before collateral goes to the auditor [Paperstac — '
                                     'MkofIE1Xq0o @ 00:12:07].',
                                     'On a wrap, run title, disclose the underlying lien, and use partial '
                                     'proceeds to pay that lien off so the note moves to first position '
                                     '[Paperstac — 5bOm5hdSRXc @ 00:07:29].',
                                     'Model payoff, auction, and REO splits between the partial investor '
                                     'and the tail holder before selling any partial [Cal Ewing — '
                                     'LCY-eZOK6gw @ 00:12:50].']}}],
 'pull_quote': '"Record your assignments and record your deeds." — Paperstac (MkofIE1Xq0o @ 00:14:43).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Build the listing with photos, a recent BPO value document, pay history, and '
                      'private files, because buyers will ask for the files anyway [Paperstac — '
                      'chL0454K1Zs @ 00:01:24].',
                      'Choose flexible, firm, or make-an-offer pricing and write a subtitle and seller '
                      "description that tell the note's story [Paperstac — chL0454K1Zs @ 00:01:45].",
                      'Assemble the sale package: promissory note, deed of trust, settlement statement, '
                      'insurance and tax records, and the borrower credit report, where a 650-plus score '
                      'draws the highest price [Texas Capital Finance — w4PRGbUrreA @ 00:04:25].',
                      "Size any partial to the seller's actual cash need and leave servicing where it "
                      'already sits [Paperstac — UwiEQOh84Y4 @ 00:18:02].',
                      'Before pitching local banks, prepare a roughly 20-page banker package of '
                      "financials, quarterly reports, and a PFS, modeled on Stinson Bland's 'banker's "
                      "bible' [Note Investing & Seller Financing - JKP Holdings — b-4NVMQ1GZ8 @ 00:21:08].",
                      'Close through escrow plus a collateral audit, and sign the disbursement agreement '
                      'only after reviewing that audit [Patrick Franz — y6ljJ3T0eNg @ 00:44:17].'],
 'statutory_citations': [{'title': 'Paperstac — Partial Mortgage Note Training with Fred & Tracy Rewey '
                                   '[00:23:31]',
                          'url': 'https://www.youtube.com/watch?v=UwiEQOh84Y4&t=1411s',
                          'relevance': 'Primary practitioner testimony on buy-full, sell-partial '
                                       'structuring, partial pricing math, and tail retention.'},
                         {'title': 'Cal Ewing — How to Cash Out of a Performing Note Without Selling It – '
                                   'Real Case Study on Selling Partials! [00:09:12]',
                          'url': 'https://www.youtube.com/watch?v=LCY-eZOK6gw&t=552s',
                          'relevance': 'Primary practitioner testimony on a first-time partial sale to an '
                                       'IRA investor and payoff, auction, and REO split modeling.'},
                         {'title': 'Note Investing & Seller Financing - JKP Holdings — Note Hypothecation '
                                   'with Local Banks w/ Justin Roberts | Real Estate Notes Show Ep 134 '
                                   '[00:08:47]',
                          'url': 'https://www.youtube.com/watch?v=b-4NVMQ1GZ8&t=527s',
                          'relevance': 'Primary practitioner testimony on hypothecation versus partials, '
                                       'bank advance rates, and legal lending limits.'},
                         {'title': 'Paperstac — 5 Mistakes That Will Wreck Your First Mortgage Note Deal '
                                   '[00:14:54]',
                          'url': 'https://www.youtube.com/watch?v=MkofIE1Xq0o&t=894s',
                          'relevance': 'Primary practitioner testimony on closing failures, vesting '
                                       'errors, IRA delays, and unrecorded assignments.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'jFBvJbcMbFA',
                       'title': 'Mortgage Note Arbitrage & the Future of the Industry (Interview)',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': "A lot of times it's not what we pay it's how we pay stuff.",
                       'tip': "A lot of times it's not what we pay it's how we pay stuff.",
                       'timestamp': 1654,
                       'timestamp_seconds': 1654,
                       'timestamp_label': '[00:27:34]',
                       'url': 'https://www.youtube.com/watch?v=jFBvJbcMbFA&t=1654s',
                       'markdown': '[00:27:34](https://www.youtube.com/watch?v=jFBvJbcMbFA&t=1654s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UwiEQOh84Y4',
                       'title': 'Partial Mortgage Note Training with Fred & Tracy Rewey',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'We bought the $54,000 note at 11.5% for $47,500, sold the next 279 '
                               'payments for $51,000, netted $3,500, and kept 79 payments.',
                       'tip': 'We bought the $54,000 note at 11.5% for $47,500, sold the next 279 payments '
                              'for $51,000, netted $3,500, and kept 79 payments.',
                       'timestamp': 1685,
                       'timestamp_seconds': 1685,
                       'timestamp_label': '[00:28:05]',
                       'url': 'https://www.youtube.com/watch?v=UwiEQOh84Y4&t=1685s',
                       'markdown': '[00:28:05](https://www.youtube.com/watch?v=UwiEQOh84Y4&t=1685s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LCY-eZOK6gw',
                       'title': 'How to Cash Out of a Performing Note Without Selling It – Real Case Study '
                                'on Selling Partials!',
                       'channel': 'Cal Ewing',
                       'author': 'Cal Ewing',
                       'text': "This is the first time I've ever sold partials.",
                       'tip': "This is the first time I've ever sold partials.",
                       'timestamp': 499,
                       'timestamp_seconds': 499,
                       'timestamp_label': '[00:08:19]',
                       'url': 'https://www.youtube.com/watch?v=LCY-eZOK6gw&t=499s',
                       'markdown': '[00:08:19](https://www.youtube.com/watch?v=LCY-eZOK6gw&t=499s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'w4PRGbUrreA',
                       'title': 'How to Sell Your Mortgage Note for the Best Price | Step-by-Step Guide',
                       'channel': 'Texas Capital Finance',
                       'author': 'Texas Capital Finance',
                       'text': 'The simplest way to explain price is the closer your mortgage resembles a '
                               "traditional bank's mortgage the higher the price and vice versa.",
                       'tip': 'The simplest way to explain price is the closer your mortgage resembles a '
                              "traditional bank's mortgage the higher the price and vice versa.",
                       'timestamp': 398,
                       'timestamp_seconds': 398,
                       'timestamp_label': '[00:06:38]',
                       'url': 'https://www.youtube.com/watch?v=w4PRGbUrreA&t=398s',
                       'markdown': '[00:06:38](https://www.youtube.com/watch?v=w4PRGbUrreA&t=398s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bhfdMe7Dpwk',
                       'title': 'How To Buy Mortgage Notes With No Money? | @CherifMedawar',
                       'channel': 'Cherif Medawar',
                       'author': 'Cherif Medawar',
                       'text': 'VA loans go up to $2 million with no money down, and borrowers with no '
                               'skin in the game walk away, so require a real cash down payment.',
                       'tip': 'VA loans go up to $2 million with no money down, and borrowers with no skin '
                              'in the game walk away, so require a real cash down payment.',
                       'timestamp': 368,
                       'timestamp_seconds': 368,
                       'timestamp_label': '[00:06:08]',
                       'url': 'https://www.youtube.com/watch?v=bhfdMe7Dpwk&t=368s',
                       'markdown': '[00:06:08](https://www.youtube.com/watch?v=bhfdMe7Dpwk&t=368s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XRyBErGyKgQ',
                       'title': 'Mortgage Note Partials – The How & Why To Do It',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'Buy the loan, sell a partial at 12 to 14 percent to cover your cost, and '
                               'keep the last eight or so years of the 18.',
                       'tip': 'Buy the loan, sell a partial at 12 to 14 percent to cover your cost, and '
                              'keep the last eight or so years of the 18.',
                       'timestamp': 805,
                       'timestamp_seconds': 805,
                       'timestamp_label': '[00:13:25]',
                       'url': 'https://www.youtube.com/watch?v=XRyBErGyKgQ&t=805s',
                       'markdown': '[00:13:25](https://www.youtube.com/watch?v=XRyBErGyKgQ&t=805s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_BvWeumu2WI',
                       'title': '5 Creative Ways to Fund Your Next Mortgage Note Purchase',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': "They might buy something for 35,000 that's worth, you know, the principal "
                               "balance on it is 55 or 60,000, and they'll turn around and sell a partial "
                               'on it for 34,000.',
                       'tip': "They might buy something for 35,000 that's worth, you know, the principal "
                              "balance on it is 55 or 60,000, and they'll turn around and sell a partial "
                              'on it for 34,000.',
                       'timestamp': 121,
                       'timestamp_seconds': 121,
                       'timestamp_label': '[00:02:01]',
                       'url': 'https://www.youtube.com/watch?v=_BvWeumu2WI&t=121s',
                       'markdown': '[00:02:01](https://www.youtube.com/watch?v=_BvWeumu2WI&t=121s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MkofIE1Xq0o',
                       'title': '5 Mistakes That Will Wreck Your First Mortgage Note Deal',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'Record your assignments and record your deeds.',
                       'tip': 'Record your assignments and record your deeds.',
                       'timestamp': 883,
                       'timestamp_seconds': 883,
                       'timestamp_label': '[00:14:43]',
                       'url': 'https://www.youtube.com/watch?v=MkofIE1Xq0o&t=883s',
                       'markdown': '[00:14:43](https://www.youtube.com/watch?v=MkofIE1Xq0o&t=883s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MkofIE1Xq0o',
                       'title': '5 Mistakes That Will Wreck Your First Mortgage Note Deal',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'This is a good way to get banned is if you go through and just go to every '
                               "single listing and offer 20 grand underneath what it's listed for.",
                       'tip': 'This is a good way to get banned is if you go through and just go to every '
                              "single listing and offer 20 grand underneath what it's listed for.",
                       'timestamp': 790,
                       'timestamp_seconds': 790,
                       'timestamp_label': '[00:13:10]',
                       'url': 'https://www.youtube.com/watch?v=MkofIE1Xq0o&t=790s',
                       'markdown': '[00:13:10](https://www.youtube.com/watch?v=MkofIE1Xq0o&t=790s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'usXnfzN3Wmc',
                       'title': 'Can I Sell My Seller Financed Mortgage Note After Just ONE Payment?',
                       'channel': 'Moxxie Education - Seller Financing & Notes',
                       'author': 'Moxxie Education - Seller Financing & Notes',
                       'text': 'Technically, you can sell a note the day after you create it.',
                       'tip': 'Technically, you can sell a note the day after you create it.',
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=usXnfzN3Wmc&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=usXnfzN3Wmc&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5bOm5hdSRXc',
                       'title': 'Turn a Rental with a Current Mortgage into a Mortgage Note (How to)',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'Doing partials on a wrap could get potentially sticky.',
                       'tip': 'Doing partials on a wrap could get potentially sticky.',
                       'timestamp': 381,
                       'timestamp_seconds': 381,
                       'timestamp_label': '[00:06:21]',
                       'url': 'https://www.youtube.com/watch?v=5bOm5hdSRXc&t=381s',
                       'markdown': '[00:06:21](https://www.youtube.com/watch?v=5bOm5hdSRXc&t=381s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b-4NVMQ1GZ8',
                       'title': 'Note Hypothecation with Local Banks w/ Justin Roberts | Real Estate Notes '
                                'Show Ep 134',
                       'channel': 'Note Investing & Seller Financing - JKP Holdings',
                       'author': 'Note Investing & Seller Financing - JKP Holdings',
                       'text': "So, I would not bank on 80% if you're looking to start doing this day one.",
                       'tip': "So, I would not bank on 80% if you're looking to start doing this day one.",
                       'timestamp': 1170,
                       'timestamp_seconds': 1170,
                       'timestamp_label': '[00:19:30]',
                       'url': 'https://www.youtube.com/watch?v=b-4NVMQ1GZ8&t=1170s',
                       'markdown': '[00:19:30](https://www.youtube.com/watch?v=b-4NVMQ1GZ8&t=1170s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XsNZ5SQXdCI',
                       'title': 'The Note Investing Strategy for Busy W-2 Professionals with Sierra Davis',
                       'channel': 'Agent2Investor Podcast',
                       'author': 'Agent2Investor Podcast',
                       'text': "I mean, I don't like it lower than 10%.",
                       'tip': "I mean, I don't like it lower than 10%.",
                       'timestamp': 2611,
                       'timestamp_seconds': 2611,
                       'timestamp_label': '[00:43:31]',
                       'url': 'https://www.youtube.com/watch?v=XsNZ5SQXdCI&t=2611s',
                       'markdown': '[00:43:31](https://www.youtube.com/watch?v=XsNZ5SQXdCI&t=2611s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'y6ljJ3T0eNg',
                       'title': 'PaperStac Marketplace & Mortgage Note Investing Guide',
                       'channel': 'Patrick Franz',
                       'author': 'Patrick Franz',
                       'text': 'Due diligence is half the battle in this game.',
                       'tip': 'Due diligence is half the battle in this game.',
                       'timestamp': 1209,
                       'timestamp_seconds': 1209,
                       'timestamp_label': '[00:20:09]',
                       'url': 'https://www.youtube.com/watch?v=y6ljJ3T0eNg&t=1209s',
                       'markdown': '[00:20:09](https://www.youtube.com/watch?v=y6ljJ3T0eNg&t=1209s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WaCgDRVF1rY',
                       'title': 'How to Buy and Sell Mortgage Notes Online (Without the Headache)',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': "It's free to list, with over 6,000 registered buyers, you'll get real bids "
                               'at market values, almost immediately.',
                       'tip': "It's free to list, with over 6,000 registered buyers, you'll get real bids "
                              'at market values, almost immediately.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=WaCgDRVF1rY&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=WaCgDRVF1rY&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zhg1k-uMJM0',
                       'title': 'Inside the New Paperstac: A New Era for Mortgage Note Trading',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': "Auction isn't to scare anybody, it's the way that a lot of people do "
                               'things.',
                       'tip': "Auction isn't to scare anybody, it's the way that a lot of people do "
                              'things.',
                       'timestamp': 219,
                       'timestamp_seconds': 219,
                       'timestamp_label': '[00:03:39]',
                       'url': 'https://www.youtube.com/watch?v=zhg1k-uMJM0&t=219s',
                       'markdown': '[00:03:39](https://www.youtube.com/watch?v=zhg1k-uMJM0&t=219s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'chL0454K1Zs',
                       'title': 'How to List a Mortgage Note That Sells in Under 30 Days',
                       'channel': 'Paperstac',
                       'author': 'Paperstac',
                       'text': 'Buyers are going to ask for the files, so load them up front and set them '
                               'private so you can share them per transaction.',
                       'tip': 'Buyers are going to ask for the files, so load them up front and set them '
                              'private so you can share them per transaction.',
                       'timestamp': 69,
                       'timestamp_seconds': 69,
                       'timestamp_label': '[00:01:09]',
                       'url': 'https://www.youtube.com/watch?v=chL0454K1Zs&t=69s',
                       'markdown': '[00:01:09](https://www.youtube.com/watch?v=chL0454K1Zs&t=69s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
