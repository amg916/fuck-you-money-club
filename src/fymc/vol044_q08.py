from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'customs-valuation-first-sale-import-record-intelligence',
 'question_prompt': 'How is customs value determined, how can the first sale rule lower it, and how can '
                    "customs import records reveal competitors' sourcing?",
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Customs Valuation, First Sale and Import-Record Intelligence',
 'subtitle': 'Valuation methods for import duty, U.S. customs value, the first sale rule for middleman '
             'purchases, and using ImportGenius, Panjiva and I-Power shipment data for competitor, '
             'supplier and buyer research',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Customs brokers, valuation trainers and trade-data sellers converge on one point: '
                      'transaction value, the price actually paid or payable, drives 90 to 95 percent of '
                      'import valuations, and every dollar of markup baked into that price gets taxed. '
                      'Harry F. Long, Scarbrough, Flexport and Ask The Customs Manager all teach the US '
                      'first sale rule as the lever: declare the factory-to-middleman price instead of the '
                      "middleman's resale price, provided the first sale is arm's length, bona fide, and "
                      'the goods are locked to the US at manufacture. Street numbers run from a $10-to-$7 '
                      'jacket cut worth 30 percent to $6 per unit at a stacked 30 percent duty rate. '
                      'ImportGenius operators show bill-of-lading data exposing hidden suppliers and '
                      'freight-forwarder masks. The fault lines: whether the two sales may be '
                      "simultaneous, and how far Europe's latest-sale logic diverges.",
 'key_metrics': [{'label': 'Share of imports valued on transaction value',
                  'metric': 'Share of imports valued on transaction value',
                  'value': '90 to 95 percent of import transactions globally',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Flexport's Anna, a licensed broker and CPA, on how dominant invoice-price "
                             'valuation is worldwide',
                  'source': 'Flexport ([yR_RXKhapxo @ 00:09:13])'},
                 {'label': 'First sale duty liability cut on the jacket example',
                  'metric': 'First sale duty liability cut on the jacket example',
                  'value': '30 percent ($7 factory price declared instead of $10 middleman price)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Hong Kong trading company resells Vietnam factory jackets; declaring the '
                             'factory price strips the markup from the duty base',
                  'source': 'Ask The Customs Manager ([5fk-EKpR8Zw @ 00:01:26])'},
                 {'label': 'Per-unit duty savings at a stacked 30 percent rate',
                  'metric': 'Per-unit duty savings at a stacked 30 percent rate',
                  'value': '$6 per unit ($24 duty on $80 first sale versus $30 on $100 second sale)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': '5 percent NTR rate plus 25 percent Section 301 tariff on a Chinese product, '
                             'used as a back-of-envelope savings case',
                  'source': 'Flexport ([yR_RXKhapxo @ 00:10:37])'},
                 {'label': 'Share of US imports valued under first sale',
                  'metric': 'Share of US imports valued under first sale',
                  'value': 'Approximately 2.4 percent of all US imports',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Figure from a 2009 International Trade Commission report to Congress cited '
                             'by Flexport, which believes usage is higher today',
                  'source': 'Flexport ([yR_RXKhapxo @ 00:10:59])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every valuation conversation starts at the invoice. Customs Directory '
                              'frames most duty as ad valorem: a 10 percent rate is 10 percent of the '
                              'customs value, so a wrong value is a wrong tax bill, and transaction value, '
                              'the price actually paid or payable in the specific sale that shipped the '
                              'goods, covers a staggering 95 percent of global imports [3WCCVWQIggA @ '
                              "00:02:42]. Flexport's Anna, a licensed broker and CPA with 20 years in "
                              'brokerage, puts the figure at 90 to 95 percent globally and describes the '
                              'method as valuing goods off the invoice price [yR_RXKhapxo @ 00:09:13]. '
                              "Clark-Esposito's Lauren anchors the US version to the price paid or payable "
                              'when goods are sold for export to the United States, then loads in packing, '
                              'royalties and licensing fees the buyer is on the hook for [yXBLHYkmz0A @ '
                              "00:00:58]. Steve Cork, a former HMRC officer who built that agency's "
                              'valuation training for audit staff, runs the same formula from the UK side: '
                              'price paid or payable means all payments by the buyer to the seller as a '
                              'condition of sale, including money routed to third parties, such as a buyer '
                              "paying a sub-assembly supplier or covering a factory's electricity bill "
                              '[mimI2zifsUA @ 00:09:18]. The consensus is blunt: the invoice is the '
                              'starting line, never the finish line.',
                              'On the US side, four separate channels teach the first sale rule as the '
                              'single biggest legal valuation lever. Ask The Customs Manager calls it one '
                              'of the most lucrative, legally approved cost-saving strategies in global '
                              'trade, saving multinational brands millions in duty every year [5fk-EKpR8Zw '
                              "@ 00:00:15]. Harry F. Long's Heather Rush calls it a coupon code for entry "
                              'valuation: use the factory-to-middleman price rather than the higher price '
                              'the importer pays later, as long as the first sale is a legitimate '
                              "arm's-length transaction clearly destined for export to the US [oOC1WI_WDJs "
                              "@ 00:01:05]. Flexport's Tom Gould, a licensed broker with more than 30 "
                              'years advising on duty savings, explains the hook: US rules value goods on '
                              'the sale for export to the United States, not the import, which is why a '
                              'court case brought by a trading company opened the door to the first sale, '
                              'and why Europe and Australia, which once allowed it, rewrote their laws to '
                              "kill it [yR_RXKhapxo @ 00:05:42]. Scarbrough's Pat adds the strategic "
                              'angle: the rule traces to early-1990s court cases, is not tied to any '
                              'country, blunts Section 232 and 301 duties now, and keeps generating '
                              'savings in perpetuity after those tariffs disappear [Cif7o8T-mG4 @ '
                              '00:01:53].',
                              'The prerequisites line up across speakers almost word for word. Ask The '
                              'Customs Manager lists three non-negotiable tests: two distinct sales, '
                              'factory to middleman and middleman to importer; goods destined for the '
                              "importer's country at the moment the factory sells, proven by "
                              "country-specific safety labels, language tags or the buyer's logo printed "
                              'during manufacturing; and an unbroken paper trail of factory invoice, '
                              'factory purchase order and the bank transfer showing the middleman paying '
                              'the factory [5fk-EKpR8Zw @ 00:01:42]. Tom Gould frames the same filter as '
                              'bona fide sales, meaning a real transfer of ownership for consideration, '
                              'plus merchandise clearly destined for the US without the possibility of '
                              'diversion at the time of the first sale [yR_RXKhapxo @ 00:14:50]. Heather '
                              'Rush reduces it to genuine sales backed by invoices, contracts and shipping '
                              'records proving US export intent, warning that mapping the supply chain can '
                              "be complicated and slow [oOC1WI_WDJs @ 00:02:31]. Scarbrough's Pat flags "
                              'the two complications everyone circles back to: related-party trading '
                              'companies and factories draw extra scrutiny because customs does not want '
                              'artificially created values, and trading companies that supply raw '
                              'materials to the factory muddy the math, though Scarbrough says it has '
                              'worked these issues out hundreds of thousands of times [Cif7o8T-mG4 @ '
                              '00:02:10].'],
               'table': {'caption': 'Where valuation, first sale and import-data practitioners agree',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Transaction value dominates every valuation decision',
                                   'Price actually paid or payable values 95 percent of global imports',
                                   'Build every declaration from the invoice, then apply statutory '
                                   'additions and deductions',
                                   'Customs Directory ([3WCCVWQIggA @ 00:02:42])'],
                                  ['Valuation methods follow a strict waterfall order',
                                   'Six methods run in strict order; only deductive and computed may swap '
                                   'places',
                                   'Never cherry-pick a friendlier method when related-party pricing '
                                   'blocks transaction value',
                                   'Chartered Inst. of Export & International Trade ([mimI2zifsUA @ '
                                   '00:07:44])'],
                                  ['Assists supplied free to the factory get added back',
                                   'Free denim fabric and design sketches given to the supplier raise '
                                   'customs value',
                                   'Track every free-of-charge input and push it onto the entry '
                                   'declaration',
                                   'Customs Directory ([3WCCVWQIggA @ 00:04:01])'],
                                  ['First sale is a legal, US-only valuation lever',
                                   'US values goods on the sale for export, so the factory sale can '
                                   'qualify',
                                   'Audit every multi-tier supply chain for a lower, documentable first '
                                   'sale price',
                                   'Flexport ([yR_RXKhapxo @ 00:05:42])'],
                                  ["Arm's length plus locked US destination is mandatory",
                                   "First sale must be a legitimate arm's-length deal clearly destined for "
                                   'US export',
                                   'Prove destination with US-only purchase orders, labeling and delivery '
                                   'addresses at manufacture',
                                   'Harry F. Long, Inc. - U.S. Customs Brokers ([oOC1WI_WDJs @ 00:01:05])'],
                                  ['The upstream paper trail decides the claim',
                                   'Factory invoice, factory purchase order and middleman-to-factory bank '
                                   'transfer are required',
                                   'Secure the upstream documents before declaring the lower value, not '
                                   'after an audit',
                                   'Ask The Customs Manager ([5fk-EKpR8Zw @ 00:02:16])'],
                                  ['Bill-of-lading records are the intelligence layer',
                                   'One data line equals one bill of lading showing shipper, consignee, '
                                   'cartons and weight',
                                   "Use shipment records to map competitors' suppliers, middlemen and "
                                   'sourcing shifts over time',
                                   'ImportGenius Korea ([HLvI3nZIlT4 @ 00:00:59])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The first sale math is simple enough to run on a napkin. Ask The Customs '
                              "Manager's jacket deal: the importer pays a Hong Kong trading company $10 "
                              'per jacket, the trading company buys the same jackets from a Vietnam '
                              'factory at $7, and declaring the $7 factory price instead of $10 cuts duty '
                              'liability by 30 percent instantly [5fk-EKpR8Zw @ 00:01:26]. Heather Rush '
                              'scales it to deal size: apparel bought by the middleman for $100,000 and '
                              'resold at $160,000 lets the importer declare $100,000; Chinese electronics '
                              'drop from $300,000 to $200,000; and Mexican-made auto parts with US export '
                              'terms drop from $180,000 to $120,000, with tariff stacking magnifying every '
                              "dollar saved [oOC1WI_WDJs @ 00:01:49]. Flexport's Anna runs the unit math "
                              'on a Chinese product with a 5 percent normal trade relations rate plus a 25 '
                              'percent Section 301 tariff, a 30 percent effective rate: $80 first sale '
                              'yields $24 duty, $100 second sale yields $30, so $6 per unit times annual '
                              'volume becomes the back-of-envelope savings case [yR_RXKhapxo @ 00:10:37]. '
                              "Scarbrough's example shows the stakes at the extreme: paying 25 percent on "
                              'a $5 import versus a $25 resale price is the difference between a '
                              'successful business and being put out of business, with return on '
                              'investment often recovered in the first month [Cif7o8T-mG4 @ 00:03:34].',
                              'Execution lives in the documents and the title timeline. Tom Gould warns '
                              'that customs attacks flash title, where both sales transfer ownership at '
                              'the same instant, such as two FOB Hong Kong sales, so operators structure '
                              'the middleman to hold title for a distinct period, even less than a day, '
                              'before the second transfer [yR_RXKhapxo @ 00:15:59]. For related-party '
                              'structures, which Gould says make up many first sale programs, customs '
                              'wants a description of the parties, how they negotiate, purchase orders, '
                              'commercial invoices and proof of payment tied to a neutral third party like '
                              "the bank, plus contracts, negotiation emails and both companies' financial "
                              'records; Anna adds that comparables in a transfer pricing study usually run '
                              'five to ten companies, profit must land inside that range, and customs '
                              'prefers operating profit as the indicator [yR_RXKhapxo @ 00:27:42]. The '
                              'commercial standoff, a middleman refusing to reveal margin, gets solved '
                              'with a blind trust or third-party compliance auditor who receives the '
                              'factory pricing, packages the file and submits it straight to customs so '
                              'the importer never sees the factory invoice [5fk-EKpR8Zw @ 00:02:49]. Steve '
                              "Cork's tooling rule applies to assists in any structure: expect a million "
                              'phones a year for five years, divide the tooling cost by five million and '
                              'add that sliver to every unit [mimI2zifsUA @ 00:57:03].',
                              'On the data side, ImportGenius staff teach the search craft that turns '
                              'bills of lading into supplier and pricing intelligence. Its advanced-search '
                              'video recommends dropping Inc, Limited, Co and street words from company '
                              "names, searching the importer's name in the consignee address field when "
                              'the consignee field comes up empty, adding an asterisk to catch plurals, '
                              'which added 300 results to a 1,492-result basketball search, and clicking '
                              'related house bills of lading to strip away freight-forwarder masters and '
                              'expose the real Pakistani shipper and US importer [9IaKZ1JUPmU @ 00:05:51]. '
                              'Because US ocean data carries no price, Cody Estep pulls pricing from the '
                              'export side of other countries, where CIF, FOB or unit values usually '
                              'appear [XuTLIlW6tdk @ 00:29:16], and Kiona confirms bills from Indonesia, '
                              'the Philippines and Vietnam show price, letting a buyer test whether a '
                              'quote is competitive [i3e313EJJPE @ 00:01:13]. The ImportGenius webinar '
                              'panel adds that anonymity filings only mask the consignee, supplier or '
                              'relationship, never the product volumes entering the market, and one client '
                              "noticed Home Depot's containers always carry the same four-digit prefix and "
                              'now searches that prefix to track shipments that are supposed to be '
                              'confidential [XuTLIlW6tdk @ 00:25:23].'],
               'table': {'caption': 'First sale math, recovery levers and trade-data quotas as '
                                    'practitioners run them',
                         'headers': ['Mechanic',
                                     'Exact Numbers or Settings',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['First sale jacket markup strip',
                                   '$10 middleman price versus $7 factory price, a 30 percent duty '
                                   'reduction',
                                   'Declare the factory price only with full upstream invoice and payment '
                                   'proof',
                                   'Ask The Customs Manager ([5fk-EKpR8Zw @ 00:01:26])'],
                                  ['Stacked-rate per-unit savings model',
                                   '5 percent NTR plus 25 percent Section 301 equals 30 percent; $24 '
                                   'versus $30',
                                   'Multiply the $6 per-unit savings by annual volume to size the program',
                                   'Flexport ([yR_RXKhapxo @ 00:10:37])'],
                                  ['ACE portal five-year entry data pull',
                                   'Free ACE account; Flexport analyzes five years of broker-filed entries '
                                   'for clients',
                                   'Screen past entries for first sale candidates, classification gains '
                                   'and compliance risks',
                                   'Flexport ([yR_RXKhapxo @ 00:40:09])'],
                                  ['Retroactive volume discount duty recovery',
                                   'Goods bought at 100 pounds, year-end volume discount drops price to 95 '
                                   'pounds',
                                   "Amend that year's earlier import entries and claw back the overpaid "
                                   'duty',
                                   'Chartered Inst. of Export & International Trade ([mimI2zifsUA @ '
                                   '00:08:40])'],
                                  ['ImportGenius contact and export quotas',
                                   '25 researched contacts monthly, 10,000 exportable lines monthly, '
                                   'contacts within 48 hours',
                                   'Ration contact requests to top targets and batch Excel exports every '
                                   'month',
                                   'ImportGenius Korea ([HLvI3nZIlT4 @ 00:03:17])'],
                                  ['Plan history depth on shipment searches',
                                   'Standard plan sees one year of shipments; Enterprise gets almost five '
                                   'years',
                                   'Upgrade or request one-time older reports when the visual map shows '
                                   'hidden history',
                                   'ImportGenius ([Zdmg7G-W9_Q @ 00:02:59])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Valuation and data-search edges practitioners actually use',
                           'body': 'Small structuring and search moves that separate a defensible first '
                                   'sale claim and a clean supplier map from a rejected entry or a '
                                   'dead-end search.',
                           'items': ['Break flash title with staggered FOB points: Tom Gould says '
                                     'back-to-back FOB sales can survive when delivery points differ, such '
                                     'as FOB Shenzhen on the first sale and FOB Hong Kong on the second '
                                     '[Flexport — yR_RXKhapxo @ 00:43:19].',
                                     'Read the contract, not just the Incoterm: Anna has seen title pass '
                                     'after the boat is on the water through contract language separate '
                                     'from the invoice terms, so a full document review decides when the '
                                     'middleman owned the goods [Flexport — yR_RXKhapxo @ 00:44:21].',
                                     'Hunt hidden importers through house bills: when a master bill shows '
                                     'only a freight forwarder, scroll to related bills of lading and '
                                     'click the house bill to surface the true shipper and consignee '
                                     '[ImportGenius — 9IaKZ1JUPmU @ 00:05:51].',
                                     'Use reverse data for dark countries: when a country does not publish '
                                     "customs records, search the destination country's import data, which "
                                     'is how Kiona identifies Taiwanese suppliers shipping into the US '
                                     '[💎Kiona 職場 x 行銷筆記💎 — i3e313EJJPE @ 00:00:46].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pull the official import history',
                              'action': 'Open a free ACE portal account and extract five years of entry '
                                        'data filed by every broker.',
                              'detail': 'Flexport runs this five-year ACE pull for clients to spot first '
                                        'sale candidates, classification gains and duty risks such as '
                                        'antidumping exposure [Flexport — yR_RXKhapxo @ 00:40:09].'},
                             {'step': 2,
                              'title': 'Map the tiers and price the first sale',
                              'action': 'Identify every middleman between factory and importer and model '
                                        'per-unit savings against annual volume.',
                              'detail': "Anna's model takes the first sale versus second sale price at the "
                                        'effective duty rate, producing $6 per unit at 30 percent, then '
                                        'multiplies by expected units [Flexport — yR_RXKhapxo @ '
                                        '00:10:37].'},
                             {'step': 3,
                              'title': 'Lock the upstream paper trail',
                              'action': 'Collect factory invoice, factory purchase order and '
                                        'middleman-to-factory bank transfer, routed through a blind trust '
                                        'if the vendor hides margin.',
                              'detail': 'The independent auditor receives the confidential factory '
                                        'pricing, packages the file and submits it to customs while the '
                                        'importer never sees the invoice [Ask The Customs Manager — '
                                        '5fk-EKpR8Zw @ 00:02:49].'},
                             {'step': 4,
                              'title': 'Test with a ruling and wire the broker',
                              'action': 'Submit a representative transaction for a customs ruling and set '
                                        'up a process to feed statutory additions to the filing broker.',
                              'detail': 'Tom Gould says a favorable ruling on a representative transaction '
                                        'anchors the program, but customs will compare future entries '
                                        'against it, and undeclared additions on the first sale are where '
                                        'companies get in trouble [Flexport — yR_RXKhapxo @ 00:33:31].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on first sale is how you pry factory pricing out of a '
                              'middleman who has every reason to hide it. Ask The Customs Manager frames '
                              'the conflict bluntly: the vendor will not hand over the factory invoice '
                              'because you will see their margin and might cut them out, so major brands '
                              'route the factory invoice, purchase order and bank transfer through a blind '
                              'trust or third-party trade compliance auditor who packages the file and '
                              'submits it straight to customs, and the importer never sees the numbers '
                              "[5fk-EKpR8Zw @ 00:02:49]. Flexport's Tom Gould runs a different play: "
                              'persuade the trading company directly, because there are reasons the '
                              'program benefits the factory and the trading company too, and Flexport says '
                              'it has done that successfully for clients [yR_RXKhapxo @ 00:42:28]. Harry '
                              "F. Long's Heather Rush warns that mapping a supply chain for first sale is "
                              'complicated and takes time, but sells it as a coupon code on entry value, '
                              'citing shirts bought for $160,000 and declared at the $100,000 factory '
                              "price [oOC1WI_WDJs @ 00:01:05]. Scarbrough Global's Pat pushes the payback "
                              'case even harder, claiming the return on investment often comes back in the '
                              'first month or so, after which every entry is pure savings [Cif7o8T-mG4 @ '
                              '00:04:25].',
                              "Practitioners split hard on related-party structures. Flexport's Tom Gould "
                              'says many first sale programs run on a related factory selling to a related '
                              'middleman, and they hold up only when the company can show customs the '
                              "deals were negotiated at arm's length, the way unrelated parties would "
                              "bargain [yR_RXKhapxo @ 00:06:50]. Scarbrough Global's Pat concedes customs "
                              'scrutinizes related-party first sale harder, because it does not want '
                              'values artificially created to save duty, and that trading-company raw '
                              'materials complicate the file, yet insists those issues get worked out and '
                              'claims the firm has done it hundreds of thousands of times [Cif7o8T-mG4 @ '
                              '00:02:10]. Steve Cork of the Chartered Institute, a former HMRC valuation '
                              'trainer, is far colder: if an officer asks whether the intercompany '
                              'relationship gets you a cheaper price and you answer yes, you have just '
                              'disqualified yourself from method one transaction value [mimI2zifsUA @ '
                              '00:11:48]. Geography flips the whole playbook. Flexport says first sale '
                              'survives only in the United States, because Europe and Australia changed '
                              'their laws [yR_RXKhapxo @ 00:05:42]. Cork describes the opposite instinct '
                              'on the EU side, where customs looks to levy duty on the latest sale it can '
                              'find in a chain, so importers running pre-sold, dealership-style structures '
                              'should distance later sales from the original supply as much as possible.',
                              'On import-record intelligence, the vendors pitch opposite philosophies. '
                              'Kiona, who sells I-Power, claims 60 countries and over 10 million records '
                              'versus roughly 22 countries for ImportGenius and 19 for Panjiva, and '
                              'attacks ImportGenius pricing as $199 a month for 12 months of data with 25 '
                              'searches or $399 for 17 months with 50 searches, arguing search caps break '
                              'you when a competitor files underwear under a different term like boxers '
                              "[LggBClCtXNY @ 00:04:54]. ImportGenius's Dan McKill counters that the "
                              'platform does not alter customs records with AI, applying machine learning '
                              'only to standardization and formatting so the data stays as received from '
                              'customs [XuTLIlW6tdk @ 00:30:01]. Contact discovery splits the same way. '
                              "ImportGenius Korea's Juwan says the research team finds company contacts by "
                              'hand, which caps clients at 25 companies a month, with replies inside 48 '
                              'working hours [HLvI3nZIlT4 @ 00:02:40]. Kiona runs the opposite machine: AI '
                              'email search, verification, AI-written templates and bulk sending, showing '
                              'a campaign of 7,778 emails with 546 validated and tracking who opened and '
                              'clicked, and claiming a one-person company can mail 1,000 to 10,000 '
                              'prospects in a single day [i3e313EJJPE @ 00:04:50].'],
               'table': {'caption': 'Competing playbooks on first sale structuring and import-record '
                                    'intelligence',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Prying factory pricing out of the middleman',
                                   'Route factory invoice, purchase order and bank transfer through a '
                                   'blind trust or third-party auditor so the importer never sees the '
                                   'margin',
                                   'Convince the trading company directly that the first sale program also '
                                   'benefits the factory and the trading company',
                                   'Ask The Customs Manager ([5fk-EKpR8Zw @ 00:02:49]); Flexport '
                                   '([yR_RXKhapxo @ 00:42:28])'],
                                  ['Related factory and middleman structures',
                                   'Workable at scale; Scarbrough says related-party issues get worked out '
                                   'and claims hundreds of thousands of setups',
                                   'Cork says admitting the relationship lowers your price immediately '
                                   'disqualifies you from method one valuation',
                                   'Scarbrough Global ([Cif7o8T-mG4 @ 00:02:28]); Chartered Inst. of '
                                   'Export & International Trade ([mimI2zifsUA @ 00:11:48])'],
                                  ['Title transfer timing between the two sales',
                                   'Both sales FOB Hong Kong with simultaneous title transfer is often '
                                   'ruled unacceptable flash title by customs',
                                   'Back-to-back FOB Shenzhen then FOB Hong Kong may suffice, and contract '
                                   'language can move title separately from incoterms',
                                   'Flexport ([yR_RXKhapxo @ 00:43:19])'],
                                  ['Which sale in a chain sets the duty value',
                                   'The United States accepts the earlier factory-to-middleman sale for '
                                   'export under the first sale rule',
                                   'EU customs looks to levy duty on the latest sale it can identify in '
                                   'the chain of transactions',
                                   'Flexport ([yR_RXKhapxo @ 00:05:42]); Chartered Inst. of Export & '
                                   'International Trade ([mimI2zifsUA @ 00:11:08])'],
                                  ['Where first sale pays off the most',
                                   'Harry F. Long says stacked general and reciprocal tariffs make the '
                                   'lower first sale value save far more money',
                                   'Flexport finds no correlation with duty rate; machinery and computers '
                                   'lead usage, driven by product value instead',
                                   'Harry F. Long, Inc. - U.S. Customs Brokers ([oOC1WI_WDJs @ 00:01:28]); '
                                   'Flexport ([yR_RXKhapxo @ 00:11:59])'],
                                  ['Customs data coverage and search limits',
                                   'Kiona pitches I-Power with 60 countries, over 10 million trade records '
                                   'and no search limits at all',
                                   'ImportGenius covers 25 countries with shipment-level visibility; Kiona '
                                   'says its plans cap searches at 25 or 50',
                                   '💎Kiona 職場 x 行銷筆記💎 ([LggBClCtXNY @ 00:04:54]); ImportGenius '
                                   '([XuTLIlW6tdk @ 00:02:25])'],
                                  ['Finding contacts at importers and suppliers',
                                   'ImportGenius Korea researchers find contacts manually, 25 companies '
                                   'per month, delivered within 48 working hours',
                                   'Kiona runs AI email search, verification and bulk sends, citing 7,778 '
                                   'emails sent with 546 validated',
                                   'ImportGenius Korea ([HLvI3nZIlT4 @ 00:02:40]); 💎Kiona 職場 x 行銷筆記💎 '
                                   '([i3e313EJJPE @ 00:04:50])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Flexport's Tom Gould names flash title as the fastest way to lose a first "
                              'sale claim: when both sales are set up FOB Hong Kong and title moves on '
                              'both at the same instant, customs has often ruled the middleman never truly '
                              'owned the goods, so working programs build in a separate title transfer to '
                              'the middleman, even one lasting less than a day, before the second transfer '
                              'to the importer [yR_RXKhapxo @ 00:15:27]. Diversion is the second killer. A '
                              'purchase order splitting 100,000 units between Canada and the US fails, and '
                              'multilingual labels or certifications for several destination countries can '
                              'let customs invalidate the claim outright [yR_RXKhapxo @ 00:18:24]. Ask The '
                              'Customs Manager supplies the inverse proof: factory-printed '
                              'country-specific safety labels, language tags or your corporate logo show '
                              'the goods were destined for you at the moment of sale, and you cannot guess '
                              'the factory price because customs heavily audits the strategy [5fk-EKpR8Zw '
                              '@ 00:01:26]. Anna Zjack of Flexport flags a quieter trap: distributor '
                              'agreements carrying consigned inventory or post-delivery conditions can '
                              'undercut a bona fide sale even when the invoice incoterm looks clean, '
                              'because incoterms do not settle ownership and title often transfers only '
                              'after the boat is on the water [yR_RXKhapxo @ 00:44:21].',
                              'The money leaks Tom Gould has watched companies walk into come from '
                              'additions. When an importer declares the first sale, it must add assists, '
                              'royalties and proceeds of subsequent sale tied to that first sale even when '
                              'the middleman paid them, such as fabric the middleman hands the factory '
                              'free, and Gould says this is exactly where companies get in trouble when no '
                              'process feeds those numbers to the broker; a ruling on a representative '
                              'transaction is no blanket shield either, because customs compares every '
                              'later entry against it for differences [yR_RXKhapxo @ 00:34:06]. Steve Cork '
                              'lists the hidden dutiable items importers miss: pre-shipment testing fees '
                              'are dutiable whether the buyer or the manufacturer pays them, and free '
                              'samples not written into the sales contract get valued as identical goods '
                              '[mimI2zifsUA @ 00:41:48]. Tooling supplied to a factory must be apportioned '
                              'over its production life, dividing the cost by five million phones if you '
                              'expect a million a year for five years [mimI2zifsUA @ 00:57:03]. Customs '
                              'Directory spells out the bill for getting value wrong: audits reaching back '
                              'years, massive unexpected duty, fines and penalties, cargo stuck at port or '
                              'seized, and criminal charges for deliberate undervaluation [3WCCVWQIggA @ '
                              '00:06:13].',
                              "Import-record users hit their own walls. ImportGenius's visual mapping "
                              'trainer warns that a trading connection can show on the map while view '
                              'latest shipments comes up empty, because standard plans see one year of '
                              'data while Enterprise subscribers see almost five, and the same brand '
                              'splits into separate entities such as Lululemon Athletica USA Inc versus '
                              'Lululemon Athletica Inc, hiding trading connections behind the wrong record '
                              '[Zdmg7G-W9_Q @ 00:02:46]. The advanced-search trainer says shipments go '
                              'missing when the importer name lands in the consignee address field, when '
                              'you type Inc or Limited, or when a freight forwarder sits on the master '
                              'bill, fixed by scrolling to the related house bill to reveal the real '
                              'shipper and the real importer [9IaKZ1JUPmU @ 00:05:32]. Dan McKill says '
                              'anonymity filings only mask the consignee, supplier or relationship, and '
                              "one customer beat Home Depot's anonymity by searching the four-digit "
                              'container prefix that always ends at Home Depot warehouses [XuTLIlW6tdk @ '
                              '00:25:05]. Kiona warns that buying just one month of Panjiva is a trap '
                              'because countries update daily, weekly or monthly, so a short subscription '
                              'carries a high chance of missing the latest records you paid to see '
                              '[LggBClCtXNY @ 00:04:29].'],
               'table': {'caption': 'Firsthand traps in first sale valuation and import-record research',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw',
                                     'Economics Check / Fix',
                                     'Expert Source'],
                         'rows': [['Flash title on simultaneous sales',
                                   'Both sales set FOB Hong Kong with title moving at once; customs often '
                                   'rejects the first sale claim',
                                   'Give the middleman real ownership, even for under a day, before the '
                                   'second title transfer',
                                   'Flexport ([yR_RXKhapxo @ 00:15:27])'],
                                  ['Diversion risk and multilingual labeling',
                                   'Purchase orders splitting 100,000 units between Canada and the US, or '
                                   'multi-country labels, undercut US destination',
                                   'Show US delivery addresses and factory-printed country-specific '
                                   'labels, tags or logos applied during manufacturing',
                                   'Flexport ([yR_RXKhapxo @ 00:18:24]); Ask The Customs Manager '
                                   '([5fk-EKpR8Zw @ 00:02:00])'],
                                  ['Missing additions on the declared first sale',
                                   'Middleman supplies free fabric or pays royalties, but the importer '
                                   'never reports them on the first sale',
                                   'Build a process where the middleman tells the importer the additions '
                                   'and the broker declares them',
                                   'Flexport ([yR_RXKhapxo @ 00:46:53])'],
                                  ['Hidden dutiable costs riding on the invoice',
                                   'Pre-shipment testing fees and free samples left outside the sales '
                                   'contract both pull extra duty',
                                   'Write free-of-charge supply into the sales contract and apportion '
                                   'tooling across its full production life',
                                   'Chartered Inst. of Export & International Trade ([mimI2zifsUA @ '
                                   '00:41:48])'],
                                  ['Declaring goods you do not own',
                                   'Importer declares delivered-duty-paid goods for a supplier, then '
                                   'recovers import VAT it was never entitled to',
                                   'Cork warns officers can demand the VAT plus a 100% penalty, roughly '
                                   '40% of goods value',
                                   'Chartered Inst. of Export & International Trade ([mimI2zifsUA @ '
                                   '00:52:51])'],
                                  ['Visual map shows a ghost trading connection',
                                   'Trading partner appears on the map but view latest shipments returns '
                                   'nothing on the one-year standard plan',
                                   'Upgrade to Enterprise for almost five years of data or request a '
                                   'one-time report download',
                                   'ImportGenius ([Zdmg7G-W9_Q @ 00:02:46])'],
                                  ['No prices in US ocean import records',
                                   'US customs does not share price data on ocean freight bills of lading '
                                   'with data vendors',
                                   "Pull CIF, FOB or unit values from the exporting country's records "
                                   'bound for the United States',
                                   'ImportGenius ([XuTLIlW6tdk @ 00:29:01])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill-Switch Checks Before Filing a First Sale Entry',
                           'body': 'Every item below is a failure point the practitioners watched sink '
                                   'first sale claims or blow up valuation files. Clear all four before '
                                   'the broker files the lower value.',
                           'items': ['Confirm the middleman takes title at a separate point in time from '
                                     'the importer; simultaneous FOB Hong Kong transfers are flash title '
                                     'and customs has often rejected them [Flexport — yR_RXKhapxo @ '
                                     '00:15:27].',
                                     'Hold the complete paper trail before declaring: original factory '
                                     'invoice, factory purchase order and the bank transfer showing the '
                                     'middleman paid the factory price [Ask The Customs Manager — '
                                     '5fk-EKpR8Zw @ 00:02:16].',
                                     'Stand up the additions pipeline first, so assists, royalties and '
                                     'proceeds of subsequent sale on the first sale reach the broker on '
                                     'every entry [Flexport — yR_RXKhapxo @ 00:34:06].',
                                     'Never declare goods you do not own at import; Cork warns officers '
                                     'will reclaim the VAT and stack a penalty on top [Chartered Inst. of '
                                     'Export & International Trade — mimI2zifsUA @ 00:43:33].']}}],
 'pull_quote': '"If your company buys imported goods through a trading company, a middleman, or a foreign '
               'vendor rather than buying directly from the factory, you are voluntarily paying the '
               'government extra taxes on another company\'s profit margin." — Ask The Customs Manager '
               '(5fk-EKpR8Zw @ 00:00:00).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Run the Flexport back-of-envelope math: at a 30% effective rate, an $80 first sale '
                      'versus a $100 second sale saves $6 per unit, then multiply by annual unit volume '
                      '[Flexport — yR_RXKhapxo @ 00:10:14].',
                      'Open a free ACE portal account and pull up to five years of entry data to screen '
                      'for first sale candidates, classification issues and other duty savings [Flexport — '
                      'yR_RXKhapxo @ 00:39:31].',
                      'Have the middleman hand factory pricing to a blind trust or third-party trade '
                      'auditor who packages the file and submits it directly to customs [Ask The Customs '
                      'Manager — 5fk-EKpR8Zw @ 00:02:49].',
                      'Request a binding ruling on a representative transaction when the valuation method '
                      'is uncertain, then keep future entries matching that transaction [Clark-Esposito '
                      'Law Firm P.C. — yXBLHYkmz0A @ 00:01:58].',
                      'Trace a competitor that vanished from Asian ocean data into Mexico border data, '
                      'filter by product, and use the prices they paid as your supplier benchmark '
                      '[ImportGenius — XuTLIlW6tdk @ 00:19:04].',
                      'Clean every search: drop Inc, Limited and Co, add an asterisk for plurals, check '
                      'address fields, and click the related house bill behind freight forwarders '
                      '[ImportGenius — 9IaKZ1JUPmU @ 00:04:12].'],
 'statutory_citations': [{'title': 'Flexport — Flexport Customs: Mastering the First Sale Rule [00:06:13]',
                          'url': 'https://www.youtube.com/watch?v=yR_RXKhapxo&t=373s',
                          'relevance': 'Primary practitioner testimony on the court case origin of the '
                                       "first sale rule, the arm's length requirement and the "
                                       'clearly-destined-for-export test.'},
                         {'title': 'Ask The Customs Manager — Save Thousands on Import Duties With This '
                                   'Strategy [00:01:42]',
                          'url': 'https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=102s',
                          'relevance': 'Primary practitioner testimony on the three tests for first sale '
                                       'and the blind trust workaround for middleman pricing secrecy.'},
                         {'title': 'Chartered Inst. of Export & International Trade — Customs 101: Methods '
                                   'of valuation for import duty [00:08:02]',
                          'url': 'https://www.youtube.com/watch?v=mimI2zifsUA&t=482s',
                          'relevance': 'Primary practitioner testimony on the six valuation methods, their '
                                       'strict order, and dutiable additions and deductions.'},
                         {'title': 'Scarbrough Global — First Sale Rule – U.S. Customs and Imports '
                                   '[00:00:43]',
                          'url': 'https://www.youtube.com/watch?v=Cif7o8T-mG4&t=43s',
                          'relevance': 'Primary practitioner testimony on multi-sale export structures, '
                                       'related-party scrutiny and first sale savings surviving tariff '
                                       'changes.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'HLvI3nZIlT4',
                       'title': 'How to use the ImportGenius Application_Eng Ver',
                       'channel': 'ImportGenius Korea',
                       'author': 'ImportGenius Korea',
                       'text': 'You can get 25 contact information of the companies per month because our '
                               'research team searched the contact information manually.',
                       'tip': 'You can get 25 contact information of the companies per month because our '
                              'research team searched the contact information manually.',
                       'timestamp': 160,
                       'timestamp_seconds': 160,
                       'timestamp_label': '[00:02:40]',
                       'url': 'https://www.youtube.com/watch?v=HLvI3nZIlT4&t=160s',
                       'markdown': '[00:02:40](https://www.youtube.com/watch?v=HLvI3nZIlT4&t=160s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'LggBClCtXNY',
                       'title': 'Top 3 Customs Data Suppliers Compared: Panjiva vs. ImportGenius vs. '
                                'I-POWER',
                       'channel': '💎Kiona 職場 x 行銷筆記💎',
                       'author': '💎Kiona 職場 x 行銷筆記💎',
                       'text': 'Plan B is 399 per month, this plan allows you to access the data for the '
                               'past 17 months and include 50 searches.',
                       'tip': 'Plan B is 399 per month, this plan allows you to access the data for the '
                              'past 17 months and include 50 searches.',
                       'timestamp': 294,
                       'timestamp_seconds': 294,
                       'timestamp_label': '[00:04:54]',
                       'url': 'https://www.youtube.com/watch?v=LggBClCtXNY&t=294s',
                       'markdown': '[00:04:54](https://www.youtube.com/watch?v=LggBClCtXNY&t=294s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XuTLIlW6tdk',
                       'title': 'Trade secrets exposed: how to see what your competitors are importing, '
                                'selling, and sourcing',
                       'channel': 'ImportGenius',
                       'author': 'ImportGenius',
                       'text': 'They found out that Home Depot also labels their containers with a special '
                               'container number, and it always starts with the same four digits.',
                       'tip': 'They found out that Home Depot also labels their containers with a special '
                              'container number, and it always starts with the same four digits.',
                       'timestamp': 1505,
                       'timestamp_seconds': 1505,
                       'timestamp_label': '[00:25:05]',
                       'url': 'https://www.youtube.com/watch?v=XuTLIlW6tdk&t=1505s',
                       'markdown': '[00:25:05](https://www.youtube.com/watch?v=XuTLIlW6tdk&t=1505s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XuTLIlW6tdk',
                       'title': 'Trade secrets exposed: how to see what your competitors are importing, '
                                'selling, and sourcing',
                       'channel': 'ImportGenius',
                       'author': 'ImportGenius',
                       'text': "When it comes to the US ocean freight data, they don't share the price "
                               'with us.',
                       'tip': "When it comes to the US ocean freight data, they don't share the price with "
                              'us.',
                       'timestamp': 1741,
                       'timestamp_seconds': 1741,
                       'timestamp_label': '[00:29:01]',
                       'url': 'https://www.youtube.com/watch?v=XuTLIlW6tdk&t=1741s',
                       'markdown': '[00:29:01](https://www.youtube.com/watch?v=XuTLIlW6tdk&t=1741s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'i3e313EJJPE',
                       'title': 'How AI Finds Global Buyers 10X FASTER Than Manual Search! #I-Power '
                                '#panjiva #importgenius',
                       'channel': '💎Kiona 職場 x 行銷筆記💎',
                       'author': '💎Kiona 職場 x 行銷筆記💎',
                       'text': 'In some specific countries, for example Indonesia, Philippines and '
                               'Vietnam, you can see the price on the bills of lading.',
                       'tip': 'In some specific countries, for example Indonesia, Philippines and Vietnam, '
                              'you can see the price on the bills of lading.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=i3e313EJJPE&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=i3e313EJJPE&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9IaKZ1JUPmU',
                       'title': 'Import Genius Advanced Search Techniques Help Video',
                       'channel': 'ImportGenius',
                       'author': 'ImportGenius',
                       'text': "If you see a shipment that's hidden behind a freight forwarder, scroll all "
                               "the way down to the bottom and you've got related bills of lading.",
                       'tip': "If you see a shipment that's hidden behind a freight forwarder, scroll all "
                              "the way down to the bottom and you've got related bills of lading.",
                       'timestamp': 332,
                       'timestamp_seconds': 332,
                       'timestamp_label': '[00:05:32]',
                       'url': 'https://www.youtube.com/watch?v=9IaKZ1JUPmU&t=332s',
                       'markdown': '[00:05:32](https://www.youtube.com/watch?v=9IaKZ1JUPmU&t=332s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NmWdt9dMzjM',
                       'title': 'Identify High-Value Sales Prospects with Import Genius',
                       'channel': 'ImportGenius',
                       'author': 'ImportGenius',
                       'text': "Visual mapping gives you a graphical representation of this company's "
                               'supply chain showing all of their trading partners as nodes on the web of '
                               'trade connections.',
                       'tip': "Visual mapping gives you a graphical representation of this company's "
                              'supply chain showing all of their trading partners as nodes on the web of '
                              'trade connections.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=NmWdt9dMzjM&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=NmWdt9dMzjM&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Zdmg7G-W9_Q',
                       'title': 'Import Genius Visual Mapping Instruction',
                       'channel': 'ImportGenius',
                       'author': 'ImportGenius',
                       'text': "Enterprise subscribers get all of our data, so it's almost five years "
                               'worth of shipment data, where standard subscribers only get one year of '
                               'data.',
                       'tip': "Enterprise subscribers get all of our data, so it's almost five years worth "
                              'of shipment data, where standard subscribers only get one year of data.',
                       'timestamp': 179,
                       'timestamp_seconds': 179,
                       'timestamp_label': '[00:02:59]',
                       'url': 'https://www.youtube.com/watch?v=Zdmg7G-W9_Q&t=179s',
                       'markdown': '[00:02:59](https://www.youtube.com/watch?v=Zdmg7G-W9_Q&t=179s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'irUncYGL5Jg',
                       'title': 'Marble Imports',
                       'channel': 'ImportGenius',
                       'author': 'ImportGenius',
                       'text': "There's the phone number for that factory, I'm sure I can google them very "
                               'quickly and find out exactly their email address and start a dialogue with '
                               'them.',
                       'tip': "There's the phone number for that factory, I'm sure I can google them very "
                              'quickly and find out exactly their email address and start a dialogue with '
                              'them.',
                       'timestamp': 61,
                       'timestamp_seconds': 61,
                       'timestamp_label': '[00:01:01]',
                       'url': 'https://www.youtube.com/watch?v=irUncYGL5Jg&t=61s',
                       'markdown': '[00:01:01](https://www.youtube.com/watch?v=irUncYGL5Jg&t=61s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5fk-EKpR8Zw',
                       'title': 'Save Thousands on Import Duties With This Strategy',
                       'channel': 'Ask The Customs Manager',
                       'author': 'Ask The Customs Manager',
                       'text': 'If your company buys imported goods through a trading company, a '
                               'middleman, or a foreign vendor rather than buying directly from the '
                               'factory, you are voluntarily paying the government extra taxes on another '
                               "company's profit margin.",
                       'tip': 'If your company buys imported goods through a trading company, a middleman, '
                              'or a foreign vendor rather than buying directly from the factory, you are '
                              "voluntarily paying the government extra taxes on another company's profit "
                              'margin.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5fk-EKpR8Zw',
                       'title': 'Save Thousands on Import Duties With This Strategy',
                       'channel': 'Ask The Customs Manager',
                       'author': 'Ask The Customs Manager',
                       'text': 'They use a blind trust or a third-party trade compliance auditor, and the '
                               'middleman hands the highly confidential factory pricing data directly to '
                               'the independent auditor.',
                       'tip': 'They use a blind trust or a third-party trade compliance auditor, and the '
                              'middleman hands the highly confidential factory pricing data directly to '
                              'the independent auditor.',
                       'timestamp': 169,
                       'timestamp_seconds': 169,
                       'timestamp_label': '[00:02:49]',
                       'url': 'https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=169s',
                       'markdown': '[00:02:49](https://www.youtube.com/watch?v=5fk-EKpR8Zw&t=169s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oOC1WI_WDJs',
                       'title': 'Customs Quick Tips - First Sale Rule',
                       'channel': 'Harry F. Long, Inc. - U.S. Customs Brokers',
                       'author': 'Harry F. Long, Inc. - U.S. Customs Brokers',
                       'text': "With the tariff stacking that's going on with general tariffs and now "
                               'reciprocal tariffs on top of it, that lower duty valuation is going to '
                               'save a lot of money.',
                       'tip': "With the tariff stacking that's going on with general tariffs and now "
                              'reciprocal tariffs on top of it, that lower duty valuation is going to save '
                              'a lot of money.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=oOC1WI_WDJs&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=oOC1WI_WDJs&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cif7o8T-mG4',
                       'title': 'First Sale Rule – U.S. Customs and Imports',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': "If your supply chain is set up to take advantage of this and you're not "
                               "taking advantage of it, it's just money sitting out there that you could "
                               'be saving.',
                       'tip': "If your supply chain is set up to take advantage of this and you're not "
                              "taking advantage of it, it's just money sitting out there that you could be "
                              'saving.',
                       'timestamp': 233,
                       'timestamp_seconds': 233,
                       'timestamp_label': '[00:03:53]',
                       'url': 'https://www.youtube.com/watch?v=Cif7o8T-mG4&t=233s',
                       'markdown': '[00:03:53](https://www.youtube.com/watch?v=Cif7o8T-mG4&t=233s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6Fco88JHSNg',
                       'title': 'A Quick Guide to Customs Valuation Methods to Determine the Value of '
                                'Goods | Customs-Declarations.uk',
                       'channel': 'CustomsDeclarationsUK',
                       'author': 'CustomsDeclarationsUK',
                       'text': 'This principal way of determining transaction value accounts for '
                               'approximately 90% of transactions in the UK.',
                       'tip': 'This principal way of determining transaction value accounts for '
                              'approximately 90% of transactions in the UK.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=6Fco88JHSNg&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=6Fco88JHSNg&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3WCCVWQIggA',
                       'title': 'Customs Valuation Explained – How Customs Calculate Import Duty',
                       'channel': 'Customs Directory',
                       'author': 'Customs Directory',
                       'text': 'A staggering 95% of all global imports are valued using this one single '
                               'method.',
                       'tip': 'A staggering 95% of all global imports are valued using this one single '
                              'method.',
                       'timestamp': 162,
                       'timestamp_seconds': 162,
                       'timestamp_label': '[00:02:42]',
                       'url': 'https://www.youtube.com/watch?v=3WCCVWQIggA&t=162s',
                       'markdown': '[00:02:42](https://www.youtube.com/watch?v=3WCCVWQIggA&t=162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yXBLHYkmz0A',
                       'title': 'U.S. Customs Value Explained',
                       'channel': 'Clark-Esposito Law Firm P.C.',
                       'author': 'Clark-Esposito Law Firm P.C.',
                       'text': "If you're unsure about your valuation method, CBP allows importers to "
                               'request binding rulings for added certainty.',
                       'tip': "If you're unsure about your valuation method, CBP allows importers to "
                              'request binding rulings for added certainty.',
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=yXBLHYkmz0A&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=yXBLHYkmz0A&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yR_RXKhapxo',
                       'title': 'Flexport Customs: Mastering the First Sale Rule',
                       'channel': 'Flexport',
                       'author': 'Flexport',
                       'text': 'A flash title is when the transaction in the two sales happen at the same '
                               "time, so there's really not a clear distinction of when that middleman "
                               'company actually owns the goods.',
                       'tip': 'A flash title is when the transaction in the two sales happen at the same '
                              "time, so there's really not a clear distinction of when that middleman "
                              'company actually owns the goods.',
                       'timestamp': 927,
                       'timestamp_seconds': 927,
                       'timestamp_label': '[00:15:27]',
                       'url': 'https://www.youtube.com/watch?v=yR_RXKhapxo&t=927s',
                       'markdown': '[00:15:27](https://www.youtube.com/watch?v=yR_RXKhapxo&t=927s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mimI2zifsUA',
                       'title': 'Customs 101: Methods of valuation for import duty',
                       'channel': 'Chartered Inst. of Export & International Trade',
                       'author': 'Chartered Inst. of Export & International Trade',
                       'text': 'If customs asked whether you get a cheaper price because of the '
                               "intercompany relationship and you answered yes, then immediately you're "
                               'disqualifying yourself from using method one.',
                       'tip': 'If customs asked whether you get a cheaper price because of the '
                              "intercompany relationship and you answered yes, then immediately you're "
                              'disqualifying yourself from using method one.',
                       'timestamp': 708,
                       'timestamp_seconds': 708,
                       'timestamp_label': '[00:11:48]',
                       'url': 'https://www.youtube.com/watch?v=mimI2zifsUA&t=708s',
                       'markdown': '[00:11:48](https://www.youtube.com/watch?v=mimI2zifsUA&t=708s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
