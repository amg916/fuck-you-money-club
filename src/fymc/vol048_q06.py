from __future__ import annotations

CHAPTER_6 = {'id': 'Q6',
 'chapter_id': 'Q6',
 'chapter_number': 6,
 'question_number': 6,
 'slug': 'stark-anti-kickback-referral-arrangements-fca-triggers',
 'question_prompt': 'How do the Stark Law and Anti-Kickback Statute turn referral and compensation '
                    'arrangements into False Claims Act liability?',
 'kicker': 'Q6 / THE BIG MONEY PLAYBOOKS',
 'title': 'Stark and Anti-Kickback: Referral Arrangements as FCA Triggers',
 'subtitle': "Stark vs. AKS differences, OIG's AKS essentials, fair market value and commercial "
             'reasonableness, safe harbors and exceptions, the final value-based enterprise rules, health '
             'care real estate leases, and compliance-leader guidance',
 'layout_template': 'step_by_step_blueprint',
 'reading_time_minutes': 15,
 'executive_summary': 'Practitioners from K&L Gates, OIG, Holland & Hart, Hall Render, and specialist '
                      'healthcare firms agree that Stark (civil, strict liability) and the Anti-Kickback '
                      'Statute (criminal, one-purpose intent) both feed False Claims Act liability, and '
                      'that remuneration means anything of value flowing in either direction. The street '
                      'mechanics come from settled files. Wheeling Hospital paid physicians a percentage '
                      "of net revenue tracked by 'physician impact reports' and settled for $50 million, "
                      'with $10 million going to a former-executive relator. Catholic Medical Center gave '
                      'a referring cardiologist free call coverage that other cardiologists were paid '
                      '$10,000 per weekend to provide, and settled at $3.8 million. Penalty math runs '
                      '$25,820 per Stark claim and treble damages plus $11,000 per FCA claim. '
                      'Disagreements center on statutory penalty figures, how much Stark compliance covers '
                      'kickback risk, and whether AKS-based FCA claims require but-for causation.',
 'key_metrics': [{'label': 'Wheeling Hospital Settlement and Relator Share',
                  'metric': 'Wheeling Hospital Settlement and Relator Share',
                  'value': '$50M settlement; $10M to the whistleblower',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Outside management firm paid physicians a percentage of net revenue or '
                             "income and tracked technical fees in 'physician impact reports'; motion to "
                             'dismiss denied; relator was a former executive.',
                  'source': 'KLGatesLaw ([MMcEwUD0PNo @ 00:06:05])'},
                 {'label': 'Catholic Medical Center Free Call Coverage Settlement',
                  'metric': 'Catholic Medical Center Free Call Coverage Settlement',
                  'value': '$3.8M settlement; market rate $10,000/weekend and $3,000/night',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Hospital gave a referring sole-practitioner cardiologist free weekend and '
                             'holiday call coverage while paying other cardiologists for the same work; '
                             'bona fide employee safe harbor did not apply.',
                  'source': 'KLGatesLaw ([MMcEwUD0PNo @ 00:12:18])'},
                 {'label': 'Stark Penalty Per Claim',
                  'metric': 'Stark Penalty Per Claim',
                  'value': '$25,820 per claim, adjusted for inflation',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Holland & Hart warns the per-claim figure 'can add up really quickly,' with "
                             'exclusion, FCA treble damages, and qui tam suits layered on top.',
                  'source': 'Holland & Hart LLP ([wODno0XW8l4 @ 00:07:02])'},
                 {'label': 'False Claims Act Exposure Per Claim',
                  'metric': 'False Claims Act Exposure Per Claim',
                  'value': "Three times the program's loss plus $11,000 per claim",
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'OIG attorney Meredith Williams on the civil side of kickback exposure, '
                             'alongside exclusion and civil monetary penalties.',
                  'source': 'OIGatHHS ([a4KhqqeAaUg @ 00:02:30])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner on the panel starts from the same split. Stark is the '
                              'civil, strict-liability self-referral rule. Michael H. Cohen notes a '
                              "physician can violate it 'all on your own' because it applies whenever the "
                              'referrer holds a financial interest, and it reaches the practitioner who '
                              'merely should have known [yUDp-6sl7yI @ 00:00:47]. The Holland & Hart panel '
                              'puts it bluntly: no proof of intent is required to establish liability, so '
                              'an arrangement must fit an exception exactly [wODno0XW8l4 @ 00:04:27]. The '
                              'Anti-Kickback Statute runs the other way. It is a criminal, intent-based '
                              "felony, but the government only needs 'one purpose' of the payment to be "
                              'inducing referrals, and remuneration means cash, in-kind benefits, or '
                              'anything of value [MMcEwUD0PNo @ 00:05:23]. The bridge to qui tam money is '
                              'the False Claims Act. The K&L Gates team, which includes former acting U.S. '
                              'Attorney Norman Acker with 32 years in the Eastern District of North '
                              'Carolina office, frames Stark and the kickback statute as FCA predicates, '
                              'and the civil and criminal labels do not change that [MMcEwUD0PNo @ '
                              '00:03:31]. In practice, Stark exposure can exist with no bad intent at all, '
                              'while kickback exposure turns on what the payment was meant to do, and both '
                              'routes end at the same per-claim liability once tainted claims are '
                              'submitted to a federal program.',
                              'The second point of agreement is how wide the net is. OIG attorney Meredith '
                              'Williams defines the offense as knowingly and willfully offering, paying, '
                              'soliciting, or receiving anything of value for referrals, with both sides '
                              'liable. Her example is a device maker handing surgeons vacations or sham '
                              "'consulting fees' [a4KhqqeAaUg @ 00:00:44]. Neal Goldstein uses 'pitcher' "
                              "for the giver and 'catcher' for the recipient to make the same point: the "
                              'person writing the check and the person cashing it are both on the hook '
                              '[gIyVCP3OhyM @ 00:03:46]. Dirty Medicine lists the forms value takes in '
                              'practice, from Lamborghinis and trips to all-inclusive stays and filet and '
                              'lobster dinners, and stresses that the exchange does not have to be money '
                              '[6IVcs5MTeF8 @ 00:05:35]. Juan Carlos Santos of Chapman Law Group says the '
                              'statute applies to everybody involved in the healthcare industry, naming '
                              'sales reps, marketing people, physicians, toxicology labs, pharmacists, and '
                              'medical entities [RvnCdJAJ4FQ @ 00:01:06]. The working consensus is that '
                              'any transfer of value touching a referral stream belongs on the review '
                              'list, in either direction and at any point in the chain. That covers a '
                              'check, a perk, a trip, a dinner, or a service performed for free, and it '
                              'applies whether the person handing it over carries a medical license, a '
                              'sales quota, or a marketing title.',
                              'On structure, the speakers converge on a short list of elements every '
                              'defensible deal must carry. The K&L Gates panel lists the core Stark '
                              'exception requirements: a written agreement, compensation that does not '
                              "reflect the volume or value of referrals, commercial reasonableness 'even "
                              "if there are no referrals,' and fair market value [MMcEwUD0PNo @ 00:04:48]. "
                              'Charles Oppenheim and Joe Wolf call fair market value, commercial '
                              'reasonableness, and the prohibition on taking referrals into account the '
                              "'big three' concepts, and they describe them as critically important to "
                              "every Stark analysis [6O2jbkASdfY @ 00:05:13]. Children's of Alabama's "
                              'compliance training adds a signed writing, specified items, and a term of '
                              'at least one year on top of fair market value and commercial reasonableness '
                              '[yrBJ3oA7mHw @ 00:02:36]. PYA opens its briefing with a check on '
                              "overconfidence: fair market value 'does not always establish compliance,' "
                              'and an executed agreement on its own does not guarantee it either '
                              '[T_14t1wDSrY @ 00:00:00]. The shared reading is that these elements stack '
                              'rather than substitute for one another. An arrangement priced perfectly at '
                              'market but left unsigned, or signed but keyed to referral counts, still '
                              'fails. Every element has to be present at the same time and stay present '
                              'for the full life of the deal.'],
               'table': {'caption': 'Where the practitioners agree on Stark, kickback, and False Claims '
                                    'Act exposure',
                         'headers': ['Consensus Point',
                                     'Operator Reading of the Rule',
                                     'Where It Bites in a Referral File',
                                     'Expert Source'],
                         'rows': [['Stark is a strict liability statute',
                                   'No proof of intent is required, so the arrangement must fit an '
                                   'exception exactly',
                                   'A single missing exception element creates exposure regardless of what '
                                   'anyone actually meant',
                                   'Holland & Hart LLP ([wODno0XW8l4 @ 00:04:27])'],
                                  ['The kickback statute applies a one-purpose test',
                                   'Liability attaches if one purpose of the payment is inducing federal '
                                   'program referrals',
                                   'A legitimate business reason does not cure a parallel purpose of '
                                   'moving referrals',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:05:23])'],
                                  ['Both statutes are False Claims Act predicates',
                                   'Stark is civil and the kickback statute is criminal, yet both feed FCA '
                                   'claims',
                                   'Tainted claims become per-claim False Claims Act exposure on top of '
                                   'the underlying statute',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:03:31])'],
                                  ['Remuneration means anything of value given or received',
                                   'Cash, in-kind benefits, surgeon vacations, and sham consulting fees '
                                   'all count as remuneration',
                                   'The party offering or paying and the party soliciting or receiving are '
                                   'both liable',
                                   'OIGatHHS ([a4KhqqeAaUg @ 00:00:44])'],
                                  ['The big three anchor every Stark analysis',
                                   'Fair market value, commercial reasonableness, and no taking referrals '
                                   'into account',
                                   'Each exception review begins by testing the deal against these three '
                                   'core concepts',
                                   'American Health Law Association ([6O2jbkASdfY @ 00:05:13])'],
                                  ['Fair market value alone never closes the file',
                                   'An executed agreement or a fair market value price does not establish '
                                   'compliance alone',
                                   'Reviewers keep asking whether the arrangement could be read as '
                                   'inducing referrals in any way',
                                   'PYA, PC ([T_14t1wDSrY @ 00:00:00])'],
                                  ['Everyone in the referral chain is reachable',
                                   'Sales reps, marketing people, physicians, toxicology labs, and '
                                   'pharmacists are all covered by the statute',
                                   'Vendors and marketers face the same exposure as the physicians who '
                                   'make the referrals',
                                   'Chapman Law Group: Health Care Attorneys ([RvnCdJAJ4FQ @ '
                                   '00:01:06])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The case files show what a referral-driven compensation formula looks like '
                              'on paper. In Wheeling Hospital, the K&L Gates panel describes an outside '
                              'management firm paying physicians a percentage of net revenue or income '
                              "while producing 'physician impact reports' that tracked technical fees. The "
                              'motion to dismiss was denied, the matter settled for $50 million, and the '
                              'whistleblower, a former executive, collected $10 million [MMcEwUD0PNo @ '
                              '00:06:05]. Their takeaway is mechanical: build firewalls between referral '
                              "data and compensation, and 'either don't keep those spreadsheets' or wall "
                              'them off [MMcEwUD0PNo @ 00:08:56]. They add that paying above fair market '
                              "value 'took those arguments off the table' for the defense [MMcEwUD0PNo @ "
                              '00:10:50]. Neal Goldstein traces the same structure back to Greber in 1985. '
                              'Cardiomed paid internists 40% of Medicare receipts for Holter monitor work '
                              "labeled 'interpretation fees,' and Greber testified the internists would "
                              'not refer without the fee. The case produced the one-purpose test, and '
                              "Goldstein says similar sham-service ruses persist 'to this day' "
                              '[gIyVCP3OhyM @ 00:05:09]. Across both files the signal pattern is the same. '
                              'Pay is keyed to the revenue the referrals generate, internal reports tie '
                              'physician activity to dollars, and a nominal service label sits on top of '
                              'the payment.',
                              'Smaller files run on the same playbook with cheaper props. Catholic Medical '
                              'Center gave a referring sole-practitioner cardiologist free weekend and '
                              'holiday call coverage while paying other cardiologists $10,000 per weekend '
                              'and $3,000 per night for the same work. The bona fide employee safe harbor '
                              'did not apply, and the hospital settled for $3.8 million [MMcEwUD0PNo @ '
                              '00:12:18]. The panel notes the same free coverage for employees would be '
                              'fine if it met fair market value and commercial reasonableness [MMcEwUD0PNo '
                              '@ 00:14:51]. Juan Carlos Santos describes a DME rep who offered a physician '
                              "a 'medical director' role at $3,500 a month. No conferences or services "
                              'were ever requested while the physician referred patients for knee and back '
                              'braces, and the result was a subpoena and an indictment [RvnCdJAJ4FQ @ '
                              '00:01:29]. David Holt and Patricia Graham flag MSO management fees tied to '
                              'patient volume or service counts as a violation pattern they see in client '
                              'structures, sitting alongside marketers who expect a cut of profits for '
                              'every patient they send [L-RuzumCY2k @ 00:05:32]. The tell in each file is '
                              'a gap between what was paid and what was actually delivered. A title with '
                              'no duties, coverage handed out free to the one doctor who refers, and a fee '
                              'that rises with volume all leave the same footprint.',
                              'The penalty arithmetic is what turns a single referral deal into a qui tam '
                              'payday. Holland & Hart puts the Stark penalty at $25,820 per claim as '
                              "adjusted for inflation, warning it 'can add up really quickly,' with "
                              'improper payments due back within 60 days and exclusion, FCA treble '
                              "damages, and qui tam suits layered on top [wODno0XW8l4 @ 00:07:02]. OIG's "
                              "Meredith Williams sets the FCA exposure at three times the program's loss "
                              'plus $11,000 per claim, and the civil monetary penalty at $50,000 per '
                              "violation plus up to three times the kickback, 'even if some part of the "
                              "payment was for a legitimate purpose' [a4KhqqeAaUg @ 00:02:30]. On the "
                              'structuring side, Dorsey & Whitney walks through the meaningful downside '
                              'risk test for value-based deals. Under Stark, 10% of physician compensation '
                              'must be at risk, illustrated as a $100,000 base with $25,000 at risk. The '
                              'kickback version requires 30% or 20% payer risk with at least 5% shared by '
                              "participants [lzireoG9EFw @ 00:27:55]. Hall Render's real estate team adds "
                              'a square-footage check: load factors typically run 15 to 20%, so a 2,000 '
                              'square foot physician suite gets billed as 2,300 square feet once a 15% '
                              'load is added [_1_drZryqm4 @ 00:44:43].'],
               'table': {'caption': 'Referral arrangement patterns, the exact figures attached, and how '
                                    'they read in an FCA file',
                         'headers': ['Mechanic or Pattern',
                                     'Exact Number or Term Stated',
                                     'How It Reads in an FCA File',
                                     'Expert Source'],
                         'rows': [['Revenue-percentage physician pay with tracking reports',
                                   'Percentage of net revenue or income plus physician impact reports on '
                                   'technical fees',
                                   'Motion to dismiss denied; $50M settlement and $10M to a '
                                   'former-executive relator',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:06:05])'],
                                  ['Free call coverage for a referring cardiologist',
                                   'Other cardiologists paid $10,000 per weekend and $3,000 per night',
                                   'Bona fide employee safe harbor inapplicable; the hospital settled for '
                                   '$3.8M',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:12:18])'],
                                  ['Sham interpretation fees paid to referring internists',
                                   '40% of Medicare receipts labeled as Holter monitor interpretation fees',
                                   'Produced the one-purpose test; similar sham-service ruses persist to '
                                   'this day',
                                   'Group Practice with Neal Goldstein ([gIyVCP3OhyM @ 00:05:09])'],
                                  ['Phantom medical director role offered by a DME rep',
                                   '$3,500 per month with no conferences or services ever requested',
                                   'Knee and back brace referrals followed by a subpoena and an indictment',
                                   'Chapman Law Group: Health Care Attorneys ([RvnCdJAJ4FQ @ 00:01:29])'],
                                  ['MSO compensation that rises with ordering volume',
                                   'Percentage-based fees or bonuses paid for ordering more tests',
                                   'Holt treats the bonus as a Stark violation and steers clients to flat '
                                   'fees',
                                   'Holt Law: For Healthcare Businesses ([L-RuzumCY2k @ 00:12:06])'],
                                  ['Rent formula that correlates with test volume',
                                   'Example of $5,000 rent minus $5 per test performed',
                                   'Correlation formulas tie compensation to referral volume or value '
                                   'under the final rules',
                                   'Dorsey & Whitney LLP ([lzireoG9EFw @ 00:58:45])'],
                                  ['Per-claim Stark penalty after inflation adjustment',
                                   '$25,820 per claim, with improper payments returned within 60 days',
                                   'Multiplies across every claim tied to the arrangement and stacks with '
                                   'FCA damages',
                                   'Holland & Hart LLP ([wODno0XW8l4 @ 00:07:02])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'What the defense bar watches before a relator does',
                           'body': 'These are the moves practitioners say separate a defensible referral '
                                   'arrangement from a settlement file, drawn from the cases and drafting '
                                   'habits they described.',
                           'items': ['Firewall the referral data: K&L Gates tells hospitals to either not '
                                     'keep spreadsheets that track physician referrals against pay, or '
                                     'wall them off from compensation decisions, which is the gap that '
                                     'surfaced in Wheeling Hospital [KLGatesLaw — MMcEwUD0PNo @ 00:08:56].',
                                     "Scrub the paper trail for intent: Hall Render's Alyssa James warns "
                                     'that board comments, emails, or texts can be read as improper '
                                     "intent, with '800 pages' of good purposes undone by 'one sentence' "
                                     '[Dallas-Fort Worth Hospital Council — _1_drZryqm4 @ 00:07:29].',
                                     'Run fair market value work through counsel: James says a third-party '
                                     'appraisal is optional, appraisers should have healthcare experience, '
                                     'engaging them through counsel preserves attorney-client privilege, '
                                     'and FMV is a range where the high and low ends are equally compliant '
                                     '[Dallas-Fort Worth Hospital Council — _1_drZryqm4 @ 00:36:13].',
                                     "Price the self-disclosure exit: the K&L Gates panel says 'anyone can "
                                     "be a relator,' urges investigating employee complaints, and notes "
                                     "the Stark self-disclosure protocol can mean 'pennies on the dollar' "
                                     '[KLGatesLaw — MMcEwUD0PNo @ 00:19:36].']},
               'sop_steps': [{'step': 1,
                              'title': 'Run the Stark analysis first',
                              'action': 'Open every referral arrangement review with the strict-liability '
                                        'Stark analysis before turning to kickback intent.',
                              'detail': 'Dorsey & Whitney says Stark is strict liability so the analysis '
                                        'starts there, while the kickback statute applies a one-purpose '
                                        'test and safe harbor compliance is voluntary [Dorsey & Whitney '
                                        'LLP — lzireoG9EFw @ 00:10:39]. Joe Wolf likewise starts with '
                                        'Stark and its state analog [American Health Law Association — '
                                        '6O2jbkASdfY @ 00:20:05].'},
                             {'step': 2,
                              'title': 'Map the deal against every element',
                              'action': 'Line the arrangement up against each element of the exception or '
                                        'safe harbor and confirm all are present at once.',
                              'detail': 'For space rentals, Sadie Zelflu lists a signed written agreement, '
                                        'identified premises, a term of at least one year, rent set in '
                                        'advance at FMV, no tie to referral volume or value, and space '
                                        'limited to what is reasonably necessary, and recommends a suite '
                                        'number plus a floor plan exhibit [Dallas-Fort Worth Hospital '
                                        'Council — _1_drZryqm4 @ 00:25:24].'},
                             {'step': 3,
                              'title': 'Stress-test the compensation formula',
                              'action': 'Check whether any payment term rises or falls with the volume or '
                                        'value of referrals or tests ordered.',
                              'detail': 'Holt Law bars percentage-based MSO fees and bonuses for ordering '
                                        'more tests and pushes flat fees [Holt Law: For Healthcare '
                                        'Businesses — L-RuzumCY2k @ 00:12:06]. Dorsey & Whitney flags '
                                        'correlation formulas such as $5,000 rent minus $5 per test '
                                        '[Dorsey & Whitney LLP — lzireoG9EFw @ 00:58:45].'},
                             {'step': 4,
                              'title': 'Monitor the arrangement across its life cycle',
                              'action': 'Re-check signatures, time logs, terms, and schedules for as long '
                                        'as the arrangement runs.',
                              'detail': 'PYA says Stark failures are mostly operational: unsigned '
                                        'agreements, missing time logs, and failure to monitor exception '
                                        'requirements over the life cycle [PYA, PC — T_14t1wDSrY @ '
                                        "00:03:03]. Hall Render's pitfall list adds expired leases, "
                                        'physicians moving in before signing, changes agreed by email, '
                                        'miscalculated CPI escalators, and schedule drift [Dallas-Fort '
                                        'Worth Hospital Council — _1_drZryqm4 @ 00:33:55].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over what intent actually means. Michael H. Cohen '
                              'frames the Anti-Kickback Statute as requiring intent to violate, while '
                              "Stark bites whenever the practitioner merely 'should have known' "
                              '[yUDp-6sl7yI @ 00:01:28]. Alyssa James of Hall Render reads the kickback '
                              'statute differently: the relevant intent is intent to reward referrals, not '
                              'intent to violate the statute itself [_1_drZryqm4 @ 00:06:33]. On Stark, '
                              "PYA pushes further than Cohen's should-have-known framing, telling "
                              'compliance leaders that once no exception is satisfied there is an issue no '
                              "matter what anyone intended, because 'really intent here doesn't matter' "
                              '[T_14t1wDSrY @ 00:02:40]. Holland & Hart lands in the same camp, calling '
                              "Stark a strict liability law where 'there is no proof of intent that is "
                              "required to establish liability,' so an arrangement has to fit an exception "
                              'exactly [wODno0XW8l4 @ 00:04:27]. That leaves two different evidentiary '
                              'burdens sitting inside the same referral deal. The Stark count turns on '
                              'whether every element of an exception was met, with no state-of-mind story '
                              'needed at all. The kickback count turns on proof that someone meant to '
                              'reward referrals, and under the Hall Render reading that proof does not '
                              'require showing that anyone knew the statute existed or set out to break '
                              'it.',
                              'Documentation is the second fault line, and it runs straight through the '
                              'American Health Law Association panel. Charles Oppenheim notes that missing '
                              'signatures and lapsed terms were once treated as foot faults and that, '
                              'looking back, timesheets, emails, board minutes and canceled checks can now '
                              'establish a writing, yet going forward he still wants a formal, '
                              'board-approved contract [6O2jbkASdfY @ 00:14:58]. Joe Wolf leans harder on '
                              'the flexibility: a collection of contemporaneous documents can satisfy the '
                              'writing requirement and that rule is now in the statute, electronic '
                              'signatures work under state law, there is a 90-day window for the writing '
                              'and signature, and roughly $6,200 a year can be paid under limited '
                              'remuneration without a signed writing [6O2jbkASdfY @ 00:16:05]. Dorsey & '
                              'Whitney quotes that limited remuneration exception at $5,000 a year and '
                              'attaches a hard warning to the 90-day grace period: modifications must be '
                              'written before they take effect [lzireoG9EFw @ 01:13:22]. Hall Render '
                              'converts the flexibility into a salvage routine for a lease that expired '
                              'six months ago: hunt for auto-renewal or extension writings, check whether '
                              'the holdover clause permits the same terms, paper a new lease at current '
                              'fair market value, then escalate to compliance about possible disclosure '
                              '[_1_drZryqm4 @ 00:56:55].',
                              'Compensation flexibility splits the room too. Under the value-based '
                              'enterprise rules, Ed White of Nelson Mullins tells the Pinnacle Healthcare '
                              'Consulting audience there is no fair market value requirement and no '
                              'prohibition on compensation varying with the volume or value of referrals '
                              '[k11FLIP3Vk4 @ 00:28:10]. Later in the same session he pulls back hard: '
                              "'we're not advocating you use a no fair market value requirement to go out "
                              "and pay people excessively' [k11FLIP3Vk4 @ 00:50:51]. Alyssa James of Hall "
                              'Render works the conventional side of the line, insisting on meeting fair '
                              'market value every time while treating it as a range rather than a single '
                              'number, with the high and low ends equally compliant, and making a '
                              'third-party appraisal optional so long as the appraiser has healthcare '
                              'experience and is engaged through counsel to keep attorney-client privilege '
                              '[_1_drZryqm4 @ 00:36:13]. The KLGatesLaw panel shows what happens past the '
                              'top of that range: in the Wheeling Hospital matter, pay above fair market '
                              "value 'took those arguments off the table' [MMcEwUD0PNo @ 00:10:50]. The "
                              'working read is that value-based structures loosen the formal valuation '
                              'test, while the case history these speakers walk through still punishes pay '
                              'that cannot be placed inside a defensible, documented range.'],
               'table': {'caption': 'Side-by-side splits on intent, penalties, documentation, pay and '
                                    'causation',
                         'headers': ['Contested Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Which intent the Anti-Kickback count actually needs',
                                   'Cohen frames the kickback statute as requiring intent to violate the '
                                   'law.',
                                   'Hall Render says the relevant intent is rewarding referrals, not '
                                   'violating the statute.',
                                   'Michael H. Cohen – Healthcare Law ([yUDp-6sl7yI @ 00:01:28]); '
                                   'Dallas-Fort Worth Hospital Council ([_1_drZryqm4 @ 00:06:33])'],
                                  ['Criminal penalty ceiling quoted for kickback violations',
                                   'OIG attorney Meredith Williams cites up to $25,000 per violation and '
                                   'up to 5 years.',
                                   'Holland & Hart says the 2018 budget bill raised fines to $100,000 and '
                                   'jail to 10 years.',
                                   'OIGatHHS ([a4KhqqeAaUg @ 00:01:46]); Holland & Hart LLP ([wODno0XW8l4 '
                                   '@ 00:13:35])'],
                                  ['Whether a clean Stark analysis also covers the kickback side',
                                   'Oppenheim says 99% of the time satisfying Stark leaves you in good '
                                   'shape on kickback.',
                                   'Holland & Hart says providers who think providing a service cannot '
                                   'implicate the kickback statute are wrong.',
                                   'American Health Law Association ([6O2jbkASdfY @ 00:20:36]); Holland & '
                                   'Hart LLP ([wODno0XW8l4 @ 00:58:57])'],
                                  ['How the Stark writing requirement gets satisfied in practice',
                                   'Oppenheim still wants a formal, board-approved contract on every '
                                   'arrangement going forward.',
                                   'Wolf accepts a collection of contemporaneous documents, e-signatures '
                                   'and a 90-day signature window.',
                                   'American Health Law Association ([6O2jbkASdfY @ 00:14:58]); American '
                                   'Health Law Association ([6O2jbkASdfY @ 00:16:05])'],
                                  ['Fair market value targeting on physician compensation',
                                   'Wolf says there is no need to slavishly target the 50th percentile '
                                   'benchmark.',
                                   'White warns the value-based no-FMV rules are not a license to pay '
                                   'people excessively.',
                                   'American Health Law Association ([6O2jbkASdfY @ 00:24:34]); Pinnacle '
                                   'Healthcare Consulting ([k11FLIP3Vk4 @ 00:50:51])'],
                                  ['But-for causation in kickback-tainted False Claims Act cases',
                                   'The Eighth Circuit in DS Medical requires but-for causation for '
                                   'AKS-FCA claims.',
                                   'KLGatesLaw flags the circuit split and treats the causation argument '
                                   'only as a fallback.',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:17:18])'],
                                  ['How often to refresh a fair market value appraisal',
                                   "No legal deadline; follow the appraiser's reliance period and reassess "
                                   'earlier in volatile markets.',
                                   "Sadie Zelflu adds that refresh timing ultimately turns on the client's "
                                   'own risk tolerance.',
                                   'Dallas-Fort Worth Hospital Council ([_1_drZryqm4 @ 00:58:49]); '
                                   'Dallas-Fort Worth Hospital Council ([_1_drZryqm4 @ 01:00:19])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The cases that blew up share one mechanic: money tied to referral volume '
                              'and dressed up as something else. In Wheeling Hospital, an outside '
                              'management firm paid physicians a percentage of net revenue or income and '
                              "tracked technical fees in 'physician impact reports'; the motion to dismiss "
                              'was denied, the hospital settled for $50 million, and the whistleblower, a '
                              'former executive, collected $10 million [MMcEwUD0PNo @ 00:06:05]. Catholic '
                              'Medical Center in New Hampshire gave a referring sole-practitioner '
                              'cardiologist free weekend and holiday call coverage while paying other '
                              'cardiologists $10,000 per weekend and $3,000 per night, the bona fide '
                              'employee safe harbor did not apply, and the settlement hit $3.8 million '
                              '[MMcEwUD0PNo @ 00:12:18]. Juan Carlos Santos of Chapman Law Group describes '
                              "a DME rep handing a physician a $3,500-a-month 'medical director' role with "
                              'no conferences or services ever requested while knee and back brace '
                              'referrals flowed, which ended in a subpoena and an indictment [RvnCdJAJ4FQ '
                              '@ 00:01:29]. Group Practice with Neal Goldstein traces the template back to '
                              'Greber, where Cardiomed paid internists 40% of Medicare receipts as '
                              "'interpretation fees' and Greber testified the internists would not refer "
                              'without the fee; the speaker says similar sham-service ruses persist to '
                              'this day [gIyVCP3OhyM @ 00:05:09].',
                              'Most Stark exposure is operational rather than conceptual. PYA lists the '
                              'recurring failures as unsigned agreements, missing time logs and '
                              'arrangements nobody monitors against exception requirements across their '
                              'life cycle, and warns against deals left on autopilot without periodic '
                              'reassessment [T_14t1wDSrY @ 00:03:03]. The Hall Render team on the '
                              'Dallas-Fort Worth Hospital Council webinar gives the real estate version: '
                              'expired leases, physicians moving in before signing, changes agreed by '
                              'email, miscalculated CPI escalators, and schedule drift such as a Monday '
                              '1-to-5 time-share slot sliding to Thursday, which needs an amendment '
                              '[_1_drZryqm4 @ 00:33:55]. The same panel flags escalators that were never '
                              'billed, unpaid receptionist services inside a time-share, and excess space '
                              'as red flags [_1_drZryqm4 @ 00:51:32]. Dorsey & Whitney adds the most '
                              'expensive monitoring trap: under the Stark no-risk value-based arrangement '
                              'rules, annual monitoring is required and failing to do it taints all '
                              'referrals, while the kickback side allows only in-kind support with a 15% '
                              'recipient contribution and bars physician-owned device makers [lzireoG9EFw '
                              '@ 00:32:25]. None of these traps requires bad intent; each is a missing '
                              'signature, a stale number or an unpaid perk sitting in the file where an '
                              'auditor or relator can find it.',
                              'Run the exposure math before signing anything. Holland & Hart puts the '
                              "Stark penalty at $25,820 per claim as adjusted for inflation, warns 'that "
                              "can add up really quickly,' requires improper payments returned within 60 "
                              'days, and stacks exclusion, False Claims Act treble damages and qui tam '
                              'suits on top [wODno0XW8l4 @ 00:07:02]. Meredith Williams of the OIG adds '
                              'treble damages plus $11,000 per claim under the False Claims Act, and civil '
                              'monetary penalties of $50,000 per violation plus up to three times the '
                              'kickback, even if some part of the payment was for a legitimate purpose '
                              '[a4KhqqeAaUg @ 00:02:30]. Hall Render explains why the paper cannot save a '
                              'bad deal: board comments, emails or texts can be read as improper intent, '
                              'so 800 pages of good purposes can be undone by one sentence [_1_drZryqm4 @ '
                              '00:07:29]. The KLGatesLaw panel closes with the counterweight: anyone can '
                              'be a relator, employee complaints have to be investigated, and the Stark '
                              "self-disclosure protocol can mean 'pennies on the dollar' [MMcEwUD0PNo @ "
                              '00:20:53]. The economics check is therefore per-claim multiplication '
                              'against a single bad email, with self-disclosure as the cheapest exit the '
                              'speakers identify once a defect is found internally before a relator '
                              'files.'],
               'table': {'caption': 'Failure modes with the dollars and outcomes practitioners reported',
                         'headers': ['Failure Mode', 'What Went Wrong', 'Economics Check', 'Expert Source'],
                         'rows': [['Referral data wired into physician compensation formulas',
                                   'Management firm paid physicians a percentage of net revenue and '
                                   'tracked technical fees in impact reports.',
                                   '$50M settlement; former-executive whistleblower received $10M after '
                                   'the dismissal motion failed.',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:06:05])'],
                                  ['Free call coverage for a referring cardiologist',
                                   'Hospital covered weekends and holidays free for one referring '
                                   'sole-practitioner cardiologist.',
                                   'Other cardiologists were paid $10,000 per weekend and $3,000 per '
                                   'night; settled for $3.8M.',
                                   'KLGatesLaw ([MMcEwUD0PNo @ 00:12:18])'],
                                  ['Sham medical director stipend from a DME rep',
                                   'Physician paid $3,500 monthly with no services requested while '
                                   'referring brace patients.',
                                   'The arrangement ended in a subpoena followed by an indictment.',
                                   'Chapman Law Group: Health Care Attorneys ([RvnCdJAJ4FQ @ 00:01:29])'],
                                  ['Percentage-based MSO fees and test-ordering bonuses',
                                   'MSO fees tied to patient volume or service counts, plus bonuses for '
                                   'ordering more tests.',
                                   'Holt Law says switch to a flat fee; everybody doing it is no defense.',
                                   'Holt Law: For Healthcare Businesses ([L-RuzumCY2k @ 00:12:06])'],
                                  ['Waived co-payments for federal program patients',
                                   'Practices waiving co-payments for patients covered by federal '
                                   'healthcare programs.',
                                   'Dirty Medicine calls it fraud that violates the Anti-Kickback Statute '
                                   'outright.',
                                   'Dirty Medicine ([6IVcs5MTeF8 @ 00:06:25])'],
                                  ['Free point-of-care supplies, gift cards and staff perks',
                                   'Even free point-of-care test cups can be treated as a kickback to the '
                                   'recipient.',
                                   'Gift cards are banned and medical staff incidental benefits stay under '
                                   '$36 per occurrence.',
                                   "Children's of Alabama ([yrBJ3oA7mHw @ 00:06:19]); Children's of "
                                   'Alabama ([yrBJ3oA7mHw @ 00:03:15])'],
                                  ['Holdover running at a stale fair market value rate',
                                   'Expired lease keeps running on holdover, for example a 2020 rate still '
                                   'paid in 2026.',
                                   'Holdover sits on the list of lease provisions with economic value that '
                                   'must be reviewed.',
                                   'Dallas-Fort Worth Hospital Council ([_1_drZryqm4 @ 00:45:55])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop-Ship Checks Before Any Referral-Linked Deal Goes Live',
                           'body': 'Each gate below comes straight from a practitioner-reported failure. '
                                   'Clear all four before money, space or services change hands.',
                           'items': ['Wall referral and technical-fee data off from anyone setting '
                                     "physician pay; the Wheeling lesson is either don't keep those "
                                     'spreadsheets or firewall them [KLGatesLaw — MMcEwUD0PNo @ 00:08:56].',
                                     'No physician moves into space before signature and no email-only '
                                     'changes; schedule drift and escalator changes need a written '
                                     'amendment [Dallas-Fort Worth Hospital Council — _1_drZryqm4 @ '
                                     '00:33:55].',
                                     'Calendar at least annual monitoring for value-based arrangements; an '
                                     'ineffective activity gets 30 days to wind down or 90 days to modify, '
                                     'which Amber Ellis calls pretty short [Holland & Hart LLP — '
                                     'wODno0XW8l4 @ 00:57:26].',
                                     'On a subpoena, search warrant or CID, say nothing to agents, expect '
                                     'good cop and bad cop, and call counsel immediately [Chapman Law '
                                     'Group: Health Care Attorneys — RvnCdJAJ4FQ @ 00:04:36].']}}],
 'pull_quote': '"Regulators are going to look past the label of what the document actually says and into '
               'what it says and to see what\'s actually being exchanged." — Dallas-Fort Worth Hospital '
               'Council (_1_drZryqm4 @ 00:23:59).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Run every physician arrangement through Stark and its state analog first, then the '
                      'kickback analysis [American Health Law Association — 6O2jbkASdfY @ 00:20:05].',
                      'Paper space leases with a signed writing, a suite number plus floor-plan exhibit, a '
                      'term of at least 1 year, and rent set in advance at fair market value [Dallas-Fort '
                      'Worth Hospital Council — _1_drZryqm4 @ 00:25:24].',
                      'Engage any fair market value appraiser through counsel, insist on healthcare '
                      'experience, and treat FMV as a range [Dallas-Fort Worth Hospital Council — '
                      '_1_drZryqm4 @ 00:36:13].',
                      'Replace percentage-based MSO fees and test-ordering bonuses with a flat fee [Holt '
                      'Law: For Healthcare Businesses — L-RuzumCY2k @ 00:12:06].',
                      'Investigate every employee complaint, because anyone can be a relator, and price '
                      'the Stark self-disclosure protocol as a pennies-on-the-dollar exit [KLGatesLaw — '
                      'MMcEwUD0PNo @ 00:19:36].',
                      'Require signed agreements before services start, written amendments for every '
                      'change, and escalation of policy exceptions to counsel [American Health Law '
                      'Association — 6O2jbkASdfY @ 00:22:18].'],
 'statutory_citations': [{'title': 'KLGatesLaw — Stark Law and the Anti-Kickback Statute Under the False '
                                   'Claims Act [00:06:05]',
                          'url': 'https://www.youtube.com/watch?v=MMcEwUD0PNo&t=365s',
                          'relevance': 'Primary practitioner testimony on the Wheeling Hospital $50M '
                                       'settlement, physician impact reports and the $10M relator award.'},
                         {'title': 'Holland & Hart LLP — New Final Rules for Stark and Anti Kickback '
                                   'Reforms: An In-Depth Review [00:07:02]',
                          'url': 'https://www.youtube.com/watch?v=wODno0XW8l4&t=422s',
                          'relevance': 'Primary practitioner testimony on the $25,820 per-claim Stark '
                                       'penalty, the 60-day repayment window and qui tam exposure.'},
                         {'title': 'Dallas-Fort Worth Hospital Council — DFWHC and Hall Render webinar '
                                   '“Stark and Anti-Kickback Provisions in Health Care Real Estate” '
                                   '[00:33:55]',
                          'url': 'https://www.youtube.com/watch?v=_1_drZryqm4&t=2035s',
                          'relevance': 'Primary practitioner testimony on expired leases, pre-signature '
                                       'move-ins, email changes, escalator errors and schedule drift.'},
                         {'title': 'American Health Law Association — Stark Law: Latest Trends and '
                                   'Developments [00:20:36]',
                          'url': 'https://www.youtube.com/watch?v=6O2jbkASdfY&t=1236s',
                          'relevance': 'Primary practitioner testimony on running Stark first and the 99% '
                                       'overlap with kickback compliance.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'yUDp-6sl7yI',
                       'title': 'Stark vs Anti-Kickback: The Key Differences',
                       'channel': 'Michael H. Cohen – Healthcare Law',
                       'author': 'Michael H. Cohen – Healthcare Law',
                       'text': 'To begin, we have to keep in mind that Stark Law prohibits making '
                               'referrals where the referring physician has a financial interest, so '
                               "that's something you can violate all on your own.",
                       'tip': 'To begin, we have to keep in mind that Stark Law prohibits making referrals '
                              "where the referring physician has a financial interest, so that's something "
                              'you can violate all on your own.',
                       'timestamp': 47,
                       'timestamp_seconds': 47,
                       'timestamp_label': '[00:00:47]',
                       'url': 'https://www.youtube.com/watch?v=yUDp-6sl7yI&t=47s',
                       'markdown': '[00:00:47](https://www.youtube.com/watch?v=yUDp-6sl7yI&t=47s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yUDp-6sl7yI',
                       'title': 'Stark vs Anti-Kickback: The Key Differences',
                       'channel': 'Michael H. Cohen – Healthcare Law',
                       'author': 'Michael H. Cohen – Healthcare Law',
                       'text': "The Anti-Kickback Statute doesn't have specific exceptions the way Stark "
                               'Law does.',
                       'tip': "The Anti-Kickback Statute doesn't have specific exceptions the way Stark "
                              'Law does.',
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=yUDp-6sl7yI&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=yUDp-6sl7yI&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MMcEwUD0PNo',
                       'title': 'Stark Law and the Anti-Kickback Statute Under the False Claims Act',
                       'channel': 'KLGatesLaw',
                       'author': 'KLGatesLaw',
                       'text': 'Paying physicians above fair market value took those arguments off the '
                               'table.',
                       'tip': 'Paying physicians above fair market value took those arguments off the '
                              'table.',
                       'timestamp': 650,
                       'timestamp_seconds': 650,
                       'timestamp_label': '[00:10:50]',
                       'url': 'https://www.youtube.com/watch?v=MMcEwUD0PNo&t=650s',
                       'markdown': '[00:10:50](https://www.youtube.com/watch?v=MMcEwUD0PNo&t=650s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'MMcEwUD0PNo',
                       'title': 'Stark Law and the Anti-Kickback Statute Under the False Claims Act',
                       'channel': 'KLGatesLaw',
                       'author': 'KLGatesLaw',
                       'text': 'Anyone can be a relator.',
                       'tip': 'Anyone can be a relator.',
                       'timestamp': 1176,
                       'timestamp_seconds': 1176,
                       'timestamp_label': '[00:19:36]',
                       'url': 'https://www.youtube.com/watch?v=MMcEwUD0PNo&t=1176s',
                       'markdown': '[00:19:36](https://www.youtube.com/watch?v=MMcEwUD0PNo&t=1176s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gIyVCP3OhyM',
                       'title': 'Overview of the Anti-Kickback Statute',
                       'channel': 'Group Practice with Neal Goldstein',
                       'author': 'Group Practice with Neal Goldstein',
                       'text': 'Both the pitcher who gives the remuneration and the catcher who receives '
                               'it are liable under the statute.',
                       'tip': 'Both the pitcher who gives the remuneration and the catcher who receives it '
                              'are liable under the statute.',
                       'timestamp': 226,
                       'timestamp_seconds': 226,
                       'timestamp_label': '[00:03:46]',
                       'url': 'https://www.youtube.com/watch?v=gIyVCP3OhyM&t=226s',
                       'markdown': '[00:03:46](https://www.youtube.com/watch?v=gIyVCP3OhyM&t=226s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'lzireoG9EFw',
                       'title': 'Final Stark and Anti-Kickback Statute Rules: What You Need to Know',
                       'channel': 'Dorsey & Whitney LLP',
                       'author': 'Dorsey & Whitney LLP',
                       'text': 'There is a 90-day grace period for the writing, but modifications must be '
                               'put in writing before they take effect.',
                       'tip': 'There is a 90-day grace period for the writing, but modifications must be '
                              'put in writing before they take effect.',
                       'timestamp': 4402,
                       'timestamp_seconds': 4402,
                       'timestamp_label': '[01:13:22]',
                       'url': 'https://www.youtube.com/watch?v=lzireoG9EFw&t=4402s',
                       'markdown': '[01:13:22](https://www.youtube.com/watch?v=lzireoG9EFw&t=4402s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a4KhqqeAaUg',
                       'title': 'Federal Anti-Kickback Statute',
                       'channel': 'OIGatHHS',
                       'author': 'OIGatHHS',
                       'text': 'Violating the Anti-Kickback Statute is a felony, which means violators can '
                               'go to jail.',
                       'tip': 'Violating the Anti-Kickback Statute is a felony, which means violators can '
                              'go to jail.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=a4KhqqeAaUg&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=a4KhqqeAaUg&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a4KhqqeAaUg',
                       'title': 'Federal Anti-Kickback Statute',
                       'channel': 'OIGatHHS',
                       'author': 'OIGatHHS',
                       'text': "A provider can be penalized up to three times the government program's "
                               'loss, plus $11,000 per claim.',
                       'tip': "A provider can be penalized up to three times the government program's "
                              'loss, plus $11,000 per claim.',
                       'timestamp': 150,
                       'timestamp_seconds': 150,
                       'timestamp_label': '[00:02:30]',
                       'url': 'https://www.youtube.com/watch?v=a4KhqqeAaUg&t=150s',
                       'markdown': '[00:02:30](https://www.youtube.com/watch?v=a4KhqqeAaUg&t=150s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yrBJ3oA7mHw',
                       'title': 'COA Corporate Compliance: Understanding the Stark Law and Anti-Kickback '
                                'Statute',
                       'channel': "Children's of Alabama",
                       'author': "Children's of Alabama",
                       'text': 'Even free point-of-care test cups can be a kickback.',
                       'tip': 'Even free point-of-care test cups can be a kickback.',
                       'timestamp': 379,
                       'timestamp_seconds': 379,
                       'timestamp_label': '[00:06:19]',
                       'url': 'https://www.youtube.com/watch?v=yrBJ3oA7mHw&t=379s',
                       'markdown': '[00:06:19](https://www.youtube.com/watch?v=yrBJ3oA7mHw&t=379s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6IVcs5MTeF8',
                       'title': 'Healthcare Fraud & Abuse (Stark Law, Anti-Kickback, etc.)',
                       'channel': 'Dirty Medicine',
                       'author': 'Dirty Medicine',
                       'text': 'You cannot waive co-payments for patients in federal healthcare programs; '
                               "you can't do it, it's fraud, it violates the anti-kickback statute.",
                       'tip': 'You cannot waive co-payments for patients in federal healthcare programs; '
                              "you can't do it, it's fraud, it violates the anti-kickback statute.",
                       'timestamp': 385,
                       'timestamp_seconds': 385,
                       'timestamp_label': '[00:06:25]',
                       'url': 'https://www.youtube.com/watch?v=6IVcs5MTeF8&t=385s',
                       'markdown': '[00:06:25](https://www.youtube.com/watch?v=6IVcs5MTeF8&t=385s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k11FLIP3Vk4',
                       'title': 'Using the New CMS and OIG Stark and Anti Kickback Revisions with Value '
                                'Based Enterprises',
                       'channel': 'Pinnacle Healthcare Consulting',
                       'author': 'Pinnacle Healthcare Consulting',
                       'text': "So we're not advocating you use a no fair market value requirement to go "
                               'out and pay people excessively.',
                       'tip': "So we're not advocating you use a no fair market value requirement to go "
                              'out and pay people excessively.',
                       'timestamp': 3051,
                       'timestamp_seconds': 3051,
                       'timestamp_label': '[00:50:51]',
                       'url': 'https://www.youtube.com/watch?v=k11FLIP3Vk4&t=3051s',
                       'markdown': '[00:50:51](https://www.youtube.com/watch?v=k11FLIP3Vk4&t=3051s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'T_14t1wDSrY',
                       'title': 'Anti-Kickback and Stark Law: What Compliance Leaders Need to Know',
                       'channel': 'PYA, PC',
                       'author': 'PYA, PC',
                       'text': 'Fair market value does not always establish compliance.',
                       'tip': 'Fair market value does not always establish compliance.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=T_14t1wDSrY&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=T_14t1wDSrY&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'RvnCdJAJ4FQ',
                       'title': 'Federal Anti-Kickback Statute by Health Care Lawyer',
                       'channel': 'Chapman Law Group: Health Care Attorneys',
                       'author': 'Chapman Law Group: Health Care Attorneys',
                       'text': "Now many people believe that if you don't take federal money, Medicare or "
                               "Medicaid, you don't have to worry about the anti-kickback; that's false.",
                       'tip': "Now many people believe that if you don't take federal money, Medicare or "
                              "Medicaid, you don't have to worry about the anti-kickback; that's false.",
                       'timestamp': 167,
                       'timestamp_seconds': 167,
                       'timestamp_label': '[00:02:47]',
                       'url': 'https://www.youtube.com/watch?v=RvnCdJAJ4FQ&t=167s',
                       'markdown': '[00:02:47](https://www.youtube.com/watch?v=RvnCdJAJ4FQ&t=167s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'L-RuzumCY2k',
                       'title': 'Stark Law and Anti-Kickback Explained What Healthcare Businesses Must '
                                'Know',
                       'channel': 'Holt Law: For Healthcare Businesses',
                       'author': 'Holt Law: For Healthcare Businesses',
                       'text': 'So, you want to build compliantly from the beginning.',
                       'tip': 'So, you want to build compliantly from the beginning.',
                       'timestamp': 817,
                       'timestamp_seconds': 817,
                       'timestamp_label': '[00:13:37]',
                       'url': 'https://www.youtube.com/watch?v=L-RuzumCY2k&t=817s',
                       'markdown': '[00:13:37](https://www.youtube.com/watch?v=L-RuzumCY2k&t=817s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'wODno0XW8l4',
                       'title': 'New Final Rules for Stark and Anti Kickback Reforms: An In-Depth Review',
                       'channel': 'Holland & Hart LLP',
                       'author': 'Holland & Hart LLP',
                       'text': 'Currently, as adjusted for inflation, 25,820 per claim, so that can add up '
                               'really quickly.',
                       'tip': 'Currently, as adjusted for inflation, 25,820 per claim, so that can add up '
                              'really quickly.',
                       'timestamp': 422,
                       'timestamp_seconds': 422,
                       'timestamp_label': '[00:07:02]',
                       'url': 'https://www.youtube.com/watch?v=wODno0XW8l4&t=422s',
                       'markdown': '[00:07:02](https://www.youtube.com/watch?v=wODno0XW8l4&t=422s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '6O2jbkASdfY',
                       'title': 'Stark Law: Latest Trends and Developments',
                       'channel': 'American Health Law Association',
                       'author': 'American Health Law Association',
                       'text': "It's the rare instance where I feel I'm fine on Stark, but I'm worried "
                               'about kickback.',
                       'tip': "It's the rare instance where I feel I'm fine on Stark, but I'm worried "
                              'about kickback.',
                       'timestamp': 1254,
                       'timestamp_seconds': 1254,
                       'timestamp_label': '[00:20:54]',
                       'url': 'https://www.youtube.com/watch?v=6O2jbkASdfY&t=1254s',
                       'markdown': '[00:20:54](https://www.youtube.com/watch?v=6O2jbkASdfY&t=1254s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '_1_drZryqm4',
                       'title': 'DFWHC and Hall Render webinar “Stark and Anti-Kickback Provisions in '
                                'Health Care Real Estate”',
                       'channel': 'Dallas-Fort Worth Hospital Council',
                       'author': 'Dallas-Fort Worth Hospital Council',
                       'text': 'This is a basic thing, but there are so many times where leases are '
                               "unsigned and it's a common issue that we see.",
                       'tip': 'This is a basic thing, but there are so many times where leases are '
                              "unsigned and it's a common issue that we see.",
                       'timestamp': 2938,
                       'timestamp_seconds': 2938,
                       'timestamp_label': '[00:48:58]',
                       'url': 'https://www.youtube.com/watch?v=_1_drZryqm4&t=2938s',
                       'markdown': '[00:48:58](https://www.youtube.com/watch?v=_1_drZryqm4&t=2938s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q6.'}]}
