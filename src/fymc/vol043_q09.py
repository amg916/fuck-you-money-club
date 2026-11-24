from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'axs-workflows-back-office-ticketing-tools',
 'question_prompt': 'How do you handle AXS tickets and back-office ticketing, repricing and support '
                    'workflows?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'AXS Workflows and Back-Office Ticketing Tools',
 'subtitle': 'AXS app fixes, missing tickets and delivery methods, AXS-to-SeatGeek and Ticketmaster '
             'transfers, PromoTix event setup, Logitix event detail pages, Fastweigh repricing, s-ticket '
             'box office, and support-ticket and bulk order intake',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'AXS and back-office ticketing operators converge on hard rules: the phone app holds '
                      'the entry credential, the purchase email controls whether inventory appears, and '
                      'any trustworthy transfer voids the old QR code. AXS cannot push tickets straight '
                      'into Ticketmaster, so practitioners list on StubHub or SeatGeek or sell and rebuy, '
                      'and delivery-method changes go only through live chat. PromoTix runs shared '
                      'inventory caps, daisy-chained price tiers, will-call comps, and a 5% or 10% '
                      'organizer fee hidden inside the service fee line. Logitix One pushes inventory to '
                      'marketplaces through mass edit, mass apply, and one-click activation, while '
                      's-ticket and Zippykind cover door scans, refunds, and 1,000-row imports. The split: '
                      'Guide Gurus describes an AXS-to-SeatGeek claim-code transfer, while AidensGotGuides '
                      'treats cross-platform moves as resale workarounds.',
 'key_metrics': [{'label': 'Organizer Add-On Fee Bundled Into Service Fees',
                  'metric': 'Organizer Add-On Fee Bundled Into Service Fees',
                  'value': '5% or 10% on top of ticket price',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'PromoTix lets organizers add their own percentage that buyers see only as '
                             'part of one service fees line item, so a $20 ticket clears above face value.',
                  'source': 'PromoTix ([IdHpcPxQTfU @ 00:10:46])'},
                 {'label': 'Automatic Confirmation Email Resend Window',
                  'metric': 'Automatic Confirmation Email Resend Window',
                  'value': '24 hours before event start',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'PromoTix re-sends every previously issued confirmation email so buyers stop '
                             'flooding the organizer with lost-ticket requests in the final hour.',
                  'source': 'PromoTix ([IdHpcPxQTfU @ 00:17:15])'},
                 {'label': 'Bulk Ticket Import Row Cap Per File',
                  'metric': 'Bulk Ticket Import Row Cap Per File',
                  'value': 'Up to 1,000 rows per file',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Zippykind's Data Importer auto-maps spreadsheet columns, saves mapping "
                             'templates, and holds tickets off the map for a minute or two while '
                             'coordinates generate.',
                  'source': 'Zippykind ([OaCa2-zmCe8 @ 00:00:51])'},
                 {'label': 'AXS Tickets App Footprint',
                  'metric': 'AXS Tickets App Footprint',
                  'value': 'Over 10 million downloads, 3.9-star rating',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Web Mind cites the AXS Tickets app install base and store rating while '
                             'walking through concert and sports booking on mobile.',
                  'source': 'Web Mind ([RDQeHkadlqk @ 00:00:16])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator who teaches the AXS fan-side flow lands on the same '
                              'baseline: the phone is the ticket. Quick and Easy states flatly that buyers '
                              'can purchase on the website from a computer, but they must download the AXS '
                              'Tickets mobile app to actually attend, sign into the account holding the '
                              'inventory, and tap the tickets icon on the bottom menu to see every '
                              'upcoming event [oQOmX8EOyW4 @ 00:00:16]. Inside each event the same screen '
                              'exposes the three controls an operator lives in: manage, transfer, and '
                              'sell, with a QR code at the top that gets scanned at the gate on event day, '
                              'and the presenter adds that the code is reportedly reachable even without '
                              'an internet connection [oQOmX8EOyW4 @ 00:01:19]. Web Mind lays out the buy '
                              'path as location first, then category such as concert or sports match, then '
                              'price check, payment, and digital delivery straight to the phone, with '
                              'transfer to someone else available afterward [RDQeHkadlqk @ 00:00:45]. '
                              'Simply Finance closes the loop on vanished inventory: sign in with the '
                              'exact email address used at purchase, verify that email if the device is '
                              'new or has been idle, then open My Tickets and My Events, and if a fresh '
                              'purchase still does not show, wait a couple of hours before chasing the '
                              'organizer or seller with screenshots [SnJa0jDKiKE @ 00:00:42].',
                              'The second point of agreement is that a clean handoff kills the old '
                              'barcode. PromoTix COO Sebastian Schulze explains that an organizer-side '
                              'transfer cancels the original QR code and issues a fresh one to the new '
                              'registered owner, and CEO Will Royall frames this as the fix for the '
                              'classic resale scam where a seller emails a PDF copy, then gets in line '
                              'early and walks in ahead of the buyer, or sells the same PDF to several '
                              'people [IdHpcPxQTfU @ 00:22:35]. Brian Jones shows the identical logic at '
                              'the door in s-ticket: a ticket already used, or shared as a screenshot, '
                              'scans red with the time it was used and the staffer who let the holder in, '
                              'and a refunded ticket scans red as well [4Ddm_7kF3nc @ 00:04:44]. On '
                              'cross-platform moves, AidensGotGuides is blunt that AXS and Ticketmaster '
                              'run separate security systems, transfer rules, and delivery processes, so a '
                              'direct AXS-to-Ticketmaster transfer usually is not possible and hunting for '
                              'a hidden button wastes time [xEM0K5YLBZk @ 00:00:16]. The working path is '
                              'to list the AXS ticket on a resale marketplace such as StubHub or SeatGeek, '
                              'or sell it on an open marketplace and buy a replacement on Ticketmaster '
                              'through a completely separate transaction [xEM0K5YLBZk @ 00:01:21].',
                              'Back-office operators agree on one support doctrine: categorize hard, '
                              'because the category decides who touches the problem and how fast. '
                              'Stephanie at DigitalThinker tells users to write the high-level problem up '
                              'front, push specifics into the detail section, set a priority, and pick the '
                              'category carefully because it determines which department the ticket is '
                              "routed to [Y0_GSVWwMIw @ 00:01:57]. Vodafone's Supplier Digital Portal "
                              'makes the subcategory a mandatory step before subject and description '
                              'unlock, and first surfaces a click-here notification with the document '
                              'details so a supplier can back out to the dashboard without raising a '
                              'ticket at all [Db5sc_kyZFE @ 00:01:26]. Michael Pfaff of NDSE pushes the '
                              'same discipline: every request logged, assigned, and documented with '
                              'device, user, system, and fix notes, and categories built around how work '
                              'actually happens rather than one vague queue [N4lHcJFrT1E @ 00:00:53]. On '
                              'AXS itself, Simply Finance reports that delivery methods are predetermined '
                              'by the venue, spanning standard mail, will call, e-ticket, and most '
                              'popularly AXS Mobile ID, and that any change request goes only through live '
                              'chat with an agent via Profile, Help and Support Center, then the Buying '
                              'Tickets question button, followed by a patient wait for the reply '
                              '[s7E1Yc3RoQc @ 00:00:19].'],
               'table': {'caption': 'Where AXS and back-office ticketing practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Do',
                                     'Why It Matters To Operators',
                                     'Expert Source'],
                         'rows': [['The AXS mobile app is the actual entry credential',
                                   'Buy on the website if needed, but attend through the AXS Tickets app '
                                   'QR code',
                                   'The gate scan happens off the phone, not off the desktop purchase '
                                   'confirmation',
                                   'Quick and Easy ([oQOmX8EOyW4 @ 00:00:16])'],
                                  ['Missing AXS tickets usually trace back to the login email',
                                   'Sign in with the exact purchase email, verify it, then check My Events',
                                   'A mismatched account hides inventory even after a confirmed and paid '
                                   'purchase',
                                   'Simply Finance ([SnJa0jDKiKE @ 00:00:15])'],
                                  ['Legitimate transfers must void the original barcode every time',
                                   'Use the platform transfer so the old QR cancels and a new one issues',
                                   'Stops one PDF copy being sold twice or used early by the seller',
                                   'PromoTix ([IdHpcPxQTfU @ 00:22:09])'],
                                  ['AXS to Ticketmaster has no direct transfer pipe available',
                                   'List on StubHub or SeatGeek, or sell and rebuy a replacement on '
                                   'Ticketmaster',
                                   'Separate security systems and transfer rules block a straight '
                                   'platform-to-platform move',
                                   'AidensGotGuides ([xEM0K5YLBZk @ 00:00:16])'],
                                  ['AXS delivery method changes require a live chat agent',
                                   'Go Profile, Help and Support Center, Buying Tickets, then the question '
                                   'button',
                                   'The venue predetermines mail, will call, e-ticket, or AXS Mobile ID '
                                   'delivery',
                                   'Simply Finance ([s7E1Yc3RoQc @ 00:00:19])'],
                                  ['Support ticket category drives routing to the right department',
                                   'Choose category and priority carefully, then load specifics into the '
                                   'detail fields',
                                   'A wrong category sends the issue to the wrong department and stalls it',
                                   'DigitalThinker Inc. ([Y0_GSVWwMIw @ 00:01:57])'],
                                  ['Every request gets logged, assigned, and fully documented upfront',
                                   'Record the device, user, system, and the fix applied on each request',
                                   'Documented fixes shorten future troubleshooting and expose repeat '
                                   'interruption patterns',
                                   'NDSE ([N4lHcJFrT1E @ 00:00:37])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['PromoTix pitches event setup as really only four steps, and the ticket type '
                              "step is where inventory gets engineered. Schulze's demo stack pairs a "
                              'reserved-seating VIP tier, where buyers pick exact rows and seat numbers '
                              'during checkout, with a general admission type set at 500 inventory for $20 '
                              'apiece [IdHpcPxQTfU @ 00:03:53]. A password-required ticket type, usually '
                              'discounted, runs an exclusive presale by sharing the password only with the '
                              'target list, while a private ticket type disappears from the online '
                              "storefront but stays sellable through the organizer's point of sale and "
                              'issuable to guests [IdHpcPxQTfU @ 00:06:01]. Tiered pricing runs on '
                              'autopilot by daisy-chaining types, so standard pricing goes live the moment '
                              'early bird sells out or goes off sale and last chance follows behind it, '
                              'while a shared inventory pool caps combined adult, child, and senior sales '
                              'at venue capacity, 500 in the example, then auto-flags every linked type '
                              'sold out [IdHpcPxQTfU @ 00:09:21]. Brian Jones adds a seat-control move in '
                              's-ticket: switch to Block seats, give a reason such as house seats, and '
                              'click them blue, which pulls them from online sale while leaving them '
                              'sellable at the box office, and orange seats flag live online holds staff '
                              'cannot touch [4Ddm_7kF3nc @ 00:01:52].',
                              'The money layer is where the sharpest edge sits. PromoTix lets the '
                              'organizer stack their own 5% or 10% fee on top of the ticket price, and '
                              'Will Royall calls it a built-in rebate hidden inside the service fee, with '
                              'Schulze confirming buyers see only one line item labelled service fees and '
                              'are unaware a portion goes back to the organizer, so a $20 ticket clears '
                              'above face value [IdHpcPxQTfU @ 00:11:42]. PromoTix service fees pass to '
                              'buyers by default, processor options cover PayPal, Stripe, and PromoTix '
                              'Processing Pro for US enterprise accounts, and Venmo, PayPal Pay Later, '
                              'Apple Pay, and Google Pay switch on by checkbox with no extra setup '
                              '[IdHpcPxQTfU @ 00:13:05]. Refunds run full or partial on any processor, '
                              'with checkboxes to invalidate the QR codes on the order [IdHpcPxQTfU @ '
                              '00:24:41]. Brian Jones shows the s-ticket correction flow in pounds: a '
                              'member charged full price gets both seats switched to member pricing, the '
                              'page computes £6.00 to hand back, staff log how it was returned and why, '
                              'and the booking history keeps takings balanced, while a full refund puts '
                              'the seats straight back on sale and the old ticket stops being accepted at '
                              'the door [4Ddm_7kF3nc @ 00:02:51].',
                              'For brokers running inventory across marketplaces, Logitix product manager '
                              'Marty Carney maps the Logitix One event detail page: marketplace icons link '
                              'out to each event listing, and a grayed-out icon means the mapping does not '
                              'exist yet [YaZpToURgBk @ 00:01:20]. The inventory grid splits into a zone '
                              'grid and a ticket group grid; selecting a unified zone or section unlocks '
                              'mass edit to change share threshold, activate inventory, or flip automation '
                              "settings in a few clicks, while mass apply copies one zone's settings to "
                              'the same zone in other productions filtered by primary performer and venue '
                              '[YaZpToURgBk @ 00:02:59]. Clicking the check mark turns a group blue and '
                              'exports it to marketplaces, pressing enter after typing a new list price '
                              'jumps to the next group, right-click splits or merges groups, and a red '
                              "corner flag marks unsaved changes. Fastweigh's repricing module offers "
                              'single-ticket price edits that leave every other ticket untouched plus '
                              'single-ticket rate locks, and it only reprices tickets not yet invoiced '
                              "[SqgRdPpIv_I @ 00:01:21]. Zippykind's Data Importer caps each file at 1,000 "
                              'rows, auto-maps columns even when spreadsheets change shape, and saves '
                              'mapping templates so repeat files map themselves [OaCa2-zmCe8 @ 00:00:51].'],
               'table': {'caption': 'Exact tool settings and numbers practitioners demonstrated',
                         'headers': ['Tool', 'Workflow Lever', 'Exact Setting Or Number', 'Expert Source'],
                         'rows': [['PromoTix shared inventory pool feature',
                                   'Cap combined adult, child, and senior ticket types at venue capacity',
                                   'Combined cap of 500 in the example, all types auto sold out',
                                   'PromoTix ([IdHpcPxQTfU @ 00:09:21])'],
                                  ['PromoTix organizer percentage fee setting',
                                   'Fold an organizer cut into the platform service fee line item',
                                   '5% or 10% added on top, buyers see one service fees line',
                                   'PromoTix ([IdHpcPxQTfU @ 00:10:46])'],
                                  ['PromoTix confirmation email automation',
                                   'Re-send every ticket confirmation automatically before the doors open',
                                   'All confirmations re-sent 24 hours before the event start time',
                                   'PromoTix ([IdHpcPxQTfU @ 00:17:15])'],
                                  ['PromoTix discount code usage limits',
                                   'Throttle promo code abuse per buyer and across all buyers',
                                   'One use per buyer email address, 50 total orders in the example',
                                   'PromoTix ([IdHpcPxQTfU @ 00:41:51])'],
                                  ['Logitix One mass apply in the zone grid',
                                   "Copy one zone's settings to the same zone in other productions",
                                   'Eligible events dictated by primary performer and venue matching',
                                   'Logitix ([YaZpToURgBk @ 00:03:16])'],
                                  ['s-ticket box office complimentary ticket entry',
                                   'Issue a comp at the box office with an audit reason attached',
                                   'Other price set to £0 with a reason such as press ticket',
                                   'Brian Jones ([4Ddm_7kF3nc @ 00:01:03])'],
                                  ['Zippykind Data Importer bulk ticket upload',
                                   'Load spreadsheet tickets with auto column mapping and saved templates',
                                   'Up to 1,000 rows per file, coordinates take a minute or two',
                                   'Zippykind ([OaCa2-zmCe8 @ 00:00:51])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Box Office, Comp, and Broadcast Moves the Operators Actually Use',
                           'body': 'Small configuration choices decide whether free tickets leak onto the '
                                   'market, whether door lines move, and whether inventory ever reaches '
                                   'buyers on the marketplaces.',
                           'items': ['Issue guest-list comps and contest-winner tickets as will call so '
                                     'the guest gets notified without a QR code and must show ID at the '
                                     'door, which Royall says stops free tickets being resold and flooding '
                                     'the market against your own sales [PromoTix — IdHpcPxQTfU @ '
                                     '00:33:47]',
                                     'On a box office sale, answer no to the check-in prompt when the '
                                     'buyer is entering later so the items stay checked out and can be '
                                     'scanned at arrival; answer yes only when they walk straight in '
                                     '[PromoTix — IdHpcPxQTfU @ 00:29:26]',
                                     'For a split party, tap the missing seat to leave it out and admit '
                                     'the rest; the rescan shows amber for the remaining seat, and every '
                                     'door phone stays in step because the list updates every few seconds '
                                     '[Brian Jones — 4Ddm_7kF3nc @ 00:04:26]',
                                     'A grayed-out marketplace icon in Logitix One means no mapping exists '
                                     'for that event yet, so inventory will not broadcast there until '
                                     'mapping is in place and the group is activated blue [Logitix — '
                                     'YaZpToURgBk @ 00:01:20]']},
               'sop_steps': [{'step': 1,
                              'title': 'Engineer the inventory structure',
                              'action': 'Build reserved and GA ticket types, daisy-chain the price tiers, '
                                        'and wrap them in a shared inventory cap.',
                              'detail': 'Create early bird, standard, and last chance types and chain each '
                                        'to go live when the previous tier sells out or goes off sale, '
                                        'then pool adult, child, and senior types under one venue capacity '
                                        'such as 500 so the system auto-flags sold out [PromoTix — '
                                        'IdHpcPxQTfU @ 00:07:25]'},
                             {'step': 2,
                              'title': 'Stack the fee and payment layer',
                              'action': 'Pass platform fees to buyers, add the organizer percentage, and '
                                        'connect processors with alternate payment methods.',
                              'detail': 'Turn on the organizer fee at 5% or 10% so it bundles into the '
                                        'single service fees line, then connect PayPal, Stripe, or '
                                        'PromoTix Processing Pro and tick Venmo, PayPal Pay Later, Apple '
                                        'Pay, and Google Pay [PromoTix — IdHpcPxQTfU @ 00:10:46]'},
                             {'step': 3,
                              'title': 'Broadcast and reprice broker inventory',
                              'action': 'Activate ticket groups to export them, then mass edit list prices '
                                        'and notes across groups.',
                              'detail': 'In the Logitix One ticket group grid, select marketplace icons, '
                                        'click the check mark to activate and export, mass edit to update '
                                        'listing prices or internal and external notes, and publish before '
                                        'leaving so red-flagged unsaved changes are not lost [Logitix — '
                                        'YaZpToURgBk @ 00:03:35]'},
                             {'step': 4,
                              'title': 'Run the door and clear AXS app failures',
                              'action': 'Scan QR codes on staff phones with names logged, and triage '
                                        'broken AXS apps before the gate.',
                              'detail': 'Door staff log in once, add a first name, and scan with the '
                                        'camera where green is valid and red is used, screenshotted, or '
                                        'refunded; for an AXS app that will not load, confirm stable '
                                        'Wi-Fi, update from the App Store, offload the app, then delete '
                                        'and reinstall [Brian Jones — 4Ddm_7kF3nc @ 00:04:08] [iKnow iOS — '
                                        'zghU1cQya5k @ 00:00:00]'}]},
              {'section_number': 3,
               'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split in the AXS back office is whether a ticket can leave the '
                              'AXS ecosystem cleanly. Guide Gurus frames AXS to SeatGeek as a '
                              'straightforward few-step job: log into AXS, locate the tickets, have the '
                              "buyer's name and email address ready, hit the transfer button in My "
                              'Account, and the recipient gets an email, creates a SeatGeek account if '
                              'needed, and enters a claim code under My Tickets [6Og6Y7NbLsk @ 00:00:21] '
                              '[6Og6Y7NbLsk @ 00:01:15]. AidensGotGuides takes the opposite line for '
                              'Ticketmaster: moving a ticket directly from AXS into Ticketmaster usually '
                              "isn't possible because the two run on separate platforms, each with its own "
                              'security system, transfer rules, and delivery process, so there is '
                              'generally no built-in bridge [xEM0K5YLBZk @ 00:00:16]. Their playbook is to '
                              'stop hunting for a hidden transfer option, check whether the AXS ticket can '
                              'be listed on a secondary marketplace like StubHub or SeatGeek, and if '
                              'Ticketmaster is mandatory, sell the AXS ticket on an open marketplace and '
                              'buy a replacement on Ticketmaster as a separate transaction [xEM0K5YLBZk @ '
                              '00:01:21]. That leaves two distinct inventory decisions: treat '
                              'SeatGeek-bound AXS seats as a transfer-and-claim workflow, and treat '
                              'Ticketmaster-bound demand as a sell-then-rebuy trade where you need to know '
                              'current market value before listing and move fast before prices shift on '
                              'the replacement leg.',
                              'Practitioners also split on how much trust to put in a delivered barcode. '
                              'Quick and Easy treats the AXS event screen as a simple control panel: tap '
                              'the event and you can manage the ticket, transfer it, sell it, and show the '
                              "QR code to be scanned on event day [oQOmX8EOyW4 @ 00:00:47]. PromoTix's "
                              'Will Royall and Sebastian Schulze argue that loose copies are the real '
                              'exposure: their transfer feature cancels the original QR code and issues a '
                              'fresh one to the new registered owner, while simply emailing a PDF lets a '
                              'reseller get in line early and walk in before the buyer, or sell the same '
                              "PDF to multiple people [IdHpcPxQTfU @ 00:22:35]. Brian Jones's s-ticket "
                              'door app pushes enforcement to the scan itself: a party admitted partially '
                              'scans amber until the rest arrive, while a used ticket, a shared '
                              'screenshot, or a refunded ticket scans red with the time it was used and '
                              'the staff member who let the holder in [4Ddm_7kF3nc @ 00:04:26]. For comps, '
                              'PromoTix offers the alternative of will call, which notifies guests without '
                              'delivering QR codes and forces an ID check at the door, so a contest winner '
                              'cannot turn around and resell a free ticket and put more supply on the '
                              "market that undercuts the organizer's own revenue [IdHpcPxQTfU @ 00:34:06].",
                              'On pricing, the tools teach three different operating philosophies. '
                              'PromoTix pushes set-and-forget automation: build early bird, standard, and '
                              'last chance ticket types, then daisy chain them so each tier goes on sale '
                              'automatically the moment the previous tier goes off sale or sells out '
                              '[IdHpcPxQTfU @ 00:07:47]. Royall and Schulze also show a stacked margin '
                              'play, adding a 5 or 10 percent organizer fee bundled into the single '
                              'service fees line at checkout, so buyers are unaware a portion goes back to '
                              'the organizer and the seller clears more than face value [IdHpcPxQTfU @ '
                              '00:11:42]. Logitix product manager Marty Carney demonstrates a hands-on '
                              'revenue desk instead: click into a list price in the ticket group grid, '
                              'type a new number, press enter to jump straight to the next group, and use '
                              'mass edit or mass apply to push share thresholds, activation, and '
                              'automation settings across zones and other productions with the same '
                              "primary performer and venue [YaZpToURgBk @ 00:04:17]. Fastweigh's repricing "
                              'sits between the two, letting operators reprice an individual unbilled '
                              'ticket, bulk reprice selected tickets against the latest rates, and lock '
                              'rates on single tickets so later changes cannot touch them [SqgRdPpIv_I @ '
                              '00:01:21]. The real choice is automation that runs unattended versus a grid '
                              'you actively steer.'],
               'table': {'caption': 'Competing playbooks for AXS transfers, ticket security, pricing, and '
                                    'back-office intake',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Moving AXS seats onto another ticketing platform',
                                   'Transfer from AXS My Account to SeatGeek using buyer name and email; '
                                   'recipient claims with emailed code',
                                   'Treat direct AXS to Ticketmaster transfer as unsupported; sell on an '
                                   'open marketplace and buy a replacement',
                                   'Guide Gurus ([6Og6Y7NbLsk @ 00:00:39]); AidensGotGuides ([xEM0K5YLBZk '
                                   '@ 00:01:21])'],
                                  ['Protecting a resold or transferred ticket from duplication',
                                   'Platform transfer cancels the original QR code and issues a new one to '
                                   'the new owner',
                                   'Emailing a PDF copy lets the seller show up early or sell the same '
                                   'file repeatedly',
                                   'PromoTix ([IdHpcPxQTfU @ 00:22:09]); PromoTix ([IdHpcPxQTfU @ '
                                   '00:22:35])'],
                                  ['Issuing complimentary and guest list tickets to friends and winners',
                                   'Generate QR codes immediately and deliver them inside the guest '
                                   'confirmation email for instant access',
                                   'Use will call so guests show ID at the door and cannot resell free '
                                   'tickets',
                                   'PromoTix ([IdHpcPxQTfU @ 00:33:28]); PromoTix ([IdHpcPxQTfU @ '
                                   '00:34:06])'],
                                  ['First move when the AXS app stops working',
                                   'Offload the app through iPhone Storage first, then update, then delete '
                                   'and reinstall it',
                                   'Confirm a stable Wi-Fi connection first, then update, offload, and '
                                   'reinstall as the last step',
                                   'TechTutorXpress ([edUbHihe2lI @ 00:00:19]); iKnow iOS ([zghU1cQya5k @ '
                                   '00:00:19])'],
                                  ['Running ticket price changes across the sales cycle',
                                   'Daisy chained tiers flip on sale automatically when the prior tier '
                                   'sells out or goes off sale',
                                   'Manual list price edits and mass edit inside the Logitix ticket group '
                                   'grid, then publish',
                                   'PromoTix ([IdHpcPxQTfU @ 00:07:47]); Logitix ([YaZpToURgBk @ '
                                   '00:04:17])'],
                                  ['Getting tickets into the back-office system at volume',
                                   'Single entry through an Add New Ticket form or a support portal '
                                   'submission form',
                                   'Data Importer wizard with saved column mapping templates, or a direct '
                                   'API integration',
                                   'Zippykind ([OaCa2-zmCe8 @ 00:00:00]); DigitalThinker Inc. '
                                   '([Y0_GSVWwMIw @ 00:01:29])'],
                                  ['Handling a support question before escalating it to a team',
                                   'Review the self-serve document details and return to dashboard without '
                                   'creating any ticket at all',
                                   'Log, assign, and document every request, then route by categories that '
                                   'mirror real work',
                                   'Supplier Digital Portal ([Db5sc_kyZFE @ 00:01:08]); NDSE ([N4lHcJFrT1E '
                                   '@ 00:00:37])']]}},
              {'section_number': 4,
               'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common firsthand failure is the AXS app itself dying before the '
                              'scan. TechTutorXpress runs a three-stage escalation on iPhone: Settings, '
                              'General, iPhone Storage, offload the app and tap reinstall; if that fails, '
                              'check the App Store for a pending update; and if the problem persists, '
                              'delete the app and reinstall it from the cloud icon, which they say usually '
                              'resolves it [edUbHihe2lI @ 00:00:37] [edUbHihe2lI @ 00:01:06]. iKnow iOS '
                              'diagnoses connectivity first, telling users to confirm a stable Wi-Fi '
                              'connection before touching the app, then updating, then offloading, which '
                              'they describe as clearing the cache and storage to remove unwanted bugs, '
                              'with uninstall and reinstall as the step that will definitely fix it '
                              '[zghU1cQya5k @ 00:01:16]. That connectivity warning sits awkwardly next to '
                              "Quick and Easy's claim that the ticket can be accessed even without "
                              "internet, a point they hedge with 'they say,' and they stress that while "
                              'you can buy on a computer, you need the mobile app to actually attend '
                              '[oQOmX8EOyW4 @ 00:01:19]. The operating lesson is to have the app updated, '
                              'signed in, and loading the QR code well before gates open, because every '
                              'fix on this list involves reinstalling, re-signing, and waiting on a '
                              'download at exactly the wrong moment.',
                              'Delivery and timing are where AXS workflows quietly stall. Simply Finance '
                              'reports that delivery methods are predetermined by the venue, covering '
                              'standard mail, will call, e-ticket, and most popularly AXS Mobile ID, and '
                              'that change requests can only be made through live chat with an agent from '
                              'the Help and Support Center, where a reply takes a while and you just have '
                              'to wait patiently [s7E1Yc3RoQc @ 00:00:19]. Missing tickets follow a '
                              'similarly slow path: sign in with the exact email used at purchase, verify '
                              'it if prompted, check My Event, wait a couple of hours after a recent '
                              'purchase, and only then contact the organizer or seller with a screenshot '
                              '[SnJa0jDKiKE @ 00:00:55]. Guide Gurus warns that AXS to SeatGeek transfers '
                              'can take time to complete, that recipients need sufficient time to claim '
                              'before the event, and that transfer fees vary by platform and event '
                              '[6Og6Y7NbLsk @ 00:01:33]. AidensGotGuides adds that some tickets only '
                              'become transferable or sellable closer to the event date, that resale can '
                              'be restricted by venue, organizer, or ticket type, and that prices and '
                              'availability change quickly on popular events [xEM0K5YLBZk @ 00:01:04]. '
                              'Each delay compounds: the window to fix delivery, finish a claim, or resell '
                              'can close before the problem is solved.',
                              'Inside the back office, the traps are small interface states that cost '
                              "money if missed. Logitix's Marty Carney points out that a grayed-out "
                              "marketplace icon means the mapping to that marketplace doesn't exist yet, "
                              'inventory only exports once activated with the blue check mark, and unsaved '
                              'price changes carry a red flag in the cell corner, with a warning if you '
                              'try to leave the page without publishing [YaZpToURgBk @ 00:04:40]. Brian '
                              "Jones's s-ticket box office shows orange seats that an online buyer is "
                              'choosing right now, which cannot be sold at the window until released, and '
                              'a refund cancels the booking, puts the seats straight back on sale, and '
                              'kills the old ticket at the door [4Ddm_7kF3nc @ 00:03:31]. Zippykind caps '
                              'each import file at 1,000 rows and holds new tickets off the dashboard map '
                              'and driver app for a minute or two while coordinates generate, with an '
                              'orange warning symbol flagging a pending fetch or a bad address that must '
                              "be refetched [OaCa2-zmCe8 @ 00:01:14]. NDSE's Michael Pfaff frames the "
                              'economics check: small IT interruptions quickly become workflow problems, '
                              'security concerns, and downtime risks, so repeat issues should trigger a '
                              'real review rather than another temporary fix that guarantees the same '
                              'ticket next week [N4lHcJFrT1E @ 00:01:29].'],
               'table': {'caption': 'Firsthand failure modes in AXS fulfillment and back-office ticketing, '
                                    'with the fixes practitioners teach',
                         'headers': ['Failure Mode',
                                     'What Breaks Or Was Warned',
                                     'Operator Fix Taught',
                                     'Expert Source'],
                         'rows': [['AXS app crashes or refuses to load tickets',
                                   'Ticket screen and QR code become unavailable right when the holder '
                                   'needs entry',
                                   'Offload through iPhone Storage, update in the App Store, then delete '
                                   'and reinstall',
                                   'TechTutorXpress ([edUbHihe2lI @ 00:00:37])'],
                                  ['Unstable connection makes the AXS app misbehave',
                                   'Connectivity problems are named as a likely root cause of the app not '
                                   'working',
                                   'Confirm a stable Wi-Fi connection first, then update the app to the '
                                   'latest version',
                                   'iKnow iOS ([zghU1cQya5k @ 00:00:00])'],
                                  ['Recently purchased tickets missing from the account',
                                   'Tickets do not appear in the purchase list or the My Event section',
                                   'Sign in with the purchase email, verify it, wait, then contact the '
                                   'seller with screenshots',
                                   'Simply Finance ([SnJa0jDKiKE @ 00:00:15])'],
                                  ['Wrong delivery method locked onto the order',
                                   'Delivery options are predetermined by the venue and cannot be '
                                   'self-edited in the app',
                                   'Open Help and Support Center, choose buying tickets, and request the '
                                   'change through live chat',
                                   'Simply Finance ([s7E1Yc3RoQc @ 00:00:19])'],
                                  ['Duplicate PDF ticket sold to multiple buyers',
                                   'Seller shows up early with the same copy and enters before the real '
                                   'buyer arrives',
                                   'Use the platform transfer feature so the old QR code is invalidated '
                                   'and reissued',
                                   'PromoTix ([IdHpcPxQTfU @ 00:22:35])'],
                                  ['Used ticket or shared screenshot presented at the door',
                                   'Scan shows red with the time it was used and which staff member '
                                   'admitted it',
                                   'Search the synced door list by name, seat, or receipt, and tap Undo on '
                                   'mistakes',
                                   'Brian Jones ([4Ddm_7kF3nc @ 00:04:44])'],
                                  ['Price edits never reach the marketplaces at all',
                                   'Unsaved changes sit flagged red and grayed marketplace icons mean no '
                                   'mapping exists yet',
                                   'Activate inventory with the blue check mark and publish before '
                                   'navigating away from the page',
                                   'Logitix ([YaZpToURgBk @ 00:04:40])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Sale and Pre-Event Fulfillment Gate',
                           'body': 'Run these four checks before committing AXS inventory to a buyer or a '
                                   'marketplace. Each one comes straight from a failure the practitioners '
                                   'hit or warned about: blocked cross-platform moves, locked delivery '
                                   'methods, duplicated barcodes, and edits that never went live.',
                           'items': ['Confirm the exit route before selling AXS seats to a '
                                     'Ticketmaster-bound buyer, because direct cross-platform transfers '
                                     'between AXS and Ticketmaster are generally not supported '
                                     '[AidensGotGuides — xEM0K5YLBZk @ 00:02:09].',
                                     'Lock the delivery method early, since it is predetermined by the '
                                     'venue and changes only happen through a live chat agent who takes a '
                                     'while to respond [Simply Finance — s7E1Yc3RoQc @ 00:00:19].',
                                     'Move tickets by platform transfer, never by emailed PDF, so the '
                                     'original QR code is canceled and a new one is issued to the new '
                                     'registered owner [PromoTix — IdHpcPxQTfU @ 00:22:09].',
                                     'Verify every marketplace icon is mapped and not grayed out, then '
                                     'publish all flagged edits before leaving the event detail page '
                                     '[Logitix — YaZpToURgBk @ 00:01:20].']}}],
 'pull_quote': '"Direct cross-platform transfers between AXS and Ticketmaster are generally not supported. '
               'So, your best option is to use a resale marketplace if available, or sell the AXS ticket '
               'and buy a replacement through Ticketmaster." — AidensGotGuides (xEM0K5YLBZk @ 00:02:09)',
 'diagram_id': 'diag-05',
 'action_checklist': ['Download the AXS mobile app, sign into the account that holds the tickets, tap the '
                      'tickets icon, and confirm the event QR code loads before event day [Quick and Easy '
                      '— oQOmX8EOyW4 @ 00:00:32].',
                      'If the AXS app fails, offload it under Settings, General, iPhone Storage, check the '
                      'App Store for updates, and delete and reinstall if it still breaks [TechTutorXpress '
                      '— edUbHihe2lI @ 00:00:19].',
                      "For SeatGeek buyers, collect the buyer's name and email, use the transfer button in "
                      'AXS My Account, and leave time for the recipient to claim with the emailed code '
                      '[Guide Gurus — 6Og6Y7NbLsk @ 00:00:21].',
                      "For Ticketmaster-only demand, check the AXS ticket's current market value, list it "
                      'on an open marketplace, and buy the replacement on Ticketmaster once it sells '
                      '[AidensGotGuides — xEM0K5YLBZk @ 00:01:38].',
                      'In Logitix One, activate inventory with the blue check mark, select marketplace '
                      'icons to broadcast, edit list prices in the ticket group grid, and publish [Logitix '
                      '— YaZpToURgBk @ 00:03:57].',
                      'On self-run events, cap total capacity with shared inventory, daisy chain price '
                      'tiers, and issue guest comps as will call to block resale [PromoTix — IdHpcPxQTfU @ '
                      '00:09:21].'],
 'statutory_citations': [{'title': 'AidensGotGuides — How to Transfer AXS Tickets to Ticketmaster '
                                   '[00:02:09]',
                          'url': 'https://www.youtube.com/watch?v=xEM0K5YLBZk&t=129s',
                          'relevance': 'Primary practitioner testimony on why AXS to Ticketmaster '
                                       'transfers fail and the sell-then-rebuy workaround.'},
                         {'title': 'Guide Gurus — How To Transfer Tickets From Axs To Seatgeek (2025) '
                                   '[00:00:21]',
                          'url': 'https://www.youtube.com/watch?v=6Og6Y7NbLsk&t=21s',
                          'relevance': 'Primary practitioner testimony on the AXS to SeatGeek '
                                       'transfer-and-claim workflow, timing, and fees.'},
                         {'title': 'Logitix — Logitix One - Event Detail Page [00:03:57]',
                          'url': 'https://www.youtube.com/watch?v=YaZpToURgBk&t=237s',
                          'relevance': 'Primary practitioner testimony on broker inventory activation, '
                                       'marketplace broadcasting, and grid repricing.'},
                         {'title': 'PromoTix — Create, Sell, and Manage Tickets for Any Event: Ticketing '
                                   'Demo || PromoTix [00:21:49]',
                          'url': 'https://www.youtube.com/watch?v=IdHpcPxQTfU&t=1309s',
                          'relevance': 'Primary practitioner testimony on QR-invalidating transfers, PDF '
                                       'resale fraud, and will-call guest controls.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'Y0_GSVWwMIw',
                       'title': 'Learn how to submit Support Tickets & Navigate the DTI portal!',
                       'channel': 'DigitalThinker Inc.',
                       'author': 'DigitalThinker Inc.',
                       'text': 'Now category is important because it determines how your ticket is routed '
                               'to what departments at Digital Thinker.',
                       'tip': 'Now category is important because it determines how your ticket is routed '
                              'to what departments at Digital Thinker.',
                       'timestamp': 117,
                       'timestamp_seconds': 117,
                       'timestamp_label': '[00:01:57]',
                       'url': 'https://www.youtube.com/watch?v=Y0_GSVWwMIw&t=117s',
                       'markdown': '[00:01:57](https://www.youtube.com/watch?v=Y0_GSVWwMIw&t=117s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IdHpcPxQTfU',
                       'title': 'Create, Sell, and Manage Tickets for Any Event: Ticketing Demo || '
                                'PromoTix',
                       'channel': 'PromoTix',
                       'author': 'PromoTix',
                       'text': 'What happens there is the original QR code is canceled and then a new QR '
                               'code is generated and issued to the new registered owner.',
                       'tip': 'What happens there is the original QR code is canceled and then a new QR '
                              'code is generated and issued to the new registered owner.',
                       'timestamp': 1309,
                       'timestamp_seconds': 1309,
                       'timestamp_label': '[00:21:49]',
                       'url': 'https://www.youtube.com/watch?v=IdHpcPxQTfU&t=1309s',
                       'markdown': '[00:21:49](https://www.youtube.com/watch?v=IdHpcPxQTfU&t=1309s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IdHpcPxQTfU',
                       'title': 'Create, Sell, and Manage Tickets for Any Event: Ticketing Demo || '
                                'PromoTix',
                       'channel': 'PromoTix',
                       'author': 'PromoTix',
                       'text': "So they'll have to show up and show their ID or some other form of "
                               'identification for you, event organizer to check their tickets in '
                               'manually.',
                       'tip': "So they'll have to show up and show their ID or some other form of "
                              'identification for you, event organizer to check their tickets in manually.',
                       'timestamp': 2027,
                       'timestamp_seconds': 2027,
                       'timestamp_label': '[00:33:47]',
                       'url': 'https://www.youtube.com/watch?v=IdHpcPxQTfU&t=2027s',
                       'markdown': '[00:33:47](https://www.youtube.com/watch?v=IdHpcPxQTfU&t=2027s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YaZpToURgBk',
                       'title': 'Logitix One - Event Detail Page',
                       'channel': 'Logitix',
                       'author': 'Logitix',
                       'text': "If a marketplace icon is grayed out it means the mapping doesn't exist "
                               'yet.',
                       'tip': "If a marketplace icon is grayed out it means the mapping doesn't exist yet.",
                       'timestamp': 80,
                       'timestamp_seconds': 80,
                       'timestamp_label': '[00:01:20]',
                       'url': 'https://www.youtube.com/watch?v=YaZpToURgBk&t=80s',
                       'markdown': '[00:01:20](https://www.youtube.com/watch?v=YaZpToURgBk&t=80s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Db5sc_kyZFE',
                       'title': 'Ticket Creation',
                       'channel': 'Supplier Digital Portal',
                       'author': 'Supplier Digital Portal',
                       'text': 'Select the back to dashboard option. This will allow you to access the '
                               'relevant details without creating a ticket.',
                       'tip': 'Select the back to dashboard option. This will allow you to access the '
                              'relevant details without creating a ticket.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=Db5sc_kyZFE&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=Db5sc_kyZFE&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'edUbHihe2lI',
                       'title': 'AXS Tickets App Not Working: How to FIX AXS Tickets App Not Working '
                                '(FIXED)',
                       'channel': 'TechTutorXpress',
                       'author': 'TechTutorXpress',
                       'text': 'However, if you continue to encounter this issue, then you will need to '
                               'completely reinstall the app, which usually resolves the problem.',
                       'tip': 'However, if you continue to encounter this issue, then you will need to '
                              'completely reinstall the app, which usually resolves the problem.',
                       'timestamp': 66,
                       'timestamp_seconds': 66,
                       'timestamp_label': '[00:01:06]',
                       'url': 'https://www.youtube.com/watch?v=edUbHihe2lI&t=66s',
                       'markdown': '[00:01:06](https://www.youtube.com/watch?v=edUbHihe2lI&t=66s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oQOmX8EOyW4',
                       'title': 'How To Use AXS Tickets (Quick and Easy!)',
                       'channel': 'Quick and Easy',
                       'author': 'Quick and Easy',
                       'text': 'You will need to download the mobile app in order to attend.',
                       'tip': 'You will need to download the mobile app in order to attend.',
                       'timestamp': 16,
                       'timestamp_seconds': 16,
                       'timestamp_label': '[00:00:16]',
                       'url': 'https://www.youtube.com/watch?v=oQOmX8EOyW4&t=16s',
                       'markdown': '[00:00:16](https://www.youtube.com/watch?v=oQOmX8EOyW4&t=16s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RDQeHkadlqk',
                       'title': 'how to buy tickets on axs !! How to use axs tickets app',
                       'channel': 'Web Mind',
                       'author': 'Web Mind',
                       'text': 'After booking, your ticket will be shown to you digitally. It will be '
                               'shown on your mobile.',
                       'tip': 'After booking, your ticket will be shown to you digitally. It will be shown '
                              'on your mobile.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=RDQeHkadlqk&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=RDQeHkadlqk&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SnJa0jDKiKE',
                       'title': "What Should I Do If I Can't Find My Tickets In The Axs App !",
                       'channel': 'Simply Finance',
                       'author': 'Simply Finance',
                       'text': 'You can go and directly contact the organizer or the seller who has '
                               'actually sold the ticket and state the issue and send them some sort of '
                               'screenshot.',
                       'tip': 'You can go and directly contact the organizer or the seller who has '
                              'actually sold the ticket and state the issue and send them some sort of '
                              'screenshot.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=SnJa0jDKiKE&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=SnJa0jDKiKE&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zghU1cQya5k',
                       'title': 'AXS App Not Working: How to Fix AXS Tickets App Not Working',
                       'channel': 'iKnow iOS',
                       'author': 'iKnow iOS',
                       'text': 'The issue might arise due to the connectivity issue, in that case you have '
                               'to check whether your internet connection is stable or not.',
                       'tip': 'The issue might arise due to the connectivity issue, in that case you have '
                              'to check whether your internet connection is stable or not.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=zghU1cQya5k&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=zghU1cQya5k&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 's7E1Yc3RoQc',
                       'title': 'Can I Change The Delivery Method Of My Tickets In The Axs App !',
                       'channel': 'Simply Finance',
                       'author': 'Simply Finance',
                       'text': 'Request for delivery method changes can only be made by using the live '
                               'chat to connect with an agent.',
                       'tip': 'Request for delivery method changes can only be made by using the live chat '
                              'to connect with an agent.',
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=s7E1Yc3RoQc&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=s7E1Yc3RoQc&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6Og6Y7NbLsk',
                       'title': 'How To Transfer Tickets From Axs To Seatgeek (2025)',
                       'channel': 'Guide Gurus',
                       'author': 'Guide Gurus',
                       'text': 'It is crucial to note that the transfer process may take some time to '
                               'complete and it is essential to allow sufficient time for the recipient to '
                               'claim their tickets before the event.',
                       'tip': 'It is crucial to note that the transfer process may take some time to '
                              'complete and it is essential to allow sufficient time for the recipient to '
                              'claim their tickets before the event.',
                       'timestamp': 93,
                       'timestamp_seconds': 93,
                       'timestamp_label': '[00:01:33]',
                       'url': 'https://www.youtube.com/watch?v=6Og6Y7NbLsk&t=93s',
                       'markdown': '[00:01:33](https://www.youtube.com/watch?v=6Og6Y7NbLsk&t=93s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'xEM0K5YLBZk',
                       'title': 'How to Transfer AXS Tickets to Ticketmaster',
                       'channel': 'AidensGotGuides',
                       'author': 'AidensGotGuides',
                       'text': 'Direct cross-platform transfers between AXS and Ticketmaster are generally '
                               'not supported.',
                       'tip': 'Direct cross-platform transfers between AXS and Ticketmaster are generally '
                              'not supported.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=xEM0K5YLBZk&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=xEM0K5YLBZk&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SqgRdPpIv_I',
                       'title': 'Ticket Repricing Overview',
                       'channel': 'Fastweigh',
                       'author': 'Fastweigh',
                       'text': 'Single ticket rate locks, this provides the ability to lock rates for '
                               'individual tickets preventing further changes.',
                       'tip': 'Single ticket rate locks, this provides the ability to lock rates for '
                              'individual tickets preventing further changes.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=SqgRdPpIv_I&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=SqgRdPpIv_I&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4Ddm_7kF3nc',
                       'title': 's-ticket for staff: box office, parking, refunds and door check-in '
                                '(5-minute guide)',
                       'channel': 'Brian Jones',
                       'author': 'Brian Jones',
                       'text': 'If a ticket has already been used, or someone shares a screenshot of it, '
                               'it shows red, with the time it was used and who let them in.',
                       'tip': 'If a ticket has already been used, or someone shares a screenshot of it, it '
                              'shows red, with the time it was used and who let them in.',
                       'timestamp': 266,
                       'timestamp_seconds': 266,
                       'timestamp_label': '[00:04:26]',
                       'url': 'https://www.youtube.com/watch?v=4Ddm_7kF3nc&t=266s',
                       'markdown': '[00:04:26](https://www.youtube.com/watch?v=4Ddm_7kF3nc&t=266s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'N4lHcJFrT1E',
                       'title': 'IT Helpdesk Best Practices That Reduce Tickets And Keep Work Moving',
                       'channel': 'NDSE',
                       'author': 'NDSE',
                       'text': 'Repeat issues should trigger review, not another temporary fix.',
                       'tip': 'Repeat issues should trigger review, not another temporary fix.',
                       'timestamp': 89,
                       'timestamp_seconds': 89,
                       'timestamp_label': '[00:01:29]',
                       'url': 'https://www.youtube.com/watch?v=N4lHcJFrT1E&t=89s',
                       'markdown': '[00:01:29](https://www.youtube.com/watch?v=N4lHcJFrT1E&t=89s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OaCa2-zmCe8',
                       'title': 'Bulk Import Delivery Orders From a Spreadsheet | Zippykind',
                       'channel': 'Zippykind',
                       'author': 'Zippykind',
                       'text': 'Each file can hold up to 1,000 rows.',
                       'tip': 'Each file can hold up to 1,000 rows.',
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=OaCa2-zmCe8&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=OaCa2-zmCe8&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
