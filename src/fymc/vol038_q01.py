from __future__ import annotations

CHAPTER_1 = {'id': 'Q1',
 'chapter_id': 'Q1',
 'chapter_number': 1,
 'question_number': 1,
 'slug': 'small-parcel-auditing-guaranteed-service-refund-recovery',
 'question_prompt': 'How do contingent parcel-audit firms recover late-delivery (GSR) refunds and billing '
                    'errors from FedEx and UPS, and how should a shipper evaluate an audit provider?',
 'kicker': 'Q1 / THE BIG MONEY PLAYBOOKS',
 'title': 'Small-Parcel Auditing and Guaranteed-Service Refund Recovery',
 'subtitle': 'Late-package GSR claims, automatic vs. requested refunds, denied-refund handling, audit '
             'workflows, qualifying a good auditor, common misconceptions, free audit tools like Audisee, '
             'and percentage-of-savings onboarding',
 'layout_template': 'opportunity_overview',
 'reading_time_minutes': 15,
 'executive_summary': 'FedEx and UPS guarantee time-definite delivery, and practitioners from Refund '
                      'Retriever, Empact Parcel, and Compete Consulting Group agree a package delivered '
                      'even a minute late earns a full refund the carriers will never flag. The shared '
                      'playbook: take online billing credentials, auto-download every invoice, audit 40 to '
                      '44 points per shipment, file inside the 15-day window, and bill only on '
                      "contingency, from Cerasis's 30 percent model to Refund Retriever's 50 percent "
                      'starting split. Scarbrough Global and Refund Retriever both say the money sits in '
                      'follow-up, with resubmission loops and live phone agents beating automatic denials, '
                      'including FedEx rejecting GSR claims on already-paid invoices. Practitioners split '
                      'on refund honesty, speed benchmarks, and minimums: Share a Refund bills only '
                      'refunds it acted on and reads check refunds as a slow audit, while Cerasis argues '
                      'tiny shippers cannot justify manual auditing.',
 'key_metrics': [{'label': 'GSR Late-Delivery Trigger',
                  'metric': 'GSR Late-Delivery Trigger',
                  'value': '60 seconds late',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Refund Retriever states guaranteed service refunds are available when FedEx '
                             'or UPS delivers a package even 60 seconds late.',
                  'source': 'Refund Retriever ([JeLyjRF9HEk @ 00:00:00])'},
                 {'label': 'Late-Package Claim Window',
                  'metric': 'Late-Package Claim Window',
                  'value': '15 days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Refund Retriever reports a 15-day time limit to get refunds for late '
                             'packages, confirmed while working a batch of denied FedEx disputes.',
                  'source': 'Refund Retriever ([JeLyjRF9HEk @ 00:01:06])'},
                 {'label': 'Contingency Starting Fee',
                  'metric': 'Contingency Starting Fee',
                  'value': '50% of savings ($25 fee on $50 recovered)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Brian Gibbs says Refund Retriever starts at 50 percent of whatever it saves '
                             'and negotiates the rate down for higher-volume shippers.',
                  'source': 'Refund Retriever ([vOX4irOA_Tk @ 00:05:11])'},
                 {'label': 'Phone-Escalation Recovery on One Invoice',
                  'metric': 'Phone-Escalation Recovery on One Invoice',
                  'value': '$98.42 on a $4,253.53 invoice (2.3%)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Phone dispute agents reversed FedEx auto-denials on all 5 late packages; '
                             'without the calls the client would have received 0 refunds on that invoice.',
                  'source': 'Refund Retriever ([JeLyjRF9HEk @ 00:01:42])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator in this lane builds on the same premise: FedEx and UPS sell '
                              'a time-definite promise, and when they break it the shipment is free. Brian '
                              'Gibbs of Refund Retriever states that both carriers guarantee all ground '
                              'and express packages to arrive by a certain date or time or the charge '
                              'comes back [vOX4irOA_Tk @ 00:02:44], and his team defines a guaranteed '
                              'service refund as available when a package lands even 60 seconds late '
                              '[JeLyjRF9HEk @ 00:00:00]. The second shared belief is that the carrier will '
                              'never flag the money for you. Empact Parcel runs the same one-minute '
                              'trigger, frames the pitch bluntly as late packages being free, and warns '
                              'that the carriers will not tell you which shipments are due a refund '
                              '[frD9iyAvyds @ 00:00:19], while Compete Consulting Group compares '
                              'carrier-provided monitoring tools to asking the fox to guard the henhouse '
                              'and claims two billion dollars went unclaimed in a single year [RCPFFZVF7qs '
                              '@ 00:00:35]. That combination, a hair-trigger refund right plus a '
                              'counterparty with zero incentive to surface it, is the whole business. '
                              'Nobody disputes that the refund exists; the fight is entirely about who '
                              'detects the late scan, files first, and keeps pressing until the credit '
                              'actually posts to the account.',
                              'The practitioners also agree that a human with a highlighter cannot win '
                              'this game at volume. Watchdog Advisory describes monthly bills running to '
                              'hundreds of pages of shipping invoices that are difficult if not impossible '
                              'to review for errors [5eTaFaKQdHY @ 00:00:00], and Compete Consulting Group '
                              'says carrier invoices can run hundreds of pages each week, enough to bury '
                              'an entire team of accountants working shipment by shipment [RCPFFZVF7qs @ '
                              '00:01:06]. RAF Logistics points to more than 130 different add-on fees the '
                              'carriers can now charge [eEERM3QJqyI @ 00:00:17], and Refund Retriever adds '
                              "that surcharges alone can account for up to 35 percent of a shipper's "
                              'parcel spend, with dimensional weight, residential delivery, peak season, '
                              'and overweight fees piling on as prices rise every year [vOX4irOA_Tk @ '
                              '00:01:33]. The consensus response is full automation keyed off the '
                              "carrier's own billing portal. Every vendor here sells the same onboarding "
                              'promise: hand over online billing access, do nothing else, and watch '
                              'credits land. Nobody pitches a model where the shipper keeps working the '
                              'invoices; RAF says there is nothing you need to send weekly, Compete '
                              'promises no work for you once you sign up, and Watchdog calls its setup '
                              "three minutes with no work on the client's part.",
                              'On money, the consensus is pure contingency. Watchdog Advisory charges no '
                              'setup costs or fees and takes a portion of savings, so no savings means no '
                              'fee [5eTaFaKQdHY @ 00:01:47]; Refund Retriever bills a percentage of actual '
                              'recovery with no cancellation, setup, or monthly fee [vOX4irOA_Tk @ '
                              '00:04:55]; Empact Parcel stays profitable on a split of refund amounts. '
                              'That alignment matters because the second consensus point is that filing is '
                              'the easy part. Scarbrough Global says customers could find the late '
                              'packages and surcharges and even make the requests themselves, but the real '
                              'fortune is in the follow-up, because carriers often deny requests for no '
                              'reason, which their data shows, likely to discourage human filers '
                              '[NKDaSW7CKiQ @ 00:01:27]. Scarbrough ties that persistence to its billing: '
                              'the product is paid only on success, so squeezing out every refund is how '
                              'it makes money. The third shared prerequisite is speed. Share a Refund '
                              'describes a limited window right after an invoice posts in which claims can '
                              'be filed, after which each refund is lost forever [PheSsrwvW9c @ 00:00:23], '
                              'and Refund Retriever and Compete both pin the late-package window at 15 '
                              'days. Credentials, automation, contingency, relentless follow-up, and a '
                              'fast clock are the baseline every one of these operators treats as '
                              'non-negotiable.'],
               'table': {'caption': 'Baseline consensus every small-parcel recovery operator builds on',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Late delivery means the shipment is free',
                                   'FedEx and UPS guarantee ground and express packages by a set date or '
                                   'time, or the charge is refunded',
                                   'Every late scan on an invoice is recoverable cash only if somebody '
                                   'files for it',
                                   'Refund Retriever ([vOX4irOA_Tk @ 00:02:44])'],
                                  ['Carriers stay silent about refunds owed',
                                   'The carriers will not tell shippers which shipments are due a refund '
                                   'under the guarantee',
                                   'Detection must be run by the shipper or a third-party auditor, never '
                                   'the carrier',
                                   'Empact Parcel ([frD9iyAvyds @ 00:00:19])'],
                                  ['Manual invoice review collapses at real volume',
                                   'Carrier invoices can run hundreds of pages each week, requiring a '
                                   'whole accounting team to check',
                                   'Automated software is the entry ticket, not an optional upgrade, for '
                                   'serious recovery',
                                   'Compete Consulting Group ([RCPFFZVF7qs @ 00:01:06])'],
                                  ['Online billing access is the only onboarding input',
                                   'All the auditor needs is FedEx and UPS online billing access, then '
                                   'invoices are downloaded weekly',
                                   'Onboarding friction is near zero, so the pitch is credentials in and '
                                   'credits out',
                                   'Refund Retriever ([vOX4irOA_Tk @ 00:03:17])'],
                                  ['Pricing runs on contingency with no upfront fees',
                                   'No setup costs or fees; the fee is a portion of savings, and no '
                                   'savings means no fee',
                                   'The shipper carries no cash risk, and the auditor eats the cost of '
                                   'failed recoveries',
                                   'Watchdog Advisory ([5eTaFaKQdHY @ 00:01:47])'],
                                  ['The real money sits in follow-up after denials',
                                   'Carriers often deny requests for no reason, apparently to discourage '
                                   'human beings from filing',
                                   'Resubmission loops and live phone escalation separate real recovery '
                                   'from simple filing',
                                   'Scarbrough Global ([NKDaSW7CKiQ @ 00:01:27])'],
                                  ['Speed decides whether a refund survives at all',
                                   'A limited window opens right after invoice posting; refunds not '
                                   'captured then are lost forever',
                                   'Audit and file within the same weekly billing cycle the invoice posts',
                                   'Share a Refund ([PheSsrwvW9c @ 00:00:23])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The workflow Nick of Share a Refund lays out runs in a fixed sequence: '
                              'invoice retrieval, shipment audit, claim submission, claim verification, '
                              'reporting, and billing [eTB0fyueR5A @ 00:00:37]. Retrieval goes one of two '
                              'ways. Large multinationals and Fortune 500 shippers with existing EDI '
                              'integrations open FTP data pools, while the more common setup is handing '
                              'the auditor a username and password for the carrier accounts so invoices '
                              'are pulled directly from the carrier website [eTB0fyueR5A @ 00:00:55]. '
                              "Refund Retriever's signup is exactly that second path: contact details in "
                              'step one, then FedEx and UPS online billing credentials plus billing '
                              'address in step two, with a warning to confirm the login actually has '
                              'invoice access; the company compares its always-on credential monitoring to '
                              'mint.com [P3sA9eO0D-k @ 00:00:52]. Once invoices are in hand, the audit has '
                              'to test every cost component on every shipment, both whether the charge '
                              'should apply at all and whether its amount reflects the negotiated '
                              'discount. Share a Refund checks 40 points per shipment, using the '
                              'residential surcharge as its showcase: verify the ship-to really is '
                              'residential, then verify the discount on that surcharge was applied '
                              '[eTB0fyueR5A @ 00:02:08]. Compete Consulting Group runs a 44-point audit on '
                              'each shipment, and Watchdog sweeps late deliveries, invalid surcharges, and '
                              'dimensional and weight charges.',
                              'Share a Refund insists each claim be filed fast, under the correct claim '
                              'type, and for the exact amount of the mistake: if the residential discount '
                              'was skipped, request the net difference; if a residential surcharge hit a '
                              'commercial delivery, request the entire component [eTB0fyueR5A @ 00:03:16]. '
                              'Its claims verification service then captures every response type, '
                              'reconciles each credit to its dispute, and runs a decision agent on '
                              'rejections, choosing between filing an invalid address correction dispute, '
                              'resubmitting the service failure, or dropping the shipment [eTB0fyueR5A @ '
                              '00:04:36]. Scarbrough Global runs hundreds of checks before submitting only '
                              'charges it is very confident about, then resubmits, resubmits, resubmits, '
                              'and finally has an internal team call a live human being [NKDaSW7CKiQ @ '
                              '00:02:25]. Refund Retriever added a denial filter feeding in-house phone '
                              'dispute agents, then proved it when a client emailed a list of denied FedEx '
                              'disputes. In the FedEx invoice history, the team found the denial reason '
                              'was an existing payment on file, because the client paid the invoice the '
                              'moment it posted, which made FedEx auto-deny every GSR request. Phone '
                              'agents called FedEx customer service inside the 15-day window and won '
                              'refunds on all five late packages, recovering $98.42 on a $4,253.53 '
                              'invoice, a 2.3 percent savings that would otherwise have been zero '
                              '[JeLyjRF9HEk @ 00:01:42].',
                              'The unit economics are simple percentages. Refund Retriever starts at 50 '
                              'percent of whatever it saves, so $50 of late-delivery refunds in a month '
                              'produces a $25 fee, invoiced with the tracking number and the invoice where '
                              'the credit sits, and Brian Gibbs says the rate drops and is negotiable for '
                              'heavy shippers, citing a $25 million a year UPS account as one he would '
                              'work with [vOX4irOA_Tk @ 00:05:11]. Cerasis models a 30 percent auditor '
                              'fee: $1,000 in total savings nets the shipper $700, scaling to as much as '
                              '$70,000 across an enterprise [GnXmnbxCZ-A @ 00:05:14]. On the recovery '
                              'side, Gibbs found roughly 10 percent of the packages from his own eBay '
                              'reselling business arriving late before he automated the process '
                              '[1JZzLbF5PrI @ 00:00:50], Compete puts daily late deliveries at four to six '
                              'percent, Empact pitches an immediate 1 to 5 percent cut in parcel spend, '
                              'and Cerasis says proper auditing can recoup up to 5 percent. Watchdog '
                              'claims its clients average roughly 30 percent savings when audit recovery '
                              'is combined with parcel intelligence and carrier contract engineering, on '
                              'technology used by more than 3,300 companies [5eTaFaKQdHY @ 00:01:12]. For '
                              "a free first look, Lojistic's Audisee web tool takes uploaded UPS or FedEx "
                              'invoices and instantly returns findings, per-tracking-number details, '
                              'charts, and stats, though it will not audit both carriers in one batch.'],
               'table': {'caption': 'Audit engines, tools, and unit economics quoted by practitioners',
                         'headers': ['Mechanic or Tool',
                                     'Exact Number or Spec',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Per-shipment multi-point audit engine',
                                   '40 checkpoints per shipment, including residential address and '
                                   'surcharge discount validation',
                                   'Test both whether each charge applies and whether the negotiated '
                                   'discount was honored',
                                   'Share a Refund ([eTB0fyueR5A @ 00:02:08])'],
                                  ['Proprietary audit software with automated refund filing',
                                   '44-point audit run on each and every shipment, with refunds automated',
                                   "Credits pile up directly on the shipper's FedEx or UPS online accounts",
                                   'Compete Consulting Group ([RCPFFZVF7qs @ 00:01:24])'],
                                  ['Cloud audit plus intelligence and contract engineering',
                                   'Used by more than 3,300 companies; clients average approximately 30 '
                                   'percent savings',
                                   'Pair refund recovery with network design and carrier contract rework '
                                   'for larger savings',
                                   'Watchdog Advisory ([5eTaFaKQdHY @ 00:01:12])'],
                                  ['Outsourced audit fee taken off the top',
                                   '30 percent fee on $1,000 savings leaves a $700 net refund; enterprise '
                                   'up to $70,000',
                                   'Frame outsourcing as an active revenue stream rather than a cost line',
                                   'Cerasis , now part of GlobalTranz ([GnXmnbxCZ-A @ 00:05:14])'],
                                  ['Contingency split with volume-based negotiation',
                                   'Starts at 50 percent of savings; $50 recovered produces a $25 fee',
                                   'Negotiate the split downward as annual shipping spend and refund '
                                   'volume grow',
                                   'Refund Retriever ([vOX4irOA_Tk @ 00:05:11])'],
                                  ['Audisee free instant audit web tool',
                                   'Findings, details, charts, and stats tabs; cannot audit UPS and FedEx '
                                   'together',
                                   'Upload invoices for a quick recovery estimate before chasing the '
                                   'carrier for money',
                                   'Lojistic ([5yyeqQ4VAFU @ 00:00:45])'],
                                  ['Fee-complexity check across carrier invoices',
                                   'Over 130 different add-on fees the carriers can now charge on '
                                   'shipments',
                                   'Justifies automated checks for billing errors and late deliveries on '
                                   'every invoice',
                                   'RAF Logistics ([eEERM3QJqyI @ 00:00:17])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Where the extra refunds and honest billing actually come from',
                           'body': 'These are the edge moves practitioners use to squeeze more credits out '
                                   'of the carriers and to catch auditors billing for work they never did.',
                           'items': ['Check the original reason column in FedEx online billing invoice '
                                     "history: 'systematic SVC fail' means FedEx refunded automatically, "
                                     'and an auditor billing you for it may be dishonest [Refund Retriever '
                                     '— 8Bw_30ivpb4 @ 00:00:48]',
                                     'Read the refund method as an audit-speed meter: credits on unpaid '
                                     'invoices signal a fast audit, while credit-card refunds or mailed '
                                     'checks signal late filing [Share a Refund — PheSsrwvW9c @ 00:01:23]',
                                     'Paying a FedEx invoice the moment it posts triggers automatic GSR '
                                     'denials for an existing payment on file; phone agents reversed all 5 '
                                     'denials inside the 15-day window [Refund Retriever — JeLyjRF9HEk @ '
                                     '00:01:25]',
                                     'When a service-failure dispute is rejected, decide between filing an '
                                     'invalid address correction dispute, resubmitting the service '
                                     'failure, or taking no further action [Share a Refund — eTB0fyueR5A @ '
                                     '00:04:36]']},
               'sop_steps': [{'step': 1,
                              'title': 'Connect carrier billing access',
                              'action': 'Hand the auditor FedEx and UPS online billing credentials, or '
                                        'open an EDI/FTP data pool for enterprise accounts.',
                              'detail': 'Fill in contact details, then enter FedEx and UPS online billing '
                                        'IDs and passwords with confirmed invoice access plus billing '
                                        'address; past and future invoices are then downloaded for '
                                        'processing [Refund Retriever — P3sA9eO0D-k @ 00:00:35]'},
                             {'step': 2,
                              'title': 'Audit every cost component',
                              'action': 'Run each shipment through a multi-point check covering late '
                                        'delivery, surcharge validity, and discount application.',
                              'detail': 'Validate both the application of each cost component and its '
                                        'amount against negotiated discounts, then prioritize findings so '
                                        'the maximum refund is pursued on each shipment [Share a Refund — '
                                        'eTB0fyueR5A @ 00:01:31]'},
                             {'step': 3,
                              'title': 'File fast with the right claim type and amount',
                              'action': 'Submit disputes inside the carrier window, under the correct '
                                        'claim type, for the exact billing-mistake amount.',
                              'detail': 'Request the net discount difference when a residential discount '
                                        'was skipped, or the entire component when a residential surcharge '
                                        'hit a commercial delivery [Share a Refund — eTB0fyueR5A @ '
                                        '00:03:16]'},
                             {'step': 4,
                              'title': 'Verify, resubmit, then escalate by phone',
                              'action': 'Track every carrier response, resubmit denied high-confidence '
                                        'claims, and push stubborn denials to a live carrier agent.',
                              'detail': 'Resubmit denied charges repeatedly, and if they still get denied, '
                                        'have an internal team reach out and talk to a live human being at '
                                        'the carrier [Scarbrough Global — NKDaSW7CKiQ @ 00:02:25]'}]},
              {'title': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Fee structure is the sharpest split between shops. Brian at Refund '
                              'Retriever says the firm starts at 50% of whatever it saves, so a $50 month '
                              'of late-delivery refunds produces a $25 fee, and a shipper doing $25 '
                              'million a year in UPS can negotiate that rate down because it is not set in '
                              'stone [vOX4irOA_Tk @ 00:05:11]. Cerasis models the outsourced deal at a 30% '
                              'cut instead: $1,000 in total savings still leaves the shipper a $700 net '
                              'refund, scaling to as much as $70,000 across an enterprise [GnXmnbxCZ-A @ '
                              '00:05:14]. Nick at Share a Refund attacks the billing base rather than the '
                              'percentage, charging that competitors bill on all refunds delivered, even '
                              'ones they took no action on, while Share a Refund only splits refunds on '
                              'shipments where its system acted, which the firm says yields a lower '
                              'service fee [eTB0fyueR5A @ 00:07:18]. Refund Retriever matches that stance '
                              'for one credit class: when FedEx drops a systematic GSR refund onto an '
                              'invoice unprompted, the firm marks it and never bills the client for it '
                              '[8Bw_30ivpb4 @ 00:00:19]. Headline percentage and billable base are '
                              'separate levers, and a cheaper-looking split can cost more if the auditor '
                              'invoices credits it never chased.',
                              'Practitioners split hard on whether small shippers belong in the game at '
                              'all. Nick at Share a Refund says auditors that refuse anyone spending under '
                              'a threshold such as a million dollars a year are exposing limited '
                              'bandwidth, thin automation, and throughput caps, and asks whether those '
                              'shops could audit every shipment once peak season hits [PheSsrwvW9c @ '
                              '00:05:50]. Refund Retriever takes the opposite posture, onboarding '
                              'companies from 50 shipments a week to 50 shipments a minute because its '
                              'invoice downloads are run by programs rather than staff logging in '
                              '[vOX4irOA_Tk @ 00:04:05]. Cerasis splits the difference with math: for a '
                              'shipper using parcel only now and again, a 50-invoice audit that finds a '
                              '10% markup on 10% of invoices at $22 per shipment saves roughly one dollar, '
                              'so paying an employee two hours to find it costs more than leaving the '
                              'invoices alone [GnXmnbxCZ-A @ 00:03:04]. The same Cerasis host then argues '
                              'that once the process is automated, audits cost no more than the software, '
                              'which is why companies outsource and why the low-volume objection collapses '
                              '[GnXmnbxCZ-A @ 00:04:39]. The working rule from all three: low volume kills '
                              'manual in-house auditing, while automated contingency shops will still '
                              'chase small accounts.',
                              "When carriers reject a claim, the playbooks diverge. Scarbrough Global's "
                              'team says carriers often deny requests for no reason, which their data '
                              'shows, and they believe it is done to discourage humans; their answer is '
                              'brute persistence, resubmitting the same charge again and again and then '
                              'putting an internal team on the phone with a live human [NKDaSW7CKiQ @ '
                              '00:01:27] [NKDaSW7CKiQ @ 00:02:25]. Scarbrough frames the follow-up, not '
                              'the detection, as where the real fortune sits. Refund Retriever runs a '
                              'filter that catches denied FedEx late-package disputes and routes them to '
                              'in-house phone dispute agents who call FedEx customer service, conceding it '
                              'is time consuming but that clients see more refunds each week [JeLyjRF9HEk '
                              '@ 00:00:33]. Nick at Share a Refund treats rejection as a branching '
                              'decision: a decision agent inside the claims verification service reads '
                              'each rejected service-failure dispute and picks the next move, which might '
                              'be filing on an invalid address correction instead, resubmitting the same '
                              'service-failure dispute, or taking no further action at all [eTB0fyueR5A @ '
                              '00:04:36]. Scarbrough bets on volume of retries backed by hundreds of '
                              'checks, Refund Retriever on human phone escalation for a filtered list, and '
                              'Share a Refund on per-shipment branching logic that also reconciles every '
                              'credit back to its dispute for statistical feedback.'],
               'table': {'caption': 'Competing Parcel-Recovery Playbooks Side by Side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Contingency fee level charged on recovered refunds',
                                   'Refund Retriever starts at 50% of savings and negotiates down for '
                                   'heavy UPS shippers',
                                   'Cerasis models a 30% cut that still leaves $700 net on $1,000 '
                                   'recovered',
                                   'Refund Retriever ([vOX4irOA_Tk @ 00:05:11]); Cerasis , now part of '
                                   'GlobalTranz ([GnXmnbxCZ-A @ 00:05:14])'],
                                  ['Which credits the auditor is allowed to bill',
                                   'Share a Refund splits only refunds on shipments where its system took '
                                   'action',
                                   'Refund Retriever refuses to bill FedEx systematic GSR credits it never '
                                   'requested',
                                   'Share a Refund ([eTB0fyueR5A @ 00:07:18]); Refund Retriever '
                                   '([8Bw_30ivpb4 @ 00:00:19])'],
                                  ['Account size minimums before an auditor takes you',
                                   'Share a Refund says million-dollar minimums signal thin automation and '
                                   'throughput limits',
                                   'Refund Retriever takes shippers from 50 shipments a week to 50 a '
                                   'minute',
                                   'Share a Refund ([PheSsrwvW9c @ 00:05:50]); Refund Retriever '
                                   '([vOX4irOA_Tk @ 00:04:05])'],
                                  ['How carrier invoices reach the auditing system',
                                   'Large EDI-integrated shippers open FTP data pools to pass invoices '
                                   'electronically',
                                   'Most shippers hand over carrier usernames and passwords for direct '
                                   'website retrieval',
                                   'Share a Refund ([eTB0fyueR5A @ 00:00:55]); Refund Retriever '
                                   '([P3sA9eO0D-k @ 00:00:52])'],
                                  ['Self-serve audit tool versus done-for-you recovery',
                                   "Lojistic's free Audisee tool instantly audits uploaded UPS or FedEx "
                                   'invoices on screen',
                                   'Lojistic admits chasing the carrier down for the money is easier said '
                                   'than done',
                                   'Lojistic ([5yyeqQ4VAFU @ 00:00:00]); Lojistic ([5yyeqQ4VAFU @ '
                                   '00:02:07])'],
                                  ['Response when the carrier denies a refund claim',
                                   'Scarbrough resubmits repeatedly, then has an internal team call a live '
                                   'human',
                                   "Share a Refund's decision agent picks address-correction dispute, "
                                   'resubmission, or no action',
                                   'Scarbrough Global ([NKDaSW7CKiQ @ 00:02:25]); Share a Refund '
                                   '([eTB0fyueR5A @ 00:04:55])'],
                                  ['Headline savings promised to prospective shipper clients',
                                   'Watchdog Advisory says clients average approximately 30% savings using '
                                   'its 3D approach',
                                   'Empact Parcel pitches 1 to 5% immediately; Cerasis says up to 5% '
                                   'recoupable',
                                   'Watchdog Advisory ([5eTaFaKQdHY @ 00:00:56]); Empact Parcel '
                                   '([frD9iyAvyds @ 00:00:00]); Cerasis , now part of GlobalTranz '
                                   '([nGN0KikmdVk @ 00:00:16])']]}},
              {'title': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive self-inflicted wound is paying the carrier too fast. '
                              "Refund Retriever pulled a client's FedEx invoice history after every "
                              'submitted dispute came back denied and found the reason: an existing '
                              'payment on file. The client had paid the invoice the moment it posted, '
                              'which caused FedEx to automatically deny every GSR service-failure request '
                              'even though the claims were inside the 15-day window [JeLyjRF9HEk @ '
                              '00:01:06] [JeLyjRF9HEk @ 00:01:25]. A phone dispute agent clawed back all '
                              'five late packages, $98.42 on a $4,253.53 invoice, a 2.3% savings that '
                              'would have been zero without the individual calls [JeLyjRF9HEk @ 00:01:42]. '
                              'Nick at Share a Refund explains the mechanic: credits land on unpaid '
                              'invoices during the gap between posting and payment, credits to open '
                              'invoices are easier, and claims filed fast succeed more often; refunds '
                              'arriving on the credit card on file or by mailed check signal disputes '
                              'filed later than the ideal timeline [PheSsrwvW9c @ 00:02:03]. Nick also '
                              'flags accounts payable working from a paper copy of the original invoice, '
                              'instead of the updated credited amount, which overpays the carrier and '
                              'forces refunds back as checks. Protect the payment gap until claims are '
                              'filed, or auto-denials and slow refunds eat the recovery.',
                              'Brian Gibbs, President of Refund Retriever, built the company after getting '
                              'burned around 2005: signing up with an existing recovery firm produced only '
                              'more work, sending copies of invoices, and zero refunds [1JZzLbF5PrI @ '
                              '00:00:32]. Tracking packages by hand each week, Gibbs found about 10% of '
                              'shipments from that eBay selling business arriving late, applied for every '
                              'refund, and started getting money back before hiring a programmer to '
                              'automate it [1JZzLbF5PrI @ 00:00:50]. The second trap is paying a vendor '
                              'for credits the carrier gave away. Refund Retriever reports never seeing '
                              'UPS refund a late parcel automatically, while FedEx rarely posts a '
                              'systematic GSR failure credit on its own; if systematic SVC fail appears in '
                              'the original reason column of the FedEx online billing invoice history, '
                              'FedEx issued it automatically, and an auditor billing for it may be '
                              'dishonest, though a refund applied within hours of the invoice publishing '
                              'might be an honest dispute [8Bw_30ivpb4 @ 00:00:48]. Compete Consulting '
                              'Group explains why shippers cannot simply rely on the carrier: you only '
                              'have 15 days to claim, the carrier is not going to call to say a package '
                              'arrived late, and trusting carrier web tools to flag every miss is like '
                              'asking the fox to guard the henhouse [RCPFFZVF7qs @ 00:00:35].',
                              'The in-house math is where DIY auditors bleed. Cerasis calculates that if a '
                              'single audit takes five minutes, a shipper spending $10,000 or less a year '
                              'on small parcels would burn a full-time employee eight hours a day, five '
                              'days a week, for nearly 21 weeks, and if 50% of audits require a claim, the '
                              'time could double or triple while some carriers enforce strict filing '
                              'limits [nGN0KikmdVk @ 00:02:50] [nGN0KikmdVk @ 00:03:05]. Even after '
                              'finding errors, Cerasis warns that shippers must still contact carriers, '
                              'prove their case, and request the refund, a process complex enough that an '
                              'international refund can take weeks [GnXmnbxCZ-A @ 00:03:43]. Sloppy claims '
                              'fail too. Nick at Share a Refund insists claims go in quickly and every '
                              'claim carry the correct claim type and the right amount: a residential '
                              'surcharge that missed its negotiated discount should be claimed at the net '
                              'expected refund, while a residential surcharge slapped on a commercial '
                              'delivery should be claimed in full [eTB0fyueR5A @ 00:03:16]. Speed, claim '
                              'type, context, expected amount, and priority are all important '
                              'considerations when filing. Share a Refund checks 40 different points per '
                              'shipment to catch these, and Compete Consulting Group runs a 44-point audit '
                              'on every shipment.'],
               'table': {'caption': 'Firsthand Recovery Failures and the Economics Behind Them',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Paying FedEx invoices the moment they post',
                                   'Client paid immediately, so FedEx auto-denied every GSR dispute citing '
                                   'an existing payment',
                                   'Phone agents recovered $98.42 on $4,253.53, a 2.3% save otherwise zero',
                                   'Refund Retriever ([JeLyjRF9HEk @ 00:01:25])'],
                                  ['Hiring a recovery vendor that creates more work',
                                   "Brian Gibbs' first recovery firm demanded invoice copies and produced "
                                   'zero refunds',
                                   "Manual tracking then showed roughly 10% of the eBay business's "
                                   'packages arriving late',
                                   'Refund Retriever ([1JZzLbF5PrI @ 00:00:50])'],
                                  ['Paying contingency fees on automatic carrier credits',
                                   'FedEx systematic SVC fail credits can be billed by dishonest auditors '
                                   'as their own',
                                   'UPS never auto-refunds late parcels per Refund Retriever, and FedEx '
                                   'only rarely',
                                   'Refund Retriever ([8Bw_30ivpb4 @ 00:00:00])'],
                                  ['Giving up after carrier denials with no reason',
                                   'Scarbrough data shows carriers deny requests for no reason to '
                                   'discourage human filers',
                                   'The fortune is in follow-up: resubmit repeatedly, then call a live '
                                   'human',
                                   'Scarbrough Global ([NKDaSW7CKiQ @ 00:01:27])'],
                                  ['Slow audits leaking refunds past the window',
                                   'Refunds landing on credit cards or mailed checks signal late dispute '
                                   'filing',
                                   'Monthly-reporting auditors likely miss refunds because carriers bill '
                                   'on weekly cycles',
                                   'Share a Refund ([PheSsrwvW9c @ 00:04:54])'],
                                  ['Manual in-house auditing for occasional parcel shippers',
                                   'A 50-invoice audit example surfaced errors worth roughly one dollar in '
                                   'total',
                                   'If savings do not exceed auditor wage times hours, auditing costs more '
                                   'than ignoring invoices',
                                   'Cerasis , now part of GlobalTranz ([GnXmnbxCZ-A @ 00:03:23])'],
                                  ['Missing the late-delivery claim window entirely',
                                   'Carriers never call shippers to report late packages and claims expire '
                                   'after 15 days',
                                   'Compete cites four to six percent of packages delivered late every day',
                                   'Compete Consulting Group ([RCPFFZVF7qs @ 00:00:17])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Signature Recovery Checks',
                           'body': 'Four practitioner-reported leaks that zero out parcel refunds before '
                                   'any contingency split even matters.',
                           'items': ['Hold FedEx invoice payment until GSR disputes are filed inside the '
                                     '15-day window, because an existing payment on file triggered '
                                     'automatic denial of every late-package claim [Refund Retriever — '
                                     'JeLyjRF9HEk @ 00:01:06].',
                                     'Scan the FedEx online billing original reason column for systematic '
                                     'SVC fail credits before paying any auditor fee on those refunds '
                                     '[Refund Retriever — 8Bw_30ivpb4 @ 00:00:48].',
                                     'Require a denied-claim escalation path of repeated resubmission plus '
                                     'live phone follow-up, since carriers deny requests for no reason '
                                     '[Scarbrough Global — NKDaSW7CKiQ @ 00:02:25].',
                                     'Judge audit speed by the aggregate refund method: mostly invoice '
                                     'credits means fast filing, while card credits or checks mean late '
                                     'filing [Share a Refund — PheSsrwvW9c @ 00:04:02].']}}],
 'pull_quote': '"The real fortune is in the follow-up, because the carriers often deny the requests." — '
               'Scarbrough Global (NKDaSW7CKiQ @ 00:01:27).',
 'diagram_id': 'diag-01',
 'action_checklist': ['Hand the auditor UPS and/or FedEx Online Billing credentials with invoice access '
                      'confirmed, plus the current billing address, so invoices can be downloaded and '
                      'monitored continuously [Refund Retriever — P3sA9eO0D-k @ 00:00:52].',
                      'Run a free instant audit on a batch of UPS or FedEx invoices through Audisee, one '
                      'carrier at a time, and review the findings, details, charts, and stats tabs to size '
                      'recoverable dollars [Lojistic — 5yyeqQ4VAFU @ 00:00:45].',
                      'Start a free 30-day invoice audit with no cost, commitment, or obligation to '
                      'measure carrier credits before committing to a vendor [MTC Recovery Consultants — '
                      'bNqu0vah45U @ 00:01:01].',
                      'Confirm the auditor validates every cost component, such as checking that '
                      'residential surcharges hit truly residential addresses and carry the negotiated '
                      'discount [Share a Refund — eTB0fyueR5A @ 00:01:51].',
                      'Negotiate the starting 50% contingency split downward as shipping volume and weekly '
                      'refund counts rise [Refund Retriever — vOX4irOA_Tk @ 00:05:29].',
                      'Demand recurring reports showing the number of incorrect billing statements, the '
                      'amount recouped from the carrier, and net savings after all third-party fees '
                      '[Cerasis , now part of GlobalTranz — nGN0KikmdVk @ 00:04:14].'],
 'statutory_citations': [{'title': 'Refund Retriever — FedEx Late Package Refund Denied? [00:01:06]',
                          'url': 'https://www.youtube.com/watch?v=JeLyjRF9HEk&t=66s',
                          'relevance': 'Primary practitioner testimony on FedEx auto-denying GSR disputes '
                                       'after early invoice payment and recovering them by phone.'},
                         {'title': 'Scarbrough Global — How does the Parcel Audit work? [00:01:27]',
                          'url': 'https://www.youtube.com/watch?v=NKDaSW7CKiQ&t=87s',
                          'relevance': 'Primary practitioner testimony on carriers denying refund requests '
                                       'for no reason and the resubmit-then-call follow-up playbook.'},
                         {'title': 'Share a Refund — One way to qualify a good parcel audit [00:02:03]',
                          'url': 'https://www.youtube.com/watch?v=PheSsrwvW9c&t=123s',
                          'relevance': 'Primary practitioner testimony on filing claims during the '
                                       'unpaid-invoice gap and reading refund methods as audit-speed '
                                       'signals.'},
                         {'title': 'Refund Retriever — Automatic UPS & FedEx GSR Service Failure Refunds '
                                   '[00:00:48]',
                          'url': 'https://www.youtube.com/watch?v=8Bw_30ivpb4&t=48s',
                          'relevance': 'Primary practitioner testimony on spotting systematic SVC fail '
                                       'credits that auditors should never bill.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'P3sA9eO0D-k',
                       'title': 'How to get started with Refund Retriever FedEx UPS auditing',
                       'channel': 'Refund Retriever',
                       'author': 'Refund Retriever',
                       'text': 'Our functionality is similar to mint.com, we constantly use these '
                               'credentials to monitor your invoices and shipping activity.',
                       'tip': 'Our functionality is similar to mint.com, we constantly use these '
                              'credentials to monitor your invoices and shipping activity.',
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=P3sA9eO0D-k&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=P3sA9eO0D-k&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JeLyjRF9HEk',
                       'title': 'FedEx Late Package Refund Denied?',
                       'channel': 'Refund Retriever',
                       'author': 'Refund Retriever',
                       'text': 'Our client had paid for the invoice as soon as it was available. This '
                               'caused FedEx to automatically deny any GSR service failure requests.',
                       'tip': 'Our client had paid for the invoice as soon as it was available. This '
                              'caused FedEx to automatically deny any GSR service failure requests.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=JeLyjRF9HEk&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=JeLyjRF9HEk&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bNqu0vah45U',
                       'title': 'Parcel Auditing to Lower FedEx, UPS, DHL, and Purolator Bills',
                       'channel': 'MTC Recovery Consultants',
                       'author': 'MTC Recovery Consultants',
                       'text': "Go ahead and take advantage of our free 30-day invoice audit, there's no "
                               'cost, no commitment or obligation.',
                       'tip': "Go ahead and take advantage of our free 30-day invoice audit, there's no "
                              'cost, no commitment or obligation.',
                       'timestamp': 61,
                       'timestamp_seconds': 61,
                       'timestamp_label': '[00:01:01]',
                       'url': 'https://www.youtube.com/watch?v=bNqu0vah45U&t=61s',
                       'markdown': '[00:01:01](https://www.youtube.com/watch?v=bNqu0vah45U&t=61s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5eTaFaKQdHY',
                       'title': 'Parcel Shipping Audit',
                       'channel': 'Watchdog Advisory',
                       'author': 'Watchdog Advisory',
                       'text': 'Our fee is simply a portion of your savings and contingent on results, if '
                               "there is no savings then there's no fee.",
                       'tip': 'Our fee is simply a portion of your savings and contingent on results, if '
                              "there is no savings then there's no fee.",
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=5eTaFaKQdHY&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=5eTaFaKQdHY&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eTB0fyueR5A',
                       'title': 'Workflow of a good parcel audit',
                       'channel': 'Share a Refund',
                       'author': 'Share a Refund',
                       'text': 'Share a Refund only splits the refunds on shipments where actions were '
                               'taken by our system to secure refunds, and this results in a lower service '
                               'fee.',
                       'tip': 'Share a Refund only splits the refunds on shipments where actions were '
                              'taken by our system to secure refunds, and this results in a lower service '
                              'fee.',
                       'timestamp': 438,
                       'timestamp_seconds': 438,
                       'timestamp_label': '[00:07:18]',
                       'url': 'https://www.youtube.com/watch?v=eTB0fyueR5A&t=438s',
                       'markdown': '[00:07:18](https://www.youtube.com/watch?v=eTB0fyueR5A&t=438s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PheSsrwvW9c',
                       'title': 'One way to qualify a good parcel audit',
                       'channel': 'Share a Refund',
                       'author': 'Share a Refund',
                       'text': "The credits lower the total amount of the invoice, and we've "
                               'scientifically concluded that filing claims quickly increases the success '
                               'rate of the refund delivered.',
                       'tip': "The credits lower the total amount of the invoice, and we've scientifically "
                              'concluded that filing claims quickly increases the success rate of the '
                              'refund delivered.',
                       'timestamp': 123,
                       'timestamp_seconds': 123,
                       'timestamp_label': '[00:02:03]',
                       'url': 'https://www.youtube.com/watch?v=PheSsrwvW9c&t=123s',
                       'markdown': '[00:02:03](https://www.youtube.com/watch?v=PheSsrwvW9c&t=123s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GnXmnbxCZ-A',
                       'title': 'Reducing Parcel Shipping Costs with Parcel Audits',
                       'channel': 'Cerasis , now part of GlobalTranz',
                       'author': 'Cerasis , now part of GlobalTranz',
                       'text': 'If the total savings is a thousand, a shipper paying 30% to the auditing '
                               'service would still see a net refund of $700.',
                       'tip': 'If the total savings is a thousand, a shipper paying 30% to the auditing '
                              'service would still see a net refund of $700.',
                       'timestamp': 314,
                       'timestamp_seconds': 314,
                       'timestamp_label': '[00:05:14]',
                       'url': 'https://www.youtube.com/watch?v=GnXmnbxCZ-A&t=314s',
                       'markdown': '[00:05:14](https://www.youtube.com/watch?v=GnXmnbxCZ-A&t=314s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5yyeqQ4VAFU',
                       'title': 'Audisee Tutorial',
                       'channel': 'Lojistic',
                       'author': 'Lojistic',
                       'text': 'You can choose multiple invoices all at once from UPS or FedEx, but right '
                               "now Audisee won't let you audit UPS and FedEx invoices at the same time.",
                       'tip': 'You can choose multiple invoices all at once from UPS or FedEx, but right '
                              "now Audisee won't let you audit UPS and FedEx invoices at the same time.",
                       'timestamp': 45,
                       'timestamp_seconds': 45,
                       'timestamp_label': '[00:00:45]',
                       'url': 'https://www.youtube.com/watch?v=5yyeqQ4VAFU&t=45s',
                       'markdown': '[00:00:45](https://www.youtube.com/watch?v=5yyeqQ4VAFU&t=45s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RCPFFZVF7qs',
                       'title': 'Understanding Shipping Invoicing | Invoice Auditing Service | Compete '
                                'Consulting Group',
                       'channel': 'Compete Consulting Group',
                       'author': 'Compete Consulting Group',
                       'text': 'On average four to six percent of packages are delivered late every day, '
                               'and you only have 15 days to claim the money.',
                       'tip': 'On average four to six percent of packages are delivered late every day, '
                              'and you only have 15 days to claim the money.',
                       'timestamp': 17,
                       'timestamp_seconds': 17,
                       'timestamp_label': '[00:00:17]',
                       'url': 'https://www.youtube.com/watch?v=RCPFFZVF7qs&t=17s',
                       'markdown': '[00:00:17](https://www.youtube.com/watch?v=RCPFFZVF7qs&t=17s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'vOX4irOA_Tk',
                       'title': 'Importance of Small Parcel Auditing',
                       'channel': 'Refund Retriever',
                       'author': 'Refund Retriever',
                       'text': 'We start at 50% of whatever we save you, so if in a certain month we get '
                               'you back $50 worth of refunds on late deliveries, our fee is going to be '
                               '25.',
                       'tip': 'We start at 50% of whatever we save you, so if in a certain month we get '
                              'you back $50 worth of refunds on late deliveries, our fee is going to be '
                              '25.',
                       'timestamp': 311,
                       'timestamp_seconds': 311,
                       'timestamp_label': '[00:05:11]',
                       'url': 'https://www.youtube.com/watch?v=vOX4irOA_Tk&t=311s',
                       'markdown': '[00:05:11](https://www.youtube.com/watch?v=vOX4irOA_Tk&t=311s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NKDaSW7CKiQ',
                       'title': 'How does the Parcel Audit work?',
                       'channel': 'Scarbrough Global',
                       'author': 'Scarbrough Global',
                       'text': "We're going to resubmit it, resubmit it, and if it still gets denied, "
                               "we're going to have our internal team actually reach out and talk to a "
                               'live human being about it.',
                       'tip': "We're going to resubmit it, resubmit it, and if it still gets denied, we're "
                              'going to have our internal team actually reach out and talk to a live human '
                              'being about it.',
                       'timestamp': 145,
                       'timestamp_seconds': 145,
                       'timestamp_label': '[00:02:25]',
                       'url': 'https://www.youtube.com/watch?v=NKDaSW7CKiQ&t=145s',
                       'markdown': '[00:02:25](https://www.youtube.com/watch?v=NKDaSW7CKiQ&t=145s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'nGN0KikmdVk',
                       'title': '7 Misconceptions of Parcel Audits',
                       'channel': 'Cerasis , now part of GlobalTranz',
                       'author': 'Cerasis , now part of GlobalTranz',
                       'text': 'If a single audit takes five minutes to complete, that would equal a '
                               'full-time employee working eight hours per day, five days a week, for '
                               'nearly 21 weeks.',
                       'tip': 'If a single audit takes five minutes to complete, that would equal a '
                              'full-time employee working eight hours per day, five days a week, for '
                              'nearly 21 weeks.',
                       'timestamp': 170,
                       'timestamp_seconds': 170,
                       'timestamp_label': '[00:02:50]',
                       'url': 'https://www.youtube.com/watch?v=nGN0KikmdVk&t=170s',
                       'markdown': '[00:02:50](https://www.youtube.com/watch?v=nGN0KikmdVk&t=170s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1JZzLbF5PrI',
                       'title': 'About Refund Retriever UPS & FedEx Parcel Auditing',
                       'channel': 'Refund Retriever',
                       'author': 'Refund Retriever',
                       'text': 'Sending them copies of invoices and getting zero refunds; I quickly '
                               'realized about 10% of my packages were arriving late.',
                       'tip': 'Sending them copies of invoices and getting zero refunds; I quickly '
                              'realized about 10% of my packages were arriving late.',
                       'timestamp': 50,
                       'timestamp_seconds': 50,
                       'timestamp_label': '[00:00:50]',
                       'url': 'https://www.youtube.com/watch?v=1JZzLbF5PrI&t=50s',
                       'markdown': '[00:00:50](https://www.youtube.com/watch?v=1JZzLbF5PrI&t=50s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8Bw_30ivpb4',
                       'title': 'Automatic UPS & FedEx GSR Service Failure Refunds',
                       'channel': 'Refund Retriever',
                       'author': 'Refund Retriever',
                       'text': 'We have never seen UPS give a refund on a late delivered parcel '
                               'automatically.',
                       'tip': 'We have never seen UPS give a refund on a late delivered parcel '
                              'automatically.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=8Bw_30ivpb4&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=8Bw_30ivpb4&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'frD9iyAvyds',
                       'title': 'Parcel Auditing - Empact Parcel',
                       'channel': 'Empact Parcel',
                       'author': 'Empact Parcel',
                       'text': "In other words if your packages are late they're free; the problem is the "
                               "carriers won't tell you what shipments are due a refund.",
                       'tip': "In other words if your packages are late they're free; the problem is the "
                              "carriers won't tell you what shipments are due a refund.",
                       'timestamp': 19,
                       'timestamp_seconds': 19,
                       'timestamp_label': '[00:00:19]',
                       'url': 'https://www.youtube.com/watch?v=frD9iyAvyds&t=19s',
                       'markdown': '[00:00:19](https://www.youtube.com/watch?v=frD9iyAvyds&t=19s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eEERM3QJqyI',
                       'title': 'RAFL Parcel Invoice Auditing Video',
                       'channel': 'RAF Logistics',
                       'author': 'RAF Logistics',
                       'text': "With over 130 different add-on fees the carriers can now charge, it's a "
                               'daunting task.',
                       'tip': "With over 130 different add-on fees the carriers can now charge, it's a "
                              'daunting task.',
                       'timestamp': 17,
                       'timestamp_seconds': 17,
                       'timestamp_label': '[00:00:17]',
                       'url': 'https://www.youtube.com/watch?v=eEERM3QJqyI&t=17s',
                       'markdown': '[00:00:17](https://www.youtube.com/watch?v=eEERM3QJqyI&t=17s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q1.'}]}
