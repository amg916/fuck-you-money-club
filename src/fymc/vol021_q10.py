from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'automated-support-and-retention',
 'question_prompt': 'How do I automate customer support and turn first-time buyers into repeat subscribers '
                    'with email and SMS?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'Automated Support and Retention',
 'subtitle': 'Gorgias help desk and AI Agent setup, pricing, and alternatives, AI handling of "where is my '
             'order" and damaged-item tickets, Klaviyo email and SMS flows, post-purchase thank-you flows, '
             'Recharge subscription flows, and a case study that tripled email revenue',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Support and retention operators agree on one split: AI handles order-status '
                      'tickets, humans own refunds and exceptions, and Klaviyo post-purchase flows chase '
                      'the second order, where the profit lives. Macha prices Gorgias AI Agent at $0.90 '
                      'annual or $1 monthly per automated interaction, with $1.50 over the allowance, and '
                      "shows the bill climbing as the resolution rate rises. Macha's own agent starts at "
                      '$299 for 750 tickets and breaks even against Gorgias only near 50% resolution. Amol '
                      'Walunj sends refunds over $75 to a manager queue. Tarun Brar shows a 3x ROAS first '
                      'order leaving $26 while the second order earns $60. Derek Stroh targets a '
                      'repurchase inside 30 to 60 days. The practitioners split on per-resolution versus '
                      'flat pricing, on 10-minute versus 20-minute delays behind Shopify emails, and on '
                      'how early to fire offers and review requests.',
 'key_metrics': [{'label': 'Gorgias AI Agent Price Per Automated Interaction',
                  'metric': 'Gorgias AI Agent Price Per Automated Interaction',
                  'value': '$0.90 annual billing / $1 monthly billing / $1.50 over the plan allowance',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Macha's pricing breakdown of Gorgias AI Agent, checked 20 Nov 2026. Flow "
                             'resolutions draw on the same allowance as AI resolutions.',
                  'source': 'Macha ([7Ac3MIM55Yc @ 00:00:00])'},
                 {'label': 'Post-Purchase Flow Open Rate Benchmark',
                  'metric': 'Post-Purchase Flow Open Rate Benchmark',
                  'value': 'Over 50% average; 74% for the top 10% of senders',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Tarun Brar calls post-purchase the highest-engagement flow. Placed-order '
                             'rate is 0.4% on average and 2% for the top 10%.',
                  'source': 'Tarun Brar - eCom Email Marketing ([coevagBV6wU @ 00:02:13])'},
                 {'label': 'Scooch Subscription Retention Result',
                  'metric': 'Scooch Subscription Retention Result',
                  'value': 'Churn down 33%, subscriber LTV tripled, ad spend down 48%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Milan Raviji's Recharge plus Klaviyo client result. They report revenue fell "
                             'only 5% while ad spend dropped 48%.',
                  'source': 'Milan Raviji│Klaviyo & Email Marketing ([6xiaPZPDBCQ @ 00:00:39])'},
                 {'label': 'Second-Order Loyalty Window',
                  'metric': 'Second-Order Loyalty Window',
                  'value': 'Repeat purchase inside the first 30 to 60 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Derek Stroh reports that loyalty is much higher when the buyer purchases '
                             'again within 30 to 60 days of the first order.',
                  'source': 'Derek Stroh ([cerX0RFHJ0c @ 00:09:35])'}],
 'sections': [{'title': 'The Practitioner Consensus',
               'paragraphs': ["Every support operator here starts automation with the same ticket: 'where "
                              "is my order.' Macha's agent reads the ticket, pulls the order from Shopify "
                              'and checks that the order email matches the person asking. It then answers '
                              'with one of three states: shipped (with carrier, tracking number and link), '
                              'not shipped yet, or late. Anything outside the rules goes to the team with '
                              "an internal note [VsY0GsB1UI0 @ 00:00:00]. Amol Walunj's Cevanos demo "
                              'applies a stricter identity check. A one-time code goes to the account '
                              'email before any refund moves, and order 1016 ($149, paid and fulfilled) '
                              "comes straight from Shopify through the connector: 'That last line comes "
                              "from Savano's, not the AI' [QZz9_VSA1lA @ 00:01:31]. Brandon Amoroso shows "
                              'Gorgias already covering self-service without AI. Customers can track, '
                              'cancel, return or report an issue after looking up the order by email code '
                              'or order number [Pwv-LlhTPwo @ 00:04:59]. All three follow the same rule: '
                              'the bot answers status questions and a human owns money and exceptions. '
                              'Macha always routes these to people: delivered-not-received, damaged or '
                              'wrong items, address changes, cancelled or refunded orders, anger and '
                              'chargeback threats. The agent issues no refund or reship unless the written '
                              'rules allow it [VsY0GsB1UI0 @ 00:05:00].',
                              'On retention, the speakers agree on one claim: the money is in order two, '
                              "not order one. Tarun Brar opens with 'Most of your profit doesn't come from "
                              "the first order' and backs it with funnel math. 400 visitors converting at "
                              '3% give 12 buyers, and a 20-25% return rate gives roughly 3 repeat buyers '
                              '[coevagBV6wU @ 00:00:00]. Gavin Hewitson states the same point plainly: the '
                              'second order is typically more profitable because you are not spending as '
                              'much on advertising to get the buyer across the line [Cu4iN3jgMwI @ '
                              '00:13:16]. Derek Stroh puts a clock on it. If a buyer purchases again '
                              'inside the first 30 to 60 days, loyalty runs much higher than if that '
                              'repeat never happens. Their stated goals are higher AOV and LTV and less '
                              'reliance on cold traffic [cerX0RFHJ0c @ 00:09:35]. Milan Raviji applies the '
                              'same logic to subscriptions. Churn falls sharply after the third box, and '
                              "'if you keep a customer for 3 months, the likelihood that they stay for "
                              "longer is extraordinarily high' [6xiaPZPDBCQ @ 00:06:42]. The shared "
                              'message from all four is that the window right after checkout drives '
                              'profit. Brands that send a generic thank-you there, or nothing, give up the '
                              'cheapest revenue in the business and keep paying full acquisition cost for '
                              'every future sale.',
                              'The baseline post-purchase build is nearly identical across the Klaviyo '
                              'practitioners. Derek Stroh triggers on Placed Order and filters out '
                              'canceled and refunded orders. They then split by product, category, desired '
                              'outcome, order value and quantity, so each buyer gets usage and cross-sell '
                              'content that fits [cerX0RFHJ0c @ 00:05:22]. Gavin Hewitson adds a 20-minute '
                              'delay so the Shopify or WooCommerce confirmation lands first, which keeps '
                              'the two messages from clashing and makes the flow look more human. They '
                              'also run a second flow off Fulfilled Order because fulfillment timing is '
                              'more accurate [Cu4iN3jgMwI @ 00:03:49]. Emiel Dingemans uses a 10-minute '
                              "wait for the same reason, since the buyer receives Shopify's transactional "
                              'email in that gap. They then split on two or more placed orders and rejoin '
                              'the paths afterward [6OklvvWTGmw @ 00:34:33]. Tarun Brar splits new versus '
                              'returning buyers and routes VIPs with more than 3 orders, or the top '
                              "10-15%. They insist on a review request 'no matter what', sent after "
                              'delivery rather than at checkout [coevagBV6wU @ 00:12:12]. Gavin and Emiel '
                              'both send plain-text founder emails that do not sell, and both say replies '
                              'to those emails help deliverability and make the brand feel human.'],
               'table': {'caption': 'Where support and retention operators agree on automation baselines',
                         'headers': ['Consensus Point',
                                     'How Operators Execute It',
                                     'Why It Pays Off',
                                     'Expert Source'],
                         'rows': [["Automate 'where is my order' tickets first",
                                   'Agent pulls the Shopify order, verifies the email, then replies '
                                   'shipped, not shipped, or late',
                                   'Highest-volume repetitive category, answerable directly from Shopify '
                                   'order data',
                                   'Macha ([VsY0GsB1UI0 @ 00:00:00])'],
                                  ['Humans own refunds, damage claims and chargeback threats',
                                   'Delivered-not-received, wrong items, address changes and angry '
                                   'customers always go to staff',
                                   'Agent never refunds or reships unless the written rules explicitly '
                                   'allow it',
                                   'Macha ([VsY0GsB1UI0 @ 00:05:00])'],
                                  ['Verify identity before any money moves',
                                   'One-time code sent to the account email before the agent processes any '
                                   'refund',
                                   'Stops refunds to the wrong person and keeps a clean audit trail',
                                   'Amol Walunj ([QZz9_VSA1lA @ 00:01:31])'],
                                  ['The second order carries the real profit',
                                   'Post-purchase flows push repeat buyers without paying ad spend to '
                                   'close them',
                                   'Second order is typically more profitable because acquisition cost is '
                                   'not repeated',
                                   'Gavin Hewitson ([Cu4iN3jgMwI @ 00:13:16])'],
                                  ['Win the repeat purchase within 30 to 60 days',
                                   'Sequence education, cross-sell and an expiring offer inside that first '
                                   'two-month window',
                                   'Buyers who reorder early show much higher loyalty than those who never '
                                   'return',
                                   'Derek Stroh ([cerX0RFHJ0c @ 00:09:35])'],
                                  ["Delay flow emails behind Shopify's transactional email",
                                   'Wait 10 to 20 minutes after Placed Order before the first flow email '
                                   'fires',
                                   'Avoids doubled-up messages in the inbox and makes the brand look human',
                                   'Emiel Dingemans | eCommerce Retention Marketing ([6OklvvWTGmw @ '
                                   '00:34:33])'],
                                  ['Ask for reviews only after delivery',
                                   'Send the review request seven to ten days after the product arrives',
                                   'Buyers can only review a product they have actually used',
                                   'Tarun Brar - eCom Email Marketing ([coevagBV6wU @ 00:12:12])']]}},
              {'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The AI agent bill is where operators either get burned or win, and Macha, '
                              'which sells a competing agent, runs the numbers in public. Gorgias AI Agent '
                              'costs $0.90 per automated interaction on annual billing or $1 monthly. The '
                              '$550 Pro plan bundles $360 of helpdesk (2,000 tickets) with $190 of AI (190 '
                              'interactions). Overage runs $1.50, and any ticket a human replies to within '
                              '72 hours bills as a normal ticket instead [eusN-cV9bSQ @ 00:02:55]. At 30% '
                              "resolution, Macha's worked math lands at $715 total for 1,000 tickets and "
                              '$2,885 for 5,000. At 5,000 tickets, the AI line jumps from about $2,000 to '
                              "$3,485 if resolution climbs to 50%, because 'the AI part of the bill grows "
                              "with every resolution' [7Ac3MIM55Yc @ 00:05:06]. Macha prices its own agent "
                              'at $299 for 750 tickets (about $0.40 each), $599 for 1,500 and $3,999 for '
                              '10,000, with no setup fee and $50 of free usage [VsY0GsB1UI0 @ 00:05:47]. '
                              'Its six-tool comparison models a 1,000-ticket month with 300 resolutions. '
                              'Siena lands highest at $1,020, Fini costs $267 at $0.89 per resolution, and '
                              'My Ask AI is lowest at $199. Macha concedes it only breaks even with '
                              'Gorgias near 50% resolution [iqOjQraqwcM @ 00:05:42].',
                              "The 'where is my order' playbook is scripted rule by rule. Macha's agent "
                              "uses the Shopify 'Get order' tool on an order number, or searches by email "
                              'when no number is given. It follows an existing Gorgias macro and tags '
                              'tickets wismo and AI draft. It never guesses a delivery date, because '
                              'Shopify stores the tracking number, not the latest carrier scan '
                              '[VsY0GsB1UI0 @ 00:03:22]. Edge cases have fixed responses. An unfulfilled '
                              "order under a 2-business-day policy gets 'should leave by Thursday.' A "
                              'fulfilled order with no tracking number gets told it shipped while the '
                              'ticket goes to HIGH priority. An order unfulfilled after 3 business days '
                              'gets an apology, assignment to the fulfilment team and no new date. An '
                              'email mismatch gets nothing until the customer supplies the order number '
                              "and checkout email [VsY0GsB1UI0 @ 00:03:42]. Amol Walunj's Cevanos build "
                              'sends any refund over $75 to a manager approval queue. When a replacement '
                              'must ship, it opens a Gorgias ticket with the order and refund details. It '
                              'refuses duplicate refunds by policy, with the reason on record [QZz9_VSA1lA '
                              '@ 00:02:09]. Brandon Amoroso adds plain Gorgias rules on top. A Shopify '
                              "last order above $1,000 gets tagged 'high value order', assigned to an "
                              'agent, auto-replied or flagged to the owner [Pwv-LlhTPwo @ 00:07:28].',
                              "Tarun Brar's unit economics justify the retention build. A $100 AOV at 60% "
                              'margin leaves $60 gross profit. A 3x ROAS means about $33 CAC, leaving only '
                              '$26 on order one, while the second order earns the full $60 and lifetime '
                              'runs about $86 [coevagBV6wU @ 00:03:22]. Their sequence front-loads the '
                              'first 7-10 days of a 30-45-day flow and sends the cross-sell 5 days after '
                              'delivery. New buyers get a flash offer around day 45 (30 days for protein, '
                              '2-3 months for skincare). Photo reviews earn a $20 voucher and video '
                              "reviews $50. Gavin Hewitson turns off Shopify's own shipping email and "
                              'applies for transactional status so E1 lands in Updates rather than '
                              'Promotions. They assume 4-day transit, send E1B 6 days out and offer 10-15% '
                              'on the second order [Cu4iN3jgMwI @ 00:07:12]. Milan Raviji escalates '
                              'card-decline messaging with each decline and treats the 4th decline as a '
                              'churned customer. A free pouch in box 2 targets products with high '
                              'month-one churn [6xiaPZPDBCQ @ 00:11:45]. Emiel Dingemans closes the loop '
                              'with a sunset flow. Anyone inactive for 120 days who has received at least '
                              '8 emails gets one plain-text email at 7am local time. Five days later they '
                              'are set to unengaged and suppressed [6OklvvWTGmw @ 00:41:03].'],
               'table': {'caption': 'Tools, prices and unit economics quoted by support and retention '
                                    'operators',
                         'headers': ['Lever or Tool',
                                     'Exact Number Quoted',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Gorgias AI Agent per-interaction billing',
                                   '$0.90 annual or $1 monthly; $1.50 per interaction over allowance',
                                   'Each automated interaction also counts as a helpdesk ticket; human '
                                   'replies within 72 hours bill as normal tickets',
                                   'Macha ([eusN-cV9bSQ @ 00:02:55])'],
                                  ['Gorgias helpdesk plan tiers with AI allowance',
                                   'Starter $40, Basic $90, Pro $550, Advanced $1,430 monthly',
                                   'Pro includes 2,000 tickets and 190 AI interactions; Advanced includes '
                                   '5,000 and 530',
                                   'Macha ([7Ac3MIM55Yc @ 00:03:22])'],
                                  ['Macha agent flat ticket bundles',
                                   '$299 for 750, $599 for 1,500, $3,999 for 10,000 tickets',
                                   'Runs in safe mode until about nine in ten drafts are approved',
                                   'Macha ([VsY0GsB1UI0 @ 00:05:47])'],
                                  ['Fini per-resolution pricing with no minimum',
                                   '$0.89 per resolution, about $267 for 300 resolutions',
                                   'Implementation included, but the bill grows as the AI resolves more '
                                   'tickets',
                                   'Macha ([iqOjQraqwcM @ 00:03:11])'],
                                  ['Cevanos refund approval threshold',
                                   'Any refund above $75 goes to a manager approval queue',
                                   'The manager records a reason and approves; duplicate refunds are '
                                   'refused by policy',
                                   'Amol Walunj ([QZz9_VSA1lA @ 00:02:09])'],
                                  ['Post-purchase first-order unit economics',
                                   '$100 AOV, 60% margin, 3x ROAS leaves about $26 profit',
                                   'The second order earns the full $60 gross profit, so the flow pays for '
                                   'itself',
                                   'Tarun Brar - eCom Email Marketing ([coevagBV6wU @ 00:03:37])'],
                                  ['Post-purchase flow performance benchmarks',
                                   'Open over 50% average, 74% top 10%; placed order 0.4% to 2%',
                                   'Use these numbers to judge whether the flow is underperforming before '
                                   'rebuilding',
                                   'Tarun Brar - eCom Email Marketing ([coevagBV6wU @ 00:02:13])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small settings that change the bill and the inbox',
                           'body': 'Four adjustments the practitioners make that cut AI cost, protect '
                                   'deliverability and keep offers urgent.',
                           'items': ['Never let the agent quote a delivery date. Shopify holds the '
                                     'tracking number, not the latest carrier scan, so point the customer '
                                     'to the tracking link [Macha — VsY0GsB1UI0 @ 00:03:22].',
                                     'Model your own resolution rate before signing up for per-resolution '
                                     'pricing. With Fini and similar tools, the bill grows as the AI '
                                     'resolves more tickets [Macha — iqOjQraqwcM @ 00:03:11].',
                                     "Turn off Shopify's shipping email and apply for transactional status "
                                     "in Klaviyo so the email lands in Updates, not Promotions: 'You get "
                                     "better deliverability if it ends up here' [Gavin Hewitson — "
                                     'Cu4iN3jgMwI @ 00:07:54].',
                                     "Cap flash offers in the post-purchase flow: 'You don't want these "
                                     "offers to last more than 3 to 4 days,' followed by a 24-hour last "
                                     'chance [Tarun Brar - eCom Email Marketing — coevagBV6wU @ '
                                     '00:15:48].']},
               'sop_steps': [{'step': 1,
                              'title': 'Connect and scope the order-status agent',
                              'action': 'Authorize the agent from the Gorgias app store with read and '
                                        'write access to customers and tickets, then point it at Shopify '
                                        'order lookup.',
                              'detail': 'Gorgias shows the requested scopes at authorization [Amol Walunj '
                                        "— QZz9_VSA1lA @ 00:00:18]. The agent uses the Shopify 'Get order' "
                                        'tool or searches by email, follows an existing macro and tags '
                                        'tickets wismo and AI draft [Macha — VsY0GsB1UI0 @ 00:01:58].'},
                             {'step': 2,
                              'title': 'Run safe mode until drafts clear the bar',
                              'action': 'Keep the agent drafting rather than sending until about nine in '
                                        'ten drafts are approved, then take the first category live.',
                              'detail': "'Before launch, we agree the bar with your team, usually about "
                                        "nine in ten drafts approved.' Setup is a 20-minute call, and the "
                                        'first category goes live within a week [Macha — VsY0GsB1UI0 @ '
                                        '00:06:31].'},
                             {'step': 3,
                              'title': 'Build the post-purchase flow from the template',
                              'action': "Open Flows, click Create flow, search 'post purchase', pick the "
                                        'template for your integration and add cancel and refund filters.',
                              'detail': "Search 'post purchase' in the template bar and pick the Shopify, "
                                        'WooCommerce or BigCommerce variant [TUTOR BASE — qaQ0aFPTDKA @ '
                                        '00:00:55]. Trigger on Placed Order with canceled = 0 and refunded '
                                        '= 0 filters [Derek Stroh — cerX0RFHJ0c @ 00:05:22].'},
                             {'step': 4,
                              'title': 'Add the second-order incentive and the review request',
                              'action': 'Split on placed order = 1, wait four days, offer 10-15% on the '
                                        'second order, and send the review ask after delivery.',
                              'detail': 'Use a placed order = 1 split, a 4-day delay and a 10-15% '
                                        'second-order incentive [Gavin Hewitson — Cu4iN3jgMwI @ 00:12:37]. '
                                        'Wait until after delivery to ask for a review [Tarun Brar - eCom '
                                        'Email Marketing — coevagBV6wU @ 00:12:12].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split in AI support is how the bill scales with volume. '
                              'Gorgias AI Agent charges $0.90 per automated interaction on annual billing '
                              "and $1 monthly, each one also counted as a helpdesk ticket, and Macha's "
                              'review notes the Pro plan includes only 190 interactions before overage '
                              'jumps to $1.50, while scoring Gorgias 62/100 against its own 92 '
                              "[eusN-cV9bSQ @ 00:02:55]. In Macha's six-tool shootout at 1,000 tickets "
                              'with 300 resolved, Gorgias lands at $355 for the AI layer, Siena at $1,020 '
                              'on a $750 monthly platform fee, Fini at $267 on $0.89 per resolution with '
                              'no minimum, and My Ask AI at $199 for 1,000 tickets with white-glove setup '
                              'from $999 a month [iqOjQraqwcM @ 00:03:11]. Macha sells flat tiers instead, '
                              'and at 1,000 tickets its own product needs the $599 plan, so it scores '
                              'itself 3 on cost and concedes it breaks even against Gorgias only when it '
                              'resolves close to half of all tickets [iqOjQraqwcM @ 00:05:42]. At 5,000 '
                              'tickets the comparison flips: Macha puts its own price at $1,999, level '
                              "with Gorgias at 30% resolution and lower above it, while Gorgias's bill at "
                              'that volume runs $2,885 total at 30% and the AI portion alone climbs toward '
                              '$3,485 at 50% [7Ac3MIM55Yc @ 00:06:32]. The operator call is simple: pick '
                              "the pricing model that matches your real resolution rate, not the vendor's "
                              'headline automation claim.',
                              'The second disagreement is who signs off before a customer sees an AI '
                              'answer. Macha runs every new client through a 20-minute call and then safe '
                              'mode, holding drafts until the team approves about nine in ten, with the '
                              'first category live within a week and no setup fee [VsY0GsB1UI0 @ '
                              "00:06:31]. Macha's review of Gorgias AI Agent 3.0 flags the opposite "
                              'design: Playground testing is unbilled and a second AI model checks answers '
                              'before sending, but there is no step for the team to approve drafts before '
                              'customers see them [eusN-cV9bSQ @ 00:02:35]. Amol Walunj demos a third '
                              'playbook in Cevanos where the gate is a hard dollar policy rather than '
                              'draft review: the agent sends a one-time code to the account email before '
                              'any refund, and any refund over $75 lands in an approval queue where a '
                              'manager enters a reason and approves; a duplicate refund gets refused by '
                              'policy, not by AI judgement, with the reason on record [QZz9_VSA1lA @ '
                              '00:02:09]. Brandon Amoroso skips AI for routing altogether, building native '
                              'Gorgias rules that tag a Shopify last order over $1,000 as a high value '
                              'order, assign an agent, fire an auto-reply, or alert the owner directly, '
                              'and argues the helpdesk drastically reduces hours on its own [Pwv-LlhTPwo @ '
                              '00:07:28].',
                              'Retention builders split on how the post-purchase flow is wired and when '
                              'money goes on the table. Gavin Hewitson runs two flows: one on Placed Order '
                              'with 20-minute-delayed, text-only founder emails that are not designed to '
                              'sell, and one on Fulfilled Order because fulfillment timing is more '
                              'accurate, then drops a 10 to 15% second-order incentive after a 4-day delay '
                              'and gives the else path the same offer [Cu4iN3jgMwI @ 00:12:37]. Emiel '
                              "Dingemans runs a single Placed Order flow, waits 10 minutes so Shopify's "
                              'transactional email lands first, splits on placed order of two or more, '
                              'rejoins the paths, and sends a founder check-in at about two weeks because '
                              'replies help deliverability [6OklvvWTGmw @ 00:34:33]. Tarun Brar holds the '
                              'money much longer: education at plus 3 days, cross-sell 5 days after '
                              'delivery, then a flash offer for new buyers only around day 45, stretched '
                              'to 2 to 3 months for skincare and cut to 30 days for protein, with offers '
                              'capped at 3 to 4 days [coevagBV6wU @ 00:10:02]. Derek Stroh runs eight '
                              'emails, lands 10% off at E5, and fires an expiring custom code at E7 that '
                              'cannot be found on Reddit, because a repurchase inside 30 to 60 days makes '
                              'loyalty much higher [cerX0RFHJ0c @ 00:09:48].'],
               'table': {'caption': 'Competing playbooks for AI support and retention flows, side by side',
                         'headers': ['Decision Point',
                                     'Playbook A',
                                     'Playbook B',
                                     'Operator Read',
                                     'Expert Source'],
                         'rows': [['AI support pricing model at 1,000 tickets',
                                   'Gorgias per-interaction billing: $190 for 190 included plus 110 at '
                                   '$1.50 equals $355',
                                   'Macha flat tier: 1,000 tickets requires the $599 plan, scored 3 on '
                                   'cost',
                                   'Macha only breaks even against Gorgias near 50% resolution at this '
                                   'volume',
                                   'Macha ([iqOjQraqwcM @ 00:05:42])'],
                                  ['AI support pricing model at 5,000 tickets',
                                   'Gorgias runs $2,885 total at 30% resolution, AI part rising with '
                                   'resolutions',
                                   'Macha prices 5,000 tickets at $1,999 regardless of resolution rate '
                                   'achieved',
                                   'Level with Gorgias at 30% resolution and cheaper at every rate above '
                                   'it',
                                   'Macha ([7Ac3MIM55Yc @ 00:06:32])'],
                                  ['Human sign-off before AI answers reach customers',
                                   'Safe mode holds drafts until roughly nine in ten get team approval',
                                   'Gorgias 3.0 uses a second AI model check with no team draft approval',
                                   'Choose draft review when brand voice risk outweighs speed to launch',
                                   'Macha ([eusN-cV9bSQ @ 00:02:35])'],
                                  ['Refund control inside an AI support agent',
                                   'Hard policy gate: any refund over $75 routes to a manager approval '
                                   'queue',
                                   'One-time code to the account email before any refund gets processed',
                                   'Duplicate refunds refused by written policy, not AI judgement, with '
                                   'reason logged',
                                   'Amol Walunj ([QZz9_VSA1lA @ 00:02:09])'],
                                  ['Post-purchase flow trigger architecture and confirmation timing',
                                   'Two flows on Placed Order and Fulfilled Order with 20-minute founder '
                                   'email delay',
                                   'One Placed Order flow, 10-minute wait, split on two-plus orders, then '
                                   'rejoin',
                                   'Fulfilled Order timing is more accurate for shipping and cross-sell '
                                   'sends',
                                   'Gavin Hewitson ([Cu4iN3jgMwI @ 00:12:37])'],
                                  ['When to put the second-order discount in front of buyers',
                                   '10 to 15% second-order incentive after a 4-day delay on first orders',
                                   'Flash offer for new buyers only near day 45, adjusted by product '
                                   'category',
                                   "Match the offer window to the product's real usage and repurchase "
                                   'cycle',
                                   'Tarun Brar - eCom Email Marketing ([coevagBV6wU @ 00:10:02])'],
                                  ['Email revenue share target and SMS lift claims',
                                   'Host benchmark says email should drive 35 to 50% of attributed revenue',
                                   'Theo Clough targets 30 to 40% of revenue and claims $36 back per $1',
                                   'Guest brand sat at only 10 to 15%, showing the gap left on the table',
                                   'Carbon Box Media ([wFXlLgdV31A @ 00:05:47])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The WISMO failures are data failures before they are AI failures. Macha '
                              'warns that Gorgias macros read only the most recent order, so a customer '
                              'with several open orders can get the wrong answer from a macro-driven reply '
                              '[VsY0GsB1UI0 @ 00:00:38]. Shopify stores the tracking number, not the '
                              'latest carrier scan, so the agent points to the tracking link and never '
                              'guesses a delivery date; email mismatch is the privacy trap, where the '
                              'agent shares nothing and asks for the order number and checkout email '
                              'instead [VsY0GsB1UI0 @ 00:03:22]. Macha also flags that past tickets are '
                              'not a knowledge source in Gorgias AI Agent, and that Flow resolutions '
                              'quietly draw on the same allowance as AI resolutions, so scripted '
                              'automation eats the same budget [7Ac3MIM55Yc @ 00:02:16]. Amol Walunj shows '
                              'the hard action ceiling in a live demo: the Cevanos agent cannot ship a '
                              'replacement, so it opens a Gorgias ticket carrying the order and refund '
                              "details for a human to execute [QZz9_VSA1lA @ 00:02:54]. Macha's "
                              'always-human list covers delivered-not-received, damaged or wrong items, '
                              'address changes, cancelled or refunded orders, anger and chargeback '
                              'threats, with no refund or reship issued unless the written rules '
                              'explicitly allow it.',
                              "The economics trap is that AI support pricing punishes success. Macha's own "
                              'review boils its Gorgias criticism down to two lines, you do the work and '
                              'price grows with success, and spells out that the $550 Pro plan splits into '
                              '$360 helpdesk for 2,000 tickets and $190 AI for 190 interactions, with '
                              '$1.50 per interaction past that, while a human reply inside 72 hours gets '
                              'billed as a normal ticket instead [eusN-cV9bSQ @ 00:04:06]. Worked at 30% '
                              'resolution, 1,000 tickets runs $715 total and 5,000 tickets runs $2,885; '
                              'push resolution to 50% and the AI part climbs from about $2,000 to $3,485, '
                              'because the AI part of the bill grows with every resolution [7Ac3MIM55Yc @ '
                              "00:05:06]. Macha hangs the same warning on Fini's $0.89 per resolution with "
                              'no minimum: model your own resolution rate first before signing anything '
                              '[iqOjQraqwcM @ 00:03:11]. Subscription retention carries its own brutal '
                              'math: Milan Raviji reports paid-ad subscriber acquisition costing 4 to 5 '
                              'times more than one-time buyers, 80% cancelling in month one, and the '
                              'Scooch rebuild cutting ad spend 48% while revenue fell only 5% [6xiaPZPDBCQ '
                              '@ 00:12:48]. Payment failure sits on the churn list too, with the fourth '
                              'card decline treated as a churned customer.',
                              'Retention flows break on timing, triggers and lazy copy. Derek Stroh lists '
                              'the killers he sees in audits: generic thanks, review, buy-more series, '
                              'promo overload, no education, review requests fired before delivery, no '
                              'split between first-time, repeat and VIP buyers, and a first offer bigger '
                              'than the second [cerX0RFHJ0c @ 00:11:51]. Emiel Dingemans calls out the '
                              'common build error of a cart flow that actually runs on a checkout trigger, '
                              'insisting the cart abandonment flow and the checkout abandonment flow are '
                              'two separate flows that both need to be live, built on the newer Shopify '
                              "Added to Cart trigger [6OklvvWTGmw @ 00:21:34]. Gavin Hewitson's fix for "
                              'clashing confirmations is a 20-minute delay so the Shopify or Woo email '
                              "lands first, plus switching off Shopify's own shipping email and applying "
                              'for transactional status so the notice lands in Updates instead of '
                              'Promotions for better deliverability [Cu4iN3jgMwI @ 00:07:54]. On SMS, '
                              'Tarun Brar warns that order phone numbers do not count as consent, US '
                              'abandoned checkout gets one text only, and if SMS costs exceed revenue the '
                              'move is to shrink segments to recent clickers rather than quitting the '
                              'channel [JT1uQ-EOyhM @ 00:14:04].'],
               'table': {'caption': 'Firsthand traps in AI support and retention flows, with the '
                                    'practitioner fix',
                         'headers': ['Failure Mode', 'What Breaks', 'Practitioner Fix', 'Expert Source'],
                         'rows': [['Gorgias macros answering order status questions',
                                   'Macros only read the most recent order, missing other open orders',
                                   'Agent pulls the order via Shopify Get order and lists each open order '
                                   'by number',
                                   'Macha ([VsY0GsB1UI0 @ 00:00:38])'],
                                  ['Per-resolution AI billing as automation improves',
                                   'The AI part of the bill grows with every single resolution',
                                   'Model your real resolution rate before choosing per-resolution or flat '
                                   'pricing',
                                   'Macha ([7Ac3MIM55Yc @ 00:05:06])'],
                                  ['Review requests sent right after the order is placed',
                                   'Buyers get asked to review a product they have not received',
                                   'Wait until after delivery, roughly 7 to 10 days with product in hand',
                                   'Tarun Brar - eCom Email Marketing ([coevagBV6wU @ 00:12:12])'],
                                  ['Cart flow secretly built on a checkout trigger',
                                   'Cart abandoners never enter a flow built for their stage',
                                   'Run separate cart and checkout flows, cart on Shopify Added to Cart',
                                   'Emiel Dingemans | eCommerce Retention Marketing ([6OklvvWTGmw @ '
                                   '00:21:34])'],
                                  ['Welcome flow with 12-hour delays and smart sending left on',
                                   'Sequence fires too tightly and subscribers silently skip flow emails',
                                   'Use 1-day delays and turn smart sending off inside the welcome flow',
                                   'Theo Clough | Email Marketing ([AZHCdf0AuwM @ 00:11:25])'],
                                  ['Subscription card declines treated as a billing afterthought',
                                   'Payment failure quietly becomes one of the five churn reasons',
                                   'Escalate messaging by decline count and treat the fourth decline as '
                                   'churned',
                                   'Milan Raviji│Klaviyo & Email Marketing ([6xiaPZPDBCQ @ 00:11:45])'],
                                  ['Running retention on Shopify Email and judging it by opens',
                                   'Machine opens after iOS 14 make open rate an unreliable success metric',
                                   'Move to Klaviyo or Omnisend and measure flows on clicks instead of '
                                   'opens',
                                   'Carbon Box Media ([wFXlLgdV31A @ 00:06:02])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four checks before AI support and retention flows go live',
                           'body': 'Every item below comes from a pitfall a practitioner hit or flagged '
                                   'directly. Clear all four before turning on automated replies or the '
                                   'post-purchase sequence.',
                           'items': ['Hard-route delivered-not-received, damaged or wrong items, address '
                                     'changes, cancelled or refunded orders, anger and chargebacks to a '
                                     'human, and block any refund or reship the rules do not allow [Macha '
                                     '— VsY0GsB1UI0 @ 00:05:00].',
                                     'Model your own resolution rate before signing a per-resolution AI '
                                     'contract, because the bill grows as the AI resolves more tickets '
                                     '[Macha — iqOjQraqwcM @ 00:03:11].',
                                     'Hold every review request until after delivery, with the product in '
                                     'hand roughly 7 to 10 days [Tarun Brar - eCom Email Marketing — '
                                     'coevagBV6wU @ 00:12:12].',
                                     'Filter post-purchase flows to canceled 0 and refunded 0 since '
                                     'starting so refunded buyers never get thank-you or cross-sell sends '
                                     '[Gavin Hewitson — Cu4iN3jgMwI @ 00:05:58].']}}],
 'pull_quote': '"The AI part of the bill grows with every resolution." — Macha (7Ac3MIM55Yc @ 00:05:06).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Launch the AI agent in safe mode and agree the bar with the team before going live, '
                      'usually about nine in ten drafts approved, with the first category live within a '
                      'week [Macha — VsY0GsB1UI0 @ 00:06:31].',
                      'Gate refunds by policy: send a one-time code to the account email before any refund '
                      'and route every refund over $75 to a manager approval queue [Amol Walunj — '
                      'QZz9_VSA1lA @ 00:02:09].',
                      'Build a Gorgias rule that tags any Shopify last order over $1,000 as a high value '
                      'order, assigns an agent, and alerts you [Brandon Amoroso — Pwv-LlhTPwo @ 00:07:28].',
                      "Trigger the post-purchase flow on Placed Order, wait about 10 minutes for Shopify's "
                      'transactional email, then split on placed order of two or more [Emiel Dingemans | '
                      'eCommerce Retention Marketing — 6OklvvWTGmw @ 00:34:33].',
                      'Add a surprise-and-delight free pouch in box 2 for products with high month-one '
                      'churn, and offer pause, then a discount, then a win-back flow for customers with '
                      'too much product [Milan Raviji│Klaviyo & Email Marketing — 6xiaPZPDBCQ @ 00:05:27].',
                      'Add SMS to post-purchase, replenishment and birthday flows to build loyalty '
                      'alongside email [Klaviyo — zfCLuKMRGEE @ 00:02:56].'],
 'statutory_citations': [{'title': 'Macha — Gorgias AI explained (2026): AI Agent, automation and cost '
                                   '[00:05:06]',
                          'url': 'https://www.youtube.com/watch?v=7Ac3MIM55Yc&t=306s',
                          'relevance': 'Primary practitioner testimony on Gorgias AI Agent plan tiers and '
                                       'how the AI bill scales with resolution rate.'},
                         {'title': 'Macha — AI for "where is my order" tickets in Gorgias [00:06:31]',
                          'url': 'https://www.youtube.com/watch?v=VsY0GsB1UI0&t=391s',
                          'relevance': 'Primary practitioner testimony on WISMO automation rules, human '
                                       'handover cases, and safe-mode launch.'},
                         {'title': 'Tarun Brar - eCom Email Marketing — Klaviyo Tutorial: How to Setup the '
                                   'Post-Purchase Flow 2025 (Step by Step) [00:10:02]',
                          'url': 'https://www.youtube.com/watch?v=coevagBV6wU&t=602s',
                          'relevance': 'Primary practitioner testimony on post-purchase unit economics, '
                                       'flow structure, and review timing.'},
                         {'title': 'Milan Raviji│Klaviyo & Email Marketing — Recharge Subscription Flows '
                                   'Tutorial For 2026 (Full Strategy) [00:06:42]',
                          'url': 'https://www.youtube.com/watch?v=6xiaPZPDBCQ&t=402s',
                          'relevance': 'Primary practitioner testimony on subscription churn reasons and '
                                       'retention flows.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'VsY0GsB1UI0',
                       'title': 'AI for "where is my order" tickets in Gorgias',
                       'channel': 'Macha',
                       'author': 'Macha',
                       'text': 'Before launch, we agree the bar with your team, usually about nine in ten '
                               'drafts approved.',
                       'tip': 'Before launch, we agree the bar with your team, usually about nine in ten '
                              'drafts approved.',
                       'timestamp': 391,
                       'timestamp_seconds': 391,
                       'timestamp_label': '[00:06:31]',
                       'url': 'https://www.youtube.com/watch?v=VsY0GsB1UI0&t=391s',
                       'markdown': '[00:06:31](https://www.youtube.com/watch?v=VsY0GsB1UI0&t=391s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QZz9_VSA1lA',
                       'title': 'How to Automate Gorgias Customer Support with Cevanos AI | Live Demo',
                       'channel': 'Amol Walunj',
                       'author': 'Amol Walunj',
                       'text': 'Any refund over $75 goes to a person through an approval queue.',
                       'tip': 'Any refund over $75 goes to a person through an approval queue.',
                       'timestamp': 129,
                       'timestamp_seconds': 129,
                       'timestamp_label': '[00:02:09]',
                       'url': 'https://www.youtube.com/watch?v=QZz9_VSA1lA&t=129s',
                       'markdown': '[00:02:09](https://www.youtube.com/watch?v=QZz9_VSA1lA&t=129s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eusN-cV9bSQ',
                       'title': 'Gorgias AI Agent review (2026): AI Agent 3.0, price and setup, scored',
                       'channel': 'Macha',
                       'author': 'Macha',
                       'text': 'Our own review comes down to three points.',
                       'tip': 'Our own review comes down to three points.',
                       'timestamp': 246,
                       'timestamp_seconds': 246,
                       'timestamp_label': '[00:04:06]',
                       'url': 'https://www.youtube.com/watch?v=eusN-cV9bSQ&t=246s',
                       'markdown': '[00:04:06](https://www.youtube.com/watch?v=eusN-cV9bSQ&t=246s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'iqOjQraqwcM',
                       'title': 'Best AI agent for Gorgias and Shopify support (2026)',
                       'channel': 'Macha',
                       'author': 'Macha',
                       'text': "Against Gorgias's AI Agent, Macha breaks even only when it resolves close "
                               'to half your tickets.',
                       'tip': "Against Gorgias's AI Agent, Macha breaks even only when it resolves close "
                              'to half your tickets.',
                       'timestamp': 342,
                       'timestamp_seconds': 342,
                       'timestamp_label': '[00:05:42]',
                       'url': 'https://www.youtube.com/watch?v=iqOjQraqwcM&t=342s',
                       'markdown': '[00:05:42](https://www.youtube.com/watch?v=iqOjQraqwcM&t=342s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7Ac3MIM55Yc',
                       'title': 'Gorgias AI explained (2026): AI Agent, automation and cost',
                       'channel': 'Macha',
                       'author': 'Macha',
                       'text': 'The AI part of the bill grows with every resolution.',
                       'tip': 'The AI part of the bill grows with every resolution.',
                       'timestamp': 306,
                       'timestamp_seconds': 306,
                       'timestamp_label': '[00:05:06]',
                       'url': 'https://www.youtube.com/watch?v=7Ac3MIM55Yc&t=306s',
                       'markdown': '[00:05:06](https://www.youtube.com/watch?v=7Ac3MIM55Yc&t=306s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Pwv-LlhTPwo',
                       'title': "Gorgias Overview & Demo | Shopify's #1 Customer Service App",
                       'channel': 'Brandon Amoroso',
                       'author': 'Brandon Amoroso',
                       'text': 'Gorgias drastically reduces the number of hours spent on customer support.',
                       'tip': 'Gorgias drastically reduces the number of hours spent on customer support.',
                       'timestamp': 556,
                       'timestamp_seconds': 556,
                       'timestamp_label': '[00:09:16]',
                       'url': 'https://www.youtube.com/watch?v=Pwv-LlhTPwo&t=556s',
                       'markdown': '[00:09:16](https://www.youtube.com/watch?v=Pwv-LlhTPwo&t=556s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6xiaPZPDBCQ',
                       'title': 'Recharge Subscription Flows Tutorial For 2026 (Full Strategy)',
                       'channel': 'Milan Raviji│Klaviyo & Email Marketing',
                       'author': 'Milan Raviji│Klaviyo & Email Marketing',
                       'text': 'If you keep a customer for 3 months, the likelihood that they stay for '
                               'longer is extraordinarily high.',
                       'tip': 'If you keep a customer for 3 months, the likelihood that they stay for '
                              'longer is extraordinarily high.',
                       'timestamp': 402,
                       'timestamp_seconds': 402,
                       'timestamp_label': '[00:06:42]',
                       'url': 'https://www.youtube.com/watch?v=6xiaPZPDBCQ&t=402s',
                       'markdown': '[00:06:42](https://www.youtube.com/watch?v=6xiaPZPDBCQ&t=402s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wFXlLgdV31A',
                       'title': 'How to 3x Your Email Revenue (Shopify Brand Case Study) | Lifecycle Talks',
                       'channel': 'Carbon Box Media',
                       'author': 'Carbon Box Media',
                       'text': 'Email should be somewhere between 35 and 50 percent of your attributed '
                               'revenue.',
                       'tip': 'Email should be somewhere between 35 and 50 percent of your attributed '
                              'revenue.',
                       'timestamp': 347,
                       'timestamp_seconds': 347,
                       'timestamp_label': '[00:05:47]',
                       'url': 'https://www.youtube.com/watch?v=wFXlLgdV31A&t=347s',
                       'markdown': '[00:05:47](https://www.youtube.com/watch?v=wFXlLgdV31A&t=347s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JT1uQ-EOyhM',
                       'title': 'Klaviyo SMS Marketing Tutorial: Step-by-Step for Beginners',
                       'channel': 'Tarun Brar - eCom Email Marketing',
                       'author': 'Tarun Brar - eCom Email Marketing',
                       'text': "It's basically 14 times higher than email.",
                       'tip': "It's basically 14 times higher than email.",
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=JT1uQ-EOyhM&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=JT1uQ-EOyhM&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'AZHCdf0AuwM',
                       'title': 'Klaviyo Email Marketing For Beginners In (2026 Q4 Tutorial)',
                       'channel': 'Theo Clough | Email Marketing',
                       'author': 'Theo Clough | Email Marketing',
                       'text': 'So, the profitability is like no other and that is why email is your '
                               'highest ROI platform.',
                       'tip': 'So, the profitability is like no other and that is why email is your '
                              'highest ROI platform.',
                       'timestamp': 68,
                       'timestamp_seconds': 68,
                       'timestamp_label': '[00:01:08]',
                       'url': 'https://www.youtube.com/watch?v=AZHCdf0AuwM&t=68s',
                       'markdown': '[00:01:08](https://www.youtube.com/watch?v=AZHCdf0AuwM&t=68s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cerX0RFHJ0c',
                       'title': 'Klaviyo Post Purchase Thank You Flow Strategies',
                       'channel': 'Derek Stroh',
                       'author': 'Derek Stroh',
                       'text': 'So, what we found is that if we can get someone to purchase again in the '
                               'first 30 to 60 days, people are going to come back and loyalty is going to '
                               "be much higher than if we can't do that.",
                       'tip': 'So, what we found is that if we can get someone to purchase again in the '
                              'first 30 to 60 days, people are going to come back and loyalty is going to '
                              "be much higher than if we can't do that.",
                       'timestamp': 575,
                       'timestamp_seconds': 575,
                       'timestamp_label': '[00:09:35]',
                       'url': 'https://www.youtube.com/watch?v=cerX0RFHJ0c&t=575s',
                       'markdown': '[00:09:35](https://www.youtube.com/watch?v=cerX0RFHJ0c&t=575s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'coevagBV6wU',
                       'title': 'Klaviyo Tutorial: How to Setup the Post-Purchase Flow 2025 (Step by Step)',
                       'channel': 'Tarun Brar - eCom Email Marketing',
                       'author': 'Tarun Brar - eCom Email Marketing',
                       'text': 'For example, we want to wait until after delivery to ask for review.',
                       'tip': 'For example, we want to wait until after delivery to ask for review.',
                       'timestamp': 732,
                       'timestamp_seconds': 732,
                       'timestamp_label': '[00:12:12]',
                       'url': 'https://www.youtube.com/watch?v=coevagBV6wU&t=732s',
                       'markdown': '[00:12:12](https://www.youtube.com/watch?v=coevagBV6wU&t=732s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zfCLuKMRGEE',
                       'title': 'Klaviyo SMS & Email Integration: Boost Conversions & Engagement | Klaviyo '
                                'Academy',
                       'channel': 'Klaviyo',
                       'author': 'Klaviyo',
                       'text': 'Try adding SMS to the following flows, post purchase, replenishment and '
                               'birthday flows.',
                       'tip': 'Try adding SMS to the following flows, post purchase, replenishment and '
                              'birthday flows.',
                       'timestamp': 176,
                       'timestamp_seconds': 176,
                       'timestamp_label': '[00:02:56]',
                       'url': 'https://www.youtube.com/watch?v=zfCLuKMRGEE&t=176s',
                       'markdown': '[00:02:56](https://www.youtube.com/watch?v=zfCLuKMRGEE&t=176s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'qaQ0aFPTDKA',
                       'title': 'How to Set Up Post Purchase Flow in Klaviyo 2026 (Quick Guide)',
                       'channel': 'TUTOR BASE',
                       'author': 'TUTOR BASE',
                       'text': 'In this bar, type the words post purchase.',
                       'tip': 'In this bar, type the words post purchase.',
                       'timestamp': 55,
                       'timestamp_seconds': 55,
                       'timestamp_label': '[00:00:55]',
                       'url': 'https://www.youtube.com/watch?v=qaQ0aFPTDKA&t=55s',
                       'markdown': '[00:00:55](https://www.youtube.com/watch?v=qaQ0aFPTDKA&t=55s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cu4iN3jgMwI',
                       'title': 'Klaviyo Post Purchase Flow Tutorial | Shopify Thank You Flow Setup',
                       'channel': 'Gavin Hewitson',
                       'author': 'Gavin Hewitson',
                       'text': "Keep in mind, the second order is typically more profitable because you're "
                               'not spending as much money on advertising to get them across the line.',
                       'tip': "Keep in mind, the second order is typically more profitable because you're "
                              'not spending as much money on advertising to get them across the line.',
                       'timestamp': 796,
                       'timestamp_seconds': 796,
                       'timestamp_label': '[00:13:16]',
                       'url': 'https://www.youtube.com/watch?v=Cu4iN3jgMwI&t=796s',
                       'markdown': '[00:13:16](https://www.youtube.com/watch?v=Cu4iN3jgMwI&t=796s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Cu4iN3jgMwI',
                       'title': 'Klaviyo Post Purchase Flow Tutorial | Shopify Thank You Flow Setup',
                       'channel': 'Gavin Hewitson',
                       'author': 'Gavin Hewitson',
                       'text': 'You get better deliverability if it ends up here.',
                       'tip': 'You get better deliverability if it ends up here.',
                       'timestamp': 474,
                       'timestamp_seconds': 474,
                       'timestamp_label': '[00:07:54]',
                       'url': 'https://www.youtube.com/watch?v=Cu4iN3jgMwI&t=474s',
                       'markdown': '[00:07:54](https://www.youtube.com/watch?v=Cu4iN3jgMwI&t=474s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6OklvvWTGmw',
                       'title': 'Klaviyo Flows Tutorial For Beginners (2025 Full Course for Shopify)',
                       'channel': 'Emiel Dingemans | eCommerce Retention Marketing',
                       'author': 'Emiel Dingemans | eCommerce Retention Marketing',
                       'text': 'This flow is important because right after buying people are still in '
                               'buying mode as we call it.',
                       'tip': 'This flow is important because right after buying people are still in '
                              'buying mode as we call it.',
                       'timestamp': 1688,
                       'timestamp_seconds': 1688,
                       'timestamp_label': '[00:28:08]',
                       'url': 'https://www.youtube.com/watch?v=6OklvvWTGmw&t=1688s',
                       'markdown': '[00:28:08](https://www.youtube.com/watch?v=6OklvvWTGmw&t=1688s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6OklvvWTGmw',
                       'title': 'Klaviyo Flows Tutorial For Beginners (2025 Full Course for Shopify)',
                       'channel': 'Emiel Dingemans | eCommerce Retention Marketing',
                       'author': 'Emiel Dingemans | eCommerce Retention Marketing',
                       'text': 'Between those 10 minutes they will receive a transactional email from '
                               'Shopify.',
                       'tip': 'Between those 10 minutes they will receive a transactional email from '
                              'Shopify.',
                       'timestamp': 2073,
                       'timestamp_seconds': 2073,
                       'timestamp_label': '[00:34:33]',
                       'url': 'https://www.youtube.com/watch?v=6OklvvWTGmw&t=2073s',
                       'markdown': '[00:34:33](https://www.youtube.com/watch?v=6OklvvWTGmw&t=2073s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
