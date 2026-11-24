from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'q9-high-risk-accounts-chargeback-defense',
 'question_prompt': 'How do high-risk merchants get approved, and how do they prevent chargebacks with '
                    'alert networks so they keep their accounts?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'High-Risk Accounts and Chargeback Defense',
 'subtitle': 'High-risk classification and approval; high-risk gateways; supplement brands and payment '
             'routing; staying under card network thresholds; Verifi CDRN, RDR, and Ethoca alerts and '
             'enrollment setup; Verifi RESOLVE, RECOVER, and Inform (TC40/TC15 data)',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'High-risk is a bank underwriting call, not a gateway feature. Adaptiv Payments, '
                      'PaymentCloud and Funnelish all say the acquiring bank decides, and the price is '
                      'higher fees, reserves released in about 3 to 6 months, and a tighter chargeback '
                      "leash. The thresholds cited are Visa's VAMP flag at 1.5% with 1,500 fraud reports "
                      'and disputes, Mastercard at 100 chargebacks and 1.5%, and Visa tightening toward '
                      '0.5%. The street mechanics are a routed multi-processor stack (Stripe default, '
                      'high-risk SKUs to Authorize.net, declines retried on NMI) plus pre-dispute alerts: '
                      'Ethoca and CDRN go live in roughly 12 to 24 hours and RDR in days to weeks, priced '
                      'anywhere from $5 to $40 per alert depending on vendor. Practitioners split on '
                      'whether alerts are core defense or a temporary bandage that hides root causes.',
 'key_metrics': [{'label': 'Visa VAMP US Flag Threshold',
                  'metric': 'Visa VAMP US Flag Threshold',
                  'value': '1.5% with at least 1,500 fraud reports and disputes in a month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Adaptiv Payments' figure for when Visa flags a US merchant, counting fraud "
                             "reports and disputes together against card-not-present sales; Mastercard's "
                             "program starts at 100 chargebacks and 1.5% of the prior month's "
                             'transactions.',
                  'source': 'High-Risk Merchant Accounts | Adaptiv Payments ([NdTgGwtE_N4 @ 00:00:51])'},
                 {'label': 'Per-Alert Pricing (Chargeback.io)',
                  'metric': 'Per-Alert Pricing (Chargeback.io)',
                  'value': '$29 per Ethoca alert; $15 per RDR or CDRN alert',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Chargeback.io's pay-per-alert-received pricing, with a recommendation that "
                             'high-risk merchants enroll in all three providers for broadest coverage.',
                  'source': 'Chargeback ([sH9CslJpDeA @ 00:01:33])'},
                 {'label': 'Subscription App Chargeback Reduction',
                  'metric': 'Subscription App Chargeback Reduction',
                  'value': 'From 13% to under 1%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Georges Rayess deployed both Ethoca and Verifi at a 200,000-user '
                             'subscription app as part of a playbook that cut chargebacks from 13% to '
                             'under one percent.',
                  'source': 'Georges Rayess ([gH8-LQ4srZY @ 00:02:28])'},
                 {'label': 'Reserve Release Window',
                  'metric': 'Reserve Release Window',
                  'value': 'About 3 to 6 months',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "PaymentCloud's timeline for when a high-risk reserve, a percentage of sales "
                             'held in a separate account to cover chargebacks and fraud, is released back '
                             'if all goes well.',
                  'source': 'PaymentCloud ([XwCDjPAfKtY @ 00:03:17])'}],
 'sections': [{'section_number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['The operators agree on one blunt point: high-risk is a label the acquiring '
                              'bank puts on your industry, not a feature of software. Adaptiv Payments '
                              'says gateways like Authorize.net and NMI are neither high-risk nor low-risk '
                              'on their own; a high-risk gateway is simply one wired to a merchant account '
                              'at a bank that approves your vertical, so the real question is which bank '
                              'will underwrite you [D7Ea5oEHwpM @ 00:00:50]. PaymentCloud lists the '
                              'triggers that get you tagged: regulated verticals such as adult, CBD and '
                              'firearms, future-delivery models like tickets, travel and subscriptions, '
                              'and your own creditworthiness [XwCDjPAfKtY @ 00:00:36]. Funnelish narrows '
                              'it for supplement sellers to four drivers: health claims, subscriptions and '
                              'free trials, a category reputation built on years of pay-shipping diet pill '
                              'offers that quietly turned into $80 monthly charges, and restricted '
                              'ingredients like CBD, kratom and testosterone boosters [-G2UpQAf8L0 @ '
                              '00:01:33]. Funnelish also warns that Stripe and PayPal bundle the gateway '
                              'and merchant account together, which is exactly why one decision from them '
                              'can shut everything down at once and leave 90 days of revenue locked inside '
                              '[-G2UpQAf8L0 @ 00:01:18]. PaymentProcessorCom adds that the label does not '
                              'mean you did anything wrong, and that every provider runs different rules, '
                              'so the first question is whether this provider can support what you '
                              'actually sell [q9nKd4oVwnw @ 00:00:47].',
                              'Every speaker prices the label the same way: higher fees, a reserve, and a '
                              'tighter leash. PaymentCloud says high-risk accounts carry higher fees and '
                              'longer settlement periods, plus a reserve agreement that parks a percentage '
                              'of sales in a separate account, released in about 3 to 6 months if all goes '
                              'well [XwCDjPAfKtY @ 00:03:04]. In exchange the merchant gets higher '
                              'chargeback thresholds, fraud tools and a dedicated account manager '
                              '[XwCDjPAfKtY @ 00:01:44]. The thresholds are where the consensus gets '
                              "specific. Adaptiv Payments puts Visa's VAMP flag for US merchants at 1.5% "
                              "with at least 1,500 fraud reports and disputes in a month, and Mastercard's "
                              "program at 100 chargebacks and 1.5% of the previous month's transactions, "
                              'with Mastercard announcing that limit will tighten [NdTgGwtE_N4 @ '
                              '00:01:12]. Scott E. Adams tells merchants who just received a monitoring '
                              'notice that crossing 100 can trigger it but they generally also need to be '
                              'over 0.9%, and to take it seriously without panicking [gROmfVmEsYs @ '
                              '00:00:55]. Pablo Torres of The Reach Network describes Visa moving the '
                              'monthly ratio from 1% to 90 basis points and then toward 0.5% in 2025 '
                              '[fO958wEcK8A @ 00:12:23]. Adaptiv names the end of the road: excessive '
                              'chargebacks is a MATCH list reason code, and most banks step in well before '
                              'the network limits, so the goal is to stay far under them [NdTgGwtE_N4 @ '
                              '00:01:29].',
                              'The third point of agreement: chargeback alerts are a pre-dispute layer, '
                              'and nobody treats them as a substitute for fixing causes. Georges Rayess '
                              'frames Ethoca and Verifi as two halves of one defense, Mastercard and Visa, '
                              'because tools like Stripe Radar stop fraud before authorization but do '
                              'nothing once a settled charge is disputed [gH8-LQ4srZY @ 00:00:00]. A '
                              'dispute intercepted through either network never posts as a chargeback, so '
                              "it never counts toward Mastercard's ECM program or Visa's VAMP [gH8-LQ4srZY "
                              "@ 00:01:34]. Chargeflow's Dove Karp describes the same 24 to 72-hour grace "
                              'period to refund before the chargeback takes root, but concedes alerts are '
                              'a quick fix that does not touch underlying causes and cannot help a '
                              'chargeback that gets through [sBnXe7LYFO8 @ 00:07:04]. Pablo Torres goes '
                              'harder: Ethoca and Verifi should not be used as your fraud or chargeback '
                              'mitigation strategy, only as a break while you find the root issue after an '
                              'attack or an order mix-up [fO958wEcK8A @ 00:10:31]. Funnelish lists the '
                              'root fixes that recur across speakers: compliant claims, obvious '
                              'subscription terms at checkout, a clear billing descriptor, fast support '
                              'replies, easy refunds and shipping confirmations, because a lot of '
                              'chargebacks start as an unanswered question and a refund is almost always '
                              'cheaper than a chargeback [-G2UpQAf8L0 @ 00:05:26].'],
               'table': {'caption': 'Where the high-risk and chargeback-defense practitioners line up',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['The bank, not the gateway, decides risk',
                                   'Authorize.net and NMI are neither high-risk nor low-risk on their own; '
                                   'the underwriting bank decides',
                                   'Shop for the acquiring bank that approves your industry before picking '
                                   'software',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([D7Ea5oEHwpM @ '
                                   '00:00:50])'],
                                  ['Industry and delivery model trigger the label',
                                   'Adult, CBD, firearms, tickets, travel, subscriptions and weak credit '
                                   'get merchants tagged high-risk',
                                   'Expect closer underwriting, background checks and longer approval '
                                   'times on these verticals',
                                   'PaymentCloud ([XwCDjPAfKtY @ 00:00:36])'],
                                  ['Reserves are standard on high-risk accounts',
                                   'A percentage of sales sits in a separate account, released in roughly '
                                   '3 to 6 months',
                                   'Model cash flow around held funds before paying suppliers ahead of '
                                   'shipping',
                                   'PaymentCloud ([XwCDjPAfKtY @ 00:03:17])'],
                                  ['Network monitoring thresholds are tight',
                                   'Visa VAMP flags at 1.5% with 1,500 events; Mastercard at 100 '
                                   'chargebacks and 1.5%',
                                   'Stay far under the limits because banks step in well before networks '
                                   'do',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([NdTgGwtE_N4 @ '
                                   '00:01:12])'],
                                  ['Intercepted disputes stay off the ratio',
                                   'Disputes caught by Ethoca or Verifi never post as chargebacks under '
                                   'ECM or VAMP',
                                   'Run both networks because no single product covers Visa and Mastercard '
                                   'together',
                                   'Georges Rayess ([gH8-LQ4srZY @ 00:01:34])'],
                                  ['Alerts are a bandage, not the cure',
                                   'Ethoca and Verifi buy a break while you fix descriptors, fulfillment '
                                   'and customer communication',
                                   'Keep reading every dispute so the root cause actually gets fixed over '
                                   'time',
                                   'The Reach Network ([fO958wEcK8A @ 00:10:31])'],
                                  ['Never rely on a single processor',
                                   'Bundled processors like Stripe and PayPal can shut down everything '
                                   'with one decision',
                                   'Spread volume across two or more accounts and route risky products '
                                   'correctly',
                                   'Funnelish ([-G2UpQAf8L0 @ 00:07:44])']]}},
              {'section_number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Start with the stack. Adaptiv Payments splits every card payment into three '
                              'pieces: the gateway captures the card, the processor carries it through the '
                              'networks, and the merchant account at the acquiring bank settles it '
                              '[D7Ea5oEHwpM @ 00:00:15]. Check your cart before applying: WooCommerce runs '
                              'most gateways at no extra cost, while Shopify charges an outside-gateway '
                              'fee of 2% on Basic, 1% on Grow, 0.6% on Advanced and 0.2% on Plus '
                              '[D7Ea5oEHwpM @ 00:01:29]. The underwriting file is website terms, refund '
                              'policy and contact details, formation documents and EIN, ID for every owner '
                              'at 25% or more, and 3 to 6 months of processing statements, with approval '
                              'taking a few days to a few weeks [D7Ea5oEHwpM @ 00:03:58]. '
                              'PaymentProcessorCom says to disclose any prior closure, because tweaking '
                              'your description to hide a past issue causes bigger problems later '
                              '[q9nKd4oVwnw @ 00:01:50]. Funnelish runs a route called main failover: '
                              'Stripe takes every payment by default, products tagged high-risk go to '
                              'Authorize.net on a high-risk merchant account, and declines retry '
                              'automatically on NMI tied to a second merchant account, with rules checked '
                              'top to bottom [-G2UpQAf8L0 @ 00:06:55]. Adaptiv draws the hard line: '
                              'separate business lines can each carry their own account and descriptor, '
                              'but splitting one business across accounts to hide chargebacks breaks '
                              'network rules, and Visa can fine $25,000 per merchant, per month '
                              '[D7Ea5oEHwpM @ 00:03:41].',
                              'Alert enrollment is where the numbers get concrete. Chargeback.io lists '
                              'coverage: Ethoca covers 95% of Mastercard transactions, RDR covers 97% of '
                              'Visa transactions, and CDRN covers US transactions only, hitting 95% of '
                              'Visa among them [sH9CslJpDeA @ 00:00:18]. Ethoca and CDRN go live in up to '
                              '12 business hours versus up to 72 for RDR; Ethoca and CDRN need only a '
                              'billing descriptor, while RDR also needs ARN and CAID codes; pricing is $29 '
                              'per Ethoca alert and $15 for RDR or CDRN, and the shop recommends high-risk '
                              'merchants enroll in all three, medium-risk in Ethoca and RDR [sH9CslJpDeA @ '
                              '00:01:33]. Scott E. Adams clocks CDRN and Ethoca at under 24 hours, while '
                              'RDR can take days or weeks depending on getting BIN and CAIDs from a '
                              'processor that is sometimes wrong, so submit what you have, ARNs included, '
                              'and let Visa research it [gROmfVmEsYs @ 00:01:32]. Pricing swings hard by '
                              'vendor. Chargeflow cites a uniform $40 per alert charged regardless of '
                              'success, with Verifi mostly covering US issuers and Ethoca reaching banks '
                              'in Europe, Asia and Canada [sBnXe7LYFO8 @ 00:06:00]. Georges Rayess puts '
                              'the alert fee at $5 to $15 against a $15 to $25 chargeback fee, arguing the '
                              'ratio protection matters more than the per-alert cost [gH8-LQ4srZY @ '
                              '00:01:34].',
                              'Execution detail is where operators separate. RDR runs on rules you '
                              'configure once, and Visa resolves matching disputes in real time; Georges '
                              'Rayess says the 24 to 72-hour alert window is too tight for manual review '
                              'at any real volume, which makes RDR the high-leverage piece, though it '
                              'auto-refunds disputes you might have won, so calibrate rules to your reason '
                              'mix [gH8-LQ4srZY @ 00:01:53]. On Ethoca, Scott E. Adams sets 24 hours as '
                              'the rule of thumb, close to a sure thing inside that window, and says late '
                              'responses still tend to work, so respond anyway [Ghanuu5dNMk @ 00:01:34]. '
                              'Adams also pushes Verifi Inform as one of the most important products in '
                              'the mix: it delivers the TC40 fraud file and TC15 chargeback file in near '
                              'real time, the only practical way to track fraud-flagged transactions that '
                              'issuers never charge back, usually on low-ticket items [gJ_2exzq6FA @ '
                              '00:01:00]. That speed lets you stop a shipment, disentitle a digital good '
                              'or block repeat purchases [gJ_2exzq6FA @ 00:02:31]. When a chargeback does '
                              'land, Adaptiv Payments matches evidence to the reason code: tracking and '
                              'delivery confirmation for not-received, agreed terms and cancellation '
                              'records for subscriptions, and Compelling Evidence 3.0 for Visa friendly '
                              'fraud, pointing to two earlier undisputed purchases on the same card with '
                              'matching IP address or device [NdTgGwtE_N4 @ 00:03:50].'],
               'table': {'caption': 'Street-level numbers, tools and settings the practitioners actually '
                                    'run',
                         'headers': ['Mechanic',
                                     'Exact Number or Tool',
                                     'How Operators Execute It',
                                     'Expert Source'],
                         'rows': [['Shopify outside-gateway surcharge',
                                   '2% Basic, 1% Grow, 0.6% Advanced, 0.2% Plus',
                                   'Price the platform surcharge before wiring an external high-risk '
                                   'gateway',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([D7Ea5oEHwpM @ '
                                   '00:01:29])'],
                                  ['Alert network coverage',
                                   'Ethoca 95% Mastercard; RDR 97% Visa; CDRN US-only at 95% Visa',
                                   'Enroll in all three if high-risk; Ethoca plus RDR if medium-risk',
                                   'Chargeback ([sH9CslJpDeA @ 00:00:18])'],
                                  ['Alert go-live timing',
                                   'CDRN and Ethoca under 24 hours; RDR days to weeks',
                                   'Turn on CDRN and Ethoca first, then chase BIN and CAIDs for RDR',
                                   'Scott E. Adams | Chargeback Expert ([gROmfVmEsYs @ 00:02:13])'],
                                  ['CDRN decision window',
                                   '72 hours to refund or let the chargeback flow',
                                   'Match the case in your gateway by ARN, amount and date inside Verifi '
                                   'One',
                                   'Verifi, A Visa Solution ([0mvbNuyEem8 @ 00:01:23])'],
                                  ['Sample RDR rule set',
                                   'Under $50, fraud-category reason code, chosen currency',
                                   'Refunds fire at the acquiring level; merchant receives an '
                                   'informational notice only',
                                   'The Reach Network ([fO958wEcK8A @ 00:02:49])'],
                                  ['Third-party alert auto-refund threshold',
                                   'Anything under $100 in a set currency refunded automatically',
                                   'Let the alert provider clear small tickets so the inbox is not flooded',
                                   'The Reach Network ([fO958wEcK8A @ 00:01:49])'],
                                  ['Visa decline retry ceiling',
                                   'Up to 20 retries in 30 days on approvable declines',
                                   'Set gateway retry logic and never retry declines that will never '
                                   'approve',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([D7Ea5oEHwpM @ '
                                   '00:03:23])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small moves that keep the account alive',
                           'body': 'Four operator-level habits pulled straight from the people running '
                                   'high-risk books and alert programs.',
                           'items': ["Spend five minutes reading your processor's restricted businesses "
                                     'list before you scale; it is almost certainly on their site and can '
                                     'save a shutdown [Funnelish — -G2UpQAf8L0 @ 00:03:22]',
                                     'Kill fraud before you ship: once an issuer logs a fraud report it '
                                     "counts toward Visa's ratio even if you refund the order later "
                                     '[High-Risk Merchant Accounts | Adaptiv Payments — NdTgGwtE_N4 @ '
                                     '00:02:37]',
                                     "Test Ethoca's former safe feed of cancelled-card fraud data; "
                                     'lower-ticket or higher-risk merchants tend to just refund all of '
                                     'them, higher-ticket merchants may not [Scott E. Adams | Chargeback '
                                     'Expert — Ghanuu5dNMk @ 00:02:32]',
                                     'Use Verifi Inform to pull the exact descriptors on each transaction '
                                     'and as the feedback loop for Compelling Evidence 3.0 and Order '
                                     'Insight pings [Scott E. Adams | Chargeback Expert — gJ_2exzq6FA @ '
                                     '00:03:19]']},
               'sop_steps': [{'step': 1,
                              'title': 'Build an underwriting-ready file',
                              'action': 'Assemble documents and clean up the website before applying to a '
                                        'high-risk provider.',
                              'detail': 'Bring formation documents, EIN, ID for every 25%-plus owner and 3 '
                                        'to 6 months of statements, and make price, delivery, refund '
                                        'policy and subscription cancellation obvious to a first-time '
                                        'buyer [High-Risk Merchant Accounts | Adaptiv Payments — '
                                        'D7Ea5oEHwpM @ 00:03:58] [PaymentProcessorCom — q9nKd4oVwnw @ '
                                        '00:02:06]'},
                             {'step': 2,
                              'title': 'Wire a routed, redundant stack',
                              'action': 'Connect the high-risk merchant account through a supported '
                                        'gateway and set routing rules.',
                              'detail': 'Default low-risk volume to Stripe, send high-risk tagged products '
                                        'to Authorize.net on a high-risk account, and auto-retry declines '
                                        'on NMI tied to a second merchant account so a single problem '
                                        'never kills the sale [Funnelish — -G2UpQAf8L0 @ 00:07:11]'},
                             {'step': 3,
                              'title': 'Enroll alerts fast, then RDR',
                              'action': 'Turn on CDRN and Ethoca for immediate coverage, then complete RDR '
                                        'enrollment.',
                              'detail': 'Find out why you are in a program, talk to your processor, get '
                                        'CDRN and Ethoca live for quick coverage, then get into RDR once '
                                        'BIN and CAIDs are submitted [Scott E. Adams | Chargeback Expert — '
                                        'gROmfVmEsYs @ 00:03:09]'},
                             {'step': 4,
                              'title': 'Work the queue and fight only winnable disputes',
                              'action': 'Resolve each alert in the portal and reserve representment for '
                                        'disputes you can win.',
                              'detail': 'Match each CDRN case by ARN, amount and date and record the '
                                        'outcome in Verifi One [Verifi, A Visa Solution — 0mvbNuyEem8 @ '
                                        '00:01:23]; refund when the customer has a point or the order is '
                                        'small, and track win results by reason code [High-Risk Merchant '
                                        'Accounts | Adaptiv Payments — NdTgGwtE_N4 @ 00:04:11]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over how many alert networks to stack. Georges Rayess '
                              'frames Ethoca and Verifi as two halves of one defense, Mastercard on one '
                              'side and Visa on the other, and insists there is no overlap and no single '
                              "product covers both networks, so running only one leaves the other brand's "
                              'disputes uncovered [gH8-LQ4srZY @ 00:02:28]. Scott E. Adams draws the map '
                              'less cleanly: CDRN is mostly Visa and Ethoca is mostly Mastercard, but both '
                              'carry some coverage on both networks and can handle Discover and Amex '
                              'depending on how the merchant is set up [gROmfVmEsYs @ 00:02:13]. '
                              'Chargeflow turns that overlap into a cost leak, warning that enrolling in '
                              "both can fire double dispute alerts when a cardholder's bank sits in both "
                              'networks, which means double fees, so the golden rule is a cost-benefit '
                              'analysis before committing [sBnXe7LYFO8 @ 00:06:18]. Sequencing splits the '
                              'field too. Rayess says that if engineering time is tight, start with Verifi '
                              'RDR because it is configure once and then autonomous. Adams runs the '
                              'opposite order for merchants hit with a monitoring-program notice: get CDRN '
                              'and Ethoca live for quick coverage, because both can be running in about 24 '
                              'hours, then get into RDR and go from there [gROmfVmEsYs @ 00:03:09].',
                              'Nobody quotes the same price for an alert, and the spread changes the math. '
                              'Chargeflow says both Verifi CDRN and Ethoca levy a uniform $40 charge for '
                              'each alert received, regardless of its success, then pitches its own '
                              'bundled layer as paying only for alerts that actually prevented a '
                              'chargeback, with no duplicate charges [sBnXe7LYFO8 @ 00:06:00]. '
                              'Chargeback.io quotes $29 per Ethoca alert and a shared $15 rate for RDR and '
                              'CDRN, billed only for alerts received, and needs nothing but a billing '
                              'descriptor to enroll Ethoca and CDRN [sH9CslJpDeA @ 00:01:33]. Georges '
                              'Rayess pegs the intercept at roughly $5 to $15 per alert against a $15 to '
                              '$25 chargeback fee, and argues the per-alert fee matters less than the '
                              'ratio, because an intercepted dispute never posts as a chargeback and never '
                              "counts toward Mastercard's ECM program or Visa's VAMP [gH8-LQ4srZY @ "
                              '00:01:34]. Pablo Torres remembers the older resistance: merchants Torres '
                              'talked to asked why they should pay $35 for an alert when they could just '
                              'focus on not getting the chargeback at all, which Torres calls the right '
                              'attitude [fO958wEcK8A @ 00:10:04]. Read side by side, the same alert ranges '
                              'from $5 to $40 depending on the vendor quoting it.',
                              'The deepest philosophical fight is whether to refund on autopilot or keep '
                              'eyes on every dispute. Adams pitches Ethoca partly as a way to automate the '
                              'chargeback process and just not worry about it, and suggests lower-ticket '
                              'or higher-risk merchants simply refund the SAFE fraud-feed alerts while '
                              'higher-ticket or lower-risk merchants test and possibly skip them '
                              '[Ghanuu5dNMk @ 00:02:49]. Rayess flags the cost of autopilot: RDR '
                              'auto-refunds disputes you might have won in representment, so the rules '
                              'have to be calibrated to your reason-code mix [gH8-LQ4srZY @ 00:01:53]. '
                              'Pablo Torres goes further, arguing Ethoca and Verifi should not be a fraud '
                              'or chargeback mitigation strategy at all, only a short break while the root '
                              'issue gets fixed, and that asking a vendor to stop telling you about '
                              'refunds is turning a blind eye [fO958wEcK8A @ 00:10:31]. On the fight side, '
                              'Adaptiv Payments says save representment for the disputes you can actually '
                              'win, and refund when the customer has a point or the order was small '
                              '[NdTgGwtE_N4 @ 00:04:11]. Adaptiv also says to track results by reason '
                              'code, so you know which fixes are working, which is the opposite of the '
                              'inbox-silencing setup Torres warns against.'],
               'table': {'caption': 'Side-by-side playbooks where chargeback practitioners split on '
                                    'alerts, pricing, timing and account strategy',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which alert networks to enroll in first',
                                   'Rayess: start with Verifi RDR because it is configure once and '
                                   'autonomous',
                                   'Adams: get CDRN and Ethoca live in about 24 hours, then add RDR',
                                   'Georges Rayess ([gH8-LQ4srZY @ 00:02:28]); Scott E. Adams | Chargeback '
                                   'Expert ([gROmfVmEsYs @ 00:03:09])'],
                                  ['How many alert providers a high-risk merchant needs',
                                   'Chargeback.io: high-risk merchants enroll in Ethoca, RDR and CDRN all '
                                   'together',
                                   'Chargeflow: stacking Verifi and Ethoca risks double alerts and double '
                                   'fees',
                                   'Chargeback ([sH9CslJpDeA @ 00:01:33]); Chargeflow ([sBnXe7LYFO8 @ '
                                   '00:06:18])'],
                                  ['Price actually paid per intercepted dispute alert notification',
                                   'Chargeflow quotes $40 per alert on both networks regardless of success',
                                   'Chargeback.io quotes $29 Ethoca and $15 RDR or CDRN; Rayess quotes $5 '
                                   'to $15',
                                   'Chargeflow ([sBnXe7LYFO8 @ 00:06:00]); Chargeback ([sH9CslJpDeA @ '
                                   '00:01:33]); Georges Rayess ([gH8-LQ4srZY @ 00:01:34])'],
                                  ['Response window after a pre-dispute alert lands',
                                   'Verifi CDRN gives the merchant 72 hours to refund or let it flow',
                                   'Adams: Ethoca rule of thumb is 24 hours, though slightly late often '
                                   'still works',
                                   'Verifi, A Visa Solution ([0mvbNuyEem8 @ 00:00:48]); Scott E. Adams | '
                                   'Chargeback Expert ([Ghanuu5dNMk @ 00:01:34])'],
                                  ['Whether RDR disputes count against your ratio',
                                   "Adaptiv: disputes resolved through RDR do not count toward Visa's "
                                   'ratio',
                                   'Adams: not supposed to count, but downstream processors often miss the '
                                   'M flag',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([NdTgGwtE_N4 @ '
                                   '00:03:15]); Scott E. Adams | Chargeback Expert ([5mi35dvcRrA @ '
                                   '00:03:50])'],
                                  ['Refund fraud-flagged transactions or hold the line',
                                   'Adams on Ethoca SAFE feed: lower-ticket and higher-risk merchants just '
                                   'refund them all',
                                   'Adams on TC40 fraud flags via Inform: generally do not refund, stop '
                                   'the shipment instead',
                                   'Scott E. Adams | Chargeback Expert ([Ghanuu5dNMk @ 00:02:49]); Scott '
                                   'E. Adams | Chargeback Expert ([gJ_2exzq6FA @ 00:03:02])'],
                                  ['Whether supplement-style brands need a high-risk account immediately',
                                   'Funnelish: most do not on day one, but route risky SKUs and keep a '
                                   'backup',
                                   'PaymentCloud: a high-risk merchant account protects a high-risk '
                                   'business from financial risk',
                                   'Funnelish ([-G2UpQAf8L0 @ 00:07:44]); PaymentCloud ([XwCDjPAfKtY @ '
                                   '00:01:27])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The first trap is building the whole business on one processor. Funnelish '
                              'opens on the nightmare case: sales start coming in and the payment account '
                              'gets frozen with 90 days of revenue locked inside, a pattern common for '
                              'supplement, skin care, CBD and subscription brands [-G2UpQAf8L0 @ '
                              '00:00:00]. Because Stripe and PayPal bundle the gateway and the merchant '
                              'account, one decision from them can shut down everything at once, and '
                              'jumping 10 times your volume overnight is a great way to get noticed '
                              '[-G2UpQAf8L0 @ 00:06:03]. A high-risk account is not a free pass either; '
                              'Funnelish warns you can still lose it if chargebacks climb too high. The '
                              'thresholds are lower than most operators assume. Scott E. Adams says a '
                              'monitoring-program notice can trigger at over 100 chargebacks combined with '
                              'a ratio generally over 0.9 percent, and that merchants with no real '
                              'relationship with their bank often have no idea what to do when it lands '
                              '[gROmfVmEsYs @ 00:00:55]. Adaptiv Payments adds that excessive chargebacks '
                              'is a reason code for the MATCH list, and that most banks step in well '
                              'before the network limits, so the target is to stay far under them, not '
                              'just under the line [NdTgGwtE_N4 @ 00:01:29].',
                              'The second cluster of losses comes from data the merchant never sees. '
                              'Adaptiv Payments flags the detail most merchants miss: once a bank logs a '
                              "fraud report, it counts toward Visa's ratio even if you refund the order "
                              'later, so fraud has to be stopped before you ship [NdTgGwtE_N4 @ 00:02:37]. '
                              'Adams explains why that bites low-ticket sellers hardest: issuers often '
                              'flag a cheap transaction as fraud without bothering to charge it back, and '
                              "that flag still goes against you in Visa's fraud monitoring, so watching "
                              'chargebacks alone leaves you blind and the TC40 file becomes critical '
                              '[gJ_2exzq6FA @ 00:01:17]. RDR carries its own reporting trap. The refund is '
                              'pulled by the acquirer and marked with what Adams believes is an M flag, '
                              'but processors, ISOs and gateways further down the chain often never get '
                              'that change, see a chargeback, and treat it as one, so you have to track it '
                              'really carefully; RDR also does nothing to keep you out of the fraud '
                              'program [5mi35dvcRrA @ 00:04:08]. Alerts, by contrast, more often clear '
                              'both the fraud flag and the chargeback, and Adams reports good luck getting '
                              'clients out of monitoring programs with alerts and RDR in combination '
                              '[5mi35dvcRrA @ 00:05:19].',
                              'The last set of traps is operational and shows up directly in the margin. '
                              'Chargeback.io warns that without a gateway integration, Ethoca and CDRN '
                              'alerts cannot be matched to the transaction, so you manually locate and '
                              'refund every single alert, while only RDR refunds automatically without '
                              'integration [sH9CslJpDeA @ 00:00:50]. Rayess says that at any real volume '
                              'the 24 to 72-hour window is too tight for manual review, which is the whole '
                              "case for RDR's automation [gH8-LQ4srZY @ 00:01:53]. Pablo Torres describes "
                              'the small-team version of the failure: a one or two person dropshipping '
                              'operation marking goods up 200 to 300 percent cannot keep up with customer '
                              'inquiries, things fall off the side, and chargebacks follow; silence the '
                              'alerts on top of that and you cannot see the disease [fO958wEcK8A @ '
                              '00:05:58]. Adaptiv Payments closes the cheapest escape route: splitting one '
                              'business across several accounts to hide chargebacks breaks card network '
                              'rules, and Visa can fine $25,000 per merchant, per month [D7Ea5oEHwpM @ '
                              '00:03:41]. Adaptiv draws the line clearly: separate business lines can each '
                              'carry their own merchant account and descriptor, one business split to mask '
                              'its ratio cannot.'],
               'table': {'caption': 'Firsthand failure modes with the economics check each practitioner '
                                    'attaches to them',
                         'headers': ['Failure Mode',
                                     'What Practitioners Report',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Single bundled processor freezes the entire revenue stream',
                                   'Account frozen with 90 days of revenue locked inside after sales start',
                                   'Route risky SKUs to a high-risk account and keep an NMI failover',
                                   'Funnelish ([-G2UpQAf8L0 @ 00:00:00]); Funnelish ([-G2UpQAf8L0 @ '
                                   '00:07:11])'],
                                  ['Refunding fraud after the bank already logged it',
                                   "A logged fraud report counts toward Visa's ratio even after a refund",
                                   'Stop fraud at checkout with address and CVV checks, 3-D Secure and '
                                   'velocity limits',
                                   'High-Risk Merchant Accounts | Adaptiv Payments ([NdTgGwtE_N4 @ '
                                   '00:02:37])'],
                                  ['RDR refunds misread as chargebacks further down the chain',
                                   'Gateways, ISOs or processors miss the M flag and see a chargeback',
                                   'Track every RDR case carefully against what your processor reports as '
                                   'chargebacks',
                                   'Scott E. Adams | Chargeback Expert ([5mi35dvcRrA @ 00:04:08])'],
                                  ['Duplicate alerts from enrolling in both Verifi and Ethoca',
                                   "Same dispute fires twice when the cardholder's bank participates in "
                                   'both networks',
                                   'Each alert carries a $40 fee regardless of whether it succeeds',
                                   'Chargeflow ([sBnXe7LYFO8 @ 00:06:18]); Chargeflow ([sBnXe7LYFO8 @ '
                                   '00:05:28])'],
                                  ['Manual alert handling without a payment gateway integration',
                                   'Ethoca and CDRN alerts cannot be auto-matched, forcing manual '
                                   'locate-and-refund work',
                                   'Integrate the gateway, or lean on RDR, which refunds without any '
                                   'integration',
                                   'Chargeback ([sH9CslJpDeA @ 00:00:50]); Georges Rayess ([gH8-LQ4srZY @ '
                                   '00:01:53])'],
                                  ['Reserve and settlement holds starving supplier cash flow',
                                   'Reserves hold a percentage of sales, released in about three to six '
                                   'months',
                                   'Ask how much is held, how long, and release conditions before signing',
                                   'PaymentCloud ([XwCDjPAfKtY @ 00:03:17]); PaymentProcessorCom '
                                   '([q9nKd4oVwnw @ 00:03:16])'],
                                  ['Hiding a past account closure on the new application',
                                   'Tweaking your business description to hide a past issue causes bigger '
                                   'problems later',
                                   'Disclose the closure and bring statements plus a reason-code '
                                   'chargeback report',
                                   'PaymentProcessorCom ([q9nKd4oVwnw @ 00:01:50]); High-Risk Merchant '
                                   'Accounts | Adaptiv Payments ([NdTgGwtE_N4 @ 00:04:27])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Kill-Switch Checks Before You Scale Volume',
                           'body': 'Every item below is a loss or reversal practitioners reported '
                                   'firsthand. Clear all four before pushing ad spend or adding a new '
                                   'product line.',
                           'items': ['Confirm a backup merchant account and routing rule are live before '
                                     'scaling; jumping 10 times your volume overnight gets you noticed and '
                                     'one bundled provider can shut everything down [Funnelish — '
                                     '-G2UpQAf8L0 @ 00:06:03].',
                                     'Do not treat a refund as a fraud fix: once the issuer logs a fraud '
                                     "report it counts toward Visa's ratio, so block suspect orders before "
                                     'shipment [High-Risk Merchant Accounts | Adaptiv Payments — '
                                     'NdTgGwtE_N4 @ 00:02:37].',
                                     'Reconcile every RDR case against processor chargeback reports '
                                     'because downstream ISOs and gateways often miss the M flag and see a '
                                     'chargeback [Scott E. Adams | Chargeback Expert — 5mi35dvcRrA @ '
                                     '00:04:08].',
                                     'Never split one business across accounts to mask a ratio; Visa can '
                                     'fine $25,000 per merchant, per month [High-Risk Merchant Accounts | '
                                     'Adaptiv Payments — D7Ea5oEHwpM @ 00:03:41].']}}],
 'pull_quote': '"How do you know that you\'re sick when you can\'t see the disease? But if you\'re not '
               'seeing the chargebacks, how are you supposed to improve as a business?" — Pablo Torres, '
               'The Reach Network (fO958wEcK8A @ 00:09:07).',
 'diagram_id': 'diag-05',
 'action_checklist': ['Enroll your billing descriptors in Verifi CDRN and Ethoca first for coverage inside '
                      'about 24 hours, then submit BINs and CAIDs from your processor to get RDR live '
                      '[Scott E. Adams | Chargeback Expert — gROmfVmEsYs @ 00:01:32].',
                      'Connect your alert provider to your payment gateway so Ethoca and CDRN alerts are '
                      'matched and refunded automatically instead of by hand [Chargeback — sH9CslJpDeA @ '
                      '00:01:04].',
                      'Calibrate RDR rules to your reason-code mix so it does not auto-refund disputes you '
                      'could have won in representment [Georges Rayess — gH8-LQ4srZY @ 00:01:53].',
                      'Pull TC40 and TC15 data through Verifi Inform to see fraud flags in real time, stop '
                      'shipments and disentitle digital goods [Scott E. Adams | Chargeback Expert — '
                      'gJ_2exzq6FA @ 00:02:45].',
                      'Build a routing rule set: Stripe as default, high-risk tagged products to '
                      'Authorize.net on a high-risk merchant account, and declines retried on NMI '
                      '[Funnelish — -G2UpQAf8L0 @ 00:06:55].',
                      'Before applying, assemble 3 to 6 months of processing statements, a chargeback '
                      'report by reason code, and your fixes to descriptor, refund policy, fraud tools and '
                      'alerts [High-Risk Merchant Accounts | Adaptiv Payments — NdTgGwtE_N4 @ 00:04:27].'],
 'statutory_citations': [{'title': 'Scott E. Adams | Chargeback Expert — Rapid Dispute Resolution (RDR) vs '
                                   "Verifi CDRN and Ethoca Alerts - What's the Difference? [00:04:08]",
                          'url': 'https://www.youtube.com/watch?v=5mi35dvcRrA&t=248s',
                          'relevance': 'Primary practitioner testimony on RDR M-flag reporting gaps and '
                                       'fraud-program exposure.'},
                         {'title': 'Georges Rayess — Ethoca vs Verifi: The Two Dispute-Interception '
                                   'Networks Every Subscription App Needs [00:01:34]',
                          'url': 'https://www.youtube.com/watch?v=gH8-LQ4srZY&t=94s',
                          'relevance': 'Primary practitioner testimony on alert fees versus chargeback '
                                       'fees and ratio impact.'},
                         {'title': 'High-Risk Merchant Accounts | Adaptiv Payments — Chargeback '
                                   'Prevention: How to Stop Chargebacks and Keep Your Merchant Account '
                                   '(2026) [00:02:37]',
                          'url': 'https://www.youtube.com/watch?v=NdTgGwtE_N4&t=157s',
                          'relevance': 'Primary practitioner testimony on fraud reports counting toward '
                                       "Visa's ratio after refunds."},
                         {'title': 'The Reach Network — True Fraud #8 - Avoid Chargeback Blind Spots With '
                                   'Ethoca and Verifi [00:10:31]',
                          'url': 'https://www.youtube.com/watch?v=fO958wEcK8A&t=631s',
                          'relevance': 'Primary practitioner testimony on alerts as a temporary break '
                                       'rather than a core strategy.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'D7Ea5oEHwpM',
                       'title': 'High-Risk Payment Gateway: What It Is and How to Get One (2026)',
                       'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
                       'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
                       'text': 'Splitting one business across several accounts to hide chargebacks breaks '
                               'the card network rules. Visa can fine $25,000 per merchant, per month.',
                       'tip': 'Splitting one business across several accounts to hide chargebacks breaks '
                              'the card network rules. Visa can fine $25,000 per merchant, per month.',
                       'timestamp': 221,
                       'timestamp_seconds': 221,
                       'timestamp_label': '[00:03:41]',
                       'url': 'https://www.youtube.com/watch?v=D7Ea5oEHwpM&t=221s',
                       'markdown': '[00:03:41](https://www.youtube.com/watch?v=D7Ea5oEHwpM&t=221s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XwCDjPAfKtY',
                       'title': 'High-Risk Merchant Accounts EXPLAINED: What to Do If Your Business Is '
                                'Considered High-Risk',
                       'channel': 'PaymentCloud',
                       'author': 'PaymentCloud',
                       'text': 'With reserves, a percentage of your sales are held in a separate account '
                               'to cover any possible losses that your business might experience due to '
                               'chargebacks and fraud.',
                       'tip': 'With reserves, a percentage of your sales are held in a separate account to '
                              'cover any possible losses that your business might experience due to '
                              'chargebacks and fraud.',
                       'timestamp': 184,
                       'timestamp_seconds': 184,
                       'timestamp_label': '[00:03:04]',
                       'url': 'https://www.youtube.com/watch?v=XwCDjPAfKtY&t=184s',
                       'markdown': '[00:03:04](https://www.youtube.com/watch?v=XwCDjPAfKtY&t=184s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NdTgGwtE_N4',
                       'title': 'Chargeback Prevention: How to Stop Chargebacks and Keep Your Merchant '
                                'Account (2026)',
                       'channel': 'High-Risk Merchant Accounts | Adaptiv Payments',
                       'author': 'High-Risk Merchant Accounts | Adaptiv Payments',
                       'text': "Once a bank logs a fraud report, it counts toward Visa's ratio, even if "
                               'you refund the order later. So stop fraud before you ship, not after.',
                       'tip': "Once a bank logs a fraud report, it counts toward Visa's ratio, even if you "
                              'refund the order later. So stop fraud before you ship, not after.',
                       'timestamp': 157,
                       'timestamp_seconds': 157,
                       'timestamp_label': '[00:02:37]',
                       'url': 'https://www.youtube.com/watch?v=NdTgGwtE_N4&t=157s',
                       'markdown': '[00:02:37](https://www.youtube.com/watch?v=NdTgGwtE_N4&t=157s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'q9nKd4oVwnw',
                       'title': 'How to Get a High Risk Merchant Account',
                       'channel': 'PaymentProcessorCom',
                       'author': 'PaymentProcessorCom',
                       'text': 'If a previous provider closed your account, be upfront about what '
                               'happened. Tweaking your business description to hide a past issue can '
                               'cause bigger problems later.',
                       'tip': 'If a previous provider closed your account, be upfront about what happened. '
                              'Tweaking your business description to hide a past issue can cause bigger '
                              'problems later.',
                       'timestamp': 110,
                       'timestamp_seconds': 110,
                       'timestamp_label': '[00:01:50]',
                       'url': 'https://www.youtube.com/watch?v=q9nKd4oVwnw&t=110s',
                       'markdown': '[00:01:50](https://www.youtube.com/watch?v=q9nKd4oVwnw&t=110s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-G2UpQAf8L0',
                       'title': 'Do All Supplement Brands Need a High Risk Merchant Account? (+ Payment '
                                'Routing)',
                       'channel': 'Funnelish',
                       'author': 'Funnelish',
                       'text': 'Some companies like Stripe and PayPal bundle the payment gateway and the '
                               'merchant account together, which is exactly why one decision from them can '
                               'shut down everything at once.',
                       'tip': 'Some companies like Stripe and PayPal bundle the payment gateway and the '
                              'merchant account together, which is exactly why one decision from them can '
                              'shut down everything at once.',
                       'timestamp': 78,
                       'timestamp_seconds': 78,
                       'timestamp_label': '[00:01:18]',
                       'url': 'https://www.youtube.com/watch?v=-G2UpQAf8L0&t=78s',
                       'markdown': '[00:01:18](https://www.youtube.com/watch?v=-G2UpQAf8L0&t=78s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sBnXe7LYFO8',
                       'title': 'How Chargeback Alerts Work: Verifi RDR, Ethoca & CDRN Explained for '
                                'Merchants',
                       'channel': 'Chargeflow',
                       'author': 'Chargeflow',
                       'text': 'Vendors could potentially receive double dispute alerts when a cardholder '
                               'initiates a dispute at a bank affiliated with both service providers, and '
                               'this in turn results in double fees.',
                       'tip': 'Vendors could potentially receive double dispute alerts when a cardholder '
                              'initiates a dispute at a bank affiliated with both service providers, and '
                              'this in turn results in double fees.',
                       'timestamp': 378,
                       'timestamp_seconds': 378,
                       'timestamp_label': '[00:06:18]',
                       'url': 'https://www.youtube.com/watch?v=sBnXe7LYFO8&t=378s',
                       'markdown': '[00:06:18](https://www.youtube.com/watch?v=sBnXe7LYFO8&t=378s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gROmfVmEsYs',
                       'title': 'How long does it take to setup Verifi CDRN and Ethoca Alerts',
                       'channel': 'Scott E. Adams | Chargeback Expert',
                       'author': 'Scott E. Adams | Chargeback Expert',
                       'text': 'The quicker things to do would be Verifi and Ethoca, so Verifi CDRN can be '
                               'live in under 24 hours, same thing with Ethoca.',
                       'tip': 'The quicker things to do would be Verifi and Ethoca, so Verifi CDRN can be '
                              'live in under 24 hours, same thing with Ethoca.',
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=gROmfVmEsYs&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=gROmfVmEsYs&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'sH9CslJpDeA',
                       'title': 'Chargeback.io - Ethoca, RDR & CDRN Enrollment Explained',
                       'channel': 'Chargeback',
                       'author': 'Chargeback',
                       'text': 'You only pay for alerts received; Ethoca alerts are priced at $29 each '
                               'while RDR and CDRN share a rate of $15 per alert.',
                       'tip': 'You only pay for alerts received; Ethoca alerts are priced at $29 each '
                              'while RDR and CDRN share a rate of $15 per alert.',
                       'timestamp': 93,
                       'timestamp_seconds': 93,
                       'timestamp_label': '[00:01:33]',
                       'url': 'https://www.youtube.com/watch?v=sH9CslJpDeA&t=93s',
                       'markdown': '[00:01:33](https://www.youtube.com/watch?v=sH9CslJpDeA&t=93s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gH8-LQ4srZY',
                       'title': 'Ethoca vs Verifi: The Two Dispute-Interception Networks Every '
                                'Subscription App Needs',
                       'channel': 'Georges Rayess',
                       'author': 'Georges Rayess',
                       'text': 'At any real volume, the 24 to 72-hour window is too tight for manual '
                               "review. That's why RDR's automation is the high leverage piece.",
                       'tip': 'At any real volume, the 24 to 72-hour window is too tight for manual '
                              "review. That's why RDR's automation is the high leverage piece.",
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=gH8-LQ4srZY&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=gH8-LQ4srZY&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0mvbNuyEem8',
                       'title': 'Verifi Explainer | RESOLVE Solution: CDRN Walkthrough',
                       'channel': 'Verifi, A Visa Solution',
                       'author': 'Verifi, A Visa Solution',
                       'text': 'The merchant has 72 hours to decide if they want to proactively refund the '
                               'pre-dispute to avoid a chargeback or allow the pre-dispute to follow the '
                               'traditional chargeback flow.',
                       'tip': 'The merchant has 72 hours to decide if they want to proactively refund the '
                              'pre-dispute to avoid a chargeback or allow the pre-dispute to follow the '
                              'traditional chargeback flow.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=0mvbNuyEem8&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=0mvbNuyEem8&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5mi35dvcRrA',
                       'title': "Rapid Dispute Resolution (RDR) vs Verifi CDRN and Ethoca Alerts - What's "
                                'the Difference?',
                       'channel': 'Scott E. Adams | Chargeback Expert',
                       'author': 'Scott E. Adams | Chargeback Expert',
                       'text': "They never get that notification, so they see a chargeback and they don't "
                               "realize it's already RDR, and so you have to track this stuff really "
                               'carefully.',
                       'tip': "They never get that notification, so they see a chargeback and they don't "
                              "realize it's already RDR, and so you have to track this stuff really "
                              'carefully.',
                       'timestamp': 248,
                       'timestamp_seconds': 248,
                       'timestamp_label': '[00:04:08]',
                       'url': 'https://www.youtube.com/watch?v=5mi35dvcRrA&t=248s',
                       'markdown': '[00:04:08](https://www.youtube.com/watch?v=5mi35dvcRrA&t=248s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '84OsVYhwoxY',
                       'title': 'Verifi Explainer Series | RECOVER Solution: Managed Chargeback '
                                'Representment for Sellers',
                       'channel': 'Verifi, A Visa Solution',
                       'author': 'Verifi, A Visa Solution',
                       'text': "The funds have been removed from the seller's bank account and at that "
                               'point the seller is effectively guilty until proven innocent.',
                       'tip': "The funds have been removed from the seller's bank account and at that "
                              'point the seller is effectively guilty until proven innocent.',
                       'timestamp': 44,
                       'timestamp_seconds': 44,
                       'timestamp_label': '[00:00:44]',
                       'url': 'https://www.youtube.com/watch?v=84OsVYhwoxY&t=44s',
                       'markdown': '[00:00:44](https://www.youtube.com/watch?v=84OsVYhwoxY&t=44s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gJ_2exzq6FA',
                       'title': 'Verifi Inform - Visa TC40, Visa TC15, Visa Fraud and Chargeback Data all '
                                'in Real Time',
                       'channel': 'Scott E. Adams | Chargeback Expert',
                       'author': 'Scott E. Adams | Chargeback Expert',
                       'text': "The issuer may think it's not worth doing a chargeback, so they might flag "
                               "it but not charge it back, and in that case it's a fraud flag transaction "
                               'which goes against you in the Visa monitoring programs for fraud.',
                       'tip': "The issuer may think it's not worth doing a chargeback, so they might flag "
                              "it but not charge it back, and in that case it's a fraud flag transaction "
                              'which goes against you in the Visa monitoring programs for fraud.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=gJ_2exzq6FA&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=gJ_2exzq6FA&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Ghanuu5dNMk',
                       'title': 'Ethoca Alerts and Chargeback Prevention',
                       'channel': 'Scott E. Adams | Chargeback Expert',
                       'author': 'Scott E. Adams | Chargeback Expert',
                       'text': "With Ethoca you need to respond a little bit quicker, and if you're after "
                               "24 hours I would still respond, there's just a higher chance that you'll "
                               'get a chargeback.',
                       'tip': "With Ethoca you need to respond a little bit quicker, and if you're after "
                              "24 hours I would still respond, there's just a higher chance that you'll "
                              'get a chargeback.',
                       'timestamp': 94,
                       'timestamp_seconds': 94,
                       'timestamp_label': '[00:01:34]',
                       'url': 'https://www.youtube.com/watch?v=Ghanuu5dNMk&t=94s',
                       'markdown': '[00:01:34](https://www.youtube.com/watch?v=Ghanuu5dNMk&t=94s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fO958wEcK8A',
                       'title': 'True Fraud #8 - Avoid Chargeback Blind Spots With Ethoca and Verifi',
                       'channel': 'The Reach Network',
                       'author': 'The Reach Network',
                       'text': 'Ethoca and Verifi should not be used as a fraud strategy or a chargeback '
                               'mitigation strategy; it should be used as a way to mitigate and give you a '
                               'little bit of a break while you figure it out.',
                       'tip': 'Ethoca and Verifi should not be used as a fraud strategy or a chargeback '
                              'mitigation strategy; it should be used as a way to mitigate and give you a '
                              'little bit of a break while you figure it out.',
                       'timestamp': 631,
                       'timestamp_seconds': 631,
                       'timestamp_label': '[00:10:31]',
                       'url': 'https://www.youtube.com/watch?v=fO958wEcK8A&t=631s',
                       'markdown': '[00:10:31](https://www.youtube.com/watch?v=fO958wEcK8A&t=631s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'fO958wEcK8A',
                       'title': 'True Fraud #8 - Avoid Chargeback Blind Spots With Ethoca and Verifi',
                       'channel': 'The Reach Network',
                       'author': 'The Reach Network',
                       'text': 'A few years ago Visa moved the chargeback ratio per month from 1% to 90 '
                               "basis points, and for 2025 they're moving in the direction of dropping it "
                               'to 0.5 or 50 basis points.',
                       'tip': 'A few years ago Visa moved the chargeback ratio per month from 1% to 90 '
                              "basis points, and for 2025 they're moving in the direction of dropping it "
                              'to 0.5 or 50 basis points.',
                       'timestamp': 718,
                       'timestamp_seconds': 718,
                       'timestamp_label': '[00:11:58]',
                       'url': 'https://www.youtube.com/watch?v=fO958wEcK8A&t=718s',
                       'markdown': '[00:11:58](https://www.youtube.com/watch?v=fO958wEcK8A&t=718s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KktmiaWBVe8',
                       'title': 'Verifi Explainer Series | RESOLVE for Merchants',
                       'channel': 'Verifi, A Visa Solution',
                       'author': 'Verifi, A Visa Solution',
                       'text': 'RDR is an automated resolution that redirects pre-disputes through '
                               "Verifi's rule-based decision engine, allowing sellers to set "
                               'pre-configured rules to determine in real time whether to refund the '
                               'transaction automatically or not.',
                       'tip': "RDR is an automated resolution that redirects pre-disputes through Verifi's "
                              'rule-based decision engine, allowing sellers to set pre-configured rules to '
                              'determine in real time whether to refund the transaction automatically or '
                              'not.',
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=KktmiaWBVe8&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=KktmiaWBVe8&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
