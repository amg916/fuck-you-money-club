from __future__ import annotations

CHAPTER_9 = {'id': 'Q9',
 'chapter_id': 'Q9',
 'chapter_number': 9,
 'question_number': 9,
 'slug': 'superbills-oon-benefits-patient-submitted-reimbursement',
 'question_prompt': 'How do cash-pay and out-of-network practices use superbills, benefit verification, '
                    'and patient cost-sharing math to drive patient reimbursement?',
 'kicker': 'Q9 / THE BIG MONEY PLAYBOOKS',
 'title': 'Superbills and OON Benefits: Patient-Submitted Reimbursement for Cash Practices',
 'subtitle': 'Superbill required elements, cash-package superbills, EHR claim filing vs. superbills, '
             'patient claim forms, coinsurance plus balance billing, allowed amounts, FAIR Health cost '
             'estimates, client self-service benefit verification, eligibility checks, and copay, '
             'coinsurance, and deductible calculations',
 'layout_template': 'tool_resource_directory',
 'reading_time_minutes': 15,
 'executive_summary': 'Cash and out-of-network practitioners agree on a two-track model. Collect the full '
                      'fee at the visit. Then either hand over a superbill for patient self-claims, or '
                      'courtesy-bill the payer with assignment declined so reimbursement flows to the '
                      'patient. The working math is a separate out-of-network deductible, an allowed '
                      'amount often set below the fee, and a reimbursement rate commonly reported at 50 to '
                      '80 percent. Street mechanics include SimplePractice and Jane auto-generated '
                      'superbills, a single per-CPT fee schedule with line-item discounts for packages, '
                      'NPI-first payer calls, and embedded benefit checkers such as Reimbursify and '
                      'Mentaya at $29 a month. The practitioners split on quoting benefits. Jarod Carter '
                      'refuses to quote benefits to patients because the practice gets blamed when claims '
                      'deny. Alicia Murray and Reimbursify put real-time benefit checks directly on the '
                      'website to drive conversion.',
 'key_metrics': [{'label': 'Out-of-network full-charge billing vs self-pay rate',
                  'metric': 'Out-of-network full-charge billing vs self-pay rate',
                  'value': 'About $220 per visit billed out-of-network vs a self-pay rate of about $179',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A Carter coaching client sends full charges to a couple of popular payers '
                             'and gets the full amount back, beating their discounted self-pay rate.',
                  'source': 'Jarod Carter ([cA7tBJf4KyY @ 00:06:06])'},
                 {'label': 'Balance-billing patient responsibility',
                  'metric': 'Balance-billing patient responsibility',
                  'value': '$185 total ($35 coinsurance plus $150 balance bill)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'A $250 hourly charge against a $100 out-of-network allowed amount at 35 '
                             'percent coinsurance, with assignment not accepted.',
                  'source': 'The Private Practice Outsider ([TNKYk9V0ty8 @ 00:01:58])'},
                 {'label': 'Allowed amount on a real self-filed claim',
                  'metric': 'Allowed amount on a real self-filed claim',
                  'value': '$167 allowed on a $185 appointment',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'The Reimbursify host filed out-of-network claims for their own family on a '
                             'small-business plan and saw allowed amounts close to the charge.',
                  'source': 'Reimbursify ([of48SgwvfiI @ 00:06:50])'},
                 {'label': 'Website benefits checker cost',
                  'metric': 'Website benefits checker cost',
                  'value': '$29 per month after a free month',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Murray pays for the Mentaya benefits checker embedded on the practice fees '
                             'page, with a schedule-now button underneath.',
                  'source': 'Alicia Murray | The Therapist HQ \U0001faa9 ([eXrZnEwRRH4 @ 00:23:09])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every operator on this beat runs the same fork in the road. Jarod Carter '
                              'lays out two paths for any cash or out-of-network shop. The first is to '
                              'hand over a superbill at or after the visit and let the patient file '
                              'self-claims. The second is to bill the payer out-of-network on the '
                              "patient's behalf, a route most common in practices that dropped contracts "
                              'but kept a billing department [cA7tBJf4KyY @ 00:02:21]. Kym Tolson frames '
                              'the identical split as superbill versus courtesy billing. Tolson stresses '
                              'that either way the practice collects its full self-pay rate, and the '
                              "insurer's check lands with the client, not the clinician [FpNL1YIlvD0 @ "
                              '00:00:17]. Alicia Murray runs a fully virtual, fully private-pay group that '
                              'does complimentary billing. Murray calls the superbill route the very '
                              'low-lift option, where the clinician just sends the document and the client '
                              'carries the rest [eXrZnEwRRH4 @ 00:08:13]. Lisa at Craft Your Practice '
                              'compresses the doctrine into two rules. The client, not the practice, files '
                              'the claim. Any money that comes back goes to the client, because the '
                              'practice was already paid [tkUfu8WA56U @ 00:02:24]. The baseline '
                              'prerequisite is therefore cash in hand at the time of service. '
                              "Reimbursement is the patient's side transaction, not practice revenue.",
                              'The superbill itself is where consensus gets granular. Dr. Marie Fang of '
                              'Private Practice Skills lists the non-negotiables payers require to make '
                              "sure 'you are who you say you are': provider name, address and phone, tax "
                              'ID, NPI and license number. On the client side Fang lists name, birth date '
                              'and ICD-10 code, plus an itemized list with date of service, CPT code, '
                              'description and fee. Fang adds a place-of-service code, a paid-in-full '
                              'statement that this is not a bill, and a signature [HqCQhe8wbVM @ '
                              '00:03:11]. Lisa at Craft Your Practice warns that a missing field is the '
                              'most common reason a client submission bounces back. Lisa tells clinicians '
                              'to print an EIN instead of a Social Security number, and flags telehealth '
                              'place-of-service codes because plans do check [tkUfu8WA56U @ 00:05:12]. Dr. '
                              'Lauren Baker adds that a superbill without a paid column needs a separate '
                              'receipt proving payment before reimbursement happens [zsaby8gJNmg @ '
                              "00:04:43]. Jarod Carter's hard rule sits underneath all of it: one fee "
                              'schedule, with the same charge per CPT code for every patient. Mobile '
                              'visits get priced up through a convenience fee or travel surcharge rather '
                              'than inflated codes [cA7tBJf4KyY @ 00:07:01]. Patients may not like that '
                              'the surcharge goes unreimbursed. Carter calls that simply part of the '
                              'convenience being sold.',
                              'On the money, the practitioners converge on one sobering formula. Lisa at '
                              'Craft Your Practice explains that out-of-network benefits usually carry '
                              'their own deductible, often higher than the in-network one, and nothing '
                              'comes back until it is met. After that, the plan pays a percentage, '
                              'commonly fifty to seventy percent, of an allowed amount the plan sets, '
                              "often well below the fee. In Lisa's example, a $150 session with a $100 "
                              'allowed amount at sixty percent returns $60, for a real cost of $90 '
                              '[tkUfu8WA56U @ 00:03:58]. Jasmine at Inlera University defines the allowed '
                              "amount as the payer's fee schedule filtered through the patient's own "
                              'benefit plan. A service listed on the fee schedule still pays nothing if '
                              'the plan excludes it [3JOMCnMqhvI @ 00:01:27]. Nate Page reports clients '
                              'getting fifty percent, many getting sixty to eighty percent, and some '
                              'getting one hundred percent back. Page runs a 30 percent coinsurance '
                              'example where a $200 session nets $140 back and $60 out of pocket '
                              '[rdwGJdKffpI @ 00:04:16]. The Reimbursify office-hours host adds a '
                              'deductible detail. The same dollars apply to both the individual and family '
                              'out-of-network deductibles, and benefits kick in once either one is met '
                              '[of48SgwvfiI @ 00:01:10].'],
               'table': {'caption': 'Where cash and out-of-network practitioners line up on superbill '
                                    'fundamentals',
                         'headers': ['Consensus Point',
                                     'Operator Practice',
                                     'Why It Holds',
                                     'Expert Source'],
                         'rows': [['Two billing paths exist for every cash practice',
                                   'Hand over a superbill for self-claims or bill the payer out-of-network '
                                   "on the patient's behalf",
                                   'The superbill route carries the lowest administrative burden for '
                                   'cash-based shops',
                                   'Jarod Carter ([cA7tBJf4KyY @ 00:02:21])'],
                                  ['Full fee is collected at the time of service',
                                   'Collect the full self-pay rate whether issuing a superbill or a '
                                   'courtesy claim',
                                   'The practice has nothing to do with what the insurer later reimburses',
                                   'Kym Tolson The Traveling Therapist ([FpNL1YIlvD0 @ 00:00:35])'],
                                  ['Reimbursement checks must go to the client',
                                   'Decline assignment and leave the remit-payment-to-provider box blank '
                                   'on out-of-network claims',
                                   'The client already paid in full, so the insurer check belongs to them',
                                   'Alicia Murray | The Therapist HQ \U0001faa9 ([eXrZnEwRRH4 @ '
                                   '00:09:14])'],
                                  ['Superbill fields must be complete and identifying',
                                   'Include tax ID, NPI, license, ICD-10, CPT, place of service, fees and '
                                   'signature',
                                   'Payers demand identity details on every superbill to screen out '
                                   'potential insurance fraud',
                                   'Private Practice Skills ([HqCQhe8wbVM @ 00:03:11])'],
                                  ['One fee schedule governs every superbill issued',
                                   'Keep the same charge per CPT code for every patient, clinic or mobile',
                                   'Mobile premiums belong in a separate convenience or travel surcharge '
                                   'line instead',
                                   'Jarod Carter ([cA7tBJf4KyY @ 00:07:01])'],
                                  ['The out-of-network deductible gates every dollar back',
                                   'Treat the out-of-network deductible as separate, often higher, and '
                                   'payable first',
                                   'Until it is met, the real session cost equals the full fee charged',
                                   'Craft Your Practice ([tkUfu8WA56U @ 00:03:09])'],
                                  ['The allowed amount differs from the payer fee schedule',
                                   'Read the allowed amount as the fee schedule combined with the '
                                   "patient's benefit plan",
                                   'Services the plan excludes return nothing even when a fee schedule '
                                   'lists them',
                                   'Inlera University ([3JOMCnMqhvI @ 00:01:27])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["The software mechanics are click-level. Kym Tolson's SimplePractice "
                              'walkthrough starts in the client record. Set billing to self-pay rather '
                              'than insurance, then add only the payer and member ID. Open the other CMS '
                              'claim fields and set accept assignment to No, so the insurer pays the '
                              'client. For superbills, pick a date range and hit create superbill. The '
                              'statement auto-fills provider NPI, license and tax ID, dates of service, a '
                              'GT modifier on telehealth lines, diagnosis and charges, totaling $540 in '
                              "the demo [FpNL1YIlvD0 @ 00:01:57]. Alicia Murray's Jane setup "
                              'auto-populates a superbill after every appointment, and it takes one or two '
                              'clicks to email it [eXrZnEwRRH4 @ 00:06:50]. Dr. Lauren Baker walks the '
                              'patient side of a Humana claims form. Carry over CPT 97162 for the '
                              'evaluation and 97530 with the GP modifier in 15-minute units. Use place of '
                              'service 11 roughly 99 percent of the time. Baker charges $30 a unit, or '
                              '$120 an hour. Baker says to leave the assignment box unsigned so the check '
                              'goes to the patient, expect 20 to 60 days, and call around day 30 to 45 '
                              '[zsaby8gJNmg @ 00:11:49]. Baker also insists on giving payers the NPI, not '
                              'the EIN. Payers never locate Baker by tax ID but find the NPI instantly '
                              '[zsaby8gJNmg @ 00:13:48].',
                              'Package superbills are where Jarod Carter gets surgical. A purchase receipt '
                              'cannot serve as a superbill, because nothing can be submitted for visits '
                              'that have not happened yet. Every date of service gets its own entry. '
                              "Carter's example is a $200 hour sold at $10 off per session in a 10-pack. "
                              'The units still add up to the full rate, and a line-item package discount '
                              'drops each visit to $190. Alternatively, one bottom-line discount, such as '
                              '$10 times six dates for $60, does the same job. Carter warns that letting a '
                              'patient submit $200 when they paid $190 would be insurance fraud '
                              "[heiuukmxgss @ 00:04:02]. Carter's own shop charges $195 for 60 minutes and "
                              '$125 for 30. The four hour units still total $250 on paper, and a full-hour '
                              'session discount brings the line down to $195. Package buyers get a second, '
                              'stacked package discount line [heiuukmxgss @ 00:06:33]. On collection, '
                              'Carter pulls the card on file through online intake and refuses to split '
                              'packages under four figures into payments. Payment plans must clear within '
                              'six months of likely discharge [cA7tBJf4KyY @ 00:10:57]. One80 Physical '
                              'Therapy also pairs discounted punch passes with payment plans, so patients '
                              'do not pay the whole pass upfront [GVdiKSs4kvU @ 00:02:24].',
                              'Benefit checks are increasingly self-serve. The Reimbursify host pushes '
                              "clinicians to 'liberate yourself' from running verifications. The fix is a "
                              'web-app button or unique link that lets prospects submit their name, '
                              'contact and insurance details. The result drops into the practice portal as '
                              'an unread message. The host cites a personal claim where a $185 appointment '
                              'drew a $167 allowed amount. Across plans, the host puts allowed amounts at '
                              'roughly 60 or 70 percent of charges up to 100 percent [of48SgwvfiI @ '
                              "00:13:26]. Alicia Murray embeds Mentaya's checker on the fees page at $29 a "
                              'month after a free month, with a schedule-now button directly beneath it. '
                              'Murray notes that Mentaya and Thrizer can submit and rectify claims at no '
                              "cost to the therapist, because the fee comes out of the client's claim "
                              '[eXrZnEwRRH4 @ 00:23:09]. For practices that bill out-of-network without '
                              'accepting assignment, The Private Practice Outsider runs the '
                              'balance-billing math. A $250 charge against a $100 allowed amount at 35 '
                              'percent coinsurance leaves the patient owing $35. Add the $150 balance '
                              'bill, and the total is $185. Alternatively, the practice can take the $100 '
                              'allowed amount as payment in full, collecting $35 from the patient and $65 '
                              'from the payer [TNKYk9V0ty8 @ 00:01:58].'],
               'table': {'caption': 'Settings, codes and dollar figures practitioners run on live '
                                    'superbill and out-of-network workflows',
                         'headers': ['Mechanic',
                                     'Exact Setting or Number',
                                     'Execution Detail',
                                     'Expert Source'],
                         'rows': [['SimplePractice courtesy out-of-network claim setup',
                                   'Accept assignment set to No inside the other CMS claim fields',
                                   'Client marked self-pay with only the payer and member ID entered',
                                   'Kym Tolson The Traveling Therapist ([FpNL1YIlvD0 @ 00:02:12])'],
                                  ['Physical therapy claim coding on the form',
                                   '97162 evaluation, 97530 with GP modifier, charged at $30 per unit',
                                   'Place of service 11 is used on roughly 99 percent of claims',
                                   'Dr. Lauren Baker ([zsaby8gJNmg @ 00:10:19])'],
                                  ['Mailed claim follow-up cadence and tracking',
                                   'Payer processing typically takes 20 to 60 days before checks mail',
                                   'Copy everything, log the mail date, then call near day 30 to 45',
                                   'Dr. Lauren Baker ([zsaby8gJNmg @ 00:16:08])'],
                                  ['Package discount shown as a separate line item',
                                   '$200 full hour minus a $10 ten-pack discount bills $190',
                                   'CPT units total the full rate before the discount line subtracts',
                                   'Jarod Carter ([heiuukmxgss @ 00:04:46])'],
                                  ['Half-hour versus full-hour pricing on superbills',
                                   'Four units total $250, then full-hour discount down to $195',
                                   'Thirty-minute sessions bill two units at the same per-code $125',
                                   'Jarod Carter ([heiuukmxgss @ 00:06:33])'],
                                  ['Embedded website benefits checker for conversion',
                                   'Mentaya checker runs $29 per month after one free month',
                                   'Schedule-now button sits directly beneath the embedded benefits widget',
                                   'Alicia Murray | The Therapist HQ \U0001faa9 ([eXrZnEwRRH4 @ '
                                   '00:23:09])'],
                                  ['Balance billing when assignment is not accepted',
                                   '$250 charge, $100 allowed, 35 percent coinsurance yields $185 owed',
                                   'Alternatively accept the $100 allowed amount as full payment instead',
                                   'The Private Practice Outsider ([TNKYk9V0ty8 @ 00:01:58])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Small superbill moves that keep reimbursement flowing',
                           'body': 'Field-tested details from practitioners who submit, chase and price '
                                   'out-of-network claims every week.',
                           'items': ['Give payers the NPI first, not just the EIN: Baker says insurers '
                                     'never locate an out-of-network provider by tax ID but find the NPI '
                                     'immediately, and a dropped NPI is the usual reason a claim stalls '
                                     '[Dr. Lauren Baker — zsaby8gJNmg @ 00:13:48]',
                                     "In Murray's experience, an adjustment disorder on its own does not "
                                     'get reimbursed out-of-network, so a secondary diagnosis is needed. A '
                                     'payer asking for a W-9 on a first out-of-network claim is routine '
                                     'admin, not a trap [Alicia Murray | The Therapist HQ \U0001faa9 — '
                                     'eXrZnEwRRH4 @ 00:26:08]',
                                     'Plans can cap member submission windows at as little as ninety days, '
                                     'so issue superbills monthly or have the software send them '
                                     'automatically rather than letting clients hoard six months of '
                                     'paperwork [Craft Your Practice — tkUfu8WA56U @ 00:09:32]',
                                     'Before dropping a contract, check what that payer actually pays '
                                     'out-of-network: a Carter coaching client collects about $220 a visit '
                                     'billing full charges, against a self-pay rate of about $179 [Jarod '
                                     'Carter — cA7tBJf4KyY @ 00:05:52]']},
               'sop_steps': [{'step': 1,
                              'title': 'Front-load the benefit questions',
                              'action': 'Put the four insurer questions into the intake email or a short '
                                        'handout before the first session.',
                              'detail': 'Clients should ask four things. Do I have out-of-network '
                                        'benefits? What is my out-of-network deductible, and how much is '
                                        'met? What percentage of which allowed amount do you reimburse? '
                                        'How do I submit, and is there a deadline? Then run the arithmetic '
                                        'with the client once [Craft Your Practice — tkUfu8WA56U @ '
                                        '00:07:08]'},
                             {'step': 2,
                              'title': 'Capture the card on file at intake',
                              'action': 'Build a card-on-file page into the online intake paperwork and '
                                        'charge after the session ends.',
                              'detail': 'Carter avoids ending the hour with a painful card swipe. Staff '
                                        'tell the patient the admin will bill the card on file at the end '
                                        'of the day, and the card is collected through the intake link '
                                        '[Jarod Carter — cA7tBJf4KyY @ 00:10:00]'},
                             {'step': 3,
                              'title': 'Configure the EHR for out-of-network output',
                              'action': 'Set the client to self-pay, add the payer and member ID, and set '
                                        'accept assignment to No.',
                              'detail': 'With assignment set to No, the payer sends the money to the '
                                        'client. Use the date-range create-superbill function to auto-fill '
                                        'NPI, license, tax ID, codes, modifiers and charges [Kym Tolson '
                                        'The Traveling Therapist — FpNL1YIlvD0 @ 00:01:23]'},
                             {'step': 4,
                              'title': 'Line-item every discount against full CPT charges',
                              'action': 'Keep per-CPT charges identical on every superbill and subtract '
                                        'package or session discounts as separate lines.',
                              'detail': 'Use a per-date-of-service discount line, or one bottom-line '
                                        'discount multiplied by the number of dates. The total must match '
                                        'what the patient actually paid [Jarod Carter — heiuukmxgss @ '
                                        '00:04:32]'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The first split is who files. Jarod Carter calls the superbill handoff the '
                              'lowest administrative burden path and runs a cash practice that way, but '
                              'Carter also teaches that some payers in some regions make out-of-network '
                              'billing far more lucrative: one coaching client with a roughly $179 '
                              'self-pay rate sends the full undiscounted bill and collects about $220 a '
                              'visit [cA7tBJf4KyY @ 00:02:21] [cA7tBJf4KyY @ 00:06:06]. Kym Tolson '
                              'recommends the superbill route because it is easier on the provider, and '
                              'when courtesy-filing in SimplePractice, Tolson marks accept assignment as '
                              'no so the check goes to the client while the practice still collects the '
                              'full self-pay rate [FpNL1YIlvD0 @ 00:02:42]. Alicia Murray runs the '
                              'opposite playbook across a fully out-of-network virtual group practice: '
                              'complimentary billing, which Murray credits for visible gains in retention '
                              'and conversion over superbills alone, at the cost of storing insurance '
                              "cards, driver's licenses and policyholder birth dates, and eventually "
                              'hiring a biller once claim volume exceeded what Murray could personally '
                              'handle [eXrZnEwRRH4 @ 00:04:40] [eXrZnEwRRH4 @ 00:11:48]. The operator call '
                              "is money versus admin: Carter's test is whether you already have a billing "
                              "department, and Murray's is whether your bandwidth can absorb rework.",
                              'The sharpest disagreement is whether the practice should quote benefits at '
                              'all. Jarod Carter uses Reimbursify to pull out-of-network benefits quickly, '
                              'yet tells superbill-only practices not to look them up for patients, '
                              'because insurers deny claims they should pay, and when a promised 60 '
                              'percent never arrives, the bad taste lands on your practice even with a '
                              'signed acknowledgment; Carter hands prospects a question list instead '
                              '[cA7tBJf4KyY @ 00:04:19] [cA7tBJf4KyY @ 00:05:00]. Reimbursify pushes the '
                              'other way: put its web app in the corner of your website, let visitors '
                              'submit their own name, phone, email and insurance, then share the result '
                              'with one click and stop running verifications yourself [of48SgwvfiI @ '
                              '00:13:26]. Alicia Murray embeds a Mentaya checker on the practice fees page '
                              'showing deductible, amount met and reimbursement percentage, with a '
                              'schedule-now button directly under it to strike while the iron is hot, at '
                              '$29 a month after a free month [eXrZnEwRRH4 @ 00:14:29] [eXrZnEwRRH4 @ '
                              '00:23:09]. Lisa of Craft Your Practice sits between the camps: script four '
                              'questions about benefits, deductible, percentage of allowed amount, and '
                              'submission deadline into the intake email, then do the arithmetic with the '
                              'client once they report back [tkUfu8WA56U @ 00:07:08].',
                              "Packaging and pricing split the room too. Jarod Carter's general rule is "
                              'that a package under four figures is not split into payments, because the '
                              'prepay discount exists to buy cash flow and spreading it out just hands '
                              'away the discount for nothing; Carter would not argue against two or three '
                              'monthly payments on two, five or ten thousand dollar packages [cA7tBJf4KyY '
                              '@ 00:10:57]. One80 Physical Therapy goes the other way, offering payment '
                              'plans on its punch passes so patients do not pay it all upfront, and '
                              'pitches the pass as roughly equal to in-network costs before a deductible '
                              'is hit, delivered in a fraction of the visits [GVdiKSs4kvU @ 00:02:24] '
                              '[GVdiKSs4kvU @ 00:03:19]. On rate design, Carter insists on one per-CPT fee '
                              'schedule for every patient, so mobile visits carry a separate convenience '
                              'or travel surcharge rather than inflated code charges, while Dr. Lauren '
                              'Baker simply prices every unit at $30, or $120 per 60 minutes, regardless '
                              'of which code is billed [cA7tBJf4KyY @ 00:07:18] [zsaby8gJNmg @ 00:06:36]. '
                              "Nate Page adds a sequencing rule Page's practice follows: always check "
                              'health insurance benefits first, and only then explore sliding scale, with '
                              'clinicians holding roughly 10 percent sliding scale or pro bono until their '
                              'student loans are paid [rdwGJdKffpI @ 00:06:41] [rdwGJdKffpI @ 00:06:58].'],
               'table': {'caption': 'Competing out-of-network playbooks for cash and hybrid practices',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Who files the out-of-network claim with the payer',
                                   'Hand over a superbill and let the patient self-submit, the lowest '
                                   'admin burden path',
                                   'Courtesy-file in SimplePractice with accept assignment set to no so '
                                   'payment reaches the client',
                                   'Kym Tolson The Traveling Therapist ([FpNL1YIlvD0 @ 00:00:17]); Jarod '
                                   'Carter ([cA7tBJf4KyY @ 00:02:21])'],
                                  ['Whether the practice looks up patient out-of-network benefits',
                                   'Do not quote benefits; give prospects a question list to ask their own '
                                   'insurer',
                                   'Embed a self-serve benefits checker on the website and share results '
                                   'with one click',
                                   'Jarod Carter ([cA7tBJf4KyY @ 00:05:12]); Reimbursify ([of48SgwvfiI @ '
                                   '00:13:26])'],
                                  ['Billing on behalf of patients versus collecting a discounted self-pay '
                                   'rate',
                                   'Collect the discounted self-pay rate of about $179 and hand over a '
                                   'superbill',
                                   'Send the full undiscounted bill out-of-network and collect about $220 '
                                   'per visit',
                                   'Jarod Carter ([cA7tBJf4KyY @ 00:08:40])'],
                                  ['Splitting prepaid package payments into monthly installments',
                                   'Packages under four figures are paid upfront because the discount '
                                   'exists to buy cash flow',
                                   'Punch passes come with payment plans so patients avoid paying '
                                   'everything upfront',
                                   'Jarod Carter ([cA7tBJf4KyY @ 00:11:11]); One80 Physical Therapy '
                                   '([GVdiKSs4kvU @ 00:02:24])'],
                                  ['Handling claim problems after the paperwork leaves the practice',
                                   'Superbill-only clinician is finished once the document is handed to '
                                   'the client',
                                   'Practice helps rectify problems and asks clients to forward odd '
                                   'letters or stalled checks',
                                   'Private Practice Skills ([HqCQhe8wbVM @ 00:04:33]); Alicia Murray | '
                                   'The Therapist HQ \U0001faa9 ([eXrZnEwRRH4 @ 00:10:39])'],
                                  ['Who carries the complimentary billing workload day to day',
                                   'Solo clinicians file their own claims with a solid EHR at lower claim '
                                   'volume',
                                   'Hire a biller or use Mentaya or Thrizer, with the cost coming out of '
                                   'the client claim',
                                   'Alicia Murray | The Therapist HQ \U0001faa9 ([eXrZnEwRRH4 @ 00:13:08] '
                                   '[eXrZnEwRRH4 @ 00:23:43])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The costliest blowup practitioners report is an expectation gap, not a '
                              'paperwork gap. Lisa at Craft Your Practice describes the pattern: providers '
                              'guess hopeful, then three months later the client opens a letter with a '
                              'number far smaller than expected, or zero, and the disappointment lands on '
                              "the therapist. Lisa's math: a $150 fee, a $100 plan-set allowed amount and "
                              'a 60 percent benefit returns $60, so the real cost is $90, and before the '
                              'separate, often higher out-of-network deductible is met it is the full $150 '
                              "[tkUfu8WA56U @ 00:00:54] [tkUfu8WA56U @ 00:03:58]. Reimbursify's "
                              'verification lead reports allowed amounts ranging from about 60 or 70 '
                              "percent of the local charge up to 100 percent, citing the presenter's own "
                              '$185 appointment that allowed $167, with large self-insured employers such '
                              'as universities, Apple, Google or NYU tending toward healthier allowances '
                              '[of48SgwvfiI @ 00:07:12]. The Private Practice Outsider shows how the gap '
                              'gets billed when assignment is not accepted: a $250 charge against a $100 '
                              'allowed amount leaves a $150 balance bill plus 35 percent coinsurance, so '
                              'the patient owes $185; accept the allowed amount as payment in full and you '
                              'collect $100 total, $35 from the patient and $65 from the payer '
                              '[TNKYk9V0ty8 @ 00:01:58] [TNKYk9V0ty8 @ 00:02:21].',
                              'Paperwork kickbacks have specific, repeatable causes. Lisa flags a missing '
                              'field as the most common reason a client submission bounces, and warns that '
                              'telehealth place-of-service codes differ from the office code and plans do '
                              "check [tkUfu8WA56U @ 00:04:45] [tkUfu8WA56U @ 00:05:35]. Jarod Carter's "
                              'package trap: an upfront purchase receipt cannot be submitted, because '
                              'nothing can be claimed before it occurs, and a superbill saying $200 when '
                              'the patient paid $190 would be insurance fraud; list full per-unit charges, '
                              "then subtract a line-item package discount, and in Carter's practice a full "
                              'hour shows $250 in codes, a full-hour discount down to $195, then a second '
                              '10-pack discount [heiuukmxgss @ 00:04:02] [heiuukmxgss @ 00:07:05]. Dr. '
                              'Lauren Baker reports insurers scan the claim form but sometimes not the '
                              'attachments, so write details out rather than relying on see-attached; '
                              'insurers phone the provider as a fraud check; and whenever Baker gives the '
                              'EIN, insurers cannot locate the provider, but the NPI works instantly. '
                              "Baker's other trap: signing the payment-to-provider box sends a check meant "
                              'for the family to the provider [zsaby8gJNmg @ 00:09:39] [zsaby8gJNmg @ '
                              '00:13:48]. Alicia Murray adds that adjustment disorders alone have not been '
                              'reimbursed on any plan Murray has come across [eXrZnEwRRH4 @ 00:26:08].',
                              'Cash and time leaks come from deadlines, follow-up and expired cards. Lisa '
                              'warns that plans give members a submission window sometimes as short as '
                              'ninety days, so a client who hoards six months of superbills can lose some '
                              'of them; issuing superbills monthly or auto-sending them from software '
                              "removes that risk [tkUfu8WA56U @ 00:09:32]. Dr. Lauren Baker's family-side "
                              'workflow assumes 20 to 60 days of processing: copy everything, keep a '
                              'folder with a sticky note showing the mail date, and call around day 30 or '
                              '45, because a provider NPI that was submitted but never carried forward '
                              'happens all the time [zsaby8gJNmg @ 00:16:08] [zsaby8gJNmg @ 00:17:00]. '
                              "Jarod Carter's collections bottleneck is the card on file: losses come "
                              'mainly from cards expiring and not being updated, so skip payment plans '
                              'when the balance cannot be finished within six months of likely discharge, '
                              'though Carter says the yeses won from offering plans far outweigh those '
                              'rare losses [cA7tBJf4KyY @ 00:12:35] [cA7tBJf4KyY @ 00:13:02]. Inlera '
                              'University ranks phoning a live insurance rep dead last among five '
                              'verification methods because hold times have kept growing, and tells '
                              'billers to warn patients that any quote of benefits is only an estimate '
                              'until the claim actually processes [XyBNgMnFz0Y @ 00:06:58] [XyBNgMnFz0Y @ '
                              '00:07:30].'],
               'table': {'caption': 'Firsthand out-of-network failure modes and the fixes practitioners '
                                    'use',
                         'headers': ['Failure Mode',
                                     'What Happened Or Was Measured',
                                     'Operator Fix Taught',
                                     'Expert Source'],
                         'rows': [['Hopeful guesses about what the plan will reimburse',
                                   'Client opens a letter months later showing a much smaller number or '
                                   'zero',
                                   'Hand over the four insurer questions and run the arithmetic before '
                                   'session one',
                                   'Craft Your Practice ([tkUfu8WA56U @ 00:00:54])'],
                                  ['Practice quotes benefits that the insurer later refuses to pay',
                                   'Patient blames the practice even after signing an acknowledgment of '
                                   'responsibility',
                                   'Superbill-only practices give insurer questions instead of quoting '
                                   'benefit levels',
                                   'Jarod Carter ([cA7tBJf4KyY @ 00:04:49])'],
                                  ['Upfront package receipt submitted as if it were a superbill',
                                   'Receipt for a purchase covers dates that have not occurred and cannot '
                                   'be claimed',
                                   'Issue per-date superbills with full CPT charges and line-item package '
                                   'discounts',
                                   'Jarod Carter ([heiuukmxgss @ 00:01:29])'],
                                  ['Clients hoard months of superbills before submitting anything',
                                   'Submission windows can be as short as ninety days so some claims are '
                                   'lost',
                                   'Send superbills monthly or set the practice software to send them '
                                   'automatically',
                                   'Craft Your Practice ([tkUfu8WA56U @ 00:09:32])'],
                                  ['Attached superbill documents vanish during insurer scanning',
                                   'Insurers scan the claim form but sometimes skip the attached '
                                   'supporting documents',
                                   'Carry codes and dates onto the form itself and keep copies with mail '
                                   'dates',
                                   'Dr. Lauren Baker ([zsaby8gJNmg @ 00:09:39])'],
                                  ['Adjustment disorder listed as the only diagnosis code',
                                   'Murray has not come across a plan reimbursing it on out-of-network '
                                   'claims',
                                   'Diagnose a secondary condition and explain the clinical interpretation '
                                   'to the client',
                                   'Alicia Murray | The Therapist HQ \U0001faa9 ([eXrZnEwRRH4 @ '
                                   '00:26:23])'],
                                  ['Medicare patients expecting a superbill from a non-participating '
                                   'clinic',
                                   'Non-participating providers cannot give Medicare patients a superbill '
                                   'to submit',
                                   'Position monthly or six-week cash tune-up visits for prevention and '
                                   'fall work',
                                   'One80 Physical Therapy ([GVdiKSs4kvU @ 00:04:02])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Checks Before The First Superbill Goes Out',
                           'body': 'Every item below comes from a kickback, a lost reimbursement, or a '
                                   'misdirected check that practitioners hit firsthand. Run them once '
                                   'against a test superbill and your intake paperwork before the next new '
                                   'client starts.',
                           'items': ['Confirm the superbill carries name and credentials, individual NPI, '
                                     'license number, tax ID or EIN, CPT, place-of-service and diagnosis '
                                     'codes, fee and amount paid, because a missing field is what bounces '
                                     'submissions [Craft Your Practice — tkUfu8WA56U @ 00:05:12].',
                                     'Confirm per-CPT charges are identical for every patient and session '
                                     'length, with package and full-hour pricing handled through line-item '
                                     'discounts that match what the patient actually paid [Jarod Carter — '
                                     'heiuukmxgss @ 00:07:34].',
                                     'Confirm the client knows a diagnosis code goes on the superbill and '
                                     'to the plan before the first one is handed over, so the choice to '
                                     'submit is theirs [Craft Your Practice — tkUfu8WA56U @ 00:08:22].',
                                     'If courtesy billing, confirm accept assignment is not checked and '
                                     'the remit-payment box is left blank so the reimbursement check goes '
                                     'directly to the client [Alicia Murray | The Therapist HQ \U0001faa9 '
                                     '— eXrZnEwRRH4 @ 00:09:00].']}}],
 'pull_quote': '"The form is the easy part. The real work is the expectation... clear and early beats '
               'hopeful every time." — Craft Your Practice (tkUfu8WA56U @ 00:10:43)',
 'diagram_id': 'diag-05',
 'action_checklist': ['Put the four insurer questions on benefits, deductible met, reimbursement '
                      'percentage of allowed amount, and submission deadline into the intake email or a '
                      'short handout [Craft Your Practice — tkUfu8WA56U @ 00:07:33].',
                      'Collect a card on file through the online intake paperwork and have the admin bill '
                      'it at end of day instead of ending the session with a card swipe [Jarod Carter — '
                      'cA7tBJf4KyY @ 00:10:00].',
                      'For courtesy claims in SimplePractice, set the client to self-pay, add the payer '
                      'and member ID, and set accept assignment to no in the CMS claim fields [Kym Tolson '
                      'The Traveling Therapist — FpNL1YIlvD0 @ 00:01:57].',
                      'Embed a benefits checker on the fees page and place a schedule-now button directly '
                      'underneath it to book clients while the reimbursement numbers are in front of them '
                      '[Alicia Murray | The Therapist HQ \U0001faa9 — eXrZnEwRRH4 @ 00:16:08].',
                      'Add the place-of-service code and a clear statement that the client has paid in '
                      'full and the document is not a bill, then sign and date each superbill [Private '
                      'Practice Skills — HqCQhe8wbVM @ 00:04:03].',
                      'Before dropping contracts, check what each payer actually pays on average for '
                      'out-of-network services and bill on behalf of patients where full charges beat the '
                      'self-pay rate [Jarod Carter — cA7tBJf4KyY @ 00:05:52].'],
 'statutory_citations': [{'title': 'Jarod Carter — Top 4 Out-of-Network Billing & Superbill Tips '
                                   '[00:06:06]',
                          'url': 'https://www.youtube.com/watch?v=cA7tBJf4KyY&t=366s',
                          'relevance': 'Primary practitioner testimony on billing out-of-network at full '
                                       'charges for about $220 a visit versus a $179 self-pay rate.'},
                         {'title': 'Craft Your Practice — Superbills for Therapists: How Out-of-Network '
                                   'Reimbursement Actually Works [00:03:36]',
                          'url': 'https://www.youtube.com/watch?v=tkUfu8WA56U&t=216s',
                          'relevance': 'Primary practitioner testimony on allowed-amount math that turns a '
                                       '$150 fee into $60 back and a $90 real cost.'},
                         {'title': 'The Private Practice Outsider — Out of Network Billing [Coinsurance '
                                   'plus Balance Billing] Amount Explained [00:01:39]',
                          'url': 'https://www.youtube.com/watch?v=TNKYk9V0ty8&t=99s',
                          'relevance': 'Primary practitioner testimony on coinsurance plus balance billing '
                                       'when assignment is not accepted.'},
                         {'title': 'Jarod Carter — Superbill Secrets for Cash Practice Packages - '
                                   'Out-of-Network Billing Reimbursement Tips [00:04:02]',
                          'url': 'https://www.youtube.com/watch?v=heiuukmxgss&t=242s',
                          'relevance': 'Primary practitioner testimony on line-item package discounts and '
                                       'matching superbills to amounts actually paid.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'cA7tBJf4KyY',
                       'title': 'Top 4 Out-of-Network Billing & Superbill Tips',
                       'channel': 'Jarod Carter',
                       'author': 'Jarod Carter',
                       'text': 'One of my coaching clients has a self-pay rate of about 179, and there are '
                               'a couple of popular payers that pay over two hundred dollars for actual '
                               'charges, coming out to about 220 dollars a visit.',
                       'tip': 'One of my coaching clients has a self-pay rate of about 179, and there are '
                              'a couple of popular payers that pay over two hundred dollars for actual '
                              'charges, coming out to about 220 dollars a visit.',
                       'timestamp': 366,
                       'timestamp_seconds': 366,
                       'timestamp_label': '[00:06:06]',
                       'url': 'https://www.youtube.com/watch?v=cA7tBJf4KyY&t=366s',
                       'markdown': '[00:06:06](https://www.youtube.com/watch?v=cA7tBJf4KyY&t=366s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cA7tBJf4KyY',
                       'title': 'Top 4 Out-of-Network Billing & Superbill Tips',
                       'channel': 'Jarod Carter',
                       'author': 'Jarod Carter',
                       'text': 'As a general rule, if the package is less than four figures in cost, then '
                               'I do not split those up into payments.',
                       'tip': 'As a general rule, if the package is less than four figures in cost, then I '
                              'do not split those up into payments.',
                       'timestamp': 657,
                       'timestamp_seconds': 657,
                       'timestamp_label': '[00:10:57]',
                       'url': 'https://www.youtube.com/watch?v=cA7tBJf4KyY&t=657s',
                       'markdown': '[00:10:57](https://www.youtube.com/watch?v=cA7tBJf4KyY&t=657s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '3JOMCnMqhvI',
                       'title': 'What is the Allowed Amount? | Healthcare Medical Billing',
                       'channel': 'Inlera University',
                       'author': 'Inlera University',
                       'text': "It takes a combination of the patient's benefit plan along with the "
                               "insurance company's fee schedule, and that is what makes the allowed "
                               'amount, so the allowed amount is not the same thing as a fee schedule.',
                       'tip': "It takes a combination of the patient's benefit plan along with the "
                              "insurance company's fee schedule, and that is what makes the allowed "
                              'amount, so the allowed amount is not the same thing as a fee schedule.',
                       'timestamp': 87,
                       'timestamp_seconds': 87,
                       'timestamp_label': '[00:01:27]',
                       'url': 'https://www.youtube.com/watch?v=3JOMCnMqhvI&t=87s',
                       'markdown': '[00:01:27](https://www.youtube.com/watch?v=3JOMCnMqhvI&t=87s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'FpNL1YIlvD0',
                       'title': 'Out Of Network Billing Via Filing Claims Through an EHR and a Superbill',
                       'channel': 'Kym Tolson The Traveling Therapist',
                       'author': 'Kym Tolson The Traveling Therapist',
                       'text': 'If you select no on accept assignment, they are not going to send the '
                               'money to you; they are going to send the money to the client.',
                       'tip': 'If you select no on accept assignment, they are not going to send the money '
                              'to you; they are going to send the money to the client.',
                       'timestamp': 132,
                       'timestamp_seconds': 132,
                       'timestamp_label': '[00:02:12]',
                       'url': 'https://www.youtube.com/watch?v=FpNL1YIlvD0&t=132s',
                       'markdown': '[00:02:12](https://www.youtube.com/watch?v=FpNL1YIlvD0&t=132s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'WuZrwo-Qxww',
                       'title': 'Understand Your Medical Cost Estimate — FAIRHealthConsumer.org (Part 1)',
                       'channel': 'FAIR Health',
                       'author': 'FAIR Health',
                       'text': 'You can use your estimate to manage your deductible, negotiate costs with '
                               'your providers, or appeal a payment from your insurer.',
                       'tip': 'You can use your estimate to manage your deductible, negotiate costs with '
                              'your providers, or appeal a payment from your insurer.',
                       'timestamp': 133,
                       'timestamp_seconds': 133,
                       'timestamp_label': '[00:02:13]',
                       'url': 'https://www.youtube.com/watch?v=WuZrwo-Qxww&t=133s',
                       'markdown': '[00:02:13](https://www.youtube.com/watch?v=WuZrwo-Qxww&t=133s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'of48SgwvfiI',
                       'title': 'Benefit Verifications 101 - Let your clients check their own '
                                'out-of-network coverage!',
                       'channel': 'Reimbursify',
                       'author': 'Reimbursify',
                       'text': 'The amounts can range between maybe 60 or 70 percent of what someone is '
                               'charging up to 100 percent of what they are charging.',
                       'tip': 'The amounts can range between maybe 60 or 70 percent of what someone is '
                              'charging up to 100 percent of what they are charging.',
                       'timestamp': 410,
                       'timestamp_seconds': 410,
                       'timestamp_label': '[00:06:50]',
                       'url': 'https://www.youtube.com/watch?v=of48SgwvfiI&t=410s',
                       'markdown': '[00:06:50](https://www.youtube.com/watch?v=of48SgwvfiI&t=410s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zsaby8gJNmg',
                       'title': 'How To Fill Out A Claims Form For Out of Network Reimbursement | PT Out '
                                'of Network Claim',
                       'channel': 'Dr. Lauren Baker',
                       'author': 'Dr. Lauren Baker',
                       'text': 'As an out-of-network provider you are absolutely going to want to have the '
                               'NPI number, because they are never able to locate me by tax ID number, but '
                               'with my NPI number they find me right away.',
                       'tip': 'As an out-of-network provider you are absolutely going to want to have the '
                              'NPI number, because they are never able to locate me by tax ID number, but '
                              'with my NPI number they find me right away.',
                       'timestamp': 828,
                       'timestamp_seconds': 828,
                       'timestamp_label': '[00:13:48]',
                       'url': 'https://www.youtube.com/watch?v=zsaby8gJNmg&t=828s',
                       'markdown': '[00:13:48](https://www.youtube.com/watch?v=zsaby8gJNmg&t=828s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'TNKYk9V0ty8',
                       'title': 'Out of Network Billing [Coinsurance plus Balance Billing] Amount '
                                'Explained',
                       'channel': 'The Private Practice Outsider',
                       'author': 'The Private Practice Outsider',
                       'text': 'The patient will owe you 35 percent of the 100, which is 35 dollars, plus '
                               'the balance bill amount of 150 dollars, so 185 dollars total.',
                       'tip': 'The patient will owe you 35 percent of the 100, which is 35 dollars, plus '
                              'the balance bill amount of 150 dollars, so 185 dollars total.',
                       'timestamp': 118,
                       'timestamp_seconds': 118,
                       'timestamp_label': '[00:01:58]',
                       'url': 'https://www.youtube.com/watch?v=TNKYk9V0ty8&t=118s',
                       'markdown': '[00:01:58](https://www.youtube.com/watch?v=TNKYk9V0ty8&t=118s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'rdwGJdKffpI',
                       'title': 'Out of Network Therapist | Superbills and Health Insurance',
                       'channel': 'Nate Page',
                       'author': 'Nate Page',
                       'text': 'Some get 50 percent, a lot get 60 to 80 percent, and we even have some '
                               'clients that say they get a hundred percent back from their health '
                               'insurance.',
                       'tip': 'Some get 50 percent, a lot get 60 to 80 percent, and we even have some '
                              'clients that say they get a hundred percent back from their health '
                              'insurance.',
                       'timestamp': 50,
                       'timestamp_seconds': 50,
                       'timestamp_label': '[00:00:50]',
                       'url': 'https://www.youtube.com/watch?v=rdwGJdKffpI&t=50s',
                       'markdown': '[00:00:50](https://www.youtube.com/watch?v=rdwGJdKffpI&t=50s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HqCQhe8wbVM',
                       'title': 'Superbills in Private Practice | Out-of-Network Billing',
                       'channel': 'Private Practice Skills',
                       'author': 'Private Practice Skills',
                       'text': 'Once you get into the swing of things with super bills, it really only '
                               'takes like a minute and a half to complete per client.',
                       'tip': 'Once you get into the swing of things with super bills, it really only '
                              'takes like a minute and a half to complete per client.',
                       'timestamp': 257,
                       'timestamp_seconds': 257,
                       'timestamp_label': '[00:04:17]',
                       'url': 'https://www.youtube.com/watch?v=HqCQhe8wbVM&t=257s',
                       'markdown': '[00:04:17](https://www.youtube.com/watch?v=HqCQhe8wbVM&t=257s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tkUfu8WA56U',
                       'title': 'Superbills for Therapists: How Out-of-Network Reimbursement Actually '
                                'Works',
                       'channel': 'Craft Your Practice',
                       'author': 'Craft Your Practice',
                       'text': 'Plans give members a limited window to submit, sometimes as short as '
                               'ninety days, sometimes a year.',
                       'tip': 'Plans give members a limited window to submit, sometimes as short as ninety '
                              'days, sometimes a year.',
                       'timestamp': 572,
                       'timestamp_seconds': 572,
                       'timestamp_label': '[00:09:32]',
                       'url': 'https://www.youtube.com/watch?v=tkUfu8WA56U&t=572s',
                       'markdown': '[00:09:32](https://www.youtube.com/watch?v=tkUfu8WA56U&t=572s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eXrZnEwRRH4',
                       'title': 'Out-of-network 101 for therapists',
                       'channel': 'Alicia Murray | The Therapist HQ \U0001faa9',
                       'author': 'Alicia Murray | The Therapist HQ \U0001faa9',
                       'text': 'Adjustment disorders on their own do not get reimbursed for out of network '
                               'benefits.',
                       'tip': 'Adjustment disorders on their own do not get reimbursed for out of network '
                              'benefits.',
                       'timestamp': 1568,
                       'timestamp_seconds': 1568,
                       'timestamp_label': '[00:26:08]',
                       'url': 'https://www.youtube.com/watch?v=eXrZnEwRRH4&t=1568s',
                       'markdown': '[00:26:08](https://www.youtube.com/watch?v=eXrZnEwRRH4&t=1568s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GVdiKSs4kvU',
                       'title': 'Insurance Pay vs Out-of-Network: Why One80 Physical Therapy is Different',
                       'channel': 'One80 Physical Therapy',
                       'author': 'One80 Physical Therapy',
                       'text': 'We are non-participating with Medicare, which means we cannot give you a '
                               'super bill.',
                       'tip': 'We are non-participating with Medicare, which means we cannot give you a '
                              'super bill.',
                       'timestamp': 242,
                       'timestamp_seconds': 242,
                       'timestamp_label': '[00:04:02]',
                       'url': 'https://www.youtube.com/watch?v=GVdiKSs4kvU&t=242s',
                       'markdown': '[00:04:02](https://www.youtube.com/watch?v=GVdiKSs4kvU&t=242s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dta7Y_d4nYA',
                       'title': 'Top Medical Billing Interview Questions & Answers | Coinsurance vs '
                                'Eligibility vs Preauthorization',
                       'channel': 'MediBill Pro',
                       'author': 'MediBill Pro',
                       'text': 'The percentage that the patient is going to pay after that specific '
                               'deductible is called the co-insurance amount.',
                       'tip': 'The percentage that the patient is going to pay after that specific '
                              'deductible is called the co-insurance amount.',
                       'timestamp': 48,
                       'timestamp_seconds': 48,
                       'timestamp_label': '[00:00:48]',
                       'url': 'https://www.youtube.com/watch?v=dta7Y_d4nYA&t=48s',
                       'markdown': '[00:00:48](https://www.youtube.com/watch?v=dta7Y_d4nYA&t=48s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'SdYPzcQPWOw',
                       'title': 'How to Calculate Patient and Payer Responsibility (Copay vs Coinsurance '
                                'vs Deductible)',
                       'channel': 'Ask The Biller',
                       'author': 'Ask The Biller',
                       'text': "Everyone's deductible does not reset on January 1st, so verify whether the "
                               'benefits are based on a calendar year or a plan year.',
                       'tip': "Everyone's deductible does not reset on January 1st, so verify whether the "
                              'benefits are based on a calendar year or a plan year.',
                       'timestamp': 117,
                       'timestamp_seconds': 117,
                       'timestamp_label': '[00:01:57]',
                       'url': 'https://www.youtube.com/watch?v=SdYPzcQPWOw&t=117s',
                       'markdown': '[00:01:57](https://www.youtube.com/watch?v=SdYPzcQPWOw&t=117s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'XyBNgMnFz0Y',
                       'title': '5 Ways to verify patient Insurance Eligibility | Medical Billing Terms',
                       'channel': 'Inlera University',
                       'author': 'Inlera University',
                       'text': 'Talking to a human at an insurance company is last on the list because it '
                               'takes an enormous amount of time, and hold times are incredibly long right '
                               'now.',
                       'tip': 'Talking to a human at an insurance company is last on the list because it '
                              'takes an enormous amount of time, and hold times are incredibly long right '
                              'now.',
                       'timestamp': 418,
                       'timestamp_seconds': 418,
                       'timestamp_label': '[00:06:58]',
                       'url': 'https://www.youtube.com/watch?v=XyBNgMnFz0Y&t=418s',
                       'markdown': '[00:06:58](https://www.youtube.com/watch?v=XyBNgMnFz0Y&t=418s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'heiuukmxgss',
                       'title': 'Superbill Secrets for Cash Practice Packages - Out-of-Network Billing '
                                'Reimbursement Tips',
                       'channel': 'Jarod Carter',
                       'author': 'Jarod Carter',
                       'text': 'It would be insurance fraud if you let them send in something that said '
                               'they paid 200 dollars when they only paid 190 dollars for that session.',
                       'tip': 'It would be insurance fraud if you let them send in something that said '
                              'they paid 200 dollars when they only paid 190 dollars for that session.',
                       'timestamp': 242,
                       'timestamp_seconds': 242,
                       'timestamp_label': '[00:04:02]',
                       'url': 'https://www.youtube.com/watch?v=heiuukmxgss&t=242s',
                       'markdown': '[00:04:02](https://www.youtube.com/watch?v=heiuukmxgss&t=242s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q9.'}]}
