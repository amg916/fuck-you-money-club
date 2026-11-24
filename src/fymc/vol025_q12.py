from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'cargo-liability-insurance-and-claims',
 'question_prompt': 'When cargo is lost or damaged, who is liable, what does insurance actually pay, and '
                    'how do I file a claim?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'Cargo Liability, Insurance and Claims',
 'subtitle': "Carmack Amendment and why it doesn't apply to brokers, carrier limits of liability, cargo "
             'vs. contingent cargo coverage and its gaps, contingent auto pricing, policy evidence '
             'requirements, and step-by-step claim filing',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Freight brokerage practitioners agree on the liability map. Under the Carmack '
                      'Amendment the motor carrier is automatically liable. Brokers sit outside Carmack '
                      "and are governed by contract. A broker's contingent cargo policy only ever matches "
                      'what the carrier already carries, and Freight 360 reports one contingent payout, '
                      '$17,000, in 45 years at Peerless Road Warrior Logistics. The street mechanics are '
                      'documentary: a written claim with a dollar figure and commercial invoice, the '
                      '30-day acknowledgment and 120-day disposition clocks, agent-emailed confirmation '
                      'that excluded commodities are covered, and CIF-plus-10% valuation on international '
                      'cargo. Carrier liability is a floor, and Cargolinked shows a $300,000 container '
                      'returning about $22,000. The disagreements are over three questions: whether '
                      "contingent is 'fake insurance' or a product that has come a long way, how long "
                      'claimants really have to file, and whether shippers must prove carrier negligence.',
 'key_metrics': [{'label': 'Contingent cargo payouts in 45 years',
                  'metric': 'Contingent cargo payouts in 45 years',
                  'value': '1 claim paid, $17,000',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Freight 360 host reports that Peerless Road Warrior Logistics, in business '
                             '45 years, has had exactly one contingent cargo claim pay out.',
                  'source': 'Freight 360 ([qTcDOmwZMjI @ 00:14:27])'},
                 {'label': 'Federal claim processing clock',
                  'metric': 'Federal claim processing clock',
                  'value': '30 days to acknowledge, 120 days to pay, deny, or compromise',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Cassandra Gaines tells brokers to use these regulatory deadlines when motor '
                             'carriers stop responding to cargo claims.',
                  'source': 'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ 00:05:11])'},
                 {'label': 'Carrier payout on a $300,000 ocean container loss',
                  'metric': 'Carrier payout on a $300,000 ocean container loss',
                  'value': 'About $22,000, roughly 7%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Under the usual sea rules carrier liability is capped by weight or package '
                             'rather than value, so a container lost overboard returns a fraction of its '
                             'worth.',
                  'source': 'Cargolinked ([rbmdGEpBKCI @ 00:00:01])'},
                 {'label': 'Theft response window',
                  'metric': 'Theft response window',
                  'value': '24 to 48 hours',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Jared Palmer says that once a theft is known, victims have about 24 to 48 '
                             'hours to act before the freight is probably heading toward the port and '
                             'overseas.',
                  'source': 'CargoRex ([xQYjaYAvyms @ 00:13:43])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every liability conversation starts with the Carmack Amendment, and the '
                              'practitioners line up hard on who it hits. Transportation attorney '
                              "Cassandra Gaines calls it the 'big fat cat' because it sits on top of state "
                              'law and leaves motor carriers almost no wiggle room. The carrier is '
                              'automatically liable, and the claimant only has to show three things: the '
                              'goods were tendered in good condition on an un-notated bill of lading, they '
                              'were delivered damaged or lost, and a commercial invoice backs the value '
                              '[Ig6sI3O1a14 @ 00:11:37]. Brokers sit outside that box. Gaines states '
                              'flatly that Carmack applies only to motor carriers and freight forwarders. '
                              'For a broker, the governing law is the contract. If there is no paper, it '
                              'is the oral agreement to arrange transportation. That is the line to throw '
                              'back at an angry customer who insists the broker owns the claim '
                              '[NyOX8UjzDAo @ 00:00:44]. TLI tells shippers the same thing from the 3PL '
                              'seat. The motor carrier, not the broker, is the liable party, so the play '
                              'is to maximize value with that carrier, file against it, and pass 100% of '
                              'the settlement back to the shipper [fxzUlwnz1mE @ 00:00:52]. Cerasis frames '
                              "the shipper's burden in three matching elements, citing Title 49 U.S. Code "
                              '14706: good-condition tender, damaged or unreasonably late delivery, and '
                              'the dollar amount of the damages [mJw3vbSaJbw @ 00:03:54].',
                              'The second point of agreement is that contingent cargo is not primary '
                              "coverage, whatever a customer's insurance requirement implies. Nate Cross "
                              'of Freight 360 defines it as a secondary policy that depends on the '
                              "carrier's primary cargo insurance already being in place. It is built as a "
                              'safety net for the cases where that primary policy denies a claim or '
                              'refuses to pay, and customers need to be told it is not a primary cargo '
                              'policy [kAT7s21mZIE @ 00:01:33]. In the shorter Freight 360 clip the '
                              'mechanics get blunter. The contingent policy only ever matches what the '
                              'selected motor carrier already has. Take a $200,000 electronics load on a '
                              'carrier with $100,000 in coverage and an electronics exclusion: it gets '
                              "nothing from a broker's $250,000 contingent policy, even though that is "
                              'exactly the scenario shippers think they are buying protection for '
                              '[FtL-2SOSFOU @ 00:00:45]. The hosts name only rare triggers. One is a '
                              'carrier policy lapsing mid-transit without anyone knowing. The other is the '
                              "carrier's insurer folding or simply failing to respond. That is why they "
                              "call contingent 'fake insurance' and a 'feel-good' for shipper management "
                              '[FtL-2SOSFOU @ 00:02:14]. TLI lands in the same place. It describes '
                              'contingent as cover for extreme outlier events, such as a carrier going '
                              'bankrupt in the middle of a freight claim, and notes that not all '
                              'commodities are covered [fxzUlwnz1mE @ 00:01:26].',
                              'Third, every practitioner who touches carrier liability treats it as a '
                              'floor rather than real cover. Trade Risk Guaranty says carrier '
                              "reimbursement generally covers only a fraction of the shipper's loss. Its "
                              'prescription: the only way to ensure reimbursement for full value is to buy '
                              'cargo insurance, which covers loss, damage, or theft between origin and '
                              'final destination even when the carrier is at fault [pbs3U-vmpzM @ '
                              '00:03:18]. Cargolinked puts a number on the gap. A $300,000 container that '
                              'goes overboard returns roughly $22,000 under the usual sea rules, about 7%, '
                              'because carrier liability is capped by weight or package and never by '
                              'value, and carriers still keep defenses like perils of the sea and poor '
                              'packing [rbmdGEpBKCI @ 00:00:01]. The fourth shared baseline is that the '
                              'paper a broker vets does not tell the whole story. Freight 360 points out '
                              'that a certificate of insurance shows policy limits and coverage dates but '
                              'does not always show the exclusions, which creates risk for both broker and '
                              'customer. Freight 360 also says a cheap policy often has a ton of gaps '
                              '[kAT7s21mZIE @ 00:03:00]. Jared Palmer of Epic Insurance Brokers is just as '
                              'blunt. Good insurance costs money, cheap insurance and the best coverage '
                              'are competitors, and a $50,000 premium that should have been $150,000 will '
                              'not respond the way the buyer expects when the loss hits [xQYjaYAvyms @ '
                              '00:17:34].'],
               'table': {'caption': 'Where the practitioners agree on cargo liability and coverage',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Motor carriers are strictly liable under Carmack',
                                   'Claimant proves good-condition tender, damaged or lost delivery, and '
                                   'commercial invoice value',
                                   'Build every claim file around those three proofs, not around fault',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ 00:11:37])'],
                                  ['Carmack does not apply to freight brokers',
                                   'Broker liability runs on the contract, or on an oral agreement to '
                                   'arrange transportation',
                                   'Push back when customers claim the broker is liable under Carmack',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([NyOX8UjzDAo @ 00:00:44])'],
                                  ["Contingent cargo only matches the carrier's existing coverage",
                                   'A $250,000 contingent policy pays nothing on excluded $200,000 '
                                   'electronics with a $100,000 carrier',
                                   'Never sell contingent as a fix for carrier exclusions or low limits',
                                   'Freight 360 ([FtL-2SOSFOU @ 00:00:45])'],
                                  ['Contingent triggers are rare outlier events',
                                   'Policy lapse in transit, insurer folding or not responding, carrier '
                                   'bankrupt mid-claim',
                                   'Expect contingent mostly to fund legal defense, not to pay the shipper',
                                   'TLI ([fxzUlwnz1mE @ 00:01:26])'],
                                  ['Carrier liability is a floor, not insurance',
                                   'Reimbursement generally covers a fraction of loss; cargo insurance '
                                   'pays even on carrier fault',
                                   'Steer high-value shippers toward separate cargo insurance before the '
                                   'loss',
                                   'Trade Risk Guaranty ([pbs3U-vmpzM @ 00:03:18])'],
                                  ['Certificates of insurance hide the exclusions',
                                   'COI lists limits and dates but does not always list excluded '
                                   'commodities',
                                   'Verify commodity coverage separately from the certificate on every '
                                   'risky load',
                                   'Freight 360 ([kAT7s21mZIE @ 00:03:00])'],
                                  ['Cargo claims are not for dabblers',
                                   'Hire attorneys and adjusters who have actually worked cargo claims '
                                   'before',
                                   'Inexperienced handlers get taken advantage of by experienced carrier '
                                   'claims teams',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ '
                                   '00:01:10])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Claim filing is where brokers get taken advantage of. Gaines lays out the '
                              'minimum filing requirements from the federal regulations she tells '
                              'operators to look up at 49 CFR Part 370. First, the claim must be a formal '
                              'written communication to the motor carrier. Notating the bill of lading '
                              'does not count, and neither does phoning in that a couple of pallets are '
                              'missing. Second, it must state a specific dollar amount, normally backed by '
                              'a commercial invoice, because retail value is off the table under Carmack. '
                              'Third, it must name the carrier as the liable party [Ig6sI3O1a14 @ '
                              "00:06:19]. Brent of Anderson Trucking Service walks through the broker's "
                              'side of the workflow. The broker logs the claim and forwards it to the '
                              'claims department. The department requests the original BOL, the original '
                              'paid freight bill, the original or a certified invoice, and any photo, '
                              'video, or other proof. That package goes to the customer and the carrier, '
                              'the carrier submits it to its insurer, and the agent facilitates '
                              'communication from there [id2FXFnynHM @ 00:00:43]. Quote Factory adds the '
                              'hard edges. The claim covers cost incurred, not profit, measured as '
                              'original value minus damaged value. Concealed damage and shortages must be '
                              'reported within five days. Damaged freight should be retained rather than '
                              'refused, and the freight bill gets paid regardless of damage, loss, or '
                              'theft [Ti9MeFBKijM @ 00:05:41].',
                              'On pre-load verification, Freight 360 runs the most detailed playbook. A '
                              'certificate of insurance is usually one or two pages, while the actual '
                              "policy contract is most likely about 60 pages. When a carrier says 'yeah, "
                              "it covers it' on a load of eggs, the broker is just taking their word for "
                              'it [qTcDOmwZMjI @ 00:23:12]. The fix is to pull the certificate from an '
                              'authorized third party such as Highway, AssureAssist, or RMIS rather than '
                              "from the carrier or dispatcher. Then have the carrier's insurance agent "
                              'email the certificate, with the carrier on copy, and confirm in writing '
                              'that the commodity is covered in the event of a claim. This matters most '
                              'for the usual exclusions: eggs, frozen seafood, firearms, electronics, and '
                              'alcohol [qTcDOmwZMjI @ 00:27:38]. Ben of Freight 360 warns that adding '
                              'reefer breakdown can bring 10 to 20 more exclusions, so the carrier can end '
                              'up with less coverage. The suggested workaround is to feed the policy to an '
                              'LLM, have it find and summarize the exclusions, and use that list to ask '
                              'the agent sharper questions [qTcDOmwZMjI @ 00:25:02]. Large brokerages also '
                              'ask carriers on a recorded line whether anything on the vehicle needs '
                              'service, because maintenance fine print can void cargo coverage. That might '
                              'be an oil light the driver did not get to one of five approved mechanics. '
                              'The hosts concede the recorded question still does not hold up anyway '
                              '[FtL-2SOSFOU @ 00:04:23].',
                              'The numbers side runs through valuation and premium math. Logistics '
                              'YouTuber IINO san lays out the international formula. The insured amount is '
                              'usually 110% of the CIF price on the invoice. The premium is that insured '
                              'amount times a rate of roughly 0.3 to 0.5%, with a minimum of about US$30 '
                              'per case and extra war and SRCC charges on some routes. In the worked '
                              'example, a $10,000 machine plus $500 in Thai inland and clearance costs '
                              'plus $1,000 in ocean freight, times 110%, gives a $12,650 insured amount '
                              'and a $37.95 premium at 0.3% [xxk_vmQarVo @ 00:04:12]. Cargolinked agrees '
                              'on CIF plus 10% and warns that insuring for less cuts claims in proportion. '
                              'It also notes that only Institute Cargo Clause A covers theft, '
                              'non-delivery, handling damage, and breakage [rbmdGEpBKCI @ 00:01:07]. '
                              'Domestically, Quote Factory quotes carrier coverage of about $25 per pound '
                              'for new goods and 10 cents per pound for used goods, because nothing proves '
                              'a used item worked when it was loaded [Ti9MeFBKijM @ 00:01:44]. TLI sells '
                              'the gap-fill inside its platform. On a $300,000 dedicated truckload where '
                              'the carrier tops out at $100,000, the shipper buys the extra $200,000 of '
                              'cargo liability in Viewpoint TMS while generating the bill of lading '
                              '[fxzUlwnz1mE @ 00:01:58].'],
               'table': {'caption': 'Hard numbers, clocks, and tools the practitioners actually use',
                         'headers': ['Mechanic',
                                     'Exact Figure or Tool',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Federal claim response clock',
                                   '30 days to acknowledge, 120 days to pay, deny, or compromise',
                                   'Brokers cite it when motor carriers go silent on filed claims',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ 00:05:11])'],
                                  ['Federal court threshold under Carmack',
                                   'Claims over $10,000 can be filed in federal court',
                                   'Gives claimants a federal forum because Carmack is a federal statute',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ 00:10:40])'],
                                  ['All-risk cargo insurance versus carrier liability',
                                   'Claims typically paid within 30 days with no proof of carrier '
                                   'negligence',
                                   'Pitch all-risk to shippers who cannot wait months for carrier '
                                   'settlements',
                                   'Trade Risk Guaranty ([pbs3U-vmpzM @ 00:02:36])'],
                                  ['Covert GPS tracking device cost',
                                   'Was $750 per device; now roughly $15 per device',
                                   'Embed covert trackers in any load worth tracking, with shipper help',
                                   'CargoRex ([xQYjaYAvyms @ 00:26:34])'],
                                  ['Carrier cargo limit selection',
                                   'Many brokers ask for $100,000; pick the limit from the most valuable '
                                   'load',
                                   'Carriers owe the difference when load value exceeds their limit',
                                   'MyFullCoverage ([x_fzUHiNELw @ 00:01:10])'],
                                  ['Certificate-only primary coverage workaround',
                                   "Agent listed the broker's personal pickup truck to produce a primary "
                                   'certificate',
                                   "Meets the shipper's certificate requirement while covering nothing "
                                   'they actually want',
                                   'Freight 360 ([qTcDOmwZMjI @ 00:52:23])'],
                                  ['Placeholder coverage line on a policy',
                                   '$1,000 add-on where binding language excludes everything, versus about '
                                   '$25,000 for real cover',
                                   "Satisfies a customer's certificate demand at minimal cost for a remote "
                                   'brokerage',
                                   'Freight 360 ([qTcDOmwZMjI @ 00:53:43])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the veterans do that new brokers skip',
                           'body': 'Four moves pulled straight from practitioners who have eaten losses, '
                                   'worked the claims desk, or sat as expert witnesses.',
                           'items': ['Script the coverage check: tell the carrier the load is eggs, the '
                                     'limits are fine, and ask them to have their insurance agent email '
                                     'the certificate with them on copy, confirming eggs are covered in '
                                     'the event of a claim. That is part of what the agent is paid for '
                                     '[Freight 360 — qTcDOmwZMjI @ 00:27:57]',
                                     'Never post a high-value load on a load board. Palmer lost Super Bowl '
                                     'TVs in 2006 that way, and tells operators to call relationship '
                                     "carriers whose owners' numbers are in their phone for loads like "
                                     '$400,000 of copper [CargoRex — xQYjaYAvyms @ 00:24:46]',
                                     'If a carrier says a claim is too old, check the bill of lading and '
                                     'the contracts for a specific nine-month limit. Gaines says courts '
                                     'require it in the contract, and if it is not there, the claim can '
                                     'still be submitted [LOGISTICS RISK EXPERT by Cassandra Gaines — '
                                     'Ig6sI3O1a14 @ 00:07:42]',
                                     'Start building the claim file before a claim exists: bill of lading, '
                                     'commercial invoice, packing list, photos, and every email with the '
                                     'carrier. Waiting means people leave and evidence gets lost or '
                                     'tampered with [Cargo Rant — NxIispBOkz8 @ 00:03:18]']},
               'sop_steps': [{'step': 1,
                              'title': 'Verify coverage before the truck is booked',
                              'action': 'Pull the certificate from an authorized third party and get '
                                        'written agent confirmation for commonly excluded or high-value '
                                        'commodities.',
                              'detail': 'Source the certificate through Highway, AssureAssist, or RMIS '
                                        "rather than the carrier or dispatcher, then have the carrier's "
                                        'insurance agent confirm by email that the specific commodity is '
                                        'not excluded [Freight 360 — qTcDOmwZMjI @ 00:27:38]'},
                             {'step': 2,
                              'title': 'Lock down the delivery evidence',
                              'action': 'Have the consignee inspect every item, note damage or shortage on '
                                        'the delivery receipt, photograph it, and keep the damaged '
                                        'freight.',
                              'detail': 'Consignees should not be rushed by drivers, should open crates to '
                                        'check for concealed damage, should never refuse the shipment, and '
                                        'should report concealed damage within five days [Quote Factory — '
                                        'Ti9MeFBKijM @ 00:04:20]'},
                             {'step': 3,
                              'title': 'File a compliant written claim',
                              'action': 'Send a formal written claim to the motor carrier with a specific '
                                        'dollar amount, a commercial invoice, and the carrier named as '
                                        'liable.',
                              'detail': 'A notated bill of lading or a phone call does not meet the filing '
                                        'requirements, and retail value cannot be claimed under Carmack. '
                                        'Then hold the carrier to its 30-day acknowledgment and 120-day '
                                        'disposition deadlines [LOGISTICS RISK EXPERT by Cassandra Gaines '
                                        '— Ig6sI3O1a14 @ 00:06:19]'},
                             {'step': 4,
                              'title': 'Move inside 48 hours on theft',
                              'action': 'Hand CargoNet, law enforcement, and the insurer the driver '
                                        'identity, timeline, and location data immediately.',
                              'detail': "Palmer's instruction is to be a good victim: report properly and "
                                        'timely within about 24 to 48 hours, because calling three months '
                                        'later with no driver, time, or location drops recovery odds to '
                                        'roughly zero [CargoRex — xQYjaYAvyms @ 00:13:43]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ["The sharpest split runs straight through Freight 360's own catalog. In the "
                              'explainer, Nate Cross pitches contingent cargo as a huge recommendation for '
                              "brokers, a secondary safety net that kicks in when a carrier's policy is "
                              'cancelled, runs short on limits, or excludes a commodity like seafood '
                              '[kAT7s21mZIE @ 00:03:16]. On Episode 342, the same channel repeats an '
                              'insurance agent calling it fake insurance, and Nate drops the receipts: '
                              'Peerless Road Warrior Logistics, 45 years in business, one contingent '
                              'payout totaling $17,000 [qTcDOmwZMjI @ 00:14:27]. The newer position is '
                              'blunt: the contingent form only ever matches what the motor carrier already '
                              'holds, so a $200,000 electronics load on a carrier with $100,000 and an '
                              "electronics exclusion gets nothing from the broker's policy. Nate also "
                              'calls the customer demand a feel-good requirement, usually pushed by an '
                              'attorney or upper management. Jared Palmer of Epic Insurance Brokers splits '
                              'the difference. Palmer admits the old mystique was that some forms were not '
                              'worth the paper they were written on, but says the product has come a long '
                              'way and good contingent programs and forms now exist [xQYjaYAvyms @ '
                              '00:16:43]. TLI frames it narrowly as cover for extreme outlier events, such '
                              'as a carrier going bankrupt while a claim is in process [fxzUlwnz1mE @ '
                              '00:01:26].',
                              'On who actually owes the shipper, Cassandra Gaines, a transportation '
                              'attorney, gives brokers a clean script: the Carmack Amendment is a federal '
                              'statute that applies only to motor carriers, so when a customer insists the '
                              'broker is liable, dispute it on the spot [NyOX8UjzDAo @ 00:01:05]. For the '
                              'broker, the contracts between the parties govern, and with no paper at all '
                              'it is an oral agreement to arrange transportation. B3FinalMile shows the '
                              'underwriting side of the same coin: contingent auto is priced on the '
                              'assumption that a sued broker will argue federal preemption and '
                              'non-liability, and once a brokerage leases assets and holds itself out as a '
                              'carrier in a contract, that defense gets much harder and the underwriter '
                              'would have declined or re-priced the account [pRXH47gm66A @ 00:00:57]. '
                              'Freight 360 reports the street reality cutting the other way. The broker is '
                              'not legally responsible to pay out, yet many brokers make the customer '
                              'whole to save the relationship, often paying cash because money almost '
                              'never comes back from the carrier [qTcDOmwZMjI @ 00:21:21]. Some '
                              'brokerages, once they scale, self-insure theft and double-brokering second '
                              'payments out of pocket rather than pay an insurer to cover it [qTcDOmwZMjI '
                              '@ 00:48:44].',
                              'The claims math itself is contested. Gaines teaches strict liability: the '
                              'shipper or broker proves good-condition tender, damaged or lost delivery, '
                              'and a commercial invoice, and the motor carrier must then clear one of five '
                              'defenses, for example with ECM data from the truck [Ig6sI3O1a14 @ '
                              '00:11:37]. Trade Risk Guaranty tells shippers the opposite burden, that '
                              "they must prove the damage was the carrier's fault, a process that can take "
                              'months or years [pbs3U-vmpzM @ 00:01:06]. The nine-month window splits the '
                              'same way. Cerasis tells shippers flatly that they have nine months to file, '
                              'while Gaines calls that a common misconception: courts require the limit to '
                              'appear in the bill of lading or contract, so a claim branded too old should '
                              'be checked against the paper before anyone walks away [Ig6sI3O1a14 @ '
                              '00:07:42]. On valuation, Gaines bars retail value under Carmack and Quote '
                              'Factory says the claim covers cost, not profit, while Kingsley of Cargo '
                              'Rant tells ocean claimants to price arrived sound market value minus '
                              'arrived damaged value and include potential loss of profit [NxIispBOkz8 @ '
                              '00:03:49]. Quote Factory also splits carrier coverage by condition, '
                              'typically twenty-five dollars per pound on new goods against ten cents per '
                              'pound on used goods, because used freight may have been broken before '
                              'pickup.'],
               'table': {'caption': 'Head-to-head practitioner splits on contingent cargo, broker '
                                    'liability, burden of proof, deadlines, valuation and insurance '
                                    'shopping',
                         'headers': ['Flashpoint', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Whether a broker should buy contingent cargo at all',
                                   'Huge recommendation; secondary safety net for cancelled policies, '
                                   'short limits, and commodity exclusions',
                                   'Fake insurance; one $17,000 contingent payout across 45 years at '
                                   'Peerless',
                                   'Freight 360 ([kAT7s21mZIE @ 00:03:16]); Freight 360 ([qTcDOmwZMjI @ '
                                   '00:14:27])'],
                                  ["What today's contingent cargo forms actually respond to",
                                   'Reserved for extreme outlier events like a carrier going bankrupt '
                                   'mid-claim',
                                   'Product has come a long way; good contingent programs and forms now '
                                   'exist',
                                   'TLI ([fxzUlwnz1mE @ 00:01:26]); CargoRex ([xQYjaYAvyms @ 00:16:43])'],
                                  ["Broker exposure when the shipper's cargo is lost or damaged",
                                   'Carmack applies only to motor carriers; contracts or an oral agreement '
                                   'govern brokers',
                                   'Brokers often pay the customer out in cash anyway to keep the account',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([NyOX8UjzDAo @ 00:00:44]); '
                                   'Freight 360 ([qTcDOmwZMjI @ 00:21:21])'],
                                  ['Who carries the burden of proof on a cargo claim',
                                   'Carrier strictly liable; shipper proves tender, damaged delivery, and '
                                   'the commercial invoice',
                                   "Shipper must prove the damage was the carrier's fault, taking months "
                                   'or years',
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ 00:11:37]); '
                                   'Trade Risk Guaranty ([pbs3U-vmpzM @ 00:01:06])'],
                                  ['The nine-month deadline for filing against the motor carrier',
                                   'Shippers have nine months to file but should file as soon as damage '
                                   'occurs',
                                   'Common misconception unless nine months is written into the bill of '
                                   'lading or contract',
                                   'Cerasis , now part of GlobalTranz ([mJw3vbSaJbw @ 00:03:32]); '
                                   'LOGISTICS RISK EXPERT by Cassandra Gaines ([Ig6sI3O1a14 @ 00:07:25])'],
                                  ['How the dollar amount of the claim gets valued',
                                   'Cost incurred by the shipper only, original value minus damaged value, '
                                   'never profit',
                                   'Arrived sound market value minus arrived damaged value, plus potential '
                                   'loss of profit',
                                   'Quote Factory ([Ti9MeFBKijM @ 00:05:41]); Cargo Rant ([NxIispBOkz8 @ '
                                   '00:03:49])'],
                                  ['How to shop and review the brokerage insurance program',
                                   'One or two brokers with carved-out markets, testing the waters about '
                                   'every five years',
                                   'Half-afternoon review every year, using an LLM to surface exclusions '
                                   'before questioning the agent',
                                   'CargoRex ([xQYjaYAvyms @ 00:19:11]); Freight 360 ([qTcDOmwZMjI @ '
                                   '00:42:44])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["Freight 360's stolen-load case is the clearest economics check on record. A "
                              'broker moving a high-value, commonly excluded commodity bought a '
                              'third-party all-risk policy that happened to include theft, the load was '
                              'stolen, and the deductible was $25,000 [qTcDOmwZMjI @ 00:32:11]. The broker '
                              'reached for the contingent policy to offset it, only to hit language '
                              'requiring the broker to use its best endeavors to obtain proof of the '
                              "carrier's cargo coverage, a subjective phrase the insurer can use to argue "
                              'the broker never vetted the carrier because it bought outside cover '
                              "[qTcDOmwZMjI @ 00:33:52]. Nate's correction: contingent covers theft only "
                              "when the carrier's own policy also covers theft. Denials on the carrier "
                              'side are just as technical. Ben from Freight 360 describes a reefer claim '
                              'voided because an oil light came on and the driver did not reach one of '
                              'five approved mechanics, and notes that recorded-line questions about '
                              'vehicle service still do not hold up [FtL-2SOSFOU @ 00:04:07]. Adding '
                              'reefer breakdown can bolt on 10 to 20 more exclusions, and MyFullCoverage '
                              'warns that spoilage claims without temperature records get denied '
                              '[x_fzUHiNELw @ 00:01:10]. The certificate itself hides the trap: a one- or '
                              'two-page COI fronts a policy that probably runs around 60 pages.',
                              'Cosmetic coverage is a recurring failure. When one Freight 360 customer '
                              'demanded primary cargo or auto liability from a broker, the agent offered '
                              "to list the owner's personal pickup truck on a primary policy that met the "
                              'certificate and covered nothing the shipper actually needed [qTcDOmwZMjI @ '
                              '00:52:07]. A fully remote brokerage told to carry workers comp got the same '
                              'treatment: real coverage was quoted around $25,000, so the agent charged '
                              '$1,000 for an add-on whose binding language excludes everything. Palmer '
                              'flags the internal version: a compliance policy you cannot actually execute '
                              'becomes evidence against you, worse than having none [xQYjaYAvyms @ '
                              '00:06:28]. Overbuying limits backfires too. Palmer carried a $50 million '
                              'umbrella at AFN after a truck accident case and dropped it after about a '
                              "year, because plaintiffs' attorneys see big limits as 50 million reasons "
                              'never to settle [xQYjaYAvyms @ 00:22:41]. On the ocean side, Cargolinked '
                              'puts the cap in dollars: a $300,000 container lost overboard pays about '
                              '$22,000, roughly 7 percent, and general average can demand 10 to 50 percent '
                              'of CIF value as security with the final figure taking 2 to 5 years '
                              '[rbmdGEpBKCI @ 00:02:04]. Insuring below CIF plus 10 percent gets claims '
                              'cut in proportion.',
                              'Timing kills claims. Palmer, working alongside CargoNet, says victims who '
                              'call three months later with no driver, no theft date and no location have '
                              'near-zero recovery odds; the window is 24 to 48 hours before freight heads '
                              'toward the port [xQYjaYAvyms @ 00:13:43]. The same practitioner lost Super '
                              'Bowl TVs in 2006 after posting them on load boards, and now points out '
                              'covert trackers that cost $750 then run about $15 [xQYjaYAvyms @ 00:26:34]. '
                              'Palmer also ties premiums to loss frequency and severity, citing truckers '
                              'whose rates jumped 51 percent or went from $13,000 to $28,000 per truck. '
                              'Gaines warns that notating the bill of lading or phoning in missing pallets '
                              'is not a claim; it takes formal written communication with a specified '
                              'dollar amount [Ig6sI3O1a14 @ 00:06:19]. Quote Factory lists consignee '
                              'errors that sink payouts: refusing or discarding damaged freight, missing '
                              'the five-day window for concealed damage, and withholding the freight bill, '
                              'which must be paid regardless [Ti9MeFBKijM @ 00:05:55]. Kingsley adds that '
                              'calling in a recovery agent only after the shipping line rejects the claim '
                              "can jeopardize it beyond repair. Freight 360's downstream cost is "
                              'relationship damage: denied claims lose customers who then sit on unpaid '
                              'invoices.'],
               'table': {'caption': 'Firsthand traps, what went wrong, and the dollar consequence '
                                    'practitioners reported',
                         'headers': ['Trap', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Shipper demands $250K contingent to cover excluded electronics',
                                   '$200,000 electronics load on a carrier with $100,000 and an '
                                   'electronics exclusion',
                                   'Broker contingent policy pays nothing because it only matches carrier '
                                   'coverage',
                                   'Freight 360 ([FtL-2SOSFOU @ 00:00:45])'],
                                  ['Best endeavors clause buried in the contingent policy wording',
                                   'High-value load stolen while covered by a third-party all-risk policy '
                                   'with theft',
                                   '$25,000 deductible stood and contingent was blocked over carrier '
                                   'vetting language',
                                   'Freight 360 ([qTcDOmwZMjI @ 00:32:11])'],
                                  ["Maintenance fine print inside the carrier's cargo policy",
                                   'Oil light ignored and driver nowhere near one of five approved '
                                   'mechanics',
                                   'Claim denied, shipper withholds payment, contingent only funds the '
                                   'legal defense',
                                   'Freight 360 ([FtL-2SOSFOU @ 00:04:07])'],
                                  ['Reefer breakdown add-on bought without discipline on temperature '
                                   'records',
                                   'Spoilage claims filed with no temperature records to back them up',
                                   'Claims denied, and the add-on can carry 10 to 20 extra exclusions',
                                   'MyFullCoverage ([x_fzUHiNELw @ 00:01:10]); Freight 360 ([qTcDOmwZMjI @ '
                                   '00:25:02])'],
                                  ['Treating ocean carrier liability as if it were cargo insurance',
                                   '$300,000 container of goods goes overboard under the usual sea rules',
                                   'Carrier pays about $22,000, roughly 7 percent of the cargo value',
                                   'Cargolinked ([rbmdGEpBKCI @ 00:00:01])'],
                                  ['Reporting a cargo theft months after the load disappeared',
                                   'Victim calls three months later with no driver, date, or location',
                                   'Recovery odds go to near zero once the 24 to 48 hour window closes',
                                   'CargoRex ([xQYjaYAvyms @ 00:13:43])'],
                                  ['Overbuying liability limits after a scare with a truck accident',
                                   '$50 million umbrella carried at AFN following a truck accident case',
                                   'Plaintiffs see 50 million reasons not to settle; policy dropped after '
                                   'a year',
                                   'CargoRex ([xQYjaYAvyms @ 00:22:41])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before the Next High-Value or Excluded-Commodity Load '
                                    'Ships',
                           'body': 'Every item below comes from a loss, denial, or blown recovery the '
                                   'practitioners lived through. Clear all four before tender, not after '
                                   'the claim lands.',
                           'items': ["Get the carrier's insurance agent to confirm in writing, by email "
                                     'with you on copy or in the COI remarks section, that the commodity '
                                     "is not excluded; a carrier's verbal yes is just taking their word "
                                     'for it [Freight 360 — qTcDOmwZMjI @ 00:27:57].',
                                     'Pull certificates from a third party such as Highway, RMIS or '
                                     'AssureAssist acting as certificate holder, never from the carrier or '
                                     'dispatcher directly [Freight 360 — qTcDOmwZMjI @ 00:27:38].',
                                     'Never post a high-value load on a load board; book it with a known '
                                     'relationship carrier and push for a covert tracker now that devices '
                                     'run about $15 instead of $750 [CargoRex — xQYjaYAvyms @ 00:24:46].',
                                     'File every claim as a formal written communication with a specified '
                                     'dollar amount and the commercial invoice; a notated bill of lading '
                                     'or a phone call about missing pallets does not count [LOGISTICS RISK '
                                     'EXPERT by Cassandra Gaines — Ig6sI3O1a14 @ 00:06:19].']}}],
 'pull_quote': "'If you think it's covered, it's probably not. If your customer thinks this insurance "
               "covers it, it probably doesn't.' Freight 360 (qTcDOmwZMjI @ 00:00:36).",
 'diagram_id': 'diag-08',
 'action_checklist': ['Before chasing a special COI, sit down with the customer and ask what they are '
                      'actually trying to accomplish with the insurance requirement, then match a product '
                      'to that use case [Freight 360 — qTcDOmwZMjI @ 00:34:36].',
                      "When a truckload is worth more than the carrier's $100,000 max, buy the additional "
                      'cargo liability on the fly in the TMS while generating the bill of lading so the '
                      'full $300,000 is covered [TLI — fxzUlwnz1mE @ 00:01:58].',
                      'Run the claim desk the way the agent does: log it, collect the original BOL, paid '
                      'freight bill, original invoice or certified copy, plus photo and video proof, then '
                      'route it to customer and carrier so the carrier submits to its insurer [Anderson '
                      'Trucking Service — id2FXFnynHM @ 00:00:29].',
                      'Train consignees to inspect every item, note shortages and damage on the delivery '
                      'receipt, photograph it, keep the damaged freight intact, and report concealed '
                      'damage within five days [Quote Factory — Ti9MeFBKijM @ 00:04:20].',
                      'Hold carriers to the clock: 30 days to acknowledge receipt and 120 days to pay, '
                      'deny or compromise, and use those rules when carriers stop responding [LOGISTICS '
                      'RISK EXPERT by Cassandra Gaines — Ig6sI3O1a14 @ 00:05:11].',
                      'On international moves, insure 110 percent of the CIF price at a premium rate '
                      'around 0.3 to 0.5 percent, and choose Clause A with war and strikes checked for the '
                      'route [【Logistics YouTuber】 IINO san — xxk_vmQarVo @ 00:01:31] [Cargolinked — '
                      'rbmdGEpBKCI @ 00:01:07].'],
 'statutory_citations': [{'title': 'LOGISTICS RISK EXPERT by Cassandra Gaines — Cargo Claims Basics! '
                                   '[00:08:20]',
                          'url': 'https://www.youtube.com/watch?v=Ig6sI3O1a14&t=500s',
                          'relevance': 'Primary practitioner testimony on Carmack federal preemption, '
                                       'carrier strict liability, and who must prove what in a cargo '
                                       'claim.'},
                         {'title': 'LOGISTICS RISK EXPERT by Cassandra Gaines — Did You Know THIS About '
                                   'the Carmack Amendment? [00:00:26]',
                          'url': 'https://www.youtube.com/watch?v=NyOX8UjzDAo&t=26s',
                          'relevance': 'Primary practitioner testimony on Carmack applying only to motor '
                                       'carriers and contracts governing broker liability.'},
                         {'title': 'Freight 360 — What Contingent Cargo Insurance Actually Covers | '
                                   'Episode 342 [00:15:06]',
                          'url': 'https://www.youtube.com/watch?v=qTcDOmwZMjI&t=906s',
                          'relevance': 'Primary practitioner testimony on contingent cargo only matching '
                                       "the motor carrier's existing coverage."},
                         {'title': 'Trade Risk Guaranty — Carrier Limit of Liability: Filing a Claim '
                                   '[00:01:58]',
                          'url': 'https://www.youtube.com/watch?v=pbs3U-vmpzM&t=118s',
                          'relevance': 'Primary practitioner testimony on carrier-liability claims versus '
                                       'all-risk cargo insurance claims.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'FtL-2SOSFOU',
                       'title': 'The Truth About Contingent Cargo Insurance in Trucking | Freight 360 '
                                'Clips',
                       'channel': 'Freight 360',
                       'author': 'Freight 360',
                       'text': "Our policy's never going to kick in for that because the contingent policy "
                               'will only ever match what a motor carrier has.',
                       'tip': "Our policy's never going to kick in for that because the contingent policy "
                              'will only ever match what a motor carrier has.',
                       'timestamp': 45,
                       'timestamp_seconds': 45,
                       'timestamp_label': '[00:00:45]',
                       'url': 'https://www.youtube.com/watch?v=FtL-2SOSFOU&t=45s',
                       'markdown': '[00:00:45](https://www.youtube.com/watch?v=FtL-2SOSFOU&t=45s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ig6sI3O1a14',
                       'title': 'Cargo Claims Basics!',
                       'channel': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
                       'author': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
                       'text': 'The common misconception is people think they have nine months to file a '
                               'cargo claim with the motor carrier.',
                       'tip': 'The common misconception is people think they have nine months to file a '
                              'cargo claim with the motor carrier.',
                       'timestamp': 445,
                       'timestamp_seconds': 445,
                       'timestamp_label': '[00:07:25]',
                       'url': 'https://www.youtube.com/watch?v=Ig6sI3O1a14&t=445s',
                       'markdown': '[00:07:25](https://www.youtube.com/watch?v=Ig6sI3O1a14&t=445s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ig6sI3O1a14',
                       'title': 'Cargo Claims Basics!',
                       'channel': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
                       'author': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
                       'text': 'Motor carriers are automatically liable, and there are only a few things '
                               'that a shipper or the broker representing the shipper have to demonstrate.',
                       'tip': 'Motor carriers are automatically liable, and there are only a few things '
                              'that a shipper or the broker representing the shipper have to demonstrate.',
                       'timestamp': 697,
                       'timestamp_seconds': 697,
                       'timestamp_label': '[00:11:37]',
                       'url': 'https://www.youtube.com/watch?v=Ig6sI3O1a14&t=697s',
                       'markdown': '[00:11:37](https://www.youtube.com/watch?v=Ig6sI3O1a14&t=697s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kAT7s21mZIE',
                       'title': 'What is contingent cargo insurance? Everything you need to know',
                       'channel': 'Freight 360',
                       'author': 'Freight 360',
                       'text': 'When you vet a carrier their certificate of insurance only tells you their '
                               "policy limits and coverage dates but it doesn't always give you the "
                               'exclusions of their policy.',
                       'tip': 'When you vet a carrier their certificate of insurance only tells you their '
                              "policy limits and coverage dates but it doesn't always give you the "
                              'exclusions of their policy.',
                       'timestamp': 180,
                       'timestamp_seconds': 180,
                       'timestamp_label': '[00:03:00]',
                       'url': 'https://www.youtube.com/watch?v=kAT7s21mZIE&t=180s',
                       'markdown': '[00:03:00](https://www.youtube.com/watch?v=kAT7s21mZIE&t=180s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'mJw3vbSaJbw',
                       'title': 'Talking Freight (5) - What is the Carmack Amendment?',
                       'channel': 'Cerasis , now part of GlobalTranz',
                       'author': 'Cerasis , now part of GlobalTranz',
                       'text': "They don't want to pay your freight claim in full, it hurts their bottom "
                               "line, but that doesn't mean you should give up just because they're "
                               'pushing back.',
                       'tip': "They don't want to pay your freight claim in full, it hurts their bottom "
                              "line, but that doesn't mean you should give up just because they're pushing "
                              'back.',
                       'timestamp': 198,
                       'timestamp_seconds': 198,
                       'timestamp_label': '[00:03:18]',
                       'url': 'https://www.youtube.com/watch?v=mJw3vbSaJbw&t=198s',
                       'markdown': '[00:03:18](https://www.youtube.com/watch?v=mJw3vbSaJbw&t=198s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pbs3U-vmpzM',
                       'title': 'Carrier Limit of Liability: Filing a Claim',
                       'channel': 'Trade Risk Guaranty',
                       'author': 'Trade Risk Guaranty',
                       'text': 'If your shipment is covered by all-risk cargo insurance, claims are '
                               'typically paid within 30 days, claim payments cover all losses under the '
                               'policy limit, and you are not required to prove carrier negligence.',
                       'tip': 'If your shipment is covered by all-risk cargo insurance, claims are '
                              'typically paid within 30 days, claim payments cover all losses under the '
                              'policy limit, and you are not required to prove carrier negligence.',
                       'timestamp': 156,
                       'timestamp_seconds': 156,
                       'timestamp_label': '[00:02:36]',
                       'url': 'https://www.youtube.com/watch?v=pbs3U-vmpzM&t=156s',
                       'markdown': '[00:02:36](https://www.youtube.com/watch?v=pbs3U-vmpzM&t=156s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'pRXH47gm66A',
                       'title': 'Why Contingent Auto Pricing Breaks Down When You Act Like a Carrier',
                       'channel': 'B3FinalMile',
                       'author': 'B3FinalMile',
                       'text': "It's going to be much more difficult for any attorney, any insurance "
                               "company to defend you because now you're no longer acting as just a "
                               'freight broker.',
                       'tip': "It's going to be much more difficult for any attorney, any insurance "
                              "company to defend you because now you're no longer acting as just a freight "
                              'broker.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=pRXH47gm66A&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=pRXH47gm66A&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'id2FXFnynHM',
                       'title': 'Cargo Claims Explained [What Your Broker Actually Does]',
                       'channel': 'Anderson Trucking Service',
                       'author': 'Anderson Trucking Service',
                       'text': "At this point, it's the carrier's responsibility to submit the claim to "
                               'their insurance company, and the agent will then facilitate communication '
                               'between the customer and the carrier.',
                       'tip': "At this point, it's the carrier's responsibility to submit the claim to "
                              'their insurance company, and the agent will then facilitate communication '
                              'between the customer and the carrier.',
                       'timestamp': 57,
                       'timestamp_seconds': 57,
                       'timestamp_label': '[00:00:57]',
                       'url': 'https://www.youtube.com/watch?v=id2FXFnynHM&t=57s',
                       'markdown': '[00:00:57](https://www.youtube.com/watch?v=id2FXFnynHM&t=57s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qTcDOmwZMjI',
                       'title': 'What Contingent Cargo Insurance Actually Covers | Episode 342',
                       'channel': 'Freight 360',
                       'author': 'Freight 360',
                       'text': 'We have had one contingent cargo policy claim that has paid out in 45 '
                               'years, and it covered $17,000.',
                       'tip': 'We have had one contingent cargo policy claim that has paid out in 45 '
                              'years, and it covered $17,000.',
                       'timestamp': 867,
                       'timestamp_seconds': 867,
                       'timestamp_label': '[00:14:27]',
                       'url': 'https://www.youtube.com/watch?v=qTcDOmwZMjI&t=867s',
                       'markdown': '[00:14:27](https://www.youtube.com/watch?v=qTcDOmwZMjI&t=867s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qTcDOmwZMjI',
                       'title': 'What Contingent Cargo Insurance Actually Covers | Episode 342',
                       'channel': 'Freight 360',
                       'author': 'Freight 360',
                       'text': 'The verbiage states that the broker must use their best endeavors to '
                               "obtain proof of the carrier's cargo liability coverage.",
                       'tip': 'The verbiage states that the broker must use their best endeavors to obtain '
                              "proof of the carrier's cargo liability coverage.",
                       'timestamp': 2013,
                       'timestamp_seconds': 2013,
                       'timestamp_label': '[00:33:33]',
                       'url': 'https://www.youtube.com/watch?v=qTcDOmwZMjI&t=2013s',
                       'markdown': '[00:33:33](https://www.youtube.com/watch?v=qTcDOmwZMjI&t=2013s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xQYjaYAvyms',
                       'title': 'Cargo Insurance, Evidence and Doing What Your Policy Says | Jared Palmer',
                       'channel': 'CargoRex',
                       'author': 'CargoRex',
                       'text': 'You have about 24 to 48 hours once you know that a theft occurred to jump '
                               'on it and respond.',
                       'tip': 'You have about 24 to 48 hours once you know that a theft occurred to jump '
                              'on it and respond.',
                       'timestamp': 823,
                       'timestamp_seconds': 823,
                       'timestamp_label': '[00:13:43]',
                       'url': 'https://www.youtube.com/watch?v=xQYjaYAvyms&t=823s',
                       'markdown': '[00:13:43](https://www.youtube.com/watch?v=xQYjaYAvyms&t=823s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'x_fzUHiNELw',
                       'title': "Cargo insurance: what it pays, what it doesn't, and your limit",
                       'channel': 'MyFullCoverage',
                       'author': 'MyFullCoverage',
                       'text': 'Spoilage claims without them get denied. Pick your limit from your most '
                               'valuable load, not your average one.',
                       'tip': 'Spoilage claims without them get denied. Pick your limit from your most '
                              'valuable load, not your average one.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=x_fzUHiNELw&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=x_fzUHiNELw&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NxIispBOkz8',
                       'title': 'How to nail your next cargo claim against a shipping line',
                       'channel': 'Cargo Rant',
                       'author': 'Cargo Rant',
                       'text': 'Please do not wait until the shipping line has rejected your claim and you '
                               'have provided all the evidence in your possession before you turn to your '
                               'consultant.',
                       'tip': 'Please do not wait until the shipping line has rejected your claim and you '
                              'have provided all the evidence in your possession before you turn to your '
                              'consultant.',
                       'timestamp': 472,
                       'timestamp_seconds': 472,
                       'timestamp_label': '[00:07:52]',
                       'url': 'https://www.youtube.com/watch?v=NxIispBOkz8&t=472s',
                       'markdown': '[00:07:52](https://www.youtube.com/watch?v=NxIispBOkz8&t=472s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xxk_vmQarVo',
                       'title': 'Explanation of the basic of Cargo Insurance！Insured Amount and how to '
                                'calculate Insurance Premium',
                       'channel': '【Logistics YouTuber】 IINO san',
                       'author': '【Logistics YouTuber】 IINO san',
                       'text': 'The premium is calculated by multiplying the insurance amount by the '
                               'premium rate, about 0.3 to 0.5 percent.',
                       'tip': 'The premium is calculated by multiplying the insurance amount by the '
                              'premium rate, about 0.3 to 0.5 percent.',
                       'timestamp': 110,
                       'timestamp_seconds': 110,
                       'timestamp_label': '[00:01:50]',
                       'url': 'https://www.youtube.com/watch?v=xxk_vmQarVo&t=110s',
                       'markdown': '[00:01:50](https://www.youtube.com/watch?v=xxk_vmQarVo&t=110s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rbmdGEpBKCI',
                       'title': "Cargo Insurance Explained: Why Carrier Liability Isn't Enough",
                       'channel': 'Cargolinked',
                       'author': 'Cargolinked',
                       'text': 'A container of goods worth 300,000 dollars goes overboard, and under the '
                               'usual sea rules the carrier pays about 22,000, roughly 7 percent.',
                       'tip': 'A container of goods worth 300,000 dollars goes overboard, and under the '
                              'usual sea rules the carrier pays about 22,000, roughly 7 percent.',
                       'timestamp': 1,
                       'timestamp_seconds': 1,
                       'timestamp_label': '[00:00:01]',
                       'url': 'https://www.youtube.com/watch?v=rbmdGEpBKCI&t=1s',
                       'markdown': '[00:00:01](https://www.youtube.com/watch?v=rbmdGEpBKCI&t=1s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NyOX8UjzDAo',
                       'title': 'Did You Know THIS About the Carmack Amendment?',
                       'channel': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
                       'author': 'LOGISTICS RISK EXPERT by Cassandra Gaines',
                       'text': 'You can easily dispute that by saying no, the Carmack Amendment is a '
                               'federal statute that only applies to motor carriers.',
                       'tip': 'You can easily dispute that by saying no, the Carmack Amendment is a '
                              'federal statute that only applies to motor carriers.',
                       'timestamp': 65,
                       'timestamp_seconds': 65,
                       'timestamp_label': '[00:01:05]',
                       'url': 'https://www.youtube.com/watch?v=NyOX8UjzDAo&t=65s',
                       'markdown': '[00:01:05](https://www.youtube.com/watch?v=NyOX8UjzDAo&t=65s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fxzUlwnz1mE',
                       'title': "Cargo Liability vs Contingent Cargo Liability in Transportation: What's "
                                'the Difference?',
                       'channel': 'TLI',
                       'author': 'TLI',
                       'text': "Instead of just calling it at the max of the carrier's liability, which "
                               'would be $100,000, you could purchase the additional $200,000 of cargo '
                               'liability in Viewpoint TMS right on the fly.',
                       'tip': "Instead of just calling it at the max of the carrier's liability, which "
                              'would be $100,000, you could purchase the additional $200,000 of cargo '
                              'liability in Viewpoint TMS right on the fly.',
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=fxzUlwnz1mE&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=fxzUlwnz1mE&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ti9MeFBKijM',
                       'title': 'Freight Claims 101: A Comprehensive Step-by-Step Guide',
                       'channel': 'Quote Factory',
                       'author': 'Quote Factory',
                       'text': "Regardless of any damage, loss or theft, it's important to pay the freight "
                               'bill as soon as possible.',
                       'tip': "Regardless of any damage, loss or theft, it's important to pay the freight "
                              'bill as soon as possible.',
                       'timestamp': 370,
                       'timestamp_seconds': 370,
                       'timestamp_label': '[00:06:10]',
                       'url': 'https://www.youtube.com/watch?v=Ti9MeFBKijM&t=370s',
                       'markdown': '[00:06:10](https://www.youtube.com/watch?v=Ti9MeFBKijM&t=370s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
