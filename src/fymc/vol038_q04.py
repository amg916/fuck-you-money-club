from __future__ import annotations

CHAPTER_4 = {'id': 'Q4',
 'chapter_id': 'Q4',
 'chapter_number': 4,
 'question_number': 4,
 'slug': 'utility-bill-audits-error-recovery',
 'question_prompt': 'How do utility bill auditors find overcharges and misclassifications in electric, '
                    'gas, and water bills and recover refunds on a contingency basis?',
 'kicker': 'Q4 / THE BIG MONEY PLAYBOOKS',
 'title': 'Utility Bill Audits and Error Recovery',
 'subtitle': 'Rate-class misclassifications, water meter and billing errors, demand ratchet charges, '
             'demand tariffs and tariff calculation, utility tariff-setting models, National Utilities '
             'Refund partnerships, and no-recovery-no-fee audit programs',
 'layout_template': 'comparison_matrix',
 'reading_time_minutes': 15,
 'executive_summary': 'Contingent utility bill auditors agree on the thesis: commercial invoices are '
                      'routinely wrong, errors almost always favor the utility, and the customer carries '
                      'the burden of catching them before the lookback window closes. Puleo Energy and '
                      'Waste Consultants each report errors or savings in about 80 percent of audits, Vert '
                      'Energy Group claims 70 percent of clients save 10 to 20 percent, and Poteck Power '
                      'recovers in about 30 percent of cases. Street mechanics center on pulling three to '
                      'five years of bills, tariffs, meter data, and exemption certificates, then '
                      'rebuilding each invoice from the rate book to catch misclassified rate plans, '
                      'misread demand, meter multiplier errors, ratchet misapplication, and lapsed '
                      "exemptions. Puleo's NUR fee is 50 percent of refunds plus 50 percent of realized "
                      'savings for 24 months. Practitioners split on lookback depth, turnaround speed, and '
                      'in-house versus outsourced review.',
 'key_metrics': [{'label': 'Contingency Fee Split',
                  'metric': 'Contingency Fee Split',
                  'value': '50% of refunds received; 50% of realized monthly savings for 24 months, 100% '
                           'to client from month 25',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Puleo Energy's National Utilities Refund billing schedule, invoiced only "
                             'after the refund check, bill credit, or monthly savings is actually realized',
                  'source': 'Puleo Energy ([a4dO2n1QfzQ @ 00:05:57])'},
                 {'label': 'Typical Refund Lookback',
                  'metric': 'Typical Refund Lookback',
                  'value': 'About 36 months on average, as far back as the state allows',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Reach-back period Puleo Energy uses when hunting historical overbillings for '
                             'refund',
                  'source': 'Puleo Energy ([a4dO2n1QfzQ @ 00:00:54])'},
                 {'label': 'Client Savings Hit Rate',
                  'metric': 'Client Savings Hit Rate',
                  'value': '70% of clients realize savings; average savings 10% to 20%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Vert Energy Group's reported share of clients who realize savings and the "
                             'average savings range',
                  'source': 'Vert Energy Group ([bQpXnGBfNJY @ 00:02:18])'},
                 {'label': 'Error Sizing Math',
                  'metric': 'Error Sizing Math',
                  'value': '1% error on $5 million over three years = $150,000; 3% = $450,000',
                  'confidence': 'attributed_practitioner_claim',
                  'context': "Daniel Burke's illustration of how a modest error rate compounds across "
                             'multi-year commercial and industrial utility spend',
                  'source': 'Daniel Burke ([4pb6YRGZx4s @ 00:06:16])'}],
 'sections': [{'heading': 'Section 1: The Practitioner Consensus',
               'paragraphs': ['Every practitioner selling this service opens with the same thesis: '
                              'commercial utility invoices are wrong far more often than finance teams '
                              'assume, and the money keeps bleeding until someone forces a correction. Sam '
                              'at Puleo Energy, reselling the National Utilities Refund program, cites a '
                              'U.S. Ways and Means Committee study that pegged consumer overbilling at 19 '
                              'billion dollars with 60 percent of bills carrying some error, then says '
                              'closer to 80 percent of their own audits have turned up an error '
                              '[a4dO2n1QfzQ @ 00:00:16]. Andreas Suarez of Waste Consultants lands on the '
                              'same 80 percent figure, explaining it is the number the firm arrived at '
                              'after at least a decade of running utility and telecom audits [zV8cq0gJWOA '
                              "@ 00:00:00]. Vincent DiMaio's NUR pitch frames it as 80 percent of "
                              'organisations overspending thousands because they pay invoices at face '
                              'value [E0kxjgPAax0 @ 00:00:00]. Daniel Burke of Tactical Energy Group adds '
                              'the detail operators should remember: the billing errors Burke has seen '
                              'over and over almost always favor the utility, not through malice but '
                              'through human error, system changes, account changes, and customer service '
                              'reps carrying more accounts than they can manage at a deep and detailed '
                              'level [4pb6YRGZx4s @ 00:07:51]. The upshot across all four is blunt: an '
                              'unaudited portfolio is presumed to be leaking cash.',
                              'The second point of agreement is that the burden of catching mistakes sits '
                              'entirely on the customer. Vert Energy Group states that electric, water, '
                              'and telephone utilities are not required to review every account to catch '
                              'mistakes or even to ensure the customer sits on the correct rate plan, and '
                              'that utilities typically enroll a business on a default plan based on its '
                              'industry that ends up costing more than it should [bQpXnGBfNJY @ 00:00:35]. '
                              'UB Engineering repeats the same structural argument, adding that the '
                              'default plan assigned when service starts usually costs more as the '
                              'business grows and uses more resources [V-4ioYMhiuo @ 00:03:05]. Puleo '
                              'Energy lists why errors persist: finance pays any bill that fits the '
                              'budget, tariffs and USOC codes are complex equations end users cannot read, '
                              'and responsibility for identifying errors rests on the end user '
                              '[a4dO2n1QfzQ @ 00:03:11]. Burke goes further and attacks the comfort of a '
                              'friendly account rep, saying they have met very few reps who truly act as '
                              "auditors, that the utility's incentive is to recover as much revenue as it "
                              'can inside its rules, and that leaning on that rep puts one person in the '
                              'role of both scorekeeper and player [4pb6YRGZx4s @ 00:09:36]. The consensus '
                              'prerequisite: an independent party who reads the tariff, not the total.',
                              'Every commercial seller agrees on the business model: zero upfront cost, '
                              'paid only from money actually recovered or saved. OEO Energy Solutions '
                              'calls it purely contingent, with no consulting fees or hidden charges, and '
                              'states flatly that if the audit finds nothing the firm walks away with '
                              'nothing [vxnBn-sUk98 @ 00:01:12]. Jeremy at Poteck Power works the same '
                              'way, charging only a percentage of what is successfully refunded and '
                              'pitching the service to a property-management CFO who, in the Poteck '
                              'telling, had nothing to lose [5_ptAtJKgqM @ 00:00:52]. Burke frames the '
                              "buyer's exposure as mostly the time spent gathering data, calling a regular "
                              'audit rhythm a smart move rather than a luxury for sizable commercial and '
                              'industrial operators, so the downside is time and attention, not a fee '
                              '[4pb6YRGZx4s @ 00:01:50]. The other shared premise is that time works '
                              'against the customer. DiMaio warns the statute of limitations severely '
                              'restricts the window to identify and declare errors, while OEO says every '
                              'month that passes is potentially another month the money stays with the '
                              'utility forever [E0kxjgPAax0 @ 00:00:00]. That is why practitioners push to '
                              'start immediately and, as OEO notes, to pull every utility account at once, '
                              'because covering all utilities increases the chances of finding something '
                              'recoverable.'],
               'table': {'caption': 'Where the contingent bill-audit practitioners line up',
                         'headers': ['Consensus Point',
                                     'What the Practitioner Reports',
                                     'Operator Takeaway',
                                     'Expert Source'],
                         'rows': [['Billing errors are widespread across commercial portfolios',
                                   'Closer to 80 percent of NUR-partnered audits have surfaced some error '
                                   'on the invoice',
                                   'Assume a multi-account portfolio holds at least one recoverable '
                                   'billing discrepancy',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:00:36])'],
                                  ["Errors almost always run in the utility's favor",
                                   'Mistakes come from human error, system changes, account changes, and '
                                   'overloaded reps',
                                   "Never treat a regulated utility's invoice as presumptively correct or "
                                   'neutral',
                                   'Daniel Burke ([4pb6YRGZx4s @ 00:07:51])'],
                                  ['The customer carries the full detection burden',
                                   'Utilities are not required to review accounts or confirm the correct '
                                   'rate plan',
                                   'Nobody on the utility side will volunteer a cheaper tariff or a refund',
                                   'Vert Energy Group ([bQpXnGBfNJY @ 00:00:35])'],
                                  ['Default rate plans quietly overcharge growing businesses',
                                   'New service gets a default industry plan that costs more as usage '
                                   'grows',
                                   'Re-check rate class whenever operations, size, or resource usage have '
                                   'expanded',
                                   'UtilityBillAudits ([V-4ioYMhiuo @ 00:03:05])'],
                                  ['Pure contingency pricing with nothing owed on a miss',
                                   'No consulting fees or hidden charges; if nothing is found the firm '
                                   'walks away',
                                   "The buyer's real cost is time and data, so the audit decision is "
                                   'low-risk',
                                   'OEO Energy Solutions ([vxnBn-sUk98 @ 00:01:12])'],
                                  ['The recovery clock is always running against you',
                                   'The statute of limitations severely restricts time to identify and '
                                   'declare errors',
                                   'Start the audit early, because every passing month may become '
                                   'unrecoverable',
                                   'Vincent DiMaio ([E0kxjgPAax0 @ 00:00:00])'],
                                  ['Utility account reps are not your auditors',
                                   "Very few reps truly operate as auditors; the utility's incentive is "
                                   'maximum revenue',
                                   'Hire an independent auditor instead of relying on the utility account '
                                   "rep's word",
                                   'Daniel Burke ([4pb6YRGZx4s @ 00:09:36])']]}},
              {'heading': 'Section 2: Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ['Burke lays out the most complete workflow in six phases: data collection of '
                              'three to five years of bills plus special contracts, tariff sheets, meter '
                              'information, and tax exemption certificates; a baseline review mapping '
                              'which meters feed which facilities and flagging accounts on odd rates or '
                              'with demand charges out of proportion to consumption; a bill-by-bill '
                              'examination; error quantification across the whole audit period; a recovery '
                              'report; and forward-looking recommendations [4pb6YRGZx4s @ 00:03:08]. The '
                              'intake load on the client is deliberately light. Puleo Energy asks only for '
                              'recent invoices plus authorization to download historical invoices directly '
                              'from the utilities, quoting six to eight weeks for the full audit with '
                              'preliminary findings along the way, then preparing all the paperwork for '
                              'the utility once the client approves the findings [a4dO2n1QfzQ @ 00:05:06]. '
                              'Waste Consultants starts with just the most current invoice per account, '
                              "then pulls 12 months of history from the vendor's online billing portal, "
                              'noting most companies hand over an invoice or login in a few hours, with '
                              'audits running 30 to 90 days depending on location count [zV8cq0gJWOA @ '
                              '00:01:50]. Ashokan Water Meter and Backflow strips water intake even '
                              'further, asking only for the property address and bringing accountants, '
                              'lawyers, forensic auditors, programmers, and engineering staff to find '
                              'physical as well as accounting errors [PRQE0XuoBbg @ 00:01:10].',
                              "The line-item checks are specific. Burke's bill-by-bill test asks whether "
                              'the correct tariff applies for customer type and voltage level, whether '
                              'energy and demand charges including time-of-use windows compute correctly, '
                              'whether meter readings and multipliers match the meter nameplate or reveal '
                              'estimated reads never trued up, whether contract terms and tax exemptions '
                              'held, and whether ratchets and riders follow commission-approved rules '
                              "[4pb6YRGZx4s @ 00:03:51]. Vert Energy Group's XYZ case shows the payoff: a "
                              'misclassification onto the small business rate plan produced $21,000 in '
                              'overpayments over a year and a half, and a misread demand charge five times '
                              'the normal read added $3,500, yielding a negotiated refund of $24,500 '
                              "[bQpXnGBfNJY @ 00:02:36]. UB Engineering's version reviews 30 months of "
                              'billing, finds the same $21,000 small-business-rate overcharge plus a '
                              '$5,400 meter-reader typographical error, and puts the refund at almost '
                              '$30,000 [V-4ioYMhiuo @ 00:01:56]. Ratchets deserve hand calculation: Oncor '
                              'sets its demand ratchet at 80 percent of the trailing 12-month peak, so a '
                              '135 kW August peak locks in 108 kW for the next 11 months, meaning a 100 kW '
                              'October bills at 108 kW while a 132 kW September bills at actual demand, '
                              'until a new peak above 135 kW resets the ratchet higher [yHlhF0nEJ14 @ '
                              '00:02:08].',
                              'Pricing is where the dollars get split. Puleo Energy, through National '
                              'Utilities Refund, bills 50 percent of any refund check or bill credit only '
                              'after it lands, and 50 percent of realized monthly savings from corrected '
                              'recurring errors or rate changes for 24 months, with month 25 onward fully '
                              "the client's [a4dO2n1QfzQ @ 00:06:15]. Those savings are calculated each "
                              'month, for example after moving a client from rate schedule A to rate '
                              'schedule B, and every finding must be true, uncontested, and '
                              'client-approved before implementation. Forward optimization is the second '
                              'revenue stream: Vert Energy Group kept monitoring XYZ after the refund, and '
                              'when the utility released new tariffs eight months later, rate plan B cut '
                              'costs by 2 cents per kilowatt hour, followed by a business expansion that '
                              'qualified XYZ for another plan saving an additional 1 cent per kilowatt '
                              '[bQpXnGBfNJY @ 00:03:09]. Speed varies sharply. Poteck Power came back in '
                              'one week with a $50,000 finding filed as a credit on the next invoice, '
                              'reporting recovery in about 30 percent of cases and some clients owed over '
                              '$90,000 [5_ptAtJKgqM @ 00:01:11]. Burke supplies the sizing math for the '
                              'finance meeting: a 1 percent error on $5 million over three years equals '
                              '$150,000, and a 3 percent error equals $450,000 [4pb6YRGZx4s @ 00:06:16].'],
               'table': {'caption': 'Street-level numbers, error vectors, and fee mechanics',
                         'headers': ['Mechanic or Error Vector',
                                     'Exact Number or Rule',
                                     'How Practitioners Use It',
                                     'Expert Source'],
                         'rows': [['Contingency share on historical refunds',
                                   '50 percent of the refund check or bill credit, billed after receipt',
                                   "Fee triggers only once the client's recovered money actually arrives",
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:05:57])'],
                                  ['Contingency share on recurring bill reductions',
                                   '50 percent of realized monthly savings for 24 months; client keeps 100 '
                                   'percent from month 25',
                                   'Auditor calculates actual monthly savings from each corrected error or '
                                   'rate move',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:06:15])'],
                                  ['Rate class misclassification on a larger business',
                                   '$21,000 overpaid over a year and a half on a small business rate plan',
                                   'Audit rate class first because default plans compound quietly over '
                                   'time',
                                   'Vert Energy Group ([bQpXnGBfNJY @ 00:02:36])'],
                                  ['Misread demand charge on the electric bill',
                                   'Demand read five times normal added $3,500; total negotiated refund '
                                   '$24,500',
                                   'Flag demand spikes that are out of line with consumption and history',
                                   'Vert Energy Group ([bQpXnGBfNJY @ 00:02:36])'],
                                  ['Meter reader typographical error',
                                   '$5,400 typo found within a 30-month billing review; refund near '
                                   '$30,000 combined',
                                   'Compare recorded reads against usage history to catch keyed-in reading '
                                   'mistakes',
                                   'UtilityBillAudits ([V-4ioYMhiuo @ 00:02:11])'],
                                  ['Demand ratchet floor on delivery charges',
                                   '80 percent of trailing 12-month peak; a 135 kW peak sets a 108 kW '
                                   'floor',
                                   'Recompute which months billed at the ratchet versus actual monthly '
                                   'peak demand',
                                   'Oncor ([yHlhF0nEJ14 @ 00:01:46])'],
                                  ['Peak-window demand charge measurement',
                                   'Highest half-hour demand between 4 pm and 9 pm sets the monthly demand '
                                   'charge',
                                   'Load shifting and staggering appliances outside the window lowers the '
                                   'demand charge',
                                   'Ergon Energy ([ArxvRqneZ_c @ 00:01:13])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'How the contingent auditors squeeze extra findings out of a file',
                           'body': 'The working auditors win by going behind the face of the bill, pulling '
                                   'the full account universe, and re-checking items the client assumes '
                                   'were settled long ago.',
                           'items': ['Get signed authorization to download historical invoices straight '
                                     'from each utility rather than making the client dig up years of '
                                     'paper [Puleo Energy — a4dO2n1QfzQ @ 00:04:47]',
                                     'Comb the customer service records and the utility tariffs, not just '
                                     'the invoice, because that is where NUR says hidden billing errors '
                                     'are resolved [Vincent DiMaio — E0kxjgPAax0 @ 00:00:59]',
                                     'Re-verify tax exemptions every cycle, since accounts exempted from '
                                     'certain taxes or fees can find themselves opted back in [Daniel '
                                     'Burke — 4pb6YRGZx4s @ 00:04:30]',
                                     'Ask for bills the client never flagged, because knowing all state '
                                     'tariffs lets the auditor request accounts the customer did not know '
                                     'were improperly rated [Ryan Sumerlan — h6W5k5owNiU @ 00:01:43]']},
               'sop_steps': [{'step': 1,
                              'title': 'Enroll and lock down data access',
                              'action': 'Sign the enrollment form, send the most recent bill for every '
                                        'utility account, and authorize direct invoice downloads.',
                              'detail': 'Summerlin starts with a simple enrollment form plus bill copies '
                                        '[Ryan Sumerlan — h6W5k5owNiU @ 00:01:43]; Puleo pairs recent '
                                        'invoices with authorization to pull history from each utility '
                                        '[Puleo Energy — a4dO2n1QfzQ @ 00:04:47].'},
                             {'step': 2,
                              'title': 'Rebuild every bill from the tariff',
                              'action': 'Re-run each invoice using actual readings, multipliers, '
                                        'contracts, and the applicable rate schedule, then compare to what '
                                        'the utility billed.',
                              'detail': 'Burke defines the audit as asking whether billing run from '
                                        'scratch under the correct rules, readings, multipliers, and '
                                        'tariffs produces the same answer the utility billed [Daniel Burke '
                                        '— 4pb6YRGZx4s @ 00:02:26].'},
                             {'step': 3,
                              'title': 'Quantify across the whole audit period and report',
                              'action': 'Apply the correct rule across every affected month and document '
                                        'account, tariff, line item, date range, and total overcharge.',
                              'detail': 'The report names account X, tariff Y, line item Z, the date '
                                        'range, the correct calculation, and the total overcharge, and '
                                        'becomes the basis for credits or refunds [Daniel Burke — '
                                        '4pb6YRGZx4s @ 00:05:21].'},
                             {'step': 4,
                              'title': 'Negotiate recovery, then monitor tariffs',
                              'action': "Negotiate refunds and credits with the utility on the client's "
                                        'behalf, move the account to the optimal plan, and keep watching '
                                        'tariff changes.',
                              'detail': 'Vert negotiates recovery once refund and tariff opportunities are '
                                        'found, then keeps monitoring for tariff changes [Vert Energy '
                                        'Group — bQpXnGBfNJY @ 00:01:18]; UB Engineering does the same '
                                        'post-optimization monitoring [UtilityBillAudits — V-4ioYMhiuo @ '
                                        '00:03:18].'}]},
              {'title': 'Section 3: Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['The hit-rate claims swing hard depending on who is pitching. Sam at Puleo '
                              'Energy cites a U.S. Ways and Means committee study finding consumers '
                              'overbilled to the tune of 19 billion dollars, with 60 percent of bills '
                              'carrying some error, then says closer to 80 percent of the audits their '
                              'team has performed surfaced an error on the invoice [a4dO2n1QfzQ @ '
                              '00:00:16]. Vert Energy Group runs cooler: on average 70 percent of their '
                              'clients realize savings, with average savings ranging from 10 to 20 percent '
                              '[bQpXnGBfNJY @ 00:02:18]. UtilityBillAudits drops lower again, saying three '
                              'out of five companies they work with save money and pitching the whole '
                              'engagement as a performance deal where no savings means no paycheck '
                              '[5A8gPPLuUaY @ 00:01:24]. At the bottom of the range, Poteck Power '
                              "Corporation's Jeremy recovers funds in about 30 percent of cases, though "
                              'some of those clients were owed over $90,000 and the fee is only a '
                              'percentage of what actually gets refunded [5_ptAtJKgqM @ 00:00:52]. The '
                              'operator read: Puleo audits electricity, natural gas, water, sewer, trash, '
                              'and telecom together, while the Poteck number comes from electricity '
                              'verification alone. Forecast pipeline on the low end and widen the utility '
                              'scope to lift the hit rate.',
                              'Savings magnitude and lookback windows split the field just as sharply. OEO '
                              'Energy Solutions says they have seen bills cut by 40 percent [vxnBn-sUk98 @ '
                              '00:01:29], and UtilityBillAudits claims ongoing savings that can reduce a '
                              'bill up to 30 percent per month. Daniel Burke pours cold water on those '
                              'headline numbers, framing a realistic outcome as recovering a small '
                              'percentage of past spend, 1 to 3 percent across a few years and 1 to 5 '
                              'percent at the outer band, while showing that a 1 percent error on $5 '
                              'million over three years still equals $150,000 [4pb6YRGZx4s @ 00:06:16]. On '
                              'lookback depth, Puleo Energy goes back as far as the state allows, about 36 '
                              'months on average [a4dO2n1QfzQ @ 00:00:54], Burke wants three to five years '
                              'of bills or more, and Waste Consultants starts with only 12 months of bills '
                              'to establish a baseline before reviewing rate structures and trends '
                              '[zV8cq0gJWOA @ 00:01:30]. Turnaround diverges too: Puleo quotes six to '
                              'eight weeks for the full audit, Waste Consultants quotes 30 to 90 days '
                              'depending on portfolio size, and Poteck delivered a $50,000 finding to a '
                              'property management CFO one week after engagement. The playbook choice is a '
                              'deep multi-year forensic dig with a slower cash cycle versus a fast '
                              '12-month rate-structure review that books recurring savings sooner.',
                              'The sharpest philosophical split is whether to run this in-house at all. '
                              "ASHE AHA's Energy to Care program publishes an ECM that walks facilities "
                              'through performing their own utility bill audit, backed by a free dashboard '
                              'built to manage and mitigate utility mistakes [bPG_PW4MubQ @ 00:00:23]. '
                              'Ashokan Water Meter & Backflow says the opposite for water: try to deal '
                              'with the utility yourself and you will just be tearing your hair out, which '
                              'is why they field accountants, lawyers, forensic auditors, trained '
                              'programmers, and engineering staff to catch physical errors as well as '
                              'accounting errors [PRQE0XuoBbg @ 00:01:10]. Daniel Burke splits the '
                              'difference: commercial and industrial operators should learn to read their '
                              'bills and rate structures inside finance and accounting, but a full '
                              'forensic audit across years of history belongs to a specialist who is '
                              'unusually fascinated by meter multipliers and tariff footnotes [4pb6YRGZx4s '
                              '@ 00:12:20]. Control over implementation also varies. Puleo insists '
                              "implementation is 100 percent the client's choice and nothing gets changed "
                              'automatically, while Vert Energy Group negotiates directly with the utility '
                              "on the client's behalf and keeps monitoring the account for tariff changes "
                              'afterward [bQpXnGBfNJY @ 00:01:18]. Match the model to whether the client '
                              'wants hands-off recovery or sign-off on every adjustment.'],
               'table': {'caption': 'Competing audit playbooks side by side, as run by named practitioners',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['How the fee splits across refunds and recurring reductions',
                                   'Puleo/NUR bills 50 percent of refunds after receipt, plus 50 percent '
                                   'of realized monthly savings for 24 months; month 25 onward is all the '
                                   "client's",
                                   'Poteck charges only a percentage of what was successfully refunded and '
                                   'files the recovery as a credit on the next invoice',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:06:15]) vs Poteck Power Corporation '
                                   '([5_ptAtJKgqM @ 00:01:11])'],
                                  ['How far back the auditor digs into billing history',
                                   'Puleo goes back as far as the state allows, typically about 36 months '
                                   'on average',
                                   'Burke wants three to five years of bills plus special contracts, '
                                   'tariff sheets, meter information, and exemption certificates',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:00:54]) vs Daniel Burke ([4pb6YRGZx4s '
                                   '@ 00:03:08])'],
                                  ['What the client hands over to start the audit',
                                   'Ashokan asks the client to just provide the property address and takes '
                                   'it from there',
                                   'Waste Consultants starts with the current invoice per account, then '
                                   "pulls historical copies from the vendor's online billing portal",
                                   'Ashokan Water Meter & Backflow ([PRQE0XuoBbg @ 00:01:10]) vs Waste '
                                   'Consultants ([zV8cq0gJWOA @ 00:01:50])'],
                                  ['Whether to self-audit or hire a forensic specialist',
                                   "ASHE's Energy to Care ECM walks facilities through performing their "
                                   'own utility bill audit with a free dashboard',
                                   'Burke says finance should learn the basics, but a full multi-year '
                                   'forensic audit belongs with a specialist',
                                   'ASHE AHA ([bPG_PW4MubQ @ 00:00:23]) vs Daniel Burke ([4pb6YRGZx4s @ '
                                   '00:12:20])'],
                                  ['Who controls implementation of the audit findings',
                                   'Puleo requires the client to approve and authorize every finding; '
                                   'nothing is implemented automatically',
                                   "Vert negotiates with the utility on the client's behalf and keeps "
                                   'monitoring for tariff changes afterward',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:05:21]) vs Vert Energy Group '
                                   '([bQpXnGBfNJY @ 00:01:18])'],
                                  ['How the demand charge is actually calculated and attacked',
                                   'Oncor ratchet bills 80 percent of the highest 15-minute peak across '
                                   'the current and previous 11 months',
                                   'Ergon demand tariff bills the highest half-hour reading between 4pm '
                                   'and 9pm, cut through load shifting and staggering',
                                   'Oncor ([yHlhF0nEJ14 @ 00:01:46]) vs Ergon Energy ([ArxvRqneZ_c @ '
                                   '00:01:13])'],
                                  ['What hit rate to expect when forecasting the pipeline',
                                   'Puleo reports closer to 80 percent of its audits finding some error on '
                                   'the invoice',
                                   'Poteck recovers funds in about 30 percent of cases, with some clients '
                                   'owed over $90,000',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:00:36]) vs Poteck Power Corporation '
                                   '([5_ptAtJKgqM @ 00:00:52])']]}},
              {'title': 'Section 4: Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['The most common failure is not a bad audit; it is never auditing. Puleo '
                              'Energy names the root cause bluntly: as long as the bill fits within the '
                              'budget, the finance team pays it, tariffs and USOC codes are too complex to '
                              'parse, and the responsibility to identify errors sits on the end user, so '
                              'overpayment can run for years unnoticed [a4dO2n1QfzQ @ 00:03:28]. ASHE AHA '
                              'adds that many facilities managers never even see the utility bills before '
                              'or after the accounting group pays them [bPG_PW4MubQ @ 00:00:42]. Daniel '
                              'Burke goes after the comfort blanket of the friendly account rep, reporting '
                              'meeting very few utility reps who truly operate as auditors for their '
                              "customers, because the utility's incentive is to recover as much revenue as "
                              "it can inside its rules while the customer's incentive is the opposite, "
                              'which makes the rep both scorekeeper and player [4pb6YRGZx4s @ 00:09:36]. '
                              "Poteck Power Corporation's case shows the cost: Richard, a property "
                              'management CFO, called the power company, was told the account was up to '
                              'date, and still turned out to be owed $50,000 once Jeremy verified the '
                              'bills [5_ptAtJKgqM @ 00:00:19]. Internal reviews that only check totals '
                              'against last month never recalculate each line from the rate book.',
                              'Metering and estimation are where the money leaks fastest. OEO Energy '
                              'Solutions flags metering errors and overestimated demand charges caused by '
                              'estimated meter reads, and warns that every month that goes by is '
                              'potentially another month that money stays with the utility forever '
                              '[vxnBn-sUk98 @ 00:00:40]. Ashokan Water Meter & Backflow lists water '
                              'readings incorrectly recorded, meters unknowingly connected to other '
                              'properties or broken and leaking for years, usage estimates that bear no '
                              'relation to actual consumption, and charges under the wrong rate '
                              'classification [PRQE0XuoBbg @ 00:00:33]. They also flag the reverse trap: '
                              'under-billing can be even more damaging when the customer gets hit with an '
                              'astronomical bill for many years of past usage. Demand ratchets then '
                              'compound any bad peak. Oncor sets its ratchet at 80 percent of the highest '
                              '15-minute demand across the current and previous 11 months, so a 135 kW '
                              'August peak locks in 108 kW, and an October that only hits 100 kW still '
                              'bills at the 108 kW ratchet [yHlhF0nEJ14 @ 00:02:08]. Daniel Burke warns '
                              'that when a ratchet is misapplied systemically for years, the premium '
                              'repeats every single month going forward unless someone corrects it '
                              '[4pb6YRGZx4s @ 00:06:39]. Any inflated or estimated peak feeds straight '
                              'into that ratchet math.',
                              'Classification and exemption drift are the slow-burn traps. Vert Energy '
                              'Group says utilities usually sign a business up on a default plan based on '
                              'its industry, and their XYZ client sat misclassified on the small business '
                              'rate plan for $21,000 in overpayments over a year and a half, plus a '
                              'misread demand charge five times higher than normal that added $3,500, for '
                              'a $24,500 refund [bQpXnGBfNJY @ 00:02:36]. Daniel Burke calls lapsed tax '
                              'exemptions a big one: an account can get exempted and then suddenly find '
                              'itself opted back in [4pb6YRGZx4s @ 00:04:30]. Time works against the '
                              "customer: Vincent DiMaio's NUR pitch says the liability of reporting still "
                              'lies with the customer and the statute of limitations severely restricts '
                              'the window to identify and declare errors [E0kxjgPAax0 @ 00:00:00]. '
                              'UtilityBillAudits warns not to expect large utility firms to simply hand '
                              'over a check for overages [5A8gPPLuUaY @ 00:00:21]. The economics check '
                              'cuts both ways. Burke concedes that for small single-site operations with '
                              'modest spend the effort may not pay, and that some charges, like a power '
                              'factor penalty, are legitimate and call for a fix project rather than a '
                              'dispute. Waste Consultants adds that a freshly renovated building can drive '
                              'cost increases that are fair, not errors.'],
               'table': {'caption': 'Firsthand traps and the dollar math practitioners attached to them',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Approving utility bills at face value because they fit budget',
                                   'Finance pays as long as the bill fits the budget; tariffs and USOC '
                                   'codes are too complex to check',
                                   'Overpayment can run for years because the responsibility to identify '
                                   'errors sits on the end user',
                                   'Puleo Energy ([a4dO2n1QfzQ @ 00:03:28])'],
                                  ['Treating the utility account rep as your independent auditor',
                                   "Burke reports very few reps operate as auditors; Poteck's CFO client "
                                   'was told the account was up to date',
                                   'That same Poteck client was owed $50,000, filed as a credit on the '
                                   'next invoice',
                                   'Daniel Burke ([4pb6YRGZx4s @ 00:09:56]); Poteck Power Corporation '
                                   '([5_ptAtJKgqM @ 00:01:11])'],
                                  ['Estimated meter reads inflating the billed demand charges',
                                   'OEO sees metering errors and overestimated demand charges because the '
                                   'meter was estimated',
                                   'Every month that passes is potentially another month that money stays '
                                   'with the utility forever',
                                   'OEO Energy Solutions ([vxnBn-sUk98 @ 00:00:40])'],
                                  ['Demand ratchet locked in by one peak month',
                                   'A 135 kW August peak sets a 108 kW ratchet for the next 11 months',
                                   'An October with only 100 kW actual demand still gets billed at the 108 '
                                   'kW ratchet',
                                   'Oncor ([yHlhF0nEJ14 @ 00:02:31])'],
                                  ['Larger business left sitting on a small business rate plan',
                                   'UB Engineering reviewed 30 months of billing and found the wrong rate '
                                   'plan plus a meter reader typo',
                                   '$21,000 rate overcharge plus $5,400 typographical error, for a refund '
                                   'of almost $30,000',
                                   'UtilityBillAudits ([V-4ioYMhiuo @ 00:01:56])'],
                                  ['Under-billing that returns later as an astronomical catch-up bill',
                                   'Ashokan warns under-billing can be even more damaging than overbilling '
                                   'on water accounts',
                                   'The customer gets hit with a bill covering many years of past usage at '
                                   'once',
                                   'Ashokan Water Meter & Backflow ([PRQE0XuoBbg @ 00:00:53])'],
                                  ['Tax exemptions that silently lapse on the account',
                                   'Burke sees accounts exempted from charges that later find themselves '
                                   'opted back in',
                                   'Verify eligible exemptions were applied to the right accounts and '
                                   'stayed in force over time',
                                   'Daniel Burke ([4pb6YRGZx4s @ 00:04:30])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Clear These Four Gates Before Signing or Disputing',
                           'body': 'Every gate below comes from a trap a named practitioner hit or '
                                   'measured in the field. Clear all four before the engagement letter is '
                                   'signed or a dispute goes to the utility.',
                           'items': ['Never approve a bill on its total alone; recalculate each line '
                                     'against the rate book, which is the source of truth, because '
                                     'internal reviews rarely go line by line [Daniel Burke — 4pb6YRGZx4s '
                                     '@ 00:08:21].',
                                     'Rebuild the demand ratchet yourself: confirm it equals 80 percent of '
                                     'the highest peak across the current and previous 11 months, and that '
                                     'months above the ratchet bill actual demand [Oncor — yHlhF0nEJ14 @ '
                                     '00:01:46].',
                                     'Flag every estimated read, any meter that may connect to another '
                                     'property, and any meter broken or leaking for years before trusting '
                                     'the usage history [Ashokan Water Meter & Backflow — PRQE0XuoBbg @ '
                                     '00:00:33].',
                                     'Lock the fee math in writing: 50 percent of refunds after receipt '
                                     'and 50 percent of realized savings for 24 months, billed only on '
                                     'true and uncontested findings [Puleo Energy — a4dO2n1QfzQ @ '
                                     '00:06:15].']}}],
 'pull_quote': '"The reality I have seen over and over is that billing errors almost always favor the '
               'utility." — Daniel Burke (4pb6YRGZx4s @ 00:07:51).',
 'diagram_id': 'diag-07',
 'action_checklist': ['Total the last three to five years of electricity, gas, and other utility spend and '
                      'confirm whether it has ever had a forensic bill audit [Daniel Burke — 4pb6YRGZx4s @ '
                      '00:15:13].',
                      'Collect the most current invoice for every account plus online billing portal '
                      'log-ons so 12 months of history can be pulled directly [Waste Consultants — '
                      'zV8cq0gJWOA @ 00:01:50].',
                      'Compare every tariff the utility offers against the default plan the business was '
                      'signed onto by industry [Vert Energy Group — bQpXnGBfNJY @ 00:01:03].',
                      "Check each month's billed demand against the ratchet and reset it whenever a new "
                      'peak exceeds the prior 12-month high [Oncor — yHlhF0nEJ14 @ 00:02:31].',
                      'Review city and state tax exemption opportunities for every location and confirm '
                      'they are actually applied [Waste Consultants — zV8cq0gJWOA @ 00:03:19].',
                      'Vet the audit firm on industry experience, knowledge of your utility territories, '
                      'contingency terms, and data security, and name an internal owner [Daniel Burke — '
                      '4pb6YRGZx4s @ 00:15:34].'],
 'statutory_citations': [{'title': 'Daniel Burke — Energy Decision #09 - Utility Bill Audits and Error '
                                   'Recovery | Energy Answers by TEG [00:02:26]',
                          'url': 'https://www.youtube.com/watch?v=4pb6YRGZx4s&t=146s',
                          'relevance': 'Primary practitioner testimony on the forensic audit definition, '
                                       'the six-phase process, and the 1 to 3 percent recovery math.'},
                         {'title': 'Puleo Energy — Overview: Utility Bill Audit [00:05:57]',
                          'url': 'https://www.youtube.com/watch?v=a4dO2n1QfzQ&t=357s',
                          'relevance': 'Primary practitioner testimony on the 50 percent refund split and '
                                       '24-month shared-savings contingency structure.'},
                         {'title': 'Oncor — Understanding Demand Ratchet Charges for Businesses [00:01:46]',
                          'url': 'https://www.youtube.com/watch?v=yHlhF0nEJ14&t=106s',
                          'relevance': 'Primary practitioner testimony on the 80 percent demand ratchet '
                                       'mechanics and the 135 kW to 108 kW worked example.'},
                         {'title': 'Vert Energy Group — Utility Bill Audit - Introduction [00:02:36]',
                          'url': 'https://www.youtube.com/watch?v=bQpXnGBfNJY&t=156s',
                          'relevance': 'Primary practitioner testimony on rate misclassification and '
                                       'misread demand recovery totaling a $24,500 refund.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'vxnBn-sUk98',
                       'title': 'FREE Utility Bill Audit — Are You Being Overcharged?',
                       'channel': 'OEO Energy Solutions',
                       'author': 'OEO Energy Solutions',
                       'text': 'We go through the historical usage to see if there were any errors billed '
                               'where we can obtain a refund; sometimes we see metering errors and '
                               'overestimated demand charges because the meter was estimated.',
                       'tip': 'We go through the historical usage to see if there were any errors billed '
                              'where we can obtain a refund; sometimes we see metering errors and '
                              'overestimated demand charges because the meter was estimated.',
                       'timestamp': 40,
                       'timestamp_seconds': 40,
                       'timestamp_label': '[00:00:40]',
                       'url': 'https://www.youtube.com/watch?v=vxnBn-sUk98&t=40s',
                       'markdown': '[00:00:40](https://www.youtube.com/watch?v=vxnBn-sUk98&t=40s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'a4dO2n1QfzQ',
                       'title': 'Overview: Utility Bill Audit',
                       'channel': 'Puleo Energy',
                       'author': 'Puleo Energy',
                       'text': 'If we are successful in obtaining a refund for you, after you receive that '
                               'refund check or bill credit we will then bill you 50 percent of that total '
                               'refund amount.',
                       'tip': 'If we are successful in obtaining a refund for you, after you receive that '
                              'refund check or bill credit we will then bill you 50 percent of that total '
                              'refund amount.',
                       'timestamp': 357,
                       'timestamp_seconds': 357,
                       'timestamp_label': '[00:05:57]',
                       'url': 'https://www.youtube.com/watch?v=a4dO2n1QfzQ&t=357s',
                       'markdown': '[00:05:57](https://www.youtube.com/watch?v=a4dO2n1QfzQ&t=357s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5A8gPPLuUaY',
                       'title': 'Utility Bill Audit Service | Get Overages Refunded Using Our Free Utility '
                                'Bill Analysis',
                       'channel': 'UtilityBillAudits',
                       'author': 'UtilityBillAudits',
                       'text': "If we can't find savings or refund, we don't get paid. However, we find "
                               'that three out of five companies we work with save money.',
                       'tip': "If we can't find savings or refund, we don't get paid. However, we find "
                              'that three out of five companies we work with save money.',
                       'timestamp': 84,
                       'timestamp_seconds': 84,
                       'timestamp_label': '[00:01:24]',
                       'url': 'https://www.youtube.com/watch?v=5A8gPPLuUaY&t=84s',
                       'markdown': '[00:01:24](https://www.youtube.com/watch?v=5A8gPPLuUaY&t=84s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'E0kxjgPAax0',
                       'title': 'National Utilities Refund "NUR" Utility Bill Audit',
                       'channel': 'Vincent DiMaio',
                       'author': 'Vincent DiMaio',
                       'text': '80 percent of organisations end up overspending thousands of dollars by '
                               'paying their utility invoices at face value because the liability of '
                               'reporting still lies with the customer.',
                       'tip': '80 percent of organisations end up overspending thousands of dollars by '
                              'paying their utility invoices at face value because the liability of '
                              'reporting still lies with the customer.',
                       'timestamp': 0,
                       'timestamp_seconds': 0,
                       'timestamp_label': '[00:00:00]',
                       'url': 'https://www.youtube.com/watch?v=E0kxjgPAax0&t=0s',
                       'markdown': '[00:00:00](https://www.youtube.com/watch?v=E0kxjgPAax0&t=0s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'h6W5k5owNiU',
                       'title': 'Utility Bill Audit Secrets',
                       'channel': 'Ryan Sumerlan',
                       'author': 'Ryan Sumerlan',
                       'text': 'We are familiar with all state tariffs so we may surprise you and ask for '
                               'a utility bill you may not have known you were improperly rated for.',
                       'tip': 'We are familiar with all state tariffs so we may surprise you and ask for a '
                              'utility bill you may not have known you were improperly rated for.',
                       'timestamp': 103,
                       'timestamp_seconds': 103,
                       'timestamp_label': '[00:01:43]',
                       'url': 'https://www.youtube.com/watch?v=h6W5k5owNiU&t=103s',
                       'markdown': '[00:01:43](https://www.youtube.com/watch?v=h6W5k5owNiU&t=103s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'PRQE0XuoBbg',
                       'title': 'Utility Water Bill Audit',
                       'channel': 'Ashokan Water Meter & Backflow',
                       'author': 'Ashokan Water Meter & Backflow',
                       'text': "Under billing can be even more damaging when you're hit with an "
                               "astronomical bill for many years past usage; we've examined over 125,000 "
                               'water bills and returned tens of millions of dollars to our clients.',
                       'tip': "Under billing can be even more damaging when you're hit with an "
                              "astronomical bill for many years past usage; we've examined over 125,000 "
                              'water bills and returned tens of millions of dollars to our clients.',
                       'timestamp': 53,
                       'timestamp_seconds': 53,
                       'timestamp_label': '[00:00:53]',
                       'url': 'https://www.youtube.com/watch?v=PRQE0XuoBbg&t=53s',
                       'markdown': '[00:00:53](https://www.youtube.com/watch?v=PRQE0XuoBbg&t=53s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bQpXnGBfNJY',
                       'title': 'Utility Bill Audit - Introduction',
                       'channel': 'Vert Energy Group',
                       'author': 'Vert Energy Group',
                       'text': 'The electric company misclassified XYZ and had them on the small business '
                               'rate plan, which resulted in $21,000 in overpayments over the last year '
                               'and a half.',
                       'tip': 'The electric company misclassified XYZ and had them on the small business '
                              'rate plan, which resulted in $21,000 in overpayments over the last year and '
                              'a half.',
                       'timestamp': 156,
                       'timestamp_seconds': 156,
                       'timestamp_label': '[00:02:36]',
                       'url': 'https://www.youtube.com/watch?v=bQpXnGBfNJY&t=156s',
                       'markdown': '[00:02:36](https://www.youtube.com/watch?v=bQpXnGBfNJY&t=156s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'V-4ioYMhiuo',
                       'title': 'Utility Bill Audit',
                       'channel': 'UtilityBillAudits',
                       'author': 'UtilityBillAudits',
                       'text': "We can take a look at a company's previous 30 months of billing and see "
                               'that the utility company had this larger business on a small business rate '
                               'plan, resulting in an overcharge of $21,000.',
                       'tip': "We can take a look at a company's previous 30 months of billing and see "
                              'that the utility company had this larger business on a small business rate '
                              'plan, resulting in an overcharge of $21,000.',
                       'timestamp': 116,
                       'timestamp_seconds': 116,
                       'timestamp_label': '[00:01:56]',
                       'url': 'https://www.youtube.com/watch?v=V-4ioYMhiuo&t=116s',
                       'markdown': '[00:01:56](https://www.youtube.com/watch?v=V-4ioYMhiuo&t=116s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yHlhF0nEJ14',
                       'title': 'Understanding Demand Ratchet Charges for Businesses',
                       'channel': 'Oncor',
                       'author': 'Oncor',
                       'text': "By analyzing your business's electric usage for the current month and the "
                               'previous 11 months, we can find the peak demand over the past year, and '
                               'for our tariff we set your demand ratchet at 80 percent of that peak.',
                       'tip': "By analyzing your business's electric usage for the current month and the "
                              'previous 11 months, we can find the peak demand over the past year, and for '
                              'our tariff we set your demand ratchet at 80 percent of that peak.',
                       'timestamp': 106,
                       'timestamp_seconds': 106,
                       'timestamp_label': '[00:01:46]',
                       'url': 'https://www.youtube.com/watch?v=yHlhF0nEJ14&t=106s',
                       'markdown': '[00:01:46](https://www.youtube.com/watch?v=yHlhF0nEJ14&t=106s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'EAW0K0M906s',
                       'title': 'Financial Modelling for Utility Tariff Setting',
                       'channel': 'Power Futures Lab',
                       'author': 'Power Futures Lab',
                       'text': 'Most African countries have tariffs which are not really cost reflective.',
                       'tip': 'Most African countries have tariffs which are not really cost reflective.',
                       'timestamp': 70,
                       'timestamp_seconds': 70,
                       'timestamp_label': '[00:01:10]',
                       'url': 'https://www.youtube.com/watch?v=EAW0K0M906s&t=70s',
                       'markdown': '[00:01:10](https://www.youtube.com/watch?v=EAW0K0M906s&t=70s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4pb6YRGZx4s',
                       'title': 'Energy Decision #09 - Utility Bill Audits and Error Recovery | Energy '
                                'Answers by TEG',
                       'channel': 'Daniel Burke',
                       'author': 'Daniel Burke',
                       'text': 'The reality I have seen over and over is that billing errors almost always '
                               'favor the utility.',
                       'tip': 'The reality I have seen over and over is that billing errors almost always '
                              'favor the utility.',
                       'timestamp': 471,
                       'timestamp_seconds': 471,
                       'timestamp_label': '[00:07:51]',
                       'url': 'https://www.youtube.com/watch?v=4pb6YRGZx4s&t=471s',
                       'markdown': '[00:07:51](https://www.youtube.com/watch?v=4pb6YRGZx4s&t=471s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4pb6YRGZx4s',
                       'title': 'Energy Decision #09 - Utility Bill Audits and Error Recovery | Energy '
                                'Answers by TEG',
                       'channel': 'Daniel Burke',
                       'author': 'Daniel Burke',
                       'text': 'A 1 percent error on $5 million over three years is $150,000; if the error '
                               "is 3 percent, it's $450,000.",
                       'tip': 'A 1 percent error on $5 million over three years is $150,000; if the error '
                              "is 3 percent, it's $450,000.",
                       'timestamp': 376,
                       'timestamp_seconds': 376,
                       'timestamp_label': '[00:06:16]',
                       'url': 'https://www.youtube.com/watch?v=4pb6YRGZx4s&t=376s',
                       'markdown': '[00:06:16](https://www.youtube.com/watch?v=4pb6YRGZx4s&t=376s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'zV8cq0gJWOA',
                       'title': 'What is a Utility Audit?',
                       'channel': 'Waste Consultants',
                       'author': 'Waste Consultants',
                       'text': 'We need 12 months of bills for all utilities, electric, gas, water and '
                               'sewer; looking at 12 months of history gives us the context we need to '
                               'evaluate your baseline costs.',
                       'tip': 'We need 12 months of bills for all utilities, electric, gas, water and '
                              'sewer; looking at 12 months of history gives us the context we need to '
                              'evaluate your baseline costs.',
                       'timestamp': 90,
                       'timestamp_seconds': 90,
                       'timestamp_label': '[00:01:30]',
                       'url': 'https://www.youtube.com/watch?v=zV8cq0gJWOA&t=90s',
                       'markdown': '[00:01:30](https://www.youtube.com/watch?v=zV8cq0gJWOA&t=90s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'ArxvRqneZ_c',
                       'title': 'Demand tariffs explained',
                       'channel': 'Ergon Energy',
                       'author': 'Ergon Energy',
                       'text': 'The more appliances you run during the same half hour block between 4pm '
                               'and 9pm each day, the higher your demand charge will be.',
                       'tip': 'The more appliances you run during the same half hour block between 4pm and '
                              '9pm each day, the higher your demand charge will be.',
                       'timestamp': 97,
                       'timestamp_seconds': 97,
                       'timestamp_label': '[00:01:37]',
                       'url': 'https://www.youtube.com/watch?v=ArxvRqneZ_c&t=97s',
                       'markdown': '[00:01:37](https://www.youtube.com/watch?v=ArxvRqneZ_c&t=97s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Kf0-irBt3DU',
                       'title': 'Tariff Calculation for Power/Energy/Electricity',
                       'channel': 'Mock Theta Studies',
                       'author': 'Mock Theta Studies',
                       'text': 'Capacity charge is derived on the basis of AFC, which constitutes return '
                               'on equity, interest on loan capital, depreciation, interest on working '
                               'capital and O and M expenses.',
                       'tip': 'Capacity charge is derived on the basis of AFC, which constitutes return on '
                              'equity, interest on loan capital, depreciation, interest on working capital '
                              'and O and M expenses.',
                       'timestamp': 573,
                       'timestamp_seconds': 573,
                       'timestamp_label': '[00:09:33]',
                       'url': 'https://www.youtube.com/watch?v=Kf0-irBt3DU&t=573s',
                       'markdown': '[00:09:33](https://www.youtube.com/watch?v=Kf0-irBt3DU&t=573s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '5_ptAtJKgqM',
                       'title': 'Bill Audit Video',
                       'channel': 'Poteck Power Corporation',
                       'author': 'Poteck Power Corporation',
                       'text': 'Jeremy offered his services on contingency and recovers funds in about 30 '
                               'percent of cases, with some clients being owed over $90,000.',
                       'tip': 'Jeremy offered his services on contingency and recovers funds in about 30 '
                              'percent of cases, with some clients being owed over $90,000.',
                       'timestamp': 52,
                       'timestamp_seconds': 52,
                       'timestamp_label': '[00:00:52]',
                       'url': 'https://www.youtube.com/watch?v=5_ptAtJKgqM&t=52s',
                       'markdown': '[00:00:52](https://www.youtube.com/watch?v=5_ptAtJKgqM&t=52s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'bPG_PW4MubQ',
                       'title': 'Utility Bill Audit',
                       'channel': 'ASHE AHA',
                       'author': 'ASHE AHA',
                       'text': 'Utility bills can have calculation errors, meter reading errors, or even '
                               'have the facility in the wrong customer rate class.',
                       'tip': 'Utility bills can have calculation errors, meter reading errors, or even '
                              'have the facility in the wrong customer rate class.',
                       'timestamp': 58,
                       'timestamp_seconds': 58,
                       'timestamp_label': '[00:00:58]',
                       'url': 'https://www.youtube.com/watch?v=bPG_PW4MubQ&t=58s',
                       'markdown': '[00:00:58](https://www.youtube.com/watch?v=bPG_PW4MubQ&t=58s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q4.'}]}
