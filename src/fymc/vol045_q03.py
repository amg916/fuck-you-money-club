from __future__ import annotations

CHAPTER_3 = {'id': 'Q3',
 'chapter_id': 'Q3',
 'chapter_number': 3,
 'question_number': 3,
 'slug': 'nsa-compliance-layer-qpa-gfe-state-law-erisa-preemption',
 'question_prompt': 'What compliance obligations surround NSA disputes—QPA calculation, good faith '
                    'estimates, patient-provider dispute resolution, state surprise-billing laws, and '
                    'ERISA preemption—and how do they shape who can arbitrate where?',
 'kicker': 'Q3 / THE BIG MONEY PLAYBOOKS',
 'title': 'The Compliance Layer: QPA Methodology, Good Faith Estimates, State Laws, and ERISA Preemption',
 'subtitle': 'CMS QPA calculation webinar, AMA out-of-network payment process, good faith estimate and '
             'PPDR requirements, provider GFE training, Texas, Michigan, and New Hampshire state dispute '
             'regimes, fully insured vs. self-funded ERISA plans, preemption and anti-subrogation, and '
             'business associate agreements',
 'layout_template': 'financial_analysis',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from the AMA, CMS, state regulators, billing firms and law firms '
                      'converge on one operating reality: No Surprises Act protections are narrow, '
                      'facility-bound, and governed by a strict precedence of all-payer model, specified '
                      'state law, then federal IDR, with self-funded ERISA plans staying federal unless '
                      'they opt in. The street mechanics are hard numbers: 30 days to invoke negotiation, '
                      '4 days to file IDR, a 50-minute portal timeout, QPA built on the 2019 median '
                      'contracted rate with at least 3 rates, and a $400 per-provider PPDR trigger with a '
                      '$25 fee. The fights are real: the AMA says the QPA presumption tilted the scale '
                      'toward insurers, NSCHBC Edge speakers see resolutions sliding to the lowest '
                      'Medicaid rate, and Michigan, New Hampshire, and Texas each layer state-specific '
                      'routes, fees, and opt-in rules on top.',
 'key_metrics': [{'label': 'PPDR Dispute Trigger Threshold',
                  'metric': 'PPDR Dispute Trigger Threshold',
                  'value': '$400 or more over the good faith estimate, assessed per provider',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'CMS presenters set patient-provider dispute eligibility at billed charges of '
                             'at least $400 above the GFE; a $300 estimate against an $850 bill qualifies, '
                             'filed within 120 days with a $25 administrative fee.',
                  'source': 'CMSHHSgov ([RRI2VT8QiiI @ 00:40:00])'},
                 {'label': 'Federal IDR Initiation Window',
                  'metric': 'Federal IDR Initiation Window',
                  'value': '4 days after the 30-day open negotiation ends',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'The AMA panel reports the provider has 4 days to initiate IDR on the portal '
                             'once negotiation fails, after which the parties pick an IDR entity or the '
                             'federal government picks one.',
                  'source': 'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:22:04])'},
                 {'label': 'New Hampshire State IDR Batch Size',
                  'metric': 'New Hampshire State IDR Batch Size',
                  'value': 'Up to 25 qualified items or services per single fee',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'The New Hampshire Insurance Department lets a certified IDR entity consider '
                             'up to 25 batched items for one fee, with tiered fees per additional 25, for '
                             'the same provider and carrier within 30 days.',
                  'source': 'New Hampshire Insurance Department ([C6hIoQuEWeA @ 00:04:45])'},
                 {'label': 'QPA Methodology Penalty Exposure',
                  'metric': 'QPA Methodology Penalty Exposure',
                  'value': 'Up to $100 per day, per entity, per affected individual',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'CMS compliance staff describe QPA penalties adjusted annually, waived only '
                             'if the failure was unknowable or had reasonable cause and was fixed within '
                             '30 days, with the burden on the entity.',
                  'source': 'CMSHHSgov ([Sp7aK2UsmlE @ 00:48:11])'}],
 'sections': [{'section_number': 1,
               'heading': 'The Practitioner Consensus: Narrow Protections, Strict Precedence, and Two '
                          'Anchor Documents',
               'paragraphs': ['The protected zone is narrower than most billing offices assume, and every '
                              'serious practitioner lines up on that point. The American Medical '
                              'Association panel maps three protected lanes: emergency services at '
                              'out-of-network hospital EDs or freestanding EDs, non-emergency '
                              'out-of-network care delivered inside an in-network hospital or ambulatory '
                              'surgery center, and air ambulance, with payers owing payment within 30 days '
                              'and an initial payment that must be reasonably complete [6_ODgJ97UtA @ '
                              '00:08:13]. The NSCHBC Edge Podcast discussion with healthcare attorney '
                              'Amanda Wish lands in the same place: the facility rules hit hospitals, '
                              'long-term acute care, ambulatory surgery centers, and facilities, not '
                              'physician clinics, and the federal law only applies in very limited '
                              'circumstances [uUBAmK-bcwg @ 00:21:49]. DAS Health draws the transport '
                              'line, with air ambulance inside the protections and ground ambulance '
                              'outside them [e5b1ICVPSZs @ 00:10:37]. The economic engine behind the whole '
                              "fight is the staffing model rather than the patient: WFAA's reporting shows "
                              'most Texas ER doctors do not actually work for the hospital, they are '
                              'contracted out, and they do not take the same plans as the building they '
                              'stand in [_ofpUW91u8o @ 00:00:37]. Operators therefore start every file '
                              'with setting triage, confirming the place of service, the facility network '
                              'status, and the physician arrangement before quoting a single protection to '
                              'anyone.',
                              'Which law governs a claim is the second point of agreement, and no '
                              'practitioner pretends the answer is easy. The AMA panel lays out a strict '
                              'order of precedence, an all-payer model first (Maryland only), then a '
                              'specified state law, then the federal IDR, with ERISA plans generally '
                              'staying federal unless the plan opts in to the state process [6_ODgJ97UtA @ '
                              "00:12:56]. Zotec's Marc Eisenberg and Thomas Harold, speaking at Becker's "
                              'Hospital Review, name New Jersey and Texas as states letting self-funded '
                              'plans opt in and flag the operational trap: remittance files do not '
                              "identify whether a plan is ERISA [RJps0omOazk @ 00:28:17]. Miller Johnson's "
                              'Michigan team hits the same wall, warning there is no reliable way to tell '
                              "self-funded from insured coverage when a card may carry only a small 'sf' "
                              "[EwlPyAVGU8k @ 00:08:21]. New Hampshire's insurance department confirms the "
                              'pattern at the state level: its IDR route is mandatory for fully insured '
                              'plans, optional for self-funded plans, and no self-funded plan had opted in '
                              'yet, though Consumer Services can confirm plan type on request [C6hIoQuEWeA '
                              '@ 00:16:15]. Plan-type confirmation is therefore a standing intake step, '
                              'not an afterthought, because the wrong forum assumption burns the filing '
                              'clock.',
                              'The two documents that move money are the qualifying payment amount on the '
                              'plan side and the good faith estimate on the provider side, and the '
                              "speakers agree on what each one is. CMS's Colin Goldfinch and team define "
                              "the QPA as the plan's median contracted rate as of January 31, 2019, "
                              'increased for inflation, and IDR entities must consider it [Sp7aK2UsmlE @ '
                              '00:07:55]. The AMA panel argues the original rules put a thumb on the scale '
                              'for insurers by presuming that median correct, which drove the AMA/AHA and '
                              'Texas Medical Association lawsuits and the February vacatur of the '
                              'weighting in the Eastern District of Texas [6_ODgJ97UtA @ 00:02:14]. On the '
                              'estimate side, CMS presenters treat any cost inquiry as a GFE request '
                              '[RRI2VT8QiiI @ 00:18:56], and HIPAA TV goes further, saying any cost '
                              'conversation triggers a GFE, the rule reaches every licensed provider '
                              'including cash-only, non-HIPAA practices, and the exposure runs to ten '
                              'thousand dollar penalties [T99RB14fdY4 @ 00:02:44]. The operating consensus '
                              "is blunt: the QPA sets the plan's anchor price, the GFE sets the yardstick "
                              'a self-pay patient can dispute against, and front-desk staff who discuss '
                              'price without issuing paperwork create exposure on the spot.'],
               'table': {'caption': 'Where the practitioners agree: scope, forum precedence, plan-type '
                                    'blind spots, and the two anchor documents',
                         'headers': ['Consensus Point',
                                     'What The Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Protected settings are narrow and tied to facilities',
                                   'Emergency care at out-of-network EDs, out-of-network care inside '
                                   'in-network hospitals or ASCs, plus air ambulance',
                                   'Most services delivered in a physician office fall outside these '
                                   'federal balance billing rules entirely',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:08:13])'],
                                  ['Physician clinics sit outside the facility rules',
                                   'The rules hit hospitals, long-term acute care, ambulatory surgery '
                                   'centers and facilities, not physician clinics',
                                   'Confirm the place of service before invoking any No Surprises Act '
                                   'protection or defense',
                                   'NSCHBC Edge Podcast ([uUBAmK-bcwg @ 00:21:49])'],
                                  ['Forum precedence runs in a fixed order',
                                   'All-payer model first (Maryland only), then a specified state law, '
                                   'then the federal IDR process',
                                   'Self-funded ERISA plans generally stay federal unless the plan '
                                   'affirmatively opts into state law',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:12:56])'],
                                  ['ERISA status is invisible on the remit',
                                   'Remittance files do not identify whether the paying plan is an ERISA '
                                   'plan at all',
                                   'Build a separate plan-type verification step because the remit alone '
                                   'will never tell you',
                                   "Becker's Hospital Review ([RJps0omOazk @ 00:28:17])"],
                                  ['Member cards are a weak plan-type signal',
                                   'No reliable way to tell self-funded from insured plans; a card may '
                                   "only show a small 'sf'",
                                   'Treat the card as a hint and confirm self-funded status through '
                                   'another channel before filing',
                                   'Miller Johnson ([EwlPyAVGU8k @ 00:08:21])'],
                                  ["The QPA is the plan's anchor number",
                                   'Median contracted rate as of January 31, 2019, increased for '
                                   'inflation, and IDR entities must consider it',
                                   'Expect every plan offer and every arbitration file to be framed around '
                                   'this single median figure',
                                   'CMSHHSgov ([Sp7aK2UsmlE @ 00:07:55])'],
                                  ['Any price conversation triggers a good faith estimate',
                                   'Applies to all licensed providers, including cash-only non-HIPAA '
                                   'practices, with ten thousand dollar penalties',
                                   'Script front-desk staff so every price question produces a written '
                                   'estimate in the required format',
                                   'HIPAA TV ([T99RB14fdY4 @ 00:02:44])']]}},
              {'section_number': 2,
               'heading': 'Exact Street Mechanics, Tools & Numbers: Clocks, QPA Math, and GFE Thresholds',
               'paragraphs': ['The federal clock is unforgiving and the AMA panel walks it day by day. The '
                              'plan pays or denies within 30 days; the provider then has 30 days to invoke '
                              'a 30-day open negotiation by form notice, then 4 days to initiate IDR on '
                              'the portal, where the parties pick an IDR entity or the federal government '
                              'picks one [6_ODgJ97UtA @ 00:21:22]. Offers are due within 10 days, the '
                              'decision within 30, and payment within 30, with a 90-day cooling-off period '
                              'during which claims are batched; the portal form also carries a 50-minute '
                              'timeout, so the file has to be assembled before login [6_ODgJ97UtA @ '
                              '00:24:00]. The arbiter must select one of the two offers, baseball style, '
                              "and the providers are really in the driver's seat about initiating. New "
                              "Hampshire's insurance department pitches a faster state lane: no "
                              "administrative fee, each party paying half the entity's fee instead of "
                              'loser-pays, and up to 25 qualified items batched for a single fee when they '
                              'share provider, carrier, and a 30-day window [C6hIoQuEWeA @ 00:04:45]. The '
                              'enforcement teeth are real: a party that fails to submit its half of the '
                              'fee by day 10 eats a default judgment, and the decision lands by day 30 '
                              '[C6hIoQuEWeA @ 00:12:38].',
                              'Inside the QPA math, CMS presenters give operators the exact levers to '
                              'probe. Each separate contract counts as one rate, a group contract with a '
                              'uniform rate counts once, and each unique rate inside a multi-provider '
                              'contract counts separately, while single-case agreements and letters of '
                              'agreement are excluded and rented or TPA-managed network rates count '
                              '[Sp7aK2UsmlE @ 00:11:20]. Sufficient information means at least 3 '
                              'contracted rates as of January 31, 2019, anesthesia runs as indexed '
                              'conversion factor times base, time, and physical-status modifier units, and '
                              'every initial payment or denial must carry the QPA, a compliance '
                              'certification, notice of the 30-day negotiation and 4-day IDR windows, and '
                              'contact information; on request the plan must also disclose '
                              'non-fee-for-service rate use, the database used, related codes, and '
                              'excluded incentive payments [Sp7aK2UsmlE @ 00:36:07]. The pressure point is '
                              'enforcement, not arbitration: the AMA panel stresses that the IDR entity '
                              'does not check whether the QPA was calculated correctly, so suspected '
                              'errors get reported to the government [6_ODgJ97UtA @ 00:31:34]. CMS then '
                              'audits up to 25 plans or issuers a year plus complaint-triggered audits, '
                              'demands a step-by-step methodology narrative and a file of all QPAs, and '
                              'penalizes up to $100 per day, per entity, per affected individual '
                              '[Sp7aK2UsmlE @ 00:39:14].',
                              'On the estimate side the numbers are hard-coded. CMS presenters set the '
                              'PPDR trigger at billed charges of $400 or more over the GFE, assessed per '
                              'provider, with a $300 estimate against an $850 bill qualifying, a 120-day '
                              'filing window, a $25 administrative fee, no collections during the dispute, '
                              'and 6-year retention [RRI2VT8QiiI @ 00:40:00]. HIPAA TV hammers the '
                              'per-provider math: three providers each over by $300, $900 in total, does '
                              'not trigger arbitration, and the listed defenses are acuity, scope, and '
                              'complications [T99RB14fdY4 @ 00:18:25]. DAS Health runs the same test with '
                              'a $1,000 estimate split $500/$500 and billed $800/$700, which is not '
                              'eligible, and adds that a settlement must cut the bill by at least half the '
                              'fee with notice within 3 business days [e5b1ICVPSZs @ 00:39:42]. For '
                              'recurring care, Dr. Marie Fang of Private Practice Skills works from the '
                              'CMS template, customizes it per client, and issues one recurring GFE '
                              'covering up to 12 months, roughly 40 to 52 sessions, starting with a TBD '
                              'diagnosis and re-issuing whenever costs change or annually with rate '
                              'increases [JT1pxEvMFxw @ 00:08:54]. That single document collapses dozens '
                              'of per-session estimates into one renewal cycle, the admin relief Fang '
                              'wants as a clinician who would rather see clients than do paperwork.'],
               'table': {'caption': 'Street-level clocks, thresholds, and batch rules operators run '
                                    'against',
                         'headers': ['Mechanic',
                                     'Exact Number Or Rule',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Federal open negotiation trigger',
                                   '30 days after the initial payment or denial to invoke a 30-day '
                                   'negotiation by form notice',
                                   'Calendar the remit date immediately so the negotiation notice window '
                                   'never quietly lapses',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:21:22])'],
                                  ['Federal IDR initiation window',
                                   '4 days after negotiation closes to initiate IDR on the federal portal',
                                   'Start the portal filing the moment negotiation fails, with the claim '
                                   'data already assembled',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:22:04])'],
                                  ['Federal portal session limit',
                                   'The portal form has a 50-minute timeout and claims ready before April '
                                   '15 were due May 6',
                                   'Gather every field and attachment offline before logging in so the '
                                   'session does not expire',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:24:00])'],
                                  ['New Hampshire state batching',
                                   'Up to 25 items per fee for the same provider and carrier within 30 '
                                   'days',
                                   'Bundle the same patient or similar services across patients to spread '
                                   'one fee across the batch',
                                   'New Hampshire Insurance Department ([C6hIoQuEWeA @ 00:04:45])'],
                                  ['New Hampshire half-fee default',
                                   'Each party pays half the entity fee by day 10 or a default judgment is '
                                   'entered',
                                   'Pay your half on time and watch for carriers that miss theirs and lose '
                                   'by default',
                                   'New Hampshire Insurance Department ([C6hIoQuEWeA @ 00:12:38])'],
                                  ['QPA sufficient information floor',
                                   'At least 3 contracted rates as of January 31, 2019, plus 25% claims '
                                   'volume for later years',
                                   'Below that floor the plan falls back to an eligible database, so ask '
                                   'which one it used',
                                   'CMSHHSgov ([Sp7aK2UsmlE @ 00:25:50])'],
                                  ['PPDR eligibility threshold',
                                   '$400 or more over the GFE per provider, filed within 120 days, with a '
                                   '$25 fee',
                                   "Keep each provider's bill within $400 of its own estimate to stay "
                                   'outside the dispute process',
                                   'CMSHHSgov ([RRI2VT8QiiI @ 00:40:00])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': "What the Practitioners Do That the Forms Don't Say",
                           'body': 'These are the moves the speakers flag as the difference between a '
                                   'recovered claim and a dead file: prep before the clock, front-load the '
                                   "argument, use the patient's policy, and force the plan to show its QPA "
                                   'work.',
                           'items': ['Assemble the entire IDR submission offline before opening the '
                                     'federal portal, because the form times out at 50 minutes and the '
                                     'filing windows are measured in days [American Medical Association '
                                     '(AMA) — 6_ODgJ97UtA @ 00:24:00].',
                                     'Put your full case into the negotiation with the plan, because in '
                                     'Michigan you are not supposed to add information by the time you '
                                     'reach arbitration, so do it right the first time [Miller Johnson — '
                                     'EwlPyAVGU8k @ 00:27:15].',
                                     "On ERISA claims, pull the timely-filing limit from the patient's "
                                     'policy rather than the provider contract: if the policy says a year, '
                                     'it is a year even if the contract says three months, and '
                                     'unchallenged recoupment letters are how insurers get away with it '
                                     '[Orion Billing - Medical Billing Basics — _z9Vfv0D6_4 @ 00:01:52].',
                                     'Request the on-demand QPA disclosures, covering non-fee-for-service '
                                     'rate use, the database used, related codes, and excluded incentive '
                                     'payments, since the plan must supply them on request [CMSHHSgov — '
                                     'Sp7aK2UsmlE @ 00:36:07].']},
               'sop_steps': [{'step': 1,
                              'title': 'Classify the claim before touching a form',
                              'action': 'Confirm the plan, the provider or facility, and the item or '
                                        'service, then rule out a plain billing error.',
                              'detail': 'Run the three-variable check on plan, provider/facility, and '
                                        'item/service to decide whether a state law applies [American '
                                        'Medical Association (AMA) — 6_ODgJ97UtA @ 00:15:21]; the first '
                                        'analysis is whether the NSA applies at all or whether the file is '
                                        'simply a billing error [NSCHBC Edge Podcast — uUBAmK-bcwg @ '
                                        '00:10:30].'},
                             {'step': 2,
                              'title': 'Read the remit for the federal signal',
                              'action': 'Check whether the plan sent a QPA and the required disclosures '
                                        'with its initial payment or denial.',
                              'detail': 'A plan that believes federal law applies sends the QPA with its '
                                        'remittance advice [American Medical Association (AMA) — '
                                        '6_ODgJ97UtA @ 00:19:50]; that initial payment or denial must also '
                                        'carry a compliance certification, the 30-day negotiation and '
                                        '4-day IDR notice, and contact information [CMSHHSgov — '
                                        'Sp7aK2UsmlE @ 00:36:07].'},
                             {'step': 3,
                              'title': 'Run the negotiation and filing clock',
                              'action': 'Invoke open negotiation inside 30 days, then file IDR inside the '
                                        'initiation window on the correct portal.',
                              'detail': 'Invoke the 30-day open negotiation within 30 days of the payment '
                                        'or denial, then initiate IDR within 4 days [American Medical '
                                        'Association (AMA) — 6_ODgJ97UtA @ 00:22:04]; in New Hampshire the '
                                        'provider can instead file the state route within 4 business days '
                                        'after negotiation ends, uploaded via the portal [New Hampshire '
                                        'Insurance Department — C6hIoQuEWeA @ 00:09:29].'},
                             {'step': 4,
                              'title': 'Build the offer on allowed factors only',
                              'action': 'Load the offer with permitted factors and strip out every '
                                        'prohibited benchmark.',
                              'detail': 'Argue provider expertise, training and quality, market share, '
                                        'patient acuity and complexity, teaching status and case mix, and '
                                        '4 years of good-faith network efforts [American Medical '
                                        'Association (AMA) — 6_ODgJ97UtA @ 00:25:42]; keep billed charges, '
                                        'Medicare/Medicaid rates, and usual-and-customary charges out of '
                                        'the submission [American Medical Association (AMA) — 6_ODgJ97UtA '
                                        '@ 00:26:17].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split in the compliance layer is over whether anyone should '
                              'trust the qualifying payment amount. The AMA panel argues that the '
                              "implementing regulations put 'a thumb on the scale' for insurers by "
                              "presuming the QPA, which is the plan's own median in-network rate, is the "
                              'correct answer [6_ODgJ97UtA @ 00:02:14]. Michael Culver adds that the IDR '
                              'entity never checks whether that QPA was calculated correctly, so suspected '
                              'errors get reported to the government instead of being argued inside the '
                              'arbitration [6_ODgJ97UtA @ 00:31:34]. CMS presents the opposite picture. It '
                              'describes a rule-bound median of contracted rates as of January 31, 2019, '
                              'inflated by CPI-U. Single-case agreements and letters of agreement are '
                              'stripped out, and each separate contract counts as one rate regardless of '
                              "claim volume [Sp7aK2UsmlE @ 00:07:55]. The Zotec speakers on the Becker's "
                              "panel reject that comfort and call carrier databases unverified, 'a black "
                              "box' [RJps0omOazk @ 00:53:01]. Operators should read the gap literally. The "
                              'regulator describes a precise formula, while billing-side practitioners say '
                              'nobody outside the plan can see the inputs. The QPA printed on the '
                              'remittance is therefore a number the plan controls. The only outside '
                              'pressure point the AMA names is a report to the government, not a challenge '
                              'inside the IDR file itself.',
                              'Practitioners also split on whether a provider ever gets to pick a forum. '
                              "The AMA panel's line is flat: there should be one process that applies to "
                              'any given claim, either the state or the federal process, and parties get '
                              'no choice between them [6_ODgJ97UtA @ 00:54:45]. The New Hampshire '
                              'Insurance Department describes its Chapter 143 process as an alternative to '
                              'federal IDR that the provider chooses. It sells that lane on hard terms: no '
                              'administrative fee, faster turnaround, each party paying half the entity '
                              'fee instead of loser-pays, and a department that strictly enforces carrier '
                              'payment [C6hIoQuEWeA @ 00:02:55]. Amanda Wish on the NSCHBC Edge Podcast '
                              'frames the question as layering rather than choosing. Her instruction is to '
                              'first comply with the federal law and then also comply with the more '
                              'specific state law [uUBAmK-bcwg @ 00:27:05]. The ERISA wrinkle cuts across '
                              'all three views. The Zotec speakers say New Jersey and Texas let '
                              'self-funded plans opt into state rules, and Washington was added in Q&A '
                              '[RJps0omOazk @ 00:27:38]. New Hampshire, by contrast, reports that none of '
                              'its self-funded plans had opted in yet. The playbooks really do differ. A '
                              'New Hampshire provider holding a fully insured claim gets a cheaper lane, '
                              'while a Texas operator faces what the AMA calls all Texas or all federal.',
                              'On the good faith estimate, the front-desk trainers give operators '
                              'conflicting instructions. Dr. Marie Fang of Private Practice Skills tells '
                              'therapists to ask whether the client will use in- or out-of-network '
                              'benefits and to document the answer. Fang treats those clients as exempt '
                              'for now but still advises issuing a GFE anyway [JT1pxEvMFxw @ 00:06:15]. '
                              'HIPAA TV takes a harder line: group-plan members who are not using their '
                              'benefits count as self-pay, and any cost conversation triggers an estimate '
                              '[T99RB14fdY4 @ 00:01:45]. The co-provider requirement splits the same way. '
                              "DAS Health's Lindsay Lanning reports that co-provider estimates were not "
                              'enforced in 2022 and were pushed to 2023 after industry letters cited the '
                              'manual burden [e5b1ICVPSZs @ 00:33:29]. Amanda Wish, however, says the '
                              'co-provider requirement is still there [uUBAmK-bcwg @ 00:16:40]. Delivery '
                              'timing diverges too. Fang counts three business days from the date the '
                              'appointment is scheduled, while HIPAA TV counts back to three days before '
                              'the service date for appointments booked ten days out. Record retention '
                              "adds a third fork, with Miller Johnson's Michigan disclosure rule running "
                              "seven years against HIPAA TV's six-year NSA minimum. Fang's fallback of "
                              "issuing the GFE even to exempt clients lines up with HIPAA TV's "
                              'estimate-everyone stance, and it keeps a practice on the stricter side of '
                              'both camps.'],
               'table': {'caption': 'Side-by-side practitioner disagreements on QPA trust, forum routing, '
                                    'ERISA opt-in, and GFE scope',
                         'headers': ['Contested Issue',
                                     'Position A As Taught',
                                     'Position B As Taught',
                                     'Expert Source'],
                         'rows': [['Whether the plan-calculated QPA deserves a presumption of correctness',
                                   'AMA says the rules put a thumb on the scale for insurers, and IDR '
                                   'entities never check QPA math',
                                   'CMS describes the QPA as the median contracted rate as of January 31, '
                                   '2019, inflated by CPI-U',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:02:14]); '
                                   'CMSHHSgov ([Sp7aK2UsmlE @ 00:07:55])'],
                                  ['Whether carrier rate data can be verified by anyone outside the plan',
                                   'Zotec speakers call carrier databases unverified and a black box that '
                                   'providers cannot audit',
                                   'CMS says it audits up to 25 plans or issuers per year, plus audits '
                                   'triggered by complaints',
                                   "Becker's Hospital Review ([RJps0omOazk @ 00:53:01]); CMSHHSgov "
                                   '([Sp7aK2UsmlE @ 00:39:14])'],
                                  ['Whether a provider can choose between the state and federal dispute '
                                   'forums',
                                   'AMA says one process applies to any given claim, and the parties get '
                                   'no choice',
                                   'New Hampshire runs a provider-chosen state alternative with no '
                                   'administrative fee and a split entity fee',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:54:45]); New '
                                   'Hampshire Insurance Department ([C6hIoQuEWeA @ 00:02:12])'],
                                  ['Whether self-funded ERISA plans can be pulled into state surprise '
                                   'billing processes',
                                   'Zotec speakers report that New Jersey, Texas, and later Washington let '
                                   'self-funded plans opt in',
                                   'New Hampshire says self-funded participation is optional, and no '
                                   'self-funded plan had opted in yet',
                                   "Becker's Hospital Review ([RJps0omOazk @ 00:27:38]); New Hampshire "
                                   'Insurance Department ([C6hIoQuEWeA @ 00:16:15])'],
                                  ['Whether insured clients who skip their benefits still need a good '
                                   'faith estimate',
                                   'Fang treats in- or out-of-network benefit users as exempt for now but '
                                   'advises issuing anyway',
                                   'HIPAA TV counts group-plan members not using benefits as self-pay and '
                                   'estimates every cost conversation',
                                   'Private Practice Skills ([JT1pxEvMFxw @ 00:06:15]); HIPAA TV '
                                   '([T99RB14fdY4 @ 00:01:45])'],
                                  ["Whether co-provider charges must appear on the convening provider's "
                                   'estimate today',
                                   'Lanning says co-provider estimates were not enforced in 2022 and were '
                                   'moved to 2023',
                                   'Wish says the co-provider good faith estimate requirement is still '
                                   'there for practices',
                                   'DAS Health ([e5b1ICVPSZs @ 00:33:29]); NSCHBC Edge Podcast '
                                   '([uUBAmK-bcwg @ 00:16:40])'],
                                  ['Whether emergency departments can collect balance billing consent '
                                   'before emergent treatment',
                                   'Fletcher claims the ER must obtain a patient signature before emergent '
                                   'treatment is delivered',
                                   'DAS Health says consent is barred for emergency medicine, '
                                   'anesthesiology, pathology, radiology, and lab services',
                                   'NSCHBC Edge Podcast ([uUBAmK-bcwg @ 00:20:37]); DAS Health '
                                   '([e5b1ICVPSZs @ 00:24:18])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most expensive failures are clock failures, and the speakers describe '
                              'them bluntly. Michael Culver of the AMA panel warns that the federal IDR '
                              'portal form times out after 50 minutes, so the claim data has to be '
                              'gathered before logging in. Culver also notes that claims ready before '
                              'April 15 had to be filed by May 6 [6_ODgJ97UtA @ 00:24:00]. The same panel '
                              'warns that parties stalling while they work through a state regulator can '
                              'miss the federal deadlines entirely, because the four-day initiation window '
                              "keeps running. Miller Johnson's Michigan team describes the state-side "
                              'version. A claim submitted after 60 days leaves the provider stuck, with no '
                              'ability to balance bill [EwlPyAVGU8k @ 00:46:02]. Once a dispute reaches '
                              'arbitration, the team says, you are not supposed to be adding additional '
                              'information, so you want to do it right the first time when arguing with '
                              'the plan [EwlPyAVGU8k @ 00:27:15]. New Hampshire adds a cash trap: a party '
                              'that fails to submit its half of the IDR entity fee by day 10 has a default '
                              'judgment entered against it [C6hIoQuEWeA @ 00:12:38]. Each of these losses '
                              'is procedural. The record built during open negotiation is the record that '
                              'decides the dispute, and a missed fee, a stale claim, or a late portal '
                              'filing can end the fight before value is ever argued.',
                              'The economics checks raised by billing-side speakers are about leverage, '
                              'not paperwork. Marc Eisenberg and Thomas Harold of Zotec, speaking on the '
                              "Becker's panel, warn about California's standard, spoken as 25% of "
                              'Medicare. They say it is pushing carriers to cancel contracts priced above '
                              'that level, and they report a Georgia contract cancelled after a demand for '
                              'a 25% rate cut [RJps0omOazk @ 00:06:29]. They also put a price on the '
                              'dispute machinery itself: IDR costs, slower recoveries, and roughly $20,000 '
                              "to use Colorado's all-payer claims database [RJps0omOazk @ 00:09:23]. On "
                              'the NSCHBC Edge Podcast, the hosts describe what happens on the ground. '
                              'Billing companies file hundreds of IDR requests and get pennies on the '
                              'dollar without reaching a resolution [uUBAmK-bcwg @ 00:04:15]. The podcast '
                              'also reports an anesthesia group closed out of UHC contracting. It adds '
                              'that many resolutions end up paying just the very lowest Medicaid rate '
                              '[uUBAmK-bcwg @ 00:13:20]. The Zotec speakers warned of a slide toward '
                              'Medicare allowable for all. They calculated that the House Pallone '
                              'threshold would leave fewer than 4 to 5% of hospital-based claims eligible '
                              'for arbitration. In their account, an out-of-network position that once '
                              'funded negotiation now triggers contract termination, while arbitration '
                              'volume rises and per-claim recovery falls.',
                              "The quieter failures happen inside the provider's own workflow. On the "
                              'NSCHBC Edge Podcast, a lab client drew two patient complaints after '
                              'ASC-sourced specimens turned out to be out of network with one plan. The '
                              'lab then adjusted the bills to the Medicare allowable. The speakers call '
                              'that noncompliant, because the remit and EOB never showed in-network '
                              'patient responsibility [uUBAmK-bcwg @ 00:19:32]. HIPAA TV reports that the '
                              'EMR-generated estimates evaluated so far fail the GFE requirements and that '
                              'dental-style estimates are wholly inadequate. A practice relying on '
                              'software defaults is exposed to penalties the trainer pegs at $10,000 '
                              "[T99RB14fdY4 @ 00:21:37]. CMS's PPDR walkthrough shows the cost of sloppy "
                              'scoping on the dispute side. A bill without credible justification is cut '
                              'to the GFE amount, and an unjustified new item drops to $0 [RRI2VT8QiiI @ '
                              '01:05:37]. The subrogation lawyers at Matthiesen, Wickert & Lehrer describe '
                              'a parallel recovery leak on the plan side. They see far too many claims '
                              'abandoned because the plan is non-ERISA or fully insured, even though saved '
                              'statutes and governed-by clauses can leave room to recover [M-sP3O4XgCs @ '
                              '00:42:33]. Across these cases, the damage comes from treating a default as '
                              'the compliant answer, whether that default is an EMR template, a Medicare '
                              'adjustment, or a preemption assumption.'],
               'table': {'caption': 'Firsthand failure modes, reported losses, and the fixes the '
                                    'practitioners themselves teach',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Warned',
                                     'Fix Taught By The Speaker',
                                     'Expert Source'],
                         'rows': [['Federal IDR portal session expiring mid-filing',
                                   'The portal form has a 50-minute timeout that wipes an unfinished '
                                   'submission',
                                   'Gather all claim, offer, and party information before opening the '
                                   'portal form',
                                   'American Medical Association (AMA) ([6_ODgJ97UtA @ 00:24:00])'],
                                  ['Michigan claim submitted after the 60-day mark',
                                   'The provider is stuck with the capped payment and cannot balance bill',
                                   'Get the claim in before 60 days, because the carrier must pay within '
                                   '60 days',
                                   'Miller Johnson ([EwlPyAVGU8k @ 00:46:02])'],
                                  ['Thin argument record carried into Michigan arbitration',
                                   'New information is not supposed to be added once the dispute reaches '
                                   'arbitration',
                                   'Make the full argument right the first time while negotiating with the '
                                   'plan',
                                   'Miller Johnson ([EwlPyAVGU8k @ 00:27:15])'],
                                  ['Unpaid half-fee in New Hampshire state IDR',
                                   'A party that fails to submit its half of the fee gets a default '
                                   'judgment',
                                   'Submit the offer and the half-fee together by day 10 of the process',
                                   'New Hampshire Insurance Department ([C6hIoQuEWeA @ 00:12:38])'],
                                  ['Lab adjusting out-of-network bills down to Medicare allowable',
                                   'Two patient complaints followed, and the adjustment was called '
                                   'noncompliant',
                                   'First analyze whether the NSA applies or whether it is a billing error',
                                   'NSCHBC Edge Podcast ([uUBAmK-bcwg @ 00:19:32]); NSCHBC Edge Podcast '
                                   '([uUBAmK-bcwg @ 00:10:30])'],
                                  ['Relying on EMR-generated or dental-style good faith estimates',
                                   'The EMR estimates evaluated so far fail, and dental-style estimates '
                                   'are wholly inadequate',
                                   'Work with the EMR company to build compliant estimates, or start from '
                                   'the CMS template',
                                   'HIPAA TV ([T99RB14fdY4 @ 00:21:37]); Private Practice Skills '
                                   '([JT1pxEvMFxw @ 00:07:24])'],
                                  ['Abandoning recoveries on fully insured or non-ERISA plans',
                                   'Far too many claims are dropped simply because the plan is non-ERISA '
                                   'or fully insured',
                                   'Identify the source of the rule, read the statutory text closely, and '
                                   'check saved statutes',
                                   'Matthiesen, Wickert & Lehrer, S.C. ([M-sP3O4XgCs @ 00:42:33]); '
                                   'Matthiesen, Wickert & Lehrer, S.C. ([M-sP3O4XgCs @ 00:07:48])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Four Checks Before Filing, Billing, Or Collecting',
                           'body': 'Each check below comes from a pitfall a practitioner hit or warned '
                                   'about directly. Clear all four before an out-of-network claim moves to '
                                   'negotiation, dispute, or collections.',
                           'items': ['Confirm plan type before routing the claim. There is no reliable way '
                                     'to tell self-funded from insured plans, and a card may show only a '
                                     "small 'sf' [Miller Johnson — EwlPyAVGU8k @ 00:08:21].",
                                     'Read the remittance for the QPA before choosing a forum. A plan '
                                     'sends the QPA with its remittance advice when it believes federal '
                                     'law applies [American Medical Association (AMA) — 6_ODgJ97UtA @ '
                                     '00:19:50].',
                                     'Freeze collections the moment a PPDR case opens. Suspend all '
                                     'collections and the accrual of late fees on unpaid amounts while the '
                                     'resolution is pending [DAS Health — e5b1ICVPSZs @ 00:42:00].',
                                     'Push back on ERISA overpayment refund and recoupment letters. Orion '
                                     'Billing calls them illegal and says insurers get away with them '
                                     'because nobody challenges them [Orion Billing - Medical Billing '
                                     'Basics — _z9Vfv0D6_4 @ 00:02:13].']}}],
 'pull_quote': '"You\'re not supposed to be adding additional information by the time you get to '
               'arbitration, so you want to make sure you do it right the first time when arguing with the '
               'plan." Attributed to Miller Johnson (EwlPyAVGU8k @ 00:27:15).',
 'diagram_id': 'diag-03',
 'action_checklist': ['Before invoking any dispute process, check the plan, the provider or facility, and '
                      'the item or service to decide whether a specified state law or the federal IDR '
                      'applies, and read the CMS letter to that state rather than relying on the state '
                      'chart [American Medical Association (AMA) — 6_ODgJ97UtA @ 00:15:21].',
                      'Calendar the 30-day open negotiation and the 4-day IDR initiation window from the '
                      'date of the initial payment or denial, and pre-assemble portal data so the '
                      '50-minute form timeout cannot kill the filing [American Medical Association (AMA) — '
                      '6_ODgJ97UtA @ 00:22:04].',
                      "Request the plan's on-request QPA disclosures, covering non-fee-for-service rate "
                      'use, the database used, related codes, and excluded incentive payments, alongside '
                      'the QPA and certification that must accompany every initial payment or denial '
                      '[CMSHHSgov — Sp7aK2UsmlE @ 00:36:07].',
                      'Build each good faith estimate around the most comprehensive single code and the '
                      'cash-pay rate net of discounts and financial-assistance adjustments, and issue a '
                      'new GFE at least 1 business day before service if the scope changes [CMSHHSgov — '
                      'RRI2VT8QiiI @ 00:13:33].',
                      'Post the GFE and dispute-rights notices in the lobby, on the website home page, and '
                      'in financial-discussion rooms, and retain records for at least 6 years [HIPAA TV — '
                      'T99RB14fdY4 @ 00:15:20].',
                      'On fully insured or non-ERISA recoveries, identify whether the made-whole or '
                      'anti-subrogation rule is judge-made or statutory, read the text, and check whether '
                      "the plan uses 'governed by' choice-of-law language before abandoning the claim "
                      '[Matthiesen, Wickert & Lehrer, S.C. — M-sP3O4XgCs @ 00:31:50].'],
 'statutory_citations': [{'title': 'American Medical Association (AMA) — Out-of-network payment process '
                                   'under the No Surprises Act [00:12:56]',
                          'url': 'https://www.youtube.com/watch?v=6_ODgJ97UtA&t=776s',
                          'relevance': 'Primary practitioner testimony on the order of precedence among an '
                                       'all-payer model, a specified state law, and the federal IDR.'},
                         {'title': 'CMSHHSgov — No Surprises Act: Qualifying Payment Amount Calculation '
                                   'Methodology [00:07:55]',
                          'url': 'https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=475s',
                          'relevance': 'Primary practitioner testimony on the QPA as the median contracted '
                                       'rate as of January 31, 2019, increased for inflation.'},
                         {'title': 'CMSHHSgov — No Surprises Act: Understanding Good Faith Estimates & '
                                   'Patient Provider Dispute Resolution Reqs [00:40:00]',
                          'url': 'https://www.youtube.com/watch?v=RRI2VT8QiiI&t=2400s',
                          'relevance': 'Primary practitioner testimony on the $400-per-provider PPDR '
                                       'eligibility threshold over the good faith estimate.'},
                         {'title': 'Matthiesen, Wickert & Lehrer, S.C. — Fully Insured and Non ERISA '
                                   'Plans  Advanced Topics in Preemption and Anti Subrogation Exceptions '
                                   '[00:03:29]',
                          'url': 'https://www.youtube.com/watch?v=M-sP3O4XgCs&t=209s',
                          'relevance': 'Primary practitioner testimony on the three-part ERISA preemption '
                                       'test covering relate-to, the savings clause, and the deemer '
                                       'clause.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': '6_ODgJ97UtA',
                       'title': 'Out-of-network payment process under the No Surprises Act',
                       'channel': 'American Medical Association (AMA)',
                       'author': 'American Medical Association (AMA)',
                       'text': 'There should be one process that applies to any given claim, either the '
                               'state or the federal process.',
                       'tip': 'There should be one process that applies to any given claim, either the '
                              'state or the federal process.',
                       'timestamp': 3285,
                       'timestamp_seconds': 3285,
                       'timestamp_label': '[00:54:45]',
                       'url': 'https://www.youtube.com/watch?v=6_ODgJ97UtA&t=3285s',
                       'markdown': '[00:54:45](https://www.youtube.com/watch?v=6_ODgJ97UtA&t=3285s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6_ODgJ97UtA',
                       'title': 'Out-of-network payment process under the No Surprises Act',
                       'channel': 'American Medical Association (AMA)',
                       'author': 'American Medical Association (AMA)',
                       'text': "As we're going to discuss, the providers are really in the driver's seat "
                               'about initiating the process.',
                       'tip': "As we're going to discuss, the providers are really in the driver's seat "
                              'about initiating the process.',
                       'timestamp': 1213,
                       'timestamp_seconds': 1213,
                       'timestamp_label': '[00:20:13]',
                       'url': 'https://www.youtube.com/watch?v=6_ODgJ97UtA&t=1213s',
                       'markdown': '[00:20:13](https://www.youtube.com/watch?v=6_ODgJ97UtA&t=1213s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Sp7aK2UsmlE',
                       'title': 'No Surprises Act: Qualifying Payment Amount Calculation Methodology',
                       'channel': 'CMSHHSgov',
                       'author': 'CMSHHSgov',
                       'text': 'The rate negotiated under a contract constitutes a single contracted rate '
                               'regardless of the number of claims paid at that contracted rate.',
                       'tip': 'The rate negotiated under a contract constitutes a single contracted rate '
                              'regardless of the number of claims paid at that contracted rate.',
                       'timestamp': 658,
                       'timestamp_seconds': 658,
                       'timestamp_label': '[00:10:58]',
                       'url': 'https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=658s',
                       'markdown': '[00:10:58](https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=658s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Sp7aK2UsmlE',
                       'title': 'No Surprises Act: Qualifying Payment Amount Calculation Methodology',
                       'channel': 'CMSHHSgov',
                       'author': 'CMSHHSgov',
                       'text': 'Additionally, plans and issuers are responsible for the cost associated '
                               'with using an eligible database to determine the QPA.',
                       'tip': 'Additionally, plans and issuers are responsible for the cost associated '
                              'with using an eligible database to determine the QPA.',
                       'timestamp': 1914,
                       'timestamp_seconds': 1914,
                       'timestamp_label': '[00:31:54]',
                       'url': 'https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=1914s',
                       'markdown': '[00:31:54](https://www.youtube.com/watch?v=Sp7aK2UsmlE&t=1914s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RRI2VT8QiiI',
                       'title': 'No Surprises Act: Understanding Good Faith Estimates & Patient Provider '
                                'Dispute Resolution Reqs',
                       'channel': 'CMSHHSgov',
                       'author': 'CMSHHSgov',
                       'text': 'Provider or facility must also suspend the accrual of any late fees on '
                               'unpaid bill amounts until after the PPDR process is completed.',
                       'tip': 'Provider or facility must also suspend the accrual of any late fees on '
                              'unpaid bill amounts until after the PPDR process is completed.',
                       'timestamp': 3223,
                       'timestamp_seconds': 3223,
                       'timestamp_label': '[00:53:43]',
                       'url': 'https://www.youtube.com/watch?v=RRI2VT8QiiI&t=3223s',
                       'markdown': '[00:53:43](https://www.youtube.com/watch?v=RRI2VT8QiiI&t=3223s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_ofpUW91u8o',
                       'title': 'Surprise medical billing will be banished in Texas starting Jan. 1',
                       'channel': 'WFAA',
                       'author': 'WFAA',
                       'text': 'Most ER doctors in Texas do not actually work for the hospital.',
                       'tip': 'Most ER doctors in Texas do not actually work for the hospital.',
                       'timestamp': 37,
                       'timestamp_seconds': 37,
                       'timestamp_label': '[00:00:37]',
                       'url': 'https://www.youtube.com/watch?v=_ofpUW91u8o&t=37s',
                       'markdown': '[00:00:37](https://www.youtube.com/watch?v=_ofpUW91u8o&t=37s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RJps0omOazk',
                       'title': 'Surprise Billing Legislation - Overview, Response, and Future '
                                'Implications',
                       'channel': "Becker's Hospital Review",
                       'author': "Becker's Hospital Review",
                       'text': 'Carrier databases are unverified, a black box.',
                       'tip': 'Carrier databases are unverified, a black box.',
                       'timestamp': 3181,
                       'timestamp_seconds': 3181,
                       'timestamp_label': '[00:53:01]',
                       'url': 'https://www.youtube.com/watch?v=RJps0omOazk&t=3181s',
                       'markdown': '[00:53:01](https://www.youtube.com/watch?v=RJps0omOazk&t=3181s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EwlPyAVGU8k',
                       'title': 'Michigan’s Surprise Billing Law:  What Providers and Health Plans Need to '
                                'Know',
                       'channel': 'Miller Johnson',
                       'author': 'Miller Johnson',
                       'text': "You're not supposed to be adding additional information by the time you "
                               'get to arbitration so you want to make sure you do it right the first time '
                               'when arguing with the plan.',
                       'tip': "You're not supposed to be adding additional information by the time you get "
                              'to arbitration so you want to make sure you do it right the first time when '
                              'arguing with the plan.',
                       'timestamp': 1635,
                       'timestamp_seconds': 1635,
                       'timestamp_label': '[00:27:15]',
                       'url': 'https://www.youtube.com/watch?v=EwlPyAVGU8k&t=1635s',
                       'markdown': '[00:27:15](https://www.youtube.com/watch?v=EwlPyAVGU8k&t=1635s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yI1fsZFZPwY',
                       'title': 'What is a Business Associate Agreement',
                       'channel': 'Compliancy Group',
                       'author': 'Compliancy Group',
                       'text': 'Some examples of business associates include medical billing companies, IT '
                               'service providers and cloud storage vendors.',
                       'tip': 'Some examples of business associates include medical billing companies, IT '
                              'service providers and cloud storage vendors.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=yI1fsZFZPwY&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=yI1fsZFZPwY&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_z9Vfv0D6_4',
                       'title': 'ERISA explained (and Why it Matters)',
                       'channel': 'Orion Billing - Medical Billing Basics',
                       'author': 'Orion Billing - Medical Billing Basics',
                       'text': "If the policy says that the timely filing deadline is a year then it's a "
                               "year even if the doctor's contract says it's three months.",
                       'tip': "If the policy says that the timely filing deadline is a year then it's a "
                              "year even if the doctor's contract says it's three months.",
                       'timestamp': 112,
                       'timestamp_seconds': 112,
                       'timestamp_label': '[00:01:52]',
                       'url': 'https://www.youtube.com/watch?v=_z9Vfv0D6_4&t=112s',
                       'markdown': '[00:01:52](https://www.youtube.com/watch?v=_z9Vfv0D6_4&t=112s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'C6hIoQuEWeA',
                       'title': 'Explaining the Independent Dispute Resolution Process in New Hampshire',
                       'channel': 'New Hampshire Insurance Department',
                       'author': 'New Hampshire Insurance Department',
                       'text': "Each party pays half of the IDR entity's fee rather than the loser paying "
                               'the full fee.',
                       'tip': "Each party pays half of the IDR entity's fee rather than the loser paying "
                              'the full fee.',
                       'timestamp': 205,
                       'timestamp_seconds': 205,
                       'timestamp_label': '[00:03:25]',
                       'url': 'https://www.youtube.com/watch?v=C6hIoQuEWeA&t=205s',
                       'markdown': '[00:03:25](https://www.youtube.com/watch?v=C6hIoQuEWeA&t=205s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'JT1pxEvMFxw',
                       'title': 'How the No Surprises Act Impacts your Practice | Good Faith Estimate',
                       'channel': 'Private Practice Skills',
                       'author': 'Private Practice Skills',
                       'text': "Fortunately we don't have to create a new good faith estimate for every "
                               'single therapy session, we can create a recurring good faith estimate for '
                               'up to 12 months.',
                       'tip': "Fortunately we don't have to create a new good faith estimate for every "
                              'single therapy session, we can create a recurring good faith estimate for '
                              'up to 12 months.',
                       'timestamp': 534,
                       'timestamp_seconds': 534,
                       'timestamp_label': '[00:08:54]',
                       'url': 'https://www.youtube.com/watch?v=JT1pxEvMFxw&t=534s',
                       'markdown': '[00:08:54](https://www.youtube.com/watch?v=JT1pxEvMFxw&t=534s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T99RB14fdY4',
                       'title': 'No Surprises Act  Provider Training',
                       'channel': 'HIPAA TV',
                       'author': 'HIPAA TV',
                       'text': "I'm recommending that everybody get with their EMR company to do these.",
                       'tip': "I'm recommending that everybody get with their EMR company to do these.",
                       'timestamp': 1297,
                       'timestamp_seconds': 1297,
                       'timestamp_label': '[00:21:37]',
                       'url': 'https://www.youtube.com/watch?v=T99RB14fdY4&t=1297s',
                       'markdown': '[00:21:37](https://www.youtube.com/watch?v=T99RB14fdY4&t=1297s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'e5b1ICVPSZs',
                       'title': 'Don’t Be Surprised by the No Surprises Act!',
                       'channel': 'DAS Health',
                       'author': 'DAS Health',
                       'text': 'You have to suspend all collections and accrual late fees on any unpaid '
                               'amounts while this resolution process is pending.',
                       'tip': 'You have to suspend all collections and accrual late fees on any unpaid '
                              'amounts while this resolution process is pending.',
                       'timestamp': 2520,
                       'timestamp_seconds': 2520,
                       'timestamp_label': '[00:42:00]',
                       'url': 'https://www.youtube.com/watch?v=e5b1ICVPSZs&t=2520s',
                       'markdown': '[00:42:00](https://www.youtube.com/watch?v=e5b1ICVPSZs&t=2520s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UVJoOmtBD-s',
                       'title': 'No Surprises Act - Take Control of your Medical Bills!',
                       'channel': 'Ziegler Diamond Law: Debt Fighters',
                       'author': 'Ziegler Diamond Law: Debt Fighters',
                       'text': 'Any out of network provider has to give at least 72 hours notice to the '
                               'patient of the out of network rates and the patient must agree prior to '
                               'the procedure to pay those rates.',
                       'tip': 'Any out of network provider has to give at least 72 hours notice to the '
                              'patient of the out of network rates and the patient must agree prior to the '
                              'procedure to pay those rates.',
                       'timestamp': 66,
                       'timestamp_seconds': 66,
                       'timestamp_label': '[00:01:06]',
                       'url': 'https://www.youtube.com/watch?v=UVJoOmtBD-s&t=66s',
                       'markdown': '[00:01:06](https://www.youtube.com/watch?v=UVJoOmtBD-s&t=66s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'uUBAmK-bcwg',
                       'title': 'No Surprises Act for 2026',
                       'channel': 'NSCHBC Edge Podcast',
                       'author': 'NSCHBC Edge Podcast',
                       'text': 'And so the No Surprises Act, while I get it, I understand why they passed '
                               'this federal law to protect consumers, it only applies in very limited '
                               'circumstances.',
                       'tip': 'And so the No Surprises Act, while I get it, I understand why they passed '
                              'this federal law to protect consumers, it only applies in very limited '
                              'circumstances.',
                       'timestamp': 679,
                       'timestamp_seconds': 679,
                       'timestamp_label': '[00:11:19]',
                       'url': 'https://www.youtube.com/watch?v=uUBAmK-bcwg&t=679s',
                       'markdown': '[00:11:19](https://www.youtube.com/watch?v=uUBAmK-bcwg&t=679s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'OtQr6GmQzSY',
                       'title': "'No Surprises Act' meant to protect patients from surprise medical bills "
                                'takes effect Jan. 1',
                       'channel': 'WJHL',
                       'author': 'WJHL',
                       'text': 'It has always been our policy regardless of what the federal law is.',
                       'tip': 'It has always been our policy regardless of what the federal law is.',
                       'timestamp': 109,
                       'timestamp_seconds': 109,
                       'timestamp_label': '[00:01:49]',
                       'url': 'https://www.youtube.com/watch?v=OtQr6GmQzSY&t=109s',
                       'markdown': '[00:01:49](https://www.youtube.com/watch?v=OtQr6GmQzSY&t=109s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'M-sP3O4XgCs',
                       'title': 'Fully Insured and Non ERISA Plans  Advanced Topics in Preemption and Anti '
                                'Subrogation Exceptions',
                       'channel': 'Matthiesen, Wickert & Lehrer, S.C.',
                       'author': 'Matthiesen, Wickert & Lehrer, S.C.',
                       'text': "We see far too many claims just being abandoned because they're non-ERISA "
                               "or they're fully insured.",
                       'tip': "We see far too many claims just being abandoned because they're non-ERISA "
                              "or they're fully insured.",
                       'timestamp': 2553,
                       'timestamp_seconds': 2553,
                       'timestamp_label': '[00:42:33]',
                       'url': 'https://www.youtube.com/watch?v=M-sP3O4XgCs&t=2553s',
                       'markdown': '[00:42:33](https://www.youtube.com/watch?v=M-sP3O4XgCs&t=2553s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q3.'}]}
