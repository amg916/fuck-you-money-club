from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'returns-refunds-chargebacks-dropshipping-playbook',
 'question_prompt': 'How do I set up and process returns, refunds, exchanges, and chargebacks without '
                    'losing money, especially when dropshipping?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Returns, Refunds, and Chargebacks',
 'subtitle': 'Shopify self-serve returns and exchanges, Loop Returns and AI return apps, the pre-order '
             'integration, dropshipping return policies and supplier realities, chargeback prevention and '
             'disputes, and product-injury claim exposure',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners treat returns as a budgeted line item, not an emergency. The '
                      'consensus: publish a plain-language return policy before the first sale (30 days is '
                      'the common window), ship only with tracking, reply to every customer fast, and '
                      'refund-and-let-keep on cheap overseas goods where reverse shipping costs more than '
                      'the item. Dropshipping Deep Dive puts online returns near 19.3%, apparel at 20 to '
                      "40%, a $15 Shopify Payments chargeback fee, and CJ's three-day damage-dispute "
                      'window, then builds a per-order reserve around those figures. Shopify Mastery '
                      'refunds without a return under $20 and prices in a 3 to 5% buffer. Operators split '
                      'on deflection versus generosity: Flying Start Online makes refund-seekers ship to a '
                      'virtual US address, while others push partial refunds, exchanges, store credit, or '
                      'instant make-it-right resolutions.',
 'key_metrics': [{'label': 'Online Return Rate Benchmark',
                  'metric': 'Online Return Rate Benchmark',
                  'value': 'About 19.3% of online sales (apparel online commonly 20 to 40%)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Roughly one in five online orders comes back in some form; apparel stores '
                             'are told to plan on the apparel band, not the average.',
                  'source': 'Dropshipping Deep Dive ([1L4TNDjsICQ @ 00:02:33])'},
                 {'label': 'Shopify Payments Chargeback Fee',
                  'metric': 'Shopify Payments Chargeback Fee',
                  'value': '$15 per chargeback, plus the disputed amount pulled from the next payout',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Evidence window typically 7 to 21 days; amount and fee return only if the '
                             'seller wins the dispute.',
                  'source': 'Dropshipping Deep Dive ([1L4TNDjsICQ @ 00:08:13])'},
                 {'label': 'CJ Damage Dispute Window',
                  'metric': 'CJ Damage Dispute Window',
                  'value': '3 days from customer receipt (7 days for electronics)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Miss the window and the seller holds the entire cost of a damaged item '
                             'instead of sharing it with the supplier.',
                  'source': 'Dropshipping Deep Dive ([1L4TNDjsICQ @ 00:13:07])'},
                 {'label': 'Refund-Without-Return Threshold',
                  'metric': 'Refund-Without-Return Threshold',
                  'value': 'Items under $20: almost always refund without requiring a return',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Return friction is not justified at low item values; issue the refund, mark '
                             'it resolved, and move on.',
                  'source': 'Shopify Mastery ([EjZsqaOIDsc @ 00:04:21])'}],
 'sections': [{'number': 1,
               'title': 'The Practitioner Consensus: Returns Are a Line Item, Not a Surprise',
               'paragraphs': ['Every operator on this beat agrees the return policy gets written before '
                              'the first sale, not improvised after the first angry email. Eric Hunley '
                              'Tucker of Shopify Mastery sets a 30-day window as the sweet spot, warns '
                              'that anything under 14 days triggers distrust, and notes that Shopify '
                              'auto-links the saved refund policy into the footer, which is exactly what '
                              'Shopify Payments, Stripe, and PayPal look at when a dispute lands '
                              '[EjZsqaOIDsc @ 00:02:02]. Manizha & Ryan hit the same footer point from the '
                              'entitlement angle: without a strong posted policy, customers who spot a '
                              'small business are prone to milking it, so the terms must sit visibly in '
                              'the footer where nobody can claim they never saw them [B2xFNVqbu7c @ '
                              '00:07:09]. Flying Start Online treats the shipping and refund policies as '
                              'the two most important pages on the store, because a crystal-clear return '
                              'path quietly suppresses refund requests while still letting the operator '
                              'advertise a 30-day guarantee on product pages for better conversions '
                              '[rhATJAycfEU @ 00:15:44]. The Dropshipping Deep Dive hosts add the hard '
                              'constraint: the policy has to describe the process you will actually '
                              'follow, because a page promising returns to an overseas warehouse that '
                              'takes three months is a policy you cannot honorably run, and banks deciding '
                              'chargebacks can smell it [1L4TNDjsICQ @ 00:16:21].',
                              'The second consensus point is proof of delivery plus response speed, which '
                              'every chargeback-focused speaker treats as one weapon. Dean Alma learned it '
                              'selling on eBay, eating losses when buyers claimed non-receipt with no way '
                              'to prove otherwise, and now insists on tracked shipping even at greater '
                              'cost, because a signature-backed delivery scan stops dishonest '
                              'never-arrived claims cold [GYROU1C9Mks @ 00:00:51]. ZIK Analytics makes the '
                              'same call: a tracking number visible to both the buyer and the payment '
                              'provider makes it much harder for a customer to win a non-receipt '
                              'chargeback, and AliExpress tracking numbers are easy to follow on 17track '
                              "or the carrier's own site [7GY4PPBU0GY @ 00:03:54]. Flying Start Online "
                              'pins the trigger for most refunds and chargebacks on silence: a customer '
                              'who gets no reply for four days goes to PayPal, while a five-second reply '
                              'tells them someone is on the other end even when the shipment is taking a '
                              'month [rhATJAycfEU @ 00:17:49]. Dropshipping Deep Dive puts a price on that '
                              'delay, calling a fast, easy refund offered before the customer ever calls '
                              'their bank the cheapest chargeback strategy in the world, since $15 buys a '
                              'lot of promptness and speed is a financial strategy, not just good manners '
                              '[1L4TNDjsICQ @ 00:09:15].',
                              'The third point of agreement is that for cheap dropshipped goods, '
                              'physically recovering the item is usually a money-loser, so the '
                              'refund-or-reship-and-keep play wins. Shopify Mastery runs the math on a $12 '
                              'item where shipping back to China could cost $20 or more, shows that a $10 '
                              'product with a $6 return label recovers only $4 of value while annoying the '
                              'customer, and sets a hard rule: anything under $20 almost always gets '
                              'refunded without a return, marked resolved, and closed [EjZsqaOIDsc @ '
                              '00:04:21]. Dropshipping Deep Dive pushes the line higher, arguing that for '
                              'most overseas-sourced items under roughly $30 or $40 the recovery cost sits '
                              'near the recoverable value, and that asking a customer to pay $14 to ship '
                              'back a $25 item is friction that breeds one-star reviews and chargeback '
                              'risk [1L4TNDjsICQ @ 00:25:56]. Dean Alma applies the same logic to defects: '
                              'have the supplier ship a free replacement, tell the customer to keep the '
                              'faulty unit, but demand pictures as proof first so the damage claim holds '
                              'up with the supplier [GYROU1C9Mks @ 00:00:11]. ZIK Analytics confirms the '
                              'supplier side behaves the same way, reporting that AliExpress sellers on '
                              'cheap products will in most cases refund without needing the product '
                              'returned at all [7GY4PPBU0GY @ 00:08:23].'],
               'table': {'caption': 'Consensus rules multiple operators run on every store before returns '
                                    'start landing',
                         'headers': ['Consensus Principle',
                                     'What the Operator Actually Does',
                                     'Why It Pays Off',
                                     'Expert Source'],
                         'rows': [['Written return policy live before the first sale',
                                   'Sets a 30-day window, requires original condition, adds a 72-hour '
                                   'photo rule for damage',
                                   'Anything under 14 days triggers distrust; a published policy is '
                                   'first-line chargeback defense',
                                   'Shopify Mastery ([EjZsqaOIDsc @ 00:02:02])'],
                                  ['Policies visible in the store footer at all times',
                                   'Lists refund and return policies in the footer of every page on the '
                                   'storefront',
                                   'Customers can never claim they had no access to the terms they '
                                   'accepted',
                                   'Tutorials by Manizha & Ryan ([B2xFNVqbu7c @ 00:07:25])'],
                                  ['Pay for tracked shipping even at greater cost',
                                   'Uses tracked, signature-backed delivery so the carrier system logs the '
                                   'receipt',
                                   'Dishonest buyers claiming non-receipt cannot subvert the logged '
                                   'delivery proof',
                                   'Dean Alma ([GYROU1C9Mks @ 00:00:51])'],
                                  ['Tracking number shared with buyer and payment provider',
                                   'Adds the tracking number to the Shopify order so both parties can '
                                   'follow the parcel',
                                   'Non-receipt chargebacks become much harder for the customer to win',
                                   'ZIK Analytics ([7GY4PPBU0GY @ 00:03:54])'],
                                  ['Reply to every email, comment, and Facebook message',
                                   'Answers all channels, sending tracking IDs to anyone frustrated about '
                                   'shipping times',
                                   'Unanswered customers escalate to PayPal refunds or bank chargebacks '
                                   'within days',
                                   'Flying Start Online ([rhATJAycfEU @ 00:08:42])'],
                                  ['Refund without requiring a return on low-value items',
                                   'Issues the refund on anything under $20 and closes the case in one '
                                   'message',
                                   'Return shipping often exceeds item value, so recovery would lose more '
                                   'money',
                                   'Shopify Mastery ([EjZsqaOIDsc @ 00:04:21])'],
                                  ['Nudge exchanges and store credit ahead of cash refunds',
                                   'Runs Loop Returns to steer customers into swapping items or taking '
                                   'store credit',
                                   'Keeps revenue inside the store instead of issuing a full refund every '
                                   'time',
                                   'PreProduct ([ZXDpWj-RfOQ @ 00:00:21])']]}},
              {'number': 2,
               'title': 'Exact Street Mechanics, Tools and Numbers',
               'paragraphs': ['Dropshipping Deep Dive brings the hardest return math. The hosts cite about '
                              '19.3% of online sales coming back, apparel running 20 to 40% online, and '
                              'fit and sizing driving about half of apparel returns [1L4TNDjsICQ @ '
                              '00:03:09]. Their worked order: a $40 sale, $18 landed cost, roughly $1.46 '
                              'in card fees at 2.9% plus 30 cents. On a refund-and-keep the card fee never '
                              'comes back and the ad spend that bought the order is sunk, so an order that '
                              'looked like $10 of contribution can end up $30 to $40 underwater '
                              '[1L4TNDjsICQ @ 00:07:02]. Their expected-cost model: one in five orders '
                              'returning at about $30 all-in means roughly $6 of return cost riding on '
                              'every shipped order, a very large bite out of a $14 contribution '
                              '[1L4TNDjsICQ @ 00:07:19]. A lost chargeback stacks worse: the $40, the $15 '
                              'fee, the $18 landed cost, and the ad spend, with the product long gone. '
                              'Shopify Mastery runs a lighter model, assuming a 3 to 5% return rate for '
                              'general merchandise dropshipping and adding 3 to 5% onto the target cost '
                              'when setting the selling price, so returns become a known cost already '
                              'baked into the price instead of a surprise eating unplanned profit '
                              '[EjZsqaOIDsc @ 00:09:08].',
                              'The supplier side runs on short clocks. Dropshipping Deep Dive reports that '
                              "under CJ's published dispute policy a damage dispute on an ordinary product "
                              'should be opened within three days of the customer receiving it, seven for '
                              'electronics, while lost-in-transit refunds or resends only kick in around '
                              '45 days for the United States and 60 days for much of the rest of the '
                              "world; the gap between that clock and the customer's is the seller's float "
                              '[1L4TNDjsICQ @ 00:13:07]. That is why their first reply demands all three '
                              'photos in one message: the damaged item, the packaging, and the shipping '
                              'label [1L4TNDjsICQ @ 00:13:42]. ZIK Analytics walks the AliExpress route: '
                              'My Orders, open dispute, select return goods, enter delivery status, '
                              'reason, refund or replacement, a refund amount equal to what was paid, plus '
                              'photos or video collected from the Shopify buyer. The seller has 5 days to '
                              'respond, a free return label follows approval, refusals escalate to '
                              'AliExpress, and refunds typically land within 10 business days [7GY4PPBU0GY '
                              '@ 00:08:04]. For US retail suppliers, ZIK starts an Amazon return, '
                              'screenshots the QR code, and sends it to the buyer, who drops the package '
                              'at UPS for free [7GY4PPBU0GY @ 00:09:36].',
                              "When a dispute lands, Flying Start Online's evidence packet is four or five "
                              'screenshots: exported Shopify order information, the AliExpress order page '
                              "with tracking, the tracking result from the carrier's site, the PayPal or "
                              'Stripe transaction, and any customer email transcripts. It takes 10 to 15 '
                              'minutes per chargeback, with one or two a month expected at hundreds of '
                              'units [rhATJAycfEU @ 00:13:15]. Dropshipping Deep Dive frames the stakes: '
                              'Shopify Payments in the US pulls the disputed amount from the next payout '
                              'plus a $15 fee, typically allows 7 to 21 days to submit evidence, and '
                              'providers start restricting accounts as the chargeback rate climbs toward '
                              '1% of transactions [1L4TNDjsICQ @ 00:08:34]. Anatoliy Labinskiy layers '
                              'front-end deterrents: custom text in the thank-you email flagging holiday '
                              'or stock delays, an app that pushes shipping numbers to payment providers '
                              'to avoid holds, and a virtual phone number whose voicemail, recorded for a '
                              'couple of bucks by an American-accented voice, tells callers all agents are '
                              'busy and routes them to email [XED26wvEepA @ 00:01:12]. Flying Start Online '
                              'automates first contact with a free Chatfuel bot on the Facebook page that '
                              'replies instantly and points people to the support address [rhATJAycfEU @ '
                              '00:20:26].'],
               'table': {'caption': 'Return tools, settings, and numbers operators actually configure and '
                                    'run',
                         'headers': ['Tool or Lever',
                                     'Exact Mechanic or Number',
                                     'Operator Use Case',
                                     'Expert Source'],
                         'rows': [['Shopify return rules under Settings and Policies',
                                   'Return window, who pays return shipping, optional 1% or 2% restocking '
                                   'fee, final sale items',
                                   'Locks default rules so the written policy reflects the same terms '
                                   'automatically',
                                   'Tutorials by Manizha & Ryan ([B2xFNVqbu7c @ 00:01:59])'],
                                  ['Shopify self-serve returns for customer accounts',
                                   'Requires new customer accounts and a fulfilled order; merchant '
                                   'approves or declines each line',
                                   'Lets customers request returns from their account while the merchant '
                                   'controls approval',
                                   'Sunrise Integration ([daoVeRnScfo @ 00:06:15])'],
                                  ['Loop Returns exchange-first returns portal',
                                   'Instant product or size swaps without waiting on the return, branded '
                                   'portal, automated labels',
                                   'Fits medium to large stores; smaller stores may find the cost higher '
                                   'than simpler options',
                                   'Wise Explainer ([X3G7DDq6KD8 @ 00:01:36])'],
                                  ['Return Dot Ai approval and refund routing',
                                   'Compares logistics rates, auto-generates AWB and label, refunds via '
                                   'gift card, credit, codes, or original method',
                                   'Automates approvals and picks the cheapest or fastest courier per '
                                   'return',
                                   'Returndotai ([JzyBmddGOms @ 00:01:17])'],
                                  ['Shopify native exchange workflow inside Return',
                                   'Add products under exchange items, pick the exact variant, then review '
                                   'the payment difference',
                                   'Handles size or color swaps while collecting or refunding any price '
                                   'difference',
                                   "Jim's Ecommerce Tutorials ([HPTGnp51Iks @ 00:01:52])"],
                                  ['Store credit as the default refund method',
                                   'Choose store credit instead of the original payment method when '
                                   'configuring the refund',
                                   'Usually much faster to process than pushing money back to the customer',
                                   'Tutorial Stack ([YnEcCYA-UDs @ 00:02:51])'],
                                  ['Per-order returns reserve pot moved weekly',
                                   '100 orders at $40 with a $20 blended loss per return equals $400, '
                                   'about $4 per order',
                                   'Refunds come out of a dedicated pot instead of rent money or next '
                                   "week's ad budget",
                                   'Dropshipping Deep Dive ([1L4TNDjsICQ @ 00:31:04])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Street-Level Plays Operators Use to Shrink the Refund Bill',
                           'body': 'Four tactics practitioners run to cut refund payouts, keep revenue '
                                   'inside the store, and catch problems before they become chargebacks.',
                           'items': ['Answer refund demands with a template: the order is on its way, and '
                                     'once it arrives ship it to a virtual US address (about 10 bucks a '
                                     'month) for an instant refund; of 10 who ask, only a couple actually '
                                     'ship it back [Flying Start Online — rhATJAycfEU @ 00:11:03]',
                                     'Offer 50% back with no shipping required on higher-value items the '
                                     'supplier will not take; most customers prefer some money now over '
                                     'packaging and a post office trip [Shopify Mastery — EjZsqaOIDsc @ '
                                     '00:07:07]',
                                     'Tick continue selling when out of stock so Loop lets customers swap '
                                     'into a pre-order size, then let PreProduct place a fulfillment hold '
                                     'so the 3PL does not ship stock that does not exist yet [PreProduct — '
                                     'ZXDpWj-RfOQ @ 00:01:41]',
                                     'After delivery, send a feedback email offering 10, 20, sometimes 30% '
                                     'off the next purchase to surface what went wrong before it turns '
                                     'into a chargeback and to win repeat buyers [Anatoliy Labinskiy | '
                                     'E-com business encyclopedia — XED26wvEepA @ 00:05:10]']},
               'sop_steps': [{'step': 1,
                              'title': 'Configure policy and return rules',
                              'action': 'Open Settings, Policies, and Return rules; set the window, return '
                                        'shipping cost, restocking fee, and final sale list, then generate '
                                        'and edit the written policy.',
                              'detail': 'Self-serve returns require the new customer accounts setting, and '
                                        'the written policy must match the rules just saved since the '
                                        'template text is only an example [Sunrise Integration — '
                                        'daoVeRnScfo @ 00:01:59]'},
                             {'step': 2,
                              'title': 'Fulfill every order with tracking',
                              'action': 'Enter the supplier tracking number in Shopify and mark the order '
                                        'fulfilled so the shipping update email fires automatically.',
                              'detail': 'Shopify only sends the tracking email once the order is marked '
                                        'fulfilled with the AliExpress tracking code entered [Flying Start '
                                        'Online — rhATJAycfEU @ 00:23:11]'},
                             {'step': 3,
                              'title': 'Triage same day and collect evidence',
                              'action': 'Reply the same day, classify the case as fault, delivery, or '
                                        'preference, and request order number, reason, and three damage '
                                        'photos in one message.',
                              'detail': 'Fault and delivery cases get refund or resend with the supplier '
                                        'dispute opened the same day; preference cases run the ladder of '
                                        'information, exchange, store credit, then refund [Dropshipping '
                                        'Deep Dive — 1L4TNDjsICQ @ 00:24:07]'},
                             {'step': 4,
                              'title': 'Process the refund in Shopify admin',
                              'action': 'Open the order, click Refund, enter line-item quantities, decide '
                                        'on refunding shipping, and uncheck restock when no inventory is '
                                        'coming back.',
                              'detail': 'Refund shipping on defects or errors but not on change-of-mind; '
                                        'card refunds take 5 to 10 business days and PayPal usually 3 to 5 '
                                        '[Shopify Mastery — EjZsqaOIDsc @ 00:06:12]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first fault line is how many returns an operator should even budget '
                              'for. Flying Start Online, running the Common Panda store, tells '
                              'physical-product sellers to expect refunds under five percent, says that '
                              'sitting at five percent means you are doing something wrong, pushes the '
                              'real target under one percent, and reports not a single refund request '
                              'after more than 250 units, with chargebacks aimed below 0.01% [rhATJAycfEU '
                              '@ 00:05:22]. Shopify Mastery lands in the middle, pegging a typical '
                              'general-merchandise dropshipping return rate at 3 to 5% and telling sellers '
                              'to add that same 3 to 5% onto target cost as a built-in buffer [EjZsqaOIDsc '
                              '@ 00:09:08]. Dropshipping Deep Dive throws both numbers out for '
                              'apparel-heavy stores, quoting the National Retail Federation and Happy '
                              'Returns figure of about 19.3% of online sales coming back, apparel online '
                              'at 20 to 40%, footwear from the high teens to around 30%, and fit driving '
                              'roughly half of apparel returns [1L4TNDjsICQ @ 00:02:33] [1L4TNDjsICQ @ '
                              '00:03:09]. The operator read: a gadget store with tight listings can '
                              'plausibly live near the Flying Start number, but a clothing store priced '
                              "for one percent returns is priced for a fantasy, and Deep Dive's 20% "
                              'apparel planning assumption is the safer seed until real data exists.',
                              'The sharpest split is whether the physical item should ever come back. '
                              'Flying Start Online runs a friction play: confirm the order is on its way, '
                              'then tell any refund-seeker to ship the product to a virtual US mailing '
                              'address that costs about $10 a month, using a copy-paste template; after '
                              'talking with other Shopify sellers, the claim is that of ten people who '
                              'ask, only about two actually mail it back [rhATJAycfEU @ 00:10:16]. Dean '
                              'Alma also wants non-defective returns sent to a personal address with the '
                              'buyer paying shipping, refunds the item minus shipping, then recycles the '
                              "unit for better product photos, promo samples, or the next customer's order "
                              '[GYROU1C9Mks @ 00:01:14]. Dropshipping Deep Dive argues the opposite for '
                              'cheap overseas goods: when recovery cost sits anywhere near recoverable '
                              'value, which they say covers most items under about $30 or $40, '
                              'refund-and-keep wins, and charging a customer $14 to ship back a $25 item '
                              'is friction that breeds one-star reviews and chargeback risk [1L4TNDjsICQ @ '
                              '00:25:39]. Shopify Mastery draws the line lower, telling sellers to almost '
                              'always refund without a return on anything under $20 and to reserve prepaid '
                              'labels through USPS or Pirate Ship for higher-value items where the math '
                              'holds [EjZsqaOIDsc @ 00:04:21].',
                              'Refund currency and returns tooling split the room just as hard. Tutorials '
                              'by Manizha & Ryan run a policy with no cash refunds, only store credit '
                              "added to the customer's account, and argue that for a small shop a mailed "
                              'return request beats an always-open self-serve button that makes customers '
                              'feel returns are permanently on the table [B2xFNVqbu7c @ 00:01:10]. '
                              'Tutorial Stack backs the credit lean on pure speed, saying it is usually '
                              'much faster to offer customers store credit than cash [YnEcCYA-UDs @ '
                              '00:02:51]. Dropshipping Deep Dive puts a hard limit on that play: credit '
                              'works where the policy allows it and the customer genuinely prefers it, and '
                              'some sellers add a small bonus because credit keeps the sale inside the '
                              'store, but credit should never be forced where a refund is owed on fault or '
                              'delivery cases [1L4TNDjsICQ @ 00:25:03]. On software, Wise Explainer '
                              "pitches Loop Returns' exchange-first portal, automated labels, and returns "
                              'analytics, yet concedes it fits medium to large-scale stores and that '
                              'smaller stores may find the cost higher than simpler solutions, though in '
                              'its verdict the time savings, automation, and professional customer '
                              'experience often justify the investment [X3G7DDq6KD8 @ 00:01:21].'],
               'table': {'caption': 'Competing returns playbooks: who argues what, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How many returns and refunds to budget for',
                                   'Under 5% refunds on physical products, real target under 1%, '
                                   'chargebacks below 0.01%',
                                   'Plan on the 19.3% online average and 20 to 40% for apparel',
                                   'Flying Start Online ([rhATJAycfEU @ 00:05:22]); Dropshipping Deep Dive '
                                   '([1L4TNDjsICQ @ 00:02:33])'],
                                  ['Whether to make the customer send the item back',
                                   'Require shipment to a virtual US address; only about two of ten ever '
                                   'send it',
                                   'Refund and let the customer keep anything under $20 without a return',
                                   'Flying Start Online ([rhATJAycfEU @ 00:11:03]); Shopify Mastery '
                                   '([EjZsqaOIDsc @ 00:04:21])'],
                                  ['Who pays for the return shipping leg',
                                   'Buyer ships to a personal address, refund item minus shipping, reuse '
                                   'unit for photos',
                                   'Prepaid label via 3PL, AliExpress dispute, or Amazon QR code for a '
                                   'smoother experience',
                                   'Dean Alma ([GYROU1C9Mks @ 00:01:14]); ZIK Analytics ([7GY4PPBU0GY @ '
                                   '00:06:15])'],
                                  ['What currency the refund lands in',
                                   'Store credit only with no cash refunds, and credit is faster to '
                                   'process',
                                   'Credit only when the customer prefers it, never forced where a refund '
                                   'is owed',
                                   'Tutorials by Manizha & Ryan ([B2xFNVqbu7c @ 00:01:10]); Dropshipping '
                                   'Deep Dive ([1L4TNDjsICQ @ 00:25:03])'],
                                  ['How customers submit a return request',
                                   'Mail-in requests for small shops so returns never feel permanently '
                                   'open',
                                   'Shopify self-serve returns via new customer accounts with return rules '
                                   'and final-sale lists',
                                   'Tutorials by Manizha & Ryan ([B2xFNVqbu7c @ 00:05:30]); Sunrise '
                                   'Integration ([daoVeRnScfo @ 00:01:40])'],
                                  ['Which returns software tier to run',
                                   'Loop Returns exchange-first branded portal, best suited to medium and '
                                   'large-scale stores',
                                   'Return Dot Ai rule engine automatically applying the highest-priority '
                                   'policy per order',
                                   'Wise Explainer ([X3G7DDq6KD8 @ 00:01:21]); Returndotai ([JzyBmddGOms @ '
                                   '00:02:19])'],
                                  ['How to resolve a damaged or defective item',
                                   'Supplier ships a free replacement and customer keeps the faulty item '
                                   'after photo proof',
                                   'Photo within 72 hours of delivery, then full refund or replacement '
                                   'with no return',
                                   'Dean Alma ([GYROU1C9Mks @ 00:00:11]); Shopify Mastery ([EjZsqaOIDsc @ '
                                   '00:02:20])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The costliest firsthand failure belongs to Anatoliy Labinskiy's shoe store. "
                              'The first Oxford shoe looked shiny and premium in supplier pictures, tested '
                              'as a winner, and was scaled to about 50K a month before chargebacks piled '
                              'in because the shoe turned out to be plastic with no leather at all; the '
                              'verdict was blunt, pictures are always lying, and the experience cost a lot '
                              '[XED26wvEepA @ 00:03:36]. The fix taught afterward: read YouTube comments '
                              'and Amazon reviews before launch, then demand photo and video of the actual '
                              'unit from the supplier once a product wins, and drop any supplier that '
                              'refuses, because chargebacks freeze cash on PayPal, Stripe, and other '
                              'platforms [XED26wvEepA @ 00:04:39]. Dean Alma took losses on eBay from '
                              'buyers claiming non-delivery with no way to prove receipt, and tells '
                              'sellers to pay for tracked shipping even at higher cost so the carrier '
                              'record shuts down dishonest claims [GYROU1C9Mks @ 00:00:38]. ZIK Analytics '
                              'flags a different account killer: heavily regulated products like '
                              'hemp-based items or alcoholic beverages can get a store flagged or blocked '
                              "by its payment provider, so the provider's product policy and "
                              'destination-country rules get checked before listing [7GY4PPBU0GY @ '
                              '00:02:12].',
                              'The unit economics of a single bad order are uglier than most sellers '
                              'model. Dropshipping Deep Dive walks a $40 sale with $18 landed cost, about '
                              '$1.46 in card fees, and roughly $12 in ad spend: on a refund-and-keep, the '
                              'swing against the seller is roughly $70 versus where the order seemed to '
                              'stand, and the card fee never comes back [1L4TNDjsICQ @ 00:06:23]. A lost '
                              'Shopify Payments chargeback stacks a $15 fee on top, the disputed amount '
                              'leaves the next payout immediately, and providers start restricting '
                              'accounts as the chargeback rate climbs toward 1% of transactions '
                              '[1L4TNDjsICQ @ 00:08:13]. Supplier clocks compound it: CJ wants damage '
                              'disputes opened within three days of the customer receiving an ordinary '
                              'product and seven for electronics, so a customer who opens a parcel Friday '
                              'and reports Tuesday, with a dispute filed Wednesday, can leave the seller '
                              'holding the entire cost, while lost-parcel resolution only kicks in around '
                              '45 days for the US and 60 for much of the world [1L4TNDjsICQ @ 00:13:07]. '
                              'Shopify Mastery adds the reverse-logistics wall: AliExpress suppliers '
                              'generally refuse returns, and shipping a $12 item back to China can run $20 '
                              'or more, so the math simply does not work [EjZsqaOIDsc @ 00:00:55].',
                              'Most of the remaining losses are self-inflicted communication and setup '
                              'failures. Flying Start Online warns that a customer left unanswered for '
                              'four days goes to PayPal for a chargeback or refund, and that a five-second '
                              'reply proving a human is on the other end defuses most of it; a Facebook '
                              'commenter demanding an undelivered order turned out to have bought from '
                              "another vendor entirely, spotted because the store's order numbers all "
                              'start with #CP [rhATJAycfEU @ 00:17:49]. The same operator set a hard '
                              'Christmas cutoff of 27 November, the Cyber Monday date, flagged on every '
                              'winning product page, because three to four weeks of shipping makes angry '
                              'gift buyers certain otherwise [rhATJAycfEU @ 00:24:46]. Tutorials by '
                              'Manizha & Ryan hit a cash-on-delivery trap: Shopify refunds go back through '
                              'the original payment method, so a COD refund means collecting the '
                              "customer's bank details first and marking it refunded manually [B2xFNVqbu7c "
                              '@ 00:04:36]. PreProduct exposes an exchange trap: Loop will swap a customer '
                              "into an out-of-stock pre-order size whenever Shopify's continue-selling box "
                              'is ticked, so without a fulfillment hold the 3PL software tries to ship an '
                              'item that does not exist yet [ZXDpWj-RfOQ @ 00:01:23].'],
               'table': {'caption': 'Firsthand failure modes, the damage they caused, and the fix taught',
                         'headers': ['Failure Mode', 'Firsthand Damage', 'Fix Taught', 'Expert Source'],
                         'rows': [['Scaling a product without checking real quality',
                                   'Plastic Oxford shoes scaled to 50K monthly triggered a wave of '
                                   'chargebacks',
                                   'Read YouTube and Amazon reviews, then demand supplier photo and video',
                                   'Anatoliy Labinskiy | E-com business encyclopedia ([XED26wvEepA @ '
                                   '00:03:53])'],
                                  ['Shipping cheap orders without any tracking',
                                   'eBay forced refunds on non-delivery claims with no proof of receipt',
                                   'Pay for tracked shipping even at greater cost to block dishonest '
                                   'claims',
                                   'Dean Alma ([GYROU1C9Mks @ 00:00:38])'],
                                  ['Pricing as if refund-and-keep cost zero',
                                   'A $40 order swings roughly $70 against the seller after refund',
                                   'Build expected return cost per order into product math from day one',
                                   'Dropshipping Deep Dive ([1L4TNDjsICQ @ 00:06:23])'],
                                  ['Missing the CJ damage dispute window',
                                   'Three-day ordinary and seven-day electronics windows leave full cost '
                                   'on seller',
                                   'Collect item, packaging, and label photos in the very first reply',
                                   'Dropshipping Deep Dive ([1L4TNDjsICQ @ 00:13:42])'],
                                  ['Slow or missing replies to customer messages',
                                   'Four days of silence pushes buyers to PayPal chargebacks and refunds',
                                   'Custom-domain support inbox plus a Chatfuel auto-reply bot on Facebook',
                                   'Flying Start Online ([rhATJAycfEU @ 00:17:49])'],
                                  ['Exchanging customers into pre-order stock blindly',
                                   '3PL warehouse software tries fulfilling a size that does not exist yet',
                                   'Connect PreProduct with a Loop API key so exchange orders go on hold',
                                   'PreProduct ([ZXDpWj-RfOQ @ 00:01:41])'],
                                  ['Selling physical goods with no liability cover',
                                   'Retailer can be held responsible even without designing or making the '
                                   'product',
                                   'General liability policy including product liability, set up online in '
                                   'about 10 minutes',
                                   'Insurance Assurance ([XxorvB6ExNs @ 00:00:59])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Before the Next Ad Budget Increase',
                           'body': 'Every item below comes from a loss, freeze, or forced refund that a '
                                   'practitioner took firsthand. Do not scale a product past test spend '
                                   'until all four are in place.',
                           'items': ['Supplier sends real photo and video of the actual unit before '
                                     'purchase volume rises; a supplier that refuses gets dropped '
                                     '[Anatoliy Labinskiy | E-com business encyclopedia — XED26wvEepA @ '
                                     '00:04:09].',
                                     'Every order ships tracked and the tracking number is entered in '
                                     'Shopify so both the buyer and the payment provider can see delivery '
                                     '[ZIK Analytics — 7GY4PPBU0GY @ 00:03:37].',
                                     'A chargeback evidence pack is ready: Shopify order export, '
                                     'AliExpress tracking, carrier screenshot, Stripe or PayPal '
                                     'transaction, and copies of customer emails, about 10 to 15 minutes '
                                     'per dispute [Flying Start Online — rhATJAycfEU @ 00:13:15].',
                                     'A per-order returns reserve is funded weekly, sized from 90 days of '
                                     'real data or a 20% apparel planning assumption [Dropshipping Deep '
                                     'Dive — 1L4TNDjsICQ @ 00:27:46].']}}],
 'pull_quote': '"Returns are not an interruption of the business. They are a line item in the business." '
               'Attributed to Dropshipping Deep Dive (1L4TNDjsICQ @ 00:29:17).',
 'diagram_id': 'diag-05',
 'action_checklist': ['On any damage report, request photos of the item, the packaging, and the shipping '
                      'label in the first reply and open the CJ dispute the same day [Dropshipping Deep '
                      'Dive — 1L4TNDjsICQ @ 00:13:42].',
                      'When a chargeback lands, send the Shopify order export, AliExpress tracking '
                      'screenshot, carrier tracking screenshot, Stripe or PayPal transaction record, and '
                      'any customer emails [Flying Start Online — rhATJAycfEU @ 00:12:30].',
                      'Refund without requiring a return on items under $20, and leave the restock box '
                      'unchecked when no inventory is coming back [Shopify Mastery — EjZsqaOIDsc @ '
                      '00:04:21].',
                      'Fulfill each order in Shopify, click add tracking, and enter the tracking number '
                      'and carrier so the buyer and payment provider can follow delivery [ZIK Analytics — '
                      '7GY4PPBU0GY @ 00:05:03].',
                      'Once a product proves itself as a winner, ask the supplier for photo and video of '
                      'the real unit before buying volume [Anatoliy Labinskiy | E-com business '
                      'encyclopedia — XED26wvEepA @ 00:04:09].',
                      'Calculate real return rate and cost per return, then move the per-order reserve '
                      'into a separate pot every week and keep a one-page returns playbook [Dropshipping '
                      'Deep Dive — 1L4TNDjsICQ @ 00:27:46].'],
 'statutory_citations': [{'title': 'Dropshipping Deep Dive — Returns Without the Bleed: Refunds, '
                                   'Exchanges, and the Supplier Reality [00:08:13]',
                          'url': 'https://www.youtube.com/watch?v=1L4TNDjsICQ&t=493s',
                          'relevance': 'Primary practitioner testimony on chargeback fees, payout '
                                       'clawbacks, and the 1% account-restriction threshold.'},
                         {'title': 'Flying Start Online — DEALING WITH SHOPIFY REFUNDS & CHARGEBACKS (Day '
                                   '27/30) #Bizathon3 [00:12:30]',
                          'url': 'https://www.youtube.com/watch?v=rhATJAycfEU&t=750s',
                          'relevance': 'Primary practitioner testimony on assembling chargeback evidence '
                                       'for physical dropshipped products.'},
                         {'title': 'Shopify Mastery — How to Handle Shopify Dropshipping Returns, Refunds, '
                                   'and Return Policies. [00:03:35]',
                          'url': 'https://www.youtube.com/watch?v=EjZsqaOIDsc&t=215s',
                          'relevance': 'Primary practitioner testimony on refunding without a return and '
                                       'the photo evidence method.'},
                         {'title': 'Anatoliy Labinskiy | E-com business encyclopedia — How to Deal with '
                                   'Shopify Chargebacks, Refunds, and Returns | Dropshipping Beginner '
                                   'Mistakes in Ecom [00:03:36]',
                          'url': 'https://www.youtube.com/watch?v=XED26wvEepA&t=216s',
                          'relevance': 'Primary practitioner testimony on a product-quality failure that '
                                       'triggered chargebacks at scale.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '3VDc8PoFZa8',
                       'title': 'How to update Shopify returns with Loop Returns - Step By Step',
                       'channel': 'GuidePixel',
                       'author': 'GuidePixel',
                       'text': 'Inform the customer of any changes made by using the communication tools '
                               'within Loop Returns.',
                       'tip': 'Inform the customer of any changes made by using the communication tools '
                              'within Loop Returns.',
                       'timestamp': 73,
                       'timestamp_seconds': 73,
                       'timestamp_label': '[00:01:13]',
                       'url': 'https://www.youtube.com/watch?v=3VDc8PoFZa8&t=73s',
                       'markdown': '[00:01:13](https://www.youtube.com/watch?v=3VDc8PoFZa8&t=73s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JzyBmddGOms',
                       'title': 'Shopify Returns Management App Demo | Automate Returns & Exchanges in 2 '
                                'Minutes',
                       'channel': 'Returndotai',
                       'author': 'Returndotai',
                       'text': 'Refunds can be processed via gift cards, store credit, discount codes, the '
                               'original payment method, or through third-party refund providers.',
                       'tip': 'Refunds can be processed via gift cards, store credit, discount codes, the '
                              'original payment method, or through third-party refund providers.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=JzyBmddGOms&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=JzyBmddGOms&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'X3G7DDq6KD8',
                       'title': 'Loop Returns Dropshipping Honest Review - Watch Before Using',
                       'channel': 'Wise Explainer',
                       'author': 'Wise Explainer',
                       'text': 'While Loop Returns excels at automating returns and improving the customer '
                               'experience, it is best suited for medium to large-scale drop shipping '
                               'stores that handle a significant number of orders and returns.',
                       'tip': 'While Loop Returns excels at automating returns and improving the customer '
                              'experience, it is best suited for medium to large-scale drop shipping '
                              'stores that handle a significant number of orders and returns.',
                       'timestamp': 81,
                       'timestamp_seconds': 81,
                       'timestamp_label': '[00:01:21]',
                       'url': 'https://www.youtube.com/watch?v=X3G7DDq6KD8&t=81s',
                       'markdown': '[00:01:21](https://www.youtube.com/watch?v=X3G7DDq6KD8&t=81s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7GY4PPBU0GY',
                       'title': 'How To Handle Returns & Refunds on Shopify | 2026 Shipping Tutorial',
                       'channel': 'ZIK Analytics',
                       'author': 'ZIK Analytics',
                       'text': 'The second thing you need to keep in mind is to provide proof of shipping, '
                               'and the best way to do that is by giving the buyer a tracking number that '
                               'both they and your payment provider can access.',
                       'tip': 'The second thing you need to keep in mind is to provide proof of shipping, '
                              'and the best way to do that is by giving the buyer a tracking number that '
                              'both they and your payment provider can access.',
                       'timestamp': 217,
                       'timestamp_seconds': 217,
                       'timestamp_label': '[00:03:37]',
                       'url': 'https://www.youtube.com/watch?v=7GY4PPBU0GY&t=217s',
                       'markdown': '[00:03:37](https://www.youtube.com/watch?v=7GY4PPBU0GY&t=217s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GYROU1C9Mks',
                       'title': 'How to Deal With Refunds & Returns (Shopify Dropshipping)',
                       'channel': 'Dean Alma',
                       'author': 'Dean Alma',
                       'text': "You always want to pay for tracked shipping even if it's greater cost "
                               'because it prevents the number of returns.',
                       'tip': "You always want to pay for tracked shipping even if it's greater cost "
                              'because it prevents the number of returns.',
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=GYROU1C9Mks&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=GYROU1C9Mks&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'B2xFNVqbu7c',
                       'title': 'How To Handle Shopify Refunds And Returns 2026 (For Beginners)',
                       'channel': 'Tutorials by Manizha & Ryan',
                       'author': 'Tutorials by Manizha & Ryan',
                       'text': "If you don't have a strong policy in place, people are going to be very "
                               'prone to just milking out your business.',
                       'tip': "If you don't have a strong policy in place, people are going to be very "
                              'prone to just milking out your business.',
                       'timestamp': 413,
                       'timestamp_seconds': 413,
                       'timestamp_label': '[00:06:53]',
                       'url': 'https://www.youtube.com/watch?v=B2xFNVqbu7c&t=413s',
                       'markdown': '[00:06:53](https://www.youtube.com/watch?v=B2xFNVqbu7c&t=413s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'YnEcCYA-UDs',
                       'title': 'How to Handle Shopify Refunds and Returns (Step-by-Step)',
                       'channel': 'Tutorial Stack',
                       'author': 'Tutorial Stack',
                       'text': "Usually, it's much faster to offer them store credit.",
                       'tip': "Usually, it's much faster to offer them store credit.",
                       'timestamp': 171,
                       'timestamp_seconds': 171,
                       'timestamp_label': '[00:02:51]',
                       'url': 'https://www.youtube.com/watch?v=YnEcCYA-UDs&t=171s',
                       'markdown': '[00:02:51](https://www.youtube.com/watch?v=YnEcCYA-UDs&t=171s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'daoVeRnScfo',
                       'title': 'How To Use Shopify Self-Serve Returns - Shopify Tutorial',
                       'channel': 'Sunrise Integration',
                       'author': 'Sunrise Integration',
                       'text': "It's a good idea for the store merchant to wait for receipt of the item "
                               'before choosing to initiate the refund.',
                       'tip': "It's a good idea for the store merchant to wait for receipt of the item "
                              'before choosing to initiate the refund.',
                       'timestamp': 419,
                       'timestamp_seconds': 419,
                       'timestamp_label': '[00:06:59]',
                       'url': 'https://www.youtube.com/watch?v=daoVeRnScfo&t=419s',
                       'markdown': '[00:06:59](https://www.youtube.com/watch?v=daoVeRnScfo&t=419s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EjZsqaOIDsc',
                       'title': 'How to Handle Shopify Dropshipping Returns, Refunds, and Return Policies.',
                       'channel': 'Shopify Mastery',
                       'author': 'Shopify Mastery',
                       'text': 'For lower value items, say anything under $20, almost always just refund '
                               'without return.',
                       'tip': 'For lower value items, say anything under $20, almost always just refund '
                              'without return.',
                       'timestamp': 261,
                       'timestamp_seconds': 261,
                       'timestamp_label': '[00:04:21]',
                       'url': 'https://www.youtube.com/watch?v=EjZsqaOIDsc&t=261s',
                       'markdown': '[00:04:21](https://www.youtube.com/watch?v=EjZsqaOIDsc&t=261s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EjZsqaOIDsc',
                       'title': 'How to Handle Shopify Dropshipping Returns, Refunds, and Return Policies.',
                       'channel': 'Shopify Mastery',
                       'author': 'Shopify Mastery',
                       'text': "Tell the customer that you're going to give them 50% back and they don't "
                               'need to ship anything.',
                       'tip': "Tell the customer that you're going to give them 50% back and they don't "
                              'need to ship anything.',
                       'timestamp': 427,
                       'timestamp_seconds': 427,
                       'timestamp_label': '[00:07:07]',
                       'url': 'https://www.youtube.com/watch?v=EjZsqaOIDsc&t=427s',
                       'markdown': '[00:07:07](https://www.youtube.com/watch?v=EjZsqaOIDsc&t=427s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ZXDpWj-RfOQ',
                       'title': 'Loop Returns Pre-order Integration for Shopify',
                       'channel': 'PreProduct',
                       'author': 'PreProduct',
                       'text': 'In Shopify orders admin, we need to apply a fulfillment status of hold so '
                               "your 3PL warehouse software doesn't try to fulfill an item which doesn't "
                               'actually exist in stock yet.',
                       'tip': 'In Shopify orders admin, we need to apply a fulfillment status of hold so '
                              "your 3PL warehouse software doesn't try to fulfill an item which doesn't "
                              'actually exist in stock yet.',
                       'timestamp': 101,
                       'timestamp_seconds': 101,
                       'timestamp_label': '[00:01:41]',
                       'url': 'https://www.youtube.com/watch?v=ZXDpWj-RfOQ&t=101s',
                       'markdown': '[00:01:41](https://www.youtube.com/watch?v=ZXDpWj-RfOQ&t=101s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rhATJAycfEU',
                       'title': 'DEALING WITH SHOPIFY REFUNDS & CHARGEBACKS (Day 27/30) #Bizathon3',
                       'channel': 'Flying Start Online',
                       'author': 'Flying Start Online',
                       'text': 'If 10 people asked for a refund, only about a couple of them will actually '
                               'send the product back to you.',
                       'tip': 'If 10 people asked for a refund, only about a couple of them will actually '
                              'send the product back to you.',
                       'timestamp': 663,
                       'timestamp_seconds': 663,
                       'timestamp_label': '[00:11:03]',
                       'url': 'https://www.youtube.com/watch?v=rhATJAycfEU&t=663s',
                       'markdown': '[00:11:03](https://www.youtube.com/watch?v=rhATJAycfEU&t=663s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rhATJAycfEU',
                       'title': 'DEALING WITH SHOPIFY REFUNDS & CHARGEBACKS (Day 27/30) #Bizathon3',
                       'channel': 'Flying Start Online',
                       'author': 'Flying Start Online',
                       'text': "If a customer asks something and you don't reply to them for four days, "
                               'they are going to get upset and go to PayPal and either do a chargeback or '
                               'do a refund.',
                       'tip': "If a customer asks something and you don't reply to them for four days, "
                              'they are going to get upset and go to PayPal and either do a chargeback or '
                              'do a refund.',
                       'timestamp': 1069,
                       'timestamp_seconds': 1069,
                       'timestamp_label': '[00:17:49]',
                       'url': 'https://www.youtube.com/watch?v=rhATJAycfEU&t=1069s',
                       'markdown': '[00:17:49](https://www.youtube.com/watch?v=rhATJAycfEU&t=1069s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XED26wvEepA',
                       'title': 'How to Deal with Shopify Chargebacks, Refunds, and Returns | Dropshipping '
                                'Beginner Mistakes in Ecom',
                       'channel': 'Anatoliy Labinskiy | E-com business encyclopedia',
                       'author': 'Anatoliy Labinskiy | E-com business encyclopedia',
                       'text': 'We start getting a lot of chargebacks because our shoes were really ugly; '
                               'there was no leather there, it was like a plastic shoe.',
                       'tip': 'We start getting a lot of chargebacks because our shoes were really ugly; '
                              'there was no leather there, it was like a plastic shoe.',
                       'timestamp': 233,
                       'timestamp_seconds': 233,
                       'timestamp_label': '[00:03:53]',
                       'url': 'https://www.youtube.com/watch?v=XED26wvEepA&t=233s',
                       'markdown': '[00:03:53](https://www.youtube.com/watch?v=XED26wvEepA&t=233s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XxorvB6ExNs',
                       'title': 'Product Liability Insurance Coverage and Cost | What is Product '
                                'Liability? Small Business Insurance',
                       'channel': 'Insurance Assurance',
                       'author': 'Insurance Assurance',
                       'text': "Even if you didn't design or make the product, you can still be held "
                               'responsible as a retailer.',
                       'tip': "Even if you didn't design or make the product, you can still be held "
                              'responsible as a retailer.',
                       'timestamp': 59,
                       'timestamp_seconds': 59,
                       'timestamp_label': '[00:00:59]',
                       'url': 'https://www.youtube.com/watch?v=XxorvB6ExNs&t=59s',
                       'markdown': '[00:00:59](https://www.youtube.com/watch?v=XxorvB6ExNs&t=59s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HPTGnp51Iks',
                       'title': 'How To Process Shopify Returns And Exchanges (Easy Guide)',
                       'channel': "Jim's Ecommerce Tutorials",
                       'author': "Jim's Ecommerce Tutorials",
                       'text': 'Depending on the products involved, the customer may need to pay more, '
                               'receive a partial refund, or have a balance adjusted.',
                       'tip': 'Depending on the products involved, the customer may need to pay more, '
                              'receive a partial refund, or have a balance adjusted.',
                       'timestamp': 127,
                       'timestamp_seconds': 127,
                       'timestamp_label': '[00:02:07]',
                       'url': 'https://www.youtube.com/watch?v=HPTGnp51Iks&t=127s',
                       'markdown': '[00:02:07](https://www.youtube.com/watch?v=HPTGnp51Iks&t=127s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V0kR_J_Vdkw',
                       'title': 'How To Handle Shopify Refunds And Returns 2025 For Beginners',
                       'channel': 'Guides by Dan',
                       'author': 'Guides by Dan',
                       'text': 'Click on return rules; these rules set the foundation for how returns are '
                               'handled within your store.',
                       'tip': 'Click on return rules; these rules set the foundation for how returns are '
                              'handled within your store.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=V0kR_J_Vdkw&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=V0kR_J_Vdkw&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1L4TNDjsICQ',
                       'title': 'Returns Without the Bleed: Refunds, Exchanges, and the Supplier Reality',
                       'channel': 'Dropshipping Deep Dive',
                       'author': 'Dropshipping Deep Dive',
                       'text': "Under CJ's published dispute policy, a damage dispute for an ordinary "
                               'product should be opened within three days of the customer receiving it, '
                               'and for electronics the window is seven days.',
                       'tip': "Under CJ's published dispute policy, a damage dispute for an ordinary "
                              'product should be opened within three days of the customer receiving it, '
                              'and for electronics the window is seven days.',
                       'timestamp': 787,
                       'timestamp_seconds': 787,
                       'timestamp_label': '[00:13:07]',
                       'url': 'https://www.youtube.com/watch?v=1L4TNDjsICQ&t=787s',
                       'markdown': '[00:13:07](https://www.youtube.com/watch?v=1L4TNDjsICQ&t=787s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
