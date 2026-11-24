from __future__ import annotations

CHAPTER_7 = {'id': 'Q7',
 'chapter_id': 'Q7',
 'chapter_number': 7,
 'question_number': 7,
 'slug': 'asset-based-lending-and-supply-chain-finance',
 'question_prompt': 'How do asset-based lending facilities and supply chain or trade finance unlock '
                    'working capital tied up in receivables, inventory, and goods in transit?',
 'kicker': 'Q7 / THE BIG MONEY PLAYBOOKS',
 'title': 'Asset-Based Lending and Supply Chain Finance',
 'subtitle': 'Borrowing Base Facilities, ABL Primers and Institutional Asset-Based Finance, Pledging vs. '
             'Factoring vs. Secured Borrowing, Inventory and Import/Export Finance, Trade Finance vs. '
             'Supply Chain Finance, Reverse Factoring for Supplier Liquidity, and the Evolution of SCF',
 'layout_template': 'thirty_day_roadmap',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one diagnosis: profitable companies starve because cash '
                      'leaves before receivables and inventory turn back into cash, and asset-based tools '
                      'monetize that trapped working capital. ABL lenders size availability off a '
                      'borrowing base, eligible AR and inventory times advance rates minus reserves, '
                      'underwriting to liquidation rather than face value. SG Credit Partners walks a '
                      'sample base: 85-cent AR advances, a 25% concentration threshold, finished goods at '
                      'the lesser of 65 cents or 85% of NOLV. Supply chain finance flips the credit: the '
                      "supplier funds at the buyer's 2% instead of its own 12%. On the street, factoring "
                      'brokers earn 10-15% of a roughly 2.5-3% monthly fee. Speakers split on inventory '
                      'financing as a last resort, bank versus non-bank pricing, and whether factoring or '
                      'pledging belongs on the balance sheet.',
 'key_metrics': [{'label': 'ABL Concentration Threshold',
                  'metric': 'ABL Concentration Threshold',
                  'value': '25% per customer',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Evan Wagner of SG Credit Partners says most lenders implement a 25% '
                             'concentration threshold; in his sample borrowing base the cap stripped about '
                             '11% of AR after past-due ineligibles removed 9%.',
                  'source': 'Naturally New York ([oobK7A-p9-U @ 00:33:42])'},
                 {'label': 'ABL Receivables Advance Rate',
                  'metric': 'ABL Receivables Advance Rate',
                  'value': '85 cents on the dollar (586 net eligible AR yields 498)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Wagner's Michael Scott Paper Co. borrowing base applies an 85-cent advance "
                             'to net eligible AR after aging and concentration cuts.',
                  'source': 'Naturally New York ([oobK7A-p9-U @ 00:39:00])'},
                 {'label': 'Factoring Broker Commission',
                  'metric': 'Factoring Broker Commission',
                  'value': '10-15% of the factoring fee ($300-$450/month on a $3,000 monthly fee)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Bob McMahon of Aegis Factors describes a 10% industry-standard commission '
                             'paid on a 10-15% sliding grid against a typical fee of about 2.5% per 30 '
                             'days.',
                  'source': 'Simon White (SEO, AEO & Digital & Marketing) ([G9RrpSanefM @ 00:31:19])'},
                 {'label': 'SCF Credit Arbitrage Spread',
                  'metric': 'SCF Credit Arbitrage Spread',
                  'value': 'Supplier 12% bank rate vs. buyer 2% rate',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Vanijja's example of a supplier burdened with a 12% bank loan funding itself "
                             "at its buyer's 2% rate through supply chain finance, likened to co-signing.",
                  'source': 'Vanijja | Trade Insights ([RcVypdN4SHs @ 00:04:08])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner starts from the same wound: the business is profitable '
                              'on paper and broke at the bank. Financely Group frames it bluntly, cash '
                              'goes out upfront for operations while revenue sits trapped in receivables, '
                              'and asset-based lending exists to monetize receivables and inventory before '
                              'customers pay [xY3rD_awSEg @ 00:00:13]. Vanijja calls the belief that '
                              'profit equals cash a classic mistake and teaches the cash conversion cycle '
                              'as the real scoreboard [kMiyyMuSUDU @ 00:01:21]. Natasha Condon of '
                              'JPMorgan, with roughly two decades in the business, reduces the whole '
                              'supply chain finance industry to one tension: somebody wants to pay as late '
                              'as possible and somebody wants to get paid as quick as possible '
                              '[ltw4tGEw31o @ 00:01:25]. Shane Walton of the Commercial Loan Broker '
                              'Institute, whose firm has supported more than 400 brokerages, names the '
                              'same gap the cash clock, the stretch between paying cash out and collecting '
                              'it back, and trains brokers to hunt it [4fxpQTB_spA @ 00:04:21]. The '
                              'consensus prerequisite follows directly: the client must have real '
                              'receivables, real inventory, or a creditworthy buyer whose obligations can '
                              "be financed. Lenders and factors are not funding the founder's story; they "
                              'are buying or lending against the timing gap itself, and they price that '
                              'gap off whoever is most likely to pay.',
                              'On asset-based lending specifically, the speakers agree that collateral, '
                              'not the income statement, drives the deal. Financely Group contrasts the '
                              'ABL revolver, collateral-focused with formula-driven availability that '
                              'fluctuates, against the cash-flow loan built on enterprise value and EBITDA '
                              'with a fixed commitment and periodic tests, and says lenders underwrite '
                              'collectibility rather than face value by tracking aging, dilution and '
                              'cross-aging [xY3rD_awSEg @ 00:00:26]. Evan Wagner of SG Credit Partners, a '
                              'family-office lender to high-growth consumer brands, puts it harder: '
                              'asset-based lenders are underwriting to a liquidation, to a worst-case '
                              'scenario [oobK7A-p9-U @ 00:34:49]. FinanceKid draws the usage boundary: ABL '
                              'is working-capital money for companies too leveraged or too small for more '
                              'bank debt in cyclical sectors like steel, retail and transportation, it is '
                              'usually closed within twelve months, and it is not used to finance '
                              'long-term operations [u5hujmtiiaY @ 00:01:32]. On controls, Wagner says '
                              'every asset-based lender will require a collections-account sweep or '
                              'lockbox, and his stack adds a CPA-run field exam and an NOLV appraisal on '
                              'inventory [oobK7A-p9-U @ 00:51:11]. Financely lists the same machinery: the '
                              'borrowing base certificate as the primary control document, blocked '
                              'accounts with active or triggered dominion, and field exams to catch fraud. '
                              'Financely sets the disqualifier: weak asset quality or reporting the '
                              'borrower cannot support makes ABL the wrong tool.',
                              "The supply chain finance camp agrees on a different engine: the buyer's "
                              'credit does the heavy lifting. Supply Chain Finance Academy builds the '
                              "whole technique on the buyer's irrevocable payment undertaking, contrasting "
                              'it with letters of credit and export credit insurance that are complex, '
                              "multi-party and may demand collateral [Db19fMNKoJY @ 00:01:17]. Vanijja's "
                              'credit-arbitrage example shows the payoff: a supplier stuck with a 12% bank '
                              'loan funds itself at the 2% rate its strong buyer enjoys, which the speaker '
                              "likens to co-signing [RcVypdN4SHs @ 00:04:08]. The same channel's cash-flow "
                              'episode lays out the two-sided trade: the buyer stretches terms from 30 to '
                              '60, 90 or 120 days and improves DPO, while the supplier gets paid on day '
                              "one or two, priced off the buyer's rating [kMiyyMuSUDU @ 00:05:56]. "
                              'Eslatainment walks a four-step reverse factoring flow through Liberte: the '
                              'supplier submits an electronic invoice, the buyer approves online, the '
                              'supplier receives a significant portion often within 24 hours, and the '
                              'buyer repays on the agreed date while Liberte handles collections '
                              '[3Y7TjakDREI @ 00:02:05]. Vanijja also separates the instruments: trade '
                              'finance underwrites one shipment at a time and can fund pre-shipment, while '
                              'supply chain finance funds a continuous flow of approved invoices after '
                              'shipment.'],
               'table': {'caption': 'Where the practitioners line up on asset-based lending and supply '
                                    'chain finance',
                         'headers': ['Consensus Point',
                                     'What the Practitioners Report',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Profit on paper is not cash in the bank',
                                   'Cash leaves upfront for operations while revenue stays trapped in '
                                   'receivables until customers pay',
                                   'Diagnose the timing gap before pitching any facility to the business '
                                   'owner',
                                   'Financely Group ([xY3rD_awSEg @ 00:00:13])'],
                                  ['ABL underwrites to liquidation value, not EBITDA',
                                   'Asset-based lenders underwrite to a liquidation and a worst-case '
                                   'scenario on the collateral',
                                   'Expect availability to track what the collateral would fetch in a '
                                   'wind-down',
                                   'Naturally New York ([oobK7A-p9-U @ 00:34:49])'],
                                  ['Collectibility beats face value on every invoice',
                                   'Lenders track aging, dilution and cross-aging and exclude stale or '
                                   'disputed invoices',
                                   'Clean the aging report before submission so ineligibles do not gut the '
                                   'base',
                                   'Financely Group ([xY3rD_awSEg @ 00:01:08])'],
                                  ['ABL is short-term working capital money only',
                                   'Not used to finance long-term operations and usually closed within '
                                   'twelve months',
                                   'Pitch ABL for cycle gaps, growth, acquisitions and seasonal builds, '
                                   'not long-term operations',
                                   'FinanceKid ([u5hujmtiiaY @ 00:01:32])'],
                                  ["The buyer's credit powers supply chain finance",
                                   "SCF rests on the buyer's irrevocable payment undertaking instead of "
                                   'supplier collateral',
                                   'Target suppliers selling to strong, highly rated buyers that approve '
                                   'invoices online',
                                   'Supply Chain Finance Academy ([Db19fMNKoJY @ 00:01:17])'],
                                  ['Both sides of payables finance come out ahead',
                                   'Buyers extend terms to 60, 90 or 120 days while suppliers get paid on '
                                   'day one or two',
                                   'Sell the buyer on DPO and the supplier on DSO in the same conversation',
                                   'Vanijja | Trade Insights ([kMiyyMuSUDU @ 00:05:56])'],
                                  ['Lender control of collections is universal',
                                   'Every asset-based lender will require a collections-account sweep or '
                                   'lockbox on remittances',
                                   'Warn clients upfront that customer payments will route through '
                                   'lender-controlled accounts',
                                   'Naturally New York ([oobK7A-p9-U @ 00:51:11])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Evan Wagner walks a full borrowing base through his Michael Scott Paper Co. '
                              'example. AR more than 30 days past due is ineligible and strips 9% of the '
                              'pool, then a concentration cap removes about 11% more, since most lenders '
                              'implement a 25% concentration threshold [oobK7A-p9-U @ 00:33:19]. Net '
                              'eligible AR of 586 at an 85-cent advance yields 498. Finished goods advance '
                              'at the lesser of 65 cents or 85% of NOLV, raw materials up to about 50%, '
                              'and work in process and packaging get nothing; inventory sitting at small '
                              'locations like Nashua and Utica is ineligible. The base totals $832K '
                              'against a $1M cap, less a $42K AP reserve, for $790K, leaving $162K of '
                              'excess availability [oobK7A-p9-U @ 00:45:24]. Financely Group states the '
                              'same formula in one line: eligible receivables plus inventory, times '
                              'advance rates, minus reserves, with net availability the lesser of the base '
                              'or total commitments, and inventory must be saleable and unencumbered '
                              '[xY3rD_awSEg @ 00:00:40]. FinanceKid quotes the inventory advance as '
                              'usually 80% of net orderly liquidation value, below market value, and pairs '
                              'it with invoice factoring [u5hujmtiiaY @ 00:13:38]. Wagner then measures '
                              'liquidity as excess availability plus cash against burn: most lenders want '
                              'twelve months of historical burn covered, and three months is a tough call.',
                              'Pricing is quoted openly. FinanceKid prices recourse factoring at up to 90% '
                              'of eligible receivables aged 90 days or less: on $1,000 of invoices, $900 '
                              'is advanced, a 5% fee costs $45, and $55 comes back after 20 days. '
                              'Non-recourse drops to 70 to 80% with higher fees, so the same $1,000 '
                              'advances $700, carries a $105 fee at 15%, and rebates $195 [u5hujmtiiaY @ '
                              '00:04:44]. Purchase order advances hinge on the customer, not the borrower: '
                              '90% for a safe customer, 70 to 80% for a riskier one, with a 7% fee in the '
                              'worked example [u5hujmtiiaY @ 00:08:59]. Bob McMahon of Aegis Factors puts '
                              'typical factoring near 2.5% per 30 days and frames 3% on $100K, or $3,000, '
                              'as comparable to the $2,000 to $2,500 a merchant pays in Visa fees '
                              "[G9RrpSanefM @ 00:30:40]. Wagner's ABL grid runs wider: non-banks from "
                              'Prime plus zero, even Prime minus one, up to Prime plus 10 or 15; banks at '
                              'SOFR plus 2 to 4% or Prime minus 2 to Prime flat; revenue-based financing '
                              'at 10% to 25 or 30% and up; venture debt at 15 to 25% with PIK and warrants '
                              '[oobK7A-p9-U @ 00:56:44]. Committed facilities cost more than demand notes, '
                              'and covenants can include minimum EBITDA, revenue, DSCR, FCCR and '
                              'liquidity.',
                              'For brokers, Shane Walton teaches a four-move playbook: ask timeline '
                              'questions, find the stuck link in the cash clock, match the tool, and '
                              'package the deal [4fxpQTB_spA @ 00:11:24]. He maps tools to zones: PO or '
                              'contract financing and vendor terms at the front of the chain, a '
                              'working-capital line or equipment financing mid-process, and AR financing '
                              'or factoring, which he calls selling an asset, at the back. His document '
                              'stacks are specific: factoring needs the aging report, invoices, '
                              'concentration, proof of delivery and disputes; PO financing needs the PO, '
                              'quotes, margins and plan; a line of credit needs financials, bank '
                              'statements, tax returns and use of proceeds [4fxpQTB_spA @ 00:13:58]. '
                              'McMahon runs the referral version: network through the Chamber of Commerce, '
                              'organizations and social media, spot the cash-flow problem, then set up a '
                              'conference call with an underwriter, and route the deal to a factor, '
                              'merchant cash advance, purchase order funder or equipment lessor '
                              '[G9RrpSanefM @ 00:23:28]. The factor does all the selling and contracting. '
                              'His economics: a 10% industry-standard commission, 10 to 15% on a sliding '
                              'grid, so a $3,000 monthly fee pays the broker $300 to $450 a month, and '
                              'about $2M a month across 10 to 20 small clients generates six figures '
                              '[G9RrpSanefM @ 00:31:19].'],
               'table': {'caption': 'Advance rates, pricing and mechanics quoted by the practitioners',
                         'headers': ['Instrument', 'Advance or Price', 'Mechanic', 'Expert Source'],
                         'rows': [['ABL revolver against accounts receivable',
                                   '85 cents on 586 of net eligible AR yields 498 of availability',
                                   'Strip AR over 30 days past due and concentrations above 25% first',
                                   'Naturally New York ([oobK7A-p9-U @ 00:39:00])'],
                                  ['ABL advance against finished goods inventory',
                                   'Lesser of 65 cents or 85% of NOLV; raw materials about 50%',
                                   'WIP, packaging and inventory at small locations are excluded from the '
                                   'base',
                                   'Naturally New York ([oobK7A-p9-U @ 00:43:00])'],
                                  ['Recourse invoice factoring on small receivables',
                                   'Up to 90% of eligible AR; 5% fee on a $900 advance is $45',
                                   'Only invoices aged 90 days or less count; $55 rebated after 20 days',
                                   'FinanceKid ([u5hujmtiiaY @ 00:04:44])'],
                                  ['Non-recourse invoice factoring with credit protection',
                                   '70 to 80% advance; 15% fee of $105 on a $700 advance',
                                   'Higher fees for shifting customer credit risk; $195 rebated on $1,000 '
                                   'of AR',
                                   'FinanceKid ([u5hujmtiiaY @ 00:05:34])'],
                                  ['Inventory financing line paired with factoring',
                                   'About 80% of NOLV at Prime plus 4 to 6% plus warehousing',
                                   'Lender audits every three to six months; high DIO risks default',
                                   'FinanceKid ([u5hujmtiiaY @ 00:18:04])'],
                                  ['Small-business factoring sourced by a broker',
                                   'About 2.5% per 30 days; 3% on $100K equals $3,000 a month',
                                   'Broker earns 10 to 15% of the monthly fee on a sliding grid',
                                   'Simon White (SEO, AEO & Digital & Marketing) ([G9RrpSanefM @ '
                                   '00:30:40])'],
                                  ['Non-bank ABL facility for scaled consumer brands',
                                   'Prime plus 3 to 8, or 10 to 15% total yield with Prime at 8.5%',
                                   'Quoted as total-yield shorthand alongside the Prime plus zero to plus '
                                   '15 range',
                                   'Naturally New York ([oobK7A-p9-U @ 01:03:06])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the operators do before the lender ever sees the file',
                           'body': 'Four moves the practitioners use to protect availability, price the '
                                   'deal off the strongest credit, and get paid on the referral.',
                           'items': ['Scrub the aging report before the lender does: AR more than 30 days '
                                     "past due killed 9% of Wagner's pool and the concentration cap took "
                                     'about 11% more [Naturally New York — oobK7A-p9-U @ 00:33:19]',
                                     "Pitch PO and factoring advances off the end customer's certainty of "
                                     "payment, not the borrower's credit, because that is what sets the "
                                     '90% versus 70-80% advance [FinanceKid — u5hujmtiiaY @ 00:08:59]',
                                     'Check vendor terms first: Walton calls trade credit often the '
                                     'cheapest capital if it is available because the client is simply '
                                     'extending payables [Commercial Loan Broker Institute — 4fxpQTB_spA @ '
                                     '00:06:12]',
                                     "Sell suppliers the credit arbitrage: funding at the buyer's 2% "
                                     'instead of a 12% bank loan, which Vanijja likens to the buyer '
                                     'co-signing [Vanijja | Trade Insights — RcVypdN4SHs @ 00:04:08]']},
               'sop_steps': [{'step': 1,
                              'title': 'Run the timing audit',
                              'action': 'Ask timeline questions to find where cash sits stuck between '
                                        'paying out and collecting.',
                              'detail': 'Walton closes prospects with a 5-question timing audit that maps '
                                        'the cash clock and locates the stuck link before any product is '
                                        'named [Commercial Loan Broker Institute — 4fxpQTB_spA @ '
                                        '00:14:55]'},
                             {'step': 2,
                              'title': 'Pull the matching document stack',
                              'action': 'Collect the exact package for the tool that fits the stuck link.',
                              'detail': 'Factoring needs the aging report, invoices, concentration, proof '
                                        'of delivery and disputes; PO financing needs the PO, quotes, '
                                        'margins and plan; a line of credit needs financials, bank '
                                        'statements, tax returns and use of proceeds [Commercial Loan '
                                        'Broker Institute — 4fxpQTB_spA @ 00:13:58]'},
                             {'step': 3,
                              'title': 'Model the borrowing base',
                              'action': 'Build a pro forma base: eligible AR and inventory times advance '
                                        'rates, minus reserves.',
                              'detail': 'Financely prepares borrowers with a readiness review plus a '
                                        'borrowing base model so availability and reporting capacity are '
                                        "known before the lender's field exam [Financely Group — "
                                        'xY3rD_awSEg @ 00:02:44]'},
                             {'step': 4,
                              'title': 'Route the deal and lock the commission',
                              'action': 'Put the client on a call with an underwriter and let the funder '
                                        'sell and contract.',
                              'detail': 'McMahon sets up a conference call with an underwriter, routes to '
                                        'a factor, MCA, PO funder or equipment lessor, and the broker '
                                        'collects 10-15% of the monthly fee [Simon White (SEO, AEO & '
                                        'Digital & Marketing) — G9RrpSanefM @ 00:22:49]'}]},
              {'number': 3,
               'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Collateral formula versus enterprise value is the first fork. Financely '
                              'Group frames it bluntly: the ABL revolver is collateral-focused with '
                              'formula-driven availability that fluctuates, while the cash-flow loan rests '
                              'on enterprise value and EBITDA with a fixed commitment and periodic tests '
                              '[xY3rD_awSEg @ 00:00:26]. Evan Wagner of SG Credit Partners splits the '
                              'lender side the same way and adds the price tag: once a company is scaled '
                              'and profitable, bank term sheets come in cheaper, while non-banks are '
                              'pricier but more aggressive [oobK7A-p9-U @ 00:17:36]. His quoted spreads '
                              'run SOFR+2-4% or Prime-2 to Prime+0 at banks, versus non-bank paper '
                              'anywhere from Prime+0, even Prime-1, up to Prime+10 or Prime+15 '
                              '[oobK7A-p9-U @ 00:56:44]. FinanceKid sets the benchmark further down the '
                              'capital stack: an ABL facility is usually cheaper than high-yield debt or '
                              'mezzanine financing and dodges dilutive warrant kickers [u5hujmtiiaY @ '
                              "00:25:02]. Wagner's own rate card backs that contrast, putting venture debt "
                              'at 15-25% with PIK interest and warrants and revenue-based financing at 10% '
                              'to 25-30% or more. The operator read: bank ABL wins on price for clean, '
                              'scaled borrowers; non-bank ABL wins on aggressiveness; venture debt is '
                              'sized to the equity-raise valuation and revenue-based money and MCAs to the '
                              'top line, not to liquidatable receivables and inventory.',
                              'Sale or loan is the second fault line, and the accounting instructors and '
                              'the working-capital practitioners draw it differently. Vanijja sorts '
                              'receivables purchase into an off-balance-sheet bucket, while loan-based '
                              'solutions show up on the books as debt [kMiyyMuSUDU @ 00:04:57]. FinanceKid '
                              'prices the same choice in advance rates: recourse deals advance up to 90% '
                              'of eligible AR aged 90 days or less, while non-recourse drops to 70-80% '
                              'with higher fees. On $1,000 of AR that is $900 advanced with a 5% fee of '
                              '$45 and $55 rebated after 20 days, versus $700 advanced with a 15% fee of '
                              '$105 and $195 rebated [u5hujmtiiaY @ 00:04:44]. Mike Brown on Mar T warns '
                              'that recourse muddies the sale label: a with-recourse transfer counts as a '
                              'sale only if the obligation can be estimated, control is relinquished, and '
                              'no forced repurchase is possible; otherwise it is a loan, though replacing '
                              'bad receivables is allowed [PPTyFBcPTUw @ 00:06:44]. Farhat Lectures '
                              'supplies the horror case from 2007-08: Lehman Brothers pledged poor-quality '
                              'CDOs but recorded the transactions as sales, dodging large unrealized-loss '
                              'write-downs on mortgage-backed assets until the fraud surfaced and, in the '
                              "lecturer's words, brought the whole market with it [j1xpasTho-0 @ "
                              '00:10:50]. Operator takeaway: label the structure correctly before quoting '
                              'any advance rate to a client.',
                              'Trade finance versus supply chain finance splits the tool kit, and the '
                              'practitioners disagree on timing and on how digital the business really is. '
                              'Vanijja draws the timing line: trade finance can fund pre-shipment against '
                              'the purchase contract with security over cargo or insurance, while SCF '
                              'funds post-shipment only once the invoice is approved, reviewing a '
                              'continuous flow of invoices instead of one shipment at a time [RcVypdN4SHs '
                              '@ 00:03:19]. Shane Walton of the Commercial Loan Broker Institute pushes '
                              'brokers further upstream: at the front of the chain PO or contract '
                              'financing works, but vendor terms or trade credit is often the cheapest '
                              "capital if it's available because you're extending your payables "
                              '[4fxpQTB_spA @ 00:06:12]. On delivery channels the Trade Finance Global '
                              'panel splits. Susan reports risk skittishness pushing a return toward '
                              'documentary and unfunded products, with hybrid digital-documentary models '
                              'emerging [LlAxD5FEW5Q @ 00:02:19], while Brian expects no two-tier system '
                              'as non-banks enter. Natasha Condon of JPMorgan counters that SCF was born '
                              'digital and already sits embedded in Oracle Fusion with SAP integration '
                              '[ltw4tGEw31o @ 00:03:44]. Operator playbook: a pre-shipment gap goes to '
                              'trade finance or PO money; a post-invoice gap with a strong buyer goes to '
                              "payables finance, where a supplier stuck at 12% funds at the buyer's 2%; "
                              'and Vanijja says running both together is possible.'],
               'table': {'caption': 'Side-by-side playbooks where Chapter Q7 practitioners split on '
                                    'structure, pricing, and timing',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['ABL revolver versus cash-flow loan for the borrower',
                                   'Collateral-focused revolver with formula-driven availability that '
                                   'fluctuates with eligible assets',
                                   'Cash-flow loan sized to enterprise value and EBITDA with fixed '
                                   'commitment and periodic tests',
                                   'Financely Group ([xY3rD_awSEg @ 00:00:26])'],
                                  ['Bank versus non-bank asset-based lender for scaled companies',
                                   'Bank pricing at SOFR+2-4% or Prime-2 to Prime+0 for scaled profitable '
                                   'borrowers',
                                   'Non-bank pricing from Prime+0 up to Prime+10 or Prime+15 with more '
                                   'aggressive structures',
                                   'Naturally New York ([oobK7A-p9-U @ 00:56:44])'],
                                  ['Recourse versus non-recourse factoring on the same invoices',
                                   'Recourse advances up to 90% of eligible AR aged 90 days or less',
                                   'Non-recourse advances only 70-80% of AR and carries noticeably higher '
                                   'fees',
                                   'FinanceKid ([u5hujmtiiaY @ 00:04:44])'],
                                  ['Factoring sale versus secured borrowing on the balance sheet',
                                   'Factoring is a complete sale of receivables and AR is credited off the '
                                   'books',
                                   'Secured borrowing pledges AR as loan collateral and the company still '
                                   'owns the receivables',
                                   'Accounting Videos ([-sIN2gar6BU @ 00:00:36])'],
                                  ['Trade finance versus supply chain finance funding timing',
                                   'Trade finance can fund pre-shipment against the purchase contract with '
                                   'cargo security',
                                   'SCF funds post-shipment once the buyer approves the invoice in a '
                                   'continuous flow',
                                   'Vanijja | Trade Insights ([RcVypdN4SHs @ 00:03:19])'],
                                  ['Collateral-heavy trade finance versus buyer-credit supply chain '
                                   'finance',
                                   'Letters of credit and export credit insurance are complex, multi-party '
                                   'and may require collateral',
                                   "SCF rests on the buyer's irrevocable payment undertaking and uses the "
                                   "buyer's credit instead",
                                   'Supply Chain Finance Academy ([Db19fMNKoJY @ 00:01:56])'],
                                  ['Digital-first delivery versus documentary revival in the market',
                                   'Panelist Susan sees risk skittishness driving a return to documentary '
                                   'and unfunded products',
                                   'Natasha Condon says SCF was born digital and is embedded in Oracle '
                                   'Fusion and SAP',
                                   'Trade Finance Global ([LlAxD5FEW5Q @ 00:02:19]); Trade Finance Global '
                                   '([ltw4tGEw31o @ 00:03:44])']]}},
              {'number': 4,
               'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The borrowing base is where deal sizes collapse, and the haircut math is '
                              'firsthand. Financely Group warns that lenders underwrite collectibility, '
                              'not face value, tracking aging, dilution, and cross-aging [xY3rD_awSEg @ '
                              '00:01:08]. Evan Wagner walks the Michael Scott Paper Co. book through the '
                              'knife: AR more than 30 days past due is ineligible, stripping 9%, and a '
                              'concentration cap, where most lenders implement a 25% threshold, strips '
                              'about 11% more [oobK7A-p9-U @ 00:33:19]. Net eligible AR of 586 advanced at '
                              '85 cents yields 498. Inventory gets cut harder: finished goods advance at '
                              'the lesser of 65 cents or 85% of NOLV, raw materials up to about 50%, WIP '
                              'and packaging are excluded, and stock sitting at small locations like '
                              'Nashua and Utica is ineligible. Stack it up and a $1M facility shows a '
                              'borrowing base of $832K, less a $42K AP reserve, for $790K available and '
                              "only $162K of excess availability [oobK7A-p9-U @ 00:45:24]. Wagner's reason "
                              'is blunt: asset-based lenders are underwriting to a liquidation, to a worst '
                              'case scenario [oobK7A-p9-U @ 00:34:49]. The economics check follows from '
                              "Financely's formula that net availability is the lesser of the borrowing "
                              'base or total commitments: model eligible collateral after aging, '
                              'concentration, location, and reserve cuts before promising a client any '
                              'number.',
                              'Inventory-heavy and burn-heavy borrowers are the second trap. FinanceKid '
                              'says many people call inventory financing the last alternative among ABL '
                              'options because of the double fees [u5hujmtiiaY @ 00:16:25]. The stack he '
                              'lists: Prime+4-6%, plus warehousing costs, audits every 3-6 months, and a '
                              'high DIO that is risky and can lead to default [u5hujmtiiaY @ 00:18:04]. '
                              'The positive case he allows is narrow: building stock in June for December '
                              'demand. Wagner adds the liquidity test lenders actually run: excess '
                              'availability plus cash, measured against burn, where three months of '
                              'coverage is a tough call and most lenders prefer enough liquidity to cover '
                              'at least 12 months of historical burn [oobK7A-p9-U @ 00:48:23]. He also '
                              'flags that later-stage equity investors resist using their dollars to buy '
                              'inventory, which is why the paper company leaned on roughly $628,000 of ABL '
                              'after Staples slowed to 45 days and Hammermill demanded net 10. Financely '
                              'Group draws the hard exit line: ABL is unsuitable when asset quality is '
                              "weak or reporting can't be supported [xY3rD_awSEg @ 00:02:30]. Financely "
                              'lists the controls that police it: the borrowing base certificate as the '
                              'primary control document, lockboxes and blocked accounts with dominion '
                              'active or triggered, and field exams and appraisals that detect fraud, with '
                              'Wagner adding seasonal paydown to zero.',
                              'The broker-side economics check comes from Bob McMahon of Aegis Factors, '
                              'and his numbers arrive as monthly trickles rather than lump sums. Typical '
                              'factoring runs about 2.5% per 30 days; in his example, a $3,000 monthly '
                              'factoring fee pays the broker $300 to $450 a month on a 10-15% sliding grid '
                              '[G9RrpSanefM @ 00:31:01]. Six figures takes roughly $2 million a month in '
                              'volume spread across 10-20 small clients [G9RrpSanefM @ 00:32:13]; a '
                              'janitorial deal paid about $200 a month, and one good deal a year adds '
                              'about $5,000. He also warns against paying $5,000-$15,000 for broker '
                              'courses, pointing to ICFB training under $200, and notes California alone '
                              'requires a lender license with a bond. The friction is paperwork. Shane '
                              "Walton's factoring package demands the aging report, invoices, "
                              'concentration, proof of delivery, and disputes, while PO deals need the PO, '
                              'quotes, margins, and plan [4fxpQTB_spA @ 00:13:58]. Peter Nicolao of Peak '
                              'Capital warns that applications are extensive, covering business plan, '
                              'stakeholders, sector, assets, and debts, and that terms vary by lender '
                              '[J-guTckEVMA @ 00:03:57]. Operator check: weigh trailing commission against '
                              'packaging hours, and qualify on documents before chasing volume.'],
               'table': {'caption': 'Firsthand failure modes and the economics checks practitioners attach '
                                    'to them',
                         'headers': ['Failure Mode',
                                     'Firsthand Number or Event',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Aged and concentrated receivables dropped from the borrowing base',
                                   'AR over 30 days past due removed 9% and the concentration cap removed '
                                   'about 11% more',
                                   'Model eligibility haircuts before quoting any availability figure to '
                                   'the client',
                                   'Naturally New York ([oobK7A-p9-U @ 00:33:19])'],
                                  ['Thin excess availability on a fully committed facility',
                                   '$832K base against a $1M cap, less a $42K AP reserve, left $162K '
                                   'excess availability',
                                   'Treat the commitment as a ceiling; excess availability plus cash is '
                                   'the real liquidity',
                                   'Naturally New York ([oobK7A-p9-U @ 00:45:24])'],
                                  ['Short liquidity runway measured against historical cash burn',
                                   'Three months of coverage is a tough call; most lenders prefer 12 '
                                   'months of burn',
                                   'Measure excess availability plus cash against trailing burn before '
                                   'submitting the deal',
                                   'Naturally New York ([oobK7A-p9-U @ 00:48:23])'],
                                  ['Inventory financing double-fee drag on a slow-turning book',
                                   'Prime+4-6% plus warehousing costs, audits every 3-6 months, and high '
                                   'DIO default risk',
                                   'Use inventory financing last, mainly for seasonal builds like June '
                                   'stock for December',
                                   'FinanceKid ([u5hujmtiiaY @ 00:18:04])'],
                                  ['Pledged receivables recorded as an outright sale on the books',
                                   'Lehman pledged poor-quality CDOs but recorded them as sales, avoiding '
                                   'unrealized-loss write-downs',
                                   'Book pledges as notes payable with footnote disclosure because selling '
                                   'means selling',
                                   'Farhat Lectures | CPA, CMA, EA & Accounting ([j1xpasTho-0 @ '
                                   '00:10:50])'],
                                  ['Owners confusing reported profit with available operating cash',
                                   'Vanijja calls the belief that profit equals cash a classic cash-flow '
                                   'mistake',
                                   'Map the cash conversion cycle, illustrated with the t-shirt example, '
                                   'before choosing a product',
                                   'Vanijja | Trade Insights ([kMiyyMuSUDU @ 00:01:21])'],
                                  ['Overpaying for broker training before closing a single deal',
                                   'McMahon warned against $5,000-$15,000 courses while ICFB training '
                                   'costs under $200',
                                   'Expect $300-$450 monthly per $3,000 factoring fee rather than large '
                                   'upfront paydays',
                                   'Simon White (SEO, AEO & Digital & Marketing) ([G9RrpSanefM @ '
                                   '00:16:47])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four kill-switch checks before a borrowing base deal goes to a lender',
                           'body': 'Each gate comes straight from a pitfall a practitioner hit or flagged; '
                                   'a deal that fails any one of them gets restructured or rerouted before '
                                   'submission.',
                           'items': ['Strip AR more than 30 days past due and anything above a 25% '
                                     'customer concentration threshold before sizing the line [Naturally '
                                     'New York — oobK7A-p9-U @ 00:33:42].',
                                     'Confirm excess availability plus cash covers at least 12 months of '
                                     'historical burn; three months is a tough call [Naturally New York — '
                                     'oobK7A-p9-U @ 00:48:23].',
                                     'Kill the ABL route if asset quality is weak or the client cannot '
                                     'support borrowing base reporting [Financely Group — xY3rD_awSEg @ '
                                     '00:02:30].',
                                     'Hold inventory financing for last because of double fees, Prime+4-6% '
                                     'pricing, warehousing costs, and 3-6 month audits [FinanceKid — '
                                     'u5hujmtiiaY @ 00:16:25].']}}],
 'pull_quote': '"Keep in mind asset based lenders are underwriting to a liquidation, they\'re underwriting '
               'to a worst case scenario." — Naturally New York (oobK7A-p9-U @ 00:34:49).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Run the timing audit: ask the client timeline questions and find the stuck link in '
                      'the cash clock between paying out cash and collecting it [Commercial Loan Broker '
                      'Institute — 4fxpQTB_spA @ 00:11:24].',
                      'Match the tool to the zone: PO or vendor terms at the front, line of credit or '
                      'equipment financing mid-process, AR financing or factoring at the back [Commercial '
                      'Loan Broker Institute — 4fxpQTB_spA @ 00:12:44].',
                      'Build a borrowing base model: eligible AR plus inventory times advance rates minus '
                      'reserves, with net availability as the lesser of the base or total commitments '
                      '[Financely Group — xY3rD_awSEg @ 00:00:40].',
                      'Package the factoring file with the aging report, invoices, concentration, proof of '
                      'delivery, and disputes before calling a funder [Commercial Loan Broker Institute — '
                      '4fxpQTB_spA @ 00:13:58].',
                      'Set up a conference call with an underwriter and route each deal to the right '
                      'lender type: factor, merchant cash advance, purchase order finance, or equipment '
                      'lessor [Simon White (SEO, AEO & Digital & Marketing) — G9RrpSanefM @ 00:23:28].',
                      "Pitch payables finance where a supplier paying 12% can fund itself at the buyer's "
                      '2% rate off an approved invoice [Vanijja | Trade Insights — RcVypdN4SHs @ '
                      '00:04:08].'],
 'statutory_citations': [{'title': 'Naturally New York — A Primer on Asset Based Lending (ABL) presented '
                                   'by SG Credit Partners [00:34:49]',
                          'url': 'https://www.youtube.com/watch?v=oobK7A-p9-U&t=2089s',
                          'relevance': 'Primary practitioner testimony on borrowing base haircuts, '
                                       'liquidation underwriting, liquidity runway, and bank versus '
                                       'non-bank ABL pricing.'},
                         {'title': 'FinanceKid — Asset Based Lending (ABL) - Business Financing Explained '
                                   '[00:16:25]',
                          'url': 'https://www.youtube.com/watch?v=u5hujmtiiaY&t=985s',
                          'relevance': 'Primary practitioner testimony on recourse versus non-recourse '
                                       'advance rates, PO financing, and inventory financing as the last '
                                       'alternative.'},
                         {'title': 'Simon White (SEO, AEO & Digital & Marketing) — Invoice Factoring & '
                                   'Asset Based Lending [00:31:01]',
                          'url': 'https://www.youtube.com/watch?v=G9RrpSanefM&t=1861s',
                          'relevance': 'Primary practitioner testimony on factoring broker commission '
                                       'grids, deal routing, and volume needed for six-figure income.'},
                         {'title': 'Commercial Loan Broker Institute — Unlock the Lucrative World of '
                                   'Supply Chain Financing [00:12:02]',
                          'url': 'https://www.youtube.com/watch?v=4fxpQTB_spA&t=722s',
                          'relevance': 'Primary practitioner testimony on the broker playbook of finding '
                                       'the stuck link, matching the tool, and packaging the deal.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'xY3rD_awSEg',
                       'title': 'Asset-Based Lending and Borrowing Base Facilities',
                       'channel': 'Financely Group',
                       'author': 'Financely Group',
                       'text': 'Cash is paid upfront for operations, while revenue is trapped in '
                               'receivables.',
                       'tip': 'Cash is paid upfront for operations, while revenue is trapped in '
                              'receivables.',
                       'timestamp': 13,
                       'timestamp_seconds': 13,
                       'timestamp_label': '[00:00:13]',
                       'url': 'https://www.youtube.com/watch?v=xY3rD_awSEg&t=13s',
                       'markdown': '[00:00:13](https://www.youtube.com/watch?v=xY3rD_awSEg&t=13s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C4UI_wc_sUU',
                       'title': 'Asset-Based Finance Explained',
                       'channel': 'PIMCO U.S.',
                       'author': 'PIMCO U.S.',
                       'text': 'The consumer category includes consumer orientated credit such as auto '
                               'loans, credit card receivables, student loans, or other types of personal '
                               'loans.',
                       'tip': 'The consumer category includes consumer orientated credit such as auto '
                              'loans, credit card receivables, student loans, or other types of personal '
                              'loans.',
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=C4UI_wc_sUU&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=C4UI_wc_sUU&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Db19fMNKoJY',
                       'title': 'Mastering Supply Chain Finance: Technique, Risk & Innovation - '
                                'Introduction to Supply Chain Finance',
                       'channel': 'Supply Chain Finance Academy',
                       'author': 'Supply Chain Finance Academy',
                       'text': 'Supply chain finance is not just about digitalization.',
                       'tip': 'Supply chain finance is not just about digitalization.',
                       'timestamp': 156,
                       'timestamp_seconds': 156,
                       'timestamp_label': '[00:02:36]',
                       'url': 'https://www.youtube.com/watch?v=Db19fMNKoJY&t=156s',
                       'markdown': '[00:02:36](https://www.youtube.com/watch?v=Db19fMNKoJY&t=156s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RcVypdN4SHs',
                       'title': 'Trade Finance vs. Supply Chain Finance: Key Differences Explained (With '
                                'Real Examples)',
                       'channel': 'Vanijja | Trade Insights',
                       'author': 'Vanijja | Trade Insights',
                       'text': 'So, they are burdened with a high 12% interest rate for bank loans.',
                       'tip': 'So, they are burdened with a high 12% interest rate for bank loans.',
                       'timestamp': 248,
                       'timestamp_seconds': 248,
                       'timestamp_label': '[00:04:08]',
                       'url': 'https://www.youtube.com/watch?v=RcVypdN4SHs&t=248s',
                       'markdown': '[00:04:08](https://www.youtube.com/watch?v=RcVypdN4SHs&t=248s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kMiyyMuSUDU',
                       'title': "Cash Flow Problems? Here's How Supply Chain Finance Provides the Solution",
                       'channel': 'Vanijja | Trade Insights',
                       'author': 'Vanijja | Trade Insights',
                       'text': 'Their free cash flow more than triples, jumping from 20 million to 70 '
                               'million.',
                       'tip': 'Their free cash flow more than triples, jumping from 20 million to 70 '
                              'million.',
                       'timestamp': 518,
                       'timestamp_seconds': 518,
                       'timestamp_label': '[00:08:38]',
                       'url': 'https://www.youtube.com/watch?v=kMiyyMuSUDU&t=518s',
                       'markdown': '[00:08:38](https://www.youtube.com/watch?v=kMiyyMuSUDU&t=518s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LlAxD5FEW5Q',
                       'title': '4 - The evolution of Supply Chain Finance',
                       'channel': 'Trade Finance Global',
                       'author': 'Trade Finance Global',
                       'text': 'The key is standardizing the data fields.',
                       'tip': 'The key is standardizing the data fields.',
                       'timestamp': 585,
                       'timestamp_seconds': 585,
                       'timestamp_label': '[00:09:45]',
                       'url': 'https://www.youtube.com/watch?v=LlAxD5FEW5Q&t=585s',
                       'markdown': '[00:09:45](https://www.youtube.com/watch?v=LlAxD5FEW5Q&t=585s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3Y7TjakDREI',
                       'title': 'Supply Chain Finance',
                       'channel': 'Eslatainment',
                       'author': 'Eslatainment',
                       'text': 'High-interest loans eat into profits.',
                       'tip': 'High-interest loans eat into profits.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=3Y7TjakDREI&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=3Y7TjakDREI&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ltw4tGEw31o',
                       'title': '25 years of supply chain finance  A journey to unlock liquidity',
                       'channel': 'Trade Finance Global',
                       'author': 'Trade Finance Global',
                       'text': "Fundamentally, you're solving a very simple problem in that somebody wants "
                               'to pay as late as possible and somebody wants to get paid as quick as '
                               'possible.',
                       'tip': "Fundamentally, you're solving a very simple problem in that somebody wants "
                              'to pay as late as possible and somebody wants to get paid as quick as '
                              'possible.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=ltw4tGEw31o&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=ltw4tGEw31o&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4fxpQTB_spA',
                       'title': 'Unlock the Lucrative World of Supply Chain Financing',
                       'channel': 'Commercial Loan Broker Institute',
                       'author': 'Commercial Loan Broker Institute',
                       'text': "And then you have vendor terms or trade credit, and that's often the "
                               "cheapest capital if it's available because you're extending your payables.",
                       'tip': "And then you have vendor terms or trade credit, and that's often the "
                              "cheapest capital if it's available because you're extending your payables.",
                       'timestamp': 372,
                       'timestamp_seconds': 372,
                       'timestamp_label': '[00:06:12]',
                       'url': 'https://www.youtube.com/watch?v=4fxpQTB_spA&t=372s',
                       'markdown': '[00:06:12](https://www.youtube.com/watch?v=4fxpQTB_spA&t=372s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'J-guTckEVMA',
                       'title': 'What is Trade Finance?',
                       'channel': 'Peak Capital',
                       'author': 'Peak Capital',
                       'text': 'Applications are extensive, covering the business plan, stakeholders, '
                               'sector, assets, and debts.',
                       'tip': 'Applications are extensive, covering the business plan, stakeholders, '
                              'sector, assets, and debts.',
                       'timestamp': 237,
                       'timestamp_seconds': 237,
                       'timestamp_label': '[00:03:57]',
                       'url': 'https://www.youtube.com/watch?v=J-guTckEVMA&t=237s',
                       'markdown': '[00:03:57](https://www.youtube.com/watch?v=J-guTckEVMA&t=237s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PPTyFBcPTUw',
                       'title': 'F3 M2 5 Pledging & Factoring of Accounts Receivables',
                       'channel': 'Mar T',
                       'author': 'Mar T',
                       'text': 'They retain the title, but they have pledged that the proceeds as those '
                               'receivables are collected will be used to pay down the loan.',
                       'tip': 'They retain the title, but they have pledged that the proceeds as those '
                              'receivables are collected will be used to pay down the loan.',
                       'timestamp': 57,
                       'timestamp_seconds': 57,
                       'timestamp_label': '[00:00:57]',
                       'url': 'https://www.youtube.com/watch?v=PPTyFBcPTUw&t=57s',
                       'markdown': '[00:00:57](https://www.youtube.com/watch?v=PPTyFBcPTUw&t=57s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oobK7A-p9-U',
                       'title': 'A Primer on Asset Based Lending (ABL) presented by SG Credit Partners',
                       'channel': 'Naturally New York',
                       'author': 'Naturally New York',
                       'text': 'Keep in mind asset based lenders are underwriting to a liquidation, '
                               "they're underwriting to a worst case scenario.",
                       'tip': "Keep in mind asset based lenders are underwriting to a liquidation, they're "
                              'underwriting to a worst case scenario.',
                       'timestamp': 2089,
                       'timestamp_seconds': 2089,
                       'timestamp_label': '[00:34:49]',
                       'url': 'https://www.youtube.com/watch?v=oobK7A-p9-U&t=2089s',
                       'markdown': '[00:34:49](https://www.youtube.com/watch?v=oobK7A-p9-U&t=2089s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oobK7A-p9-U',
                       'title': 'A Primer on Asset Based Lending (ABL) presented by SG Credit Partners',
                       'channel': 'Naturally New York',
                       'author': 'Naturally New York',
                       'text': 'Most lenders will implement a concentration threshold of 25%.',
                       'tip': 'Most lenders will implement a concentration threshold of 25%.',
                       'timestamp': 2022,
                       'timestamp_seconds': 2022,
                       'timestamp_label': '[00:33:42]',
                       'url': 'https://www.youtube.com/watch?v=oobK7A-p9-U&t=2022s',
                       'markdown': '[00:33:42](https://www.youtube.com/watch?v=oobK7A-p9-U&t=2022s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-sIN2gar6BU',
                       'title': 'Factoring vs. Secured Borrowing Part 1',
                       'channel': 'Accounting Videos',
                       'author': 'Accounting Videos',
                       'text': 'Factoring is a complete sale of your accounts receivable.',
                       'tip': 'Factoring is a complete sale of your accounts receivable.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=-sIN2gar6BU&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=-sIN2gar6BU&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'u5hujmtiiaY',
                       'title': 'Asset Based Lending (ABL) - Business Financing Explained',
                       'channel': 'FinanceKid',
                       'author': 'FinanceKid',
                       'text': 'Many many people say inventory financing should be your last alternative '
                               'when considering other ABL options.',
                       'tip': 'Many many people say inventory financing should be your last alternative '
                              'when considering other ABL options.',
                       'timestamp': 985,
                       'timestamp_seconds': 985,
                       'timestamp_label': '[00:16:25]',
                       'url': 'https://www.youtube.com/watch?v=u5hujmtiiaY&t=985s',
                       'markdown': '[00:16:25](https://www.youtube.com/watch?v=u5hujmtiiaY&t=985s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'G9RrpSanefM',
                       'title': 'Invoice Factoring & Asset Based Lending',
                       'channel': 'Simon White (SEO, AEO & Digital & Marketing)',
                       'author': 'Simon White (SEO, AEO & Digital & Marketing)',
                       'text': "Let's just say the factoring fee was 3,000 a month, you as the broker "
                               'would earn between $300 and $450 a month.',
                       'tip': "Let's just say the factoring fee was 3,000 a month, you as the broker would "
                              'earn between $300 and $450 a month.',
                       'timestamp': 1861,
                       'timestamp_seconds': 1861,
                       'timestamp_label': '[00:31:01]',
                       'url': 'https://www.youtube.com/watch?v=G9RrpSanefM&t=1861s',
                       'markdown': '[00:31:01](https://www.youtube.com/watch?v=G9RrpSanefM&t=1861s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'G9RrpSanefM',
                       'title': 'Invoice Factoring & Asset Based Lending',
                       'channel': 'Simon White (SEO, AEO & Digital & Marketing)',
                       'author': 'Simon White (SEO, AEO & Digital & Marketing)',
                       'text': "You don't need to take these expensive courses, you don't need to take "
                               '5,000, 10,000, $15,000 courses.',
                       'tip': "You don't need to take these expensive courses, you don't need to take "
                              '5,000, 10,000, $15,000 courses.',
                       'timestamp': 1007,
                       'timestamp_seconds': 1007,
                       'timestamp_label': '[00:16:47]',
                       'url': 'https://www.youtube.com/watch?v=G9RrpSanefM&t=1007s',
                       'markdown': '[00:16:47](https://www.youtube.com/watch?v=G9RrpSanefM&t=1007s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'j1xpasTho-0',
                       'title': 'Factoring Receivable and Pledging of Receivable',
                       'channel': 'Farhat Lectures | CPA, CMA, EA & Accounting',
                       'author': 'Farhat Lectures | CPA, CMA, EA & Accounting',
                       'text': 'So, they pledged them as an asset, but they record the transaction as a '
                               'sale.',
                       'tip': 'So, they pledged them as an asset, but they record the transaction as a '
                              'sale.',
                       'timestamp': 650,
                       'timestamp_seconds': 650,
                       'timestamp_label': '[00:10:50]',
                       'url': 'https://www.youtube.com/watch?v=j1xpasTho-0&t=650s',
                       'markdown': '[00:10:50](https://www.youtube.com/watch?v=j1xpasTho-0&t=650s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q7.'}]}
