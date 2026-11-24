from __future__ import annotations

CHAPTER_12 = {'id': 'Q12',
 'chapter_id': 'Q12',
 'chapter_number': 12,
 'question_number': 12,
 'slug': 'atm-hardware-vault-cash-security-high-risk-cash-businesses',
 'question_prompt': 'How do you buy, program, fund, and protect ATMs, and how do cash-heavy, high-risk '
                    'businesses like dispensaries handle payments?',
 'kicker': 'Q12 / THE BIG MONEY PLAYBOOKS',
 'title': 'ATM Hardware, Vault Cash, Security, and High-Risk Cash Businesses',
 'subtitle': 'Genmega vs. Hyosung; buying machines without getting scammed; unboxing and Genmega '
             'programming; vault cash and vaulter services; whether to become a vault casher; theft risk; '
             'avoiding automation-course scams; pros and cons; dispensary ATMs and cashless '
             'point-of-banking; and high-risk merchant account alternatives',
 'layout_template': 'action_worksheet_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'ATM operators and high-risk processing reps converge on a blunt picture: the '
                      'machine is the business, the vault cash is the bottleneck, and cash-heavy verticals '
                      'pay a premium for anyone willing to carry the risk. Genmega gets the loudest '
                      'hardware endorsement, EMV and TLS 1.2 are the non-negotiable floor for any '
                      'purchase, and vaulters earn 70 cents to $1.25 per transaction under written '
                      'agreements that spell out thresholds and response times. Philip Webb reports '
                      'dispensary splits running from 60 percent to the operator down to 50/50 for '
                      'operators who load their own cash, while Anthony of ATM Connect shows real '
                      'locations needing $4,200 to $6,200 a week in vault cash. Disagreement centers on '
                      'whether vaulting for others is a portfolio launchpad or just another job, and '
                      'whether $1,000 per machine is enough cash.',
 'key_metrics': [{'label': 'Vaulter Pay Per Transaction',
                  'metric': 'Vaulter Pay Per Transaction',
                  'value': '70 cents to $1.25 per transaction',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Webb's stated industry standard for paying a vault casher, scaled by "
                             'location volume and transaction count.',
                  'source': 'Philip Webb ([6k0qIHsvs0M @ 00:05:06])'},
                 {'label': 'Weekly Vault Cash Per Busy Location',
                  'metric': 'Weekly Vault Cash Per Busy Location',
                  'value': '$4,200 to $6,200 per week; $16,000 minimum across three locations',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Anthony's own locations running 283 to 350 transactions and dispensing "
                             '$17,000 to $25,000.',
                  'source': 'ATM Connect ([kXEFZM-F90k @ 00:10:13])'},
                 {'label': 'Dispensary Surcharge Split',
                  'metric': 'Dispensary Surcharge Split',
                  'value': '60 percent to the ATM operator down to 50/50',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Splits Webb hears across the industry for dispensary placements where the '
                             'operator supplies all cash.',
                  'source': 'Philip Webb ([ZN0dj7u6nmo @ 00:03:11])'},
                 {'label': 'Durango High-Risk Card Pricing',
                  'metric': 'Durango High-Risk Card Pricing',
                  'value': '1.95% to 4.95% plus 15 to 25 cents; 5 to 10% rolling reserve held 90 to 180 '
                           'days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Listed high-risk merchant account costs, including $15 to $25 per '
                             'chargeback, as of November 2026.',
                  'source': 'Megalith ([lnoavHYKfcI @ 00:01:28])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Hardware is where the ATM operators agree fastest. Chad Otsuji says he has '
                              'owned both Genmega and Hyosung units and calls Genmega the best brand by '
                              'far: his first Genmega has run four years without a jam or error, a '
                              'workhorse since day one. His lone Hyosung, placed an hour and a half from '
                              'home, passed a $20 test withdrawal and was dead by the time he got home, '
                              'then failed again two days later; after three or four round trips he sold '
                              'it and swapped in a Genmega, adding that members of his Facebook group post '
                              'jam after jam on Hyosung hardware and that he received an email warning '
                              'Hyosung machines are prone to jackpotting [6zaxeyp07Zg @ 00:01:41]. '
                              'ATMDepot names the solid models as the Genmega G2500, Hyosung Halo 2, '
                              'Genmega Onyx and Hyosung Force, and flags the Triton 9600, Genmega G1900, '
                              'Hyosung 1800 CE, Tranax and most old bank ATMs as too old, too bulky or not '
                              'upgradeable [ETBd5FI2JHY @ 00:03:14]. The minimum spec is shared: an EMV '
                              'chip reader, updated Windows CE software that can run secure connections, '
                              'and TLS 1.2 encryption, the exact SSL version Rocket ATM dials in on a '
                              'Genmega before it ever talks to a processor [ETBd5FI2JHY @ 00:02:06] '
                              '[gS2sjD2NYOU @ 00:08:06]. A $500 machine, ATMDepot says, is probably just '
                              'an expensive paperweight.',
                              'Every operator who talks about cash agrees the machine is only as good as '
                              'the money inside it and the person loading it. ATMDepot frames the business '
                              'as semi-passive, not hands-off: owners still find locations, build '
                              'relationships with business owners, refill cash and paper, handle repairs, '
                              'and must pass a background check, since a felony or financial crime on the '
                              'record bars someone from legally running an ATM business [Cb9qwLOH7y0 @ '
                              '00:01:38]. Philip Webb says the cheaper and better-serviced alternative to '
                              'an armored car is a vault casher, because armored carriers often show up '
                              'next day or two days later on service calls, while a vaulter treats the '
                              'machine as if it were their own and puts in their own money [zHPWp60QbG4 @ '
                              '00:01:15]. Webb is equally firm that every vault relationship runs on a '
                              "written agreement defining the vaulter's role, the minimum cash threshold "
                              'and the response time for service calls, anywhere from an hour to two days, '
                              'with penalties if the vaulter misses it [6k0qIHsvs0M @ 00:04:20]. Anthony '
                              'of ATM Connect, a Los Angeles operator, backs the same logic from the cash '
                              'side: the national average withdrawal is $80 to $100, so a machine stocked '
                              'with $1,000 runs dry fast and the marketing claim that $1,000 per ATM is '
                              'enough falls apart on simple math [kXEFZM-F90k @ 00:09:58].',
                              'The cash-heavy and high-risk verticals share one root cause: the card '
                              'networks and the banks behind them. Grace of Velocity Merchant Services '
                              'explains that because cannabis remains federally illegal, Visa, Mastercard '
                              'and American Express do not permit its purchase, leaving dispensaries '
                              'cash-dependent, exposed to security risk and starved of impulse buys '
                              '[uBEewd90EL8 @ 00:00:20]. Webb reads that as a home run for ATM operators, '
                              'then immediately adds the catch: ATM operators run under sponsor banks such '
                              'as Pueblo Bank and Trust and MetaBank, which for years refused dispensary '
                              'placements, and armored carriers will not service those sites because they '
                              'are federally regulated, so the loading falls to local operators '
                              '[ZN0dj7u6nmo @ 00:01:26]. On the card side, the processing reps agree that '
                              'high risk means custom quotes, variable pricing and holdbacks. Merchant '
                              'Maverick notes Durango does not disclose pricing and that merchants should '
                              'expect highly variable rates, a long-term contract and early termination '
                              'fees [2E0M95jxJpU @ 00:01:46], while Adaptiv Payments says new and '
                              'high-risk stores often get a reserve, a share of each sale held for a set '
                              'period and then released, and that a clean processing history is the best '
                              'route to lowering or removing it [7jkV0JkaEZA @ 00:01:27]. Being labeled '
                              'high risk changes the price and terms, not whether the money can move.'],
               'table': {'caption': 'Where ATM operators and high-risk processing reps line up on the '
                                    'fundamentals',
                         'headers': ['Consensus Point',
                                     'What Practitioners Agree On',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Genmega as the field reliability benchmark',
                                   'A four-year-old Genmega still runs jam-free while a Hyosung failed '
                                   'repeatedly',
                                   'Pay for proven hardware before chasing a cheaper remote unit',
                                   'Chad Otsuji ATM Business ([6zaxeyp07Zg @ 00:00:40])'],
                                  ['EMV, Windows CE software and TLS 1.2 as the floor',
                                   'Machines lacking chip readers or secure connections may never connect '
                                   'to a processor',
                                   'Reject any used unit missing these three items outright',
                                   'ATMDepot - Make Money with ATM Machines ([ETBd5FI2JHY @ 00:02:06])'],
                                  ['Buy through authorized distributors or processing companies',
                                   'Distributors deliver official warranty, better pricing and decades of '
                                   'setup support',
                                   'Skip overseas sellers and auction-site old bank ATMs entirely',
                                   'ATMDepot - Make Money with ATM Machines ([ETBd5FI2JHY @ 00:01:01])'],
                                  ['Vault relationships must be written into an agreement',
                                   'Define roles, minimum cash threshold, response times and who pays for '
                                   'parts',
                                   'Sign a vaulter agreement before any cash goes into the machine',
                                   'Philip Webb ([6k0qIHsvs0M @ 00:02:00])'],
                                  ['Real vault cash dwarfs what course sellers advertise',
                                   'An $80 to $100 average withdrawal drains a $1,000 load very quickly',
                                   'Plan on roughly $5,000 to $10,000 of cash per machine',
                                   'ATM Connect ([kXEFZM-F90k @ 00:11:05])'],
                                  ['Card networks keep cannabis purchases off credit cards',
                                   'Federal illegality keeps Visa, Mastercard and American Express out of '
                                   'dispensaries',
                                   'Dispensaries need cash ATMs or cashless point-of-banking workarounds',
                                   'Velocity Merchant Services - VMS ([uBEewd90EL8 @ 00:00:40])'],
                                  ['High-risk card accounts carry reserves and custom pricing',
                                   'Banks hold back a share of each sale until history proves clean',
                                   'Build a clean processing record to lower or remove the reserve',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([7jkV0JkaEZA @ '
                                   '00:01:27])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Rocket ATM walks a factory-fresh Genmega G2500 from error code 0030 to '
                              'online. In key management, enter the default secure password of six zeros '
                              'twice, then assign two new six-digit codes (the demo uses all ones and all '
                              'twos), let the 30-second countdown finish without cutting power, and '
                              'confirm the EPP state change to move from maintenance into operation mode '
                              '[gS2sjD2NYOU @ 00:00:42]. Operator functions open with 555555. Under '
                              'customer setup, confirm surcharge mode is enabled, because a disabled '
                              'setting means the machine never charges anyone, set the surcharge owner '
                              'name, and raise the default $1.50 surcharge, which the demo sets to $3 '
                              '[gS2sjD2NYOU @ 00:04:02]. Processor settings go to SSL pass-through for '
                              'internet communication, Standard 3, seven bits even parity, reversal on '
                              'host error enabled, TLS 1.2 with hostname verification, Gen DCC and Visa '
                              'DCC enabled, the Standard 3 options set enable, enable, disable, disable, '
                              'and EMV with all AIDs enabled. For Columbus Data, host setup takes routing '
                              'ID CDSA0, host IP 208.35.209.1 and port 6965 on both lines, with '
                              'configuration set to scheduled [gS2sjD2NYOU @ 00:16:29]. ATM Connect adds '
                              'the physical side: every Genmega ships with the same default vault code, '
                              '123456 then pound, plus universal keys for the chest door and the top '
                              '[ujDLOkqXvfg @ 00:03:46].',
                              'Anthony of ATM Connect puts real numbers on vault cash using three of his '
                              'own locations. The first ran 327 transactions, dispensed $22,000 and '
                              'produced $1,100 in total profit, needing at least $5,500 a week; the second '
                              'ran 283 transactions, dispensed $17,000 for $990 profit and needs $4,200 a '
                              'week; the third ran 350 transactions, dispensed $25,000 for $700 profit and '
                              'needs $6,200 a week, so the three together demand a minimum of $16,000 just '
                              'to stay in service [kXEFZM-F90k @ 00:10:13]. He pegs the average surcharge '
                              'at $3, which means a $40,000 automation package needs 13,333 transactions '
                              'to pay back [kXEFZM-F90k @ 00:13:55]. Webb converts the cash load into '
                              'vaulter terms: the industry standard pays a vaulter between 70 cents and '
                              '$1.25 per transaction depending on volume, and his lesson from a vaulter '
                              'who loaded only $500 twice a week is to require $3,000 per load and '
                              'immediate refills when the machine hits a $200 or $100 threshold '
                              '[6k0qIHsvs0M @ 00:03:50]. He separates level one service, meaning bill '
                              'jams, paper jams and cash-outs covered by the base deal, from repairs like '
                              'dispenser failures, broken keypads, screen replacements, reprogramming and '
                              'software upgrades, which the ATM owner should pay the vaulter extra to '
                              'handle [zHPWp60QbG4 @ 00:04:14].',
                              "For dispensaries, Webb's build is specific. Under the new sponsor-bank "
                              'guidelines the operator loads only their own cash, never mixing it with '
                              'dispensary money, fills out the rules package through the ISO to the '
                              'sponsor bank, and discloses where the dispensaries are, how much cash goes '
                              'in and what commission is paid; he suggests an off-the-record conversation '
                              'with the local bank first to take their temperature [ZN0dj7u6nmo @ '
                              '00:05:35]. The hardware spec is a new machine with a 2K cassette, ideally '
                              'two for 4K because the location needs a lot of money, and possibly a second '
                              "ATM so one failure does not leave the owner blowing up the operator's phone "
                              '[ZN0dj7u6nmo @ 00:07:10]. Velocity Merchant Services describes the cashless '
                              'alternative: point-of-banking runs an ATM-style card withdrawal inside the '
                              'POS, prints a voucher receipt instead of cash, works in increments of 10, '
                              '20, 50 up to 1,000, and settles in change, so a $17.20 sale runs as $20 '
                              'with $2.80 handed back, with the fee paid by merchant or cardholder '
                              "[uBEewd90EL8 @ 00:02:22]. Megalith's Open Receive skips approval entirely, "
                              'taking Bitcoin or USDT and USDC through a receive-only NWC code with no '
                              'reserve, no cut and no chargebacks, installed on their own WooCommerce '
                              'store by a coding agent [lnoavHYKfcI @ 00:02:57].'],
               'table': {'caption': 'Exact settings, cash loads and rates the practitioners actually use',
                         'headers': ['Mechanic',
                                     'Exact Setting or Number',
                                     'Why It Matters',
                                     'Expert Source'],
                         'rows': [['Genmega key management password reset',
                                   'Default 000000 entered twice, then two new six-digit codes',
                                   'Moves the EPP out of maintenance into operation mode',
                                   'Rocket ATM ([gS2sjD2NYOU @ 00:01:12])'],
                                  ['Surcharge mode and surcharge amount',
                                   'Keep surcharge enabled and raise the default $1.50 to $3',
                                   'A disabled surcharge means the machine never charges customers',
                                   'Rocket ATM ([gS2sjD2NYOU @ 00:05:32])'],
                                  ['Columbus Data host configuration values',
                                   'Routing ID CDSA0, IP 208.35.209.1, port 6965, scheduled',
                                   'Points the terminal at the processor over SSL pass-through',
                                   'Rocket ATM ([gS2sjD2NYOU @ 00:16:29])'],
                                  ['Weekly vault cash at busy locations',
                                   '$4,200 to $6,200 per week at 283 to 350 transactions',
                                   'Three locations require at least $16,000 to stay in service',
                                   'ATM Connect ([kXEFZM-F90k @ 00:10:49])'],
                                  ['Vaulter compensation per transaction',
                                   '70 cents to $1.25 per transaction depending on volume',
                                   'The vaulter has to make money or the route is not worth their time',
                                   'Philip Webb ([6k0qIHsvs0M @ 00:05:20])'],
                                  ['Durango high-risk card account pricing',
                                   '1.95% to 4.95%, 15 to 25 cents, $15 to $25 per chargeback',
                                   'Rolling reserve of 5 to 10% held for 90 to 180 days',
                                   'Megalith ([lnoavHYKfcI @ 00:01:28])'],
                                  ['Payment Nerds flat high-risk processing rate',
                                   '2.99% plus 3 cents per transaction with no monthly fees',
                                   'Fully disclosed high-risk pricing is almost unheard of online',
                                   'Merchant Maverick ([2E0M95jxJpU @ 00:04:01])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Bench-Tested Moves From the Operators',
                           'body': 'Small checks that separate a machine that earns from one that becomes '
                                   'a paperweight or a lost location.',
                           'items': ['Before buying any used machine, get the model number, manufacture '
                                     'date and software version, confirm the seller has both passwords and '
                                     'the combo, then run it past your processing company before paying '
                                     '[ATMDepot - Make Money with ATM Machines — ETBd5FI2JHY @ 00:02:28].',
                                     'Check the tip indicator before signing for delivery; metallic silver '
                                     'means it was not tipped, and transport the ATM with its back on the '
                                     'truck bed and the front facing the sky [ATM Connect — ujDLOkqXvfg @ '
                                     '00:00:13].',
                                     'Set the ATM clock to current time because processors look at '
                                     'transaction timing, and turn on Spanish alongside English where '
                                     'customers need it [Rocket ATM — gS2sjD2NYOU @ 00:12:21].',
                                     'Write a lead clause into the vaulter deal so new locations the '
                                     'vaulter hears about become yours, paid as a lead fee, before the '
                                     'vaulter cuts you out with their own machine [Philip Webb — '
                                     '6k0qIHsvs0M @ 00:06:54].']},
               'sop_steps': [{'step': 1,
                              'title': 'Source a compliant machine',
                              'action': 'Buy a Genmega G2500, Onyx, Hyosung Halo 2 or Force from an '
                                        'authorized distributor or processing company.',
                              'detail': 'Reject anything without an EMV reader, secure-connection software '
                                        'or TLS 1.2, and treat refurbished units as acceptable only with '
                                        'at least a 90-day or six-month warranty [ATMDepot - Make Money '
                                        'with ATM Machines — ETBd5FI2JHY @ 00:02:45].'},
                             {'step': 2,
                              'title': 'Unbox, open and power up',
                              'action': 'Inspect the tip indicator, open the vault with 123456 then pound, '
                                        'untwist the shipping wires and power on.',
                              'detail': 'Keep the black rodent caps in every cable hole, swapping the flat '
                                        'cap and the pass-through cap to whichever side the outlet sits on '
                                        '[ATM Connect — ujDLOkqXvfg @ 00:05:06].'},
                             {'step': 3,
                              'title': 'Program surcharge, processor and host',
                              'action': 'Reset key management passwords, enable surcharge, set SSL '
                                        'pass-through with TLS 1.2, enable EMV, then enter terminal '
                                        'number, routing ID and host IP and port.',
                              'detail': 'Finish with a cassette total to test the printer and add cash, '
                                        'where ten bills registering as $200 confirms a $20 denomination, '
                                        'then call the office for the key management information [Rocket '
                                        'ATM — gS2sjD2NYOU @ 00:22:19].'},
                             {'step': 4,
                              'title': 'Fund the vault and lock in service',
                              'action': 'Load cash sized to real weekly dispense, not $1,000, and sign a '
                                        'vaulter agreement if someone else loads it.',
                              'detail': "Size loads from history, with Anthony's locations needing $4,200 "
                                        'to $6,200 a week, and require vaulters to load $3,000 at a time '
                                        'and refill at a $200 or $100 threshold [ATM Connect — kXEFZM-F90k '
                                        '@ 00:10:30] [Philip Webb — 6k0qIHsvs0M @ 00:03:50].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Hardware loyalty splits the operator bench. Chad Otsuji has owned both '
                              'brands and calls Genmega the clear winner: their first Genmega ran four '
                              'years without a single jam or error, while one Hyosung placed an hour and a '
                              'half from home failed the same day it went live, came back broken two days '
                              'after the fix, and forced three or four round trips before Otsuji sold it '
                              '[6zaxeyp07Zg @ 00:00:40]. Otsuji adds that owners in their Facebook group '
                              'report jam after jam on Hyosung units, and that an email landed flagging '
                              'Hyosung machines as prone to jackpotting, where hackers drain the cash with '
                              'no reimbursement [6zaxeyp07Zg @ 00:02:41]. Weigh that against the fact that '
                              "Genmega is the only brand Otsuji's site sells. ATMDepot draws the line by "
                              'model rather than badge: the Genmega G2500, Hyosung Halo 2, Genmega Onyx '
                              'and Hyosung Force sit on its good list, while the Triton 9600, Genmega '
                              'G1900, Hyosung 1800 CE, Tranax and most old bank ATMs land on the avoid '
                              'list as too old, too bulky or not upgradeable [ETBd5FI2JHY @ 00:03:14]. The '
                              'working read: buy the specific model, verify EMV, TLS 1.2 and current '
                              "software, and treat brand-wide verdicts as one operator's route history.",
                              'Vault cashing is where Philip Webb argues both sides on camera. In one '
                              'video Webb tells operators not to become vault cashers at all, because '
                              "filling someone else's machines for 70 cents to $1.25 per transaction while "
                              'carrying the service calls and fronting your own cash just swaps one '
                              'nine-to-five for another [oIqtdUU2Qtg @ 00:00:33]. In the same breath Webb '
                              'admits PDQ did it anyway, and lays out the alternate playbook: take a vault '
                              'route in a new city to buy credibility, build relationships with the store '
                              'owners, prospect new bars, convenience stores and gas stations while you '
                              'are already driving there, and then either cut the owner loose or buy their '
                              "portfolio [oIqtdUU2Qtg @ 00:01:45]. From the owner's side of the deal, Webb "
                              'prefers a vaulter over an armored car because it runs a little cheaper, and '
                              'armored crews usually show up next day or two days after a service call '
                              '[zHPWp60QbG4 @ 00:01:15]. Anthony of ATM Connect pushes the other '
                              'direction: hiring a third-party company to load your ATMs significantly '
                              'decreases profits you are already splitting with the business owner '
                              '[kXEFZM-F90k @ 00:11:22]. Net: outsourced vaulting buys reach and coverage, '
                              'the margin pays for it, so run the per-transaction math first.',
                              'High-risk and cash-heavy merchants get two competing playbooks. For '
                              'dispensaries, Velocity Merchant Services pushes the cashless ATM, or point '
                              'of banking: the card runs like a withdrawal through the POS, a receipt acts '
                              'as the voucher, amounts round to increments such as $20, and the clerk '
                              'hands back change, so on $17.20 the customer selects $20 and gets $2.80 '
                              'back [uBEewd90EL8 @ 00:02:22]. Philip Webb runs the physical-cash play '
                              'instead: sponsor banks now allow dispensary placements if the ATM owner '
                              'loads their own cash and never mixes it with dispensary money, armored '
                              'carriers will not service it, and splits run from 60 to the operator down '
                              'to 50/50 [ZN0dj7u6nmo @ 00:02:19]. For card-not-present high-risk sellers, '
                              "Megalith lays Durango's 1.95 to 4.95 percent plus a 5 to 10 percent rolling "
                              'reserve held 90 to 180 days against Open Receive, a free Bitcoin and '
                              'stablecoin rail with no approval and no chargebacks that runs beside a card '
                              'account rather than replacing it [lnoavHYKfcI @ 00:01:28]. Merchant '
                              "Maverick's top pick, Payment Nerds, publishes a flat 2.99 percent plus 3 "
                              'cents, which the reviewer calls almost unheard of in high-risk processing, '
                              'while Durango keeps pricing undisclosed with long contracts [2E0M95jxJpU @ '
                              '00:04:01].'],
               'table': {'caption': 'Head-to-head operator disputes on hardware, vaulting, dispensary '
                                    'cash, and high-risk rails',
                         'headers': ['Dispute', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Genmega versus Hyosung brand loyalty for route machines',
                                   'Otsuji calls Genmega the only brand worth buying after a four-year '
                                   'jam-free workhorse',
                                   'ATMDepot rates Hyosung Halo 2 and Force as good while flagging Genmega '
                                   'G1900 as bad',
                                   'Chad Otsuji ATM Business ([6zaxeyp07Zg @ 00:00:40]); ATMDepot - Make '
                                   'Money with ATM Machines ([ETBd5FI2JHY @ 00:03:14])'],
                                  ["Whether to vault cash for another operator's machines",
                                   'Webb says 70 cents to $1.25 per transaction just swaps one '
                                   'nine-to-five for another',
                                   'Webb took a vault route anyway to buy credibility and build a new-city '
                                   'portfolio',
                                   'Philip Webb ([oIqtdUU2Qtg @ 00:00:33]); Philip Webb ([oIqtdUU2Qtg @ '
                                   '00:01:45])'],
                                  ['Who loads and services a remote ATM you own',
                                   'Webb picks vaulters as cheaper with faster service than next-day '
                                   'armored car crews',
                                   'Anthony says third-party loaders significantly cut profits already '
                                   'shared with the merchant',
                                   'Philip Webb ([zHPWp60QbG4 @ 00:01:15]); ATM Connect ([kXEFZM-F90k @ '
                                   '00:11:22])'],
                                  ['How dispensaries take card money without card network approval',
                                   'VMS cashless point of banking runs through POS and rounds to $20 '
                                   'increments',
                                   'Webb places a physical ATM loaded with operator cash at 60/40 to 50/50 '
                                   'splits',
                                   'Velocity Merchant Services - VMS ([uBEewd90EL8 @ 00:02:22]); Philip '
                                   'Webb ([ZN0dj7u6nmo @ 00:03:11])'],
                                  ['Card-not-present high-risk sellers needing a payment rail',
                                   'Durango merchant account at 1.95 to 4.95 percent with 5 to 10 percent '
                                   'reserve',
                                   'Open Receive takes Bitcoin and stablecoins with no approval, reserve, '
                                   'or chargebacks at all',
                                   'Megalith ([lnoavHYKfcI @ 00:01:28]); Megalith ([lnoavHYKfcI @ '
                                   '00:02:14])'],
                                  ['How much a single placed ATM really earns monthly',
                                   'ATMDepot pitches low expenses where most of the money collected is '
                                   'pure profit',
                                   'Anthony puts the average ATM at about 200 to 250 dollars a month',
                                   'ATMDepot - Make Money with ATM Machines ([Cb9qwLOH7y0 @ 00:00:45]); '
                                   'ATM Connect ([kXEFZM-F90k @ 00:03:59])'],
                                  ['Where and how much to pay for the machine itself',
                                   'ATMDepot routes buyers to authorized distributors for warranty, '
                                   'pricing, and long-term support',
                                   'Anthony says an ATM should run below $2,500 and you can self-start '
                                   'under that',
                                   'ATMDepot - Make Money with ATM Machines ([ETBd5FI2JHY @ 00:00:45]); '
                                   'ATM Connect ([kXEFZM-F90k @ 00:16:02])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures on the route are empty machines and missed '
                              'service. Philip Webb hired a vaulter who loaded $500 on Monday, ran dry '
                              'Monday night, and did not return until Friday, leaving the ATM down two or '
                              'three days at a stretch; when confronted, the vaulter insisted they loaded '
                              'thousands, but the journals showed $500 in and $500 out [6k0qIHsvs0M @ '
                              "00:03:06]. Webb's fix is written into the agreement: a minimum load of "
                              '$2,000, really $3,000, and an immediate refill when the balance hits the '
                              '$200 or $100 threshold, plus defined response windows from one hour out to '
                              'two days, with penalties when the vaulter misses them [6k0qIHsvs0M @ '
                              "00:03:50]. Distance compounds every failure: Chad Otsuji's Hyosung sat an "
                              'hour and a half away, worked for a day or two after each fix, and burned '
                              'three or four round trips before being sold off and replaced [6zaxeyp07Zg @ '
                              "00:01:41]. Webb's dispensary advice reads like a scar from the same "
                              'problem: place a new unit with a 2K cassette, or two for 4K because the '
                              'location needs a lot of money, and consider a second ATM so one going down '
                              'does not leave the owner blowing up your phone [ZN0dj7u6nmo @ 00:07:10].',
                              'The economics trap is underfunding and overpaying. Anthony of ATM Connect '
                              'pulls three of their own locations: 327 transactions dispensing $22,000 for '
                              '$1,100 profit needs at least $5,500 a week, 283 transactions dispensing '
                              '$17,000 for $990 needs $4,200, and 350 transactions dispensing $25,000 for '
                              '$700 needs $6,200, so the three together need a minimum of $16,000 in vault '
                              'cash [kXEFZM-F90k @ 00:10:13]. That shreds the guru line of filling each '
                              'machine with $1,000, since at an $80 to $100 average withdrawal the box '
                              'empties fast. Anthony also flags a $40,000 ten-machine automation package '
                              'promising 24,000 to 48,000 in year one; at a $3 average surcharge it takes '
                              '13,333 transactions just to recover the buy-in, and one buyer posted 77 '
                              'approved withdrawals in three months, about $144, on a barbershop placement '
                              'with $1 going to the merchant and no contract [kXEFZM-F90k @ 00:14:11]. '
                              'Philip Webb lived the small-scale version: a hotel vault deal on a $4 '
                              'surcharge paying $1.50 per transaction produced 40 to 50 transactions a '
                              'month, about $40 to $60, for two or three trips, and the location could not '
                              'be sold, so it carried no intrinsic value [YgQxm2IWnKw @ 00:02:06].',
                              'Security and banking relationships are the tail risks. WKRN News 2 filmed a '
                              'four-man crew at a Reliant Bank parking lot at 2:15 in the morning pry the '
                              'outer layer with heavy crowbars in 30 seconds, hook tow chains from a '
                              'stolen Ford F-250 to the half-inch safe door, rip the unit off its '
                              'pedestal, and leave with more than $20,000 in under two minutes '
                              '[DzLysrdcerg @ 00:00:45]. On the dispensary side, Philip Webb describes '
                              'years of operators running ATMs under fictitious names like a plant shop or '
                              'an auto body store, paying commissions in cash or by check; when caught, '
                              'the sponsor bank shut it down, the ATM came out, and it went right back in '
                              'under a new name [ZN0dj7u6nmo @ 00:05:06]. The above-board path now means '
                              'reporting locations, cash and commissions to the ISO and possibly the local '
                              'bank, which puts your whole banking relationship at stake. Webb also warns '
                              "that a vaulter servicing a location for years can take the owner's "
                              'referrals and cut you out of the next deal, so lead ownership belongs in '
                              'the agreement [6k0qIHsvs0M @ 00:06:21]. ATMDepot closes the gate: a felony '
                              'or financial crime on your record means you cannot legally run an ATM '
                              'business [Cb9qwLOH7y0 @ 00:02:08].'],
               'table': {'caption': 'Firsthand route failures with the numbers behind each economics check',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['Underloaded vaulter leaving the machine empty for days',
                                   'Vaulter loaded $500 Monday, ran dry that night, returned only Friday',
                                   'Require $2,000 to $3,000 minimum loads and refill at $200 or $100',
                                   'Philip Webb ([6k0qIHsvs0M @ 00:03:06])'],
                                  ["Unreliable machine placed far from the operator's home base",
                                   'Hyosung an hour and a half away broke repeatedly after each repair '
                                   'visit',
                                   'Three or four round trips wasted before selling it for a Genmega',
                                   'Chad Otsuji ATM Business ([6zaxeyp07Zg @ 00:01:41])'],
                                  ['Thin vault-for-hire deal at a low volume hotel location',
                                   '$1.50 per transaction on a $4 surcharge at 40 to 50 monthly '
                                   'transactions',
                                   'About $40 to $60 monthly for two or three trips, location unsellable',
                                   'Philip Webb ([YgQxm2IWnKw @ 00:02:06])'],
                                  ['Buying a done-for-you ATM automation package from a guru',
                                   'Buyer cleared only 77 approved withdrawals in three months, about $144 '
                                   'earned',
                                   'A $40,000 package needs 13,333 transactions at $3 just to break even',
                                   'ATM Connect ([kXEFZM-F90k @ 00:14:11])'],
                                  ['Underestimating vault cash needed per productive location',
                                   'Guru advice said fill each machine with only $1,000 of cash',
                                   'Three real locations needed a combined minimum of $16,000 in weekly '
                                   'cash',
                                   'ATM Connect ([kXEFZM-F90k @ 00:10:13])'],
                                  ['Smash-and-grab theft on an exposed outdoor bank ATM',
                                   'Crowbars opened the shell in 30 seconds, tow chains ripped the safe '
                                   'door',
                                   'Crew took more than $20,000 in under two minutes and escaped',
                                   'WKRN News 2 ([DzLysrdcerg @ 00:00:45])'],
                                  ['Misprogrammed machine settings straight out of the factory box',
                                   'Surcharge mode found disabled and the clock still set back to 1999',
                                   'Disabled surcharge means the ATM never charges any customer a fee',
                                   'Rocket ATM ([gS2sjD2NYOU @ 00:04:02]); Rocket ATM ([gS2sjD2NYOU @ '
                                   '00:11:48])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Lock These Down Before Cash Goes In The Box',
                           'body': 'Every gate below comes from a loss, a fired vaulter, or a dead machine '
                                   'that a named operator lived through on their own route.',
                           'items': ["Put the vaulter's minimum fill level, refill threshold, service "
                                     'response time, and penalties in a signed agreement before they touch '
                                     'your machine [Philip Webb — 6k0qIHsvs0M @ 00:04:05].',
                                     'Add a clause that any location leads the vaulter picks up from your '
                                     'merchant belong to you, with a paid referral if you want, so they '
                                     'cannot cut you out [Philip Webb — 6k0qIHsvs0M @ 00:06:54].',
                                     'Reconcile every vaulted ATM against your settlement deposits daily '
                                     'and monthly, because a vault casher can move your money with a click '
                                     'of a mouse [Philip Webb — zHPWp60QbG4 @ 00:06:39].',
                                     'On any used machine, get the model number, manufacture date, '
                                     'software version, both passwords and the combo, then clear it with '
                                     'your processor before paying [ATMDepot - Make Money with ATM '
                                     'Machines — ETBd5FI2JHY @ 00:02:28].']}}],
 'pull_quote': "We don't get in this business to get a job, we get in this business to leave our job. — "
               'Philip Webb (YgQxm2IWnKw @ 00:02:45)',
 'diagram_id': 'diag-08',
 'action_checklist': ['Program the surcharge before going live: confirm surcharge mode is enabled, enter '
                      'the owner name, set the amount to $3.00, and accept with Enter [Rocket ATM — '
                      'gS2sjD2NYOU @ 00:05:32].',
                      'Set communication to SSL pass-through with TLS 1.2, enable EMV and all AIDs, and '
                      'set the clock to current time because processors look at transaction timing [Rocket '
                      'ATM — gS2sjD2NYOU @ 00:10:29].',
                      'On delivery, check the tip indicator is still silver before signing, transport the '
                      'unit lying on its back, and keep the black hole caps in so rodents cannot chew the '
                      'wires [ATM Connect — ujDLOkqXvfg @ 00:00:00].',
                      'Size vault cash from real dispense history: divide monthly dollars dispensed by '
                      'four weeks to get the minimum weekly cash each location needs [ATM Connect — '
                      'kXEFZM-F90k @ 00:10:30].',
                      'Price any vaulter deal against volume, budgeting the industry standard of 70 cents '
                      'to $1.25 per transaction so it pays both you and the vaulter [Philip Webb — '
                      '6k0qIHsvs0M @ 00:05:06].',
                      'Before chasing a dispensary placement, have an off-the-record conversation with '
                      'your local bank to take their temperature so you do not lose the whole banking '
                      'relationship [Philip Webb — ZN0dj7u6nmo @ 00:06:04].'],
 'statutory_citations': [{'title': 'Philip Webb — ATM machine in dispensaries (Placing ATM in Dispensaries '
                                   'Explained) [00:02:19]',
                          'url': 'https://www.youtube.com/watch?v=ZN0dj7u6nmo&t=139s',
                          'relevance': 'Primary practitioner testimony on sponsor bank rules for '
                                       'dispensary ATMs, operator-only cash loading, splits, and the '
                                       'fictitious-name history.'},
                         {'title': 'Philip Webb — Atm Cash Vault Services -  Top 5 things you should know '
                                   'before you get a vaulter for your ATM [00:02:50]',
                          'url': 'https://www.youtube.com/watch?v=6k0qIHsvs0M&t=170s',
                          'relevance': 'Primary practitioner testimony on vaulter role definitions, '
                                       'minimum load thresholds, response times, pay rates, and '
                                       'relationship theft.'},
                         {'title': 'ATM Connect — Avoid ATM Automation Packages!!! [00:10:13]',
                          'url': 'https://www.youtube.com/watch?v=kXEFZM-F90k&t=613s',
                          'relevance': 'Primary practitioner testimony on real per-location vault cash '
                                       'requirements, average ATM earnings, and automation package '
                                       'losses.'},
                         {'title': 'Chad Otsuji ATM Business — Buy this ATM machine NOW! [00:00:40]',
                          'url': 'https://www.youtube.com/watch?v=6zaxeyp07Zg&t=40s',
                          'relevance': 'Primary practitioner testimony on Genmega versus Hyosung '
                                       'reliability, remote repair trips, and jackpotting exposure.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '2E0M95jxJpU',
                       'title': 'The Best High-Risk Merchant Accounts',
                       'channel': 'Merchant Maverick',
                       'author': 'Merchant Maverick',
                       'text': "Payment Nerds' high-risk processing fees are a flat-rate of 2.99% plus 3 "
                               'cents per transaction, and international cards and manually entered cards '
                               'incur additional fees.',
                       'tip': "Payment Nerds' high-risk processing fees are a flat-rate of 2.99% plus 3 "
                              'cents per transaction, and international cards and manually entered cards '
                              'incur additional fees.',
                       'timestamp': 241,
                       'timestamp_seconds': 241,
                       'timestamp_label': '[00:04:01]',
                       'url': 'https://www.youtube.com/watch?v=2E0M95jxJpU&t=241s',
                       'markdown': '[00:04:01](https://www.youtube.com/watch?v=2E0M95jxJpU&t=241s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lnoavHYKfcI',
                       'title': 'High-Risk Payment Processing: Get Paid Without a Merchant Account',
                       'channel': 'Megalith',
                       'author': 'Megalith',
                       'text': 'Durango Merchant Services lists 1.95 to 4.95% of sale, plus 15 to 25 cents '
                               'per authorization and $15 to $25 per chargeback, and a rolling reserve, '
                               'typically 5 to 10% of your sales, held for 90 to 180 days.',
                       'tip': 'Durango Merchant Services lists 1.95 to 4.95% of sale, plus 15 to 25 cents '
                              'per authorization and $15 to $25 per chargeback, and a rolling reserve, '
                              'typically 5 to 10% of your sales, held for 90 to 180 days.',
                       'timestamp': 88,
                       'timestamp_seconds': 88,
                       'timestamp_label': '[00:01:28]',
                       'url': 'https://www.youtube.com/watch?v=lnoavHYKfcI&t=88s',
                       'markdown': '[00:01:28](https://www.youtube.com/watch?v=lnoavHYKfcI&t=88s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7jkV0JkaEZA',
                       'title': 'Ecommerce Merchant Account: What Banks Check Before They Approve Your '
                                'Store (2026)',
                       'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
                       'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
                       'text': 'New and high-risk stores often get a reserve. The bank holds back a share '
                               'of each sale for a set period, then releases it.',
                       'tip': 'New and high-risk stores often get a reserve. The bank holds back a share '
                              'of each sale for a set period, then releases it.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=7jkV0JkaEZA&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=7jkV0JkaEZA&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6zaxeyp07Zg',
                       'title': 'Buy this ATM machine NOW!',
                       'channel': 'Chad Otsuji ATM Business',
                       'author': 'Chad Otsuji ATM Business',
                       'text': 'I actually just received this email about Hyosung machines being prone to '
                               'jackpotting, and that basically means that hackers are able to go up to '
                               'your machine and basically steal all of your money without you being '
                               'reimbursed for it.',
                       'tip': 'I actually just received this email about Hyosung machines being prone to '
                              'jackpotting, and that basically means that hackers are able to go up to '
                              'your machine and basically steal all of your money without you being '
                              'reimbursed for it.',
                       'timestamp': 161,
                       'timestamp_seconds': 161,
                       'timestamp_label': '[00:02:41]',
                       'url': 'https://www.youtube.com/watch?v=6zaxeyp07Zg&t=161s',
                       'markdown': '[00:02:41](https://www.youtube.com/watch?v=6zaxeyp07Zg&t=161s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gS2sjD2NYOU',
                       'title': 'Genmega Hantle ATM Setup Step By Step Guide - CDS',
                       'channel': 'Rocket ATM',
                       'author': 'Rocket ATM',
                       'text': 'By default it should be enabled, and if you find it disabled that means '
                               'your ATM will never charge any customer for using the ATM machine, which '
                               'sort of defeats the purpose.',
                       'tip': 'By default it should be enabled, and if you find it disabled that means '
                              'your ATM will never charge any customer for using the ATM machine, which '
                              'sort of defeats the purpose.',
                       'timestamp': 242,
                       'timestamp_seconds': 242,
                       'timestamp_label': '[00:04:02]',
                       'url': 'https://www.youtube.com/watch?v=gS2sjD2NYOU&t=242s',
                       'markdown': '[00:04:02](https://www.youtube.com/watch?v=gS2sjD2NYOU&t=242s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ETBd5FI2JHY',
                       'title': 'Where to Buy an ATM Machine (Without Getting Scammed)',
                       'channel': 'ATMDepot - Make Money with ATM Machines',
                       'author': 'ATMDepot - Make Money with ATM Machines',
                       'text': 'If looking at used machines, always ask for the model number, manufactured '
                               'date, software version, and ensure the seller has both passwords and the '
                               'combo, then check with your processing company before making a purchase.',
                       'tip': 'If looking at used machines, always ask for the model number, manufactured '
                              'date, software version, and ensure the seller has both passwords and the '
                              'combo, then check with your processing company before making a purchase.',
                       'timestamp': 148,
                       'timestamp_seconds': 148,
                       'timestamp_label': '[00:02:28]',
                       'url': 'https://www.youtube.com/watch?v=ETBd5FI2JHY&t=148s',
                       'markdown': '[00:02:28](https://www.youtube.com/watch?v=ETBd5FI2JHY&t=148s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ujDLOkqXvfg',
                       'title': 'How to unbox a new ATM (Genmega) | ATM Business',
                       'channel': 'ATM Connect',
                       'author': 'ATM Connect',
                       'text': 'These little black caps are for the holes, and you want to make sure '
                               "they're always placed on the ATM, because rats and little rodents can get "
                               'inside and start chewing on the wires and messing up your ATM.',
                       'tip': 'These little black caps are for the holes, and you want to make sure '
                              "they're always placed on the ATM, because rats and little rodents can get "
                              'inside and start chewing on the wires and messing up your ATM.',
                       'timestamp': 287,
                       'timestamp_seconds': 287,
                       'timestamp_label': '[00:04:47]',
                       'url': 'https://www.youtube.com/watch?v=ujDLOkqXvfg&t=287s',
                       'markdown': '[00:04:47](https://www.youtube.com/watch?v=ujDLOkqXvfg&t=287s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cb9qwLOH7y0',
                       'title': 'ATM Business Pros and Cons 2025 | Is It Still Worth Starting an ATM '
                                'Business Today?',
                       'channel': 'ATMDepot - Make Money with ATM Machines',
                       'author': 'ATMDepot - Make Money with ATM Machines',
                       'text': "You'll need to pass a background check, and if you have a felony or "
                               "financial crime on your record, you won't be able to legally run an ATM "
                               'business.',
                       'tip': "You'll need to pass a background check, and if you have a felony or "
                              "financial crime on your record, you won't be able to legally run an ATM "
                              'business.',
                       'timestamp': 128,
                       'timestamp_seconds': 128,
                       'timestamp_label': '[00:02:08]',
                       'url': 'https://www.youtube.com/watch?v=Cb9qwLOH7y0&t=128s',
                       'markdown': '[00:02:08](https://www.youtube.com/watch?v=Cb9qwLOH7y0&t=128s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uBEewd90EL8',
                       'title': 'Cannabis dispensary owners guide to Cashless ATMs and Point of Banking',
                       'channel': 'Velocity Merchant Services - VMS',
                       'author': 'Velocity Merchant Services - VMS',
                       'text': 'They are usually programmed to only dispense in increments, 10, 20, 50 all '
                               'the way up to 1,000, so if the price is say $17.20 the customer would '
                               'select $20 and then the merchant would give the customer $2.80 in change.',
                       'tip': 'They are usually programmed to only dispense in increments, 10, 20, 50 all '
                              'the way up to 1,000, so if the price is say $17.20 the customer would '
                              'select $20 and then the merchant would give the customer $2.80 in change.',
                       'timestamp': 142,
                       'timestamp_seconds': 142,
                       'timestamp_label': '[00:02:22]',
                       'url': 'https://www.youtube.com/watch?v=uBEewd90EL8&t=142s',
                       'markdown': '[00:02:22](https://www.youtube.com/watch?v=uBEewd90EL8&t=142s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZN0dj7u6nmo',
                       'title': 'ATM machine in dispensaries (Placing ATM in Dispensaries Explained)',
                       'channel': 'Philip Webb',
                       'author': 'Philip Webb',
                       'text': "If you file certain guidelines we're okay with you placing an ATM in a "
                               'dispensary, as long as you, the ATM owner, put your cash in there and '
                               "don't mix it with the dispensary money.",
                       'tip': "If you file certain guidelines we're okay with you placing an ATM in a "
                              "dispensary, as long as you, the ATM owner, put your cash in there and don't "
                              'mix it with the dispensary money.',
                       'timestamp': 139,
                       'timestamp_seconds': 139,
                       'timestamp_label': '[00:02:19]',
                       'url': 'https://www.youtube.com/watch?v=ZN0dj7u6nmo&t=139s',
                       'markdown': '[00:02:19](https://www.youtube.com/watch?v=ZN0dj7u6nmo&t=139s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zHPWp60QbG4',
                       'title': 'Top 5 ATM Vault Cash questions answered in detail (ATM Business 2021)',
                       'channel': 'Philip Webb',
                       'author': 'Philip Webb',
                       'text': 'They have to have a minimum threshold; we had a vaulter and they just put '
                               "in 500 at a time, and when that money ran out they didn't come in until "
                               'they were in the neighborhood again.',
                       'tip': 'They have to have a minimum threshold; we had a vaulter and they just put '
                              "in 500 at a time, and when that money ran out they didn't come in until "
                              'they were in the neighborhood again.',
                       'timestamp': 329,
                       'timestamp_seconds': 329,
                       'timestamp_label': '[00:05:29]',
                       'url': 'https://www.youtube.com/watch?v=zHPWp60QbG4&t=329s',
                       'markdown': '[00:05:29](https://www.youtube.com/watch?v=zHPWp60QbG4&t=329s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6k0qIHsvs0M',
                       'title': 'Atm Cash Vault Services -  Top 5 things you should know before you get a '
                                'vaulter for your ATM',
                       'channel': 'Philip Webb',
                       'author': 'Philip Webb',
                       'text': 'Standard right now in the industry is somewhere between 70 cents and 1.25, '
                               'and it all depends on volume and how many transactions that location is '
                               'going to do in a given amount of time.',
                       'tip': 'Standard right now in the industry is somewhere between 70 cents and 1.25, '
                              'and it all depends on volume and how many transactions that location is '
                              'going to do in a given amount of time.',
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=6k0qIHsvs0M&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=6k0qIHsvs0M&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oIqtdUU2Qtg',
                       'title': "Why You Shouldn't Become A Vault Casher, But We DID! - ATM Business 2020",
                       'channel': 'Philip Webb',
                       'author': 'Philip Webb',
                       'text': "All we're doing is we're replacing one nine to five job with another, and "
                               "somebody's paying you anywhere from 70 to 1.25 per transaction to fill "
                               'their ATMs.',
                       'tip': "All we're doing is we're replacing one nine to five job with another, and "
                              "somebody's paying you anywhere from 70 to 1.25 per transaction to fill "
                              'their ATMs.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=oIqtdUU2Qtg&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=oIqtdUU2Qtg&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YgQxm2IWnKw',
                       'title': 'Should you Become A Vault Casher? - ATM Business 2020',
                       'channel': 'Philip Webb',
                       'author': 'Philip Webb',
                       'text': "I couldn't sell the location, so I had no intrinsic value at all; all we "
                               'were doing is basically we were a hired gun to put our money in and to '
                               'service that ATM.',
                       'tip': "I couldn't sell the location, so I had no intrinsic value at all; all we "
                              'were doing is basically we were a hired gun to put our money in and to '
                              'service that ATM.',
                       'timestamp': 218,
                       'timestamp_seconds': 218,
                       'timestamp_label': '[00:03:38]',
                       'url': 'https://www.youtube.com/watch?v=YgQxm2IWnKw&t=218s',
                       'markdown': '[00:03:38](https://www.youtube.com/watch?v=YgQxm2IWnKw&t=218s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DzLysrdcerg',
                       'title': 'Suspects open ATM in 30 seconds',
                       'channel': 'WKRN News 2',
                       'author': 'WKRN News 2',
                       'text': 'The driver floors it, launching the half inch safe door across the parking '
                               'lot, and in under 2 minutes this crew steals more than $20,000 and they '
                               'get away scot-free.',
                       'tip': 'The driver floors it, launching the half inch safe door across the parking '
                              'lot, and in under 2 minutes this crew steals more than $20,000 and they get '
                              'away scot-free.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=DzLysrdcerg&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=DzLysrdcerg&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kXEFZM-F90k',
                       'title': 'Avoid ATM Automation Packages!!!',
                       'channel': 'ATM Connect',
                       'author': 'ATM Connect',
                       'text': 'So that means with these three locations I need a minimum of sixteen '
                               'thousand dollars for them to be in service and to earn that amount of '
                               'profit.',
                       'tip': 'So that means with these three locations I need a minimum of sixteen '
                              'thousand dollars for them to be in service and to earn that amount of '
                              'profit.',
                       'timestamp': 649,
                       'timestamp_seconds': 649,
                       'timestamp_label': '[00:10:49]',
                       'url': 'https://www.youtube.com/watch?v=kXEFZM-F90k&t=649s',
                       'markdown': '[00:10:49](https://www.youtube.com/watch?v=kXEFZM-F90k&t=649s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kXEFZM-F90k',
                       'title': 'Avoid ATM Automation Packages!!!',
                       'channel': 'ATM Connect',
                       'author': 'ATM Connect',
                       'text': 'They overestimate the profits and underestimate the difficulties; the '
                               'average ATM makes about 200 to 250 dollars a month.',
                       'tip': 'They overestimate the profits and underestimate the difficulties; the '
                              'average ATM makes about 200 to 250 dollars a month.',
                       'timestamp': 239,
                       'timestamp_seconds': 239,
                       'timestamp_label': '[00:03:59]',
                       'url': 'https://www.youtube.com/watch?v=kXEFZM-F90k&t=239s',
                       'markdown': '[00:03:59](https://www.youtube.com/watch?v=kXEFZM-F90k&t=239s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q12.'}]}
