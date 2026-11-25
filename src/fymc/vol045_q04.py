from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'federal-idr-eligibility-open-negotiation-initiation-workflow',
 'question_prompt': 'How do providers determine whether a claim is IDR-eligible and move it from open '
                    'negotiation through initiation, entity selection, and submission?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Filing Federal IDR: Eligibility Screening, Open Negotiation, and Initiation Workflow',
 'subtitle': 'Three-part eligibility test, specified-state vs. federal jurisdiction, 30-business-day open '
             'negotiation and 4-day initiation windows, CMS Notice of IDR Initiation and Resubmission web '
             'form demos, IDR entity selection, CMS disputing-party Q&A, dispute-management software, '
             'outsourced filing services, and catching underpaid OON claims before deadlines close',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from CMS, K&L Gates, Lido, Staffingly, Vee Healthtek, CoGenetix and '
                      'ANS Solutions, and Adam Cartabiano on the Ryan Downs show agree the money in '
                      'federal IDR is won or lost at the screen. Claims qualify through three doors: '
                      'ED-admitted out-of-network events, out-of-network clinicians on in-network events, '
                      'and emergency air ambulance. Plan funding decides whether the claim goes federal or '
                      'to a state process. Open negotiation must start within 30 business days of the '
                      'initial payment or denial and is mandatory proof before arbitration. Initiation '
                      'then opens a four-business-day window that Staffingly calls absolute. Cartabiano '
                      'targets claims paid 15 to 17 percent of charges. Staffingly reports an 88 percent '
                      'win rate at roughly 450 percent of QPA, but one in five disputes is ineligible. The '
                      'speakers split on clocks, IDRE strike counts, and vendor economics.',
 'key_metrics': [{'label': 'IDR initiation window after open negotiation',
                  'metric': 'IDR initiation window after open negotiation',
                  'value': '4 business days',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Cartabiano: once the 30-day open negotiation window ends, filers have '
                             'exactly four business days to submit the case to the CMS portal for '
                             'arbitration.',
                  'source': 'Ryan Downs ([7lqb5ev54mA @ 00:05:15])'},
                 {'label': 'Target underpayment band',
                  'metric': 'Target underpayment band',
                  'value': '15 to 17% of billed charges',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Audits show a 50/50 split between OON payments at 60-100% of charges and '
                             'payments at 15-17% of charges; the low-paid half is the target population, '
                             'pushed toward 45-55% of charges.',
                  'source': 'Ryan Downs ([7lqb5ev54mA @ 00:03:38])'},
                 {'label': 'Provider win rate and award size',
                  'metric': 'Provider win rate and award size',
                  'value': '88% win rate; awards average 450% of QPA',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Staffingly comparison of baseline payments to arbitration outcomes for '
                             'providers that file.',
                  'source': 'Staffingly, Inc ([ASHyX7v13Eo @ 00:01:25])'},
                 {'label': 'Disputes deemed ineligible',
                  'metric': 'Disputes deemed ineligible',
                  'value': '1 in 5 disputes, yielding zero recovery',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Staffingly reports one in five disputes thrown out as ineligible due to '
                             'errors, which drives the case for pre-filing eligibility checks.',
                  'source': 'Staffingly, Inc ([ASHyX7v13Eo @ 00:01:25])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner screens before filing, and the screen starts with three '
                              'qualifying buckets. Adam Cartabiano lays them out on the Ryan Downs show: a '
                              'fully out-of-network event where the admit source was the emergency room, '
                              'an out-of-network charge on an in-network event, and emergency air '
                              'ambulance [0BGnlP4Q71M @ 00:00:23]. Cartabiano flags a common '
                              'misperception. The rule is not limited to ED patients; it turns on admit '
                              'source. A patient who came through the ED and matriculated to observation '
                              'or inpatient status still qualifies, and inpatient is where the big dollars '
                              'come into play [0BGnlP4Q71M @ 00:00:40]. The second bucket drives most of '
                              'the volume in the public CMS files: anesthesiologists, ED docs, '
                              'hospitalists, pathologists, radiologists and surgical groups. Team Health '
                              'and SCP are named as the biggest private submitters [0BGnlP4Q71M @ '
                              '00:01:32]. K&L Gates partner Steve Pine maps the same perimeter from the '
                              'statute side. It covers emergency services at an out-of-network facility '
                              'including facility fees, emergency and non-emergency services by '
                              'out-of-network providers inside in-network facilities, and out-of-network '
                              'air ambulance. Ground ambulance is excluded [VbqFYBvnpas @ 00:01:30]. CMS '
                              'presenter Amanda Brander repeats the identical three triggers as step one '
                              'of the pre-IDR sequence [7lzQt8aAlG0 @ 00:03:30].',
                              'The second consensus point is that plan funding decides the route, and '
                              'getting it wrong ends the claim. Cartabiano splits the map into two kinds '
                              'of states. Federal states push everything through the CMS process. In '
                              'bifurcated states, fully funded plans governed by the state Department of '
                              'Insurance go to the state process, while ERISA self-insured populations '
                              'still follow the federal track [7lqb5ev54mA @ 00:00:20]. The instruction is '
                              'blunt: read the insurance card or call the payer to confirm self-insured '
                              "versus fully funded, because you'll get kicked out if you send it to the "
                              'wrong place [7lqb5ev54mA @ 00:01:25]. Andres, CBO at Lido, has codified '
                              "this fork in Lido's eligibility audit engine. A fully insured Texas plan "
                              'goes to SB 1264 arbitration, and self-funded ERISA plans go federal. The '
                              'team calls the full rule set quite complicated, which is why they '
                              'hard-coded it [NHWPEtUOyK0 @ 00:04:44]. Brander adds the detail that keeps '
                              'volume federal. Some states let self-funded plans opt into the state '
                              'process, but nothing forces them to. The federal process stays open to '
                              'every self-insured plan that has not opted in, and to FEHB carriers whose '
                              'Office of Personnel Management contract does not direct them to a state '
                              'process [7lzQt8aAlG0 @ 00:17:56]. Plan type is therefore the first field '
                              'verified, not the last.',
                              'Third, nobody skips open negotiation and nobody files everything. Brander '
                              'sets the clock: open negotiation must be initiated within 30 business days, '
                              'starting the day the provider receives the initial payment or denial '
                              'notice. Both sides must participate in good faith and hand over the '
                              'information needed if talks fail [7lzQt8aAlG0 @ 00:05:08]. Cartabiano '
                              'explains why the step is non-optional in practice. You must show proof you '
                              'went through it, and if you skip it the arbitration organization rejects '
                              'the claim. A payer that simply ignores you does not owe the demand; you '
                              "just advance to arbitration [7lqb5ev54mA @ 00:02:51]. On selection, Lido's "
                              'Andres opens the Lido workflow with a two-part filter. Is the claim NSA '
                              'eligible? Even if it is, is the expected award value worth the IDR route '
                              '[NHWPEtUOyK0 @ 00:00:51]? Vee Healthtek turns that filter into a triage '
                              'grid. Every paid out-of-network account goes into one of four bins: payment '
                              'complete, recovery justified, value undetermined, or likely recovery that '
                              'does not justify the cost. Each bin gets its own action: close accurate '
                              'accounts, prioritize supported recovery, correct missing data before '
                              'estimating the gap, and monitor low-value patterns without chasing every '
                              'balance [GpHExH5dquQ @ 00:00:32].'],
               'table': {'caption': 'Consensus eligibility and routing rules practitioners apply before '
                                    'any IDR filing',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['ED admit source qualifies the event',
                                   'Qualification turns on the emergency room admit source, not on the '
                                   "patient's later status",
                                   'Patients moving from the ED into inpatient status carry the biggest '
                                   'recovery dollars',
                                   'Ryan Downs ([0BGnlP4Q71M @ 00:00:40])'],
                                  ['OON clinicians on in-network events',
                                   'Out-of-network clinicians at in-network events generate most of the '
                                   'public CMS filing volume',
                                   'Anesthesia, radiology, pathology, hospitalist and ED groups dominate '
                                   'the lists of top submitters',
                                   'Ryan Downs ([0BGnlP4Q71M @ 00:01:32])'],
                                  ['Statutory perimeter excludes ground ambulance',
                                   'The act covers OON facility emergencies, OON providers inside '
                                   'in-network facilities, and air ambulance',
                                   'Ground ambulance claims fall outside the act and come off the filing '
                                   'list immediately',
                                   'KLGatesLaw ([VbqFYBvnpas @ 00:01:30])'],
                                  ['Funding type routes the claim',
                                   'Fully funded plans in bifurcated states go to the state process under '
                                   'the Department of Insurance',
                                   'Confirm self-insured versus fully funded from the card or a payer call '
                                   'before filing',
                                   'Ryan Downs ([7lqb5ev54mA @ 00:01:25])'],
                                  ['Self-funded plans default to federal',
                                   'Self-funded plans that never opted into a state process stay federal '
                                   'in every state',
                                   'Treat non-opt-in self-insured plans as federal IDR candidates '
                                   'regardless of the service state',
                                   'CMSHHSgov ([7lzQt8aAlG0 @ 00:17:56])'],
                                  ['Codify routing rules in software',
                                   'Fully insured Texas plans route to SB 1264 while self-funded ERISA '
                                   'plans go federal',
                                   'Hard-coded rules surface missing ERA or EOB documents that block the '
                                   'eligibility call',
                                   'Lido ([NHWPEtUOyK0 @ 00:04:44])'],
                                  ['Open negotiation is a hard prerequisite',
                                   'Skipping the open negotiation step gets the claim rejected by the '
                                   'arbitration organization',
                                   'Document every negotiation step because proof is required to reach the '
                                   'arbitration stage',
                                   'Ryan Downs ([7lqb5ev54mA @ 00:02:51])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The execution clock runs in fixed blocks. The open negotiation notice must '
                              'carry dates of service, service codes, the initial payment or denial '
                              'notice, an out-of-network rate offer, and sender contact details. Brander '
                              'relays a payer-side complaint that the form cannot identify the customer. '
                              'Providers solve it by adding their own fields or attaching an EOB; '
                              'otherwise the payer reaches back for information [7lzQt8aAlG0 @ 00:09:52]. '
                              'Cartabiano anchors that offer to the in-network commercial equivalent. '
                              'Audits of client organizations find a 50/50 split. The half paid around 15 '
                              'to 17 percent of billed charges, against a QPA typically couched at roughly '
                              '100 to 115 percent of Medicare, is the population targeted toward 45, 50, '
                              'or 55 percent of charges [7lqb5ev54mA @ 00:03:38]. When the 30 business '
                              'days expire without a deal, the CMS web form demo allows four business days '
                              'to initiate [cw4MI_h6Gns @ 00:00:05]. Staffingly calls that window '
                              'absolute: a miss forfeits the claim entirely [ASHyX7v13Eo @ 00:02:49]. '
                              'Cartabiano explains why four days hurts. The arbitration package is far '
                              'heavier than the single negotiation letter, and fresh claims keep rolling '
                              'off their own negotiation periods while the team builds it. Without '
                              'structure, the workload compounds fast.',
                              'Inside the Notice of IDR Initiation web form, the traps are mechanical. The '
                              'demo warns the form must be completed in one session and times out after 60 '
                              'minutes of inactivity. An open negotiation start date more than 34 business '
                              'days back triggers an extension-justification prompt, and at least one '
                              'upload proving that start date is mandatory [cw4MI_h6Gns @ 00:04:22]. Each '
                              'line item needs a claim number, date of service, QPA, a claim-and-QPA '
                              'document, cost sharing, service code, up to four two-character modifiers, '
                              'and place of service. The portal blocks any duplicate combination of claim '
                              'number, date, code, and modifier unless a cooling-off closure or approved '
                              "extension applies [cw4MI_h6Gns @ 00:11:17]. CMS's Matt Meidell fixes the "
                              'offer math. The offer is the full amount requested, including what was '
                              'already paid, expressed both as a dollar figure and as a percentage of the '
                              'QPA. The QPA entered should match the initial payment or denial notice '
                              "[7lzQt8aAlG0 @ 00:20:34]. Lido's Andres flags the newest bottleneck: the "
                              'centralized IDR gateway no longer offers an API. Filers either key data '
                              'manually or use a vendor that automates entry without one, which Lido '
                              'claims to have caught ahead of the market [NHWPEtUOyK0 @ 00:06:21].',
                              'Batching is where fee savings and rejections collide. Meidell lists the '
                              'four batching tests: same provider, group, or facility; same plan or '
                              'issuer; same or similar service code; and all items furnished within the '
                              'same 30 business day period [7lzQt8aAlG0 @ 00:23:43]. Staffingly confirms '
                              'CMS allows grouping to save fees but says improperly grouped claims are '
                              'immediately rejected [ASHyX7v13Eo @ 00:02:33]. The evidence package is the '
                              "other heavy lift. Cartabiano's three core elements are a demographic case "
                              'positioning the organization as one that commands premium in-network rates, '
                              'a clinical complexity review pulled from the medical record, and a '
                              'financial comparison. That comparison lines up the in-network commercial '
                              'rate, amount paid, Medicare, and Medicaid for that service and region, with '
                              'specifics rather than broad strokes [7lqb5ev54mA @ 00:05:47]. Cartabiano '
                              'sharpens the package by meeting IDR entities directly to learn what they '
                              'score as a successful argument, then building that feedback into the '
                              'process. The CoGenetix and ANS Solutions team builds the same thing as '
                              'standing provider profiles covering credentials, service complexity, and '
                              'regional market benchmarks. They argue fellowship training and surgical '
                              'complexity are powerful arbitration tools for orthopedic groups '
                              '[dTrA6r3pGyE @ 00:01:54].'],
               'table': {'caption': 'Hard clocks, form rules, and cost figures for the open negotiation to '
                                    'initiation run',
                         'headers': ['Mechanic',
                                     'Exact Number or Rule',
                                     'Execution Detail',
                                     'Expert Source'],
                         'rows': [['Open negotiation initiation window',
                                   '30 business days from receipt of the initial payment or denial notice',
                                   'The clock starts the day the provider receives the payment or the '
                                   'denial',
                                   'CMSHHSgov ([7lzQt8aAlG0 @ 00:05:08])'],
                                  ['Federal IDR initiation window',
                                   'Four business days after the 30-business-day open negotiation period '
                                   'ends',
                                   'Initiation only proceeds if the parties reached no agreement on the '
                                   'out-of-network rate',
                                   'CMSHHSgov ([cw4MI_h6Gns @ 00:00:05])'],
                                  ['Web form session limit',
                                   'Single session required, with a timeout after 60 minutes of inactivity',
                                   'Negotiation proof plus claim and QPA documents are uploaded inside '
                                   'that session',
                                   'CMSHHSgov ([cw4MI_h6Gns @ 00:01:18])'],
                                  ['Late start-date flag',
                                   'A start date beyond 34 business days triggers an extension '
                                   'justification prompt',
                                   'Upload the extension approval or evidence tied to the cooling-off '
                                   'dispute reference number',
                                   'CMSHHSgov ([cw4MI_h6Gns @ 00:04:22])'],
                                  ['Batch date-of-service rule',
                                   'All batched items must fall within 30 business days of each other',
                                   'The rule does not apply when the 90-calendar-day cooling off period '
                                   'applies',
                                   'CMSHHSgov ([cw4MI_h6Gns @ 00:12:56])'],
                                  ['Serving the non-initiating party',
                                   'Send the initiation PDF to the non-initiating party on the submission '
                                   'day',
                                   'Download the PDF from the confirmation page because the portal does '
                                   'not forward it',
                                   'CMSHHSgov ([cw4MI_h6Gns @ 00:15:54])'],
                                  ['Outsourced filing cost versus in-house',
                                   'Flat $399 per week versus a $55,000 to $75,000 in-house specialist '
                                   'salary',
                                   'Most practices go live in 14 days, with a weekly KPI dashboard on '
                                   'throughput',
                                   'Staffingly, Inc ([ASHyX7v13Eo @ 00:04:27])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Filing-floor moves that protect the claim and the margin',
                           'body': 'Four tactics practitioners use to keep offers alive, rank inventory, '
                                   'and sharpen submissions before the four-day window closes.',
                           'items': ['Pay the IDR entity fee and the administrative fee together with the '
                                     'offer. An offer is not considered received until both are paid, and '
                                     'an unreceived offer hands the other side its number as the final '
                                     'payment amount [CMSHHSgov — 7lzQt8aAlG0 @ 00:25:17]',
                                     'Rank inventory by net recoverable value, not balance size. Weigh the '
                                     'likely additional payment, filing expense, specialist effort, and '
                                     'time remaining, and keep evidence preparation upstream of the filing '
                                     'decision [Vee Healthtek — s3194z7bdwY @ 00:00:54]',
                                     'Aggregate small variances. A $200 recoverable gap across 5,000 '
                                     'claims equals $1 million before fees and collection costs, so '
                                     'per-claim thresholds should not hide recurring exposure [Vee '
                                     'Healthtek — GpHExH5dquQ @ 00:01:25]',
                                     'Meet with the IDR entities and ask what they treat as a successful '
                                     'argument. They will tell you, and that feedback goes straight back '
                                     'into the submission process [Ryan Downs — 7lqb5ev54mA @ 00:09:44]']},
               'sop_steps': [{'step': 1,
                              'title': 'Ingest documents and run the eligibility audit',
                              'action': 'Pull the CMS-1500, 835, EOB, and insurance card into one record, '
                                        'then decide eligibility and route.',
                              'detail': 'Lido ingests from email, Google Drive, OneDrive, SharePoint, and '
                                        'the EMR, then flags missing 835 or EOB documents that block the '
                                        'eligibility call and generates document requests from the same '
                                        'screen [Lido — NHWPEtUOyK0 @ 00:01:52]'},
                             {'step': 2,
                              'title': 'Send the open negotiation notice',
                              'action': 'Within 30 business days of the payment or denial, send a notice '
                                        'carrying dates of service, service codes, the initial payment or '
                                        'denial, an offer, and contact details.',
                              'detail': 'These are the required notice elements, and they should already '
                                        "appear on the payer's initial payment or denial of payment "
                                        '[CMSHHSgov — 7lzQt8aAlG0 @ 00:06:15]'},
                             {'step': 3,
                              'title': 'Build the arbitration package during negotiation',
                              'action': 'Assemble the organization demographics, the clinical complexity '
                                        'review, and the financial rate comparison before the negotiation '
                                        'period lapses.',
                              'detail': 'Cartabiano requires a clinical complexity case plus an in-network '
                                        'commercial versus paid versus Medicare versus Medicaid comparison '
                                        'for that service and region, because the four-day window leaves '
                                        'no room to start from scratch [Ryan Downs — 7lqb5ev54mA @ '
                                        '00:06:04]'},
                             {'step': 4,
                              'title': 'File in the portal and serve the payer',
                              'action': 'Submit the Notice of IDR Initiation, pick a preferred certified '
                                        'IDR entity, attest to no conflict of interest, then send the PDF '
                                        'to the payer.',
                              'detail': 'The initiating party must download the PDF and send a copy to the '
                                        'non-initiating party on the same day the form is submitted, and '
                                        'both sides then receive portal confirmation emails [CMSHHSgov — '
                                        'cw4MI_h6Gns @ 00:15:54]'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Win-rate math is where the vendor pitches split hardest. CoGenetix and ANS '
                              'Solutions open with a win rate of over 90% for providers, later quoting a '
                              '90% to 95% track record, and cite industry data showing approximately 86% '
                              'of decisions favoring providers [dTrA6r3pGyE @ 00:01:16]. Staffingly runs a '
                              'lower headline of 88% wins with payouts averaging 450% of the qualifying '
                              'payment amount, then immediately cuts that number down: one in five '
                              'disputes was deemed ineligible due to errors and yielded zero recovery '
                              "[ASHyX7v13Eo @ 00:01:25]. Adam Cartabiano, appearing on Ryan Downs' mini "
                              'episodes, attacks the idea that any win rate is predictable at the claim '
                              'level. He says IDREs lack an objective way to evaluate each claim on its '
                              'own merit, so two identical claims for the same service, submitted with '
                              'identical information, can split with one won and one lost [7lqb5ev54mA @ '
                              '00:09:05]. Some IDREs judge holistically from a case-rate perspective while '
                              'others go through every single CPT, HCPCS and DRG code before landing on a '
                              'fair number [7lqb5ev54mA @ 00:08:28]. His fix is consistency: meet with the '
                              'IDREs to learn what they treat as a successful argument, then build that '
                              'feedback into purpose-built technology so every submission argues the same '
                              'way with high confidence.',
                              'The fee-risk story depends entirely on who is talking. CoGenetix tells '
                              'providers that IDR filing fees are a necessary component but are typically '
                              'reimbursed by the payer because the win rate is so high, framing the whole '
                              'program as a low-risk, high-reward strategy [dTrA6r3pGyE @ 00:02:11]. '
                              'Staffingly paints the opposite picture at system scale, citing Georgetown '
                              'University research that IDR administrative fees reached $844 million in '
                              'just the first half of 2025, and argues that practices managing the '
                              'workflow internally are actively losing money once labor costs and '
                              'filing-error penalties are counted [ASHyX7v13Eo @ 00:00:49]. CMS staff on '
                              'the disputing-party call draw the hard line: administrative fees are '
                              'non-refundable, although they should not be collected until the certified '
                              'IDR entity finishes its initial screening for eligibility [7lzQt8aAlG0 @ '
                              '00:26:12]. Vee Healthtek runs a middle playbook built on pre-filing triage. '
                              'It ranks inventory by net recoverable value, weighing likely additional '
                              'payment, filing expense, specialist effort and time remaining, and warns '
                              'that a large balance is not automatically the best opportunity when '
                              'stronger evidence and cheaper collection sit elsewhere [s3194z7bdwY @ '
                              '00:01:11]. A repeated payer methodology hitting hundreds of similar claims, '
                              'in its view, calls for negotiation, payment validation or an upstream '
                              'correction instead of recovering the same shortfall dispute after dispute.',
                              'Operating models diverge on who carries the workload. Staffingly prices an '
                              'in-house specialist at $55,000 to $75,000 a year against 32% annual billing '
                              'turnover and an average 68 days to replace, then sells an outsourced, '
                              'AI-augmented team for a flat $399 per week, with most practices live in 14 '
                              'days [ASHyX7v13Eo @ 00:04:27]. CoGenetix goes strictly performance-based, '
                              'with no upfront costs and a tiered structure, plus a complimentary '
                              'out-of-network assessment to open the relationship [dTrA6r3pGyE @ '
                              '00:03:49]. Lido splits the difference, running an end-to-end IDR resolution '
                              'service internally while letting customers who prefer to do the process '
                              'themselves work the same eligibility data in its portal. Even the IDRE '
                              'selection mechanics get described differently. Cartabiano says there are 13 '
                              'IDRE vendors, soon going to 15, and that the payer can reject the '
                              "provider's pick up to three times before the fourth gets assigned "
                              'automatically [7lqb5ev54mA @ 00:07:36]. CMS staff describe a tighter clock: '
                              'the non-initiating party has three business days to agree with the '
                              'preferred entity or make an alternative selection, and if the parties '
                              'cannot agree, the Departments randomly select a certified IDR entity no '
                              'later than six business days after initiation and notify both sides by '
                              'email [7lzQt8aAlG0 @ 00:16:43].'],
               'table': {'caption': 'Side-by-side playbooks where IDR practitioners take different '
                                    'positions',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Expected provider win rate before filing',
                                   'CoGenetix and ANS claim over 90% wins and a 90% to 95% track record',
                                   'Staffingly cites 88% wins but one in five disputes ineligible with '
                                   'zero recovery',
                                   'CoGenetix Wellness ([m8zdt3GQSjY @ 00:02:30]); Staffingly, Inc '
                                   '([ASHyX7v13Eo @ 00:01:25])'],
                                  ['Risk carried by IDR filing fees',
                                   'Fees are typically reimbursed by the payer, making IDR low-risk and '
                                   'high-reward',
                                   'Administrative fees are non-refundable, collected only after the IDRE '
                                   'eligibility screen',
                                   'CoGenetix Wellness ([m8zdt3GQSjY @ 00:02:11]); CMSHHSgov ([7lzQt8aAlG0 '
                                   '@ 00:26:12])'],
                                  ['Predictability of a single claim outcome',
                                   'Lido projects expected payout weighted by confidence from its award '
                                   'history warehouse',
                                   'Cartabiano reports identical claims with identical evidence can be won '
                                   'and lost',
                                   'Lido ([NHWPEtUOyK0 @ 00:03:39]); Ryan Downs ([7lqb5ev54mA @ '
                                   '00:09:05])'],
                                  ['How the certified IDR entity gets chosen',
                                   'Payer can reject the provider pick three times, fourth is '
                                   'auto-assigned',
                                   'Three business days to agree, then random selection within six '
                                   'business days',
                                   'Ryan Downs ([7lqb5ev54mA @ 00:07:36]); CMSHHSgov ([7lzQt8aAlG0 @ '
                                   '00:16:43])'],
                                  ['Who staffs and runs the dispute workflow',
                                   'Staffingly outsourced specialists at a flat $399 per week versus a '
                                   '$75,000 salary',
                                   'P3Fusion robotic process automation selects the IDR entity and AI '
                                   'reads dispute emails',
                                   'Staffingly, Inc ([ASHyX7v13Eo @ 00:04:27]); P3Fusion ([IQXlcicB37I @ '
                                   '00:00:49])'],
                                  ['How much weight the QPA should carry',
                                   'CoGenetix says insurers often set the QPA well below market value',
                                   'Vee Healthtek calls QPA a reference point; KL Gates reports the Texas '
                                   'court vacated the presumption',
                                   'CoGenetix Wellness ([m8zdt3GQSjY @ 00:00:56]); Vee Healthtek '
                                   '([GpHExH5dquQ @ 00:01:07]); KLGatesLaw ([VbqFYBvnpas @ 00:13:00])'],
                                  ['Whether awarded money actually arrives on time',
                                   'CoGenetix says payers cannot claw back and must pay awards within 30 '
                                   'days',
                                   'Staffingly says nearly a quarter of awarded payments are delayed or '
                                   'underpaid by insurers',
                                   'CoGenetix Wellness ([m8zdt3GQSjY @ 00:04:25]); Staffingly, Inc '
                                   '([ASHyX7v13Eo @ 00:02:49])']]},
               'key_metrics': [{'label': 'Provider win rate and payout claimed by Staffingly',
                                'metric': 'Provider win rate and payout claimed by Staffingly',
                                'value': '88% of disputes won; payouts average 450% of the QPA',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Offset by one in five disputes deemed ineligible due to '
                                           'errors, yielding zero recovery.',
                                'source': 'Staffingly, Inc ([ASHyX7v13Eo @ 00:01:25])'},
                               {'label': 'IDR administrative fees in the first half of 2025',
                                'metric': 'IDR administrative fees in the first half of 2025',
                                'value': '$844 million',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Cited by Staffingly from Georgetown research to argue internal '
                                           'IDR programs lose money.',
                                'source': 'Staffingly, Inc ([ASHyX7v13Eo @ 00:00:49])'},
                               {'label': 'IDRE vendor pool and payer veto',
                                'metric': 'IDRE vendor pool and payer veto',
                                'value': '13 vendors, soon 15; payer can reject up to three times',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Cartabiano says the fourth selection is assigned '
                                           'automatically.',
                                'source': 'Ryan Downs ([7lqb5ev54mA @ 00:07:36])'}]},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures happen on the clock, not in front of the '
                              'arbitrator. Staffingly calls the post-negotiation filing slot an absolute '
                              'four business day window and says missing it forfeits the claim entirely '
                              '[ASHyX7v13Eo @ 00:02:49]. Cartabiano explains why teams blow it: the open '
                              'negotiation letter is one form with a small amount of information, but the '
                              'arbitration submission needs hospital demographic positioning, a clinical '
                              'complexity review pulled from the medical record, and a financial '
                              'comparison of in-network commercial, paid, Medicare and Medicaid rates, all '
                              'while new cases keep running off their own negotiation periods [7lqb5ev54mA '
                              '@ 00:05:47]. Skipping open negotiation is fatal too, because the '
                              'arbitration organization rejects the claim without proof that the first '
                              'step happened [7lqb5ev54mA @ 00:02:51]. Venue mistakes kill files before '
                              'the clock even matters. In bifurcated states, fully funded plans governed '
                              'by the state Department of Insurance go to the state process while '
                              'self-insured ERISA populations stay federal, and Cartabiano warns that '
                              'sending a claim to the wrong place gets it kicked out. Lido codifies the '
                              'same split, routing fully insured Texas plans to SB 1264 arbitration and '
                              'self-funded ERISA plans to federal IDR [NHWPEtUOyK0 @ 00:04:44].',
                              'The CMS web form demos surface a second layer of traps that cost operators '
                              'real filings. The Notice of IDR Initiation form must be completed in a '
                              'single session and times out after 60 minutes of inactivity; it requires at '
                              'least one upload proving the open negotiation start date, and if that date '
                              'is more than 34 business days before the current date it forces an '
                              'extension justification [cw4MI_h6Gns @ 00:04:22]. Answering that the '
                              'provider received patient consent to waive surprise billing protections '
                              'makes the dispute ineligible, and the form blocks duplicate line items '
                              'sharing the same claim number, date of service, service code and modifiers '
                              '[cw4MI_h6Gns @ 00:11:17]. After submission the burden flips to the filer: '
                              'CMS staff say the initiation notice will not be available in the portal, so '
                              'the initiating party must send the copy to the non-initiating party '
                              'directly [7lzQt8aAlG0 @ 00:15:33]. On the resubmission form, the filer must '
                              'hit Print PDF before Continue Submitting because there is no way back to '
                              'that confirmation page afterwards, and the initiating party alone is '
                              'responsible for confirming every regrouped line item still meets batching '
                              'and bundling criteria [Vy31vkzfNBE @ 00:09:48]. The original demo adds that '
                              'the PDF copy goes to the non-initiating party on the same day the form is '
                              'submitted.',
                              'Economics checks fail quietly upstream. Vee Healthtek warns that a paid '
                              'out-of-network claim can still leave recoverable money behind because '
                              'payment status confirms that money moved, not that the amount was accurate; '
                              'automatic adjustments hide variances before a specialist ever looks, and a '
                              '$200 recoverable variance across 5,000 claims is $1 million before fees and '
                              'collection costs [GpHExH5dquQ @ 00:01:25]. Its second video adds that '
                              'recovery can fail before arbitration begins when a low payment posts as '
                              'final and the opportunity closes before anyone takes responsibility '
                              '[s3194z7bdwY @ 00:00:00]. Lido shows the document version of that failure: '
                              'a missing 835 and EOB block a final eligibility call even when the CMS-1500 '
                              'lines up with the NSA rules [NHWPEtUOyK0 @ 00:02:50]. Inside the process, '
                              'CMS staff spell out a default trap: an offer is not considered received '
                              'until both the certified IDR entity fee and the administrative fee are '
                              "paid, and if one side's offer is not received the entity selects the other "
                              "party's offer as the final payment amount [7lzQt8aAlG0 @ 00:25:17]. They "
                              'also want the offer stated as the full requested amount including anything '
                              'already paid, expressed as a dollar figure and a percentage of the QPA, and '
                              'the QPA entered should be the one listed on the initial payment or denial '
                              'notice.'],
               'table': {'caption': 'Firsthand IDR failure modes and the operator responses practitioners '
                                    'teach',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Warned',
                                     'Operator Response Taught',
                                     'Expert Source'],
                         'rows': [['Missing the four business day initiation window',
                                   'Staffingly says missing this absolute deadline forfeits the claim '
                                   'entirely',
                                   'Build workflow structure and automate information collection before '
                                   'the window opens',
                                   'Staffingly, Inc ([ASHyX7v13Eo @ 00:02:49]); Ryan Downs ([7lqb5ev54mA @ '
                                   '00:07:01])'],
                                  ['Sending the claim to the wrong venue',
                                   'Claims sent to the wrong state or federal process get kicked out',
                                   'Confirm self-insured versus fully funded via the plan card or by '
                                   'calling the payer',
                                   'Ryan Downs ([7lqb5ev54mA @ 00:01:25])'],
                                  ['Skipping the open negotiation step entirely',
                                   'The arbitration organization rejects claims lacking proof of open '
                                   'negotiation',
                                   'Send the standard CMS open negotiation letter to the NSA email listed '
                                   'on the EOB',
                                   'Ryan Downs ([7lqb5ev54mA @ 00:02:19])'],
                                  ['Grouping claims into an improper batch',
                                   'Improperly grouped claims are immediately rejected by the federal '
                                   'process',
                                   'Batch only same provider, same plan, same or similar code, within 30 '
                                   'business days',
                                   'Staffingly, Inc ([ASHyX7v13Eo @ 00:02:33]); CMSHHSgov ([7lzQt8aAlG0 @ '
                                   '00:24:02])'],
                                  ['Filing claims that were never eligible',
                                   'One in five disputes deemed ineligible due to errors, yielding zero '
                                   'recovery',
                                   'Run a codified eligibility audit and request missing documents before '
                                   'filing',
                                   'Staffingly, Inc ([ASHyX7v13Eo @ 00:01:25]); Lido ([NHWPEtUOyK0 @ '
                                   '00:03:12])'],
                                  ['Unpaid fees at the offer deadline',
                                   "Offer counts as not received and the other party's offer is selected",
                                   'Pay the certified IDR entity fee and administrative fee with the offer '
                                   'submission',
                                   'CMSHHSgov ([7lzQt8aAlG0 @ 00:24:47])'],
                                  ['Awards that are won but never fully paid',
                                   'Payers sometimes sit on payments after an official award is issued',
                                   'Compare determination to cash received, escalate differences, and file '
                                   'CMS complaints',
                                   'Vee Healthtek ([s3194z7bdwY @ 00:02:01]); Lido ([NHWPEtUOyK0 @ '
                                   '00:07:40])']]},
               'key_metrics': [{'label': 'Share of disputes deemed ineligible',
                                'metric': 'Share of disputes deemed ineligible',
                                'value': 'One in five, yielding zero recovery',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Staffingly ties ineligibility to filing errors that erase the '
                                           'value of an 88% win rate.',
                                'source': 'Staffingly, Inc ([ASHyX7v13Eo @ 00:01:25])'},
                               {'label': 'Portfolio variance hidden in paid claims',
                                'metric': 'Portfolio variance hidden in paid claims',
                                'value': '$200 across 5,000 claims equals $1 million before fees',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Vee Healthtek says this does not mean every claim should be '
                                           'disputed, only that thresholds should not hide recurring '
                                           'exposure.',
                                'source': 'Vee Healthtek ([GpHExH5dquQ @ 00:01:25])'},
                               {'label': 'Initiation web form inactivity timeout',
                                'metric': 'Initiation web form inactivity timeout',
                                'value': '60 minutes; form must be completed in a single session',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Shown on the welcome page of the Notice of IDR Initiation web '
                                           'form demo.',
                                'source': 'CMSHHSgov ([cw4MI_h6Gns @ 00:01:18])'},
                               {'label': 'Awarded payments delayed or underpaid',
                                'metric': 'Awarded payments delayed or underpaid',
                                'value': 'Nearly a quarter of all awarded IDR payments',
                                'confidence': 'attributed_practitioner_claim',
                                'context': 'Staffingly says even a victory requires aggressive follow-up.',
                                'source': 'Staffingly, Inc ([ASHyX7v13Eo @ 00:02:49])'}],
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Pre-Filing Kill Switches',
                           'body': 'Run every claim through these four checks before a dollar of fees or '
                                   'an hour of specialist time goes into an IDR filing.',
                           'items': ['Confirm plan funding and state route first, because a claim sent to '
                                     'the wrong process gets kicked out [Ryan Downs — 7lqb5ev54mA @ '
                                     '00:01:25].',
                                     'Hold any initiation that lacks an uploaded proof of the open '
                                     'negotiation start date, and expect an extension justification if '
                                     'that date is more than 34 business days old [CMSHHSgov — cw4MI_h6Gns '
                                     '@ 00:04:22].',
                                     'Never let a posted remit close the account; one owner carries the '
                                     'claim position, deadline and unresolved barriers [Vee Healthtek — '
                                     's3194z7bdwY @ 00:00:17].',
                                     'Pay both the certified IDR entity fee and the administrative fee '
                                     "with the offer, or the other side's offer wins by default [CMSHHSgov "
                                     '— 7lzQt8aAlG0 @ 00:25:17].']}}],
 'pull_quote': '"I submit the exact same information, the first claim could be won and the second claim '
               'could be lost." — Adam Cartabiano on Ryan Downs (7lqb5ev54mA @ 00:09:05).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Determine whether each claim is NSA eligible and whether its expected award value '
                      'justifies the IDR route before filing [Lido — NHWPEtUOyK0 @ 00:00:51].',
                      'Route by plan funding: fully funded plans in bifurcated states go to the state '
                      'process, self-insured ERISA plans go federal [Ryan Downs — 7lqb5ev54mA @ 00:01:25].',
                      'Send the open negotiation notice with dates of service, service codes, initial '
                      'payment or denial, an out-of-network rate offer, and contact information [CMSHHSgov '
                      '— 7lzQt8aAlG0 @ 00:06:15].',
                      'Pre-build the arbitration package of hospital demographics, clinical complexity '
                      'review, and financial rate comparison before the four business day window opens '
                      '[Ryan Downs — 7lqb5ev54mA @ 00:06:04].',
                      'After submitting the initiation form, print the PDF and send it to the '
                      'non-initiating party on the same day [CMSHHSgov — cw4MI_h6Gns @ 00:15:54].',
                      'Follow every award through payment, compare the determination with cash received, '
                      'escalate differences, and reconcile final cash [Vee Healthtek — s3194z7bdwY @ '
                      '00:02:01].'],
 'statutory_citations': [{'title': 'CMSHHSgov — Notice of IDR Initiation Web Form Demo [00:04:22]',
                          'url': 'https://www.youtube.com/watch?v=cw4MI_h6Gns&t=262s',
                          'relevance': 'Primary practitioner testimony on open negotiation start-date '
                                       'evidence, extension justifications, and eligibility screening '
                                       'inside the initiation web form.'},
                         {'title': 'CMSHHSgov — An Overview of the Independent Dispute Resolution Process '
                                   'for Disputing Parties, Part II [00:24:02]',
                          'url': 'https://www.youtube.com/watch?v=7lzQt8aAlG0&t=1442s',
                          'relevance': 'Primary practitioner testimony on batching criteria, offer '
                                       "formatting, fee timing, and default selection of the other party's "
                                       'offer.'},
                         {'title': 'Ryan Downs — Mini Episode: Breaking Down The IDR Process with Adam '
                                   'Cartabiano [00:05:15]',
                          'url': 'https://www.youtube.com/watch?v=7lqb5ev54mA&t=315s',
                          'relevance': 'Primary practitioner testimony on the four business day initiation '
                                       'window and the argument package needed to win.'},
                         {'title': 'Staffingly, Inc — NSA IDR Dispute Filing Services for Medical '
                                   'Practices | Recover What Insurers Owe [00:02:33]',
                          'url': 'https://www.youtube.com/watch?v=ASHyX7v13Eo&t=153s',
                          'relevance': 'Primary practitioner testimony on batching rejections, deadline '
                                       'forfeiture, and in-house versus outsourced IDR economics.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'VbqFYBvnpas',
                       'title': 'Navigating the Independent Dispute Resolution Process Under the No '
                                'Surprises Act',
                       'channel': 'KLGatesLaw',
                       'author': 'KLGatesLaw',
                       'text': 'The court did not vacate the October final rule in its entirety, just the '
                               'portion that dealt with the QPA presumption, so the IDR process remains in '
                               'effect today.',
                       'tip': 'The court did not vacate the October final rule in its entirety, just the '
                              'portion that dealt with the QPA presumption, so the IDR process remains in '
                              'effect today.',
                       'timestamp': 780,
                       'timestamp_seconds': 780,
                       'timestamp_label': '[00:13:00]',
                       'url': 'https://www.youtube.com/watch?v=VbqFYBvnpas&t=780s',
                       'markdown': '[00:13:00](https://www.youtube.com/watch?v=VbqFYBvnpas&t=780s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7lzQt8aAlG0',
                       'title': 'An Overview of the Independent Dispute Resolution Process for Disputing '
                                'Parties, Part II',
                       'channel': 'CMSHHSgov',
                       'author': 'CMSHHSgov',
                       'text': 'An offer will not be considered received by the certified IDR entity until '
                               'the certified IDR entity fee and the administrative fee have been paid.',
                       'tip': 'An offer will not be considered received by the certified IDR entity until '
                              'the certified IDR entity fee and the administrative fee have been paid.',
                       'timestamp': 1517,
                       'timestamp_seconds': 1517,
                       'timestamp_label': '[00:25:17]',
                       'url': 'https://www.youtube.com/watch?v=7lzQt8aAlG0&t=1517s',
                       'markdown': '[00:25:17](https://www.youtube.com/watch?v=7lzQt8aAlG0&t=1517s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NHWPEtUOyK0',
                       'title': 'Is This Claim Eligible for IDR? How to Check Before You File (No '
                                'Surprises Act)',
                       'channel': 'Lido',
                       'author': 'Lido',
                       'text': "You don't always want to go the IDR route; the first thing you need to do "
                               'is determine if a claim is NSA eligible.',
                       'tip': "You don't always want to go the IDR route; the first thing you need to do "
                              'is determine if a claim is NSA eligible.',
                       'timestamp': 51,
                       'timestamp_seconds': 51,
                       'timestamp_label': '[00:00:51]',
                       'url': 'https://www.youtube.com/watch?v=NHWPEtUOyK0&t=51s',
                       'markdown': '[00:00:51](https://www.youtube.com/watch?v=NHWPEtUOyK0&t=51s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dTrA6r3pGyE',
                       'title': 'CoGenetix & ANS Solutions- OON IDR Webinar',
                       'channel': 'Ben Martin',
                       'author': 'Ben Martin',
                       'text': 'IDR filing fees are a necessary component, but because our win rate is so '
                               'high, these costs are typically reimbursed by the payer.',
                       'tip': 'IDR filing fees are a necessary component, but because our win rate is so '
                              'high, these costs are typically reimbursed by the payer.',
                       'timestamp': 131,
                       'timestamp_seconds': 131,
                       'timestamp_label': '[00:02:11]',
                       'url': 'https://www.youtube.com/watch?v=dTrA6r3pGyE&t=131s',
                       'markdown': '[00:02:11](https://www.youtube.com/watch?v=dTrA6r3pGyE&t=131s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 's3194z7bdwY',
                       'title': 'How to Improve Out-of-Network Reimbursement and IDR Recovery',
                       'channel': 'Vee Healthtek',
                       'author': 'Vee Healthtek',
                       'text': 'Keep evidence preparation upstream; waiting until a filing decision can '
                               'leave too little time to assemble a defensible submission.',
                       'tip': 'Keep evidence preparation upstream; waiting until a filing decision can '
                              'leave too little time to assemble a defensible submission.',
                       'timestamp': 54,
                       'timestamp_seconds': 54,
                       'timestamp_label': '[00:00:54]',
                       'url': 'https://www.youtube.com/watch?v=s3194z7bdwY&t=54s',
                       'markdown': '[00:00:54](https://www.youtube.com/watch?v=s3194z7bdwY&t=54s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'IQXlcicB37I',
                       'title': 'No Surprises Act Dispute Management Solution | IDR | P3Fusion',
                       'channel': 'P3Fusion',
                       'author': 'P3Fusion',
                       'text': 'Once a dispute is initiated in the NSA portal the system automatically '
                               'tracks emails, reads the notice of IDR initiation and manages the entire '
                               'process from that point forward.',
                       'tip': 'Once a dispute is initiated in the NSA portal the system automatically '
                              'tracks emails, reads the notice of IDR initiation and manages the entire '
                              'process from that point forward.',
                       'timestamp': 33,
                       'timestamp_seconds': 33,
                       'timestamp_label': '[00:00:33]',
                       'url': 'https://www.youtube.com/watch?v=IQXlcicB37I&t=33s',
                       'markdown': '[00:00:33](https://www.youtube.com/watch?v=IQXlcicB37I&t=33s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Vy31vkzfNBE',
                       'title': 'No Surprises Act: Notice of IDR Initiation - Resubmission Web Form Demo',
                       'channel': 'CMSHHSgov',
                       'author': 'CMSHHSgov',
                       'text': 'It is the responsibility of the initiating party to review all line items '
                               'in a particular grouping and ensure that any line items being resubmitted '
                               'together are compliant with federal IDR batching and bundling criteria.',
                       'tip': 'It is the responsibility of the initiating party to review all line items '
                              'in a particular grouping and ensure that any line items being resubmitted '
                              'together are compliant with federal IDR batching and bundling criteria.',
                       'timestamp': 264,
                       'timestamp_seconds': 264,
                       'timestamp_label': '[00:04:24]',
                       'url': 'https://www.youtube.com/watch?v=Vy31vkzfNBE&t=264s',
                       'markdown': '[00:04:24](https://www.youtube.com/watch?v=Vy31vkzfNBE&t=264s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cw4MI_h6Gns',
                       'title': 'Notice of IDR Initiation Web Form Demo',
                       'channel': 'CMSHHSgov',
                       'author': 'CMSHHSgov',
                       'text': 'If surprise billing protections were waived, the dispute will not be '
                               'eligible.',
                       'tip': 'If surprise billing protections were waived, the dispute will not be '
                              'eligible.',
                       'timestamp': 303,
                       'timestamp_seconds': 303,
                       'timestamp_label': '[00:05:03]',
                       'url': 'https://www.youtube.com/watch?v=cw4MI_h6Gns&t=303s',
                       'markdown': '[00:05:03](https://www.youtube.com/watch?v=cw4MI_h6Gns&t=303s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ASHyX7v13Eo',
                       'title': 'NSA IDR Dispute Filing Services for Medical Practices | Recover What '
                                'Insurers Owe',
                       'channel': 'Staffingly, Inc',
                       'author': 'Staffingly, Inc',
                       'text': 'CMS allows claims to be grouped to save fees, but batching rules are '
                               'complex, and improperly grouped claims are immediately rejected.',
                       'tip': 'CMS allows claims to be grouped to save fees, but batching rules are '
                              'complex, and improperly grouped claims are immediately rejected.',
                       'timestamp': 153,
                       'timestamp_seconds': 153,
                       'timestamp_label': '[00:02:33]',
                       'url': 'https://www.youtube.com/watch?v=ASHyX7v13Eo&t=153s',
                       'markdown': '[00:02:33](https://www.youtube.com/watch?v=ASHyX7v13Eo&t=153s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0BGnlP4Q71M',
                       'title': 'Mini Episode: Explaining What Accounts Qualify for the IDR Process with '
                                'Adam Cartabiano',
                       'channel': 'Ryan Downs',
                       'author': 'Ryan Downs',
                       'text': 'Most of the volume comes from an out of network charge on an in-network '
                               'event, such as your anesthesiologist, your ED docs, your hospitalists and '
                               'pathologists.',
                       'tip': 'Most of the volume comes from an out of network charge on an in-network '
                              'event, such as your anesthesiologist, your ED docs, your hospitalists and '
                              'pathologists.',
                       'timestamp': 92,
                       'timestamp_seconds': 92,
                       'timestamp_label': '[00:01:32]',
                       'url': 'https://www.youtube.com/watch?v=0BGnlP4Q71M&t=92s',
                       'markdown': '[00:01:32](https://www.youtube.com/watch?v=0BGnlP4Q71M&t=92s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7lqb5ev54mA',
                       'title': 'Mini Episode: Breaking Down The IDR Process with Adam Cartabiano',
                       'channel': 'Ryan Downs',
                       'author': 'Ryan Downs',
                       'text': 'If you skip that step up front, the arbitration organization will reject '
                               "the claim because you didn't take that first step as outlined by CMS.",
                       'tip': 'If you skip that step up front, the arbitration organization will reject '
                              "the claim because you didn't take that first step as outlined by CMS.",
                       'timestamp': 171,
                       'timestamp_seconds': 171,
                       'timestamp_label': '[00:02:51]',
                       'url': 'https://www.youtube.com/watch?v=7lqb5ev54mA&t=171s',
                       'markdown': '[00:02:51](https://www.youtube.com/watch?v=7lqb5ev54mA&t=171s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9TnGgGAGY8c',
                       'title': 'Intro to IDR: What To Know About Income-Driven Repayment (IDR) Plans for '
                                'Student Loans',
                       'channel': 'Federal Student Aid',
                       'author': 'Federal Student Aid',
                       'text': "Every year, you're required to recertify your income-driven repayment plan "
                               'by providing your updated income and family size information.',
                       'tip': "Every year, you're required to recertify your income-driven repayment plan "
                              'by providing your updated income and family size information.',
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=9TnGgGAGY8c&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=9TnGgGAGY8c&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'oP8xNI1bG3E',
                       'title': 'Income-Driven Repayment Explained: How to Lower Your Student Loan '
                                'Payments (2026)',
                       'channel': 'Unfiltered Money Labs',
                       'author': 'Unfiltered Money Labs',
                       'text': 'Missing your annual income recertification or paying scam companies are '
                               'massive financial pitfalls you just have to avoid.',
                       'tip': 'Missing your annual income recertification or paying scam companies are '
                              'massive financial pitfalls you just have to avoid.',
                       'timestamp': 321,
                       'timestamp_seconds': 321,
                       'timestamp_label': '[00:05:21]',
                       'url': 'https://www.youtube.com/watch?v=oP8xNI1bG3E&t=321s',
                       'markdown': '[00:05:21](https://www.youtube.com/watch?v=oP8xNI1bG3E&t=321s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GpHExH5dquQ',
                       'title': 'Out-of-Network Reimbursement: Why Paid Claims Can Still Hide Lost Revenue',
                       'channel': 'Vee Healthtek',
                       'author': 'Vee Healthtek',
                       'text': 'A paid out of network claim can still leave recoverable reimbursement '
                               'behind, because payment status confirms that money moved, not that the '
                               'amount was accurate.',
                       'tip': 'A paid out of network claim can still leave recoverable reimbursement '
                              'behind, because payment status confirms that money moved, not that the '
                              'amount was accurate.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=GpHExH5dquQ&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=GpHExH5dquQ&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ikQ6l3STH18',
                       'title': 'Contentious Clinic: Executor and Administrator Removal Disputes',
                       'channel': 'IDR Law',
                       'author': 'IDR Law',
                       'text': 'Engage reasonably with initial correspondence, look at the reasons why you '
                               'were appointed in the first place in your file notes, and remember the '
                               'personal risk as to cost.',
                       'tip': 'Engage reasonably with initial correspondence, look at the reasons why you '
                              'were appointed in the first place in your file notes, and remember the '
                              'personal risk as to cost.',
                       'timestamp': 3179,
                       'timestamp_seconds': 3179,
                       'timestamp_label': '[00:52:59]',
                       'url': 'https://www.youtube.com/watch?v=ikQ6l3STH18&t=3179s',
                       'markdown': '[00:52:59](https://www.youtube.com/watch?v=ikQ6l3STH18&t=3179s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'm8zdt3GQSjY',
                       'title': 'CoGenetix & ANS Solutions  OON IDR Webinar',
                       'channel': 'CoGenetix Wellness',
                       'author': 'CoGenetix Wellness',
                       'text': 'IDR determinations are legally binding; payers cannot initiate clawbacks '
                               'and they are required to pay awarded amounts within 30 days.',
                       'tip': 'IDR determinations are legally binding; payers cannot initiate clawbacks '
                              'and they are required to pay awarded amounts within 30 days.',
                       'timestamp': 265,
                       'timestamp_seconds': 265,
                       'timestamp_label': '[00:04:25]',
                       'url': 'https://www.youtube.com/watch?v=m8zdt3GQSjY&t=265s',
                       'markdown': '[00:04:25](https://www.youtube.com/watch?v=m8zdt3GQSjY&t=265s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
