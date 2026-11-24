from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'compliance-contracts-and-claims',
 'question_prompt': "Which audit, export, contracting, and claims rules apply once I'm buying, selling, or "
                    'contracting around government surplus?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Compliance, Contracts, and Claims',
 'subtitle': 'Resale-certificate misuse and audit liability, NY ST-120 and Texas certificates, exemption '
             'certificate management, ITAR, EAR, and FTR export rules, DLA DIBBS awards, inspections, '
             'shipping, and counteroffers, and surplus-funds claim contracts',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners across DLA awards, resale paperwork, and surplus-fund claims converge '
                      'on one rule: the file wins. Tristan Thomas treats traceability requests, '
                      'counteroffers, and informal cost breakdowns as signs an award is close, answers in '
                      'PDF on the original thread, and has refused government counteroffers and still won. '
                      'Thomas prices DLA bids at a 10 to 15 percent margin, judges profit in dollars, and '
                      'reads every award for PR numbers, inspection boxes, and IDC minimums. Sales-tax '
                      'operators insist a certificate must be complete, signed, dated, and plausible on '
                      'its face, with Texas giving 90 days after written notice and New York cutting off '
                      'single-use certificates at 90 days. Surplus-fund closers file the claim fast with a '
                      '$4 grant deed. Disagreement centers on verification depth: New York good faith '
                      'requires only retention, while others push lookups and periodic renewals.',
 'key_metrics': [{'label': 'DLA Bid Profit Margin Sweet Spot',
                  'metric': 'DLA Bid Profit Margin Sweet Spot',
                  'value': '10% to 15% (20% to 25% gets underbid)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Tristan Thomas's target margin when converting vendor cost, packaging, and "
                             'inspection into a DIBBS bid price.',
                  'source': 'Secureframe ([v7nJCLRc0uo @ 00:38:03])'},
                 {'label': 'Informal Cost Breakdown Example',
                  'metric': 'Informal Cost Breakdown Example',
                  'value': '6.75% profit; $50,895 total over 195 pieces = $261 per unit',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "MeND's Excel template rolling material, overhead, labor, other direct costs, "
                             'G&A, and packaging into a per-unit price used to answer counteroffers.',
                  'source': 'Tris10 @ MeND ([Y895jCYSE5A @ 00:11:46])'},
                 {'label': 'Texas Certificate Production Window',
                  'metric': 'Texas Certificate Production Window',
                  'value': '90 days after written Comptroller notice; keep certificates at least 4 years',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Deadline for a seller to produce missing exemption certificates in a Texas '
                             'audit; later deliveries are not accepted.',
                  'source': 'Tax Expert Today ([WZL5m9rfNSQ @ 00:03:20])'},
                 {'label': 'Grant Deed Copy Cost',
                  'metric': 'Grant Deed Copy Cost',
                  'value': 'About $4 per copy via Property Radar',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Greg's first move after a signed surplus-funds contract arrives: order the "
                             'grant deed, not the tax deed, to support the county claim.',
                  'source': 'Overage Acquisition ([X_Oq8vv4j_c @ 00:01:22])'}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Tristan Thomas of MeND Sourcing lists four documents a contracting officer '
                              'may demand before an award: a traceability request, a vendor capability '
                              'questionnaire, a counteroffer, and an informal cost breakdown, and says '
                              "receiving any one of them means the bid is 'this close' to winning "
                              '[Y895jCYSE5A @ 00:01:18]. The capability questionnaire typically lands on '
                              'newer companies or shops with one or two prior awards, because the '
                              'government wants proof the vendor can actually supply the item. After '
                              'roughly five years in business, MeND still gets traceability requests more '
                              'than any other form, and they arrive in different boilerplate wordings that '
                              'all ask for the same thing: proof the part comes from the source quoted in '
                              'the bid [Y895jCYSE5A @ 00:02:11]. Thomas ties this to how DLA ranks '
                              'bidders, telling a Secureframe audience that price is the number one '
                              'factor, followed by delivery time and credibility measured by the spur '
                              'score, which works like a FICO score built on on-time delivery and correct '
                              'parts [v7nJCLRc0uo @ 00:30:32]. MeND reports a spur score of 317, which '
                              'Thomas compares to a 780 to 800 FICO. The baseline is a clean paper trail '
                              'plus a delivery record the agency can trust.',
                              'On the sales-tax side, every practitioner starts from the same burden: the '
                              'seller carries the tax unless the file proves otherwise. Tax Expert Today '
                              'walks through Texas Tax Code section 151.054, under which every gross '
                              'receipt is presumed taxable until the seller accepts a properly completed '
                              'resale or exemption certificate, and good-faith acceptance shifts the '
                              'liability onto the buyer who signed [WZL5m9rfNSQ @ 00:00:16]. Hands Off '
                              'Sales Tax puts it bluntly: the buyer hands over the certificate, but the '
                              'vendor is the party on the hook, which is why vendors may reject a '
                              'certificate the buyer believes is fine [Q9wYQaLDoHQ @ 00:02:56]. The Sales '
                              'Tax Sisters, Stephanie and Mary Thomas, say an auditor will compare total '
                              "sales to taxable sales, and explaining the gap with 'John called me up and "
                              "told me he was exempt' gets you laughed out of the room [uZA19ayitYY @ "
                              '00:03:43]. Brian Greer of TaxConnex adds the cost of a gap: missing, '
                              'outdated, or invalid certificates lead the auditor to treat the sale as '
                              'taxable and assess tax, interest, and a penalty [FPLS7VL_qTA @ 00:03:01]. '
                              "Greer's default posture is to charge tax on any taxable item unless the "
                              'certificate is in hand, with the burden of supplying it sitting on the '
                              'buyer. No paper, no exemption.',
                              'Across DLA and surplus-fund work, the operators agree that the contract '
                              'itself, read end to end, is the compliance manual. Thomas lists not reading '
                              'the full solicitation down to the asterisks as the first of five fatal '
                              'mistakes MeND made early, because bidders who jump straight to the CLIN '
                              'miss who pays shipping and what packaging is required [v7nJCLRc0uo @ '
                              '00:45:05]. On awards, Thomas reads every page from page two down to the '
                              'asterisks, flowing sampling data and drawing revision letters to the '
                              'manufacturer on the purchase order, since the distributor may not '
                              'understand the specs but the manufacturer will [sG-wAF0b7kQ @ 00:05:25]. '
                              'Go-to-Market Solutions warns that FOB terms are not always in Section F; '
                              'they turn up in Section A or buried elsewhere, so the fix is to download '
                              "the solicitation and Ctrl-F or Command-F for 'FOB', 'inspection', and "
                              "'DCMA' [szkqa7FwjYE @ 00:00:31]. Greg of Overage Acquisition applies the "
                              'same discipline to surplus claims, having a VA locate the grant deed during '
                              'research, often before speaking to the claimant, so the claim ships the '
                              'moment the signed contract arrives. The shared baseline: know the paperwork '
                              'before the money is committed.'],
               'table': {'caption': 'Where the practitioners agree on contracts, certificates, and claims',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Pre-award document requests from the contracting officer signal a near '
                                   'win',
                                   'Answer traceability, capability questionnaire, counteroffer, or cost '
                                   'breakdown requests fast and fully',
                                   'Any one of the four requests means the contract is very close',
                                   'Tris10 @ MeND ([Y895jCYSE5A @ 00:01:58]) - Tristan Thomas on pre-award '
                                   'requests'],
                                  ['Price leads DLA evaluation, followed by delivery time and spur score',
                                   'Quote the lead time the vendor can actually hit, even past the '
                                   'requested date',
                                   'MeND has won awards quoting 300 days against a 25-day government ask',
                                   'Secureframe ([v7nJCLRc0uo @ 00:30:32]) - Tristan Thomas on DLA award '
                                   'factors'],
                                  ['Every Texas receipt is presumed taxable until a certificate rebuts it',
                                   'Accept only properly completed certificates at or before the sale in '
                                   'good faith',
                                   'Good-faith acceptance moves the tax liability onto the buyer who '
                                   'signed',
                                   'Tax Expert Today ([WZL5m9rfNSQ @ 00:00:16]) - Texas presumption and '
                                   'good faith'],
                                  ["A customer's verbal exemption claim is worthless when the auditor "
                                   'arrives',
                                   'Collect a signed, dated, fully completed certificate for every exempt '
                                   'sale',
                                   'Auditors compare total sales to taxable sales and demand written '
                                   'substantiation',
                                   'Sales Tax Sisters ([uZA19ayitYY @ 00:03:43]) - Stephanie and Mary '
                                   'Thomas on audits'],
                                  ['Missing or invalid certificates convert exempt sales into assessed tax',
                                   'Review each incoming certificate for name, tax ID, reason, date, and '
                                   'signature',
                                   'Auditor assesses tax, interest, and penalty when certificates cannot '
                                   'be produced',
                                   'TaxConnex ([FPLS7VL_qTA @ 00:02:42]) - Brian Greer on certificate '
                                   'management'],
                                  ['Read the full award down to the asterisks before ordering parts',
                                   'Highlight contract number, PR number, Box 7 administrator, and the '
                                   'facility box',
                                   'Missed caveats on shipping, packaging, or inspection sink fulfillment '
                                   'and credibility',
                                   'Tris10 @ MeND ([sG-wAF0b7kQ @ 00:02:51]) - Tristan Thomas on award '
                                   'review'],
                                  ['File surplus-fund claims immediately with the core supporting '
                                   'documents',
                                   'Submit grant deed, claimant ID, heirship affidavit, and death '
                                   'certificate right away',
                                   'Early filing leaves time to answer county requests for additional '
                                   'documents',
                                   'Overage Acquisition ([X_Oq8vv4j_c @ 00:03:33]) - Greg on post-contract '
                                   'claim filing']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Thomas's bid formula at the Secureframe summit is plain arithmetic: take "
                              'the vendor cost, for example 250 units at $185 for $46,250, add packaging '
                              "(MeND's minimum charge is $350), add any labeling cost and $250 if DCMA "
                              'inspection applies, add freight only when the award is not FOB origin, then '
                              'stack the profit on the subtotal and divide by quantity to get the bid '
                              'price entered in DIBBS [v7nJCLRc0uo @ 00:38:23]. The target margin is 10 to '
                              '15 percent; bidders opening at 20 to 25 percent simply get underbid '
                              '[v7nJCLRc0uo @ 00:10:01]. The bigger lever came when MeND stopped chasing a '
                              'percentage and asked whether the $7,035 profit justified the work; if '
                              '$6,500 or $6,000 would do, the lower bid price made MeND more competitive '
                              'and produced far more awards [v7nJCLRc0uo @ 00:39:51]. The same logic '
                              "powers MeND's informal cost breakdown template: material, material "
                              'overhead, labor, and other direct costs roll up to manufacturing cost, then '
                              'G&A and packaging, then a 6.75 percent profit, producing $50,895 across 195 '
                              'pieces, or $261 a unit [Y895jCYSE5A @ 00:11:19]. Thomas sends that Excel '
                              'sheet whenever an officer pushes back on price.',
                              'When an officer asks for traceability plus a 45 to 60 day quote extension, '
                              'Thomas first confirms the vendor still holds the old price, since requests '
                              'in February 2025 still referenced quotes pulled in June and July 2024, then '
                              'resubmits the same quote in DIBBS. Every document goes over as a PDF, never '
                              'a PNG, JPEG, or raw screenshot the government system may not display, and '
                              'the vendor price is redacted unless the email forbids it; if Thomas charges '
                              '$3 and pays $1.25, there is no reason to show the $1.25 [Y895jCYSE5A @ '
                              '00:05:27]. Replies go on the original email thread so the officer can trace '
                              "the history. Acceptable proof includes the vendor's quote PDF with logo and "
                              "manufacturer part number, a branded Word quote, or the vendor's pricing "
                              'email with signature. Counteroffers are negotiable: the officer anchors on '
                              'the last purchase price plus inflation, and MeND answered one by blaming '
                              'raw-material scarcity rather than a 3 percent CPI, attaching an informal '
                              'cost breakdown [Y895jCYSE5A @ 00:09:47]. On another, a $3 bid met a $1.50 '
                              'counteroffer and settled at $2.50. Go-to-Market Solutions flags the clause '
                              'to check before pricing: FOB origin shifts risk to the government at the '
                              'UPS scan, while FOB destination leaves damage and freight on the seller '
                              '[szkqa7FwjYE @ 00:01:07].',
                              'Award decoding is a checklist Thomas runs on every DLA award before a '
                              'purchase order goes to the vendor [sG-wAF0b7kQ @ 00:03:44]. Box 7 names the '
                              'administrator: DLA appears on destination-inspection awards, while DCMA '
                              'should appear when inspection is at origin. If the facility box in box 9 is '
                              'blank, inspection happens at destination; if it holds a CAGE code, '
                              'inspection happens at that location before anything ships. The PR number '
                              'ties the award back to the RFQ, and its prefix flags the contract type: a '
                              "PR starting with '100' marks an indefinite delivery contract, while '700' "
                              "or '090' marks a standalone buy for an exact quantity [sG-wAF0b7kQ @ "
                              "00:15:16]. Thomas's IDC example showed a flat $250,000 on page one that was "
                              'only the maximum value, with 2,712 guaranteed pieces, four estimated orders '
                              'of at least 2,260 each, a $31 unit price, 175-day delivery, and packaging '
                              'in groups of 25; nothing ships until a delivery order arrives. Go-to-Market '
                              'Solutions says inspection at your own CAGE location must be requested in '
                              'the bid with facility address, then confirmed on the award, with a call to '
                              'the contracting officer if it is unclear [szkqa7FwjYE @ 00:03:13].'],
               'table': {'caption': 'Street numbers and tools the operators actually use',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['DLA bid margin target for small-business contractors',
                                   '10 to 15 percent sweet spot; 20 to 25 percent gets underbid',
                                   'Price at margin, then ask whether the profit dollars justify the work',
                                   'Secureframe ([v7nJCLRc0uo @ 00:10:01]) - Tristan Thomas on bid '
                                   'pricing'],
                                  ['Informal cost breakdown sent with counteroffer replies',
                                   '6.75 percent profit; $50,895 across 195 pieces equals $261 per unit',
                                   'Build it with vendor input and attach the Excel file to justify price',
                                   'Tris10 @ MeND ([Y895jCYSE5A @ 00:11:46]) - Tristan Thomas on cost '
                                   'breakdowns'],
                                  ['Gov Scraper for daily RFQ research across DIBBS',
                                   '$100 per month; 8 to 10 minutes per RFQ cut to about 30 seconds',
                                   'Spend the saved hours on calls that build vendor relationships',
                                   'Secureframe ([v7nJCLRc0uo @ 00:55:03]) - Tristan Thomas on research '
                                   'time'],
                                  ['Grant deed pull for a surplus-funds county claim',
                                   'About $4 via Property Radar; certified copy from clerk recorder if '
                                   'requested',
                                   'Order the grant deed, not the tax deed, and file the claim immediately',
                                   'Overage Acquisition ([X_Oq8vv4j_c @ 00:01:22]) - Greg on claim '
                                   'documents'],
                                  ['Cook County surplus motion attorney fee negotiation',
                                   '$3,500 upfront quote rejected; local attorney cut $2,500 to $1,250 '
                                   'contingency',
                                   'Recruit a known attorney, explain the state law, and negotiate '
                                   'contingency',
                                   'Money Making Juggernaut ([MmWoRR82S9g @ 00:05:06]) - Sheila on '
                                   'attorney fees'],
                                  ['New York ST-120 single-use certificate and misuse exposure',
                                   'Dated within 90 days; 100 percent tax penalty plus $50 per fraudulent '
                                   'certificate',
                                   'Prefer blanket certificates on file for repeat customers to avoid date '
                                   'traps',
                                   'Matt Sokol Business ([Y3GHPpoT08s @ 00:06:16]) - Matt Sokol on ST-120 '
                                   'rules'],
                                  ['Texas certificate retention and audit production deadline',
                                   'Keep at least 4 years; produce within 90 days of written notice',
                                   'Build the certificate file before the sale and store it with invoices',
                                   'Tax Expert Today ([WZL5m9rfNSQ @ 00:03:20]) - Texas audit window']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Field Moves That Win the Paperwork Fight',
                           'body': 'Four plays the speakers run to hold price, build supplier leverage, '
                                   'cut claim costs, and harden certificate files.',
                           'items': ['Refuse a counteroffer when the math does not work: MeND has told '
                                     'officers this is our price, do what you want, and still won the '
                                     'award, backing the number with an Excel informal cost breakdown '
                                     '[Tris10 @ MeND — Y895jCYSE5A @ 00:08:22].',
                                     'Turn every vendor no-bid into a phone call using the number in the '
                                     "email signature; one of MeND's biggest authorized partners started "
                                     'as a no-bid [Secureframe — v7nJCLRc0uo @ 00:54:07].',
                                     'Negotiate surplus-fund counsel: Sheila turned down a $3,500 upfront '
                                     'attorney fee, then talked a local attorney from $2,500 down to '
                                     '$1,250 on contingency for the Cook County motion [Money Making '
                                     'Juggernaut — MmWoRR82S9g @ 00:05:06].',
                                     "Go past bare good faith on New York ST-120s: run the buyer's EIN or "
                                     'certificate of authority number through the state vendor lookup to '
                                     'confirm business name and registered address [Matt Sokol Business — '
                                     'Y3GHPpoT08s @ 00:09:07].']},
               'sop_steps': [{'step': 1,
                              'title': 'Decode the award before issuing a vendor PO',
                              'action': 'Highlight contract number, award date, PR number, Box 7 '
                                        'administrator, and the facility box on page one.',
                              'detail': 'A blank facility box means destination inspection; a CAGE code '
                                        'means inspection at that site before shipping; a PR starting with '
                                        '100 means an IDC with no quantity until a delivery order lands; '
                                        'flow sampling data and drawing revision letters to the '
                                        'manufacturer [Tris10 @ MeND — sG-wAF0b7kQ @ 00:03:03].'},
                             {'step': 2,
                              'title': 'Answer traceability in PDF on the same thread',
                              'action': 'Reconfirm vendor pricing, convert the vendor quote or email to '
                                        'PDF, redact cost unless forbidden, and reply on the original '
                                        'email.',
                              'detail': 'The government system may not read PNGs, JPEGs, or small '
                                        'screenshots, and replying in-thread lets the officer trace the '
                                        'full history; resubmit the DIBBS quote if a 45 to 60 day '
                                        'extension is requested [Tris10 @ MeND — Y895jCYSE5A @ 00:05:11].'},
                             {'step': 3,
                              'title': 'Build the bid price or counter from the cost stack',
                              'action': 'Add vendor cost, packaging, labeling, DCMA inspection, and '
                                        'freight when not FOB origin, then add profit and divide by '
                                        'quantity.',
                              'detail': 'Example: 250 units at $185 is $46,250, plus a $350 packaging '
                                        'minimum and $250 inspection, plus $7,035 profit; test whether the '
                                        'profit dollars justify the work and trim to win [Secureframe — '
                                        'v7nJCLRc0uo @ 00:38:23].'},
                             {'step': 4,
                              'title': 'Lock the certificate file before the sale',
                              'action': 'Collect a complete certificate, check its stated reason against '
                                        'what the customer buys, and file it with the supporting invoices.',
                              'detail': 'Texas Rule 3.287 requires purchaser name and address, item '
                                        'description, exemption reason, signature and date, and seller '
                                        'name and address; keep it at least 4 years, since missing '
                                        'certificates must be produced within 90 days of written notice '
                                        '[Tax Expert Today — WZL5m9rfNSQ @ 00:03:37].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Pricing posture is the sharpest split in the DLA lane. Tristan Thomas of '
                              'Tris10 @ MeND treats a contracting officer counteroffer as an opening move, '
                              'not an order: the MeND team has told buyers this is our price, it is what '
                              'it is, do what you want, and still won the award [Y895jCYSE5A @ 00:08:22]. '
                              'When Tristan does bend, the play is to meet in the middle, answering a '
                              '$1.50 government ask on a $3 bid with $2.50, and attaching an informal cost '
                              'breakdown that blames a raw-material supply shortage rather than the 3% CPI '
                              'logic the buyer used [Y895jCYSE5A @ 00:09:02]. On the Secureframe stage, '
                              'the same operator argues the margin side: newcomers who open at 20 to 25 '
                              'percent simply get underbid, and the sweet spot sits between 10 and 15 '
                              'percent [v7nJCLRc0uo @ 00:10:01]. The bigger reversal came when the team '
                              'stopped chasing a margin percentage and asked whether raw profit dollars, '
                              '$7,035 in the worked example, justified the work; trimming that to $6,500 '
                              'or $6,000 lowered the bid price and produced far more awards [v7nJCLRc0uo @ '
                              '00:39:33]. Delivery promises follow the same contrarian logic, because '
                              'Tristan quotes the lead time the vendor can actually hit and has won awards '
                              'quoting 300 days against a requested 25.',
                              'Fulfillment strategy splits sharply on who controls inspection and '
                              'packaging. Go-to-Market Solutions pushes operators to take control up '
                              'front: if you want DCMA inspecting at your own CAGE location, request it in '
                              'the bid with your CAGE code and facility address, confirm the award '
                              'actually lists it, and call the contracting officer instead of assuming '
                              '[szkqa7FwjYE @ 00:03:13]. Tris10 @ MeND reads the same question straight '
                              'off the finished award: a blank facility box means inspection at '
                              'destination, while a CAGE code in that box means origin inspection before '
                              'anything ships [sG-wAF0b7kQ @ 00:03:59]. On packaging, Tristan Thomas lays '
                              'out two distinct playbooks for the Secureframe summit audience. ASM D3951 '
                              'commercial packaging is low cost and something people can handle '
                              'themselves, but newcomers should just bid, build vendor relationships, and '
                              'outsource MIL-STD-2073 work and MIL-STD-129 labels, ideally shopping two or '
                              'three packaging partners because many packaging houses charge an insane '
                              'amount that kills competitiveness [v7nJCLRc0uo @ 00:44:36]. Tristan also '
                              'flatly rejects the popular advice to mine RFQs 60 to 90 days old on the '
                              'theory that nobody bid; according to DLA contacts, those stale listings are '
                              'leftovers from internal reassignments nobody closed out, so the MeND team '
                              'works newest-first and knocks them out one by one [v7nJCLRc0uo @ 00:20:44].',
                              'Sales tax certificate practitioners split on how much policing a seller '
                              'owes and how forgiving the audit clock runs. Brian Greer of TaxConnex '
                              "frames it as the buyer's job to hand over the exemption certificate, with "
                              'the seller charging tax by default until one arrives and then checking '
                              'customer name, state ID number, reason, date and signature [FPLS7VL_qTA @ '
                              "00:03:44]. Matt Sokol calls New York's good-faith standard somewhat loose: "
                              'accept the ST-120, retain it on file, and you are covered, with a vendor '
                              'lookup by EIN or certificate of authority number as an optional extra step '
                              '[Y3GHPpoT08s @ 00:07:01]. The Sales Tax Sisters push harder, telling '
                              'sellers to smell-test every certificate, toss one where a candy seller '
                              'claims resale on a cash register, and verify exempt status in the '
                              "Comptroller's searchable taxpayer database. They also say Texas lets a "
                              'seller rehab a missing certificate inside an audit years later under '
                              'increased scrutiny, while New York shuts the door 90 days after the '
                              'transaction [uZA19ayitYY @ 00:16:30]. Tax Expert Today describes a tighter '
                              'Texas clock: after written notice the seller has 90 days to produce '
                              'certificates, later deliveries are rejected, and anything gathered once '
                              'fieldwork begins is verified before it counts [WZL5m9rfNSQ @ 00:03:20].'],
               'table': {'caption': 'Side-by-side playbooks where practitioners take different routes on '
                                    'DLA bids, sales tax paper, and surplus claims',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Responding to a contracting officer counteroffer on unit price',
                                   'Hold firm and tell the buyer this is our price; the MeND team has '
                                   'still won the award',
                                   'Meet in the middle, such as $2.50 against a $1.50 ask on a $3 bid, '
                                   'backed by an informal cost breakdown',
                                   'Tris10 @ MeND ([Y895jCYSE5A @ 00:08:22]); Tris10 @ MeND ([Y895jCYSE5A '
                                   '@ 00:09:02])'],
                                  ['Setting the profit layer on a DLA bid price',
                                   'Target a 10 to 15 percent margin because 20 to 25 percent openers get '
                                   'underbid',
                                   'Ignore percentage and ask whether profit dollars like $7,035 justify '
                                   'the work, then trim toward $6,000',
                                   'Secureframe ([v7nJCLRc0uo @ 00:38:03]); Secureframe ([v7nJCLRc0uo @ '
                                   '00:39:33])'],
                                  ['Controlling where DCMA inspection of supplies takes place',
                                   'Request inspection at your own CAGE location in the bid, then confirm '
                                   'it on the award',
                                   'Read the facility box on the award: blank means destination, a CAGE '
                                   'code means origin',
                                   'Go-to-Market Solutions ([szkqa7FwjYE @ 00:03:13]); Tris10 @ MeND '
                                   '([sG-wAF0b7kQ @ 00:03:59])'],
                                  ['Handling packaging requirements on awarded DLA contracts',
                                   'Do ASM D3951 commercial packaging in-house because it is low cost and '
                                   'simple enough',
                                   'Outsource MIL-STD-2073 and MIL-STD-129 work and shop two or three '
                                   'competing packaging partners',
                                   'Secureframe ([v7nJCLRc0uo @ 00:41:06]); Secureframe ([v7nJCLRc0uo @ '
                                   '00:48:11])'],
                                  ['Validating a resale certificate handed over by a customer',
                                   'Accept in good faith and retain on file; the New York vendor lookup is '
                                   'an optional extra',
                                   'Smell-test every certificate and verify exempt status in the '
                                   'Comptroller searchable taxpayer database',
                                   'Matt Sokol Business ([Y3GHPpoT08s @ 00:07:01]); Sales Tax Sisters '
                                   '([uZA19ayitYY @ 00:15:07])'],
                                  ['Fixing a missing certificate after the sale already closed',
                                   'Texas lets you rehab inside an audit years later, under increased '
                                   'scrutiny from the auditor',
                                   'After written Comptroller notice the seller gets 90 days; later '
                                   'certificates are not accepted at all',
                                   'Sales Tax Sisters ([uZA19ayitYY @ 00:16:30]); Tax Expert Today '
                                   '([WZL5m9rfNSQ @ 00:03:20])'],
                                  ['Sourcing surplus funds leads and claimant contact data',
                                   'Buy a fully skip traced, DNC-checked Texas and Georgia list with a '
                                   'two-hour training for $50',
                                   'Dig Cook County judicial sale records in person, where fewer '
                                   'competitors bother to look',
                                   'Money Making Juggernaut ([KdtNDjlE4WQ @ 00:01:33]); Money Making '
                                   'Juggernaut ([MmWoRR82S9g @ 00:08:23])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive DLA mistakes surface after the win. Tristan Thomas of '
                              'Tris10 @ MeND admits that when the team won its first contract three months '
                              'into bidding, nobody knew what to do with it, and every question to DLA '
                              'came back as file a mod or call the contracting officer [sG-wAF0b7kQ @ '
                              '00:00:25]. The recurring client trap is the indefinite delivery contract: '
                              'an award showing a flat $250,000 is only the maximum value, flagged by a PR '
                              'number starting 1-0-0, with zero quantity until a delivery order arrives; '
                              'the example guaranteed just 2,712 pieces, was issued October 5, 2023, and '
                              'drew its first delivery order two weeks later [sG-wAF0b7kQ @ 00:14:13]. On '
                              "the bid side, Tristan's Secureframe list of fatal mistakes opens with not "
                              'reading the solicitation down to the asterisks, which hides who pays '
                              'freight and what packaging applies, then trusting one supplier quote '
                              'without tracking why bids were lost [v7nJCLRc0uo @ 00:45:32]. Go-to-Market '
                              'Solutions sees the same blind spot in shipping: FOB terms hide in section '
                              'F, section A or elsewhere, and on FOB destination the box, including any '
                              'damage, belongs to the seller all the way to the government warehouse '
                              '[szkqa7FwjYE @ 00:01:23]. Tristan adds that packaging can cost more than '
                              'the physical part, which wrecks any bid priced on item cost alone.',
                              'Sales tax audits punish files that look complete but are not. The Sales Tax '
                              'Sisters say a seller who explains exempt sales by saying a customer named '
                              'John phoned in a claim will be laughed out of the room, and clients '
                              "routinely file a customer's sales tax permit or a 501(c)(3) IRS letter as "
                              'if it were a certificate, when neither substantiates a tax-free sale '
                              '[uZA19ayitYY @ 00:12:48]. Tax Expert Today adds that a Texas certificate '
                              'missing any of the five Rule 3.287 items is disallowed no matter when it '
                              'was obtained, that knowing misuse runs from a class C misdemeanor below $20 '
                              'to a second degree felony at $20,000 or more, and that sellers must keep '
                              'certificates at least four years [WZL5m9rfNSQ @ 00:02:07]. TaxConnex '
                              "describes the auditor's default move: any exempt line without a valid, "
                              'current certificate is treated as taxable and assessed tax, interest and a '
                              "penalty [FPLS7VL_qTA @ 00:03:01]. Matt Sokol lists New York's misuse "
                              'penalties at 100 percent of the tax due plus a $50 penalty for each '
                              'fraudulent certificate issued, with possible revocation of the certificate '
                              'of authority [Y3GHPpoT08s @ 00:06:16]. Hands Off Sales Tax explains why '
                              'vendors grow strict: the liability sits with the vendor, so a vendor can '
                              'reject a certificate even when the buyer believes it is correct.',
                              'Surplus funds and export work carry their own firsthand traps. Money Making '
                              'Juggernaut warns that Texas and Georgia non-judicial deals hide costs only '
                              'the foreclosure attorney or trustee can see, including accrued interest, '
                              "the cost of the sale and the trustee's commission, so due diligence on "
                              'additional debt and liens has to come first [KdtNDjlE4WQ @ 00:01:03]. '
                              'Sheila, a 20-year Chicago broker featured on the same channel, spent about '
                              'eight months hunting one claimant with no phone number or address and '
                              'another month before a cautious niece passed the contact along; on an '
                              'earlier deal Sheila went to court acting as the attorney and the judge '
                              'laughed and ruled Sheila could not be part of the case. The attorney fix '
                              'had its own math problem: $3,500 up front felt too risky on a credit card, '
                              "and a $2,500 fee made no sense against one claimant's $19,000, so Sheila "
                              'negotiated $1,250 on contingency [MmWoRR82S9g @ 00:05:06]. On the export '
                              'side, Go Ask David flags the deemed export, where showing controlled '
                              'technical data to a colleague from Japan at a conference in Arizona still '
                              'counts as an export [c89xP1NJIx0 @ 00:04:21], and Cleared Systems prices '
                              'violations at hefty fines, criminal charges and loss of export privileges '
                              '[tEbWiX3Z22A @ 00:01:31].'],
               'table': {'caption': 'Firsthand failure modes with the economics or exposure each one '
                                    'created for the operator',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics or Exposure',
                                     'Expert Source'],
                         'rows': [['Misreading a flat $250,000 IDC award as real booked revenue',
                                   'Clients send over awards excited about the dollar figure while the '
                                   'line quantity shows zero',
                                   'Only the guaranteed minimum of 2,712 pieces is assured; $250,000 is '
                                   'just the contract ceiling',
                                   'Tris10 @ MeND ([sG-wAF0b7kQ @ 00:12:58])'],
                                  ['Answering traceability requests with stale vendor pricing still on '
                                   'file',
                                   'Traceability requests arriving in February 2025 hit quotes originally '
                                   'pulled in June and July 2024',
                                   'Resubmitting at an old price can erase margin, so re-confirm the '
                                   'vendor still holds it first',
                                   'Tris10 @ MeND ([Y895jCYSE5A @ 00:03:32])'],
                                  ['Sending screenshots or PNG files to the contracting officer',
                                   'Government systems cannot see PNGs or render small images, so key '
                                   'details get lost',
                                   'Convert every traceability file to PDF and redact your cost unless '
                                   'told you cannot',
                                   'Tris10 @ MeND ([Y895jCYSE5A @ 00:05:11])'],
                                  ['Underestimating per-item packaging cost when building the bid price',
                                   'Packaging an item has cost more than the actual physical part inside '
                                   'the box',
                                   'A $350 packaging minimum and $250 DCMA inspection belong in the '
                                   'subtotal before margin',
                                   'Secureframe ([v7nJCLRc0uo @ 00:36:36]); Secureframe ([v7nJCLRc0uo @ '
                                   '00:38:23])'],
                                  ['Missing FOB destination terms buried deep inside the solicitation',
                                   'Bidders realize too late they are the ones responsible for the '
                                   'shipping all the way',
                                   'Freight and any in-transit damage are on you, so ship with tracking '
                                   'and insurance',
                                   'Go-to-Market Solutions ([szkqa7FwjYE @ 00:05:35])'],
                                  ['Filing customer permits or 501(c)(3) letters as exemption certificates',
                                   'Clients feel covered until reviewers find permits and IRS letters '
                                   'instead of real certificates',
                                   'The auditor treats those exempt sales as taxable and assesses tax, '
                                   'interest and penalty',
                                   'Sales Tax Sisters ([uZA19ayitYY @ 00:12:48]); TaxConnex ([FPLS7VL_qTA '
                                   '@ 00:03:01])'],
                                  ['Trusting the visible surplus figure on a non-judicial foreclosure sale',
                                   'Accrued interest, sale costs and the trustee commission stay visible '
                                   'only to the trustee',
                                   'The headline surplus overstates the claim until due diligence on liens '
                                   'and debt is done',
                                   'Money Making Juggernaut ([KdtNDjlE4WQ @ 00:01:03])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checkpoints Before Money or Paper Moves',
                           'body': 'Each checkpoint comes straight from a loss, reversal, or near miss the '
                                   'practitioners hit firsthand. Clear all four before you quote, ship, '
                                   'release a tax-free sale, or sign counsel on a surplus claim.',
                           'items': ['Before quoting, read the PR number: 1-0-0 means an estimated IDC '
                                     'quantity, while 700 or 090 means a firm quantity you must supply '
                                     '[Tris10 @ MeND — sG-wAF0b7kQ @ 00:15:16].',
                                     'Before answering a traceability request, re-confirm the vendor '
                                     'price, convert everything to PDF, and reply inside the same email '
                                     'thread [Tris10 @ MeND — Y895jCYSE5A @ 00:06:09].',
                                     'Before releasing a tax-free sale, hold a complete, signed, dated '
                                     'certificate whose stated reason matches what the customer actually '
                                     'buys [Tax Expert Today — WZL5m9rfNSQ @ 00:03:37].',
                                     'Before signing a surplus attorney, size the fee against the claimant '
                                     'share; $2,500 on $19,000 failed and $1,250 contingency worked [Money '
                                     'Making Juggernaut — MmWoRR82S9g @ 00:04:46].']}}],
 'pull_quote': 'Get the documentation upfront when everybody still likes each other. Sales Tax Sisters '
               '(uZA19ayitYY @ 00:15:59).',
 'diagram_id': 'diag-08',
 'action_checklist': ['Download every solicitation and press Ctrl-F or Command-F for FOB, inspection, and '
                      'DCMA before pricing a single line [Go-to-Market Solutions — szkqa7FwjYE @ '
                      '00:00:46].',
                      'Build an informal cost breakdown with your vendor covering material, material '
                      'overhead, labor, other direct costs, G&A, packaging, and profit to defend your '
                      'price on counteroffers [Tris10 @ MeND — Y895jCYSE5A @ 00:11:19].',
                      'Price bids from vendor cost plus packaging, inspection, and freight when the '
                      'government is not paying, then divide by quantity and judge the profit dollars '
                      '[Secureframe — v7nJCLRc0uo @ 00:38:23].',
                      'Follow every vendor quote email or no-bid reply with a phone call to the person in '
                      'the signature block [Secureframe — v7nJCLRc0uo @ 00:53:55].',
                      'Order the grant deed copy for about $4, file the claim fast with ID, affidavit, and '
                      'death certificate, then send the claimant the USPS tracking number and call the '
                      'county [Overage Acquisition — X_Oq8vv4j_c @ 00:01:22].',
                      'Request fresh exemption certificates at least every couple of years, annually in '
                      'Florida, and add management software once you pass roughly 1,000 exempt customers '
                      '[TaxConnex — FPLS7VL_qTA @ 00:04:59].'],
 'statutory_citations': [{'title': 'Tris10 @ MeND — Traceability, Cost Breakdowns, and Counteroffers for '
                                   'Government Contracts - DLA / DIBBS [00:07:43]',
                          'url': 'https://www.youtube.com/watch?v=Y895jCYSE5A&t=463s',
                          'relevance': 'Primary practitioner testimony on counteroffers, traceability '
                                       'PDFs, price redaction, and informal cost breakdowns.'},
                         {'title': 'Tris10 @ MeND — Understanding Your DLA Award - Uncover Potential '
                                   'Pitfalls and Mistakes [00:14:13]',
                          'url': 'https://www.youtube.com/watch?v=sG-wAF0b7kQ&t=853s',
                          'relevance': 'Primary practitioner testimony on indefinite delivery contracts, '
                                       'PR number codes, and inspection location reads.'},
                         {'title': 'Secureframe — Defense Logistics Agency Contracts: How to Bid '
                                   'Effectively with the DLA [00:45:05]',
                          'url': 'https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2705s',
                          'relevance': 'Primary practitioner testimony on the five fatal DLA bidding '
                                       'mistakes, margin strategy, and packaging costs.'},
                         {'title': 'Sales Tax Sisters — Sales Tax Compliance- Top 5 Resale Certificate & '
                                   'Exemption Certificate Mistakes [00:16:30]',
                          'url': 'https://www.youtube.com/watch?v=uZA19ayitYY&t=990s',
                          'relevance': 'Primary practitioner testimony on certificate mistakes, permits '
                                       'versus certificates, and late-certificate windows.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Y895jCYSE5A',
                       'title': 'Traceability, Cost Breakdowns, and Counteroffers for Government Contracts '
                                '- DLA / DIBBS',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': 'Just because they are giving you a counter offer does not mean that you '
                               'necessarily have to agree to it to win the award.',
                       'tip': 'Just because they are giving you a counter offer does not mean that you '
                              'necessarily have to agree to it to win the award.',
                       'timestamp': 490,
                       'timestamp_seconds': 490,
                       'timestamp_label': '[00:08:10]',
                       'url': 'https://www.youtube.com/watch?v=Y895jCYSE5A&t=490s',
                       'markdown': '[00:08:10](https://www.youtube.com/watch?v=Y895jCYSE5A&t=490s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y895jCYSE5A',
                       'title': 'Traceability, Cost Breakdowns, and Counteroffers for Government Contracts '
                                '- DLA / DIBBS',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': 'I want to ensure that all the traceability documents that I send over to '
                               'them are in PDF form.',
                       'tip': 'I want to ensure that all the traceability documents that I send over to '
                              'them are in PDF form.',
                       'timestamp': 311,
                       'timestamp_seconds': 311,
                       'timestamp_label': '[00:05:11]',
                       'url': 'https://www.youtube.com/watch?v=Y895jCYSE5A&t=311s',
                       'markdown': '[00:05:11](https://www.youtube.com/watch?v=Y895jCYSE5A&t=311s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tEbWiX3Z22A',
                       'title': 'What is ITAR Compliance? | Cleared Systems',
                       'channel': 'Cleared Systems',
                       'author': 'Cleared Systems',
                       'text': 'Penalties for violations can include hefty fines, criminal charges, and '
                               'even the loss of export privileges.',
                       'tip': 'Penalties for violations can include hefty fines, criminal charges, and '
                              'even the loss of export privileges.',
                       'timestamp': 91,
                       'timestamp_seconds': 91,
                       'timestamp_label': '[00:01:31]',
                       'url': 'https://www.youtube.com/watch?v=tEbWiX3Z22A&t=91s',
                       'markdown': '[00:01:31](https://www.youtube.com/watch?v=tEbWiX3Z22A&t=91s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uZA19ayitYY',
                       'title': 'Sales Tax Compliance- Top 5 Resale Certificate & Exemption Certificate '
                                'Mistakes',
                       'channel': 'Sales Tax Sisters',
                       'author': 'Sales Tax Sisters',
                       'text': "There are some states like New York, if you don't get that certificate "
                               "within 90 days of the transaction, you're out of luck.",
                       'tip': "There are some states like New York, if you don't get that certificate "
                              "within 90 days of the transaction, you're out of luck.",
                       'timestamp': 990,
                       'timestamp_seconds': 990,
                       'timestamp_label': '[00:16:30]',
                       'url': 'https://www.youtube.com/watch?v=uZA19ayitYY&t=990s',
                       'markdown': '[00:16:30](https://www.youtube.com/watch?v=uZA19ayitYY&t=990s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WZL5m9rfNSQ',
                       'title': 'Texas Sales Tax Exemption Certificate: Who Pays If It Fails (2026)',
                       'channel': 'Tax Expert Today',
                       'author': 'Tax Expert Today',
                       'text': 'Miss one and the certificate is incomplete. An incomplete certificate is '
                               'disallowed in an audit, no matter when it was obtained.',
                       'tip': 'Miss one and the certificate is incomplete. An incomplete certificate is '
                              'disallowed in an audit, no matter when it was obtained.',
                       'timestamp': 110,
                       'timestamp_seconds': 110,
                       'timestamp_label': '[00:01:50]',
                       'url': 'https://www.youtube.com/watch?v=WZL5m9rfNSQ&t=110s',
                       'markdown': '[00:01:50](https://www.youtube.com/watch?v=WZL5m9rfNSQ&t=110s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lnmHPqYrNN8',
                       'title': 'How YOU SHOULD Actually Obtain And Use Resale Certificates',
                       'channel': 'Hands Off Sales Tax (HOST)',
                       'author': 'Hands Off Sales Tax (HOST)',
                       'text': 'Using the wrong form, even with the correct information, can still cause '
                               'delays or rejections.',
                       'tip': 'Using the wrong form, even with the correct information, can still cause '
                              'delays or rejections.',
                       'timestamp': 97,
                       'timestamp_seconds': 97,
                       'timestamp_label': '[00:01:37]',
                       'url': 'https://www.youtube.com/watch?v=lnmHPqYrNN8&t=97s',
                       'markdown': '[00:01:37](https://www.youtube.com/watch?v=lnmHPqYrNN8&t=97s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KdtNDjlE4WQ',
                       'title': '5+ Million in Surplus Opportunities Texas and Georgia 11/4 sale',
                       'channel': 'Money Making Juggernaut',
                       'author': 'Money Making Juggernaut',
                       'text': "You have to perform due diligence. You have to check to see if there's any "
                               'additional debt or any liens.',
                       'tip': "You have to perform due diligence. You have to check to see if there's any "
                              'additional debt or any liens.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=KdtNDjlE4WQ&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=KdtNDjlE4WQ&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MmWoRR82S9g',
                       'title': 'Realtor Tries Surplus Funds And Does $94,000 in Deals In Her First Year',
                       'channel': 'Money Making Juggernaut',
                       'author': 'Money Making Juggernaut',
                       'text': 'He said okay and he lowered his fee to 1250 on contingency.',
                       'tip': 'He said okay and he lowered his fee to 1250 on contingency.',
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=MmWoRR82S9g&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=MmWoRR82S9g&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'X_Oq8vv4j_c',
                       'title': 'Got a Surplus Funds Contract? Here’s Your Next Move',
                       'channel': 'Overage Acquisition',
                       'author': 'Overage Acquisition',
                       'text': 'We want to get this claim in as quickly as possible to the county, because '
                               'in case they asked for any other additional supporting documentation, '
                               "we'll have plenty of time to do that.",
                       'tip': 'We want to get this claim in as quickly as possible to the county, because '
                              "in case they asked for any other additional supporting documentation, we'll "
                              'have plenty of time to do that.',
                       'timestamp': 116,
                       'timestamp_seconds': 116,
                       'timestamp_label': '[00:01:56]',
                       'url': 'https://www.youtube.com/watch?v=X_Oq8vv4j_c&t=116s',
                       'markdown': '[00:01:56](https://www.youtube.com/watch?v=X_Oq8vv4j_c&t=116s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sG-wAF0b7kQ',
                       'title': 'Understanding Your DLA Award - Uncover Potential Pitfalls and Mistakes',
                       'channel': 'Tris10 @ MeND',
                       'author': 'Tris10 @ MeND',
                       'text': "If that PR number on that bid is a one 0, do know that they're giving you "
                               "an estimate quantity of what they're needing, not an actual quantity.",
                       'tip': "If that PR number on that bid is a one 0, do know that they're giving you "
                              "an estimate quantity of what they're needing, not an actual quantity.",
                       'timestamp': 916,
                       'timestamp_seconds': 916,
                       'timestamp_label': '[00:15:16]',
                       'url': 'https://www.youtube.com/watch?v=sG-wAF0b7kQ&t=916s',
                       'markdown': '[00:15:16](https://www.youtube.com/watch?v=sG-wAF0b7kQ&t=916s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'szkqa7FwjYE',
                       'title': 'DLA Inspections and Shipping Simplified: Step-by-Step Guide',
                       'channel': 'Go-to-Market Solutions',
                       'author': 'Go-to-Market Solutions',
                       'text': "If it's FOB destination you're responsible for the bolts all the way to "
                               'the government warehouse.',
                       'tip': "If it's FOB destination you're responsible for the bolts all the way to the "
                              'government warehouse.',
                       'timestamp': 67,
                       'timestamp_seconds': 67,
                       'timestamp_label': '[00:01:07]',
                       'url': 'https://www.youtube.com/watch?v=szkqa7FwjYE&t=67s',
                       'markdown': '[00:01:07](https://www.youtube.com/watch?v=szkqa7FwjYE&t=67s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FPLS7VL_qTA',
                       'title': 'Sales Tax Bytes Ep. 11 | Exemption Certificate Management',
                       'channel': 'TaxConnex',
                       'author': 'TaxConnex',
                       'text': "If you don't have them and if they're not up-to-date, they're not valid, "
                               "what's going to happen is that auditor is going to assume that that "
                               'transaction was taxable.',
                       'tip': "If you don't have them and if they're not up-to-date, they're not valid, "
                              "what's going to happen is that auditor is going to assume that that "
                              'transaction was taxable.',
                       'timestamp': 162,
                       'timestamp_seconds': 162,
                       'timestamp_label': '[00:02:42]',
                       'url': 'https://www.youtube.com/watch?v=FPLS7VL_qTA&t=162s',
                       'markdown': '[00:02:42](https://www.youtube.com/watch?v=FPLS7VL_qTA&t=162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'v7nJCLRc0uo',
                       'title': 'Defense Logistics Agency Contracts: How to Bid Effectively with the DLA',
                       'channel': 'Secureframe',
                       'author': 'Secureframe',
                       'text': 'We looked at the profit dollar amount and asked ourselves this one '
                               'question: does this $7,035 justify the amount of work that I need to do.',
                       'tip': 'We looked at the profit dollar amount and asked ourselves this one '
                              'question: does this $7,035 justify the amount of work that I need to do.',
                       'timestamp': 2373,
                       'timestamp_seconds': 2373,
                       'timestamp_label': '[00:39:33]',
                       'url': 'https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2373s',
                       'markdown': '[00:39:33](https://www.youtube.com/watch?v=v7nJCLRc0uo&t=2373s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fPLM1TULIx4',
                       'title': 'The Three R’s of Export Compliance: FTR, EAR & ITAR Explained',
                       'channel': 'Shipping Solutions',
                       'author': 'Shipping Solutions',
                       'text': 'ITAR violations can lead to severe penalties that can bar your company '
                               'from future exports.',
                       'tip': 'ITAR violations can lead to severe penalties that can bar your company from '
                              'future exports.',
                       'timestamp': 152,
                       'timestamp_seconds': 152,
                       'timestamp_label': '[00:02:32]',
                       'url': 'https://www.youtube.com/watch?v=fPLM1TULIx4&t=152s',
                       'markdown': '[00:02:32](https://www.youtube.com/watch?v=fPLM1TULIx4&t=152s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'c89xP1NJIx0',
                       'title': 'How the US regulates international business | What is the ITAR?',
                       'channel': 'Go Ask David',
                       'author': 'Go Ask David',
                       'text': 'If you show some controlled information to a colleague from Japan while '
                               "both of you are at a conference in Arizona, you're still making an export.",
                       'tip': 'If you show some controlled information to a colleague from Japan while '
                              "both of you are at a conference in Arizona, you're still making an export.",
                       'timestamp': 261,
                       'timestamp_seconds': 261,
                       'timestamp_label': '[00:04:21]',
                       'url': 'https://www.youtube.com/watch?v=c89xP1NJIx0&t=261s',
                       'markdown': '[00:04:21](https://www.youtube.com/watch?v=c89xP1NJIx0&t=261s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q9wYQaLDoHQ',
                       'title': 'Stop MISUSING Resale Certificates Before Your Audit!',
                       'channel': 'Hands Off Sales Tax (HOST)',
                       'author': 'Hands Off Sales Tax (HOST)',
                       'text': 'A missing certificate can turn an otherwise legitimate resale transaction '
                               'into unexpected tax exposure.',
                       'tip': 'A missing certificate can turn an otherwise legitimate resale transaction '
                              'into unexpected tax exposure.',
                       'timestamp': 258,
                       'timestamp_seconds': 258,
                       'timestamp_label': '[00:04:18]',
                       'url': 'https://www.youtube.com/watch?v=Q9wYQaLDoHQ&t=258s',
                       'markdown': '[00:04:18](https://www.youtube.com/watch?v=Q9wYQaLDoHQ&t=258s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Y3GHPpoT08s',
                       'title': 'Tips For Accepting a ST-120 New York State Resale Certificate for Sales '
                                'Tax Exemption',
                       'channel': 'Matt Sokol Business',
                       'author': 'Matt Sokol Business',
                       'text': "If it's the case that it is a single use certificate it has to be dated "
                               'within 90 days of that transaction.',
                       'tip': "If it's the case that it is a single use certificate it has to be dated "
                              'within 90 days of that transaction.',
                       'timestamp': 144,
                       'timestamp_seconds': 144,
                       'timestamp_label': '[00:02:24]',
                       'url': 'https://www.youtube.com/watch?v=Y3GHPpoT08s&t=144s',
                       'markdown': '[00:02:24](https://www.youtube.com/watch?v=Y3GHPpoT08s&t=144s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
