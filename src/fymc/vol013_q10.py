from __future__ import annotations

CHAPTER_10 = {'id': 'Q10',
 'chapter_id': 'Q10',
 'chapter_number': 10,
 'question_number': 10,
 'slug': 'administer-audit-and-account-for-royalties',
 'question_prompt': 'How do I administer licensing agreements, interpret royalty statements, investigate '
                    'missing payments and account for licensing revenue?',
 'kicker': 'Q10 / THE BIG MONEY PLAYBOOKS',
 'title': 'Administer, Audit and Account for Royalties',
 'subtitle': 'Flowhaven agreement and approval workflows, royalty-audit red flags, publisher statements, '
             'book advances, author finances, contract pitfalls and ASC 606/PFRS 15',
 'layout_template': 'expert_commentary',
 'reading_time_minutes': 15,
 'executive_summary': 'Across music, publishing, brand, and patent licensing, practitioners agree royalty '
                      'statements are wrong more often than not: Uncover Fraud cites up to 89% of audited '
                      'licensees underreporting, and CPA Julie Tate finds errors about 75% of the time, '
                      'typically 10-20% underreported. The consensus playbook is to lock audit rights, '
                      'cost-shifting thresholds of 5-10%, and long look-back windows into the contract, '
                      'then escalate from desktop review to formal audit. Street mechanics include '
                      "Flowhaven's line-by-line contract-matched statement checks, Keith Bernstein's "
                      "seasonal-quarter sampling with a 36-month fallback, Tate's per-ISBN unit tracking "
                      "and BookScan checks at about $50-65 per ISBN, and BISG's proposed 35-field rights "
                      'statement standard. Recoveries reportedly run 5-20 times audit cost. Disagreements '
                      'center on gross versus net royalty bases, paying undisputed amounts immediately, '
                      'and whether audits are worth their cost versus switching distributors.',
 'key_metrics': [{'label': 'Audited licensees that underreport',
                  'metric': 'Audited licensees that underreport',
                  'value': 'Up to 89%',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Royalty compliance report cited for licensees that underreport and underpay, '
                             'whether intentionally or unintentionally',
                  'source': 'Uncover Fraud ([9Fku-QlhyHc @ 00:03:28])'},
                 {'label': 'Royalty recovery multiple versus audit cost',
                  'metric': 'Royalty recovery multiple versus audit cost',
                  'value': '5 to 20 times the cost of the audit',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Findings from royalty audits and royalty compliance investigations on '
                             'recoveries relative to audit spend',
                  'source': 'Uncover Fraud ([9Fku-QlhyHc @ 00:05:08])'},
                 {'label': 'Frequency of errors in reviewed royalty statements',
                  'metric': 'Frequency of errors in reviewed royalty statements',
                  'value': 'About 75% of the time',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Julie Tate, CPA, on how often her publisher royalty reviews find errors; '
                             'underreporting typically runs 10-20%',
                  'source': 'Authors Guild ([NrMiKZwGTD4 @ 00:45:56])'},
                 {'label': 'Audit cost reimbursement trigger',
                  'metric': 'Audit cost reimbursement trigger',
                  'value': 'Underpayment finding of 5% or greater',
                  'confidence': 'attributed_practitioner_claim',
                  'context': 'Contract term Tate tells authors to insert so the publisher reimburses the '
                             'cost of the audit',
                  'source': 'Authors Guild ([NrMiKZwGTD4 @ 00:57:10])'}],
 'sections': [{'section_number': 1,
               'title': 'The Practitioner Consensus',
               'paragraphs': ['Every audit-side practitioner here starts from the same premise: royalty '
                              'statements usually contain errors, and the licensor who never checks '
                              'absorbs the loss. Uncover Fraud cites a royalty compliance report finding '
                              'that up to 89% of audited licensees underreport and underpay, whether '
                              'intentionally or not, and frames royalty administration as a cost center '
                              'for the licensee [9Fku-QlhyHc @ 00:03:28]. Julie Tate, the CPA presenting '
                              'for the Authors Guild, says errors turn up about 75% of the time, with '
                              'underreporting typically landing between 10% and 20% of what is owed '
                              '[NrMiKZwGTD4 @ 00:45:56]. PKF Texas agrees misreporting is common but calls '
                              'most of it unintentional: licensees do not set their systems up for each '
                              'agreement, and large licensees juggling many deals simply cannot meet them '
                              'all [Z-vXnFsa6zY @ 00:00:55]. Secrets of the music industry says the '
                              "label's whole bet is that artists will never use the audit right, because "
                              'exercising it costs tens of thousands of dollars, eats months, runs into '
                              'unfamiliarity with the process, and triggers fear for their careers '
                              '[DfuXhSrezTU @ 00:01:42]. The shared conclusion across music, books, and '
                              "brand licensing is blunt: the error lives inside the licensee's process, so "
                              "catching it is the licensor's job, not the licensee's.",
                              'The second point of agreement is that the audit right has to be engineered '
                              'into the deal before the first statement arrives. Legal Tips for Smart '
                              'Entrepreneurs lays out the standard trade: if the discrepancy exceeds a '
                              'percentage the parties agree on, the licensee pays for the audit, and below '
                              'it the licensor pays, with the licensor fronting the cost out of pocket '
                              'first [GLaoDfT8SDA @ 00:01:39]. In the Artist Rights Institute session with '
                              'Keith Bernstein, cost-shifting triggers land at 5%, 7.5%, or 10%, and '
                              'look-back periods usually run 24 to 36 months [cirxW12BS2k @ 00:27:47]. '
                              'Julie Tate pushes for reimbursement at a 5% underpayment finding and warns '
                              'hard against look-back limits, recalling a client who accepted a 2-year '
                              'window against an 11-year statute [NrMiKZwGTD4 @ 00:52:45]. Secrets of the '
                              'music industry hammers the same clock: most contracts give only a 2- or '
                              '3-year window to audit a statement, so you cannot wait around [DfuXhSrezTU '
                              '@ 00:04:03]. Tate also notes the limits differ by state, with New York '
                              'allowing 6 years and California 4. The baseline package therefore has three '
                              'parts: a written audit right, a cost-shifting threshold, and the longest '
                              'look-back the licensor can win at the table.',
                              'Practitioners also agree that auditing is a ladder, not a switch. Sabarwal '
                              'Law calls the binary view a misconception: low earnings may justify no '
                              'audit or only limited procedures, and a desk audit uses nothing but the '
                              'agreement and incoming statements to confirm reported rates match the '
                              'contract [4ZKPBotNzQw @ 00:00:47]. Bernstein tells artists to start desktop '
                              'reviews within 6 to 9 months, act as their own income tracker, and check '
                              'metadata before anyone talks about a full audit [cirxW12BS2k @ 00:04:40]. '
                              'Flowhaven builds the same discipline into software, checking each quarterly '
                              'report line by line against the contract and kicking flagged lines back to '
                              'the partner while accepting the rest [M69XC4rxxQc @ 00:03:10]. When the '
                              'stakes justify escalation, Uncover Fraud wants forensic accountants on the '
                              'job, especially where litigation is possible, and insists the posture stay '
                              'non-hostile throughout [9Fku-QlhyHc @ 00:11:11]. The deterrent effect is '
                              'the other common thread: licensees self-correct once notified of an audit, '
                              'per Uncover Fraud, and Secrets of the music industry says even the threat '
                              'of an audit deters errors. The minimum viable royalty function, by '
                              'consensus, is a licensor who reads every statement against the contract, '
                              'escalates in measured steps, and makes clear that someone is watching.'],
               'table': {'caption': 'Where practitioners converge on royalty administration and audit '
                                    'baselines',
                         'headers': ['Consensus Point',
                                     'What Practitioners Report',
                                     'Operator Implication',
                                     'Expert Source'],
                         'rows': [['Underreporting is the norm across audited licensees, not the exception',
                                   'Up to 89% of audited licensees underreport and underpay their '
                                   'royalties',
                                   'Assume every statement needs checking before accepting the payment as '
                                   'final',
                                   'Uncover Fraud ([9Fku-QlhyHc @ 00:03:28])'],
                                  ['Most misreporting stems from licensee systems rather than deliberate '
                                   'intent',
                                   'Systems are not set up per agreement; large licensees cannot meet them '
                                   'all',
                                   'Aim trend analysis, late statements, and missed payments at the '
                                   'riskiest agreements',
                                   'PKF Texas ([Z-vXnFsa6zY @ 00:01:29])'],
                                  ['Errors surface in most publisher statements that get professionally '
                                   'reviewed',
                                   'Errors appear about 75% of the time; underreporting typically runs '
                                   '10-20%',
                                   'Budget review time for every statement cycle, not occasional spot '
                                   'checks',
                                   'Authors Guild ([NrMiKZwGTD4 @ 00:45:56])'],
                                  ['Contractual audit windows are short and close on the licensor quietly',
                                   'Most contracts allow only a 2 or 3 year window to audit a statement',
                                   'Calendar every statement date and launch reviews well before the '
                                   'window expires',
                                   'Secrets of the music industry ([DfuXhSrezTU @ 00:04:03])'],
                                  ['Audit cost-shifting thresholds belong in the original license, not '
                                   'later negotiations',
                                   'Licensee pays for the audit when the discrepancy exceeds the agreed '
                                   'percentage',
                                   'Negotiate the threshold upfront because the licensor fronts audit '
                                   'costs out of pocket',
                                   'Legal Tips for Smart Entrepreneurs ([GLaoDfT8SDA @ 00:01:39])'],
                                  ['Audits scale from a cheap desk review up to a formal engagement',
                                   'Desk audit checks reported rates against the contract using only '
                                   'incoming statements',
                                   'Start cheap and escalate to audit notice and attorneys only when '
                                   'warranted',
                                   'Sabarwal Law ([4ZKPBotNzQw @ 00:00:47])'],
                                  ['Contract-matched line checks catch out-of-scope sales before money is '
                                   'accepted',
                                   'Flagged lines included an ungranted territory, unapproved product, and '
                                   'mismatched rate',
                                   'Send flagged lines back to the partner, accept the rest, raise the '
                                   'invoice',
                                   'Flowhaven ([M69XC4rxxQc @ 00:03:10])']]}},
              {'section_number': 2,
               'title': 'Exact Street Mechanics, Tools & Numbers',
               'paragraphs': ["Uncover Fraud's execution sequence is the most complete audit playbook any "
                              'practitioner here lays out. Plan from red flags, meaning communication '
                              'history, licensor-side analysis, interpretation errors, and non-reporting; '
                              "run the first audit after year one; learn the licensee's systems; then send "
                              'the timeline and document requests [9Fku-QlhyHc @ 00:07:59]. In fieldwork, '
                              'test the sales base whether unit, gross, or net, then net-sales '
                              'adjustments, return allocation, tiered rates, and derivative products; '
                              'recalculate what should have been paid, compare it to what was paid, '
                              'reconcile to inventory, invoices, and purchases, and chase the cause of '
                              'every variance [9Fku-QlhyHc @ 00:11:51]. Bernstein sets scope by deal type: '
                              'for unit-based deals, test usage data against the statement; for '
                              'receipts-based deals, examine the books; for subscriber-based or greater-of '
                              'deals, check subscriber counts [cirxW12BS2k @ 00:09:58]. His sampling trick '
                              'is to pull one seasonal quarter, classify each error as system, '
                              'non-recurring, creative, or inadvertent, and project a recurring rate; if '
                              'the licensee refuses to accept that rate, demand data for every month '
                              "across all 36 [cirxW12BS2k @ 00:15:49]. Uncover Fraud's toolkit runs to "
                              'data warehouses, data mining, software, and programming languages, and '
                              'Bernstein notes some audits involve 16 billion streams a month, so he '
                              'requests upstream raw logs.',
                              "On the publishing side, Julie Tate's checks start at the statement itself, "
                              'line by line. Royalties are reported per ISBN, so track life-to-date units '
                              'by hand and verify tiering, since she has caught missed escalations such as '
                              'an extra 2% after 5,000 copies [NrMiKZwGTD4 @ 00:28:39]. She trends the '
                              'effective rate against units, checks ISBNs in Bookwire, which surfaced '
                              '$300K underpaid on high-school editions, and pulls Nielsen BookScan data at '
                              'about $50 to $65 per ISBN, while distrusting Amazon Author Rank '
                              '[NrMiKZwGTD4 @ 00:26:20]. Her standard records request covers sales detail, '
                              'inventory, subrights contracts and remittances, return reserves around 10%, '
                              'the bill of materials, and destroyed copies above 3 to 5%; up to 3% '
                              'unaccounted inventory is acceptable, while 15% is a big problem. For rights '
                              'income, Sebastian Richer, a sub-agent at More Books, matches payment to '
                              'statement, statement to contract via a contract or deal ID because the ISBN '
                              'is useless at contract level, then line items via ONIX [Xy0iIdZDIHk @ '
                              "00:22:50]. The BISG committee's proposed standard runs about 35 fields, "
                              'including original advance and currency, life-to-date net units, ISBN-13, '
                              'ONIX codes, royalty basis, and bank and FX details, to kill what it calls '
                              'mystery money [Xy0iIdZDIHk @ 00:13:33].',
                              'Brand and patent licensors front-load the controls into the agreement '
                              "itself. Flowhaven's setup starts from an agreement type, assigns licensor "
                              'and licensee, sets rights by brand, category, channel, and territory such '
                              'as FI, SE, NO, and DK, then sets a rate per channel, ten percent for '
                              'wholesale and twelve for online, plus a minimum guarantee with '
                              'installments, due dates, and visible recoupment [M69XC4rxxQc @ 00:01:48]. '
                              'Unused rights show up as white space you can sell, and a factory with an '
                              'expired audit simply cannot be picked at approval. Legal Tips for Smart '
                              'Entrepreneurs prefers a percentage of gross sales because net profit is '
                              'more work to calculate, and has the parties fix a monthly, quarterly, or '
                              'yearly payment schedule [GLaoDfT8SDA @ 00:00:58]. Bao Tran wants net sales '
                              'precisely defined, instead of the 25% rule rejected in Uniloc v. Microsoft, '
                              'a 30-day payment cure window and a 60-day breach window, and annual '
                              'minimums or milestones on any exclusive license so the licensee cannot '
                              'shelve the invention [k9Sb2smIIjM @ 00:04:48]. The payoff math justifies '
                              'the effort: Uncover Fraud reports recoveries running 5 to 20 times the '
                              "audit cost, and a $60M recovery still only ranks among the speaker's top "
                              'five engagements [9Fku-QlhyHc @ 00:05:08].'],
               'table': {'caption': 'Exact numbers, tools, and mechanics practitioners use to administer '
                                    'and audit royalties',
                         'headers': ['Mechanic',
                                     'Exact Numbers or Tools Stated',
                                     'How Operators Use It',
                                     'Expert Source'],
                         'rows': [['Per-channel royalty rates set inside the agreement record',
                                   '10% for wholesale or retail and 12% for online sales',
                                   'Rates are fixed per channel before any quarterly report is checked',
                                   'Flowhaven ([M69XC4rxxQc @ 00:01:48])'],
                                  ['Desktop review timing and look-back window for artist deals',
                                   'Start desktop reviews within 6-9 months; look-back usually 24-36 '
                                   'months',
                                   'Act as your own income tracker and check metadata early and often',
                                   'Artist Rights Institute ([cirxW12BS2k @ 00:04:40])'],
                                  ['Auditor cost-coverage threshold written into the audit clause',
                                   'Auditor costs covered at a 5%, 7.5%, or 10% discrepancy threshold',
                                   'Write the trigger and specify the exact source data owed to auditors',
                                   'Artist Rights Institute ([cirxW12BS2k @ 00:27:47])'],
                                  ['Inventory reconciliation tolerance for publisher royalty audits',
                                   'Up to 3% unaccounted inventory acceptable; 15% signals a big problem',
                                   'Request inventory records and reconcile against reported sales and '
                                   'destroyed copies',
                                   'Authors Guild ([NrMiKZwGTD4 @ 00:33:03])'],
                                  ['Independent unit data to test publisher-reported sales figures',
                                   'Nielsen BookScan at roughly $50-65 per ISBN; Bookwire ISBN checks',
                                   'Bookwire check found $300K underpaid on high-school editions of a '
                                   'title',
                                   'Authors Guild ([NrMiKZwGTD4 @ 00:47:52])'],
                                  ['Rights statement processing load measured across industry respondents',
                                   '77% spent a full day or more on single statements; 58% follow up one '
                                   'in three',
                                   'Push senders for standardized fields and a unique deal identifier on '
                                   'statements',
                                   'Book Industry Study Group ([Xy0iIdZDIHk @ 00:09:06])'],
                                  ['Revenue recognition split for a bundled software and brand license',
                                   '$660,000 deal: $330,000 recognized in Q1, $330,000 deferred over 33 '
                                   'months',
                                   'Book functional IP point-in-time; symbolic brand license ratably at '
                                   '$10,000 monthly',
                                   'Jobank CPA ([eoUe3NebB3E @ 00:08:18])']]},
               'callout': {'kind': 'INSIDER PRO-TIPS',
                           'title': 'Clause and fieldwork moves the auditors swear by',
                           'body': 'These are the small contractual and procedural levers practitioners '
                                   'use to keep audits fast, cheap, and defensible once the licensee '
                                   'starts pushing back.',
                           'items': ['Demand a draft-report review clause: a $500K+ claim collapsed over a '
                                     'formula error and an overlooked box-set amendment, and the fix was '
                                     'later adopted in statutory audits [Artist Rights Institute — '
                                     'cirxW12BS2k @ 00:19:54].',
                                     'Specify the source data in the audit clause, because one auditee '
                                     "answered an 'all books and records' request by printing everything "
                                     'out onto a table [Artist Rights Institute — cirxW12BS2k @ 00:28:04].',
                                     'Treat unexplained adjustments, chronically late statements, '
                                     'Excel-made statements, new statement formats or software, new '
                                     'royalty staff, and mergers as red flags [Authors Guild — NrMiKZwGTD4 '
                                     '@ 00:08:28].',
                                     'When one audit quote comes in cheaper, ask what procedures it is '
                                     'skipping, and do only the minimum work needed to find out what '
                                     'really happened [Sabarwal Law — 4ZKPBotNzQw @ 00:02:29].']},
               'sop_steps': [{'step': 1,
                              'title': 'Build the contract-matched royalty record',
                              'action': 'Load every agreement with rights, rates, and minimum guarantee '
                                        'terms before the first report arrives.',
                              'detail': 'Start from an agreement type, pick licensor and licensee, set '
                                        'rights by brand, category, channel, and territory, then enter '
                                        'per-channel rates and minimum guarantee installments with due '
                                        'dates so recoupment is visible [Flowhaven — M69XC4rxxQc @ '
                                        '00:01:32].'},
                             {'step': 2,
                              'title': 'Desk-review every incoming statement',
                              'action': 'Check reported rates against the contract using only the '
                                        'agreement and the statement.',
                              'detail': 'Run the desk audit on each statement to confirm reported rates '
                                        'match the contract, and track life-to-date units per ISBN by hand '
                                        'to verify tiering and escalations [Sabarwal Law — 4ZKPBotNzQw @ '
                                        '00:00:47].'},
                             {'step': 3,
                              'title': 'Escalate with system knowledge and document requests',
                              'action': "Learn the licensee's systems, then send the timeline and the "
                                        'document request list.',
                              'detail': 'Plan from red flags such as communication history and '
                                        'non-reporting, run the first audit after year one, learn the '
                                        "licensee's systems, then issue the timeline and document requests "
                                        '[Uncover Fraud — 9Fku-QlhyHc @ 00:08:18].'},
                             {'step': 4,
                              'title': 'Sample, classify, and recalculate',
                              'action': 'Test a seasonal quarter, classify every error, and push for a '
                                        'recurring error rate.',
                              'detail': 'Sample a seasonal quarter, classify errors as system, '
                                        'non-recurring, creative, or inadvertent, and if the other side '
                                        'rejects the recurring error rate, demand data for every month '
                                        'across all 36 months [Artist Rights Institute — cirxW12BS2k @ '
                                        '00:14:52].'}]},
              {'heading': 'Where Practitioners Disagree & Alternative Playbooks',
               'paragraphs': ['Who fronts the audit bill and when to pull the trigger splits the room. '
                              'Legal Tips for Smart Entrepreneurs builds the audit right around a '
                              'negotiated discrepancy percentage: if the gap lands above the number both '
                              'parties agreed, the licensee eats the audit cost; below it, the licensor '
                              'pays, and the licensor fronts the money out of pocket first [GLaoDfT8SDA @ '
                              '00:01:39]. Julie Tate of the Authors Guild hardwires the number instead, '
                              'telling authors to write an underpayment finding of 5% or greater into the '
                              'contract as the trigger for the publisher reimbursing the cost of an audit '
                              '[NrMiKZwGTD4 @ 00:57:10]. Timing diverges just as sharply. Uncover Fraud '
                              'schedules the first audit after year one of the license, once a reporting '
                              "history exists, and only after learning the licensee's systems and sending "
                              'a timeline with document requests [9Fku-QlhyHc @ 00:07:59]. The Artist '
                              'Rights Institute session with Keith Bernstein moves faster and cheaper: '
                              'start desktop reviews within six to nine months, act as your own income '
                              'tracker, and check the metadata before anyone talks about a formal audit '
                              '[cirxW12BS2k @ 00:04:40]. The operator split is clear: lock a cost-shift '
                              'percentage into the deal early, then decide whether the first move is a '
                              'self-run desk check or a scheduled forensic engagement.',
                              'How deep to dig is the second fault line. Sabarwal Law rejects the idea '
                              'that an audit is binary: low earnings may justify no audit or only limited '
                              'procedures, and a desk audit uses nothing but the agreement and the '
                              'incoming statements to confirm the reported rates match the contract '
                              '[4ZKPBotNzQw @ 00:00:47]. Uncover Fraud pushes the opposite direction, '
                              'arguing forensic accountants should run the engagement, especially where '
                              'litigation is possible, testing the sales base, net-sales adjustments, '
                              'return allocations, tiered rates and derivative products before reconciling '
                              'to inventory, invoices and purchases [9Fku-QlhyHc @ 00:11:11]. The Artist '
                              'Rights Institute panel concedes audits can be cost prohibitive and offers a '
                              'street-level alternative: send general questions first, and treat switching '
                              'distributors as its own test of whether the old statements ran short '
                              '[cirxW12BS2k @ 00:07:54]. Secrets of the music industry frames the cost '
                              "problem as the label's bet, that artists will never use the right because "
                              'an audit runs tens of thousands of dollars, eats months, feels unfamiliar '
                              'and scares people about their careers [DfuXhSrezTU @ 00:02:16]. Its '
                              'counter-play is pooling costs through collectives and leaning on the fact '
                              'that even the threat of an audit deters errors.',
                              'The third split is over why the money goes missing and how hard to push. '
                              'PKF Texas reads most misreporting as unintentional: systems are not set up '
                              'for each individual agreement, and large licensees juggling many deals '
                              "simply can't meet them all, and the firm serves licensors and licensees "
                              'only on separate engagements to maintain a level of independence '
                              "[Z-vXnFsa6zY @ 00:00:55]. Uncover Fraud lists fraud and non-arm's-length "
                              'related-party sales right beside misinterpretation, and cites a compliance '
                              'report showing up to 89% of audited licensees underreport and underpay, '
                              'whether intentional or not [9Fku-QlhyHc @ 00:03:28]. Inside the Artist '
                              'Rights Institute session the host and Keith Bernstein split on settlement '
                              'tactics: the host wants undisputed amounts paid now, while Bernstein flags '
                              'timing and settlement concerns with that move [cirxW12BS2k @ 00:25:39]. On '
                              'statement standards, the Book Industry Study Group committee refuses to '
                              'play enforcer, stating there are no royalty police in the ecosystem and '
                              'pushing enforcement through the deal itself, even after an attendee pushed '
                              'back that the industry has been talking about this literally for years '
                              '[Xy0iIdZDIHk @ 00:52:59]. Operators choose between a non-hostile posture '
                              'that assumes system error and an adversarial one that assumes leakage until '
                              'the recalculation proves otherwise.'],
               'table': {'caption': 'Competing royalty administration and audit playbooks, side by side',
                         'headers': ['Decision Point', 'Playbook A', 'Playbook B', 'Expert Source'],
                         'rows': [['Royalty base: gross sales versus defined net sales',
                                   'Use a percentage of gross sales because gross takes out most of the '
                                   'headaches of net profit math',
                                   'Use precisely defined net sales; academic presses pay on net while '
                                   'trade more commonly bases royalties on list price',
                                   'Legal Tips for Smart Entrepreneurs ([GLaoDfT8SDA @ 00:00:20]); Bao '
                                   'Tran, Esq. | Patent Attorney ([k9Sb2smIIjM @ 00:03:43]); Ideas on Fire '
                                   '([QHV5OSGnAMg @ 00:11:12])'],
                                  ['Audit cost shift threshold written into the license',
                                   'Licensee pays only above a discrepancy percentage the parties '
                                   'negotiate, with the licensor fronting costs first',
                                   'Hardwire reimbursement at a 5% underpayment finding, or negotiate '
                                   'auditor cost coverage at 5%, 7.5% or 10%',
                                   'Legal Tips for Smart Entrepreneurs ([GLaoDfT8SDA @ 00:01:39]); Authors '
                                   'Guild ([NrMiKZwGTD4 @ 00:57:10]); Artist Rights Institute '
                                   '([cirxW12BS2k @ 00:27:47])'],
                                  ['Timing of the first royalty review',
                                   "Run the first formal audit after year one, once the licensee's systems "
                                   'are learned and documents requested',
                                   'Start self-run desktop reviews within six to nine months and act as '
                                   'your own income tracker',
                                   'Uncover Fraud ([9Fku-QlhyHc @ 00:07:59]); Artist Rights Institute '
                                   '([cirxW12BS2k @ 00:04:40])'],
                                  ['Depth of audit procedures',
                                   'Desk audit using only the agreement and incoming statements to verify '
                                   'reported rates match the contract',
                                   'Forensic engagement using data warehouses, data mining, software and '
                                   'programming languages to recalculate everything',
                                   'Sabarwal Law ([4ZKPBotNzQw @ 00:00:47]); Uncover Fraud ([9Fku-QlhyHc @ '
                                   '00:15:04])'],
                                  ['Look-back coverage and sampling strategy',
                                   'Sample a seasonal quarter, classify the errors, then demand all 36 '
                                   'months if the error rate is rejected',
                                   'Refuse contractual look-back limits entirely; one client accepted two '
                                   'years against an 11-year statute',
                                   'Artist Rights Institute ([cirxW12BS2k @ 00:15:49]); Authors Guild '
                                   '([NrMiKZwGTD4 @ 00:52:45])'],
                                  ['Undisputed amounts while the audit claim is contested',
                                   'Host position: get the undisputed money paid now while the contested '
                                   'items are still fought',
                                   'Keith Bernstein position: raises timing and settlement concerns about '
                                   'splitting payment out early',
                                   'Artist Rights Institute ([cirxW12BS2k @ 00:25:39])'],
                                  ['Enforcing rights royalty statement standards',
                                   'Committee publishes recommended fields with no royalty police; '
                                   'enforcement runs through the deal itself',
                                   'Attendee pushback that the industry has been talking about this '
                                   'problem literally for years',
                                   'Book Industry Study Group ([Xy0iIdZDIHk @ 00:52:59]); Book Industry '
                                   'Study Group ([Xy0iIdZDIHk @ 00:51:58])']]}},
              {'heading': 'Firsthand Failure Modes, Traps & Economics Checks',
               'paragraphs': ['Statement errors are the baseline, not the exception. Julie Tate of the '
                              'Authors Guild reports errors turn up about 75% of the time, and her error '
                              'log reads like a checklist of leaks: wrong royalty base, unreported ISBNs, '
                              'printing cost deducted, currency-conversion mistakes and missed escalations '
                              'such as the extra 2% owed after 5,000 copies [NrMiKZwGTD4 @ 00:45:56]. '
                              "Flowhaven's demo shows the same leaks surfacing at the line level in a "
                              'single quarterly report: three lines flagged for an ungranted territory, an '
                              'unapproved product and a mismatched rate, with the flagged lines sent back '
                              'to the partner, the rest accepted and an invoice request raised '
                              '[M69XC4rxxQc @ 00:03:10]. The reconciliation labor is the hidden cost. The '
                              'Book Industry Study Group survey found 77% of respondents spent a full day '
                              'or more on single statements, 58% said one in three statements needs '
                              'follow-up with the sender, and eight respondents spent weeks or months '
                              'reconciling [Xy0iIdZDIHk @ 00:09:06]. Even unearned statements carry money: '
                              'an accountant reviewing statements with no royalties yet due found '
                              'significant revenue in errors [Xy0iIdZDIHk @ 00:07:47]. Skipping the '
                              'line-by-line check means accepting those error rates as paid in full.',
                              'The auditor can be the failure point too. The Artist Rights Institute panel '
                              'warns against rabbit holes such as chasing a $400 issue, and reports '
                              'auditors inflating claims, including a 20% claim built on nothing more than '
                              'a missing comma [cirxW12BS2k @ 00:18:13]. The worst reversal: a claim north '
                              'of $500,000 collapsed because of a formula error and an overlooked box-set '
                              'amendment, and the fix was a draft-report review clause, later adopted in '
                              'statutory audits [cirxW12BS2k @ 00:19:54]. Records requests fail when they '
                              'are vague; one auditee answered a demand for all books and records by '
                              "printing them out and laying them on a table, so the panel's playbook is to "
                              'specify source data and request upstream raw logs, in audits that can '
                              'involve 16 billion streams a month [cirxW12BS2k @ 00:28:04]. Sabarwal Law '
                              'adds the economic sanity check: a shortfall may simply mean the product is '
                              'underperforming, not that anyone is stealing, so the job is to do the '
                              'minimum work needed to find out what really happened [4ZKPBotNzQw @ '
                              '00:03:55]. A custom proposal of procedures and fees beats a cheap quote, '
                              'because a lower number raises the question of what the auditor is skipping.',
                              'Some losses are locked in at signing. Julie Tate describes a client who '
                              'accepted a two-year look-back limit against an 11-year statute, and notes '
                              'New York allows six years and California four, so a short contractual cap '
                              'quietly forfeits recoverable money [NrMiKZwGTD4 @ 00:52:45]. Bao Tran shows '
                              'how a patent license can vanish outright: three maintenance fees total '
                              '$14,470, a late payment adds a $540 surcharge, and a lapse evaporates the '
                              "license [k9Sb2smIIjM @ 00:02:48]. On the licensor's own books, Jobank CPA "
                              'walks through a $660,000 deal where sales and the CFO wanted the full '
                              'amount in month one; booking the $360,000 symbolic brand license upfront '
                              'leads to restatements and board fallout, because it recognizes at $10,000 a '
                              'month over 36 months [eoUe3NebB3E @ 00:05:13]. Alexa Donne flags the '
                              'author-side accounting trap in a two-book deal at $25,000 each: book one '
                              'earns $30,000, which alone would pay $5,000 in royalties, but book two '
                              'earns only $10,000, so the joint $40,000 total sits short of the $50,000 '
                              'advance and nothing pays out, which is why agents fight for separate '
                              'accounting [yAYeomyyeP8 @ 00:12:19]. Each trap is visible on paper long '
                              'before the money goes missing.'],
               'table': {'caption': 'Firsthand royalty failure modes with the economics check '
                                    'practitioners apply',
                         'headers': ['Failure Mode',
                                     'What Practitioners Saw',
                                     'Economics Check',
                                     'Expert Source'],
                         'rows': [['Late and irregular royalty statements',
                                   "One client's statements always arrived six months late; Donne's "
                                   'statements sometimes arrive eight months late',
                                   'Treat late statements and missed payments as red flags and run trend '
                                   'analysis on risky areas',
                                   'Authors Guild ([NrMiKZwGTD4 @ 00:08:28]); Alexa Donne ([yAYeomyyeP8 @ '
                                   '00:10:53]); PKF Texas ([Z-vXnFsa6zY @ 00:01:29])'],
                                  ['Unaccounted inventory at the licensee or publisher',
                                   'Inventory records requested during the audit show copies that cannot '
                                   'be accounted for',
                                   'Up to 3% unaccounted is acceptable; 15% of inventory unaccounted for '
                                   'is a big problem',
                                   'Authors Guild ([NrMiKZwGTD4 @ 00:33:03])'],
                                  ['Auditor claim collapses at the finish line',
                                   'A claim above $500,000 collapsed on a formula error and an overlooked '
                                   'box-set amendment',
                                   'Require a draft-report review clause so errors surface before the '
                                   'claim goes final',
                                   'Artist Rights Institute ([cirxW12BS2k @ 00:19:54])'],
                                  ['Patent maintenance fees lapse mid-license',
                                   'A lapse evaporates the license and the running royalty stream attached '
                                   'to it',
                                   'Three maintenance fees total $14,470 and a late payment adds a $540 '
                                   'surcharge',
                                   'Bao Tran, Esq. | Patent Attorney ([k9Sb2smIIjM @ 00:02:48])'],
                                  ['Symbolic IP or usage royalties booked too early',
                                   'Sales and the CFO wanted a $660,000 deal booked in month one; auditors '
                                   'flag it and force restatement',
                                   'Recognize $330,000 in Q1 and defer $330,000 over 33 months; wait for '
                                   'actual sale or usage on royalties',
                                   'Jobank CPA ([eoUe3NebB3E @ 00:08:18]); Accountancy Students Hub '
                                   '([o0riJRlxTsY @ 00:04:28])'],
                                  ['Joint accounting across a multi-book deal',
                                   'Book one earns $30,000 but book two earns $10,000 against two $25,000 '
                                   'advances',
                                   'Joint $40,000 total stays short of the $50,000 advance, so push for '
                                   'separate accounting',
                                   'Alexa Donne ([yAYeomyyeP8 @ 00:12:19])'],
                                  ['Exclusive license with no minimums or milestones',
                                   'Licensee can shelve the invention while exclusivity bars even the '
                                   'inventor in that field',
                                   'Tie exclusivity to annual minimums or milestones; non-exclusive terms '
                                   'allow multiple partners',
                                   'Bao Tran, Esq. | Patent Attorney ([k9Sb2smIIjM @ 00:01:27]); Bao Tran, '
                                   'Esq. | Patent Attorney ([k9Sb2smIIjM @ 00:03:25])']]},
               'callout': {'kind': 'OPERATOR GATE',
                           'title': 'Stop-Loss Checks Before Signing or Filing a Royalty Claim',
                           'body': 'Every item below is a loss a practitioner watched happen firsthand; '
                                   'clear all four before signing the license or pushing an audit claim to '
                                   'final.',
                           'items': ['Strike short contractual look-back caps; a client who accepted two '
                                     'years against an 11-year statute forfeited most of the recoverable '
                                     'window [Authors Guild — NrMiKZwGTD4 @ 00:52:45].',
                                     'Demand a draft-report review before any claim goes final; a $500K+ '
                                     'claim collapsed on a formula error and an overlooked box-set '
                                     'amendment [Artist Rights Institute — cirxW12BS2k @ 00:19:54].',
                                     'Rule out plain underperformance before alleging underpayment, '
                                     'because a shortfall may simply mean the product is not selling '
                                     '[Sabarwal Law — 4ZKPBotNzQw @ 00:03:55].',
                                     'Check every royalty line against granted territory, approved product '
                                     'and contracted rate before accepting the report and raising an '
                                     'invoice [Flowhaven — M69XC4rxxQc @ 00:03:10].']}}],
 'pull_quote': '"According to one royalty compliance report, whether due to intentional or unintentional '
               'causes, up to 89% of audited licensees underreport and underpay royalties." Uncover Fraud '
               '(9Fku-QlhyHc @ 00:03:28).',
 'diagram_id': 'diag-02',
 'action_checklist': ['Track life-to-date units per ISBN by hand and verify every tier escalation against '
                      'the contract [Authors Guild — NrMiKZwGTD4 @ 00:07:12].',
                      'Start desktop reviews within six to nine months, act as your own income tracker and '
                      'check the metadata [Artist Rights Institute — cirxW12BS2k @ 00:04:40].',
                      'Check each quarterly report line by line, send flagged territory, product and rate '
                      'lines back to the partner, and accept the rest [Flowhaven — HkDV-RELNXc @ '
                      '00:03:10].',
                      'Write the audit right so the licensee pays for the audit when the discrepancy '
                      'exceeds the agreed percentage [Legal Tips for Smart Entrepreneurs — GLaoDfT8SDA @ '
                      '00:01:39].',
                      'Match payment to statement, then statement to contract with a contract or deal ID, '
                      'then line items via ONIX [Book Industry Study Group — Xy0iIdZDIHk @ 00:22:50].',
                      'Specify source data in the audit clause and request upstream raw logs instead of a '
                      'generic books-and-records demand [Artist Rights Institute — cirxW12BS2k @ '
                      '00:30:15].'],
 'statutory_citations': [{'title': 'Uncover Fraud — Royalty Audit: Why Every Licensor & Artist Needs a '
                                   'Forensic Accountant on Their Side | Uncover Fraud [00:05:08]',
                          'url': 'https://www.youtube.com/watch?v=9Fku-QlhyHc&t=308s',
                          'relevance': 'Primary practitioner testimony on royalty recoveries running 5 to '
                                       '20 times the cost of the audit.'},
                         {'title': 'Authors Guild — Understanding Your Royalty Statements and Learning '
                                   'What Questions to Ask Your Publisher [00:40:39]',
                          'url': 'https://www.youtube.com/watch?v=NrMiKZwGTD4&t=2439s',
                          'relevance': 'Primary practitioner testimony on underreporting typically running '
                                       '10 to 20% in royalty audits.'},
                         {'title': 'Artist Rights Institute — Royalty audits, steps and strategies. '
                                   '[00:27:47]',
                          'url': 'https://www.youtube.com/watch?v=cirxW12BS2k&t=1667s',
                          'relevance': 'Primary practitioner testimony on audit clause cost thresholds at '
                                       '5%, 7.5% or 10% and source data terms.'},
                         {'title': 'Jobank CPA — Episode 7 ASC 606 Licensing: Functional vs. Symbolic '
                                   'Intellectual Property [00:08:18]',
                          'url': 'https://www.youtube.com/watch?v=eoUe3NebB3E&t=498s',
                          'relevance': 'Primary practitioner testimony on splitting a $660,000 license '
                                       'deal into $330,000 recognized and $330,000 deferred.'}],
 'source_citations': [{'source_type': 'video_pro_tip',
                       'video_id': 'M69XC4rxxQc',
                       'title': 'How licensing teams run agreements, approvals and royalties in one place',
                       'channel': 'Flowhaven',
                       'author': 'Flowhaven',
                       'text': 'Then the rate for each channel: ten percent for wholesale, twelve for '
                               'online.',
                       'tip': 'Then the rate for each channel: ten percent for wholesale, twelve for '
                              'online.',
                       'timestamp': 108,
                       'timestamp_seconds': 108,
                       'timestamp_label': '[00:01:48]',
                       'url': 'https://www.youtube.com/watch?v=M69XC4rxxQc&t=108s',
                       'markdown': '[00:01:48](https://www.youtube.com/watch?v=M69XC4rxxQc&t=108s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'HkDV-RELNXc',
                       'title': 'How brand licensing teams run agreements, approvals and royalties in one '
                                'place',
                       'channel': 'Flowhaven',
                       'author': 'Flowhaven',
                       'text': 'The quarterly report is checked line by line, and three lines are flagged: '
                               'an ungranted territory, an unapproved product, and a mismatched rate.',
                       'tip': 'The quarterly report is checked line by line, and three lines are flagged: '
                              'an ungranted territory, an unapproved product, and a mismatched rate.',
                       'timestamp': 190,
                       'timestamp_seconds': 190,
                       'timestamp_label': '[00:03:10]',
                       'url': 'https://www.youtube.com/watch?v=HkDV-RELNXc&t=190s',
                       'markdown': '[00:03:10](https://www.youtube.com/watch?v=HkDV-RELNXc&t=190s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'GLaoDfT8SDA',
                       'title': 'Negotiate Like a Pro: Secure Your Royalties with This Licensing Fee '
                                'Secret',
                       'channel': 'Legal Tips for Smart Entrepreneurs',
                       'author': 'Legal Tips for Smart Entrepreneurs',
                       'text': 'If the discrepancy is above the percentage the parties agree on, the '
                               'licensee pays for the audit; below it, the licensor pays.',
                       'tip': 'If the discrepancy is above the percentage the parties agree on, the '
                              'licensee pays for the audit; below it, the licensor pays.',
                       'timestamp': 99,
                       'timestamp_seconds': 99,
                       'timestamp_label': '[00:01:39]',
                       'url': 'https://www.youtube.com/watch?v=GLaoDfT8SDA&t=99s',
                       'markdown': '[00:01:39](https://www.youtube.com/watch?v=GLaoDfT8SDA&t=99s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9Fku-QlhyHc',
                       'title': 'Royalty Audit: Why Every Licensor & Artist Needs a Forensic Accountant on '
                                'Their Side | Uncover Fraud',
                       'channel': 'Uncover Fraud',
                       'author': 'Uncover Fraud',
                       'text': 'Evidence from findings of royalty audits conducted by auditors and royalty '
                               'compliance investigation professionals suggest that royalty recoveries are '
                               'within the magnitude of 5 to 20 times the cost of conducting the royalty '
                               'audit.',
                       'tip': 'Evidence from findings of royalty audits conducted by auditors and royalty '
                              'compliance investigation professionals suggest that royalty recoveries are '
                              'within the magnitude of 5 to 20 times the cost of conducting the royalty '
                              'audit.',
                       'timestamp': 308,
                       'timestamp_seconds': 308,
                       'timestamp_label': '[00:05:08]',
                       'url': 'https://www.youtube.com/watch?v=9Fku-QlhyHc&t=308s',
                       'markdown': '[00:05:08](https://www.youtube.com/watch?v=9Fku-QlhyHc&t=308s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '9Fku-QlhyHc',
                       'title': 'Royalty Audit: Why Every Licensor & Artist Needs a Forensic Accountant on '
                                'Their Side | Uncover Fraud',
                       'channel': 'Uncover Fraud',
                       'author': 'Uncover Fraud',
                       'text': 'According to one royalty compliance report, whether due to intentional or '
                               'unintentional causes, up to 89% of audited licensees underreport and '
                               'underpay royalties.',
                       'tip': 'According to one royalty compliance report, whether due to intentional or '
                              'unintentional causes, up to 89% of audited licensees underreport and '
                              'underpay royalties.',
                       'timestamp': 208,
                       'timestamp_seconds': 208,
                       'timestamp_label': '[00:03:28]',
                       'url': 'https://www.youtube.com/watch?v=9Fku-QlhyHc&t=208s',
                       'markdown': '[00:03:28](https://www.youtube.com/watch?v=9Fku-QlhyHc&t=208s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cirxW12BS2k',
                       'title': 'Royalty audits, steps and strategies.',
                       'channel': 'Artist Rights Institute',
                       'author': 'Artist Rights Institute',
                       'text': 'Then I guess you got to give me the data for every month 36 months for '
                               'three years.',
                       'tip': 'Then I guess you got to give me the data for every month 36 months for '
                              'three years.',
                       'timestamp': 949,
                       'timestamp_seconds': 949,
                       'timestamp_label': '[00:15:49]',
                       'url': 'https://www.youtube.com/watch?v=cirxW12BS2k&t=949s',
                       'markdown': '[00:15:49](https://www.youtube.com/watch?v=cirxW12BS2k&t=949s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Z-vXnFsa6zY',
                       'title': 'Red Flags in Licensing and Royalty Audits | PKF Texas - The '
                                "Entrepreneur's Playbook",
                       'channel': 'PKF Texas',
                       'author': 'PKF Texas',
                       'text': 'Late statements, missed payments and general misreporting are red flags, '
                               'and trend analysis can locate the risky areas.',
                       'tip': 'Late statements, missed payments and general misreporting are red flags, '
                              'and trend analysis can locate the risky areas.',
                       'timestamp': 89,
                       'timestamp_seconds': 89,
                       'timestamp_label': '[00:01:29]',
                       'url': 'https://www.youtube.com/watch?v=Z-vXnFsa6zY&t=89s',
                       'markdown': '[00:01:29](https://www.youtube.com/watch?v=Z-vXnFsa6zY&t=89s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': '4ZKPBotNzQw',
                       'title': '22.5. What is a Royalty Audit',
                       'channel': 'Sabarwal Law',
                       'author': 'Sabarwal Law',
                       'text': 'A shortfall may simply mean the product is underperforming.',
                       'tip': 'A shortfall may simply mean the product is underperforming.',
                       'timestamp': 235,
                       'timestamp_seconds': 235,
                       'timestamp_label': '[00:03:55]',
                       'url': 'https://www.youtube.com/watch?v=4ZKPBotNzQw&t=235s',
                       'markdown': '[00:03:55](https://www.youtube.com/watch?v=4ZKPBotNzQw&t=235s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'DfuXhSrezTU',
                       'title': 'Your Right to AUDIT: How to Catch Your Label Stealing Your Royalties 🕵️',
                       'channel': 'Secrets of the music industry',
                       'author': 'Secrets of the music industry',
                       'text': 'Most contracts only give you a 2 or 3 year window to audit a statement, so '
                               "you can't wait around.",
                       'tip': 'Most contracts only give you a 2 or 3 year window to audit a statement, so '
                              "you can't wait around.",
                       'timestamp': 243,
                       'timestamp_seconds': 243,
                       'timestamp_label': '[00:04:03]',
                       'url': 'https://www.youtube.com/watch?v=DfuXhSrezTU&t=243s',
                       'markdown': '[00:04:03](https://www.youtube.com/watch?v=DfuXhSrezTU&t=243s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NrMiKZwGTD4',
                       'title': 'Understanding Your Royalty Statements and Learning What Questions to Ask '
                                'Your Publisher',
                       'channel': 'Authors Guild',
                       'author': 'Authors Guild',
                       'text': "Now, if there is 15% of inventory unaccounted for, there's a big problem.",
                       'tip': "Now, if there is 15% of inventory unaccounted for, there's a big problem.",
                       'timestamp': 1983,
                       'timestamp_seconds': 1983,
                       'timestamp_label': '[00:33:03]',
                       'url': 'https://www.youtube.com/watch?v=NrMiKZwGTD4&t=1983s',
                       'markdown': '[00:33:03](https://www.youtube.com/watch?v=NrMiKZwGTD4&t=1983s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'NrMiKZwGTD4',
                       'title': 'Understanding Your Royalty Statements and Learning What Questions to Ask '
                                'Your Publisher',
                       'channel': 'Authors Guild',
                       'author': 'Authors Guild',
                       'text': 'The other thing to look for, and this is something you should put in your '
                               'contract, is underpayment finding of 5% or greater, the publisher will '
                               'reimburse the author for the cost of an audit.',
                       'tip': 'The other thing to look for, and this is something you should put in your '
                              'contract, is underpayment finding of 5% or greater, the publisher will '
                              'reimburse the author for the cost of an audit.',
                       'timestamp': 3430,
                       'timestamp_seconds': 3430,
                       'timestamp_label': '[00:57:10]',
                       'url': 'https://www.youtube.com/watch?v=NrMiKZwGTD4&t=3430s',
                       'markdown': '[00:57:10](https://www.youtube.com/watch?v=NrMiKZwGTD4&t=3430s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'yAYeomyyeP8',
                       'title': 'How Book Advances and Royalties Work',
                       'channel': 'Alexa Donne',
                       'author': 'Alexa Donne',
                       'text': 'I can tell you up front most authors will never earn out.',
                       'tip': 'I can tell you up front most authors will never earn out.',
                       'timestamp': 224,
                       'timestamp_seconds': 224,
                       'timestamp_label': '[00:03:44]',
                       'url': 'https://www.youtube.com/watch?v=yAYeomyyeP8&t=224s',
                       'markdown': '[00:03:44](https://www.youtube.com/watch?v=yAYeomyyeP8&t=224s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'cEP_oNaMQcw',
                       'title': '💸 a guide to author finances // advances, royalties, taxes, & what worked '
                                'for me',
                       'channel': 'Lynn D. Jung',
                       'author': 'Lynn D. Jung',
                       'text': 'You have to sell 33,333 copies first before you start getting $3 per book.',
                       'tip': 'You have to sell 33,333 copies first before you start getting $3 per book.',
                       'timestamp': 496,
                       'timestamp_seconds': 496,
                       'timestamp_label': '[00:08:16]',
                       'url': 'https://www.youtube.com/watch?v=cEP_oNaMQcw&t=496s',
                       'markdown': '[00:08:16](https://www.youtube.com/watch?v=cEP_oNaMQcw&t=496s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'Xy0iIdZDIHk',
                       'title': 'Rights Royalty Statement Standards: The Details Make the Difference',
                       'channel': 'Book Industry Study Group',
                       'author': 'Book Industry Study Group',
                       'text': '77% reported that they have spent a full day or more on single statements.',
                       'tip': '77% reported that they have spent a full day or more on single statements.',
                       'timestamp': 546,
                       'timestamp_seconds': 546,
                       'timestamp_label': '[00:09:06]',
                       'url': 'https://www.youtube.com/watch?v=Xy0iIdZDIHk&t=546s',
                       'markdown': '[00:09:06](https://www.youtube.com/watch?v=Xy0iIdZDIHk&t=546s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'QHV5OSGnAMg',
                       'title': 'Understanding Contracts, Royalties, and Rights - Academic Publishing '
                                'Series',
                       'channel': 'Ideas on Fire',
                       'author': 'Ideas on Fire',
                       'text': "In the trade world, I think it's more common to probably base that on list "
                               'price.',
                       'tip': "In the trade world, I think it's more common to probably base that on list "
                              'price.',
                       'timestamp': 672,
                       'timestamp_seconds': 672,
                       'timestamp_label': '[00:11:12]',
                       'url': 'https://www.youtube.com/watch?v=QHV5OSGnAMg&t=672s',
                       'markdown': '[00:11:12](https://www.youtube.com/watch?v=QHV5OSGnAMg&t=672s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'k9Sb2smIIjM',
                       'title': 'Patent Licensing: Why You’re Losing Royalties (and How to Fix It)',
                       'channel': 'Bao Tran, Esq. | Patent Attorney',
                       'author': 'Bao Tran, Esq. | Patent Attorney',
                       'text': 'Three maintenance fees total $14,470, a late payment adds a $540 '
                               'surcharge, and a lapse evaporates the license.',
                       'tip': 'Three maintenance fees total $14,470, a late payment adds a $540 surcharge, '
                              'and a lapse evaporates the license.',
                       'timestamp': 168,
                       'timestamp_seconds': 168,
                       'timestamp_label': '[00:02:48]',
                       'url': 'https://www.youtube.com/watch?v=k9Sb2smIIjM&t=168s',
                       'markdown': '[00:02:48](https://www.youtube.com/watch?v=k9Sb2smIIjM&t=168s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'o0riJRlxTsY',
                       'title': 'AFAR Revenue 06: PFRS 15 Licensing – Right to Access vs. Right to Use; '
                                'Usage-Based Royalties',
                       'channel': 'Accountancy Students Hub',
                       'author': 'Accountancy Students Hub',
                       'text': 'You must wait until the actual sale or usage takes place to recognize that '
                               'revenue.',
                       'tip': 'You must wait until the actual sale or usage takes place to recognize that '
                              'revenue.',
                       'timestamp': 268,
                       'timestamp_seconds': 268,
                       'timestamp_label': '[00:04:28]',
                       'url': 'https://www.youtube.com/watch?v=o0riJRlxTsY&t=268s',
                       'markdown': '[00:04:28](https://www.youtube.com/watch?v=o0riJRlxTsY&t=268s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'},
                      {'source_type': 'video_pro_tip',
                       'video_id': 'eoUe3NebB3E',
                       'title': 'Episode 7 ASC 606 Licensing: Functional vs. Symbolic Intellectual '
                                'Property',
                       'channel': 'Jobank CPA',
                       'author': 'Jobank CPA',
                       'text': 'Because it is strictly point-in-time, that entire $300,000 is recognized '
                               'immediately in Q1.',
                       'tip': 'Because it is strictly point-in-time, that entire $300,000 is recognized '
                              'immediately in Q1.',
                       'timestamp': 414,
                       'timestamp_seconds': 414,
                       'timestamp_label': '[00:06:54]',
                       'url': 'https://www.youtube.com/watch?v=eoUe3NebB3E&t=414s',
                       'markdown': '[00:06:54](https://www.youtube.com/watch?v=eoUe3NebB3E&t=414s)',
                       'epistemic_status': 'attributed_practitioner_claim',
                       'relevance': 'Verbatim practitioner testimony from Chapter Q10.'}]}
