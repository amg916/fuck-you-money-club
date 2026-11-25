from __future__ import annotations

CHAPTER_2 = {'id': 'Q2',
 'chapter_id': 'Q2',
 'chapter_number': 2,
 'question_number': 2,
 'slug': 'surprise-bills-patient-disputes-loopholes-ground-ambulance-gap',
 'question_prompt': 'Where do surprise bills still slip through, and how do patients identify, challenge, '
                    'and negotiate bills the No Surprises Act should have blocked?',
 'kicker': 'Q2 / THE BIG MONEY PLAYBOOKS',
 'title': 'Surprise Bills in the Wild: Patient Disputes, Loopholes, and the Ground Ambulance Gap',
 'subtitle': 'ER and in-network-facility surprise bills, denied ER claims, out-of-network lab referrals, '
             'ground ambulance exclusions, in-network/out-of-network bait-and-switch, private-equity '
             'staffing, and complaint and negotiation scripts for killing improper bills',
 'layout_template': 'executive_summary',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners converge on one map: since January 1, 2022, the No Surprises Act caps '
                      'patients at in-network cost sharing for emergency care, out-of-network doctors at '
                      'in-network facilities, and air ambulance, while ground ambulance, urgent care, and '
                      'non-hospital facilities sit outside it. Street mechanics start with refusing to '
                      'pay, pulling an itemized bill with CPT codes, and auditing for the errors auditors '
                      'find in up to 80% of bills. Escalation runs from an insurer reprocessing call to '
                      'the 1-800-985-3059 Help Desk complaint, with the uninsured using a $25 dispute when '
                      'a bill beats the good faith estimate by $400. The friction: FOX 26 says '
                      'out-of-network labs can still balance bill while Insured and Informed argues labs '
                      'are protected ancillary services, and AS DESIGNED shows a self-funded plan leaving '
                      'a family paying a $3,180 ground ambulance ride.',
 'key_metrics': [{'label': 'Ground Ambulance Balance Bill Left Standing',
                  'metric': 'Ground Ambulance Balance Bill Left Standing',
                  'value': '$3,180 billed; $1,340 allowed; $1,840 balance bill',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A 6-minute ground ambulance ride under a self-funded plan; the allowed '
                             'amount hit an unmet $12,000 out-of-network deductible, so the plan paid '
                             'nothing and the family paid every dollar lawfully.',
                  'source': 'AS DESIGNED | Risk & Insurance Stories ([w_lpas-cNkc @ 00:06:25])'},
                 {'label': 'Out-of-Network Share of Ground Ambulance Transports',
                  'metric': 'Out-of-Network Share of Ground Ambulance Transports',
                  'value': 'Over 50%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'National data cited on emergency ground ambulance transports involving an '
                             'out-of-network provider, making ground ambulances the largest source of '
                             'out-of-network emergency bills for insured Americans.',
                  'source': 'Law & Business ([88cpe80FbyY @ 00:01:41])'},
                 {'label': 'Uninsured Patient-Provider Dispute Trigger',
                  'metric': 'Uninsured Patient-Provider Dispute Trigger',
                  'value': '$400 over the good faith estimate; $25 fee; 120 days from the first bill',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Self-pay and uninsured patients can force an independent reviewer to decide '
                             'a fair price, but only if they kept the written estimate.',
                  'source': 'Law Unpacked ([0NouMpFWLHI @ 00:02:32])'},
                 {'label': 'Help Desk Complaint Wipeout',
                  'metric': 'Help Desk Complaint Wipeout',
                  'value': '$9,800 of $14,238 wiped within 6 weeks',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Appendectomy at an in-network hospital with an out-of-network surgeon, '
                             'anesthesiologist, and radiologist; a complaint through the No Surprises Help '
                             'Desk erased the illegal portion.',
                  'source': 'Bill Fighter ([OWN7CBskcIQ @ 00:09:41])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner working this beat draws the same three-zone map. Maya of '
                              'The Patient Blueprint lists the banned balance bills as out-of-network '
                              'emergency care, non-emergency services by an out-of-network doctor at an '
                              'in-network facility, and out-of-network air ambulance, with cost sharing '
                              'calculated as if the provider were in network [3OCpShEAIJs @ 00:00:20]. '
                              'Covered USA confirms the same trio and adds the scope line operators need '
                              'first: the protection runs to private coverage bought through an employer, '
                              'the marketplace, or directly from an insurer, while Medicare, Medicaid, and '
                              'Tricare carry their own protections [zDmKmfxl84c @ 00:00:32]. Bill Fighter, '
                              'a medical billing advocate with 15 years in the trade, puts the rule '
                              'bluntly: hit any emergency room, even an out-of-network one, and you can '
                              'only be charged your in-network rate [1VtIU2oIxEY @ 00:02:50]. Problem '
                              'Solved Lab extends the cap past the crash cart, noting that care received '
                              'after stabilization stays protected unless the patient signed a written '
                              'consent giving those protections up [ofqIwNzp8lA @ 00:00:19]. The operating '
                              'consequence is identical across all four: the in-network copay, '
                              'coinsurance, and deductible is the ceiling, and the payment fight over '
                              'everything above it moves to the provider and the plan, where the patient '
                              'is not part of the negotiation.',
                              'The same practitioners agree just as hard on where the net tears. Ground '
                              'ambulance is the headline gap: Problem Solved Lab warns that the ambulance '
                              'that drives to the hospital can still send an out-of-network bill unless '
                              'the state has its own protection, and that clinics and urgent care centers '
                              'generally sit outside the law too [ofqIwNzp8lA @ 00:01:49]. Satra Taylor of '
                              'Share My Lesson widens the exclusion list to facilities that are not '
                              'hospitals or ambulatory surgical centers, including urgent care clinics, '
                              'substance use treatment facilities, and birthing centers, plus elective '
                              'services where the patient picks the out-of-network doctor [Q11eG-8d-Hw @ '
                              '00:03:00]. FOX 26 Houston consumer reporter Heather Sullivan flags two '
                              'street-level traps: urgent care facilities escape unless licensed for '
                              'emergency care, and when a doctor ships test results to an out-of-network '
                              'lab, the lab can still balance bill [9dOW3txIHG0 @ 00:01:30]. Law & '
                              'Business quantifies why the ambulance hole matters, reporting that over 50% '
                              'of emergency ground ambulance transports involve an out-of-network provider '
                              'and calling ground ambulances the single largest source of out-of-network '
                              'emergency bills for insured Americans [88cpe80FbyY @ 00:01:41]. Knowing the '
                              'boundary is the whole game, as Problem Solved Lab puts it.',
                              'Baseline discipline is unanimous: do not pay first. Evolutio Labs opens its '
                              'five-step sequence with exactly that, arguing that paying can be '
                              'interpreted as accepting the charges, then moves straight to the itemized '
                              'bill [HwCCcS3hQls @ 00:01:35]. The second prerequisite is knowing the '
                              'waiver rules cold. Covered USA stresses that for ancillary services such as '
                              'anesthesiology, pathology, radiology, and neonatology the protection cannot '
                              'be waived at all, and that for other non-emergency services the notice must '
                              'be a separate document, carry a good faith estimate, offer an in-network '
                              'alternative, and arrive at least 72 hours ahead when the appointment is '
                              'scheduled that far out [zDmKmfxl84c @ 00:01:35]. Capital Autopsy hardens '
                              'the list of doctors who cannot even ask for the waiver: emergency medicine, '
                              'anesthesiology, radiology, pathology, assistant surgeons, hospitalists, and '
                              'intensivists, with the form never usable for emergency care itself '
                              '[PVUGwjJg-VI @ 00:10:36]. HealthWatch Wisconsin adds a limit operators '
                              'often miss: emergency protections do not stretch to all of the follow-up or '
                              'ancillary treatment a patient gets after the emergency has concluded, and '
                              'non-emergency protections can be waived under some conditions [MsP7ttGr9OA '
                              '@ 00:01:53]. The working rule is simple: freeze payment, identify the '
                              'protected zone, and check whether any waiver on file was even legal to '
                              'request.'],
               'table': {'caption': 'Where the practitioners agree: protected zones, gaps, and baseline '
                                    'moves',
                         'headers': ['Consensus Point',
                                     'What Practitioners Say',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Emergency care is capped at in-network cost sharing',
                                   'Out-of-network ER doctors and facilities can only charge the '
                                   'in-network copay, coinsurance, and deductible',
                                   'Treat any emergency balance above the EOB patient share as an illegal '
                                   'bill to dispute',
                                   'Bill Fighter ([1VtIU2oIxEY @ 00:02:50])'],
                                  ['Out-of-network doctors inside in-network facilities are covered',
                                   'Anesthesiologists, radiologists, pathologists, and lab work you never '
                                   'chose generally cannot balance bill you',
                                   'Audit every separate physician bill after an in-network surgery for '
                                   'illegal balance billing',
                                   'Law Unpacked ([0NouMpFWLHI @ 00:01:17])'],
                                  ['Air ambulance is protected but ground ambulance is not',
                                   'Helicopter and plane transports are covered while ground ambulance is '
                                   'not covered federally at all',
                                   'Route ground ambulance bills to state law checks and negotiation '
                                   'instead of federal arguments',
                                   'Covered USA ([zDmKmfxl84c @ 00:02:39])'],
                                  ['Waivers are narrow and banned for key specialties',
                                   'Waiver needs written notice 72 hours ahead and can never cover '
                                   'emergency, anesthesia, radiology, or pathology',
                                   'Refuse ancillary waivers outright and challenge any signature '
                                   'collected for those specialties',
                                   'Welcome to The Patient Blueprint. ([3OCpShEAIJs @ 00:01:46])'],
                                  ['Never pay before the dispute is filed',
                                   'Paying can be interpreted as accepting the charges, so the bill stays '
                                   'unpaid during review',
                                   'Freeze payments, payment plans, and credit card charges until the '
                                   'itemized bill arrives',
                                   'Evolutio Labs ([HwCCcS3hQls @ 00:01:35])'],
                                  ['Uninsured patients get a separate $400 dispute path',
                                   'Bills at least $400 over the good faith estimate can be disputed '
                                   'within 120 days for $25',
                                   'Keep the written estimate because without it the patient cannot open a '
                                   'dispute',
                                   'Law Unpacked ([0NouMpFWLHI @ 00:02:32])'],
                                  ['The federal help desk is the escalation backstop',
                                   'The No Surprises Help Desk at 1-800-985-3059 investigates and tells '
                                   'the provider to knock it off',
                                   'Use the hotline once the insurer or the collector refuses to reprocess '
                                   'the claim',
                                   'Share My Lesson ([Q11eG-8d-Hw @ 00:04:43])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The audit comes before any argument. Problem Solved Lab cites auditors '
                              'estimating that up to 80% of medical bills carry at least one error, with '
                              'one audit putting the average overcharge on hospital bills over $10,000 at '
                              'about $1,300 [ofqIwNzp8lA @ 00:00:50]. The same channel names the five '
                              'errors to hunt line by line: duplicate charges such as the same supply kit '
                              'billed twice, upcoding a simple visit into a complex procedure, services '
                              'never received like an anesthesia consultation when only local numbing '
                              'happened, wrong dates, and units that do not match documentation, such as '
                              '10 units of something given once [ofqIwNzp8lA @ 00:03:13]. Bill Fighter '
                              "supplies the exact request language for the billing office: 'Please send me "
                              "an itemized statement with all CPT codes,' the five-digit codes that "
                              'identify each service, because a lump sum hides everything [1VtIU2oIxEY @ '
                              "00:05:54]. Bill Fighter's negotiation playbook stacks four documents before "
                              "any call: the itemized bill, the insurer's explanation of benefits, the "
                              "visit's medical records, and the policy's out-of-network section, because "
                              "where the EOB and the bill disagree 'is where the money lives' [OWN7CBskcIQ "
                              '@ 00:04:06]. Each disputed line gets a written, plain-words reason.',
                              'Once errors are logged, the escalation ladder runs on scripts. Satra Taylor '
                              "of Share My Lesson hands over the insurer line verbatim, 'Hi, I believe "
                              'this bill is prohibited under the No Surprises Act. Can you confirm whether '
                              "this was processed as an in network?', then tells collectors, 'This bill "
                              'appears to violate the No Surprises Act. Please stop collection and '
                              "reprocess through my insurance company as an in-network claim' [Q11eG-8d-Hw "
                              '@ 00:04:22]. Bill Fighter says that single reprocessing call often solves '
                              'the problem, and when it does not, the federal complaint at 1-800-985-3059 '
                              'is free, with providers facing fines up to $10,000 per violation, so '
                              'hospitals that hear from CMS tend to fix things quickly [1VtIU2oIxEY @ '
                              '00:06:28]. Evolutio Labs layers in the appeal content: name the No '
                              'Surprises Act, assert the prudent layperson standard, demand in-network '
                              'cost sharing, then push to external review, with 120 days from the denial '
                              'to file in most cases [HwCCcS3hQls @ 00:02:12]. The Patient Blueprint shows '
                              'the math to quote on the call: a $3,500 anesthesia charge against a $1,800 '
                              'in-network allowed amount leaves 20% coinsurance of $360, and the attempted '
                              '$1,340 balance bill is prohibited, so the patient pays only $360 '
                              '[3OCpShEAIJs @ 00:01:02].',
                              'When the bill falls outside the protected zone, practitioners switch to '
                              'price leverage. Problem Solved Lab benchmarks with Fair Health Consumer, '
                              'entering the procedure code and zip code to see typical charges and insurer '
                              'payments, then cross-checks the Medicare fee schedule, and asks three '
                              'questions in order: a self-pay or prompt-pay discount, financial assistance '
                              'or charity care, and whether billing will match the benchmark or meet '
                              'between it and the billed charge [ofqIwNzp8lA @ 00:04:21]. Bill Fighter '
                              'adds Healthcare Bluebook, notes that hospital cash prices can run 50, 60, '
                              'even 80% lower, and coaches callers to ask for the financial assistance '
                              "office or billing supervisor and say 'I'd like to discuss a settlement on "
                              "my account,' opening at about 25% of the original bill because hospitals "
                              "routinely accept 30 to 50% [OWN7CBskcIQ @ 00:07:31]. The advocate's Sarah "
                              'case shows the federal path working first: $9,800 of a $14,238 '
                              'out-of-pocket demand was wiped within six weeks after a Help Desk '
                              'complaint, because it was never legal in the first place [OWN7CBskcIQ @ '
                              '00:09:41]. For ground ambulance, Law & Business pushes an itemized bill, an '
                              'insurer out-of-network exception arguing no choice of provider, and a check '
                              'for municipal ordinances barring balance billing of local taxpayers '
                              '[88cpe80FbyY @ 00:10:01].'],
               'table': {'caption': 'Street mechanics: scripts, thresholds, and numbers practitioners '
                                    'actually use',
                         'headers': ['Mechanic',
                                     'Exact Number or Script',
                                     'How It Is Used',
                                     'Expert Source'],
                         'rows': [['Itemized bill request',
                                   "'Please send me an itemized statement with all CPT codes'",
                                   'Exposes duplicates, upcoding, phantom services, wrong dates, and unit '
                                   'mismatches line by line',
                                   'Bill Fighter ([1VtIU2oIxEY @ 00:05:54])'],
                                  ['Error audit odds',
                                   'Up to 80% of bills carry errors; about $1,300 average overcharge on '
                                   'bills over $10,000',
                                   'Justifies a full line audit before any payment, payment plan, or '
                                   'credit card charge',
                                   'Problem Solved Lab ([ofqIwNzp8lA @ 00:00:50])'],
                                  ['Settlement opening offer',
                                   'Open near 25% of the bill; hospitals routinely accept 30 to 50%',
                                   "Say 'settlement,' not 'discount,' to the billing supervisor and expect "
                                   'a counteroffer',
                                   'Bill Fighter ([OWN7CBskcIQ @ 00:07:31])'],
                                  ['Written release language',
                                   "'Payment in full satisfies the account' or 'this settles the debt in "
                                   "full'",
                                   'Get it by email before paying so the remainder cannot be rebilled '
                                   'months later',
                                   'Bill Fighter ([OWN7CBskcIQ @ 00:07:51])'],
                                  ['Federal complaint pressure',
                                   'Free complaint at 1-800-985-3059; providers fined up to $10,000 per '
                                   'violation',
                                   'Escalate after the insurer reprocessing call fails to remove the '
                                   'illegal balance',
                                   'Bill Fighter ([1VtIU2oIxEY @ 00:06:47])'],
                                  ['Uninsured dispute economics',
                                   '$25 fee when a single provider bills $400 over the estimate, filed '
                                   'within 120 days',
                                   'Independent reviewer decides what is owed and collections should pause '
                                   'while pending',
                                   'Problem Solved Lab ([ofqIwNzp8lA @ 00:05:50])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Front-Desk and Back-Office Moves That Kill Surprise Bills Early',
                           'body': 'The cheapest surprise bill to fight is the one that never gets '
                                   'created. These four moves happen before or during care, or before the '
                                   'first collections letter lands.',
                           'items': ["Decline a waiver at check-in with one line: 'No, thank you. I'd like "
                                     "to be billed at my in-network rate.' Providers often treat anyway "
                                     'because they still get paid the in-network rate [Bill Fighter — '
                                     '1VtIU2oIxEY @ 00:05:01].',
                                     'Before blood work, ask checkout staff which lab gets the samples and '
                                     'whether it is in network; if they cannot confirm, ask for the lab '
                                     'prescription and go to an in-network lab yourself [Insured and '
                                     'Informed — wySlaLru-l4 @ 00:03:36].',
                                     "Never ask whether a provider 'accepts' or 'takes' your insurance; "
                                     'ask whether you are in network, the question that actually controls '
                                     'the bill [FOX 26 Houston — 9dOW3txIHG0 @ 00:02:07].',
                                     'Ask HR in writing whether the plan is fully insured or self-funded; '
                                     'the answer lives in the plan document, not the brochure, and decides '
                                     'whether state surprise billing laws reach you [AS DESIGNED | Risk & '
                                     'Insurance Stories — w_lpas-cNkc @ 00:15:10].']},
               'sop_steps': [{'step': 1,
                              'title': 'Freeze Payment and Pull the Paper',
                              'action': 'Stop all payments, payment plans, and card charges; request the '
                                        'itemized bill and the EOB.',
                              'detail': 'A payment plan can be read as acceptance of the full amount, so '
                                        'the itemized bill, EOB, and dated record come first, and every '
                                        'line that cannot be matched to actual care goes back to billing '
                                        'for a written explanation [Problem Solved Lab — ofqIwNzp8lA @ '
                                        '00:03:46].'},
                             {'step': 2,
                              'title': 'Classify the Bill Against the Boundary',
                              'action': 'Sort the bill into emergency, in-network facility, air ambulance, '
                                        'or outside-the-law (ground ambulance, clinic, urgent care).',
                              'detail': 'Ground ambulances, clinics, and urgent care centers generally sit '
                                        'outside the federal law; a bill inside the boundary is challenged '
                                        'under the law, while a bill outside it needs a different strategy '
                                        '[Problem Solved Lab — ofqIwNzp8lA @ 00:02:05].'},
                             {'step': 3,
                              'title': 'Reprocess, Then Complain Federally',
                              'action': 'Call the insurer to reprocess at the in-network rate; if that '
                                        'fails, file with the No Surprises Help Desk.',
                              'detail': 'The complaint at 1-800-985-3059 is free, providers can be fined '
                                        'up to $10,000 per violation, and once a hospital hears from CMS '
                                        'it tends to fix things quickly [Bill Fighter — 1VtIU2oIxEY @ '
                                        '00:06:47].'},
                             {'step': 4,
                              'title': 'Settle Outside-the-Law Balances in Writing',
                              'action': 'Negotiate a settlement against benchmarks and lock it in by email '
                                        'before paying a penny.',
                              'detail': "Demand language stating 'payment in full satisfies the account' "
                                        "or 'this settles the debt in full', because without that paper "
                                        'trail the provider can come back 6 months later and bill the '
                                        'remainder [Bill Fighter — OWN7CBskcIQ @ 00:07:51].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is whether a surprise bill gets fought or bargained. '
                              'Bill Fighter draws a hard line: if the emergency, in-network-facility, or '
                              'air ambulance categories apply, the first step is not to negotiate, it is '
                              'to dispute, because that bill may flat out be illegal under federal law, so '
                              'write down the date and the situation and prepare to challenge it '
                              '[OWN7CBskcIQ @ 00:03:31]. Only when the law misses does Bill Fighter switch '
                              'to a settlement call, opening at about 25% of the original bill and quoting '
                              'hospitals that routinely accept 30 to 50% when paid quickly [OWN7CBskcIQ @ '
                              '00:07:11]. Problem Solved Lab runs a softer bargaining sequence in a fixed '
                              'order: ask for a self-pay or prompt-pay discount, then ask about financial '
                              'assistance or charity care and the application, then ask whether billing '
                              'will match the Fair Health area benchmark or meet you between the benchmark '
                              'and the billed charge, with any agreement in writing first [ofqIwNzp8lA @ '
                              '00:04:37]. Insured and Informed pushes the fight even earlier, telling a '
                              'New York patient facing a $2,000 out-of-network lab bill to appeal instead '
                              'of immediately assuming the full amount is owed, and before asking the '
                              "doctor's office for a reduced payment, a payment plan, or financial "
                              'assistance [wySlaLru-l4 @ 00:02:50]. The operator sequence that falls out: '
                              'dispute wherever a protected category arguably fits, and hold the '
                              'benchmark-and-settlement script as the fallback.',
                              'Escalation ladders differ in both rung order and who gets called. Evolutio '
                              'Labs runs the insurer appeal first, with a letter that names the No '
                              'Surprises Act, asserts the visit meets the prudent layperson standard, and '
                              'states that federal law requires in-network cost-sharing, then a free CMS '
                              'complaint, then an external review where an independent reviewer checks '
                              'whether federal law was followed [HwCCcS3hQls @ 00:01:55]. Share My Lesson '
                              'adds the collector as its own rung: after calling the insurer, call the '
                              "collection agency and say the bill 'appears to violate the No Surprises "
                              'Act. Please stop collection and reprocess through my insurance company as '
                              "an in network claim,' then file with the CMS help desk hotline [Q11eG-8d-Hw "
                              '@ 00:04:22]. On collections themselves the split is direct. Bill Fighter '
                              'argues that once a bill has gone to collections you actually have more '
                              'leverage, not less, because agencies buy these debts for pennies on the '
                              'dollar and paid medical collections under $500 no longer appear on credit '
                              'reports at Equifax, Experian, and TransUnion, so negotiate hard '
                              '[OWN7CBskcIQ @ 00:08:07]. Problem Solved Lab treats collections as a '
                              'failure state: never let a bill go to collections while you are disputing '
                              'it in writing, send every dispute by a method you can prove, keep copies of '
                              'everything, and log the date, the name of the person, and the reference '
                              'number on every call [ofqIwNzp8lA @ 00:07:22].',
                              'The ground ambulance numbers do not reconcile, and the spread matters for '
                              'anyone triaging a transport bill. Law & Business counts approximately 14 '
                              'states with statutes directly restricting ground ambulance balance billing, '
                              'and pegs self-funded enrollment at about 60% of commercially insured '
                              'workers, who sit outside every state ambulance protection and stay exposed '
                              'to balance billing even in states with active consumer laws [88cpe80FbyY @ '
                              '00:08:04]. AS DESIGNED reports more than 20 states had some protection by '
                              '2026, frames self-funding as covering most American workers, and stresses '
                              'that the fully insured versus self-funded answer lives in the plan '
                              'document, not the brochure [w_lpas-cNkc @ 00:15:10]. The two camps then '
                              'diverge on whether an unprotected ride is fightable at all. Law & Business '
                              'still prescribes a playbook: pull the itemized bill for coding errors and '
                              'duplicated charges, ask the insurer for an administrative review or a '
                              'formal out-of-network exception arguing there was no choice of provider, '
                              'and check for municipal ordinances that bar city-operated ambulances from '
                              "balance billing local taxpayers [88cpe80FbyY @ 00:10:18]. AS DESIGNED's "
                              'Whitaker case is the counterweight: the plan allowed $1,340 of a $3,180 '
                              'ride, applied it to a $12,000 out-of-network deductible standing at zero, '
                              'and there was no error to dispute and no appeal that would change it, so '
                              'the full $3,180 went onto a payment plan at $92 a month [w_lpas-cNkc @ '
                              '00:07:05].'],
               'table': {'caption': 'Practitioner Disagreements on Surprise Bill Tactics, Rules, and '
                                    'Numbers',
                         'headers': ['Contested Issue', 'Position A', 'Position B', 'Expert Source'],
                         'rows': [['Notice window on the out-of-network waiver form',
                                   'Notice must arrive at least 72 hours before scheduled care, on a '
                                   'separate document with a good faith estimate',
                                   'Providers must give a good faith estimate and a special 45day notice '
                                   'form, and a signature grabbed in the chaos might not count',
                                   'Covered USA ([zDmKmfxl84c @ 00:02:22]); Share My Lesson ([Q11eG-8d-Hw '
                                   '@ 00:03:19])'],
                                  ['How often medical bills carry billing errors',
                                   'Billing errors are found in up to 80% of medical bills, and errors '
                                   'alone can reduce or eliminate the balance',
                                   'Patients who simply check for billing errors find them about half the '
                                   'time, per a NerdWallet figure quoted on the call',
                                   'Evolutio Labs ([HwCCcS3hQls @ 00:01:35]); Bill Fighter ([OWN7CBskcIQ @ '
                                   '00:05:37])'],
                                  ['Credit damage from medical collections on a disputed bill',
                                   'Paid medical collections under $500 no longer appear on credit '
                                   'reports, so collections becomes negotiating leverage',
                                   'Paid medical debt was removed, but unpaid balances over $500 can still '
                                   'remain on reports for years',
                                   'Bill Fighter ([OWN7CBskcIQ @ 00:08:07]); Law & Business ([88cpe80FbyY '
                                   '@ 00:09:26])'],
                                  ['Out-of-network ER physician working inside an in-network hospital',
                                   'A wraps policy covers radiology, anesthesia, and pathology, but '
                                   'whether the ER physician bill processes in-network depends',
                                   'Emergency care cannot be billed at out-of-network rates even if the ER '
                                   'doctor was out of network, period',
                                   'AHealthcareZ - Healthcare Finance Explained ([8NDnQoTkjb4 @ '
                                   '00:01:19]); Bill Fighter ([OWN7CBskcIQ @ 00:02:55])'],
                                  ['Care delivered after the emergency patient is stabilized',
                                   'Protection covers care received after you are stable unless you signed '
                                   'written consent giving those protections up',
                                   'Emergency protections do not apply to all follow-up or ancillary '
                                   'treatment after the emergency has concluded',
                                   'Problem Solved Lab ([ofqIwNzp8lA @ 00:00:34]); HealthWatch Wisconsin '
                                   '([MsP7ttGr9OA @ 00:01:53])'],
                                  ['Labs sent by an in-network doctor to an out-of-network lab',
                                   'Lab work is an ancillary service tied to in-network care, the consent '
                                   'exception cannot apply, so file the appeal',
                                   'If your doctor sends test results to an out-of-network lab, the lab '
                                   'can still balance bill you',
                                   'Insured and Informed ([wySlaLru-l4 @ 00:02:17]); FOX 26 Houston '
                                   '([9dOW3txIHG0 @ 00:01:48])'],
                                  ['Final rung after the insurer refuses to fix it',
                                   'File the CMS complaint, then request an external review by an '
                                   'independent reviewer before the deadline',
                                   'Insurer appeal, then a federal complaint for a covered surprise bill, '
                                   'then the $400 dispute path if uninsured or self-pay',
                                   'Evolutio Labs ([HwCCcS3hQls @ 00:02:12]); Problem Solved Lab '
                                   '([ofqIwNzp8lA @ 00:07:05])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ["The most expensive firsthand case in the set is AS DESIGNED's Whitaker "
                              'household, and it loses money at three separate boundaries without a single '
                              'denied claim. First, the provider type: a 6-minute county-dispatched ground '
                              'ambulance ride billed $3,180, the plan allowed $1,340, the $1,840 remainder '
                              'was a lawful balance bill, and the allowed amount landed on an untouched '
                              '$12,000 out-of-network deductible, so the family paid every dollar '
                              '[w_lpas-cNkc @ 00:05:44]. Second, the plan type: HR confirmed in writing '
                              'that the plan was self-funded, ERISA overrode the state ground ambulance '
                              'law, and a neighbor on a fully insured plan paid $268 for the same kind of '
                              'ride from the same company in the same month [w_lpas-cNkc @ 00:08:05]. Law '
                              '& Business describes the identical trap at national scale, with two '
                              'neighbors in the same town facing completely different financial outcomes '
                              'for the same ambulance service based entirely on how the employer funds '
                              'benefits [88cpe80FbyY @ 00:08:22]. Third, the calendar: surgery on December '
                              '27 and a post-surgical infection treated on January 2 straddled the plan '
                              'year, re-charging the already-met $6,000 deductible plus $1,480 '
                              'coinsurance. The all-in damage was $23,960, or 30.7% of a $78,000 household '
                              'year, including $1,540 of employer match lost permanently after a '
                              'retirement contribution cut [w_lpas-cNkc @ 00:13:22].',
                              'The second cluster of failures is self-inflicted paperwork. Evolutio Labs '
                              'warns that paying can be interpreted as accepting the charges, that the '
                              'appeal window is 120 days from the date of the denial in most cases, and '
                              'that the process only works if it starts before that deadline because the '
                              'clock is already running [HwCCcS3hQls @ 00:02:12]. Problem Solved Lab '
                              'extends the acceptance trap to installments: dispute before you pay, before '
                              'you set up a payment plan, and before you put the bill on a credit card, '
                              'because a payment plan can be read as acceptance of the full amount '
                              '[ofqIwNzp8lA @ 00:03:46]. For uninsured and self-pay patients, Law Unpacked '
                              'flags the single document whose absence kills the $400 dispute path: keep '
                              'the written good faith estimate, because without it you cannot dispute, and '
                              'the window is 120 days from the first bill at a $25 fee [0NouMpFWLHI @ '
                              '00:02:51]. Even a won negotiation can unravel. Bill Fighter insists on '
                              'written settlement language such as payment in full satisfies the account '
                              'before paying one penny, usually by email, because without that paper trail '
                              'they could come back 6 months later and bill you for the remainder '
                              '[OWN7CBskcIQ @ 00:07:51]. The common failure across all four is acting on '
                              'the bill before building the record, and the record is what wins the '
                              'dispute.',
                              'The third failure layer is structural: loopholes and counterparties that '
                              "outlast the patient. FOX 26 Houston's Cristina Lawson called on the way to "
                              'the hospital to confirm it accepted her insurance, then received a $26,000 '
                              "bill from an out-of-network physician's assistant after an emergency "
                              'appendectomy, because the Texas law originally excluded out-of-state '
                              'insurers like her Anthem Blue Cross in California, and it took months of '
                              'phone calls to get the bill reduced [9dOW3txIHG0 @ 00:00:56]. AHealthcareZ '
                              'shows the mismatch running the other direction, with an in-network '
                              'proceduralist billing around $250 while the out-of-network facility bill '
                              'runs upwards of $20,000, a pattern Dr. Eric Bricker says his team has '
                              'literally seen happen [8NDnQoTkjb4 @ 00:01:50]. Capital Autopsy documents '
                              'the counterparty muscle on the provider side: a TeamHealth subsidiary filed '
                              'more than 4,800 lawsuits against patients in Shelby County courts starting '
                              'in 2017, in some cases seeking to garnish wages of low-income workers, '
                              'before dropping pending cases after press scrutiny [PVUGwjJg-VI @ '
                              '00:06:14]. Once the fight moved to IDR, regulators projected about 17,000 '
                              'disputes a year while providers filed about 650,000 in 2023, won more than '
                              '80% of decided cases, and the biggest filers took median awards of roughly '
                              'three to nine times the median in-network rate [PVUGwjJg-VI @ 00:08:06].'],
               'table': {'caption': 'Firsthand Failure Modes and the Dollar Damage Practitioners Measured',
                         'headers': ['Failure Mode',
                                     'What Happened Firsthand',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Self-funded plan meets an emergency ground ambulance',
                                   'A county-dispatched 6-minute ride billed $3,180 and the state '
                                   'ambulance law never reached the self-funded plan',
                                   'A neighbor on a fully insured plan paid $268 for the same kind of ride '
                                   'from the same company',
                                   'AS DESIGNED | Risk & Insurance Stories ([w_lpas-cNkc @ 00:07:45])'],
                                  ['Plan-year reset in the middle of one illness',
                                   'Surgery on December 27 and infection treatment on January 2 landed in '
                                   'two different plan years',
                                   'The already-met $6,000 deductible was charged again plus $1,480 '
                                   'coinsurance for a $7,480 share',
                                   'AS DESIGNED | Risk & Insurance Stories ([w_lpas-cNkc @ 00:11:32])'],
                                  ['Labs quietly shipped to an out-of-network lab',
                                   'A first-visit free annual checkup produced EOBs showing over $2,000 '
                                   'owed, and the doctor never mentioned the lab',
                                   'Appeal under ancillary lab protections before asking for reduced '
                                   'payment, a payment plan, or assistance',
                                   'Insured and Informed ([wySlaLru-l4 @ 00:00:44])'],
                                  ['Urgent care and clinic blind spot in coverage',
                                   'Urgent care facilities fall outside the law unless licensed for '
                                   'emergency care, and clinics are generally outside too',
                                   'A bill outside the boundary needs a different strategy than a No '
                                   'Surprises Act challenge',
                                   'FOX 26 Houston ([9dOW3txIHG0 @ 00:01:30]); Problem Solved Lab '
                                   '([ofqIwNzp8lA @ 00:02:05])'],
                                  ['Waiver signature collected in the chaos of admission',
                                   'Providers must deliver a good faith estimate and notice form, but '
                                   'hospitals often do not follow the rules',
                                   'Do not assume your signature makes the out-of-network charge legit, '
                                   'and challenge it anyway',
                                   'Share My Lesson ([Q11eG-8d-Hw @ 00:03:19])'],
                                  ['Paying a summary bill without the itemized line review',
                                   'Auditors estimate up to 80% of medical bills contain at least one '
                                   'error, including duplicates and upcoding',
                                   'One audit put the average overcharge on hospital bills over $10,000 at '
                                   'about $1,300',
                                   'Problem Solved Lab ([ofqIwNzp8lA @ 00:00:50])'],
                                  ['Emergency surgery bills left unchallenged at face value',
                                   'An appendicitis patient at an in-network hospital faced out-of-network '
                                   'surgeon, anesthesiologist, and radiologist bills totaling $14,238',
                                   'A No Surprises Help Desk complaint wiped out $9,800 of that bill '
                                   'within 6 weeks',
                                   'Bill Fighter ([OWN7CBskcIQ @ 00:09:41])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Checks Before Paying Any Surprise Bill',
                           'body': 'Every loss in this chapter traces to a payment, a signature, a missed '
                                   'deadline, or an unasked plan question that happened before the record '
                                   'was built. Run these four checks before a dollar moves.',
                           'items': ['Get HR to state in writing whether the plan is fully insured or '
                                     'self-funded, because state ground ambulance protections stopped at '
                                     "the door of the Whitaker family's self-funded plan [AS DESIGNED | "
                                     'Risk & Insurance Stories — w_lpas-cNkc @ 00:15:10].',
                                     'Freeze every payment, payment plan, and credit card charge until the '
                                     'itemized bill is reviewed and each disputed line is written down '
                                     'with its reason [Problem Solved Lab — ofqIwNzp8lA @ 00:03:31].',
                                     'Calendar the 120-day appeal clock from the date of the denial the '
                                     'day the denial arrives, because the process only works if it starts '
                                     'before the deadline [Evolutio Labs — HwCCcS3hQls @ 00:02:12].',
                                     'Refuse any waiver for an anesthesiologist or other ancillary '
                                     'service, and for other planned out-of-network care demand the '
                                     'separate notice, the estimate, and the 72-hour window or refuse '
                                     '[Covered USA — zDmKmfxl84c @ 00:03:44].']}}],
 'pull_quote': 'Air ambulance is covered. The helicopter is protected, the road is not. Attributed to AS '
               'DESIGNED | Risk & Insurance Stories (w_lpas-cNkc @ 00:06:05).',
 'diagram_id': 'diag-04',
 'action_checklist': ['Do not pay the bill yet, then call billing and say: please send me an itemized '
                      'statement with all CPT codes [Bill Fighter — 1VtIU2oIxEY @ 00:05:38].',
                      'Call the insurer, state that you received a surprise bill covered under the No '
                      'Surprises Act, and ask them to reprocess the claim at the in-network rate [Bill '
                      'Fighter — 1VtIU2oIxEY @ 00:06:11].',
                      "Compare the bill to the insurer's explanation of benefits and confirm your share "
                      'matches your in-network costs [Law Unpacked — 0NouMpFWLHI @ 00:03:10].',
                      'If the bill is with a collector, call and say it appears to violate the No '
                      'Surprises Act and ask them to stop collection and reprocess as an in-network claim '
                      '[Share My Lesson — Q11eG-8d-Hw @ 00:04:22].',
                      'If the provider keeps billing in a protected situation, file a complaint with the '
                      'CMS No Surprises Help Desk at 1-800-985-3059 [Welcome to The Patient Blueprint. — '
                      '3OCpShEAIJs @ 00:01:25].',
                      'Before blood work, ask which lab your samples go to and confirm it is in network, '
                      'or request the lab prescription and use an in-network lab yourself [Insured and '
                      'Informed — wySlaLru-l4 @ 00:03:36].'],
 'statutory_citations': [{'title': 'AS DESIGNED | Risk & Insurance Stories — The Law Stops Surprise '
                                   'Medical Bills. Why Not the Ambulance? [00:05:44]',
                          'url': 'https://www.youtube.com/watch?v=w_lpas-cNkc&t=344s',
                          'relevance': 'Primary practitioner testimony on the $3,180 ground ambulance '
                                       'balance bill, self-funded ERISA preemption, and plan-year '
                                       'deductible reset.'},
                         {'title': 'Law & Business — Are Ambulances Covered Under Surprise Billing Laws? '
                                   '[00:08:04]',
                          'url': 'https://www.youtube.com/watch?v=88cpe80FbyY&t=484s',
                          'relevance': 'Primary practitioner testimony on state ground ambulance laws, the '
                                       '60% self-funded exemption, and unprotected-bill dispute tactics.'},
                         {'title': 'Capital Autopsy — In-Network Hospital, Out-of-Network Doctor: The '
                                   'Private Equity Trap [00:08:06]',
                          'url': 'https://www.youtube.com/watch?v=PVUGwjJg-VI&t=486s',
                          'relevance': 'Primary practitioner testimony on private equity ER staffing, '
                                       'patient lawsuits, and IDR filing volumes and provider win rates.'},
                         {'title': 'Bill Fighter — Out-of-Network Bill Shock? Negotiate It Down 60% With '
                                   'This Script [00:09:41]',
                          'url': 'https://www.youtube.com/watch?v=OWN7CBskcIQ&t=581s',
                          'relevance': 'Primary practitioner testimony on dispute-first tactics, the '
                                       'settlement script, and the $9,800 help desk recovery.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'HwCCcS3hQls',
                       'title': 'ER Bill Denied? Do NOT Pay Until You Watch This (The No Surprises Act)',
                       'channel': 'Evolutio Labs',
                       'author': 'Evolutio Labs',
                       'text': 'Under federal law, the standard is the prudent layperson standard, meaning '
                               'if a reasonable person in your situation would have gone to the ER, it '
                               'qualifies.',
                       'tip': 'Under federal law, the standard is the prudent layperson standard, meaning '
                              'if a reasonable person in your situation would have gone to the ER, it '
                              'qualifies.',
                       'timestamp': 63,
                       'timestamp_seconds': 63,
                       'timestamp_label': '[00:01:03]',
                       'url': 'https://www.youtube.com/watch?v=HwCCcS3hQls&t=63s',
                       'markdown': '[00:01:03](https://www.youtube.com/watch?v=HwCCcS3hQls&t=63s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '0NouMpFWLHI',
                       'title': 'Do You Have to Pay a Surprise Medical Bill? (The No Surprises Act '
                                'Explained)',
                       'channel': 'Law Unpacked',
                       'author': 'Law Unpacked',
                       'text': 'Air ambulances, meaning helicopters and planes, are covered by the law. '
                               'But ground ambulances generally are not.',
                       'tip': 'Air ambulances, meaning helicopters and planes, are covered by the law. But '
                              'ground ambulances generally are not.',
                       'timestamp': 132,
                       'timestamp_seconds': 132,
                       'timestamp_label': '[00:02:12]',
                       'url': 'https://www.youtube.com/watch?v=0NouMpFWLHI&t=132s',
                       'markdown': '[00:02:12](https://www.youtube.com/watch?v=0NouMpFWLHI&t=132s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zDmKmfxl84c',
                       'title': 'The Surprise Bill Ban: What the No Surprises Act Actually Covers — and '
                                'the One Ambulance It Does Not',
                       'channel': 'Covered USA',
                       'author': 'Covered USA',
                       'text': 'Ground ambulance services are not covered by the No Surprises Act at all.',
                       'tip': 'Ground ambulance services are not covered by the No Surprises Act at all.',
                       'timestamp': 159,
                       'timestamp_seconds': 159,
                       'timestamp_label': '[00:02:39]',
                       'url': 'https://www.youtube.com/watch?v=zDmKmfxl84c&t=159s',
                       'markdown': '[00:02:39](https://www.youtube.com/watch?v=zDmKmfxl84c&t=159s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ofqIwNzp8lA',
                       'title': 'The No Surprises Act Cut Your ER Bill Already — Did You Pay $1,300 Too '
                                'Much? (2026)',
                       'channel': 'Problem Solved Lab',
                       'author': 'Problem Solved Lab',
                       'text': 'A payment plan can be read as acceptance of the full amount.',
                       'tip': 'A payment plan can be read as acceptance of the full amount.',
                       'timestamp': 226,
                       'timestamp_seconds': 226,
                       'timestamp_label': '[00:03:46]',
                       'url': 'https://www.youtube.com/watch?v=ofqIwNzp8lA&t=226s',
                       'markdown': '[00:03:46](https://www.youtube.com/watch?v=ofqIwNzp8lA&t=226s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9dOW3txIHG0',
                       'title': 'Loopholes in No Surprises Act can leave some patients with high bills',
                       'channel': 'FOX 26 Houston',
                       'author': 'FOX 26 Houston',
                       'text': 'Consumers will often ask if a provider accepts or takes their insurance, '
                               'and that is not the question; you want to ask whether you are in network.',
                       'tip': 'Consumers will often ask if a provider accepts or takes their insurance, '
                              'and that is not the question; you want to ask whether you are in network.',
                       'timestamp': 127,
                       'timestamp_seconds': 127,
                       'timestamp_label': '[00:02:07]',
                       'url': 'https://www.youtube.com/watch?v=9dOW3txIHG0&t=127s',
                       'markdown': '[00:02:07](https://www.youtube.com/watch?v=9dOW3txIHG0&t=127s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Q11eG-8d-Hw',
                       'title': 'The No Surprises Act Explained: How to Fight Surprise Medical Bills',
                       'channel': 'Share My Lesson',
                       'author': 'Share My Lesson',
                       'text': 'Step two, call the collection agency and say this bill appears to violate '
                               'the No Surprises Act, please stop collection and reprocess through my '
                               'insurance company as an in network claim.',
                       'tip': 'Step two, call the collection agency and say this bill appears to violate '
                              'the No Surprises Act, please stop collection and reprocess through my '
                              'insurance company as an in network claim.',
                       'timestamp': 262,
                       'timestamp_seconds': 262,
                       'timestamp_label': '[00:04:22]',
                       'url': 'https://www.youtube.com/watch?v=Q11eG-8d-Hw&t=262s',
                       'markdown': '[00:04:22](https://www.youtube.com/watch?v=Q11eG-8d-Hw&t=262s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'w_lpas-cNkc',
                       'title': 'The Law Stops Surprise Medical Bills. Why Not the Ambulance?',
                       'channel': 'AS DESIGNED | Risk & Insurance Stories',
                       'author': 'AS DESIGNED | Risk & Insurance Stories',
                       'text': 'Air ambulance is covered. The helicopter is protected, the road is not.',
                       'tip': 'Air ambulance is covered. The helicopter is protected, the road is not.',
                       'timestamp': 365,
                       'timestamp_seconds': 365,
                       'timestamp_label': '[00:06:05]',
                       'url': 'https://www.youtube.com/watch?v=w_lpas-cNkc&t=365s',
                       'markdown': '[00:06:05](https://www.youtube.com/watch?v=w_lpas-cNkc&t=365s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'w_lpas-cNkc',
                       'title': 'The Law Stops Surprise Medical Bills. Why Not the Ambulance?',
                       'channel': 'AS DESIGNED | Risk & Insurance Stories',
                       'author': 'AS DESIGNED | Risk & Insurance Stories',
                       'text': 'The state insurance department never had jurisdiction. The state had a '
                               'ground ambulance law of its own. It reached fully insured plans.',
                       'tip': 'The state insurance department never had jurisdiction. The state had a '
                              'ground ambulance law of its own. It reached fully insured plans.',
                       'timestamp': 507,
                       'timestamp_seconds': 507,
                       'timestamp_label': '[00:08:27]',
                       'url': 'https://www.youtube.com/watch?v=w_lpas-cNkc&t=507s',
                       'markdown': '[00:08:27](https://www.youtube.com/watch?v=w_lpas-cNkc&t=507s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '88cpe80FbyY',
                       'title': 'Are Ambulances Covered Under Surprise Billing Laws?',
                       'channel': 'Law & Business',
                       'author': 'Law & Business',
                       'text': 'Approximately 60% of commercially insured workers are enrolled in these '
                               'self-funded employer plans, completely exempting them from any state-level '
                               'ambulance protections.',
                       'tip': 'Approximately 60% of commercially insured workers are enrolled in these '
                              'self-funded employer plans, completely exempting them from any state-level '
                              'ambulance protections.',
                       'timestamp': 484,
                       'timestamp_seconds': 484,
                       'timestamp_label': '[00:08:04]',
                       'url': 'https://www.youtube.com/watch?v=88cpe80FbyY&t=484s',
                       'markdown': '[00:08:04](https://www.youtube.com/watch?v=88cpe80FbyY&t=484s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1VtIU2oIxEY',
                       'title': 'No Surprises Act Exposed - How to Kill an $8,472 Surprise Bill',
                       'channel': 'Bill Fighter',
                       'author': 'Bill Fighter',
                       'text': "You do not have to sign it. If you don't sign that form, the provider "
                               'cannot balance bill you.',
                       'tip': "You do not have to sign it. If you don't sign that form, the provider "
                              'cannot balance bill you.',
                       'timestamp': 285,
                       'timestamp_seconds': 285,
                       'timestamp_label': '[00:04:45]',
                       'url': 'https://www.youtube.com/watch?v=1VtIU2oIxEY&t=285s',
                       'markdown': '[00:04:45](https://www.youtube.com/watch?v=1VtIU2oIxEY&t=285s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MsP7ttGr9OA',
                       'title': 'Quick Take: No Surprises Act: Out of Network Charges',
                       'channel': 'HealthWatch Wisconsin',
                       'author': 'HealthWatch Wisconsin',
                       'text': "The emergency services protections don't apply to all of the follow-up or "
                               'ancillary treatment that individuals might get after that emergency has '
                               'concluded.',
                       'tip': "The emergency services protections don't apply to all of the follow-up or "
                              'ancillary treatment that individuals might get after that emergency has '
                              'concluded.',
                       'timestamp': 113,
                       'timestamp_seconds': 113,
                       'timestamp_label': '[00:01:53]',
                       'url': 'https://www.youtube.com/watch?v=MsP7ttGr9OA&t=113s',
                       'markdown': '[00:01:53](https://www.youtube.com/watch?v=MsP7ttGr9OA&t=113s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wySlaLru-l4',
                       'title': 'My In-Network Doctor Sent My Labs Out-of-Network… Now I Owe $2,000?',
                       'channel': 'Insured and Informed',
                       'author': 'Insured and Informed',
                       'text': 'CMS guidance states that the notice and consent exception cannot be '
                               'applied to ancillary services, which includes laboratory services.',
                       'tip': 'CMS guidance states that the notice and consent exception cannot be applied '
                              'to ancillary services, which includes laboratory services.',
                       'timestamp': 137,
                       'timestamp_seconds': 137,
                       'timestamp_label': '[00:02:17]',
                       'url': 'https://www.youtube.com/watch?v=wySlaLru-l4&t=137s',
                       'markdown': '[00:02:17](https://www.youtube.com/watch?v=wySlaLru-l4&t=137s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PVUGwjJg-VI',
                       'title': 'In-Network Hospital, Out-of-Network Doctor: The Private Equity Trap',
                       'channel': 'Capital Autopsy',
                       'author': 'Capital Autopsy',
                       'text': 'Federal regulators estimated the system would handle about seventeen '
                               'thousand disputes a year. Instead, providers filed about six hundred and '
                               'fifty thousand in twenty twenty-three.',
                       'tip': 'Federal regulators estimated the system would handle about seventeen '
                              'thousand disputes a year. Instead, providers filed about six hundred and '
                              'fifty thousand in twenty twenty-three.',
                       'timestamp': 486,
                       'timestamp_seconds': 486,
                       'timestamp_label': '[00:08:06]',
                       'url': 'https://www.youtube.com/watch?v=PVUGwjJg-VI&t=486s',
                       'markdown': '[00:08:06](https://www.youtube.com/watch?v=PVUGwjJg-VI&t=486s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8NDnQoTkjb4',
                       'title': 'Healthcare In-Network / Out-of-Network Bait and Switch',
                       'channel': 'AHealthcareZ - Healthcare Finance Explained',
                       'author': 'AHealthcareZ - Healthcare Finance Explained',
                       'text': 'The in-network physician bill might only be like $250 but the out of '
                               'network facility bill could be upwards of like $20,000.',
                       'tip': 'The in-network physician bill might only be like $250 but the out of '
                              'network facility bill could be upwards of like $20,000.',
                       'timestamp': 110,
                       'timestamp_seconds': 110,
                       'timestamp_label': '[00:01:50]',
                       'url': 'https://www.youtube.com/watch?v=8NDnQoTkjb4&t=110s',
                       'markdown': '[00:01:50](https://www.youtube.com/watch?v=8NDnQoTkjb4&t=110s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3OCpShEAIJs',
                       'title': 'Surprise Medical Bills: No Surprises Act Protections Explained',
                       'channel': 'Welcome to The Patient Blueprint.',
                       'author': 'Welcome to The Patient Blueprint.',
                       'text': "That $1,340 comes from $3,500 minus $1,800 minus $360, and it's prohibited "
                               'under the No Surprises Act. Mark pays only $360.',
                       'tip': "That $1,340 comes from $3,500 minus $1,800 minus $360, and it's prohibited "
                              'under the No Surprises Act. Mark pays only $360.',
                       'timestamp': 85,
                       'timestamp_seconds': 85,
                       'timestamp_label': '[00:01:25]',
                       'url': 'https://www.youtube.com/watch?v=3OCpShEAIJs&t=85s',
                       'markdown': '[00:01:25](https://www.youtube.com/watch?v=3OCpShEAIJs&t=85s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '1tAnAfBQ9O8',
                       'title': 'Unexpected Medical Bill? Know Your Rights Under the No Surprises Act',
                       'channel': 'The On-Air Advocate',
                       'author': 'The On-Air Advocate',
                       'text': 'If your rights are violated, you still file your complaint with CMS. You '
                               "have 120 days to take action, and it's completely free to file.",
                       'tip': 'If your rights are violated, you still file your complaint with CMS. You '
                              "have 120 days to take action, and it's completely free to file.",
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=1tAnAfBQ9O8&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=1tAnAfBQ9O8&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OWN7CBskcIQ',
                       'title': 'Out-of-Network Bill Shock? Negotiate It Down 60% With This Script',
                       'channel': 'Bill Fighter',
                       'author': 'Bill Fighter',
                       'text': 'Pro tip on your opening offer. Start at about 25% of the original bill.',
                       'tip': 'Pro tip on your opening offer. Start at about 25% of the original bill.',
                       'timestamp': 431,
                       'timestamp_seconds': 431,
                       'timestamp_label': '[00:07:11]',
                       'url': 'https://www.youtube.com/watch?v=OWN7CBskcIQ&t=431s',
                       'markdown': '[00:07:11](https://www.youtube.com/watch?v=OWN7CBskcIQ&t=431s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q2.'}]}
