from __future__ import annotations

CHAPTER_8 = {'id': 'Q8',
 'chapter_id': 'Q8',
 'chapter_number': 8,
 'question_number': 8,
 'slug': 'ticketmaster-delivery-transfers-and-refunds',
 'question_prompt': 'How do you choose a resale platform and deliver, transfer and troubleshoot '
                    'Ticketmaster tickets, including refunds?',
 'kicker': 'Q8 / THE BIG MONEY PLAYBOOKS',
 'title': 'Ticketmaster Delivery, Transfers and Refunds',
 'subtitle': 'Ticketmaster vs. StubHub vs. SeatGeek, legitimacy checks for resale sites, SafeTix rotating '
             'barcodes, Apple Wallet adds and transfers, barcode fixes, phone-to-phone transfers, and '
             'refund policies for cancelled and postponed events',
 'layout_template': 'legal_compliance_callout',
 'reading_time_minutes': 15,
 'executive_summary': 'Ticketmaster is the custody layer: Nexustech, Patchwave and thumbsuprun all treat '
                      'the account, not Apple Wallet, as the real ticket, and even StubHub-bought BTS '
                      'seats arrive as Ticketmaster transfers. The street flow is My Events, Transfer, '
                      'select seats, OTP check, recipient email or phone, then the buyer clicks accept and '
                      "the sender's barcodes die. Numbers that matter: SafeTix codes rotate every 15 "
                      'seconds, barcodes surface 24 to 48 hours out, transfer deadlines typically sit at '
                      "72 hours, and Ticketmaster's refund plan offered up to 150% concert cash, 60-day "
                      'postponement triggers and 30-day processing. Practitioners split on whether Apple '
                      'Wallet sharing can move a ticket at all, on website versus app for bulk sends, and '
                      'on refunds: direct Ticketmaster buyers got cash for postponed shows while StubHub '
                      'offered vouchers and Vivid Seats called sales final.',
 'key_metrics': [{'label': 'SafeTix Barcode Rotation Interval',
                  'metric': 'SafeTix Barcode Rotation Interval',
                  'value': 'Dynamic code changes every 15 seconds',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Security measure rolled out after cloning and fraud complaints, including '
                             'the Bad Bunny entry failure where buyers got a full refund plus 20% '
                             'compensation.',
                  'source': 'Paso a paso ([EwQdnuSrWAo @ 00:00:18])'},
                 {'label': 'Barcode Release Window',
                  'metric': 'Barcode Release Window',
                  'value': '24 to 48 hours before the event',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Barcodes for some events are withheld until close to the date to prevent '
                             'ticket fraud; My Events shows a notice when this applies.',
                  'source': 'Helpful Solutions ([hNlTOy1daSA @ 00:00:19])'},
                 {'label': 'Typical Transfer Deadline',
                  'metric': 'Typical Transfer Deadline',
                  'value': '72 hours before the event starts',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Many events now set transfer cutoffs, and dynamically priced tickets may '
                             'carry transfer restrictions aimed at scalping.',
                  'source': 'Gadget Tune ([8yXxF_U1uek @ 00:01:13])'},
                 {'label': 'Concert Cash Credit Ceiling',
                  'metric': 'Concert Cash Credit Ceiling',
                  'value': 'Up to 150% of the ticket price',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Offered as an alternative to a cash refund on cancelled events under '
                             "Ticketmaster's revised refund program; unclear whether fees were included.",
                  'source': 'thumbsuprun ([s9mNdqH694I @ 00:03:09])'}],
 'sections': [{'heading': '1. The Practitioner Consensus',
               'paragraphs': ['The first rule every transfer operator repeats is that the ticket lives '
                              'inside Ticketmaster, not on the phone. Nexustech states it flatly: you '
                              'cannot transfer a ticket from Apple Wallet directly, because Wallet only '
                              'stores a copy and the real ticket always sits in the Ticketmaster account, '
                              'so any send happens inside the app or on ticketmaster.com [lBLVmAx5wkQ @ '
                              '00:00:21]. Patchwave Tutorials gives the same order to anyone trying to '
                              'load a pass just to pass it along: bypass Apple Wallet entirely and hit the '
                              'built-in transfer button to move the ticket to an email address or '
                              'Ticketmaster account [Wqb02oxLDJ0 @ 00:01:17]. Rez at thumbsuprun applies '
                              "the rule to secondary-market inventory. A viewer's BTS seats were bought on "
                              'StubHub, yet the tickets themselves were transferred out of Ticketmaster '
                              'and housed there, so that is where the search has to start [MP1aH4hgG70 @ '
                              '00:00:39]. The operational read is simple: the marketplace that took the '
                              'money is not the system that controls the barcode. Whoever holds the '
                              'Ticketmaster account holds the seat, and every delivery, re-send, wallet '
                              'load and gate scan runs through that login. Brokers who treat a wallet '
                              'pass, a screenshot or a forwarded email as the asset are working with a '
                              'copy that the scanner may never honor.',
                              'On the send itself, the practitioners walk the same rails. Sarah at The '
                              'Savvy Professor lays out the ground rules: sender and receiver both need a '
                              'Ticketmaster account, a receiver without one must create it, there is no '
                              'limit on how many tickets can be transferred, and once a transfer succeeds '
                              'the sender can no longer use those tickets, though a received ticket can '
                              'still be retransferred [kC2NXuA1XV4 @ 00:00:21]. Fixed Formulas runs the '
                              'identical path in 2026: My Account, upcoming events under My Tickets, open '
                              'the ticket, hit Transfer, choose which ticket if several are held for the '
                              'same event, then enter first name, last name, email and an optional message '
                              'before confirming; the recipient clicks Accept Ticket from an email or '
                              "phone link and the ticket lands in the recipient's account [f7BuIdB0-6I @ "
                              '00:02:17]. Rez at thumbsuprun spells out what happens on the back end once '
                              "the buyer says yes. The sender's status flips from pending to complete, the "
                              "tickets disappear from the sender's account, and the old barcodes are "
                              'invalid even if they were saved to a wallet or issued as hard stock; only '
                              'the newly transferred barcodes are valid [MP1aH4hgG70 @ 00:04:01]. That '
                              'acceptance click is the real moment of delivery, and every source treats it '
                              'as the point where custody changes hands for good.',
                              'The refund side has its own consensus, and it centers on who actually sold '
                              'the seat. Rez at thumbsuprun ranks the fan guarantee or refund policy as '
                              'the number one thing any resale site must show: resale platforms generally '
                              'own none of the inventory, they earn on service charges, and a real '
                              'guarantee either finds replacement tickets to get the buyer in or pays a '
                              '100% money-back refund; if no fan guarantee, buyer guarantee or refund '
                              'policy can be found, Rez says to stay away completely [sIgspwKXj_0 @ '
                              '00:02:12]. WCPO 9 shows why the seller of record matters when shows move. '
                              'Nikki Agee paid $648 for four Elton John tickets through Vivid Seats, and '
                              'any refund had to come back through the person who transferred the tickets, '
                              'while Kelly and Tom Rally were offered only StubHub vouchers on $800 of Foo '
                              'Fighters seats; meanwhile Ticketmaster, after outrage from fans and '
                              'lawmakers, was refunding both cancelled and postponed shows bought directly '
                              '[VBj60jqiycw @ 00:01:24]. GigaBits, after two weeks of side-by-side '
                              'testing, still calls Ticketmaster strict and slow on refunds [7KU-5HUqmzA @ '
                              '00:02:58] but essential for official releases and guaranteed legitimacy '
                              '[7KU-5HUqmzA @ 00:03:39]. WCPO frames direct Ticketmaster purchase as the '
                              'good-news side of every postponement story.'],
               'table': {'caption': 'Where Ticketmaster delivery and refund practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Why It Matters To Operators',
                                     'Expert Source'],
                         'rows': [['Ticketmaster account holds the real ticket, not the wallet',
                                   'Apple Wallet only stores a copy; transfers must happen inside the '
                                   'Ticketmaster app or website',
                                   'Never treat a wallet pass or screenshot as transferable inventory',
                                   'Nexustech ([lBLVmAx5wkQ @ 00:00:21])'],
                                  ['Resale marketplace purchases still settle through Ticketmaster '
                                   'transfers',
                                   'StubHub-bought BTS tickets were transferred out of and housed inside '
                                   'Ticketmaster',
                                   'Start every delivery search in the Ticketmaster account, not the '
                                   'marketplace',
                                   'thumbsuprun ([MP1aH4hgG70 @ 00:00:39])'],
                                  ['Both parties need Ticketmaster accounts to complete any transfer',
                                   'Receiver without an account must create one; no limit on ticket count',
                                   'Tell buyers to set up an account before the send goes out',
                                   'The Savvy Professor ([kC2NXuA1XV4 @ 00:00:21])'],
                                  ["Recipient acceptance kills the sender's barcodes for good",
                                   'Once accepted, old wallet and hard stock barcodes are invalid; only '
                                   'new ones work',
                                   'Seller cannot reuse the seats after the recipient accepts the transfer',
                                   'thumbsuprun ([MP1aH4hgG70 @ 00:04:01])'],
                                  ['Dynamic barcodes defeat screenshots and copies at the entry gate',
                                   'Wallet tickets refresh every few seconds; entry scanners reject '
                                   'screenshots or copies',
                                   'Only a live rotating barcode tied to the account gets a buyer inside',
                                   'Nexustech ([lBLVmAx5wkQ @ 00:02:13])'],
                                  ['Fan guarantee is the number one resale site requirement',
                                   'Guarantee means replacement tickets or a 100% money-back refund if '
                                   'entry fails',
                                   'Without a posted guarantee, the advice is to not buy at all',
                                   'thumbsuprun ([sIgspwKXj_0 @ 00:01:32])'],
                                  ['Direct Ticketmaster buyers fared better on postponed show refunds',
                                   'Ticketmaster refunded cancelled and postponed shows; Vivid Seats and '
                                   'StubHub withheld cash on postponements',
                                   'Seller of record decides whether postponed-show cash ever comes back',
                                   'WCPO 9 ([VBj60jqiycw @ 00:01:24])']]}},
              {'heading': '2. Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The send flow has a few levers that matter to anyone moving volume. '
                              'Poolarity works from the Ticketmaster website on a phone instead of the app '
                              'because the site allows multi-select, letting several tickets go to one '
                              'email in a single pass rather than one by one; the same demo confirms a '
                              'pair can be split, sending one seat to a buyer and routing the other '
                              'separately [IENQeieAOCo @ 00:01:29]. Expect a security gate before anything '
                              'moves. Fixed Formulas shows Ticketmaster firing an OTP to the registered '
                              'email address and phone number, which must be entered and confirmed before '
                              'the recipient screen appears [f7BuIdB0-6I @ 00:01:09]. Gadget Tune lists '
                              "the recipient's email address or phone number as the target and warns that "
                              'a simple typo sends the tickets to the wrong person, so the address gets '
                              'verified and the recipient gets a heads-up to watch for the notification '
                              "and accept promptly [8yXxF_U1uek @ 00:02:06]. After the send, Poolarity's "
                              'screen states the transfer can be cancelled at any time as long as the '
                              'recipient has not accepted, and the ticket list keeps a permanent history '
                              'with a pending or accepted status, so nothing sits in limbo [IENQeieAOCo @ '
                              "00:02:42]. That pending window is the seller's only undo button.",
                              'Rez at thumbsuprun adds the eligibility screen and the confirmation '
                              'workaround. Not every event shows the transfer feature: either the delivery '
                              'delay has not been lifted so tickets cannot be accessed yet, or the ticket '
                              'type is ineligible, with hard stock and will call tickets generally blocked '
                              'and will call usually picked up at the event itself [MP1aH4hgG70 @ '
                              '00:01:35]. Sarah at The Savvy Professor gives the visual tell: if the '
                              'transfer button is gray, the tickets cannot be moved [kC2NXuA1XV4 @ '
                              '00:01:21]. When the button is live, the phone flow lets a seller pick a '
                              'saved contact to save taps, or enter the name, email address or phone '
                              'number manually, and then the transfer simply completes with no '
                              'confirmation step. The catch, per Rez, is that a computer transfer triggers '
                              'an email confirmation showing the address typed in, while a mobile transfer '
                              'sends none and the confirmation page shows only first and last name '
                              "[MP1aH4hgG70 @ 00:04:15]. The fix: type the recipient's full name in the "
                              'First Name line, paste the email address into the Last Name line, paste it '
                              'again in the email or mobile field, and hit transfer; the confirmation '
                              'screen then displays the address in the last-name slot, which confirmed the '
                              "intended inbox in Rez's own demo [MP1aH4hgG70 @ 00:04:41].",
                              "The refund math comes from Rez's breakdown of how Ticketmaster rewrote its "
                              'policy as events collapsed. The old policy refunded cancelled, postponed or '
                              'rescheduled events within seven to ten business days, with minimal '
                              'exceptions for US Open and MLB tickets [s9mNdqH694I @ 00:00:38]. In late '
                              'March or early April Ticketmaster quietly narrowed refunds to cancelled '
                              'events only, then on April 17 launched a program that kept cash refunds for '
                              'cancellations but added the option of up to 150% of the ticket price as '
                              'concert cash credit, with Rez noting it was unclear whether fees were '
                              'included [s9mNdqH694I @ 00:03:09]. Postponed events with a rescheduled date '
                              'could request a refund in a May 1 to May 30 selection window, and the April '
                              '24 update added any postponed event without a new date set within 60 days '
                              'of postponement [s9mNdqH694I @ 00:05:16]. Refunds take 30 days to process, '
                              'Rez reads the design as cash-flow management through batching, and doing '
                              'nothing simply keeps the tickets live. Buying into an event that was '
                              "already postponed generally does not qualify. Rez's own take is that the "
                              'credit can be worth it as near-free future tickets if the cash can stay '
                              'tied up for a year or two. Resale buyers hit a different wall: Kelly and '
                              'Tom Rally were offered only StubHub vouchers for $800 of Foo Fighters '
                              'tickets [VBj60jqiycw @ 00:01:08].'],
               'table': {'caption': 'Delivery, wallet and refund numbers practitioners actually quote',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Setting',
                                     'How Practitioners Use It',
                                     'Expert Source'],
                         'rows': [['SafeTix rotating barcode built against cloning and fraud',
                                   'Dynamic code changes every 15 seconds on the digital ticket',
                                   'Show it original size, moving, on an undamaged charged screen without '
                                   'anti-spy protector',
                                   'Paso a paso ([EwQdnuSrWAo @ 00:00:18])'],
                                  ['Barcode release timing for events withheld against fraud',
                                   'Barcodes typically appear 24 to 48 hours before the event',
                                   'Check My Events for a notice that the barcode unlocks closer to date',
                                   'Helpful Solutions ([hNlTOy1daSA @ 00:00:19])'],
                                  ['Event-level transfer deadline set by many current events',
                                   'Cutoff typically lands 72 hours before the event starts',
                                   'If the deadline passed, contact Ticketmaster customer service for '
                                   'emergency transfer assistance',
                                   'Gadget Tune ([8yXxF_U1uek @ 00:01:13])'],
                                  ['Apple Wallet pass that refuses to load from the app',
                                   'Log in through Safari instead of the app, then tap Add to Apple Wallet',
                                   'Treat Safari login as the most effective first fix before updating '
                                   'software',
                                   'Patchwave Tutorials ([Wqb02oxLDJ0 @ 00:00:00])'],
                                  ['Wallet error triggers that block adding tickets to Apple Wallet',
                                   'iOS older than 16.4, will call, print at home, phone-rep sales, VIP or '
                                   'premium tickets',
                                   'Update the app or iOS, otherwise enter with the rotating barcode in '
                                   'the Ticketmaster app',
                                   'The Savvy Professor ([zH4ITvC9voc @ 00:01:43])'],
                                  ['Concert cash credit offered instead of a cash refund',
                                   'Up to 150% of the price paid for the tickets',
                                   'Take the credit when cash can stay tied up for future ticket buying',
                                   'thumbsuprun ([s9mNdqH694I @ 00:03:09])'],
                                  ['Postponed event refund trigger under the updated Ticketmaster plan',
                                   'No rescheduled date within 60 days of postponement qualifies for '
                                   'refund',
                                   'Make the refund or credit selection inside the Ticketmaster account '
                                   'once the window opens',
                                   'thumbsuprun ([s9mNdqH694I @ 00:05:16])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Delivery Desk Pro-Tips',
                           'body': 'Small moves practitioners use to send faster, confirm delivery and '
                                   'keep postponed inventory working.',
                           'items': ['Run bulk sends from the Ticketmaster website on your phone, not the '
                                     'app: the site multi-selects several tickets to one email instead of '
                                     'sending them one at a time [Poolarity - Life Hacks — IENQeieAOCo @ '
                                     '00:00:00].',
                                     "On mobile transfers, paste the recipient's email into the Last Name "
                                     'field so the confirmation screen shows exactly which address '
                                     'received the seats, since mobile sends no confirmation email '
                                     '[thumbsuprun — MP1aH4hgG70 @ 00:04:41].',
                                     'When a pass refuses to load into Apple Wallet, log in to '
                                     'Ticketmaster through Safari on the iPhone instead of the app and tap '
                                     'Add to Apple Wallet from there [Patchwave Tutorials — Wqb02oxLDJ0 @ '
                                     '00:00:00].',
                                     'Postponed-show inventory keeps working: barcodes are tied to the '
                                     'event manifest, not the date, so old barcodes scan at the '
                                     'rescheduled show even before a new date is set [thumbsuprun — '
                                     'MP1aH4hgG70 @ 00:05:39].']},
               'sop_steps': [{'step': 1,
                              'title': 'Confirm the seats can move',
                              'action': 'Open My Events, select the event and check whether the transfer '
                                        'button is live.',
                              'detail': 'A gray transfer button means the tickets cannot be transferred '
                                        '[The Savvy Professor — kC2NXuA1XV4 @ 00:01:21]; a missing '
                                        'transfer feature usually means the delivery delay has not been '
                                        'lifted or the tickets are hard stock or will call [thumbsuprun — '
                                        'MP1aH4hgG70 @ 00:01:35].'},
                             {'step': 2,
                              'title': 'Authenticate and pick only the sold seats',
                              'action': 'Tap Transfer, enter the OTP and select the individual seats going '
                                        'to this buyer.',
                              'detail': 'Ticketmaster sends an OTP to the registered email address and '
                                        'phone number before the recipient screen opens, and a single '
                                        'ticket can be picked when several are held for one event [Fixed '
                                        'Formulas — f7BuIdB0-6I @ 00:01:09].'},
                             {'step': 3,
                              'title': 'Lock the recipient address',
                              'action': 'Put the full name in First Name, paste the email into Last Name '
                                        'and the email field, then message the buyer.',
                              'detail': 'The last-name paste exposes the exact address on the confirmation '
                                        'screen [thumbsuprun — MP1aH4hgG70 @ 00:04:41]; a typo sends '
                                        'tickets to the wrong person, so tell the recipient to watch for '
                                        'the notification and accept promptly [Gadget Tune — 8yXxF_U1uek @ '
                                        '00:02:06].'},
                             {'step': 4,
                              'title': 'Track acceptance until complete',
                              'action': 'Watch the pending status and cancel or resend before acceptance '
                                        'if anything is wrong.',
                              'detail': 'A transfer can be cancelled any time before the recipient accepts '
                                        'and the history shows pending or accepted [Poolarity - Life Hacks '
                                        '— IENQeieAOCo @ 00:02:42]; once accepted the status reads '
                                        "complete and the sender's old barcodes are invalid [thumbsuprun — "
                                        'MP1aH4hgG70 @ 00:04:01].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split on delivery is where the transfer actually originates. '
                              'Poolarity - Life Hacks runs transfers from the Ticketmaster mobile website '
                              'rather than the app, because the site allows multi-select and pushes '
                              'several SafeTix to one email in a single pass instead of one by one in the '
                              'app [IENQeieAOCo @ 00:00:00]. Gadget Tune pitches a second lane entirely: '
                              'open Apple Wallet, tap the three-dot share button, and fire the ticket out '
                              'by AirDrop, Messages, or email, with the recipient accepting inside their '
                              'own Ticketmaster account, and calls that the quick option for nearby '
                              'contacts [8yXxF_U1uek @ 00:00:56]. Nexustech flatly contradicts that '
                              'playbook, stating you cannot transfer a ticket from Apple Wallet directly '
                              'because the wallet only stores a copy and the real ticket always lives '
                              'inside Ticketmaster [lBLVmAx5wkQ @ 00:00:21]. Patchwave Tutorials lands on '
                              'the same side, telling anyone loading a pass just to forward it to skip '
                              'Apple Wallet entirely and use the built-in transfer button inside the app '
                              'or website [Wqb02oxLDJ0 @ 00:01:17]. The operator read: three of the four '
                              'route every transfer through the Ticketmaster account itself, so any '
                              'wallet-share lane should be tested on a live order before a buyer is '
                              'promised delivery that way.',
                              'Refund reliability splits the room depending on whether a speaker judges '
                              'calm-weather service or crisis behavior. GigaBits, after two weeks testing '
                              'all three platforms, rates Ticketmaster refunds strict and slow, StubHub '
                              'helpful but inconsistent depending on the seller, and SeatGeek surprisingly '
                              'responsive [7KU-5HUqmzA @ 00:02:58]. thumbsuprun calls the resale fan '
                              'guarantee the number one filter, because a real guarantee either sources '
                              'replacement tickets or pays a 100% money-back refund if the tickets fail to '
                              'get you in [sIgspwKXj_0 @ 00:01:32]. WCPO 9 reported the inverse during '
                              'mass postponements: after outrage from fans and lawmakers, buyers who '
                              'purchased directly from Ticketmaster got refunds for both cancelled and '
                              'postponed shows, while neither Vivid Seats nor StubHub paid cash on '
                              'postponed concerts [VBj60jqiycw @ 00:01:24]. The same report shows StubHub '
                              'offering a couple holding 800 dollars of Foo Fighters tickets only '
                              'vouchers, with its president explaining that in normal times the '
                              'marketplace fronts buyer refunds before recouping them from the seller '
                              '[VBj60jqiycw @ 00:01:08]. Net read: the resale guarantee thumbsuprun leans '
                              'on is funded by seller recoupment, and that recoupment is exactly what '
                              'stalled when events froze, so tickets bought direct from Ticketmaster held '
                              'the stronger refund position in a wave event.',
                              'On postponed shows, the playbooks diverge between holding, crediting, and '
                              "fighting. thumbsuprun's hold case is that any postponed and rescheduled "
                              'event keeps the original barcodes valid, even before a new date is set, '
                              'because the barcode manifest is tied to the event rather than the calendar '
                              "date [MP1aH4hgG70 @ 00:05:39]. The channel's Ticketmaster refund breakdown "
                              'adds a credit lane: skip the cash and take up to 150 percent concert cash '
                              'credit, framed as basically a free event ticket down the road, with the '
                              'catch that your cash stays tied up [s9mNdqH694I @ 00:03:09]. WGRZ-TV '
                              'profiled the fight lane: Tate Helms bought eight Rolling Stones tickets, '
                              "was stonewalled under Vivid's all-sales-final postponement terms, and still "
                              "recovered 1,577 dollars, with the station's advice being to send strongly "
                              'worded emails, be loud, and demand the refund [YksJO2KDmnk @ 00:02:16]. Yet '
                              'a WGRZ anchor reported a refund for a concert from the previous summer that '
                              'simply came back without any strongly worded email, only a few weeks before '
                              'the broadcast [YksJO2KDmnk @ 00:03:00]. Escalation worked for one buyer and '
                              'patience worked for another, and thumbsuprun says there is nothing wrong '
                              'with either the refund or the credit, as long as the choice matches how '
                              'urgently the cash is needed.'],
               'table': {'caption': 'Competing transfer, wallet and refund playbooks taught by the '
                                    'practitioners',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Where to start a multi-ticket transfer run',
                                   'Ticketmaster website on the phone with multi-select pushes several '
                                   'SafeTix to one email in one pass',
                                   'App transfer flow goes seat by seat but lets you pick a saved contact '
                                   'to save taps',
                                   'Poolarity - Life Hacks ([IENQeieAOCo @ 00:00:00]); thumbsuprun '
                                   '([MP1aH4hgG70 @ 00:02:42])'],
                                  ['Apple Wallet as a delivery lane for buyers',
                                   'Share from the Wallet three-dot menu by AirDrop, Messages or email, '
                                   'recipient accepts in Ticketmaster',
                                   'Wallet holds only a copy, so every transfer must run through the '
                                   'Ticketmaster app or website',
                                   'Gadget Tune ([8yXxF_U1uek @ 00:00:56]); Nexustech ([lBLVmAx5wkQ @ '
                                   '00:00:21])'],
                                  ['Which platform handles refunds and support best',
                                   'Ticketmaster rated strict and slow, StubHub helpful but inconsistent '
                                   'depending on the seller',
                                   'SeatGeek rated surprisingly responsive and fastest at solving issues '
                                   'after two weeks of testing',
                                   'GigaBits ([7KU-5HUqmzA @ 00:02:58]); GigaBits ([7KU-5HUqmzA @ '
                                   '00:03:20])'],
                                  ['Resale guarantee versus mass-postponement reality',
                                   'Fan guarantee promises replacement tickets or a full 100% money-back '
                                   'refund on entry failure',
                                   'During postponements StubHub offered only vouchers and neither StubHub '
                                   'nor Vivid Seats paid cash',
                                   'thumbsuprun ([sIgspwKXj_0 @ 00:01:32]); WCPO 9 ([VBj60jqiycw @ '
                                   '00:01:24])'],
                                  ['Postponed show with tickets already in the account',
                                   'Hold the tickets because original barcodes stay valid for the '
                                   'rescheduled date automatically',
                                   'Request a refund once no rescheduled date is set within 60 days of the '
                                   'postponement',
                                   'thumbsuprun ([MP1aH4hgG70 @ 00:05:39]); thumbsuprun ([s9mNdqH694I @ '
                                   '00:05:01])'],
                                  ['Cash refund versus Ticketmaster account credit choice',
                                   'Take the cash refund and accept roughly 30 days of batched processing '
                                   'time',
                                   'Take up to 150 percent concert cash credit and accept that the cash '
                                   'stays tied up',
                                   'thumbsuprun ([s9mNdqH694I @ 00:03:09]); thumbsuprun ([s9mNdqH694I @ '
                                   '00:05:31])'],
                                  ['Escalation on a stonewalled resale refund request',
                                   'Send strongly worded emails, be loud and demand it, as Tate Helms '
                                   'recovered 1,577 dollars',
                                   "Wait it out, as one WGRZ anchor's refund simply came back without any "
                                   'email at all',
                                   'WGRZ-TV ([YksJO2KDmnk @ 00:02:16]); WGRZ-TV ([YksJO2KDmnk @ '
                                   '00:03:00])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Delivery mistakes start at the recipient field. Gadget Tune warns that a '
                              "simple typo in the recipient's email address or phone number can send your "
                              'tickets to the wrong person, and tells senders to let the recipient know '
                              'tickets are coming so the notification gets accepted promptly [8yXxF_U1uek '
                              '@ 00:01:50]. thumbsuprun flagged a quieter trap: a transfer sent from the '
                              'mobile app fires with no confirmation and no email receipt, and the '
                              'completion screen shows only first and last name, so the sender cannot see '
                              'which address was actually used [MP1aH4hgG70 @ 00:04:15]. The same Ticket '
                              'Tip Thursday episode explains a missing transfer button: either the '
                              'delivery delay has not been lifted yet, or the ticket type, such as hard '
                              'stock or will call, is simply not eligible for transfer [MP1aH4hgG70 @ '
                              '00:01:35]. Poolarity - Life Hacks supplies the recovery lever: an '
                              'unaccepted transfer stays in the list as pending with full history, and it '
                              'can be cancelled at any time as long as the recipient has not accepted '
                              '[IENQeieAOCo @ 00:02:29]. The economics check is blunt: until the other '
                              'side clicks accept, the seller still controls the seats, and once they '
                              "accept, the sender's status flips from pending to complete and the seats "
                              'are gone.',
                              'Gate-day failures cluster around the barcode itself. Helpful Solutions '
                              'points out that barcodes for some events do not appear until 24 to 48 hours '
                              'before the event, held back on purpose to prevent ticket fraud, so an empty '
                              'wallet days out should be checked against the event notice before anyone '
                              "panics [hNlTOy1daSA @ 00:00:19]. The Savvy Professor's error list doubles "
                              'as a resale red-flag sheet: a ticket bought from someone else who did not '
                              'transfer it properly, will call or print-at-home chosen at checkout, a '
                              'phone order through a sales rep, VIP or premium tickets, and non-refundable '
                              'add-ons can all block Apple Wallet [zH4ITvC9voc @ 00:02:02]. Patchwave '
                              'Tutorials adds device-side blockers: an active VPN or iCloud private relay '
                              'can break the Apple Wallet handshake, the iPhone region must match the '
                              'purchase country, and a phone with no passcode or Face ID gets new passes '
                              'rejected [Wqb02oxLDJ0 @ 00:00:43]. Nexustech closes the screenshot '
                              'loophole: Wallet tickets carry dynamic barcodes that refresh every few '
                              'seconds, so screenshots or copies get rejected by entry scanners '
                              '[lBLVmAx5wkQ @ 00:02:13]. Each of these produces the same delivery-day '
                              'outcome: a ticket that exists in the account but cannot be added, '
                              'displayed, or scanned when the buyer reaches the gate.',
                              'Cash-flow traps dominate the refund side. thumbsuprun walked through '
                              'Ticketmaster quietly switching in late March or early April to refunds for '
                              'canceled events only, leaving postponed, suspended, and on-hold shows '
                              'stranded while nobody had a new date [s9mNdqH694I @ 00:01:07]. Even under '
                              'the revised plan, undated postponed shows only qualified once 60 days '
                              'passed without a rescheduled date, refunds were quoted at 30 days to '
                              'process, and buying into an already-postponed event generally did not '
                              "qualify, a structure the channel read as built to manage Ticketmaster's "
                              'cash flow [s9mNdqH694I @ 00:05:31]. WCPO 9 showed the resale-chain dead '
                              'end: Nikki Agee paid 648 dollars for four Elton John tickets through Vivid '
                              'Seats and was told any refund had to come from the person who transferred '
                              'the tickets, meaning the tickets would go back to the original owner '
                              "[VBj60jqiycw @ 00:00:20]. WGRZ-TV's Better Business Bureau source, Tom "
                              'Bartholomy, warned that the terms and conditions are where the landmines '
                              'sit and reported never seeing a time limit on how long a postponement can '
                              'run [YksJO2KDmnk @ 00:01:42]. Stack those together and the economics check '
                              'is plain: on resale inventory with no-refund postponement terms, buyer cash '
                              'can sit frozen indefinitely, while even direct Ticketmaster refunds ride a '
                              'batched 30-day processing clock.'],
               'table': {'caption': 'Firsthand transfer, wallet and refund failures with the fix each '
                                    'practitioner used',
                         'headers': ['Failure Mode',
                                     'What Went Wrong',
                                     'Fix Or Economic Check',
                                     'Expert Source'],
                         'rows': [['Typo in the recipient email or phone number',
                                   'A single wrong character sends the tickets to the wrong person '
                                   'entirely',
                                   'Verify recipient details before initiating and tell the recipient to '
                                   'watch for the notification',
                                   'Gadget Tune ([8yXxF_U1uek @ 00:01:50])'],
                                  ['Mobile transfer fires with no email confirmation',
                                   'Completion screen shows only first and last name, never the address '
                                   'actually used',
                                   'Put the full name in First Name and paste the email into Last Name to '
                                   'display it',
                                   'thumbsuprun ([MP1aH4hgG70 @ 00:04:28])'],
                                  ['Transfer button greyed out or missing on the order',
                                   'Delivery delay not lifted yet, or hard stock and will call tickets are '
                                   'ineligible',
                                   'Check the event page for transferability before promising delivery to '
                                   'any buyer',
                                   'thumbsuprun ([MP1aH4hgG70 @ 00:01:35]); The Savvy Professor '
                                   '([kC2NXuA1XV4 @ 00:01:21])'],
                                  ['Transfer deadline missed close to showtime',
                                   'Many events set deadlines typically 72 hours before start, and dynamic '
                                   'pricing can restrict transfers',
                                   'Contact Ticketmaster customer service immediately for emergency '
                                   'transfer assistance',
                                   'Gadget Tune ([8yXxF_U1uek @ 00:01:13]); Gadget Tune ([8yXxF_U1uek @ '
                                   '00:02:24])'],
                                  ['Apple Wallet refuses to add the pass',
                                   'VPN or private relay, region mismatch, no passcode, or iOS older than '
                                   '16.4 blocks the add',
                                   'Log in through Safari and add from there, then update iOS and the '
                                   'Ticketmaster app',
                                   'Patchwave Tutorials ([Wqb02oxLDJ0 @ 00:00:00]); The Savvy Professor '
                                   '([zH4ITvC9voc @ 00:01:43])'],
                                  ['Scanner rejects the ticket at the entrance gate',
                                   'Screenshots of dynamic codes, resized barcodes, anti-spy protectors, '
                                   'damaged screens or low battery',
                                   'Present the live moving barcode at original size on a charged, '
                                   'undamaged, unprotected screen',
                                   'Nexustech ([lBLVmAx5wkQ @ 00:02:13]); Paso a paso ([EwQdnuSrWAo @ '
                                   '00:01:15])'],
                                  ['Resale refund dead end on a postponed concert',
                                   'Vivid buyer told refunds must come from the original transferor, and '
                                   'terms say all sales final',
                                   'Buy direct from Ticketmaster, which offered refunds on both cancelled '
                                   'and postponed shows',
                                   'WCPO 9 ([VBj60jqiycw @ 00:00:20]); WGRZ-TV ([YksJO2KDmnk @ '
                                   '00:01:25])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Kill Switches Before Any Ticket Changes Hands',
                           'body': 'Each gate below comes from a transfer, wallet or refund failure the '
                                   'practitioners hit firsthand; clear all four before a buyer is told the '
                                   'tickets are on the way.',
                           'items': ['Do not promise delivery until the transfer button is live on the '
                                     'order, since an unlifted delivery delay or hard stock and will call '
                                     'tickets block transfers [thumbsuprun — MP1aH4hgG70 @ 00:01:35].',
                                     'On mobile, confirm the recipient address by pasting the email into '
                                     'the Last Name field before hitting transfer, because no confirmation '
                                     'email is sent [thumbsuprun — MP1aH4hgG70 @ 00:04:28].',
                                     'Never deliver screenshots or Apple Wallet copies; dynamic barcodes '
                                     'refresh every few seconds and entry scanners reject copies, so move '
                                     'tickets only through Ticketmaster [Nexustech — lBLVmAx5wkQ @ '
                                     '00:02:13].',
                                     'Before buying into a postponed event, assume no refund lane: '
                                     'purchases into an already-postponed event generally do not qualify '
                                     'for the Ticketmaster refund program [thumbsuprun — s9mNdqH694I @ '
                                     '00:07:24].']}}],
 'pull_quote': '"Only shop at places where you\'re getting a full 100 percent guarantee for your '
               'tickets... without this do not buy tickets." — thumbsuprun (sIgspwKXj_0 @ 00:02:25).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Run multi-ticket transfers from the Ticketmaster website with multi-select to push '
                      'several tickets to one email instead of sending them one by one in the app '
                      '[Poolarity - Life Hacks — IENQeieAOCo @ 00:00:00].',
                      'Clear the OTP authentication sent to your registered email and phone number, then '
                      "enter the recipient's first name, last name and email before confirming the "
                      'transfer [Fixed Formulas — f7BuIdB0-6I @ 00:01:09].',
                      'On mobile transfers, paste the recipient email into the Last Name field so the '
                      'confirmation screen displays the exact address the tickets went to [thumbsuprun — '
                      'MP1aH4hgG70 @ 00:04:28].',
                      'Watch the transfer history for pending status and cancel any transfer the recipient '
                      'has not yet accepted if the deal falls through [Poolarity - Life Hacks — '
                      'IENQeieAOCo @ 00:02:29].',
                      'When a barcode is missing from the wallet, check whether it unlocks 24 to 48 hours '
                      'out, then remove and re-add the ticket, update the apps, and test on another device '
                      '[Helpful Solutions — hNlTOy1daSA @ 00:01:26].',
                      'On postponed events, choose between the cash refund and up to 150 percent concert '
                      'cash credit inside the selection window, and push stonewalled resale refunds with '
                      'strongly worded emails [thumbsuprun — s9mNdqH694I @ 00:03:09] [WGRZ-TV — '
                      'YksJO2KDmnk @ 00:02:16].'],
 'statutory_citations': [{'title': 'thumbsuprun — HOW TO TRANSFER TICKETS ON TICKETMASTER TO ANOTHER PHONE '
                                   '| TICKET TIP THURSDAY [00:05:39]',
                          'url': 'https://www.youtube.com/watch?v=MP1aH4hgG70&t=339s',
                          'relevance': 'Primary practitioner testimony on transfer mechanics, the '
                                       'no-confirmation mobile trap, and barcodes staying valid for '
                                       'postponed events.'},
                         {'title': 'thumbsuprun — TICKETMASTER REFUND POLICY UPDATE FOR CANCELLED AND '
                                   'POSTPONED EVENTS | TICKET REFUND PLAN [00:05:01]',
                          'url': 'https://www.youtube.com/watch?v=s9mNdqH694I&t=301s',
                          'relevance': 'Primary practitioner testimony on the 60-day postponement rule, '
                                       '30-day refund processing, and the 150 percent credit option.'},
                         {'title': 'WCPO 9 — Struggle for concert ticket refunds [00:01:24]',
                          'url': 'https://www.youtube.com/watch?v=VBj60jqiycw&t=84s',
                          'relevance': 'Primary practitioner testimony on direct Ticketmaster refunds '
                                       'versus StubHub and Vivid Seats refusing cash on postponed '
                                       'concerts.'},
                         {'title': 'Nexustech — How To Transfer Ticketmaster Tickets from Apple Wallet to '
                                   'Someone Else [2026 GUIDE] [00:00:21]',
                          'url': 'https://www.youtube.com/watch?v=lBLVmAx5wkQ&t=21s',
                          'relevance': 'Primary practitioner testimony on Apple Wallet holding only a copy '
                                       'and dynamic barcodes defeating screenshots.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '7KU-5HUqmzA',
                       'title': 'Ticketmaster vs StubHub vs SeatGeek (2025) – What Ticket Seller Do We '
                                'Need in 2026?',
                       'channel': 'GigaBits',
                       'author': 'GigaBits',
                       'text': 'Ticket Master is the most reliable for official mobile entry, and on '
                               'refunds and customer support Ticket Master is strict and slow.',
                       'tip': 'Ticket Master is the most reliable for official mobile entry, and on '
                              'refunds and customer support Ticket Master is strict and slow.',
                       'timestamp': 178,
                       'timestamp_seconds': 178,
                       'timestamp_label': '[00:02:58]',
                       'url': 'https://www.youtube.com/watch?v=7KU-5HUqmzA&t=178s',
                       'markdown': '[00:02:58](https://www.youtube.com/watch?v=7KU-5HUqmzA&t=178s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sIgspwKXj_0',
                       'title': 'THE 5 THINGS ANY TICKET RESALE WEBSITE NEEDS TO HAVE | ARE THEY LEGIT?',
                       'channel': 'thumbsuprun',
                       'author': 'thumbsuprun',
                       'text': 'If they do not get you in, they will either make sure they get replacement '
                               'tickets to get you into that event regardless or they will give you a 100% '
                               'money-back guarantee on your tickets.',
                       'tip': 'If they do not get you in, they will either make sure they get replacement '
                              'tickets to get you into that event regardless or they will give you a 100% '
                              'money-back guarantee on your tickets.',
                       'timestamp': 92,
                       'timestamp_seconds': 92,
                       'timestamp_label': '[00:01:32]',
                       'url': 'https://www.youtube.com/watch?v=sIgspwKXj_0&t=92s',
                       'markdown': '[00:01:32](https://www.youtube.com/watch?v=sIgspwKXj_0&t=92s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IENQeieAOCo',
                       'title': 'TicketMaster SafeTix Transfer Tickets | How To Demo',
                       'channel': 'Poolarity - Life Hacks',
                       'author': 'Poolarity - Life Hacks',
                       'text': "I'm preferring the website over the app because the website actually "
                               'allows me to do multi select so I could transfer multiple tickets to one '
                               'email versus one by one in the app.',
                       'tip': "I'm preferring the website over the app because the website actually allows "
                              'me to do multi select so I could transfer multiple tickets to one email '
                              'versus one by one in the app.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=IENQeieAOCo&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=IENQeieAOCo&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EwQdnuSrWAo',
                       'title': '¿Cómo usar SafeTix de Ticketmaster? Tutorial paso a paso',
                       'channel': 'Paso a paso',
                       'author': 'Paso a paso',
                       'text': 'It features a dynamic code that changes every 15 seconds.',
                       'tip': 'It features a dynamic code that changes every 15 seconds.',
                       'timestamp': 18,
                       'timestamp_seconds': 18,
                       'timestamp_label': '[00:00:18]',
                       'url': 'https://www.youtube.com/watch?v=EwQdnuSrWAo&t=18s',
                       'markdown': '[00:00:18](https://www.youtube.com/watch?v=EwQdnuSrWAo&t=18s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EwQdnuSrWAo',
                       'title': '¿Cómo usar SafeTix de Ticketmaster? Tutorial paso a paso',
                       'channel': 'Paso a paso',
                       'author': 'Paso a paso',
                       'text': 'Present the dynamic barcode of your digital ticket in its original size. '
                               'Do not make it larger or smaller.',
                       'tip': 'Present the dynamic barcode of your digital ticket in its original size. Do '
                              'not make it larger or smaller.',
                       'timestamp': 75,
                       'timestamp_seconds': 75,
                       'timestamp_label': '[00:01:15]',
                       'url': 'https://www.youtube.com/watch?v=EwQdnuSrWAo&t=75s',
                       'markdown': '[00:01:15](https://www.youtube.com/watch?v=EwQdnuSrWAo&t=75s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lBLVmAx5wkQ',
                       'title': 'How To Transfer Ticketmaster Tickets from Apple Wallet to Someone Else '
                                '[2026 GUIDE]',
                       'channel': 'Nexustech',
                       'author': 'Nexustech',
                       'text': 'You cannot transfer a ticket from Apple Wallet directly. Apple Wallet only '
                               'stores a copy of the ticket.',
                       'tip': 'You cannot transfer a ticket from Apple Wallet directly. Apple Wallet only '
                              'stores a copy of the ticket.',
                       'timestamp': 21,
                       'timestamp_seconds': 21,
                       'timestamp_label': '[00:00:21]',
                       'url': 'https://www.youtube.com/watch?v=lBLVmAx5wkQ&t=21s',
                       'markdown': '[00:00:21](https://www.youtube.com/watch?v=lBLVmAx5wkQ&t=21s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8yXxF_U1uek',
                       'title': 'How to Transfer Ticketmaster Tickets from Apple Wallet – Step By Step '
                                'Guide',
                       'channel': 'Gadget Tune',
                       'author': 'Gadget Tune',
                       'text': 'Many events now have specific transfer deadlines, typically 72 hours '
                               'before the event starts.',
                       'tip': 'Many events now have specific transfer deadlines, typically 72 hours before '
                              'the event starts.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=8yXxF_U1uek&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=8yXxF_U1uek&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hNlTOy1daSA',
                       'title': 'How To Fix Ticketmaster Barcode Not Showing In Wallet (Easy Solutions To '
                                'Troubleshoot The Issue)',
                       'channel': 'Helpful Solutions',
                       'author': 'Helpful Solutions',
                       'text': 'The barcodes are typically made available 24 to 48 hours before the event '
                               'to prevent ticket fraud.',
                       'tip': 'The barcodes are typically made available 24 to 48 hours before the event '
                              'to prevent ticket fraud.',
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=hNlTOy1daSA&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=hNlTOy1daSA&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Wqb02oxLDJ0',
                       'title': 'How to Fix Unable to Add Pass to Apple Wallet from Ticketmaster – iPhone '
                                'Setup & Fix Guide',
                       'channel': 'Patchwave Tutorials',
                       'author': 'Patchwave Tutorials',
                       'text': 'Disable any active VPN or Apple private relay in your iCloud settings as '
                               'security proxies frequently block Apple Wallet API handshakes.',
                       'tip': 'Disable any active VPN or Apple private relay in your iCloud settings as '
                              'security proxies frequently block Apple Wallet API handshakes.',
                       'timestamp': 43,
                       'timestamp_seconds': 43,
                       'timestamp_label': '[00:00:43]',
                       'url': 'https://www.youtube.com/watch?v=Wqb02oxLDJ0&t=43s',
                       'markdown': '[00:00:43](https://www.youtube.com/watch?v=Wqb02oxLDJ0&t=43s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'f7BuIdB0-6I',
                       'title': 'How to Transfer Tickets on Ticketmaster [2026] UPDATED',
                       'channel': 'Fixed Formulas',
                       'author': 'Fixed Formulas',
                       'text': 'After clicking on the transfer option, you will have to first of all '
                               'authenticate your account, so on your registered email address and your '
                               'phone number they are going to send an OTP.',
                       'tip': 'After clicking on the transfer option, you will have to first of all '
                              'authenticate your account, so on your registered email address and your '
                              'phone number they are going to send an OTP.',
                       'timestamp': 69,
                       'timestamp_seconds': 69,
                       'timestamp_label': '[00:01:09]',
                       'url': 'https://www.youtube.com/watch?v=f7BuIdB0-6I&t=69s',
                       'markdown': '[00:01:09](https://www.youtube.com/watch?v=f7BuIdB0-6I&t=69s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'kC2NXuA1XV4',
                       'title': 'How to Transfer Tickets on Ticketmaster (What is a Ticket Transfer?)',
                       'channel': 'The Savvy Professor',
                       'author': 'The Savvy Professor',
                       'text': "Once you've viewed that the details of the ticket are accurate click on "
                               "transfer, however if the transfer button is gray you can't transfer them.",
                       'tip': "Once you've viewed that the details of the ticket are accurate click on "
                              "transfer, however if the transfer button is gray you can't transfer them.",
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=kC2NXuA1XV4&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=kC2NXuA1XV4&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zH4ITvC9voc',
                       'title': 'How to Save Ticketmaster Tickets to Apple Wallet (How Do I Add Tickets to '
                                'a Digital Wallet?)',
                       'channel': 'The Savvy Professor',
                       'author': 'The Savvy Professor',
                       'text': "You bought your ticket from someone else and they didn't transfer it "
                               'properly, or you selected will call or print at home during checkout.',
                       'tip': "You bought your ticket from someone else and they didn't transfer it "
                              'properly, or you selected will call or print at home during checkout.',
                       'timestamp': 122,
                       'timestamp_seconds': 122,
                       'timestamp_label': '[00:02:02]',
                       'url': 'https://www.youtube.com/watch?v=zH4ITvC9voc&t=122s',
                       'markdown': '[00:02:02](https://www.youtube.com/watch?v=zH4ITvC9voc&t=122s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Mkuhus1taO4',
                       'title': 'How To Use Digital Tickets On Ticketmaster',
                       'channel': 'Guide Nation',
                       'author': 'Guide Nation',
                       'text': "You can either click on view ticket and then here you'll see a digital "
                               'version of your ticket, so at the gate the scanner person can actually '
                               'scan this barcode so that you can be allowed into the event.',
                       'tip': "You can either click on view ticket and then here you'll see a digital "
                              'version of your ticket, so at the gate the scanner person can actually scan '
                              'this barcode so that you can be allowed into the event.',
                       'timestamp': 36,
                       'timestamp_seconds': 36,
                       'timestamp_label': '[00:00:36]',
                       'url': 'https://www.youtube.com/watch?v=Mkuhus1taO4&t=36s',
                       'markdown': '[00:00:36](https://www.youtube.com/watch?v=Mkuhus1taO4&t=36s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MP1aH4hgG70',
                       'title': 'HOW TO TRANSFER TICKETS ON TICKETMASTER TO ANOTHER PHONE | TICKET TIP '
                                'THURSDAY',
                       'channel': 'thumbsuprun',
                       'author': 'thumbsuprun',
                       'text': 'Any tickets you bought where an event has been postponed and rescheduled '
                               "to a new date, even if the date hasn't yet been set, the old barcodes will "
                               'always work for the new event.',
                       'tip': 'Any tickets you bought where an event has been postponed and rescheduled to '
                              "a new date, even if the date hasn't yet been set, the old barcodes will "
                              'always work for the new event.',
                       'timestamp': 339,
                       'timestamp_seconds': 339,
                       'timestamp_label': '[00:05:39]',
                       'url': 'https://www.youtube.com/watch?v=MP1aH4hgG70&t=339s',
                       'markdown': '[00:05:39](https://www.youtube.com/watch?v=MP1aH4hgG70&t=339s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 's9mNdqH694I',
                       'title': 'TICKETMASTER REFUND POLICY UPDATE FOR CANCELLED AND POSTPONED EVENTS | '
                                'TICKET REFUND PLAN',
                       'channel': 'thumbsuprun',
                       'author': 'thumbsuprun',
                       'text': 'You can go ahead and get up to a hundred and fifty percent concert cash '
                               'credit back on your account.',
                       'tip': 'You can go ahead and get up to a hundred and fifty percent concert cash '
                              'credit back on your account.',
                       'timestamp': 189,
                       'timestamp_seconds': 189,
                       'timestamp_label': '[00:03:09]',
                       'url': 'https://www.youtube.com/watch?v=s9mNdqH694I&t=189s',
                       'markdown': '[00:03:09](https://www.youtube.com/watch?v=s9mNdqH694I&t=189s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 's9mNdqH694I',
                       'title': 'TICKETMASTER REFUND POLICY UPDATE FOR CANCELLED AND POSTPONED EVENTS | '
                                'TICKET REFUND PLAN',
                       'channel': 'thumbsuprun',
                       'author': 'thumbsuprun',
                       'text': 'Any postponed events that do not have a rescheduled date set within 60 '
                               'days of when it was postponed, these will also now qualify for a refund.',
                       'tip': 'Any postponed events that do not have a rescheduled date set within 60 days '
                              'of when it was postponed, these will also now qualify for a refund.',
                       'timestamp': 301,
                       'timestamp_seconds': 301,
                       'timestamp_label': '[00:05:01]',
                       'url': 'https://www.youtube.com/watch?v=s9mNdqH694I&t=301s',
                       'markdown': '[00:05:01](https://www.youtube.com/watch?v=s9mNdqH694I&t=301s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'VBj60jqiycw',
                       'title': 'Struggle for concert ticket refunds',
                       'channel': 'WCPO 9',
                       'author': 'WCPO 9',
                       'text': 'If you purchase directly from Ticketmaster, after outrage from fans and '
                               'lawmakers Ticketmaster is now offering refunds for both cancelled and '
                               'postponed shows.',
                       'tip': 'If you purchase directly from Ticketmaster, after outrage from fans and '
                              'lawmakers Ticketmaster is now offering refunds for both cancelled and '
                              'postponed shows.',
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=VBj60jqiycw&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=VBj60jqiycw&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YksJO2KDmnk',
                       'title': 'Wednesday Town Hall: Can you get a refund on canceled or postponed '
                                'concert tickets?',
                       'channel': 'WGRZ-TV',
                       'author': 'WGRZ-TV',
                       'text': 'Tate was able to get his 1577 dollars back, and the best advice is send '
                               'strongly worded emails, be loud about it and demand that refund.',
                       'tip': 'Tate was able to get his 1577 dollars back, and the best advice is send '
                              'strongly worded emails, be loud about it and demand that refund.',
                       'timestamp': 136,
                       'timestamp_seconds': 136,
                       'timestamp_label': '[00:02:16]',
                       'url': 'https://www.youtube.com/watch?v=YksJO2KDmnk&t=136s',
                       'markdown': '[00:02:16](https://www.youtube.com/watch?v=YksJO2KDmnk&t=136s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q8.'}]}
