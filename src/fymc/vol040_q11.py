from __future__ import annotations

CHAPTER_11 = {'id': 'Q11',
 'chapter_id': 'Q11',
 'chapter_number': 11,
 'question_number': 11,
 'slug': 'workers-comp-experience-mods-and-class-codes',
 'question_prompt': "How is a workers' comp experience mod calculated, and how can an employer read the "
                    'worksheet and classification codes to cut premium?',
 'kicker': 'Q11 / THE BIG MONEY PLAYBOOKS',
 'title': "Workers' Comp Experience Mods and Class Codes",
 'subtitle': 'E-mod formula, primary and excess losses, minimum mod, experience rating worksheets, '
             'California and NCCI formula changes, and how classification codes set premium',
 'layout_template': 'chapter_opener',
 'reading_time_minutes': 15,
 'executive_summary': 'Workers comp brokers, consultants, and a carrier converge on one model: the '
                      'experience mod compares three of your last four years of payroll and claims against '
                      "your industry's expected losses, 1.00 is average, and the factor multiplies "
                      'straight against premium, turning a $100,000 standard premium into $82,000 or '
                      '$122,000. They agree frequency hurts more than severity, medical-only claims enter '
                      'at 30 percent, and a couple of moderate claims can flip a 0.8 to a 1.2 for three '
                      'years. Street mechanics center on the minimum mod (stabilizing value over expected '
                      "totals), state split points like Illinois's $30,000 with W-factor weighting, "
                      "Illinois contractor's credit worth up to 40 percent, and mod and class-code audits, "
                      'with one estimate that 60 to 70 percent of mods are wrong. Practitioners split on '
                      'paying claims outside the system and on funding light duty.',
 'key_metrics': [{'label': 'Share of Mods Estimated to Be Wrong',
                  'metric': 'Share of Mods Estimated to Be Wrong',
                  'value': '60 to 70 percent',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Gordon Coyle reports some experts believe 60 to 70 percent of mods in all '
                             'workers comp policies are wrong, and that the bureau, carrier, and broker '
                             'are not responsible for verifying accuracy.',
                  'source': 'The Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:04:19])'},
                 {'label': 'Medical-Only Claim Weighting',
                  'metric': 'Medical-Only Claim Weighting',
                  'value': '70 percent reduction; $100 claim enters as $30',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Texas Mutual explains a $100 medical-only claim is adjusted by 70 percent so '
                             'only $30 impacts the emod formula.',
                  'source': 'Texas Mutual Insurance Co ([gt3I3IxlEkE @ 00:01:45])'},
                 {'label': 'Illinois Split Point',
                  'metric': 'Illinois Split Point',
                  'value': '$30,000 (Indiana $18,500, Wisconsin $21,500)',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Ryan Hanigan states every dollar up to the split point is 100 percent '
                             'weighted, with dollars above it reduced by the W factor.',
                  'source': 'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:14:58])'},
                 {'label': 'Credit Mod vs Minimum Mod Premium Gap',
                  'metric': 'Credit Mod vs Minimum Mod Premium Gap',
                  'value': '$400,000 at 0.8 vs $200,000 at 0.4 minimum',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Michael Stack shows a $500,000 manual premium company at a 0.8 mod paying '
                             'twice what it could at its 0.4 minimum mod.',
                  'source': "Amaxx | Workers' Comp for Employers ([z2GYx81GGEM @ 00:05:12])"}],
 'sections': [{'title': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner describes the experience mod the same way: a rating '
                              'factor built specifically for your company that compares your claims '
                              'against what is expected for your payroll size and industry, with 1.00 '
                              'sitting at average. Gordon Coyle of The Coyle Group explains that the state '
                              'rating bureau or the NCCI runs three of the last four years of payroll and '
                              'claims data through its formula, producing a number like 0.82 for a credit '
                              'or 1.22 for a debit [V5MJi6gMjSg @ 00:00:53]. Ryan Hanigan of JJ Doorhy & '
                              'Associates frames it bluntly: under one you are better than average and '
                              'earn a premium credit, over one your losses ran above what was expected and '
                              'you eat a debit, and no matter which insurance company writes the policy, '
                              'the same percentage gets applied [cgxTiDoClOs @ 00:01:49]. Coyle adds the '
                              "system's stated purpose: charge employers with more claims than expected "
                              'more, give credits to those with fewer, and use that spread as a lever to '
                              'push employers toward safer workplaces [Nfw1Tq_wDio @ 00:02:14]. Jay '
                              'Roberts of Wade Associates compares the mod to a credit score that pits '
                              'your injury history against every competitor in your state, home builders '
                              'against home builders and trucking against trucking, calling it the '
                              'almighty equalizer behind massive discounts or surcharges [hX_4HXaXi4U @ '
                              '00:00:21].',
                              'The second point of agreement is that the mod is pure multiplication '
                              'against your premium, so the dollar swing scales with your spend. Coyle '
                              'runs two employers with the same $100,000 standard premium: the safe shop '
                              'at 0.82 pays $82,000, the claims-heavy shop at 1.22 pays $122,000, a '
                              '$40,000 penalty for the same payroll [V5MJi6gMjSg @ 00:01:46]. Hanigan '
                              'pushes the math higher with a $500,000 manual premium, where a 0.90 mod '
                              'pulls $50,000 off and a 1.10 mod adds $50,000, a $100,000 swing that lands '
                              'directly on the bottom line [cgxTiDoClOs @ 00:03:15]. Ryan Stillwell of '
                              'Stillwell Risk Partners pulls a real Pennsylvania bar and restaurant policy '
                              'showing a 138.9 percent mod that turns $12,538 of manual premium into '
                              '$17,415, nearly $5,000 extra on a twelve-thousand-dollar policy, and '
                              'estimates a claim-free 0.8 would have flipped that into a $7,500 difference '
                              '[tUclSqTs7E8 @ 00:03:24]. Stillwell also sets a working threshold: once '
                              'workers comp premium runs past $25,000, monitoring the mod starts paying '
                              'off because the multiplier effect and your control both grow. Trent Hess of '
                              'BCF Group warns the move is fast and sticky: a couple of moderate claims '
                              'can take a business from 0.8 to 1.2, and that hit stays for three years '
                              '[c069PHgKa8Y @ 00:01:30].',
                              'The third consensus pillar is that frequency, not severity, is what wrecks '
                              'a mod, and the formula is deliberately built that way. Coyle reduces the '
                              'whole playbook to one line: you lower the mod by having fewer claims, '
                              'period, and those claims can be controlled, though old losses stick until '
                              'they flush out of the three-of-four-year window [V5MJi6gMjSg @ 00:02:58]. '
                              'Hanigan says the formula refuses to punish one fluke accident, so one '
                              '$50,000 claim hurts less than five $10,000 claims carrying the same total '
                              'dollars, and underwriters pricing the account read frequency as the bigger '
                              'red flag too [cgxTiDoClOs @ 00:13:33]. Scott Simmonds walks the actual '
                              'worksheet and makes the same point with smaller numbers: five $1,200 claims '
                              'hit harder than a single $7,000 claim [UkIk-T0NP3M @ 00:02:05]. Jonathan at '
                              'Texas Mutual adds the second built-in discount: the NCCI formula is '
                              'adjusted to lower the impact of severe and medical-only losses, so a $100 '
                              'medical-only claim is cut by 70 percent and only $30 touches the emod, '
                              'while some small losses never move the mod at all [gt3I3IxlEkE @ 00:01:45]. '
                              'The operator takeaway everyone lands on is identical: count claims, keep '
                              'them medical-only where possible, and get injured workers back on the job.'],
               'table': {'caption': 'Where the Practitioners Agree on Experience Mod Basics',
                         'headers': ['Consensus Point',
                                     'How It Works',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Mod benchmarks you against your industry average',
                                   '1.00 is average; below one earns a credit, above one triggers a debit',
                                   'Know your exact mod number before every renewal and every bid',
                                   'Wade Associates ([hX_4HXaXi4U @ 00:00:54])'],
                                  ['Mod multiplies directly against standard or manual premium',
                                   '$100,000 standard premium becomes $82,000 at 0.82 or $122,000 at 1.22',
                                   'Same payroll produces a $40,000 gap driven purely by claims experience',
                                   'The Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:01:46])'],
                                  ['Three of the last four years feed the formula',
                                   'Current policy year, then a gap year, then three preceding years count',
                                   'Every claim follows you for three years, so start safety work '
                                   'immediately',
                                   'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:10:05])'],
                                  ['Frequency is punished harder than severity by design',
                                   'Five $1,200 claims outweigh one $7,000 claim on the mod worksheet',
                                   'Drive claim counts down before chasing big-loss severity numbers',
                                   'Scott Simmonds ([UkIk-T0NP3M @ 00:02:05])'],
                                  ['Medical-only claims enter the formula heavily discounted',
                                   'A $100 medical-only claim is reduced 70 percent to just $30',
                                   'Keep injured workers off lost time whenever the doctor allows it',
                                   'Texas Mutual Insurance Co ([gt3I3IxlEkE @ 00:01:45])'],
                                  ['Mods can be wrong and nobody is assigned to check',
                                   'Bureau, carrier, and broker are not responsible for verifying; some '
                                   'experts estimate 60 to 70 percent are wrong',
                                   'Order a mod audit and verify the bureau data on your own account',
                                   'The Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:04:19])'],
                                  ['Credit-to-debit swing happens fast on only a few claims',
                                   'A couple of moderate claims moves a business from 0.8 to 1.2',
                                   'Treat every moderate claim as a three-year premium event for budgeting',
                                   'BCF Group ([c069PHgKa8Y @ 00:01:30])']]}},
              {'title': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['The sharpest street tool is the minimum mod, the number you would carry '
                              'with zero injuries and zero claim costs. Michael Stack, CEO of Amaxx, pulls '
                              'just two numbers off the NCCI rating worksheet: divide the stabilizing '
                              'value by the expected totals and you have your lowest possible mod '
                              "[z2GYx81GGEM @ 00:01:47]. Stack's board example takes $10 million of "
                              'payroll at a 5.05 class rate, lands manual premium at $500,000, and shows a '
                              '0.8 mod producing $400,000; if the minimum is 0.4, that same premium could '
                              'be $200,000, meaning the company celebrating its credit mod is paying twice '
                              'what it could, and larger organizations tend to have lower minimums because '
                              'of the weighting value [z2GYx81GGEM @ 00:05:12]. Jay Roberts runs a smaller '
                              'version: a business paying $100,000 with a 0.91 mod whose minimum is 0.71 '
                              'still has another 20 percent of room, and Roberts insists you never settle '
                              'just because you are under one [dLKCbT6-S3c @ 00:01:17]. Coyle stretches it '
                              'further with a $200,000 account at 1.10 and a 0.77 minimum, a 33-point '
                              'spread worth at least $60,000, plus roughly $20,000 more from competitive '
                              'rating tiers, which practically halves premium [njIghi8P9jQ @ 00:01:46].',
                              'The mechanic behind frequency weighting is the split point. Simmonds walks '
                              'the worksheet: any loss over $5,000 carries into the actual primary losses '
                              'column at only $5,000, so a $10,000 claim moves over at $5,000, and open '
                              'claims count paid dollars plus reserves [UkIk-T0NP3M @ 00:03:44]. '
                              'ClinardInsGroup reports the NCCI phase-in beginning in 2012, raising that '
                              '$5,000 frequency cap each year until it reached $17,000 in 2015, then '
                              'indexing it for inflation, so more of every loss now lands on the frequency '
                              'side [-hUWvUBIr1A @ 00:01:36]. Hanigan gives current state split points of '
                              '$30,000 in Illinois, $18,500 in Indiana, and $21,500 in Wisconsin: every '
                              'dollar up to the split counts at 100 percent, and above it only the W '
                              'factor share enters. With a W of 0.40, a $50,000 Illinois claim sends '
                              '$30,000 plus $8,000 into the formula while 60 percent of the excess is '
                              'thrown out [cgxTiDoClOs @ 00:15:39]. Hanigan then adds two levers that '
                              'matter at the desk: medical-only claims enter at 30 cents on the dollar, so '
                              'a $25,000 claim with the worker on light duty counts as $7,500, and open '
                              'reserves are locked in exactly like paid dollars when loss runs go to NCCI '
                              '[cgxTiDoClOs @ 00:16:45].',
                              'The payroll side of the equation gets its own street mechanics. Coyle says '
                              'the business, not individual job tasks, sets the governing classification: '
                              'a New York landscaper sits in 0042 for mowing, hedge trimming and planting '
                              'alike, with clerical office staff split into 8810 as the common exception, '
                              'and rates stack state loss costs with insurer loss cost multipliers that '
                              'big carriers run in 5 to 12 tiered versions [7sfUUlxeHHk @ 00:03:54]. '
                              'WorkCompConsultants counts roughly 700 codes across state rating '
                              'authorities, each with its own rate, and pushes a proactive code review '
                              'before an auditor finds the misclassification and bills it as large '
                              'additional premium [tkOuTso-3RA @ 00:01:52]. On the mod itself, Coyle '
                              'describes contingency audit consultants who look back up to three years for '
                              'errors, earn refunds on prior policies, and keep 50 percent of those '
                              'refunds as their fee, versus specialist brokers who verify mods for '
                              'committed new clients with no fee [V5MJi6gMjSg @ 00:04:37]. Fusco On '
                              'Insurance adds a timing trap: if payroll audits run late, only losses or '
                              'expected losses reach the WCIRB without your payroll, making the California '
                              'E-Mod look worse, so Fusco drives audits to finish on time and runs reports '
                              'to check bureau data [8Reu6Q_HdTE @ 00:03:59].'],
               'table': {'caption': 'Street Mechanics, Formulas and Dollar Figures Practitioners Use',
                         'headers': ['Mechanic', 'Exact Numbers', 'How Operators Use It', 'Expert Source'],
                         'rows': [['Minimum mod formula pulled from the NCCI worksheet',
                                   'Stabilizing value divided by expected totals equals the lowest '
                                   'possible mod',
                                   'Sets the zero-claim floor and shows how much savings room remains',
                                   "Amaxx | Workers' Comp for Employers ([z2GYx81GGEM @ 00:01:47])"],
                                  ['Minimum mod payoff on a midsize workers comp account',
                                   '$200,000 premium at 1.10 versus a 0.77 minimum saves at least $60,000',
                                   'Gives leadership a concrete bogey and a road map to build toward',
                                   'The Coyle Group - Business Insurance ([njIghi8P9jQ @ 00:01:46])'],
                                  ['State split points combined with the W factor',
                                   '$30,000 Illinois, $18,500 Indiana, $21,500 Wisconsin; W of 0.40 '
                                   'example',
                                   'Only 40 cents of each excess dollar above the split enters the formula',
                                   'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:14:58])'],
                                  ["Illinois union contractor's credit stacked after the mod",
                                   '1 to 40 percent extra credit, about 30 percent average, only at 1.00 '
                                   'or below',
                                   'Same $200,000 contractor pays $126,000 at 0.90 versus $220,000 at 1.10',
                                   'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:08:39])'],
                                  ['Primary loss cap on the experience mod worksheet',
                                   'Losses over $5,000 are carried into the primary column at $5,000 only',
                                   'Match loss run claim numbers to worksheet rows line by line for errors',
                                   'Scott Simmonds ([UkIk-T0NP3M @ 00:02:42])'],
                                  ['Mod audit contingency economics for prior policy refunds',
                                   'Consultants look back up to three years and keep 50 percent of refunds',
                                   'Compare against specialist brokers who verify mods free for new '
                                   'clients',
                                   'The Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:04:54])'],
                                  ['Rate structure behind each four-digit class code',
                                   'State loss costs times insurer LCMs, with 5 to 12 tiered versions per '
                                   'carrier',
                                   'Have a skilled broker submit to the right underwriters for a firm '
                                   'quote',
                                   'The Coyle Group - Business Insurance ([7sfUUlxeHHk @ 00:06:37])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Keeping Claim Dollars Out of the Formula',
                           'body': 'The working brokers lean on a handful of desk-level moves that shrink '
                                   'what the rating bureau ever sees and how the mod gets read by buyers.',
                           'items': ['In many states the claims impact on the mod drops dramatically '
                                     'without lost time, so it may make sense to pay an injured employee '
                                     'who cannot work for several days to avoid getting hammered by the '
                                     'mod, though Coyle says this takes finesse [The Coyle Group - '
                                     'Business Insurance — Nfw1Tq_wDio @ 00:05:27].',
                                     'Offer doctor-approved light duty: once approved the worker cannot '
                                     'refuse it, many dislike desk or nonprofit placements and heal '
                                     'faster, and some carriers partner with nonprofits so those indemnity '
                                     'dollars stay off loss runs and out of the mod [JJ Doorhy & '
                                     'Associates — cgxTiDoClOs @ 00:18:28].',
                                     'When a mod above 1.0 threatens bid eligibility with a general '
                                     'contractor, brokers can run tools showing what the mod would be '
                                     "without one shock loss and advocate on the contractor's behalf [JJ "
                                     'Doorhy & Associates — cgxTiDoClOs @ 00:05:26].',
                                     'Place comp with dedicated work comp carriers that run their own '
                                     'nurses and caseworkers, because they push injured workers back '
                                     'sooner and the higher frequency cap puts more of each loss on the '
                                     'frequency side [ClinardInsGroup — -hUWvUBIr1A @ 00:02:10].']},
               'sop_steps': [{'step': 1,
                              'title': 'Pull the Loss Runs and Mod Worksheet',
                              'action': 'Request five years of loss runs plus the current experience '
                                        'rating worksheet and reconcile them claim by claim.',
                              'detail': 'Coyle names nobody watching claims as the most common employer '
                                        'mistake and says to ask the broker for five years of loss runs '
                                        'and a sit-down explanation [The Coyle Group - Business Insurance '
                                        '— Nfw1Tq_wDio @ 00:07:51]; Simmonds lines up claim numbers on the '
                                        'loss run against each worksheet row [Scott Simmonds — UkIk-T0NP3M '
                                        '@ 00:02:42].'},
                             {'step': 2,
                              'title': 'Compute the Minimum Mod and the Dollar Gap',
                              'action': 'Divide the stabilizing value by expected totals, then multiply '
                                        'manual premium by both the current and minimum mod.',
                              'detail': 'Stack uses this calculation to show a 0.8 mod company at $400,000 '
                                        'that could pay $200,000 at its 0.4 minimum, a vivid number for '
                                        "senior managers [Amaxx | Workers' Comp for Employers — "
                                        'z2GYx81GGEM @ 00:05:34].'},
                             {'step': 3,
                              'title': 'Audit Mod Accuracy, Reserves and Class Codes',
                              'action': 'Verify bureau data, challenge inflated reserves, and confirm the '
                                        'carrier is not misclassifying employees.',
                              'detail': 'Coyle offers contingency consultants at 50 percent of refunds or '
                                        'a specialist broker for prior-year error recovery [The Coyle '
                                        'Group - Business Insurance — V5MJi6gMjSg @ 00:04:37]; Hanigan '
                                        'says misclassified class codes and payroll happen more often than '
                                        'you might think [JJ Doorhy & Associates — cgxTiDoClOs @ '
                                        '00:22:24].'},
                             {'step': 4,
                              'title': 'Run the Forward Claim-Control Playbook',
                              'action': 'Report claims immediately, triage with a nurse, return workers on '
                                        'light duty, and aggressively close open claims.',
                              'detail': 'Hanigan lists fast reporting, light duty, closing claims, cutting '
                                        'frequency, and fighting questionable claims [JJ Doorhy & '
                                        'Associates — cgxTiDoClOs @ 00:21:33]; Coyle adds nurse triage on '
                                        'every claim to control costs and outcomes [The Coyle Group - '
                                        'Business Insurance — Nfw1Tq_wDio @ 00:05:10].'}]},
              {'heading': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The sharpest split is over what to do with a small injury before it ever '
                              'reaches the formula. Gordon Coyle of The Coyle Group says that in many '
                              'states the mod impact drops dramatically if no lost time is incurred, so it '
                              'may make sense to pay an injured employee who cannot work for several days '
                              'so the business does not get hammered by the mod, while admitting the move '
                              'takes some finesse [Nfw1Tq_wDio @ 00:05:27]. Jonathan at Texas Mutual takes '
                              'the opposite line: paying benefits directly to the worker or medical '
                              'provider and leaving the carrier out is legal, but not a great idea. The '
                              'employer can lose negotiated medical savings from the Texas Star Network, '
                              'trigger penalties by wrongly denying or reducing benefits, overpay, invite '
                              'abusive claims from other employees, and accrue penalties for failing to '
                              'report Medicare information. The verdict: the juice is just not worth the '
                              'squeeze [gt3I3IxlEkE @ 00:03:08]. Ryan Hanigan of JJ Doorhy & Associates '
                              'runs a third playbook: report the claim but keep indemnity off the loss '
                              'runs through light duty, including carriers partnered with nonprofits where '
                              'the employer pays the worker to work at the nonprofit [cgxTiDoClOs @ '
                              '00:18:28]. Hanigan says the math is strongest for high-deductible or '
                              'alternative risk clients, who pay those dollars anyway up to, for example, '
                              'a $500,000 per-claim deductible [cgxTiDoClOs @ 00:19:18].',
                              'On how often the mod is wrong, the same firm gives two different '
                              'temperatures. In one video Gordon Coyle cites experts who believe 60 to 70 '
                              'percent of mods in all workers comp policies are wrong, and stresses that '
                              'the rating bureau, the carrier using the mod, and the broker selling the '
                              'policy are not responsible for verifying its accuracy [V5MJi6gMjSg @ '
                              '00:04:19]. In another, Coyle says the old hand-calculated worksheets were '
                              "prone to errors, while today's software-driven formula still produces "
                              'errors but less often, so the recommendation softens to an audit every '
                              'couple of years to avoid overpaying [Nfw1Tq_wDio @ 00:04:20]. The payment '
                              'model splits too: contingency mod-audit consultants look back up to three '
                              'years for errors on prior policies and typically keep fifty percent of the '
                              'refunds, while specialist brokers like Coyle run the same accuracy check '
                              'and refund look-back for new clients with no fee or contingency, pitched as '
                              'a value-add to the relationship [V5MJi6gMjSg @ 00:04:37]. In California, '
                              'Fusco On Insurance keeps verification in-house, working with carriers and '
                              'the WCIRB, generating reports to confirm the data the WCIRB received is '
                              'correct, and running reporting tools to project future mods [8Reu6Q_HdTE @ '
                              '00:02:18]. The operator choice is between surrendering half of any refund '
                              'and committing the account to a specialist broker.',
                              'The frequency-over-severity mechanic is universal, but the dollar line '
                              'where a loss stops counting in full depends on whose worksheet is on the '
                              'table. Scott Simmonds walks a worksheet where any loss over $5,000 carries '
                              'into actual primary losses at only $5,000, so a $10,000 claim moves over at '
                              '$5,000 and five $1,200 claims hurt more than one $7,000 claim [UkIk-T0NP3M '
                              '@ 00:03:44]. ClinardInsGroup describes the NCCI phase-in that raised that '
                              'old $5,000 cap gradually from 2012 until it hit $17,000 in 2015, then '
                              'indexed it for inflation, pushing more of every loss onto the frequency '
                              'side and making fast return to work even more valuable [-hUWvUBIr1A @ '
                              '00:01:36]. Ryan Hanigan quotes split points of $30,000 in Illinois, $18,500 '
                              'in Indiana and $21,500 in Wisconsin, with an illustrative 0.40 W factor '
                              'letting only 40 cents of each excess dollar into the formula [cgxTiDoClOs @ '
                              '00:14:35]. The carrier playbook diverges from there: Clinard prefers '
                              'dedicated work comp companies with their own nurses and caseworkers because '
                              "they push injured workers back sooner, warning that today's premium may "
                              'matter less than what a carrier that does not actively manage claims costs '
                              'down the road [-hUWvUBIr1A @ 00:02:10].'],
               'table': {'caption': 'Competing playbooks on claims handling, mod audits, frequency caps '
                                    'and placement',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Small lost-time injury before it reaches the formula',
                                   'Pay the injured employee for several days off so lost time never '
                                   'hammers the mod, using some finesse',
                                   'Always report the claim because self-paying risks lost network '
                                   'savings, penalties, overpayment and abusive claims',
                                   'The Coyle Group - Business Insurance ([Nfw1Tq_wDio @ 00:05:27]); Texas '
                                   'Mutual Insurance Co ([gt3I3IxlEkE @ 00:02:19])'],
                                  ['Injured skilled worker cleared by the doctor for light duty',
                                   'Some employers refuse to pay a skilled worker to basically sit in the '
                                   'office',
                                   'Offer clerical light duty or a paid nonprofit placement so indemnity '
                                   'dollars never reach the loss runs',
                                   'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:17:33]); JJ Doorhy & '
                                   'Associates ([cgxTiDoClOs @ 00:18:28])'],
                                  ['Who checks the mod for errors and how they get paid',
                                   'Contingency mod-audit consultant reviews up to three years back and '
                                   'keeps fifty percent of refunds',
                                   'Specialist broker verifies the mod and hunts refunds for new clients '
                                   'with no fee or contingency',
                                   'The Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:04:37]); The '
                                   'Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:04:54])'],
                                  ['How often experience mods are actually calculated wrong',
                                   'Experts cited believe 60 to 70 percent of mods across all workers comp '
                                   'policies are wrong',
                                   'Software calculation means errors still occur but less often, so audit '
                                   'every couple of years',
                                   'The Coyle Group - Business Insurance ([V5MJi6gMjSg @ 00:04:19]); The '
                                   'Coyle Group - Business Insurance ([Nfw1Tq_wDio @ 00:04:38])'],
                                  ['Dollar line where a single loss stops counting in full',
                                   'Worksheet caps primary losses at $5,000 per claim, with the old NCCI '
                                   'cap phased up to $17,000',
                                   'Split points of $30,000 Illinois, $18,500 Indiana and $21,500 '
                                   'Wisconsin with W factor weighting above',
                                   'Scott Simmonds ([UkIk-T0NP3M @ 00:03:44]); ClinardInsGroup '
                                   '([-hUWvUBIr1A @ 00:01:36]); JJ Doorhy & Associates ([cgxTiDoClOs @ '
                                   '00:14:35])'],
                                  ['Who runs the minimum mod calculation for the business',
                                   'Divide the stabilizing value by expected totals straight off the NCCI '
                                   'rating worksheet yourself',
                                   'Hand the data to a broker; if the current broker never computed it, '
                                   'they likely cannot help',
                                   "Amaxx | Workers' Comp for Employers ([z2GYx81GGEM @ 00:01:47]); The "
                                   'Coyle Group - Business Insurance ([njIghi8P9jQ @ 00:02:20]); Wade '
                                   'Associates ([dLKCbT6-S3c @ 00:01:52])'],
                                  ['Where to place the workers comp policy itself',
                                   'Online or payroll-provider purchase often delivers little support, and '
                                   'portal-suggested codes may cost more',
                                   'Dedicated work comp carrier with in-house nurses, placed through a '
                                   'skilled broker who audits the codes',
                                   'The Coyle Group - Business Insurance ([Nfw1Tq_wDio @ 00:08:21]); '
                                   'ClinardInsGroup ([-hUWvUBIr1A @ 00:02:10]); The Coyle Group - Business '
                                   'Insurance ([7sfUUlxeHHk @ 00:09:16])']]}},
              {'heading': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common failure Gordon Coyle finds when stepping into a new account '
                              'is that nobody is watching claims: not the CEO, the CFO, the controller or '
                              'the HR manager. No one knows how many claims hit in the past four years, '
                              'how much was paid, what the reserves are, or how to stop repeats, and the '
                              'fix is pulling five years of loss runs and making the broker sit down and '
                              'explain them [Nfw1Tq_wDio @ 00:07:19]. That blindness is expensive because '
                              'Ryan Hanigan says open reserves and paid dollars are not differentiated: '
                              'once loss runs go to NCCI, a $50,000 reserve is locked in and treated '
                              'exactly like $50,000 paid, so inflated reserves directly inflate the mod '
                              '[cgxTiDoClOs @ 00:12:03]. Scott Simmonds shows the same mechanic on the '
                              'worksheet itself, where an open claim, flagged O rather than F for final, '
                              'carries payments already made plus the reserves the carrier expects to pay '
                              'later [UkIk-T0NP3M @ 00:03:24]. Lag time compounds the damage: Hanigan '
                              'cites NCCI and Liberty Mutual data showing late-reported claims cost more, '
                              'because slow adjuster contact leaves the injured worker worried about being '
                              'taken care of and more likely to hire an attorney, which pushes expense '
                              'costs even higher [cgxTiDoClOs @ 00:21:02].',
                              'Class codes produce the most violent reversals, and they surface at audit. '
                              'Gordon Coyle describes owners buying directly online who try to rig the '
                              'system, intentionally or accidentally misclassifying to get a lower '
                              'premium; it works only until the audit, when insurers can go back up to '
                              'three years, charge the correct class rate, bill it in one chunk, and in '
                              'some states assess penalties on top [7sfUUlxeHHk @ 00:08:11]. The '
                              'subcontractor version is quieter: a small sub may carry a policy that '
                              'covers only clerical employees and excludes the owners, so when the hiring '
                              "business submits that certificate at audit, the sub's work gets charged at "
                              "the higher-cost carpenter class rate on the hiring business's own policy "
                              '[7sfUUlxeHHk @ 00:08:42]. WorkCompConsultants warns against assuming codes '
                              'are correct and waiting until an auditor discovers a misclassification, '
                              'because the correction arrives as a large additional premium bill due at '
                              'audit time [tkOuTso-3RA @ 00:01:52]. Audit timing creates its own trap in '
                              'California: Fusco On Insurance says that when audits are delayed, payroll '
                              'never gets reported to the WCIRB while losses or expected losses do, making '
                              'the rating ratio and the E-Mod look worse than they really are [8Reu6Q_HdTE '
                              '@ 00:03:59].',
                              'The economics trap that fools strong performers is complacency below 1.0. '
                              'Michael Stack of Amaxx runs a $10 million payroll at a 5.05 rate into '
                              '$500,000 of manual premium; a 0.8 mod cuts that to $400,000 and the team '
                              'throws a parade, but if the minimum mod is 0.4 the floor is $200,000, '
                              'meaning the company is still paying twice what it could with zero claim '
                              'costs [z2GYx81GGEM @ 00:05:12]. On the other side of 1.0 the penalty is a '
                              'cliff, not a slope: Ryan Hanigan says a mod above one can bar a contractor '
                              'from even bidding, and Illinois union contractors at 1.00 or below can '
                              "stack a contractor's credit of 1 to 40 percent, around 30 percent on "
                              'average, so a same-size contractor pays $126,000 at a 0.9 mod but $220,000 '
                              'at 1.10, and even a 1.01 forfeits the credit [cgxTiDoClOs @ 00:09:20]. '
                              "Small policies feel it too: Ryan Stillwell's Pennsylvania bar and "
                              'restaurant example multiplies $12,538 by a 1.389 mod to reach $17,415, '
                              'nearly $5,000 extra [tUclSqTs7E8 @ 00:03:24]. Trent Hess of BCF Group adds '
                              'that only a couple of moderate claims can swing a business from 0.8 to 1.2, '
                              'and it sticks for three years [c069PHgKa8Y @ 00:01:30].'],
               'table': {'caption': 'Firsthand traps that inflate the mod or trigger audit rebills, with '
                                    'the dollar check',
                         'headers': ['Failure Mode', 'What Happened', 'Economics Check', 'Expert Source'],
                         'rows': [['No one inside the company monitoring claims history',
                                   'CEO, CFO, controller and HR cannot say how many claims occurred in '
                                   'four years',
                                   'Pull five years of loss runs and make the broker explain the report',
                                   'The Coyle Group - Business Insurance ([Nfw1Tq_wDio @ 00:07:19])'],
                                  ['Inflated open reserves locked into the loss runs',
                                   'A $50,000 reserve reaches NCCI and counts exactly like $50,000 '
                                   'actually paid out',
                                   'Have the broker challenge reserves and aggressively close open claims '
                                   'before data locks',
                                   'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:12:03]); JJ Doorhy & '
                                   'Associates ([cgxTiDoClOs @ 00:21:50])'],
                                  ['Self-selected class codes bought online without a broker',
                                   'Owner misclassifies the policy for a lower premium until the audit '
                                   'catches it',
                                   'Insurers can rebill up to three years in one chunk, plus penalties in '
                                   'some states',
                                   'The Coyle Group - Business Insurance ([7sfUUlxeHHk @ 00:08:11])'],
                                  ['Accepting subcontractor certificates at face value',
                                   "Sub's policy covers only clerical employees and excludes the owners "
                                   'when audited',
                                   "The hiring business gets charged the sub's work at the higher "
                                   'carpenter class rate',
                                   'The Coyle Group - Business Insurance ([7sfUUlxeHHk @ 00:08:59])'],
                                  ['Delayed payroll audits in California',
                                   'Payroll never reaches the WCIRB while losses and expected losses still '
                                   'get reported',
                                   'The E-Mod looks worse than reality, so audits must be finished on time',
                                   'Fusco On Insurance ([8Reu6Q_HdTE @ 00:03:59])'],
                                  ['Mod creeping just above 1.00 for a union contractor',
                                   "Contractor gets barred from bids and loses Illinois contractor's "
                                   'credit even at 1.01',
                                   'Same-size contractor pays $220,000 instead of $126,000 in workers comp '
                                   'premium',
                                   'JJ Doorhy & Associates ([cgxTiDoClOs @ 00:08:39]); JJ Doorhy & '
                                   'Associates ([cgxTiDoClOs @ 00:09:20])'],
                                  ['Paying small claims out of pocket to protect the mod',
                                   'Employer leaves the carrier out and pays benefits directly to the '
                                   'worker or provider',
                                   'Lost network savings, overpayment, abusive claims and Medicare '
                                   'reporting penalties outweigh the savings',
                                   'Texas Mutual Insurance Co ([gt3I3IxlEkE @ 00:02:51]); Texas Mutual '
                                   'Insurance Co ([gt3I3IxlEkE @ 00:03:08])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Operator Gate: Clear These Before Renewal and Audit',
                           'body': 'Each gate maps to a loss practitioners watched clients absorb '
                                   'firsthand: blind claims files, locked-in reserves, audit rebills on '
                                   'bad codes, and self-paid claims that backfired.',
                           'items': ['Confirm someone owns claims monitoring and has the last five years '
                                     'of loss runs explained line by line by the broker [The Coyle Group - '
                                     'Business Insurance — Nfw1Tq_wDio @ 00:07:36].',
                                     'Before loss data goes to NCCI, verify every open reserve is '
                                     'appropriate and not inflated, since reserves count the same as paid '
                                     'dollars [JJ Doorhy & Associates — cgxTiDoClOs @ 00:12:21].',
                                     'Run a class code review and check every subcontractor certificate '
                                     'for excluded owners and clerical-only coverage before the auditor '
                                     'does [WorkCompConsultants — tkOuTso-3RA @ 00:01:52]; [The Coyle '
                                     'Group - Business Insurance — 7sfUUlxeHHk @ 00:08:42].',
                                     'Before paying a small claim directly, weigh lost Texas Star Network '
                                     'savings, overpayment, abusive claims and Medicare penalties against '
                                     'the mod hit [Texas Mutual Insurance Co — gt3I3IxlEkE @ '
                                     '00:02:34].']}}],
 'pull_quote': "The mod can be your friend or it can be your foe; it's up to you which it's going to be. — "
               'The Coyle Group - Business Insurance (V5MJi6gMjSg @ 00:02:39)',
 'diagram_id': 'diag-06',
 'action_checklist': ['Calculate the minimum mod by dividing the stabilizing value by expected totals on '
                      'the NCCI rating worksheet, then price the gap against current premium (Amaxx | '
                      "Workers' Comp for Employers, z2GYx81GGEM @ 00:01:47).",
                      'Request five years of loss runs from the broker and have them walk through claim '
                      'counts, payouts and reserves with leadership (The Coyle Group - Business Insurance, '
                      'Nfw1Tq_wDio @ 00:07:36).',
                      'Report every claim as quickly as possible so the adjuster reaches the injured '
                      'worker before an attorney gets involved (JJ Doorhy & Associates, cgxTiDoClOs @ '
                      '00:20:28).',
                      'Stand up a return-to-work and light duty program so claims close as medical-only, '
                      'where only 30 cents on the dollar enters the formula (JJ Doorhy & Associates, '
                      'cgxTiDoClOs @ 00:16:45).',
                      'Audit the experience mod for accuracy every couple of years and pursue refunds on '
                      'prior policy errors (The Coyle Group - Business Insurance, Nfw1Tq_wDio @ 00:04:38).',
                      'Audit class codes starting from the governing classification and run the research '
                      'past underwriters and audit departments before audit time (The Coyle Group - '
                      'Business Insurance, 7sfUUlxeHHk @ 00:05:02).'],
 'statutory_citations': [{'title': 'The Coyle Group - Business Insurance — What is the Workers Comp '
                                   'Experience Mod? [00:04:19]',
                          'url': 'https://www.youtube.com/watch?v=V5MJi6gMjSg&t=259s',
                          'relevance': 'Primary practitioner testimony on mod error rates, contingency mod '
                                       'audits and the 50 percent refund fee model.'},
                         {'title': 'JJ Doorhy & Associates — How Your EMR Actually Works | The Formula '
                                   "Behind Your Workers' Comp Mod [00:14:35]",
                          'url': 'https://www.youtube.com/watch?v=cgxTiDoClOs&t=875s',
                          'relevance': 'Primary practitioner testimony on state split points, W factor '
                                       "weighting, reserves and contractor's credit economics."},
                         {'title': 'The Coyle Group - Business Insurance — Workers Comp Class Codes, What '
                                   'Are They For? 2026 [00:08:11]',
                          'url': 'https://www.youtube.com/watch?v=7sfUUlxeHHk&t=491s',
                          'relevance': 'Primary practitioner testimony on misclassification rebills at '
                                       'audit and subcontractor certificate traps.'},
                         {'title': "Amaxx | Workers' Comp for Employers — How to Calculate Your Minimum "
                                   'Experience Modification Factor [00:05:12]',
                          'url': 'https://www.youtube.com/watch?v=z2GYx81GGEM&t=312s',
                          'relevance': 'Primary practitioner testimony on the minimum mod calculation and '
                                       'complacency below 1.0.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'V5MJi6gMjSg',
                       'title': 'What is the Workers Comp Experience Mod?',
                       'channel': 'The Coyle Group - Business Insurance',
                       'author': 'The Coyle Group - Business Insurance',
                       'text': 'Some experts believe that 60 to 70 percent of mods in all workers comp '
                               'policies are wrong.',
                       'tip': 'Some experts believe that 60 to 70 percent of mods in all workers comp '
                              'policies are wrong.',
                       'timestamp': 259,
                       'timestamp_seconds': 259,
                       'timestamp_label': '[00:04:19]',
                       'url': 'https://www.youtube.com/watch?v=V5MJi6gMjSg&t=259s',
                       'markdown': '[00:04:19](https://www.youtube.com/watch?v=V5MJi6gMjSg&t=259s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z2GYx81GGEM',
                       'title': 'How to Calculate Your Minimum Experience Modification Factor',
                       'channel': "Amaxx | Workers' Comp for Employers",
                       'author': "Amaxx | Workers' Comp for Employers",
                       'text': "You take that stabilizing value over your expected totals, and that's how "
                               'you calculate your lowest possible or minimum mod.',
                       'tip': "You take that stabilizing value over your expected totals, and that's how "
                              'you calculate your lowest possible or minimum mod.',
                       'timestamp': 107,
                       'timestamp_seconds': 107,
                       'timestamp_label': '[00:01:47]',
                       'url': 'https://www.youtube.com/watch?v=z2GYx81GGEM&t=107s',
                       'markdown': '[00:01:47](https://www.youtube.com/watch?v=z2GYx81GGEM&t=107s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'z2GYx81GGEM',
                       'title': 'How to Calculate Your Minimum Experience Modification Factor',
                       'channel': "Amaxx | Workers' Comp for Employers",
                       'author': "Amaxx | Workers' Comp for Employers",
                       'text': "In essence what this means is you're paying twice as much as you could if "
                               'you had zero claim costs.',
                       'tip': "In essence what this means is you're paying twice as much as you could if "
                              'you had zero claim costs.',
                       'timestamp': 312,
                       'timestamp_seconds': 312,
                       'timestamp_label': '[00:05:12]',
                       'url': 'https://www.youtube.com/watch?v=z2GYx81GGEM&t=312s',
                       'markdown': '[00:05:12](https://www.youtube.com/watch?v=z2GYx81GGEM&t=312s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'KAFn9iNy8cA',
                       'title': 'WORKERS COMP X-MOD | Demystifying The Experience Modification on Workers '
                                'Compensation Insurance',
                       'channel': 'Colony Solutions - Business Insurance',
                       'author': 'Colony Solutions - Business Insurance',
                       'text': 'You get a 10% credit on your workers comp rate, and if you have a horrible '
                               'loss your x-mod is gonna shoot up until it could come back down.',
                       'tip': 'You get a 10% credit on your workers comp rate, and if you have a horrible '
                              'loss your x-mod is gonna shoot up until it could come back down.',
                       'timestamp': 162,
                       'timestamp_seconds': 162,
                       'timestamp_label': '[00:02:42]',
                       'url': 'https://www.youtube.com/watch?v=KAFn9iNy8cA&t=162s',
                       'markdown': '[00:02:42](https://www.youtube.com/watch?v=KAFn9iNy8cA&t=162s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Nfw1Tq_wDio',
                       'title': 'Workers Comp ERM or E-Mod Explained',
                       'channel': 'The Coyle Group - Business Insurance',
                       'author': 'The Coyle Group - Business Insurance',
                       'text': 'It may make sense to pay an employee who is injured and unable to work for '
                               "several days so that you don't get hammered by the mod, but this does take "
                               'some finesse.',
                       'tip': 'It may make sense to pay an employee who is injured and unable to work for '
                              "several days so that you don't get hammered by the mod, but this does take "
                              'some finesse.',
                       'timestamp': 327,
                       'timestamp_seconds': 327,
                       'timestamp_label': '[00:05:27]',
                       'url': 'https://www.youtube.com/watch?v=Nfw1Tq_wDio&t=327s',
                       'markdown': '[00:05:27](https://www.youtube.com/watch?v=Nfw1Tq_wDio&t=327s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Nfw1Tq_wDio',
                       'title': 'Workers Comp ERM or E-Mod Explained',
                       'channel': 'The Coyle Group - Business Insurance',
                       'author': 'The Coyle Group - Business Insurance',
                       'text': 'The most common mistake made by employers large and small is that no one '
                               'has been monitoring the claims experience.',
                       'tip': 'The most common mistake made by employers large and small is that no one '
                              'has been monitoring the claims experience.',
                       'timestamp': 423,
                       'timestamp_seconds': 423,
                       'timestamp_label': '[00:07:03]',
                       'url': 'https://www.youtube.com/watch?v=Nfw1Tq_wDio&t=423s',
                       'markdown': '[00:07:03](https://www.youtube.com/watch?v=Nfw1Tq_wDio&t=423s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cgxTiDoClOs',
                       'title': "How Your EMR Actually Works | The Formula Behind Your Workers' Comp Mod",
                       'channel': 'JJ Doorhy & Associates',
                       'author': 'JJ Doorhy & Associates',
                       'text': "In Illinois the split point is $30,000, Indiana it's $18,500, Wisconsin "
                               "it's $21,500.",
                       'tip': "In Illinois the split point is $30,000, Indiana it's $18,500, Wisconsin "
                              "it's $21,500.",
                       'timestamp': 875,
                       'timestamp_seconds': 875,
                       'timestamp_label': '[00:14:35]',
                       'url': 'https://www.youtube.com/watch?v=cgxTiDoClOs&t=875s',
                       'markdown': '[00:14:35](https://www.youtube.com/watch?v=cgxTiDoClOs&t=875s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cgxTiDoClOs',
                       'title': "How Your EMR Actually Works | The Formula Behind Your Workers' Comp Mod",
                       'channel': 'JJ Doorhy & Associates',
                       'author': 'JJ Doorhy & Associates',
                       'text': 'You could have a $50,000 reserve on a claim and you could have $50,000 '
                               "paid out on a claim, and it's going to impact you the same.",
                       'tip': 'You could have a $50,000 reserve on a claim and you could have $50,000 paid '
                              "out on a claim, and it's going to impact you the same.",
                       'timestamp': 723,
                       'timestamp_seconds': 723,
                       'timestamp_label': '[00:12:03]',
                       'url': 'https://www.youtube.com/watch?v=cgxTiDoClOs&t=723s',
                       'markdown': '[00:12:03](https://www.youtube.com/watch?v=cgxTiDoClOs&t=723s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tUclSqTs7E8',
                       'title': 'What is the Workers Comp Experience Modification Rate - and why should '
                                'you care?',
                       'channel': 'Stillwell Risk Partners',
                       'author': 'Stillwell Risk Partners',
                       'text': "12,538 times 138.9 percent gives you 17,415, and that's an additional "
                               'premium of almost five thousand dollars.',
                       'tip': "12,538 times 138.9 percent gives you 17,415, and that's an additional "
                              'premium of almost five thousand dollars.',
                       'timestamp': 204,
                       'timestamp_seconds': 204,
                       'timestamp_label': '[00:03:24]',
                       'url': 'https://www.youtube.com/watch?v=tUclSqTs7E8&t=204s',
                       'markdown': '[00:03:24](https://www.youtube.com/watch?v=tUclSqTs7E8&t=204s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'dLKCbT6-S3c',
                       'title': 'The Workers Compensation Experience Mod | How Low Can It Go?',
                       'channel': 'Wade Associates',
                       'author': 'Wade Associates',
                       'text': 'What if your minimum mod was actually 0.71? That would mean that you have '
                               'room to lower your workers comp cost by another 20 percent.',
                       'tip': 'What if your minimum mod was actually 0.71? That would mean that you have '
                              'room to lower your workers comp cost by another 20 percent.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=dLKCbT6-S3c&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=dLKCbT6-S3c&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'hX_4HXaXi4U',
                       'title': 'What is the Workers Comp EXPERIENCE MOD?',
                       'channel': 'Wade Associates',
                       'author': 'Wade Associates',
                       'text': 'The mod ultimately determines how much you pay for workers comp; it is the '
                               'almighty equalizer that results in either massive discounts or massive '
                               'surcharges.',
                       'tip': 'The mod ultimately determines how much you pay for workers comp; it is the '
                              'almighty equalizer that results in either massive discounts or massive '
                              'surcharges.',
                       'timestamp': 71,
                       'timestamp_seconds': 71,
                       'timestamp_label': '[00:01:11]',
                       'url': 'https://www.youtube.com/watch?v=hX_4HXaXi4U&t=71s',
                       'markdown': '[00:01:11](https://www.youtube.com/watch?v=hX_4HXaXi4U&t=71s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'c069PHgKa8Y',
                       'title': 'Workers’ Comp Experience Modification Factor. What you need to know.',
                       'channel': 'BCF Group',
                       'author': 'BCF Group',
                       'text': 'It only takes a couple moderate workers comp claims in order to go from a '
                               '0.8 to a 1.2 mod, and it sticks with you for three years.',
                       'tip': 'It only takes a couple moderate workers comp claims in order to go from a '
                              '0.8 to a 1.2 mod, and it sticks with you for three years.',
                       'timestamp': 72,
                       'timestamp_seconds': 72,
                       'timestamp_label': '[00:01:12]',
                       'url': 'https://www.youtube.com/watch?v=c069PHgKa8Y&t=72s',
                       'markdown': '[00:01:12](https://www.youtube.com/watch?v=c069PHgKa8Y&t=72s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'njIghi8P9jQ',
                       'title': 'What is a Workers Comp Minimum Experience Modifier',
                       'channel': 'The Coyle Group - Business Insurance',
                       'author': 'The Coyle Group - Business Insurance',
                       'text': 'Achieving a minimum modifier practically cuts your workers comp premium in '
                               'half.',
                       'tip': 'Achieving a minimum modifier practically cuts your workers comp premium in '
                              'half.',
                       'timestamp': 124,
                       'timestamp_seconds': 124,
                       'timestamp_label': '[00:02:04]',
                       'url': 'https://www.youtube.com/watch?v=njIghi8P9jQ&t=124s',
                       'markdown': '[00:02:04](https://www.youtube.com/watch?v=njIghi8P9jQ&t=124s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '7sfUUlxeHHk',
                       'title': 'Workers Comp Class Codes, What Are They For? 2026',
                       'channel': 'The Coyle Group - Business Insurance',
                       'author': 'The Coyle Group - Business Insurance',
                       'text': 'In cases like this insurers can go back up to 3 years and charge the '
                               'appropriate class rate and bill the insured in one chunk.',
                       'tip': 'In cases like this insurers can go back up to 3 years and charge the '
                              'appropriate class rate and bill the insured in one chunk.',
                       'timestamp': 491,
                       'timestamp_seconds': 491,
                       'timestamp_label': '[00:08:11]',
                       'url': 'https://www.youtube.com/watch?v=7sfUUlxeHHk&t=491s',
                       'markdown': '[00:08:11](https://www.youtube.com/watch?v=7sfUUlxeHHk&t=491s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'tkOuTso-3RA',
                       'title': 'Workers Compensation Codes',
                       'channel': 'WorkCompConsultants',
                       'author': 'WorkCompConsultants',
                       'text': "Making assumptions can get you into trouble, so don't just assume your "
                               'workers comp codes are correct.',
                       'tip': "Making assumptions can get you into trouble, so don't just assume your "
                              'workers comp codes are correct.',
                       'timestamp': 96,
                       'timestamp_seconds': 96,
                       'timestamp_label': '[00:01:36]',
                       'url': 'https://www.youtube.com/watch?v=tkOuTso-3RA&t=96s',
                       'markdown': '[00:01:36](https://www.youtube.com/watch?v=tkOuTso-3RA&t=96s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'UkIk-T0NP3M',
                       'title': 'Workers Compensation Insurance Experience Mod Worksheet',
                       'channel': 'Scott Simmonds',
                       'author': 'Scott Simmonds',
                       'text': 'Five $1,200 claims has more of an impact than one claim at $7,000.',
                       'tip': 'Five $1,200 claims has more of an impact than one claim at $7,000.',
                       'timestamp': 125,
                       'timestamp_seconds': 125,
                       'timestamp_label': '[00:02:05]',
                       'url': 'https://www.youtube.com/watch?v=UkIk-T0NP3M&t=125s',
                       'markdown': '[00:02:05](https://www.youtube.com/watch?v=UkIk-T0NP3M&t=125s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'gt3I3IxlEkE',
                       'title': 'What is an experience modifier?',
                       'channel': 'Texas Mutual Insurance Co',
                       'author': 'Texas Mutual Insurance Co',
                       'text': 'When it comes to not reporting claims, the juice is just not worth the '
                               'squeeze.',
                       'tip': 'When it comes to not reporting claims, the juice is just not worth the '
                              'squeeze.',
                       'timestamp': 171,
                       'timestamp_seconds': 171,
                       'timestamp_label': '[00:02:51]',
                       'url': 'https://www.youtube.com/watch?v=gt3I3IxlEkE&t=171s',
                       'markdown': '[00:02:51](https://www.youtube.com/watch?v=gt3I3IxlEkE&t=171s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '8Reu6Q_HdTE',
                       'title': 'Everything you need to know about California Experience Modification '
                                'Factors (EMOD)',
                       'channel': 'Fusco On Insurance',
                       'author': 'Fusco On Insurance',
                       'text': "If there's delays in audits you don't have the benefit of your payroll "
                               'being reported to the WCIRB; only your losses or expected losses are '
                               'reported.',
                       'tip': "If there's delays in audits you don't have the benefit of your payroll "
                              'being reported to the WCIRB; only your losses or expected losses are '
                              'reported.',
                       'timestamp': 218,
                       'timestamp_seconds': 218,
                       'timestamp_label': '[00:03:38]',
                       'url': 'https://www.youtube.com/watch?v=8Reu6Q_HdTE&t=218s',
                       'markdown': '[00:03:38](https://www.youtube.com/watch?v=8Reu6Q_HdTE&t=218s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '-hUWvUBIr1A',
                       'title': 'Work Comp Experience Mod Formula Is Changing',
                       'channel': 'ClinardInsGroup',
                       'author': 'ClinardInsGroup',
                       'text': 'Under the old formula you would not be penalized any more for a hundred '
                               'thousand dollar loss than you would for a five thousand dollar loss, and '
                               'beginning in 2012 that formula is changing to increase the cap.',
                       'tip': 'Under the old formula you would not be penalized any more for a hundred '
                              'thousand dollar loss than you would for a five thousand dollar loss, and '
                              'beginning in 2012 that formula is changing to increase the cap.',
                       'timestamp': 77,
                       'timestamp_seconds': 77,
                       'timestamp_label': '[00:01:17]',
                       'url': 'https://www.youtube.com/watch?v=-hUWvUBIr1A&t=77s',
                       'markdown': '[00:01:17](https://www.youtube.com/watch?v=-hUWvUBIr1A&t=77s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q11.'}]}
