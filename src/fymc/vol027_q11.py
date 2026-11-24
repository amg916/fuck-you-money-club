from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'asset-vs-stock-purchases-tax-allocation-buyer-protections',
 'question_prompt': 'Should the deal be an asset or stock purchase, and how do tax allocation, reps and '
                    'warranties, and set-off rights protect the buyer?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': 'Asset vs. Stock Purchases, Tax Allocation, and Buyer Protections',
 'subtitle': 'Asset vs. share purchases and buyer/seller preferences, inherited liabilities, IRS Form 8594 '
             "and Section 1060 allocation, what a seller note can't spread, fixed-asset accounting for "
             'asset acquisitions, QSBS and F-reorgs, the three primary deal structures, representations '
             'and warranties, and set-off rights against seller notes',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners line up on one rule: sellers want to sell stock for capital-gains '
                      'treatment, buyers want to buy assets for liability protection and a stepped-up '
                      'basis, and almost every main street and lower middle market deal closes as an asset '
                      "sale. Stock deals hand the buyer the entity's full history, so they demand heavier "
                      'diligence; asset deals leave old debts with the seller but force third-party '
                      'consents, new bank accounts, rehired staff, and a matching Form 8594 allocation. '
                      'Hard numbers: a $1M intangible amortizes over 15 years, a standalone C Corp seller '
                      'eats roughly 21% twice, and SMB protection runs on 10-15% indemnity caps, escrows, '
                      'holdbacks, and set-off against the seller note. Disagreement centers on whether '
                      'share purchases are administratively easier, whether asset buyers inherit '
                      'liabilities, and whether reps and warranties are worth anything without a note to '
                      'offset.',
 'key_metrics': [{'label': 'Lower middle market escrow prevalence',
                  'metric': 'Lower middle market escrow prevalence',
                  'value': '89% of deals carry an escrow, median 10%; SMB deal escrows likely under 5%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'SMB Law Group LLP citing the Aquiem study on lower middle market deal terms '
                             'versus smaller SMB deals',
                  'source': 'SMB Law Group LLP ([iNOj__jXGpE @ 00:43:34])'},
                 {'label': 'Intangible amortization period on an asset purchase',
                  'metric': 'Intangible amortization period on an asset purchase',
                  'value': '15 years on a $1M intangible-only purchase price',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Same $1M bought as stock stays trapped in stock basis until exit, for '
                             'example 5 years later',
                  'source': 'Tax Hack Accounting Group ([Wd1__Z4Nz6k @ 00:02:32])'},
                 {'label': 'SMB indemnity cap and matching seller note size',
                  'metric': 'SMB indemnity cap and matching seller note size',
                  'value': 'Indemnity cap 10-15%; deductible 0.5-1%; seller note sized at 10-15% to match '
                           'the cap',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Market terms reported across roughly 130+ deals last year; survival periods '
                             '12-24 months, 12-18 the norm',
                  'source': 'SMB Law Group LLP ([iNOj__jXGpE @ 00:26:54])'},
                 {'label': 'Substantially all screen test threshold',
                  'metric': 'Substantially all screen test threshold',
                  'value': 'Around 90% of gross asset fair value in one asset or group of similar assets',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'No bright line; near 90% means running the full framework to separate an '
                             'asset acquisition from a business',
                  'source': 'PwC US ([b43cWRS8RKE @ 00:05:35])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['The split is the first thing every practitioner says out loud. Brett Cenkus '
                              'puts it flatly: sellers want to sell stock, buyers want to buy assets, '
                              'because stock delivers capital gains that go long-term after one year and '
                              'possibly zero tax under QSBS, while an asset buyer re-depreciates '
                              'everything at market value [ASUM5illI98 @ 00:01:56]. Tax Hack Accounting '
                              'Group goes further, saying the seller is always going to want to sell stock '
                              'and that sellers volunteering for asset sales is very rare, since an asset '
                              'sale computes gain asset by asset and drags depreciation recapture, '
                              'cash-basis receivables, and inventory into higher ordinary rates '
                              '[Wd1__Z4Nz6k @ 00:00:21]. Jeremy A. Johnson, CPA frames the buyer side as '
                              'liability protection plus a step-up in basis, and the seller side as '
                              'capital gains, warning that sellers must know their basis to calculate the '
                              'gain [xVt6suFrCqE @ 00:00:49]. Despite seller preference, the market lands '
                              'on assets: Walker Deibel states that almost all lower middle market and '
                              'main street transactions are going to be an asset sale and not a stock '
                              "sale, and Deibel's framing is that the assets generate the cash, not the "
                              'legal entity, so the buyer is really paying for what produces the cash '
                              '[NM-ZwBNBHQE @ 00:02:06].',
                              'The second point of consensus is liability. A share purchaser acquires the '
                              'company with its history, as Thomas Efraim LLP puts it, which is why in the '
                              "firm's scenario the buyer switches to an asset purchase after price is "
                              'agreed and forces the economics to be revisited [l2gJwZbVVnc @ 00:01:27]. '
                              'Walker Deibel uses a toxic waste example for inherited history: the stock '
                              'buyer takes everything the entity ever did, while in an asset sale the '
                              "buyer forms a new entity, the seller's entity is left hollow, and employees "
                              'are terminated and rehired in the following days [NM-ZwBNBHQE @ 00:05:28]. '
                              'Tax Hack Accounting Group says stock buyers inherit all historic '
                              'liabilities, federal, state, and sales and use, while asset buyers '
                              'generally escape income tax exposure but can still pick up sales and use, '
                              'payroll, and gross receipts taxes [Wd1__Z4Nz6k @ 00:03:07]. Paper Rich adds '
                              'the escape hatches that collapse the asset shield: you assumed the debts, a '
                              'de facto merger, a mere continuation, or a fraudulent dodge, and in New '
                              "York the buyer gives the tax department 10 days' notice or risks liability "
                              "for the seller's sales tax [Qqgfjq8CujE @ 00:01:11]. The operator takeaway "
                              'is consistent: asset structure narrows exposure, it does not erase it.',
                              'Every adviser who spoke to timing says the same thing: lock structure '
                              'before price. Josh Siegel, a CPA and tax attorney, tells Dennis Unrein that '
                              'tax structure belongs in the LOI, because a silent LOI lets the buyer '
                              'assume an asset deal while the seller assumes a stock deal, and that '
                              'conversation is not productive post LOI [hDmKsEVGoBI @ 00:01:23]. Thomas '
                              "Efraim LLP's checklist runs the same order: settle structure early, involve "
                              'tax advisors before price, identify third-party consents, do legal '
                              'diligence, and document which liabilities are assumed [l2gJwZbVVnc @ '
                              '00:02:23]. The consensus exceptions, where stock wins even for the buyer, '
                              'are just as consistent. Walker Deibel lists a non-transferable essential '
                              'contract or license, a minority equity investment, and larger deals where '
                              'the seller retains 20% and the buyer takes 80% [NM-ZwBNBHQE @ 00:06:34]. '
                              'Chris Barsness flags non-transferable licenses such as alcohol licenses, '
                              'change-of-control clauses, contract assignability, leases, landlord '
                              'consents, and minority-shareholder consents as the items that decide '
                              'whether an asset deal can physically close, and Barsness notes that if you '
                              "only want part of the assets a stock purchase usually won't work "
                              '[-DthgkqGsGA @ 00:06:31]. Structure is a diligence output, not a '
                              'preference.'],
               'table': {'caption': 'Where practitioners agree on asset versus stock structure',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Sellers want stock while buyers want assets',
                                   'Stock gives sellers capital gains; assets let buyers re-depreciate at '
                                   'market value',
                                   'Expect seller pushback the moment an asset structure is proposed in '
                                   'talks',
                                   'Brett Cenkus ([ASUM5illI98 @ 00:01:56])'],
                                  ['Main street and lower middle market deals default to assets',
                                   'Almost all transactions at that size close as asset sales, not stock '
                                   'sales',
                                   'Model every small deal as an asset purchase unless something forces '
                                   'stock',
                                   'Walker Deibel ([NM-ZwBNBHQE @ 00:02:06])'],
                                  ['Stock buyers inherit the full corporate history and all liabilities',
                                   'All historic federal, state, and sales and use tax liabilities '
                                   'transfer with stock',
                                   'Run much deeper diligence on any stock deal than on an asset deal',
                                   'Tax Hack Accounting Group ([Wd1__Z4Nz6k @ 00:03:07])'],
                                  ['The asset shield has known exceptions that pull liability onto buyers',
                                   'Assumed debts, de facto merger, mere continuation, or a fraudulent '
                                   'dodge break protection',
                                   'Never structure an asset deal that looks like a continuation dodge of '
                                   'old debts',
                                   'Paper Rich ([Qqgfjq8CujE @ 00:01:11])'],
                                  ['Tax structure must be fixed in the LOI before price',
                                   'A silent LOI lets each side assume a different structure and different '
                                   'economics',
                                   'Write asset or stock, and any election path, into the LOI itself',
                                   'Dennis Unrein / SMB PE LLC ([hDmKsEVGoBI @ 00:01:23])'],
                                  ['Non-transferable licenses and consents can force a stock deal',
                                   'Alcohol licenses, change-of-control clauses, leases, landlord and '
                                   'minority consents decide feasibility',
                                   'Inventory every license and consent before choosing the final deal '
                                   'structure',
                                   'Chris Barsness - Securities Law Media ([-DthgkqGsGA @ 00:06:31])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The tax mechanics explain why buyers fight for assets. Tax Hack Accounting '
                              'Group runs a $1M intangible-only deal: as a stock purchase the $1M is '
                              'trapped in stock basis until exit, say five years later, but as an asset '
                              'purchase it is amortizable over 15 years [Wd1__Z4Nz6k @ 00:02:32]. Josh '
                              'Siegel confirms that buying $1M of C Corp stock gives $1M of basis with no '
                              'depreciation, no amortization, and no step-up, that price is allocated '
                              'across seven asset classes recovered over 1 to 15 years with goodwill at '
                              '15, and that a $1M step-up on 3-year trucks throws off one third per year '
                              '[hDmKsEVGoBI @ 00:07:44]. The seller side has its own math. Walker Deibel '
                              'shows a $100 price netting the seller $65 in an asset sale versus $75 in a '
                              'stock sale, so a buyer may pay about $90 for stock [NM-ZwBNBHQE @ '
                              '00:07:41]. Siegel says a standalone C Corp asset sale is quite hard to make '
                              'work: the seller pays 21% corporate tax, then roughly another 21% on '
                              'distribution plus state tax, demands a gross-up, and that gross-up is '
                              'neutral only with full year-one depreciation [hDmKsEVGoBI @ 00:09:32]. The '
                              'workaround Siegel names is synthetic asset treatment through 338(h)(10), '
                              '336(e), or an F reorg.',
                              'Once the structure is set, the allocation becomes the battlefield. Paper '
                              'Rich notes that in an asset deal both sides report the price split to the '
                              'IRS [Qqgfjq8CujE @ 00:00:53], and Teach Me! Personal Finance walks Form '
                              '8594 line by line: seller and buyer both file it for a business purchase, '
                              'not for single pieces of equipment, Class 1 is actual cash, goodwill sits '
                              'in Class 6 and 7, and side deals for a non-compete, license, or lease are '
                              'reported at maximum consideration, such as $50K a year for 3 years equaling '
                              '$150K [G0f0r8tYMnk @ 00:09:15]. Both returns must match, or the IRS is '
                              'probably going to catch that. Hans Goldstein ties the allocation to the '
                              'seller note: under IRC 1060(a) a written allocation binds both sides, '
                              'inventory in Class IV is ordinary income that is completely ineligible for '
                              'installment reporting, and a seller note only spreads the goodwill, so the '
                              'allocation and the down payment have to be negotiated together [I8L23gqP5to '
                              "@ 00:02:57]. Goldstein's 2026 example runs a 72.0% gross profit ratio, a "
                              'year-one payment of $410,047, interest of $201,600, and gain of $956,482. '
                              'Martin Godfrey Legido adds the HMRC angle: in an asset deal every value '
                              'needs accountant work and vendor agreement, and HMRC watches undervalue '
                              'transfers [04Uy5gfO_PU @ 00:07:37].',
                              'Protection mechanics are where the SMB Law Group LLP team gets specific, '
                              'drawing on 399 deals closed as a firm. Escrow money moves only on joint '
                              'instructions or a court order; a holdback on a $4M deal wires $3.5M and '
                              'keeps $0.5M, which shifts the burden to the seller; and set-off against the '
                              'seller note is the most common tool [iNOj__jXGpE @ 00:10:09]. Their market '
                              'terms: survival periods of 12 to 24 months with 12 to 18 the norm, an '
                              'indemnity cap of 10 to 15%, a deductible of 0.5 to 1%, and in SMB deals an '
                              'escrow equal to the cap, with the seller note sized at 10 to 15% so it '
                              'matches the cap [iNOj__jXGpE @ 00:26:54]. The tactic when a $100K claim '
                              'lands is to pause note payments, such as $11,000 a month, and not spend the '
                              'withheld money. David C Barnett reaches the same tool from the street: reps '
                              'and warranties are words on paper, suing over $10K costs too much, so '
                              'protection number two after the seller relationship is a note you can '
                              'offset, like skipping 10 payments of $1,000 [LStVgWOM2LI @ 00:02:08]. Brett '
                              'Cenkus adds that sellers give 15 to 30 reps against 4 to 10 from buyers, '
                              'and that sellers are usually liable jointly and severally [cnvG-qb6w9Q @ '
                              '00:01:11].'],
               'table': {'caption': 'Street mechanics, numbers, and how operators deploy them',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Asset step-up on an intangible-only purchase',
                                   '$1M price amortizable over 15 years versus trapped in stock basis '
                                   'until exit',
                                   'Price the tax shield into your offer and debt service model',
                                   'Tax Hack Accounting Group ([Wd1__Z4Nz6k @ 00:02:32])'],
                                  ['Seller net proceeds in an asset sale versus a stock sale',
                                   '$100 price nets $65 as assets and $75 as stock; buyer may pay about '
                                   '$90 for stock',
                                   'Use the after-tax gap to trade price for structure in negotiation',
                                   'Walker Deibel ([NM-ZwBNBHQE @ 00:07:41])'],
                                  ['Synthetic asset elections when buying corporate stock',
                                   '338(h)(10) needs a C Corp buyer; 336(e) allows LLC buyers; both '
                                   'require at least 80% within one year',
                                   'Buying 70% or 79% kills the election, so size the stake accordingly',
                                   'Dennis Unrein / SMB PE LLC ([hDmKsEVGoBI @ 00:19:33])'],
                                  ['Form 8594 side-deal reporting for non-competes, licenses, and leases',
                                   'Report maximum consideration, for example $50K a year for 3 years '
                                   'equals $150K',
                                   'Match buyer and seller filings exactly so the IRS has nothing to catch',
                                   'Teach Me! Personal Finance ([G0f0r8tYMnk @ 00:09:15])'],
                                  ['Holdback at closing on a mid-size SMB deal',
                                   '$4M deal wires $3.5M at closing and holds back $0.5M from the seller',
                                   'Shift the burden of chasing recovery money onto the seller instead of '
                                   'yourself',
                                   'SMB Law Group LLP ([iNOj__jXGpE @ 00:10:09])'],
                                  ['Rep and warranty insurance pricing on SMB deals',
                                   'Example premium of $140K quoted against a $4M purchase price',
                                   'Compare premium cost against escrow and set-off before choosing a '
                                   'protection',
                                   'SMB Law Group LLP ([iNOj__jXGpE @ 00:14:25])'],
                                  ['SBA 7(a) financing and the buyer equity requirement',
                                   'SBA 7(a) covers 80% of price, so a $4M deal needs $800-900K of buyer '
                                   'cash',
                                   'Budget the full equity check plus working cash before committing to a '
                                   'deal',
                                   'SMB Law Group LLP ([iNOj__jXGpE @ 00:37:16])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Recovery and allocation moves the practitioners actually use',
                           'body': "These are the specific moves that keep a buyer's claim collectible and "
                                   "a seller's tax bill from blowing up the deal after the price is "
                                   'agreed.',
                           'items': ['Make the individual shareholders parties to the indemnity, or the '
                                     "seller's company empties its cash after closing and your claim is "
                                     'worthless [SMB Law Group LLP — iNOj__jXGpE @ 00:19:51]',
                                     'Do not use set-off against the seller note for a working-capital '
                                     "adjustment; set-off does not solve today's cash shortage [SMB Law "
                                     'Group LLP — iNOj__jXGpE @ 00:11:52]',
                                     'Negotiate the allocation and the down payment together, because a '
                                     'seller note only spreads the goodwill and inventory is completely '
                                     'ineligible for installment reporting [Hans Goldstein: Tax & Exit '
                                     'Planning — I8L23gqP5to @ 00:02:57]',
                                     'When the seller is a sole trader or partnership, set up a limited '
                                     'company with a similar name to buy the assets and expect painful '
                                     'bank account opening under money-laundering controls [Martin Godfrey '
                                     'Legido — 04Uy5gfO_PU @ 00:05:42]']},
               'sop_steps': [{'step': 1,
                              'title': 'Fix the structure in the LOI',
                              'action': 'Write asset or stock, plus any 338(h)(10), 336(e), or F reorg '
                                        'path, into the LOI before agreeing price.',
                              'detail': 'A silent LOI lets the buyer assume assets while the seller '
                                        'assumes stock, and the conversation is not productive post LOI, '
                                        'so pre-LOI is ideal [Dennis Unrein / SMB PE LLC — hDmKsEVGoBI @ '
                                        '00:01:23]'},
                             {'step': 2,
                              'title': 'Clear contracts, licenses, and consents',
                              'action': 'Inventory change-of-control clauses, assignability, leases, '
                                        'non-transferable licenses, landlord consents, and '
                                        'minority-shareholder consents.',
                              'detail': 'Change-of-control and assignability terms, plus licenses such as '
                                        'alcohol licenses, decide whether an asset deal can close or stock '
                                        'becomes the only route [Chris Barsness - Securities Law Media — '
                                        '-DthgkqGsGA @ 00:05:13]'},
                             {'step': 3,
                              'title': 'Stand up the buying entity',
                              'action': 'Form the new entity, file a DBA to keep the trade name, and plan '
                                        'the employee termination and rehire.',
                              'detail': "The buyer forms a new entity, the seller's entity is left hollow, "
                                        'and a DBA costs about $10, renewed roughly every 3 years [Walker '
                                        'Deibel — NM-ZwBNBHQE @ 00:09:29]'},
                             {'step': 4,
                              'title': 'Allocate, file, and lock protections',
                              'action': 'Agree a written allocation for matching Form 8594 filings, size '
                                        'the seller note at 10-15% to match the indemnity cap, and set '
                                        'escrow or holdback terms.',
                              'detail': 'Sizing the seller note at 10-15% so it matches the cap gives the '
                                        'buyer a set-off source equal to its maximum indemnity claim [SMB '
                                        'Law Group LLP — iNOj__jXGpE @ 00:34:44]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The loudest split is over which structure an operator should reach for '
                              'first. Martin Godfrey Legido, drawing on more than 30 years of deals, '
                              'prefers buying shares as the easier route: the customers, creditors, '
                              "suppliers and the bank account all come across in one move, and Legido's "
                              'bottom line is that the share purchase is easier from the administrative '
                              'side [04Uy5gfO_PU @ 00:08:32]. Walker Deibel runs the opposite default for '
                              'small buyers, stating that almost all lower middle market and Main Street '
                              'transactions are going to be an asset sale and not a stock sale, with the '
                              "buyer forming a new entity and leaving the seller's entity hollow "
                              '[NM-ZwBNBHQE @ 00:02:06]. Brett Cenkus frames the tension as a standing '
                              'conflict of interest: sellers want stock for capital gains, long-term after '
                              'one year and possibly no tax under QSBS, while buyers want assets so they '
                              'can re-depreciate at market value [ASUM5illI98 @ 00:01:56]. Cenkus adds a '
                              'street-level reason asset sales dominate listings: brokers tend to market '
                              'asset deals because they lack securities licenses, which means the '
                              "structure on the teaser can reflect the broker's licensing rather than the "
                              'best economics for either side [ASUM5illI98 @ 00:04:18]. Read every listing '
                              'with that bias in mind before accepting the default structure the broker '
                              'hands you.',
                              'Even asset-first buyers flip to stock when the deal forces it. Walker '
                              'Deibel lists the triggers: an essential contract or license that cannot '
                              'transfer, a minority equity investment, or a larger deal where the seller '
                              'retains 20% and the buyer takes 80% [NM-ZwBNBHQE @ 00:06:34]. Deibel then '
                              'shows the price lever: on a $100 price the seller nets $65 in an asset sale '
                              'versus $75 in a stock sale, so the buyer may only need to pay about $90 for '
                              'stock to leave the seller whole [NM-ZwBNBHQE @ 00:07:41]. Josh Siegel, a '
                              'CPA and tax attorney appearing with Dennis Unrein, argues the entity type '
                              'decides it: from a standalone C Corp, the seller pays 21% corporate tax and '
                              "then roughly another 21% on the distribution plus state tax, so if it's a "
                              "standalone C Corp it's quite hard to make the economics work, while S corps "
                              'and LLCs in the lower middle market generally do asset deals [hDmKsEVGoBI @ '
                              "00:12:19]. Siegel's alternative playbook is synthetic asset treatment "
                              'through 338(h)(10), 336(e) or an F reorg, with the hard rule that '
                              '338(h)(10) and 336(e) both require buying at least 80% of the stock within '
                              'one year, so a 70% or 79% purchase fails outright [hDmKsEVGoBI @ 00:19:33].',
                              'The deepest philosophical split is over whether the purchase agreement '
                              'itself protects you. David C Barnett calls representations and warranties '
                              'words on paper, pointing out that suing over a $10K problem costs too much, '
                              'and ranks protection number one as a good relationship with the seller and '
                              'number two as a seller note that can be offset, for example by skipping 10 '
                              'payments of $1,000 [LStVgWOM2LI @ 00:02:08]. Brett Cenkus treats reps as '
                              'the engineering of the deal: sellers give 15 to 30 reps, buyers give 4 to '
                              '10, reps are the basis for indemnity claims, and the real question they '
                              'answer is who carries the risk rather than which facts are true '
                              '[cnvG-qb6w9Q @ 00:05:51]. SMB Law Group LLP, closing roughly 130-plus deals '
                              'last year and trending toward 150, layers hard cash mechanisms on top: an '
                              'escrow that releases money only on joint instructions or a court order, a '
                              'holdback such as wiring $3.5M of a $4M deal and holding $0.5M to shift the '
                              'burden to the seller, and rep and warranty insurance at roughly a $140K '
                              'premium on a $4M deal [iNOj__jXGpE @ 00:10:09]. The operator choice comes '
                              'down to relationship plus note offset, or signed paper backed by parked '
                              'cash.'],
               'table': {'caption': 'Competing playbooks on structure, liabilities, tax treatment and '
                                    'buyer protection',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Default structure for a small acquisition',
                                   'Buy shares so customers, creditors, suppliers and the bank account '
                                   'transfer in one administrative move',
                                   'Buy assets, because almost all lower middle market and Main Street '
                                   'deals close as asset sales',
                                   'Martin Godfrey Legido ([04Uy5gfO_PU @ 00:08:32]); Walker Deibel '
                                   '([NM-ZwBNBHQE @ 00:02:06])'],
                                  ['What an asset buyer actually takes on',
                                   'Buyer acquires both the assets and the liabilities while the seller '
                                   'retains the legal entity',
                                   'Buyer picks specific liabilities to assume, such as a car loan, and '
                                   'leaves the rest behind',
                                   'Jeremy A. Johnson, CPA ([xVt6suFrCqE @ 00:00:16]); Chris Barsness - '
                                   'Securities Law Media ([-DthgkqGsGA @ 00:03:32])'],
                                  ['Whether old liabilities can really be left behind',
                                   'Old debts stay with the seller unless assumed, a de facto merger, mere '
                                   'continuation or fraudulent dodge',
                                   'Non-income taxes such as sales/use, payroll and gross receipts can '
                                   'still transfer to asset buyers',
                                   'Paper Rich ([Qqgfjq8CujE @ 00:01:11]); Tax Hack Accounting Group '
                                   '([Wd1__Z4Nz6k @ 00:03:07])'],
                                  ['Capturing asset-style tax benefits in a stock deal',
                                   'Use a 338(h)(10), 336(e) or F reorg after buying at least 80% of stock '
                                   'within one year',
                                   'Pay less for stock, around $90 instead of $100, because the seller '
                                   'nets more after tax',
                                   'Dennis Unrein / SMB PE LLC ([hDmKsEVGoBI @ 00:19:33]); Walker Deibel '
                                   '([NM-ZwBNBHQE @ 00:07:41])'],
                                  ['Key contracts that resist transfer to a buyer',
                                   'Anti-assignment clauses in critical contracts push the deal toward a '
                                   'stock purchase structure',
                                   'Consents may be needed even in share deals, so identify every '
                                   'third-party consent early',
                                   'Brett Cenkus ([ASUM5illI98 @ 00:04:53]); Thomas Efraim LLP '
                                   '([l2gJwZbVVnc @ 00:01:08])'],
                                  ['Primary buyer protection after the closing',
                                   'Seller relationship first, then an offsettable seller note, because '
                                   'suing over $10K costs too much',
                                   'Escrow on joint instructions, a holdback and rep and warranty '
                                   'insurance on larger deals',
                                   'David C Barnett Small Business and Deal Making SMB ([LStVgWOM2LI @ '
                                   '00:02:08]); SMB Law Group LLP ([iNOj__jXGpE @ 00:10:09])'],
                                  ['Why an operator buys assets in the first place',
                                   'Asset stripping: buy undervalued plant, machinery or trucks, refurbish '
                                   'and resell, hold property in a prop co',
                                   'Buy assets to run the business when the seller is a sole trader or '
                                   'partnership',
                                   'Martin Godfrey Legido ([04Uy5gfO_PU @ 00:03:18]); Martin Godfrey '
                                   'Legido ([04Uy5gfO_PU @ 00:05:42])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive trap is winning a claim you cannot collect. SMB Law '
                              'Group LLP warns that if the individual shareholders are not parties to the '
                              "indemnity, the seller's company empties its cash after closing and the "
                              'claim is worthless; the first avenue of recovery is making sure the person '
                              'with the money is someone you actually have a claim back against '
                              '[iNOj__jXGpE @ 00:19:51]. The same firm flags that set-off against the '
                              "seller note, the most common recovery tool, does not solve today's cash "
                              'shortage, and that using it for a working-capital adjustment is a mistake '
                              "to avoid [iNOj__jXGpE @ 00:11:52]. David C Barnett's pizzeria buyer lived "
                              'the set-off play: the seller note was 40% of the deal, and the buyer '
                              'stopped paying when cash sales came in short of what the seller had claimed '
                              '[LStVgWOM2LI @ 00:06:26]. Barnett also reports the harder loss: hidden '
                              'damage to an architect relationship that had no way to be valued as a '
                              'claim, so neither a rep nor a note offset could recover it [LStVgWOM2LI @ '
                              '00:07:18]. The economics check is identical in every case: a claim only has '
                              'real value when money is already parked in escrow or a holdback, or is '
                              'still owed to the seller on a note you control.',
                              'Tax surprises land late and wreck the agreed price. Josh Siegel warns that '
                              'a silent LOI lets the buyer assume an asset deal while the seller assumes a '
                              'stock deal, and recalls a roughly $60M deal where the seller questioned the '
                              "after-tax cash late in the process; the rule is that it's not a productive "
                              'conversation to have post LOI, so pre-LOI is ideal [hDmKsEVGoBI @ '
                              '00:28:08]. Thomas Efraim LLP sketches the same collapse: the buyer later '
                              'proposes an asset purchase to avoid historical corporate liabilities after '
                              'the price is agreed, so the economics must be revisited from scratch '
                              '[l2gJwZbVVnc @ 00:00:50]. On the seller side, Tax Hack Accounting Group '
                              'notes an asset sale computes gain asset by asset, with depreciation '
                              'recapture, cash-basis accounts receivable and inventory taxed at higher '
                              'ordinary rates [Wd1__Z4Nz6k @ 00:01:01]. Hans Goldstein adds the '
                              'installment trap: inventory sits in Class IV as ordinary income and is '
                              'completely ineligible for installment reporting, so a seller note only '
                              'spreads the goodwill, and allocation and down payment must be negotiated '
                              'together; the 2026 example runs a 72.0% gross profit ratio, a year-one '
                              'payment of $410,047, $201,600 of interest and a $956,482 gain [I8L23gqP5to '
                              '@ 00:02:19]. Sellers who assume the note defers everything get blindsided '
                              'at filing time.',
                              'The back-office traps hit after the wire clears. Teach Me! Personal Finance '
                              'warns that buyer and seller Form 8594 filings must match, or the IRS is '
                              'probably going to catch that, and that side deals for a non-compete, '
                              'license or lease must be reported at maximum consideration, such as $50K '
                              "per year over 3 years for $150K [G0f0r8tYMnk @ 00:05:35]. Siegel's "
                              'diligence warning is blunter: the biggest surprises come from not doing tax '
                              'diligence, because after Wayfair roughly $100,000 of sales into a state '
                              'creates economic nexus, and with no return filed the statute of limitations '
                              'never starts, while a VDA generally looks back 3 years and litigating a '
                              '$100K issue can cost $200K to $400K or more [hDmKsEVGoBI @ 00:38:06]. Paper '
                              "Rich adds a state-level landmine: in New York, skip the 10 days' notice to "
                              "the tax department and the buyer risks liability for the seller's sales tax "
                              '[Qqgfjq8CujE @ 00:01:30]. On the books, PwC US partner Beth Paul stresses '
                              'that the screen test is not optional, that a bargain purchase gain is not '
                              'recognized in an asset acquisition, and that the value of the long-lived '
                              'assets acquired is reduced instead, while transaction costs are capitalized '
                              'rather than expensed [b43cWRS8RKE @ 00:17:35].'],
               'table': {'caption': 'Firsthand traps, what went wrong, and the economics check that '
                                    'prevents a repeat',
                         'headers': ['Trap', 'What Went Wrong', 'Economics Check', 'Expert Source'],
                         'rows': [['Indemnity signed only by an empty shell entity',
                                   "Seller's company drained its cash after closing, leaving the indemnity "
                                   'claim worthless',
                                   'Make the individual shareholders parties to the indemnity before '
                                   'anyone signs',
                                   'SMB Law Group LLP ([iNOj__jXGpE @ 00:19:51])'],
                                  ['Spending withheld seller note payments during a dispute',
                                   'Pausing $11,000 monthly note payments on a $100K claim, then spending '
                                   'the withheld cash',
                                   'Pausing payments is the tactic; keep every withheld dollar untouched '
                                   'until resolution',
                                   'SMB Law Group LLP ([iNOj__jXGpE @ 00:22:03])'],
                                  ['Hidden damage that cannot be valued as a claim',
                                   'A damaged architect relationship surfaced after closing with no way to '
                                   'price it',
                                   'Suing over $10K costs too much, so lean on relationship and note '
                                   'offset',
                                   'David C Barnett Small Business and Deal Making SMB ([LStVgWOM2LI @ '
                                   '00:07:18])'],
                                  ['LOI that stays silent on tax structure',
                                   'Buyer assumed an asset deal, seller assumed stock, and after-tax cash '
                                   'was questioned late',
                                   'Write the tax structure into the LOI and bring tax advisors in pre-LOI',
                                   'Dennis Unrein / SMB PE LLC ([hDmKsEVGoBI @ 00:01:23])'],
                                  ['Supplier and customer pushback after an ownership change',
                                   'Suppliers got nervous after the change of owner and customers pushed '
                                   'for better prices',
                                   'Renegotiate supplier prices but budget for customer price pressure '
                                   'after the closing',
                                   'Martin Godfrey Legido ([04Uy5gfO_PU @ 00:02:25])'],
                                  ['Undervalued transfers in an asset purchase',
                                   'Every asset value needs accountant work and vendor agreement, and HMRC '
                                   'watches undervalue transfers',
                                   'Document each asset value with the accountant and vendor before the '
                                   'transfer happens',
                                   'Martin Godfrey Legido ([04Uy5gfO_PU @ 00:07:37])'],
                                  ['Mismatched Form 8594 allocations between buyer and seller',
                                   'Buyer and seller reported different allocations on their returns and '
                                   'the IRS catches it',
                                   'Agree one written allocation, which binds both sides, and file '
                                   'matching forms',
                                   'Teach Me! Personal Finance ([G0f0r8tYMnk @ 00:05:35]); Hans Goldstein: '
                                   'Tax & Exit Planning ([I8L23gqP5to @ 00:01:06])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Do Not Close Until These Four Clear',
                           'body': 'Each gate comes straight from a loss, reversal or late-stage blowup '
                                   'that practitioners reported firsthand. Clear all four before funds '
                                   'move.',
                           'items': ['Every selling shareholder signs the indemnity personally, and the '
                                     'seller note is sized at 10-15% so it matches the indemnity cap [SMB '
                                     'Law Group LLP — iNOj__jXGpE @ 00:34:44].',
                                     'Tax structure, including any 338(h)(10), 336(e) or F reorg path and '
                                     'the 80% stock threshold, is written into the LOI instead of left '
                                     'silent [Dennis Unrein / SMB PE LLC — hDmKsEVGoBI @ 00:01:23].',
                                     'Allocation and down payment are negotiated together, because '
                                     'inventory is ineligible for installment reporting and the seller '
                                     'note only spreads the goodwill [Hans Goldstein: Tax & Exit Planning '
                                     '— I8L23gqP5to @ 00:02:57].',
                                     'Every change-of-control clause, lease, landlord consent and '
                                     'non-transferable license, such as an alcohol license, is cleared '
                                     'before closing [Chris Barsness - Securities Law Media — -DthgkqGsGA '
                                     '@ 00:06:31].']}}],
 'pull_quote': '"The first avenue of recovery is making sure that the person with the money, you actually '
               'have a claim back against them." — SMB Law Group LLP (iNOj__jXGpE @ 00:19:51)',
 'diagram_id': 'diag-06',
 'action_checklist': ['Settle the deal structure early and involve tax advisors before price is agreed, '
                      'then document exactly which liabilities are assumed [Thomas Efraim LLP — '
                      'l2gJwZbVVnc @ 00:02:23].',
                      'Run tax diligence on every state where the target sells roughly $100,000 or more, '
                      'and cover exposure with a purchase price adjustment, escrow or indemnity [Dennis '
                      'Unrein / SMB PE LLC — hDmKsEVGoBI @ 00:37:14].',
                      'Make the individual shareholders parties to the indemnity so the claim survives the '
                      "seller's company emptying its cash [SMB Law Group LLP — iNOj__jXGpE @ 00:19:51].",
                      'When a claim is made, pause seller note payments, such as $11,000 per month against '
                      'a $100K claim, and do not spend the withheld money [SMB Law Group LLP — iNOj__jXGpE '
                      '@ 00:22:03].',
                      'Report non-compete, license or lease side deals on Form 8594 at maximum '
                      'consideration, such as $50K per year over 3 years for $150K [Teach Me! Personal '
                      'Finance — G0f0r8tYMnk @ 00:09:15].',
                      "On a New York deal, give the tax department 10 days' notice so the buyer does not "
                      "pick up the seller's sales tax [Paper Rich — Qqgfjq8CujE @ 00:01:30]."],
 'statutory_citations': [{'title': 'SMB Law Group LLP — Seller Financing and Set-Off Rights: Recovery '
                                   'Mechanisms in M&A Deals [00:19:51]',
                          'url': 'https://www.youtube.com/watch?v=iNOj__jXGpE&t=1191s',
                          'relevance': 'Primary practitioner testimony on indemnity parties, escrow, '
                                       'holdbacks, set-off against seller notes and SMB market terms.'},
                         {'title': 'Dennis Unrein / SMB PE LLC — M&A Tax Structuring 101: Asset vs. Stock '
                                   'Purchases, QSBS, and F-Reorgs Explained with Josh Siegel [00:19:33]',
                          'url': 'https://www.youtube.com/watch?v=hDmKsEVGoBI&t=1173s',
                          'relevance': 'Primary practitioner testimony on 338(h)(10), 336(e), F reorg '
                                       'mechanics, C Corp double tax and tax diligence.'},
                         {'title': 'Hans Goldstein: Tax & Exit Planning — Asset Sale Allocation: What '
                                   "Can't a Seller Note Spread? (2026) [00:02:19]",
                          'url': 'https://www.youtube.com/watch?v=I8L23gqP5to&t=139s',
                          'relevance': 'Primary practitioner testimony on binding allocations, inventory '
                                       'ineligibility for installment reporting and seller note limits.'},
                         {'title': 'Teach Me! Personal Finance — IRS Form 8594 walkthrough (Asset '
                                   'Acquisition Statement under IRC Section 1060) [00:05:35]',
                          'url': 'https://www.youtube.com/watch?v=G0f0r8tYMnk&t=335s',
                          'relevance': 'Primary practitioner testimony on Form 8594 matching, asset '
                                       'classes and maximum consideration for side deals.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '04Uy5gfO_PU',
                       'title': 'One Wrong Move, Scary Result: Asset Purchase vs Share Purchase',
                       'channel': 'Martin Godfrey Legido',
                       'author': 'Martin Godfrey Legido',
                       'text': 'I would recommend personally from the administrative side, the share '
                               'purchase is easier.',
                       'tip': 'I would recommend personally from the administrative side, the share '
                              'purchase is easier.',
                       'timestamp': 512,
                       'timestamp_seconds': 512,
                       'timestamp_label': '[00:08:32]',
                       'url': 'https://www.youtube.com/watch?v=04Uy5gfO_PU&t=512s',
                       'markdown': '[00:08:32](https://www.youtube.com/watch?v=04Uy5gfO_PU&t=512s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-DthgkqGsGA',
                       'title': 'Asset purchase or stock purchase?',
                       'channel': 'Chris Barsness - Securities Law Media',
                       'author': 'Chris Barsness - Securities Law Media',
                       'text': "Sellers prefer a stock deal because once it closes they're done, while "
                               'buyers prefer an asset deal so they can choose what to take and avoid '
                               'unknown liabilities.',
                       'tip': "Sellers prefer a stock deal because once it closes they're done, while "
                              'buyers prefer an asset deal so they can choose what to take and avoid '
                              'unknown liabilities.',
                       'timestamp': 117,
                       'timestamp_seconds': 117,
                       'timestamp_label': '[00:01:57]',
                       'url': 'https://www.youtube.com/watch?v=-DthgkqGsGA&t=117s',
                       'markdown': '[00:01:57](https://www.youtube.com/watch?v=-DthgkqGsGA&t=117s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NM-ZwBNBHQE',
                       'title': 'Asset Sale vs Stock Sale',
                       'channel': 'Walker Deibel',
                       'author': 'Walker Deibel',
                       'text': 'Almost all lower middle market and main street transactions are going to '
                               'be an asset sale and not a stock sale.',
                       'tip': 'Almost all lower middle market and main street transactions are going to be '
                              'an asset sale and not a stock sale.',
                       'timestamp': 126,
                       'timestamp_seconds': 126,
                       'timestamp_label': '[00:02:06]',
                       'url': 'https://www.youtube.com/watch?v=NM-ZwBNBHQE&t=126s',
                       'markdown': '[00:02:06](https://www.youtube.com/watch?v=NM-ZwBNBHQE&t=126s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iNOj__jXGpE',
                       'title': 'Seller Financing and Set-Off Rights: Recovery Mechanisms in M&A Deals',
                       'channel': 'SMB Law Group LLP',
                       'author': 'SMB Law Group LLP',
                       'text': 'The first avenue of recovery is making sure that the person with the '
                               'money, you actually have a claim back against them.',
                       'tip': 'The first avenue of recovery is making sure that the person with the money, '
                              'you actually have a claim back against them.',
                       'timestamp': 1191,
                       'timestamp_seconds': 1191,
                       'timestamp_label': '[00:19:51]',
                       'url': 'https://www.youtube.com/watch?v=iNOj__jXGpE&t=1191s',
                       'markdown': '[00:19:51](https://www.youtube.com/watch?v=iNOj__jXGpE&t=1191s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iNOj__jXGpE',
                       'title': 'Seller Financing and Set-Off Rights: Recovery Mechanisms in M&A Deals',
                       'channel': 'SMB Law Group LLP',
                       'author': 'SMB Law Group LLP',
                       'text': '89% of lower middle market deals per the Aquiem study have an escrow.',
                       'tip': '89% of lower middle market deals per the Aquiem study have an escrow.',
                       'timestamp': 2614,
                       'timestamp_seconds': 2614,
                       'timestamp_label': '[00:43:34]',
                       'url': 'https://www.youtube.com/watch?v=iNOj__jXGpE&t=2614s',
                       'markdown': '[00:43:34](https://www.youtube.com/watch?v=iNOj__jXGpE&t=2614s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Qqgfjq8CujE',
                       'title': 'Part 1 of Acquiring a Business (Asset purchase vs Stock purchase)',
                       'channel': 'Paper Rich',
                       'author': 'Paper Rich',
                       'text': "In New York, give the tax department 10 days' notice or you risk liability "
                               "for the seller's sales tax.",
                       'tip': "In New York, give the tax department 10 days' notice or you risk liability "
                              "for the seller's sales tax.",
                       'timestamp': 90,
                       'timestamp_seconds': 90,
                       'timestamp_label': '[00:01:30]',
                       'url': 'https://www.youtube.com/watch?v=Qqgfjq8CujE&t=90s',
                       'markdown': '[00:01:30](https://www.youtube.com/watch?v=Qqgfjq8CujE&t=90s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VBNjS7UATHo',
                       'title': 'What Exactly Are You Buying in an M&A Deal? Share Purchase vs Asset '
                                'Purchase #mergersandacquisitions',
                       'channel': 'Acquireman M&A',
                       'author': 'Acquireman M&A',
                       'text': 'If you acquire 100% of those shares, you become the owner of the company '
                               'itself.',
                       'tip': 'If you acquire 100% of those shares, you become the owner of the company '
                              'itself.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=VBNjS7UATHo&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=VBNjS7UATHo&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'G0f0r8tYMnk',
                       'title': 'IRS Form 8594 walkthrough (Asset Acquisition Statement under IRC Section '
                                '1060)',
                       'channel': 'Teach Me! Personal Finance',
                       'author': 'Teach Me! Personal Finance',
                       'text': "Both the buyer's and the seller's returns must match, or the IRS is "
                               'probably going to catch that.',
                       'tip': "Both the buyer's and the seller's returns must match, or the IRS is "
                              'probably going to catch that.',
                       'timestamp': 335,
                       'timestamp_seconds': 335,
                       'timestamp_label': '[00:05:35]',
                       'url': 'https://www.youtube.com/watch?v=G0f0r8tYMnk&t=335s',
                       'markdown': '[00:05:35](https://www.youtube.com/watch?v=G0f0r8tYMnk&t=335s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'I8L23gqP5to',
                       'title': "Asset Sale Allocation: What Can't a Seller Note Spread? (2026)",
                       'channel': 'Hans Goldstein: Tax & Exit Planning',
                       'author': 'Hans Goldstein: Tax & Exit Planning',
                       'text': 'It is completely ineligible for installment reporting.',
                       'tip': 'It is completely ineligible for installment reporting.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=I8L23gqP5to&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=I8L23gqP5to&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LStVgWOM2LI',
                       'title': 'Do Representations and Warranties have any value?  business broker vendor '
                                'financing seller financing',
                       'channel': 'David C Barnett Small Business and Deal Making SMB',
                       'author': 'David C Barnett Small Business and Deal Making SMB',
                       'text': 'The number one protection is a good relationship with the seller, and '
                               'number two is a seller note that can be offset.',
                       'tip': 'The number one protection is a good relationship with the seller, and '
                              'number two is a seller note that can be offset.',
                       'timestamp': 128,
                       'timestamp_seconds': 128,
                       'timestamp_label': '[00:02:08]',
                       'url': 'https://www.youtube.com/watch?v=LStVgWOM2LI&t=128s',
                       'markdown': '[00:02:08](https://www.youtube.com/watch?v=LStVgWOM2LI&t=128s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cnvG-qb6w9Q',
                       'title': 'Representations and Warranties in Mergers and Acquisitions (M&A)',
                       'channel': 'Brett Cenkus',
                       'author': 'Brett Cenkus',
                       'text': 'Sellers are usually liable jointly and severally, but a 5% passive holder '
                               'can be carved out and a contribution agreement splits the cost among '
                               'sellers.',
                       'tip': 'Sellers are usually liable jointly and severally, but a 5% passive holder '
                              'can be carved out and a contribution agreement splits the cost among '
                              'sellers.',
                       'timestamp': 450,
                       'timestamp_seconds': 450,
                       'timestamp_label': '[00:07:30]',
                       'url': 'https://www.youtube.com/watch?v=cnvG-qb6w9Q&t=450s',
                       'markdown': '[00:07:30](https://www.youtube.com/watch?v=cnvG-qb6w9Q&t=450s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ASUM5illI98',
                       'title': 'Merger & Acquisition (M&A) Deal Structures Explained',
                       'channel': 'Brett Cenkus',
                       'author': 'Brett Cenkus',
                       'text': 'Generally speaking, sellers want to sell stock, and buyers want to buy '
                               'assets.',
                       'tip': 'Generally speaking, sellers want to sell stock, and buyers want to buy '
                              'assets.',
                       'timestamp': 116,
                       'timestamp_seconds': 116,
                       'timestamp_label': '[00:01:56]',
                       'url': 'https://www.youtube.com/watch?v=ASUM5illI98&t=116s',
                       'markdown': '[00:01:56](https://www.youtube.com/watch?v=ASUM5illI98&t=116s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'b43cWRS8RKE',
                       'title': 'Fixed asset toolkit: Asset acquisitions',
                       'channel': 'PwC US',
                       'author': 'PwC US',
                       'text': 'The screen test is not optional.',
                       'tip': 'The screen test is not optional.',
                       'timestamp': 540,
                       'timestamp_seconds': 540,
                       'timestamp_label': '[00:09:00]',
                       'url': 'https://www.youtube.com/watch?v=b43cWRS8RKE&t=540s',
                       'markdown': '[00:09:00](https://www.youtube.com/watch?v=b43cWRS8RKE&t=540s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Wd1__Z4Nz6k',
                       'title': 'Difference Between a Stock and an Asset Purchase in an M&A',
                       'channel': 'Tax Hack Accounting Group',
                       'author': 'Tax Hack Accounting Group',
                       'text': 'You are inheriting the historic liabilities, all historic liabilities of '
                               'that entity.',
                       'tip': 'You are inheriting the historic liabilities, all historic liabilities of '
                              'that entity.',
                       'timestamp': 207,
                       'timestamp_seconds': 207,
                       'timestamp_label': '[00:03:27]',
                       'url': 'https://www.youtube.com/watch?v=Wd1__Z4Nz6k&t=207s',
                       'markdown': '[00:03:27](https://www.youtube.com/watch?v=Wd1__Z4Nz6k&t=207s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xVt6suFrCqE',
                       'title': 'Asset Sale vs. Stock Sale: Buyer vs. Seller Preference Explained',
                       'channel': 'Jeremy A. Johnson, CPA',
                       'author': 'Jeremy A. Johnson, CPA',
                       'text': "You don't want to make these decisions when the buyer is in the room.",
                       'tip': "You don't want to make these decisions when the buyer is in the room.",
                       'timestamp': 157,
                       'timestamp_seconds': 157,
                       'timestamp_label': '[00:02:37]',
                       'url': 'https://www.youtube.com/watch?v=xVt6suFrCqE&t=157s',
                       'markdown': '[00:02:37](https://www.youtube.com/watch?v=xVt6suFrCqE&t=157s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hDmKsEVGoBI',
                       'title': 'M&A Tax Structuring 101: Asset vs. Stock Purchases, QSBS, and F-Reorgs '
                                'Explained with Josh Siegel',
                       'channel': 'Dennis Unrein / SMB PE LLC',
                       'author': 'Dennis Unrein / SMB PE LLC',
                       'text': 'The biggest surprises can come out of not doing tax diligence.',
                       'tip': 'The biggest surprises can come out of not doing tax diligence.',
                       'timestamp': 2217,
                       'timestamp_seconds': 2217,
                       'timestamp_label': '[00:36:57]',
                       'url': 'https://www.youtube.com/watch?v=hDmKsEVGoBI&t=2217s',
                       'markdown': '[00:36:57](https://www.youtube.com/watch?v=hDmKsEVGoBI&t=2217s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hDmKsEVGoBI',
                       'title': 'M&A Tax Structuring 101: Asset vs. Stock Purchases, QSBS, and F-Reorgs '
                                'Explained with Josh Siegel',
                       'channel': 'Dennis Unrein / SMB PE LLC',
                       'author': 'Dennis Unrein / SMB PE LLC',
                       'text': "If it's a standalone C Corp it's quite hard to make the economics work.",
                       'tip': "If it's a standalone C Corp it's quite hard to make the economics work.",
                       'timestamp': 739,
                       'timestamp_seconds': 739,
                       'timestamp_label': '[00:12:19]',
                       'url': 'https://www.youtube.com/watch?v=hDmKsEVGoBI&t=739s',
                       'markdown': '[00:12:19](https://www.youtube.com/watch?v=hDmKsEVGoBI&t=739s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'l2gJwZbVVnc',
                       'title': 'Asset Sale or Share Sale? Understanding Two Very Different Ways to Sell a '
                                'Business',
                       'channel': 'Thomas Efraim LLP',
                       'author': 'Thomas Efraim LLP',
                       'text': 'The headline price is only one part of a business sale.',
                       'tip': 'The headline price is only one part of a business sale.',
                       'timestamp': 162,
                       'timestamp_seconds': 162,
                       'timestamp_label': '[00:02:42]',
                       'url': 'https://www.youtube.com/watch?v=l2gJwZbVVnc&t=162s',
                       'markdown': '[00:02:42](https://www.youtube.com/watch?v=l2gJwZbVVnc&t=162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
